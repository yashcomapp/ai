import { adminDb } from '@/lib/firebase/admin';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { getDateKeyIST } from '@/lib/dateUtils';
import { runCompleteAutomatedPurge } from '@/lib/purgeUtils';
import { ExamReviewService } from '@/services/examReview.service';

export interface DailyMaintenanceResult {
  executed: boolean;
  reason?: string;
  dateIST: string;
  durationMs?: number;
  stats?: {
    purge?: any;
    expiredTargetsDeleted?: number;
    reschedule?: any;
    autonomousReviews?: any;
  };
}

/**
 * Executes the complete daily maintenance lifecycle once per calendar day in IST.
 * Utilizes a Firestore transaction on `config/systemMaintenance` to claim the day atomically.
 * Guarantees zero duplicate execution across multiple serverless cold-starts or warm instances.
 */
export async function runDailyMaintenanceOpportunistic(): Promise<DailyMaintenanceResult> {
  const todayStr = getDateKeyIST();
  const maintenanceRef = adminDb.collection('config').doc('systemMaintenance');

  // Step 1: Atomic transaction to claim the calendar day
  const claimResult = await adminDb.runTransaction(async (tx) => {
    const doc = await tx.get(maintenanceRef);
    const data = doc.data();

    // Already completed or currently active today
    if (data?.lastDailyRunIST === todayStr) {
      if (data.status === 'completed') {
        return { claimed: false, status: 'completed' };
      }
      // If running within last 15 mins, wait for it
      if (data.status === 'running') {
        const claimedAt = data.claimedAt ? new Date(data.claimedAt).getTime() : 0;
        if (Date.now() - claimedAt < 15 * 60 * 1000) {
          return { claimed: false, status: 'running' };
        }
      }
      // If failed or stale running lock (>15m), allow retry
    }

    tx.set(maintenanceRef, {
      lastDailyRunIST: todayStr,
      status: 'running',
      claimedAt: new Date().toISOString()
    }, { merge: true });

    return { claimed: true };
  });

  if (!claimResult.claimed) {
    return {
      executed: false,
      reason: `Maintenance for ${todayStr} already claimed/executed (status: ${claimResult.status})`,
      dateIST: todayStr
    };
  }

  const startTime = Date.now();
  console.log(`[Daily Maintenance] Claimed daily maintenance run for ${todayStr}. Executing pillars...`);

  const stats: DailyMaintenanceResult['stats'] = {};

  try {
    // 1. Automated Purge of expired proctoring snapshots & parent photo verification
    try {
      stats.purge = await runCompleteAutomatedPurge();
    } catch (err: any) {
      console.error('[Daily Maintenance] Purge error:', err);
      stats.purge = { error: err.message };
    }

    // 2. Targeted cleanup of expired liveClassTargets using indexed expiresAt <= now query
    try {
      const now = new Date();
      const expiredTargetsSnap = await adminDb.collection('liveClassTargets')
        .where('expiresAt', '<=', now)
        .get();

      const targetBatch = new ChunkedBatch(adminDb);
      expiredTargetsSnap.docs.forEach(d => targetBatch.delete(d.ref));
      if (expiredTargetsSnap.size > 0) {
        await targetBatch.commit();
      }
      stats.expiredTargetsDeleted = expiredTargetsSnap.size;
    } catch (err: any) {
      console.error('[Daily Maintenance] Target cleanup error:', err);
      stats.expiredTargetsDeleted = 0;
    }


    // 4. Sweep autonomous exam reviews (evaluates parent reviews past review deadline)
    try {
      stats.autonomousReviews = await ExamReviewService.sweepAutonomousReviews();
    } catch (err: any) {
      console.error('[Daily Maintenance] Autonomous review sweep error:', err);
      stats.autonomousReviews = { error: err.message };
    }

    const durationMs = Date.now() - startTime;

    // Record completion in config/systemMaintenance
    await maintenanceRef.set({
      lastDailyRunIST: todayStr,
      status: 'completed',
      completedAt: new Date().toISOString(),
      durationMs,
      stats
    }, { merge: true });

    console.log(`[Daily Maintenance] Completed daily maintenance in ${durationMs}ms:`, stats);

    return {
      executed: true,
      dateIST: todayStr,
      durationMs,
      stats
    };
  } catch (error: any) {
    console.error('[Daily Maintenance] Unexpected failure during maintenance run:', error);
    await maintenanceRef.set({
      lastDailyRunIST: todayStr,
      status: 'failed',
      failedAt: new Date().toISOString(),
      error: error.message
    }, { merge: true });

    throw error;
  }
}
