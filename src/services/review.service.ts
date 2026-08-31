import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ReviewRepository } from '@/repositories/review.repository';
import { MasteryService } from '@/services/mastery.service';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

export class ReviewService {
  /**
   * Orchestrates classmate peer review submissions, matching attempts status updates,
   * assignments completeness updates, and exam status transitions atomically in a transaction.
   * For Class 10 students, automatically computes and updates topic mastery in studentTopicMastery.
   */
  static async submitPeerReview(params: {
    studentCode: string;
    attemptId: string;
    examId: string;
    revieweeCode: string;
    questionReviews: any;
    totalScore: number;
  }): Promise<{ success: boolean }> {
    const { studentCode, attemptId, examId, revieweeCode, questionReviews, totalScore } = params;

    // 1. Verify access authority
    const assignments = await ReviewRepository.getPeerAssignments(examId, studentCode, revieweeCode);
    if (assignments.length === 0) {
      throw new Error('Access Denied. You are not assigned to grade this student\'s exam.');
    }

    const reviewData = {
      attemptId,
      examId,
      reviewerId: studentCode,
      reviewerType: 'peer' as const,
      revieweeCode,
      questionReviews,
      totalScore: Number(totalScore) || 0,
      isFinal: true,
      submittedAt: new Date(),
      createdAt: new Date()
    };

    // 2. Perform atomic transaction
    await adminDb.runTransaction(async (tx) => {
      // 2.1 Perform all READS first
      const attemptRef = adminDb.collection('subjectiveAttempts').doc(attemptId);
      const revieweeQuery = adminDb.collection('subjectiveAttempts')
        .where('examId', '==', examId)
        .where('studentCode', '==', revieweeCode);
      const reviewerAssignQuery = adminDb.collection('peerAssignments')
        .where('examId', '==', examId)
        .where('reviewerStudentCode', '==', studentCode);
      const allAssignsQuery = adminDb.collection('peerAssignments').where('examId', '==', examId);
      const examRef = adminDb.collection('subjectiveExams').doc(examId);
      const revieweeUserQuery = adminDb.collection('users')
        .where('studentCode', '==', revieweeCode)
        .limit(1);

      const [attemptSnap, revieweeAttemptsSnap, peerAssignSnap, allPeerAssignsSnap, examSnap, revieweeUserSnap] = await Promise.all([
        tx.get(attemptRef),
        tx.get(revieweeQuery),
        tx.get(reviewerAssignQuery),
        tx.get(allAssignsQuery),
        tx.get(examRef),
        tx.get(revieweeUserQuery)
      ]);

      // Verify attempt is authorized (IDOR Protection of reviewer)
      if (!attemptSnap.exists) {
        throw new Error('Access Denied. Subjective attempt does not exist.');
      }
      const attemptData = attemptSnap.data() || {};
      if (attemptData.studentCode !== studentCode || attemptData.examId !== examId) {
        throw new Error('Access Denied. Reviewer/Attempt discrepancy.');
      }

      if (revieweeAttemptsSnap.empty) {
        throw new Error('Access Denied. Reviewee attempt does not exist.');
      }

      const revieweeAttemptDoc = revieweeAttemptsSnap.docs[0];
      const revieweeAttemptId = revieweeAttemptDoc.id;
      const revieweeAttemptData = revieweeAttemptDoc.data() || {};
      const examData = examSnap.exists ? examSnap.data()! : {};
      const revieweeUserData = revieweeUserSnap.empty ? {} : revieweeUserSnap.docs[0].data();
      const revieweeClass = revieweeUserData.class || examData.class;

      // Extract questions map for mastery evaluation
      let questionsList: any[] = [];
      if (Array.isArray(revieweeAttemptData.questionSnapshot) && revieweeAttemptData.questionSnapshot.length > 0) {
        questionsList = revieweeAttemptData.questionSnapshot;
      } else if (Array.isArray(examData.questions) && examData.questions.length > 0) {
        questionsList = examData.questions;
      }

      const questionMap = new Map<string, any>();
      questionsList.forEach(q => {
        if (q) {
          if (q.id) questionMap.set(String(q.id), q);
          if (q.questionCode) questionMap.set(String(q.questionCode), q);
        }
      });

      // Prepare Class 10 Topic Mastery reads if applicable
      const topicBuckets: { [topicCode: string]: any[] } = {};
      let isClass10Target = MasteryService.isClass10(revieweeClass);

      if (Array.isArray(questionReviews)) {
        questionReviews.forEach((qr: any) => {
          const q = questionMap.get(String(qr.questionId)) || {};
          const qCode = q.questionCode || qr.questionId;
          const topicCode = q.topicCode || deriveTopicCodeFromQuestionCode(qCode);

          if (topicCode) {
            if (MasteryService.isClass10(revieweeClass, topicCode)) {
              isClass10Target = true;
              if (!topicBuckets[topicCode]) {
                topicBuckets[topicCode] = [];
              }
              topicBuckets[topicCode].push({
                id: qr.questionId,
                questionCode: qCode,
                topicCode: topicCode,
                difficulty: q.difficulty || 'medium',
                bloomLevel: q.bloomLevel || (q.type === 'subjective_long' ? 'Analyze' : 'Apply'),
                marksAwarded: Number(qr.marksAwarded) || 0,
                maxMarks: Number(qr.maxMarks) || q.marks || 2,
                isCorrect: (Number(qr.marksAwarded) || 0) >= ((Number(qr.maxMarks) || 2) * 0.5)
              });
            }
          }
        });
      }

      const topicCodes = isClass10Target ? Object.keys(topicBuckets) : [];
      const topicMasteryRefs = topicCodes.map(tCode => ({
        tCode,
        ref: adminDb.collection('studentTopicMastery').doc(`${revieweeCode}_${tCode}`)
      }));
      const topicMasterySnaps = await Promise.all(topicMasteryRefs.map(m => tx.get(m.ref)));

      // --- 2.2 PERFORM ALL WRITES ---
      // Write peer review evaluation doc
      ReviewRepository.saveSubjectiveReview({
        ...reviewData,
        attemptId: revieweeAttemptId
      }, tx);

      // Update reviewee subjectiveAttempt status
      revieweeAttemptsSnap.docs.forEach(doc => {
        tx.update(doc.ref, {
          status: 'peer_reviewed',
          peerReviewedAt: new Date(),
          peerScore: Number(totalScore) || 0
        });
      });

      // Update reviewer's peerAssignments mapping status
      peerAssignSnap.docs.forEach(doc => {
        tx.update(doc.ref, {
          status: 'completed',
          completedAt: new Date(),
          marksAwarded: Number(totalScore) || 0
        });
      });

      // Update subjectiveExams completed count if all peer assignments are finished
      let pendingCount = 0;
      allPeerAssignsSnap.docs.forEach(doc => {
        const isBeingCompleted = peerAssignSnap.docs.some(d => d.id === doc.id);
        const currentStatus = doc.data().status;
        if (!isBeingCompleted && currentStatus === 'pending') {
          pendingCount++;
        }
      });

      if (pendingCount === 0 && examSnap.exists) {
        tx.update(adminDb.collection('subjectiveExams').doc(examId), {
          peerReviewStatus: 'completed',
          peerReviewCompletedAt: new Date(),
          updatedAt: new Date()
        });
      }

      // Update Topic Mastery for Class 10 students
      if (topicCodes.length > 0) {
        topicMasteryRefs.forEach((m, idx) => {
          const snap = topicMasterySnaps[idx];
          const existing = snap.exists ? snap.data()! : null;
          const initialData = existing ? { ...existing } : {
            studentCode: revieweeCode,
            topicCode: m.tCode,
            mastery: 0,
            confidence: 0,
            questionsAttempted: 0,
            questionsCorrect: 0,
            questionsWrong: 0,
            weightedPointsEarned: 0,
            weightedPointsPossible: 0,
            lastExamCode: '',
            questionHistory: [] as any[],
            createdAt: new Date()
          };

          const updatedData = MasteryService.calculateTopicMasteryUpdate(
            initialData,
            topicBuckets[m.tCode],
            examId
          );

          tx.set(m.ref, updatedData, { merge: true });
        });
      }
    });

    return { success: true };
  }
}
