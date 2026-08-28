import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { ExamAttempt } from '@/types/attempt.types';

export class AttemptRepository {
  /**
   * Retrieves a student's attempt for a specific exam.
   */
  static async getAttempt(examId: string, studentCode: string): Promise<ExamAttempt | null> {
    const snap = await adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`).get();
    if (!snap.exists) return null;
    return { id: snap.id, ...snap.data() } as ExamAttempt;
  }

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

  /**
   * Lists all attempts for a given student.
   */
  static async getAttemptsByStudent(studentCode: string): Promise<ExamAttempt[]> {
    const snap = await adminDb.collection('examAttempts')
      .where('studentCode', '==', studentCode)
      .get();
    return snap.docs.map(doc => ({ id: doc.id, ...doc.data() } as ExamAttempt));
  }

  /**
   * Lists attempts for a given exam.
   */
  static async getAttemptsByExam(examId: string): Promise<ExamAttempt[]> {
    const snap = await adminDb.collection('examAttempts')
      .where('examId', '==', examId)
      .get();
    return snap.docs.map(doc => ({ id: doc.id, ...doc.data() } as ExamAttempt));
  }
}
