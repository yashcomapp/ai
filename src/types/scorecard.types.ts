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

/**
 * Returns CSS color variable based on mastery or score percentage (SSOT):
 * >= 90: var(--success)
 * >= 50: var(--warning)
 * < 50: var(--danger)
 */
export function getProgressColor(pct: number): string {
  if (pct >= 90) return 'var(--success)';
  if (pct >= 50) return 'var(--warning)';
  return 'var(--danger)';
}

/**
 * Returns score class string for badges (SSOT):
 * < 40: score-low
 * < 75: score-medium
 * >= 75: score-high
 */
export function getScoreClass(pct: number): 'score-low' | 'score-medium' | 'score-high' {
  if (pct < 40) return 'score-low';
  if (pct < 75) return 'score-medium';
  return 'score-high';
}

