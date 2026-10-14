import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { getDateKeyIST, getMidnightIST } from '@/lib/dateUtils';

export interface PurgeResult {
  purgedAttemptsCount: number;
  purgedLiveSessionsCount: number;
  purgedParentLogsCount: number;
}

/**
 * Purges expired student exam webcam proctoring snapshots from examAttempts & liveExamSessions
 * (Snapshots are auto-purged at 12:00 AM IST on the same day).
 */
export async function purgeExpiredProctoringSnapshots(): Promise<{ purgedAttemptsCount: number; purgedLiveSessionsCount: number }> {
  const now = new Date();
  const todayKeyIST = getDateKeyIST(now);
  let purgedAttemptsCount = 0;
  let purgedLiveSessionsCount = 0;

  // 1. Purge from examAttempts
  const attemptsSnap = await adminDb.collection('examAttempts').get();
  const attemptBatch = new ChunkedBatch(adminDb);
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    const hasSnapshots = Array.isArray(d.proctoringSnapshots) && d.proctoringSnapshots.length > 0;
    if (!hasSnapshots) return;

    const rawCompleted = d.completedAt || d.createdAt || d.startedAt;
    const completedDate = rawCompleted?.toDate ? rawCompleted.toDate() : (rawCompleted ? new Date(rawCompleted) : null);
    const attemptDateKey = completedDate ? getDateKeyIST(completedDate) : null;
    const expiresAt = d.proctoringSnapshotsExpiresAt ? new Date(d.proctoringSnapshotsExpiresAt) : null;

    const isPastDay = attemptDateKey ? attemptDateKey < todayKeyIST : false;
    const isExpired = isPastDay || (expiresAt ? expiresAt.getTime() <= now.getTime() : false) || (completedDate ? completedDate.getTime() < getMidnightIST(completedDate).getTime() && now.getTime() >= getMidnightIST(completedDate).getTime() : false);

    if (isExpired) {
      attemptBatch.update(doc.ref, {
        proctoringSnapshots: [],
        proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      purgedAttemptsCount++;
    }
  });
  await attemptBatch.commit();

  // 2. Purge from liveExamSessions older than current date / 12 AM
  const liveSnap = await adminDb.collection('liveExamSessions').get();
  const liveBatch = new ChunkedBatch(adminDb);
  liveSnap.docs.forEach(doc => {
    const d = doc.data();
    const hasSnapshots = Array.isArray(d.proctoringSnapshots) && d.proctoringSnapshots.length > 0;
    if (!hasSnapshots) return;

    const rawLastActive = d.lastActive || d.updatedAt || d.createdAt;
    const lastActiveDate = rawLastActive?.toDate ? rawLastActive.toDate() : (rawLastActive ? new Date(rawLastActive) : null);
    const sessionDateKey = lastActiveDate ? getDateKeyIST(lastActiveDate) : null;
    const expiresAt = d.proctoringSnapshotsExpiresAt ? new Date(d.proctoringSnapshotsExpiresAt) : null;

    const isPastDay = sessionDateKey ? sessionDateKey < todayKeyIST : false;
    const isExpired = isPastDay || (expiresAt ? expiresAt.getTime() <= now.getTime() : false);

    if (isExpired) {
      liveBatch.update(doc.ref, {
        proctoringSnapshots: []
      });
      purgedLiveSessionsCount++;
    }
  });
  await liveBatch.commit();

  return { purgedAttemptsCount, purgedLiveSessionsCount };
}

/**
 * Purges expired parent review verification camera photos older than 24 hours from parentSincerityLogs.
 */
export async function purgeExpiredParentSincerityLogs(): Promise<{ purgedParentLogsCount: number }> {
  const nowMs = Date.now();
  const oneDayAgo = nowMs - 24 * 60 * 60 * 1000;
  let purgedParentLogsCount = 0;

  const logsSnap = await adminDb.collection('parentSincerityLogs').get();
  const batch = new ChunkedBatch(adminDb);

  logsSnap.docs.forEach(doc => {
    const data = doc.data();
    const recordTime = data.timestamp || (data.createdAt?.toDate ? data.createdAt.toDate().toISOString() : data.createdAt) || null;
    const recordTimestampMs = recordTime ? new Date(recordTime).getTime() : 0;
    const isExpired = Boolean(data.expiresAt && data.expiresAt < nowMs) || (recordTimestampMs > 0 && recordTimestampMs < oneDayAgo);

    if (isExpired) {
      batch.delete(doc.ref);
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
