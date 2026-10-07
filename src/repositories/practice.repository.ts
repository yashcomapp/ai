import { adminDb } from '@/lib/firebase/admin';
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
}
