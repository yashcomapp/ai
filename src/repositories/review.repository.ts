import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { SubjectiveReview, PeerAssignment } from '@/types/review.types';

export class ReviewRepository {
  /**
   * Locates peer assignments matching exam, reviewer, and reviewee parameters.
   */
  static async getPeerAssignments(
    examId: string,
    reviewerStudentCode: string,
    revieweeCode: string
  ): Promise<PeerAssignment[]> {
    const snap = await adminDb.collection('peerAssignments')
      .where('examId', '==', examId)
      .where('reviewerStudentCode', '==', reviewerStudentCode)
      .where('revieweeStudentCode', '==', revieweeCode)
      .get();
    return snap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        examId: data.examId,
        reviewerStudentCode: data.reviewerStudentCode,
        revieweeCode: data.revieweeStudentCode || data.revieweeCode || '',
        status: data.status,
        completedAt: data.completedAt,
        marksAwarded: data.marksAwarded
      } as PeerAssignment;
    });
  }

  /**
   * Saves subjective reviews inside or outside transactions.
   */
  static saveSubjectiveReview(
    data: Partial<SubjectiveReview>,
    tx?: admin.firestore.Transaction
  ): void {
    const ref = adminDb.collection('subjectiveReviews').doc();
    if (tx) {
      tx.set(ref, data);
    } else {
      ref.set(data);
    }
  }

  /**
   * Updates subjective attempt attributes inside a transaction.
   */
  static updateSubjectiveAttempt(
    attemptId: string,
    data: any,
    tx?: admin.firestore.Transaction
  ): void {
    const ref = adminDb.collection('subjectiveAttempts').doc(attemptId);
    if (tx) {
      tx.update(ref, data);
    } else {
      ref.update(data);
    }
  }
}
