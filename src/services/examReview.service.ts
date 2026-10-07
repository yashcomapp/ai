import { adminDb } from '@/lib/firebase/admin';
import { parseDateInput, getDateKeyIST } from '@/lib/dateUtils';
import { invalidateCache } from '@/lib/firebase/cache';

export interface ExamReviewStatus {
  hasAttempt: boolean;
  examId: string;
  studentCode: string;
  completedAt: string | null;
  elapsedMinutes: number;
  remainingMinutes: number;
  isWithin60MinWindow: boolean;
  status: 'pending' | 'on_time' | 'late';
  reviewedAt?: string | null;
  timeSpentSeconds?: number;
  reviewedQuestionCount?: number;
  disputeCount?: number;
  bountyEarnedCount?: number;
}

export interface QuestionDisputeInput {
  questionId: string;
  questionCode: string;
  reason: 'wrong_key' | 'typo' | 'no_correct_option' | 'math_error' | 'ambiguous';
  suggestedAnswer?: string;
  notes?: string;
  questionText?: string;
}

export class ExamReviewService {
  /**
   * Checks the review timing and status for a student's exam attempt
   */
  static async getReviewStatus(studentCode: string, examId: string): Promise<ExamReviewStatus> {
    const sCodeUpper = studentCode.trim().toUpperCase();
    let canonicalExamId = examId.trim();
    if (sCodeUpper && canonicalExamId.toUpperCase().endsWith(`_${sCodeUpper}`)) {
      canonicalExamId = canonicalExamId.slice(0, canonicalExamId.length - (sCodeUpper.length + 1));
    }
    
    // 1. Fetch official exam review doc if submitted across all candidate doc IDs
    let reviewData: any = null;
    const candidateDocIds = Array.from(new Set([
      `${canonicalExamId}_${sCodeUpper}`,
      `${canonicalExamId}_${studentCode}`,
      `${examId}_${sCodeUpper}`,
      `${examId}_${studentCode}`,
      `${sCodeUpper}_${canonicalExamId}`,
      `${sCodeUpper}_${examId}`,
      canonicalExamId,
      examId
    ].filter(Boolean)));

    const reviewRefs = candidateDocIds.map(id => adminDb.collection('reviews').doc(id));
    const rSnaps = await adminDb.getAll(...reviewRefs).catch(() => []);
    for (const snap of rSnaps) {
      if (snap && snap.exists) {
        reviewData = snap.data();
        break;
      }
    }

    if (!reviewData) {
      // Fallback query in reviews
      const candidateExamIds = Array.from(new Set([canonicalExamId, examId].filter(Boolean)));
      const qSnap = await adminDb.collection('reviews')
        .where('studentCode', 'in', [sCodeUpper, studentCode])
        .where('examId', 'in', candidateExamIds)
        .limit(1)
        .get()
        .catch(() => ({ empty: true, docs: [] } as any));
      if (!qSnap.empty) reviewData = qSnap.docs[0].data();
    }

    // Fallback query in examAttempts if review not found
    if (!reviewData) {
      const attemptRefs = candidateDocIds.map(id => adminDb.collection('examAttempts').doc(id));
      const aSnaps = await adminDb.getAll(...attemptRefs).catch(() => []);
      for (const snap of aSnaps) {
        if (snap && snap.exists) {
          reviewData = snap.data();
          break;
        }
      }

      if (!reviewData) {
        const candidateExamIds = Array.from(new Set([canonicalExamId, examId].filter(Boolean)));
        const attemptSnapQuery = await adminDb.collection('examAttempts')
          .where('studentCode', 'in', [sCodeUpper, studentCode])
          .where('examId', 'in', candidateExamIds)
          .limit(1)
          .get()
          .catch(() => ({ empty: true, docs: [] } as any));
        if (!attemptSnapQuery.empty) {
          reviewData = attemptSnapQuery.docs[0].data();
        }
      }
    }

    const completedDate = parseDateInput(reviewData?.completedAt || reviewData?.submittedAt || reviewData?.createdAt || new Date());

    const now = new Date();
    const elapsedMinutes = completedDate ? Math.max(0, Math.floor((now.getTime() - completedDate.getTime()) / 60000)) : 0;
    const remainingMinutes = Math.max(0, 60 - elapsedMinutes);
    const isWithin60MinWindow = elapsedMinutes <= 60;

    // 2. Fetch verified examReview submission
    let examReviewDoc = await adminDb.collection('examReviews').doc(`${sCodeUpper}_${canonicalExamId}`).get().catch(() => ({ exists: false, data: () => null } as any));
    if (!examReviewDoc.exists && examId !== canonicalExamId) {
      const altDoc = await adminDb.collection('examReviews').doc(`${sCodeUpper}_${examId}`).get().catch(() => ({ exists: false, data: () => null } as any));
      if (altDoc.exists) examReviewDoc = altDoc;
    }
    const examReviewData = examReviewDoc.exists ? examReviewDoc.data() : null;

    let status: 'pending' | 'on_time' | 'late' = 'pending';
    if (examReviewData) {
      status = examReviewData.status || (examReviewData.elapsedMinutesAtSubmission <= 60 ? 'on_time' : 'late');
    }

    return {
      hasAttempt: !!reviewData || !!examReviewData,
      examId: canonicalExamId,
      studentCode: sCodeUpper,
      completedAt: completedDate ? completedDate.toISOString() : null,
      elapsedMinutes,
      remainingMinutes,
      isWithin60MinWindow,
      status,
      reviewedAt: examReviewData?.submittedAt || null,
      timeSpentSeconds: examReviewData?.timeSpentSeconds || 0,
      reviewedQuestionCount: examReviewData?.reviewedQuestionIds?.length || 0,
      disputeCount: examReviewData?.disputeCount || 0,
      bountyEarnedCount: examReviewData?.bountyEarnedCount || 0
    };
  }

