import * as fs from 'fs';
import * as path from 'path';
import { adminDb } from '@/lib/firebase/admin';

export interface SnapshotMetadata {
  snapshotId: string;
  timestamp: string;
  reason: string;
  collections: { [collectionName: string]: number };
  snapshotFilePath: string;
}

export async function createPreMutationSnapshot(
  collections: string[],
  reason: string
): Promise<SnapshotMetadata> {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}`;
  const snapshotsDir = path.resolve(process.cwd(), 'backups', 'snapshots');

  if (!fs.existsSync(snapshotsDir)) {
    fs.mkdirSync(snapshotsDir, { recursive: true });
  }

  const snapshotData: { [collectionName: string]: any[] } = {};
  const collectionCounts: { [collectionName: string]: number } = {};

  for (const colName of collections) {
    const snap = await adminDb.collection(colName).get();
    const docs = snap.docs.map(doc => ({ _docId: doc.id, ...doc.data() }));
    snapshotData[colName] = docs;
    collectionCounts[colName] = docs.length;
  }

  const snapshotFileName = `${snapshotId}.json`;
  const snapshotFilePath = path.join(snapshotsDir, snapshotFileName);
  fs.writeFileSync(snapshotFilePath, JSON.stringify(snapshotData, null, 2), 'utf8');

  const metadata: SnapshotMetadata = {
    snapshotId,
    timestamp: new Date().toISOString(),
    reason,
    collections: collectionCounts,
    snapshotFilePath
  };

  try {
    await adminDb.collection('_systemBackups').doc(snapshotId).set(metadata);
  } catch (err) {
    console.warn('Could not write snapshot record to _systemBackups:', err);
  }

  return metadata;
}

export async function restoreSnapshot(snapshotFileNameOrId: string): Promise<boolean> {
  const snapshotsDir = path.resolve(process.cwd(), 'backups', 'snapshots');
  let filePath = path.join(snapshotsDir, snapshotFileNameOrId);
  if (!filePath.endsWith('.json')) filePath += '.json';

  if (!fs.existsSync(filePath)) {
    throw new Error(`Snapshot file not found: ${filePath}`);
  }

  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  for (const [colName, docs] of Object.entries<any[]>(data)) {
    console.log(`Restoring collection ${colName} (${docs.length} documents)...`);
    const batchSize = 400;
    for (let i = 0; i < docs.length; i += batchSize) {
      const chunk = docs.slice(i, i + batchSize);
      const batch = adminDb.batch();
      chunk.forEach(docData => {
        const docId = docData._docId;
        const cleanData = { ...docData };
        delete cleanData._docId;
        const ref = adminDb.collection(colName).doc(docId);
        batch.set(ref, cleanData);
      });
      await batch.commit();
    }
  }

  return true;
}
