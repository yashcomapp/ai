'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import dynamic from 'next/dynamic';
const ScorecardModal = dynamic(() => import('@/components/ScorecardModal'), { ssr: false });
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
const AssignExamModal = dynamic(() => import('@/components/admin/exams/AssignExamModal'), { ssr: false });
const EditAssignmentModal = dynamic(() => import('@/components/admin/exams/EditAssignmentModal'), { ssr: false });
const PeerReviewModal = dynamic(() => import('@/components/admin/exams/PeerReviewModal'), { ssr: false });
const TruthTestModal = dynamic(() => import('@/components/admin/exams/TruthTestModal'), { ssr: false });
const PracticeHistoryModal = dynamic(() => import('@/components/admin/exams/PracticeHistoryModal'), { ssr: false });
const TopicStatusBreakdownModal = dynamic(() => import('@/components/admin/exams/TopicStatusBreakdownModal'), { ssr: false });
import { useMathRender } from '@/hooks/useMathRender';
import { useScorecard } from '@/hooks/useScorecard';
import { exportUniversalExamPDF } from '@/lib/pdfExport';
import { toISTDateTimeLocalInput, formatDateDMY, parseDateInput, getDateKeyIST, formatDateTimeIST } from '@/lib/dateUtils';
import ObjectiveTab from '@/components/admin/exams/ObjectiveTab';
import SubjectiveTab from '@/components/admin/exams/SubjectiveTab';
import PracticeTab from '@/components/admin/exams/PracticeTab';
import { isExamAssigned } from '@/components/admin/exams/types';

interface Exam {
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
}

