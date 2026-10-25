'use client';

import React, { useEffect, useRef, useState, useCallback, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { stripOptionLabel, preprocessMathText, parseAnswerList, isOptionSelectedByUser, isOptionCorrect, getQuestionCorrectAnswer, getRawOptionKey, getRawOptionText, extractAssertionAndReason, isMultipleChoiceType, isSingleChoiceType, isTrueFalseType, isAssertionReasonType, isNumericalType, isFillBlanksType, isObjectiveType, resolveOptionDisplayText, DEFAULT_ASSERTION_REASON_OPTIONS, getOptionText } from '@/lib/questionTypes';
import QuestionDisplay, { RichMathText } from '@/components/QuestionDisplay';
import { useMathRender } from '@/hooks/useMathRender';
import { db } from '@/lib/firebase/firestore';
import { useExamTimer } from '@/hooks/useExamTimer';
import { useLiveExam } from '@/hooks/useLiveExam';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';
import { InterruptionLockoutModal } from '@/components/InterruptionLockoutModal';
import { ExamErrorBoundary } from '@/components/ExamErrorBoundary';
import { parseDateToMs } from '@/lib/dateUtils';
import { RTC_CONFIG } from '@/lib/rtcConfig';
import { Question } from '@/types/question.types';
import { Exam } from '@/types/exam.types';


// Extend window interface for CDN scripts
declare global {
  interface Window {
    FaceMesh: any;
    Camera: any;
    renderMathInElement: any;
  }
}

function TakeExamContent() {
  const { firebaseUser, logout, user } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();
  const examId = searchParams.get('examId') || searchParams.get('id');
  const isPreviewMode = searchParams.get('preview') === 'true' || user?.role === 'admin';

  const [exam, setExam] = useState<Exam | null>(null);
  const [assignment, setAssignment] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Grace period timer ref
  const startTimeRef = useRef<number>(0);

  // Exam state
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState<Array<{ answer: string; timeSpentSeconds: number }>>([]);
  const [startedAt] = useState<number>(Date.now());
  const [examSubmitted, setExamSubmitted] = useState(false);

  // UI state
  const [isMounted, setIsMounted] = useState(false);
  const [cameraModalOpen, setCameraModalOpen] = useState(true);
  const [isStartingExam, setIsStartingExam] = useState(false);

  useEffect(() => {
    if (!cameraModalOpen && !startTimeRef.current) {
      startTimeRef.current = Date.now();
    }
  }, [cameraModalOpen]);
  const [reviewModalOpen, setReviewModalOpen] = useState(false);
  const [blockingMessage, setBlockingMessage] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitCooldown, setSubmitCooldown] = useState(0);
  const [submitErrorMessage, setSubmitErrorMessage] = useState('');
  const [submissionRescueOpen, setSubmissionRescueOpen] = useState(false);
  const [tokenCopied, setTokenCopied] = useState(false);
  const questionTimeSpentRef = useRef<number[]>([]);
  const lastSavedAnswersHashRef = useRef<string>('');

  // Submit cooldown timer
  useEffect(() => {
    if (submitCooldown <= 0) return;
    const timer = setInterval(() => {
      setSubmitCooldown(prev => Math.max(0, prev - 1));
    }, 1000);
    return () => clearInterval(timer);
  }, [submitCooldown]);

  const [wrongAnswers, setWrongAnswers] = useState<any[]>([]);
  const [unattemptedQuestions, setUnattemptedQuestions] = useState<any[]>([]);
  const [reviewedQuestions, setReviewedQuestions] = useState<Set<number>>(new Set());
  const [selectedReasons, setSelectedReasons] = useState<{[key: number]: string}>({});
  const [reviewScores, setReviewScores] = useState<{ score: number, totalMarks: number, percentage: number } | null>(null);
  const [reviewSecondsRemaining, setReviewSecondsRemaining] = useState(0);

  useEffect(() => {
    if (!reviewModalOpen) {
      setReviewSecondsRemaining(0);
      return;
    }
    const totalMistakes = wrongAnswers.length + unattemptedQuestions.length;
    const targetSeconds = Math.min(45, Math.max(10, totalMistakes * 6));
    setReviewSecondsRemaining(targetSeconds);

    const timer = setInterval(() => {
      setReviewSecondsRemaining(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [reviewModalOpen, wrongAnswers.length, unattemptedQuestions.length]);
  const [reviewSubmitting, setReviewSubmitting] = useState(false);
  const [showResultModal, setShowResultModal] = useState(false);
  const [activeViolationWarning, setActiveViolationWarning] = useState<string | null>(null);
  const [questionFilterTab, setQuestionFilterTab] = useState<'all' | 'incorrect' | 'unanswered'>('all');
  const [autoSubmittedReason, setAutoSubmittedReason] = useState<string | null>(null);

  // Refs
  const videoRef = useRef<HTMLVideoElement | null>(null);

  const questionContainerRef = useRef<HTMLDivElement | null>(null);
  const reviewContainerRef = useRef<HTMLDivElement | null>(null);
  const lastActiveTimeRef = useRef<number>(Date.now());
  const prevTabViolationsRef = useRef<number>(0);
  // Hook 1: countdown timer
  const {
    timeRemaining,
    setTimeRemaining,
    formattedTime,
    addExtraTime
  } = useExamTimer({
    initialSeconds: exam ? ((exam.duration || 0) * 60) : 0,
    isPaused: loading || examSubmitted || !exam || cameraModalOpen,
    onTimeUp: () => {
      // Non-blocking auto-submit on time expiry
      submitExamAction();
    },
    onTick: () => {
      // Light-weight ref ticker to prevent 1,800 unnecessary React re-renders and preserve debounce timer
      if (questionTimeSpentRef.current && questionTimeSpentRef.current[currentQIndex] !== undefined) {
        questionTimeSpentRef.current[currentQIndex] += 1;
      }
    }
  });

  const answeredCount = useMemo(() => {
    return userAnswers.filter(a => a.answer !== '').length;
  }, [userAnswers]);

  const questionsToReview = useMemo(() => {
    return [
      ...wrongAnswers.map((w, idx) => ({ ...w, globalIdx: idx, type: 'incorrect' })),
      ...unattemptedQuestions.map((u, idx) => ({ ...u, globalIdx: wrongAnswers.length + idx, type: 'unanswered' }))
    ];
  }, [wrongAnswers, unattemptedQuestions]);

  const filteredQuestionsToReview = useMemo(() => {
    return questionsToReview.filter(q => {
      if (questionFilterTab === 'incorrect') return q.type === 'incorrect';
      if (questionFilterTab === 'unanswered') return q.type === 'unanswered';
      return true;
    });
  }, [questionsToReview, questionFilterTab]);

  const isLateStart = useMemo(() => {
    if (!assignment || assignment.openMode !== 'scheduled' || !assignment.startAt) return false;
    const startMs = parseDateToMs(assignment.startAt);
    if (startMs <= 0) return false;
    return (startedAt - startMs) > 2 * 60 * 1000;
  }, [assignment, startedAt]);

  const {
    tabViolations,
    setTabViolations,
    proctoringViolations,
    setProctoringViolations,
    isInterrupted,
    resumeExam,
    cameraStatus,
    cameraStream,
    micBypassed,
    proctoringSnapshots,
    addProctoringSnapshot,
    startCameraStream,
    stopCameraStream,
    cleanupProctoring
  } = useLiveExam({
    examId: examId || '',
    examName: exam?.name || 'Untitled Exam',
    studentCode: user?.studentCode || '',
    studentName: user?.name || user?.email || 'Student',
    examType: 'mcq',
    totalQuestions: exam?.questions?.length || null,
    currentQuestionIndex: currentQIndex,
    answeredCount,
    cameraVideoRef: videoRef,
    autonomous: (user as any)?.autonomous || false,
    started: !cameraModalOpen && !examSubmitted,
    isLate: isLateStart
  });

  const activeQuestionForHeuristic = exam?.questions?.[currentQIndex];
  const isNumerical = useMemo(() => {
    if (!activeQuestionForHeuristic) return false;
    // Database explicit relaxProctoring or isNumerical overrides
    if ((activeQuestionForHeuristic as any).relaxProctoring === true || (activeQuestionForHeuristic as any).isNumerical === true) {
      return true;
    }
    const rawText = activeQuestionForHeuristic.text ?? (activeQuestionForHeuristic as any).questionText ?? '';
    const text = typeof rawText === 'string' ? rawText : (rawText && typeof rawText === 'object' ? JSON.stringify(rawText) : String(rawText || ''));
    const textLower = text ? text.toLowerCase() : '';
    
    // Detect KaTeX rendering blocks \(...\), \[...\], $...$, or LaTeX macros (\frac, \ce, \sqrt, \vec, \sum, etc.)
    const optionsText = Array.isArray(activeQuestionForHeuristic.options)
      ? activeQuestionForHeuristic.options.map((o: any) => typeof o === 'object' ? (o?.text || o?.value || '') : String(o || '')).join(' ')
      : '';
    const fullContent = text + ' ' + optionsText;

    const katexInlineCount = (fullContent.match(/\\\([\s\S]*?\\\)/g) || []).length;
    const katexDisplayCount = (fullContent.match(/\\\[[\s\S]*?\\\]/g) || []).length;
    const katexDollarCount = (fullContent.match(/\$[^$]+\$/g) || []).length;
    const katexMacroCount = (fullContent.match(/\\[a-zA-Z]+/g) || []).length;

    const totalKatexBlocks = katexInlineCount + katexDisplayCount + katexDollarCount;
    // Relax proctoring if 2 or more KaTeX rendering blocks or LaTeX macros are detected
    if (totalKatexBlocks >= 2 || katexMacroCount >= 2) {
      return true;
    }

    const mathKeywords = [
      'calculate', 'solve', 'evaluate', 'find the value', 'find the length', 
      'find the area', 'simplify', 'ratio', 'percentage', 'theorem', 
      'derivative', 'integral', 'factorize', 'expand', 'equation', 'expression',
      'probability', 'mean', 'median', 'mode', 'standard deviation', 'calculate',
      'numerical', 'geometry', 'algebra', 'prove', 'find the', 'what is the value'
    ];
    if (mathKeywords.some(keyword => textLower.includes(keyword))) return true;

    const mathSymbols = [
      '\\frac', '\\sqrt', '\\times', '\\div', '\\angle', '\\cong', '\\parallel', 
      '\\Delta', '\\pi', '\\theta', '\\alpha', '\\beta', '^', '=', '+', '-', '*', '/'
    ];
    if (mathSymbols.some(symbol => textLower.includes(symbol))) return true;

    if (/\d+/.test(textLower)) return true;

    return false;
  }, [activeQuestionForHeuristic]);

  const {
    faceStatus,
    faceStatusClass,
    noFaceDetected,
    isLookingAway,
    permissionBlocked,
    micAttemptsRemaining,
    setMicAttemptsRemaining,
    setPermissionBlocked,
    handleRunCheck,
    stopAllProctoring,
    recalibrateBaseline
  } = useProctoring({
    videoRef,
    enabled: !cameraModalOpen && !examSubmitted,
    lockdownShortcuts: true,
    lockdownContextMenu: true,
    lockdownWindowFocus: false, // Managed exclusively by useLiveExam SSOT (Rule 2.S)
    lockdownFullscreen: false,  // Managed exclusively by useLiveExam SSOT (Rule 2.S)
    startCameraStream,
    stopCameraStream,
    cleanupLiveExam: cleanupProctoring,
    isNumerical: isNumerical,
    onSnapshotCaptured: addProctoringSnapshot,
    onViolation: (type) => {
      if (type === 'tab_switch') {
        // Tab switch violations are strictly managed and debounced by useLiveExam SSOT hook
        return;
      } else if (type === 'no_face') {
        setProctoringViolations(prev => ({ ...prev, noFace: prev.noFace + 1 }));
      } else if (type === 'multiple_faces') {
        setProctoringViolations(prev => ({ ...prev, multipleFaces: prev.multipleFaces + 1 }));
      } else if (type === 'gaze') {
        setProctoringViolations(prev => ({ ...prev, lookingAway: prev.lookingAway + 1 }));
      } else if (type === 'movement') {
        setProctoringViolations(prev => ({ ...prev, headMovement: prev.headMovement + 1 }));
      }
    }
  });

  // Recalibrate baseline pose as soon as camera modal closes & exam starts
  useEffect(() => {
    if (!cameraModalOpen && !examSubmitted) {
      recalibrateBaseline();
    }
  }, [cameraModalOpen, examSubmitted, recalibrateBaseline]);

  useEffect(() => {
    if (cameraModalOpen || examSubmitted) {
      setActiveViolationWarning(null);
      return;
    }
    if (noFaceDetected) {
      setActiveViolationWarning('⚠️ Face not detected! Please look at the camera.');
    } else if (faceStatus.includes('Multiple')) {
      setActiveViolationWarning('⚠️ Multiple faces detected! Only you should be in front of the camera.');
    } else if (isLookingAway) {
      setActiveViolationWarning('⚠️ Please keep your eyes on the exam screen!');
    } else {
      setActiveViolationWarning(null);
    }
  }, [noFaceDetected, faceStatus, isLookingAway, cameraModalOpen, examSubmitted]);

  const audioLevel = useAudioLevel(cameraStream);

  useMathRender([currentQIndex, exam]);

  useEffect(() => {
    if (videoRef.current && cameraStream && videoRef.current.srcObject !== cameraStream) {
      videoRef.current.srcObject = cameraStream;
      videoRef.current.play().catch(() => {});
    }
  }, [cameraStream, cameraModalOpen]);
  
  const faceStatusRef = useRef('👤 Initializing Face Detection...');

  // Auto-autosave keys
  const getSaveKey = () => `exam_state_${examId}_${user?.uid || 'guest'}`;

  // 1. Fetch exam configuration
  useEffect(() => {
    if (!examId || !firebaseUser) return;
    
    const fetchExam = async () => {
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch(`/api/student/exams?id=${encodeURIComponent(examId)}`, {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });
        if (!res.ok) {
          const errData = await res.json();
          throw new Error(errData.message || 'Failed to load exam');
        }
        const data = await res.json();
        
        // Check if we are resuming an active attempt
        let isResuming = false;
        try {
          const saved = localStorage.getItem(getSaveKey());
          if (saved) {
            const parsed = JSON.parse(saved);
            if (parsed.examId === examId && Date.now() - parsed.timestamp < 3600000) {
              isResuming = true;
            }
          }
        } catch {}

        // Enforce 5-minute late entry limit for scheduled slots (unless resuming)
        if (!isResuming && data.assignment && data.assignment.openMode === 'scheduled' && data.assignment.startAt) {
          const enforceLate = data.assignment.lateEntryRestriction === true;
          if (enforceLate) {
            const startAtMs = parseDateToMs(data.assignment.startAt);
            if (startAtMs > 0) {
              const lateLimitMs = startAtMs + (5 * 60 * 1000); // 5 minutes late limit
              if (Date.now() > lateLimitMs) {
                throw new Error('Late entry is not allowed. You cannot start the exam more than 5 minutes after the scheduled start time.');
              }
            }
          }
        }

        setExam(data.exam);
        setAssignment(data.assignment || null);
        
        // Initialize userAnswers array
        const initialAnswers = data.exam.questions.map(() => ({ answer: '', timeSpentSeconds: 0 }));
        questionTimeSpentRef.current = new Array(data.exam.questions.length).fill(0);
        
        let initialTimeRemaining = (data.exam?.duration || 30) * 60;
        if (data.assignment && data.assignment.openMode === 'scheduled' && data.assignment.endAt) {
          const endAtMs = parseDateToMs(data.assignment.endAt);
          if (endAtMs > 0) {
            const secondsUntilEnd = Math.floor((endAtMs - Date.now()) / 1000);
            if (secondsUntilEnd <= 0) {
              if (!isResuming) {
                throw new Error('The scheduled time for this exam has already ended.');
              }
              // Active resuming student whose window just expired: lock inputs immediately and submit
              initialTimeRemaining = 0;
            } else if (!isNaN(secondsUntilEnd) && secondsUntilEnd > 0) {
              initialTimeRemaining = Math.min(initialTimeRemaining, secondsUntilEnd);
            }
          }
        }
        if (isNaN(initialTimeRemaining) || initialTimeRemaining < 0) {
          initialTimeRemaining = 0;
        }

        // Check autosave
        try {
          const saved = localStorage.getItem(getSaveKey());
          if (saved) {
            const parsed = JSON.parse(saved);
            const totalQuestionsCount = (data.exam?.questions || []).length;
            if (parsed.examId === examId && Date.now() - parsed.timestamp < 3600000 && totalQuestionsCount > 0) {
              const safeIndex = Math.max(0, Math.min(totalQuestionsCount - 1, Number(parsed.currentQIndex) || 0));
              let safeAnswers = initialAnswers;
              if (Array.isArray(parsed.userAnswers) && parsed.userAnswers.length === totalQuestionsCount) {
                safeAnswers = parsed.userAnswers;
              } else if (Array.isArray(parsed.userAnswers)) {
                safeAnswers = initialAnswers.map((defaultAns: any, i: number) => parsed.userAnswers[i] || defaultAns);
              }

              questionTimeSpentRef.current = safeAnswers.map((a: any) => Number(a?.timeSpentSeconds) || 0);
              setUserAnswers(safeAnswers);
              setCurrentQIndex(safeIndex);
              
              let resumedTime = parsed.timeRemaining ?? ((data.exam?.duration || 30) * 60);
              if (data.assignment && data.assignment.openMode === 'scheduled' && data.assignment.endAt) {
                const endAtMs = parseDateToMs(data.assignment.endAt);
                if (endAtMs > 0) {
                  const secondsUntilEnd = Math.floor((endAtMs - Date.now()) / 1000);
                  if (!isNaN(secondsUntilEnd)) {
                    resumedTime = Math.min(resumedTime, Math.max(0, secondsUntilEnd));
                  }
                }
              }
              if (isNaN(resumedTime) || resumedTime < 0) {
                resumedTime = 0;
              }
              
              setTimeRemaining(resumedTime);
              setTabViolations(parsed.tabViolations || 0);
              const pv = parsed.proctoringViolations;
              setProctoringViolations({
                noFace: Number(pv?.noFace) || 0,
                multipleFaces: Number(pv?.multipleFaces) || 0,
                lookingAway: Number(pv?.lookingAway) || 0,
                headMovement: Number(pv?.headMovement) || 0
              });
              setLoading(false);
              return;
            }
          }
        } catch {}

        setUserAnswers(initialAnswers);
        setTimeRemaining(initialTimeRemaining);
      } catch (err: any) {
        console.error(err);
        setError(err.message || 'Error loading exam');
      } finally {
        setLoading(false);
      }
    };

    fetchExam();
  }, [examId, firebaseUser]);


  const [diagnosticRunning, setDiagnosticRunning] = useState(true);

  // 1b. Auto-trigger camera diagnostic check on mount with a 2.5-second delay to release device locks
  useEffect(() => {
    if (cameraModalOpen && !cameraStream && exam) {
      setDiagnosticRunning(true);
      const timer = setTimeout(async () => {
        await handleRunCheck();
        setDiagnosticRunning(false);
      }, 2500);
      return () => clearTimeout(timer);
    } else if (cameraStream) {
      setDiagnosticRunning(false);
    }
  }, [cameraModalOpen, cameraStream, exam]);




  // 3. Proctoring violation limits & Auto-submit
  useEffect(() => {
    if (examSubmitted || !exam) return;

    // ONLY tab switching triggers auto-submission, at 3 violations.
    const crossedTabSubmit = tabViolations >= 3;

    if (crossedTabSubmit) {
      setAutoSubmittedReason('Auto-submitted due to exceeding allowed tab switches (3/3).');
      submitExamAction(tabViolations, true);
      return;
    }

    if (tabViolations > prevTabViolationsRef.current) {
      setActiveViolationWarning(`⚠️ WARNING: Tab switch / focus loss detected! (Violation ${tabViolations}/3). Reaching 3/3 will auto-submit your exam.`);
    }

    prevTabViolationsRef.current = tabViolations;
  }, [tabViolations, examSubmitted, exam]);




  // Stop webcam stream and cleanup when component unmounts
  useEffect(() => {
    return () => {
      stopAllProctoring();
    };
  }, []);

  // 4a. Immediate Local Storage Autosave (Instant on device, zero server cost)
  useEffect(() => {
    if (!exam || examSubmitted || cameraModalOpen) return;
    try {
      const compiled = userAnswers.map((ua, idx) => ({
        ...ua,
        timeSpentSeconds: questionTimeSpentRef.current[idx] ?? ua.timeSpentSeconds ?? 0
      }));
      const state = {
        examId,
        userAnswers: compiled,
        currentQIndex,
        timeRemaining,
        tabViolations,
        proctoringViolations,
        timestamp: Date.now()
      };
      localStorage.setItem(getSaveKey(), JSON.stringify(state));
    } catch {}
  }, [userAnswers, currentQIndex, timeRemaining, tabViolations, proctoringViolations, exam, examSubmitted, cameraModalOpen, examId]);

  const answersHash = useMemo(() => {
    return userAnswers.map(a => a.answer || '').join('||');
  }, [userAnswers]);

  // 4b. Throttled Server Autosave (Every 60s debounced, ONLY when actual selected answers change)
  useEffect(() => {
    if (!exam || examSubmitted || cameraModalOpen || !firebaseUser || !examId) return;
    if (!userAnswers || userAnswers.length === 0) return;
    if (answersHash === lastSavedAnswersHashRef.current) return;

    const timer = setTimeout(async () => {
      try {
        const idToken = await firebaseUser.getIdToken();
        const compiled = userAnswers.map((ua, idx) => ({
          ...ua,
          timeSpentSeconds: questionTimeSpentRef.current[idx] ?? ua.timeSpentSeconds ?? 0
        }));
        await fetch('/api/student/exams', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({
            action: 'autosave',
            examId,
            userAnswers: compiled
          })
        });
        lastSavedAnswersHashRef.current = answersHash;
      } catch (e) {
        console.warn("DB Autosave failed (cached locally):", e);
      }
    }, 60000);

    return () => clearTimeout(timer);
  }, [answersHash, exam, examSubmitted, cameraModalOpen, examId, firebaseUser, userAnswers]);

  // 5. LateX rendering trigger on current question




  const handleProceedToExam = async () => {
    if (isStartingExam) return;
    setIsStartingExam(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/student/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'start', examId })
      });
      if (!res.ok) {
        throw new Error('Server returned an error starting the exam.');
      }
      setCameraModalOpen(false);
      
      // Trigger fullscreen
      try {
        document.documentElement.requestFullscreen().catch(() => {});
      } catch {}
    } catch (e) {
      console.error("Failed to set in-progress status:", e);
      alert('❌ Failed to establish exam session with server. Please check your internet connection and try again.');
    } finally {
      setIsStartingExam(false);
    }
  };





  const submitExamAction = async (finalTabViolations?: number, proctoringViolationTriggered?: boolean) => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    setSubmitErrorMessage('');
    stopAllProctoring();
    setBlockingMessage('Submitting exam... Please do not close this window.');
    
    const activeTabViolations = finalTabViolations ?? tabViolations;
    const durationSpent = exam ? (((exam.duration || 0) * 60) - timeRemaining) : 0;
    const compiledAnswers = userAnswers.map((ua, idx) => ({
      ...ua,
      timeSpentSeconds: questionTimeSpentRef.current[idx] ?? ua.timeSpentSeconds ?? 0
    }));

    try {
      const idToken = await firebaseUser!.getIdToken();
      const startMs = parseDateToMs(assignment?.startAt);
      const isLateStart = Boolean(
        assignment &&
        assignment.openMode === 'scheduled' &&
        startMs > 0 &&
        (startedAt - startMs > 2 * 60 * 1000)
      );

      // Fast Lane Submission: pure text payload (< 3 KB) executes in ~50ms
      const res = await fetch('/api/student/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId,
          userAnswers: compiledAnswers,
          durationSpent,
          preview: isPreviewMode,
          tabViolations: activeTabViolations,
          proctoringViolations,
          startedAt,
          isLate: isLateStart,
          proctoringViolationTriggered: !!proctoringViolationTriggered,
          micBypassed: !!micBypassed,
          proctoringSnapshots: (proctoringSnapshots || []).slice(-5),
          violations: {
            tabOutCount: activeTabViolations,
            noFaceCount: proctoringViolations.noFace || 0,
            multipleFacesCount: proctoringViolations.multipleFaces || 0,
            lookingAwayCount: proctoringViolations.lookingAway || 0,
            headMovementCount: proctoringViolations.headMovement || 0
          }
        })
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.message || 'Submission failed.');
      }

      setExamSubmitted(true);
      setBlockingMessage('');
      setSubmissionRescueOpen(false);
      localStorage.removeItem(getSaveKey());

      // Async Background Lane: upload compressed proctoring snapshots without blocking student feedback
      if (proctoringSnapshots && proctoringSnapshots.length > 0 && !isPreviewMode) {
        firebaseUser!.getIdToken().then(freshToken => {
          fetch('/api/student/exams', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${freshToken}`
            },
            body: JSON.stringify({
              action: 'upload_snapshots',
              examId,
              screenshots: proctoringSnapshots
            })
          }).catch(err => console.warn('Background snapshot sync failed:', err));
        }).catch(() => {});
      }
      
      if (resData.status === 'student_review') {
        setWrongAnswers(resData.wrongAnswers || []);
        setUnattemptedQuestions(resData.unattemptedQuestions || []);
        setReviewScores({
          score: resData.score,
          totalMarks: resData.totalMarks,
          percentage: resData.percentage
        });
        setReviewedQuestions(new Set());
        setSelectedReasons({});
        setReviewModalOpen(true);
      } else {
        setReviewScores({
          score: resData.score,
          totalMarks: resData.totalMarks,
          percentage: resData.percentage
        });
        setShowResultModal(true);
      }
    } catch (err: any) {
      console.error('Submit exam error:', err);
      setSubmitCooldown(0); // Allow immediate retry on failure
      setSubmissionRescueOpen(true);
      setSubmitErrorMessage(`⚠️ ${err.message || 'Connection lost'}. All answers are securely saved on your device.`);
      setBlockingMessage('');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleCopyEmergencyToken = () => {
    try {
      const payload = {
        examId,
        studentCode: user?.studentCode,
        studentName: user?.name,
        timestamp: Date.now(),
        userAnswers: userAnswers.map((ua, idx) => ({
          ...ua,
          timeSpentSeconds: questionTimeSpentRef.current[idx] ?? ua.timeSpentSeconds ?? 0
        }))
      };
      const token = btoa(unescape(encodeURIComponent(JSON.stringify(payload))));
      navigator.clipboard.writeText(token);
      setTokenCopied(true);
      setTimeout(() => setTokenCopied(false), 4000);
    } catch (e) {
      console.error('Failed to copy token:', e);
    }
  };

  const handleDownloadBackup = () => {
    try {
      const payload = {
        examId,
        studentCode: user?.studentCode,
        studentName: user?.name,
        timestamp: new Date().toISOString(),
        userAnswers: userAnswers.map((ua, idx) => ({
          ...ua,
          timeSpentSeconds: questionTimeSpentRef.current[idx] ?? ua.timeSpentSeconds ?? 0
        }))
      };
      const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `backup_${examId}_${user?.studentCode || 'student'}.json`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error('Failed to download backup:', e);
    }
  };

  // Answer handler
  const handleSelectOption = (qIdx: number, value: string) => {
    setUserAnswers(prev => {
      const updated = [...prev];
      const currentVal = updated[qIdx]?.answer || '';
      const newVal = currentVal === value ? '' : value;
      updated[qIdx] = { ...updated[qIdx], answer: newVal };
      return updated;
    });
  };

  const handleCheckboxOption = (qIdx: number, value: string) => {
    setUserAnswers(prev => {
      const updated = [...prev];
      let currentVal: string[] = [];
      try {
        currentVal = JSON.parse(updated[qIdx].answer || '[]');
      } catch {}
      
      if (currentVal.includes(value)) {
        currentVal = currentVal.filter(v => v !== value);
      } else {
        currentVal.push(value);
      }

      updated[qIdx] = { ...updated[qIdx], answer: JSON.stringify(currentVal) };
      return updated;
    });
  };

  const handleTextInput = (qIdx: number, value: string) => {
    setUserAnswers(prev => {
      const updated = [...prev];
      updated[qIdx] = { ...updated[qIdx], answer: value };
      return updated;
    });
  };

  const totalQCount = exam?.questions?.length || 1;
  const safeQIndex = Math.max(0, Math.min(totalQCount - 1, currentQIndex));
  const currentQuestion = exam?.questions?.[safeQIndex] || exam?.questions?.[0] || { id: 'fallback', text: '', options: [], marks: 1, type: 'mcq' };
  const currentAnswerObj = userAnswers[safeQIndex];
  const currentAnswer = currentAnswerObj?.answer || '';

  const handleSelectOptionCurrent = (letter: string) => {
    // Strictly disable input if exam time expired or already submitting/submitted
    if (!currentQuestion || timeRemaining <= 0 || isSubmitting || examSubmitted) return;
    if (isMultipleChoiceType(currentQuestion.type)) {
      handleCheckboxOption(safeQIndex, letter);
    } else {
      handleSelectOption(safeQIndex, letter);
    }
  };

  const handleTextInputCurrent = (val: string) => {
    // Strictly disable input if exam time expired or already submitting/submitted
    if (!currentQuestion || timeRemaining <= 0 || isSubmitting || examSubmitted) return;
    handleTextInput(safeQIndex, val);
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading exam configurations...
        </div>
      </div>
    );
  }

  if (error || !exam) {
    const isBlockedNotice = error.includes('pending review') || error.includes('self-reflection') || error.includes('missed') || error.includes('parent') || error.includes('blocked');
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div style={{
          maxWidth: '540px',
          width: '100%',
          textAlign: 'center',
          padding: '32px 24px',
          background: 'var(--surface)',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--border-light)',
          boxShadow: 'var(--shadow-lg)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '14px'
        }}>
          <div style={{ fontSize: '3.5rem' }}>{isBlockedNotice ? '🔒' : '⚠️'}</div>
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
              {isBlockedNotice ? 'Action Required to Unlock Exam' : 'Exam Unavailable'}
            </h3>
            {isBlockedNotice && (
              <div style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--primary)', marginTop: '4px' }}>
                परीक्षेचा लॉक काढण्यासाठी आवश्यक कृती
              </div>
            )}
          </div>
          
          <div style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', margin: 0, textAlign: 'center', width: '100%' }}>
            {error ? (
              error.split('\n\n').map((paragraph, idx) => (
                <p key={idx} style={{ margin: '0 0 10px 0', whiteSpace: 'pre-line' }}>
                  {paragraph}
                </p>
              ))
            ) : (
              <p style={{ margin: '0 0 10px 0' }}>Exam configurations failed to load.</p>
            )}

            {isBlockedNotice && (
              <div style={{
                background: 'rgba(59, 130, 246, 0.08)',
                border: '1px solid rgba(59, 130, 246, 0.25)',
                borderRadius: '8px',
                padding: '12px 14px',
                color: 'var(--text)',
                fontSize: '13px',
                lineHeight: '1.6',
                textAlign: 'left',
                marginTop: '12px'
              }}>
                <div style={{ fontWeight: 700, marginBottom: '4px', color: 'var(--primary)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>📌</span>
                  <span>परीक्षेचा लॉक कसा काढायचा (Action Steps to Unlock):</span>
                </div>
                <div>
                  १. पालकांनी त्यांच्या मोबाईलवरून <strong>पालक पोर्टल (Parent Portal)</strong> मध्ये लॉगिन करावे.<br/>
                  २. डॅशबोर्डवरील <strong>गैरहजर परीक्षा पुनरावलोकन (Absent Exam Review)</strong> पर्यायावर क्लिक करावे.<br/>
                  ३. मागील परीक्षा न देण्याचे कारण नोंदवून सबमिट करावे. पालकांनी नोंद पूर्ण करताच परीक्षा लगेच सुरू होईल.
                </div>
              </div>
            )}
          </div>

          <button 
            className="btn btn-primary" 
            onClick={() => router.push(user?.role === 'admin' ? '/admin/exams' : '/student')} 
            style={{ padding: '12px 24px', borderRadius: '8px', fontWeight: 700, marginTop: '8px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2px' }}
          >
            <span>{user?.role === 'admin' ? '← Back to Exam Management' : '🏠 Return to Dashboard & Complete Actions'}</span>
            {user?.role !== 'admin' && (
              <span style={{ fontSize: '12px', fontWeight: 500, opacity: 0.9 }}>डॅशबोर्डवर परत जा आणि कृती पूर्ण करा</span>
            )}
          </button>
        </div>
      </div>
    );
  }

  if (!exam.questions || exam.questions.length === 0) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '500px', textAlign: 'center' }}>
          This exam contains no questions or is not configured yet. Please contact your administrator.
        </div>
        <button className="btn btn-primary" onClick={() => router.push(user?.role === 'admin' ? '/admin/exams' : '/student')} style={{ marginTop: '20px' }}>
          {user?.role === 'admin' ? '← Back to Exam Management' : 'Go Back'}
        </button>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh' }}>
      {/* Admin Simulator Mode Banner (SSOT unification) */}
      {isPreviewMode && (
        <div style={{
          background: 'linear-gradient(90deg, rgba(234, 179, 8, 0.15), rgba(59, 130, 246, 0.15))',
          borderBottom: '1px solid rgba(234, 179, 8, 0.35)',
          padding: '8px 16px',
          textAlign: 'center',
          fontSize: '12px',
          fontWeight: 700,
          color: '#fbbf24',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '10px'
        }}>
          <span>🛠️ Admin Simulator Mode</span>
          <span>•</span>
          <span>Running Unified Student Exam Engine</span>
          <span>•</span>
          <button 
            type="button"
            onClick={() => router.push('/admin/exams')}
            style={{
              background: 'transparent',
              border: '1px solid rgba(251, 191, 36, 0.5)',
              color: '#fbbf24',
              borderRadius: '4px',
              padding: '2px 8px',
              fontSize: '11px',
              cursor: 'pointer'
            }}
          >
            ← Exit Simulator
          </button>
        </div>
      )}

      {/* Floating Alert Banner for active proctoring violations */}
      {activeViolationWarning && (
        <div style={{
          position: 'fixed',
          top: '20px',
          left: '50%',
          transform: 'translateX(-50%)',
          background: 'var(--warning)',
          color: 'white',
          padding: '12px 24px',
          borderRadius: '8px',
          fontWeight: 'bold',
          boxShadow: '0 4px 15px rgba(0,0,0,0.3)',
          zIndex: 99999,
          fontSize: '14px',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          {activeViolationWarning}
        </div>
      )}

      {/* Interruption Lockout & Resume Modal (Phone call / tab switch recovery SSOT) */}
      <InterruptionLockoutModal
        isOpen={(isInterrupted || tabViolations >= 3) && !cameraModalOpen}
        tabViolations={tabViolations}
        maxViolations={3}
        durationSeconds={45}
        isSubmitting={examSubmitted}
        onManualResume={() => {
          try {
            window.focus();
          } catch {}
          try {
            if (!document.fullscreenElement && document.documentElement.requestFullscreen) {
              document.documentElement.requestFullscreen().catch(() => {});
            }
          } catch {}
          resumeExam();
        }}
        onTimeoutAutoSubmit={() => {
          if (!examSubmitted) {
            setAutoSubmittedReason('Auto-submitted due to unresumed exam window departure (3/3).');
            submitExamAction(tabViolations, true);
          }
        }}
      />
      {/* Script Injections for MediaPipe (Idempotent lazy loading) */}
      <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
      <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />


      {cameraModalOpen && (
        <div className="camera-modal" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'flex-start', justifyContent: 'center', padding: '40px 20px', overflowY: 'auto' }}>
          <div className="camera-modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius)', padding: '30px', maxWidth: '500px', width: '90%', textAlign: 'center', boxShadow: 'var(--shadow-lg)', margin: '0 auto' }}>
            {diagnosticRunning ? (
              <div style={{ padding: '20px 0' }}>
                <div className="spinner" style={{ border: '3px solid rgba(255, 255, 255, 0.1)', borderTop: '3px solid var(--accent)', borderRadius: '50%', width: '40px', height: '40px', margin: '0 auto 16px', animation: 'spin 1s linear infinite' }} />
                <style dangerouslySetInnerHTML={{__html: `
                  @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                `}} />
                <h3 style={{ fontSize: '15px', fontWeight: 700 }}>Initializing proctoring safeguards...</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '12px', marginTop: '6px' }}>Releasing previous device locks to prevent conflicts.</p>
              </div>
            ) : (
              <>
                {/* Exam Blueprint Card (SSOT Transparency) */}
                {exam && (
                  <div style={{
                    background: 'var(--surface)',
                    border: '1px solid var(--border-light)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '12px 14px',
                    marginBottom: '16px',
                    textAlign: 'left',
                    boxShadow: 'var(--shadow-sm)'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
                      <span style={{ fontSize: '13px', fontWeight: 800, color: 'var(--text)' }}>
                        📝 {exam.name}
                      </span>
                      <span style={{
                        fontSize: '9.5px',
                        fontWeight: 700,
                        textTransform: 'uppercase',
                        padding: '2px 6px',
                        borderRadius: '4px',
                        background: 'var(--info-bg)',
                        color: 'var(--info)',
                        border: '1px solid rgba(56, 189, 248, 0.3)'
                      }}>
                        Exam Blueprint
                      </span>
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                      <span><strong>{exam.questions?.length || 0}</strong> Questions</span>
                      <span>•</span>
                      <span><strong>{exam.duration || 30}</strong> Mins</span>
                      <span>•</span>
                      <span><strong>{exam.totalMarks || (Array.isArray(exam.questions) ? exam.questions.reduce((sum: number, q: any) => sum + (q?.marks || 4), 0) : 0)}</strong> Total Marks</span>
                      {exam.subject && (
                        <>
                          <span>•</span>
                          <span><strong>{exam.subject}</strong></span>
                        </>
                      )}
                    </div>
                  </div>
                )}
                <h2>Pre-Exam Hardware Diagnostic</h2>
                <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '10px 0 16px' }}>Verify your camera and microphone are functioning before entering the proctored workspace.</p>

            <div style={{ 
              background: 'var(--danger-bg)', 
              border: '1px dashed var(--danger-border)', 
              borderRadius: 'var(--radius-sm)', 
              padding: '12px 16px', 
              marginBottom: '16px', 
              textAlign: 'left' 
            }}>
              <strong style={{ fontSize: '12px', color: 'var(--danger)', display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
                ⚠️ Proctored Exam Rules & Violation Limits
              </strong>
              <ul style={{ margin: 0, paddingLeft: '16px', fontSize: '11px', color: 'var(--text-muted)', display: 'flex', flexDirection: 'column', gap: '4px', lineHeight: '1.4' }}>
                <li><strong>Tab Switching:</strong> Max 2 focus-loss warnings allowed. Exceeding this (3rd switch) will auto-submit your exam.</li>
                <li><strong>Face & Gaze Tracking:</strong> Enabled for integrity logging (no auto-submission).</li>
              </ul>
            </div>
            
            <div className="camera-preview" style={{ width: '100%', height: '240px', background: 'var(--bg-card)', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative' }}>
              {cameraStream ? (
                <video 
                  ref={(el) => {
                    if (el && el.srcObject !== cameraStream) {
                      el.srcObject = cameraStream;
                      try {
                        const playPromise = el.play();
                        if (playPromise !== undefined) {
                          playPromise.catch(() => {});
                        }
                      } catch {}
                    }
                  }}
                  autoPlay
                  playsInline
                  muted
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              ) : (
                <div style={{ color: 'var(--text-muted)' }}>Webcam Feed Offline</div>
              )}
            </div>

            {cameraStream && (
              <div style={{ margin: '20px 0 10px', textAlign: 'left' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                  <span>🎙️ Mic Activity Level</span>
                  <strong>{audioLevel > 0 ? `${audioLevel}%` : 'Silent / No Input'}</strong>
                </div>
                <div style={{ height: '8px', background: 'var(--bg-soft)', borderRadius: '4px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', background: 'var(--success)', width: `${audioLevel}%`, transition: 'width 0.1s ease' }}></div>
                </div>
              </div>
            )}

            {cameraStatus && <div className="status-msg" style={{ display: 'block', margin: '15px 0', fontSize: '12px', color: 'var(--text-muted)' }}>{cameraStatus}</div>}
            
            {!cameraStream ? (
              <button 
                className="btn btn-primary" 
                onClick={handleRunCheck} 
                style={{ marginTop: '15px', width: '100%' }}
                disabled={permissionBlocked && micAttemptsRemaining === 0}
              >
                {permissionBlocked ? '❌ Hardware Blocked (Retry)' : 'Test Camera & Microphone'}
              </button>
            ) : (
              <button 
                className="btn btn-success" 
                onClick={handleProceedToExam} 
                disabled={isStartingExam}
                style={{ marginTop: '15px', width: '100%' }}
              >
                {isStartingExam ? 'Starting Exam...' : 'Start Exam / Proceed'}
              </button>
            )}

            {isPreviewMode && (
              <button 
                type="button"
                className="btn btn-secondary" 
                onClick={() => setCameraModalOpen(false)}
                style={{ 
                  marginTop: '10px', 
                  width: '100%', 
                  border: '1px dashed var(--accent)', 
                  color: 'var(--accent)', 
                  fontWeight: 700,
                  fontSize: '12px'
                }}
              >
                ⚡ Admin Simulator: Bypass Hardware Diagnostic & Enter Exam
              </button>
            )}
              </>
            )}
          </div>
        </div>
      )}

      {/* Proctoring Bar */}
      <div style={{
        display: cameraModalOpen ? 'none' : 'block',
        background: 'rgba(30, 34, 49, 0.95)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '12px',
        padding: '8px 12px',
        margin: '10px auto',
        maxWidth: '960px',
        width: '95%',
        boxShadow: '0 4px 16px rgba(0, 0, 0, 0.2)'
      }}>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          gap: '8px',
          flexWrap: 'nowrap'
        }}>
          {/* Left side camera section */}
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexShrink: 0 }}>
            <div style={{
              position: 'relative',
              width: '64px',
              height: '48px',
              borderRadius: '6px',
              overflow: 'hidden',
              border: `2px solid ${faceStatusClass === 'success' ? 'var(--success)' : 'var(--warning)'}`,
              boxShadow: '0 2px 6px rgba(0,0,0,0.5)'
            }}>
              <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', height: '100%', objectFit: 'cover' }}></video>
            </div>
            <div style={{
              padding: '2px 4px',
              borderRadius: '4px',
              background: faceStatusClass === 'success' ? 'var(--success-bg)' : 'var(--warning-bg)',
              border: `1px solid ${faceStatusClass === 'success' ? 'var(--success)' : 'var(--warning)'}`,
              color: faceStatusClass === 'success' ? 'var(--success)' : 'var(--warning)',
              fontSize: '9px',
              fontWeight: 'bold',
              textAlign: 'center',
              maxWidth: '75px',
              whiteSpace: 'nowrap',
              overflow: 'hidden',
              textOverflow: 'ellipsis'
            }}>
              {(faceStatus || '').replace(' Detected', '').replace(' Verified', '')}
            </div>
          </div>

          {/* Right side stats inline flow */}
          <div style={{
            display: 'flex',
            gap: '6px',
            flex: 1,
            justifyContent: 'flex-end',
            alignItems: 'center',
            flexWrap: 'nowrap',
            overflowX: 'auto'
          }}>
            {/* Tab */}
            <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '45px' }}>
              <span style={{ fontSize: '9px', color: 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>Tab</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'white' }}>{tabViolations}/3</span>
            </div>
            {/* No Face */}
            <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '45px' }}>
              <span style={{ fontSize: '9px', color: 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>NoFace</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations?.noFace ?? 0}</span>
            </div>
            {/* Multiple */}
            <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '45px' }}>
              <span style={{ fontSize: '9px', color: 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>Multi</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations?.multipleFaces ?? 0}</span>
            </div>
            {/* Timer */}
            <div style={{ background: timeRemaining <= 120 ? 'rgba(239, 68, 68, 0.15)' : 'rgba(255,255,255,0.03)', border: `1px solid ${timeRemaining <= 120 ? 'var(--danger)' : 'rgba(255,255,255,0.05)'}`, borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '60px' }}>
              <span style={{ fontSize: '9px', color: timeRemaining <= 120 ? 'var(--danger)' : 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>Time</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: timeRemaining <= 120 ? 'var(--danger)' : 'white' }}>{formattedTime}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Page Layout */}
      {!cameraModalOpen && (
        <div className="main-content" style={{ maxWidth: '960px', margin: '0 auto', padding: '12px 8px', userSelect: 'none', WebkitUserSelect: 'none' }}>
          {/* Header */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '16px', marginBottom: '12px' }}>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: '13px', margin: 0, fontWeight: 700, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: 'var(--text)' }} title={exam.name}>{exam.name}</div>
              <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: '2px 0 0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{exam.chapter}{exam.topicName ? ` > ${exam.topicName}` : ''}</p>
            </div>
          </div>

          {/* Question Navigator */}
          <div className="question-nav" style={{ display: 'flex', gap: '6px', overflowX: 'auto', padding: '8px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)', marginBottom: '12px' }}>
            {(exam.questions || []).map((_, idx) => {
              const answered = (userAnswers[idx]?.answer || '') !== '';
              const isCurrent = idx === currentQIndex;
              return (
                <div 
                  key={idx} 
                  className={`nav-q ${isCurrent ? 'current' : answered ? 'answered' : 'unanswered'}`}
                  onClick={() => setCurrentQIndex(idx)}
                  style={{ width: '36px', height: '36px', display: 'flex', alignItems: 'center', justifyContent: 'center', borderRadius: 'var(--radius-sm)', cursor: 'pointer', fontWeight: 'bold', fontSize: '13px', flexShrink: 0 }}
                >
                  {idx + 1}
                </div>
              );
            })}
          </div>

          {/* Question Card */}
          <div ref={questionContainerRef} key={currentQuestion?.id || safeQIndex} className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', padding: '16px', marginBottom: '12px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '12px', color: 'var(--text-muted)', fontSize: '12px' }}>
              <span>Question {safeQIndex + 1} of {exam.questions?.length || 0}</span>
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                <span className="badge">{currentQuestion?.marks || 1} Marks</span>
              </div>
            </div>


            <QuestionDisplay
              mode="exam"
              question={currentQuestion}
              userAnswer={currentAnswer}
              onSelectOption={handleSelectOptionCurrent}
              onTextInput={handleTextInputCurrent}
            />
          </div>

          {/* Navigation Buttons */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => setCurrentQIndex(prev => Math.max(0, prev - 1))}
              disabled={currentQIndex === 0}
            >
              ← Previous
            </button>
            
            {currentQIndex === (exam.questions?.length || 1) - 1 ? (
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '6px' }}>
                <button 
                  className="btn btn-danger" 
                  disabled={isSubmitting || submitCooldown > 0}
                  onClick={() => submitExamAction()}
                  style={{ 
                    opacity: (isSubmitting || submitCooldown > 0) ? 0.6 : 1,
                    cursor: (isSubmitting || submitCooldown > 0) ? 'not-allowed' : 'pointer',
                    minWidth: '160px',
                    fontWeight: 700
                  }}
                >
                  {submitCooldown > 0 
                    ? `⏳ Retry in ${submitCooldown}s (Saved)` 
                    : (isSubmitting ? 'Submitting...' : '📋 Submit Exam')
                  }
                </button>
                {submitErrorMessage && (
                  <div style={{ fontSize: '11px', color: 'var(--danger)', maxWidth: '300px', textAlign: 'right', fontWeight: 600 }}>
                    {submitErrorMessage}
                  </div>
                )}
              </div>
            ) : (
              <button 
                className="btn btn-primary" 
                onClick={() => setCurrentQIndex(prev => Math.min((exam.questions?.length || 1) - 1, prev + 1))}
              >
                Next →
              </button>
            )}
          </div>
        </div>
      )}

      {/* 1. Time Expired Non-Blocking Overlay (Locks questions, submits automatically) */}
      {timeRemaining <= 0 && !examSubmitted && !loading && !cameraModalOpen && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(15, 23, 42, 0.88)',
          backdropFilter: 'blur(5px)',
          WebkitBackdropFilter: 'blur(5px)',
          zIndex: 29000,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          padding: '24px',
          textAlign: 'center'
        }}>
          <div style={{ fontSize: '48px', marginBottom: '14px' }}>⏰</div>
          <h2 style={{ fontSize: '22px', fontWeight: 800, margin: '0 0 8px 0' }}>Exam Duration Has Ended</h2>
          <p style={{ fontSize: '14px', color: '#94a3b8', maxWidth: '420px', margin: '0 0 20px 0', lineHeight: 1.5 }}>
            Time is up. Questions are strictly locked. Your answers are being submitted to the server.
          </p>

          {isSubmitting ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '14px', fontWeight: 600 }}>
              <div className="spinner" style={{ width: '22px', height: '22px' }}></div>
              <span>Finalizing and submitting your answers...</span>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', alignItems: 'center' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => submitExamAction()}
                style={{ fontWeight: 700, padding: '10px 24px', fontSize: '15px' }}
              >
                Submit Answers Now
              </button>
              {submissionRescueOpen && (
                <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', justifyContent: 'center' }}>
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={handleCopyEmergencyToken}
                    style={{ fontSize: '12px', padding: '6px 14px' }}
                  >
                    {tokenCopied ? '✅ Backup Code Copied!' : '📋 Copy Emergency Code'}
                  </button>
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={handleDownloadBackup}
                    style={{ fontSize: '12px', padding: '6px 14px' }}
                  >
                    💾 Download Backup
                  </button>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* 2. Submission Rescue Modal (Prominent fallback if network drops) */}
      {submissionRescueOpen && !examSubmitted && timeRemaining > 0 && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.65)', backdropFilter: 'blur(4px)', zIndex: 28000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover, #1e293b)', border: '1px solid var(--border-popover, #334155)', borderRadius: '12px', maxWidth: '500px', width: '100%', padding: '24px', color: 'var(--text)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '14px' }}>
              <span style={{ fontSize: '26px' }}>⚠️</span>
              <div>
                <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800 }}>Submission Network Hiccup</h3>
                <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Don't panic! Your answers are 100% saved on this device.</span>
              </div>
            </div>

            <div style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: '8px', padding: '10px 14px', color: '#ef4444', fontSize: '12.5px', fontWeight: 600, marginBottom: '16px' }}>
              {submitErrorMessage || 'Failed to connect to the examination server.'}
            </div>

            <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '20px', lineHeight: 1.5 }}>
              Your network may have momentarily disconnected. You can retry immediately, or copy/download your answers token to verify with your teacher.
            </p>

            <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', justifyContent: 'flex-end' }}>
              <button 
                className="btn btn-secondary btn-sm" 
                onClick={handleCopyEmergencyToken}
                style={{ fontWeight: 600 }}
              >
                {tokenCopied ? '✅ Copied to Clipboard!' : '📋 Copy Emergency Token'}
              </button>
              <button 
                className="btn btn-secondary btn-sm" 
                onClick={handleDownloadBackup}
                style={{ fontWeight: 600 }}
              >
                💾 Save Answers File
              </button>
              <button 
                className="btn btn-primary btn-sm" 
                onClick={() => submitExamAction()}
                disabled={isSubmitting}
                style={{ fontWeight: 700 }}
              >
                {isSubmitting ? 'Submitting...' : '🔄 Retry Submission'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Blocking overlays (submitting state) */}
      {blockingMessage && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 30000, color: 'white' }}>
          <div className="spinner"></div>
          <p style={{ marginTop: '20px', fontSize: '16px', fontWeight: 'bold' }}>{blockingMessage}</p>
        </div>
      )}
      {/* Standardized Review Scorecard Modal for incorrect and unattempted questions */}
      {reviewModalOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 25000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '800px', width: '100%', height: 'fit-content', maxHeight: '90vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--text)' }}>
                📝 Question Review &amp; Understanding Check
              </h4>
            </div>

            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {autoSubmittedReason && (
                <div style={{ background: 'var(--danger-bg)', border: '1px solid var(--danger-border)', borderRadius: '8px', padding: '12px', color: 'var(--danger)', fontSize: '13px', fontWeight: 600, marginBottom: '20px' }}>
                  🚨 {autoSubmittedReason}
                </div>
              )}
              {/* Compact Horizontal Summary Bar */}
              <div style={{ 
                background: 'var(--bg-soft)', 
                padding: '12px 16px', 
                borderRadius: 'var(--radius)', 
                display: 'flex', 
                flexDirection: 'row', 
                flexWrap: 'wrap', 
                gap: '12px 20px', 
                marginBottom: '20px',
                border: '1px solid var(--border-light)',
                color: 'var(--text)'
              }}>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Exam Title:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{exam?.name || examId}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Time Spent:</strong>{' '}
                  {(() => {
                    const spent = exam ? (((exam.duration || 0) * 60) - timeRemaining) : 0;
                    return (
                      <span style={{ fontWeight: 600 }}>{Math.floor(spent / 60)} min {spent % 60} sec</span>
                    );
                  })()}
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Score:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{reviewScores?.score} / {reviewScores?.totalMarks} ({reviewScores?.percentage}%)</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Tab Out:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{tabViolations} times</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Gaze Away:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{proctoringViolations.lookingAway || 0} times</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.4' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>No Face:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{proctoringViolations.noFace || 0} times</span>
                </div>
              </div>

              {/* Filter Tabs Bar (Correct tab is disabled) */}
              <div className="outcome-tabs" style={{ display: 'flex', gap: '8px', marginBottom: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
                <button 
                  onClick={() => setQuestionFilterTab('all')} 
                  style={{
                    padding: '6px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                    color: questionFilterTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  All ({wrongAnswers.length + unattemptedQuestions.length})
                </button>
                <button 
                  disabled
                  style={{
                    padding: '6px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: '1px dashed var(--border-light)',
                    background: 'transparent',
                    color: 'var(--text-faint)',
                    cursor: 'not-allowed',
                    opacity: 0.4
                  }}
                >
                  Correct (0)
                </button>
                <button 
                  onClick={() => setQuestionFilterTab('incorrect')} 
                  style={{
                    padding: '6px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'incorrect' ? 'var(--danger-bg)' : 'transparent',
                    color: questionFilterTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Incorrect ({wrongAnswers.length})
                </button>
                <button 
                  onClick={() => setQuestionFilterTab('unanswered')} 
                  style={{
                    padding: '6px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'unanswered' ? '1px solid var(--text-muted)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'unanswered' ? 'var(--bg-soft)' : 'transparent',
                    color: 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Unanswered ({unattemptedQuestions.length})
                </button>
              </div>

              {/* Question Cards list */}
              <h5 style={{ fontSize: '13px', fontWeight: 'bold', marginBottom: '12px', paddingBottom: '4px', color: 'var(--text)' }}>
                🔍 Self-Reflection Items
              </h5>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                {filteredQuestionsToReview.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-faint)', fontSize: '12px' }}>📭 No questions match this filter.</div>
                ) : (
                  filteredQuestionsToReview.map((qItem) => {
                    const isUnanswered = qItem.type === 'unanswered';
                    const isUnderstood = reviewedQuestions.has(qItem.globalIdx);
                    const matchingQ = exam?.questions?.find((x: any) => x.text === qItem.questionText);
                    const explanation = matchingQ?.solution || qItem.explanation || '';
                    const currentReason = selectedReasons[qItem.globalIdx];

                    return (
                       <div 
                         key={qItem.globalIdx}
                         style={{
                           padding: '16px',
                           borderRadius: 'var(--radius)',
                           border: '1px solid var(--review-card-border)',
                           background: 'var(--review-card-bg)',
                           display: 'flex',
                           flexDirection: 'column',
                           gap: '8px'
                         }}
                       >
                         <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', fontSize: '11px', color: 'var(--text-muted)' }}>
                           <div style={{ display: 'flex', alignItems: 'center' }}>
                             <span>Question {(() => {
                                 if (qItem.qIndex !== undefined) return qItem.qIndex + 1;
                                 const actualIdx = exam?.questions && matchingQ
                                   ? exam.questions.findIndex((x: any) => x.text === matchingQ.text)
                                   : -1;
                                 return actualIdx !== -1 ? actualIdx + 1 : qItem.globalIdx + 1;
                               })()} ({matchingQ?.difficulty?.toUpperCase() || 'MEDIUM'} • {matchingQ?.bloomLevel || 'Understand'})</span>
                             {currentReason && (
                               <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', border: '1px solid rgba(251, 191, 36, 0.25)', padding: '2px 6px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold', marginLeft: '8px' }}>
                                 ⚠️ Reason: {currentReason}
                               </span>
                             )}
                           </div>
                           <span style={{ 
                             fontWeight: 'bold', 
                             fontSize: '10px',
                             padding: '2px 8px',
                             borderRadius: '12px',
                             background: isUnanswered ? 'rgba(255,255,255,0.1)' : 'var(--danger-bg)',
                             color: isUnanswered ? 'var(--text-muted)' : 'var(--danger)' 
                           }}>
                             {isUnanswered ? 'Unattempted' : 'Incorrect'}
                           </span>
                         </div>

                        {/* Question Details via SSOT QuestionDisplay */}
                        <QuestionDisplay
                          mode="review"
                          question={{
                            text: qItem.questionText,
                            type: matchingQ?.type,
                            options: matchingQ?.options,
                            correctAnswer: getQuestionCorrectAnswer(matchingQ) || qItem.correctAnswer,
                            userAnswer: isUnanswered ? '' : qItem.userAnswer,
                            solution: explanation,
                            isCorrect: false
                          }}
                          isCorrect={false}
                          userAnswer={isUnanswered ? '' : (getOptionText(matchingQ || qItem.questionText, qItem.userAnswer || '', exam?.questions) || qItem.userAnswer)}
                          correctAnswer={getOptionText(matchingQ || qItem.questionText, qItem.correctAnswer, exam?.questions) || qItem.correctAnswer}
                          explanation={explanation}
                        />

                        {/* Error classification box (exactly two lines of buttons in a nice box) */}
                        <div style={{ 
                          marginTop: '10px', 
                          marginBottom: '10px', 
                          border: '1px solid var(--border-light)', 
                          borderRadius: 'var(--radius-sm)', 
                          padding: '12px', 
                          background: 'var(--bg-soft)' 
                        }}>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: 'var(--text)' }}>
                            Identify error reason:
                          </span>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                            {/* Line 1 */}
                            <div style={{ display: 'flex', gap: '6px' }}>
                              {['Reading Errors', 'Time Management', 'Over-Thinking'].map(reason => {
                                const isSelected = selectedReasons[qItem.globalIdx] === reason;
                                return (
                                  <button
                                    key={reason}
                                    type="button"
                                    onClick={() => {
                                      if (!isUnderstood) {
                                        setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }));
                                      }
                                    }}
                                    disabled={isUnderstood}
                                    className={`btn btn-sm ${isSelected ? 'btn-primary' : 'btn-secondary'}`}
                                    style={{ 
                                      fontSize: '10px', 
                                      padding: '5px 10px',
                                      flex: 1,
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border)',
                                      background: isSelected ? 'var(--accent-grad)' : 'var(--surface)',
                                      color: isSelected ? 'var(--text-white)' : 'var(--text)',
                                      cursor: isUnderstood ? 'not-allowed' : 'pointer',
                                      whiteSpace: 'nowrap'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                            {/* Line 2 */}
                            <div style={{ display: 'flex', gap: '6px' }}>
                              {['Silly Mistake', 'Concept'].map(reason => {
                                const isSelected = selectedReasons[qItem.globalIdx] === reason;
                                return (
                                  <button
                                    key={reason}
                                    type="button"
                                    onClick={() => {
                                      if (!isUnderstood) {
                                        setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }));
                                      }
                                    }}
                                    disabled={isUnderstood}
                                    className={`btn btn-sm ${isSelected ? 'btn-primary' : 'btn-secondary'}`}
                                    style={{ 
                                      fontSize: '10px', 
                                      padding: '5px 10px',
                                      flex: 1,
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border)',
                                      background: isSelected ? 'var(--accent-grad)' : 'var(--surface)',
                                      color: isSelected ? 'var(--text-white)' : 'var(--text)',
                                      cursor: isUnderstood ? 'not-allowed' : 'pointer',
                                      whiteSpace: 'nowrap'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                          </div>
                        </div>

                        <button 
                          className={`btn btn-sm ${isUnderstood ? 'btn-success' : 'btn-primary'}`}
                          disabled={isUnderstood}
                          onClick={() => {
                            if (!selectedReasons[qItem.globalIdx]) {
                              setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: 'Concept' }));
                            }
                            setReviewedQuestions(prev => {
                              const next = new Set(prev);
                              next.add(qItem.globalIdx);
                              return next;
                            });
                          }}
                          style={{ fontSize: '11px', padding: '6px 16px', alignSelf: 'flex-start', marginTop: '10px' }}
                        >
                          {isUnderstood ? '✓ Understood' : '🔘 I Understand'}
                        </button>
                      </div>
                    );
                  })
                )}
              </div>
            </div>

            {/* Review bottom status bar */}
            {(() => {
              const totalToReview = wrongAnswers.length + unattemptedQuestions.length;
              const reviewedCount = reviewedQuestions.size;
              const isAllReviewed = reviewedCount === totalToReview;
              return (
                <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px', background: 'var(--surface)' }}>
                  <div style={{ 
                    padding: '10px', 
                    fontSize: '13px', 
                    textAlign: 'center', 
                    borderRadius: 'var(--radius-sm)',
                    background: isAllReviewed ? 'var(--success-bg)' : 'var(--warning-bg)',
                    color: isAllReviewed ? 'var(--success)' : 'var(--warning)',
                    border: isAllReviewed ? '1px solid var(--success)' : '1px solid var(--warning)',
                    fontWeight: 'bold'
                  }}>
                    {isAllReviewed 
                      ? '✅ Excellent! You have reviewed all questions. You can now submit.' 
                      : `Reviewed: ${reviewedCount}/${totalToReview} completed. Click "I Understand" for each question above.`
                    }
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
                    {reviewSecondsRemaining > 0 && (
                      <span style={{ fontSize: '11px', color: 'var(--warning)', fontWeight: 700, padding: '4px 8px', background: 'var(--warning-bg)', borderRadius: '4px', border: '1px solid var(--warning-border)' }}>
                        ⏳ Please carefully review solutions ({reviewSecondsRemaining}s remaining)
                      </span>
                    )}
                    <button 
                      className="btn btn-primary" 
                      disabled={!isAllReviewed || reviewSecondsRemaining > 0 || reviewSubmitting} 
                      onClick={async () => {
                        setReviewSubmitting(true);
                        try {
                          const finalReasons: Record<string, string> = { ...selectedReasons };
                          questionsToReview.forEach(q => {
                            if (!finalReasons[q.globalIdx]) {
                              finalReasons[q.globalIdx] = 'Concept';
                            }
                          });

                          const idToken = await firebaseUser!.getIdToken();
                          const res = await fetch('/api/student/exams', {
                            method: 'PUT',
                            headers: {
                              'Content-Type': 'application/json',
                              'Authorization': `Bearer ${idToken}`
                            },
                            body: JSON.stringify({ 
                              examId,
                              wrongAnswerReasons: finalReasons
                            })
                          });
                          if (!res.ok) {
                            const errData = await res.json().catch(() => null);
                            throw new Error(errData?.message || 'Failed to update submission status');
                          }
                          
                          setReviewModalOpen(false);
                          setShowResultModal(true);
                        } catch (err: any) {
                          alert(`Error completing review: ${err.message}`);
                        } finally {
                          setReviewSubmitting(false);
                        }
                      }}
                      style={{ padding: '10px 24px' }}
                    >
                      {reviewSubmitting 
                        ? 'Submitting...' 
                        : reviewSecondsRemaining > 0
                          ? `⏳ Reading & Reflection (${reviewSecondsRemaining}s)`
                          : '🚀 Final Submit to Parents'
                      }
                    </button>
                  </div>
                </div>
              );
            })()}
          </div>
        </div>
      )}

      {/* Score Reveal Modal */}
      {showResultModal && reviewScores && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 25000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '100%', padding: '30px', border: '1px solid var(--border-popover)', textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '20px', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ fontSize: '50px' }}>🎉</div>
            <h2 style={{ fontSize: '20px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>Exam Completed!</h2>
            {autoSubmittedReason && (
              <div style={{ background: 'var(--danger-bg)', border: '1px solid var(--danger-border)', borderRadius: '8px', padding: '12px', color: 'var(--danger)', fontSize: '13px', fontWeight: 600, margin: '5px 0' }}>
                🚨 {autoSubmittedReason}
              </div>
            )}
            
            <div style={{ background: 'var(--bg-soft)', padding: '20px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Exam Title: <strong>{exam?.name || examId}</strong></div>
              <div style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--accent)', marginTop: '5px' }}>
                {reviewScores.score} / {reviewScores.totalMarks}
              </div>
              <div style={{ fontSize: '15px', fontWeight: 600, color: 'var(--text)' }}>
                Percentage: {reviewScores.percentage}%
              </div>
            </div>

            <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
              Your submission has been saved. It is currently waiting for your parent's review.
            </p>

            <button className="btn btn-primary" onClick={() => router.push(user?.role === 'admin' ? '/admin/exams' : '/student')} style={{ width: '100%', padding: '12px', fontSize: '14px', fontWeight: 'bold', marginTop: '10px' }}>
              {user?.role === 'admin' ? '← Back to Exam Management' : 'Go to Student Dashboard'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function TakeExamPageInner() {
  const searchParams = useSearchParams();
  const examId = searchParams.get('id') || searchParams.get('examId') || undefined;

  return (
    <ExamErrorBoundary
      fallbackTitle="Objective Exam Workspace Recovery"
      examId={examId}
      onReset={() => {
        try {
          if (typeof window !== 'undefined' && window.localStorage) {
            const keysToRemove: string[] = [];
            for (let i = 0; i < localStorage.length; i++) {
              const k = localStorage.key(i);
              if (k && k.startsWith('exam_state_')) {
                keysToRemove.push(k);
              }
            }
            keysToRemove.forEach(k => localStorage.removeItem(k));
          }
        } catch {}
      }}
    >
      <TakeExamContent />
    </ExamErrorBoundary>
  );
}

export default function TakeExamPage() {
  return (
    <React.Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading exam...
        </div>
      </div>
    }>
      <TakeExamPageInner />
    </React.Suspense>
  );
}
