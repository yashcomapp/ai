'use client';

import React, { useEffect, useRef, useState, useCallback, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { stripOptionLabel, preprocessMathText, parseAnswerList, isOptionSelectedByUser, getRawOptionKey, getRawOptionText, extractAssertionAndReason } from '@/lib/questionTypes';
import { useMathRender } from '@/hooks/useMathRender';
import { db } from '@/lib/firebase/firestore';
import { useExamTimer } from '@/hooks/useExamTimer';
import { useLiveExam } from '@/hooks/useLiveExam';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';

const RTC_CONFIG = {
  iceServers: [
    { urls: 'stun:stun.l.google.com:19302' },
    {
      urls: 'turn:openrelay.metered.ca:80',
      username: 'openrelayproject',
      credential: 'openrelayproject'
    },
    {
      urls: 'turn:openrelay.metered.ca:443',
      username: 'openrelayproject',
      credential: 'openrelayproject'
    }
  ]
};

// Extend window interface for CDN scripts
declare global {
  interface Window {
    FaceMesh: any;
    Camera: any;
    renderMathInElement: any;
  }
}

interface Question {
  id?: string;
  type: string;
  text: string;
  options?: any[];
  qNumber?: number;
  marks?: number;
  subject?: string;
  chapter?: string;
  topic?: string;
  class?: string;
  board?: string;
  questionCode?: string;
  solution?: string;
  difficulty?: string;
  bloomLevel?: string;
  assertion?: string;
  reason?: string;
  correctAnswer?: any;
  correctAnswers?: any;
}

interface Exam {
  id: string;
  name: string;
  duration: number;
  negativeMarks: number;
  totalMarks: number;
  subject?: string;
  chapter?: string;
  topicName?: string;
  questions: Question[];
}

function TakeExamContent() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();
  const examId = searchParams.get('examId') || searchParams.get('id');

  const [exam, setExam] = useState<Exam | null>(null);
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

  useEffect(() => {
    if (!cameraModalOpen && !startTimeRef.current) {
      startTimeRef.current = Date.now();
    }
  }, [cameraModalOpen]);
  const [reviewModalOpen, setReviewModalOpen] = useState(false);
  const [blockingMessage, setBlockingMessage] = useState('');
  const [wrongAnswers, setWrongAnswers] = useState<any[]>([]);
  const [unattemptedQuestions, setUnattemptedQuestions] = useState<any[]>([]);
  const [reviewedQuestions, setReviewedQuestions] = useState<Set<number>>(new Set());
  const [selectedReasons, setSelectedReasons] = useState<{[key: number]: string}>({});
  const [reviewScores, setReviewScores] = useState<{ score: number, totalMarks: number, percentage: number } | null>(null);
  const [reviewSubmitting, setReviewSubmitting] = useState(false);
  const [showResultModal, setShowResultModal] = useState(false);
  const [activeViolationWarning, setActiveViolationWarning] = useState<string | null>(null);
  const [questionFilterTab, setQuestionFilterTab] = useState<'all' | 'incorrect' | 'unanswered'>('all');
  const [autoSubmittedReason, setAutoSubmittedReason] = useState<string | null>(null);

  // Question Dispute & Bypass states
  const [disputedQuestionIds, setDisputedQuestionIds] = useState<Set<string>>(new Set());
  const [reportModalOpen, setReportModalOpen] = useState(false);
  const [reportReason, setReportReason] = useState('missing_options');
  const [reportNotes, setReportNotes] = useState('');
  const [isSubmittingReport, setIsSubmittingReport] = useState(false);

  const captureElementScreenshot = async (element: HTMLElement | null): Promise<string | null> => {
    if (!element) return null;
    try {
      const w = window as any;
      if (!w.html2canvas) {
        await new Promise<void>((resolve, reject) => {
          const s = document.createElement('script');
          s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
          s.onload = () => resolve();
          s.onerror = () => reject(new Error('Failed to load html2canvas.'));
          document.head.appendChild(s);
        });
      }
      const canvas = await w.html2canvas(element, { scale: 1.5, useCORS: true, backgroundColor: '#222730' });
      return canvas.toDataURL('image/jpeg', 0.7);
    } catch (err) {
      console.warn('Screenshot capture failed:', err);
      return null;
    }
  };

  const handleReportQuestion = async () => {
    if (!exam || !firebaseUser || isSubmittingReport) return;
    const currentQ = exam.questions[currentQIndex];
    if (!currentQ) return;

    setIsSubmittingReport(true);
    try {
      const screenshotData = await captureElementScreenshot(questionContainerRef.current);
      const idToken = await firebaseUser.getIdToken();

      const res = await fetch('/api/student/disputes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          questionId: currentQ.id,
          questionCode: currentQ.questionCode,
          topicCode: (currentQ as any).topicCode || '',
          source: 'exam',
          examId,
          reason: reportReason,
          notes: reportNotes,
          screenshotData,
          questionText: currentQ.text || (currentQ as any).assertion || ''
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit question report.');
      }

      const qKey = currentQ.id || currentQ.questionCode || String(currentQIndex);
      setDisputedQuestionIds(prev => new Set(prev).add(qKey));
      setReportModalOpen(false);
      setReportNotes('');
      alert('🚩 Question reported successfully! It has been excluded from your score with zero penalty.');

      // Advance to next question automatically if available
      if (currentQIndex < exam.questions.length - 1) {
        setCurrentQIndex(currentQIndex + 1);
      }
    } catch (err: any) {
      alert('Error reporting question: ' + (err.message || 'Unknown error'));
    } finally {
      setIsSubmittingReport(false);
    }
  };

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
    initialSeconds: exam ? (exam.duration * 60) : 0,
    isPaused: loading || examSubmitted || !exam || cameraModalOpen,
    onTimeUp: () => {
      alert('Time up! Submitting your exam automatically.');
      submitExamAction();
    },
    onTick: () => {
      setUserAnswers(answers => {
        const updated = [...answers];
        if (updated[currentQIndex]) {
          updated[currentQIndex] = {
            ...updated[currentQIndex],
            timeSpentSeconds: updated[currentQIndex].timeSpentSeconds + 1
          };
        }
        return updated;
      });
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

  const {
    tabViolations,
    setTabViolations,
    proctoringViolations,
    setProctoringViolations,
    cameraStatus,
    cameraStream,
    micBypassed,
    startCameraStream,
    stopCameraStream,
    cleanupProctoring
  } = useLiveExam({
    examId: examId || '',
    examName: exam?.name || 'Untitled Exam',
    studentCode: user?.studentCode || '',
    studentName: user?.name || user?.email || 'Student',
    examType: 'mcq',
    totalQuestions: exam?.questions.length || null,
    currentQuestionIndex: currentQIndex,
    answeredCount,
    cameraVideoRef: videoRef,
    autonomous: (user as any)?.autonomous || false,
    started: !cameraModalOpen && !examSubmitted
  });

  const activeQuestionForHeuristic = exam?.questions?.[currentQIndex];
  const isNumerical = useMemo(() => {
    if (!activeQuestionForHeuristic) return false;
    // Database explicit relaxProctoring or isNumerical overrides
    if ((activeQuestionForHeuristic as any).relaxProctoring === true || (activeQuestionForHeuristic as any).isNumerical === true) {
      return true;
    }
    const text = activeQuestionForHeuristic.text || '';
    const textLower = text.toLowerCase();
    
    // Detect KaTeX rendering blocks \(...\), \[...\], $...$, or LaTeX macros (\frac, \ce, \sqrt, \vec, \sum, etc.)
    const optionsText = Array.isArray(activeQuestionForHeuristic.options)
      ? activeQuestionForHeuristic.options.map((o: any) => typeof o === 'object' ? (o.text || '') : String(o)).join(' ')
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
    isFullscreen,
    isWindowFocused,
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
    lockdownWindowFocus: true,
    lockdownFullscreen: true,
    startCameraStream,
    stopCameraStream,
    cleanupLiveExam: cleanupProctoring,
    isNumerical: isNumerical,
    onViolation: (type) => {
      if (type === 'tab_switch') {
        setTabViolations(prev => prev + 1);
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



  const getOptionText = (questionText: string, ansInput: any) => {
    const list = parseAnswerList(ansInput);
    if (list.length === 0) return '(blank)';
    if (!exam || !exam.questions) return list.join(', ');
    const q = exam.questions.find((x: any) => x.text === questionText);
    if (!q || !q.options || !Array.isArray(q.options)) return list.join(', ');

    const opts: any[] = q.options;
    const matchedTexts: string[] = [];
    list.forEach(item => {
      let foundText = '';
      if (item.length === 1 && item.toUpperCase() >= 'A' && item.toUpperCase() <= 'Z') {
        const codeIndex = item.toUpperCase().charCodeAt(0) - 65;
        if (codeIndex >= 0 && codeIndex < opts.length) {
          const optVal = opts[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? (optVal.text || optVal.code || item) : String(optVal);
        }
      }
      if (!foundText && /^\d+$/.test(item)) {
        const codeIndex = parseInt(item, 10);
        if (codeIndex >= 0 && codeIndex < opts.length) {
          const optVal = opts[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? (optVal.text || optVal.code || item) : String(optVal);
        }
      }
      if (!foundText) {
        const opt = opts.find((o: any) => {
          if (o && typeof o === 'object') return o.code === item || o.text === item;
          return String(o) === item;
        });
        if (opt) {
          foundText = (opt && typeof opt === 'object') ? (opt.text || opt.code || item) : String(opt);
        }
      }
      matchedTexts.push(foundText || item);
    });

    return matchedTexts.join(', ');
  };

  // 1. Fetch exam configuration
  useEffect(() => {
    if (!examId || !firebaseUser) return;
    
    const fetchExam = async () => {
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch(`/api/student/exams?id=${examId}`, {
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
            const startAtMs = new Date(data.assignment.startAt).getTime();
            const lateLimitMs = startAtMs + (5 * 60 * 1000); // 5 minutes late limit
            if (Date.now() > lateLimitMs) {
              throw new Error('Late entry is not allowed. You cannot start the exam more than 5 minutes after the scheduled start time.');
            }
          }
        }

        setExam(data.exam);
        
        // Initialize userAnswers array
        const initialAnswers = data.exam.questions.map(() => ({ answer: '', timeSpentSeconds: 0 }));
        
        let initialTimeRemaining = data.exam.duration * 60;
        if (data.assignment && data.assignment.openMode === 'scheduled' && data.assignment.endAt) {
          const endAtMs = new Date(data.assignment.endAt).getTime();
          const secondsUntilEnd = Math.floor((endAtMs - Date.now()) / 1000);
          if (secondsUntilEnd <= 0) {
            throw new Error('The scheduled time for this exam has already ended.');
          }
          initialTimeRemaining = Math.min(initialTimeRemaining, secondsUntilEnd);
        }

        // Check autosave
        try {
          const saved = localStorage.getItem(getSaveKey());
          if (saved) {
            const parsed = JSON.parse(saved);
            if (parsed.examId === examId && Date.now() - parsed.timestamp < 3600000) {
              setUserAnswers(parsed.userAnswers || initialAnswers);
              setCurrentQIndex(parsed.currentQIndex || 0);
              
              let resumedTime = parsed.timeRemaining || (data.exam.duration * 60);
              if (data.assignment && data.assignment.openMode === 'scheduled' && data.assignment.endAt) {
                const endAtMs = new Date(data.assignment.endAt).getTime();
                const secondsUntilEnd = Math.floor((endAtMs - Date.now()) / 1000);
                resumedTime = Math.min(resumedTime, Math.max(0, secondsUntilEnd));
              }
              
              setTimeRemaining(resumedTime);
              setTabViolations(parsed.tabViolations || 0);
              setProctoringViolations(parsed.proctoringViolations || { noFace: 0, multipleFaces: 0, lookingAway: 0, headMovement: 0 });
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
      alert('🚨 Exam auto-submitted: You switched tabs or left the exam window 3 times.');
      setAutoSubmittedReason('Auto-submitted due to exceeding allowed tab switches (3/3).');
      submitExamAction(tabViolations, true);
      return;
    }

    // Show warnings via non-blocking banner for intermediate tab violations (avoids window.alert focus-loss blur cascades)
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

  // 4. Autosave state changes
  useEffect(() => {
    if (!exam || examSubmitted || cameraModalOpen) return;
    try {
      const state = {
        examId,
        userAnswers,
        currentQIndex,
        timeRemaining,
        tabViolations,
        proctoringViolations,
        timestamp: Date.now()
      };
      localStorage.setItem(getSaveKey(), JSON.stringify(state));
    } catch {}

    const timer = setTimeout(async () => {
      try {
        const idToken = await firebaseUser!.getIdToken();
        await fetch('/api/student/exams', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({
            action: 'autosave',
            examId,
            userAnswers
          })
        });
      } catch (e) {
        console.warn("DB Autosave failed:", e);
      }
    }, 10000);

    return () => clearTimeout(timer);
  }, [userAnswers, currentQIndex, timeRemaining, tabViolations, proctoringViolations, exam, examSubmitted, cameraModalOpen, examId, firebaseUser]);

  // 5. LateX rendering trigger on current question




  const handleProceedToExam = async () => {
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
    }
  };





  const submitExamAction = async (finalTabViolations?: number, proctoringViolationTriggered?: boolean) => {
    stopAllProctoring();
    setBlockingMessage('Submitting exam... Please do not close this window.');
    
    const activeTabViolations = finalTabViolations ?? tabViolations;
    const durationSpent = exam ? (exam.duration * 60) - timeRemaining : 0;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/student/exams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId,
          userAnswers,
          durationSpent,
          tabViolations: activeTabViolations,
          proctoringViolations,
          startedAt,
          proctoringViolationTriggered: !!proctoringViolationTriggered,
          micBypassed: !!micBypassed,
          disputedQuestionIds: Array.from(disputedQuestionIds),
          violations: {
            tabOutCount: activeTabViolations,
            noFaceCount: proctoringViolations.noFace || 0,
            multipleFacesCount: proctoringViolations.multipleFaces || 0,
            lookingAwayCount: proctoringViolations.lookingAway || 0,
            headMovementCount: proctoringViolations.headMovement || 0,
            screenshots: []
          }
        })
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.message || 'Submission failed.');
      }

      setExamSubmitted(true);
      setBlockingMessage('');
      localStorage.removeItem(getSaveKey());
      
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
      alert(`Error submitting: ${err.message || 'Connection lost'}. We have saved your progress locally. Please reload to try again.`);
      setBlockingMessage('');
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
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '500px' }}>{error || 'Exam configurations failed to load.'}</div>
        <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ marginTop: '20px' }}>Go Back</button>
      </div>
    );
  }

  if (!exam.questions || exam.questions.length === 0) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '500px', textAlign: 'center' }}>
          This exam contains no questions or is not configured yet. Please contact your administrator.
        </div>
        <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ marginTop: '20px' }}>Go Back</button>
      </div>
    );
  }

  const currentQuestion = exam.questions[currentQIndex];
  const currentAnswerObj = userAnswers[currentQIndex];
  const currentAnswer = currentAnswerObj?.answer || '';
  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh' }}>
      {/* Fullscreen & Focus Lockout Overlay */}
      {(!isFullscreen || !isWindowFocused) && !cameraModalOpen && !examSubmitted && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.9)',
          backdropFilter: 'blur(16px)',
          WebkitBackdropFilter: 'blur(16px)',
          zIndex: 99999,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '20px',
          color: 'var(--text)'
        }}>
          <div style={{
            background: 'var(--surface-popover)',
            border: '1px solid var(--border-popover)',
            borderRadius: '16px',
            padding: '40px 30px',
            maxWidth: '480px',
            width: '100%',
            textAlign: 'center',
            boxShadow: 'var(--shadow-xl)',
            display: 'flex',
            flexDirection: 'column',
            gap: '20px'
          }}>
            <div style={{ fontSize: '60px' }}>⚠️</div>
            {!isFullscreen ? (
              <>
                <h2 style={{ fontSize: '22px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
                  Fullscreen Required
                </h2>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.6', margin: 0 }}>
                  To maintain the integrity of this exam, you must stay in fullscreen mode. Your test progress is temporarily paused. 
                </p>
                <button
                  className="btn btn-primary"
                  onClick={() => {
                    document.documentElement.requestFullscreen().catch(() => {});
                  }}
                  style={{
                    width: '100%',
                    padding: '14px',
                    fontSize: '15px',
                    fontWeight: 'bold',
                    marginTop: '10px'
                  }}
                >
                  Re-enter Fullscreen
                </button>
              </>
            ) : (
              <>
                <h2 style={{ fontSize: '22px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
                  Window Focus Lost!
                </h2>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.6', margin: 0 }}>
                  To maintain the integrity of this exam, you must keep the exam window focused. You cannot click out, switch tabs, or use split screen during the exam.
                </p>
                <div style={{ color: 'var(--warning)', fontWeight: 700, fontSize: '13px', marginTop: '10px' }}>
                  Please click or tap here to resume focus.
                </div>
              </>
            )}
          </div>
        </div>
      )}

      {/* Floating Alert Banner for active proctoring violations */}
      {activeViolationWarning && (
        <div style={{
          position: 'fixed',
          top: '20px',
          left: '50%',
          transform: 'translateX(-50%)',
          background: '#d35400',
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
      {/* Script Injections for MediaPipe (Lazy loaded when modal is open) */}
      {cameraModalOpen && (
        <>
          <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
          <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />
        </>
      )}


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
                <h2>⚙️ Pre-Exam Hardware Diagnostic</h2>
                <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '10px 0 16px' }}>Verify your camera and microphone are functioning before entering the proctored workspace.</p>

            <div style={{ 
              background: 'rgba(239, 68, 68, 0.08)', 
              border: '1px dashed rgba(239, 68, 68, 0.3)', 
              borderRadius: 'var(--radius-sm)', 
              padding: '12px 16px', 
              marginBottom: '16px', 
              textAlign: 'left' 
            }}>
              <strong style={{ fontSize: '12px', color: '#ef4444', display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
                ⚠️ Proctored Exam Rules & Violation Limits
              </strong>
              <ul style={{ margin: 0, paddingLeft: '16px', fontSize: '11px', color: 'var(--text-muted)', display: 'flex', flexDirection: 'column', gap: '4px', lineHeight: '1.4' }}>
                <li><strong>Tab Switching:</strong> Max 2 focus-loss warnings allowed. Exceeding this (3rd switch) will auto-submit your exam.</li>
                <li><strong>Face & Gaze Tracking:</strong> Enabled for integrity logging (no auto-submission).</li>
              </ul>
            </div>
            
            <div className="camera-preview" style={{ width: '100%', height: '240px', background: '#111', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative' }}>
              {cameraStream ? (
                <video 
                  ref={(el) => {
                    if (el && el.srcObject !== cameraStream) {
                      el.srcObject = cameraStream;
                      el.play().catch(() => {});
                    }
                  }}
                  autoPlay
                  playsInline
                  muted
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              ) : (
                <div style={{ color: '#666' }}>Webcam Feed Offline</div>
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
              <button className="btn btn-success" onClick={handleProceedToExam} style={{ marginTop: '15px', width: '100%' }}>
                Start Exam / Proceed
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
              border: `2px solid ${faceStatusClass === 'success' ? '#2ecc71' : '#e67e22'}`,
              boxShadow: '0 2px 6px rgba(0,0,0,0.5)'
            }}>
              <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', height: '100%', objectFit: 'cover' }}></video>
            </div>
            <div style={{
              padding: '2px 4px',
              borderRadius: '4px',
              background: faceStatusClass === 'success' ? 'rgba(46, 204, 113, 0.15)' : 'rgba(230, 126, 34, 0.15)',
              border: `1px solid ${faceStatusClass === 'success' ? '#2ecc71' : '#e67e22'}`,
              color: faceStatusClass === 'success' ? '#2ecc71' : '#e67e22',
              fontSize: '9px',
              fontWeight: 'bold',
              textAlign: 'center',
              maxWidth: '75px',
              whiteSpace: 'nowrap',
              overflow: 'hidden',
              textOverflow: 'ellipsis'
            }}>
              {faceStatus.replace(' Detected', '').replace(' Verified', '')}
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
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations.noFace}</span>
            </div>
            {/* Multiple */}
            <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '45px' }}>
              <span style={{ fontSize: '9px', color: 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>Multi</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations.multipleFaces}</span>
            </div>
            {/* Timer */}
            <div style={{ background: timeRemaining <= 120 ? 'rgba(231, 76, 60, 0.15)' : 'rgba(255,255,255,0.03)', border: `1px solid ${timeRemaining <= 120 ? '#e74c3c' : 'rgba(255,255,255,0.05)'}`, borderRadius: '6px', padding: '4px 8px', display: 'flex', flexDirection: 'column', alignItems: 'center', minWidth: '60px' }}>
              <span style={{ fontSize: '9px', color: timeRemaining <= 120 ? '#e74c3c' : 'rgba(255,255,255,0.4)', textTransform: 'uppercase' }}>Time</span>
              <span style={{ fontSize: '11px', fontWeight: 'bold', color: timeRemaining <= 120 ? '#e74c3c' : 'white' }}>{formattedTime}</span>
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
            {exam.questions.map((_, idx) => {
              const answered = userAnswers[idx]?.answer !== '';
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
          <div ref={questionContainerRef} key={currentQuestion.id} className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', padding: '16px', marginBottom: '12px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '12px', color: 'var(--text-muted)', fontSize: '12px' }}>
              <span>Question {currentQIndex + 1} of {exam.questions.length}</span>
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                <span className="badge">{currentQuestion.marks || 1} Marks</span>
                {!disputedQuestionIds.has(currentQuestion.id || currentQuestion.questionCode || String(currentQIndex)) && (
                  <button
                    type="button"
                    onClick={() => setReportModalOpen(true)}
                    style={{
                      background: 'transparent',
                      border: '1px solid #ef4444',
                      color: '#ef4444',
                      borderRadius: '4px',
                      padding: '2px 8px',
                      fontSize: '10.5px',
                      fontWeight: 600,
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '3px'
                    }}
                    title="Report defective question (missing options, broken formula, wrong text)"
                  >
                    🚩 Report Issue
                  </button>
                )}
                {disputedQuestionIds.has(currentQuestion.id || currentQuestion.questionCode || String(currentQIndex)) && (
                  <span style={{ fontSize: '10.5px', color: '#f59e0b', fontWeight: 'bold' }}>
                    ⚠️ Bypassed
                  </span>
                )}
              </div>
            </div>


            {currentQuestion.type !== 'assertion_reason' && (
              <div 
                className="math-container"
                style={{ fontSize: '15px', lineHeight: '1.6', marginBottom: '16px', whiteSpace: 'pre-line' }}
              >
                {preprocessMathText(currentQuestion.text)}
              </div>
            )}

            {/* Options Area based on type */}
            <div style={{ padding: '0 0 10px' }}>
              {/* 1. Single MCQ / Any question with options */}
              {currentQuestion.type !== 'multiple_mcq' && currentQuestion.type !== 'multi_mcq' && currentQuestion.type !== 'true_false' && currentQuestion.type !== 'assertion_reason' && Array.isArray(currentQuestion.options) && currentQuestion.options.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {currentQuestion.options.map((opt, oIdx) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    const selected = currentAnswer === letter;
                    return (
                      <div 
                        key={`${currentQuestion.id}-${oIdx}`}
                        onClick={() => handleSelectOption(currentQIndex, letter)}
                        className="option"
                        style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px', background: selected ? 'var(--accent-soft)' : 'var(--surface-2)', borderRadius: 'var(--radius-sm)', cursor: 'pointer', border: selected ? '1px solid var(--accent)' : '1px solid transparent' }}
                      >
                        <input type="radio" checked={selected} readOnly style={{ width: '18px', height: '18px' }} />
                        <label 
                          className="math-container"
                          style={{ fontSize: '14px', cursor: 'pointer' }}
                        >
                          <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(opt))}
                        </label>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* 2. Multiple MCQ */}
              {(currentQuestion.type === 'multiple_mcq' || currentQuestion.type === 'multi_mcq') && currentQuestion.options && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {currentQuestion.options.map((opt, oIdx) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    let checked = false;
                    try {
                      checked = JSON.parse(currentAnswer || '[]').includes(letter);
                    } catch {}
                    
                    return (
                      <div 
                        key={`${currentQuestion.id}-${oIdx}`}
                        onClick={() => handleCheckboxOption(currentQIndex, letter)}
                        className="option"
                        style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px', background: checked ? 'var(--accent-soft)' : 'var(--surface-2)', borderRadius: 'var(--radius-sm)', cursor: 'pointer', border: checked ? '1px solid var(--accent)' : '1px solid transparent' }}
                      >
                        <input type="checkbox" checked={checked} readOnly style={{ width: '18px', height: '18px' }} />
                        <label 
                          className="math-container"
                          style={{ fontSize: '14px', cursor: 'pointer' }}
                        >
                          <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(opt))}
                        </label>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* 3. True / False */}
              {currentQuestion.type === 'true_false' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {['True', 'False'].map((val) => {
                    const selected = currentAnswer === val;
                    return (
                      <div 
                        key={`${currentQuestion.id}-${val}`}
                        onClick={() => handleSelectOption(currentQIndex, val)}
                        className="option"
                        style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px', background: selected ? 'var(--accent-soft)' : 'var(--surface-2)', borderRadius: 'var(--radius-sm)', cursor: 'pointer', border: selected ? '1px solid var(--accent)' : '1px solid transparent' }}
                      >
                        <input type="radio" checked={selected} readOnly style={{ width: '18px', height: '18px' }} />
                        <label style={{ fontSize: '14px', cursor: 'pointer' }}>{val}</label>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* 4. Assertion & Reason */}
              {currentQuestion.type === 'assertion_reason' && (() => {
                const { assertion, reason } = extractAssertionAndReason(currentQuestion);
                
                const defaultArOptions = [
                  { code: 'A', text: 'Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).' },
                  { code: 'B', text: 'Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).' },
                  { code: 'C', text: 'Assertion (A) is true, but Reason (R) is false.' },
                  { code: 'D', text: 'Assertion (A) is false, but Reason (R) is true.' }
                ];

                let arOptions = defaultArOptions;
                if (Array.isArray(currentQuestion.options) && currentQuestion.options.length > 0) {
                  arOptions = currentQuestion.options.map((opt: any, oIdx: number) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    if (typeof opt === 'string') {
                      return { code: letter, text: opt };
                    }
                    if (opt && typeof opt === 'object') {
                      return {
                        code: opt.code || opt.value || letter,
                        text: opt.text || opt.value || opt.label || String(opt)
                      };
                    }
                    return { code: letter, text: String(opt) };
                  });
                }
                
                return (
                  <div>
                    <div className="assertion-box" style={{ background: 'var(--accent-soft)', padding: '15px', borderRadius: 'var(--radius-sm)', marginBottom: '15px' }}>
                      <div 
                        className="math-container"
                        style={{ padding: '8px 0 8px 12px', borderLeft: '3px solid var(--accent)', margin: '4px 0', fontSize: '14px' }}
                      >
                        <strong>Assertion (A):</strong> {preprocessMathText(assertion)}
                      </div>
                      <div 
                        className="math-container"
                        style={{ padding: '8px 0 8px 12px', borderLeft: '3px solid var(--accent)', margin: '4px 0', fontSize: '14px' }}
                      >
                        <strong>Reason (R):</strong> {preprocessMathText(reason)}
                      </div>
                    </div>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      {arOptions.map((opt) => {
                        const selected = currentAnswer === opt.code;
                        return (
                          <div 
                            key={`${currentQuestion.id}-${opt.code}`}
                            onClick={() => handleSelectOption(currentQIndex, opt.code)}
                            className="option"
                            style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px', background: selected ? 'var(--accent-soft)' : 'var(--surface-2)', borderRadius: 'var(--radius-sm)', cursor: 'pointer', border: selected ? '1px solid var(--accent)' : '1px solid transparent' }}
                          >
                            <input type="radio" checked={selected} readOnly style={{ width: '18px', height: '18px' }} />
                            <label 
                              className="math-container"
                              style={{ fontSize: '14px', cursor: 'pointer' }}
                            >
                              <strong>({opt.code})</strong> {preprocessMathText(stripOptionLabel(opt.text))}
                            </label>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })()}

              {/* 5. Numerical and its variants (when no options provided) */}
              {(currentQuestion.type === 'numerical' || currentQuestion.type === 'numerical_short' || currentQuestion.type === 'numerical_long') && (!Array.isArray(currentQuestion.options) || currentQuestion.options.length === 0) && (
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Numerical Value:</label>
                  <input 
                    type="number" 
                    value={currentAnswer}
                    onChange={(e) => handleTextInput(currentQIndex, e.target.value)}
                    placeholder="Enter numbers only..."
                    style={{ width: '100%', padding: '10px', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-sm)', fontSize: '14px' }}
                  />
                </div>
              )}

              {/* 6. Fill in the Blanks */}
              {(currentQuestion.type === 'fill_blank' || currentQuestion.type === 'fill_blanks') && (
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Missing Word:</label>
                  <input 
                    type="text" 
                    value={currentAnswer}
                    onChange={(e) => handleTextInput(currentQIndex, e.target.value)}
                    placeholder="Type answer here..."
                    style={{ width: '100%', padding: '10px', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-sm)', fontSize: '14px' }}
                  />
                </div>
              )}

              {/* 7. Subjective explanations (all subjective variants) */}
              {(currentQuestion.type === 'subjective' || 
                currentQuestion.type.startsWith('subjective_') || 
                currentQuestion.type.startsWith('sub_') || 
                currentQuestion.type === 'scientific_reasoning' || 
                currentQuestion.type === 'differentiate' || 
                currentQuestion.type === 'laws_principles') && (
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Write Explanation:</label>
                  <textarea 
                    value={currentAnswer}
                    onChange={(e) => handleTextInput(currentQIndex, e.target.value)}
                    placeholder="Type detailed answer here..."
                    style={{ width: '100%', padding: '10px', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-sm)', minHeight: '120px', resize: 'vertical', fontSize: '14px' }}
                  />
                </div>
              )}
            </div>
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
            
            {currentQIndex === exam.questions.length - 1 ? (
              <button className="btn btn-danger" onClick={() => submitExamAction()}>
                📋 Submit Exam
              </button>
            ) : (
              <button 
                className="btn btn-primary" 
                onClick={() => setCurrentQIndex(prev => Math.min(exam.questions.length - 1, prev + 1))}
              >
                Next →
              </button>
            )}
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
                <div style={{ background: 'rgba(231, 76, 60, 0.1)', border: '1px solid rgba(231, 76, 60, 0.3)', borderRadius: '8px', padding: '12px', color: '#e74c3c', fontSize: '13px', fontWeight: 600, marginBottom: '20px' }}>
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
                    const spent = exam ? (exam.duration * 60) - timeRemaining : 0;
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
                               <span style={{ background: 'rgba(230,126,34,0.12)', color: '#d35400', padding: '2px 6px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold', marginLeft: '8px' }}>
                                 ⚠️ Reason: {currentReason}
                               </span>
                             )}
                           </div>
                           <span style={{ 
                             fontWeight: 'bold', 
                             fontSize: '10px',
                             padding: '2px 8px',
                             borderRadius: '12px',
                             background: isUnanswered ? 'rgba(255,255,255,0.1)' : 'rgba(244, 67, 54, 0.2)',
                             color: isUnanswered ? 'var(--text-muted)' : '#f44336' 
                           }}>
                             {isUnanswered ? 'Unattempted' : 'Incorrect'}
                           </span>
                         </div>

                        {matchingQ?.type === 'assertion_reason' && matchingQ.assertion && matchingQ.reason ? (
                          <div style={{ marginBottom: '12px', fontSize: '13px' }}>
                            <p style={{ margin: '4px 0' }}><strong>Assertion (A):</strong> <span className="math-container">{preprocessMathText(matchingQ.assertion)}</span></p>
                            <p style={{ margin: '4px 0' }}><strong>Reason (R):</strong> <span className="math-container">{preprocessMathText(matchingQ.reason)}</span></p>
                          </div>
                        ) : (
                          <p className="math-container" style={{ fontSize: '13px', margin: '0 0 12px 0', fontWeight: 'bold', lineHeight: '1.4' }}>
                            {preprocessMathText(qItem.questionText)}
                          </p>
                        )}

                        {/* Options list rendering matching result scorecard */}
                        {matchingQ?.options && matchingQ.options.length > 0 ? (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '12px' }}>
                            {matchingQ.options.map((opt: any, oi: number) => {
                              const optKey = getRawOptionKey(opt);
                              const optText = getRawOptionText(opt);
                              
                              const isCorrectOpt = Array.isArray(matchingQ.correctAnswer)
                                ? matchingQ.correctAnswer.includes(optKey)
                                : (matchingQ.correctAnswer === optKey || (Array.isArray(matchingQ.correctAnswers) && matchingQ.correctAnswers.includes(optKey)));
                              
                              const isUserOpt = isOptionSelectedByUser(qItem.userAnswer, optKey, oi, optText);

                              let border = '1px solid var(--review-option-border)';
                              let background = 'var(--review-option-bg)';
                              let color = 'var(--text)';
                              let prefix = '';

                              if (isCorrectOpt) {
                                border = '1.5px solid var(--success)';
                                background = 'var(--success-bg)';
                                color = 'var(--success)';
                                prefix = '✅ ';
                              }
                              
                              if (isUserOpt && !isCorrectOpt) {
                                border = '1.5px solid var(--danger)';
                                background = 'rgba(220, 38, 38, 0.08)';
                                color = 'var(--danger)';
                                prefix = '❌ ';
                              } else if (isUserOpt && isCorrectOpt) {
                                prefix = '🎯 ';
                              }

                              return (
                                <div 
                                  key={oi} 
                                  style={{ 
                                    display: 'flex', 
                                    alignItems: 'center', 
                                    gap: '6px',
                                    padding: '8px 12px', 
                                    border, 
                                    borderRadius: 'var(--radius-sm)', 
                                    background,
                                    color,
                                    fontSize: '12px',
                                    fontWeight: (isCorrectOpt || isUserOpt) ? 600 : 400
                                  }}
                                >
                                  {prefix && <span style={{ marginRight: '4px' }}>{prefix}</span>}
                                  <span className="math-container">{preprocessMathText(optText)}</span>
                                </div>
                              );
                            })}
                          </div>
                        ) : null}

                        {/* Answers Side-by-Side Grid */}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '12px', background: 'var(--surface-3)', padding: '8px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', marginBottom: '12px' }}>
                          <div style={{ lineHeight: '1.4' }}>
                            <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Your Answer:</strong>
                            <span className="math-container" style={{ color: 'var(--text)', fontWeight: 600 }}>
                              {preprocessMathText(
                                isUnanswered ? '(blank)' : getOptionText(qItem.questionText, qItem.userAnswer || '')
                              )}
                            </span>
                          </div>
                          <div style={{ lineHeight: '1.4' }}>
                            <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Correct Answer:</strong>
                            <span className="math-container" style={{ color: 'var(--success)', fontWeight: 'bold' }}>
                              {preprocessMathText(
                                getOptionText(qItem.questionText, qItem.correctAnswer)
                              )}
                            </span>
                          </div>
                        </div>

                        {explanation && (
                          <div style={{ marginTop: '12px', fontSize: '12px', color: 'var(--text-muted)', borderTop: '1px dashed var(--border-light)', paddingTop: '8px', marginBottom: '12px' }}>
                            <strong>Solution Explanation:</strong>
                            <p className="math-container" style={{ margin: '4px 0 0 0', lineHeight: '1.4' }}>{preprocessMathText(explanation)}</p>
                          </div>
                        )}

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
                                      color: isSelected ? '#ffffff' : 'var(--text)',
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
                                      color: isSelected ? '#ffffff' : 'var(--text)',
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
                          disabled={isUnderstood || !selectedReasons[qItem.globalIdx]}
                          onClick={() => {
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
                    background: isAllReviewed ? 'rgba(46, 204, 113, 0.15)' : 'rgba(243, 156, 18, 0.15)',
                    color: isAllReviewed ? '#2e7d32' : '#d35400',
                    border: isAllReviewed ? '1px solid #2e7d32' : '1px solid #d35400',
                    fontWeight: 'bold'
                  }}>
                    {isAllReviewed 
                      ? '✅ Excellent! You have reviewed all questions. You can now submit.' 
                      : `Reviewed: ${reviewedCount}/${totalToReview} completed. Click "I Understand" for each question above.`
                    }
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
                    <button 
                      className="btn btn-primary" 
                      disabled={!isAllReviewed || reviewSubmitting} 
                      onClick={async () => {
                        setReviewSubmitting(true);
                        try {
                          const idToken = await firebaseUser!.getIdToken();
                          const res = await fetch('/api/student/exams', {
                            method: 'PUT',
                            headers: {
                              'Content-Type': 'application/json',
                              'Authorization': `Bearer ${idToken}`
                            },
                            body: JSON.stringify({ 
                              examId,
                              wrongAnswerReasons: selectedReasons
                            })
                          });
                          if (!res.ok) throw new Error('Failed to update submission status');
                          
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
                      {reviewSubmitting ? 'Submitting...' : '🚀 Final Submit to Parents'}
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
              <div style={{ background: 'rgba(231, 76, 60, 0.1)', border: '1px solid rgba(231, 76, 60, 0.3)', borderRadius: '8px', padding: '12px', color: '#e74c3c', fontSize: '13px', fontWeight: 600, margin: '5px 0' }}>
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

            <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ width: '100%', padding: '12px', fontSize: '14px', fontWeight: 'bold', marginTop: '10px' }}>
              Go to Student Dashboard
            </button>
          </div>
        </div>
      )}

      {/* Report Question Issue Modal */}
      {reportModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', padding: '24px', maxWidth: '480px', width: '100%', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              🚩 Report Question &amp; Skip
            </h3>
            <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.4', marginBottom: '16px' }}>
              If there is a defect with this question (missing options, broken symbols, incomplete text), you can report it. An automated screenshot proof will be captured and sent to your teacher, and this question will be <strong>excluded from your score and total marks with zero penalty</strong>.
            </p>

            <div style={{ marginBottom: '14px' }}>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px', color: 'var(--text)' }}>
                Issue Category:
              </label>
              <select 
                value={reportReason}
                onChange={(e) => setReportReason(e.target.value)}
                style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px' }}
              >
                <option value="missing_options">Missing Options / No Choices</option>
                <option value="broken_formula">Broken Formula / LaTeX / Image</option>
                <option value="incorrect_text">Incomplete or Incorrect Question Text</option>
                <option value="duplicate_options">Duplicate / Confusing Options</option>
                <option value="other">Other Issue</option>
              </select>
            </div>

            <div style={{ marginBottom: '16px' }}>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px', color: 'var(--text)' }}>
                Additional Notes (Optional):
              </label>
              <textarea 
                value={reportNotes}
                onChange={(e) => setReportNotes(e.target.value)}
                placeholder="Describe what looks wrong..."
                rows={2}
                style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px', resize: 'none' }}
              />
            </div>

            <div style={{ background: 'rgba(16, 185, 129, 0.08)', border: '1px solid rgba(16, 185, 129, 0.2)', borderRadius: 'var(--radius-sm)', padding: '10px 12px', fontSize: '11.5px', color: 'var(--success)', marginBottom: '18px' }}>
              📷 <strong>Automated Proof:</strong> A clean visual snapshot of this question card will be captured and attached automatically for teacher review.
            </div>

            <div style={{ display: 'flex', gap: '10px' }}>
              <button 
                type="button"
                className="btn btn-secondary" 
                onClick={() => setReportModalOpen(false)}
                disabled={isSubmittingReport}
                style={{ flex: 1 }}
              >
                Cancel
              </button>
              <button 
                type="button"
                className="btn btn-primary" 
                onClick={handleReportQuestion}
                disabled={isSubmittingReport}
                style={{ flex: 1, background: '#ef4444', borderColor: '#ef4444' }}
              >
                {isSubmittingReport ? 'Reporting...' : 'Bypass & Report'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
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
      <TakeExamContent />
    </React.Suspense>
  );
}