function getNormExamDuration(exam: Exam, type: 'objective' | 'subjective' = 'objective'): number {
  if (typeof exam.duration === 'number' && exam.duration > 0) {
    return exam.duration;
  }
  if (typeof exam.totalTime === 'number' && exam.totalTime > 0) {
    return exam.totalTime;
  }
  if (typeof exam.examDuration === 'number' && exam.examDuration > 0) {
    return exam.examDuration;
  }

  // Calculate from questions if available
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

interface ExamScheduleStatus {
  state: 'active' | 'closed' | 'upcoming' | 'disabled';
  badgeBg: string;
  badgeColor: string;
  badgeText: string;
}

function getExamScheduleStatus(
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

      // If scheduled time window has elapsed or the scheduled assignment date is in the past
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

  // Fallback when activeAssign is not present but exam has scheduledDate or assignedAt
  if (exam.scheduledDate) {
    if (exam.scheduledDate < todayIST) {
      return {
        state: 'closed',
        badgeBg: 'rgba(107, 114, 128, 0.15)',
        badgeColor: 'var(--text-muted)',
        badgeText: '🏁 Closed / Over'
      };
    }
    if (exam.scheduledDate > todayIST) {
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

  if (exam.assignedAt) {
    const assignedDate = parseDateInput(exam.assignedAt);
    if (assignedDate) {
      const assignedDateKey = getDateKeyIST(assignedDate);
      if (assignedDateKey < todayIST) {
        return {
          state: 'closed',
          badgeBg: 'rgba(107, 114, 128, 0.15)',
          badgeColor: 'var(--text-muted)',
          badgeText: '🏁 Closed / Over'
        };
      }
      if (assignedDateKey > todayIST) {
        return {
          state: 'upcoming',
          badgeBg: 'rgba(245, 158, 11, 0.15)',
          badgeColor: 'var(--warning, #f59e0b)',
          badgeText: '⏳ Upcoming'
        };
      }
    }
  }

  return {
    state: 'active',
    badgeBg: 'rgba(16, 185, 129, 0.15)',
    badgeColor: 'var(--success)',
    badgeText: '🟢 Active / Open'
  };
}

interface Batch {
  id: string;
  name: string;
}

interface Student {
  studentCode: string;
  name: string;
  rollNumber: string;
  batchIds: string[];
  batchId: string | null;
}

interface Assignment {
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

export default function AdminExamsPage() {
  const { firebaseUser, logout } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();
  const assignExamId = searchParams?.get('assign') || null;
  const assignSubjExamId = searchParams?.get('assignSubj') || null;
  const handledAssignRef = React.useRef<string | null>(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [activeTab, setActiveTab] = useState<'objective' | 'subjective' | 'practice'>('objective');

  // Master lists
  const [exams, setExams] = useState<Exam[]>([]);
  const [subjectiveExams, setSubjectiveExams] = useState<Exam[]>([]);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [students, setStudents] = useState<Student[]>([]);
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [attemptCounts, setAttemptCounts] = useState<{ [key: string]: number }>({});
  const [practiceStats, setPracticeStats] = useState<{
    [studentCode: string]: {
      totalSessions: number;
      questionsAttempted: number;
      avgScore: number;
      lastActive: string | null;
    }
  }>({});
  const [masteryStats, setMasteryStats] = useState<{
    [studentCode: string]: {
      avgMastery: number;
      avgQuality?: number;
      mastered: number;
      practicing: number;
      needsAttention: number;
    }
  }>({});
  const [loadingPracticeTracks, setLoadingPracticeTracks] = useState(false);
  const [practiceTracksLoaded, setPracticeTracksLoaded] = useState(false);

  // Filtering states
  const [objFilterName, setObjFilterName] = useState('');
  const [objFilterTopic, setObjFilterTopic] = useState('');
  const [subjFilterName, setSubjFilterName] = useState('');
  const [subjFilterTopic, setSubjFilterTopic] = useState('');

  const isSubjectiveAvailableForAssignment = (exam: Exam) => {
    if (exam.type === 'home_practice') return false;
    return !isExamAssigned(exam, assignments, attemptCounts);
  };

  const isSubjectiveAlreadyAssigned = (exam: Exam) => {
    return isExamAssigned(exam, assignments, attemptCounts);
  };

  // Already Assigned sorting states & helpers
  const [assignedSortField, setAssignedSortField] = useState<'name' | 'date'>('date');
  const [assignedSortDir, setAssignedSortDir] = useState<'asc' | 'desc'>('desc');
  const [expandedClasses, setExpandedClasses] = useState<Set<string>>(new Set());
  const [expandedSubjects, setExpandedSubjects] = useState<Set<string>>(new Set());
  const [expandedChapters, setExpandedChapters] = useState<Set<string>>(new Set());
  const [isObjAssignedSectionExpanded, setIsObjAssignedSectionExpanded] = useState(false);
  const [isSubjAssignedSectionExpanded, setIsSubjAssignedSectionExpanded] = useState(false);
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  const toggleClassExpanded = (clsKey: string) => {
    setExpandedClasses(prev => {
      const next = new Set(prev);
      if (next.has(clsKey)) next.delete(clsKey);
      else next.add(clsKey);
      return next;
    });
  };

  const toggleSubjectExpanded = (key: string) => {
    setExpandedSubjects(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const toggleChapterExpanded = (key: string) => {
    setExpandedChapters(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const expandAllAssigned = (type: 'objective' | 'subjective', examsList: Exam[]) => {
    const nextClasses = new Set(expandedClasses);
    const nextSubjects = new Set(expandedSubjects);
    const nextChapters = new Set(expandedChapters);

    const classes = getGroupedClasses(examsList);
    classes.forEach(cls => {
      nextClasses.add(`${type}||${cls}`);
      const examsInClass = examsList.filter(exam => getExamClass(exam) === cls);
      examsInClass.forEach(exam => {
        const subj = getExamSubject(exam);
        const chap = getExamChapter(exam);
        nextSubjects.add(`subj||${type}||${cls}||${subj}`);
        nextChapters.add(`chap||${type}||${cls}||${subj}||${chap}`);
      });
    });

    setExpandedClasses(nextClasses);
    setExpandedSubjects(nextSubjects);
    setExpandedChapters(nextChapters);
  };

  const collapseAllAssigned = (type: 'objective' | 'subjective') => {
    setExpandedClasses(prev => {
      const next = new Set(prev);
      Array.from(next).forEach(k => { if (k.startsWith(`${type}||`)) next.delete(k); });
      return next;
    });
    setExpandedSubjects(prev => {
      const next = new Set(prev);
      Array.from(next).forEach(k => { if (k.startsWith(`subj||${type}||`)) next.delete(k); });
      return next;
    });
    setExpandedChapters(prev => {
      const next = new Set(prev);
      Array.from(next).forEach(k => { if (k.startsWith(`chap||${type}||`)) next.delete(k); });
      return next;
    });
  };

  const getExamSubject = (exam: any) => {
    return exam.subjectName || exam.subjects?.[0] || exam.subject || 'General Subject';
  };

  const getExamChapter = (exam: any) => {
    return exam.chapterDisplay || exam.chapter || exam.chapterName || (exam.chapterNumber ? `Chapter ${exam.chapterNumber}` : 'General / Mixed Chapters');
  };

  const getExamClass = (exam: any) => {
    if (exam.class) return exam.class;
    const parts = exam.name.split('-');
    if (parts.length > 1 && !isNaN(Number(parts[1]))) {
      return parts[1];
    }
    return 'General';
  };

  const getLatestAssignmentDateMs = (examId: string, exam?: Exam) => {
    const list = assignments.filter(a => a.examId === examId);
    if (list.length === 0) {
      if (exam) {
        const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
        if (fallbackDate) return new Date(fallbackDate).getTime();
      }
      return 0;
    }
    const dates = list.map(a => {
      const d = a.startAt ? new Date(a.startAt) : (a.createdAt ? new Date(a.createdAt) : new Date(0));
      return d.getTime();
    });
    return Math.max(...dates);
  };

  const handleAssignedSort = (field: 'name' | 'date') => {
    if (assignedSortField === field) {
      setAssignedSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setAssignedSortField(field);
      setAssignedSortDir('desc');
    }
  };

  const sortAssignedExams = (examsList: Exam[]) => {
    return [...examsList].sort((a, b) => {
      if (assignedSortField === 'name') {
        return assignedSortDir === 'asc' 
          ? a.name.localeCompare(b.name)
          : b.name.localeCompare(a.name);
      } else {
        const da = getLatestAssignmentDateMs(a.id, a);
        const db = getLatestAssignmentDateMs(b.id, b);
        return assignedSortDir === 'asc' ? da - db : db - da;
      }
    });
  };

  const getGroupedClasses = (examsList: Exam[]) => {
    const unique = Array.from(new Set(examsList.map(getExamClass)));
    return unique.sort((a, b) => {
      const na = Number(a);
      const nb = Number(b);
      if (isNaN(na) && isNaN(nb)) return a.localeCompare(b);
      if (isNaN(na)) return 1;
      if (isNaN(nb)) return -1;
      return nb - na;
    });
  };

  const getExamSortTimestamp = (exam: Exam, type: 'objective' | 'subjective') => {
    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === (type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments'));
    let examDate: Date | null = null;
    if (activeAssign) {
      const dateVal = activeAssign.startAt || activeAssign.createdAt;
      if (dateVal) {
        const dateAny = dateVal as any;
        examDate = dateAny.seconds ? new Date(dateAny.seconds * 1000) : new Date(dateVal);
      }
    } else {
      const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
      if (fallbackDate) {
        examDate = new Date(fallbackDate);
      }
    }
    return examDate && !isNaN(examDate.getTime()) ? examDate.getTime() : 0;
  };

  const isTodayOrTomorrow = (exam: Exam, type: 'objective' | 'subjective') => {
    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === (type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments'));
    let examDate: Date | null = null;
    if (activeAssign) {
      const dateVal = activeAssign.startAt || activeAssign.createdAt;
      if (dateVal) {
        const dateAny = dateVal as any;
        examDate = dateAny.seconds ? new Date(dateAny.seconds * 1000) : new Date(dateVal);
      }
    } else {
      const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
      if (fallbackDate) {
        examDate = new Date(fallbackDate);
      }
    }
    if (!examDate || isNaN(examDate.getTime())) return false;
    const todayKeyIST = getDateKeyIST(new Date());
    const tomorrowDate = new Date();
    tomorrowDate.setDate(tomorrowDate.getDate() + 1);
    const tomorrowKeyIST = getDateKeyIST(tomorrowDate);
    const examDateKeyIST = getDateKeyIST(examDate);
    return examDateKeyIST === todayKeyIST || examDateKeyIST === tomorrowKeyIST;
  };

  const getExamAssignedDateTime = (exam: Exam, type: 'objective' | 'subjective') => {
    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === (type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments'));
    let examDate: Date | null = null;
    if (activeAssign) {
      const dateVal = activeAssign.startAt || activeAssign.createdAt;
      if (dateVal) {
        const dateAny = dateVal as any;
        examDate = dateAny.seconds ? new Date(dateAny.seconds * 1000) : new Date(dateVal);
      }
    } else {
      const fallbackDate = exam.scheduledDate || exam.assignedAt || (exam as any).availableFrom;
      if (fallbackDate) {
        examDate = new Date(fallbackDate);
      }
    }
    if (!examDate || isNaN(examDate.getTime())) {
      return { dateStr: '—', timeStr: '—' };
    }
    return {
      dateStr: formatDateDMY(examDate),
      timeStr: examDate.toLocaleTimeString('en-IN', { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit' })
    };
  };

  // Practice filter & sort state
  const [pracBatchFilter, setPracBatchFilter] = useState('all');
  const [pracSearchName, setPracSearchName] = useState('');
  const [pracSortField, setPracSortField] = useState<string | null>(null);
  const [pracSortDir, setPracSortDir] = useState<'asc' | 'desc'>('asc');

  // Modals active states
  const [assignModal, setAssignModal] = useState<{
    show: boolean;
    type: 'objective' | 'subjective';
    examId: string;
    examName: string;
    // Form fields
    targetType: 'batch' | 'student' | 'mixed';
    selectedBatches: Set<string>;
    selectedStudents: Set<string>;
    openMode: 'immediate' | 'scheduled' | 'fixed-slot';
    startAtStr: string;
    endAtStr: string;
    attemptLimit: number;
    lateEntryRestriction: boolean;
    // Objective specifics
    normDuration: number;
    overrideDuration: boolean;
    examDuration: number;
    // Subjective specifics
    examMode: 'home' | 'classroom';
    classroomDuration: number;
    classroomTimePerQ: number;
    isMorningTest?: boolean;
    isEveningTest?: boolean;
  }>({
    show: false,
    type: 'objective',
    examId: '',
    examName: '',
    targetType: 'batch',
    selectedBatches: new Set(),
    selectedStudents: new Set(),
    openMode: 'immediate',
    startAtStr: '',
    endAtStr: '',
    attemptLimit: 1,
    lateEntryRestriction: false,
    normDuration: 30,
    overrideDuration: false,
    examDuration: 30,
    examMode: 'home',
    classroomDuration: 60,
    classroomTimePerQ: 5,
    isMorningTest: false,
    isEveningTest: false
  });

  const [assigning, setAssigning] = useState(false);

  const [editModal, setEditModal] = useState<{
    show: boolean;
    id: string;
    collection: string;
    examName: string;
    targetType: 'batch' | 'student' | 'mixed';
    selectedBatches: Set<string>;
    selectedStudents: Set<string>;
    openMode: 'immediate' | 'scheduled' | 'fixed-slot';
    startAtStr: string;
    endAtStr: string;
    attemptLimit: number;
    normDuration: number;
    overrideDuration: boolean;
    examDuration: number;
    lateEntryRestriction: boolean;
    isMorningTest?: boolean;
    isEveningTest?: boolean;
  }>({
    show: false,
    id: '',
    collection: '',
    examName: '',
    targetType: 'batch',
    selectedBatches: new Set(),
    selectedStudents: new Set(),
    openMode: 'immediate',
    startAtStr: '',
    endAtStr: '',
    attemptLimit: 1,
    normDuration: 30,
    overrideDuration: false,
    examDuration: 30,
    lateEntryRestriction: false,
    isMorningTest: false,
    isEveningTest: false
  });

  const [lotteryModal, setLotteryModal] = useState<{
    show: boolean;
    examId: string;
    examName: string;
    loading: boolean;
    statusData: any;
  }>({
    show: false,
    examId: '',
    examName: '',
    loading: false,
    statusData: null
  });

  const [truthTestModal, setTruthTestModal] = useState<{
    show: boolean;
    examId: string;
    examName: string;
    loading: boolean;
    data: any;
  }>({
    show: false,
    examId: '',
    examName: '',
    loading: false,
    data: null
  });

  const [truthSearchText, setTruthSearchText] = useState('');

  const [selectedPracStudent, setSelectedPracStudent] = useState<Student | null>(null);
  const [pracHistory, setPracHistory] = useState<any[]>([]);
  const [loadingPracHistory, setLoadingPracHistory] = useState(false);

  // Accordion inside Practice History modal
  const [modalExpandedSubjects, setModalExpandedSubjects] = useState<Set<string>>(new Set());
  const [modalExpandedChapters, setModalExpandedChapters] = useState<Set<string>>(new Set());
  const [modalSortKey, setModalSortKey] = useState<'name' | 'score' | 'date' | 'integrity'>('date');
  const [modalSortDirection, setModalSortDirection] = useState<'asc' | 'desc'>('desc');

  const handleModalSort = (key: 'name' | 'score' | 'date' | 'integrity') => {
    if (modalSortKey === key) {
      setModalSortDirection(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setModalSortKey(key);
      setModalSortDirection(key === 'name' ? 'asc' : 'desc');
    }
  };

  // Scorecard modal state
  const [selectedScorecardId, setSelectedScorecardId] = useState<string | null>(null);
  const { scorecard: scorecardData, loading: scorecardLoading, loadScorecard: fetchScorecard, setScorecard: setScorecardData } = useScorecard();

  const [topicStatusModal, setTopicStatusModal] = useState<{
    show: boolean;
    student: Student | null;
    initialTab: 'all' | 'mastered' | 'practicing' | 'needsAttention';
    activeTab: 'all' | 'mastered' | 'practicing' | 'needsAttention';
    loading: boolean;
    searchText: string;
    data: {
      mastered: any[];
      practicing: any[];
      needsAttention: any[];
      stats: { masteredCount: number; practicingCount: number; needsAttentionCount: number };
    } | null;
  }>({
    show: false,
    student: null,
    initialTab: 'all',
    activeTab: 'all',
    loading: false,
    searchText: '',
    data: null
  });

  const deferredPracSearchName = useDeferredValue(pracSearchName);

  const filteredPracticeBatches = useMemo(() => {
    const q = deferredPracSearchName.toLowerCase().trim();
    const activeBatches = batches.filter(b => pracBatchFilter === 'all' || b.id === pracBatchFilter);

    return activeBatches.map(batch => {
      const batchStudents = students.filter(s => {
        if (!s.batchIds || !s.batchIds.includes(batch.id)) return false;
        if (q && !s.name.toLowerCase().includes(q)) return false;
        return true;
      });

      const sortedStudents = [...batchStudents].sort((a, b) => {
        const statsA = practiceStats[a.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
        const statsB = practiceStats[b.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
        const masteryA = masteryStats[a.studentCode] || { avgMastery: 0, mastered: 0, practicing: 0, needsAttention: 0 };
        const masteryB = masteryStats[b.studentCode] || { avgMastery: 0, mastered: 0, practicing: 0, needsAttention: 0 };
        
        let valA: any = '';
        let valB: any = '';

        if (pracSortField === 'student') {
          valA = a.name.toLowerCase();
          valB = b.name.toLowerCase();
        } else if (pracSortField === 'code') {
          valA = a.studentCode;
          valB = b.studentCode;
        } else if (pracSortField === 'sessions') {
          valA = statsA.totalSessions;
          valB = statsB.totalSessions;
        } else if (pracSortField === 'questions') {
          valA = statsA.questionsAttempted;
          valB = statsB.questionsAttempted;
        } else if (pracSortField === 'score') {
          valA = statsA.avgScore;
          valB = statsB.avgScore;
        } else if (pracSortField === 'avgMastery') {
          valA = masteryA.avgMastery;
          valB = masteryB.avgMastery;
        } else if (pracSortField === 'avgQuality') {
          valA = (masteryA as any).avgQuality ?? 100;
          valB = (masteryB as any).avgQuality ?? 100;
        } else if (pracSortField === 'masteryStats') {
          valA = masteryA.mastered;
          valB = masteryB.mastered;
        } else if (pracSortField === 'active') {
          valA = statsA.lastActive ? new Date(statsA.lastActive).getTime() : 0;
          valB = statsB.lastActive ? new Date(statsB.lastActive).getTime() : 0;
        } else {
          return 0;
        }

        if (valA < valB) return pracSortDir === 'asc' ? -1 : 1;
        if (valA > valB) return pracSortDir === 'asc' ? 1 : -1;
        return 0;
      });

      return {
        batch,
        batchStudents,
        sortedStudents
      };
    }).filter(item => !q || item.sortedStudents.length > 0);
  }, [batches, pracBatchFilter, students, deferredPracSearchName, practiceStats, masteryStats, pracSortField, pracSortDir]);

  const openTopicStatusModal = async (student: Student, filterType: 'mastered' | 'practicing' | 'needsAttention' | 'all', e: React.MouseEvent) => {
    e.stopPropagation();
    setTopicStatusModal({
      show: true,
      student,
      initialTab: filterType,
      activeTab: filterType,
      loading: true,
      searchText: '',
      data: null
    });

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/exams?action=studentTopicStatus&studentCode=${student.studentCode}`, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) throw new Error('Failed to load student topic status breakdown');
      const json = await res.json();
      setTopicStatusModal(prev => ({
        ...prev,
        loading: false,
        data: json
      }));
    } catch (err: any) {
      console.error('Error loading student topic status:', err);
      setTopicStatusModal(prev => ({ ...prev, loading: false }));
    }
  };

  // Dynamically load KaTeX and auto-render math expressions
  useMathRender([selectedScorecardId, scorecardData, truthTestModal]);

  const loadScorecard = async (id: string, studentCode: string) => {
    setSelectedScorecardId(id);
    try {
      await fetchScorecard(id, studentCode);
    } catch (err) {
      setSelectedScorecardId(null);
    }
  };

  const loadData = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    setError('');
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load exams configuration data.');
      }
      const data = await res.json();
      const fetchedExams: Exam[] = data.exams || [];
      const fetchedSubjExams: Exam[] = data.subjectiveExams || [];
      setExams(fetchedExams);
      setSubjectiveExams(fetchedSubjExams);
      setBatches(data.batches || []);
      setStudents(data.students || []);
      setAssignments(data.assignments || []);
      setAttemptCounts(data.attemptCounts || {});

      // Auto-open assign modal if redirected with assign or assignSubj param
      if (assignExamId && handledAssignRef.current !== assignExamId) {
        const target = fetchedExams.find(e => e.id === assignExamId || e.name === assignExamId);
        if (target) {
          handledAssignRef.current = assignExamId;
          setActiveTab('objective');
          handleOpenAssign(target, 'objective');
        }
      } else if (assignSubjExamId && handledAssignRef.current !== assignSubjExamId) {
        const target = fetchedSubjExams.find(e => e.id === assignSubjExamId || e.name === assignSubjExamId);
        if (target) {
          handledAssignRef.current = assignSubjExamId;
          setActiveTab('subjective');
          handleOpenAssign(target, 'subjective');
        }
      }
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred loading data.');
    } finally {
      setLoading(false);
    }
  };

  const loadPracticeTracks = async () => {
    if (!firebaseUser) return;
    setLoadingPracticeTracks(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams?action=practiceTracks', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load practice tracks data.');
      }
      const data = await res.json();
      setPracticeStats(data.practiceStats || {});
      setMasteryStats(data.masteryStats || {});
      setPracticeTracksLoaded(true);
    } catch (err: any) {
      console.error('Failed to load practice tracks:', err);
    } finally {
      setLoadingPracticeTracks(false);
    }
  };

  const toggleAssignmentStatus = async (id: string, collection: string, newStatus: string) => {
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/exams', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ id, collection, status: newStatus })
      });
      if (res.ok) {
        alert(`Exam ${newStatus === 'active' ? 'enabled' : 'stopped'} successfully!`);
        await loadData();
      } else {
        const err = await res.json();
        throw new Error(err.message || 'Failed to update exam status.');
      }
    } catch (err: any) {
      alert(err.message);
    }
  };

  const handlePracSort = (field: string) => {
    if (pracSortField === field) {
      setPracSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setPracSortField(field);
      setPracSortDir('asc');
    }
  };

  const handleRowClick = async (student: Student) => {
    if (!firebaseUser) return;
    setSelectedPracStudent(student);
    setLoadingPracHistory(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/parent/review?studentCode=${student.studentCode}`, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        const history = data.practiceReviews || [];
        setPracHistory(history);

        const firstSub = history.map((h: any) => h.subject).filter(Boolean)[0];
        if (firstSub) {
          setModalExpandedSubjects(new Set([firstSub]));
        } else {
          setModalExpandedSubjects(new Set());
        }
        setModalExpandedChapters(new Set());
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoadingPracHistory(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadData();
    }
  }, [firebaseUser]);

  useEffect(() => {
    if (activeTab === 'practice' && !practiceTracksLoaded && !loadingPracticeTracks && firebaseUser) {
      loadPracticeTracks();
    }
  }, [activeTab, practiceTracksLoaded, loadingPracticeTracks, firebaseUser]);

  useEffect(() => {
    if (!loading) {
      if (assignExamId && handledAssignRef.current !== assignExamId && exams.length > 0) {
        const target = exams.find(e => e.id === assignExamId || e.name === assignExamId);
        if (target) {
          handledAssignRef.current = assignExamId;
          setActiveTab('objective');
          handleOpenAssign(target, 'objective');
        }
      } else if (assignSubjExamId && handledAssignRef.current !== assignSubjExamId && subjectiveExams.length > 0) {
        const target = subjectiveExams.find(e => e.id === assignSubjExamId || e.name === assignSubjExamId);
        if (target) {
          handledAssignRef.current = assignSubjExamId;
          setActiveTab('subjective');
          handleOpenAssign(target, 'subjective');
        }
      }
    }
  }, [assignExamId, assignSubjExamId, exams, subjectiveExams, loading]);



  // Helpers for assignments mapping
  const getAssignedNames = (examId: string, examBatchId?: string | null) => {
    const list = assignments.filter(a => a.examId === examId);
    if (list.length === 0) {
      if (examBatchId) {
        const b = batches.find(x => x.id === examBatchId);
        return `Batches: ${b ? b.name : examBatchId}`;
      }
      return 'Not assigned';
    }

    const batchIds = new Set<string>();
    const studentCodes = new Set<string>();
    list.forEach(a => {
      a.targetBatches.forEach(b => batchIds.add(b));
      a.targetStudents.forEach(s => studentCodes.add(s));
    });

    const parts = [];
    if (batchIds.size > 0) {
      const names = Array.from(batchIds).map(bid => {
        const b = batches.find(x => x.id === bid);
        return b ? b.name : bid;
      });
      parts.push(`Batches: ${names.slice(0, 2).join(', ')}${names.length > 2 ? ` +${names.length - 2}` : ''}`);
    }
    if (studentCodes.size > 0) {
      const names = Array.from(studentCodes).map(code => {
        const s = students.find(x => x.studentCode === code);
        return s ? s.name : code;
      });
      parts.push(`Students: ${names.slice(0, 2).join(', ')}${names.length > 2 ? ` +${names.length - 2}` : ''}`);
    }
    return parts.join(', ');
  };

  const getLatestAssignmentDate = (examId: string, examAssignedAt?: string | null, exam?: Exam) => {
    const list = assignments.filter(a => a.examId === examId);
    if (list.length === 0) {
      const fallbackDate = exam?.scheduledDate || examAssignedAt || (exam as any)?.availableFrom;
      if (fallbackDate) {
        return formatDateTimeIST(fallbackDate);
      }
      return '—';
    }
    const dates = list.map(a => new Date(a.startAt || a.createdAt!));
    const maxDate = new Date(Math.max(...dates.map(d => d.getTime())));
    return formatDateTimeIST(maxDate);
  };

  const getMorningTestTimes = (durationMinutes: number) => {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const y = tomorrow.getFullYear();
    const m = String(tomorrow.getMonth() + 1).padStart(2, '0');
    const d = String(tomorrow.getDate()).padStart(2, '0');
    const startStr = `${y}-${m}-${d}T06:00`;

    const endDate = new Date(tomorrow);
    endDate.setHours(6, durationMinutes || 30, 0, 0);
    const ey = endDate.getFullYear();
    const em = String(endDate.getMonth() + 1).padStart(2, '0');
    const ed = String(endDate.getDate()).padStart(2, '0');
    const eh = String(endDate.getHours()).padStart(2, '0');
    const emin = String(endDate.getMinutes()).padStart(2, '0');
    const endStr = `${ey}-${em}-${ed}T${eh}:${emin}`;

    return { startStr, endStr };
  };

  const getEveningTestTimes = (durationMinutes: number) => {
    const target = new Date();
    // If it is already past 9:00 PM (21:00) today, schedule for tomorrow 21:00
    if (target.getHours() >= 21) {
      target.setDate(target.getDate() + 1);
    }
    const y = target.getFullYear();
    const m = String(target.getMonth() + 1).padStart(2, '0');
    const d = String(target.getDate()).padStart(2, '0');
    const startStr = `${y}-${m}-${d}T21:00`;

    const endDate = new Date(target);
    endDate.setHours(21, durationMinutes || 30, 0, 0);
    const ey = endDate.getFullYear();
    const em = String(endDate.getMonth() + 1).padStart(2, '0');
    const ed = String(endDate.getDate()).padStart(2, '0');
    const eh = String(endDate.getHours()).padStart(2, '0');
    const emin = String(endDate.getMinutes()).padStart(2, '0');
    const endStr = `${ey}-${em}-${ed}T${eh}:${emin}`;

    return { startStr, endStr };
  };

  // Create Assignment Action
  const handleOpenAssign = (exam: Exam, type: 'objective' | 'subjective') => {
    const normDuration = getNormExamDuration(exam, type);
    setAssignModal({
      show: true,
      type,
      examId: exam.id,
      examName: exam.name,
      targetType: 'batch',
      selectedBatches: new Set(),
      selectedStudents: new Set(),
      openMode: 'immediate',
      startAtStr: '',
      endAtStr: '',
      attemptLimit: 1,
      lateEntryRestriction: false,
      normDuration,
      overrideDuration: false,
      examDuration: normDuration,
      examMode: exam.mode === 'classroom' ? 'classroom' : 'home',
      classroomDuration: normDuration || 60,
      classroomTimePerQ: 5,
      isMorningTest: false,
      isEveningTest: false
    });
  };

  const handleToggleBatchAssign = (batchId: string) => {
    const next = new Set(assignModal.selectedBatches);
    if (next.has(batchId)) next.delete(batchId);
    else next.add(batchId);
    setAssignModal(prev => ({ ...prev, selectedBatches: next }));
  };

  const handleToggleStudentAssign = (code: string) => {
    const next = new Set(assignModal.selectedStudents);
    if (next.has(code)) next.delete(code);
    else next.add(code);
    setAssignModal(prev => ({ ...prev, selectedStudents: next }));
  };

  const handleToggleBatchEdit = (batchId: string) => {
    const next = new Set(editModal.selectedBatches);
    if (next.has(batchId)) next.delete(batchId);
    else next.add(batchId);
    setEditModal(prev => ({ ...prev, selectedBatches: next }));
  };

  const handleToggleStudentEdit = (code: string) => {
    const next = new Set(editModal.selectedStudents);
    if (next.has(code)) next.delete(code);
    else next.add(code);
    setEditModal(prev => ({ ...prev, selectedStudents: next }));
  };

  // Edit Assignment Action
  const handleOpenEdit = (examId: string, examName: string, collection: string) => {
    const activeAssign = assignments.find(a => a.examId === examId && a.collection === collection);
    if (!activeAssign) return;

    // Check if started by anyone
    const startsCount = attemptCounts[examId] || 0;
    if (startsCount > 0) {
      alert(`❌ Cannot reschedule: this exam has already been started by ${startsCount} student(s).`);
      return;
    }

    const exam = (collection === 'batchAssignments' ? exams : subjectiveExams).find(e => e.id === examId);
    const normDuration = exam ? getNormExamDuration(exam, collection === 'batchAssignments' ? 'objective' : 'subjective') : (activeAssign.examDuration || 30);
    const isOverridden = Boolean(activeAssign.examDuration && activeAssign.examDuration !== normDuration);

    setEditModal({
      show: true,
      id: activeAssign.id,
      collection,
      examName,
      targetType: (activeAssign.targetType as any) || 'batch',
      selectedBatches: new Set(activeAssign.targetBatches || []),
      selectedStudents: new Set(activeAssign.targetStudents || []),
      openMode: activeAssign.openMode as any,
      startAtStr: activeAssign.startAt ? toISTString(activeAssign.startAt) : '',
      endAtStr: activeAssign.endAt ? toISTString(activeAssign.endAt) : '',
      attemptLimit: activeAssign.attemptLimit,
      normDuration,
      overrideDuration: isOverridden,
      examDuration: activeAssign.examDuration || normDuration,
      lateEntryRestriction: activeAssign.lateEntryRestriction === true,
      isMorningTest: false,
      isEveningTest: false
    });
  };

  const handleSaveAssignment = async () => {
    if (!firebaseUser || assigning) return;
    const { examId, type, targetType, selectedBatches, selectedStudents, openMode, startAtStr, endAtStr, attemptLimit, examDuration, examMode, classroomDuration, classroomTimePerQ, lateEntryRestriction } = assignModal;

    const batchesArr = Array.from(selectedBatches);
    const studentsArr = Array.from(selectedStudents);

    if (batchesArr.length === 0 && studentsArr.length === 0) {
      alert('Please select at least one batch or student to assign.');
      return;
    }

    if (openMode !== 'immediate' && (!startAtStr || !endAtStr)) {
      alert('Please select start and end dates.');
      return;
    }

    if (openMode !== 'immediate') {
      const now = new Date();
      const startDateTime = new Date(startAtStr);
      if (startDateTime < now) {
        alert('❌ Error: Cannot assign exams with a start date/time in the past.');
        return;
      }
      const endDateTime = new Date(endAtStr);
      if (endDateTime <= startDateTime) {
        alert('❌ Error: End datetime must be after start datetime.');
        return;
      }
    }

    setAssigning(true);

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId,
          type,
          targetType,
          targetBatches: batchesArr,
          targetStudents: studentsArr,
          openMode,
          startAtStr,
          endAtStr,
          attemptLimit,
          examDuration,
          examMode,
          classroomDuration,
          classroomTimePerQ,
          lateEntryRestriction
        })
      });

      if (!res.ok) {
        const errorData = await res.json().catch(() => ({}));
        throw new Error(errorData.message || 'Failed to save exam assignment schedule.');
      }

      alert('✅ Exam assigned successfully!');
      setAssignModal(prev => ({ ...prev, show: false }));

      if (type === 'subjective') {
        const exam = subjectiveExams.find(e => e.id === examId);
        if (exam && exam.questionIds && exam.questionIds.length > 0) {
          try {
            const qRes = await fetch(`/api/admin/questions?ids=${exam.questionIds.join(',')}`, {
              headers: { 'Authorization': `Bearer ${idToken}` }
            });
            if (qRes.ok) {
              const qData = await qRes.json();
              if (qData.questions && qData.questions.length > 0) {
                const { exportSubjectiveExamDirectPdf } = await import('@/lib/pdfExport');
                await exportSubjectiveExamDirectPdf(exam, qData.questions);
              }
            }
          } catch (pdfErr) {
            console.error('Failed to auto-generate exam PDF:', pdfErr);
          }
        }
      }

      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error occurred assigning exam.');
    } finally {
      setAssigning(false);
    }
  };

  const toISTString = toISTDateTimeLocalInput;

  const handleSaveEditedAssignment = async () => {
    if (!firebaseUser) return;
    const { id, collection, targetType, selectedBatches, selectedStudents, openMode, startAtStr, endAtStr, attemptLimit, examDuration, lateEntryRestriction } = editModal;

    const batchesArr = Array.from(selectedBatches);
    const studentsArr = Array.from(selectedStudents);

    if (batchesArr.length === 0 && studentsArr.length === 0) {
      alert('Please select at least one batch or student for the assignment.');
      return;
    }

    if (openMode !== 'immediate' && (!startAtStr || !endAtStr)) {
      alert('Please fill out scheduled start and end dates.');
      return;
    }

    if (openMode !== 'immediate') {
      const now = new Date();
      const startDateTime = new Date(startAtStr);
      if (startDateTime < now) {
        alert('❌ Error: Cannot assign exams with a start date/time in the past.');
        return;
      }
      const endDateTime = new Date(endAtStr);
      if (endDateTime <= startDateTime) {
        alert('❌ Error: End datetime must be after start datetime.');
        return;
      }
    }

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          id,
          collection,
          targetType,
          targetBatches: batchesArr,
          targetStudents: studentsArr,
          openMode,
          startAtStr,
          endAtStr,
          attemptLimit,
          examDuration,
          lateEntryRestriction
        })
      });

      if (!res.ok) {
        const errJson = await res.json().catch(() => ({}));
        throw new Error(errJson.message || 'Failed to update assignment.');
      }

      alert('✅ Assignment schedule and target audience updated!');
      setEditModal(prev => ({ ...prev, show: false }));
      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error editing assignment.');
    }
  };

  // Delete Action
  const handleDeleteExam = async (examId: string, examName: string, type: 'objective' | 'subjective') => {
    if (!confirm(`⚠️ WARNING: Deleting "${examName}" will permanently remove the exam, all student attempts, scores, evaluations, learning records, and topic masteries, and release all questions back to the Question Bank.\n\nThis cannot be undone. Continue?`)) {
      return;
    }
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/exams?examId=${examId}&type=${type}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.message || 'Failed to delete exam.');
      }

      alert('✅ Exam, student attempts, learning masteries, and question allocations deleted and rolled back successfully!');
      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error deleting exam.');
    }
  };

  // Classroom Subjective peer review lottery triggers
  const triggerPeerReviewLottery = async (examId: string, examName: string) => {
    if (!confirm(`🎲 Start peer review lottery for classroom exam: "${examName}"?\n\nThis will randomly and circularly assign each student to evaluate a classmate's paper.\n\nMake sure all students have completed writing their answers.`)) {
      return;
    }
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/lottery', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ examId })
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.message || 'Lottery computation failed.');
      }

      const data = await res.json();
      alert(`🎲 Peer Review Lottery Complete!\n\n📊 Total Students: ${data.totalStudents}\n📝 Assignments Created: ${data.totalAssignments}`);
      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error occurred starting lottery.');
    }
  };

  const openPeerReviewStatus = async (examId: string, examName: string) => {
    setLotteryModal({
      show: true,
      examId,
      examName,
      loading: true,
      statusData: null
    });
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/exams/lottery?examId=${examId}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load status.');
      }
      const data = await res.json();
      setLotteryModal(prev => ({ ...prev, loading: false, statusData: data }));
    } catch (err: any) {
      alert(err.message || 'Could not fetch status.');
      setLotteryModal(prev => ({ ...prev, show: false }));
    }
  };

  const openTruthTestReport = async (examId: string, examName: string) => {
    setTruthSearchText('');
    setTruthTestModal({
      show: true,
      examId,
      examName,
      loading: true,
      data: null
    });
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/reports/truth-test?examId=${examId}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to retrieve Truth Test report.');
      }
      const data = await res.json();
      setTruthTestModal(prev => ({ ...prev, loading: false, data }));
    } catch (err: any) {
      alert(err.message || 'Error loading Truth Test report.');
      setTruthTestModal(prev => ({ ...prev, show: false, loading: false }));
    }
  };

  // Filters application
  const filteredObjectiveExams = exams.filter(exam => {
    if (objFilterName && !exam.name.toLowerCase().includes(objFilterName.toLowerCase())) return false;
    if (objFilterTopic) {
      const codes = exam.topicCodes || [];
      if (!codes.some(c => c.toLowerCase().includes(objFilterTopic.toLowerCase()))) return false;
    }
    return true;
  });

  const filteredSubjectiveExams = subjectiveExams.filter(exam => {
    if (subjFilterName && !exam.name.toLowerCase().includes(subjFilterName.toLowerCase())) return false;
    if (subjFilterTopic) {
      const codes = exam.topicCodes || [];
      if (!codes.some(c => c.toLowerCase().includes(subjFilterTopic.toLowerCase()))) return false;
    }
    return true;
  });

  // By default, keep all classes collapsed. Expanded classes will be populated on user interaction.
  useEffect(() => {
    // No-op to avoid auto-expanding classes on load
  }, []);

  const getStudentsGroupedByBatch = () => {
    const grouped: { [batchId: string]: { batchName: string; list: Student[] } } = {};
    const unassigned: Student[] = [];

    // Initialize groups for all batches
    batches.forEach(b => {
      grouped[b.id] = { batchName: b.name, list: [] };
    });

    students.forEach(s => {
      const sBatchIds = s.batchIds && s.batchIds.length ? s.batchIds : (s.batchId ? [s.batchId] : []);
      if (sBatchIds.length === 0) {
        unassigned.push(s);
      } else {
        sBatchIds.forEach(bid => {
          if (grouped[bid]) {
            grouped[bid].list.push(s);
          } else {
            grouped[bid] = { batchName: bid, list: [s] };
          }
        });
      }
    });

    return { grouped, unassigned };
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading exams scheduler...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Page Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Manage Exams</h1>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px' }} onClick={() => router.push('/admin/exam-generator')}>
            ⚡ Exam Generator
          </button>
          <button className="btn btn-secondary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Tabs Container */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1100px', width: '100%', margin: '0 auto' }}>
        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '20px', gap: '12px' }}>
            <span>{error}</span>
            <button 
              className="btn btn-secondary btn-sm" 
              onClick={() => { setError(''); loadData(); }} 
              style={{ background: 'var(--surface)', color: 'var(--text)', whiteSpace: 'nowrap' }}
            >
              🔄 Retry
            </button>
          </div>
        )}

        <div className="tabs-container" style={{ display: 'flex', gap: '8px', marginBottom: '20px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px' }}>
          <button 
            className={`tab-btn ${activeTab === 'objective' ? 'active' : ''}`}
            onClick={() => setActiveTab('objective')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'objective' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'objective' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            Objective Exams
          </button>
          <button 
            className={`tab-btn ${activeTab === 'subjective' ? 'active' : ''}`}
            onClick={() => setActiveTab('subjective')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'subjective' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'subjective' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            Subjective Exams
          </button>
          <button 
            className={`tab-btn ${activeTab === 'practice' ? 'active' : ''}`}
            onClick={() => setActiveTab('practice')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'practice' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'practice' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            🏋️ Practice Tracks
          </button>
        </div>

        {/* Tab Content: Objective Exams */}
        {activeTab === 'objective' && (
          <ObjectiveTab
            filteredObjectiveExams={filteredObjectiveExams}
            assignments={assignments}
            attemptCounts={attemptCounts}
            objFilterName={objFilterName}
            setObjFilterName={setObjFilterName}
            objFilterTopic={objFilterTopic}
            setObjFilterTopic={setObjFilterTopic}
            isTodayOrTomorrow={isTodayOrTomorrow}
            getExamSortTimestamp={getExamSortTimestamp}
            getExamClass={getExamClass}
            getExamSubject={getExamSubject}
            getExamChapter={getExamChapter}
            getAssignedNames={getAssignedNames}
            getLatestAssignmentDate={getLatestAssignmentDate}
            getExamScheduleStatus={getExamScheduleStatus}
            expandedClasses={expandedClasses}
            toggleClassExpanded={toggleClassExpanded}
            isAssignedSectionExpanded={isObjAssignedSectionExpanded}
            setIsAssignedSectionExpanded={setIsObjAssignedSectionExpanded}
            expandedSubjects={expandedSubjects}
            toggleSubjectExpanded={toggleSubjectExpanded}
            expandedChapters={expandedChapters}
            toggleChapterExpanded={toggleChapterExpanded}
            expandAllAssigned={expandAllAssigned}
            collapseAllAssigned={collapseAllAssigned}
            assignedSortField={assignedSortField}
            assignedSortDir={assignedSortDir}
            handleAssignedSort={handleAssignedSort}
            sortAssignedExams={sortAssignedExams}
            getGroupedClasses={getGroupedClasses}
            handleOpenAssign={handleOpenAssign}
            handleDeleteExam={handleDeleteExam}
            toggleAssignmentStatus={toggleAssignmentStatus}
            exportUniversalExamPDF={exportUniversalExamPDF}
            handleOpenEdit={handleOpenEdit}
            router={router}
          />
        )}

        {/* Tab Content: Subjective Exams */}
        {activeTab === 'subjective' && (
          <SubjectiveTab
            filteredSubjectiveExams={filteredSubjectiveExams}
            assignments={assignments}
            attemptCounts={attemptCounts}
            subjFilterName={subjFilterName}
            setSubjFilterName={setSubjFilterName}
            subjFilterTopic={subjFilterTopic}
            setSubjFilterTopic={setSubjFilterTopic}
            isSubjectiveAvailableForAssignment={isSubjectiveAvailableForAssignment}
            isSubjectiveAlreadyAssigned={isSubjectiveAlreadyAssigned}
            isTodayOrTomorrow={isTodayOrTomorrow}
            getExamSortTimestamp={getExamSortTimestamp}
            getExamClass={getExamClass}
            getExamSubject={getExamSubject}
            getExamChapter={getExamChapter}
            getAssignedNames={getAssignedNames}
            getLatestAssignmentDate={getLatestAssignmentDate}
            getExamScheduleStatus={getExamScheduleStatus}
            expandedClasses={expandedClasses}
            toggleClassExpanded={toggleClassExpanded}
            isAssignedSectionExpanded={isSubjAssignedSectionExpanded}
            setIsAssignedSectionExpanded={setIsSubjAssignedSectionExpanded}
            expandedSubjects={expandedSubjects}
            toggleSubjectExpanded={toggleSubjectExpanded}
            expandedChapters={expandedChapters}
            toggleChapterExpanded={toggleChapterExpanded}
            expandAllAssigned={expandAllAssigned}
            collapseAllAssigned={collapseAllAssigned}
            assignedSortField={assignedSortField}
            assignedSortDir={assignedSortDir}
            handleAssignedSort={handleAssignedSort}
            sortAssignedExams={sortAssignedExams}
            getGroupedClasses={getGroupedClasses}
            handleOpenAssign={handleOpenAssign}
            handleDeleteExam={handleDeleteExam}
            toggleAssignmentStatus={toggleAssignmentStatus}
            exportUniversalExamPDF={exportUniversalExamPDF}
            handleOpenEdit={handleOpenEdit}
            triggerPeerReviewLottery={triggerPeerReviewLottery}
            openPeerReviewStatus={openPeerReviewStatus}
            openTruthTestReport={openTruthTestReport}
            router={router}
          />
        )}

        {/* Tab Content: Practice Track summary logs */}
        {activeTab === 'practice' && (
          <PracticeTab
            batches={batches}
            pracBatchFilter={pracBatchFilter}
            setPracBatchFilter={setPracBatchFilter}
            pracSearchName={pracSearchName}
            setPracSearchName={setPracSearchName}
            loadingPracticeTracks={loadingPracticeTracks}
            filteredPracticeBatches={filteredPracticeBatches}
            pracSortField={pracSortField}
            pracSortDir={pracSortDir}
            handlePracSort={handlePracSort}
            practiceStats={practiceStats}
            masteryStats={masteryStats}
            handleRowClick={handleRowClick}
            openTopicStatusModal={openTopicStatusModal}
            formatDateDMY={formatDateDMY}
          />
        )}
      </main>

      <AssignExamModal 
        assignModal={assignModal as any}
        setAssignModal={setAssignModal as any}
        batches={batches}
        getStudentsGroupedByBatch={getStudentsGroupedByBatch}
        handleToggleBatchAssign={handleToggleBatchAssign}
        handleToggleStudentAssign={handleToggleStudentAssign}
        getMorningTestTimes={getMorningTestTimes}
        getEveningTestTimes={getEveningTestTimes}
        handleSaveAssignment={handleSaveAssignment}
        assigning={assigning}
      />

      <EditAssignmentModal 
        editModal={editModal as any}
        setEditModal={setEditModal as any}
        batches={batches}
        getStudentsGroupedByBatch={getStudentsGroupedByBatch}
        handleToggleBatchEdit={handleToggleBatchEdit}
        handleToggleStudentEdit={handleToggleStudentEdit}
        getMorningTestTimes={getMorningTestTimes}
        getEveningTestTimes={getEveningTestTimes}
        handleSaveEditedAssignment={handleSaveEditedAssignment}
      />

      <PeerReviewModal 
        lotteryModal={lotteryModal}
        setLotteryModal={setLotteryModal}
      />

      <TruthTestModal 
        truthTestModal={truthTestModal}
        setTruthTestModal={setTruthTestModal}
      />

      <PracticeHistoryModal 
        selectedPracStudent={selectedPracStudent}
        setSelectedPracStudent={setSelectedPracStudent}
        loadingPracHistory={loadingPracHistory}
        pracHistory={pracHistory}
        modalExpandedSubjects={modalExpandedSubjects}
        setModalExpandedSubjects={setModalExpandedSubjects}
        modalExpandedChapters={modalExpandedChapters}
        setModalExpandedChapters={setModalExpandedChapters}
        modalSortKey={modalSortKey}
        modalSortDirection={modalSortDirection}
        handleModalSort={handleModalSort}
        loadScorecard={fetchScorecard}
        formatDateDMY={formatDateDMY}
      />

      <TopicStatusBreakdownModal 
        topicStatusModal={topicStatusModal as any}
        setTopicStatusModal={setTopicStatusModal as any}
      />

      <ScorecardModal 
        scorecard={scorecardData as any}
        loading={scorecardLoading}
        onClose={() => {
          setSelectedScorecardId(null);
          setScorecardData(null);
        }}
      />
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title={`YASHCOM Exams ${activeTab === 'objective' ? 'Objective' : activeTab === 'subjective' ? 'Subjective' : 'Practice'} Report`}
        filename={`Exams_${activeTab}_Report.pdf`}
        sections={
          activeTab === 'objective'
            ? [
                { id: 'templates', name: 'Objective Exam Templates List', elementId: 'objective-templates-section' },
                { id: 'assignments', name: 'Assigned Objective Sessions', elementId: 'objective-assignments-section' }
              ]
            : activeTab === 'subjective'
            ? [
                { id: 'templates', name: 'Subjective Exam Templates List', elementId: 'subjective-templates-section' },
                { id: 'assignments', name: 'Assigned Subjective Sessions', elementId: 'subjective-assignments-section' }
              ]
            : [
                { id: 'practice', name: 'Student Practice Metrics Logs', elementId: 'practice-tracks-section' }
              ]
        }
      />
    </div>
  );
}
