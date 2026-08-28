import { adminDb } from '@/lib/firebase/admin';
import { StudentProfile, StudentTopicMastery, WeeklyIntegrity } from '@/types/user.types';

export class StudentRepository {
  private static masteryCollection = adminDb.collection('studentTopicMastery');
  private static integrityCollection = adminDb.collection('integrityScores');

  /**
   * Fetch topic mastery by student code and topic code
   */
  static async getTopicMastery(studentCode: string, topicCode: string): Promise<StudentTopicMastery | null> {
    const docId = `${studentCode}_${topicCode}`;
    const doc = await this.masteryCollection.doc(docId).get();
    if (!doc.exists) return null;
    return { id: doc.id, ...doc.data() } as StudentTopicMastery;
  }

  /**
   * Fetch weekly integrity score
   */
  static async getWeeklyIntegrityScore(studentCode: string, year: number, week: number): Promise<WeeklyIntegrity | null> {
    const docId = `${studentCode}_${year}_${week}`;
    const doc = await this.integrityCollection.doc(docId).get();
    if (!doc.exists) return null;
    return doc.data() as WeeklyIntegrity;
  }

  /**
   * Retrieve list of all student accounts with full tracking details
   */
  static async listStudents(): Promise<any[]> {
    const snap = await adminDb.collection('users').where('role', '==', 'student').get();
    return snap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        name: data.name || data.displayName || 'Unknown Student',
        email: data.email || '',
        studentCode: data.studentCode || '',
        rollNumber: data.rollNumber || '',
        tempId: data.tempId || '',
        dob: data.dob || '',
        feeStatus: data.feeStatus || 'pending',
        parentEmail: (data.parentEmail || '').toLowerCase(),
        batchIds: data.batchIds || (data.batchId ? [data.batchId] : []),
        lastActiveAt: data.lastActiveAt || null,
        presenceState: data.presenceState || 'inactive',
        currentPage: data.currentPage || '',
        currentPagePath: data.currentPagePath || '',
        overallMastery: data.overallMastery || 0,
        autonomous: data.autonomous === true || data.isAutonomous === true || data.mode === 'autonomous',
        role: 'student' as const,
        status: data.status || 'active'
      };
    }).filter(s => s.status !== 'inactive');
  }

  /**
   * Retrieve list of all parent accounts with full tracking details
   */
  static async listParents(): Promise<any[]> {
    const snap = await adminDb.collection('users').where('role', '==', 'parent').get();
    return snap.docs.map(doc => {
      const data = doc.data();
      const codes = data.studentCodes || (data.studentCode ? [data.studentCode] : []);
      return {
        id: doc.id,
        name: data.name || data.displayName || 'Unknown Parent',
        email: (data.email || '').toLowerCase(),
        studentCodes: codes,
        lastActiveAt: data.lastActiveAt || null,
        presenceState: data.presenceState || 'inactive',
        currentPage: data.currentPage || '',
        currentPagePath: data.currentPagePath || '',
        role: 'parent' as const,
        status: data.status || 'active'
      };
    }).filter(p => p.status !== 'inactive');
  }
}
