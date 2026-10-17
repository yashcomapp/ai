'use client';

import DateTimeInputDMY from '@/components/DateTimeInputDMY';
import React, { useEffect, useState, useMemo, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, formatRichText, parseAnswerList, isOptionSelectedByUser, isOptionCorrect, getQuestionCorrectAnswer, getRawOptionKey, getRawOptionText, isBlank, resolveOptionDisplayText, extractAssertionAndReason, isAssertionReasonType, isMultipleChoiceType, cleanStringForMatch, isOptionMatch, getOptionText as getOptionTextCanonical } from '@/lib/questionTypes';
import QuestionDisplay, { RichMathText } from '@/components/QuestionDisplay';
import { playNotificationSound } from '@/lib/audioUtils';
import { getDateKeyIST, formatDateDMY, formatTimeIST, calculateEndDatetime, toLocalISOString, getMorningTestTimes, getEveningTestTimes, formatDateTimeShort as formatDate } from '@/lib/dateUtils';
import { formatReportStudentName, getScoreChip, getDeepScoreColor } from '@/lib/lqCardExport';

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
  proctoringSnapshots?: Array<{
    id?: string;
    timestamp: number | string;
    reason: string;
    imageData?: string;
    imageBase64?: string;
  }>;
  proctoringSnapshotsExpiresAt?: string | null;
  proctoringSnapshotsPurged?: boolean;
  isLate?: boolean;
  lateMinutes?: number;
  lateRemark?: string;
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
  duration?: number;
  durationMinutes?: number;
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
    const isToday = getDateKeyIST(lastLoginAt) === getDateKeyIST(new Date());
    const timeStr = formatTimeIST(lastLoginAt);
    if (isToday) {
      return `(Login: ${timeStr})`;
    }
    const dateStr = formatDateDMY(lastLoginAt);
    return `(Login: ${dateStr}, ${timeStr})`;
  } catch (e) {
    return '(Never Logged In)';
  }
}

