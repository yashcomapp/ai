/**
 * Canonical Scorecard Type Definitions (SSOT).
 */

export interface QuestionDetailsItem {
  id: string;
  questionCode: string;
  qNumber?: number | null;
  text: string;
  type: string;
  options: any[];
  assertion?: string;
  reason?: string;
  solution?: string;
  difficulty: string;
  bloomLevel: string;
  userAnswer: string;
  isCorrect: boolean;
  correctAnswer: string;
  correctAnswers: string[];
  marks?: number;
  timeSpent?: number;
  durationSpent?: number;
  steps?: any[];
  evaluations?: any[];
  subjectCode?: string;
  topicCode?: string;
  chapterNumber?: string | number;
  [key: string]: any;
}

export interface DetailedScorecard {
  id: string;
  examId?: string;
  studentCode?: string;
  examCode: string;
  examName: string;
  examType: string;
  score: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  submittedAt: string | null;
  tabViolations: number;
  proctoringViolations: {
    noFace?: number;
    multipleFaces?: number;
    lookingAway?: number;
    [key: string]: any;
  };
  integrityScore: number;
  status: string;
  wrongAnswerReasons?: string[];
  questions: QuestionDetailsItem[];
  subject?: string;
  chapter?: string;
  topicName?: string;
  topicCode?: string;
  practiceNumber?: number | null;
  violations?: {
    screenshots?: string[];
    [key: string]: any;
  };
  proctoringViolationTriggered?: boolean;
  [key: string]: any;
}
