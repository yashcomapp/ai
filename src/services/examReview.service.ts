import { adminDb } from '@/lib/firebase/admin';
import { parseDateInput, getDateKeyIST } from '@/lib/dateUtils';
import { EvaluationService } from './evaluation.service';
import { MasteryService } from './mastery.service';
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
    
    // 1. Fetch official exam review doc if submitted
    const reviewRef = adminDb.collection('reviews').doc(`${examId}_${sCodeUpper}`);
    let reviewSnap = await reviewRef.get();
    if (!reviewSnap.exists) {
      // Fallback query in reviews
      const qSnap = await adminDb.collection('reviews')
        .where('studentCode', '==', sCodeUpper)
        .where('examId', '==', examId)
        .limit(1)
        .get();
      if (!qSnap.empty) reviewSnap = qSnap.docs[0];
    }

    let reviewData = reviewSnap.exists ? reviewSnap.data() : null;

    // Fallback query in examAttempts if review not found
    if (!reviewData) {
      const attemptSnap = await adminDb.collection('examAttempts')
        .where('studentCode', '==', sCodeUpper)
        .where('examId', '==', examId)
        .limit(1)
        .get();
      if (!attemptSnap.empty) {
        reviewData = attemptSnap.docs[0].data();
      }
    }

    if (!reviewData) {
      return {
        hasAttempt: false,
        examId,
        studentCode: sCodeUpper,
        completedAt: null,
        elapsedMinutes: 0,
        remainingMinutes: 0,
        isWithin60MinWindow: false,
        status: 'pending',
        reviewedAt: null,
        timeSpentSeconds: 0,
        reviewedQuestionCount: 0,
        disputeCount: 0,
        bountyEarnedCount: 0
      };
    }

    const completedDate = parseDateInput(reviewData?.completedAt || reviewData?.submittedAt || reviewData?.createdAt);

    const now = new Date();
    const elapsedMinutes = completedDate ? Math.max(0, Math.floor((now.getTime() - completedDate.getTime()) / 60000)) : 0;
    const remainingMinutes = Math.max(0, 60 - elapsedMinutes);
    const isWithin60MinWindow = elapsedMinutes <= 60;

    // 2. Fetch verified examReview submission
    const examReviewDoc = await adminDb.collection('examReviews').doc(`${sCodeUpper}_${examId}`).get();
    const examReviewData = examReviewDoc.exists ? examReviewDoc.data() : null;

    let status: 'pending' | 'on_time' | 'late' = 'pending';
    if (examReviewData) {
      status = examReviewData.status || (examReviewData.elapsedMinutesAtSubmission <= 60 ? 'on_time' : 'late');
    }

    return {
      hasAttempt: true,
      examId,
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
    studentName: string;
    examId: string;
    examName?: string;
    batchId?: string;
    reviewedQuestionIds: string[];
    challenges: QuestionDisputeInput[];
    timeSpentSeconds: number;
  }): Promise<{
    success: boolean;
    status: 'on_time' | 'late';
    remainingMinutes: number;
    bountiesAwarded: number;
    message: string;
  }> {
    const {
      studentCode,
      studentName,
      examId,
      examName = 'Official Exam',
      batchId = '',
      reviewedQuestionIds,
      challenges = [],
      timeSpentSeconds
    } = params;

    const sCodeUpper = studentCode.trim().toUpperCase();
    const now = new Date();

    // Check attempt completion timestamp
    const reviewStatus = await this.getReviewStatus(sCodeUpper, examId);
    if (!reviewStatus.hasAttempt) {
      throw new Error('No exam attempt found for this student. You can only review exams you have attempted.');
    }

    const isWithin60Min = reviewStatus.isWithin60MinWindow;
    const reviewStatusValue = isWithin60Min ? 'on_time' : 'late';

    let bountyCount = 0;

    // Process and rank question challenges atomically (Strictly First 3 Reporters get bounty eligibility)
    for (const challenge of challenges) {
      const qId = challenge.questionId || challenge.questionCode;
      if (!qId) continue;

      const disputeDocId = `${examId}_${qId}_${sCodeUpper}`;
      const disputeRef = adminDb.collection('questionDisputes').doc(disputeDocId);
      const counterRef = adminDb.collection('examDisputeCounters').doc(`${examId}_${qId}`);

      const awardedBounty = await adminDb.runTransaction(async (transaction) => {
        const disputeSnap = await transaction.get(disputeRef);
        if (disputeSnap.exists) {
          // Already reported by this student
          return disputeSnap.data()?.eligibleForBounty || false;
        }

        const counterSnap = await transaction.get(counterRef);
        const currentCount = counterSnap.exists ? (Number(counterSnap.data()?.count) || 0) : 0;
        const reporterRank = currentCount + 1;
        const eligibleForBounty = reporterRank <= 3;

        transaction.set(counterRef, {
          count: reporterRank,
          examId,
          questionId: qId,
          lastReportedAt: now.toISOString()
        }, { merge: true });

        transaction.set(disputeRef, {
          id: disputeDocId,
          examId,
          examName,
          questionId: qId,
          questionCode: challenge.questionCode || qId,
          questionText: challenge.questionText || '',
          studentCode: sCodeUpper,
          studentName,
          batchId,
          reason: challenge.reason,
          suggestedAnswer: challenge.suggestedAnswer || '',
          notes: challenge.notes || '',
          source: 'exam_review',
          reporterRank,
          eligibleForBounty,
          status: 'pending',
          submittedAt: now.toISOString(),
          createdAt: now.toISOString()
        });

        return eligibleForBounty;
      });

      if (awardedBounty) {
        bountyCount++;
      }
    }

    // Save master examReview record
    const examReviewRef = adminDb.collection('examReviews').doc(`${sCodeUpper}_${examId}`);
    await examReviewRef.set({
      id: `${sCodeUpper}_${examId}`,
      studentCode: sCodeUpper,
      studentName,
      batchId,
      examId,
      examName,
      reviewedQuestionIds,
      timeSpentSeconds,
      elapsedMinutesAtSubmission: reviewStatus.elapsedMinutes,
      status: reviewStatusValue,
      disputeCount: challenges.length,
      bountyEarnedCount: bountyCount,
      submittedAt: now.toISOString()
    }, { merge: true });

    return {
      success: true,
      status: reviewStatusValue,
      remainingMinutes: reviewStatus.remainingMinutes,
      bountiesAwarded: bountyCount,
      message: isWithin60Min
        ? `✅ Review verified on-time within the 60-minute window! ${bountyCount > 0 ? `🏆 You are in the Top 3 bounty reporters for ${bountyCount} question(s)!` : ''}`
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
    action: 'correct_key' | 'bonus_all' | 'quarantine';
    notes?: string;
    adminEmail?: string;
  }): Promise<{
    studentsUpdated: number;
    top3Reporters: Array<{ studentCode: string; studentName: string; rank: number }>;
    message: string;
  }> {
    const { examId, questionId, newCorrectOption, action, notes = '', adminEmail = 'Admin' } = params;

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
        await qRef.update({
          flaggedDefective: true,
          defectiveReason: notes || 'Admin quarantined defective question',
          quarantinedAt: new Date().toISOString()
        });
      }
      invalidateCache('qb_base_');
    }

    // 2. Fetch and award bounty strictly to the first 3 reporters
    const disputesSnap = await adminDb.collection('questionDisputes')
      .where('examId', '==', examId)
      .where('questionId', '==', questionId)
      .get();

    const disputesList = disputesSnap.docs.map(d => ({ docId: d.id, ...d.data() } as any));
    disputesList.sort((a, b) => new Date(a.submittedAt).getTime() - new Date(b.submittedAt).getTime());

    const top3Reporters: Array<{ studentCode: string; studentName: string; rank: number }> = [];

    for (let i = 0; i < disputesList.length; i++) {
      const dispute = disputesList[i];
      const isTop3 = i < 3;
      const rank = dispute.reporterRank || i + 1;

      if (isTop3) {
        top3Reporters.push({
          studentCode: dispute.studentCode,
          studentName: dispute.studentName,
          rank
        });
      }

      await adminDb.collection('questionDisputes').doc(dispute.docId).update({
        status: isTop3 ? 'approved_bounty' : 'approved_no_bounty',
        actualRank: rank,
        resolvedBy: adminEmail,
        resolvedAt: new Date().toISOString(),
        resolutionNotes: notes
      });
    }

    // 3. Batch Re-Evaluate All Students on this Exam
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

      // Check if this student is among top 3 bounty recipients (+2 Diligence Bonus)
      const isBountyWinner = top3Reporters.some(r => r.studentCode?.toUpperCase() === studentCode?.toUpperCase());
      const diligenceBonus = isBountyWinner ? 2 : 0;

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
      const finalScoreWithBonus = Math.max(0, revisedScore + diligenceBonus);

      currentBatch.update(doc.ref, {
        score: finalScoreWithBonus,
        totalMarks: totalMax,
        percentage: academicPercentage,
        questionDetails: updatedQuestionDetails,
        diligenceBonusAwarded: diligenceBonus,
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
          await MasteryService.recordExamAttempt(studentCode, firstTopicCode, academicPercentage, examId);
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
      top3Reporters,
      message: `Successfully batch re-evaluated ${studentsUpdated} student exam submissions. Top ${top3Reporters.length} reporters awarded Diligence Bounty badges!`
    };
  }
}

function deriveTopicCode(qCode: string): string {
  if (!qCode) return '';
  const parts = qCode.split('-');
  return parts.length >= 5 ? parts.slice(0, 5).join('-') : '';
}
