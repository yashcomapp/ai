import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ReviewRepository } from '@/repositories/review.repository';

export class ReviewService {
  /**
   * Orchestrates classmate peer review submissions, matching attempts status updates,
   * assignments completeness updates, and exam status transitions atomically in a transaction.
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

      const [attemptSnap, revieweeAttemptsSnap, peerAssignSnap, allPeerAssignsSnap] = await Promise.all([
        tx.get(attemptRef),
        tx.get(revieweeQuery),
        tx.get(reviewerAssignQuery),
        tx.get(allAssignsQuery)
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

      const revieweeAttemptId = revieweeAttemptsSnap.docs[0].id;

      // 2.2 Write peer review evaluation doc
      ReviewRepository.saveSubjectiveReview({
        ...reviewData,
        attemptId: revieweeAttemptId
      }, tx);

      // 2.4 Update reviewee subjectiveAttempt status
      revieweeAttemptsSnap.docs.forEach(doc => {
        tx.update(doc.ref, {
          status: 'peer_reviewed',
          peerReviewedAt: new Date(),
          peerScore: Number(totalScore) || 0
        });
      });

      // 2.5 Update reviewer's peerAssignments mapping status
      peerAssignSnap.docs.forEach(doc => {
        tx.update(doc.ref, {
          status: 'completed',
          completedAt: new Date(),
          marksAwarded: Number(totalScore) || 0
        });
      });

      // 2.6 Update subjectiveExams completed count if all peer assignments are finished
      let pendingCount = 0;
      allPeerAssignsSnap.docs.forEach(doc => {
        const isBeingCompleted = peerAssignSnap.docs.some(d => d.id === doc.id);
        const currentStatus = doc.data().status;
        if (!isBeingCompleted && currentStatus === 'pending') {
          pendingCount++;
        }
      });

      if (pendingCount === 0) {
        tx.update(adminDb.collection('subjectiveExams').doc(examId), {
          peerReviewStatus: 'completed',
          peerReviewCompletedAt: new Date(),
          updatedAt: new Date()
        });
      }
    });

    return { success: true };
  }
}
