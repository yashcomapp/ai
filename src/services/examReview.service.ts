import { adminDb } from '@/lib/firebase/admin';
import { parseDateInput, getDateKeyIST } from '@/lib/dateUtils';
import { EvaluationService } from './evaluation.service';
import { MasteryService } from './mastery.service';
import { invalidateCache } from '@/lib/firebase/cache';
import { QuestionRepository } from '@/repositories/question.repository';

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
      const userSnap = await adminDb.collection('users').where('studentCode', '==', sCodeUpper).limit(1).get().catch(() => null);
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
   * 1-Click Batch Exam Re-Evaluation when an admin approves a question correction.
   * Updates question bank, awards bounty badges to the top 3 reporters, and recalculates
   * every student's score, percentage, and topic mastery on that exam.
   */
  static async batchReevaluateExam(params: {
    examId: string;
    questionId: string;
    newCorrectOption: string; // e.g. 'B' or 'C' or 'ALL_CORRECT'
    action: 'correct_key' | 'bonus_all' | 'quarantine' | 'reject_challenge' | 'dismiss';
    notes?: string;
    adminEmail?: string;
  }): Promise<{
    studentsUpdated: number;
    top3Reporters: Array<{ studentCode: string; studentName: string; rank: number }>;
    message: string;
  }> {
    const { examId, questionId, newCorrectOption, action, notes = '', adminEmail = 'Admin' } = params;

    if (action === 'reject_challenge' || (action as any) === 'dismiss') {
      return {
        studentsUpdated: 0,
        top3Reporters: [],
        message: `Action dismissed. No changes made to student marks or answer keys.`
      };
    }

    // 1. Update Question Bank document
    let qRef = adminDb.collection('questions').doc(questionId);
    let qSnap = await qRef.get();
    if (!qSnap.exists) {
      const qByCodeSnap = await adminDb.collection('questions')
        .where('questionCode', '==', questionId)
        .limit(1)
        .get();
      if (!qByCodeSnap.empty) {
        qRef = qByCodeSnap.docs[0].ref;
        qSnap = qByCodeSnap.docs[0];
      }
    }

    if (qSnap.exists) {
      if (action === 'correct_key') {
        await qRef.update({
          correctAnswer: newCorrectOption,
          answer: newCorrectOption,
          correctionAudit: {
            previousAnswer: qSnap.data()?.correctAnswer || qSnap.data()?.answer,
            correctedAnswer: newCorrectOption,
            correctedBy: adminEmail,
            correctedAt: new Date().toISOString()
          }
        });
      } else if (action === 'quarantine') {
        const qData = qSnap.data() || {};
        const qCode = qData.questionCode || questionId;

        const quarantinePayload = {
          status: 'quarantined',
          isQuarantined: true,
          flaggedDefective: true,
          quarantinedReason: notes || 'Admin quarantined defective question from Disputes Hub',
          quarantinedBy: adminEmail,
          quarantinedAt: new Date().toISOString()
        };

        // Soft-quarantine the primary question doc (preserves referential integrity for scheduled exams)
        await qRef.update(quarantinePayload);

        // Archive snapshot to quarantinedQuestions collection
        await adminDb.collection('quarantinedQuestions').doc(qRef.id).set({
          ...qData,
          ...quarantinePayload
        }, { merge: true });

        // Also soft-quarantine any duplicate documents with the same questionCode
        if (qCode) {
          const dupSnaps = await adminDb.collection('questions').where('questionCode', '==', qCode).get();
          if (!dupSnaps.empty) {
            const updBatch = adminDb.batch();
            dupSnaps.docs.forEach(d => updBatch.update(d.ref, quarantinePayload));
            await updBatch.commit();
          }
        }
      }
      invalidateCache('qb_base_');
      QuestionRepository.clearTopicCache();
    } else if (action === 'quarantine') {
      // If direct doc did not exist, search by questionCode and soft-quarantine
      const qByCodeSnap = await adminDb.collection('questions')
        .where('questionCode', '==', questionId)
        .get();
      if (!qByCodeSnap.empty) {
        const quarantinePayload = {
          status: 'quarantined',
          isQuarantined: true,
          flaggedDefective: true,
          quarantinedReason: notes || 'Admin quarantined defective question from Disputes Hub',
          quarantinedBy: adminEmail,
          quarantinedAt: new Date().toISOString()
        };

        const updBatch = adminDb.batch();
        for (const doc of qByCodeSnap.docs) {
          await adminDb.collection('quarantinedQuestions').doc(doc.id).set({
            ...doc.data(),
            ...quarantinePayload
          }, { merge: true });
          updBatch.update(doc.ref, quarantinePayload);
        }
        await updBatch.commit();
        invalidateCache('qb_base_');
        QuestionRepository.clearTopicCache();
      }
    }

    // 2. Batch Re-Evaluate All Students on this Exam if valid scheduled exam
    const isRealExam = examId && examId !== 'unassigned_exam' && examId !== 'null' && !examId.startsWith('practice_');
    if (!isRealExam) {
      return {
        studentsUpdated: 0,
        top3Reporters: [],
        message: `Question ${questionId} updated in Question Bank successfully.`
      };
    }

    const [reviewsSnap, examDocSnap] = await Promise.all([
      adminDb.collection('reviews').where('examId', '==', examId).get(),
      adminDb.collection('exams').doc(examId).get()
    ]);

    const examData = examDocSnap.exists ? examDocSnap.data() : {};
    const positiveMarks = Number(examData?.positiveMarks) || 4;
    const negativeMarks = Number(examData?.negativeMarks) || 0;

    let studentsUpdated = 0;
    const BATCH_SIZE = 400;
    let currentBatch = adminDb.batch();
    let batchOpCount = 0;

    for (const doc of reviewsSnap.docs) {
      const review = doc.data();
      const studentCode = review.studentCode;
      const questionDetails = Array.isArray(review.questionDetails) ? review.questionDetails : [];
      let revisedScore = 0;
      let totalMarks = 0;

      const updatedQuestionDetails = questionDetails.map((q: any) => {
        const qCode = q.questionCode || q.id || q.questionId;
        const matchesQ = String(qCode).toLowerCase() === String(questionId).toLowerCase();

        if (matchesQ) {
          const qPositive = q.marks || positiveMarks;
          const qNegative = q.negativeMarks !== undefined ? q.negativeMarks : negativeMarks;
          totalMarks += qPositive;

          let isNowCorrect = false;
          if (action === 'bonus_all') {
            isNowCorrect = true;
          } else if (action === 'correct_key') {
            isNowCorrect = EvaluationService.evaluate(q.type || 'single_choice', q.userAnswer, newCorrectOption, q.options);
          } else if (action === 'quarantine') {
            // Exclude from max marks calculation (pro-rata)
            totalMarks -= qPositive;
            return {
              ...q,
              isQuarantined: true,
              isCorrect: false
            };
          }

          if (isNowCorrect) {
            revisedScore += qPositive;
          } else if (q.userAnswer && q.userAnswer !== 'unanswered') {
            revisedScore -= qNegative;
          }

          return {
            ...q,
            correctAnswer: action === 'correct_key' ? newCorrectOption : q.correctAnswer,
            isCorrect: isNowCorrect
          };
        } else {
          const qPositive = q.marks || positiveMarks;
          const qNegative = q.negativeMarks !== undefined ? q.negativeMarks : negativeMarks;
          if (!q.isQuarantined) totalMarks += qPositive;

          if (q.isCorrect) {
            revisedScore += qPositive;
          } else if (q.userAnswer && q.userAnswer !== 'unanswered' && !q.isQuarantined) {
            revisedScore -= qNegative;
          }
          return q;
        }
      });

      const totalMax = Math.max(1, totalMarks);
      // Clamp academic percentage to 100% per Rule 2A
      const academicScore = Math.min(totalMax, Math.max(0, revisedScore));
      const academicPercentage = Math.min(100, Math.round((academicScore / totalMax) * 100));

      currentBatch.update(doc.ref, {
        score: academicScore,
        totalMarks: totalMax,
        percentage: academicPercentage,
        questionDetails: updatedQuestionDetails,
        recalculatedAt: new Date().toISOString(),
        recalculatedReason: `Answer key update for Q: ${questionId} by ${adminEmail}`
      });

      batchOpCount++;
      if (batchOpCount >= BATCH_SIZE) {
        await currentBatch.commit();
        currentBatch = adminDb.batch();
        batchOpCount = 0;
      }

      studentsUpdated++;

      // Trigger mastery recalculation for student if topic code present
      const firstTopicCode = review.topicCode || (updatedQuestionDetails[0]?.questionCode ? deriveTopicCode(updatedQuestionDetails[0].questionCode) : '');
      if (studentCode && firstTopicCode) {
        try {
          const masteryRef = adminDb.collection('studentTopicMastery').doc(`${studentCode}_${firstTopicCode}`);
          const masterySnap = await masteryRef.get();
          const existingMastery = masterySnap.exists ? masterySnap.data() : { studentCode, topicCode: firstTopicCode };
          const evaluations = updatedQuestionDetails.map((qd: any) => ({
            id: qd.questionId || qd.id || qd.questionCode || '',
            difficulty: qd.difficulty || 'medium',
            bloomLevel: qd.bloomLevel || 'Understand',
            isCorrect: !!qd.isCorrect,
            marksAwarded: qd.isCorrect ? (qd.marks || 4) : 0,
            maxMarks: qd.marks || 4,
            examCategory: 'standard'
          }));
          const updatedMasteryData = MasteryService.calculateTopicMasteryUpdate(existingMastery, evaluations, examId);
          await masteryRef.set(updatedMasteryData, { merge: true });
        } catch (mErr) {
          console.warn('Failed to update mastery on re-evaluation:', mErr);
        }
      }
    }

    if (batchOpCount > 0) {
      await currentBatch.commit();
    }

    return {
      studentsUpdated,
      top3Reporters: [],
      message: `Successfully batch re-evaluated ${studentsUpdated} student exam submissions.`
    };
  }
}

function deriveTopicCode(qCode: string): string {
  if (!qCode) return '';
  const parts = qCode.split('-');
  return parts.length >= 5 ? parts.slice(0, 5).join('-') : '';
}
