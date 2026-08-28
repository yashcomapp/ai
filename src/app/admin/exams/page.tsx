'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ScorecardModal = dynamic(() => import('@/components/ScorecardModal'), { ssr: false });
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
import { useMathRender } from '@/hooks/useMathRender';
import { useScorecard } from '@/hooks/useScorecard';
import { exportUniversalExamPDF } from '@/lib/pdfExport';
import { isBlank } from '@/lib/questionTypes';
import { toISTDateTimeLocalInput } from '@/lib/dateUtils';

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
  questions?: string[];
  questionIds?: string[];
  totalMarks?: number;
  mode?: string;
  peerReviewStatus?: string;
  batchId?: string | null;
  assignedAt?: string | null;
  type?: string;
  scheduledDate?: string;
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
  const { toggleTheme } = useTheme();
  const router = useRouter();

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
    examDuration: number;
    // Subjective specifics
    examMode: 'home' | 'classroom';
    classroomDuration: number;
    classroomTimePerQ: number;
    isMorningTest?: boolean;
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
    examDuration: 30,
    examMode: 'home',
    classroomDuration: 60,
    classroomTimePerQ: 5,
    isMorningTest: false
  });

  const [assigning, setAssigning] = useState(false);

  const [editModal, setEditModal] = useState<{
    show: boolean;
    id: string;
    collection: string;
    examName: string;
    openMode: 'immediate' | 'scheduled' | 'fixed-slot';
    startAtStr: string;
    endAtStr: string;
    attemptLimit: number;
    examDuration: number;
    lateEntryRestriction: boolean;
    isMorningTest?: boolean;
  }>({
    show: false,
    id: '',
    collection: '',
    examName: '',
    openMode: 'immediate',
    startAtStr: '',
    endAtStr: '',
    attemptLimit: 1,
    examDuration: 30,
    lateEntryRestriction: false,
    isMorningTest: false
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
      setExams(data.exams);
      setSubjectiveExams(data.subjectiveExams);
      setBatches(data.batches);
      setStudents(data.students);
      setAssignments(data.assignments);
      setAttemptCounts(data.attemptCounts || {});
      setPracticeStats(data.practiceStats || {});
      setMasteryStats(data.masteryStats || {});
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred loading data.');
    } finally {
      setLoading(false);
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

  // Create Assignment Action
  const handleOpenAssign = (exam: Exam, type: 'objective' | 'subjective') => {
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
      lateEntryRestriction: true,
      examDuration: 30,
      examMode: exam.mode === 'classroom' ? 'classroom' : 'home',
      classroomDuration: 60,
      classroomTimePerQ: 5,
      isMorningTest: false
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

    setEditModal({
      show: true,
      id: activeAssign.id,
      collection,
      examName,
      openMode: activeAssign.openMode as any,
      startAtStr: activeAssign.startAt ? toISTString(activeAssign.startAt) : '',
      endAtStr: activeAssign.endAt ? toISTString(activeAssign.endAt) : '',
      attemptLimit: activeAssign.attemptLimit,
      examDuration: activeAssign.examDuration || 30,
      lateEntryRestriction: activeAssign.lateEntryRestriction === true,
      isMorningTest: false
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
    const { id, collection, openMode, startAtStr, endAtStr, attemptLimit, examDuration, lateEntryRestriction } = editModal;

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
          openMode,
          startAtStr,
          endAtStr,
          attemptLimit,
          examDuration,
          lateEntryRestriction
        })
      });

      if (!res.ok) {
        throw new Error('Failed to update assignment.');
      }

      alert('✅ Assignment schedule updated!');
      setEditModal(prev => ({ ...prev, show: false }));
      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error editing schedule.');
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
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Admin Scheduling & Exams Moderation Control Panel</div>
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
          <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
            {error}
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
                          const status = activeAssign?.status || 'active';
                          return (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                                {exam.name}
                                <span style={{ marginLeft: '8px', fontSize: '9px', fontWeight: 700, background: 'rgba(52, 152, 219, 0.1)', color: '#2980b9', padding: '2px 6px', borderRadius: '4px' }}>
                                  Class {getExamClass(exam)}
                                </span>
                              </td>
                              <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                              <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                              <td style={{ padding: '12px 16px' }}>
                                 <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                   {status === 'active' ? (
                                     <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(46, 204, 113, 0.15)', color: '#2ecc71', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                       🟢 Active / Open
                                     </span>
                                   ) : (
                                     <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(231, 76, 60, 0.15)', color: '#e74c3c', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                       🛑 Stopped / Disabled
                                     </span>
                                   )}
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
                                       className={`btn ${status === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                       style={{ padding: '4px 10px', fontSize: '11px', background: status === 'active' ? '#e74c3c' : '#2ecc71', color: 'white', border: 'none' }} 
                                       onClick={() => toggleAssignmentStatus(activeAssign.id, 'batchAssignments', status === 'active' ? 'disabled' : 'active')}
                                     >
                                       {status === 'active' ? '🛑 Stop' : '🟢 Start'}
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
                                                        const status = activeAssign?.status || 'active';
                                                        
                                                        return (
                                                          <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                            <td style={{ padding: '10px 14px', fontWeight: 600 }}>{exam.name}</td>
                                                            <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                                                            <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                                                            <td style={{ padding: '10px 14px' }}>
                                                               <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                                                 {status === 'active' ? (
                                                                   <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(46, 204, 113, 0.15)', color: '#2ecc71', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                     🟢 Active / Open
                                                                   </span>
                                                                 ) : (
                                                                   <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(231, 76, 60, 0.15)', color: '#e74c3c', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                     🛑 Stopped / Disabled
                                                                   </span>
                                                                 )}
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
                                                                     className={`btn ${status === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                                     style={{ padding: '4px 10px', fontSize: '11px', background: status === 'active' ? '#e74c3c' : '#2ecc71', color: 'white', border: 'none' }} 
                                                                     onClick={() => toggleAssignmentStatus(activeAssign.id, 'batchAssignments', status === 'active' ? 'disabled' : 'active')}
                                                                   >
                                                                     {status === 'active' ? '🛑 Stop' : '🟢 Start'}
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
                          const status = activeAssign?.status || 'active';
                          const mode = activeAssign?.examMode || exam.mode || 'home';
                          const peerStatus = exam.peerReviewStatus || 'not_started';
                          const count = attemptCounts[exam.id] || 0;
                          return (
                            <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                                {exam.name}
                                <span style={{ marginLeft: '8px', fontSize: '9px', fontWeight: 700, background: 'rgba(52, 152, 219, 0.1)', color: '#2980b9', padding: '2px 6px', borderRadius: '4px' }}>
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
                                     {status === 'active' ? (
                                       <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(46, 204, 113, 0.15)', color: '#2ecc71', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                         🟢 Active / Open
                                       </span>
                                     ) : (
                                       <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(231, 76, 60, 0.15)', color: '#e74c3c', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                         🛑 Stopped / Disabled
                                       </span>
                                     )}
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
                                       className={`btn ${status === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                       style={{ padding: '4px 8px', fontSize: '10px', background: status === 'active' ? '#e74c3c' : '#2ecc71', color: 'white', border: 'none' }} 
                                       onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', status === 'active' ? 'disabled' : 'active')}
                                     >
                                       {status === 'active' ? '🛑 Stop' : '🟢 Start'}
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
                                                        const status = activeAssign?.status || 'active';
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
                                                                   {status === 'active' ? (
                                                                     <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(46, 204, 113, 0.15)', color: '#2ecc71', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                       🟢 Active / Open
                                                                     </span>
                                                                   ) : (
                                                                     <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: 'rgba(231, 76, 60, 0.15)', color: '#e74c3c', fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                       🛑 Stopped / Disabled
                                                                     </span>
                                                                   )}
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
                                                             <td style={{ padding: '10px 14px', textAlign: 'right' }}>
                                                               <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                                 {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                                   <button 
                                                                     className={`btn ${status === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                                     style={{ padding: '4px 8px', fontSize: '10px', background: status === 'active' ? '#e74c3c' : '#2ecc71', color: 'white', border: 'none' }} 
                                                                     onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', status === 'active' ? 'disabled' : 'active')}
                                                                   >
                                                                     {status === 'active' ? '🛑 Stop' : '🟢 Start'}
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
            {filteredPracticeBatches.map(({ batch, batchStudents, sortedStudents }) => {
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
                                        background: mastery.avgMastery >= 90 ? 'var(--success)' : mastery.avgMastery >= 50 ? '#d97706' : 'var(--danger)'
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
                                        background: quality >= 80 ? 'var(--success)' : quality >= 50 ? '#d97706' : 'var(--danger)'
                                      }} />
                                    </div>
                                  </div>
                                </td>
                                <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>
                                  <span 
                                    onClick={(e) => openTopicStatusModal(student, 'mastered', e)} 
                                    style={{ color: 'var(--success)', fontWeight: 700, cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.25)', transition: 'all 0.15s' }} 
                                    title="Click to view Mastered Topics (>=90% && Conf>=20)"
                                  >
                                    🟢 {mastery.mastered}
                                  </span>
                                  <span 
                                    onClick={(e) => openTopicStatusModal(student, 'practicing', e)} 
                                    style={{ color: '#d97706', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(217,119,6,0.12)', border: '1px solid rgba(217,119,6,0.25)', transition: 'all 0.15s' }} 
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
                                  {stats.lastActive ? new Date(stats.lastActive).toLocaleDateString('en-IN') : 'Never'}
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

      {/* Modal: Assign Exam (Both Objective & Subjective) */}
      {assignModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '550px', width: '90%', maxHeight: '90vh', overflowY: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '16px', fontWeight: 800, margin: 0 }}>
              📋 Assign {assignModal.type === 'objective' ? 'Objective' : 'Subjective'} Exam: {assignModal.examName}
            </h3>

            {assignModal.type === 'subjective' && (
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subjective Exam Mode</label>
                <div style={{ display: 'flex', gap: '15px' }}>
                  <label style={{ fontSize: '12px' }}>
                    <input 
                      type="radio" 
                      name="examMode" 
                      checked={assignModal.examMode === 'home'} 
                      onChange={() => setAssignModal(prev => ({ ...prev, examMode: 'home' }))} 
                    /> 🏠 Home Mode (Parent review)
                  </label>
                  <label style={{ fontSize: '12px' }}>
                    <input 
                      type="radio" 
                      name="examMode" 
                      checked={assignModal.examMode === 'classroom'} 
                      onChange={() => setAssignModal(prev => ({ ...prev, examMode: 'classroom' }))} 
                    /> 🏫 Classroom Mode (Peer Lottery)
                  </label>
                </div>
              </div>
            )}

            {assignModal.type === 'subjective' && assignModal.examMode === 'classroom' && (
              <div style={{ background: 'var(--bg-soft)', padding: '10px', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--warning)', fontSize: '11px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <strong>Classroom Peer lottery Settings:</strong>
                <div style={{ display: 'flex', gap: '10px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Duration (mins)</label>
                    <input 
                      type="number" 
                      value={assignModal.classroomDuration === undefined || assignModal.classroomDuration === null ? '' : assignModal.classroomDuration} 
                      onChange={(e) => {
                        const raw = e.target.value;
                        setAssignModal(prev => ({ ...prev, classroomDuration: raw === '' ? ('' as any) : Number(raw) }));
                      }}
                      onBlur={() => {
                        if (!assignModal.classroomDuration || isNaN(Number(assignModal.classroomDuration))) {
                          setAssignModal(prev => ({ ...prev, classroomDuration: 45 }));
                        }
                      }}
                      style={{ width: '80px', padding: '4px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                    />
                  </div>
                  <div>
                    <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Mins per Q</label>
                    <input 
                      type="number" 
                      value={assignModal.classroomTimePerQ === undefined || assignModal.classroomTimePerQ === null ? '' : assignModal.classroomTimePerQ} 
                      onChange={(e) => {
                        const raw = e.target.value;
                        setAssignModal(prev => ({ ...prev, classroomTimePerQ: raw === '' ? ('' as any) : Number(raw) }));
                      }}
                      onBlur={() => {
                        if (!assignModal.classroomTimePerQ || isNaN(Number(assignModal.classroomTimePerQ))) {
                          setAssignModal(prev => ({ ...prev, classroomTimePerQ: 3 }));
                        }
                      }}
                      style={{ width: '80px', padding: '4px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                    />
                  </div>
                </div>
              </div>
            )}

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Target Audience</label>
              <div style={{ display: 'flex', gap: '15px', marginBottom: '10px' }}>
                <label style={{ fontSize: '12px' }}>
                  <input 
                    type="radio" 
                    name="targetType" 
                    checked={assignModal.targetType === 'batch'} 
                    onChange={() => setAssignModal(prev => ({ ...prev, targetType: 'batch' }))} 
                  /> Batches Only
                </label>
                <label style={{ fontSize: '12px' }}>
                  <input 
                    type="radio" 
                    name="targetType" 
                    checked={assignModal.targetType === 'student'} 
                    onChange={() => setAssignModal(prev => ({ ...prev, targetType: 'student' }))} 
                  /> Students Only
                </label>
                <label style={{ fontSize: '12px' }}>
                  <input 
                    type="radio" 
                    name="targetType" 
                    checked={assignModal.targetType === 'mixed'} 
                    onChange={() => setAssignModal(prev => ({ ...prev, targetType: 'mixed' }))} 
                  /> Mixed Audience
                </label>
              </div>

              {/* Batches selections */}
              {(assignModal.targetType === 'batch' || assignModal.targetType === 'mixed') && (
                <div style={{ marginBottom: '10px' }}>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>Select Target Batches:</label>
                  <div style={{ maxHeight: '100px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '5px' }}>
                    {batches.map(b => (
                      <label key={b.id} style={{ display: 'block', fontSize: '12px', padding: '2px 0' }}>
                        <input 
                          type="checkbox" 
                          checked={assignModal.selectedBatches.has(b.id)} 
                          onChange={() => handleToggleBatchAssign(b.id)} 
                        /> 📦 {b.name}
                      </label>
                    ))}
                  </div>
                </div>
              )}

              {/* Student selections grouped by batch */}
              {(assignModal.targetType === 'student' || assignModal.targetType === 'mixed') && (
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>Select Target Students (Grouped by Batch):</label>
                  <div style={{ maxHeight: '180px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '5px' }}>
                    {(() => {
                      const { grouped, unassigned } = getStudentsGroupedByBatch();
                      const elements: React.ReactNode[] = [];

                      Object.entries(grouped).forEach(([bid, group]) => {
                        if (group.list.length === 0) return;
                        elements.push(
                          <div key={`group-hdr-${bid}`} style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--accent)', marginTop: '8px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                            📦 {group.batchName}
                          </div>
                        );
                        group.list.forEach(s => {
                          elements.push(
                            <label key={`${bid}-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px' }}>
                              <input 
                                type="checkbox" 
                                checked={assignModal.selectedStudents.has(s.studentCode)} 
                                onChange={() => handleToggleStudentAssign(s.studentCode)} 
                              /> 👤 {s.name}
                            </label>
                          );
                        });
                      });

                      if (unassigned.length > 0) {
                        elements.push(
                          <div key="group-hdr-unassigned" style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--text-muted)', marginTop: '8px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                            👤 Unassigned / No Batch
                          </div>
                        );
                        unassigned.forEach(s => {
                          elements.push(
                            <label key={`unassigned-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px' }}>
                              <input 
                                type="checkbox" 
                                checked={assignModal.selectedStudents.has(s.studentCode)} 
                                onChange={() => handleToggleStudentAssign(s.studentCode)} 
                              /> 👤 {s.name}
                            </label>
                          );
                        });
                      }

                      return elements.length > 0 ? elements : <div style={{ fontSize: '11px', color: 'var(--text-muted)', padding: '10px 0' }}>No students found.</div>;
                    })()}
                  </div>
                </div>
              )}
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Availability Slot</label>
              <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '10px' }}>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="openMode" 
                    checked={assignModal.openMode === 'immediate'} 
                    onChange={() => setAssignModal(prev => ({ ...prev, openMode: 'immediate', isMorningTest: false }))} 
                  /> Immediate
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="openMode" 
                    checked={assignModal.openMode === 'scheduled'} 
                    onChange={() => setAssignModal(prev => ({ ...prev, openMode: 'scheduled' }))} 
                  /> Scheduled
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: 'rgba(52, 152, 219, 0.1)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.2)' }}>
                  <input 
                    type="checkbox" 
                    checked={!!assignModal.isMorningTest} 
                    onChange={(e) => {
                      const checked = e.target.checked;
                      setAssignModal(prev => {
                        let updates: any = { isMorningTest: checked };
                        if (checked) {
                          updates.openMode = 'scheduled';
                          const duration = prev.type === 'objective' ? prev.examDuration : (prev.examMode === 'classroom' ? prev.classroomDuration : 60);
                          const times = getMorningTestTimes(duration);
                          updates.startAtStr = times.startStr;
                          updates.endAtStr = times.endStr;
                        }
                        return { ...prev, ...updates };
                      });
                    }}
                  /> ☀️ 6 AM Test
                </label>
              </div>

              {assignModal.openMode === 'scheduled' && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <div style={{ flex: 1 }}>
                        <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Start Datetime</label>
                        <input 
                          type="datetime-local" 
                          value={assignModal.startAtStr}
                          disabled={assignModal.isMorningTest}
                          onChange={(e) => {
                            const val = e.target.value;
                            setAssignModal(prev => ({ 
                              ...prev, 
                              startAtStr: val, 
                              endAtStr: val 
                            }));
                          }}
                          style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                        />
                      </div>
                      <div style={{ flex: 1 }}>
                        <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>End Datetime</label>
                        <input 
                          type="datetime-local" 
                          value={assignModal.endAtStr}
                          disabled={assignModal.isMorningTest}
                          onChange={(e) => setAssignModal(prev => ({ ...prev, endAtStr: e.target.value }))}
                          style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                        />
                      </div>
                    </div>
                    {/* Late Entry Restriction Options */}
                    <div style={{ marginTop: '5px' }}>
                      <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Late Entry Restriction</label>
                      <div style={{ display: 'flex', gap: '15px' }}>
                        <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                          <input 
                            type="radio" 
                            name="lateEntryRestriction" 
                            checked={assignModal.lateEntryRestriction === true} 
                            onChange={() => setAssignModal(prev => ({ ...prev, lateEntryRestriction: true }))} 
                            style={{ cursor: 'pointer' }}
                          /> Enforce 5-minute limit
                        </label>
                        <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                          <input 
                            type="radio" 
                            name="lateEntryRestriction" 
                            checked={assignModal.lateEntryRestriction === false} 
                            onChange={() => setAssignModal(prev => ({ ...prev, lateEntryRestriction: false }))} 
                            style={{ cursor: 'pointer' }}
                          /> Allow late entry
                        </label>
                      </div>
                    </div>
                  </div>
                )}
            </div>

            <div style={{ display: 'flex', gap: '15px' }}>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Attempt Limit</label>
                <select 
                  value={assignModal.attemptLimit} 
                  onChange={(e) => setAssignModal(prev => ({ ...prev, attemptLimit: Number(e.target.value) }))}
                  style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                >
                  <option value={1}>1 Attempt</option>
                  <option value={2}>2 Attempts</option>
                  <option value={3}>3 Attempts</option>
                  <option value={-1}>Unlimited</option>
                </select>
              </div>
              {assignModal.type === 'objective' && (
                <div style={{ flex: 1 }}>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Duration (Minutes)</label>
                  <input 
                    type="number" 
                    value={assignModal.examDuration === undefined || assignModal.examDuration === null ? '' : assignModal.examDuration} 
                    onChange={(e) => {
                      const raw = e.target.value;
                      if (raw === '') {
                        setAssignModal(prev => ({ ...prev, examDuration: '' as any }));
                        return;
                      }
                      const dur = Number(raw);
                      setAssignModal(prev => {
                        let updates: any = { examDuration: isNaN(dur) ? '' : dur };
                        if (prev.isMorningTest && prev.startAtStr && !isNaN(dur) && dur > 0) {
                          const startDate = new Date(prev.startAtStr);
                          const endDate = new Date(startDate.getTime() + dur * 60000);
                          const endYear = endDate.getFullYear();
                          const endMonth = String(endDate.getMonth() + 1).padStart(2, '0');
                          const endDateStr = String(endDate.getDate()).padStart(2, '0');
                          const endHours = String(endDate.getHours()).padStart(2, '0');
                          const endMinutes = String(endDate.getMinutes()).padStart(2, '0');
                          updates.endAtStr = `${endYear}-${endMonth}-${endDateStr}T${endHours}:${endMinutes}`;
                        }
                        return { ...prev, ...updates };
                      });
                    }}
                    onBlur={() => {
                      if (!assignModal.examDuration || Number(assignModal.examDuration) < 1) {
                        setAssignModal(prev => ({ ...prev, examDuration: 45 }));
                      }
                    }}
                    style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                  />
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setAssignModal(prev => ({ ...prev, show: false }))} disabled={assigning}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveAssignment} disabled={assigning}>
                {assigning ? '⏳ Assigning Exam...' : 'Assign Exam'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Edit Assignment Schedule */}
      {editModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '450px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '16px', fontWeight: 800, margin: 0 }}>
              ✏️ Edit Assignment: {editModal.examName}
            </h3>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Availability Slot</label>
              <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '10px' }}>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="editOpenMode" 
                    checked={editModal.openMode === 'immediate'} 
                    onChange={() => setEditModal(prev => ({ ...prev, openMode: 'immediate', isMorningTest: false }))} 
                  /> Immediate
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="editOpenMode" 
                    checked={editModal.openMode === 'scheduled'} 
                    onChange={() => setEditModal(prev => ({ ...prev, openMode: 'scheduled' }))} 
                  /> Scheduled
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: 'rgba(52, 152, 219, 0.1)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.2)' }}>
                  <input 
                    type="checkbox" 
                    checked={!!editModal.isMorningTest} 
                    onChange={(e) => {
                      const checked = e.target.checked;
                      setEditModal(prev => {
                        let updates: any = { isMorningTest: checked };
                        if (checked) {
                          updates.openMode = 'scheduled';
                          const times = getMorningTestTimes(prev.examDuration || 30);
                          updates.startAtStr = times.startStr;
                          updates.endAtStr = times.endStr;
                        }
                        return { ...prev, ...updates };
                      });
                    }}
                  /> ☀️ 6 AM Test
                </label>
              </div>

              {editModal.openMode === 'scheduled' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '10px' }}>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Start Datetime</label>
                      <input 
                        type="datetime-local" 
                        value={editModal.startAtStr}
                        disabled={editModal.isMorningTest}
                        onChange={(e) => {
                          const val = e.target.value;
                          setEditModal(prev => ({ 
                            ...prev, 
                            startAtStr: val, 
                            endAtStr: val 
                          }));
                        }}
                        style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                      />
                    </div>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>End Datetime</label>
                      <input 
                        type="datetime-local" 
                        value={editModal.endAtStr}
                        disabled={editModal.isMorningTest}
                        onChange={(e) => setEditModal(prev => ({ ...prev, endAtStr: e.target.value }))}
                        style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                      />
                    </div>
                  </div>
                  {/* Late Entry Restriction Options */}
                  <div style={{ marginTop: '5px' }}>
                    <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Late Entry Restriction</label>
                    <div style={{ display: 'flex', gap: '15px' }}>
                      <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                        <input 
                          type="radio" 
                          name="editLateEntryRestriction" 
                          checked={editModal.lateEntryRestriction === true} 
                          onChange={() => setEditModal(prev => ({ ...prev, lateEntryRestriction: true }))} 
                          style={{ cursor: 'pointer' }}
                        /> Enforce 5-minute limit
                      </label>
                      <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                        <input 
                          type="radio" 
                          name="editLateEntryRestriction" 
                          checked={editModal.lateEntryRestriction === false} 
                          onChange={() => setEditModal(prev => ({ ...prev, lateEntryRestriction: false }))} 
                          style={{ cursor: 'pointer' }}
                        /> Allow late entry
                      </label>
                    </div>
                  </div>
                </div>
              )}
            </div>

            <div style={{ display: 'flex', gap: '15px' }}>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Attempt Limit</label>
                <select 
                  value={editModal.attemptLimit} 
                  onChange={(e) => setEditModal(prev => ({ ...prev, attemptLimit: Number(e.target.value) }))}
                  style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                >
                  <option value={1}>1 Attempt</option>
                  <option value={2}>2 Attempts</option>
                  <option value={3}>3 Attempts</option>
                  <option value={-1}>Unlimited</option>
                </select>
              </div>
              {editModal.collection === 'batchAssignments' && (
                <div style={{ flex: 1 }}>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Duration (Minutes)</label>
                  <input 
                    type="number" 
                    value={editModal.examDuration === undefined || editModal.examDuration === null ? '' : editModal.examDuration} 
                    onChange={(e) => {
                      const raw = e.target.value;
                      if (raw === '') {
                        setEditModal(prev => ({ ...prev, examDuration: '' as any }));
                        return;
                      }
                      const dur = Number(raw);
                      setEditModal(prev => {
                        let updates: any = { examDuration: isNaN(dur) ? '' : dur };
                        if (prev.isMorningTest && prev.startAtStr && !isNaN(dur) && dur > 0) {
                          const startDate = new Date(prev.startAtStr);
                          const endDate = new Date(startDate.getTime() + dur * 60000);
                          const endYear = endDate.getFullYear();
                          const endMonth = String(endDate.getMonth() + 1).padStart(2, '0');
                          const endDateStr = String(endDate.getDate()).padStart(2, '0');
                          const endHours = String(endDate.getHours()).padStart(2, '0');
                          const endMinutes = String(endDate.getMinutes()).padStart(2, '0');
                          updates.endAtStr = `${endYear}-${endMonth}-${endDateStr}T${endHours}:${endMinutes}`;
                        }
                        return { ...prev, ...updates };
                      });
                    }}
                    onBlur={() => {
                      if (!editModal.examDuration || Number(editModal.examDuration) < 1) {
                        setEditModal(prev => ({ ...prev, examDuration: 45 }));
                      }
                    }}
                    style={{ width: '100%', padding: '6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                  />
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setEditModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveEditedAssignment}>Save Changes</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Peer Review StatusPairings */}
      {lotteryModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '500px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
                📊 Peer Review Status: {lotteryModal.examName}
              </h3>
              <button onClick={() => setLotteryModal(prev => ({ ...prev, show: false }))} style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '16px' }}>✕</button>
            </div>

            {lotteryModal.loading ? (
              <div style={{ padding: '30px', textAlign: 'center' }}>
                <div className="spinner"></div> Fetching pairings...
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '12px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }}>
                  <span>Completed: <strong>{lotteryModal.statusData?.completedCount || 0}</strong></span>
                  <span>Pending: <strong>{lotteryModal.statusData?.pendingCount || 0}</strong></span>
                </div>

                <div style={{ maxHeight: '250px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {lotteryModal.statusData?.pendingAssignments?.map((a: any, idx: number) => (
                    <div key={`p_${idx}`} style={{ padding: '6px 10px', background: 'rgba(255,152,0,0.1)', color: 'var(--warning)', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--warning)' }}>
                      👤 {a.reviewerName} → 📝 {a.revieweeName} (Pending)
                    </div>
                  ))}
                  {lotteryModal.statusData?.completedAssignments?.map((a: any, idx: number) => (
                    <div key={`c_${idx}`} style={{ padding: '6px 10px', background: 'rgba(76,175,80,0.1)', color: 'var(--success)', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--success)' }}>
                      ✅ {a.reviewerName} → 📝 {a.revieweeName} (Completed)
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setLotteryModal(prev => ({ ...prev, show: false }))}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Truth Test report */}
      {truthTestModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '900px', width: '100%', maxHeight: '85vh', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)', overflow: 'hidden' }}>
            {/* Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', padding: '16px 24px' }}>
              <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                ⚖️ Truth Test Report: {truthTestModal.examName}
              </h3>
              <button onClick={() => setTruthTestModal(prev => ({ ...prev, show: false }))} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            {truthTestModal.loading ? (
              <div style={{ padding: '40px', textAlign: 'center', flex: 1 }}>
                <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Analyzing evaluations...
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', padding: '0 24px 24px', overflowY: 'auto', flex: 1 }}>
                
                {/* Metrics Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
                  <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>TRUTH ALIGNMENT RATE</span>
                    <span style={{ fontSize: '20px', fontWeight: 800, color: truthTestModal.data?.metrics?.alignmentRate >= 75 ? 'var(--success)' : (truthTestModal.data?.metrics?.alignmentRate >= 50 ? 'var(--warning)' : 'var(--danger)') }}>
                      {truthTestModal.data?.metrics?.alignmentRate || 0}%
                    </span>
                  </div>
                  <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>AVG PARENT OVERESTIMATE</span>
                    <span style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)' }}>
                      +{truthTestModal.data?.metrics?.avgParentOverestimate || 0} pts
                    </span>
                  </div>
                  <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>ANALYZED QUESTION PAIRS</span>
                    <span style={{ fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>
                      {truthTestModal.data?.metrics?.totalQuestionsAnalyzed || 0}
                    </span>
                  </div>
                  <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>PARENT HIGHER FLAGS</span>
                    <span style={{ fontSize: '20px', fontWeight: 800, color: truthTestModal.data?.metrics?.parentHigherCount > 0 ? 'var(--danger)' : 'var(--success)' }}>
                      {truthTestModal.data?.metrics?.parentHigherCount || 0}
                    </span>
                  </div>
                </div>

                {/* Search Bar */}
                <div style={{ display: 'flex', gap: '10px' }}>
                  <input
                    type="text"
                    className="form-control"
                    placeholder="🔍 Search by student name or question content..."
                    value={truthSearchText}
                    onChange={(e) => setTruthSearchText(e.target.value)}
                    style={{ flex: 1, padding: '8px 12px', fontSize: '12px', background: 'var(--bg-soft)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}
                  />
                </div>

                {/* Table */}
                <div className="table-responsive" style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', maxHeight: '350px', overflowY: 'auto' }}>
                  <table className="table" style={{ width: '100%', fontSize: '12px', borderCollapse: 'collapse', textAlign: 'left' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                        <th style={{ padding: '10px 14px', fontWeight: 700 }}>Student Name</th>
                        <th style={{ padding: '10px 14px', fontWeight: 700 }}>Question Prompt</th>
                        <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Home (Parent)</th>
                        <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Classroom (Peer)</th>
                        <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Variance (Δ)</th>
                        <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Truth Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      {(() => {
                        const filteredItems = (truthTestModal.data?.items || []).filter((item: any) => {
                          if (!truthSearchText) return true;
                          const s = truthSearchText.toLowerCase();
                          return (
                            item.studentName.toLowerCase().includes(s) ||
                            item.questionText.toLowerCase().includes(s)
                          );
                        });

                        if (filteredItems.length === 0) {
                          return (
                            <tr>
                              <td colSpan={6} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-faint)' }}>
                                📭 No matching question pairs found for this search.
                              </td>
                            </tr>
                          );
                        }

                        return filteredItems.map((item: any) => (
                          <tr key={item.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                            <td style={{ padding: '10px 14px', fontWeight: 600 }}>{item.studentName}</td>
                            <td style={{ padding: '10px 14px', color: 'var(--text-muted)', maxWidth: '280px', wordBreak: 'break-word', whiteSpace: 'pre-line' }}>{item.questionText}</td>
                            <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 600 }}>{item.parentMarks} / {item.maxMarks}</td>
                            <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 600 }}>{item.peerMarks} / {item.maxMarks}</td>
                            <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: item.variance > 0.5 ? 'var(--danger)' : (item.variance < -0.5 ? 'var(--accent)' : 'var(--success)') }}>
                              {item.variance > 0 ? `+${item.variance}` : item.variance}
                            </td>
                            <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                              {item.status === 'aligned' && (
                                <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(46, 204, 113, 0.15)', color: '#2ecc71', border: '1px solid rgba(46, 204, 113, 0.3)' }}>
                                  Aligned
                                </span>
                              )}
                              {item.status === 'parent_higher' && (
                                <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(231, 76, 60, 0.15)', color: '#e74c3c', border: '1px solid rgba(231, 76, 60, 0.3)' }}>
                                  Parent Higher ⚠️
                                </span>
                              )}
                              {item.status === 'peer_higher' && (
                                <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(52, 152, 219, 0.15)', color: '#3498db', border: '1px solid rgba(52, 152, 219, 0.3)' }}>
                                  Classroom Higher
                                </span>
                              )}
                            </td>
                          </tr>
                        ));
                      })()}
                    </tbody>
                  </table>
                </div>

              </div>
            )}

            {/* Footer */}
            <div style={{ display: 'flex', justifyContent: 'flex-end', padding: '16px 24px', borderTop: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}>
              <button className="btn btn-secondary" onClick={() => setTruthTestModal(prev => ({ ...prev, show: false }))}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Student Practice History Details */}
      {selectedPracStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '750px', width: '100%', maxHeight: '85vh', overflowY: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
              <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
                📚 Practice History: {selectedPracStudent.name}
              </h3>
              <button onClick={() => setSelectedPracStudent(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {loadingPracHistory ? (
                <div style={{ textAlign: 'center', padding: '20px' }}>
                  <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading history details...
                </div>
              ) : pracHistory.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '20px', color: 'var(--text-faint)' }}>
                  📭 No practice logs found for this student.
                </div>
              ) : (() => {
                const groupedPrac = new Map<string, Map<string, any[]>>();
                pracHistory.forEach(h => {
                  const sName = h.subject || 'Other Subjects';
                  const cName = h.chapter || 'General';
                  if (!groupedPrac.has(sName)) {
                    groupedPrac.set(sName, new Map());
                  }
                  const chapters = groupedPrac.get(sName)!;
                  if (!chapters.has(cName)) {
                    chapters.set(cName, []);
                  }
                  chapters.get(cName)!.push(h);
                });

                const sortedSubjs = Array.from(groupedPrac.keys());

                const getSubjAvg = (sName: string) => {
                  const chapters = groupedPrac.get(sName)!;
                  const topics = Array.from(chapters.values()).flat();
                  if (topics.length === 0) return 0;
                  return topics.reduce((acc, t) => acc + (t.scorePercent || 0), 0) / topics.length;
                };

                const getChapAvg = (topics: any[]) => {
                  if (topics.length === 0) return 0;
                  return topics.reduce((acc, t) => acc + (t.scorePercent || 0), 0) / topics.length;
                };

                const getProgressCol = (pct: number) => {
                  if (pct < 40) return '#f44336';
                  if (pct < 70) return '#ff9800';
                  return '#4caf50';
                };

                const toggleModalSubject = (subjName: string) => {
                  const next = new Set(modalExpandedSubjects);
                  if (next.has(subjName)) next.delete(subjName);
                  else next.add(subjName);
                  setModalExpandedSubjects(next);
                };

                const toggleModalChapter = (subjName: string, chapterName: string) => {
                  const key = `${subjName}||${chapterName}`;
                  const next = new Set(modalExpandedChapters);
                  if (next.has(key)) next.delete(key);
                  else next.add(key);
                  setModalExpandedChapters(next);
                };

                return (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {sortedSubjs.map(subjName => {
                      const chapters = groupedPrac.get(subjName)!;
                      const allSubjTopics = Array.from(chapters.values()).flat();
                      const subjectMastery = getSubjAvg(subjName);
                      const isSubjExpanded = modalExpandedSubjects.has(subjName);
                      const subjProgressColor = getProgressCol(subjectMastery);

                      const sortedChapters = Array.from(chapters.keys());

                      return (
                        <div key={subjName} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', background: 'var(--surface)', overflow: 'hidden' }}>
                          <div 
                            onClick={() => toggleModalSubject(subjName)}
                            style={{ padding: '12px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                          >
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span style={{ fontWeight: 'bold', fontSize: '13px' }}>📖 {subjName}</span>
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({allSubjTopics.length} sessions)</span>
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                              <div style={{ width: '60px', height: '5px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div style={{ width: `${subjectMastery}%`, height: '100%', background: subjProgressColor }}></div>
                              </div>
                              <span style={{ fontSize: '11px', fontWeight: 600 }}>{Math.round(subjectMastery)}%</span>
                              <span style={{ fontSize: '9px', transform: isSubjExpanded ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>▼</span>
                            </div>
                          </div>

                          {isSubjExpanded && (
                            <div style={{ padding: '10px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                              {sortedChapters.map(chapterName => {
                                const topics = chapters.get(chapterName)!;
                                const chapterMastery = getChapAvg(topics);
                                const chapterKey = `${subjName}||${chapterName}`;
                                const isChExpanded = modalExpandedChapters.has(chapterKey);
                                const chProgressColor = getProgressCol(chapterMastery);

                                return (
                                  <div key={chapterName} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                                    <div 
                                      onClick={() => toggleModalChapter(subjName, chapterName)}
                                      style={{ padding: '10px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', borderBottom: isChExpanded ? '1px solid var(--border-light)' : 'none' }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                        <span style={{ fontSize: '8px', transform: isChExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.15s' }}>▶</span>
                                        <span style={{ fontWeight: 600, fontSize: '12px' }}>📘 {chapterName}</span>
                                        <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({topics.length})</span>
                                      </div>
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                        <div style={{ width: '50px', height: '4px', background: 'var(--border-light)', borderRadius: '2px', overflow: 'hidden' }}>
                                          <div style={{ width: `${chapterMastery}%`, height: '100%', background: chProgressColor }}></div>
                                        </div>
                                        <span style={{ fontSize: '10px', fontWeight: 600 }}>{Math.round(chapterMastery)}%</span>
                                      </div>
                                    </div>

                                    {isChExpanded && (() => {
                                      const sortedTopics = [...topics].sort((a, b) => {
                                        let cmp = 0;
                                        if (modalSortKey === 'name') {
                                          cmp = (a.name || a.topicName || '').localeCompare(b.name || b.topicName || '', undefined, { numeric: true, sensitivity: 'base' });
                                        } else if (modalSortKey === 'score') {
                                          cmp = (a.scorePercent || 0) - (b.scorePercent || 0);
                                        } else if (modalSortKey === 'date') {
                                          const da = a.date ? new Date(a.date).getTime() : (a.createdAt ? (a.createdAt.toDate ? a.createdAt.toDate().getTime() : new Date(a.createdAt).getTime()) : 0);
                                          const db = b.date ? new Date(b.date).getTime() : (b.createdAt ? (b.createdAt.toDate ? b.createdAt.toDate().getTime() : new Date(b.createdAt).getTime()) : 0);
                                          cmp = da - db;
                                        } else if (modalSortKey === 'integrity') {
                                          const getRank = (item: any) => {
                                            if (typeof item.integrityScore === 'number') return item.integrityScore;
                                            const lvl = item.suspiciousLevel || 'green';
                                            return lvl === 'green' ? 100 : (lvl === 'yellow' ? 50 : 0);
                                          };
                                          cmp = getRank(a) - getRank(b);
                                        }
                                        return modalSortDirection === 'asc' ? cmp : -cmp;
                                      });

                                      return (
                                        <div style={{ padding: '8px' }}>
                                          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '11px' }}>
                                            <thead>
                                              <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', textTransform: 'uppercase', height: '28px' }}>
                                                <th 
                                                  onClick={() => handleModalSort('name')}
                                                  title="Click to sort by Topic / Practice Name"
                                                  style={{ padding: '4px 6px', textAlign: 'left', cursor: 'pointer', userSelect: 'none' }}
                                                >
                                                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: modalSortKey === 'name' ? 'var(--primary)' : 'inherit' }}>
                                                    Topic / Practice Name
                                                    <span style={{ fontSize: '10px', opacity: modalSortKey === 'name' ? 1 : 0.35 }}>
                                                      {modalSortKey === 'name' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                    </span>
                                                  </span>
                                                </th>
                                                <th 
                                                  onClick={() => handleModalSort('score')}
                                                  title="Click to sort by Score"
                                                  style={{ padding: '4px 6px', textAlign: 'center', width: '65px', cursor: 'pointer', userSelect: 'none' }}
                                                >
                                                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'score' ? 'var(--primary)' : 'inherit' }}>
                                                    Score
                                                    <span style={{ fontSize: '10px', opacity: modalSortKey === 'score' ? 1 : 0.35 }}>
                                                      {modalSortKey === 'score' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                    </span>
                                                  </span>
                                                </th>
                                                <th 
                                                  onClick={() => handleModalSort('date')}
                                                  title="Click to sort by Date"
                                                  style={{ padding: '4px 6px', textAlign: 'center', width: '85px', cursor: 'pointer', userSelect: 'none' }}
                                                >
                                                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'date' ? 'var(--primary)' : 'inherit' }}>
                                                    Date
                                                    <span style={{ fontSize: '10px', opacity: modalSortKey === 'date' ? 1 : 0.35 }}>
                                                      {modalSortKey === 'date' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                    </span>
                                                  </span>
                                                </th>
                                                <th 
                                                  onClick={() => handleModalSort('integrity')}
                                                  title="Click to sort by Integrity Level"
                                                  style={{ padding: '4px 6px', textAlign: 'center', width: '65px', cursor: 'pointer', userSelect: 'none' }}
                                                >
                                                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'integrity' ? 'var(--primary)' : 'inherit' }}>
                                                    Integrity
                                                    <span style={{ fontSize: '10px', opacity: modalSortKey === 'integrity' ? 1 : 0.35 }}>
                                                      {modalSortKey === 'integrity' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                    </span>
                                                  </span>
                                                </th>
                                                <th style={{ padding: '4px 6px', textAlign: 'right', width: '80px', userSelect: 'none' }}>Action</th>
                                              </tr>
                                            </thead>
                                            <tbody>
                                              {sortedTopics.map((h, hIdx) => {
                                                const score = Math.round(h.scorePercent || 0);
                                                const level = h.suspiciousLevel || 'green';
                                                const dotCol = level === 'red' ? '#f44336' : (level === 'yellow' ? '#ff9800' : '#4caf50');

                                                return (
                                                  <tr key={h.id || hIdx} style={{ borderBottom: '1px solid var(--border-light)', height: '36px' }}>
                                                    <td style={{ padding: '4px 6px', fontWeight: 600 }}>
                                                      📍 {h.name}
                                                    </td>
                                                    <td style={{ padding: '4px 6px', textAlign: 'center', fontWeight: 'bold' }}>
                                                      <span style={{
                                                        color: score < 40 ? '#f44336' : (score < 70 ? '#ff9800' : '#4caf50'),
                                                        background: score < 40 ? 'rgba(244,67,54,0.1)' : (score < 70 ? 'rgba(255,152,0,0.1)' : 'rgba(76,175,80,0.1)'),
                                                        padding: '2px 6px',
                                                        borderRadius: '4px'
                                                      }}>
                                                        {score}%
                                                      </span>
                                                    </td>
                                                    <td style={{ padding: '4px 6px', textAlign: 'center', color: 'var(--text-muted)' }}>
                                                      {h.date ? new Date(h.date).toLocaleDateString('en-IN') : '-'}
                                                    </td>
                                                    <td style={{ padding: '4px 6px', textAlign: 'center' }}>
                                                      <span style={{ display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: dotCol }} title={`Integrity level: ${level}`} />
                                                    </td>
                                                    <td style={{ padding: '4px 6px', textAlign: 'right' }}>
                                                      <button 
                                                        onClick={() => loadScorecard(h.id, selectedPracStudent.studentCode)}
                                                        style={{ padding: '3px 10px', borderRadius: '20px', fontSize: '9px', fontWeight: 600, border: 'none', background: 'var(--accent-grad)', color: 'white', cursor: 'pointer' }}
                                                      >
                                                        Scorecard
                                                      </button>
                                                    </td>
                                                  </tr>
                                                );
                                              })}
                                            </tbody>
                                          </table>
                                        </div>
                                      );
                                    })()}
                                  </div>
                                );
                              })}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                );
              })()}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid var(--border-light)', paddingTop: '12px', marginTop: '8px' }}>
              <button className="btn btn-secondary" onClick={() => setSelectedPracStudent(null)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Student Topic Status Breakdown (🟢 🟡 🔴 dots click) */}
      {topicStatusModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '800px', width: '100%', maxHeight: '88vh', overflowY: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: 'var(--shadow-lg)' }}>
            
            {/* Modal Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '14px' }}>
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  {topicStatusModal.activeTab === 'mastered' ? '🟢 Mastered Topics' : 
                   topicStatusModal.activeTab === 'practicing' ? '🟡 In Progress Topics' :
                   topicStatusModal.activeTab === 'needsAttention' ? '🔴 Needs Attention Topics' : '🎯 All Topic Mastery'}: {topicStatusModal.student?.name}
                </h3>
                <span style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
                  Real-time Diagnostic Status
                </span>
              </div>
              <button 
                onClick={() => setTopicStatusModal(prev => ({ ...prev, show: false }))} 
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.3rem', color: 'var(--text-muted)' }}
              >
                ✕
              </button>
            </div>

            {/* Filter Tabs & Search Bar */}
            {topicStatusModal.data && (
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', gap: '6px', background: 'var(--bg-soft)', padding: '4px', borderRadius: '10px', border: '1px solid var(--border-light)' }}>
                  <button
                    onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'all' }))}
                    style={{
                      padding: '5px 12px',
                      borderRadius: '8px',
                      fontSize: '11px',
                      fontWeight: topicStatusModal.activeTab === 'all' ? 700 : 500,
                      border: 'none',
                      cursor: 'pointer',
                      background: topicStatusModal.activeTab === 'all' ? 'var(--surface)' : 'transparent',
                      color: topicStatusModal.activeTab === 'all' ? 'var(--text)' : 'var(--text-muted)',
                      boxShadow: topicStatusModal.activeTab === 'all' ? 'var(--shadow-sm)' : 'none'
                    }}
                  >
                    All ({(topicStatusModal.data.mastered.length + topicStatusModal.data.practicing.length + topicStatusModal.data.needsAttention.length)})
                  </button>
                  <button
                    onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'mastered' }))}
                    style={{
                      padding: '5px 12px',
                      borderRadius: '8px',
                      fontSize: '11px',
                      fontWeight: topicStatusModal.activeTab === 'mastered' ? 700 : 500,
                      border: 'none',
                      cursor: 'pointer',
                      background: topicStatusModal.activeTab === 'mastered' ? 'rgba(16,185,129,0.15)' : 'transparent',
                      color: topicStatusModal.activeTab === 'mastered' ? '#10b981' : 'var(--text-muted)',
                      boxShadow: topicStatusModal.activeTab === 'mastered' ? 'var(--shadow-sm)' : 'none'
                    }}
                  >
                    🟢 Mastered ({topicStatusModal.data.mastered.length})
                  </button>
                  <button
                    onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'practicing' }))}
                    style={{
                      padding: '5px 12px',
                      borderRadius: '8px',
                      fontSize: '11px',
                      fontWeight: topicStatusModal.activeTab === 'practicing' ? 700 : 500,
                      border: 'none',
                      cursor: 'pointer',
                      background: topicStatusModal.activeTab === 'practicing' ? 'rgba(217,119,6,0.15)' : 'transparent',
                      color: topicStatusModal.activeTab === 'practicing' ? '#d97706' : 'var(--text-muted)',
                      boxShadow: topicStatusModal.activeTab === 'practicing' ? 'var(--shadow-sm)' : 'none'
                    }}
                  >
                    🟡 In Progress ({topicStatusModal.data.practicing.length})
                  </button>
                  <button
                    onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'needsAttention' }))}
                    style={{
                      padding: '5px 12px',
                      borderRadius: '8px',
                      fontSize: '11px',
                      fontWeight: topicStatusModal.activeTab === 'needsAttention' ? 700 : 500,
                      border: 'none',
                      cursor: 'pointer',
                      background: topicStatusModal.activeTab === 'needsAttention' ? 'rgba(239,68,68,0.15)' : 'transparent',
                      color: topicStatusModal.activeTab === 'needsAttention' ? '#ef4444' : 'var(--text-muted)',
                      boxShadow: topicStatusModal.activeTab === 'needsAttention' ? 'var(--shadow-sm)' : 'none'
                    }}
                  >
                    🔴 Needs Care ({topicStatusModal.data.needsAttention.length})
                  </button>
                </div>

                <input 
                  type="text"
                  placeholder="Search topic or chapter..."
                  value={topicStatusModal.searchText}
                  onChange={(e) => setTopicStatusModal(prev => ({ ...prev, searchText: e.target.value }))}
                  style={{
                    padding: '6px 12px',
                    fontSize: '11.5px',
                    borderRadius: '8px',
                    border: '1px solid var(--border-light)',
                    background: 'var(--bg-soft)',
                    color: 'var(--text)',
                    minWidth: '180px'
                  }}
                />
              </div>
            )}

            {/* Modal Body */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', minHeight: '150px' }}>
              {topicStatusModal.loading ? (
                <div style={{ textAlign: 'center', padding: '40px 20px' }}>
                  <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
                  <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Loading student topic breakdown & learning explanations...</div>
                </div>
              ) : !topicStatusModal.data ? (
                <div style={{ textAlign: 'center', padding: '30px', color: 'var(--text-faint)' }}>
                  Failed to load topic status data.
                </div>
              ) : (() => {
                let list = topicStatusModal.activeTab === 'mastered' 
                  ? topicStatusModal.data.mastered 
                  : topicStatusModal.activeTab === 'practicing'
                  ? topicStatusModal.data.practicing
                  : topicStatusModal.activeTab === 'needsAttention'
                  ? topicStatusModal.data.needsAttention
                  : [
                      ...topicStatusModal.data.needsAttention,
                      ...topicStatusModal.data.practicing,
                      ...topicStatusModal.data.mastered
                    ];

                if (topicStatusModal.searchText.trim()) {
                  const q = topicStatusModal.searchText.toLowerCase();
                  list = list.filter(t => 
                    (t.topicName || '').toLowerCase().includes(q) ||
                    (t.chapterName || '').toLowerCase().includes(q) ||
                    (t.subjectName || '').toLowerCase().includes(q) ||
                    (t.topicCode || '').toLowerCase().includes(q)
                  );
                }

                if (list.length === 0) {
                  return (
                    <div style={{ textAlign: 'center', padding: '36px', color: 'var(--text-muted)' }}>
                      📭 No topics found under this status filter.
                    </div>
                  );
                }

                return (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    {list.map((t, idx) => {
                      const isMastered = t.state === 'mastered';
                      const isPracticing = t.state === 'continuePractice' || t.state === 'revision';
                      const statusColor = isMastered ? '#10b981' : isPracticing ? '#f59e0b' : '#ef4444';
                      const statusBg = isMastered ? 'rgba(16,185,129,0.06)' : isPracticing ? 'rgba(245,158,11,0.06)' : 'rgba(239,68,68,0.06)';
                      const statusBorder = isMastered ? 'rgba(16,185,129,0.25)' : isPracticing ? 'rgba(245,158,11,0.25)' : 'rgba(239,68,68,0.25)';

                      return (
                        <div 
                          key={t.topicCode || idx}
                          style={{
                            border: `1px solid ${statusBorder}`,
                            borderRadius: 'var(--radius)',
                            background: statusBg,
                            padding: '14px 16px',
                            display: 'flex',
                            flexDirection: 'column',
                            gap: '8px',
                            transition: 'transform 0.15s, box-shadow 0.15s'
                          }}
                        >
                          {/* Top row: Subject / Chapter badge & Mastery Pill */}
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                              <span style={{ fontSize: '10px', fontWeight: 700, padding: '2px 7px', borderRadius: '4px', background: 'var(--surface)', border: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                                📘 {t.subjectName} • {t.chapterName}
                              </span>
                              <span style={{ fontSize: '10px', color: 'var(--text-faint)' }}>
                                Code: {t.topicCode}
                              </span>
                            </div>

                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span style={{
                                fontSize: '11px',
                                fontWeight: 800,
                                color: statusColor,
                                background: 'var(--surface)',
                                padding: '2px 8px',
                                borderRadius: '6px',
                                border: `1px solid ${statusBorder}`
                              }}>
                                {t.mastery}% Accuracy
                              </span>
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                                {t.practiceCount}/5 Practices ({t.attempts} Qs)
                              </span>
                            </div>
                          </div>

                          {/* Topic Name */}
                          <div style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--text)' }}>
                            📍 {t.topicName}
                          </div>

                          {/* Student Explanation Banner */}
                          <div style={{
                            display: 'flex',
                            alignItems: 'flex-start',
                            gap: '8px',
                            padding: '8px 12px',
                            borderRadius: '8px',
                            background: 'var(--surface)',
                            border: `1px solid var(--border-light)`,
                            fontSize: '11.5px',
                            color: t.expColor || statusColor,
                            lineHeight: 1.5
                          }}>
                            <span style={{ fontSize: '14px', flexShrink: 0 }}>{t.expIcon}</span>
                            <div>
                              <strong style={{ display: 'block', fontSize: '10.5px', textTransform: 'uppercase', letterSpacing: '0.5px', opacity: 0.8, marginBottom: '1px' }}>
                                Explanation shown to student:
                              </strong>
                              {t.expText}
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                );
              })()}
            </div>

            {/* Modal Footer */}
            <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid var(--border-light)', paddingTop: '14px', marginTop: '4px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => setTopicStatusModal(prev => ({ ...prev, show: false }))}
              >
                Close
              </button>
            </div>

          </div>
        </div>
      )}

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
