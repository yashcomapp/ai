import { adminDb } from '@/lib/firebase/admin';
import { Exam, Assignment } from '@/types/exam.types';
import { QuestionItem } from '@/types/question.types';

export class ExamRepository {
  private static examsCollection = adminDb.collection('exams');
  private static questionsCollection = adminDb.collection('questions');
  private static assignmentsCollection = adminDb.collection('batchAssignments');

  /**
   * Fetch exam by ID
   */
  static async getById(examId: string): Promise<Exam | null> {
    const doc = await this.examsCollection.doc(examId).get();
    if (!doc.exists) return null;
    return { id: doc.id, ...doc.data() } as Exam;
  }

  /**
   * Fetch full question documents from list of codes (with questionCode field fallback)
   */
  static async getQuestionsForExam(questionIds: string[]): Promise<QuestionItem[]> {
    if (!questionIds || questionIds.length === 0) return [];
    
    const refs = questionIds.map((id: string) => this.questionsCollection.doc(id));
    const questionSnaps = await adminDb.getAll(...refs).catch(() => []);
    
    let rawQuestions = questionSnaps
      .filter((snap: any) => snap && snap.exists)
      .map((snap: any) => ({ id: snap.id, ...snap.data() } as QuestionItem));

    // Fallback: If any questions were not found by document ID, search by questionCode field
    if (rawQuestions.length < questionIds.length) {
      const foundIdsAndCodes = new Set([
        ...rawQuestions.map((q: any) => q.id),
        ...rawQuestions.map((q: any) => q.questionCode).filter(Boolean)
      ]);
      const missingCodes = questionIds.filter((c: string) => !foundIdsAndCodes.has(c));

      if (missingCodes.length > 0) {
        for (let i = 0; i < missingCodes.length; i += 30) {
          const chunk = missingCodes.slice(i, i + 30);
          const qSnap = await this.questionsCollection
            .where('questionCode', 'in', chunk)
            .get();
          qSnap.docs.forEach(doc => {
            rawQuestions.push({ id: doc.id, ...doc.data() } as QuestionItem);
          });
        }
      }
    }

    return rawQuestions;
  }

  /**
   * Fetch assignments matching studentCode and examId
   */
  static async getAssignmentsForStudentExam(examId: string, studentCode: string): Promise<Assignment[]> {
    const snap = await this.assignmentsCollection
      .where('examId', '==', examId)
      .where('studentCode', '==', studentCode)
      .get();
      
    return snap.docs.map(doc => ({ id: doc.id, ...doc.data() } as Assignment));
  }
}