  /**
   * Submits a completed post-exam verification review with question challenges
   */
  static async submitReview(params: {
    studentCode: string;
    studentName?: string;
    examId: string;
    examName?: string;
    batchId?: string;
    reviewedQuestionIds?: string[];
    wrongAnswerReasons?: Record<string | number, string>;
    challenges?: QuestionDisputeInput[];
    timeSpentSeconds?: number;
  }): Promise<{
    success: boolean;
    status: 'on_time' | 'late';
    remainingMinutes: number;
    bountiesAwarded: number;
    message: string;
  }> {
    const {
      studentCode,
      studentName = 'Student',
      examId,
      examName = 'Official Exam',
      batchId = '',
      reviewedQuestionIds = [],
      wrongAnswerReasons,
      challenges = [],
      timeSpentSeconds = 0
    } = params;

    const sCodeUpper = studentCode.trim().toUpperCase();
    let canonicalExamId = examId.trim();
    if (sCodeUpper && canonicalExamId.toUpperCase().endsWith(`_${sCodeUpper}`)) {
      canonicalExamId = canonicalExamId.slice(0, canonicalExamId.length - (sCodeUpper.length + 1));
    }
    const now = new Date();

    // Check attempt completion timestamp
    const reviewStatus = await this.getReviewStatus(sCodeUpper, canonicalExamId);

    const isWithin60Min = reviewStatus.isWithin60MinWindow;
    const reviewStatusValue = isWithin60Min ? 'on_time' : 'late';

    // Save master examReview record
    const examReviewRef = adminDb.collection('examReviews').doc(`${sCodeUpper}_${canonicalExamId}`);
    await examReviewRef.set({
      id: `${sCodeUpper}_${canonicalExamId}`,
      studentCode: sCodeUpper,
      studentName: studentName || 'Student',
      batchId: batchId || '',
      examId: canonicalExamId,
      examName: examName || 'Official Exam',
      reviewedQuestionIds: reviewedQuestionIds || [],
      timeSpentSeconds: timeSpentSeconds || 0,
      elapsedMinutesAtSubmission: reviewStatus.elapsedMinutes || 0,
      status: reviewStatusValue,
      submittedAt: now.toISOString()
    }, { merge: true });

    // Also update reviews and examAttempts collections status to unlock pending student reviews
    try {
      const userSnap = await adminDb.collection('users').where('studentCode', '==', sCodeUpper).where('role', '==', 'student').limit(1).get().catch(() => null);
      const isAutonomous = userSnap && !userSnap.empty && userSnap.docs[0].data()?.autonomous === true;
      const targetStatus = isAutonomous ? 'approved' : 'pending';

      const candidateDocIds = Array.from(new Set([
        `${canonicalExamId}_${studentCode}`,
        `${canonicalExamId}_${sCodeUpper}`,
        `${examId}_${studentCode}`,
        `${examId}_${sCodeUpper}`,
        canonicalExamId,
        examId
      ].filter(Boolean)));

      const updatePayload: Record<string, any> = {
        status: targetStatus,
        studentReviewedAt: now,
        updatedAt: now
      };
      if (wrongAnswerReasons && Object.keys(wrongAnswerReasons).length > 0) {
        updatePayload.wrongAnswerReasons = wrongAnswerReasons;
      }

      const reviewRefs = candidateDocIds.map(id => adminDb.collection('reviews').doc(id));
      const rSnaps = await adminDb.getAll(...reviewRefs).catch(() => []);
      for (const snap of rSnaps) {
        if (snap && snap.exists) {
          const currentRevStatus = snap.data()?.status;
          if (currentRevStatus === 'student_review' || isAutonomous || wrongAnswerReasons) {
            await snap.ref.update(updatePayload).catch(() => null);
          }
        }
      }

      const attemptRefs = candidateDocIds.map(id => adminDb.collection('examAttempts').doc(id));
      const aSnaps = await adminDb.getAll(...attemptRefs).catch(() => []);
      for (const snap of aSnaps) {
        if (snap && snap.exists) {
          await snap.ref.update(updatePayload).catch(() => null);
        }
      }
    } catch (revErr) {
      console.warn('Could not sync status to reviews doc:', revErr);
    }

    // Invalidate caches
    try {
      invalidateCache(studentCode);
      invalidateCache(sCodeUpper);
      invalidateCache(`student_results_${studentCode}`);
      invalidateCache(`student_results_${sCodeUpper}`);
      invalidateCache(`parent_reviews_${studentCode}`);
      invalidateCache(`parent_reviews_${sCodeUpper}`);
    } catch {}

    return {
      success: true,
      status: reviewStatusValue,
      remainingMinutes: reviewStatus.remainingMinutes,
      bountiesAwarded: 0,
      message: isWithin60Min
        ? `✅ Review verified on-time within the 60-minute window!`
        : `⚠️ Review submitted after the 60-minute window (${reviewStatus.elapsedMinutes}m elapsed). Recorded as Late Review.`
    };
  }

