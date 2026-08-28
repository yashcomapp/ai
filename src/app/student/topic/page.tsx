'use client';

import React, { useEffect, useState, useRef, useCallback, Suspense, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { t } from '@/lib/i18n';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { normalizeOptionAnswer, preprocessMathText, evaluateQuestionAnswer, stripOptionLabel, extractAssertionAndReason } from '@/lib/questionTypes';
import { useMathRender } from '@/hooks/useMathRender';
import { usePractice } from '@/hooks/usePractice';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';
import { useLiveExam } from '@/hooks/useLiveExam';
import { formatDuration } from '@/lib/dateUtils';

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
  totalQuestions: number;
  questions: QuestionItem[];
  masteryAtStart: number;
  idealTimeSeconds: number;
}

function TopicPracticeContent() {
  const { startSession, submitGrading } = usePractice();
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
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
  const [lockType, setLockType] = useState<'initial' | 'cooldown' | 'daily' | null>(null);
  const [showRecoveryPrompt, setShowRecoveryPrompt] = useState(false);
  const [recoveryMessage, setRecoveryMessage] = useState('');

  // Setup practice status
  const [started, setStarted] = useState(false);
  const [finished, setFinished] = useState(false);
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [sessionId] = useState(() => `sess_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
  const [userAnswers, setUserAnswers] = useState<string[]>([]);
  const [submittedAnswers, setSubmittedAnswers] = useState<boolean[]>([]);
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
      const canvas = await w.html2canvas(element, { scale: 1.5, useCORS: true, backgroundColor: '#222730' });
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
    if (!firebaseUser || !topicCode) return;
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
  useMathRender([currentQIndex, started, finished, data, feedbackOpen, isMounted]);

  // Graded results after complete submit
  const [finalResult, setFinalResult] = useState<{
    score: number;
    totalQuestions: number;
    mastery: number;
    confidence: number;
    questions: any[];
  } | null>(null);

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
  const finishedRef = useRef(false);


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



  // Tab switching & split-screen focus proctoring
  useEffect(() => {
    if (!started || finished) return;

    const handleVisibilityChange = () => {
      if (startTimeRef.current && Date.now() - startTimeRef.current < 5000) {
        return;
      }
      if (document.hidden) {
        setTabViolations(prev => prev + 1);
        lastActiveRef.current = Date.now();
      } else {
        const awayMs = Date.now() - lastActiveRef.current;
        setTotalAwaySeconds(prev => prev + Math.round(awayMs / 1000));
      }
    };

    const handleBlur = () => {
      if (startTimeRef.current && Date.now() - startTimeRef.current < 5000) {
        return;
      }
      setIsWindowFocused(false);
      setTabViolations(prev => prev + 1);
    };

    const handleFocus = () => {
      setIsWindowFocused(true);
      const awayMs = Date.now() - lastActiveRef.current;
      setTotalAwaySeconds(prev => prev + Math.round(awayMs / 1000));
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('blur', handleBlur);
    window.addEventListener('focus', handleFocus);

    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('blur', handleBlur);
      window.removeEventListener('focus', handleFocus);
    };
  }, [started, finished]);

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

    const isCorrect = evaluateQuestionAnswer(
      q.type || 'single_mcq',
      answer,
      q.correctAnswer || q.correctAnswers || '',
      q.options
    );

    setFeedbackCorrect(isCorrect);
    setFeedbackOpen(true);

    const submitted = [...submittedAnswers];
    submitted[currentQIndex] = true;
    setSubmittedAnswers(submitted);

    if (!isCorrect) {
      setExplanationTimer(30);
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
    if (!firebaseUser || !data) return;
    setLoading(true);
    stopWebcam();

    try {
      const formattedAnswers = data.questions.map((q, idx) => ({
        questionId: q.id,
        answer: userAnswers[idx] || ''
      }));

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
          <div style={{ fontSize: '3.5rem', marginBottom: '16px' }}>🩺</div>
          <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '12px' }}>
            Guided Recovery Diagnostic / उपचारात्मक निदान
          </h3>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
            {recoveryMessage || "You have completed extensive practice on this topic. Take the Guided Recovery Diagnostic (8 targeted questions) to strengthen core concepts and achieve Mastery."}
          </p>
          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Dashboard
            </button>
            <button 
              className="btn btn-primary" 
              onClick={() => {
                setShowRecoveryPrompt(false);
                setLoading(true);
                router.push(`/student/topic?topicCode=${topicCode}&category=${category}&mode=recovery`);
              }}
              style={{ flex: 1, fontWeight: 700 }}
            >
              🚀 Start Diagnostic (8 Qs)
            </button>
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
          <h2 style={{ fontSize: '1.6rem', marginBottom: '15px' }}>{isFullyMastered ? '🏆 Topic Mastered' : 'No Questions'}</h2>
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

    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px', background: 'var(--bg)' }}>
        <div className="card results-card" style={{ maxWidth: '600px', width: '100%', textAlign: 'center', padding: '30px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)' }}>
          <h2 style={{ fontSize: '1.8rem', marginBottom: '20px' }}>🏆 Practice Complete!</h2>
          <div className="score-big" style={{ fontSize: '4rem', fontWeight: 800, color: 'var(--accent)', margin: '15px 0' }}>
            {finalResult.score}/{finalResult.totalQuestions}
          </div>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{Math.round((finalResult.score / finalResult.totalQuestions) * 100)}%</p>
          <p style={{ margin: '10px 0', fontSize: '14px' }}>
            Mastery: {data.masteryAtStart}% → {finalResult.mastery}% ({masteryChange >= 0 ? `+${masteryChange}` : masteryChange}%)
          </p>
          <p style={{ margin: '5px 0', fontSize: '13px', color: 'var(--text-muted)' }}>
            ⏱️ Time: {formatTime(totalSeconds)} / Ideal: {formatTime(data.idealTimeSeconds)} ({efficiency}% efficiency)
          </p>

          <div style={{ background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '15px', margin: '20px 0', textAlign: 'left' }}>
            <div className={`integrity-level`} style={{ fontWeight: 'bold', fontSize: '14px', marginBottom: '8px' }}>{integrity.text}</div>
            {integrity.level !== 'green' && (
              <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                {tabViolations > 0 && <p>• Tab switches: {tabViolations} times</p>}
                {totalAwaySeconds > 0 && <p>• Time away: {formatTime(totalAwaySeconds)} ({percentTimeAway}% of total)</p>}
                {noFaceCount > 0 && <p>• Face not detected: {noFaceCount} checks</p>}
                {lookingAwayCount > 0 && <p>• Gaze violations: {lookingAwayCount} checks</p>}
              </div>
            )}
          </div>

          <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', marginTop: '20px' }}>
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
    const cAnswer = (qItem as any).correctAnswer || '';
    const cAnswers = (qItem as any).correctAnswers || [];

    if (!qItem.options || qItem.options.length === 0) {
      return String(cAnswer || cAnswers.join(', ') || 'Correct option');
    }
    
    const correctOptObj = qItem.options.find((o: any) => o && typeof o === 'object' && (o.isCorrect || o.correct));
    if (correctOptObj) {
      return correctOptObj.text || correctOptObj.value || 'Correct option';
    }
    
    if (cAnswer) {
      // Find matching option by text, value, or index code
      const match = qItem.options.find((o: any, idx: number) => {
        const text = typeof o === 'object' && o ? (o.text || o.value || '') : String(o);
        const code = String.fromCharCode(65 + idx);
        return text === cAnswer || code === cAnswer || normalizeOptionAnswer(text, qItem.options) === normalizeOptionAnswer(cAnswer, qItem.options);
      });
      if (match) {
        const matchText = typeof match === 'object' ? (match.text || match.value) : String(match);
        const idx = qItem.options.indexOf(match);
        const code = String.fromCharCode(65 + idx);
        return `(${code}) ${stripOptionLabel(matchText)}`;
      }
    }
    
    if (cAnswers.length > 0) {
      const matches = qItem.options.filter((o: any, idx: number) => {
        const text = typeof o === 'object' && o ? (o.text || o.value || '') : String(o);
        const code = String.fromCharCode(65 + idx);
        return cAnswers.includes(text) || cAnswers.includes(code) || cAnswers.some((ca: any) => normalizeOptionAnswer(text, qItem.options) === normalizeOptionAnswer(ca, qItem.options));
      });
      if (matches.length > 0) {
        return matches.map((m: any) => {
          const mText = typeof m === 'object' ? (m.text || m.value) : String(m);
          const idx = qItem.options.indexOf(m);
          const code = String.fromCharCode(65 + idx);
          return `(${code}) ${stripOptionLabel(mText)}`;
        }).join(', ');
      }
    }

    return String(cAnswer || cAnswers.join(', ') || 'Correct option');
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
            <h2>⚙️ System Hardware Pre-Check</h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '10px 0 20px' }}>Verify your camera and microphone are working correctly before starting this proctored practice session.</p>
            
            <div className="camera-preview" style={{ width: '100%', height: '240px', background: '#111', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative', marginBottom: '15px' }}>
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
      <div className="proctor-bar" style={{ display: (started && !finished) ? 'block' : 'none', background: '#1a1d29', color: 'white', padding: '8px 20px', borderBottom: '2px solid var(--warning)' }}>
        <div className="proctor-top-row" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
          <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '10px', position: 'relative', flexShrink: 0 }}>
             <video ref={videoRef} autoPlay playsInline muted style={{ width: '100px', height: '75px', borderRadius: 'var(--radius-sm)', border: '2px solid var(--success)', background: '#111', objectFit: 'cover' }}></video>
            <div>
              <div style={{ fontSize: '10px', color: '#999' }}>Integrity Status:</div>
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
          <div style={{ display: 'flex', gap: '4px', marginBottom: '20px' }}>
            {data.questions.map((_, idx) => (
              <div 
                key={idx} 
                onClick={() => !isQSubmitted && setCurrentQIndex(idx)}
                style={{
                  flex: 1, 
                  height: '6px', 
                  borderRadius: '3px',
                  background: idx === currentQIndex ? 'var(--accent)' : (submittedAnswers[idx] ? 'var(--success)' : 'var(--border-light)'),
                  cursor: isQSubmitted ? 'not-allowed' : 'pointer'
                }}
              />
            ))}
          </div>

          {/* Question View */}
          <div className="card" ref={questionContainerRef} style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <span className="badge badge-info" style={{ textTransform: 'uppercase', fontSize: '10px' }}>Q {currentQIndex + 1} of {data.questions.length}</span>
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                  <span className="badge badge-secondary" style={{ textTransform: 'uppercase', fontSize: '10px' }}>{q.difficulty} • {q.bloomLevel}</span>
                  {!isQSubmitted && !disputedQuestionIds.has(q.id) && (
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
                  {disputedQuestionIds.has(q.id) && (
                    <span style={{ fontSize: '10.5px', color: '#f59e0b', fontWeight: 'bold' }}>
                      ⚠️ Bypassed
                    </span>
                  )}
                </div>
              </div>

              {(() => {
                if (q.type === 'assertion_reason') {
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
                {(q.type === 'multiple_mcq' || q.type === 'multi_mcq') && Array.isArray(q.options) && q.options.length > 0 && (
                  q.options.map((opt: any, oIdx: number) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    let isChecked = false;
                    try { isChecked = JSON.parse(uAns || '[]').includes(letter); } catch {}
                    const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
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
                          border: isChecked ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                          background: isChecked ? 'var(--accent-light)' : 'var(--surface)',
                          cursor: isQSubmitted ? 'not-allowed' : 'pointer'
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
                      </div>
                    );
                  })
                )}

                {/* 2. True/False */}
                {q.type === 'true_false' && (
                  ['True', 'False'].map((val) => {
                    const selected = uAns.toLowerCase() === val.toLowerCase();
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
                          border: selected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                          background: selected ? 'var(--accent-light)' : 'var(--surface)',
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
                      </div>
                    );
                  })
                )}

                {/* 3. Assertion & Reason */}
                {q.type === 'assertion_reason' && (() => {
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

                  return optionsToRender.map((opt: any) => {
                    const code = opt.code;
                    const selected = uAns === code;
                    const optionText = opt.text;
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
                          border: selected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                          background: selected ? 'var(--accent-light)' : 'var(--surface)',
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
                      </div>
                    );
                  });
                })()}

                {/* 4. Single MCQ / Any Question Type with Options (including Numerical MCQ) */}
                {q.type !== 'multiple_mcq' && q.type !== 'multi_mcq' && q.type !== 'true_false' && q.type !== 'assertion_reason' && Array.isArray(q.options) && q.options.length > 0 && (
                  q.options.map((opt: any, oIdx: number) => {
                    const letter = String.fromCharCode(65 + oIdx);
                    const selected = uAns === letter;
                    const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
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
                          border: selected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                          background: selected ? 'var(--accent-light)' : 'var(--surface)',
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
                      </div>
                    );
                  })
                )}

                {/* 5. Direct Numerical Input (when no options provided) */}
                {(q.type === 'numerical' || q.type === 'numerical_short' || q.type === 'numerical_long') && (!Array.isArray(q.options) || q.options.length === 0) && (
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
                {(q.type === 'fill_blank' || q.type === 'fill_blanks') && (!Array.isArray(q.options) || q.options.length === 0) && (
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
                {q.type !== 'true_false' && q.type !== 'assertion_reason' && q.type !== 'numerical' && q.type !== 'numerical_short' && q.type !== 'numerical_long' && q.type !== 'fill_blank' && q.type !== 'fill_blanks' && (!Array.isArray(q.options) || q.options.length === 0) && (
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
                  disabled={!feedbackCorrect && explanationTimer > 0}
                  style={{ width: '160px' }}
                >
                  {!feedbackCorrect && explanationTimer > 0 
                    ? `Wait (${explanationTimer}s)` 
                    : (currentQIndex === data.questions.length - 1 ? 'Finish Set →' : 'Next Question →')}
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
              disabled={!feedbackCorrect && explanationTimer > 0}
              style={{ width: '100%', padding: '14px', fontSize: '16px', fontWeight: 800, borderRadius: 'var(--radius-sm)' }}
            >
              {feedbackCorrect 
                ? 'Continue →' 
                : (explanationTimer > 0 ? `Read Explanation (${explanationTimer}s)` : '✓ I Understand')}
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
