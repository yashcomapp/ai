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
