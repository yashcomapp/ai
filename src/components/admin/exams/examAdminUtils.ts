import { Exam, Assignment, ExamScheduleStatus } from './types';
import { getDateKeyIST, parseDateInput } from '@/lib/dateUtils';

export { parseDateInput };

export function getNormExamDuration(exam: any, type: 'objective' | 'subjective' = 'objective'): number {
  if (typeof exam.duration === 'number' && exam.duration > 0) {
    return exam.duration;
  }
  if (typeof exam.totalTime === 'number' && exam.totalTime > 0) {
    return exam.totalTime;
  }
  if (typeof exam.examDuration === 'number' && exam.examDuration > 0) {
    return exam.examDuration;
  }
  if (exam.durationMinutes && !isNaN(Number(exam.durationMinutes))) {
    return Number(exam.durationMinutes);
  }

  const questions = Array.isArray(exam.questions) ? exam.questions : [];
  const questionCodes = Array.isArray(exam.questionCodes) ? exam.questionCodes : [];

  if (questions.length > 0) {
    let textualCount = 0;
    let numericalCount = 0;
    questions.forEach((q: any) => {
      const code = String(q?.questionCode || q?.code || q?.id || '');
      const qType = String(q?.type || q?.questionType || '').toLowerCase();
      const isNum = code.includes('-ONE-') || code.includes('-SSN-') || code.includes('-SLN-') ||
                    qType.includes('numerical') || qType.includes('calculation') || qType === 'one';
      if (isNum) {
        numericalCount++;
      } else {
        textualCount++;
      }
    });
    if (type === 'subjective') {
      return Math.max(15, (textualCount * 3) + (numericalCount * 5));
    }
    return Math.max(1, (textualCount * 1) + (numericalCount * 2));
  }

  if (questionCodes.length > 0) {
    let textualCount = 0;
    let numericalCount = 0;
    questionCodes.forEach((codeStr: string) => {
      const code = String(codeStr || '');
      const isNum = code.includes('-ONE-') || code.includes('-SSN-') || code.includes('-SLN-');
      if (isNum) {
        numericalCount++;
      } else {
        textualCount++;
      }
    });
    if (type === 'subjective') {
      return Math.max(15, (textualCount * 3) + (numericalCount * 5));
    }
    return Math.max(1, (textualCount * 1) + (numericalCount * 2));
  }

  if (typeof exam.questionCount === 'number' && exam.questionCount > 0) {
    return type === 'subjective' ? Math.max(15, exam.questionCount * 5) : Math.max(1, exam.questionCount * 1);
  }

  return type === 'subjective' ? 60 : 30;
}

export function getExamSubject(exam: any): string {
  return exam.subjectName || exam.subjects?.[0] || exam.subject || 'General Subject';
}

export function getExamChapter(exam: any): string {
  return exam.chapterDisplay || exam.chapter || exam.chapterName || (exam.chapterNumber ? `Chapter ${exam.chapterNumber}` : 'General / Mixed Chapters');
}

