import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  return POST(req);
}

export async function POST(req: NextRequest) {
  try {
    // 1. Verify Authorization: Admin role or valid CRON_SECRET
    const authHeader = req.headers.get('authorization') || req.headers.get('Authorization');
    const cronSecret = process.env.CRON_SECRET;
    const isCronAuthorized = Boolean(cronSecret && authHeader === `Bearer ${cronSecret}`);

    if (!isCronAuthorized) {
      const admin = await verifyRole(req, 'admin');
      if (!admin) {
        return NextResponse.json({ message: 'Unauthorized. Admin role or valid Cron Secret required.' }, { status: 401 });
      }
    }

    const todayKey = getDateKeyIST(); // "YYYY-MM-DD"
    console.log(`[Reschedule] Running reschedule and attempt reset for date: ${todayKey}`);

    const startOfTodayIST = new Date(`${todayKey}T00:00:00+05:30`);
    const startOfTomorrowIST = new Date(startOfTodayIST.getTime() + 24 * 60 * 60 * 1000);

    // Set new start time to 06:20 AM IST today
    const newStartAt = new Date(`${todayKey}T06:20:00+05:30`);
    const newEndAt = new Date(`${todayKey}T23:59:59+05:30`);

    const batch = new ChunkedBatch(adminDb);
    let assignmentsUpdated = 0;
    let attemptsReset = 0;
    const details: string[] = [];

    // 1. Update Objective Assignments (batchAssignments) for today / active
    const [
      objActiveSnap,
      objStartSnap,
      objCreatedSnap,
      subjActiveSnap,
      subjStartSnap,
      subjCreatedSnap
    ] = await Promise.all([
      adminDb.collection('batchAssignments').where('status', '==', 'active').get(),
      adminDb.collection('batchAssignments').where('startAt', '>=', startOfTodayIST).where('startAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('batchAssignments').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAssignments').where('status', '==', 'active').get(),
      adminDb.collection('subjectiveAssignments').where('startAt', '>=', startOfTodayIST).where('startAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAssignments').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any))
    ]);

    const seenObjDocIds = new Set<string>();
    for (const snap of [objActiveSnap, objStartSnap, objCreatedSnap]) {
      for (const doc of snap.docs) {
        if (seenObjDocIds.has(doc.id)) continue;
        seenObjDocIds.add(doc.id);

        const data = doc.data();
        const startAtDate = data.startAt?.toDate ? data.startAt.toDate() : (data.startAt ? new Date(data.startAt) : null);
        const createdAtDate = data.createdAt?.toDate ? data.createdAt.toDate() : (data.createdAt ? new Date(data.createdAt) : null);

        const isToday = (startAtDate && getDateKeyIST(startAtDate) === todayKey) || 
                        (createdAtDate && getDateKeyIST(createdAtDate) === todayKey) ||
                        data.status === 'active';

        if (isToday) {
          batch.set(doc.ref, {
            startAt: newStartAt,
            endAt: newEndAt,
            lateEntryRestriction: false,
            status: 'active'
          }, { merge: true });
          assignmentsUpdated++;
          details.push(`Updated Objective Assignment [${doc.id}] for exam [${data.examId}]`);
        }
      }
    }

    // 2. Update Subjective Assignments (subjectiveAssignments) for today / active
    const seenSubjDocIds = new Set<string>();
    for (const snap of [subjActiveSnap, subjStartSnap, subjCreatedSnap]) {
      for (const doc of snap.docs) {
        if (seenSubjDocIds.has(doc.id)) continue;
        seenSubjDocIds.add(doc.id);

        const data = doc.data();
        const startAtDate = data.startAt?.toDate ? data.startAt.toDate() : (data.startAt ? new Date(data.startAt) : null);
        const createdAtDate = data.createdAt?.toDate ? data.createdAt.toDate() : (data.createdAt ? new Date(data.createdAt) : null);

        const isToday = (startAtDate && getDateKeyIST(startAtDate) === todayKey) || 
                        (createdAtDate && getDateKeyIST(createdAtDate) === todayKey) ||
                        data.status === 'active';

        if (isToday) {
          batch.set(doc.ref, {
            startAt: newStartAt,
            endAt: newEndAt,
            lateEntryRestriction: false,
            status: 'active'
          }, { merge: true });
          assignmentsUpdated++;
          details.push(`Updated Subjective Assignment [${doc.id}] for exam [${data.examId}]`);
        }
      }
    }

    // 3. Clear attempts for today in examAttempts, subjectiveAttempts, reviews, subjectiveReviews, liveExamSessions
    // Queries are window-targeted to today to eliminate collection-wide full historical scans
    const [
      // examAttempts
      attCreatedSnap,
      attStartedSnap,
      attSubmittedSnap,
      attCompletedSnap,
      attDateKeySnap,
      attDateSnap,

      // subjectiveAttempts
      subCreatedSnap,
      subStartedSnap,
      subSubmittedSnap,
      subCompletedSnap,
      subDateKeySnap,
      subDateSnap,

      // reviews
      revCreatedSnap,
      revReviewedSnap,
      revTimestampSnap,
      revCompletedSnap,
      revDateKeySnap,
      revDateSnap,

      // subjectiveReviews
      subRevCreatedSnap,
      subRevSubmittedSnap,
      subRevTimestampSnap,
      subRevDateKeySnap,

      // liveExamSessions
      liveCreatedSnap,
      liveActiveSnap,
      liveDateKeySnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('examAttempts').where('startedAt', '>=', startOfTodayIST).where('startedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('examAttempts').where('submittedAt', '>=', startOfTodayIST).where('submittedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('examAttempts').where('completedAt', '>=', startOfTodayIST).where('completedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('examAttempts').where('dateKey', '==', todayKey).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('examAttempts').where('date', '==', todayKey).get().catch(() => ({ docs: [] } as any)),

      adminDb.collection('subjectiveAttempts').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAttempts').where('startedAt', '>=', startOfTodayIST).where('startedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAttempts').where('submittedAt', '>=', startOfTodayIST).where('submittedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAttempts').where('completedAt', '>=', startOfTodayIST).where('completedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAttempts').where('dateKey', '==', todayKey).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveAttempts').where('date', '==', todayKey).get().catch(() => ({ docs: [] } as any)),

      adminDb.collection('reviews').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('reviews').where('reviewedAt', '>=', startOfTodayIST).where('reviewedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('reviews').where('timestamp', '>=', startOfTodayIST).where('timestamp', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('reviews').where('completedAt', '>=', startOfTodayIST).where('completedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('reviews').where('dateKey', '==', todayKey).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('reviews').where('date', '==', todayKey).get().catch(() => ({ docs: [] } as any)),

      adminDb.collection('subjectiveReviews').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveReviews').where('submittedAt', '>=', startOfTodayIST).where('submittedAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveReviews').where('timestamp', '>=', startOfTodayIST).where('timestamp', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('subjectiveReviews').where('dateKey', '==', todayKey).get().catch(() => ({ docs: [] } as any)),

      adminDb.collection('liveExamSessions').where('createdAt', '>=', startOfTodayIST).where('createdAt', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('liveExamSessions').where('lastActive', '>=', startOfTodayIST).where('lastActive', '<', startOfTomorrowIST).get().catch(() => ({ docs: [] } as any)),
      adminDb.collection('liveExamSessions').where('dateKey', '==', todayKey).get().catch(() => ({ docs: [] } as any))
    ]);

    // Check & delete attempts from today
    const seenAttemptDocIds = new Set<string>();
    for (const snap of [attCreatedSnap, attStartedSnap, attSubmittedSnap, attCompletedSnap, attDateKeySnap, attDateSnap]) {
      for (const doc of snap.docs) {
        if (seenAttemptDocIds.has(doc.id)) continue;
        seenAttemptDocIds.add(doc.id);

        const data = doc.data();
        const d = data.submittedAt?.toDate ? data.submittedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.startedAt?.toDate ? data.startedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null)));
        if ((d && getDateKeyIST(d) === todayKey) || data.dateKey === todayKey || data.date === todayKey) {
          batch.delete(doc.ref);
          attemptsReset++;
        }
      }
    }

    const seenSubjAttemptDocIds = new Set<string>();
    for (const snap of [subCreatedSnap, subStartedSnap, subSubmittedSnap, subCompletedSnap, subDateKeySnap, subDateSnap]) {
      for (const doc of snap.docs) {
        if (seenSubjAttemptDocIds.has(doc.id)) continue;
        seenSubjAttemptDocIds.add(doc.id);

        const data = doc.data();
        const d = data.startedAt?.toDate ? data.startedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.submittedAt?.toDate ? data.submittedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null)));
        if ((d && getDateKeyIST(d) === todayKey) || data.dateKey === todayKey || data.date === todayKey) {
          batch.delete(doc.ref);
          attemptsReset++;
        }
      }
    }

    const seenReviewDocIds = new Set<string>();
    for (const snap of [revCreatedSnap, revReviewedSnap, revTimestampSnap, revCompletedSnap, revDateKeySnap, revDateSnap]) {
      for (const doc of snap.docs) {
        if (seenReviewDocIds.has(doc.id)) continue;
        seenReviewDocIds.add(doc.id);

        const data = doc.data();
        const d = data.reviewedAt?.toDate ? data.reviewedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.timestamp?.toDate ? data.timestamp.toDate() : (data.timestamp ? new Date(data.timestamp) : null)));
        if ((d && getDateKeyIST(d) === todayKey) || data.dateKey === todayKey || data.date === todayKey) {
          batch.delete(doc.ref);
          attemptsReset++;
        }
      }
    }

    const seenSubjRevDocIds = new Set<string>();
    for (const snap of [subRevCreatedSnap, subRevSubmittedSnap, subRevTimestampSnap, subRevDateKeySnap]) {
      for (const doc of snap.docs) {
        if (seenSubjRevDocIds.has(doc.id)) continue;
        seenSubjRevDocIds.add(doc.id);

        const data = doc.data();
        const d = data.submittedAt?.toDate ? data.submittedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.timestamp?.toDate ? data.timestamp.toDate() : (data.timestamp ? new Date(data.timestamp) : null)));
        if ((d && getDateKeyIST(d) === todayKey) || data.dateKey === todayKey) {
          batch.delete(doc.ref);
          attemptsReset++;
        }
      }
    }

    const seenLiveDocIds = new Set<string>();
    for (const snap of [liveCreatedSnap, liveActiveSnap, liveDateKeySnap]) {
      for (const doc of snap.docs) {
        if (seenLiveDocIds.has(doc.id)) continue;
        seenLiveDocIds.add(doc.id);
        batch.delete(doc.ref);
      }
    }

    await batch.commit();

    return NextResponse.json({
      success: true,
      message: 'All exams for today successfully rescheduled to 06:20 AM with no late entry restrictions, and attempts reset.',
      assignmentsUpdated,
      attemptsReset,
      details
    });

  } catch (error: any) {
    console.error('Reschedule error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
