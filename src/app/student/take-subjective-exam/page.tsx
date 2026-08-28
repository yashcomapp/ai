'use client';

import React, { useEffect, useRef, useState, useCallback, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { db } from '@/lib/firebase/firestore';
import { useExamTimer } from '@/hooks/useExamTimer';
import { calculateHeadPose, checkLookingAway } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';
import { useLiveExam } from '@/hooks/useLiveExam';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { preprocessMathText, formatRichText } from '@/lib/questionTypes';
import { formatDuration } from '@/lib/dateUtils';

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
  id: string;
  questionCode: string;
  qNumber?: number;
  type?: string;
  text: string;
  marks: number;
  solution?: string;
  answerLines?: Array<{ lineNo: number; text: string }>;
  steps?: Array<{ description: string; marks: number }>;
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
    <div 
      className="math-container" 
      dangerouslySetInnerHTML={{ __html: html }} 
      style={{ fontSize: '13px', marginTop: '6px', color: 'var(--text)', whiteSpace: 'pre-line' }} 
    />
  );
});

function TakeSubjectiveExamContent() {
  const { firebaseUser, user, logout } = useAuth();
  const { toggleTheme } = useTheme();
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
  
  const [startedAt, setStartedAt] = useState('');
  const [started, setStarted] = useState(false);


  const [remainingSecondsState, setRemainingSecondsState] = useState(0);
  const [submitting, setSubmitting] = useState(false);
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
  const [reviewAnswers, setReviewAnswers] = useState<{ [key: string]: number | string }>({});
  const [reviewFeedback, setReviewFeedback] = useState<{ [key: string]: string }>({});

  const {
    tabViolations,
    setTabViolations,
    awayTimeTotal,
    setAwayTimeTotal,
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
    examName: examData?.name || 'Untitled Exam',
    studentCode: user?.studentCode || (firebaseUser?.email ? firebaseUser.email.split('@')[0] : 'student'),
    studentName: user?.name || firebaseUser?.displayName || firebaseUser?.email || 'Student',
    examType: 'subjective',
    totalQuestions: questions.length || null,
    currentQuestionIndex: null,
    answeredCount: null,
    cameraVideoRef: videoRef,
    autonomous: (user as any)?.autonomous || false,
    started: started && !examSubmitted
  });

  const audioLevel = useAudioLevel(cameraStream);

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
    stopProctoring
  } = useProctoring({
    videoRef,
    enabled: started && !!cameraStream,
    lockdownShortcuts: true,
    lockdownContextMenu: true,
    lockdownWindowFocus: true,
    lockdownFullscreen: true,
    startCameraStream,
    stopCameraStream,
    cleanupLiveExam: cleanupProctoring,
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
      alert('🚨 Exam auto-submitted: You switched tabs or left the exam window 3 times.');
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
      const res = await fetch(`/api/student/exams/subjective?examId=${examId}&mode=${mode}`, {
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
    if (!firebaseUser || submitting) return;
    setSubmitting(true);
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

      setBlockingMessage('');
      setExamSubmitted(true);
    } catch (err: any) {
      console.error(err);
      alert(err.message || 'Error submitting exam.');
      setSubmitting(false);
      setBlockingMessage('');
    }
  };

  // Submit peer review
  const handleSubmitPeerReview = async () => {
    if (!firebaseUser || !examData || submitting) return;

    // Validate all evaluation fields are explicitly answered
    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      if (q.steps && q.steps.length > 0) {
        for (let s = 0; s < q.steps.length; s++) {
          const rawVal = reviewAnswers[`ps_${i}_${s}`];
          if (rawVal === undefined || rawVal === null || rawVal === "") {
            alert(`Please award marks for Question ${i + 1}, Step ${s + 1}.`);
            return;
          }
        }
      } else {
        const rawVal = reviewAnswers[`ps_${i}_0`];
        if (rawVal === undefined || rawVal === null || rawVal === "") {
          alert(`Please award marks for Question ${i + 1}.`);
          return;
        }
      }
    }

    if (!confirm('Submit peer review? This cannot be changed after submission.')) return;

    setSubmitting(true);
    setBlockingMessage('Submitting peer review...');

    try {
      const questionReviews = [];
      let totalScore = 0;

      for (let i = 0; i < questions.length; i++) {
        const q = questions[i];
        let questionTotal = 0;
        const stepMarks: Array<{ stepNo: number; awarded: number }> = [];

        if (q.steps && q.steps.length > 0) {
          for (let s = 0; s < q.steps.length; s++) {
            const val = Number(reviewAnswers[`ps_${i}_${s}`]);
            stepMarks.push({ stepNo: s + 1, awarded: val });
            questionTotal += val;
          }
        } else {
          const val = Number(reviewAnswers[`ps_${i}_0`]);
          stepMarks.push({ stepNo: 1, awarded: val });
          questionTotal = val;
        }

        const feedback = reviewFeedback[`pf_${i}`] || '';
        questionReviews.push({
          questionId: q.id,
          maxMarks: q.marks,
          marksAwarded: questionTotal,
          stepMarks,
          feedback
        });
        totalScore += questionTotal;
      }

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
          <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ background: 'var(--accent)', color: '#ffffff', border: 'none', padding: '10px 20px', borderRadius: 'var(--radius-md)', fontWeight: 'bold', cursor: 'pointer' }}>
            🏠 Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Fullscreen & Focus Lockout Overlay */}
      {(!isFullscreen || !isWindowFocused) && started && !examSubmitted && (
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
      {/* Script Injections for MediaPipe (Lazy loaded when modal is open) */}
      {mode !== 'peer-review' && cameraModalOpen && (
        <>
          <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
          <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />
        </>
      )}


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
          <button className="btn btn-secondary" onClick={() => router.push('/student')} style={{ marginLeft: '12px' }}>Dashboard</button>
        </div>
      </header>

      {!examSubmitted ? (
        <>
          {/* Camera modal permission for standard takers */}
          {mode !== 'peer-review' && cameraModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'flex-start', justifyContent: 'center', padding: '40px 20px', overflowY: 'auto' }}>
          <div className="card" style={{ maxWidth: '450px', width: '90%', padding: '30px', textAlign: 'center', background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', boxShadow: 'var(--shadow-lg)', margin: '0 auto' }}>
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
                <h2 style={{ fontSize: '1.4rem', marginBottom: '10px' }}>⚙️ Hardware Diagnostic check</h2>
                <p style={{ color: 'var(--text-muted)', fontSize: '13px', marginBottom: '16px' }}>Please check that your webcam and microphone are working correctly before starting.</p>

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
            
            <div style={{ width: '100%', height: '220px', background: '#111', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative' }}>
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
                <div style={{ color: '#555', fontSize: '12px' }}>Webcam Feed Offline</div>
              )}
            </div>

            {cameraStream && (
              <div style={{ margin: '20px 0 10px', textAlign: 'left' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                  <span>🎙️ Mic Input Activity</span>
                  <strong>{audioLevel > 0 ? `${audioLevel}%` : 'Silent'}</strong>
                </div>
                <div style={{ height: '8px', background: 'var(--bg-soft)', borderRadius: '4px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', background: 'var(--success)', width: `${audioLevel}%`, transition: 'width 0.1s ease' }}></div>
                </div>
              </div>
            )}

            {cameraStatus && <p style={{ color: 'var(--text-muted)', fontSize: '12px', margin: '15px 0 0' }}>{cameraStatus}</p>}
            
            {!cameraStream ? (
              <button 
                className="btn btn-primary" 
                onClick={handleRunCheck} 
                style={{ marginTop: '20px', width: '100%' }}
                disabled={permissionBlocked && micAttemptsRemaining === 0}
              >
                {permissionBlocked ? '❌ Hardware Blocked (Retry)' : 'Test Camera & Microphone'}
              </button>
            ) : (
              <button className="btn btn-success" onClick={handleProceedToExam} style={{ marginTop: '20px', width: '100%' }}>
                Start Exam / Proceed
              </button>
            )}
              </>
            )}
          </div>
        </div>
      )}

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
                      border: '3px solid #2ecc71',
                      boxShadow: '0 4px 12px rgba(0,0,0,0.5)'
                    }}>
                      <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', height: '100%', objectFit: 'cover' }}></video>
                    </div>
                    <div style={{
                      width: '120px',
                      padding: '4px 6px',
                      borderRadius: '6px',
                      background: 'rgba(46, 204, 113, 0.15)',
                      border: '1px solid #2ecc71',
                      color: '#2ecc71',
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
                  <div style={{ background: remainingSeconds <= 120 ? 'rgba(231, 76, 60, 0.15)' : 'rgba(255,255,255,0.03)', border: `1px solid ${remainingSeconds <= 120 ? '#e74c3c' : 'rgba(255,255,255,0.05)'}`, borderRadius: '10px', padding: '8px', textAlign: 'center', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                    <div style={{ fontSize: '11px', color: remainingSeconds <= 120 ? '#e74c3c' : 'rgba(255,255,255,0.4)', marginBottom: '4px' }}>⏱️ Remaining</div>
                    <span style={{ fontSize: '20px', fontWeight: 'bold', color: remainingSeconds <= 120 ? '#e74c3c' : 'white' }}>{formatDuration(remainingSeconds)}</span>
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
                  <p className="math-container" style={{ fontSize: '15px', color: 'var(--text)', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                     {preprocessMathText(q.text)}
                  </p>
                </div>

                {/* Peer Review Model Answer & Grading Fields */}
                {mode === 'peer-review' && (
                  <div style={{ borderTop: '1px dashed var(--border-light)', background: 'var(--bg-soft)', padding: '16px' }}>
                    <div style={{ background: 'rgba(76,175,80,0.06)', borderLeft: '4px solid var(--success)', padding: '12px', borderRadius: '4px', marginBottom: '16px' }}>
                      <strong style={{ fontSize: '12px', color: 'var(--success)' }}>📖 Model Answer:</strong>
                      <ModelAnswerBox html={answerHtml} />
                    </div>

                    <strong style={{ fontSize: '12px', display: 'block', marginBottom: '10px' }}>✏️ Award Marks:</strong>
                    
                    {/* Render Steps inputs */}
                    {q.steps && q.steps.length > 0 ? (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        {q.steps.map((step, si) => (
                          <div key={si} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', flexWrap: 'wrap', gap: '8px' }}>
                            <span style={{ fontSize: '12px', color: 'var(--text)' }}>{step.description}</span>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {step.marks}</span>
                              <input 
                                type="number" 
                                min="0" 
                                max={step.marks} 
                                step="0.5" 
                                value={reviewAnswers[`ps_${idx}_${si}`] ?? ""}
                                onChange={(e) => {
                                  const raw = e.target.value;
                                  if (raw === "") {
                                    setReviewAnswers(prev => {
                                      const copy = { ...prev };
                                      delete copy[`ps_${idx}_${si}`];
                                      return copy;
                                    });
                                  } else {
                                    const val = Math.min(step.marks, Math.max(0, parseFloat(raw) || 0));
                                    setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_${si}`]: val }));
                                  }
                                }}
                                style={{ width: '70px', padding: '4px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', textAlign: 'center', background: 'var(--surface)', color: 'var(--text)' }}
                              />
                            </div>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}>
                        <span style={{ fontSize: '12px', color: 'var(--text)' }}>Overall Question Score</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {q.marks}</span>
                          <input 
                            type="number" 
                            min="0" 
                            max={q.marks} 
                            step="0.5" 
                            value={reviewAnswers[`ps_${idx}_0`] ?? ""}
                            onChange={(e) => {
                              const raw = e.target.value;
                              if (raw === "") {
                                setReviewAnswers(prev => {
                                  const copy = { ...prev };
                                  delete copy[`ps_${idx}_0`];
                                  return copy;
                                });
                              } else {
                                const val = Math.min(q.marks, Math.max(0, parseFloat(raw) || 0));
                                setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_0`]: val }));
                              }
                            }}
                            style={{ width: '70px', padding: '4px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', textAlign: 'center', background: 'var(--surface)', color: 'var(--text)' }}
                          />
                        </div>
                      </div>
                    )}

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
                <button className="btn btn-primary" onClick={() => handleSubmitExam()} disabled={submitting} style={{ width: '100%', padding: '14px', fontSize: '15px' }}>
                  {submitting ? 'Submitting exam...' : '📝 Submit Exam (Wrote on Paper)'}
                </button>
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
                background: 'rgba(231, 76, 60, 0.1)',
                border: '1px solid rgba(231, 76, 60, 0.3)',
                borderRadius: '8px',
                padding: '12px',
                color: '#e74c3c',
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
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading subjective exam...
        </div>
      </div>
    }>
      <TakeSubjectiveExamContent />
    </Suspense>
  );
}
