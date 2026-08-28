import * as admin from 'firebase-admin';
import { AttemptService } from './attempt.service';
import { ProctoringViolations } from '@/types/attempt.types';

export class ExamService {
  /**
   * Delegates MCQ exam submission evaluation to AttemptService.
   */
  static async submitExam(params: {
    studentCode: string;
    studentId: string;
    studentName: string;
    examId: string;
    examData: any;
    questions: any[];
    userAnswers: any[];
    durationSpent: number;
    tabViolations: number;
    proctoringViolations: ProctoringViolations;
    startedAt: string | null;
    assignmentsSnap: admin.firestore.QuerySnapshot | null;
    proctoringViolationTriggered?: boolean;
    micBypassed?: boolean;
    violations?: any;
    abandoned?: boolean;
    disputedQuestionIds?: string[];
  }) {
    return AttemptService.submitAttempt(params);
  }
}
