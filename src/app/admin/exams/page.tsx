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
import { isBlank } from '@/lib/questionTypes';
import { toISTDateTimeLocalInput, formatDateDMY, parseDateInput, getDateKeyIST } from '@/lib/dateUtils';

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
    return !exam.batchId && !assignments.some(a => a.examId === exam.id && a.collection === 'subjectiveAssignments');
  };

  const isSubjectiveAlreadyAssigned = (exam: Exam) => {
    const todayIST = new Date().toLocaleDateString('en-CA', { timeZone: 'Asia/Kolkata' });
    const isWeeklySuite = exam.type === 'home_practice' || exam.type === 'classroom_test';
    
    if (isWeeklySuite) {
      if (!exam.batchId) return false;
      if (!exam.scheduledDate) return true;
      return exam.scheduledDate <= todayIST;
    }
    
    return exam.batchId || assignments.some(a => a.examId === exam.id && a.collection === 'subjectiveAssignments');
  };

  // Already Assigned sorting states & helpers
  const [assignedSortField, setAssignedSortField] = useState<'name' | 'date'>('date');
  const [assignedSortDir, setAssignedSortDir] = useState<'asc' | 'desc'>('desc');
  const [expandedClasses, setExpandedClasses] = useState<Set<string>>(new Set());
  const [collapsedSubjects, setCollapsedSubjects] = useState<Set<string>>(new Set());
  const [collapsedChapters, setCollapsedChapters] = useState<Set<string>>(new Set());
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  const toggleClassExpanded = (clsKey: string) => {
    setExpandedClasses(prev => {
      const next = new Set(prev);
      if (next.has(clsKey)) next.delete(clsKey);
      else next.add(clsKey);
      return next;
    });
  };

  const toggleSubjectCollapsed = (key: string) => {
    setCollapsedSubjects(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const toggleChapterCollapsed = (key: string) => {
    setCollapsedChapters(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
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
    const todayStr = new Date().toLocaleDateString('en-CA');
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const tomorrowStr = tomorrow.toLocaleDateString('en-CA');
    const examDateStr = examDate.toLocaleDateString('en-CA');
    return examDateStr === todayStr || examDateStr === tomorrowStr;
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
      dateStr: examDate.toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short' }),
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
        return new Date(fallbackDate).toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
      }
      return '—';
    }
    const dates = list.map(a => new Date(a.startAt || a.createdAt!));
    const maxDate = new Date(Math.max(...dates.map(d => d.getTime())));
    return maxDate.toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
  };  const getMorningTestTimes = (durationMinutes: number) => {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const y = tomorrow.getFullYear();
    const m = String(tomorrow.getMonth() + 1).padStart(2, '0');
    const d = String(tomorrow.getDate()).padStart(2, '0');
    const startStr = `${y}-${m}-${d}T06:00`;

    const endDate = new Date(tomorrow);
    endDate.setHours(6, durationMinutes, 0, 0);
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
    endDate.setHours(21, durationMinutes, 0, 0);
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
    if (!confirm(`⚠️ WARNING: Deleting "${examName}" will permanently remove the exam AND all student attempts, scores, and evaluations. This cannot be undone. Continue?`)) {
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
        throw new Error('Failed to delete exam.');
      }

      alert('✅ Exam and all related attempts deleted successfully!');
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
          <div>
            <div className="filter-row" style={{ display: 'flex', gap: '10px', marginBottom: '16px', flexWrap: 'wrap' }}>
              <input 
                type="text" 
                value={objFilterName}
                placeholder="🔍 Filter by exam name..." 
                onChange={(e) => setObjFilterName(e.target.value)}
                style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
              />
              <input 
                type="text" 
                value={objFilterTopic}
                placeholder="🔍 Filter by topic code..." 
                onChange={(e) => setObjFilterTopic(e.target.value)}
                style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
              />
              <button 
                className="btn btn-secondary" 
                onClick={() => { setObjFilterName(''); setObjFilterTopic(''); }}
              >
                Clear
              </button>
            </div>

            {/* Section 1: Available for Assignment */}
            <div id="objective-templates-section" style={{ marginBottom: '24px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📋 Exams Available for Assignment
              </h3>
              <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                <div style={{ overflowX: 'auto' }}>
                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                        <th style={{ padding: '12px 16px' }}>Exam Name</th>
                        <th style={{ padding: '12px 16px' }}>Subject</th>
                        <th style={{ padding: '12px 16px' }}>Topics</th>
                        <th style={{ padding: '12px 16px' }}>Questions</th>
                        <th style={{ padding: '12px 16px' }}>Marks</th>
                        <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredObjectiveExams.filter(exam => !exam.batchId && !assignments.some(a => a.examId === exam.id && a.collection === 'batchAssignments')).length === 0 ? (
                        <tr>
                          <td colSpan={6} style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>No exams available for assignment.</td>
                        </tr>
                      ) : (
                        filteredObjectiveExams
                          .filter(exam => !exam.batchId && !assignments.some(a => a.examId === exam.id && a.collection === 'batchAssignments'))
                          .map(exam => (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>{exam.name}</td>
                              <td style={{ padding: '12px 16px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                              <td style={{ padding: '12px 16px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                              <td style={{ padding: '12px 16px' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                              <td style={{ padding: '12px 16px' }}>{exam.totalMarks || 0}</td>
                              <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                                <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end' }}>
                                  <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                                    📋 Assign
                                  </button>
                                  <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
                                    🗑️ Delete
                                  </button>
                                </div>
                              </td>
                            </tr>
                          ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Section 1b: Today's & Tomorrow's Exams */}
            <div id="objective-today-tomorrow-section" style={{ marginBottom: '24px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📅 Today's & Tomorrow's Exams
              </h3>
              <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                <div style={{ overflowX: 'auto' }}>
                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                        <th style={{ padding: '12px 16px' }}>Exam Name</th>
                        <th style={{ padding: '12px 16px' }}>Assigned To</th>
                        <th style={{ padding: '12px 16px' }}>Assigned Date</th>
                        <th style={{ padding: '12px 16px' }}>Status / Starts</th>
                        <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {(() => {
                        const todayTomorrowExams = filteredObjectiveExams.filter(exam => 
                          (exam.batchId || assignments.some(a => a.examId === exam.id && a.collection === 'batchAssignments')) &&
                          isTodayOrTomorrow(exam, 'objective')
                        );
                        
                        const sortedTodayTomorrowExams = [...todayTomorrowExams].sort((a, b) => {
                          const timeA = getExamSortTimestamp(a, 'objective');
                          const timeB = getExamSortTimestamp(b, 'objective');
                          if (timeA !== timeB) return timeA - timeB;
                          
                          const classA = parseInt(getExamClass(a)) || 0;
                          const classB = parseInt(getExamClass(b)) || 0;
                          return classA - classB;
                        });

                        if (sortedTodayTomorrowExams.length === 0) {
                          return (
                            <tr>
                              <td colSpan={5} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No exams scheduled for today or tomorrow.</td>
                            </tr>
                          );
                        }
                        
                        return sortedTodayTomorrowExams.map(exam => {
                          const count = attemptCounts[exam.id] || 0;
                          const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'batchAssignments');
                          const rawStatus = activeAssign?.status || 'active';
                          const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'objective');
                          return (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                                {exam.name}
                                <span style={{ marginLeft: '8px', fontSize: '9px', fontWeight: 700, background: 'rgba(59, 130, 246, 0.1)', color: 'var(--accent)', padding: '2px 6px', borderRadius: '4px' }}>
                                  Class {getExamClass(exam)}
                                </span>
                              </td>
                              <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                              <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                              <td style={{ padding: '12px 16px' }}>
                                 <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                   <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
                                     {scheduleStatus.badgeText}
                                   </span>
                                   {count > 0 && (
                                     <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                       ({count} starts)
                                     </span>
                                   )}
                                 </div>
                               </td>
                               <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                                 <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                   {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                     <button 
                                       className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                       style={{ padding: '4px 10px', fontSize: '11px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                       onClick={() => toggleAssignmentStatus(activeAssign.id, 'batchAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                     >
                                       {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                     </button>
                                   )}
                                   <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                     📄 PDF
                                   </button>
                                   <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                                     📋 Assign Again
                                   </button>
                                   <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => router.push(`/admin/exam-report?examId=${exam.id}`)}>
                                     📊 Report
                                   </button>
                                   <button 
                                     className="btn btn-secondary" 
                                     style={{ 
                                       padding: '4px 10px', 
                                       fontSize: '11px', 
                                       opacity: count > 0 ? 0.5 : 1, 
                                       cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                     }} 
                                     disabled={count > 0}
                                     onClick={() => handleOpenEdit(exam.id, exam.name, 'batchAssignments')}
                                   >
                                     ✏️ Edit
                                   </button>
                                   <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
                                     🗑️ Delete
                                   </button>
                                 </div>
                               </td>
                            </tr>
                          );
                        });
                      })()}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Section 2: Already Assigned */}
            <div id="objective-assignments-section">
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📚 Exams Already Assigned
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {(() => {
                  const assignedExamsList = filteredObjectiveExams.filter(exam => exam.batchId || assignments.some(a => a.examId === exam.id && a.collection === 'batchAssignments'));
                  if (assignedExamsList.length === 0) {
                    return (
                      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        No assigned exams found.
                      </div>
                    );
                  }
                  
                  const classes = getGroupedClasses(assignedExamsList);
                  return classes.map(cls => {
                    const examsInClass = assignedExamsList.filter(exam => getExamClass(exam) === cls);
                    const sortedExams = sortAssignedExams(examsInClass);
                    const isExpanded = expandedClasses.has(`objective||${cls}`);
                    
                    return (
                      <div key={cls} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                        <div 
                          onClick={() => toggleClassExpanded(`objective||${cls}`)}
                          style={{ padding: '14px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none' }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontWeight: 'bold', fontSize: '13.5px', color: 'var(--accent)' }}>🏫 Class {cls}</span>
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({examsInClass.length} exams)</span>
                          </div>
                          <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                        </div>
                        
                        {isExpanded && (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '12px' }}>
                            {(() => {
                              const subjectGroups = new Map<string, Exam[]>();
                              sortedExams.forEach(exam => {
                                const subj = getExamSubject(exam);
                                if (!subjectGroups.has(subj)) subjectGroups.set(subj, []);
                                subjectGroups.get(subj)!.push(exam);
                              });

                              return Array.from(subjectGroups.entries()).map(([subjName, subjExams]) => {
                                const subjKey = `subj||objective||${cls}||${subjName}`;
                                const isSubjExpanded = !collapsedSubjects.has(subjKey);

                                const chapterGroups = new Map<string, Exam[]>();
                                subjExams.forEach(exam => {
                                  const chap = getExamChapter(exam);
                                  if (!chapterGroups.has(chap)) chapterGroups.set(chap, []);
                                  chapterGroups.get(chap)!.push(exam);
                                });

                                return (
                                  <div key={subjKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--surface-popover)', overflow: 'hidden' }}>
                                    {/* Subject Line with count */}
                                    <div 
                                      onClick={() => toggleSubjectCollapsed(subjKey)}
                                      style={{ padding: '10px 14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                        <span style={{ fontWeight: 800, fontSize: '13px', color: 'var(--text)' }}>📖 {subjName}</span>
                                        <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>({subjExams.length} {subjExams.length === 1 ? 'exam' : 'exams'})</span>
                                      </div>
                                      <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                    </div>

                                    {/* Chapter hierarchy */}
                                    {isSubjExpanded && (
                                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '10px' }}>
                                        {Array.from(chapterGroups.entries()).map(([chapName, chapExams]) => {
                                          const chapKey = `chap||objective||${cls}||${subjName}||${chapName}`;
                                          const isChapExpanded = !collapsedChapters.has(chapKey);

                                          return (
                                            <div key={chapKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', overflow: 'hidden' }}>
                                              {/* Chapter Line with count */}
                                              <div 
                                                onClick={() => toggleChapterCollapsed(chapKey)}
                                                style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isChapExpanded ? '1px solid var(--border-light)' : 'none' }}
                                              >
                                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                                  <span style={{ fontWeight: 700, fontSize: '12px', color: 'var(--accent)' }}>📘 {chapName}</span>
                                                  <span style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>({chapExams.length} {chapExams.length === 1 ? 'exam' : 'exams'})</span>
                                                </div>
                                                <span style={{ fontSize: '9px', transition: 'transform 0.2s', transform: isChapExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                              </div>

                                              {/* Exam Table */}
                                              {isChapExpanded && (
                                                <div style={{ overflowX: 'auto' }}>
                                                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                                                    <thead>
                                                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                                                        <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('name')}>
                                                          Exam Name {assignedSortField === 'name' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                        </th>
                                                        <th style={{ padding: '10px 14px' }}>Assigned To</th>
                                                        <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('date')}>
                                                          Assigned Date {assignedSortField === 'date' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                        </th>
                                                        <th style={{ padding: '10px 14px' }}>Status / Starts</th>
                                                        <th style={{ padding: '10px 14px', textAlign: 'right' }}>Actions</th>
                                                      </tr>
                                                    </thead>
                                                    <tbody>
                                                      {chapExams.map(exam => {
                                                        const count = attemptCounts[exam.id] || 0;
                                                        const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'batchAssignments');
const rawStatus = activeAssign?.status || 'active';
const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'objective');
                                                        
                                                        return (
                                                          <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                            <td style={{ padding: '10px 14px', fontWeight: 600 }}>{exam.name}</td>
                                                            <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                                                            <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                                                            <td style={{ padding: '10px 14px' }}>
                                                               <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                                                 <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
  {scheduleStatus.badgeText}
</span>
                                                                 {count > 0 && (
                                                                   <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                                                     ({count} starts)
                                                                   </span>
                                                                 )}
                                                               </div>
                                                             </td>
                                                             <td style={{ padding: '10px 14px', textAlign: 'right' }}>
                                                               <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                                 {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                                   <button 
                                                                     className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                                     style={{ padding: '4px 10px', fontSize: '11px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                                                     onClick={() => toggleAssignmentStatus(activeAssign.id, 'batchAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                                                   >
                                                                     {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                                                   </button>
                                                                 )}
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                                                   📄 PDF
                                                                 </button>
                                                                 <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                                                                   📋 Assign Again
                                                                 </button>
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => router.push(`/admin/exam-report?examId=${encodeURIComponent(exam.id)}`)}>
                                                                   📊 Report
                                                                 </button>
                                                                 <button 
                                                                   className="btn btn-secondary" 
                                                                   style={{ 
                                                                     padding: '4px 10px', 
                                                                     fontSize: '11px', 
                                                                     opacity: count > 0 ? 0.5 : 1, 
                                                                     cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                                                   }} 
                                                                   disabled={count > 0}
                                                                   onClick={() => handleOpenEdit(exam.id, exam.name, 'batchAssignments')}
                                                                 >
                                                                   ✏️ Edit
                                                                 </button>
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
                                                                   🗑️ Delete
                                                                 </button>
                                                               </div>
                                                             </td>
                                                          </tr>
                                                        );
                                                      })}
                                                    </tbody>
                                                  </table>
                                                </div>
                                              )}
                                            </div>
                                          );
                                        })}
                                      </div>
                                    )}
                                  </div>
                                );
                              });
                            })()}
                          </div>
                        )}
                      </div>
                    );
                  });
                })()}
              </div>
            </div>
          </div>
        )}

        {/* Tab Content: Subjective Exams */}
        {activeTab === 'subjective' && (
          <div>
            <div className="filter-row" style={{ display: 'flex', gap: '10px', marginBottom: '16px', flexWrap: 'wrap' }}>
              <input 
                type="text" 
                value={subjFilterName}
                placeholder="🔍 Filter by exam name..." 
                onChange={(e) => setSubjFilterName(e.target.value)}
                style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
              />
              <input 
                type="text" 
                value={subjFilterTopic}
                placeholder="🔍 Filter by topic code..." 
                onChange={(e) => setSubjFilterTopic(e.target.value)}
                style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
              />
              <button 
                className="btn btn-secondary" 
                onClick={() => { setSubjFilterName(''); setSubjFilterTopic(''); }}
              >
                Clear
              </button>
            </div>

            {/* Section 1: Available for Assignment */}
            <div id="subjective-templates-section" style={{ marginBottom: '24px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📋 Subjective Exams Available for Assignment
              </h3>
              <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                <div style={{ overflowX: 'auto' }}>
                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                        <th style={{ padding: '12px 16px' }}>Exam Name</th>
                        <th style={{ padding: '12px 16px' }}>Subject</th>
                        <th style={{ padding: '12px 16px' }}>Topics</th>
                        <th style={{ padding: '12px 16px' }}>Mode</th>
                        <th style={{ padding: '12px 16px' }}>Marks</th>
                        <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredSubjectiveExams.filter(isSubjectiveAvailableForAssignment).length === 0 ? (
                        <tr>
                          <td colSpan={6} style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>No subjective exams available for assignment.</td>
                        </tr>
                      ) : (
                        filteredSubjectiveExams
                          .filter(isSubjectiveAvailableForAssignment)
                          .map(exam => (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>{exam.name}</td>
                              <td style={{ padding: '12px 16px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                              <td style={{ padding: '12px 16px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                              <td style={{ padding: '12px 16px' }}>
                                <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
                              </td>
                              <td style={{ padding: '12px 16px' }}>{exam.totalMarks || 0}</td>
                              <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                                <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end' }}>
                                  <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                                    📋 Assign
                                  </button>
                                  <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
                                    🗑️ Delete
                                  </button>
                                </div>
                              </td>
                            </tr>
                          ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Section 1b: Today's & Tomorrow's Subjective Exams */}
            <div id="subjective-today-tomorrow-section" style={{ marginBottom: '24px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📅 Today's & Tomorrow's Subjective Exams
              </h3>
              <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                <div style={{ overflowX: 'auto' }}>
                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                        <th style={{ padding: '12px 16px' }}>Exam Name</th>
                        <th style={{ padding: '12px 16px' }}>Mode</th>
                        <th style={{ padding: '12px 16px' }}>Peer Review</th>
                        <th style={{ padding: '12px 16px' }}>Assigned To</th>
                        <th style={{ padding: '12px 16px' }}>Status / Starts</th>
                        <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {(() => {
                        const todayTomorrowExams = filteredSubjectiveExams.filter(exam => 
                          (exam.batchId || assignments.some(a => a.examId === exam.id && a.collection === 'subjectiveAssignments')) &&
                          isTodayOrTomorrow(exam, 'subjective')
                        );
                        
                        const sortedTodayTomorrowExams = [...todayTomorrowExams].sort((a, b) => {
                          const timeA = getExamSortTimestamp(a, 'subjective');
                          const timeB = getExamSortTimestamp(b, 'subjective');
                          if (timeA !== timeB) return timeA - timeB;
                          
                          const classA = parseInt(getExamClass(a)) || 0;
                          const classB = parseInt(getExamClass(b)) || 0;
                          return classA - classB;
                        });

                        if (sortedTodayTomorrowExams.length === 0) {
                          return (
                            <tr>
                              <td colSpan={6} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No subjective exams scheduled for today or tomorrow.</td>
                            </tr>
                          );
                        }
                        
                        return sortedTodayTomorrowExams.map(exam => {
                          const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'subjectiveAssignments');
const rawStatus = activeAssign?.status || 'active';
const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'subjective');
                          const mode = activeAssign?.examMode || exam.mode || 'home';
                          const peerStatus = exam.peerReviewStatus || 'not_started';
                          const count = attemptCounts[exam.id] || 0;
                          return (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                                {exam.name}
                                <span style={{ marginLeft: '8px', fontSize: '9px', fontWeight: 700, background: 'rgba(59, 130, 246, 0.1)', color: 'var(--accent)', padding: '2px 6px', borderRadius: '4px' }}>
                                  Class {getExamClass(exam)}
                                </span>
                              </td>
                              <td style={{ padding: '12px 16px' }}>
                                {mode === 'home' ? (
                                  <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
                                ) : (
                                  <span className="badge badge-warning" style={{ fontSize: '10px' }}>🏫 Classroom</span>
                                )}
                              </td>
                              <td style={{ padding: '12px 16px', textTransform: 'capitalize', fontSize: '12px' }}>
                                {mode === 'classroom' ? (
                                  peerStatus === 'not_started' ? (
                                    <span style={{ color: 'var(--warning)' }}>⏳ Waiting</span>
                                  ) : peerStatus === 'assigned' ? (
                                    <span style={{ color: 'var(--accent)' }}>🔄 In Progress</span>
                                  ) : (
                                    <span style={{ color: 'var(--success)' }}>✅ Finished</span>
                                  )
                                ) : '—'}
                              </td>
                              <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                              <td style={{ padding: '12px 16px' }}>
                                 <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                   <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                     <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
  {scheduleStatus.badgeText}
</span>
                                     {count > 0 && (
                                       <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                         ({count} starts)
                                       </span>
                                     )}
                                   </div>
                                   <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                                     Assigned: {getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}
                                   </div>
                                 </div>
                               </td>
                               <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                                 <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                   {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                     <button 
                                       className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                       style={{ padding: '4px 8px', fontSize: '10px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                       onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                     >
                                       {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                     </button>
                                   )}
                                   <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                     📄 PDF
                                   </button>
                                   <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                                     📋 Assign Again
                                   </button>
                                   <button 
                                     className="btn btn-secondary" 
                                     style={{ 
                                       padding: '4px 8px', 
                                       fontSize: '10px', 
                                       opacity: count > 0 ? 0.5 : 1, 
                                       cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                     }} 
                                     disabled={count > 0}
                                     onClick={() => handleOpenEdit(exam.id, exam.name, 'subjectiveAssignments')}
                                   >
                                     ✏️ Edit
                                   </button>
                                   <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}>
                                     Grade
                                   </button>
                                   <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
                                     🗑️ Delete
                                   </button>
                                 </div>
                               </td>
                            </tr>
                          );
                        });
                      })()}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            {/* Section 2: Already Assigned */}
            <div id="subjective-assignments-section">
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                📚 Subjective Exams Already Assigned
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {(() => {
                  const assignedExamsList = filteredSubjectiveExams.filter(isSubjectiveAlreadyAssigned);
                  if (assignedExamsList.length === 0) {
                    return (
                      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        No assigned subjective exams found.
                      </div>
                    );
                  }
                  
                  const classes = getGroupedClasses(assignedExamsList);
                  return classes.map(cls => {
                    const examsInClass = assignedExamsList.filter(exam => getExamClass(exam) === cls);
                    const sortedExams = sortAssignedExams(examsInClass);
                    const isExpanded = expandedClasses.has(`subjective||${cls}`);
                    
                    return (
                      <div key={cls} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                        <div 
                          onClick={() => toggleClassExpanded(`subjective||${cls}`)}
                          style={{ padding: '14px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none' }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontWeight: 'bold', fontSize: '13.5px', color: 'var(--accent)' }}>🏫 Class {cls}</span>
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({examsInClass.length} subjective exams)</span>
                          </div>
                          <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                        </div>
                        
                        {isExpanded && (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '12px' }}>
                            {(() => {
                              const subjectGroups = new Map<string, Exam[]>();
                              sortedExams.forEach(exam => {
                                const subj = getExamSubject(exam);
                                if (!subjectGroups.has(subj)) subjectGroups.set(subj, []);
                                subjectGroups.get(subj)!.push(exam);
                              });

                              return Array.from(subjectGroups.entries()).map(([subjName, subjExams]) => {
                                const subjKey = `subj||subjective||${cls}||${subjName}`;
                                const isSubjExpanded = !collapsedSubjects.has(subjKey);

                                const chapterGroups = new Map<string, Exam[]>();
                                subjExams.forEach(exam => {
                                  const chap = getExamChapter(exam);
                                  if (!chapterGroups.has(chap)) chapterGroups.set(chap, []);
                                  chapterGroups.get(chap)!.push(exam);
                                });

                                return (
                                  <div key={subjKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--surface-popover)', overflow: 'hidden' }}>
                                    {/* Subject Line with count */}
                                    <div 
                                      onClick={() => toggleSubjectCollapsed(subjKey)}
                                      style={{ padding: '10px 14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                        <span style={{ fontWeight: 800, fontSize: '13px', color: 'var(--text)' }}>📖 {subjName}</span>
                                        <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>({subjExams.length} {subjExams.length === 1 ? 'exam' : 'exams'})</span>
                                      </div>
                                      <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                    </div>

                                    {/* Chapter hierarchy */}
                                    {isSubjExpanded && (
                                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '10px' }}>
                                        {Array.from(chapterGroups.entries()).map(([chapName, chapExams]) => {
                                          const chapKey = `chap||subjective||${cls}||${subjName}||${chapName}`;
                                          const isChapExpanded = !collapsedChapters.has(chapKey);

                                          return (
                                            <div key={chapKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', overflow: 'hidden' }}>
                                              {/* Chapter Line with count */}
                                              <div 
                                                onClick={() => toggleChapterCollapsed(chapKey)}
                                                style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isChapExpanded ? '1px solid var(--border-light)' : 'none' }}
                                              >
                                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                                  <span style={{ fontWeight: 700, fontSize: '12px', color: 'var(--accent)' }}>📘 {chapName}</span>
                                                  <span style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>({chapExams.length} {chapExams.length === 1 ? 'exam' : 'exams'})</span>
                                                </div>
                                                <span style={{ fontSize: '9px', transition: 'transform 0.2s', transform: isChapExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                              </div>

                                              {/* Exam Table */}
                                              {isChapExpanded && (
                                                <div style={{ overflowX: 'auto' }}>
                                                  <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                                                    <thead>
                                                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                                                        <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('name')}>
                                                          Exam Name {assignedSortField === 'name' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                        </th>
                                                        <th style={{ padding: '10px 14px' }}>Mode</th>
                                                        <th style={{ padding: '10px 14px' }}>Peer Review</th>
                                                        <th style={{ padding: '10px 14px' }}>Assigned To</th>
                                                        <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('date')}>
                                                          Status / Starts {assignedSortField === 'date' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                        </th>
                                                        <th style={{ padding: '10px 14px', textAlign: 'right' }}>Actions</th>
                                                      </tr>
                                                    </thead>
                                                    <tbody>
                                                      {chapExams.map(exam => {
                                                        const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'subjectiveAssignments');
const rawStatus = activeAssign?.status || 'active';
const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'subjective');
                                                        const mode = activeAssign?.examMode || exam.mode || 'home';
                                                        const peerStatus = exam.peerReviewStatus || 'not_started';
                                                        const count = attemptCounts[exam.id] || 0;
                                                        
                                                        return (
                                                          <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                            <td style={{ padding: '10px 14px', fontWeight: 600 }}>{exam.name}</td>
                                                            <td style={{ padding: '10px 14px' }}>
                                                              {mode === 'home' ? (
                                                                <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
                                                              ) : (
                                                                <span className="badge badge-warning" style={{ fontSize: '10px' }}>🏫 Classroom</span>
                                                              )}
                                                            </td>
                                                            <td style={{ padding: '10px 14px', textTransform: 'capitalize', fontSize: '12px' }}>
                                                              {mode === 'classroom' ? (
                                                                peerStatus === 'not_started' ? (
                                                                  <span style={{ color: 'var(--warning)' }}>⏳ Waiting</span>
                                                                ) : peerStatus === 'assigned' ? (
                                                                  <span style={{ color: 'var(--accent)' }}>🔄 In Progress</span>
                                                                ) : (
                                                                  <span style={{ color: 'var(--success)' }}>✅ Finished</span>
                                                                )
                                                              ) : '—'}
                                                            </td>
                                                            <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                                                            <td style={{ padding: '10px 14px' }}>
                                                               <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                                                  <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                                                   <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
  {scheduleStatus.badgeText}
</span>
                                                                   {count > 0 && (
                                                                     <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                                                       ({count} starts)
                                                                     </span>
                                                                   )}
                                                                 </div>
                                                               </div>
                                                             </td>
                                                             <td style={{ padding: '10px 14px', textAlign: 'right' }}>
                                                               <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                                 {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                                   <button 
                                                                     className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                                     style={{ padding: '4px 10px', fontSize: '11px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                                                     onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                                                   >
                                                                     {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                                                   </button>
                                                                 )}
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                                                   📄 PDF
                                                                 </button>
                                                                 <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                                                                   📋 Assign Again
                                                                 </button>
                                                                 <button 
                                                                   className="btn btn-secondary" 
                                                                   style={{ 
                                                                     padding: '4px 8px', 
                                                                     fontSize: '10px', 
                                                                     opacity: count > 0 ? 0.5 : 1, 
                                                                     cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                                                   }} 
                                                                   disabled={count > 0}
                                                                   onClick={() => handleOpenEdit(exam.id, exam.name, 'subjectiveAssignments')}
                                                                 >
                                                                   ✏️ Edit
                                                                 </button>
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}>
                                                                   Grade
                                                                 </button>
                                                                 {mode === 'classroom' && (
                                                                   <>
                                                                     {peerStatus === 'not_started' && (
                                                                       <button className="btn btn-primary" style={{ padding: '4px 8px', fontSize: '10px', background: 'var(--warning)', borderColor: 'var(--warning)' }} onClick={() => triggerPeerReviewLottery(exam.id, exam.name)}>
                                                                         🎲 Lottery
                                                                       </button>
                                                                     )}
                                                                     {peerStatus === 'assigned' && (
                                                                       <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px' }} onClick={() => openPeerReviewStatus(exam.id, exam.name)}>
                                                                         📊 Status
                                                                       </button>
                                                                     )}
                                                                     <button 
                                                                       className="btn btn-secondary" 
                                                                       style={{ padding: '4px 8px', fontSize: '10px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} 
                                                                       onClick={() => openTruthTestReport(exam.id, exam.name)}
                                                                     >
                                                                       ⚖️ Truth Test
                                                                     </button>
                                                                   </>
                                                                 )}
                                                                 <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '10px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
                                                                   🗑️ Delete
                                                                 </button>
                                                               </div>
                                                             </td>
                                                          </tr>
                                                        );
                                                      })}
                                                    </tbody>
                                                  </table>
                                                </div>
                                              )}
                                            </div>
                                          );
                                        })}
                                      </div>
                                    )}
                                  </div>
                                );
                              });
                            })()}
                          </div>
                        )}
                      </div>
                    );
                  });
                })()}
              </div>
            </div>
          </div>
        )}

        {/* Tab Content: Practice Track summary logs */}
        {activeTab === 'practice' && (
          <div id="practice-tracks-section" style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {/* Filters Bar */}
            <div className="card" style={{ padding: '16px 20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexWrap: 'wrap', gap: '8px', alignItems: 'center' }}>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', minWidth: '200px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Filter by Batch</label>
                <select 
                  value={pracBatchFilter}
                  onChange={(e) => setPracBatchFilter(e.target.value)}
                  style={{ padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px' }}
                >
                  <option value="all">All Batches</option>
                  {batches.map(b => (
                    <option key={b.id} value={b.id}>{b.name}</option>
                  ))}
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', flex: 1, minWidth: '240px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Search Student</label>
                <input 
                  type="text" 
                  placeholder="Filter by student name..."
                  value={pracSearchName}
                  onChange={(e) => setPracSearchName(e.target.value)}
                  style={{ padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px' }}
                />
              </div>
            </div>

            {/* Batches & Student Lists */}
            {loadingPracticeTracks ? (
              <div className="card" style={{ padding: '60px 20px', textAlign: 'center', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
                <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
                <div style={{ color: 'var(--text-muted)', fontSize: '13px', fontWeight: 600 }}>Loading practice tracks and topic mastery...</div>
              </div>
            ) : filteredPracticeBatches.map(({ batch, batchStudents, sortedStudents }) => {
              const renderSortIndicator = (field: string) => {
                if (pracSortField !== field) return <span style={{ color: 'var(--text-faint)', marginLeft: '4px' }}>⇅</span>;
                return pracSortDir === 'asc' ? <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↑</span> : <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↓</span>;
              };

              return (
                <div key={batch.id} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden', marginBottom: '16px' }}>
                  <div style={{ background: 'var(--bg-soft)', padding: '12px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h4 style={{ fontSize: '13px', fontWeight: 'bold', margin: 0, color: 'var(--text)' }}>
                      📦 {batch.name} — <span style={{ color: 'var(--accent)' }}>{batchStudents.length} students</span>
                    </h4>
                  </div>

                  <div style={{ overflowX: 'auto' }}>
                    <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                          <th onClick={() => handlePracSort('student')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            STUDENT {renderSortIndicator('student')}
                          </th>
                          <th onClick={() => handlePracSort('sessions')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            SESSIONS {renderSortIndicator('sessions')}
                          </th>
                          <th onClick={() => handlePracSort('questions')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            QUESTIONS {renderSortIndicator('questions')}
                          </th>
                          <th onClick={() => handlePracSort('score')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            AVG SCORE {renderSortIndicator('score')}
                          </th>
                          <th onClick={() => handlePracSort('avgMastery')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            AVG MASTERY {renderSortIndicator('avgMastery')}
                          </th>
                          <th onClick={() => handlePracSort('avgQuality')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            QUALITY {renderSortIndicator('avgQuality')}
                          </th>
                          <th onClick={() => handlePracSort('masteryStats')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            STATUS {renderSortIndicator('masteryStats')}
                          </th>
                          <th onClick={() => handlePracSort('active')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                            LAST SEEN {renderSortIndicator('active')}
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        {sortedStudents.length === 0 ? (
                          <tr>
                            <td colSpan={8} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No students found in this batch.</td>
                          </tr>
                        ) : (
                          sortedStudents.map(student => {
                            const stats = practiceStats[student.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
                            const mastery = masteryStats[student.studentCode] || { avgMastery: 0, avgQuality: 100, mastered: 0, practicing: 0, needsAttention: 0 };
                            const quality = mastery.avgQuality ?? 100;
                            return (
                              <tr 
                                key={student.studentCode} 
                                onClick={() => handleRowClick(student)}
                                className="hover-row"
                                style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', transition: 'background 0.2s' }}
                              >
                                <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>{student.name}</td>
                                <td style={{ padding: '12px 16px', textAlign: 'center' }}>{stats.totalSessions}</td>
                                <td style={{ padding: '12px 16px', textAlign: 'center' }}>{stats.questionsAttempted}</td>
                                <td style={{ padding: '12px 16px', fontWeight: 'bold', color: stats.totalSessions > 0 ? 'var(--accent)' : 'inherit' }}>
                                  {stats.totalSessions > 0 ? `${stats.avgScore}%` : '—'}
                                </td>
                                <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                    <span style={{ width: '28px' }}>{mastery.avgMastery}%</span>
                                    <div style={{ width: '40px', height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                      <div style={{
                                        width: `${mastery.avgMastery}%`,
                                        height: '100%',
                                        background: mastery.avgMastery >= 90 ? 'var(--success)' : mastery.avgMastery >= 50 ? 'var(--warning)' : 'var(--danger)'
                                      }} />
                                    </div>
                                  </div>
                                </td>
                                <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                    <span style={{ width: '28px' }}>{quality}%</span>
                                    <div style={{ width: '40px', height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                      <div style={{
                                        width: `${quality}%`,
                                        height: '100%',
                                        background: quality >= 80 ? 'var(--success)' : quality >= 50 ? 'var(--warning)' : 'var(--danger)'
                                      }} />
                                    </div>
                                  </div>
                                </td>
                                <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>
                                  <span 
                                    onClick={(e) => openTopicStatusModal(student, 'mastered', e)} 
                                    style={{ color: 'var(--success)', fontWeight: 700, cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.25)', transition: 'all 0.15s' }} 
                                    title="Click to view Mastered Topics (>=90% accuracy & target confidence)"
                                  >
                                    🟢 {mastery.mastered}
                                  </span>
                                  <span 
                                    onClick={(e) => openTopicStatusModal(student, 'practicing', e)} 
                                    style={{ color: 'var(--warning)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(245,158,11,0.12)', border: '1px solid rgba(245,158,11,0.25)', transition: 'all 0.15s' }} 
                                    title="Click to view Practicing / In Progress Topics (50-89% or low confidence)"
                                  >
                                    🟡 {mastery.practicing}
                                  </span>
                                  <span 
                                    onClick={(e) => openTopicStatusModal(student, 'needsAttention', e)} 
                                    style={{ color: 'var(--danger)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(239,68,68,0.12)', border: '1px solid rgba(239,68,68,0.25)', transition: 'all 0.15s' }} 
                                    title="Click to view Needs Care / Focus Topics (<50%)"
                                  >
                                    🔴 {mastery.needsAttention}
                                  </span>
                                </td>
                                <td style={{ padding: '12px 16px', color: 'var(--text-muted)' }}>
                                  {stats.lastActive ? formatDateDMY(stats.lastActive) : 'Never'}
                                </td>
                              </tr>
                            );
                          })
                        )}
                      </tbody>
                    </table>
                  </div>
                </div>
              );
            })}
          </div>
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
