export interface Exam {
  id: string;
  name: string;
  subjects?: string[];
  subjectName?: string;
  chapterNumber?: string;
  chapter?: string;
  chapterDisplay?: string;
  topicCodes?: string[];
  topicDisplay?: string;
  questionCount?: number;
  questions?: any[];
  questionCodes?: string[];
  questionIds?: string[];
  duration?: number;
  totalTime?: number;
  examDuration?: number;
  totalMarks?: number;
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
}

export const isExamAssigned = (
  exam: Exam,
  assignments: Assignment[] = [],
  attemptCounts?: { [key: string]: number }
): boolean => {
  if (exam.batchId) return true;
  if (Array.isArray(exam.batchIds) && exam.batchIds.length > 0) return true;
  if (Array.isArray(exam.targetBatches) && exam.targetBatches.length > 0) return true;
  if (Array.isArray(exam.targetStudents) && exam.targetStudents.length > 0) return true;
  if (assignments.some(a => a.examId === exam.id)) return true;
  if (exam.scheduledDate || exam.assignedAt || exam.availableFrom) return true;
  if (exam.assigned === true || exam.isAssigned === true || exam.status === 'assigned') return true;
  if (attemptCounts && (attemptCounts[exam.id] || 0) > 0) return true;
  return false;
};

export interface Batch {
  id: string;
  name: string;
}

export interface Student {
  studentCode: string;
  name: string;
  rollNumber: string;
  batchIds: string[];
  batchId: string | null;
}

export interface Assignment {
  id: string;
  examId: string;
  collection: string;
  targetType: string;
  targetBatches: string[];
  targetStudents: string[];
  openMode: string;
  startAt: string | null;
  endAt: string | null;
  attemptLimit: number;
  examDuration?: number;
  examMode?: string;
  classroomDuration?: number;
  classroomTimePerQ?: number;
  lateEntryRestriction?: boolean;
  status?: string;
  createdAt: string | null;
}

export interface ExamScheduleStatus {
  state: 'active' | 'closed' | 'upcoming' | 'disabled';
  badgeBg: string;
  badgeColor: string;
  badgeText: string;
}