export function getExamClass(exam: any, assignments?: Assignment[], batches?: any[]): string {
  if (!exam) return 'General';
  const assigns = Array.isArray(assignments) ? assignments : undefined;
  const batchList = Array.isArray(batches) ? batches : undefined;

  // 1. Direct properties on exam
  if (exam.class) {
    const m = String(exam.class).match(/\d+/);
    if (m) return m[0];
    return String(exam.class);
  }
  if (exam.targetClass) {
    const m = String(exam.targetClass).match(/\d+/);
    if (m) return m[0];
  }
  if (exam.className) {
    const m = String(exam.className).match(/\d+/);
    if (m) return m[0];
  }

  // 2. Exam name patterns like '024-MH-8-...', 'MH-8-...', 'CBSE-10-...'
  const name = String(exam.name || '');
  const boardClassMatch = name.match(/(?:CBSE|MH|ICSE|STATE)[-_](\d+)/i);
  if (boardClassMatch) {
    return boardClassMatch[1];
  }

  // 3. Class word in exam name: 'Class 8', 'Std 9', etc.
  const classWordMatch = name.match(/(?:Class|Std|Standard)\s*(\d+)/i);
  if (classWordMatch) {
    return classWordMatch[1];
  }

  // 4. Topic codes on exam (e.g. ['MH-8-SCI-5-5.2'])
  if (Array.isArray(exam.topicCodes) && exam.topicCodes.length > 0) {
    for (const tc of exam.topicCodes) {
      const tcMatch = String(tc).match(/(?:CBSE|MH|ICSE|STATE)[-_](\d+)/i);
      if (tcMatch) return tcMatch[1];
    }
  }

  // 5. Look up assigned batches if batches list provided
  if (batchList && batchList.length > 0) {
    const targetBatchIds: string[] = [];
    if (assigns && assigns.length > 0) {
      const examAssigns = assigns.filter(a => a.examId === exam.id);
      examAssigns.forEach(a => {
        if (Array.isArray(a.targetBatches)) {
          targetBatchIds.push(...a.targetBatches);
        }
      });
    }
    if (exam.batchId) {
      targetBatchIds.push(exam.batchId);
    }
    if (Array.isArray(exam.batchIds)) {
      targetBatchIds.push(...exam.batchIds);
    }
    if (Array.isArray(exam.targetBatches)) {
      targetBatchIds.push(...exam.targetBatches);
    }
    for (const bid of targetBatchIds) {
      const b = batchList.find(x => x.id === bid);
      if (b && b.name) {
        const m = String(b.name).match(/(?:Class|Std|Standard)\s*(\d+)/i) || String(b.name).match(/\b(\d{1,2})(?:th|st|nd|rd)?\b/i);
        if (m) return m[1];
      }
    }
  }

  // 6. Name parts fallback
  const parts = name.split('-');
  if (parts.length > 1 && !isNaN(Number(parts[1]))) {
    return parts[1];
  }
  if (parts.length > 2 && !isNaN(Number(parts[2]))) {
    return parts[2];
  }

  return 'General';
}

export function getClassBadgeStyle(cls: string): { bg: string; color: string; border: string } {
  switch (cls) {
    case '8':
      return {
        bg: 'rgba(14, 165, 233, 0.16)',
        color: '#38bdf8',
        border: 'rgba(14, 165, 233, 0.4)'
      };
    case '9':
      return {
        bg: 'rgba(168, 85, 247, 0.16)',
        color: '#c084fc',
        border: 'rgba(168, 85, 247, 0.4)'
      };
    case '10':
      return {
        bg: 'rgba(245, 158, 11, 0.16)',
        color: '#fbbf24',
        border: 'rgba(245, 158, 11, 0.4)'
      };
    case '11':
      return {
        bg: 'rgba(236, 72, 153, 0.16)',
        color: '#f472b6',
        border: 'rgba(236, 72, 153, 0.4)'
      };
    case '12':
      return {
        bg: 'rgba(239, 68, 68, 0.16)',
        color: '#f87171',
        border: 'rgba(239, 68, 68, 0.4)'
      };
    default:
      return {
        bg: 'rgba(59, 130, 246, 0.16)',
        color: '#60a5fa',
        border: 'rgba(59, 130, 246, 0.4)'
      };
  }
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
          badgeText: '🏁 Closed'
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
        badgeText: '🟢 Active'
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
          badgeText: '🏁 Closed'
        };
      }

      return {
        state: 'active',
        badgeBg: 'rgba(16, 185, 129, 0.15)',
        badgeColor: 'var(--success)',
        badgeText: '🟢 Active'
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
          badgeText: '🏁 Closed'
        };
      }
      return {
        state: 'active',
        badgeBg: 'rgba(16, 185, 129, 0.15)',
        badgeColor: 'var(--success)',
        badgeText: '🟢 Active'
      };
    }
  }

  return {
    state: 'active',
    badgeBg: 'rgba(16, 185, 129, 0.15)',
    badgeColor: 'var(--success)',
    badgeText: '🟢 Active'
  };
}

export function getGroupedClasses(examsList: Exam[]): string[] {
  const unique = Array.from(new Set(examsList.map(exam => getExamClass(exam))));
  return unique.sort((a, b) => {
    const na = Number(a);
    const nb = Number(b);
    if (isNaN(na) && isNaN(nb)) return a.localeCompare(b);
    if (isNaN(na)) return 1;
    if (isNaN(nb)) return -1;
    return nb - na;
  });
}
