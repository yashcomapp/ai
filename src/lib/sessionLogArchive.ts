import fs from 'fs';
import path from 'path';
import zlib from 'zlib';
import { adminDb } from '@/lib/firebase/admin';

export interface SessionArchiveResult {
  archivedCount: number;
  archiveFilePath: string | null;
  cutoffDate: string;
}

/**
 * Zips and archives session_logs older than retentionDays (default 30 days),
 * saves them as a compressed gzip JSON file in backups/session_logs/,
 * and then safely deletes the archived logs from the live Firestore collection.
 */
export async function archiveOldSessionLogs(retentionDays: number = 30): Promise<SessionArchiveResult> {
  const cutoffTime = Date.now() - (retentionDays * 24 * 60 * 60 * 1000);
  const cutoffDate = new Date(cutoffTime);
  const cutoffIso = cutoffDate.toISOString();

  // Query logs older than cutoff
  const oldLogsSnap = await adminDb.collection('session_logs')
    .where('timestamp', '<', cutoffDate)
    .get();

  if (oldLogsSnap.empty) {
    return {
      archivedCount: 0,
      archiveFilePath: null,
      cutoffDate: cutoffIso
    };
  }

  const logsData = oldLogsSnap.docs.map(doc => {
    const d = doc.data();
    let ts = d.timestamp;
    if (ts && typeof ts.toDate === 'function') {
      ts = ts.toDate().toISOString();
    }
    return {
      id: doc.id,
      ...d,
      timestamp: ts
    };
  });

  // Ensure backup directory exists
  const backupDir = path.join(process.cwd(), 'backups', 'session_logs');
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }

  const timestampStr = new Date().toISOString().replace(/[:.]/g, '-');
  const fileName = `session_logs_archive_${timestampStr}_count_${logsData.length}.json.gz`;
  const archivePath = path.join(backupDir, fileName);

  // Compress to gzip
  const jsonBuffer = Buffer.from(JSON.stringify(logsData, null, 2), 'utf-8');
  const compressed = zlib.gzipSync(jsonBuffer);
  fs.writeFileSync(archivePath, compressed);

  // Safely batch delete archived docs from Firestore
  const batchSize = 400;
  for (let i = 0; i < oldLogsSnap.docs.length; i += batchSize) {
    const chunk = oldLogsSnap.docs.slice(i, i + batchSize);
    const batch = adminDb.batch();
    chunk.forEach(doc => batch.delete(doc.ref));
    await batch.commit();
  }

  return {
    archivedCount: logsData.length,
    archiveFilePath: archivePath,
    cutoffDate: cutoffIso
  };
}
