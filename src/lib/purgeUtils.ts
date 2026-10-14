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
 * Purges expired student exam webcam proctoring snapshots from examAttempts & liveExamSessions.
 * Uses lightweight projection (.select) to avoid downloading base64 snapshots into memory.
 * Snapshots are auto-purged at 12:00 AM IST on the same day.
 */
export async function purgeExpiredProctoringSnapshots(): Promise<{ purgedAttemptsCount: number; purgedLiveSessionsCount: number }> {
  const now = new Date();
  const todayKeyIST = getDateKeyIST(now);
  let purgedAttemptsCount = 0;
  let purgedLiveSessionsCount = 0;

  // 1. Purge from examAttempts using lightweight field projection (avoids pulling megabytes of base64 images)
  const attemptsSnap = await adminDb.collection('examAttempts')
    .select('completedAt', 'createdAt', 'startedAt', 'proctoringSnapshotsExpiresAt', 'proctoringSnapshotsPurgedAt')
    .get();

  const attemptBatch = new ChunkedBatch(adminDb);
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    // Skip if already purged
    if (d.proctoringSnapshotsPurgedAt) return;

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
  const liveSnap = await adminDb.collection('liveExamSessions')
    .select('lastActive', 'updatedAt', 'createdAt', 'proctoringSnapshotsExpiresAt', 'proctoringSnapshotsPurgedAt')
    .get();

  const liveBatch = new ChunkedBatch(adminDb);
  liveSnap.docs.forEach(doc => {
    const d = doc.data();
    if (d.proctoringSnapshotsPurgedAt) return;

    const rawLastActive = d.lastActive || d.updatedAt || d.createdAt;
    const lastActiveDate = rawLastActive?.toDate ? rawLastActive.toDate() : (rawLastActive ? new Date(rawLastActive) : null);
    const sessionDateKey = lastActiveDate ? getDateKeyIST(lastActiveDate) : null;
    const expiresAt = d.proctoringSnapshotsExpiresAt ? new Date(d.proctoringSnapshotsExpiresAt) : null;

    const isPastDay = sessionDateKey ? sessionDateKey < todayKeyIST : false;
    const isExpired = isPastDay || (expiresAt ? expiresAt.getTime() <= now.getTime() : false);

    if (isExpired) {
      liveBatch.update(doc.ref, {
        proctoringSnapshots: [],
        proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.serverTimestamp()
      });
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
export async function purgeExpiredParentSincerityLogs(): Promise<{ purgedParentLogsCount: number }> {
  const nowMs = Date.now();
  const oneDayAgo = nowMs - 24 * 60 * 60 * 1000;
  let purgedParentLogsCount = 0;

  // Lightweight projection to avoid downloading image thumbnails
  const logsSnap = await adminDb.collection('parentSincerityLogs')
    .select('timestamp', 'createdAt', 'expiresAt', 'photoPurged')
    .get();

  const batch = new ChunkedBatch(adminDb);

  logsSnap.docs.forEach(doc => {
    const data = doc.data();
    if (data.photoPurged) return; // Already stripped

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

let lastInProcessPurgeCheck = 0;

/**
 * Safe, lease-guarded daily purge runner.
 * Automatically runs once per day with a 15-minute lease to prevent parallel runs or cut-off executions.
 */
export async function triggerDailyPurgeIfNeeded(): Promise<boolean> {
  const now = Date.now();
  // Throttle in-memory check to at most once every 10 minutes to avoid redundant Firestore reads
  if (now - lastInProcessPurgeCheck < 10 * 60 * 1000) {
    return false;
  }
  lastInProcessPurgeCheck = now;

  try {
    const todayKey = getDateKeyIST(new Date());
    const ref = adminDb.collection('_systemMetadata').doc('dailyPurge');
    const doc = await ref.get().catch(() => null);
    const data = doc?.data();

    if (data?.lastPurgedDateKeyIST === todayKey && data?.status === 'completed') {
      return false; // Already completed today
    }

    if (data?.status === 'running') {
      const lastRunMs = data?.lastRunAt?.toDate ? data.lastRunAt.toDate().getTime() : (data?.lastRunAt ? new Date(data.lastRunAt).getTime() : 0);
      if (now - lastRunMs < 15 * 60 * 1000) {
        return false; // Active lease held within 15 minutes, skip concurrent run
      }
    }

    // Acquire lease
    await ref.set({
      lastPurgedDateKeyIST: todayKey,
      lastRunAt: admin.firestore.FieldValue.serverTimestamp(),
      status: 'running'
    }, { merge: true });

    try {
      const stats = await runCompleteAutomatedPurge();
      await ref.set({
        status: 'completed',
        lastCompletedAt: admin.firestore.FieldValue.serverTimestamp(),
        lastStats: stats
      }, { merge: true });
      return true;
    } catch (err: any) {
      await ref.set({
        status: 'failed',
        lastFailedAt: admin.firestore.FieldValue.serverTimestamp(),
        error: err.message
      }, { merge: true });
      return false;
    }
  } catch (err) {
    console.warn('[OpportunisticPurge] Failed to evaluate daily purge trigger:', err);
    return false;
  }
}
