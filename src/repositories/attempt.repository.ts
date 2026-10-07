import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ExamAttempt } from '@/types/attempt.types';

export class AttemptRepository {
  /**
   * Saves or merges exam attempt data. Supports writing via an optional Firestore transaction.
   */
  static saveAttempt(
    examId: string,
    studentCode: string,
    data: Partial<ExamAttempt>,
    tx?: admin.firestore.Transaction
  ): void {
    const ref = adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`);
    if (tx) {
      tx.set(ref, data, { merge: true });
    } else {
      ref.set(data, { merge: true });
    }
  }
}
