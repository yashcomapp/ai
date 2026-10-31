'use client';

import React, { useEffect, useRef, useState, useCallback, useMemo, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, useSearchParams } from 'next/navigation';
import { mutate } from 'swr';
import { mutateFresh } from '@/lib/swrFetcher';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { db } from '@/lib/firebase/firestore';
import { useExamTimer } from '@/hooks/useExamTimer';
import { calculateHeadPose, checkLookingAway } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';
import { useLiveExam } from '@/hooks/useLiveExam';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { formatRichText } from '@/lib/questionTypes';
import { formatDuration, parseDateToMs } from '@/lib/dateUtils';
import { InterruptionLockoutModal } from '@/components/InterruptionLockoutModal';
import { ExamErrorBoundary } from '@/components/ExamErrorBoundary';
import QuestionDisplay, { RichMathText } from '@/components/QuestionDisplay';
import { RTC_CONFIG } from '@/lib/rtcConfig';
import StepAnswerInput from '@/components/exams/StepAnswerInput';
import { Question } from '@/types/question.types';
import { useSubjectiveAnswers } from '@/hooks/useSubjectiveAnswers';
import ExamHardwareCheckModal from '@/components/exam/ExamHardwareCheckModal';


// Extend window interface for CDN scripts
declare global {
  interface Window {
    FaceMesh: any;
    Camera: any;
    renderMathInElement: any;
  }
}

interface ExamData {
  id: string;
  name: string;
  totalTime?: number;
  totalMarks: number;
  mode?: string;
  type?: string;
  questionIds?: string[];
}

const ModelAnswerBox = React.memo(function ModelAnswerBox({ html }: { html: string }) {
  return (
    <div style={{ fontSize: '13px', marginTop: '6px', color: 'var(--text)', whiteSpace: 'pre-line' }}>
      <RichMathText content={html} />
    </div>
  );
});

