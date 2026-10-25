import { Exam, Assignment, ExamScheduleStatus } from './types';
import { getDateKeyIST } from '@/lib/dateUtils';

export function parseDateInput(val: any): Date | null {
  if (!val) return null;
  if (val.seconds) return new Date(val.seconds * 1000);
  const d = new Date(val);
  return isNaN(d.getTime()) ? null : d;
}

export function getNormExamDuration(exam: any, examType: 'objective' | 'subjective'): number {
  if (exam.durationMinutes && !isNaN(Number(exam.durationMinutes))) {
    return Number(exam.durationMinutes);
  }
  if (exam.duration && !isNaN(Number(exam.duration))) {
    return Number(exam.duration);
  }
  return examType === 'subjective' ? 90 : 60;
}

export function getExamSubject(exam: any): string {
  return exam.subjectName || exam.subjects?.[0] || exam.subject || 'General Subject';
}

export function getExamChapter(exam: any): string {
  return exam.chapterDisplay || exam.chapter || exam.chapterName || (exam.chapterNumber ? `Chapter ${exam.chapterNumber}` : 'General / Mixed Chapters');
}

export function getExamClass(exam: any): string {
  if (exam.class) return String(exam.class);
  const parts = (exam.name || '').split('-');
  if (parts.length > 1 && !isNaN(Number(parts[1]))) {
    return parts[1];
  }
  return 'General';
}

export function getExamSortTimestamp(exam: Exam, type: 'objective' | 'subjective', assignments: Assignment[]): number {
  const targetCol = type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments';
  const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === targetCol);
  let examDate: Date | null = null;
  if (activeAssign) {
    const dateVal = activeAssign.startAt || activeAssign.createdAt;
    if (dateVal) {
      examDate = parseDateInput(dateVal);
    }
  } else {
    const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
    if (fallbackDate) {
      examDate = parseDateInput(fallbackDate);
    }
  }
  return examDate && !isNaN(examDate.getTime()) ? examDate.getTime() : 0;
}

export function isTodayOrTomorrow(exam: Exam, type: 'objective' | 'subjective', assignments: Assignment[]): boolean {
  const targetCol = type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments';
  const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === targetCol);
  let examDate: Date | null = null;
  if (activeAssign) {
    const dateVal = activeAssign.startAt || activeAssign.createdAt;
    if (dateVal) {
      examDate = parseDateInput(dateVal);
    }
  } else {
    const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
    if (fallbackDate) {
      examDate = parseDateInput(fallbackDate);
    }
  }
  if (!examDate || isNaN(examDate.getTime())) return false;
  const todayKeyIST = getDateKeyIST(new Date());
  const tomorrowDate = new Date();
  tomorrowDate.setDate(tomorrowDate.getDate() + 1);
  const tomorrowKeyIST = getDateKeyIST(tomorrowDate);
  const examDateKeyIST = getDateKeyIST(examDate);
  return examDateKeyIST === todayKeyIST || examDateKeyIST === tomorrowKeyIST;
}

export function getExamScheduleStatus(
  exam: Exam,
  activeAssign?: Assignment,
  examType: 'objective' | 'subjective' = 'objective'
): ExamScheduleStatus {
  if (activeAssign?.status === 'disabled') {
    return {
      state: 'disabled',
      badgeBg: 'rgba(239, 68, 68, 0.15)',
      badgeColor: 'var(--danger)',
      badgeText: '🛑 Stopped / Disabled'
    };
  }

  const nowMs = Date.now();
  const todayIST = getDateKeyIST(new Date());

  if (activeAssign) {
    const startDate = parseDateInput(activeAssign.startAt || activeAssign.createdAt);
    const endDate = parseDateInput(activeAssign.endAt);

    if (endDate) {
      if (nowMs > endDate.getTime()) {
        return {
          state: 'closed',
          badgeBg: 'rgba(107, 114, 128, 0.15)',
          badgeColor: 'var(--text-muted)',
          badgeText: '🏁 Closed / Over'
        };
      }
      if (startDate && nowMs < startDate.getTime()) {
        return {
          state: 'upcoming',
          badgeBg: 'rgba(245, 158, 11, 0.15)',
          badgeColor: 'var(--warning, #f59e0b)',
          badgeText: '⏳ Upcoming'
        };
      }
      return {
        state: 'active',
        badgeBg: 'rgba(16, 185, 129, 0.15)',
        badgeColor: 'var(--success)',
        badgeText: '🟢 Active / Open'
      };
    }

    if (startDate) {
      const durationMin = activeAssign.examDuration || activeAssign.classroomDuration || getNormExamDuration(exam, examType);
      const calculatedEndMs = startDate.getTime() + (durationMin * 60 * 1000);
      const startKeyIST = getDateKeyIST(startDate);

      if (nowMs < startDate.getTime()) {
        return {
          state: 'upcoming',
          badgeBg: 'rgba(245, 158, 11, 0.15)',
          badgeColor: 'var(--warning, #f59e0b)',
          badgeText: '⏳ Upcoming'
        };
      }

      if (nowMs > calculatedEndMs || startKeyIST < todayIST) {
        return {
          state: 'closed',
          badgeBg: 'rgba(107, 114, 128, 0.15)',
          badgeColor: 'var(--text-muted)',
          badgeText: '🏁 Closed / Over'
        };
      }

      return {
        state: 'active',
        badgeBg: 'rgba(16, 185, 129, 0.15)',
        badgeColor: 'var(--success)',
        badgeText: '🟢 Active / Open'
      };
    }
  }

  const legacyScheduled = exam.scheduledDate || (exam as any).availableFrom;
  if (legacyScheduled) {
    const legDate = parseDateInput(legacyScheduled);
    if (legDate) {
      const legDateKey = getDateKeyIST(legDate);
      if (legDateKey > todayIST) {
        return {
          state: 'upcoming',
          badgeBg: 'rgba(245, 158, 11, 0.15)',
          badgeColor: 'var(--warning, #f59e0b)',
          badgeText: '⏳ Upcoming'
        };
      }
      if (legDateKey < todayIST) {
        return {
          state: 'closed',
          badgeBg: 'rgba(107, 114, 128, 0.15)',
          badgeColor: 'var(--text-muted)',
          badgeText: '🏁 Closed / Over'
        };
      }
      return {
        state: 'active',
        badgeBg: 'rgba(16, 185, 129, 0.15)',
        badgeColor: 'var(--success)',
        badgeText: '🟢 Active / Open'
      };
    }
  }

  return {
    state: 'active',
    badgeBg: 'rgba(16, 185, 129, 0.15)',
    badgeColor: 'var(--success)',
    badgeText: '🟢 Active / Open'
  };
}

export function getGroupedClasses(examsList: Exam[]): string[] {
  const unique = Array.from(new Set(examsList.map(getExamClass)));
  return unique.sort((a, b) => {
    const na = Number(a);
    const nb = Number(b);
    if (isNaN(na) && isNaN(nb)) return a.localeCompare(b);
    if (isNaN(na)) return 1;
    if (isNaN(nb)) return -1;
    return nb - na;
  });
}
