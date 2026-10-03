'use client';

import React, { useEffect, useState, useRef, Suspense, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import {
  evaluateQuestionAnswer,
  isMultipleChoiceType,
  parseAnswerList
} from '@/lib/questionTypes';
import { useMathRender } from '@/hooks/useMathRender';
import { usePractice } from '@/hooks/usePractice';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { useProctoring } from '@/hooks/useProctoring';
import { useLiveExam } from '@/hooks/useLiveExam';
import { InterruptionLockoutModal } from '@/components/InterruptionLockoutModal';
import { PracticeLockPrompt } from '@/components/student/practice/PracticeLockPrompt';
import { PracticeHardwareModal } from '@/components/student/practice/PracticeHardwareModal';
import { PracticeProctorBar } from '@/components/student/practice/PracticeProctorBar';
import { PracticeQuestionCard } from '@/components/student/practice/PracticeQuestionCard';
import { PracticeFeedbackModal } from '@/components/student/practice/PracticeFeedbackModal';
import { PracticeCompletionView } from '@/components/student/practice/PracticeCompletionView';

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
  const { startSession } = usePractice();
  const { firebaseUser, user } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();

  const topicCode = searchParams.get('topicCode') || '';
  const category = searchParams.get('category') || 'continuePractice';
  const mode = searchParams.get('mode') || '';
  const isRecoveryMode = mode === 'recovery';

  // Session setup & lock state
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [data, setData] = useState<PracticeData | null>(null);
  const [requireTextbookStudy, setRequireTextbookStudy] = useState(false);
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
  const [explanationTimer, setExplanationTimer] = useState(0);

  // Timers
  const [totalSeconds, setTotalSeconds] = useState(0);
  const [currentQSeconds, setCurrentQSeconds] = useState(0);

  // Camera & FaceMesh
  const [cameraModalOpen, setCameraModalOpen] = useState(true);
  const [isMounted, setIsMounted] = useState(false);

  const videoRef = useRef<HTMLVideoElement>(null);
  const questionContainerRef = useRef<HTMLDivElement>(null);

  const prevTabViolationsRef = useRef<number>(0);
  const prevNoFaceViolationsRef = useRef<number>(0);
  const prevLookingAwayViolationsRef = useRef<number>(0);
  const hasCrossedThresholdRef = useRef<boolean>(false);
  const proctorIntervalRef = useRef<any>(null);

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

  const {
    tabViolations,
    awayTimeTotal: totalAwaySeconds,
    proctoringViolations,
    setProctoringViolations,
    isInterrupted,
    resumeExam,
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

  const currentQuestion = data?.questions?.[currentQIndex];

  const isNumerical = useMemo(() => {
    if (!currentQuestion) return false;
    if ((currentQuestion as any).relaxProctoring === true || (currentQuestion as any).isNumerical === true) {
      return true;
    }
    const text = (currentQuestion.text || '').toLowerCase();
    const mathKeywords = [
      'calculate', 'solve', 'evaluate', 'find the value', 'find the length', 
      'find the area', 'simplify', 'ratio', 'percentage', 'theorem', 
      'derivative', 'integral', 'factorize', 'expand', 'equation', 'expression',
      'probability', 'mean', 'median', 'mode', 'standard deviation', 'calculate',
      'numerical', 'geometry', 'algebra', 'prove', 'find the', 'what is the value'
    ];
    if (mathKeywords.some(keyword => text.includes(keyword))) return true;
    
    const mathSymbols = [
      '\\frac', '\\sqrt', '\\times', '\\div', '\\angle', '\\cong', '\\parallel', 
      '\\Delta', '\\pi', '\\theta', '\\alpha', '\\beta', '^', '=', '+', '-', '*', '/'
    ];
    if (mathSymbols.some(symbol => text.includes(symbol))) return true;
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
    stopProctoring
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
    onViolation: (violationType) => {
      if (violationType === 'no_face') {
        setProctoringViolations(prev => ({ ...prev, noFace: prev.noFace + 1 }));
      } else if (violationType === 'multiple_faces') {
        setProctoringViolations(prev => ({ ...prev, multipleFaces: prev.multipleFaces + 1 }));
      } else if (violationType === 'gaze') {
        setProctoringViolations(prev => ({ ...prev, lookingAway: prev.lookingAway + 1 }));
      } else if (violationType === 'movement') {
        setProctoringViolations(prev => ({ ...prev, headMovement: prev.headMovement + 1 }));
      }
    }
  });

  useMathRender([currentQIndex, started, finished, data, feedbackOpen, isMounted, finalResult]);

  useEffect(() => {
    setIsMounted(true);
  }, []);

  const stopWebcam = () => {
    if (proctorIntervalRef.current) {
      clearInterval(proctorIntervalRef.current);
      proctorIntervalRef.current = null;
    }
    stopProctoring();
    stopCameraStream();
  };

  useEffect(() => {
    if (videoRef.current && cameraStream && videoRef.current.srcObject !== cameraStream) {
      videoRef.current.srcObject = cameraStream;
      videoRef.current.play().catch(() => {});
    }
  }, [cameraStream, cameraModalOpen]);

  // Timer effect for explanation reading limit on mistakes
  useEffect(() => {
    if (explanationTimer <= 0) return;
    const interval = setInterval(() => {
      setExplanationTimer(prev => prev - 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [explanationTimer]);

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

  // Stop webcam stream when component unmounts
  useEffect(() => {
    return () => {
      stopWebcam();
    };
  }, [cameraStream]);

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

  // Proctoring limits checking
  useEffect(() => {
    if (!started || finished) return;

    if (tabViolations >= 3) {
      handleFinishPractice(true);
      return;
    }

    const noFaceVal = proctoringViolations?.noFace || 0;
    const lookingAwayVal = proctoringViolations?.lookingAway || 0;
    const cumulativeVal = tabViolations + noFaceVal + lookingAwayVal;

    const crossedTab = tabViolations > 2;
    const crossedNoFace = noFaceVal > 3;
    const crossedLookingAway = lookingAwayVal > 3;
    const crossedCumulative = cumulativeVal > 4;

    const isCrossedNow = crossedTab || crossedNoFace || crossedLookingAway || crossedCumulative;

    if (isCrossedNow) {
      if (!hasCrossedThresholdRef.current) {
        hasCrossedThresholdRef.current = true;
      } else {
        const tabIncremented = tabViolations > prevTabViolationsRef.current;
        const noFaceIncremented = noFaceVal > prevNoFaceViolationsRef.current;
        const lookingAwayIncremented = lookingAwayVal > prevLookingAwayViolationsRef.current;

        if (tabIncremented || noFaceIncremented || lookingAwayIncremented) {
          handleFinishPractice(true);
          return;
        }
      }
    }

    prevTabViolationsRef.current = tabViolations;
    prevNoFaceViolationsRef.current = noFaceVal;
    prevLookingAwayViolationsRef.current = lookingAwayVal;
  }, [tabViolations, proctoringViolations, started, finished]);

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

  const handleProceedToExam = () => {
    setCameraModalOpen(false);
    setStarted(true);
  };

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
      
      let timerSec = 20;
      if (qType.includes('numerical') || isMath || qType === 'one' || qType === 'ssn' || qType === 'sln') {
        timerSec = 40;
      } else if (qType === 'assertion_reason' || qType === 'oar' || qType.includes('multi') || qText.length > 150) {
        timerSec = 30;
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

  const handleCheckboxChange = (letter: string) => {
    let currentChoices: string[] = [];
    try {
      currentChoices = JSON.parse(userAnswers[currentQIndex] || '[]');
    } catch {
      currentChoices = [];
    }

    if (currentChoices.includes(letter)) {
      currentChoices = currentChoices.filter(x => x !== letter);
    } else {
      currentChoices.push(letter);
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

  const handleTextAnswerChange = (val: string) => {
    const updated = [...userAnswers];
    updated[currentQIndex] = val;
    setUserAnswers(updated);
  };

  if (user && (user as any).autonomous) {
    return <PracticeLockPrompt type="autonomous" topicCode={topicCode} category={category} />;
  }

  if (showRecoveryPrompt) {
    return (
      <PracticeLockPrompt 
        type="recovery" 
        topicCode={topicCode} 
        category={category}
        lockType={lockType}
        recoveryMessage={recoveryMessage}
        recoveryConfirmedCheck={recoveryConfirmedCheck}
        setRecoveryConfirmedCheck={setRecoveryConfirmedCheck}
        confirmingRecovery={confirmingRecovery}
        onApproveRecovery={handleApproveRecovery}
        onStartRecovery={() => {
          setShowRecoveryPrompt(false);
          setLoading(true);
          router.push(`/student/topic?topicCode=${encodeURIComponent(topicCode)}&category=${category}&mode=recovery`);
        }}
      />
    );
  }

  if (requireTextbookStudy) {
    return (
      <PracticeLockPrompt
        type="textbook"
        topicCode={topicCode}
        category={category}
        lockType={lockType}
        textbookStudyMessage={textbookStudyMessage}
        textbookConfirmedCheck={textbookConfirmedCheck}
        setTextbookConfirmedCheck={setTextbookConfirmedCheck}
        confirmingTextbook={confirmingTextbook}
        onConfirmTextbook={handleConfirmTextbook}
      />
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
    return (
      <PracticeCompletionView
        finalResult={finalResult}
        topicData={data}
        totalSeconds={totalSeconds}
        totalAwaySeconds={totalAwaySeconds}
        tabViolations={tabViolations}
        noFaceCount={noFaceCount}
        multipleFacesCount={multipleFacesCount}
        lookingAwayCount={lookingAwayCount}
        userAnswers={userAnswers}
        questionResults={questionResults}
      />
    );
  }

  const q = data.questions[currentQIndex];
  const uAns = userAnswers[currentQIndex] || '';
  const isQSubmitted = submittedAnswers[currentQIndex];

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Interruption Lockout & Resume Modal */}
      <InterruptionLockoutModal
        isOpen={(isInterrupted || tabViolations >= 3) && started && !finished && !cameraModalOpen}
        tabViolations={tabViolations}
        maxViolations={3}
        isSubmitting={finished}
        onManualResume={() => {
          resumeExam();
        }}
        onTimeoutAutoSubmit={() => {
          if (!finished) {
            handleFinishPractice(true);
          }
        }}
      />

      {/* Camera permission & Hardware check modal */}
      <PracticeHardwareModal
        isOpen={cameraModalOpen}
        topicData={data}
        cameraStream={cameraStream}
        audioLevel={audioLevel}
        cameraStatus={cameraStatus}
        onRunCheck={handleRunCheck}
        onProceed={handleProceedToExam}
      />

      {/* Proctoring Bar */}
      {started && !finished && (
        <PracticeProctorBar
          videoRef={videoRef}
          tabViolations={tabViolations}
          noFaceCount={noFaceCount}
          lookingAwayCount={lookingAwayCount}
          totalSeconds={totalSeconds}
          currentQSeconds={currentQSeconds}
        />
      )}

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
          <PracticeQuestionCard
            question={q}
            currentQIndex={currentQIndex}
            totalQuestions={data.questions.length}
            userAnswer={uAns}
            isQSubmitted={isQSubmitted}
            isSubmittingPractice={isSubmittingPractice}
            feedbackCorrect={feedbackCorrect}
            explanationTimer={explanationTimer}
            questionContainerRef={questionContainerRef}
            onCheckboxChange={handleCheckboxChange}
            onRadioChange={handleRadioChange}
            onTextAnswerChange={handleTextAnswerChange}
            onBack={() => currentQIndex > 0 && setCurrentQIndex(currentQIndex - 1)}
            onSubmitQuestion={handleSubmitQuestion}
            onNext={handleNext}
          />
        </div>
      )}

      {/* Immediate Corrective Feedback Modal Dialog */}
      <PracticeFeedbackModal
        isOpen={feedbackOpen}
        isCorrect={feedbackCorrect}
        question={q}
        explanationTimer={explanationTimer}
        isSubmittingPractice={isSubmittingPractice}
        onNext={handleNext}
      />
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
