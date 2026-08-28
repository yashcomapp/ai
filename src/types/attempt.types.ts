export interface ProctoringViolations {
  noFace: number;
  multipleFaces: number;
  lookingAway: number;
  headMovement: number;
}

export interface QuestionDetail {
  questionCode: string;
  questionText: string;
  userAnswer: string;
  correctAnswer: any;
  isAttempted: boolean;
  isCorrect: boolean;
  timeSpentSeconds: number;
  marks: number;
  keywords?: string[];
}

export interface ExamAttempt {
  id?: string;
  examId: string;
  examName: string;
  subject: string;
  chapter: string;
  studentCode: string;
  studentId: string;
  studentName: string;
  score: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  completedAt: any;
  createdAt: any;
  tabViolations?: number;
  proctoringViolations?: ProctoringViolations;
}

export interface ExamReview {
  id?: string;
  examId: string;
  examName: string;
  subject: string;
  chapter: string;
  studentCode: string;
  studentId: string;
  studentName: string;
  score: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  tabViolations: number;
  proctoringViolations: ProctoringViolations;
  wrongAnswers: { questionText: string; userAnswer: string; correctAnswer: any }[];
  unattemptedQuestions: { questionText: string; correctAnswer: any }[];
  questionDetails: QuestionDetail[];
  startedAt: any;
  completedAt: any;
  status: 'pending' | 'reviewed';
}
