'use client';

import React, { useEffect, useState, useMemo, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, parseAnswerList, isOptionSelectedByUser, isOptionCorrect, getQuestionCorrectAnswer, getRawOptionKey, getRawOptionText, isBlank } from '@/lib/questionTypes';
import { playNotificationSound } from '@/lib/audioUtils';

interface Attempt {
  id: string;
  studentCode: string;
  studentName: string;
  score: number;
  totalMarks: number;
  percentage: number;
  tabViolations: number;
  proctoringViolations?: {
    noFace?: number;
    multipleFaces?: number;
    lookingAway?: number;
    headMovement?: number;
  };
  wrongAnswers?: any[];
  unattemptedQuestions?: string[];
  questionDetails?: any[];
  startedAt: string | null;
  completedAt: string | null;
  status: string;
  reviewedAt?: string | null;
  durationSpent?: number;
  wrongAnswerReasons?: any;
  proctoringViolationTriggered?: boolean;
  abandoned?: boolean;
  micAvailable?: boolean;
  violations?: any;
}

interface Exam {
  id: string;
  name: string;
  subject?: string;
  subjectName?: string;
  chapter?: string;
  chapterNumber?: string;
  topicCodes?: string[];
  topicNames?: string[];
  totalMarks?: number;
  questions?: string[];
  questionCodes?: string[];
}

interface Student {
  id: string;
  studentCode: string;
  name: string;
  batchId: string | null;
  batchIds: string[];
  autonomous?: boolean;
  lastLoginAt?: string | null;
  lastActiveAt?: string | null;
}

interface Batch {
  id: string;
  name: string;
}

function formatAbsentLogin(lastLoginAt?: string | null) {
  if (!lastLoginAt) return '(Never Logged In)';
  try {
    const loginDate = new Date(lastLoginAt);
    const today = new Date();
    const isToday = loginDate.getDate() === today.getDate() &&
                    loginDate.getMonth() === today.getMonth() &&
                    loginDate.getFullYear() === today.getFullYear();
    const timeStr = loginDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    if (isToday) {
      return `(Login: ${timeStr})`;
    }
    const dateStr = loginDate.toLocaleDateString([], { month: 'short', day: 'numeric' });
    return `(Login: ${dateStr}, ${timeStr})`;
  } catch (e) {
    return '(Never Logged In)';
  }
}