  /**
   * Sweeps and auto-approves pending reviews, exam attempts, parentReviews, and evaluations
   * for all autonomous students (or a specific student if studentCode is supplied).
   */
  static async sweepAutonomousReviews(targetStudentCode?: string) {
    let studentCodes: string[] = [];
    if (targetStudentCode) {
      studentCodes = [targetStudentCode.trim().toUpperCase()];
    } else {
      const autoStudentsSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('autonomous', '==', true)
        .get();
      studentCodes = Array.from(new Set(
        autoStudentsSnap.docs
          .map(d => (d.data().studentCode || '').trim().toUpperCase())
          .filter(Boolean)
      ));
    }

    if (studentCodes.length === 0) {
      return {
        success: true,
        studentsScanned: 0,
        reviewsApproved: 0,
        attemptsApproved: 0,
        parentReviewsApproved: 0,
        evaluationsApproved: 0,
        message: 'No autonomous students found to sweep.'
      };
    }

    let reviewsApproved = 0;
    let attemptsApproved = 0;
    let parentReviewsApproved = 0;
    let evaluationsApproved = 0;

    // Process in chunks of 30 for Firestore 'in' queries
    const chunks: string[][] = [];
    for (let i = 0; i < studentCodes.length; i += 30) {
      chunks.push(studentCodes.slice(i, i + 30));
    }

    const now = new Date();

    for (const chunk of chunks) {
      // 1. Sweep 'reviews' collection
      const pendingReviewsSnap = await adminDb.collection('reviews')
        .where('studentCode', 'in', chunk)
        .where('status', 'in', ['pending', 'student_review'])
        .get()
        .catch(() => ({ docs: [] } as any));

      if (pendingReviewsSnap.docs && pendingReviewsSnap.docs.length > 0) {
        let batch = adminDb.batch();
        let bCount = 0;
        for (const doc of pendingReviewsSnap.docs) {
          batch.update(doc.ref, {
            status: 'approved',
            autoApprovedAutonomous: true,
            updatedAt: now
          });
          bCount++;
          reviewsApproved++;
          if (bCount === 400) {
            await batch.commit();
            batch = adminDb.batch();
            bCount = 0;
          }
        }
        if (bCount > 0) {
          await batch.commit();
        }
      }

      // 2. Sweep 'examAttempts' collection
      const pendingAttemptsSnap = await adminDb.collection('examAttempts')
        .where('studentCode', 'in', chunk)
        .where('status', 'in', ['pending', 'student_review'])
        .get()
        .catch(() => ({ docs: [] } as any));

      if (pendingAttemptsSnap.docs && pendingAttemptsSnap.docs.length > 0) {
        let batch = adminDb.batch();
        let bCount = 0;
        for (const doc of pendingAttemptsSnap.docs) {
          batch.update(doc.ref, {
            status: 'approved',
            autoApprovedAutonomous: true,
            updatedAt: now
          });
          bCount++;
          attemptsApproved++;
          if (bCount === 400) {
            await batch.commit();
            batch = adminDb.batch();
            bCount = 0;
          }
        }
        if (bCount > 0) {
          await batch.commit();
        }
      }

      // 3. Sweep 'parentReviews' collection
      const pendingParentReviewsSnap = await adminDb.collection('parentReviews')
        .where('studentCode', 'in', chunk)
        .where('status', '==', 'pending')
        .get()
        .catch(() => ({ docs: [] } as any));

      if (pendingParentReviewsSnap.docs && pendingParentReviewsSnap.docs.length > 0) {
        let batch = adminDb.batch();
        let bCount = 0;
        for (const doc of pendingParentReviewsSnap.docs) {
          batch.update(doc.ref, {
            status: 'approved',
            autoApprovedAutonomous: true,
            updatedAt: now
          });
          bCount++;
          parentReviewsApproved++;
          if (bCount === 400) {
            await batch.commit();
            batch = adminDb.batch();
            bCount = 0;
          }
        }
        if (bCount > 0) {
          await batch.commit();
        }
      }

      // 4. Sweep 'evaluations' collection
      const pendingEvalsSnap = await adminDb.collection('evaluations')
        .where('studentCode', 'in', chunk)
        .where('status', 'in', ['pending', 'pending_parent'])
        .get()
        .catch(() => ({ docs: [] } as any));

      if (pendingEvalsSnap.docs && pendingEvalsSnap.docs.length > 0) {
        let batch = adminDb.batch();
        let bCount = 0;
        for (const doc of pendingEvalsSnap.docs) {
          batch.update(doc.ref, {
            status: 'approved',
            autoApprovedAutonomous: true,
            updatedAt: now
          });
          bCount++;
          evaluationsApproved++;
          if (bCount === 400) {
            await batch.commit();
            batch = adminDb.batch();
            bCount = 0;
          }
        }
        if (bCount > 0) {
          await batch.commit();
        }
      }
    }

    return {
      success: true,
      studentsScanned: studentCodes.length,
      reviewsApproved,
      attemptsApproved,
      parentReviewsApproved,
      evaluationsApproved,
      message: `Swept ${studentCodes.length} autonomous students: approved ${reviewsApproved} reviews, ${attemptsApproved} attempts, ${parentReviewsApproved} parentReviews, ${evaluationsApproved} evaluations.`
    };
  }
}
