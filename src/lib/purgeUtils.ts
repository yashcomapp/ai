import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ChunkedBatch } from '@/lib/firebase/batch';

export interface PurgeResult {
  purgedAttemptsCount: number;
  purgedLiveSessionsCount: number;
  purgedParentLogsCount: number;
}

/**
 * Purges expired student exam webcam proctoring snapshots from examAttempts & liveExamSessions.
 * Queries ONLY candidate expired documents using where('proctoringSnapshotsExpiresAt', '<=', nowIso).
 * Deletes proctoringSnapshotsExpiresAt on purge so already-purged documents are never scanned again.
 * Snapshots are auto-purged at 12:00 AM IST on the same day.
 */
async function purgeExpiredProctoringSnapshots(): Promise<{ purgedAttemptsCount: number; purgedLiveSessionsCount: number }> {
  const nowIso = new Date().toISOString();
  let purgedAttemptsCount = 0;
  let purgedLiveSessionsCount = 0;

  // 1. Query ONLY candidate attempts whose snapshots have expired (bills zero reads for snapshot-less or already-purged docs)
  const attemptsSnap = await adminDb.collection('examAttempts')
    .where('proctoringSnapshotsExpiresAt', '<=', nowIso)
    .select('proctoringSnapshots')
    .get();

  const attemptBatch = new ChunkedBatch(adminDb);
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    const hasSnapshots = Array.isArray(d.proctoringSnapshots) && d.proctoringSnapshots.length > 0;

    attemptBatch.update(doc.ref, {
      proctoringSnapshots: [],
      proctoringSnapshotsExpiresAt: admin.firestore.FieldValue.delete(),
      proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    if (hasSnapshots) {
      purgedAttemptsCount++;
    }
  });
  await attemptBatch.commit();

  // 2. Query ONLY candidate live sessions whose snapshots have expired
  const liveSnap = await adminDb.collection('liveExamSessions')
    .where('proctoringSnapshotsExpiresAt', '<=', nowIso)
    .select('proctoringSnapshots')
    .get();

  const liveBatch = new ChunkedBatch(adminDb);
  liveSnap.docs.forEach(doc => {
    const d = doc.data();
    const hasSnapshots = Array.isArray(d.proctoringSnapshots) && d.proctoringSnapshots.length > 0;

    liveBatch.update(doc.ref, {
      proctoringSnapshots: [],
      proctoringSnapshotsExpiresAt: admin.firestore.FieldValue.delete(),
      proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    if (hasSnapshots) {
      purgedLiveSessionsCount++;
    }
  });
  await liveBatch.commit();

  return { purgedAttemptsCount, purgedLiveSessionsCount };
}

/**
 * Purges expired parent review verification camera photos older than 24 hours from parentSincerityLogs.
 * Retains audit log documents (duration, studentCode, parent reviewer) and only clears base64 photos.
 */
async function purgeExpiredParentSincerityLogs(): Promise<{ purgedParentLogsCount: number }> {
  const nowMs = Date.now();
  const oneDayAgo = nowMs - 24 * 60 * 60 * 1000;
  let purgedParentLogsCount = 0;

  // Query only unpurged logs using lightweight projection to avoid downloading image thumbnails
  const logsSnap = await adminDb.collection('parentSincerityLogs')
    .where('photoPurged', '==', false)
    .select('timestamp', 'createdAt', 'expiresAt')
    .get();

  const batch = new ChunkedBatch(adminDb);

  logsSnap.docs.forEach(doc => {
    const data = doc.data();

    const recordTime = data.timestamp || (data.createdAt?.toDate ? data.createdAt.toDate().toISOString() : data.createdAt) || null;
    const recordTimestampMs = recordTime ? new Date(recordTime).getTime() : 0;
    const isExpired = Boolean(data.expiresAt && data.expiresAt < nowMs) || (recordTimestampMs > 0 && recordTimestampMs < oneDayAgo);

    if (isExpired) {
      batch.update(doc.ref, {
        photoThumbnail: null,
        startPhotoThumbnail: null,
        photoPurged: true,
        photoPurgedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      purgedParentLogsCount++;
    }
  });

  await batch.commit();
  return { purgedParentLogsCount };
}

/**
 * Unified purge runner for both student exam proctoring snapshots and parent verification photos.
 */
export async function runCompleteAutomatedPurge(): Promise<PurgeResult> {
  const { purgedAttemptsCount, purgedLiveSessionsCount } = await purgeExpiredProctoringSnapshots();
  const { purgedParentLogsCount } = await purgeExpiredParentSincerityLogs();
  return { purgedAttemptsCount, purgedLiveSessionsCount, purgedParentLogsCount };
}
