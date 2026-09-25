'use client';

import React, { useEffect, useState, useRef, useCallback, Suspense, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { t } from '@/lib/i18n';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { normalizeOptionAnswer, preprocessMathText, evaluateQuestionAnswer, stripOptionLabel, extractAssertionAndReason, isMultipleChoiceType, isSingleChoiceType, isTrueFalseType, isAssertionReasonType, isFillBlanksType, isNumericalType, parseAnswerList, isOptionMatch } from '@/lib/questionTypes';
import { useMathRender } from '@/hooks/useMathRender';
import { usePractice } from '@/hooks/usePractice';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';
import { useLiveExam } from '@/hooks/useLiveExam';
import { formatDuration, formatDateTimeIST } from '@/lib/dateUtils';

interface QuestionItem {
  id: string;
  questionCode: string;
  text: string;
  type: string;
  options: any[];
  assertion?: string;
  reason?: string;
  difficulty: string;
  bloomLevel: string;
  solution?: string;
  correctAnswer?: string;
  correctAnswers?: string[];
}

interface PracticeData {
  topicCode: string;
  topicName?: string;
  topicScope?: string;
  topicClassification?: string;
  targetQuestions?: number;
  requiredConfidence?: number;
  maxSessionsAllowed?: number;
  currentSetNumber?: number;
  dailySessions?: number;
  practiceQuestionsAttempted?: number;
  totalQuestions: number;
  maxQuestionsAvailable?: number;
  totalTopicPool?: number;
  questions: QuestionItem[];
  masteryAtStart: number;
  idealTimeSeconds: number;
  totalAttemptedCount?: number;
  isRecoveryMode?: boolean;
}

function TopicPracticeContent() {
  const { startSession, submitGrading } = usePractice();
  const { firebaseUser, logout, user } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();

  const topicCode = searchParams.get('topicCode') || '';
  const category = searchParams.get('category') || 'continuePractice';
  const mode = searchParams.get('mode') || '';
  const isRecoveryMode = mode === 'recovery';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [data, setData] = useState<PracticeData | null>(null);
  const [requireTextbookStudy, setRequireTextbookStudy] = useState(false);
  const [examCategory, setExamCategory] = useState<'standard' | 'foundation'>('standard');
  const [showUnlockModal, setShowUnlockModal] = useState(false);
  const [unlockedSelected, setUnlockedSelected] = useState(false);
  const [textbookStudyMessage, setTextbookStudyMessage] = useState('');
  const [textbookConfirmedCheck, setTextbookConfirmedCheck] = useState(false);
  const [confirmingTextbook, setConfirmingTextbook] = useState(false);
  const [lockType, setLockType] = useState<'initial' | 'cooldown' | 'daily' | 'recovery_next_day' | 'recovery_awaiting_approval' | null>(null);
  const [showRecoveryPrompt, setShowRecoveryPrompt] = useState(false);
  const [recoveryMessage, setRecoveryMessage] = useState('');
  const [recoveryConfirmedCheck, setRecoveryConfirmedCheck] = useState(false);
  const [confirmingRecovery, setConfirmingRecovery] = useState(false);

  // Setup practice status
  const [started, setStarted] = useState(false);
  const [finished, setFinished] = useState(false);
  const finishedRef = useRef(false);
  const isFetchingRef = useRef(false);
  const isSubmittingPracticeRef = useRef(false);
  const [isSubmittingPractice, setIsSubmittingPractice] = useState(false);
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [sessionId] = useState(() => `sess_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
  const [userAnswers, setUserAnswers] = useState<string[]>([]);
  const [submittedAnswers, setSubmittedAnswers] = useState<boolean[]>([]);
  const [questionResults, setQuestionResults] = useState<(boolean | null)[]>([]);
  const [feedbackOpen, setFeedbackOpen] = useState(false);
  const [feedbackCorrect, setFeedbackCorrect] = useState(false);
  const [isWindowFocused, setIsWindowFocused] = useState(true);
  const [explanationTimer, setExplanationTimer] = useState(0);

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
      const canvas = await w.html2canvas(element, { scale: 1.5, useCORS: true, backgroundColor: 'var(--surface-2)' });
      return canvas.toDataURL('image/jpeg', 0.7);
    } catch (err) {
      console.warn('Screenshot capture failed:', err);
      return null;
    }
  };

  const handleReportQuestion = async () => {
    if (!data || !firebaseUser || isSubmittingReport) return;
    const currentQ = data.questions[currentQIndex];
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
          topicCode,
          source: 'practice',
          sessionId,
          reason: reportReason,
          notes: reportNotes,
          screenshotData,
          questionText: currentQ.text || currentQ.assertion || ''
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit question report.');
      }

      setDisputedQuestionIds(prev => new Set(prev).add(currentQ.id));
      setReportModalOpen(false);
      setReportNotes('');
      alert('🚩 Question reported successfully! It has been excluded from your score and topic mastery calculations.');

      // Advance to next question automatically
      if (currentQIndex < data.questions.length - 1) {
        setCurrentQIndex(currentQIndex + 1);
      } else {
        handleFinishPractice();
      }
    } catch (err: any) {
      alert('Error reporting question: ' + (err.message || 'Unknown error'));
    } finally {
      setIsSubmittingReport(false);
    }
  };

  // Timer effect for explanation reading limit on mistakes
  useEffect(() => {
    if (explanationTimer <= 0) return;
    const interval = setInterval(() => {
      setExplanationTimer(prev => prev - 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [explanationTimer]);


  // Grace period timer ref
  const startTimeRef = useRef<number>(0);
  useEffect(() => {
    if (started && !startTimeRef.current) {
      startTimeRef.current = Date.now();
    }
  }, [started]);

  // Timers
  const [totalSeconds, setTotalSeconds] = useState(0);
  const [currentQSeconds, setCurrentQSeconds] = useState(0);

  // Camera & FaceMesh
  const [cameraModalOpen, setCameraModalOpen] = useState(true);
  const [isMounted, setIsMounted] = useState(false);

  // Stop camera and cleanup proctoring
  const stopWebcam = () => {
    if (proctorIntervalRef.current) {
      clearInterval(proctorIntervalRef.current);
      proctorIntervalRef.current = null;
    }
    stopProctoring();
    stopCameraStream();
  };

  // Fetch practice questions
  const fetchQuestions = async () => {
    if (!firebaseUser || !topicCode || isFetchingRef.current) return;
    isFetchingRef.current = true;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const pData = await startSession({
        topicCode,
        category,
        size: isRecoveryMode ? 8 : 6,
        idToken,
        examCategory: 'standard',
        mode
      });
      if (pData) {
        if (pData.requireRecoveryMode || pData.allowRecovery) {
          setShowRecoveryPrompt(true);
          setLockType(pData.lockType || null);
          setRecoveryMessage(pData.message || '');
          setLoading(false);
          return;
        }
        if (pData.requireTextbookStudy) {
          setRequireTextbookStudy(true);
          setLockType(pData.lockType || 'initial');
          setTextbookStudyMessage(pData.message || '');
          setLoading(false);
          return;
        }
        setData(pData);
        setUserAnswers(new Array(pData.questions.length).fill(''));
        setSubmittedAnswers(new Array(pData.questions.length).fill(false));
        setQuestionResults(new Array(pData.questions.length).fill(null));
        
        if (pData.masteryAtStart >= 80 && (pData.totalAttemptedCount || 0) < 30 && !unlockedSelected) {
          setShowUnlockModal(true);
        }
      } else {
        throw new Error('Failed to load practice questions');
      }
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error generating practice set');
    } finally {
      isFetchingRef.current = false;
      setLoading(false);
    }
  };

  const handleProceedFromUnlock = async () => {
    setUnlockedSelected(true);
    setShowUnlockModal(false);
    
    if (examCategory === 'foundation') {
      setLoading(true);
      try {
        const idToken = await firebaseUser!.getIdToken();
        const pData = await startSession({
          topicCode,
          category,
          size: 6,
          idToken,
          examCategory: 'foundation'
        });
        if (pData) {
          setData(pData);
          setUserAnswers(new Array(pData.questions.length).fill(''));
          setSubmittedAnswers(new Array(pData.questions.length).fill(false));
        } else {
          throw new Error('Failed to load foundation practice questions');
        }
      } catch (err: any) {
        console.error(err);
        setError(err.message || 'Error generating foundation challenge practice set');
      } finally {
        setLoading(false);
      }
    }
  };

  const handleConfirmTextbook = async () => {
    if (!firebaseUser || !topicCode || confirmingTextbook) return;
    setConfirmingTextbook(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/practice', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'confirmTextbook',
          topicCode
        })
      });
      if (!res.ok) {
        throw new Error('Failed to confirm textbook review.');
      }
      setRequireTextbookStudy(false);
      setLoading(true);
      fetchQuestions();
    } catch (err: any) {
      alert(err.message || 'Error updating textbook confirmation status.');
    } finally {
      setConfirmingTextbook(false);
    }
  };

  const handleApproveRecovery = async () => {
    if (!firebaseUser || !topicCode || confirmingRecovery) return;
    setConfirmingRecovery(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/practice', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'approveRecovery',
          topicCode
        })
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.message || 'Failed to approve recovery diagnostic.');
      }
      setShowRecoveryPrompt(false);
      setLockType(null);
      setLoading(true);
      router.push(`/student/topic?topicCode=${encodeURIComponent(topicCode)}&category=${category}&mode=recovery`);
    } catch (err: any) {
      alert(err.message || 'Error unlocking recovery diagnostic.');
    } finally {
      setConfirmingRecovery(false);
    }
  };
  const videoRef = useRef<HTMLVideoElement>(null);

  const {
    tabViolations,
    setTabViolations,
    awayTimeTotal: totalAwaySeconds,
    setAwayTimeTotal: setTotalAwaySeconds,
    proctoringViolations,
    setProctoringViolations,
    cameraStatus,
    cameraStream,
    startCameraStream,
    stopCameraStream,
    cleanupProctoring
  } = useLiveExam({
    examId: topicCode || '',
    examName: topicCode || 'Practice Topic',
    studentCode: user?.studentCode || '',
    studentName: user?.name || user?.email || 'Student',
    examType: 'practice',
    totalQuestions: data?.questions.length || null,
    currentQuestionIndex: currentQIndex,
    answeredCount: userAnswers.filter(a => a !== '').length,
    cameraVideoRef: videoRef,
    autonomous: (user as any)?.autonomous || false,
    started: started && !finished
  });

  const noFaceCount = proctoringViolations.noFace;
  const multipleFacesCount = proctoringViolations.multipleFaces;
  const lookingAwayCount = proctoringViolations.lookingAway;
  const headMovementCount = proctoringViolations.headMovement;
  const audioLevel = useAudioLevel(cameraStream);
  const [showReviewList, setShowReviewList] = useState(false);
  const [reviewTab, setReviewTab] = useState<'all' | 'correct' | 'incorrect'>('all');

  // Graded results after complete submit
  const [finalResult, setFinalResult] = useState<{
    score: number;
    totalQuestions: number;
    mastery: number;
    confidence: number;
    practiceNumber?: number;
    topicCode?: string;
    topicName?: string;
    completedAt?: string;
    questions: any[];
  } | null>(null);

  useMathRender([currentQIndex, started, finished, data, feedbackOpen, isMounted, showReviewList, reviewTab, finalResult]);

  useEffect(() => {
    if (videoRef.current && cameraStream && videoRef.current.srcObject !== cameraStream) {
      videoRef.current.srcObject = cameraStream;
      videoRef.current.play().catch(() => {});
    }
  }, [cameraStream, cameraModalOpen]);
  const lastActiveRef = useRef<number>(Date.now());
  const prevTabViolationsRef = useRef<number>(0);
  const prevNoFaceViolationsRef = useRef<number>(0);
  const prevLookingAwayViolationsRef = useRef<number>(0);
  const hasCrossedThresholdRef = useRef<boolean>(false);
  const lookingAwayStartRef = useRef<number | null>(null);
  const lastLookedAwayTimeRef = useRef<number | null>(null);
  const headMovementStartRef = useRef<number | null>(null);
  const multipleFacesStartRef = useRef<number | null>(null);
  const lastNoFaceLogRef = useRef<number>(0);
  const lastMultipleLogRef = useRef<number>(0);
  
  const baselinePoseRef = useRef<{ yaw: number; pitch: number; roll: number } | null>(null);
  const baselineFramesRef = useRef<{ yaw: number; pitch: number; roll: number }[]>([]);
  const lastSampledPoseRef = useRef<{ yaw: number; pitch: number; roll: number; timestamp: number } | null>(null);
  
  const questionContainerRef = useRef<HTMLDivElement>(null);

  // MediaPipe FaceMesh state refs
  const faceMeshReady = useRef(false);
  const lastFaceCount = useRef(0);
  const lastFaceMeshResults = useRef<any>(null);
  const lastHeadPose = useRef<any>(null);
  const lastHeadPoseRef = useRef<any>(null);
  const currentQuestion = data?.questions?.[currentQIndex];
  const isNumerical = useMemo(() => {
    if (!currentQuestion) return false;
    // Database explicit relaxProctoring or isNumerical overrides
    if ((currentQuestion as any).relaxProctoring === true || (currentQuestion as any).isNumerical === true) {
      return true;
    }
    const text = (currentQuestion.text || '').toLowerCase();
    const subject = ((currentQuestion as any).subject || '').toLowerCase();
    const mathKeywords = [
      'calculate', 'solve', 'evaluate', 'find the value', 'find the length', 
      'find the area', 'simplify', 'ratio', 'percentage', 'theorem', 
      'derivative', 'integral', 'factorize', 'expand', 'equation', 'expression',
      'probability', 'mean', 'median', 'mode', 'standard deviation', 'calculate',
      'numerical', 'geometry', 'algebra', 'prove', 'find the', 'what is the value'
    ];
    const hasKeyword = mathKeywords.some(keyword => text.includes(keyword));
    if (hasKeyword) return true;
    
    const mathSymbols = [
      '\\frac', '\\sqrt', '\\times', '\\div', '\\angle', '\\cong', '\\parallel', 
      '\\Delta', '\\pi', '\\theta', '\\alpha', '\\beta', '^', '=', '+', '-', '*', '/'
    ];
    const hasMathSymbol = mathSymbols.some(symbol => text.includes(symbol));
    if (hasMathSymbol) return true;

    if (/\d+/.test(text)) return true;

    if (currentQuestion.options && Array.isArray(currentQuestion.options)) {
      for (const opt of currentQuestion.options) {
        const optText = (opt.text || '').toLowerCase();
        if (/\d+/.test(optText) || mathSymbols.some(symbol => optText.includes(symbol))) {
          return true;
        }
      }
    }
    return false;
  }, [currentQuestion]);

  const {
    faceStatus,
    faceStatusClass,
    stopProctoring,
    stopAllProctoring
  } = useProctoring({
    videoRef,
    enabled: started && !!cameraStream && !finished,
    lockdownShortcuts: false,
    lockdownContextMenu: false,
    lockdownWindowFocus: false,
    lockdownFullscreen: false,
    startCameraStream,
    stopCameraStream,
    cleanupLiveExam: cleanupProctoring,
    isNumerical: isNumerical,
    onViolation: (type) => {
      if (type === 'no_face') {
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
  const proctorIntervalRef = useRef<any>(null);


  useEffect(() => {
    setIsMounted(true);
  }, []);

  useEffect(() => {
    if ((user as any)?.autonomous) {
      setError('Access Denied. Practice sessions are restricted for this student account.');
      setLoading(false);
      return;
    }
    if (topicCode) {
      fetchQuestions();
    } else {
      setError('No topicCode provided in URL parameters.');
      setLoading(false);
    }
  }, [firebaseUser, topicCode, user]);





  useEffect(() => {
    if (!started || finished) return;

    if (tabViolations >= 3) {
      alert('🚨 Practice auto-submitted: You switched tabs or left the practice window 3 times.');
      handleFinishPractice(true);
      return;
    }

    const noFaceVal = proctoringViolations?.noFace || 0;
    const lookingAwayVal = proctoringViolations?.lookingAway || 0;
    const cumulativeVal = tabViolations + noFaceVal + lookingAwayVal;

    // Detect if we currently cross any limit
    const crossedTab = tabViolations > 2; // > max 2
    const crossedNoFace = noFaceVal > 3; // > max 3
    const crossedLookingAway = lookingAwayVal > 3; // > max 3
    const crossedCumulative = cumulativeVal > 4; // > max 4

    const isCrossedNow = crossedTab || crossedNoFace || crossedLookingAway || crossedCumulative;

    if (isCrossedNow) {
      if (!hasCrossedThresholdRef.current) {
        // Just crossed! Show critical warning
        hasCrossedThresholdRef.current = true;
        
        let reason = '';
        if (crossedTab) reason = `Tab Switch limit of 2 crossed (${tabViolations} violations).`;
        else if (crossedNoFace) reason = `Face Absence limit of 3 crossed (${noFaceVal} violations).`;
        else if (crossedLookingAway) reason = `Looking Away limit of 3 crossed (${lookingAwayVal} violations).`;
        else if (crossedCumulative) reason = `Cumulative violation limit of 4 crossed (${cumulativeVal} violations).`;

        alert(`⚠️ CRITICAL WARNING: ${reason}\nYou have crossed the allowed proctoring threshold! ANY further violation of any kind will result in immediate automatic submission of your practice session!`);
      } else {
        // Already crossed previously, and a violation incremented!
        const tabIncremented = tabViolations > prevTabViolationsRef.current;
        const noFaceIncremented = noFaceVal > prevNoFaceViolationsRef.current;
        const lookingAwayIncremented = lookingAwayVal > prevLookingAwayViolationsRef.current;

        if (tabIncremented || noFaceIncremented || lookingAwayIncremented) {
          alert('🚨 Practice auto-submitted due to a post-threshold proctoring violation!');
          handleFinishPractice(true);
          return;
        }
      }
    } else {
      // Normal warnings (not yet crossed)
      if (tabViolations > prevTabViolationsRef.current) {
        alert(`⚠️ WARNING: You switched tabs or left the practice window!\nTab Violation ${tabViolations}/2. Please return to focus.`);
      }
      if (noFaceVal > prevNoFaceViolationsRef.current) {
        alert(`⚠️ WARNING: Face not detected!\nFace Absence Violation ${noFaceVal}/3. Please look at the camera.`);
      }
      if (lookingAwayVal > prevLookingAwayViolationsRef.current) {
        alert(`⚠️ WARNING: Please keep your eyes on the screen!\nLooking Away Violation ${lookingAwayVal}/3.`);
      }
    }

    prevTabViolationsRef.current = tabViolations;
    prevNoFaceViolationsRef.current = noFaceVal;
    prevLookingAwayViolationsRef.current = lookingAwayVal;
  }, [tabViolations, proctoringViolations, started, finished]);

  // Timers
  useEffect(() => {
    if (!started || finished) return;

    const interval = setInterval(() => {
      setTotalSeconds(prev => prev + 1);
      setCurrentQSeconds(prev => prev + 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [started, finished, currentQIndex]);

  // Reset current question timer on navigation
  useEffect(() => {
    setCurrentQSeconds(0);
  }, [currentQIndex]);

  // Proctoring stream checking wrapper
  const handleRunCheck = async () => {
    const stream = await startCameraStream();
    if (!stream) {
      const confirmBypass = window.confirm(
        "⚠️ Camera access failed or denied. Do you want to proceed with the practice anyway? (Your teacher will be notified that the camera is unavailable.)"
      );
      if (confirmBypass) {
        setCameraModalOpen(false);
        setStarted(true);
      }
    }
  };

  const handleProceedToExam = async () => {
    setCameraModalOpen(false);
    setStarted(true);
  };



  // Stop webcam stream when component unmounts
  useEffect(() => {
    return () => {
      stopWebcam();
    };
  }, []);





  // Submit single question answer for immediate feedback
  const handleSubmitQuestion = () => {
    if (!data) return;
    const q = data.questions[currentQIndex];
    const answer = userAnswers[currentQIndex] || '';

    const isMultiple = isMultipleChoiceType(q.type);
    const resolvedCorrectAnswer = isMultiple
      ? (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 ? q.correctAnswers : (q.correctAnswer ? parseAnswerList(q.correctAnswer) : []))
      : (q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : ''));

    const isCorrect = evaluateQuestionAnswer(
      q.type || 'OSC',
      answer,
      resolvedCorrectAnswer,
      q.options
    );

    setFeedbackCorrect(isCorrect);
    setFeedbackOpen(true);

    const submitted = [...submittedAnswers];
    submitted[currentQIndex] = true;
    setSubmittedAnswers(submitted);

    const results = [...questionResults];
    results[currentQIndex] = isCorrect;
    setQuestionResults(results);

    if (!isCorrect) {
      const qType = String(q.type || '').toLowerCase();
      const qText = String(q.text || q.assertion || '');
      const isMath = qText.includes('\\frac') || qText.includes('\\sqrt') || qText.includes('\\int') || qText.includes('=');
      
      let timerSec = 20; // 20s for factual recall
      if (qType.includes('numerical') || isMath || qType === 'one' || qType === 'ssn' || qType === 'sln') {
        timerSec = 40; // 40s for calculative / derivation problems
      } else if (qType === 'assertion_reason' || qType === 'oar' || qType.includes('multi') || qText.length > 150) {
        timerSec = 30; // 30s for conceptual & multi-statement logic
      }
      setExplanationTimer(timerSec);
    }
  };

  const handleNext = () => {
    setFeedbackOpen(false);
    if (!data) return;
    if (currentQIndex < data.questions.length - 1) {
      setCurrentQIndex(currentQIndex + 1);
    } else {
      handleFinishPractice();
    }
  };

  // Submit complete practice set
  const handleFinishPractice = async (proctoringViolationTriggered?: boolean) => {
    if (!firebaseUser || !data || isSubmittingPracticeRef.current || finishedRef.current) return;
    isSubmittingPracticeRef.current = true;
    setIsSubmittingPractice(true);
    setLoading(true);
    stopWebcam();

    try {
      const formattedAnswers = data.questions.map((q, idx) => {
        const uAns = userAnswers[idx] || '';
        let selectedOptionText = uAns;

        if (isMultipleChoiceType(q.type)) {
          try {
            const rawList = parseAnswerList(uAns);
            if (Array.isArray(rawList) && Array.isArray(q.options) && q.options.length > 0) {
              const matchedTexts = rawList.map((letter: string) => {
                if (typeof letter === 'string' && /^[A-Z]$/i.test(letter)) {
                  const oIdx = letter.toUpperCase().charCodeAt(0) - 65;
                  if (oIdx >= 0 && oIdx < q.options.length) {
                    const opt = q.options[oIdx];
                    return typeof opt === 'object' && opt ? (opt.text || opt.value || opt.label || '') : String(opt);
                  }
                }
                return String(letter);
              });
              selectedOptionText = JSON.stringify(matchedTexts);
            }
          } catch {}
        } else if (Array.isArray(q.options) && q.options.length > 0 && typeof uAns === 'string' && /^[A-Z]$/i.test(uAns)) {
          const oIdx = uAns.toUpperCase().charCodeAt(0) - 65;
          if (oIdx >= 0 && oIdx < q.options.length) {
            const opt = q.options[oIdx];
            selectedOptionText = typeof opt === 'object' && opt ? (opt.text || opt.value || opt.label || '') : String(opt);
          }
        }

        return {
          questionId: q.id,
          answer: uAns,
          selectedOptionText,
          optionsSnapshot: q.options || []
        };
      });

      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/practice', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          topicCode,
          category,
          answers: formattedAnswers,
          durationSpent: totalSeconds,
          sessionId,
          mode,
          isRecoveryMode,
          disputedQuestionIds: Array.from(disputedQuestionIds),
          violations: {
            tabOutCount: tabViolations,
            noFaceCount,
            multipleFacesCount,
            lookingAwayCount,
            headMovementCount,
            screenshots: []
          },
          proctoringViolationTriggered: !!proctoringViolationTriggered
        })
      });

      if (!res.ok) {
        throw new Error('Failed to grade practice submission');
      }

      const resData = await res.json();
      setFinalResult(resData);
      finishedRef.current = true;
      setFinished(true);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error submitting practice session');
    } finally {
      isSubmittingPracticeRef.current = false;
      setIsSubmittingPractice(false);
      setLoading(false);
    }
  };

  const handleCheckboxChange = (optionText: string) => {
    let currentChoices: string[] = [];
    try {
      currentChoices = JSON.parse(userAnswers[currentQIndex] || '[]');
    } catch {
      currentChoices = [];
    }

    if (currentChoices.includes(optionText)) {
      currentChoices = currentChoices.filter(x => x !== optionText);
    } else {
      currentChoices.push(optionText);
    }

    const updated = [...userAnswers];
    updated[currentQIndex] = JSON.stringify(currentChoices);
    setUserAnswers(updated);
  };

  const handleRadioChange = (choice: string) => {
    const updated = [...userAnswers];
    const currentVal = updated[currentQIndex] || '';
    updated[currentQIndex] = currentVal === choice ? '' : choice;
    setUserAnswers(updated);
  };

  const getIntegrityLevel = () => {
    const totalIssues = tabViolations + noFaceCount + multipleFacesCount + lookingAwayCount;
    if (totalIssues === 0) return { level: 'green', text: '🟢 Excellent Integrity', class: 'integrity-green' };
    if (totalIssues <= 5) return { level: 'yellow', text: '🟡 Good Integrity', class: 'integrity-yellow' };
    return { level: 'red', text: '🔴 Integrity Warning', class: 'integrity-red' };
  };

  const formatTime = formatDuration;

  // Cleanup webcam if navigating away
  useEffect(() => {
    return () => {
      stopWebcam();
    };
  }, [cameraStream]);

  if (user && (user as any).autonomous) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--warning)', boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px' }}>Practice Restricted / अभ्यास प्रतिबंधित</h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.5', marginBottom: '20px' }}>
            Autonomous mode is active on your account. Self-directed topic practice is disabled.
          </p>
          <button className="btn btn-primary" onClick={() => router.push('/student')}>
            🏠 Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  if (showRecoveryPrompt) {
    const isSameDayLocked = lockType === 'recovery_next_day';
    const isAwaitingApproval = lockType === 'recovery_awaiting_approval';
    const icon = isSameDayLocked ? '⏳' : isAwaitingApproval ? '👨‍🏫' : '🩺';
    const title = isSameDayLocked 
      ? 'Guided Recovery Diagnostic (Available Tomorrow)'
      : isAwaitingApproval
        ? 'Guided Recovery Diagnostic (Awaiting Approval)'
        : 'Guided Recovery Diagnostic (8 Targeted Questions)';

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ 
          maxWidth: '520px', 
          width: '100%', 
          textAlign: 'center', 
          padding: '40px 30px', 
          background: 'var(--surface)', 
          borderRadius: 'var(--radius-lg)', 
          border: '1px solid var(--accent)', 
          boxShadow: 'var(--shadow-glass)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '16px' }}>{icon}</div>
          <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '12px' }}>
            {title}
          </h3>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
            {recoveryMessage || "You have completed extensive practice on this topic. Take the Guided Recovery Diagnostic (8 targeted questions) to strengthen core concepts and achieve Mastery."}
          </p>

          {isAwaitingApproval && (
            <label style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '10px', 
              fontSize: '13px', 
              color: 'var(--text)', 
              cursor: 'pointer',
              padding: '12px 16px',
              background: 'var(--bg)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              width: '100%',
              marginBottom: '24px',
              boxSizing: 'border-box'
            }}>
              <input 
                type="checkbox" 
                checked={recoveryConfirmedCheck} 
                onChange={(e) => setRecoveryConfirmedCheck(e.target.checked)}
                style={{ width: '18px', height: '18px', cursor: 'pointer' }}
              />
              <span style={{ textAlign: 'left', lineHeight: '1.4' }}>
                I / My parent confirm that I have thoroughly reviewed the textbook concepts and notes for this topic.
              </span>
            </label>
          )}

          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Dashboard
            </button>
            {isSameDayLocked ? (
              <button 
                className="btn btn-secondary" 
                disabled 
                style={{ flex: 1, opacity: 0.6 }}
              >
                🔒 Available Tomorrow
              </button>
            ) : isAwaitingApproval ? (
              <button 
                className="btn btn-primary" 
                disabled={!recoveryConfirmedCheck || confirmingRecovery}
                onClick={handleApproveRecovery}
                style={{ 
                  flex: 2, 
                  fontWeight: 700, 
                  background: recoveryConfirmedCheck ? 'var(--accent-grad)' : undefined, 
                  opacity: (!recoveryConfirmedCheck || confirmingRecovery) ? 0.6 : 1 
                }}
              >
                {confirmingRecovery ? '⌛ Unlocking Diagnostic...' : '📖 Confirm Review & Start Diagnostic (8 Qs)'}
              </button>
            ) : (
              <button 
                className="btn btn-primary" 
                onClick={() => {
                  setShowRecoveryPrompt(false);
                  setLoading(true);
                  router.push(`/student/topic?topicCode=${encodeURIComponent(topicCode)}&category=${category}&mode=recovery`);
                }}
                style={{ flex: 1, fontWeight: 700 }}
              >
                🚀 Start Diagnostic (8 Qs)
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  if (requireTextbookStudy) {
    const isLockedState = lockType === 'cooldown' || lockType === 'daily';
    const icon = lockType === 'cooldown' ? '⏳' : lockType === 'daily' ? '🔒' : '📖';
    const heading = lockType === 'cooldown' 
      ? 'Concept Cooldown Active / विश्राम अवधि ⏳' 
      : lockType === 'daily' 
        ? 'Daily Limit Reached / दैनिक अभ्यास सीमा 🔒' 
        : 'Time to hit the textbook! / पाठ्यपुस्तक पढ़ें 📚';

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ 
          maxWidth: '520px', 
          width: '100%', 
          textAlign: 'center', 
          padding: '40px 30px', 
          background: 'var(--surface)', 
          borderRadius: 'var(--radius-lg)', 
          border: '1px solid var(--warning)', 
          boxShadow: 'var(--shadow-glass)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '16px' }}>{icon}</div>
          <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '12px' }}>
            {heading}
          </h3>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
            {textbookStudyMessage || "Let's take a break from tests. Please read your textbook and review your class notes for this chapter before trying again."}
          </p>
          
          {!isLockedState && (
            <label style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '10px', 
              fontSize: '13px', 
              color: 'var(--text)', 
              cursor: 'pointer',
              padding: '12px 16px',
              background: 'var(--bg)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              width: '100%',
              marginBottom: '24px',
              boxSizing: 'border-box'
            }}>
              <input 
                type="checkbox" 
                checked={textbookConfirmedCheck} 
                onChange={(e) => setTextbookConfirmedCheck(e.target.checked)}
                style={{ width: '18px', height: '18px', cursor: 'pointer' }}
              />
              <span style={{ textAlign: 'left' }}>I confirm that I have reviewed this concept in my textbook/notes.</span>
            </label>
          )}

          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Back to Dashboard
            </button>
            {!isLockedState && (
              <button 
                className="btn btn-primary" 
                disabled={!textbookConfirmedCheck || confirmingTextbook}
                onClick={handleConfirmTextbook}
                style={{ flex: 1 }}
              >
                {confirmingTextbook ? 'Updating...' : '⚡ Unlock & Resume'}
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Processing practice set...
        </div>
      </div>
    );
  }

  if (error || !data) {
    const isAutonomousBlock = error && error.includes('restricted');
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error || 'Could not load practice set.'}
        </div>
        <button 
          className="btn btn-primary" 
          onClick={() => isAutonomousBlock ? router.push('/student') : window.location.reload()} 
          style={{ marginTop: '16px' }}
        >
          {isAutonomousBlock ? 'Back to Dashboard' : 'Retry'}
        </button>
      </div>
    );
  }

  // Render empty questions screen
  if (data.questions.length === 0) {
    const isFullyMastered = (data as any).fullyMastered === true;
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px', background: 'var(--bg)' }}>
        <div className="card results-card" style={{ maxWidth: '500px', width: '100%', textAlign: 'center', padding: '30px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <h2 style={{ fontSize: '1.6rem', marginBottom: '15px' }}>{isFullyMastered ? 'Topic Mastered' : 'No Questions'}</h2>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', marginBottom: '20px' }}>
            {isFullyMastered
              ? 'Great job! You have achieved 100% mastery and successfully completed all practice questions for this topic.'
              : 'No practice questions currently available for this topic.'}
          </p>
          <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ width: '100%' }}>Back to Dashboard</button>
        </div>
      </div>
    );
  }

  // Render Completion Screen
  if (finished && finalResult) {
    const integrity = getIntegrityLevel();
    const masteryChange = finalResult.mastery - data.masteryAtStart;
    const efficiency = data.idealTimeSeconds > 0 ? Math.round((data.idealTimeSeconds / totalSeconds) * 100) : 0;
    const percentTimeAway = totalSeconds > 0 ? Math.round((totalAwaySeconds / totalSeconds) * 100) : 0;
    const practiceNum = finalResult.practiceNumber || data.currentSetNumber || 1;
    const practiceTopicName = finalResult.topicName || data.topicName || topicCode;
    const completedTimestampIST = formatDateTimeIST(finalResult.completedAt || new Date()) || '-';

    const evalQuestions = finalResult.questions && finalResult.questions.length > 0 
      ? finalResult.questions 
      : data.questions.map((q, idx) => ({
          ...q,
          userAnswer: userAnswers[idx] || '',
          isCorrect: questionResults[idx] === true
        }));

    const filteredReviewQuestions = evalQuestions.filter(q => {
      if (reviewTab === 'correct') return q.isCorrect;
      if (reviewTab === 'incorrect') return !q.isCorrect;
      return true;
    });

    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px', background: 'var(--bg)' }}>
        <div className="card results-card" style={{ maxWidth: '680px', width: '100%', textAlign: 'center', padding: '28px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          
          {/* Header Badge with Practice Number and IST Date/Time */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
            <span style={{ background: 'var(--accent)', color: 'var(--text-on-accent)', fontSize: '12px', fontWeight: 800, padding: '4px 10px', borderRadius: '14px' }}>
              📚 Practice Set #{practiceNum}
            </span>
            <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>
              🗓️ {completedTimestampIST}
            </span>
          </div>

          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>Practice Complete!</h2>
          <div style={{ fontSize: '13px', color: 'var(--accent)', fontWeight: 700, marginBottom: '16px' }}>
            {practiceTopicName} <span style={{ opacity: 0.7, fontWeight: 500 }}>({topicCode})</span>
          </div>

          <div className="score-big" style={{ fontSize: '3.5rem', fontWeight: 900, color: 'var(--accent)', margin: '10px 0', lineHeight: '1.1' }}>
            {finalResult.score}/{finalResult.totalQuestions}
          </div>
          <p style={{ fontSize: '20px', fontWeight: 'bold', margin: '4px 0 12px 0' }}>{Math.round((finalResult.score / finalResult.totalQuestions) * 100)}% Accuracy</p>
          <p style={{ margin: '8px 0', fontSize: '14px' }}>
            Mastery: {data.masteryAtStart}% → {finalResult.mastery}% ({masteryChange >= 0 ? `+${masteryChange}` : masteryChange}%)
          </p>
          <p style={{ margin: '4px 0', fontSize: '13px', color: 'var(--text-muted)' }}>
            ⏱️ Time: {formatTime(totalSeconds)} / Ideal: {formatTime(data.idealTimeSeconds)} ({efficiency}% efficiency)
          </p>

          <div style={{ background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '14px', margin: '16px 0', textAlign: 'left' }}>
            <div className={`integrity-level`} style={{ fontWeight: 'bold', fontSize: '13px', marginBottom: '6px' }}>{integrity.text}</div>
            {integrity.level !== 'green' && (
              <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                {tabViolations > 0 && <p style={{ margin: '2px 0' }}>• Tab switches: {tabViolations} times</p>}
                {totalAwaySeconds > 0 && <p style={{ margin: '2px 0' }}>• Time away: {formatTime(totalAwaySeconds)} ({percentTimeAway}% of total)</p>}
                {noFaceCount > 0 && <p style={{ margin: '2px 0' }}>• Face not detected: {noFaceCount} checks</p>}
                {lookingAwayCount > 0 && <p style={{ margin: '2px 0' }}>• Gaze violations: {lookingAwayCount} checks</p>}
              </div>
            )}
          </div>

          {/* Toggle Full Question Review */}
          <div style={{ margin: '16px 0' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => setShowReviewList(!showReviewList)} 
              style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', padding: '10px', fontSize: '13px', fontWeight: 700 }}
            >
              <span>{showReviewList ? '▲ Hide Detailed Review' : '▼ Review All Practice Questions & Solutions'}</span>
            </button>
          </div>

          {showReviewList && (
            <div style={{ textAlign: 'left', marginTop: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '16px', border: '1px solid var(--border-light)' }}>
              <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
                <button 
                  onClick={() => setReviewTab('all')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: reviewTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    background: reviewTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                    color: reviewTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  All ({evalQuestions.length})
                </button>
                <button 
                  onClick={() => setReviewTab('correct')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: reviewTab === 'correct' ? '1px solid var(--success)' : '1px solid var(--border-light)',
                    background: reviewTab === 'correct' ? 'var(--success-bg)' : 'transparent',
                    color: reviewTab === 'correct' ? 'var(--success)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Correct ({evalQuestions.filter((q: any) => q.isCorrect).length})
                </button>
                <button 
                  onClick={() => setReviewTab('incorrect')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: reviewTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                    background: reviewTab === 'incorrect' ? 'var(--danger-soft)' : 'transparent',
                    color: reviewTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Incorrect ({evalQuestions.filter((q: any) => !q.isCorrect).length})
                </button>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '14px', maxHeight: '420px', overflowY: 'auto', paddingRight: '4px' }}>
                {filteredReviewQuestions.map((qItem: any, idx: number) => {
                  const isMulti = isMultipleChoiceType(qItem.type);
                  const parsedUserAns = isMulti 
                    ? (Array.isArray(qItem.userAnswer) ? qItem.userAnswer : parseAnswerList(qItem.userAnswer))
                    : [qItem.userAnswer];
                  const parsedCorrectAns = isMulti
                    ? (Array.isArray(qItem.correctAnswers) && qItem.correctAnswers.length > 0 ? qItem.correctAnswers : (Array.isArray(qItem.correctAnswer) ? qItem.correctAnswer : parseAnswerList(qItem.correctAnswer)))
                    : [qItem.correctAnswer || (Array.isArray(qItem.correctAnswers) ? qItem.correctAnswers[0] : '')];

                  return (
                    <div key={idx} style={{ background: 'var(--surface)', padding: '12px', borderRadius: 'var(--radius-sm)', border: `1px solid ${qItem.isCorrect ? 'var(--success)' : 'var(--danger)'}` }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                        <span style={{ fontWeight: 800, fontSize: '12px' }}>Q#{idx + 1} {qItem.questionCode ? `• ${qItem.questionCode}` : ''}</span>
                        <span style={{ fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '4px', background: qItem.isCorrect ? 'var(--success-bg)' : 'var(--danger-soft)', color: qItem.isCorrect ? 'var(--success)' : 'var(--danger)' }}>
                          {qItem.isCorrect ? '✓ Correct' : '✕ Incorrect'}
                        </span>
                      </div>
                      <div style={{ fontSize: '13px', lineHeight: '1.5', marginBottom: '8px', fontWeight: 500 }} dangerouslySetInnerHTML={{ __html: preprocessMathText(qItem.text || qItem.assertion || '') }} />
                      
                      {qItem.options && Array.isArray(qItem.options) && qItem.options.length > 0 && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                          {qItem.options.map((opt: any, optIdx: number) => {
                            const optText = typeof opt === 'string' ? opt : (opt.text || opt.value || '');
                            const optKey = typeof opt === 'string' ? String.fromCharCode(65 + optIdx) : (opt.key || String.fromCharCode(65 + optIdx));
                            const isSelected = parsedUserAns.some((a: string) => isOptionMatch(optText, a) || isOptionMatch(optKey, a));
                            const isRight = parsedCorrectAns.some((a: string) => isOptionMatch(optText, a) || isOptionMatch(optKey, a));

                            let optBg = 'transparent';
                            let optBorder = 'var(--border-light)';
                            let optColor = 'inherit';
                            if (isRight) {
                              optBg = 'var(--success-bg)';
                              optBorder = 'var(--success)';
                              optColor = 'var(--success)';
                            } else if (isSelected && !isRight) {
                              optBg = 'var(--danger-soft)';
                              optBorder = 'var(--danger)';
                              optColor = 'var(--danger)';
                            }

                            return (
                              <div key={optIdx} style={{ padding: '6px 10px', fontSize: '12px', borderRadius: '4px', background: optBg, border: `1px solid ${optBorder}`, color: optColor, display: 'flex', gap: '6px' }}>
                                <span style={{ fontWeight: 700 }}>({optKey})</span>
                                <span dangerouslySetInnerHTML={{ __html: preprocessMathText(optText) }} />
                                {isSelected && <span style={{ marginLeft: 'auto', fontWeight: 700, fontSize: '11px' }}>[Your Answer]</span>}
                                {isRight && <span style={{ marginLeft: isSelected ? '4px' : 'auto', fontWeight: 700, fontSize: '11px' }}>[Correct]</span>}
                              </div>
                            );
                          })}
                        </div>
                      )}

                      {qItem.solution && (
                        <div style={{ marginTop: '8px', padding: '8px 10px', background: 'var(--bg-soft)', borderRadius: '4px', fontSize: '12px', borderLeft: '3px solid var(--accent)' }}>
                          <strong style={{ color: 'var(--accent)' }}>Explanation:</strong>{' '}
                          <span dangerouslySetInnerHTML={{ __html: preprocessMathText(qItem.solution) }} />
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', marginTop: '24px' }}>
            <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ flex: 1 }}>Dashboard</button>
            <button className="btn btn-secondary" onClick={() => window.location.reload()} style={{ flex: 1 }}>Practice Again</button>
          </div>
        </div>
      </div>
    );
  }

  const q = data.questions[currentQIndex];
  const uAns = userAnswers[currentQIndex] || '';
  const isQSubmitted = submittedAnswers[currentQIndex];

  const getCorrectOptionText = (qItem: QuestionItem) => {
    const isMultiple = isMultipleChoiceType(qItem.type);
    const rawAnswers = isMultiple
      ? (Array.isArray(qItem.correctAnswers) && qItem.correctAnswers.length > 0 ? qItem.correctAnswers : parseAnswerList(qItem.correctAnswer))
      : [qItem.correctAnswer || (Array.isArray(qItem.correctAnswers) ? qItem.correctAnswers[0] : '')];

    if (!qItem.options || qItem.options.length === 0) {
      return rawAnswers.filter(Boolean).join(', ') || 'Correct option';
    }

    const matchedTexts: string[] = [];
    rawAnswers.forEach(ans => {
      if (!ans) return;
      const normLetter = normalizeOptionAnswer(ans, qItem.options);
      if (normLetter && /^[A-Z]$/.test(normLetter)) {
        const idx = normLetter.charCodeAt(0) - 65;
        if (idx >= 0 && idx < qItem.options.length) {
          const opt = qItem.options[idx];
          const text = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
          matchedTexts.push(`(${normLetter}) ${stripOptionLabel(text)}`);
          return;
        }
      }
      const match = qItem.options.find((o: any) => isOptionMatch(o, ans));
      if (match) {
        const idx = qItem.options.indexOf(match);
        const code = String.fromCharCode(65 + idx);
        const text = typeof match === 'object' ? (match.text || match.value) : String(match);
        matchedTexts.push(`(${code}) ${stripOptionLabel(text)}`);
      } else {
        matchedTexts.push(String(ans));
      }
    });

    if (matchedTexts.length > 0) {
      return Array.from(new Set(matchedTexts)).join(', ');
    }

    const correctOpts = qItem.options.filter((o: any) => o && typeof o === 'object' && (o.isCorrect || o.correct));
    if (correctOpts.length > 0) {
      return correctOpts.map((o: any) => {
        const idx = qItem.options.indexOf(o);
        const code = String.fromCharCode(65 + idx);
        return `(${code}) ${stripOptionLabel(o.text || o.value)}`;
      }).join(', ');
    }

    return 'Correct option';
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {!isWindowFocused && started && !finished && (
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
            padding: '30px',
            maxWidth: '400px',
            width: '100%',
            textAlign: 'center',
            boxShadow: 'var(--shadow-xl)',
            display: 'flex',
            flexDirection: 'column',
            gap: '16px'
          }}>
            <div style={{ fontSize: '50px' }}>⚠️</div>
            <h3 style={{ fontSize: '18px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
              Window Focus Lost!
            </h3>
            <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0, lineHeight: 1.4 }}>
              Proctoring active. You switched tabs, left the window, or opened another app in split screen.
            </p>
            <p style={{ fontSize: '12px', color: 'var(--warning)', fontWeight: 700, margin: 0 }}>
              Please click/tap here to return to focus.
            </p>
          </div>
        </div>
      )}
      {/* Script Injections for MediaPipe (Lazy loaded when modal is open) */}
      {cameraModalOpen && (
        <>
          <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
          <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />
        </>
      )}


      {/* Camera permission modal */}
      {!showUnlockModal && cameraModalOpen && (
        <div className="camera-modal" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'flex-start', justifyContent: 'center', padding: '40px 20px', overflowY: 'auto' }}>
          <div className="camera-modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius)', padding: '30px', maxWidth: '500px', width: '90%', textAlign: 'center', boxShadow: 'var(--shadow-lg)', margin: '0 auto' }}>
            <h2>System Hardware Pre-Check</h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '10px 0 16px' }}>Verify your camera and microphone are working correctly before starting this proctored practice session.</p>

            {/* Topic Blueprint & Slab Transparency Card */}
            {data && (
              <div style={{
                background: 'var(--bg-soft)',
                border: '1.5px solid var(--border-light)',
                borderRadius: 'var(--radius-sm)',
                padding: '12px 14px',
                textAlign: 'left',
                marginBottom: '16px'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '8px', marginBottom: '8px', flexWrap: 'wrap' }}>
                  <div style={{ fontWeight: 800, fontSize: '13px', color: 'var(--text)' }}>
                    📍 {data.topicName || data.topicCode}
                  </div>
                  <span style={{
                    fontSize: '10px',
                    fontWeight: 700,
                    textTransform: 'uppercase',
                    padding: '2px 8px',
                    borderRadius: '4px',
                    background: (data.topicScope === 'minor' || data.topicClassification === 'minor' || data.topicClassification === 'micro') ? 'var(--success-bg)' : (data.topicScope === 'major' || data.topicClassification === 'major' || data.topicClassification === 'calculative' || data.topicClassification === 'hots') ? 'var(--danger-bg)' : 'var(--info-bg)',
                    color: (data.topicScope === 'minor' || data.topicClassification === 'minor' || data.topicClassification === 'micro') ? 'var(--success)' : (data.topicScope === 'major' || data.topicClassification === 'major' || data.topicClassification === 'calculative' || data.topicClassification === 'hots') ? 'var(--danger)' : 'var(--info)',
                    border: `1px solid ${(data.topicScope === 'minor' || data.topicClassification === 'minor' || data.topicClassification === 'micro') ? 'rgba(52, 211, 153, 0.3)' : (data.topicScope === 'major' || data.topicClassification === 'major' || data.topicClassification === 'calculative' || data.topicClassification === 'hots') ? 'rgba(248, 113, 113, 0.3)' : 'rgba(56, 189, 248, 0.3)'}`
                  }}>
                    {(data.topicScope === 'minor' || data.topicClassification === 'minor' || data.topicClassification === 'micro') && '📘 Minor (6 Qs to Master • Max 2 Sets)'}
                    {(data.topicScope === 'medium' || data.topicClassification === 'medium' || data.topicClassification === 'moderate' || data.topicClassification === 'conceptual') && '📙 Medium (10 Qs to Master • Max 3 Sets)'}
                    {(data.topicScope === 'major' || data.topicClassification === 'major' || data.topicClassification === 'calculative' || data.topicClassification === 'hots') && '📕 Major (15 Qs to Master • Max 3 Sets)'}
                    {!data.topicScope && !data.topicClassification && '📙 Standard (10 Qs to Master • Max 3 Sets)'}
                  </span>
                </div>

                {/* Progress bar towards Required Slab */}
                <div style={{ marginBottom: '8px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>
                    <span>Confidence Progress (Score ≥ 90% Needed)</span>
                    <strong>{data.totalAttemptedCount || 0} / {data.requiredConfidence || (data.topicScope === 'minor' ? 6 : data.topicScope === 'major' ? 15 : 10)} Qs Practiced</strong>
                  </div>
                  <div style={{ height: '6px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                    <div style={{
                      height: '100%',
                      background: 'var(--accent)',
                      width: `${Math.min(100, Math.round(((data.totalAttemptedCount || 0) / Math.max(1, data.requiredConfidence || (data.topicScope === 'minor' ? 6 : data.topicScope === 'major' ? 15 : 10))) * 100))}%`,
                      transition: 'width 0.3s ease'
                    }}></div>
                  </div>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', fontSize: '11px', color: 'var(--text-muted)' }}>
                  <div>🎯 <strong>This Set:</strong> {data.questions?.length || 6} Questions</div>
                  <div>⏳ <strong>Ideal Time:</strong> {Math.round((data.idealTimeSeconds || 450) / 60)} Mins</div>
                  <div>📈 <strong>Current Mastery:</strong> {data.masteryAtStart || 0}%</div>
                  <div>🛡️ <strong>Pacing:</strong> Set {(data.dailySessions || 0) + 1} of {data.maxSessionsAllowed || (data.topicScope === 'minor' ? 2 : 3)}</div>
                </div>

                <div style={{ fontSize: '10.5px', color: 'var(--accent)', marginTop: '8px', fontWeight: 600, borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                  🔒 Dedicated Practice Vault (0% Exam Leakage) • Score ≥90% & reach slab to earn Mastered!
                </div>
              </div>
            )}

            <div className="camera-preview" style={{ width: '100%', height: '240px', background: 'var(--bg-card)', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative', marginBottom: '15px' }}>
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
                <div style={{ color: 'var(--text-muted)' }}>Webcam Feed Offline</div>
              )}
            </div>

            {cameraStream && (
              <div style={{ margin: '15px 0 10px', textAlign: 'left' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                  <span>🎙️ Microphone Input detection</span>
                  <strong>{audioLevel > 0 ? `${audioLevel}%` : 'Silent'}</strong>
                </div>
                <div style={{ height: '8px', background: 'var(--bg-soft)', borderRadius: '4px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', background: 'var(--success)', width: `${audioLevel}%`, transition: 'width 0.1s ease' }}></div>
                </div>
              </div>
            )}

            {cameraStatus && <div className="status-msg" style={{ display: 'block', margin: '10px 0', fontSize: '12px', color: 'var(--text-muted)' }}>{cameraStatus}</div>}
            
            {!cameraStream ? (
              <button className="btn btn-primary" onClick={handleRunCheck} style={{ width: '100%' }}>
                Test Camera & Microphone
              </button>
            ) : (
              <button className="btn btn-success" onClick={handleProceedToExam} style={{ width: '100%' }}>
                Start Practice / Proceed
              </button>
            )}
          </div>
        </div>
      )}
      {/* Champion Challenge selection modal overlay */}
      {showUnlockModal && (
        <div className="camera-modal" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="camera-modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius)', padding: '30px', maxWidth: '500px', width: '90%', textAlign: 'center', boxShadow: 'var(--shadow-lg)', margin: '0 auto' }}>
            <div style={{ fontSize: '3rem', marginBottom: '15px' }}>🏆</div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--text)', marginBottom: '10px' }}>Champion Challenge Unlocked!</h2>
            <p style={{ fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
              Champion Challenge Unlocked! You have mastered the core concepts of this topic with a score of <strong style={{ color: 'var(--accent)' }}>{data?.masteryAtStart}%</strong>! Ready to test your skills at higher levels?
            </p>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '24px', textAlign: 'left' }}>
              <div 
                onClick={() => setExamCategory('standard')}
                style={{ 
                  padding: '12px 16px', 
                  borderRadius: 'var(--radius-sm)', 
                  border: `2px solid ${examCategory === 'standard' ? 'var(--accent)' : 'var(--border-light)'}`, 
                  background: examCategory === 'standard' ? 'var(--accent-soft)' : 'var(--bg-soft)', 
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                  <span style={{ fontSize: '1.2rem' }}>📘</span>
                  <h4 style={{ margin: 0, fontWeight: 700, fontSize: '13px' }}>Standard Syllabus</h4>
                </div>
                <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: 0, lineHeight: '1.4' }}>
                  Practice core textbook-level questions to maintain concept clarity and board preparation.
                </p>
              </div>

              <div 
                onClick={() => setExamCategory('foundation')}
                style={{ 
                  padding: '12px 16px', 
                  borderRadius: 'var(--radius-sm)', 
                  border: `2px solid ${examCategory === 'foundation' ? 'var(--accent)' : 'var(--border-light)'}`, 
                  background: examCategory === 'foundation' ? 'var(--accent-soft)' : 'var(--bg-soft)', 
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                  <span style={{ fontSize: '1.2rem' }}>🚀</span>
                  <h4 style={{ margin: 0, fontWeight: 700, fontSize: '13px' }}>Champion Mode</h4>
                </div>
                <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: 0, lineHeight: '1.4' }}>
                  Challenge yourself with advanced foundation & logical problems. Damped mastery drop on wrong answers!
                </p>
              </div>
            </div>

            <button 
              className="btn btn-primary" 
              onClick={handleProceedFromUnlock}
              style={{ width: '100%', padding: '10px', borderRadius: '30px', fontWeight: 700 }}
            >
              Confirm &amp; Proceed
            </button>
          </div>
        </div>
      )}

      {/* Proctoring Bar */}
      <div className="proctor-bar" style={{ display: (started && !finished) ? 'block' : 'none', background: 'var(--surface)', color: 'var(--text)', padding: '8px 20px', borderBottom: '2px solid var(--warning)' }}>
        <div className="proctor-top-row" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
          <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '10px', position: 'relative', flexShrink: 0 }}>
             <video ref={videoRef} autoPlay playsInline muted style={{ width: '100px', height: '75px', borderRadius: 'var(--radius-sm)', border: '2px solid var(--success)', background: 'var(--bg-card)', objectFit: 'cover' }}></video>
            <div>
              <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Integrity Status:</div>
              <span className="badge badge-success" style={{ marginTop: '4px', fontSize: '9px', background: 'var(--success)' }}>
                Active Proctoring
              </span>
            </div>
          </div>

          <div className="violation-stats" style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center', flex: 1 }}>
            <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
              🚫 Tabs: {tabViolations}
            </div>
            <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
              👤 Away: {noFaceCount}
            </div>
            <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
              👁️ Gaze: {lookingAwayCount}
            </div>
          </div>

          <div className="proctor-timer" style={{ display: 'flex', gap: '20px', fontSize: '13px', fontWeight: 600 }}>
            <div>⏱️ Total: {formatTime(totalSeconds)}</div>
            <div>❓ Q: {formatTime(currentQSeconds)}</div>
          </div>
        </div>
      </div>

      {/* Main Practice Container */}
      {started && !finished && (
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', maxWidth: '800px', width: '100%', margin: '0 auto', padding: '24px 12px' }}>
          {/* Progress Indicator */}
          <div style={{ display: 'flex', gap: '6px', marginBottom: '20px' }}>
            {data.questions.map((_, idx) => {
              const isCurrent = idx === currentQIndex;
              const isSubmitted = submittedAnswers[idx];
              const isCorrect = questionResults[idx];
              let barColor = 'var(--border-light)';
              if (isCurrent) {
                barColor = 'var(--accent)';
              } else if (isSubmitted) {
                barColor = isCorrect === true ? 'var(--success)' : 'var(--danger)';
              }
              return (
                <div 
                  key={idx} 
                  onClick={() => !isQSubmitted && setCurrentQIndex(idx)}
                  style={{
                    flex: 1, 
                    height: '8px', 
                    borderRadius: '4px',
                    background: barColor,
                    cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                    transition: 'all 0.3s ease',
                    boxShadow: isCurrent ? '0 0 6px rgba(99, 102, 241, 0.5)' : 'none'
                  }}
                  title={`Question ${idx + 1}: ${isSubmitted ? (isCorrect ? 'Correct (✓)' : 'Incorrect (✗)') : 'Pending'}`}
                />
              );
            })}
          </div>

          {/* Question View */}
          <div className="card" ref={questionContainerRef} style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <span className="badge badge-info" style={{ textTransform: 'uppercase', fontSize: '10px' }}>
                  Q {currentQIndex + 1} of {data.questions.length}
                </span>
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                  <span className="badge badge-secondary" style={{ textTransform: 'uppercase', fontSize: '10px' }}>{q.difficulty} • {q.bloomLevel}</span>
                  {!isQSubmitted && !disputedQuestionIds.has(q.id) && (
                    <button
                      type="button"
                      onClick={() => setReportModalOpen(true)}
                      style={{
                        background: 'transparent',
                        border: '1px solid var(--danger)',
                        color: 'var(--danger)',
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
                  {disputedQuestionIds.has(q.id) && (
                    <span style={{ fontSize: '10.5px', color: 'var(--warning)', fontWeight: 'bold' }}>
                      ⚠️ Bypassed
                    </span>
                  )}
                </div>
              </div>

              {(() => {
                if (isAssertionReasonType(q.type)) {
                  const { assertion, reason } = extractAssertionAndReason(q);
                  return (
                    <div className="assertion-reason-container" style={{ margin: '15px 0' }}>
                      <div style={{ background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius-sm)', marginBottom: '10px' }}>
                        <strong>Assertion (A):</strong>
                        <p className="math-container" style={{ marginTop: '4px', fontSize: '14px' }}>{preprocessMathText(assertion)}</p>
                      </div>
                      <div style={{ background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius-sm)' }}>
                        <strong>Reason (R):</strong>
                        <p className="math-container" style={{ marginTop: '4px', fontSize: '14px' }}>{preprocessMathText(reason)}</p>
                      </div>
                    </div>
                  );
                }
                return (
                  <h3 className="math-container" style={{ fontSize: '16px', fontWeight: 700, margin: '15px 0 20px', lineHeight: '1.5' }}>{preprocessMathText(q.text || '')}</h3>
                );
              })()}

              {/* Options Selector Layout */}
              <div className="options-container" style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '16px' }}>
                {/* 1. Multiple MCQ */}
                {isMultipleChoiceType(q.type) && Array.isArray(q.options) && q.options.length > 0 && (
                  q.options.map((opt: any, oIdx: number) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    let isChecked = false;
                    try { isChecked = JSON.parse(uAns || '[]').includes(letter); } catch {}
                    const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
                    const correctList = Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0
                      ? q.correctAnswers
                      : parseAnswerList(q.correctAnswer);
                    const correctLetters = correctList.map((c: any) => normalizeOptionAnswer(c, q.options));
                    const isThisCorrect = correctLetters.includes(letter);

                    let itemBorder = isChecked ? '2px solid var(--accent)' : '1px solid var(--border-light)';
                    let itemBg = isChecked ? 'var(--accent-light)' : 'var(--surface)';
                    let badge = null;

                    if (isQSubmitted) {
                      if (isChecked) {
                        if (isThisCorrect) {
                          itemBorder = '2px solid var(--success)';
                          itemBg = 'rgba(16, 185, 129, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                        } else {
                          itemBorder = '2px solid var(--danger)';
                          itemBg = 'rgba(239, 68, 68, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                        }
                      } else if (isThisCorrect) {
                        itemBorder = '2px dashed var(--success)';
                        itemBg = 'rgba(16, 185, 129, 0.06)';
                        badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                      }
                    }

                    return (
                      <div 
                        key={`${q.id}-${oIdx}`} 
                        onClick={() => !isQSubmitted && handleCheckboxChange(letter)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-sm)',
                          border: itemBorder,
                          background: itemBg,
                          cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                          transition: 'border 0.15s, background 0.15s'
                        }}
                      >
                        <input 
                          type="checkbox" 
                          checked={isChecked}
                          onChange={() => {}}
                          disabled={isQSubmitted}
                        />
                        <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                          <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                        </div>
                        {badge}
                      </div>
                    );
                  })
                )}

                {/* 2. True/False */}
                {isTrueFalseType(q.type) && (
                  ['True', 'False'].map((val) => {
                    const selected = uAns.toLowerCase() === val.toLowerCase();
                    const correctVal = String(q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : '')).trim().toLowerCase();
                    const isThisCorrect = val.toLowerCase() === correctVal;

                    let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
                    let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
                    let badge = null;

                    if (isQSubmitted) {
                      if (selected) {
                        if (isThisCorrect) {
                          itemBorder = '2px solid var(--success)';
                          itemBg = 'rgba(16, 185, 129, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                        } else {
                          itemBorder = '2px solid var(--danger)';
                          itemBg = 'rgba(239, 68, 68, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                        }
                      } else if (isThisCorrect) {
                        itemBorder = '2px dashed var(--success)';
                        itemBg = 'rgba(16, 185, 129, 0.06)';
                        badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                      }
                    }

                    return (
                      <div 
                        key={`${q.id}-${val}`} 
                        onClick={() => !isQSubmitted && handleRadioChange(val)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-sm)',
                          border: itemBorder,
                          background: itemBg,
                          cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                          transition: 'border 0.15s, background 0.15s'
                        }}
                      >
                        <input 
                          type="radio" 
                          name={`q-${currentQIndex}`} 
                          checked={selected}
                          onChange={() => {}}
                          disabled={isQSubmitted}
                        />
                        <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>{val}</div>
                        {badge}
                      </div>
                    );
                  })
                )}

                {/* 3. Assertion & Reason */}
                {isAssertionReasonType(q.type) && (() => {
                  const defaultArOptions = [
                    { code: 'A', text: 'Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).' },
                    { code: 'B', text: 'Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).' },
                    { code: 'C', text: 'Assertion (A) is true, but Reason (R) is false.' },
                    { code: 'D', text: 'Assertion (A) is false, but Reason (R) is true.' }
                  ];

                  let optionsToRender = defaultArOptions;
                  if (Array.isArray(q.options) && q.options.length > 0) {
                    optionsToRender = q.options.map((opt: any, oIdx: number) => {
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

                  const rawCorrect = q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : '');
                  const correctCode = (typeof rawCorrect === 'string' && rawCorrect.length === 1 && /[A-D]/i.test(rawCorrect))
                    ? rawCorrect.toUpperCase()
                    : 'A';

                  return optionsToRender.map((opt: any) => {
                    const code = opt.code;
                    const selected = uAns === code;
                    const optionText = opt.text;
                    const isThisCorrect = code.toUpperCase() === correctCode;

                    let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
                    let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
                    let badge = null;

                    if (isQSubmitted) {
                      if (selected) {
                        if (isThisCorrect) {
                          itemBorder = '2px solid var(--success)';
                          itemBg = 'rgba(16, 185, 129, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                        } else {
                          itemBorder = '2px solid var(--danger)';
                          itemBg = 'rgba(239, 68, 68, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                        }
                      } else if (isThisCorrect) {
                        itemBorder = '2px dashed var(--success)';
                        itemBg = 'rgba(16, 185, 129, 0.06)';
                        badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                      }
                    }

                    return (
                      <div 
                        key={`${q.id}-${code}`} 
                        onClick={() => !isQSubmitted && handleRadioChange(code)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-sm)',
                          border: itemBorder,
                          background: itemBg,
                          cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                          transition: 'border 0.15s, background 0.15s'
                        }}
                      >
                        <input 
                          type="radio" 
                          name={`q-${currentQIndex}`} 
                          checked={selected}
                          onChange={() => {}}
                          disabled={isQSubmitted}
                        />
                        <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                          <strong>{code}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                        </div>
                        {badge}
                      </div>
                    );
                  });
                })()}

                {/* 4. Single MCQ / Any Question Type with Options (including Numerical MCQ) */}
                {!isMultipleChoiceType(q.type) && !isTrueFalseType(q.type) && !isAssertionReasonType(q.type) && Array.isArray(q.options) && q.options.length > 0 && (
                  q.options.map((opt: any, oIdx: number) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    const selected = uAns === letter;
                    const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
                    const resolvedCorrect = q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : '');
                    const isThisCorrect = normalizeOptionAnswer(letter, q.options) === normalizeOptionAnswer(resolvedCorrect, q.options);

                    let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
                    let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
                    let badge = null;

                    if (isQSubmitted) {
                      if (selected) {
                        if (isThisCorrect) {
                          itemBorder = '2px solid var(--success)';
                          itemBg = 'rgba(16, 185, 129, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                        } else {
                          itemBorder = '2px solid var(--danger)';
                          itemBg = 'rgba(239, 68, 68, 0.12)';
                          badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                        }
                      } else if (isThisCorrect) {
                        itemBorder = '2px dashed var(--success)';
                        itemBg = 'rgba(16, 185, 129, 0.06)';
                        badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                      }
                    }

                    return (
                      <div 
                        key={`${q.id}-${oIdx}`} 
                        onClick={() => !isQSubmitted && handleRadioChange(letter)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-sm)',
                          border: itemBorder,
                          background: itemBg,
                          cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                          transition: 'border 0.15s, background 0.15s'
                        }}
                      >
                        <input 
                          type="radio" 
                          name={`q-${currentQIndex}`} 
                          checked={selected}
                          onChange={() => {}}
                          disabled={isQSubmitted}
                        />
                        <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                          <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                        </div>
                        {badge}
                      </div>
                    );
                  })
                )}

                {/* 5. Direct Numerical Input (when no options provided) */}
                {isNumericalType(q.type) && (!Array.isArray(q.options) || q.options.length === 0) && (
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Numerical Value:</label>
                    <input 
                      type="number" 
                      value={uAns}
                      onChange={(e) => {
                        if (isQSubmitted) return;
                        const updated = [...userAnswers];
                        updated[currentQIndex] = e.target.value;
                        setUserAnswers(updated);
                      }}
                      disabled={isQSubmitted}
                      placeholder="Enter numerical answer..."
                      style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
                    />
                  </div>
                )}

                {/* 6. Fill in the Blanks Input (when no options provided) */}
                {isFillBlanksType(q.type) && (!Array.isArray(q.options) || q.options.length === 0) && (
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Missing Word:</label>
                    <input 
                      type="text" 
                      value={uAns}
                      onChange={(e) => {
                        if (isQSubmitted) return;
                        const updated = [...userAnswers];
                        updated[currentQIndex] = e.target.value;
                        setUserAnswers(updated);
                      }}
                      disabled={isQSubmitted}
                      placeholder="Type your answer here..."
                      style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
                    />
                  </div>
                )}

                {/* 7. General Text Input Fallback (for any question with missing options) */}
                {!isTrueFalseType(q.type) && !isAssertionReasonType(q.type) && !isNumericalType(q.type) && !isFillBlanksType(q.type) && (!Array.isArray(q.options) || q.options.length === 0) && (
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Your Answer:</label>
                    <input 
                      type="text" 
                      value={uAns}
                      onChange={(e) => {
                        if (isQSubmitted) return;
                        const updated = [...userAnswers];
                        updated[currentQIndex] = e.target.value;
                        setUserAnswers(updated);
                      }}
                      disabled={isQSubmitted}
                      placeholder="Type your answer or option..."
                      style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
                    />
                  </div>
                )}
              </div>
            </div>

            {/* Navigation buttons */}
            <div style={{ display: 'flex', justifyContent: 'space-between', gap: '15px', marginTop: '30px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => currentQIndex > 0 && setCurrentQIndex(currentQIndex - 1)}
                disabled={currentQIndex === 0 || isQSubmitted}
                style={{ width: '100px' }}
              >
                ← Back
              </button>

              {!isQSubmitted ? (
                <button 
                  className="btn btn-primary" 
                  onClick={handleSubmitQuestion}
                  disabled={!uAns}
                  style={{ width: '160px' }}
                >
                  Submit & Check
                </button>
              ) : (
                <button 
                  className="btn btn-primary" 
                  onClick={handleNext}
                  disabled={isSubmittingPractice || (!feedbackCorrect && explanationTimer > 0)}
                  style={{ width: '160px' }}
                >
                  {isSubmittingPractice
                    ? 'Submitting...'
                    : (!feedbackCorrect && explanationTimer > 0 
                      ? `Wait (${explanationTimer}s)` 
                      : (currentQIndex === data.questions.length - 1 ? 'Finish Set →' : 'Next Question →'))}
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Immediate Corrective Feedback Modal Dialog */}
      {feedbackOpen && (
        <div className="feedback-modal" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', padding: '32px 28px', maxWidth: '640px', width: '92%', borderTop: `6px solid ${feedbackCorrect ? 'var(--success)' : 'var(--danger)'}`, boxShadow: 'var(--shadow-lg)' }}>
            <h2 style={{ color: feedbackCorrect ? 'var(--success)' : 'var(--danger)', fontSize: '2rem', fontWeight: 800, margin: '0 0 16px 0' }}>
              {feedbackCorrect ? '🎉 Correct!' : '❌ Incorrect'}
            </h2>
            <div style={{ margin: '16px 0 24px 0', fontSize: '15px', color: 'var(--text)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {!feedbackCorrect && (
                <div style={{ background: 'rgba(239, 68, 68, 0.08)', padding: '14px 18px', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(239, 68, 68, 0.2)' }}>
                  <strong style={{ color: 'var(--danger)', fontSize: '16px' }}>Correct Answer: </strong>
                  <span className="math-container" style={{ fontWeight: 700, fontSize: '16px' }}>{getCorrectOptionText(q)}</span>
                </div>
              )}
              {!feedbackCorrect && (
                <div style={{ background: 'var(--bg-soft)', padding: '16px 18px', borderRadius: 'var(--radius-sm)', overflowY: 'auto', maxHeight: '260px', border: '1px solid var(--border-light)', textAlign: 'left' }}>
                  <strong style={{ color: 'var(--accent)', display: 'block', marginBottom: '8px', fontSize: '15px' }}>💡 Detailed Explanation & Solution:</strong>
                  <div className="math-container" style={{ lineHeight: '1.6', fontSize: '14.5px', color: 'var(--text)' }}>
                    {q.solution || (q as any).explanation ? (
                      preprocessMathText(q.solution || (q as any).explanation)
                    ) : (
                      <span>Analyze the key concepts: The correct choice is <strong>{getCorrectOptionText(q)}</strong>. Review topic definitions and core principles to reinforce this concept.</span>
                    )}
                  </div>
                </div>
              )}
              {feedbackCorrect && (
                <div style={{ background: 'rgba(16, 185, 129, 0.08)', padding: '18px 20px', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(16, 185, 129, 0.2)' }}>
                  <p style={{ margin: 0, fontWeight: 700, fontSize: '16px', color: 'var(--success)' }}>🎉 Well done! You evaluated this statement correctly.</p>
                  {(q.solution || (q as any).explanation) && (
                    <div className="math-container" style={{ marginTop: '12px', fontSize: '14.5px', lineHeight: '1.6', color: 'var(--text)', textAlign: 'left' }}>
                      <strong style={{ color: 'var(--text-muted)' }}>Solution Note:</strong> {preprocessMathText(q.solution || (q as any).explanation)}
                    </div>
                  )}
                </div>
              )}
            </div>
            <button 
              className="btn btn-primary" 
              onClick={handleNext} 
              disabled={isSubmittingPractice || (!feedbackCorrect && explanationTimer > 0)}
              style={{ width: '100%', padding: '14px', fontSize: '16px', fontWeight: 800, borderRadius: 'var(--radius-sm)' }}
            >
              {isSubmittingPractice
                ? 'Submitting Practice...'
                : (feedbackCorrect 
                  ? 'Continue →' 
                  : (explanationTimer > 0 ? `Read Explanation (${explanationTimer}s)` : '✓ I Understand'))}
            </button>
          </div>
        </div>
      )}

      {/* Report Question Issue Modal */}
      {reportModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 25000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', padding: '24px', maxWidth: '480px', width: '100%', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              🚩 Report Question &amp; Skip
            </h3>
            <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.4', marginBottom: '16px' }}>
              If there is an error with this question (missing options, broken symbols, incomplete text), you can report it. An automated screenshot proof will be sent to your teacher, and this question will be <strong>excluded from your score and mastery calculations with zero penalty</strong>.
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
                style={{ flex: 1, background: 'var(--danger)', borderColor: 'var(--danger)' }}
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

export default function StudentTopicPractice() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading practice...
        </div>
      </div>
    }>
      <TopicPracticeContent />
    </Suspense>
  );
}
