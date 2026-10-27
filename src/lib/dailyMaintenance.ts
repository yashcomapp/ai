import { adminDb } from '@/lib/firebase/admin';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { getDateKeyIST } from '@/lib/dateUtils';
import { runCompleteAutomatedPurge } from '@/lib/purgeUtils';
import { ExamReviewService } from '@/services/examReview.service';
import { executeRescheduleToday } from '@/app/api/admin/exams/handlers/rescheduleToday';

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

    // Already completed or claimed today
    if (data?.lastDailyRunIST === todayStr) {
      return { claimed: false, status: data.status || 'completed' };
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

    // 3. Reschedule active exams for today (06:20 AM start window with zero late entry restrictions)
    try {
      stats.reschedule = await executeRescheduleToday(todayStr);
    } catch (err: any) {
      console.error('[Daily Maintenance] Reschedule error:', err);
      stats.reschedule = { error: err.message };
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
