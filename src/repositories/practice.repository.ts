import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { TopicMasteryRecord } from '@/types/practice.types';

export class PracticeRepository {
  /**
   * Retrieves a specific topic mastery record for a student.
   */
  static async getTopicMastery(studentCode: string, topicCode: string): Promise<TopicMasteryRecord | null> {
    const snap = await adminDb.collection('studentTopicMastery').doc(`${studentCode}_${topicCode}`).get();
    if (!snap.exists) return null;
    return { id: snap.id, ...snap.data() } as any as TopicMasteryRecord;
  }

  /**
   * Saves or updates topic mastery record inside or outside a transaction.
   */
  static saveTopicMastery(
    studentCode: string,
    topicCode: string,
    data: Partial<TopicMasteryRecord>,
    tx?: admin.firestore.Transaction
  ): void {
    const ref = adminDb.collection('studentTopicMastery').doc(`${studentCode}_${topicCode}`);
    if (tx) {
      tx.set(ref, data, { merge: true });
    } else {
      ref.set(data, { merge: true });
    }
  }

  /**
   * Lists all topic masteries for a student.
   */
  static async listTopicMasteries(studentCode: string): Promise<TopicMasteryRecord[]> {
    const snap = await adminDb.collection('studentTopicMastery')
      .where('studentCode', '==', studentCode)
      .get();
    return snap.docs.map(doc => ({ id: doc.id, ...doc.data() } as any as TopicMasteryRecord));
  }
}
