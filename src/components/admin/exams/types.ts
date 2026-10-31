import { Exam, Assignment, ExamScheduleStatus } from '@/types/exam.types';
import { Batch } from '@/types/batch.types';
import { Student } from '@/types/user.types';

export type { Exam, Assignment, ExamScheduleStatus, Batch, Student };

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

export interface ExamTabCommonProps {
  assignments: Assignment[];
  attemptCounts: { [key: string]: number };
  isTodayOrTomorrow: (exam: Exam, type: 'objective' | 'subjective') => boolean;
  getExamSortTimestamp: (exam: Exam, type: 'objective' | 'subjective') => number;
  getExamClass: (exam: any) => string;
  getExamSubject: (exam: any) => string;
  getExamChapter: (exam: any) => string;
  getAssignedNames: (examId: string, directBatchId?: string | null) => string;
  getLatestAssignmentDate: (examId: string, assignedAt?: string | null, exam?: Exam) => string;
  getExamScheduleStatus: (exam: Exam, activeAssign?: Assignment, examType?: 'objective' | 'subjective') => ExamScheduleStatus;
  isAssignedSectionExpanded?: boolean;
  setIsAssignedSectionExpanded?: React.Dispatch<React.SetStateAction<boolean>>;
  expandedClasses: Set<string>;
  toggleClassExpanded: (clsKey: string) => void;
  expandedSubjects: Set<string>;
  toggleSubjectExpanded: (key: string) => void;
  expandedChapters: Set<string>;
  toggleChapterExpanded: (key: string) => void;
  expandAllAssigned?: (type: 'objective' | 'subjective', list: Exam[]) => void;
  collapseAllAssigned?: (type: 'objective' | 'subjective') => void;
  assignedSortField: 'name' | 'date';
  assignedSortDir: 'asc' | 'desc';
  handleAssignedSort: (field: 'name' | 'date') => void;
  sortAssignedExams: (examsList: Exam[]) => Exam[];
  getGroupedClasses: (examsList: Exam[]) => string[];
  handleOpenAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  handleDeleteExam: (examId: string, examName: string, type: 'objective' | 'subjective') => void;
  toggleAssignmentStatus: (assignmentId: string, collection: string, newStatus: string) => void;
  handleOpenEdit: (examId: string, examName: string, collection: string) => void;
  router: any;
}

export interface ObjectiveTabProps extends ExamTabCommonProps {
  filteredObjectiveExams: Exam[];
  objFilterName: string;
  setObjFilterName: (val: string) => void;
  objFilterTopic: string;
  setObjFilterTopic: (val: string) => void;
}

export interface SubjectiveTabProps extends ExamTabCommonProps {
  filteredSubjectiveExams: Exam[];
  subjFilterName: string;
  setSubjFilterName: (val: string) => void;
  subjFilterTopic: string;
  setSubjFilterTopic: (val: string) => void;
  isSubjectiveAvailableForAssignment: (exam: Exam) => boolean;
  isSubjectiveAlreadyAssigned: (exam: Exam) => boolean;
  triggerPeerReviewLottery?: (examId: string, examName: string) => void;
  openPeerReviewStatus?: (examId: string, examName: string) => void;
  openTruthTestReport?: (examId: string, examName: string) => void;
}

export interface AssignedExamsSectionProps extends ExamTabCommonProps {
  assignedExamsList: Exam[];
  type: 'objective' | 'subjective';
  triggerPeerReviewLottery?: (examId: string, examName: string) => void;
  openPeerReviewStatus?: (examId: string, examName: string) => void;
  openTruthTestReport?: (examId: string, examName: string) => void;
}

export function extractAssignedSectionProps(
  props: ExamTabCommonProps,
  assignedExamsList: Exam[],
  type: 'objective' | 'subjective',
  extra?: {
    triggerPeerReviewLottery?: (examId: string, examName: string) => void;
    openPeerReviewStatus?: (examId: string, examName: string) => void;
    openTruthTestReport?: (examId: string, examName: string) => void;
  }
): AssignedExamsSectionProps {
  return {
    ...props,
    assignedExamsList,
    type,
    ...extra
  };
}

export interface BaseAssignmentModalState {
  show: boolean;
  examId: string;
  examName: string;
  targetType: 'batch' | 'student' | 'mixed';
  selectedBatches: Set<string>;
  selectedStudents: Set<string>;
  openMode: 'immediate' | 'scheduled';
  startAtStr: string;
  endAtStr: string;
  attemptLimit: number;
  examDuration?: number;
  normDuration?: number;
  overrideDuration?: boolean;
  isMorningTest?: boolean;
  isEveningTest?: boolean;
  isTodaySlot?: boolean;
  lateEntryRestriction?: boolean;
  resetAttempts?: boolean;
  startsCount?: number;
}

export interface AssignmentModalCommonProps {
  batches: Batch[];
  getStudentsGroupedByBatch: () => {
    grouped: { [batchId: string]: { batchName: string; list: any[] } };
    unassigned: any[];
  };
  getMorningTestTimes: (dur: number) => { startStr: string; endStr: string };
  getEveningTestTimes: (dur: number) => { startStr: string; endStr: string };
}

export const ASSIGNMENT_MODAL_CARD_STYLE: React.CSSProperties = {
  background: 'var(--surface-popover)',
  borderRadius: 'var(--radius-lg)',
  border: '1px solid var(--border-popover)',
  width: '94%',
  maxHeight: '90vh',
  overflowY: 'auto',
  padding: '20px 24px',
  display: 'flex',
  flexDirection: 'column',
  gap: '16px'
};