function TakeSubjectiveExamContent() {
  const { firebaseUser, user, logout } = useAuth();
  const router = useRouter();
  const searchParams = useSearchParams();

  const examId = searchParams.get('examId') || '';
  const mode = searchParams.get('mode') || 'home';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [examData, setExamData] = useState<ExamData | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);

  // Refs
  const videoRef = useRef<HTMLVideoElement>(null);


  const lastActiveRef = useRef<number>(Date.now());
  const lastFaceCount = useRef<number>(0);
  const lastFaceMeshResults = useRef<any>(null);
  const faceMeshReady = useRef<boolean>(false);
  const lastNoFaceLogRef = useRef<number>(0);
  const lastMultipleLogRef = useRef<number>(0);
  const prevTabViolationsRef = useRef<number>(0);
  const prevNoFaceViolationsRef = useRef<number>(0);
  const prevLookingAwayViolationsRef = useRef<number>(0);
  const hasCrossedThresholdRef = useRef<boolean>(false);

  // Own Exam states
  const [attemptId, setAttemptId] = useState('');
  const [assignment, setAssignment] = useState<any>(null);
  const [startedAt, setStartedAt] = useState('');
  const [started, setStarted] = useState(false);

  const isLateStart = useMemo(() => {
    if (!assignment || assignment.openMode !== 'scheduled' || !assignment.startAt || !startedAt) return false;
    const startMs = parseDateToMs(assignment.startAt);
    const actualStartMs = parseDateToMs(startedAt);
    if (startMs <= 0 || actualStartMs <= 0) return false;
    return (actualStartMs - startMs) > 2 * 60 * 1000;
  }, [assignment, startedAt]);

  const [remainingSecondsState, setRemainingSecondsState] = useState(0);
  const [submitting, setSubmitting] = useState(false);
  const [isStartingExam, setIsStartingExam] = useState(false);
  const [submitCooldown, setSubmitCooldown] = useState(0);
  const [submitErrorMessage, setSubmitErrorMessage] = useState('');

  // Submit cooldown timer
  useEffect(() => {
    if (submitCooldown <= 0) return;
    const timer = setInterval(() => {
      setSubmitCooldown(prev => Math.max(0, prev - 1));
    }, 1000);
    return () => clearInterval(timer);
  }, [submitCooldown]);

  const [examSubmitted, setExamSubmitted] = useState(false);
  const [autoSubmittedReason, setAutoSubmittedReason] = useState<string | null>(null);

  // Grace period timer ref
  const startTimeRef = useRef<number>(0);
  useEffect(() => {
    if (started && !startTimeRef.current) {
      startTimeRef.current = Date.now();
    }
  }, [started]);


  // Hook 1: countdown timer
  const {
    timeRemaining: remainingSeconds,
    formattedTime
  } = useExamTimer({
    initialSeconds: remainingSecondsState,
    isPaused: !started || submitting || remainingSecondsState <= 0,
    onTimeUp: () => {
      handleAutoSubmit();
    }
  });
  const [blockingMessage, setBlockingMessage] = useState('');
  const [activeViolationWarning, setActiveViolationWarning] = useState<string | null>(null);

  // Peer review states
  const [revieweeCode, setRevieweeCode] = useState('');
  const [revieweeName, setRevieweeName] = useState('Classmate');
  const [myAttempt, setMyAttempt] = useState<any>(null);
  const {
    reviewAnswers,
    setReviewAnswers,
    reviewFeedback,
    setReviewFeedback,
    validateAnswers,
    compileReviews
  } = useSubjectiveAnswers();

  const {
    tabViolations,
    setTabViolations,
    awayTimeTotal,
    setAwayTimeTotal,
    proctoringViolations,
    setProctoringViolations,
    isInterrupted,
    resumeExam,
    cameraStatus,
    cameraStream,
    micBypassed,
    startCameraStream,
    stopCameraStream,
    cleanupProctoring
  } = useLiveExam({
    examId: examId || '',
    examName: examData?.name || 'Untitled Exam',
    studentCode: user?.studentCode || (firebaseUser?.email ? firebaseUser.email.split('@')[0] : 'student'),
    studentName: user?.name || firebaseUser?.displayName || firebaseUser?.email || 'Student',
    examType: 'subjective',
    totalQuestions: questions?.length || null,
    currentQuestionIndex: null,
    answeredCount: null,
    cameraVideoRef: videoRef,
    autonomous: (user as any)?.autonomous || false,
    started: started && !examSubmitted,
    isLate: isLateStart
  });

  const audioLevel = useAudioLevel(cameraStream);

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
    stopProctoring
  } = useProctoring({
    videoRef,
    enabled: started && !!cameraStream,
    lockdownShortcuts: true,
    lockdownContextMenu: true,
    lockdownWindowFocus: false, // Managed exclusively by useLiveExam SSOT (Rule 2.S)
    lockdownFullscreen: false,  // Managed exclusively by useLiveExam SSOT (Rule 2.S)
    startCameraStream,
    stopCameraStream,
    cleanupLiveExam: cleanupProctoring,
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



  useEffect(() => {
    if (videoRef.current && cameraStream && videoRef.current.srcObject !== cameraStream) {
      videoRef.current.srcObject = cameraStream;
      videoRef.current.play().catch(() => {});
    }
  }, [cameraStream, started]);

  const [cameraModalOpen, setCameraModalOpen] = useState(true);
  const [isMounted, setIsMounted] = useState(false);
  useMathRender([isMounted, questions, mode]);



  // Proctoring violations check & Auto-submit
  useEffect(() => {
    if (!attemptId || submitting || !started) return;

    // ONLY tab switching triggers auto-submission, at 3 violations.
    const crossedTabSubmit = tabViolations >= 3;

    if (crossedTabSubmit) {
      setAutoSubmittedReason('Auto-submitted due to exceeding allowed tab switches (3/3).');
      handleSubmitExam(true);
      return;
    }

    // Show warnings via non-blocking banner for intermediate tab violations
    if (tabViolations > prevTabViolationsRef.current) {
      setActiveViolationWarning(`⚠️ WARNING: Tab switch / focus loss detected! (Violation ${tabViolations}/3). Reaching 3/3 will auto-submit your exam.`);
    }

    prevTabViolationsRef.current = tabViolations;
  }, [tabViolations, attemptId, submitting, started]);



  useEffect(() => {
    setIsMounted(true);
  }, []);

  // Load Exam / Setup Peer Review info
  const loadExam = async () => {
    if (!firebaseUser || !examId) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/student/exams/subjective?examId=${encodeURIComponent(examId)}&mode=${encodeURIComponent(mode)}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });

      if (!res.ok) {
        const errJson = await res.json().catch(() => ({}));
        if ((user as any)?.autonomous || errJson.message?.toLowerCase().includes('autonomous')) {
          throw new Error('⛔ Permission Denied: Subjective Home Exam access is restricted for Autonomous Student accounts.');
        }
        throw new Error(errJson.message || 'Failed to retrieve subjective exam details.');
      }

      const resData = await res.json();
      if (resData.status === 'blocked' || resData.status === 'already_reviewed') {
        setError(resData.message || 'Access blocked.');
        setLoading(false);
        return;
      }
      if (resData.status === 'not_ready') {
        setError('Peer review is not ready yet. Please wait for teacher coordinates.');
        setLoading(false);
        return;
      }

      setExamData(resData.examData);
      setQuestions(resData.questions);
      setAssignment(resData.assignment || null);
      
      if (mode === 'peer-review') {
        setRevieweeCode(resData.revieweeCode);
        setRevieweeName(resData.revieweeName || 'Classmate');
        setMyAttempt(resData.myAttempt);
        const initialAnswers: { [key: string]: number | string } = {};
        setReviewAnswers(initialAnswers);
      } else {
        setAttemptId(resData.attemptId);
        setRemainingSecondsState(resData.remainingSeconds);
        setStartedAt(resData.startedAt);

        // Classroom tests bypass camera proctoring
        const isClassroom = examId.includes('CLASSROOM') || resData.examData?.type === 'classroom_test';
        if (isClassroom) {
          setCameraModalOpen(false);
          setStarted(true);
          try {
            const idToken = await firebaseUser.getIdToken();
            await fetch('/api/student/exams/subjective', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}`
              },
              body: JSON.stringify({ action: 'start', attemptId: resData.attemptId })
            });
          } catch (e) {
            console.error("Failed to start classroom test:", e);
          }
        }
      }
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred loading exam.');
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    if ((user as any)?.autonomous) {
      setError('Access Denied. Subjective exams are restricted for this student account.');
      setLoading(false);
      return;
    }
    if (examId && firebaseUser) {
      loadExam();
    }
  }, [firebaseUser, examId, mode, user]);


  const [diagnosticRunning, setDiagnosticRunning] = useState(true);

  // Auto-trigger camera diagnostic check on mount with a 2.5-second delay to release device locks
  useEffect(() => {
    if (examData && (examId.includes('CLASSROOM') || examData.type === 'classroom_test')) {
      setDiagnosticRunning(false);
      setCameraModalOpen(false);
      return;
    }
    if (cameraModalOpen && !cameraStream) {
      setDiagnosticRunning(true);
      const timer = setTimeout(async () => {
        if (examData && (examId.includes('CLASSROOM') || examData.type === 'classroom_test')) {
          setDiagnosticRunning(false);
          setCameraModalOpen(false);
          return;
        }
        await handleRunCheck();
        setDiagnosticRunning(false);
      }, 2500);
      return () => clearTimeout(timer);
    } else if (cameraStream) {
      setDiagnosticRunning(false);
    }
  }, [cameraModalOpen, cameraStream, examData, examId]);


  // WebRTC & Database Proctoring functions handled by useLiveExam hook


  const handleProceedToExam = async () => {
    if (isStartingExam) return;
    setIsStartingExam(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/student/exams/subjective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'start', attemptId })
      });
      if (!res.ok) {
        throw new Error('Server returned an error starting the exam.');
      }
      setCameraModalOpen(false);
      setStarted(true);
    } catch (e) {
      console.error("Failed to set in-progress status:", e);
      alert('❌ Failed to establish exam session with server. Please check your internet connection and try again.');
    } finally {
      setIsStartingExam(false);
    }
  };

  // Start FaceMesh once stream is active and exam started


  // Stop webcam stream when component unmounts
  useEffect(() => {
    return () => {
      stopWebcamAction();
    };
  }, []);







  // Stop camera stream cleanup
  const stopWebcamAction = () => {
    cleanupProctoring();
    stopCameraStream();
    stopProctoring();
  };

  const handleAutoSubmit = () => {
    alert('⏰ Time is up! Submitting your subjective attempt now.');
    handleSubmitExam();
  };

  const handleSubmitExam = async (proctoringViolationTriggered?: boolean) => {
    if (!firebaseUser || submitting || submitCooldown > 0) return;
    setSubmitting(true);
    setSubmitErrorMessage('');
    setBlockingMessage('Submitting your exam, please wait...');
    stopWebcamAction();

    try {
      const totalSec = (examData?.totalTime || 60) * 60;
      const timeSpent = Math.max(0, totalSec - remainingSeconds);

      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/exams/subjective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          attemptId,
          isLate: isLateStart,
          tabViolations,
          noFaceCount: proctoringViolations.noFace,
          multipleFacesCount: proctoringViolations.multipleFaces,
          awayTimeTotal,
          timeSpentSeconds: timeSpent,
          proctoringViolationTriggered: !!proctoringViolationTriggered,
          micBypassed: !!micBypassed,
          violations: {
            tabOutCount: tabViolations,
            noFaceCount: proctoringViolations.noFace || 0,
            multipleFacesCount: proctoringViolations.multipleFaces || 0,
            lookingAwayCount: proctoringViolations.lookingAway || 0,
            headMovementCount: proctoringViolations.headMovement || 0,
            screenshots: []
          }
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit exam attempt.');
      }

      if (typeof window !== 'undefined') {
        localStorage.removeItem('yc_student_learning_cache');
      }
      mutateFresh('/api/student/learning', firebaseUser).catch(() => {});
      mutateFresh('/api/student/dashboard', firebaseUser).catch(() => {});

      setBlockingMessage('');
      setExamSubmitted(true);
    } catch (err: any) {
      console.error('Submit subjective exam error:', err);
      setSubmitCooldown(20);
      setSubmitErrorMessage(`⚠️ ${err.message || 'Error submitting exam'}. Your answers are safe. Please wait a moment before retrying.`);
      setSubmitting(false);
      setBlockingMessage('');
    }
  };

  // Submit peer review
  const handleSubmitPeerReview = async () => {
    if (!firebaseUser || !examData || submitting) return;

    // Validate all evaluation fields via SSOT hook
    const validationError = validateAnswers(questions);
    if (validationError) {
      alert(validationError);
      return;
    }

    if (!confirm('Submit peer review? This cannot be changed after submission.')) return;

    setSubmitting(true);
    setBlockingMessage('Submitting peer review...');

    try {
      const { questionReviews, totalScore } = compileReviews(questions);

      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/exams/subjective/peer-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          attemptId: myAttempt.id,
          examId: examData.id,
          revieweeCode,
          questionReviews,
          totalScore
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit peer review.');
      }

      alert(`✅ Peer review submitted! Awarded ${totalScore}/${examData.totalMarks} marks to ${revieweeCode}.`);
      setTimeout(() => {
        router.push('/student');
      }, 1500);
    } catch (err: any) {
      console.error(err);
      alert(err.message || 'Error submitting peer review.');
    } finally {
      setSubmitting(false);
      setBlockingMessage('');
    }
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading subjective module...
        </div>
      </div>
    );
  }

  if (error || !examData) {
    const isPermissionDenied = ((user as any)?.autonomous && mode === 'home') || (error && (error.includes('Permission Denied') || error.includes('restricted') || error.includes('Access Denied') || error.includes('blocked')));
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: `1px solid ${isPermissionDenied ? 'var(--danger)' : 'var(--border-light)'}`, boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>{isPermissionDenied ? '🔒' : '⚠️'}</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: isPermissionDenied ? 'var(--danger)' : 'var(--text)', marginBottom: '8px' }}>
            {isPermissionDenied ? '⛔ Permission Denied / पहुँच अस्वीकृत' : 'Notice'}
          </h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text)', lineHeight: '1.5', marginBottom: '20px' }}>
            {isPermissionDenied 
              ? (error || 'Autonomous mode is active on your account. Subjective Home Exam sessions are restricted for Autonomous Student profiles.')
              : (error || 'Could not load subjective exam.')}
          </p>
          <button className="btn btn-primary" onClick={() => router.push(user?.role === 'admin' ? '/admin/exams' : '/student')} style={{ background: 'var(--accent)', color: 'var(--text-white)', border: 'none', padding: '10px 20px', borderRadius: 'var(--radius-md)', fontWeight: 'bold', cursor: 'pointer' }}>
            {user?.role === 'admin' ? '← Back to Exam Management' : '🏠 Back to Dashboard'}
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>

      {/* Script Injections for MediaPipe (Idempotent lazy loading) */}
      <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
      <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />


      {/* Top Header */}
      <header className="page-header glass" style={{ padding: '12px 24px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800 }}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Subjective Module</h1>
          </div>
        </div>
        <div className="page-header-right">
          <span className="badge badge-info">{mode === 'peer-review' ? 'Peer Reviewer' : 'Student'}</span>
          <button className="btn btn-secondary" onClick={() => router.push(user?.role === 'admin' ? '/admin/exams' : '/student')} style={{ marginLeft: '12px' }}>
            {user?.role === 'admin' ? '← Exit Simulator' : 'Dashboard'}
          </button>
        </div>
      </header>

      {!examSubmitted ? (
        <>
          {/* Camera modal permission for standard takers */}
          <ExamHardwareCheckModal
            isOpen={mode !== 'peer-review' && cameraModalOpen}
            diagnosticRunning={diagnosticRunning}
            cameraStream={cameraStream}
            audioLevel={audioLevel}
            cameraStatus={cameraStatus}
            permissionBlocked={permissionBlocked}
            micAttemptsRemaining={micAttemptsRemaining}
            isStartingExam={isStartingExam}
            onRunCheck={handleRunCheck}
            onProceed={handleProceedToExam}
          />

      {/* Interruption Lockout & Resume Modal (Phone call / tab switch recovery SSOT) */}
      <InterruptionLockoutModal
        isOpen={(isInterrupted || tabViolations >= 3) && started}
        tabViolations={tabViolations}
        maxViolations={3}
        durationSeconds={45}
        isSubmitting={submitting}
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
          if (!submitting) {
            setAutoSubmittedReason('Auto-submitted due to unresumed exam window departure (3/3).');
            handleSubmitExam(true);
          }
        }}
      />

      {/* Compact Proctoring Bar for Takers */}
      {mode !== 'peer-review' && (
        <div style={{
          display: started ? 'block' : 'none',
          background: 'rgba(30, 34, 49, 0.95)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '16px',
          padding: '16px',
          margin: '16px auto',
          maxWidth: '800px',
          width: '95%',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.2)'
        }}>
          {(() => {
            const isClassroom = examId.includes('CLASSROOM') || examData?.type === 'classroom_test';
            return (
              <div style={{
                display: 'grid',
                gridTemplateColumns: isClassroom ? '1fr' : '130px 1fr',
                gap: '16px',
                alignItems: 'center'
              }}>
                {/* Left side camera section */}
                {!isClassroom && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', alignItems: 'center' }}>
                    <div style={{
                      position: 'relative',
                      width: '120px',
                      height: '90px',
                      borderRadius: '12px',
                      overflow: 'hidden',
                      border: '3px solid var(--success)',
                      boxShadow: '0 4px 12px rgba(0,0,0,0.5)'
                    }}>
                      <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', height: '100%', objectFit: 'cover' }}></video>
                    </div>
                    <div style={{
                      width: '120px',
                      padding: '4px 6px',
                      borderRadius: '6px',
                      background: 'var(--success-bg)',
                      border: '1px solid var(--success)',
                      color: 'var(--success)',
                      fontSize: '11px',
                      fontWeight: 'bold',
                      textAlign: 'center',
                      whiteSpace: 'nowrap',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis'
                    }}>
                      {faceStatus.replace(' Detected', '').replace(' Verified', '')}
                    </div>
                  </div>
                )}

                {/* Right side stats grid */}
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(80px, 1fr))',
                  gap: '8px',
                  width: '100%'
                }}>
                  {/* Tab Switch */}
                  <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '10px', padding: '8px', textAlign: 'center', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                    <div style={{ fontSize: '11px', color: 'rgba(255,255,255,0.4)', marginBottom: '4px' }}>📑 TAB</div>
                    <span style={{ fontSize: '16px', fontWeight: 'bold', color: 'white' }}>{tabViolations}/3</span>
                  </div>
                  {/* No Face */}
                  {!isClassroom && (
                    <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '10px', padding: '8px', textAlign: 'center', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'rgba(255,255,255,0.4)', marginBottom: '4px' }}>👤 NOFACE</div>
                      <span style={{ fontSize: '16px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations.noFace}</span>
                    </div>
                  )}
                  {/* Multiple */}
                  {!isClassroom && (
                    <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '10px', padding: '8px', textAlign: 'center', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'rgba(255,255,255,0.4)', marginBottom: '4px' }}>👥 MULTI</div>
                      <span style={{ fontSize: '16px', fontWeight: 'bold', color: 'white' }}>{proctoringViolations.multipleFaces}</span>
                    </div>
                  )}
                  {/* Time */}
                  <div style={{ background: remainingSeconds <= 120 ? 'var(--danger-bg)' : 'rgba(255,255,255,0.03)', border: `1px solid ${remainingSeconds <= 120 ? 'var(--danger-border)' : 'rgba(255,255,255,0.05)'}`, borderRadius: '10px', padding: '8px', textAlign: 'center', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                    <div style={{ fontSize: '11px', color: remainingSeconds <= 120 ? 'var(--danger)' : 'rgba(255,255,255,0.4)', marginBottom: '4px' }}>⏱️ Remaining</div>
                    <span style={{ fontSize: '20px', fontWeight: 'bold', color: remainingSeconds <= 120 ? 'var(--danger)' : 'white' }}>{formatDuration(remainingSeconds)}</span>
                  </div>
                </div>
              </div>
            );
          })()}
        </div>
      )}

          {/* Main Content Area */}
          <main style={{ flex: 1, padding: '24px 12px', maxWidth: '800px', width: '100%', margin: '0 auto', userSelect: 'none', WebkitUserSelect: 'none' }}>
        {/* Exam Title and Meta */}
        <div className="card" style={{ padding: '20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', marginBottom: '20px' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>
            {mode === 'peer-review' ? `👥 Peer Review: ${examData.name}` : examData.name}
          </h2>
          <div style={{ display: 'flex', gap: '20px', color: 'var(--text-muted)', fontSize: '12px', marginTop: '10px' }}>
            <span>📋 Questions: {questions.length}</span>
            <span>⭐ Marks: {examData.totalMarks}</span>
            {mode === 'peer-review' && (
              <span style={{ color: 'var(--accent)', fontWeight: 600 }}>📝 Reviewing: {revieweeName}</span>
            )}
          </div>
        </div>

        {/* Action instructions alert */}
        <div className="alert-box alert-box-info" style={{ display: 'block', marginBottom: '24px' }}>
          {mode === 'peer-review' ? (
            <span> Look at classmate <strong>{revieweeName}</strong>'s physical paper and enter marks for each question below based on the model answers.</span>
          ) : (
            <span>📝 <strong>Instructions:</strong> Please write your answers on paper. Do not type answers in this screen. Once you have finished writing all questions, click "Submit Exam" below. Your parent will review your physical paper.</span>
          )}
        </div>

        {/* Questions Cards Loop */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {questions.map((q, idx) => {
            // Grading answer solution text helper (peer review mode only)
            let answerHtml = '';
            if (mode === 'peer-review') {
              if (q.answerLines && q.answerLines.length > 0) {
                answerHtml = q.answerLines.map(l => `<div style="margin:4px 0;">${l.lineNo}. ${formatRichText(l.text)}</div>`).join('');
              } else if (q.solution) {
                answerHtml = `<div>${formatRichText(q.solution)}</div>`;
              } else {
                answerHtml = '<em>No model answer config.</em>';
              }
            }

            return (
              <div key={q.id} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                <div style={{ padding: '10px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontWeight: 700, color: 'var(--accent)', fontSize: '13px' }}>Question {idx + 1}</span>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{q.marks} Marks</span>
                </div>

                <div style={{ padding: '20px' }}>
                  <QuestionDisplay
                    question={q}
                    mode="stem-only"
                    style={{ fontSize: '15px', color: 'var(--text)', lineHeight: 1.6 }}
                  />
                </div>

                {/* Peer Review Model Answer & Grading Fields */}
                {mode === 'peer-review' && (
                  <div style={{ borderTop: '1px dashed var(--border-light)', background: 'var(--bg-soft)', padding: '16px' }}>
                    <div style={{ background: 'rgba(76,175,80,0.06)', borderLeft: '4px solid var(--success)', padding: '12px', borderRadius: '4px', marginBottom: '16px' }}>
                      <strong style={{ fontSize: '12px', color: 'var(--success)' }}>📖 Model Answer:</strong>
                      <ModelAnswerBox html={answerHtml} />
                    </div>

                    <strong style={{ fontSize: '12px', display: 'block', marginBottom: '10px' }}>✏️ Award Marks:</strong>
                    
                    <StepAnswerInput
                      questionIndex={idx}
                      steps={q.steps}
                      questionMarks={q.marks}
                      reviewAnswers={reviewAnswers}
                      setReviewAnswers={setReviewAnswers}
                    />

                    {/* Feedback comments */}
                    <textarea 
                      placeholder="Add feedback comment (optional)"
                      rows={2}
                      value={reviewFeedback[`pf_${idx}`] || ''}
                      onChange={(e) => setReviewFeedback(prev => ({ ...prev, [`pf_${idx}`]: e.target.value }))}
                      style={{ width: '100%', marginTop: '12px', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px', background: 'var(--surface)', color: 'var(--text)', fontFamily: 'inherit' }}
                    />
                  </div>
                )}
              </div>
            );
          })}
        </div>

          {/* Submit Actions */}
          <div style={{ marginTop: '30px', display: 'flex', justifyContent: 'center' }}>
            {mode === 'peer-review' ? (
              <button className="btn btn-primary" onClick={handleSubmitPeerReview} disabled={submitting} style={{ width: '100%', padding: '14px', fontSize: '15px' }}>
                {submitting ? 'Submitting evaluations...' : '✅ Submit Peer Review'}
              </button>
            ) : (
              started && (
                <div style={{ width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '8px' }}>
                  <button 
                    className="btn btn-primary" 
                    onClick={() => handleSubmitExam()} 
                    disabled={submitting || submitCooldown > 0} 
                    style={{ 
                      width: '100%', 
                      padding: '14px', 
                      fontSize: '15px', 
                      opacity: (submitting || submitCooldown > 0) ? 0.6 : 1,
                      cursor: (submitting || submitCooldown > 0) ? 'not-allowed' : 'pointer'
                    }}
                  >
                    {submitCooldown > 0 
                      ? `⏳ Please wait ${submitCooldown}s to retry (Saved)` 
                      : (submitting ? 'Submitting exam...' : '📝 Submit Exam (Wrote on Paper)')
                    }
                  </button>
                  {submitErrorMessage && (
                    <div style={{ fontSize: '12px', color: 'var(--danger)', textAlign: 'center', fontWeight: 600 }}>
                      {submitErrorMessage}
                    </div>
                  )}
                </div>
              )
            )}
          </div>
        </main>
      </>
      ) : (
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '80vh',
          padding: '20px',
          color: 'var(--text)',
          textAlign: 'center'
        }}>
          <div style={{
            background: 'var(--surface)',
            border: '1px solid var(--border-light)',
            borderRadius: '16px',
            padding: '40px 30px',
            maxWidth: '500px',
            width: '100%',
            boxShadow: 'var(--shadow-xl)',
            display: 'flex',
            flexDirection: 'column',
            gap: '24px'
          }}>
            <div style={{ fontSize: '60px' }}>✅</div>
            <h2 style={{ fontSize: '24px', fontWeight: 800, margin: 0 }}>
              Exam Submitted!
            </h2>
            {autoSubmittedReason && (
              <div style={{
                background: 'var(--danger-bg)',
                border: '1px solid var(--danger-border)',
                borderRadius: '8px',
                padding: '12px',
                color: 'var(--danger)',
                fontSize: '13px',
                fontWeight: 600,
                margin: '5px 0'
              }}>
                🚨 {autoSubmittedReason}
              </div>
            )}
            <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', margin: 0 }}>
              Your subjective exam has been saved successfully and is waiting for parent review.
            </p>
            <button
              className="btn btn-primary"
              onClick={() => router.push('/student')}
              style={{
                width: '100%',
                padding: '14px',
                fontSize: '15px',
                fontWeight: 'bold',
                marginTop: '10px'
              }}
            >
              Go to Dashboard
            </button>
          </div>
        </div>
      )}

      {/* Blocking Submission Overlays */}
      {blockingMessage && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 30000, color: 'white' }}>
          <div className="spinner"></div>
          <p style={{ marginTop: '20px', fontSize: '15px', fontWeight: 'bold' }}>{blockingMessage}</p>
        </div>
      )}
    </div>
  );
}

export default function StudentSubjectiveExam() {
  return (
    <ExamErrorBoundary
      fallbackTitle="Subjective Exam Workspace Recovery"
      onReset={() => {
        try {
          if (typeof window !== 'undefined' && window.localStorage) {
            const keysToRemove: string[] = [];
            for (let i = 0; i < localStorage.length; i++) {
              const k = localStorage.key(i);
              if (k && k.startsWith('subjective_exam_state_')) {
                keysToRemove.push(k);
              }
            }
            keysToRemove.forEach(k => localStorage.removeItem(k));
          }
        } catch {}
      }}
    >
      <Suspense fallback={
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
          <div className="loading" style={{ display: 'block' }}>
            <div className="spinner"></div> Loading subjective exam...
          </div>
        </div>
      }>
        <TakeSubjectiveExamContent />
      </Suspense>
    </ExamErrorBoundary>
  );
}
