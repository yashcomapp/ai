import { QuestionItem } from './question.types';
import { ExamAttempt, ProctoringViolations, QuestionDetail, ExamReview } from './attempt.types';

export type { ExamAttempt, ProctoringViolations, QuestionDetail, ExamReview };

export interface Exam {
  id: string;
  name: string;
  duration?: number;
  totalTime?: number;
  examDuration?: number;
  negativeMarks?: number;
  totalMarks?: number;
  subject?: string;
  subjects?: string[];
  subjectName?: string;
  chapter?: string;
  chapterNumber?: string;
  chapterDisplay?: string;
  topicCodes?: string[];
  topicDisplay?: string;
  questionCount?: number;
  questions?: any[];
  questionCodes?: string[];
  questionIds?: string[];
  mode?: string;
  peerReviewStatus?: string;
  batchId?: string | null;
  batchIds?: string[];
  targetBatches?: string[];
  targetStudents?: string[];
  assignedAt?: string | null;
  scheduledDate?: string;
  availableFrom?: string;
  isAssigned?: boolean;
  assigned?: boolean;
  status?: string;
  type?: string;
  class?: string;
  [key: string]: any;
}

export interface Assignment {
  id: string;
  examId: string;
  collection?: string;
  targetType?: string;
  targetBatches?: string[];
  targetStudents?: string[];
  openMode?: string;
  startAt?: string | null;
  endAt?: string | null;
  attemptLimit?: number;
  examDuration?: number;
  examMode?: string;
  classroomDuration?: number;
  classroomTimePerQ?: number;
  lateEntryRestriction?: boolean;
  status?: string;
  studentCode?: string;
  completedAt?: any;
  createdAt?: any;
  [key: string]: any;
}

export interface ExamScheduleStatus {
  state: 'active' | 'closed' | 'upcoming' | 'disabled';
  badgeBg: string;
  badgeColor: string;
  badgeText: string;
}