function ExamReportContent() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();

  const examId = searchParams.get('examId') || '';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [exam, setExam] = useState<Exam | null>(null);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [students, setStudents] = useState<Student[]>([]);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [assignments, setAssignments] = useState<any[]>([]);
  const [questionsMap, setQuestionsMap] = useState<{ [key: string]: any }>({});
  const [broadcastingNotices, setBroadcastingNotices] = useState(false);

  // Sorting / Filtering states
  const [studentSortCol, setStudentSortCol] = useState('score');
  const [studentSortDir, setStudentSortDir] = useState<'asc' | 'desc'>('desc');
  const [activeFilter, setActiveFilter] = useState<'all' | 'pending' | 'flagged' | null>(null);
  const [filterLabel, setFilterLabel] = useState('');
  const [questionSortMode, setQuestionSortMode] = useState<'order' | 'correct' | 'incorrect' | 'unanswered'>('order');

  // Modal active states
  const [notStartedOpen, setNotStartedOpen] = useState(false);
  const [studentModalOpen, setStudentModalOpen] = useState(false);
  const [selectedAttempt, setSelectedAttempt] = useState<Attempt | null>(null);
  const [questionFilterTab, setQuestionFilterTab] = useState<'all' | 'correct' | 'incorrect' | 'unanswered'>('all');
  const [questionModalOpen, setQuestionModalOpen] = useState(false);
  const [activeQuestionStat, setActiveQuestionStat] = useState<any>(null);
  const [votersModalOpen, setVotersModalOpen] = useState(false);
  const [votersList, setVotersList] = useState<string[]>([]);
  const [votersTitle, setVotersTitle] = useState('');

  // Re-scoring modal states
  const [editAnswerOpen, setEditAnswerOpen] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState<any>(null);
  const [selectedCorrectOption, setSelectedCorrectOption] = useState('');
  const [savingAnswer, setSavingAnswer] = useState(false);

  // PDF Section selector states
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);
  const [exportStats, setExportStats] = useState(true);
  const [exportRoster, setExportRoster] = useState(true);
  const [exportCards, setExportCards] = useState(true);

  // Individual Reassignment states
  const [reassignModalOpen, setReassignModalOpen] = useState(false);
  const [reassignSelectedStudents, setReassignSelectedStudents] = useState<Set<string>>(new Set());
  const [reassignOpenMode, setReassignOpenMode] = useState<'immediate' | 'scheduled'>('immediate');
  const [reassignStartAtStr, setReassignStartAtStr] = useState('');
  const [reassignEndAtStr, setReassignEndAtStr] = useState('');
  const [reassignAttemptLimit, setReassignAttemptLimit] = useState(1);
  const [reassignDuration, setReassignDuration] = useState(30);
  const [reassignLateEntryRestriction, setReassignLateEntryRestriction] = useState(true);
  const [reassigning, setReassigning] = useState(false);

  const toLocalISOString = (date: Date) => {
    const tzoffset = date.getTimezoneOffset() * 60000;
    const localISOTime = (new Date(date.getTime() - tzoffset)).toISOString().slice(0, 16);
    return localISOTime;
  };

  const openReassignModal = () => {
    setReassignDuration(exam?.totalMarks ? (exam as any).duration || 30 : 30);
    setReassignAttemptLimit(1);
    setReassignOpenMode('immediate');
    setReassignLateEntryRestriction(true);
    
    const now = new Date();
    const oneHourLater = new Date(now.getTime() + 60 * 60 * 1000);
    setReassignStartAtStr(toLocalISOString(now));
    setReassignEndAtStr(toLocalISOString(oneHourLater));
    
    setReassignModalOpen(true);
  };

  // Dynamically load KaTeX and auto-render math equations on state changes
  useMathRender([loading, attempts, questionSortMode, studentModalOpen, editAnswerOpen, questionFilterTab, reassignModalOpen]);

  const { totalQuestionsCount, correctCount, incorrectCount, unansweredCount } = useMemo(() => {
    if (!selectedAttempt) return { totalQuestionsCount: 0, correctCount: 0, incorrectCount: 0, unansweredCount: 0 };
    const qDetails = selectedAttempt.questionDetails || [];
    const total = qDetails.length;
    let correct = 0;
    let incorrect = 0;
    let unanswered = 0;
    for (const qd of qDetails) {
      if (isBlank(qd)) {
        unanswered++;
      } else if (qd.isCorrect) {
        correct++;
      } else {
        incorrect++;
      }
    }
    return { totalQuestionsCount: total, correctCount: correct, incorrectCount: incorrect, unansweredCount: unanswered };
  }, [selectedAttempt]);

  const filteredQDs = useMemo(() => {
    if (!selectedAttempt) return [];
    const qDetails = selectedAttempt.questionDetails || [];
    return qDetails.filter((qd: any) => {
      const blank = isBlank(qd);
      if (questionFilterTab === 'correct') return qd.isCorrect && !blank;
      if (questionFilterTab === 'incorrect') return !qd.isCorrect && !blank;
      if (questionFilterTab === 'unanswered') return blank;
      return true;
    });
  }, [selectedAttempt, questionFilterTab]);

  const fetchReport = async () => {
    if (!firebaseUser || !examId) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/exams/objective?examId=${examId}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to retrieve objective exam report.');
      const data = await res.json();
      const examData = data.exam || {};
      if (examData) {
        examData.subject = examData.subject || (examData.subjects && examData.subjects[0]) || examData.subjectCode || '';
        examData.questions = examData.questions || examData.questionCodes || data.questions || [];
      }
      setExam(examData);
      setAttempts(data.attempts || []);
      setStudents(data.students || []);
      setBatches(data.batches || []);
      setAssignments(data.assignments || []);

      const qMap: { [key: string]: any } = {};
      (data.questions || []).forEach((q: any) => {
        qMap[q.id || q.questionCode] = q;
      });
      setQuestionsMap(qMap);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred fetching report.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (examId && firebaseUser) {
      fetchReport();
    }
  }, [firebaseUser, examId]);

  // Helper calculations
  const totalViolations = (r: Attempt) => {
    const pv = r.proctoringViolations || {};
    return (
      (r.tabViolations || 0) +
      (pv.noFace || 0) +
      (pv.multipleFaces || 0) +
      (pv.lookingAway || 0) +
      (pv.headMovement || 0)
    );
  };

  const getReviewTimeTaken = (r: Attempt) => {
    return Array.isArray(r.questionDetails) && r.questionDetails.length
      ? r.questionDetails.reduce((sum, qd) => sum + (qd.timeSpentSeconds || 0), 0)
      : (r.durationSpent || 0);
  };

  const getStudentBatchName = (studentCode: string) => {
    const s = students.find(x => x.studentCode === studentCode);
    if (!s) return 'No Batch';
    const bId = s.batchIds?.[0] || s.batchId;
    if (!bId) return 'No Batch';
    return batches.find(b => b.id === bId)?.name || bId;
  };

  const getStudentReasonForQuestion = (attempt: Attempt, qd: any) => {
    if (!attempt || !attempt.questionDetails) return null;
    const isAtt = (x: any) => x.isAttempted !== undefined ? Boolean(x.isAttempted) : Boolean(x.isCorrect || (!isBlank(x.userAnswer) && x.userAnswer !== ''));
    const wrongQs = attempt.questionDetails.filter((x: any) => isAtt(x) && !x.isCorrect);
    const unattemptedQs = attempt.questionDetails.filter((x: any) => !isAtt(x));
    const qdIsAtt = isAtt(qd);
    
    let globalIdx = -1;
    if (qdIsAtt && !qd.isCorrect) {
      globalIdx = wrongQs.findIndex((x: any) => x.questionCode === qd.questionCode);
    } else if (!qdIsAtt) {
      globalIdx = wrongQs.length + unattemptedQs.findIndex((x: any) => x.questionCode === qd.questionCode);
    }
    
    if (globalIdx !== -1 && attempt.wrongAnswerReasons) {
      return attempt.wrongAnswerReasons[globalIdx] || null;
    }
    return null;
  };



  const getOptionText = (questionCode: string, ansInput: any) => {
    const q = questionsMap[questionCode];
    const list = parseAnswerList(ansInput);
    if (list.length === 0) return '(blank)';
    if (!q || !q.options || !Array.isArray(q.options)) return list.join(', ');

    const matchedTexts: string[] = [];
    list.forEach(item => {
      let foundText = '';
      if (item.length === 1 && item.toUpperCase() >= 'A' && item.toUpperCase() <= 'Z') {
        const codeIndex = item.toUpperCase().charCodeAt(0) - 65;
        if (codeIndex >= 0 && codeIndex < q.options.length) {
          const optVal = q.options[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? ((optVal as any).text || (optVal as any).code || item) : String(optVal);
        }
      }
      if (!foundText && /^\d+$/.test(item)) {
        const codeIndex = parseInt(item, 10);
        if (codeIndex >= 0 && codeIndex < q.options.length) {
          const optVal = q.options[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? ((optVal as any).text || (optVal as any).code || item) : String(optVal);
        }
      }
      if (!foundText) {
        const opt = q.options.find((o: any) => {
          if (o && typeof o === 'object') return o.code === item || o.text === item;
          return String(o) === item;
        });
        if (opt) {
          foundText = (opt && typeof opt === 'object') ? ((opt as any).text || (opt as any).code || item) : String(opt);
        }
      }
      matchedTexts.push(foundText || item);
    });

    return matchedTexts.join(', ');
  };

  // Calculate assigned but not started students CORRECTLY
  const startedCodes = new Set(attempts.map(r => r.studentCode).filter(Boolean));
  const assignedCodes = new Set<string>();

  assignments.forEach(ba => {
    (ba.targetStudents || []).forEach((code: string) => assignedCodes.add(code));
    const targetBatches = ba.targetBatches || [];
    if (targetBatches.length > 0) {
      students.forEach(s => {
        const sBatchIds = s.batchIds && s.batchIds.length ? s.batchIds : (s.batchId ? [s.batchId] : []);
        if (s.studentCode && sBatchIds.some((b: string) => targetBatches.includes(b))) {
          assignedCodes.add(s.studentCode);
        }
      });
    }
  });

  const notStartedStudents: { code: string; name: string; lastLoginAt?: string | null; lastActiveAt?: string | null }[] = [];
  Array.from(assignedCodes).forEach(code => {
    if (!startedCodes.has(code)) {
      const s = students.find(x => x.studentCode === code);
      if (s) {
        notStartedStudents.push({ 
          code, 
          name: s.name,
          lastLoginAt: s.lastLoginAt,
          lastActiveAt: s.lastActiveAt
        });
      }
    }
  });

  const avgPercentage = attempts.length > 0
    ? Math.round(attempts.reduce((sum, a) => sum + a.percentage, 0) / attempts.length)
    : 0;

  const totalFlaggedCount = attempts.filter(r => totalViolations(r) > 0).length;
  const pendingCount = attempts.filter(r => r.status === 'pending').length;

  // Question stats breakdown builder
  const perQuestionStats: { [key: string]: any } = {};

  // 1. Pre-populate all exam questions so Question Insight Cards render even with 0 attempts
  const examQuestionList = exam?.questionCodes || exam?.questions || Object.keys(questionsMap) || [];
  examQuestionList.forEach((qItem: any, idx: number) => {
    const qKey = typeof qItem === 'string' ? qItem : (qItem?.questionCode || qItem?.id || `q_${idx}`);
    const bq = questionsMap[qKey] || (typeof qItem === 'object' ? qItem : null);
    if (!perQuestionStats[qKey]) {
      perQuestionStats[qKey] = {
        idx,
        questionText: bq?.text || bq?.questionText || `Question ${idx + 1}`,
        correct: 0,
        incorrect: 0,
        unanswered: 0,
        totalTime: 0,
        timedCount: 0,
        options: bq?.options || null,
        correctAnswer: bq?.correctAnswer || bq?.correctAnswers?.[0] || '',
        explanation: bq?.solution || bq?.explanation || '',
        questionCode: qKey,
        optionVotes: {},
        students: []
      };
    }
  });

  // 2. Aggregate attempt metrics on top of pre-populated questions
  attempts.forEach(r => {
    const label = r.studentName || r.studentCode || 'Unknown';
    if (Array.isArray(r.questionDetails) && r.questionDetails.length) {
      r.questionDetails.forEach((qd, idx) => {
        const key = qd.questionCode || examQuestionList[idx] || `q_${idx}`;
        if (!perQuestionStats[key]) {
          const bq = questionsMap[key] || null;
          perQuestionStats[key] = {
            idx,
            questionText: qd.questionText || bq?.text || `Question ${idx + 1}`,
            correct: 0,
            incorrect: 0,
            unanswered: 0,
            totalTime: 0,
            timedCount: 0,
            options: bq?.options || null,
            correctAnswer: bq?.correctAnswer || qd.correctAnswer || '',
            explanation: bq?.solution || '',
            questionCode: key,
            optionVotes: {},
            students: []
          };
        }
        const stat = perQuestionStats[key];
        const isActuallyAttempted = qd.isAttempted !== undefined
          ? Boolean(qd.isAttempted)
          : Boolean(qd.isCorrect || (!isBlank(qd.userAnswer) && qd.userAnswer !== ''));

        let status = 'unanswered';
        if (!isActuallyAttempted) {
          stat.unanswered++;
        } else if (qd.isCorrect) {
          stat.correct++;
          status = 'correct';
        } else {
          stat.incorrect++;
          status = 'incorrect';
        }
        if (qd.timeSpentSeconds) {
          stat.totalTime += qd.timeSpentSeconds;
          stat.timedCount++;
        }
        stat.students.push({ name: label, status, timeSpentSeconds: qd.timeSpentSeconds || 0 });

        // Option votes tracking
        if (isActuallyAttempted && stat.options) {
          let selected: string[] = [];
          try {
            const parsed = JSON.parse(qd.userAnswer);
            selected = Array.isArray(parsed) ? parsed : [qd.userAnswer];
          } catch {
            selected = [qd.userAnswer];
          }
          selected.forEach(ans => {
            const answerStr = String(ans).trim();
            let targetOptionKey = answerStr;
            
            if (Array.isArray(stat.options)) {
              let foundIndex = stat.options.findIndex((opt: any) => {
                const optCode = getRawOptionKey(opt);
                const optText = getRawOptionText(opt);
                return optCode === answerStr || optText === answerStr || String(opt) === answerStr;
              });
              
              if (foundIndex === -1 && /^[A-Z]$/i.test(answerStr)) {
                const letterIndex = answerStr.toUpperCase().charCodeAt(0) - 65;
                if (letterIndex >= 0 && letterIndex < stat.options.length) {
                  foundIndex = letterIndex;
                }
              }
              
              if (foundIndex === -1 && /^\d+$/.test(answerStr)) {
                const digitIndex = parseInt(answerStr, 10);
                if (digitIndex >= 0 && digitIndex < stat.options.length) {
                  foundIndex = digitIndex;
                }
              }
              
              if (foundIndex !== -1) {
                const opt = stat.options[foundIndex];
                targetOptionKey = getRawOptionKey(opt) || getRawOptionText(opt) || String(opt);
              }
            }
            
            const voteKey = targetOptionKey;
            if (!stat.optionVotes[voteKey]) {
              stat.optionVotes[voteKey] = { label: voteKey, count: 0, students: [] };
            }
            stat.optionVotes[voteKey].count++;
            stat.optionVotes[voteKey].students.push(label);
          });
        }
      });
    }
  });

  // Re-scoring save handler
  const handleSaveRescoredAnswer = async () => {
    if (!editingQuestion || !selectedCorrectOption) return;
    setSavingAnswer(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/exams/objective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId,
          action: 'rescore',
          questionId: editingQuestion.questionCode,
          newCorrectAnswer: selectedCorrectOption
        })
      });

      if (!res.ok) {
        throw new Error('Failed to update correct answer.');
      }

      alert('✅ Answer updated and all attempts re-scored!');
      setEditAnswerOpen(false);
      setEditingQuestion(null);
      await fetchReport();
    } catch (err: any) {
      alert(`❌ Failed to save: ${err.message}`);
    } finally {
      setSavingAnswer(false);
    }
  };

  // Resets attempts
  const handleResetAttempt = async (attemptId: string, studentName: string) => {
    if (!confirm(`Reset ${studentName}'s attempt for this exam?\n\nThis deletes their submitted result, undoes the mastery this exam contributed, and lets them take the exam again from scratch. This cannot be undone.`)) return;
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/exams/objective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          attemptId,
          action: 'delete'
        })
      });
      if (!res.ok) throw new Error('Reset request failed.');
      alert(`✅ ${studentName}'s attempt has been reset. They can now retake the exam.`);
      await fetchReport();
    } catch (err: any) {
      alert(`❌ Reset failed: ${err.message}`);
    }
  };

  const handleSaveReassignment = async () => {
    if (!firebaseUser || reassigning || !exam) return;
    const studentsArr = Array.from(reassignSelectedStudents);

    if (studentsArr.length === 0) {
      alert('Please select at least one student to reassign.');
      return;
    }

    if (reassignOpenMode !== 'immediate' && (!reassignStartAtStr || !reassignEndAtStr)) {
      alert('Please select start and end dates.');
      return;
    }

    if (reassignOpenMode !== 'immediate') {
      const now = new Date();
      const startDateTime = new Date(reassignStartAtStr);
      // Allow up to 10 minutes in the past for clock skew & form fill duration
      if (startDateTime.getTime() < now.getTime() - 10 * 60 * 1000) {
        alert('❌ Error: Cannot assign exams with a start date/time in the past.');
        return;
      }
      const endDateTime = new Date(reassignEndAtStr);
      if (endDateTime <= startDateTime) {
        alert('❌ Error: End datetime must be after start datetime.');
        return;
      }
    }

    setReassigning(true);

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId: exam.id,
          type: 'objective',
          targetType: 'student',
          targetBatches: [],
          targetStudents: studentsArr,
          openMode: reassignOpenMode,
          startAtStr: reassignStartAtStr,
          endAtStr: reassignEndAtStr,
          attemptLimit: reassignAttemptLimit,
          examDuration: reassignDuration,
          lateEntryRestriction: reassignLateEntryRestriction
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.message || 'Failed to reassign exam.');
      }

      alert('✅ Exam successfully reassigned to selected students!');
      setReassignModalOpen(false);
      setReassignSelectedStudents(new Set());
      await fetchReport();
    } catch (err: any) {
      alert(`❌ Reassignment failed: ${err.message}`);
    } finally {
      setReassigning(false);
    }
  };

  // Sorting attempts roster
  const getSortVal = (a: Attempt, col: string) => {
    if (col === 'name') return a.studentName.toLowerCase();
    if (col === 'batch') return getStudentBatchName(a.studentCode).toLowerCase();
    if (col === 'time') return getReviewTimeTaken(a);
    if (col === 'status') return a.status;
    if (col === 'date') return a.startedAt ? new Date(a.startedAt).getTime() : (a.completedAt ? new Date(a.completedAt).getTime() : 0);
    return a.percentage;
  };

  const filteredAttempts = attempts
    .filter(r => {
      if (!activeFilter || activeFilter === 'all') return true;
      if (activeFilter === 'pending') return r.status === 'pending';
      if (activeFilter === 'flagged') return totalViolations(r) > 0;
      return true;
    })
    .sort((a, b) => {
      const aVal = getSortVal(a, studentSortCol);
      const bVal = getSortVal(b, studentSortCol);
      const dir = studentSortDir === 'asc' ? 1 : -1;
      if (aVal < bVal) return -1 * dir;
      if (aVal > bVal) return 1 * dir;
      return 0;
    });

  const handleSortStudent = (col: string) => {
    if (studentSortCol === col) {
      setStudentSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setStudentSortCol(col);
      setStudentSortDir(col === 'score' || col === 'time' ? 'desc' : 'asc');
    }
  };

  // Question list sorting
  const questionsList = Object.entries(perQuestionStats).map(([key, val]) => ({ key, ...val }));
  if (questionSortMode === 'correct') {
    questionsList.sort((a, b) => b.correct - a.correct);
  } else if (questionSortMode === 'incorrect') {
    questionsList.sort((a, b) => b.incorrect - a.incorrect);
  } else if (questionSortMode === 'unanswered') {
    questionsList.sort((a, b) => b.unanswered - a.unanswered);
  } else {
    questionsList.sort((a, b) => a.idx - b.idx);
  }

  const formatSeconds = (sec: number) => {
    const mins = Math.floor(sec / 60);
    const remaining = sec % 60;
    return mins > 0 ? `${mins}m ${remaining}s` : `${remaining}s`;
  };

  const formatDate = (val: any) => {
    if (!val) return '—';
    const d = new Date(val);
    if (isNaN(d.getTime())) return '—';
    return d.toLocaleString('en-IN', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
  };

  const scoreColor = (pct: number) => {
    if (pct >= 80) return '#1aa54e';
    if (pct >= 60) return '#7cb305';
    if (pct >= 40) return '#e2a800';
    return '#e2483a';
  };

  // Clones chosen sections to a clean offscreen element for print-optimized A4 generation
  const runExportPDF = async () => {
    if (typeof window === 'undefined') return;

    // Load html2pdf dynamically if it is not already loaded
    const w = window as any;
    if (!w.html2pdf) {
      try {
        await new Promise<void>((resolve, reject) => {
          const s = document.createElement('script');
          s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
          s.onload = () => resolve();
          s.onerror = () => reject(new Error('Failed to load PDF library.'));
          document.head.appendChild(s);
        });
      } catch (err) {
        alert('Failed to load PDF library. Please check your network connection.');
        return;
      }
    }

    const printContainer = document.createElement('div');
    printContainer.id = 'pdf-print-container';
    printContainer.className = 'math-container';
    printContainer.style.cssText = 'font-family:Arial,sans-serif;background:#ffffff;color:#000000;padding:20px;';

    const styleOverride = document.createElement('style');
    styleOverride.innerHTML = `
      #pdf-print-container, #pdf-print-container *:not(.score-cell):not(.stat-val) {
        color: #000000 !important;
        text-shadow: none !important;
      }
      #pdf-print-container {
        background: #ffffff !important;
      }
      #pdf-print-container th {
        background: #f4f4f4 !important;
        color: #000000 !important;
      }
      #pdf-print-container td {
        border-bottom: 1px solid #eee !important;
      }
      #pdf-print-container .correct-option {
        background: rgba(26, 165, 78, 0.08) !important;
        border: 1.5px solid #1aa54e !important;
      }
      #pdf-print-container .explanation-box {
        background: #fffde7 !important;
        border: 1px solid #ffe082 !important;
      }
    `;
    printContainer.appendChild(styleOverride);

    // Title Header block
    const titleHeader = document.createElement('div');
    titleHeader.innerHTML = `
      <div style="border-bottom: 2px solid #000000; padding-bottom: 8px; margin-bottom: 20px; font-family: system-ui, sans-serif; text-align: center;">
        <h2 style="margin: 0; color: #1e40af; font-size: 20px; text-align: center;">YASHCOM Performance Analytics Report</h2>
        <div style="font-size: 13px; color: #333; margin-top: 6px; font-weight: bold; text-align: center;">
          Exam Name: ${exam?.name || examId} &nbsp;&nbsp;|&nbsp;&nbsp; Subject: ${exam?.subjectName || exam?.subject || '—'}
        </div>
        <div style="font-size: 11px; color: #555; margin-top: 4px; text-align: center;">
          Chapter: ${exam?.chapterNumber ? `${exam?.chapterNumber}. ${exam?.chapter || ''}` : (exam?.chapter || '—')} &nbsp;&nbsp;|&nbsp;&nbsp; Topic: ${exam?.topicNames?.join(', ') || exam?.topicCodes?.join(', ') || '—'} &nbsp;&nbsp;|&nbsp;&nbsp; Total Questions: ${exam?.questions?.length || 0} &nbsp;&nbsp;|&nbsp;&nbsp; Max Marks: ${exam?.totalMarks || 0}
        </div>
      </div>
    `;
    printContainer.appendChild(titleHeader);

    // 1st Section: Performance Stats Summary
    if (exportStats) {
      const statsSection = document.createElement('div');
      statsSection.style.marginBottom = '30px';
      statsSection.style.pageBreakInside = 'avoid';
      statsSection.style.breakInside = 'avoid';
      statsSection.innerHTML = `
        <h3 style="font-size: 13px; margin: 0 0 12px; text-transform: uppercase; color: #111; letter-spacing: 0.5px; font-family: system-ui, sans-serif; border-bottom: 1px solid #ddd; padding-bottom: 4px;">📊 Section 1: Performance Summary</h3>
        <div style="display: flex; gap: 10px; justify-content: space-between;">
          <div style="flex: 1; border: 1px solid #ccc; padding: 12px; border-radius: 6px; text-align: center; font-family: system-ui, sans-serif;">
            <div style="font-size: 22px; font-weight: 800;">${attempts.length}</div>
            <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 4px;">Submissions</div>
          </div>
          <div style="flex: 1; border: 1px solid #ccc; padding: 12px; border-radius: 6px; text-align: center; font-family: system-ui, sans-serif;">
            <div style="font-size: 22px; font-weight: 800; color: #555;">${notStartedStudents.length}</div>
            <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 4px;">Not Started</div>
          </div>
          <div style="flex: 1; border: 1px solid #ccc; padding: 12px; border-radius: 6px; text-align: center; font-family: system-ui, sans-serif;">
            <div class="stat-val" style="font-size: 22px; font-weight: 800; color: #1aa54e !important;">${avgPercentage}%</div>
            <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 4px;">Average Score</div>
          </div>
          <div style="flex: 1; border: 1px solid #ccc; padding: 12px; border-radius: 6px; text-align: center; font-family: system-ui, sans-serif;">
            <div class="stat-val" style="font-size: 22px; font-weight: 800; color: #e7a300 !important;">${pendingCount}</div>
            <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 4px;">Pending Review</div>
          </div>
          <div style="flex: 1; border: 1px solid #ccc; padding: 12px; border-radius: 6px; text-align: center; font-family: system-ui, sans-serif;">
            <div class="stat-val" style="font-size: 22px; font-weight: 800; color: #e2483a !important;">${totalFlaggedCount}</div>
            <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 4px;">Flagged Reviews</div>
          </div>
        </div>
      `;
      printContainer.appendChild(statsSection);
    }

    // 2nd Section: Student Submissions Roster
    if (exportRoster) {
      const rosterSection = document.createElement('div');
      rosterSection.style.marginBottom = '30px';

      let absentHtml = '';
      if (!activeFilter || activeFilter === 'all') {
        if (notStartedStudents.length > 0) {
          const sortedAbsent = [...notStartedStudents].sort((a, b) => a.name.localeCompare(b.name));
          const absentRows: any[][] = [];
          for (let i = 0; i < sortedAbsent.length; i += 3) {
            absentRows.push(sortedAbsent.slice(i, i + 3));
          }

          absentHtml = `
            <tr style="border-bottom: 1px solid #fee2e2; background: rgba(239, 68, 68, 0.08);">
              <td colspan="5" style="padding: 12px 10px; font-family: system-ui, sans-serif;">
                <div style="text-align: center; font-weight: 800; font-size: 14px; color: #dc2626 !important; margin-bottom: 8px;">
                  🔴 Absent Students (${notStartedStudents.length})
                </div>
                <table style="width: 100%; border-collapse: collapse; table-layout: fixed; border: none; margin: 0; padding: 0;">
                  <tbody>
                    ${absentRows.map(row => `
                      <tr>
                        ${[0, 1, 2].map(colIdx => {
                          const item = row[colIdx];
                          return `
                            <td style="width: 33.33%; padding: 4px 6px; border: none; font-size: 12px; font-weight: 700; color: #dc2626 !important; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; vertical-align: middle;">
                              ${item ? `• ${item.name} <span style="font-size: 9px; font-weight: normal; opacity: 0.85; color: #7f1d1d;">${formatAbsentLogin(item.lastLoginAt)}</span>` : ''}
                            </td>
                          `;
                        }).join('')}
                      </tr>
                    `).join('')}
                  </tbody>
                </table>
              </td>
            </tr>
          `;
        }
      }

      let rowsHtml = filteredAttempts.map(a => {
        const stud = students.find(s => s.studentCode === a.studentCode);
        const nameText = a.studentName + (stud?.autonomous ? ' ⭐' : '');
        const isPending = a.status === 'pending';
        const statusDate = a.reviewedAt || a.completedAt;
        const startDate = a.startedAt || a.completedAt;
        return `
          <tr style="border-bottom: 1px solid #eee; font-size: 11px; font-family: system-ui, sans-serif; height: 32px;">
            <td style="padding: 6px 8px; font-weight: 600; white-space: nowrap;">${nameText}</td>
            <td class="score-cell" style="padding: 6px 8px; font-weight: bold; color: ${scoreColor(a.percentage)} !important; white-space: nowrap;">${a.score} / ${a.totalMarks} (${a.percentage}%)</td>
            <td style="padding: 6px 8px; white-space: nowrap;">${formatSeconds(getReviewTimeTaken(a))}</td>
            <td style="padding: 6px 8px; white-space: nowrap;">
              <span style="font-size: 10px; padding: 2px 6px; border-radius: 8px; background: ${isPending ? '#fef3c7' : '#dbf3e1'}; color: ${isPending ? '#d97706' : '#1aa54e'}; font-weight: bold;">
                ${a.status}
              </span>
              <span style="font-size: 10px; color: #555; margin-left: 4px;">
                ${formatDate(statusDate)}
              </span>
            </td>
            <td style="padding: 6px 8px; color: #555; white-space: nowrap;">${formatDate(startDate)}</td>
          </tr>
        `;
      }).join('');

      if (filteredAttempts.length === 0 && notStartedStudents.length === 0) {
        rowsHtml = `<tr><td colspan="5" style="padding: 16px; text-align: center; color: #888; font-family: system-ui, sans-serif;">No attempts matching filters.</td></tr>`;
      }

      rosterSection.innerHTML = `
        <h3 style="font-size: 13px; margin: 0 0 12px; text-transform: uppercase; color: #111; letter-spacing: 0.5px; font-family: system-ui, sans-serif; border-bottom: 1px solid #ddd; padding-bottom: 4px;">👤 Section 2: Student Submissions</h3>
        <table style="width: 100%; border-collapse: collapse; text-align: left; border: 1px solid #ccc; border-radius: 4px; overflow: hidden;">
          <thead>
            <tr style="background: #f4f4f4; border-bottom: 1px solid #ccc; font-size: 11px; color: #444; height: 30px;">
              <th style="padding: 6px 8px; white-space: nowrap;">Student Name</th>
              <th style="padding: 6px 8px; white-space: nowrap;">Score</th>
              <th style="padding: 6px 8px; white-space: nowrap;">Time Taken</th>
              <th style="padding: 6px 8px; white-space: nowrap;">Status</th>
              <th style="padding: 6px 8px; white-space: nowrap;">Start Date/Time</th>
            </tr>
          </thead>
          <tbody>
            ${absentHtml}${rowsHtml}
          </tbody>
        </table>
      `;
      printContainer.appendChild(rosterSection);
    }

    // 3rd Section: Question Cards with Analysis
    if (exportCards) {
      const cardsSection = document.createElement('div');
      cardsSection.innerHTML = `
        <h3 style="font-size: 13px; margin: 0 0 15px; text-transform: uppercase; color: #111; letter-spacing: 0.5px; font-family: system-ui, sans-serif; border-bottom: 1px solid #ddd; padding-bottom: 4px;">📝 Section 3: Question Cards & Analysis</h3>
      `;

      questionsList.forEach((s, idx) => {
        const total = s.correct + s.incorrect + s.unanswered;
        const pctCorrect = total ? Math.round((s.correct / total) * 100) : 0;

        const cardDiv = document.createElement('div');
        cardDiv.className = 'math-container';
        cardDiv.style.border = '1px solid #ddd';
        cardDiv.style.padding = '14px';
        cardDiv.style.borderRadius = '6px';
        cardDiv.style.marginBottom = '14px';
        cardDiv.style.background = '#ffffff';
        cardDiv.style.pageBreakInside = 'avoid';
        cardDiv.style.breakInside = 'avoid';
        cardDiv.style.fontFamily = 'system-ui, sans-serif';

        // Options renderer
        let optionsHtml = '';
        if (s.options && s.options.length > 0) {
          optionsHtml = s.options.map((opt: any, oi: number) => {
            const optKey = getRawOptionKey(opt);
            const optText = getRawOptionText(opt);
            const vote = s.optionVotes[optKey] || { count: 0 };
            const isCorrectOpt = Array.isArray(s.correctAnswer)
              ? s.correctAnswer.includes(optKey)
              : s.correctAnswer === optKey;

            return `
              <div class="${isCorrectOpt ? 'correct-option' : ''}" style="display: flex; justify-content: space-between; align-items: center; padding: 6px 10px; margin-bottom: 4px; border: ${isCorrectOpt ? '1.5px solid #1aa54e' : '1px solid #eee'}; border-radius: 6px; background: ${isCorrectOpt ? 'rgba(26,165,78,0.05)' : '#ffffff'}; font-size: 11px;">
                <span>${isCorrectOpt ? '✅ ' : ''}${preprocessMathText(optText)}</span>
                <span style="background: #f4f4f4; border-radius: 12px; padding: 2px 8px; font-weight: bold; font-size: 10px;">${vote.count} votes</span>
              </div>
            `;
          }).join('');
        } else if (s.correctAnswer) {
          optionsHtml = `
            <div style="padding: 8px 12px; border: 1.5px solid #1aa54e; border-radius: 6px; background: rgba(26,165,78,0.05); font-size: 11px; font-weight: bold; margin-bottom: 6px;">
              ✅ Correct Answer: ${Array.isArray(s.correctAnswer) ? s.correctAnswer.join(', ') : s.correctAnswer}
            </div>
          `;
        }

        // Solution explanation builder
        let explHtml = '';
        if (s.explanation) {
          explHtml = `
            <div class="explanation-box" style="margin-top: 10px; padding: 8px 12px; border-radius: 6px; font-size: 11px; line-height: 1.4;">
              <strong>💡 Explanation:</strong> ${preprocessMathText(s.explanation)}
            </div>
          `;
        }

        cardDiv.innerHTML = `
          <div style="font-weight: 700; font-size: 12px; margin-bottom: 6px;">
            Q${(s.idx ?? idx) + 1}. ${preprocessMathText(s.questionText)}
          </div>
          <div style="height: 6px; border-radius: 3px; background: #eee; overflow: hidden; margin-bottom: 6px;">
            <div style="height: 100%; background: #1aa54e; width: ${pctCorrect}%;"></div>
          </div>
          <div style="font-size: 10px; color: #666; margin-bottom: 8px;">
            ✅ ${s.correct} correct &nbsp;•&nbsp; ❌ ${s.incorrect} incorrect &nbsp;•&nbsp; ➖ ${s.unanswered} unanswered
          </div>
          <div style="margin-bottom: 6px;">
            ${optionsHtml}
          </div>
          ${explHtml}
        `;
        cardsSection.appendChild(cardDiv);
      });

      printContainer.appendChild(cardsSection);
    }

    document.body.appendChild(printContainer);

    // Compile math formulas using KaTeX before pdf extraction
    // @ts-ignore
    const hasKatex = typeof window !== 'undefined' && !!window.renderMathInElement;
    if (hasKatex) {
      try {
        const preprocessEl = (el: any) => {
          const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
          let node;
          while ((node = walk.nextNode())) {
            let text = node.nodeValue || '';
            if (text) {
              let newText = text.replace(/(?<!\\)\(\[([^\]]+)\]\)/g, '\\([$1]\\)');
              newText = newText.replace(/(?<!\\)\(([^)]*?[\\^_][^)]*?)\)/g, '\\($1\\)');
              if (newText !== text) {
                node.nodeValue = newText;
              }
            }
          }
        };
        preprocessEl(printContainer);
        const containers = printContainer.querySelectorAll('.math-container');
        containers.forEach(preprocessEl);

        // @ts-ignore
        window.renderMathInElement(printContainer, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          throwOnError: false
        });
      } catch (e) {
        console.warn("Math rendering failed on cloned element", e);
      }
    }

    // Wait 500ms for browser layout paint and KaTeX math processing
    setTimeout(() => {
      // @ts-ignore
      const html2pdf = window.html2pdf;
      const opt = {
        margin:       [0.3, 0.4, 0.3, 0.4],
        filename:     `Exam_Report_${exam?.name || examId}.pdf`,
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2, useCORS: true },
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
      };

      html2pdf().from(printContainer).set(opt).save().then(() => {
        document.body.removeChild(printContainer);
        setPdfSelectorOpen(false);
      });
    }, 500);
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Generating performance scorecard...
        </div>
      </div>
    );
  }

  if (error || !exam) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '500px', textAlign: 'center' }}>
          {error || 'Objective exam not found.'}
        </div>
        <button className="btn btn-primary" onClick={() => router.push('/admin/exams')} style={{ marginTop: '20px' }}>Back to Exams</button>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>

      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800 }}>📊 YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Exam Report: {exam.name}</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
              Subject: {exam.subjectName || exam.subject || '—'} • Chapter: {exam.chapterNumber ? `${exam.chapterNumber}. ${exam.chapter || ''}` : (exam.chapter || '—')} • Topic: {exam.topicNames?.join(', ') || exam.topicCodes?.join(', ') || '—'} • Questions: {exam.questions?.length || 0} • Max Marks: {exam.totalMarks || 0}
            </div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        {/* Legacy-style Toolbar with Back & Export PDF & Broadcast Notices */}
        <div className="report-toolbar" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
          <button 
            className="btn btn-secondary" 
            onClick={() => router.push('/admin/exams')}
            style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '13px', fontWeight: 600 }}
          >
            ← Back to Exams
          </button>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button 
              className="btn btn-secondary" 
              disabled={broadcastingNotices}
              onClick={async () => {
                if (!confirm(`Are you sure you want to broadcast personalized result & absence notices to all assigned students and parents for exam '${exam.name}'?`)) return;
                setBroadcastingNotices(true);
                try {
                  const token = await firebaseUser!.getIdToken();
                  const res = await fetch('/api/admin/exams/broadcast-results', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({ examId })
                  });
                  const resData = await res.json();
                  if (!res.ok) throw new Error(resData.message || 'Failed to broadcast notices.');
                  playNotificationSound();
                  alert(`✅ ${resData.message || 'Exam result & absence notices dispatched successfully!'}`);
                } catch (err: any) {
                  alert(`❌ Error: ${err.message || 'Failed to dispatch notices'}`);
                } finally {
                  setBroadcastingNotices(false);
                }
              }}
              style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '13px', fontWeight: 600, background: 'rgba(139, 92, 246, 0.15)', color: '#8b5cf6', border: '1px solid rgba(139, 92, 246, 0.3)' }}
            >
              {broadcastingNotices ? '⏳ Broadcasting...' : '📢 Broadcast Results'}
            </button>
            <button 
              className="btn btn-primary" 
              onClick={() => setPdfSelectorOpen(true)}
              style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '13px', fontWeight: 600 }}
            >
              📄 Export PDF
            </button>
          </div>
        </div>

        {/* Live Interactive Content Area */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>

          {/* Clickable summary stats */}
          <div className="report-summary" style={{ display: 'flex', gap: '14px', flexWrap: 'wrap' }}>
            
            <div 
              className={`stat-summary-card ${activeFilter === 'all' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('all'); setFilterLabel('All Submissions'); }}
              style={{ flex: 1, minWidth: '130px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'all' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '16px', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '24px', fontWeight: 800 }}>{attempts.length}</div>
              <div className="stat-summary-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Submissions</div>
            </div>

            <div 
              className="stat-summary-card"
              onClick={() => setNotStartedOpen(true)}
              style={{ flex: 1, minWidth: '130px', cursor: 'pointer', background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '16px', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '24px', fontWeight: 800, color: 'var(--text-muted)' }}>{notStartedStudents.length}</div>
              <div className="stat-summary-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Not Started</div>
            </div>

            <div 
              className="stat-summary-card"
              style={{ flex: 1, minWidth: '130px', background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '16px', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '24px', fontWeight: 800 }}>{avgPercentage}%</div>
              <div className="stat-summary-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Average Score</div>
            </div>

            <div 
              className={`stat-summary-card ${activeFilter === 'pending' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('pending'); setFilterLabel('Pending Review'); }}
              style={{ flex: 1, minWidth: '130px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'pending' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '16px', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '24px', fontWeight: 800, color: 'var(--warning)' }}>{pendingCount}</div>
              <div className="stat-summary-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Pending Review</div>
            </div>

            <div 
              className={`stat-summary-card ${activeFilter === 'flagged' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('flagged'); setFilterLabel('Flagged (Proctoring)'); }}
              style={{ flex: 1, minWidth: '130px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'flagged' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '16px', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '24px', fontWeight: 800, color: 'var(--danger)' }}>{totalFlaggedCount}</div>
              <div className="stat-summary-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Flagged (Proctoring)</div>
            </div>

          </div>

          {/* Filter Notice banner */}
          {activeFilter && (
            <div style={{ background: 'var(--badge-bg)', border: '1px solid var(--badge-border)', padding: '10px 16px', borderRadius: 'var(--radius)', fontSize: '13px', color: 'var(--accent)', fontWeight: 600, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Showing: {filterLabel}</span>
              <button className="btn btn-secondary btn-sm" onClick={() => setActiveFilter(null)}>✕ Clear filter</button>
            </div>
          )}

          {/* Section: Individual Reassignment for Absent Cases */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>
                🔄 Individual Reassignment (Absent Cases)
              </h3>
              {notStartedStudents.length > 0 && (
                <span className="badge badge-danger" style={{ background: 'rgba(239, 68, 68, 0.15)', color: '#dc2626', fontWeight: 700, padding: '2px 8px', borderRadius: '10px', fontSize: '11px' }}>
                  {notStartedStudents.length} Absent
                </span>
              )}
            </div>
            
            {notStartedStudents.length === 0 ? (
              <div style={{ padding: '16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius)', fontSize: '13px', color: 'var(--text-muted)', textAlign: 'center' }}>
                🎉 All assigned students have started or completed the exam. No absent cases found.
              </div>
            ) : (
              <>
                <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: 0 }}>
                  Select absent students to schedule a make-up or reassign this exam specifically to them.
                </p>
                
                {/* Select All Toggle */}
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '4px' }}>
                  <input 
                    type="checkbox" 
                    id="reassign-select-all"
                    checked={reassignSelectedStudents.size === notStartedStudents.length}
                    onChange={(e) => {
                      if (e.target.checked) {
                        setReassignSelectedStudents(new Set(notStartedStudents.map(s => s.code)));
                      } else {
                        setReassignSelectedStudents(new Set());
                      }
                    }}
                    style={{ cursor: 'pointer' }}
                  />
                  <label htmlFor="reassign-select-all" style={{ fontSize: '12px', fontWeight: 'bold', cursor: 'pointer', userSelect: 'none' }}>
                    Select All ({notStartedStudents.length})
                  </label>
                </div>
                
                {/* Scrollable list of students */}
                <div style={{ maxHeight: '150px', overflowY: 'auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '8px', padding: '4px' }}>
                  {notStartedStudents.map(s => (
                    <label 
                      key={s.code} 
                      style={{ 
                        display: 'flex', 
                        alignItems: 'center', 
                        gap: '8px', 
                        padding: '8px 12px', 
                        background: 'var(--bg-soft)', 
                        borderRadius: 'var(--radius)', 
                        border: '1.5px solid var(--border-light)',
                        cursor: 'pointer',
                        fontSize: '12px',
                        fontWeight: 600,
                        userSelect: 'none',
                        transition: 'background 0.2s, border 0.2s'
                      }}
                      onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--surface)'; }}
                      onMouseLeave={(e) => { e.currentTarget.style.background = 'var(--bg-soft)'; }}
                    >
                      <input 
                        type="checkbox" 
                        checked={reassignSelectedStudents.has(s.code)}
                        onChange={() => {
                          const next = new Set(reassignSelectedStudents);
                          if (next.has(s.code)) {
                            next.delete(s.code);
                          } else {
                            next.add(s.code);
                          }
                          setReassignSelectedStudents(next);
                        }}
                        style={{ cursor: 'pointer' }}
                      />
                      <span style={{ textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{s.name}</span>
                    </label>
                  ))}
                </div>
                
                <div style={{ display: 'flex', justifyContent: 'flex-start', marginTop: '4px' }}>
                  <button 
                    className="btn btn-primary"
                    disabled={reassignSelectedStudents.size === 0}
                    onClick={openReassignModal}
                    style={{ fontSize: '12px', padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '6px' }}
                  >
                    🔄 Setup Reassignment ({reassignSelectedStudents.size})
                  </button>
                </div>
              </>
            )}
          </div>

          {/* Section A: Student Roster Grid */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, padding: '16px 20px 0', margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>👤 Student Submissions</h3>
            
            <div style={{ overflowX: 'auto', marginTop: '10px' }}>
              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                    <th onClick={() => handleSortStudent('name')} style={{ padding: '12px 16px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Student Name ⇅</th>
                    <th onClick={() => handleSortStudent('score')} style={{ padding: '12px 16px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Score ⇅</th>
                    <th onClick={() => handleSortStudent('time')} style={{ padding: '12px 16px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Time Taken ⇅</th>
                    <th onClick={() => handleSortStudent('status')} style={{ padding: '12px 16px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Status ⇅</th>
                    <th onClick={() => handleSortStudent('date')} style={{ padding: '12px 16px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Start Date/Time ⇅</th>
                    <th style={{ padding: '12px 16px', textAlign: 'right', whiteSpace: 'nowrap' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {/* Absent Students (pinned to top in red color, single merged row) */}
                  {(!activeFilter || activeFilter === 'all') && notStartedStudents.length > 0 && (
                    <tr 
                      style={{ borderBottom: '1px solid var(--border-light)', background: 'rgba(239, 68, 68, 0.08)' }}
                    >
                      <td colSpan={6} style={{ padding: '14px 16px', color: '#dc2626' }}>
                        <div style={{ textAlign: 'center', fontWeight: 800, fontSize: '14px', marginBottom: '10px', color: '#dc2626' }}>
                          🔴 Absent Students ({notStartedStudents.length})
                        </div>
                        <div style={{ 
                          display: 'grid', 
                          gridTemplateColumns: 'repeat(3, 1fr)', 
                          gap: '8px 16px',
                          fontSize: '13px',
                          fontWeight: 700,
                          color: '#dc2626'
                        }}>
                          {[...notStartedStudents]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(a => (
                              <div key={a.code} style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: '#dc2626', fontWeight: 700, fontSize: '13px' }} title={`${a.name} - ${formatAbsentLogin(a.lastLoginAt)}`}>
                                • {a.name}{' '}
                                <span style={{ fontSize: '10.5px', fontWeight: 400, opacity: 0.8, color: '#991b1b', marginLeft: '4px' }}>
                                  {formatAbsentLogin(a.lastLoginAt)}
                                </span>
                              </div>
                            ))
                          }
                        </div>
                      </td>
                    </tr>
                  )}

                  {/* Submitted Attempts */}
                  {filteredAttempts.length === 0 && ((activeFilter && activeFilter !== 'all') || notStartedStudents.length === 0) ? (
                    <tr>
                      <td colSpan={6} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>📭 No attempts matching the criteria.</td>
                    </tr>
                  ) : (
                    filteredAttempts.map(a => {
                      const vCount = totalViolations(a);
                      const isPending = a.status === 'pending';
                      const scoreVal = a.score || 0;
                      const statusDate = a.reviewedAt || a.completedAt;
                      const startDate = a.startedAt || a.completedAt;
                      return (
                        <tr 
                          key={a.id} 
                          className="student-row" 
                          onClick={() => { setSelectedAttempt(a); setStudentModalOpen(true); }}
                          style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer' }}
                        >
                          <td style={{ padding: '12px 16px', fontWeight: 600, whiteSpace: 'nowrap' }}>
                            {a.studentName}{students.find(s => s.studentCode === a.studentCode)?.autonomous ? ' ⭐' : ''}
                            {a.micAvailable === false && (
                              <span style={{ marginLeft: '6px', color: '#d97706', background: 'rgba(217, 119, 6, 0.1)', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Bypassed / Offline">
                                🎙️ Bypassed
                              </span>
                            )}
                            {vCount > 0 && (
                              <span style={{ marginLeft: '6px', color: 'var(--danger)', fontSize: '11px', fontWeight: 700 }} title={`${vCount} violations`}>
                                🚩 {vCount}
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 700, color: scoreColor(a.percentage), whiteSpace: 'nowrap' }}>
                            {scoreVal} / {a.totalMarks} ({a.percentage}%)
                          </td>
                          <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>{formatSeconds(getReviewTimeTaken(a))}</td>
                          <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>
                            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
                              <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: isPending ? '#fef3c7' : '#dbf3e1', color: isPending ? '#d97706' : '#1aa54e', fontWeight: 700 }}>
                                {a.status}
                              </span>
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 500 }}>
                                {formatDate(statusDate)}
                              </span>
                            </div>
                          </td>
                          <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>{formatDate(startDate)}</td>
                          <td style={{ padding: '12px 16px', textAlign: 'right', whiteSpace: 'nowrap' }} onClick={(e) => e.stopPropagation()}>
                            <button 
                              className="btn btn-secondary btn-sm" 
                              style={{ padding: '3px 8px', fontSize: '11px' }}
                              onClick={() => handleResetAttempt(a.id, a.studentName)}
                            >
                              🔄 Reset
                            </button>
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>

          {/* Section B: Auto-submitted Attempts */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, padding: '16px 20px 0', margin: 0, textTransform: 'uppercase', color: 'var(--danger)' }}>
              🚨 Auto-Submitted / Abandoned Attempts ({attempts.filter(a => a.proctoringViolationTriggered || a.abandoned).length})
            </h3>
            <div style={{ overflowX: 'auto', marginTop: '10px' }}>
              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                    <th style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>Student Name</th>
                    <th style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>Score</th>
                    <th style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>Tab Violations</th>
                    <th style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>Auto-Submission Reason</th>
                    <th style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>Date/Time</th>
                  </tr>
                </thead>
                <tbody>
                  {attempts.filter(a => a.proctoringViolationTriggered || a.abandoned).length === 0 ? (
                    <tr>
                      <td colSpan={5} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        🟢 No auto-submitted or abandoned attempts for this exam.
                      </td>
                    </tr>
                  ) : (
                    attempts.filter(a => a.proctoringViolationTriggered || a.abandoned).map(a => {
                      const scoreVal = typeof a.score === 'number' ? a.score : 0;
                      const completedAt = a.completedAt ? new Date(a.completedAt) : null;
                      
                      const getAutoSubmitReason = (attempt: Attempt) => {
                        if (attempt.abandoned) {
                          return "Closed exam window / reloaded page (Safeguard Trigger)";
                        }
                        if ((attempt.tabViolations || 0) >= 3) {
                          return "Exceeded allowed tab switches (3/3)";
                        }
                        const pv = attempt.proctoringViolations || {};
                        const noFace = pv.noFace || 0;
                        const multiple = pv.multipleFaces || 0;
                        const lookingAway = pv.lookingAway || 0;
                        if (noFace > 0 || multiple > 0 || lookingAway > 0) {
                          const parts = [];
                          if (noFace > 0) parts.push(`No Face (${noFace})`);
                          if (multiple > 0) parts.push(`Multiple Faces (${multiple})`);
                          if (lookingAway > 0) parts.push(`Looking Away (${lookingAway})`);
                          return `Proctoring violations: ${parts.join(', ')}`;
                        }
                        return "Integrity score threshold breach";
                      };

                      return (
                        <tr 
                          key={a.id} 
                          style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', transition: 'background 0.2s' }}
                          onClick={() => { setSelectedAttempt(a); setStudentModalOpen(true); }}
                          onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--bg-soft)'; }}
                          onMouseLeave={(e) => { e.currentTarget.style.background = 'transparent'; }}
                        >
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                            👤 {a.studentName}
                            {a.micAvailable === false && (
                              <span style={{ marginLeft: '6px', color: '#d97706', background: 'rgba(217, 119, 6, 0.1)', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Bypassed / Offline">
                                🎙️ Bypassed
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 700, color: 'var(--danger)' }}>
                            {a.abandoned ? '0 (Abandoned)' : `${scoreVal} / ${a.totalMarks} (${a.percentage}%)`}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 700 }}>
                            {a.abandoned ? '—' : `${a.tabViolations || 0} / 3`}
                          </td>
                          <td style={{ padding: '12px 16px', color: 'var(--danger)', fontWeight: 600 }}>
                            {getAutoSubmitReason(a)}
                          </td>
                          <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>
                            {completedAt ? completedAt.toLocaleString() : '—'}
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>

          {/* Section C: Detailed Questions Breakdown cards */}
          <div className="card" id="chipsCard" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
              <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>📝 Question Insight Cards</h3>
              
              <div style={{ display: 'flex', gap: '4px' }}>
                <button className={`btn btn-sm ${questionSortMode === 'order' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('order')} style={{ fontSize: '10px' }}>Order</button>
                <button className={`btn btn-sm ${questionSortMode === 'correct' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('correct')} style={{ fontSize: '10px' }}>Most Correct</button>
                <button className={`btn btn-sm ${questionSortMode === 'incorrect' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('incorrect')} style={{ fontSize: '10px' }}>Most Incorrect</button>
                <button className={`btn btn-sm ${questionSortMode === 'unanswered' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('unanswered')} style={{ fontSize: '10px' }}>Unanswered</button>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {questionsList.map((s, idx) => {
                const total = s.correct + s.incorrect + s.unanswered;
                const pctCorrect = total ? Math.round((s.correct / total) * 100) : 0;
                
                // Keep raw math strings intact for auto-render parsing on mount and updates
                const questionTextRaw = s.questionText;

                return (
                  <div 
                    key={s.key} 
                    className="card pq-card" 
                    style={{ background: 'var(--bg-soft)', borderLeft: '4px solid var(--accent)', padding: '16px', borderRadius: 'var(--radius)', border: '1.5px solid var(--border-light)', position: 'relative' }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px' }}>
                      <div style={{ fontWeight: 600, fontSize: '13px' }} className="math-container">
                        Q{(s.idx ?? idx) + 1}. {preprocessMathText(questionTextRaw)}
                      </div>
                      <button 
                        className="btn btn-secondary btn-sm" 
                        style={{ padding: '3px 10px', fontSize: '11px', flexShrink: 0 }}
                        onClick={() => {
                          setEditingQuestion(s);
                          setSelectedCorrectOption(s.correctAnswer);
                          setEditAnswerOpen(true);
                        }}
                      >
                        ✏️ Edit Answer
                      </button>
                    </div>

                    <div className="pq-bar-track" style={{ height: '6px', borderRadius: '3px', background: 'var(--bg)', overflow: 'hidden', marginTop: '8px' }}>
                      <div className="pq-bar-fill" style={{ height: '100%', background: '#1aa54e', width: `${pctCorrect}%` }}></div>
                    </div>

                    <div style={{ fontSize: '11px', margin: '8px 0 12px', color: 'var(--text-muted)' }}>
                      ✅ <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }} onClick={() => { setActiveQuestionStat(s); setQuestionModalOpen(true); }}>{s.correct} correct</span> &nbsp;•&nbsp;
                      ❌ <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }} onClick={() => { setActiveQuestionStat(s); setQuestionModalOpen(true); }}>{s.incorrect} incorrect</span> &nbsp;•&nbsp;
                      ➖ <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }} onClick={() => { setActiveQuestionStat(s); setQuestionModalOpen(true); }}>{s.unanswered} unanswered</span>
                    </div>

                    {/* Options breakdown votes */}
                    {s.options && s.options.length > 0 ? (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginBottom: '10px' }}>
                        {s.options.map((opt: any, oi: number) => {
                          const optKey = getRawOptionKey(opt);
                          const optText = getRawOptionText(opt);
                          const vote = s.optionVotes[optKey] || 
                                       s.optionVotes[optText] || 
                                       s.optionVotes[String(oi)] || 
                                       s.optionVotes[String.fromCharCode(65 + oi)] || 
                                       { count: 0, students: [] };
                          const isCorrectOpt = Array.isArray(s.correctAnswer)
                            ? s.correctAnswer.includes(optKey)
                            : s.correctAnswer === optKey;

                          return (
                            <div 
                              key={oi} 
                              style={{ 
                                display: 'flex', 
                                justifyContent: 'space-between', 
                                alignItems: 'center', 
                                padding: '6px 10px', 
                                border: isCorrectOpt ? '1.5px solid #1aa54e' : '1px solid var(--border-light)', 
                                borderRadius: '8px',
                                background: isCorrectOpt ? 'rgba(26,165,78,0.07)' : 'var(--surface)',
                                fontSize: '12px'
                              }}
                            >
                              <span className="math-container">{isCorrectOpt ? '✅ ' : ''}{preprocessMathText(optText)}</span>
                              <span 
                                className="pq-option-count" 
                                onClick={() => {
                                  setVotersTitle(`Option: ${optKey}`);
                                  setVotersList(vote.students || []);
                                  setVotersModalOpen(true);
                                }}
                                style={{ background: 'var(--bg-soft)', borderRadius: '12px', padding: '2px 10px', fontWeight: 700, cursor: 'pointer' }}
                              >
                                {vote.count}
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      s.correctAnswer && (
                        <div style={{ padding: '8px 12px', border: '1.5px solid #1aa54e', borderRadius: '8px', background: 'rgba(26,165,78,0.07)', fontSize: '12px', fontWeight: 600, marginBottom: '10px' }} className="math-container">
                          ✅ Correct Answer: {Array.isArray(s.correctAnswer) ? s.correctAnswer.join(', ') : String(s.correctAnswer)}
                        </div>
                      )
                    )}

                    {/* Explicit summary of the correct answer when options list is rendered */}
                    {s.options && s.options.length > 0 && s.correctAnswer && (
                      <div style={{ fontSize: '12px', color: '#1aa54e', fontWeight: 700, margin: '8px 0' }}>
                        ℹ️ Correct Answer: Option {Array.isArray(s.correctAnswer) ? s.correctAnswer.join(', ') : String(s.correctAnswer)}
                      </div>
                    )}

                    {/* Explanation / Solution block (Theme-aware styles) */}
                    {s.explanation ? (
                      <div 
                        className="pq-explanation math-container" 
                        style={{ 
                          marginTop: '10px', 
                          padding: '10px 12px', 
                          background: 'rgba(255, 255, 255, 0.05)', 
                          borderRadius: '8px', 
                          fontSize: '12px', 
                          color: 'var(--text)', 
                          border: '1px solid var(--border-light)' 
                        }}
                      >
                        <strong>💡 Explanation:</strong> {preprocessMathText(s.explanation)}
                      </div>
                    ) : (
                      s.correctAnswer && (
                        <div 
                          className="pq-explanation" 
                          style={{ 
                            marginTop: '10px', 
                            padding: '8px 12px', 
                            background: 'rgba(255, 255, 255, 0.02)', 
                            borderRadius: '8px', 
                            fontSize: '11px', 
                            color: 'var(--text-muted)', 
                            border: '1px solid var(--border-light)' 
                          }}
                        >
                          💡 No explanation mapped for this question.
                        </div>
                      )
                    )}
                  </div>
                );
              })}
            </div>
          </div>

        </div>

      </main>

      {/* Modal: PDF Section Selector */}
      {pdfSelectorOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800 }}>📄 Export Report to PDF</h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: 0 }}>Select the report sections you want to include in the exported PDF file:</p>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', margin: '10px 0' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer' }}>
                <input 
                  type="checkbox" 
                  checked={exportStats} 
                  onChange={(e) => setExportStats(e.target.checked)} 
                />
                <span>1st Section: Performance Stats Summary</span>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer' }}>
                <input 
                  type="checkbox" 
                  checked={exportRoster} 
                  onChange={(e) => setExportRoster(e.target.checked)} 
                />
                <span>2nd Section: Student Submissions Roster</span>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer' }}>
                <input 
                  type="checkbox" 
                  checked={exportCards} 
                  onChange={(e) => setExportCards(e.target.checked)} 
                />
                <span>3rd Section: Question Cards with Analysis</span>
              </label>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
              <button className="btn btn-secondary" onClick={() => setPdfSelectorOpen(false)}>Cancel</button>
              <button className="btn btn-primary" onClick={runExportPDF} disabled={!exportStats && !exportRoster && !exportCards}>
                Generate PDF
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Modal 1: Not Started list */}
      {notStartedOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '400px', width: '90%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>🕒 Not Started ({notStartedStudents.length})</h3>
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {notStartedStudents.length === 0 ? (
                <div style={{ opacity: 0.6, fontSize: '12px' }}>All assigned students have started or completed this exam.</div>
              ) : (
                notStartedStudents.map(s => (
                  <div key={s.code} style={{ padding: '8px', background: 'var(--bg-soft)', borderRadius: '4px', fontSize: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontWeight: 600 }}>{s.name}</span>
                    <span style={{ fontSize: '11px', opacity: 0.7, color: 'var(--text-muted)' }}>
                      {formatAbsentLogin(s.lastLoginAt)}
                    </span>
                  </div>
                ))
              )}
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '20px' }}>
              <button className="btn btn-secondary" onClick={() => setNotStartedOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal 2: Question voters list popup */}
      {votersModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '400px', width: '90%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>👥 Option Voters: {votersTitle}</h3>
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {votersList.length === 0 ? (
                <div style={{ opacity: 0.6, fontSize: '12px' }}>No students selected this option.</div>
              ) : (
                votersList.map((n, i) => (
                  <div key={i} style={{ padding: '8px', background: 'var(--bg-soft)', borderRadius: '4px', fontSize: '12px' }}>{n}</div>
                ))
              )}
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '20px' }}>
              <button className="btn btn-secondary" onClick={() => setVotersModalOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal 3: Question correctness details list */}
      {questionModalOpen && activeQuestionStat && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '460px', width: '90%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>🔍 Question Correctness Breakdown</h3>
            
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {activeQuestionStat.students.map((st: any, i: number) => {
                const label = st.status === 'correct' ? '✅ Correct' : (st.status === 'incorrect' ? '❌ Incorrect' : '➖ Unanswered');
                const isCorrect = st.status === 'correct';
                const isWrong = st.status === 'incorrect';
                return (
                  <div 
                    key={i} 
                    style={{ 
                      padding: '8px 12px', 
                      background: isCorrect ? 'rgba(46,204,113,0.1)' : (isWrong ? 'rgba(231,76,60,0.1)' : 'var(--bg-soft)'), 
                      borderRadius: '6px', 
                      fontSize: '12px',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center'
                    }}
                  >
                    <span>{st.name}</span>
                    <span style={{ fontWeight: 700, color: isCorrect ? '#2ecc71' : (isWrong ? '#e74c3c' : 'inherit') }}>{label} ({formatSeconds(st.timeSpentSeconds)})</span>
                  </div>
                );
              })}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '20px' }}>
              <button className="btn btn-secondary" onClick={() => { setQuestionModalOpen(false); setActiveQuestionStat(null); }}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Edit Correct Answer & Re-Score */}
      {editAnswerOpen && editingQuestion && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '90%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>✏️ Edit Correct Answer</h3>
            
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div 
                style={{ fontWeight: 600, fontSize: '13px', marginBottom: '10px' }}
                className="math-container"
              >
                {preprocessMathText(editingQuestion.questionText)}
              </div>
              
              {editingQuestion.options && editingQuestion.options.length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {editingQuestion.options.map((opt: any, oi: number) => {
                    const optKey = getRawOptionKey(opt);
                    const optText = getRawOptionText(opt);
                    const isSelected = String(selectedCorrectOption).trim().toLowerCase() === String(optKey).trim().toLowerCase() ||
                                       String(selectedCorrectOption).trim().toLowerCase() === String(optText).trim().toLowerCase() ||
                                       String(selectedCorrectOption).trim().toLowerCase() === String.fromCharCode(65 + oi).toLowerCase();
                    return (
                      <label 
                        key={oi} 
                        style={{ 
                          display: 'flex', 
                          alignItems: 'center', 
                          gap: '8px', 
                          padding: '8px 12px', 
                          border: isSelected ? '1.5px solid #1aa54e' : '1px solid var(--border-light)', 
                          borderRadius: '8px', 
                          background: isSelected ? 'rgba(26,165,78,0.07)' : 'var(--surface)',
                          cursor: 'pointer',
                          fontSize: '12px'
                        }}
                      >
                        <input 
                          type="radio" 
                          name="editCorrectRadio" 
                          value={optKey} 
                          checked={isSelected} 
                          onChange={() => setSelectedCorrectOption(optKey)} 
                        />
                        <span style={{ fontWeight: 700, color: 'var(--accent)' }}>{String.fromCharCode(65 + oi)}.</span>
                        <span className="math-container">{preprocessMathText(optText)}</span>
                      </label>
                    );
                  })}
                </div>
              ) : (
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, marginBottom: '6px', color: 'var(--text)' }}>
                    Correct Answer (Numerical / Text):
                  </label>
                  <input 
                    type="text"
                    className="form-input"
                    value={selectedCorrectOption}
                    onChange={(e) => setSelectedCorrectOption(e.target.value)}
                    placeholder="Enter correct numerical value or answer string"
                    style={{ width: '100%', padding: '8px 12px', fontSize: '13px', borderRadius: '6px', background: 'var(--bg-soft)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                  />
                </div>
              )}
              
              <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '8px', background: 'var(--bg-soft)', padding: '8px', borderRadius: '6px' }}>
                ⚠️ This will update the question bank, this exam, and re-score every existing student submission.
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => { setEditAnswerOpen(false); setEditingQuestion(null); }} disabled={savingAnswer}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveRescoredAnswer} disabled={savingAnswer}>
                {savingAnswer ? '⏳ Re-scoring...' : '💾 Save & Re-score'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Modal 4: Per-student detailed attempt response logs (Standardized Review Scorecard Modal) */}
      {studentModalOpen && selectedAttempt && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '10px 8px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '850px', width: '100%', maxHeight: '92vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden' }}>
            
            <div className="modal-header" style={{ padding: '12px 16px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold', color: 'var(--text)' }}>
                👤 Student Attempt Details: {selectedAttempt.studentName}{students.find(s => s.studentCode === selectedAttempt.studentCode)?.autonomous ? ' ⭐' : ''}
              </h4>
              <button className="close-modal" onClick={() => { setStudentModalOpen(false); setSelectedAttempt(null); }} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>

            <div className="modal-body" style={{ padding: '12px 14px', overflowY: 'auto', flex: 1 }}>
              {/* Violation notice banner inside modal */}
              {(() => {
                const tabV = selectedAttempt.tabViolations || 0;
                const pv = selectedAttempt.proctoringViolations || {};
                const faceV = pv.noFace || 0, multiV = pv.multipleFaces || 0, lookV = pv.lookingAway || 0, headV = pv.headMovement || 0;
                const totalV = tabV + faceV + multiV + lookV + headV;
                if (totalV === 0) return null;
                return (
                  <div style={{ background: 'rgba(231,76,60,0.1)', border: '1px solid rgba(231,76,60,0.3)', padding: '8px 12px', borderRadius: '6px', fontSize: '11px', color: '#e74c3c', marginBottom: '10px' }}>
                    <strong>⚠️ Proctoring Violations Detected:</strong> &nbsp;
                    {tabV > 0 && `Tab switches: ${tabV} • `}
                    {faceV > 0 && `No face: ${faceV} • `}
                    {multiV > 0 && `Multiple faces: ${multiV} • `}
                    {lookV > 0 && `Looking away: ${lookV} • `}
                    {headV > 0 && `Head movement: ${headV}`}
                  </div>
                );
              })()}

              {/* Compact Horizontal Summary Bar */}
              <div style={{ 
                background: 'var(--bg-soft)', 
                padding: '8px 12px', 
                borderRadius: 'var(--radius-sm)', 
                display: 'flex', 
                flexDirection: 'row', 
                flexWrap: 'wrap', 
                gap: '8px 16px', 
                marginBottom: '10px',
                border: '1px solid var(--border-light)',
                color: 'var(--text)'
              }}>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Score:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{selectedAttempt.score} / {selectedAttempt.totalMarks} ({selectedAttempt.percentage}%)</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Time Taken:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{formatSeconds(getReviewTimeTaken(selectedAttempt))}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Completed:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{formatDate(selectedAttempt.completedAt)}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Tab Switches:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{selectedAttempt.tabViolations || 0} times</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Microphone:</strong>{' '}
                  <span style={{ 
                    fontWeight: 600, 
                    color: selectedAttempt.micAvailable === false ? '#d97706' : '#16a34a' 
                  }}>
                    {selectedAttempt.micAvailable === false ? '⚠️ Offline' : '🟢 Active'}
                  </span>
                </div>
              </div>

              {selectedAttempt && (
                  <div>
                    <div className="outcome-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
                      <button 
                        onClick={() => setQuestionFilterTab('all')} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: 'var(--radius-sm)',
                          border: questionFilterTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                          color: questionFilterTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        All ({totalQuestionsCount})
                      </button>
                      <button 
                        onClick={() => setQuestionFilterTab('correct')} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: 'var(--radius-sm)',
                          border: questionFilterTab === 'correct' ? '1px solid var(--success)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'correct' ? 'var(--success-bg)' : 'transparent',
                          color: questionFilterTab === 'correct' ? 'var(--success)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        Correct ({correctCount})
                      </button>
                      <button 
                        onClick={() => setQuestionFilterTab('incorrect')} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: 'var(--radius-sm)',
                          border: questionFilterTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'incorrect' ? 'var(--danger-bg)' : 'transparent',
                          color: questionFilterTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        Incorrect ({incorrectCount})
                      </button>
                      <button 
                        onClick={() => setQuestionFilterTab('unanswered')} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: 'var(--radius-sm)',
                          border: questionFilterTab === 'unanswered' ? '1px solid var(--text-muted)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'unanswered' ? 'var(--bg-soft)' : 'transparent',
                          color: 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        Unanswered ({unansweredCount})
                      </button>
                    </div>

                    <h5 style={{ fontSize: '12px', fontWeight: 'bold', marginBottom: '8px', paddingBottom: '2px', color: 'var(--text)' }}>
                      🔍 Question Audit List
                    </h5>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      {filteredQDs.length === 0 ? (
                        <div style={{ textAlign: 'center', padding: '16px 0', color: 'var(--text-faint)', fontSize: '12px' }}>📭 No questions match this filter.</div>
                      ) : (
                        filteredQDs.map((qd: any, qIdx: number) => {
                          const isCorrect = qd.isCorrect;
                          const isUnattempted = isBlank(qd);
                          const bq = questionsMap[qd.questionCode] || null;
                          const explanation = bq?.solution || '';
                          const studentReason = getStudentReasonForQuestion(selectedAttempt, qd);

                          return (
                            <div 
                              key={qd.questionId || qIdx} 
                              style={{
                                width: '100%',
                                padding: '10px 12px',
                                borderRadius: 'var(--radius-sm)',
                                border: '1.5px solid var(--review-card-border)',
                                background: 'var(--review-card-bg)',
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '6px'
                              }}
                            >
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', fontSize: '11px', color: 'var(--text-muted)' }}>
                                <div style={{ display: 'flex', alignItems: 'center' }}>
                                  <span style={{ fontWeight: 600 }}>Q{(() => {
                                    if (qd.qNumber != null && qd.qNumber !== '') return qd.qNumber;
                                    const actualIdx = selectedAttempt?.questionDetails
                                      ? selectedAttempt.questionDetails.indexOf(qd)
                                      : -1;
                                    return actualIdx !== -1 ? actualIdx + 1 : qIdx + 1;
                                  })()} ({bq?.difficulty?.toUpperCase() || 'MEDIUM'} • {bq?.bloomLevel || 'Understand'} • Time: {formatSeconds(qd.timeSpentSeconds || 0)})</span>
                                  {studentReason && (
                                    <span style={{ background: 'rgba(230,126,34,0.12)', color: '#d35400', padding: '1px 5px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold', marginLeft: '6px' }}>
                                      ⚠️ Reason: {studentReason}
                                    </span>
                                  )}
                                </div>
                                <span style={{ 
                                  fontWeight: 'bold', 
                                  fontSize: '10px',
                                  padding: '1px 6px',
                                  borderRadius: '10px',
                                  background: isUnattempted ? 'var(--bg-soft)' : (isCorrect ? 'var(--success-bg)' : 'var(--danger-bg)'),
                                  color: isUnattempted ? 'var(--text-muted)' : (isCorrect ? 'var(--success)' : 'var(--danger)') 
                                }}>
                                  {isUnattempted ? 'Unattempted' : (isCorrect ? 'Correct' : 'Incorrect')}
                                </span>
                              </div>

                              {bq?.type === 'assertion_reason' && bq.assertion && bq.reason ? (
                                <div style={{ marginBottom: '8px', fontSize: '12.5px' }}>
                                  <p style={{ margin: '2px 0' }}><strong>Assertion (A):</strong> <span className="math-container">{preprocessMathText(bq.assertion)}</span></p>
                                  <p style={{ margin: '2px 0' }}><strong>Reason (R):</strong> <span className="math-container">{preprocessMathText(bq.reason)}</span></p>
                                </div>
                              ) : (
                                <p className="math-container" style={{ fontSize: '12.5px', margin: '0 0 6px 0', fontWeight: 'bold', lineHeight: '1.35' }}>
                                  {preprocessMathText(qd.questionText || bq?.text || '')}
                                </p>
                              )}

                              {bq?.options && bq.options.length > 0 ? (
                                <AuditQuestionOptions
                                  options={bq.options}
                                  correctAnswer={bq.correctAnswer || bq.answer || bq.correct_answer}
                                  correctAnswers={bq.correctAnswers}
                                  userAnswer={qd.userAnswer}
                                  isCorrect={isCorrect}
                                />
                              ) : null}

                              {/* Answers Side-by-Side Grid */}
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', background: 'var(--surface-3)', padding: '6px 8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                                <div style={{ lineHeight: '1.3' }}>
                                  <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Student Answer:</strong>
                                  <span className="math-container" style={{ color: 'var(--text)', fontWeight: 600 }}>
                                    {preprocessMathText(
                                      isUnattempted 
                                        ? '(blank)' 
                                        : getOptionText(qd.questionCode, qd.userAnswer)
                                    )}
                                  </span>
                                </div>
                                <div style={{ lineHeight: '1.3' }}>
                                  <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Correct Answer:</strong>
                                  <span className="math-container" style={{ color: 'var(--success)', fontWeight: 'bold' }}>
                                    {preprocessMathText(
                                      getOptionText(qd.questionCode, Array.isArray(qd.correctAnswer) ? qd.correctAnswer.join(', ') : qd.correctAnswer)
                                    )}
                                  </span>
                                </div>
                              </div>

                              {explanation && (
                                <div style={{ marginTop: '6px', fontSize: '11.5px', color: 'var(--text-muted)', borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                                  <strong>Solution Explanation:</strong>
                                  <p className="math-container" style={{ margin: '2px 0 0 0', lineHeight: '1.35' }}>{preprocessMathText(explanation)}</p>
                                </div>
                              )}
                            </div>
                          );
                        })
                      )}
                    </div>
                  </div>
              )}
            </div>

            <div className="modal-footer" style={{ padding: '10px 16px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '10px', background: 'var(--surface)' }}>
              <button className="btn btn-secondary" onClick={() => { setStudentModalOpen(false); setSelectedAttempt(null); }}>Close</button>
            </div>
          </div>
        </div>
      )}

      {reassignModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', maxWidth: '450px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '16px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
              🔄 Reassign Exam: {exam.name}
            </h3>

            {/* Selected students list */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>
                Reassigning To ({reassignSelectedStudents.size} Students)
              </label>
              <div style={{ maxHeight: '80px', overflowY: 'auto', background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', fontSize: '12px', display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                {Array.from(reassignSelectedStudents).map(code => {
                  const s = students.find(x => x.studentCode === code);
                  return (
                    <span key={code} style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '2px 8px', borderRadius: '12px', fontSize: '11px', fontWeight: 600 }}>
                      {s ? s.name : code}
                    </span>
                  );
                })}
              </div>
            </div>

            {/* Availability mode */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Availability Slot</label>
              <div style={{ display: 'flex', gap: '15px', marginBottom: '10px' }}>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="reassignOpenMode"
                    checked={reassignOpenMode === 'immediate'} 
                    onChange={() => setReassignOpenMode('immediate')} 
                    style={{ cursor: 'pointer' }}
                  /> Immediate
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="reassignOpenMode" 
                    checked={reassignOpenMode === 'scheduled'} 
                    onChange={() => setReassignOpenMode('scheduled')} 
                    style={{ cursor: 'pointer' }}
                  /> Scheduled
                </label>
              </div>

              {reassignOpenMode === 'scheduled' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '10px' }}>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)', marginBottom: '3px' }}>Start Datetime</label>
                      <input 
                        type="datetime-local" 
                        value={reassignStartAtStr}
                        onChange={(e) => {
                          const val = e.target.value;
                          setReassignStartAtStr(val);
                          setReassignEndAtStr(val);
                        }}
                        style={{ width: '100%', padding: '8px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}
                      />
                    </div>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)', marginBottom: '3px' }}>End Datetime</label>
                      <input 
                        type="datetime-local" 
                        value={reassignEndAtStr}
                        onChange={(e) => setReassignEndAtStr(e.target.value)}
                        style={{ width: '100%', padding: '8px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}
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
                          name="reassignLateEntryRestriction" 
                          checked={reassignLateEntryRestriction === true} 
                          onChange={() => setReassignLateEntryRestriction(true)} 
                          style={{ cursor: 'pointer' }}
                        /> Enforce 5-minute limit
                      </label>
                      <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                        <input 
                          type="radio" 
                          name="reassignLateEntryRestriction" 
                          checked={reassignLateEntryRestriction === false} 
                          onChange={() => setReassignLateEntryRestriction(false)} 
                          style={{ cursor: 'pointer' }}
                        /> Allow late entry
                      </label>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Attempt limit & Duration */}
            <div style={{ display: 'flex', gap: '15px' }}>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Attempt Limit</label>
                <select 
                  value={reassignAttemptLimit} 
                  onChange={(e) => setReassignAttemptLimit(Number(e.target.value))}
                  style={{ width: '100%', padding: '8px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px' }}
                >
                  <option value={1}>1 Attempt</option>
                  <option value={2}>2 Attempts</option>
                  <option value={3}>3 Attempts</option>
                  <option value={-1}>Unlimited</option>
                </select>
              </div>
              <div style={{ flex: 1 }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Duration (Minutes)</label>
                <input 
                  type="number" 
                  value={reassignDuration === undefined || reassignDuration === null ? '' : reassignDuration} 
                  onChange={(e) => {
                    const raw = e.target.value;
                    setReassignDuration(raw === '' ? '' as any : Number(raw));
                  }}
                  onBlur={() => {
                    if (!reassignDuration || Number(reassignDuration) < 1) {
                      setReassignDuration(45);
                    }
                  }}
                  style={{ width: '100%', padding: '8px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px' }}
                />
              </div>
            </div>

            {/* Footer actions */}
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => setReassignModalOpen(false)} 
                disabled={reassigning}
              >
                Cancel
              </button>
              <button 
                className="btn btn-primary" 
                onClick={handleSaveReassignment} 
                disabled={reassigning}
              >
                {reassigning ? '🔄 Reassigning...' : 'Confirm Reassign'}
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}

export default function ExamReportPage() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading report dashboard...
        </div>
      </div>
    }>
      <ExamReportContent />
    </Suspense>
  );
}

const AuditQuestionOptions = React.memo(({
  options,
  correctAnswer,
  correctAnswers,
  userAnswer,
  isCorrect
}: {
  options: any[];
  correctAnswer: any;
  correctAnswers: any;
  userAnswer: any;
  isCorrect?: boolean;
}) => {
  const correctAns = (Array.isArray(correctAnswers) && correctAnswers.length > 0) ? correctAnswers : correctAnswer;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
      {options.map((opt: any, oi: number) => {
        const optKey = getRawOptionKey(opt);
        const optText = getRawOptionText(opt);
        
        let isCorrectOpt = isOptionCorrect(correctAns, optKey, oi, optText);
        const isUserOpt = isOptionSelectedByUser(userAnswer, optKey, oi, optText);

        // Failsafe: if the question was evaluated as correct and user selected this option, it IS correct!
        if (isCorrect && isUserOpt) {
          isCorrectOpt = true;
        }

        let border = '1px solid var(--review-option-border)';
        let background = 'var(--review-option-bg)';
        let color = 'var(--text)';
        let prefix = '';

        if (isCorrectOpt) {
          border = '1.5px solid var(--success)';
          background = 'var(--success-bg)';
          color = 'var(--success)';
          prefix = isUserOpt ? '🎯 ' : '✅ ';
        } else if (isUserOpt) {
          border = '1.5px solid var(--danger)';
          background = 'rgba(220, 38, 38, 0.08)';
          color = 'var(--danger)';
          prefix = '❌ ';
        }

        return (
          <div 
            key={oi} 
            style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '6px',
              padding: '6px 10px', 
              border, 
              borderRadius: 'var(--radius-sm)', 
              background,
              color,
              fontSize: '11.5px',
              fontWeight: (isCorrectOpt || isUserOpt) ? 600 : 400
            }}
          >
            {prefix && <span style={{ marginRight: '2px' }}>{prefix}</span>}
            <span className="math-container">{preprocessMathText(optText)}</span>
          </div>
        );
      })}
    </div>
  );
});
AuditQuestionOptions.displayName = 'AuditQuestionOptions';
