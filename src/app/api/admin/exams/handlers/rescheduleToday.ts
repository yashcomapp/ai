import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ChunkedBatch } from '@/lib/firebase/batch';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const todayKey = getDateKeyIST(); // "2026-08-26"
    console.log(`[Reschedule] Running reschedule and attempt reset for date: ${todayKey}`);

    // Set new start time to 06:20 AM IST today
    const newStartAt = new Date(`${todayKey}T06:20:00+05:30`);
    const newEndAt = new Date(`${todayKey}T23:59:59+05:30`);

    const batch = new ChunkedBatch(adminDb);
    let assignmentsUpdated = 0;
    let attemptsReset = 0;
    const details: string[] = [];

    // 1. Update Objective Assignments (batchAssignments)
    const objAssignSnap = await adminDb.collection('batchAssignments').get();
    for (const doc of objAssignSnap.docs) {
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

    // 2. Update Subjective Assignments (subjectiveAssignments)
    const subjAssignSnap = await adminDb.collection('subjectiveAssignments').get();
    for (const doc of subjAssignSnap.docs) {
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

    // 3. Clear attempts for today in examAttempts, subjectiveAttempts, reviews, subjectiveReviews, liveExamSessions
    const [attemptsSnap, subjAttemptsSnap, reviewsSnap, subjReviewsSnap, liveSessionsSnap] = await Promise.all([
      adminDb.collection('examAttempts').get(),
      adminDb.collection('subjectiveAttempts').get(),
      adminDb.collection('reviews').get(),
      adminDb.collection('subjectiveReviews').get(),
      adminDb.collection('liveExamSessions').get()
    ]);

    // Check attempts from today
    attemptsSnap.docs.forEach(doc => {
      const data = doc.data();
      const d = data.submittedAt?.toDate ? data.submittedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null));
      if (d && getDateKeyIST(d) === todayKey) {
        batch.delete(doc.ref);
        attemptsReset++;
      }
    });

    subjAttemptsSnap.docs.forEach(doc => {
      const data = doc.data();
      const d = data.startedAt?.toDate ? data.startedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null));
      if (d && getDateKeyIST(d) === todayKey) {
        batch.delete(doc.ref);
        attemptsReset++;
      }
    });

    reviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const d = data.reviewedAt?.toDate ? data.reviewedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : null);
      if (d && getDateKeyIST(d) === todayKey) {
        batch.delete(doc.ref);
        attemptsReset++;
      }
    });

    subjReviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const d = data.submittedAt?.toDate ? data.submittedAt.toDate() : (data.createdAt?.toDate ? data.createdAt.toDate() : null);
      if (d && getDateKeyIST(d) === todayKey) {
        batch.delete(doc.ref);
        attemptsReset++;
      }
    });

    liveSessionsSnap.docs.forEach(doc => {
      batch.delete(doc.ref);
    });

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
