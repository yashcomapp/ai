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
  assignedAt?: string | null;
  type?: string;
  scheduledDate?: string;
  class?: string;
}

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