function ExamReportContent() {
  const { firebaseUser } = useAuth();
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
  const [attemptViewMode, setAttemptViewMode] = useState<'flashcard' | 'list'>('flashcard');
  const [attemptCardIndex, setAttemptCardIndex] = useState<number>(0);
  const [questionModalOpen, setQuestionModalOpen] = useState(false);
  const [activeQuestionStat, setActiveQuestionStat] = useState<any>(null);
  const [activeQuestionFilter, setActiveQuestionFilter] = useState<'all' | 'correct' | 'incorrect' | 'unanswered'>('all');
  const [votersModalOpen, setVotersModalOpen] = useState(false);
  const [votersList, setVotersList] = useState<string[]>([]);
  const [votersTitle, setVotersTitle] = useState('');
  const [previewSnapshot, setPreviewSnapshot] = useState<{ src: string; reason: string; timestamp?: number | string } | null>(null);
  const [loadingSnapshots, setLoadingSnapshots] = useState(false);

  // Re-scoring modal states
  const [editAnswerOpen, setEditAnswerOpen] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState<any>(null);
  const [selectedCorrectOption, setSelectedCorrectOption] = useState('');
  const [selectedCorrectOptions, setSelectedCorrectOptions] = useState<string[]>([]);
  const [savingAnswer, setSavingAnswer] = useState(false);

  const [exportingImage, setExportingImage] = useState(false);

  // Individual Reassignment states
  const [reassignModalOpen, setReassignModalOpen] = useState(false);
  const [reassignSelectedStudents, setReassignSelectedStudents] = useState<Set<string>>(new Set());
  const [reassignOpenMode, setReassignOpenMode] = useState<'immediate' | 'scheduled'>('immediate');
  const [reassignStartAtStr, setReassignStartAtStr] = useState('');
  const [reassignEndAtStr, setReassignEndAtStr] = useState('');
  const [reassignAttemptLimit, setReassignAttemptLimit] = useState(1);
  const [reassignDuration, setReassignDuration] = useState(30);
  const [reassignLateEntryRestriction, setReassignLateEntryRestriction] = useState(false);
  const [reassignPresetSlot, setReassignPresetSlot] = useState<'6am' | '9pm' | null>(null);
  const [reassigning, setReassigning] = useState(false);
  const [resettingAll, setResettingAll] = useState(false);

  // Rescue Submission Modal states
  const [rescueModal, setRescueModal] = useState<{
    show: boolean;
    studentCode: string;
    studentName: string;
    backupToken: string;
    isSubmitting: boolean;
    error: string;
    success: string;
  }>({
    show: false,
    studentCode: '',
    studentName: '',
    backupToken: '',
    isSubmitting: false,
    error: '',
    success: ''
  });

  const handleOpenRescueModal = (s: { code: string; name: string }) => {
    setRescueModal({
      show: true,
      studentCode: s.code,
      studentName: s.name,
      backupToken: '',
      isSubmitting: false,
      error: '',
      success: ''
    });
  };

  const handleExecuteRescue = async (useToken: boolean) => {
    if (!rescueModal.studentCode || !examId || !firebaseUser) return;
    setRescueModal(prev => ({ ...prev, isSubmitting: true, error: '', success: '' }));
    try {
      const idToken = await firebaseUser.getIdToken();
      const payload: any = {
        action: 'rescue_submit',
        examId,
        studentCode: rescueModal.studentCode
      };
      if (useToken && rescueModal.backupToken.trim()) {
        payload.backupPayload = rescueModal.backupToken.trim();
      }

      const res = await fetch('/api/student/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify(payload)
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.message || 'Rescue submission failed.');
      }

      setRescueModal(prev => ({
        ...prev,
        isSubmitting: false,
        success: `✅ Rescued and graded successfully! Score: ${resData.score}/${resData.totalMarks} (${resData.percentage}%)`
      }));

      setTimeout(async () => {
        setRescueModal(prev => ({ ...prev, show: false }));
        await fetchReport();
      }, 1500);
    } catch (err: any) {
      setRescueModal(prev => ({
        ...prev,
        isSubmitting: false,
        error: err.message || 'Failed to rescue student attempt.'
      }));
    }
  };





  const openReassignModal = () => {
    const dur = Number(exam?.duration || exam?.durationMinutes) || 30;
    setReassignDuration(dur);
    setReassignAttemptLimit(1);
    setReassignOpenMode('immediate');
    setReassignPresetSlot(null);
    setReassignLateEntryRestriction(true);
    
    const now = new Date();
    const startStr = toLocalISOString(now);
    setReassignStartAtStr(startStr);
    setReassignEndAtStr(calculateEndDatetime(startStr, dur));
    
    setReassignModalOpen(true);
  };

  // Dynamically load KaTeX and auto-render math equations on state changes
  useMathRender([loading, attempts, questionSortMode, studentModalOpen, editAnswerOpen, questionFilterTab, reassignModalOpen]);

  // On-demand fetch proctoring snapshots when a student modal is opened
  useEffect(() => {
    if (!studentModalOpen || !selectedAttempt) return;
    const isPastDay = selectedAttempt.completedAt ? (getDateKeyIST(selectedAttempt.completedAt) < getDateKeyIST(new Date())) : (selectedAttempt.startedAt ? (getDateKeyIST(selectedAttempt.startedAt) < getDateKeyIST(new Date())) : false);
    const isExpired = selectedAttempt.proctoringSnapshotsExpiresAt ? (new Date() >= new Date(selectedAttempt.proctoringSnapshotsExpiresAt)) : false;
    if (selectedAttempt.proctoringSnapshotsPurged || isPastDay || isExpired) return;

    if (selectedAttempt.proctoringSnapshots && selectedAttempt.proctoringSnapshots.length > 0) return;

    let cancelled = false;
    setLoadingSnapshots(true);
    (async () => {
      try {
        const idToken = firebaseUser ? await firebaseUser.getIdToken() : '';
        const res = await fetch(`/api/admin/exams/objective?examId=${encodeURIComponent(examId)}&snapshotsStudentCode=${encodeURIComponent(selectedAttempt.studentCode || '')}&snapshotsAttemptId=${encodeURIComponent(selectedAttempt.id || '')}`, {
          headers: idToken ? {
            'Authorization': `Bearer ${idToken}`
          } : {}
        });
        if (!res.ok) {
          console.error(`Failed to fetch on-demand proctoring snapshots (HTTP ${res.status})`);
          return;
        }
        const data = await res.json();
        if (cancelled) return;
        if (data?.snapshots !== undefined) {
          setSelectedAttempt(prev => prev && prev.id === selectedAttempt.id ? {
            ...prev,
            proctoringSnapshots: data.snapshots,
            proctoringSnapshotsPurged: Boolean(data.isPurged)
          } : prev);
        }
      } catch (err) {
        if (!cancelled) console.error('Failed to fetch on-demand proctoring snapshots:', err);
      } finally {
        if (!cancelled) setLoadingSnapshots(false);
      }
    })();

    return () => { cancelled = true; };
  }, [studentModalOpen, selectedAttempt?.id, examId, firebaseUser]);

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

  const fetchReport = async (retryCount = 0) => {
    if (!firebaseUser || !examId) return;
    setLoading(true);
    setError('');
    try {
      const idToken = await firebaseUser.getIdToken(retryCount > 0);
      const res = await fetch(`/api/admin/exams/objective?examId=${encodeURIComponent(examId)}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        if (retryCount < 2) {
          await new Promise(r => setTimeout(r, 1000));
          return fetchReport(retryCount + 1);
        }
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.message || `Failed to retrieve objective exam report (HTTP ${res.status}).`);
      }
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
      if (retryCount < 2 && (err.message?.includes('fetch') || err.name === 'TypeError')) {
        await new Promise(r => setTimeout(r, 1200));
        return fetchReport(retryCount + 1);
      }
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
    return getOptionTextCanonical(q, ansInput);
  };

  const isDemo = (s: any) => {
    if (!s) return false;
    const name = String(s.name || s.studentName || '').trim().toLowerCase();
    const email = String(s.email || '').trim().toLowerCase();
    const code = String(s.studentCode || s.code || '').trim().toUpperCase();
    return name === 'student user' || name === 'parent user' || name === 'test parent' || name === 'test student' || email === 's@c.com' || email === 'p@c.com' || (code === 'ST-2026-000001' && (name === 'student user' || email === 's@c.com'));
  };

  // Calculate assigned but not started students CORRECTLY
  const startedCodes = new Set(attempts.map(r => (r.studentCode || '').trim().toUpperCase()).filter(Boolean));
  const assignedCodes = new Set<string>();

  assignments.forEach(ba => {
    (ba.targetStudents || []).forEach((code: string) => {
      if (code) assignedCodes.add(code.trim().toUpperCase());
    });
    const targetBatches = ba.targetBatches || [];
    if (targetBatches.length > 0) {
      students.forEach(s => {
        if (isDemo(s)) return;
        const sBatchIds = s.batchIds && s.batchIds.length ? s.batchIds : (s.batchId ? [s.batchId] : []);
        if (s.studentCode && sBatchIds.some((b: string) => targetBatches.includes(b))) {
          assignedCodes.add(s.studentCode.trim().toUpperCase());
        }
      });
    }
  });

  const notStartedStudents: { code: string; name: string; lastLoginAt?: string | null; lastActiveAt?: string | null }[] = [];
  Array.from(assignedCodes).forEach(code => {
    if (!startedCodes.has(code)) {
      const s = students.find(x => (x.studentCode || '').trim().toUpperCase() === code);
      if (s && !isDemo(s)) {
        notStartedStudents.push({ 
          code: s.studentCode || code, 
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
      const qType = bq?.type || 'OSC';
      const isMulti = isMultipleChoiceType(qType);
      const correctAnswersList = (Array.isArray(bq?.correctAnswers) && bq.correctAnswers.length > 0)
        ? bq.correctAnswers
        : (isMulti ? parseAnswerList(bq?.correctAnswer) : []);
      const primaryAnswer = (isMulti && correctAnswersList.length > 0)
        ? correctAnswersList
        : (bq?.correctAnswer || bq?.correctAnswers?.[0] || '');

      perQuestionStats[qKey] = {
        idx,
        type: qType,
        questionText: bq?.text || bq?.questionText || `Question ${idx + 1}`,
        correct: 0,
        incorrect: 0,
        unanswered: 0,
        totalTime: 0,
        timedCount: 0,
        options: bq?.options || null,
        correctAnswer: primaryAnswer,
        correctAnswers: correctAnswersList.length > 0 ? correctAnswersList : (primaryAnswer ? (Array.isArray(primaryAnswer) ? primaryAnswer : [primaryAnswer]) : []),
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
        const bq = questionsMap[key] || null;
        const qType = qd.type || bq?.type || 'OSC';
        const isMulti = isMultipleChoiceType(qType);
        const correctAnswersList = (Array.isArray(bq?.correctAnswers) && bq.correctAnswers.length > 0)
          ? bq.correctAnswers
          : ((Array.isArray(qd.correctAnswers) && qd.correctAnswers.length > 0)
              ? qd.correctAnswers
              : (isMulti ? parseAnswerList(bq?.correctAnswer || qd.correctAnswer) : []));
        const primaryAnswer = (isMulti && correctAnswersList.length > 0)
          ? correctAnswersList
          : (bq?.correctAnswer || qd.correctAnswer || (correctAnswersList.length > 0 ? correctAnswersList[0] : ''));

        if (!perQuestionStats[key]) {
          perQuestionStats[key] = {
            idx,
            type: qType,
            questionText: qd.questionText || bq?.text || `Question ${idx + 1}`,
            correct: 0,
            incorrect: 0,
            unanswered: 0,
            totalTime: 0,
            timedCount: 0,
            options: bq?.options || null,
            correctAnswer: primaryAnswer,
            correctAnswers: correctAnswersList.length > 0 ? correctAnswersList : (primaryAnswer ? (Array.isArray(primaryAnswer) ? primaryAnswer : [primaryAnswer]) : []),
            explanation: bq?.solution || '',
            questionCode: key,
            optionVotes: {},
            students: []
          };
        } else {
          // Enrich existing pre-populated stat if type or correctAnswers was missing
          if (!perQuestionStats[key].type || perQuestionStats[key].type === 'OSC') {
            perQuestionStats[key].type = qType;
          }
          if ((!perQuestionStats[key].correctAnswers || perQuestionStats[key].correctAnswers.length <= 1) && correctAnswersList.length > 1) {
            perQuestionStats[key].correctAnswers = correctAnswersList;
            if (isMulti) perQuestionStats[key].correctAnswer = correctAnswersList;
          }
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
          const selected = parseAnswerList(qd.userAnswer);
          selected.forEach(ans => {
            const answerStr = String(ans).trim();
            if (!answerStr) return;
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

              if (foundIndex === -1) {
                const cleanAns = cleanStringForMatch(answerStr);
                if (cleanAns) {
                  foundIndex = stat.options.findIndex((opt: any) => {
                    const optText = getRawOptionText(opt);
                    const optKey = getRawOptionKey(opt);
                    return cleanStringForMatch(optText) === cleanAns || cleanStringForMatch(optKey) === cleanAns;
                  });
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
    if (!editingQuestion) return;
    const isMulti = isMultipleChoiceType(editingQuestion.type);
    const answerToSave = isMulti ? selectedCorrectOptions : selectedCorrectOption;
    if (isMulti && selectedCorrectOptions.length === 0) {
      alert('Please select at least one correct option.');
      return;
    }
    if (!isMulti && !selectedCorrectOption) {
      alert('Please select or enter the correct answer.');
      return;
    }

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
          newCorrectAnswer: answerToSave
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
          resetAttempts: true,
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

  const handleResetAllAttempts = async () => {
    if (!firebaseUser || !exam || resettingAll) return;
    if (!confirm(`Are you sure you want to reset all student attempts and records for '${exam.name}'?\n\nThis will remove previous attempts, scores, and evaluations so all students can take the exam cleanly and start counts drop to 0.`)) return;
    
    setResettingAll(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/objective', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'resetAllAttempts',
          examId: exam.id
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.message || 'Failed to reset attempts.');
      }

      alert('✅ All student attempts and records have been reset! Start count is 0.');
      await fetchReport();
    } catch (err: any) {
      alert(`❌ Error: ${err.message || 'Failed to reset attempts'}`);
    } finally {
      setResettingAll(false);
    }
  };

  // Comprehensive attempt statistics (Accuracy, Pace, Breakdown, Guessing Detection)
  const getAttemptStats = (a: Attempt) => {
    const qDetails = a.questionDetails || [];
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    if (qDetails.length > 0) {
      qDetails.forEach((qd: any) => {
        const isActuallyAttempted = qd.isAttempted !== undefined
          ? Boolean(qd.isAttempted)
          : Boolean(qd.isCorrect || (!isBlank(qd.userAnswer) && qd.userAnswer !== ''));
        if (!isActuallyAttempted) {
          unattemptedCount++;
        } else if (qd.isCorrect) {
          correctCount++;
        } else {
          wrongCount++;
        }
      });
    } else {
      wrongCount = (a.wrongAnswers || []).length;
      unattemptedCount = (a.unattemptedQuestions || []).length;
      const estTotal = a.totalMarks ? Math.round(a.totalMarks / 4) : 0;
      correctCount = Math.max(0, estTotal - wrongCount - unattemptedCount);
    }

    const attemptedCount = correctCount + wrongCount;
    const totalCount = correctCount + wrongCount + unattemptedCount || (a.totalMarks ? Math.round(a.totalMarks / 4) : 0);
    const accuracy = attemptedCount > 0 ? (correctCount / attemptedCount) * 100 : 0;
    const totalTimeSeconds = getReviewTimeTaken(a);
    const avgPaceSec = attemptedCount > 0 ? Math.round(totalTimeSeconds / attemptedCount) : (totalCount > 0 ? Math.round(totalTimeSeconds / totalCount) : 0);
    const penaltyLost = wrongCount * 1;
    const earnedMarks = correctCount * 4;
    const errorRatio = correctCount > 0 ? (wrongCount / correctCount) : (wrongCount > 0 ? wrongCount : 0);
    const isHighGamble = (wrongCount >= 8 && wrongCount >= correctCount * 2) || (attemptedCount >= 10 && accuracy < 40);

    return {
      correctCount,
      wrongCount,
      unattemptedCount,
      attemptedCount,
      totalCount,
      accuracy,
      totalTimeSeconds,
      avgPaceSec,
      penaltyLost,
      earnedMarks,
      errorRatio,
      isHighGamble
    };
  };

  // Sorting attempts roster
  const getSortVal = (a: Attempt, col: string) => {
    if (col === 'name') return a.studentName.toLowerCase();
    if (col === 'batch') return getStudentBatchName(a.studentCode).toLowerCase();
    if (col === 'time') return getReviewTimeTaken(a);
    if (col === 'status') return a.status;
    if (col === 'date') return a.startedAt ? new Date(a.startedAt).getTime() : (a.completedAt ? new Date(a.completedAt).getTime() : 0);
    if (col === 'accuracy') return getAttemptStats(a).accuracy;
    if (col === 'pace') return getAttemptStats(a).avgPaceSec;
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
      setStudentSortDir(col === 'score' || col === 'time' || col === 'accuracy' || col === 'pace' ? 'desc' : 'asc');
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

  const scoreColor = (pct: number) => {
    if (pct >= 80) return 'var(--success)';
    if (pct >= 60) return 'var(--accent)';
    if (pct >= 40) return 'var(--warning)';
    return 'var(--danger)';
  };

  // Dynamically load html2canvas if not already loaded
  const loadHtml2Canvas = async () => {
    if (typeof window === 'undefined') return null;
    const w = window as any;
    if (w.html2canvas) return w.html2canvas;
    return new Promise<any>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
      s.onload = () => resolve((window as any).html2canvas);
      s.onerror = () => reject(new Error('Failed to load image generation library.'));
      document.head.appendChild(s);
    });
  };

  // High-Resolution WhatsApp Result Card Exporter
  const handleExportWhatsAppImage = async () => {
    if (typeof window === 'undefined' || !exam) return;
    if (attempts.length === 0) {
      alert('No student submissions to export yet.');
      return;
    }

    setExportingImage(true);

    try {
      const html2canvas = await loadHtml2Canvas();
      if (!html2canvas) throw new Error('Could not initialize image generator.');

      // Sort attempts: score/percentage desc, then time taken asc
      const sortedRoster = [...attempts].sort((a, b) => {
        if (b.percentage !== a.percentage) return b.percentage - a.percentage;
        if ((b.score || 0) !== (a.score || 0)) return (b.score || 0) - (a.score || 0);
        return getReviewTimeTaken(a) - getReviewTimeTaken(b);
      });

      const maxScore = sortedRoster.length > 0 ? (sortedRoster[0].score || 0) : 0;
      const maxPct = sortedRoster.length > 0 ? sortedRoster[0].percentage : 0;
      const avgPct = sortedRoster.length > 0
        ? Math.round(sortedRoster.reduce((sum, a) => sum + (a.percentage || 0), 0) / sortedRoster.length)
        : 0;
      const totalAssigned = assignedCodes.size || (attempts.length + notStartedStudents.length);
      const todayFormatted = formatDateDMY(new Date());

      // Create offscreen container with Ultra-HD layout and explicit subpixel font antialiasing
      const container = document.createElement('div');
      container.style.position = 'fixed';
      container.style.left = '0';
      container.style.top = '0';
      container.style.width = '1080px';
      container.style.backgroundColor = '#ffffff';
      container.style.color = '#0f172a';
      container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif";
      (container.style as any).webkitFontSmoothing = 'antialiased';
      (container.style as any).mozOsxFontSmoothing = 'grayscale';
      (container.style as any).textRendering = 'optimizeLegibility';
      container.style.padding = '28px 32px';
      container.style.boxSizing = 'border-box';
      container.style.zIndex = '-9999';
      container.style.pointerEvents = 'none';
      container.style.opacity = '1';

      // Build roster rows with crisp, high-contrast typography and first+last name formatting
      const rowsHtml = sortedRoster.map((a, idx) => {
        const stats = getAttemptStats(a);
        const rank = idx + 1;
        const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
        const displayName = formatReportStudentName(a.studentName);
        const isGamble = stats.isHighGamble;
        const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';
        const blunderStyle = isGamble ? 'background-color: #fef2f2; border-left: 4px solid #ef4444;' : `background-color: ${rowBg};`;

        let remarkHtml = '';
        if (isGamble) {
          remarkHtml = `<span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1.5px solid #fca5a5; white-space: nowrap;">🚨 ${stats.errorRatio >= 2 ? stats.errorRatio.toFixed(1) + 'x Errors' : 'Blind Guessing'} (-${stats.penaltyLost}m)</span>`;
        } else if (stats.accuracy >= 90) {
          remarkHtml = `<span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: #dcfce7; color: #14532d; border: 1.5px solid #86efac; white-space: nowrap;">🌟 Outstanding</span>`;
        } else if (stats.accuracy >= 75) {
          remarkHtml = `<span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: #e0f2fe; color: #0369a1; border: 1.5px solid #7dd3fc; white-space: nowrap;">✅ Strong</span>`;
        } else if (stats.accuracy >= 50) {
          remarkHtml = `<span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: #fef9c3; color: #854d0e; border: 1.5px solid #fde047; white-space: nowrap;">🟡 Moderate</span>`;
        } else {
          remarkHtml = `<span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1.5px solid #fca5a5; white-space: nowrap;">⚠️ Penalty Trap</span>`;
        }

        const paceColorHex = stats.avgPaceSec > 0 && stats.avgPaceSec < 20 && stats.wrongCount > 5 ? '#b45309' : '#1e293b';

        return `
          <tr style="border-bottom: 1px solid #e2e8f0; height: 42px; ${blunderStyle}">
            <td style="padding: 8px 10px; text-align: center; font-weight: 900; font-size: 13.5px; color: #0f172a;">${rankBadge}</td>
            <td style="padding: 8px 14px; font-weight: 800; font-size: 14.5px; color: #0f172a; white-space: nowrap;">
              ${displayName}
              ${a.isLate ? '<span style="margin-left: 6px; font-size: 10px; padding: 2px 6px; background: #fee2e2; color: #991b1b; border: 1.5px solid #fca5a5; border-radius: 4px; font-weight: 900;">LATE</span>' : ''}
            </td>
            <td style="padding: 8px 12px; text-align: center; white-space: nowrap;">
              <strong style="font-size: 14.5px; color: #0f172a; font-weight: 900;">${a.score || 0}</strong> <span style="font-size: 12px; color: #64748b; font-weight: 700;">/ ${a.totalMarks}</span>
              <span style="margin-left: 6px;">${getScoreChip(a.percentage)}</span>
            </td>
            <td style="padding: 8px 12px; text-align: center; font-size: 13px; white-space: nowrap;">
              <span style="color: #14532d; font-weight: 800;">${stats.correctCount}✅</span>
              <span style="color: #991b1b; font-weight: 800; margin-left: 6px;">${stats.wrongCount}❌</span>
              <span style="color: #475569; font-weight: 700; margin-left: 6px;">${stats.unattemptedCount}⚪</span>
            </td>
            <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
              ${getScoreChip(stats.accuracy)}
            </td>
            <td style="padding: 8px 10px; text-align: center; font-size: 13px; color: ${paceColorHex}; font-weight: 800; white-space: nowrap;">
              ${stats.avgPaceSec ? `${stats.avgPaceSec}s` : '-'}
            </td>
            <td style="padding: 8px 10px; text-align: center; font-size: 12.5px; color: #475569; font-weight: 700; white-space: nowrap;">
              ${formatSeconds(getReviewTimeTaken(a))}
            </td>
            <td style="padding: 8px 12px; text-align: center; white-space: nowrap;">
              ${remarkHtml}
            </td>
          </tr>
        `;
      }).join('');

      // Absent students section with first+last name formatting
      const absentHtml = notStartedStudents.length > 0 ? `
        <div style="margin-top: 18px; padding: 12px 18px; background: #fef2f2; border: 1.5px solid #fca5a5; border-radius: 8px;">
          <div style="font-size: 12.5px; font-weight: 900; color: #991b1b; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 5px;">
            🔴 Absent Students (${notStartedStudents.length})
          </div>
          <div style="font-size: 13px; color: #7f1d1d; font-weight: 700; line-height: 1.6;">
            ${notStartedStudents.map(s => formatReportStudentName(s.name)).join(' • ')}
          </div>
        </div>
      ` : '';

      container.innerHTML = `
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 24px 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
          
          <!-- Header -->
          <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
            <div>
              <div style="color: #92400e; font-size: 15px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
                YASHCOM FOUNDATION, SHEGAON
              </div>
              <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
                🏆 Exam Performance Summary
              </div>
              <div style="color: #0369a1; font-size: 16px; font-weight: 800;">
                ${exam.name || exam.subjectName || exam.id}
              </div>
            </div>
            <div style="text-align: right;">
              <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
                📅 ${todayFormatted}
              </div>
              <div style="color: #475569; font-size: 12px; font-weight: 700; margin-top: 6px;">
                Total Marks: <strong style="color:#0f172a;">${exam.totalMarks || 96}</strong> | Penalty: <strong style="color:#991b1b;">-25% (-1 mark)</strong>
              </div>
            </div>
          </div>

          <!-- KPI Summary Cards -->
          <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 20px;">
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 26px; font-weight: 900; color: #0f172a; line-height: 1.1;">${totalAssigned}</div>
              <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Assigned</div>
            </div>
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 26px; font-weight: 900; color: #047857; line-height: 1.1;">${sortedRoster.length}</div>
              <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Submitted</div>
            </div>
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 26px; font-weight: 900; color: ${notStartedStudents.length > 0 ? '#991b1b' : '#475569'}; line-height: 1.1;">${notStartedStudents.length}</div>
              <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Absent</div>
            </div>
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 26px; font-weight: 900; color: #047857; line-height: 1.1;">${maxScore}/${exam.totalMarks || 96}</div>
              <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Highest (${maxPct}%)</div>
            </div>
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
              <div style="font-size: 26px; font-weight: 900; color: ${getDeepScoreColor(avgPct)}; line-height: 1.1;">${avgPct}%</div>
              <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Batch Average</div>
            </div>
          </div>

          <!-- Table with Executive Dark Navy Header for Maximum Legibility -->
          <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
            <thead>
              <tr style="background: #0f172a; color: #ffffff; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; height: 42px;">
                <th style="padding: 10px 10px; text-align: center; width: 55px;">Rank</th>
                <th style="padding: 10px 14px; text-align: left;">Student Name</th>
                <th style="padding: 10px 12px; text-align: center; width: 145px;">Score</th>
                <th style="padding: 10px 12px; text-align: center; width: 140px;">Breakdown</th>
                <th style="padding: 10px 10px; text-align: center; width: 95px;">Accuracy</th>
                <th style="padding: 10px 10px; text-align: center; width: 75px;">Pace</th>
                <th style="padding: 10px 10px; text-align: center; width: 80px;">Time</th>
                <th style="padding: 10px 12px; text-align: center; width: 190px;">Insight</th>
              </tr>
            </thead>
            <tbody>
              ${rowsHtml}
            </tbody>
          </table>

          <!-- Absent Box -->
          ${absentHtml}

          <!-- Educational Insight Banner (Hindi / Marathi) - High Contrast Bullet List -->
          <div style="margin-top: 20px; padding: 16px 20px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
              <span style="font-size: 20px; line-height: 1;">💡</span>
              <strong style="color: #0f172a; font-size: 14.5px; font-weight: 900; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
                परीक्षा विश्लेषण एवं महत्त्वाचे नियम (Important Exam Insights):
              </strong>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13px; line-height: 1.75; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
              <li style="margin-bottom: 6px;">
                <strong style="color: #0f172a;">📌 टोले मारणे (अंदाजे तुक्के लावणे) पूर्णपणे टाळा:</strong> प्रत्येक चुकीच्या उत्तराला <strong>-25% (१ गुण)</strong> नेगेटिव्ह मार्किंग आहे. टोले मारल्यास बरोबर उत्तरांचे कष्टाचे गुणही वजा होतात.
              </li>
              <li style="margin-bottom: 6px;">
                <strong style="color: #0f172a;">📌 प्रश्न न आल्यास सोडून देणे (Unattempted) अधिक हिताचे:</strong> अंदाज लावून टोले मारण्यापेक्षा प्रश्न अनुत्तरित सोडल्यास कोणतेही गुण वजा होत नाहीत (Zero Penalty).
              </li>
              <li style="margin-bottom: 6px;">
                <strong style="color: #0f172a;">📌 त्रुटींचे वेळेवर पुनरावलोकन (Review & Learn):</strong> परीक्षा केवळ गुणांसाठी नसून स्वतःच्या संकल्पनांमधील त्रुटी समजून घेण्यासाठी आहे.
              </li>
              <li>
                <strong style="color: #0f172a;">📌 खरी समज आणि सातत्य (True Conceptual Learning):</strong> परीक्षेनंतर चुकलेल्या प्रश्नांचे योग्य स्पष्टीकरण समजून घेणे म्हणजेच खरी शैक्षणिक प्रगती.
              </li>
            </ul>
          </div>

          <!-- Footer -->
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
            <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Academic Evaluation Portal</span>
            <span>Verified Official Snapshot • Confidential Batch Report</span>
          </div>

        </div>
      `;

      document.body.appendChild(container);

      // Wait 300ms for browser layout & fonts to fully render
      await new Promise(r => setTimeout(r, 300));

      const canvas = await html2canvas(container, {
        scale: 3, // 1080px * 3 = 3240px wide Ultra HD!
        useCORS: true,
        backgroundColor: '#ffffff',
        logging: false
      });

      document.body.removeChild(container);

      // 1. Copy lossless PNG to clipboard
      let copiedToClipboard = false;
      if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
        try {
          await new Promise<void>((resolve) => {
            canvas.toBlob(async (blob: Blob | null) => {
              if (!blob) {
                resolve();
                return;
              }
              try {
                await navigator.clipboard.write([
                  new ClipboardItem({ 'image/png': blob })
                ]);
                copiedToClipboard = true;
              } catch (clipErr) {
                console.warn('Clipboard write failed:', clipErr);
              }
              resolve();
            }, 'image/png');
          });
        } catch (err) {
          console.warn('Clipboard error:', err);
        }
      }

      // 2. Trigger automatic Lossless PNG download
      const cleanExamName = (exam.name || exam.id).replace(/[^a-zA-Z0-9_-]/g, '_');
      const fileName = `Exam_Summary_${cleanExamName}.png`;
      const imageUri = canvas.toDataURL('image/png');
      const downloadLink = document.createElement('a');
      downloadLink.download = fileName;
      downloadLink.href = imageUri;
      downloadLink.click();

      playNotificationSound();
      if (copiedToClipboard) {
        alert(`✅ Ultra HD WhatsApp Card Exported!\n\n1. Lossless Ultra-HD Image downloaded: ${fileName}\n2. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp Web.`);
      } else {
        alert(`✅ Ultra HD WhatsApp Card downloaded successfully as ${fileName}!`);
      }
    } catch (err: any) {
      alert(`❌ Failed to export WhatsApp image: ${err.message || err}`);
    } finally {
      setExportingImage(false);
    }
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', gap: '12px', padding: '20px' }}>
        <div className="loading" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div className="spinner"></div> 
          <span>Generating performance scorecard...</span>
        </div>
        <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: 0 }}>
          Retrieving questions, attempts, and proctoring metrics
        </p>
      </div>
    );
  }

  if (error || !exam) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '500px', textAlign: 'center', marginBottom: '16px' }}>
          {error || 'Objective exam not found.'}
        </div>
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
          <button className="btn btn-primary" onClick={() => fetchReport(0)} style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span>🔄</span> Retry / Refresh
          </button>
          <button className="btn btn-secondary" onClick={() => router.push('/admin/exams')}>
            Back to Exams
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '10px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', margin: '4px 0' }}>
          <h1 style={{ fontSize: '18px', margin: 0, fontWeight: 800 }}>
            Exam Report: {exam.name || exam.subjectName || exam.id}
          </h1>
          <span className="badge" style={{ fontSize: '11px', fontWeight: 600, padding: '2px 8px', background: 'var(--surface-3)', border: '1px solid var(--border-light)', borderRadius: '6px' }}>
            {exam.id}
          </span>
        </div>
        
        {/* Legacy-style Toolbar with Back & Export PDF & Broadcast Notices */}
        <div className="report-toolbar" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px', flexWrap: 'wrap', gap: '6px' }}>
          <button 
            className="btn btn-secondary" 
            onClick={() => router.push('/admin/exams')}
            style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 600, padding: '5px 12px' }}
          >
            ← Back to Exams
          </button>
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
            <span 
              role="button"
              tabIndex={0}
              onClick={resettingAll ? undefined : handleResetAllAttempts}
              title="Reset all student attempts, evaluations, and scores so all students can take the exam cleanly"
              style={{
                cursor: resettingAll ? 'not-allowed' : 'pointer',
                fontSize: '11.5px',
                fontWeight: 600,
                color: 'var(--danger)',
                textDecoration: 'underline',
                textUnderlineOffset: '3px',
                opacity: resettingAll ? 0.6 : 1,
                alignSelf: 'center',
                padding: '4px 6px'
              }}
            >
              {resettingAll ? 'Resetting...' : 'Reset All Attempts'}
            </span>
            
            <button 
              className="btn" 
              onClick={handleExportWhatsAppImage}
              disabled={exportingImage}
              style={{ 
                display: 'inline-flex', 
                alignItems: 'center', 
                gap: '6px', 
                fontSize: '12px', 
                fontWeight: 700, 
                padding: '5px 14px',
                background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                color: '#ffffff',
                border: 'none',
                borderRadius: 'var(--radius-sm, 6px)',
                cursor: exportingImage ? 'wait' : 'pointer',
                boxShadow: '0 2px 8px rgba(16, 185, 129, 0.3)'
              }}
              title="Export lossless card optimized for WhatsApp"
            >
              {exportingImage ? '⏳ Exporting...' : '📸 Export WhatsApp'}
            </button>
          </div>
        </div>

        {/* Live Interactive Content Area */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>

          {/* Clickable summary stats */}
          <div className="report-summary" style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
            
            <div 
              className={`stat-summary-card ${activeFilter === 'all' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('all'); setFilterLabel('All Submissions'); }}
              style={{ flex: 1, minWidth: '110px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'all' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '8px 12px', borderRadius: 'var(--radius)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '20px', fontWeight: 800 }}>{attempts.length}</div>
              <div className="stat-summary-label" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Submissions</div>
            </div>

            <div 
              className="stat-summary-card"
              onClick={() => setNotStartedOpen(true)}
              style={{ flex: 1, minWidth: '110px', cursor: 'pointer', background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '8px 12px', borderRadius: 'var(--radius)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-muted)' }}>{notStartedStudents.length}</div>
              <div className="stat-summary-label" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Not Started</div>
            </div>

            <div 
              className="stat-summary-card"
              style={{ flex: 1, minWidth: '110px', background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '8px 12px', borderRadius: 'var(--radius)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '20px', fontWeight: 800 }}>{avgPercentage}%</div>
              <div className="stat-summary-label" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Average Score</div>
            </div>

            <div 
              className={`stat-summary-card ${activeFilter === 'pending' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('pending'); setFilterLabel('Pending Review'); }}
              style={{ flex: 1, minWidth: '110px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'pending' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '8px 12px', borderRadius: 'var(--radius)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '20px', fontWeight: 800, color: 'var(--warning)' }}>{pendingCount}</div>
              <div className="stat-summary-label" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Pending Review</div>
            </div>

            <div 
              className={`stat-summary-card ${activeFilter === 'flagged' ? 'active-filter' : ''}`}
              onClick={() => { setActiveFilter('flagged'); setFilterLabel('Flagged (Proctoring)'); }}
              style={{ flex: 1, minWidth: '110px', cursor: 'pointer', background: 'var(--surface)', border: activeFilter === 'flagged' ? '2px solid var(--accent)' : '1px solid var(--border-light)', padding: '8px 12px', borderRadius: 'var(--radius)', textAlign: 'center' }}
            >
              <div className="stat-summary-number" style={{ fontSize: '20px', fontWeight: 800, color: 'var(--danger)' }}>{totalFlaggedCount}</div>
              <div className="stat-summary-label" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Flagged (Proctoring)</div>
            </div>

          </div>

          {/* Filter Notice banner */}
          {activeFilter && (
            <div style={{ background: 'var(--badge-bg)', border: '1px solid var(--badge-border)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', fontSize: '12px', color: 'var(--accent)', fontWeight: 600, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Showing: {filterLabel}</span>
              <button className="btn btn-secondary btn-sm" style={{ padding: '2px 8px', fontSize: '11px' }} onClick={() => setActiveFilter(null)}>✕ Clear filter</button>
            </div>
          )}

          {/* Section A: Student Roster Grid */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <h3 style={{ fontSize: '12px', fontWeight: 800, padding: '10px 14px 0', margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>👤 Student Submissions</h3>
            
            <div style={{ overflowX: 'auto', marginTop: '6px' }}>
              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12.5px', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.3px' }}>
                    <th onClick={() => handleSortStudent('name')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap' }}>Student Name ⇅</th>
                    <th onClick={() => handleSortStudent('score')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap', width: '120px' }}>Score ⇅</th>
                    <th style={{ padding: '6px 8px', whiteSpace: 'nowrap', width: '140px' }}>Breakdown</th>
                    <th onClick={() => handleSortStudent('accuracy')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap', width: '75px' }}>Accuracy ⇅</th>
                    <th onClick={() => handleSortStudent('pace')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap', width: '70px' }}>Avg Pace ⇅</th>
                    <th onClick={() => handleSortStudent('time')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap', width: '75px' }}>Time Taken ⇅</th>
                    <th onClick={() => handleSortStudent('status')} style={{ padding: '6px 8px', cursor: 'pointer', whiteSpace: 'nowrap', width: '75px' }}>Status ⇅</th>
                    <th style={{ padding: '6px 8px', textAlign: 'right', whiteSpace: 'nowrap', width: '55px' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {/* Absent Students (pinned to top in soft WhatsApp coral-rose color, single merged row) */}
                  {(!activeFilter || activeFilter === 'all') && notStartedStudents.length > 0 && (
                    <tr 
                      style={{ borderBottom: '1px solid var(--border-light)', background: 'var(--danger-bg, rgba(234, 108, 117, 0.10))' }}
                    >
                      <td colSpan={8} style={{ padding: '8px 12px', color: 'var(--danger)' }}>
                        <div style={{ textAlign: 'center', fontWeight: 800, fontSize: '12px', marginBottom: '6px', color: 'var(--danger)', letterSpacing: '0.2px' }}>
                          🔴 Absent Students ({notStartedStudents.length})
                        </div>
                        <div style={{ 
                          display: 'flex', 
                          flexWrap: 'wrap', 
                          gap: '4px 8px',
                          fontSize: '11.5px',
                          fontWeight: 600,
                          color: 'var(--danger)'
                        }}>
                          {[...notStartedStudents]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(a => (
                              <div key={a.code} style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'space-between', gap: '6px', background: 'rgba(234, 108, 117, 0.08)', padding: '2px 6px', borderRadius: '4px', flex: '1 1 200px', maxWidth: '100%' }}>
                                <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: 'var(--danger)', fontWeight: 600, fontSize: '11.5px' }} title={`${a.name} - ${formatAbsentLogin(a.lastLoginAt)}`}>
                                  • {a.name}{' '}
                                  <span style={{ fontSize: '10px', fontWeight: 500, color: 'var(--danger-muted)', opacity: 0.9, marginLeft: '4px' }}>
                                    {formatAbsentLogin(a.lastLoginAt)}
                                  </span>
                                </span>
                                <button 
                                  type="button"
                                  className="btn btn-secondary btn-sm"
                                  style={{ fontSize: '10px', padding: '1px 5px', color: '#f59e0b', borderColor: 'rgba(245, 158, 11, 0.4)', fontWeight: 700, flexShrink: 0 }}
                                  onClick={() => handleOpenRescueModal(a)}
                                  title={`Rescue attempt for ${a.name}`}
                                >
                                  ⚡ Rescue
                                </button>
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
                      <td colSpan={8} style={{ padding: '20px', textAlign: 'center', color: 'var(--text-muted)' }}>📭 No attempts matching the criteria.</td>
                    </tr>
                  ) : (
                    filteredAttempts.map(a => {
                      const vCount = totalViolations(a);
                      const isPending = a.status === 'pending';
                      const scoreVal = a.score || 0;
                      const statusDate = a.reviewedAt || a.completedAt;
                      const stats = getAttemptStats(a);

                      return (
                        <tr 
                          key={a.id} 
                          className="student-row" 
                          onClick={() => { 
                            setSelectedAttempt(a); 
                            setAttemptCardIndex(0);
                            const qDetails = a.questionDetails || [];
                            const hasMistakes = qDetails.some((qd: any) => !qd.isCorrect || isBlank(qd));
                            setQuestionFilterTab(hasMistakes ? 'incorrect' : 'all');
                            setStudentModalOpen(true); 
                          }}
                          style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', height: '34px' }}
                        >
                          <td style={{ padding: '5px 8px', fontWeight: 600, whiteSpace: 'nowrap' }}>
                            {a.isLate && (
                              <span style={{ marginRight: '6px', color: 'var(--danger)', background: 'var(--danger-bg, rgba(239, 68, 68, 0.15))', border: '1px solid var(--danger-border, rgba(239, 68, 68, 0.3))', padding: '1px 5px', borderRadius: '4px', fontSize: '10px', fontWeight: 800 }}>
                                ⏰ LATE
                              </span>
                            )}
                            {a.studentName}{students.find(s => s.studentCode === a.studentCode)?.autonomous ? ' ⭐' : ''}
                            {a.micAvailable === false && (
                              <span style={{ marginLeft: '6px', color: 'var(--warning)', background: 'var(--warning-bg, rgba(217, 119, 6, 0.1))', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Bypassed / Offline">
                                🎙️
                              </span>
                            )}
                            {vCount > 0 && (
                              <span style={{ marginLeft: '6px', color: 'var(--danger)', fontSize: '11px', fontWeight: 700 }} title={`${vCount} violations`}>
                                🚩 {vCount}
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '5px 8px', fontWeight: 700, color: scoreColor(a.percentage), whiteSpace: 'nowrap' }}>
                            {scoreVal} / {a.totalMarks} ({a.percentage}%)
                          </td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap', fontSize: '11.5px' }}>
                            <span style={{ color: '#10b981', fontWeight: 700 }}>{stats.correctCount}✅</span>
                            {' '}
                            <span style={{ color: stats.wrongCount >= 10 ? '#ef4444' : 'var(--danger)', fontWeight: stats.wrongCount >= 10 ? 800 : 600 }}>
                              {stats.wrongCount}❌
                            </span>
                            {' '}
                            <span style={{ color: 'var(--text-muted)', fontWeight: 500 }}>
                              {stats.unattemptedCount}⚪
                            </span>
                            {stats.wrongCount > 0 && (
                              <span style={{ fontSize: '10px', color: '#ef4444', marginLeft: '4px', opacity: 0.85 }} title={`Lost -${stats.penaltyLost} marks to negative penalty`}>
                                (-{stats.penaltyLost}m)
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>
                            <span style={{ 
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '4px',
                              padding: '1px 6px',
                              borderRadius: '4px',
                              fontSize: '11px',
                              fontWeight: 700,
                              background: stats.accuracy >= 75 ? 'rgba(16, 185, 129, 0.12)' : stats.accuracy >= 50 ? 'rgba(245, 158, 11, 0.12)' : 'rgba(239, 68, 68, 0.15)',
                              color: stats.accuracy >= 75 ? '#10b981' : stats.accuracy >= 50 ? '#f59e0b' : '#ef4444',
                              border: stats.accuracy < 50 ? '1px solid rgba(239, 68, 68, 0.3)' : 'none'
                            }}>
                              {stats.accuracy.toFixed(1)}%
                              {stats.isHighGamble && <span title={`${stats.errorRatio.toFixed(1)}x error blunder! High gambling detected`} style={{ fontSize: '10px' }}>⚠️</span>}
                            </span>
                          </td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>
                            <span style={{ 
                              fontWeight: 600, 
                              fontSize: '11px',
                              color: stats.avgPaceSec > 0 && stats.avgPaceSec < 20 && stats.wrongCount > 5 ? '#f59e0b' : 'inherit' 
                            }}>
                              {stats.avgPaceSec ? `${stats.avgPaceSec}s/Q` : '-'}
                              {stats.avgPaceSec > 0 && stats.avgPaceSec < 20 && stats.wrongCount > 5 && ' ⚡'}
                            </span>
                          </td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>{formatSeconds(getReviewTimeTaken(a))}</td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap' }} title={statusDate ? `Submitted: ${formatDate(statusDate)}` : undefined}>
                            <span style={{ fontSize: '10px', padding: '2px 7px', borderRadius: '6px', background: isPending ? 'var(--warning-bg)' : 'var(--success-bg)', color: isPending ? 'var(--warning)' : 'var(--success)', fontWeight: 700 }}>
                              {a.status}
                            </span>
                          </td>
                          <td style={{ padding: '5px 8px', textAlign: 'right', whiteSpace: 'nowrap' }} onClick={(e) => e.stopPropagation()}>
                            <button 
                              type="button"
                              style={{ 
                                background: 'transparent', 
                                border: 'none', 
                                padding: '0 4px', 
                                fontSize: '11px', 
                                fontWeight: 600, 
                                color: 'var(--text-muted)', 
                                textDecoration: 'underline', 
                                cursor: 'pointer' 
                              }}
                              onClick={() => handleResetAttempt(a.id, a.studentName)}
                              title={`Reset attempt for ${a.studentName}`}
                            >
                              Reset
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

          {/* Section: Individual Reassignment for Absent Cases */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', padding: '6px 12px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '12px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>
                🔄 Individual Reassignment (Absent Cases)
              </h3>
              {notStartedStudents.length > 0 && (
                <span className="badge badge-danger" style={{ background: 'var(--danger-bg, rgba(234, 108, 117, 0.10))', color: 'var(--danger)', border: '1px solid var(--danger-border, rgba(234, 108, 117, 0.22))', fontWeight: 700, padding: '2px 8px', borderRadius: '10px', fontSize: '11px' }}>
                  {notStartedStudents.length} Absent
                </span>
              )}
            </div>
            
            {notStartedStudents.length === 0 ? (
              <div style={{ padding: '8px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', fontSize: '12px', color: 'var(--text-muted)', textAlign: 'center' }}>
                🎉 All assigned students have started or completed the exam. No absent cases found.
              </div>
            ) : (
              <>
                {/* Select All Toggle & Setup Reassignment Button */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', flexWrap: 'wrap', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                    <input 
                      type="checkbox" 
                      id="reassign-select-all"
                      checked={reassignSelectedStudents.size === notStartedStudents.length && notStartedStudents.length > 0}
                      onChange={(e) => {
                        if (e.target.checked) {
                          setReassignSelectedStudents(new Set(notStartedStudents.map(s => s.code)));
                        } else {
                          setReassignSelectedStudents(new Set());
                        }
                      }}
                      style={{ cursor: 'pointer' }}
                    />
                    <label htmlFor="reassign-select-all" style={{ fontSize: '11.5px', fontWeight: 'bold', cursor: 'pointer', userSelect: 'none' }}>
                      Select All ({notStartedStudents.length})
                    </label>
                  </div>

                  <button 
                    className="btn btn-primary"
                    disabled={reassignSelectedStudents.size === 0}
                    onClick={openReassignModal}
                    style={{ fontSize: '11.5px', padding: '3px 10px', display: 'flex', alignItems: 'center', gap: '6px', height: '26px', borderRadius: 'var(--radius-pill, 999px)' }}
                  >
                    🔄 Setup Reassignment ({reassignSelectedStudents.size})
                  </button>
                </div>
                
                {/* Clean inline list of students (no box enclosure) */}
                <div style={{ maxHeight: '100px', overflowY: 'auto', display: 'flex', flexWrap: 'wrap', gap: '6px 18px', padding: '2px 0' }}>
                  {notStartedStudents.map(s => (
                    <label 
                      key={s.code} 
                      style={{ 
                        display: 'inline-flex', 
                        alignItems: 'center', 
                        gap: '6px', 
                        cursor: 'pointer',
                        fontSize: '12px',
                        fontWeight: 600,
                        color: 'var(--text)',
                        userSelect: 'none'
                      }}
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
                      <span>{s.name}</span>
                    </label>
                  ))}
                </div>
              </>
            )}
          </div>

          {/* Section B: Auto-submitted Attempts */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <h3 style={{ fontSize: '12px', fontWeight: 800, padding: '10px 14px 0', margin: 0, textTransform: 'uppercase', color: 'var(--danger)' }}>
              🚨 Auto-Submitted / Abandoned Attempts ({attempts.filter(a => a.proctoringViolationTriggered || a.abandoned).length})
            </h3>
            <div style={{ overflowX: 'auto', marginTop: '6px' }}>
              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12.5px', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '11.5px' }}>
                    <th style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>Student Name</th>
                    <th style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>Score</th>
                    <th style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>Tab Violations</th>
                    <th style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>Auto-Submission Reason</th>
                    <th style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>Date/Time</th>
                    <th style={{ padding: '5px 8px', textAlign: 'right', whiteSpace: 'nowrap' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {attempts.filter(a => a.proctoringViolationTriggered || a.abandoned).length === 0 ? (
                    <tr>
                      <td colSpan={6} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>
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
                          onClick={() => { 
                            setSelectedAttempt(a); 
                            setAttemptCardIndex(0);
                            const qDetails = a.questionDetails || [];
                            const hasMistakes = qDetails.some((qd: any) => !qd.isCorrect || isBlank(qd));
                            setQuestionFilterTab(hasMistakes ? 'incorrect' : 'all');
                            setStudentModalOpen(true); 
                          }}
                          onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--bg-soft)'; }}
                          onMouseLeave={(e) => { e.currentTarget.style.background = 'transparent'; }}
                        >
                          <td style={{ padding: '5px 8px', fontWeight: 600 }}>
                            {a.isLate && (
                              <span style={{ marginRight: '6px', color: 'var(--danger)', background: 'var(--danger-bg, rgba(239, 68, 68, 0.15))', border: '1px solid var(--danger-border, rgba(239, 68, 68, 0.3))', padding: '1px 5px', borderRadius: '4px', fontSize: '10px', fontWeight: 800 }}>
                                ⏰ LATE
                              </span>
                            )}
                            👤 {a.studentName}
                            {a.micAvailable === false && (
                              <span style={{ marginLeft: '6px', color: 'var(--warning)', background: 'var(--warning-bg, rgba(217, 119, 6, 0.1))', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Bypassed / Offline">
                                🎙️ Bypassed
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '5px 8px', fontWeight: 700, color: 'var(--danger)' }}>
                            {a.abandoned ? '0 (Abandoned)' : `${scoreVal} / ${a.totalMarks} (${a.percentage}%)`}
                          </td>
                          <td style={{ padding: '5px 8px', fontWeight: 700 }}>
                            {a.abandoned ? '—' : `${a.tabViolations || 0} / 3`}
                          </td>
                          <td style={{ padding: '5px 8px', color: 'var(--danger)', fontWeight: 600 }}>
                            {getAutoSubmitReason(a)}
                          </td>
                          <td style={{ padding: '5px 8px', whiteSpace: 'nowrap' }}>
                            {completedAt ? completedAt.toLocaleString() : '—'}
                          </td>
                          <td style={{ padding: '5px 8px', textAlign: 'right', whiteSpace: 'nowrap' }} onClick={(e) => e.stopPropagation()}>
                            <button 
                              type="button"
                              style={{ 
                                background: 'transparent', 
                                border: 'none', 
                                padding: '0 4px', 
                                fontSize: '11px', 
                                fontWeight: 600, 
                                color: 'var(--text-muted)', 
                                textDecoration: 'underline', 
                                cursor: 'pointer' 
                              }}
                              onClick={() => handleResetAttempt(a.id, a.studentName)}
                              title={`Reset attempt for ${a.studentName}`}
                            >
                              Reset
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

          {/* Section C: Detailed Questions Breakdown cards */}
          <div className="card" id="chipsCard" style={{ background: 'var(--surface)', padding: '10px 14px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', flexWrap: 'wrap', gap: '6px' }}>
              <h3 style={{ fontSize: '12px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>📝 Question Insight Cards</h3>
              
              <div style={{ display: 'flex', gap: '4px' }}>
                <button className={`btn btn-sm ${questionSortMode === 'order' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('order')} style={{ fontSize: '10px', padding: '2px 8px' }}>Order</button>
                <button className={`btn btn-sm ${questionSortMode === 'correct' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('correct')} style={{ fontSize: '10px', padding: '2px 8px' }}>Most Correct</button>
                <button className={`btn btn-sm ${questionSortMode === 'incorrect' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('incorrect')} style={{ fontSize: '10px', padding: '2px 8px' }}>Most Incorrect</button>
                <button className={`btn btn-sm ${questionSortMode === 'unanswered' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setQuestionSortMode('unanswered')} style={{ fontSize: '10px', padding: '2px 8px' }}>Unanswered</button>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {questionsList.map((s, idx) => {
                const total = s.correct + s.incorrect + s.unanswered;
                const pctCorrect = total ? Math.round((s.correct / total) * 100) : 0;
                
                // Keep raw math strings intact for auto-render parsing on mount and updates
                const questionTextRaw = s.questionText;

                return (
                  <div 
                    key={s.key} 
                    className="card pq-card" 
                    style={{ background: 'var(--bg-soft)', borderLeft: '4px solid var(--accent)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', position: 'relative' }}
                  >
                    <QuestionDisplay
                      prefix={`Q${(s.idx ?? idx) + 1}. `}
                      text={questionTextRaw}
                      type={s.type}
                      options={s.options}
                      correctAnswer={s.correctAnswer}
                      correctAnswers={s.correctAnswers}
                      explanation={s.explanation}
                      mode="report"
                      headerRight={
                        <button 
                          className="btn btn-secondary btn-sm" 
                          style={{ padding: '2px 8px', fontSize: '10.5px', flexShrink: 0 }}
                          onClick={() => {
                            setEditingQuestion(s);
                            const curList = Array.isArray(s.correctAnswers) && s.correctAnswers.length > 0
                              ? s.correctAnswers
                              : (Array.isArray(s.correctAnswer) ? s.correctAnswer : parseAnswerList(s.correctAnswer));
                            setSelectedCorrectOptions(curList);
                            setSelectedCorrectOption(Array.isArray(s.correctAnswer) ? (s.correctAnswer[0] || '') : (s.correctAnswer || curList[0] || ''));
                            setEditAnswerOpen(true);
                          }}
                        >
                          ✏️ Edit Answer
                        </button>
                      }
                      optionVotes={s.optionVotes}
                      onVoteClick={(optKey, students) => {
                        setVotersTitle(`Option: ${optKey}`);
                        setVotersList(students || []);
                        setVotersModalOpen(true);
                      }}
                      style={{ fontWeight: 600, fontSize: '12.5px' }}
                    >
                      <div className="pq-bar-track" style={{ height: '6px', borderRadius: '3px', background: 'var(--bg)', overflow: 'hidden', margin: '4px 0 8px 0' }}>
                        <div className="pq-bar-fill" style={{ height: '100%', background: 'var(--success)', width: `${pctCorrect}%` }}></div>
                      </div>

                      <div style={{ fontSize: '11px', margin: '0 0 10px 0', color: 'var(--text-muted)' }}>
                        <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600, color: 'var(--success, #16a34a)' }} onClick={() => { setActiveQuestionStat(s); setActiveQuestionFilter('correct'); setQuestionModalOpen(true); }}>✅ {s.correct} correct</span> &nbsp;•&nbsp;
                        <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600, color: 'var(--danger, #dc2626)' }} onClick={() => { setActiveQuestionStat(s); setActiveQuestionFilter('incorrect'); setQuestionModalOpen(true); }}>❌ {s.incorrect} incorrect</span> &nbsp;•&nbsp;
                        <span style={{ textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }} onClick={() => { setActiveQuestionStat(s); setActiveQuestionFilter('unanswered'); setQuestionModalOpen(true); }}>➖ {s.unanswered} unanswered</span>
                      </div>
                    </QuestionDisplay>
                  </div>
                );
              })}
            </div>
          </div>

        </div>

      </main>

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
                    <div>
                      <div style={{ fontWeight: 600 }}>{s.name}</div>
                      <div style={{ fontSize: '10.5px', opacity: 0.7, color: 'var(--text-muted)' }}>
                        {formatAbsentLogin(s.lastLoginAt)}
                      </div>
                    </div>
                    <button 
                      className="btn btn-secondary btn-sm"
                      style={{ fontSize: '11px', padding: '2px 8px', color: '#f59e0b', borderColor: 'rgba(245, 158, 11, 0.4)', fontWeight: 700 }}
                      onClick={() => handleOpenRescueModal(s)}
                    >
                      ⚡ Rescue
                    </button>
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

      {/* Rescue Attempt Modal (Admin Emergency Finalize from Report) */}
      {rescueModal.show && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover, #1e293b)', border: '1px solid var(--border-popover, #334155)', borderRadius: '12px', maxWidth: '520px', width: '100%', padding: '24px', color: 'var(--text)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px', marginBottom: '16px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>⚡ Rescue Student Submission</h3>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '12px' }} onClick={() => setRescueModal(prev => ({ ...prev, show: false }))}>✕</button>
            </div>

            <div style={{ background: 'var(--bg-soft)', padding: '12px', borderRadius: '8px', marginBottom: '16px', fontSize: '12.5px', lineHeight: 1.6 }}>
              <div><strong>Student:</strong> {rescueModal.studentName} ({rescueModal.studentCode})</div>
              <div><strong>Exam:</strong> {exam?.name || examId}</div>
            </div>

            {rescueModal.error && (
              <div style={{ background: 'var(--danger-bg, rgba(239, 68, 68, 0.12))', border: '1px solid var(--danger-border, rgba(239, 68, 68, 0.3))', color: 'var(--danger)', padding: '10px 14px', borderRadius: '8px', fontSize: '12px', fontWeight: 600, marginBottom: '14px' }}>
                ⚠️ {rescueModal.error}
              </div>
            )}

            {rescueModal.success && (
              <div style={{ background: 'rgba(16, 185, 129, 0.12)', border: '1px solid rgba(16, 185, 129, 0.3)', color: '#10b981', padding: '10px 14px', borderRadius: '8px', fontSize: '13px', fontWeight: 700, marginBottom: '14px' }}>
                {rescueModal.success}
              </div>
            )}

            {!rescueModal.success && (
              <>
                <div style={{ marginBottom: '16px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px' }}>
                    Option 1: Finalize directly from latest Firestore autosave
                  </label>
                  <button 
                    className="btn btn-primary btn-sm" 
                    onClick={() => handleExecuteRescue(false)}
                    disabled={rescueModal.isSubmitting}
                    style={{ width: '100%', fontWeight: 700, padding: '8px' }}
                  >
                    {rescueModal.isSubmitting ? 'Evaluating & Finalizing...' : '⚡ Grade from Firestore Autosave'}
                  </button>
                </div>

                <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '14px', marginBottom: '16px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px' }}>
                    Option 2: Grade from Student Emergency Backup Code
                  </label>
                  <textarea
                    rows={3}
                    placeholder="Paste student emergency backup token or JSON here..."
                    value={rescueModal.backupToken}
                    onChange={(e) => setRescueModal(prev => ({ ...prev, backupToken: e.target.value }))}
                    style={{ width: '100%', padding: '8px', borderRadius: '6px', fontSize: '11px', fontFamily: 'monospace', background: 'var(--bg)', border: '1px solid var(--border-light)', color: 'var(--text)', marginBottom: '8px' }}
                  />
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={() => handleExecuteRescue(true)}
                    disabled={rescueModal.isSubmitting || !rescueModal.backupToken.trim()}
                    style={{ width: '100%', fontWeight: 700, padding: '8px' }}
                  >
                    {rescueModal.isSubmitting ? 'Processing Token...' : '📋 Grade from Emergency Token'}
                  </button>
                </div>
              </>
            )}

            <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
              <button className="btn btn-secondary btn-sm" onClick={() => setRescueModal(prev => ({ ...prev, show: false }))}>
                Close
              </button>
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
          <div className="card" style={{ background: 'var(--surface)', padding: '20px 24px', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '90%', maxHeight: '82vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px', marginBottom: '12px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>
                {activeQuestionFilter === 'correct' ? `✅ Correct Students (${activeQuestionStat.correct})` :
                 activeQuestionFilter === 'incorrect' ? `❌ Incorrect Students (${activeQuestionStat.incorrect})` :
                 activeQuestionFilter === 'unanswered' ? `➖ Unanswered Students (${activeQuestionStat.unanswered})` :
                 `🔍 Question Q${(activeQuestionStat.idx ?? 0) + 1} Breakdown`}
              </h3>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
                Q{(activeQuestionStat.idx ?? 0) + 1}
              </span>
            </div>

            {/* Filter Switcher Tabs */}
            <div style={{ display: 'flex', gap: '4px', marginBottom: '12px', background: 'var(--bg-soft, #f1f5f9)', padding: '3px', borderRadius: '6px' }}>
              <button
                type="button"
                onClick={() => setActiveQuestionFilter('correct')}
                style={{
                  flex: 1,
                  padding: '5px 4px',
                  fontSize: '11px',
                  fontWeight: 700,
                  borderRadius: '4px',
                  border: 'none',
                  cursor: 'pointer',
                  background: activeQuestionFilter === 'correct' ? 'var(--success, #16a34a)' : 'transparent',
                  color: activeQuestionFilter === 'correct' ? '#ffffff' : 'var(--text-muted)'
                }}
              >
                ✅ Correct ({activeQuestionStat.correct})
              </button>
              <button
                type="button"
                onClick={() => setActiveQuestionFilter('incorrect')}
                style={{
                  flex: 1,
                  padding: '5px 4px',
                  fontSize: '11px',
                  fontWeight: 700,
                  borderRadius: '4px',
                  border: 'none',
                  cursor: 'pointer',
                  background: activeQuestionFilter === 'incorrect' ? 'var(--danger, #dc2626)' : 'transparent',
                  color: activeQuestionFilter === 'incorrect' ? '#ffffff' : 'var(--text-muted)'
                }}
              >
                ❌ Incorrect ({activeQuestionStat.incorrect})
              </button>
              <button
                type="button"
                onClick={() => setActiveQuestionFilter('unanswered')}
                style={{
                  flex: 1,
                  padding: '5px 4px',
                  fontSize: '11px',
                  fontWeight: 700,
                  borderRadius: '4px',
                  border: 'none',
                  cursor: 'pointer',
                  background: activeQuestionFilter === 'unanswered' ? 'var(--accent, #2563eb)' : 'transparent',
                  color: activeQuestionFilter === 'unanswered' ? '#ffffff' : 'var(--text-muted)'
                }}
              >
                ➖ None ({activeQuestionStat.unanswered})
              </button>
              <button
                type="button"
                onClick={() => setActiveQuestionFilter('all')}
                style={{
                  padding: '5px 8px',
                  fontSize: '11px',
                  fontWeight: 700,
                  borderRadius: '4px',
                  border: 'none',
                  cursor: 'pointer',
                  background: activeQuestionFilter === 'all' ? 'var(--accent, #2563eb)' : 'transparent',
                  color: activeQuestionFilter === 'all' ? '#ffffff' : 'var(--text-muted)'
                }}
              >
                All ({activeQuestionStat.students.length})
              </button>
            </div>
            
            {/* Filtered Students List */}
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {(() => {
                const filtered = activeQuestionStat.students.filter((st: any) => {
                  if (activeQuestionFilter === 'correct') return st.status === 'correct';
                  if (activeQuestionFilter === 'incorrect') return st.status === 'incorrect';
                  if (activeQuestionFilter === 'unanswered') return st.status === 'unanswered';
                  return true;
                });

                if (filtered.length === 0) {
                  return (
                    <div style={{ padding: '24px 12px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '12px' }}>
                      No students found for this status.
                    </div>
                  );
                }

                return filtered.map((st: any, i: number) => {
                  const label = st.status === 'correct' ? '✅ Correct' : (st.status === 'incorrect' ? '❌ Incorrect' : '➖ Unanswered');
                  const isCorrect = st.status === 'correct';
                  const isWrong = st.status === 'incorrect';
                  return (
                    <div 
                      key={i} 
                      style={{ 
                        padding: '8px 12px', 
                        background: isCorrect ? 'var(--success-bg, rgba(46,204,113,0.1))' : (isWrong ? 'var(--danger-bg, rgba(231,76,60,0.1))' : 'var(--bg-soft)'), 
                        borderRadius: '6px', 
                        fontSize: '12px',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                      }}
                    >
                      <span style={{ fontWeight: 600 }}>{st.name}</span>
                      <span style={{ fontWeight: 700, color: isCorrect ? 'var(--success, #16a34a)' : (isWrong ? 'var(--danger, #dc2626)' : 'inherit') }}>
                        {label} {st.timeSpentSeconds ? `(${formatSeconds(st.timeSpentSeconds)})` : ''}
                      </span>
                    </div>
                  );
                });
              })()}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '10px' }}>
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
              <QuestionDisplay
                mode="stem-only"
                text={editingQuestion.questionText}
                type={editingQuestion.type}
              />
              
              {editingQuestion.options && editingQuestion.options.length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {isMultipleChoiceType(editingQuestion.type) && (
                    <div style={{ fontSize: '11px', color: 'var(--accent)', fontWeight: 700, marginBottom: '2px' }}>
                      ☑️ Multi-Choice Question (OMC): Select all options that are correct.
                    </div>
                  )}
                  {editingQuestion.options.map((opt: any, oi: number) => {
                    const optKey = getRawOptionKey(opt);
                    const optText = getRawOptionText(opt);
                    const letter = String.fromCharCode(65 + oi);
                    const isMulti = isMultipleChoiceType(editingQuestion.type);
                    
                    const isSelected = isMulti
                      ? selectedCorrectOptions.some(ans => 
                          isOptionMatch(opt, ans) || 
                          String(ans).trim().toLowerCase() === String(optKey).trim().toLowerCase() ||
                          String(ans).trim().toLowerCase() === String(optText).trim().toLowerCase() ||
                          String(ans).trim().toLowerCase() === letter.toLowerCase()
                        )
                      : String(selectedCorrectOption).trim().toLowerCase() === String(optKey).trim().toLowerCase() ||
                        String(selectedCorrectOption).trim().toLowerCase() === String(optText).trim().toLowerCase() ||
                        String(selectedCorrectOption).trim().toLowerCase() === letter.toLowerCase();

                    return (
                      <label 
                        key={oi} 
                        style={{ 
                          display: 'flex', 
                          alignItems: 'center', 
                          gap: '8px', 
                          padding: '8px 12px', 
                          border: isSelected ? '1.5px solid var(--success)' : '1px solid var(--border-light)', 
                          borderRadius: '8px', 
                          background: isSelected ? 'rgba(26,165,78,0.07)' : 'var(--surface)',
                          cursor: 'pointer',
                          fontSize: '12px'
                        }}
                      >
                        <input 
                          type={isMulti ? "checkbox" : "radio"} 
                          name="editCorrectChoice" 
                          value={optKey} 
                          checked={isSelected} 
                          onChange={() => {
                            if (isMulti) {
                              setSelectedCorrectOptions(prev => {
                                const exists = prev.some(ans => 
                                  isOptionMatch(opt, ans) || 
                                  String(ans).trim().toLowerCase() === String(optKey).trim().toLowerCase() ||
                                  String(ans).trim().toLowerCase() === String(optText).trim().toLowerCase() ||
                                  String(ans).trim().toLowerCase() === letter.toLowerCase()
                                );
                                if (exists) {
                                  return prev.filter(ans => 
                                    !isOptionMatch(opt, ans) &&
                                    String(ans).trim().toLowerCase() !== String(optKey).trim().toLowerCase() &&
                                    String(ans).trim().toLowerCase() !== String(optText).trim().toLowerCase() &&
                                    String(ans).trim().toLowerCase() !== letter.toLowerCase()
                                  );
                                } else {
                                  return [...prev, optText || optKey];
                                }
                              });
                            } else {
                              setSelectedCorrectOption(optKey);
                            }
                          }} 
                        />
                        <span style={{ fontWeight: 700, color: 'var(--accent)' }}>{letter}.</span>
                        <RichMathText content={optText} inline />
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
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '8px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius)', maxWidth: '850px', width: '100%', maxHeight: '92vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden' }}>
            
            <div className="modal-header" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                {selectedAttempt.isLate && (
                  <span style={{ color: 'var(--danger)', background: 'var(--danger-bg, rgba(239, 68, 68, 0.15))', border: '1px solid var(--danger-border, rgba(239, 68, 68, 0.3))', padding: '1px 5px', borderRadius: '4px', fontSize: '10px', fontWeight: 800 }}>
                    ⏰ LATE
                  </span>
                )}
                <span>👤 Student Attempt Details: {selectedAttempt.studentName}{students.find(s => s.studentCode === selectedAttempt.studentCode)?.autonomous ? ' ⭐' : ''}</span>
              </h4>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                {/* View Mode Switcher */}
                <div style={{ display: 'inline-flex', background: 'var(--bg, #f1f5f9)', padding: '2px', borderRadius: '6px', border: '1px solid var(--border-light, #cbd5e1)' }}>
                  <button
                    type="button"
                    onClick={() => setAttemptViewMode('flashcard')}
                    style={{
                      padding: '2px 8px',
                      fontSize: '10.5px',
                      fontWeight: 800,
                      borderRadius: '4px',
                      border: 'none',
                      cursor: 'pointer',
                      background: attemptViewMode === 'flashcard' ? 'var(--accent)' : 'transparent',
                      color: attemptViewMode === 'flashcard' ? '#ffffff' : 'var(--text-muted)'
                    }}
                  >
                    🗂️ Flashcard
                  </button>
                  <button
                    type="button"
                    onClick={() => setAttemptViewMode('list')}
                    style={{
                      padding: '2px 8px',
                      fontSize: '10.5px',
                      fontWeight: 800,
                      borderRadius: '4px',
                      border: 'none',
                      cursor: 'pointer',
                      background: attemptViewMode === 'list' ? 'var(--accent)' : 'transparent',
                      color: attemptViewMode === 'list' ? '#ffffff' : 'var(--text-muted)'
                    }}
                  >
                    📜 List
                  </button>
                </div>

                <button 
                  type="button"
                  style={{ background: 'transparent', border: 'none', padding: '2px 6px', fontSize: '11px', color: 'var(--danger)', textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }}
                  onClick={async () => {
                    const studentName = selectedAttempt.studentName;
                    const attemptId = selectedAttempt.id;
                    setStudentModalOpen(false);
                    setSelectedAttempt(null);
                    await handleResetAttempt(attemptId, studentName);
                  }}
                  title="Reset student attempt and allow retake"
                >
                  Reset
                </button>
                <button className="close-modal" onClick={() => { setStudentModalOpen(false); setSelectedAttempt(null); }} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.1rem', padding: '2px 4px' }}>✕</button>
              </div>
            </div>

            <div className="modal-body" style={{ padding: '8px 10px', overflowY: 'auto', flex: 1 }}>
              {/* Violation notice banner inside modal */}
              {(() => {
                const tabV = selectedAttempt.tabViolations || 0;
                const pv = selectedAttempt.proctoringViolations || {};
                const faceV = pv.noFace || 0, multiV = pv.multipleFaces || 0, lookV = pv.lookingAway || 0, headV = pv.headMovement || 0;
                const totalV = tabV + faceV + multiV + lookV + headV;
                if (totalV === 0) return null;
                return (
                  <div style={{ background: 'var(--danger-bg, rgba(231,76,60,0.1))', border: '1px solid var(--danger-border, rgba(231,76,60,0.3))', padding: '6px 10px', borderRadius: '4px', fontSize: '10.5px', color: 'var(--danger)', marginBottom: '8px' }}>
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
                padding: '6px 10px', 
                borderRadius: 'var(--radius-sm)', 
                display: 'flex', 
                flexDirection: 'row', 
                flexWrap: 'wrap', 
                gap: '6px 12px', 
                marginBottom: '8px',
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
                    color: selectedAttempt.micAvailable === false ? 'var(--warning)' : 'var(--success)' 
                  }}>
                    {selectedAttempt.micAvailable === false ? '⚠️ Offline' : '🟢 Active'}
                  </span>
                </div>
              </div>

              {/* Admin-Only Proctoring Audit Snapshots (Max 5, auto-purged at 12:00 AM on same day) */}
              {(() => {
                const snapshots = selectedAttempt.proctoringSnapshots || [];
                const isPastDay = selectedAttempt.completedAt ? (getDateKeyIST(selectedAttempt.completedAt) < getDateKeyIST(new Date())) : (selectedAttempt.startedAt ? (getDateKeyIST(selectedAttempt.startedAt) < getDateKeyIST(new Date())) : false);
                const isExpired = selectedAttempt.proctoringSnapshotsExpiresAt ? (new Date() >= new Date(selectedAttempt.proctoringSnapshotsExpiresAt)) : false;
                const isPurged = selectedAttempt.proctoringSnapshotsPurged || isPastDay || isExpired || (snapshots.length === 0 && selectedAttempt.completedAt && isPastDay);
                
                return (
                  <div style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border-light)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '8px 12px',
                    marginBottom: '10px'
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: (snapshots.length > 0 || loadingSnapshots) ? '8px' : '0' }}>
                      <span style={{ fontSize: '11.5px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}>
                        📸 Proctoring Snapshots {loadingSnapshots ? '(Loading...)' : `(${snapshots.length}/5)`}
                      </span>
                      <span style={{ fontSize: '10px', color: 'var(--accent)', background: 'rgba(59, 130, 246, 0.08)', padding: '2px 6px', borderRadius: '4px', border: '1px solid rgba(59, 130, 246, 0.2)' }}>
                        🔒 Confidential • Auto-purged at 12:00 AM
                      </span>
                    </div>

                    {loadingSnapshots ? (
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontStyle: 'italic', padding: '6px 0', display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span style={{ width: '12px', height: '12px', border: '2px solid var(--accent)', borderRightColor: 'transparent', borderRadius: '50%', display: 'inline-block', animation: 'spin 0.75s linear infinite' }} />
                        Loading camera captures...
                      </div>
                    ) : isPurged && snapshots.length === 0 ? (
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontStyle: 'italic', padding: '4px 0' }}>
                        🔒 Proctoring camera captures have been permanently auto-purged per same-day 12:00 AM retention limit.
                      </div>
                    ) : snapshots.length === 0 ? (
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontStyle: 'italic', padding: '4px 0' }}>
                        📷 No proctoring camera captures recorded for this attempt.
                      </div>
                    ) : (
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(95px, 1fr))', gap: '8px' }}>
                        {snapshots.map((s, idx) => {
                          const snapImg = s.imageBase64 || s.imageData || '';
                          const dateStr = s.timestamp ? new Date(s.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }) : `#${idx + 1}`;
                          return (
                            <div 
                              key={idx}
                              onClick={() => setPreviewSnapshot({ src: snapImg, reason: s.reason, timestamp: s.timestamp })}
                              style={{
                                border: '1px solid var(--border-light)',
                                borderRadius: '4px',
                                overflow: 'hidden',
                                cursor: 'pointer',
                                background: 'var(--bg-soft)'
                              }}
                              title="Click to zoom preview"
                            >
                              <div style={{ aspectRatio: '4/3', background: '#000', overflow: 'hidden' }}>
                                <img src={snapImg} alt={`Snapshot ${idx + 1}`} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                              </div>
                              <div style={{ padding: '3px 5px', fontSize: '9px', background: 'var(--surface)' }}>
                                <div style={{ fontWeight: 700 }}>⏱️ {dateStr}</div>
                                <div style={{ color: 'var(--warning)', fontWeight: 600, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }} title={s.reason}>
                                  {s.reason || 'Audit'}
                                </div>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })()}

              {selectedAttempt && (
                  <div>
                    {/* Filter Tabs Bar */}
                    <div className="outcome-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', flexWrap: 'wrap' }}>
                      <button 
                        type="button"
                        onClick={() => { setQuestionFilterTab(incorrectCount + unansweredCount > 0 ? 'incorrect' : 'all'); setAttemptCardIndex(0); }} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: '16px',
                          border: questionFilterTab === 'incorrect' || (questionFilterTab as string) === 'needs_review' ? '2px solid var(--danger)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'incorrect' || (questionFilterTab as string) === 'needs_review' ? 'var(--danger-bg)' : 'transparent',
                          color: questionFilterTab === 'incorrect' || (questionFilterTab as string) === 'needs_review' ? 'var(--danger)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        ⚠️ Mistakes ({incorrectCount + unansweredCount})
                      </button>
                      <button 
                        type="button"
                        onClick={() => { setQuestionFilterTab('correct'); setAttemptCardIndex(0); }} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: '16px',
                          border: questionFilterTab === 'correct' ? '2px solid var(--success)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'correct' ? 'var(--success-bg)' : 'transparent',
                          color: questionFilterTab === 'correct' ? 'var(--success)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        Correct ({correctCount})
                      </button>
                      <button 
                        type="button"
                        onClick={() => { setQuestionFilterTab('all'); setAttemptCardIndex(0); }} 
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          borderRadius: '16px',
                          border: questionFilterTab === 'all' ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                          background: questionFilterTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                          color: questionFilterTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                          cursor: 'pointer'
                        }}
                      >
                        All ({totalQuestionsCount})
                      </button>
                    </div>

                    {/* FLASHCARD MODE */}
                    {attemptViewMode === 'flashcard' && (
                      <div>
                        {/* Stepper Palette */}
                        <div style={{ display: 'flex', gap: '5px', overflowX: 'auto', paddingBottom: '8px', marginBottom: '10px', alignItems: 'center' }}>
                          {filteredQDs.map((qd: any, idx: number) => {
                            const isCorr = qd.isCorrect;
                            const isCur = attemptCardIndex === idx;
                            const qNumber = qd.qNumber || (selectedAttempt?.questionDetails ? selectedAttempt.questionDetails.indexOf(qd) + 1 : idx + 1);

                            return (
                              <button
                                key={`fc_step_${qd.questionId || idx}`}
                                type="button"
                                onClick={() => setAttemptCardIndex(idx)}
                                style={{
                                  padding: '4px 10px',
                                  borderRadius: '12px',
                                  fontSize: '11px',
                                  fontWeight: 800,
                                  cursor: 'pointer',
                                  flexShrink: 0,
                                  border: isCur ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                                  background: isCur ? 'var(--accent)' : isCorr ? 'var(--success-bg)' : 'var(--danger-bg)',
                                  color: isCur ? '#ffffff' : isCorr ? 'var(--success)' : 'var(--danger)',
                                  transform: isCur ? 'scale(1.05)' : 'scale(1)',
                                  transition: 'all 0.15s ease'
                                }}
                              >
                                {isCorr ? '🟢' : '🔴'} Q{qNumber}
                              </button>
                            );
                          })}
                        </div>

                        {/* Current Question Flashcard */}
                        {filteredQDs.length === 0 ? (
                          <div style={{ textAlign: 'center', padding: '24px 0', color: 'var(--text-faint)', fontSize: '12px' }}>📭 No questions match this filter.</div>
                        ) : (() => {
                          const safeIdx = Math.min(attemptCardIndex, filteredQDs.length - 1);
                          const qd = filteredQDs[safeIdx] || filteredQDs[0];
                          const isCorrect = qd.isCorrect;
                          const isUnattempted = isBlank(qd);
                          const bq = questionsMap[qd.questionCode] || null;
                          const explanation = bq?.solution || '';
                          const studentReason = getStudentReasonForQuestion(selectedAttempt, qd);
                          const qNumber = qd.qNumber || (selectedAttempt?.questionDetails ? selectedAttempt.questionDetails.indexOf(qd) + 1 : safeIdx + 1);

                          return (
                            <div style={{
                              background: 'var(--surface)',
                              border: '1.5px solid var(--border-light)',
                              borderRadius: 'var(--radius)',
                              padding: '14px 16px',
                              display: 'flex',
                              flexDirection: 'column',
                              gap: '10px'
                            }}>
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', fontSize: '11.5px', color: 'var(--text-muted)' }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                  <span style={{ fontWeight: 800, color: 'var(--text)' }}>
                                    Card {safeIdx + 1} of {filteredQDs.length} (Q{qNumber})
                                  </span>
                                  <span>•</span>
                                  <span>{bq?.difficulty?.toUpperCase() || 'MEDIUM'}</span>
                                  <span>•</span>
                                  <span>Time: {formatSeconds(qd.timeSpentSeconds || 0)}</span>
                                  {studentReason && (
                                    <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', padding: '1px 5px', borderRadius: '4px', fontSize: '9.5px', fontWeight: 'bold' }}>
                                      ⚠️ {studentReason}
                                    </span>
                                  )}
                                </div>
                                <span style={{
                                  fontWeight: 800,
                                  fontSize: '10px',
                                  padding: '2px 8px',
                                  borderRadius: '10px',
                                  background: isUnattempted ? 'var(--bg-soft)' : (isCorrect ? 'var(--success-bg)' : 'var(--danger-bg)'),
                                  color: isUnattempted ? 'var(--text-muted)' : (isCorrect ? 'var(--success)' : 'var(--danger)')
                                }}>
                                  {isUnattempted ? '⚪ Unattempted' : (isCorrect ? '🟢 Correct' : '🔴 Incorrect')}
                                </span>
                              </div>

                              {/* Question Details via SSOT QuestionDisplay */}
                              <QuestionDisplay
                                mode="review"
                                question={{
                                  text: qd.questionText || bq?.text || '',
                                  type: bq?.type || qd.type,
                                  options: bq?.options,
                                  correctAnswer: bq?.correctAnswer || bq?.answer || bq?.correct_answer || qd.correctAnswer,
                                  correctAnswers: bq?.correctAnswers || qd.correctAnswers,
                                  userAnswer: isUnattempted ? '' : (getOptionText(qd.questionCode, qd.userAnswer) || qd.userAnswer),
                                  solution: explanation,
                                  isCorrect: isCorrect
                                }}
                                isCorrect={isCorrect}
                                userAnswer={isUnattempted ? '' : (getOptionText(qd.questionCode, qd.userAnswer) || qd.userAnswer)}
                                correctAnswer={getOptionText(qd.questionCode, Array.isArray(qd.correctAnswer) ? qd.correctAnswer.join(', ') : qd.correctAnswer) || bq?.correctAnswer || qd.correctAnswer}
                                explanation={explanation}
                              />

                              {/* Bottom Navigation */}
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '8px', borderTop: '1px solid var(--border-light)' }}>
                                <button
                                  type="button"
                                  className="btn btn-secondary btn-sm"
                                  onClick={() => setAttemptCardIndex(prev => Math.max(0, prev - 1))}
                                  disabled={safeIdx === 0}
                                  style={{ padding: '4px 12px', fontSize: '11px', fontWeight: 700 }}
                                >
                                  ← Prev
                                </button>
                                <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                                  Card {safeIdx + 1} of {filteredQDs.length}
                                </span>
                                <button
                                  type="button"
                                  className="btn btn-primary btn-sm"
                                  onClick={() => setAttemptCardIndex(prev => Math.min(filteredQDs.length - 1, prev + 1))}
                                  disabled={safeIdx >= filteredQDs.length - 1}
                                  style={{ padding: '4px 14px', fontSize: '11px', fontWeight: 700 }}
                                >
                                  Next →
                                </button>
                              </div>
                            </div>
                          );
                        })()}
                      </div>
                    )}

                    {/* LIST MODE */}
                    {attemptViewMode === 'list' && (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        {filteredQDs.length === 0 ? (
                          <div style={{ textAlign: 'center', padding: '12px 0', color: 'var(--text-faint)', fontSize: '11.5px' }}>📭 No questions match this filter.</div>
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
                                  padding: '8px 10px',
                                  borderRadius: 'var(--radius-sm)',
                                  border: '1.5px solid var(--review-card-border)',
                                  background: 'var(--review-card-bg)',
                                  display: 'flex',
                                  flexDirection: 'column',
                                  gap: '4px'
                                }}
                              >
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '3px', fontSize: '10.5px', color: 'var(--text-muted)' }}>
                                  <div style={{ display: 'flex', alignItems: 'center' }}>
                                    <span style={{ fontWeight: 600 }}>Q{(() => {
                                      if (qd.qNumber != null && qd.qNumber !== '') return qd.qNumber;
                                      const actualIdx = selectedAttempt?.questionDetails
                                        ? selectedAttempt.questionDetails.indexOf(qd)
                                        : -1;
                                      return actualIdx !== -1 ? actualIdx + 1 : qIdx + 1;
                                    })()} ({bq?.difficulty?.toUpperCase() || 'MEDIUM'} • {bq?.bloomLevel || 'Understand'} • Time: {formatSeconds(qd.timeSpentSeconds || 0)})</span>
                                    {studentReason && (
                                      <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', padding: '1px 5px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold', marginLeft: '6px' }}>
                                        ⚠️ Reason: {studentReason}
                                      </span>
                                    )}
                                  </div>
                                  <span style={{ 
                                    fontWeight: 'bold', 
                                    fontSize: '9.5px',
                                    padding: '1px 5px',
                                    borderRadius: '10px',
                                    background: isUnattempted ? 'var(--bg-soft)' : (isCorrect ? 'var(--success-bg)' : 'var(--danger-bg)'),
                                    color: isUnattempted ? 'var(--text-muted)' : (isCorrect ? 'var(--success)' : 'var(--danger)') 
                                  }}>
                                    {isUnattempted ? 'Unattempted' : (isCorrect ? 'Correct' : 'Incorrect')}
                                  </span>
                                </div>

                                <QuestionDisplay
                                  mode="review"
                                  question={{
                                    text: qd.questionText || bq?.text || '',
                                    type: bq?.type || qd.type,
                                    options: bq?.options,
                                    correctAnswer: bq?.correctAnswer || bq?.answer || bq?.correct_answer || qd.correctAnswer,
                                    correctAnswers: bq?.correctAnswers || qd.correctAnswers,
                                    userAnswer: isUnattempted ? '' : (getOptionText(qd.questionCode, qd.userAnswer) || qd.userAnswer),
                                    solution: explanation,
                                    isCorrect: isCorrect
                                  }}
                                  isCorrect={isCorrect}
                                  userAnswer={isUnattempted ? '' : (getOptionText(qd.questionCode, qd.userAnswer) || qd.userAnswer)}
                                  correctAnswer={getOptionText(qd.questionCode, Array.isArray(qd.correctAnswer) ? qd.correctAnswer.join(', ') : qd.correctAnswer) || bq?.correctAnswer || qd.correctAnswer}
                                  explanation={explanation}
                                />
                              </div>
                            );
                          })
                        )}
                      </div>
                    )}
                  </div>
              )}
            </div>

            <div className="modal-footer" style={{ padding: '8px 12px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '8px', background: 'var(--surface)' }}>
              <button 
                type="button"
                style={{ background: 'transparent', border: 'none', padding: '4px 8px', fontSize: '11px', color: 'var(--danger)', textDecoration: 'underline', cursor: 'pointer', fontWeight: 600 }}
                onClick={async () => {
                  const studentName = selectedAttempt.studentName;
                  const attemptId = selectedAttempt.id;
                  setStudentModalOpen(false);
                  setSelectedAttempt(null);
                  await handleResetAttempt(attemptId, studentName);
                }}
              >
                Reset Attempt
              </button>
              <button className="btn btn-secondary btn-sm" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => { setStudentModalOpen(false); setSelectedAttempt(null); }}>Close</button>
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
              <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '10px', flexWrap: 'wrap' }}>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="reassignOpenMode" 
                    checked={reassignOpenMode === 'immediate'} 
                    onChange={() => {
                      setReassignOpenMode('immediate');
                      setReassignPresetSlot(null);
                    }} 
                    style={{ cursor: 'pointer' }}
                  /> Immediate
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                  <input 
                    type="radio" 
                    name="reassignOpenMode" 
                    checked={reassignOpenMode === 'scheduled' && !reassignPresetSlot} 
                    onChange={() => {
                      setReassignOpenMode('scheduled');
                      setReassignPresetSlot(null);
                      const start = reassignStartAtStr || toLocalISOString(new Date());
                      setReassignStartAtStr(start);
                      setReassignEndAtStr(calculateEndDatetime(start, reassignDuration || 30));
                    }} 
                    style={{ cursor: 'pointer' }}
                  /> Scheduled
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: reassignPresetSlot === '6am' ? 'rgba(52, 152, 219, 0.2)' : 'rgba(52, 152, 219, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.25)' }}>
                  <input 
                    type="checkbox" 
                    checked={reassignPresetSlot === '6am'} 
                    onChange={(e) => {
                      const checked = e.target.checked;
                      if (checked) {
                        setReassignOpenMode('scheduled');
                        setReassignPresetSlot('6am');
                        const times = getMorningTestTimes(reassignDuration || 30);
                        setReassignStartAtStr(times.startStr);
                        setReassignEndAtStr(times.endStr);
                      } else {
                        setReassignPresetSlot(null);
                      }
                    }} 
                    style={{ cursor: 'pointer' }}
                  /> ☀️ 6 AM Test
                </label>
                <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: reassignPresetSlot === '9pm' ? 'rgba(168, 85, 247, 0.2)' : 'rgba(168, 85, 247, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(168, 85, 247, 0.25)' }}>
                  <input 
                    type="checkbox" 
                    checked={reassignPresetSlot === '9pm'} 
                    onChange={(e) => {
                      const checked = e.target.checked;
                      if (checked) {
                        setReassignOpenMode('scheduled');
                        setReassignPresetSlot('9pm');
                        const times = getEveningTestTimes(reassignDuration || 30);
                        setReassignStartAtStr(times.startStr);
                        setReassignEndAtStr(times.endStr);
                      } else {
                        setReassignPresetSlot(null);
                      }
                    }} 
                    style={{ cursor: 'pointer' }}
                  /> 🌙 9 PM Test
                </label>
              </div>

              {reassignOpenMode === 'scheduled' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '10px' }}>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)', marginBottom: '3px' }}>Start Datetime</label>
                      <DateTimeInputDMY 
                        value={reassignStartAtStr} 
                        disabled={!!reassignPresetSlot} 
                        onChange={(val) => { 
                          setReassignStartAtStr(val); 
                          setReassignEndAtStr(calculateEndDatetime(val, reassignDuration || 30)); 
                        }} 
                      />
                    </div>
                    <div style={{ flex: 1 }}>
                      <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)', marginBottom: '3px' }}>End Datetime</label>
                      <DateTimeInputDMY value={reassignEndAtStr} disabled={!!reassignPresetSlot} onChange={(val) => setReassignEndAtStr(val)} />
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
                    if (raw === '') {
                      setReassignDuration('' as any);
                      return;
                    }
                    const dur = Number(raw);
                    setReassignDuration(isNaN(dur) ? '' as any : dur);
                    if (reassignStartAtStr && !isNaN(dur) && dur > 0) {
                      setReassignEndAtStr(calculateEndDatetime(reassignStartAtStr, dur));
                    }
                  }}
                  onBlur={() => {
                    if (!reassignDuration || Number(reassignDuration) < 1) {
                      const fallback = 45;
                      setReassignDuration(fallback);
                      if (reassignStartAtStr) {
                        setReassignEndAtStr(calculateEndDatetime(reassignStartAtStr, fallback));
                      }
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

      {/* Proctoring Snapshot Zoom Modal */}
      {previewSnapshot && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', borderBottom: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}>
              <div>
                <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 700 }}>
                  📸 Proctoring Snapshot Detail
                </h4>
                <span style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>
                  {previewSnapshot.timestamp ? new Date(previewSnapshot.timestamp).toLocaleTimeString() : ''} • Reason: <strong style={{ color: 'var(--warning)' }}>{previewSnapshot.reason || 'Audit'}</strong>
                </span>
              </div>
              <button className="close-modal" onClick={() => setPreviewSnapshot(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
            <div style={{ padding: '16px', background: '#000', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
              <img src={previewSnapshot.src} alt="Proctoring Zoom" style={{ maxWidth: '100%', maxHeight: '60vh', objectFit: 'contain' }} />
            </div>
            <div style={{ padding: '10px 16px', background: 'var(--bg-soft)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px', color: 'var(--text-muted)' }}>
              <span>🔒 Admin-only log • Auto-purges after 18h</span>
              <button className="btn btn-secondary btn-sm" onClick={() => setPreviewSnapshot(null)}>Close</button>
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

