import { QuestionItem } from './question.types';
import { ExamAttempt, ProctoringViolations, QuestionDetail, ExamReview } from './attempt.types';

export type { ExamAttempt, ProctoringViolations, QuestionDetail, ExamReview };

export interface Exam {
  id: string;
  name: string;
  duration: number;
  negativeMarks: number;
  totalMarks: number;
  subject?: string;
  chapter?: string;
  questionCodes: string[];
}

export interface SecureExam extends Omit<Exam, 'questionCodes'> {
  questions: Omit<QuestionItem, 'correctAnswer' | 'correctAnswers' | 'solution'>[];
}

export interface Assignment {
  id: string;
  examId: string;
  studentCode: string;
  status: 'pending' | 'completed';
  completedAt?: any;
  createdAt?: any;
}
