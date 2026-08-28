'use client';

import React, { useState, useEffect, useRef } from 'react';
import Script from 'next/script';
import { useLiveExam } from '@/hooks/useLiveExam';
import { useAudioLevel } from '@/hooks/useAudioLevel';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement } from '@/utils/headPose';
import { useProctoring } from '@/hooks/useProctoring';

interface HardwareCheckMockTestModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const GK_QUESTIONS = [
  {
    q: "What is the capital of India?",
    options: ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
    answer: 1
  },
  {
    q: "Which planet is known as the Red Planet?",
    options: ["Venus", "Mars", "Jupiter", "Saturn"],
    answer: 1
  },
  {
    q: "What is the largest ocean on Earth?",
    options: ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
    answer: 2
  },
  {
    q: "Who wrote 'Romeo and Juliet'?",
    options: ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
    answer: 0
  },
  {
    q: "What is the chemical symbol for water?",
    options: ["CO2", "H2O", "NaCl", "O2"],
    answer: 1
  }
];

export default function HardwareCheckMockTestModal({ isOpen, onClose }: HardwareCheckMockTestModalProps) {
  const [step, setStep] = useState<'diagnostic' | 'test' | 'success'>('diagnostic');


  // Test state
  const [currentQ, setCurrentQ] = useState(0);
  const [userAnswers, setUserAnswers] = useState<number[]>(new Array(GK_QUESTIONS.length).fill(-1));

  const videoRef = useRef<HTMLVideoElement | null>(null);


  // MediaPipe FaceMesh state refs
  const faceMeshReady = useRef(false);
  const lastFaceCount = useRef(0);
  const lastFaceMeshResults = useRef<any>(null);
  const lastHeadPose = useRef<any>(null);
  const lastSampledPoseRef = useRef<any>(null);
  const baselinePoseRef = useRef<{ yaw: number; pitch: number; roll: number } | null>(null);
  const baselineFramesRef = useRef<{ yaw: number; pitch: number; roll: number }[]>([]);

  const multipleFacesStartRef = useRef<number | null>(null);
  const lookingAwayStartRef = useRef<number | null>(null);
  const headMovementStartRef = useRef<number | null>(null);
  const lastNoFaceLogRef = useRef<number>(0);
  const lastMultipleLogRef = useRef<number>(0);
  const lastViolationLogTimeRef = useRef<number>(0);

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
    examId: 'mock_diagnostic_exam',
    examName: 'Mock Diagnostic Practice',
    studentCode: 'mock_student',
    studentName: 'Diagnostic Student',
    examType: 'practice',
    totalQuestions: GK_QUESTIONS.length,
    currentQuestionIndex: currentQ,
    answeredCount: userAnswers.filter(a => a !== -1).length,
    cameraVideoRef: videoRef,
    started: step === 'test',
    mock: true
  });

  const audioLevel = useAudioLevel(cameraStream);

  const {
    faceStatus,
    faceStatusClass,
    isFullscreen,
    isWindowFocused,
    permissionBlocked,
    micAttemptsRemaining,
    setMicAttemptsRemaining,
    setPermissionBlocked,
    handleRunCheck,
    stopAllProctoring,
    setIsWindowFocused
  } = useProctoring({
    videoRef,
    enabled: isOpen && step === 'test' && !!cameraStream,
    lockdownShortcuts: false,
    lockdownContextMenu: false,
    lockdownWindowFocus: true,
    lockdownFullscreen: false,
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
    if (isOpen) {
      setStep('diagnostic');
      setMicAttemptsRemaining(1);
      setPermissionBlocked(false);
      setUserAnswers(new Array(GK_QUESTIONS.length).fill(-1));
      setCurrentQ(0);
      setIsWindowFocused(true);
      handleRunCheck();
    } else {
      stopAllHardware();
    }
    return () => {
      stopAllHardware();
    };
  }, [isOpen]);





  // Trigger Mock Auto-submission on 3 tab violations
  useEffect(() => {
    if (step === 'test' && tabViolations >= 3) {
      alert('🚨 Mock Exam Auto-submitted: You switched tabs or left the test window 3 times.');
      handleSubmitTest();
    }
  }, [tabViolations, step]);

  const stopAllHardware = () => {
    stopAllProctoring();
  };

  const handleStartTest = async () => {
    setStep('test');

    // Trigger fullscreen
    try {
      document.documentElement.requestFullscreen().catch(() => {});
    } catch {}
  };

  const handleSelectOption = (optIdx: number) => {
    const updated = [...userAnswers];
    updated[currentQ] = optIdx;
    setUserAnswers(updated);
  };

  const handleNext = () => {
    if (currentQ < GK_QUESTIONS.length - 1) {
      setCurrentQ(currentQ + 1);
    }
  };

  const handlePrev = () => {
    if (currentQ > 0) {
      setCurrentQ(currentQ - 1);
    }
  };

  const handleSubmitTest = () => {
    // Exit fullscreen
    try {
      if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
      }
    } catch {}
    stopAllHardware();
    setStep('success');
  };

  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(8px)',
      zIndex: 30000,
      display: 'flex',
      alignItems: 'flex-start',
      justifyContent: 'center',
      padding: '40px 20px',
      overflowY: 'auto'
    }}>
      {/* Script Injections for MediaPipe (Lazy loaded when mock test is active) */}
      {isOpen && (
        <>
          <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
          <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />
        </>
      )}

      <div className="card" style={{
        maxWidth: step === 'test' ? '800px' : '500px',
        width: '100%',
        background: 'var(--surface)',
        borderRadius: 'var(--radius-lg)',
        border: '1px solid var(--border-light)',
        boxShadow: 'var(--shadow-lg)',
        padding: '24px',
        position: 'relative',
        margin: '0 auto'
      }}>
        {/* Lockout focus loss warning screen overlay */}
        {!isWindowFocused && step === 'test' && (
          <div style={{
            position: 'absolute',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.9)',
            backdropFilter: 'blur(16px)',
            WebkitBackdropFilter: 'blur(16px)',
            zIndex: 99999,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px',
            color: 'var(--text)',
            borderRadius: 'var(--radius-lg)'
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

        {/* Close Button */}
        <button 
          onClick={onClose}
          style={{
            position: 'absolute',
            top: '16px',
            right: '16px',
            background: 'transparent',
            border: 'none',
            fontSize: '18px',
            color: 'var(--text-muted)',
            cursor: 'pointer',
            zIndex: 10
          }}
        >
          ✕
        </button>

        {step === 'diagnostic' && (
          <div>
            <h2 style={{ fontSize: '18px', fontWeight: 800, margin: '0 0 10px 0', color: 'var(--text)' }}>
              🖥️ Pre-Exam Hardware Diagnostic
            </h2>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: '0 0 16px 0', lineHeight: '1.4' }}>
              Verify your camera and microphone are functioning before entering the proctored mock workspace.
            </p>

            <div style={{ 
              background: 'rgba(239, 68, 68, 0.08)', 
              border: '1px dashed rgba(239, 68, 68, 0.3)', 
              borderRadius: 'var(--radius-sm)', 
              padding: '12px 16px', 
              marginBottom: '16px', 
              textAlign: 'left' 
            }}>
              <strong style={{ fontSize: '12px', color: '#ef4444', display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px' }}>
                ⚠️ Proctored Exam Rules & Simulation Info
              </strong>
              <ul style={{ margin: 0, paddingLeft: '16px', fontSize: '11px', color: 'var(--text-muted)', display: 'flex', flexDirection: 'column', gap: '4px', lineHeight: '1.4' }}>
                <li><strong>Tab Switching:</strong> Max 2 focus-loss warnings allowed. Exceeding this (3rd switch) will auto-submit your mock exam.</li>
                <li><strong>Face & Gaze Tracking:</strong> Active client-side simulation (no database logs created).</li>
              </ul>
            </div>

            {/* Webcam Preview Container */}
            <div style={{
              width: '100%',
              height: '200px',
              background: '#171a1f',
              borderRadius: '8px',
              overflow: 'hidden',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              position: 'relative',
              border: '1px solid var(--border-light)'
            }}>
              {cameraStream ? (
                <video 
                  ref={videoRef}
                  autoPlay 
                  playsInline 
                  muted 
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              ) : (
                <div style={{ color: 'var(--text-muted)', fontSize: '12px', textAlign: 'center', padding: '20px' }}>
                  🎥 Camera Feed Offline
                </div>
              )}
            </div>

            {/* Mic indicator */}
            {cameraStream && (
              <div style={{ margin: '15px 0 10px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                  <span>🎙️ Mic Input Activity</span>
                  <strong>{audioLevel > 0 ? `${audioLevel}%` : 'Silent'}</strong>
                </div>
                <div style={{ height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', background: 'var(--success)', width: `${audioLevel}%`, transition: 'width 0.1s ease' }} />
                </div>
              </div>
            )}

            <div style={{
              fontSize: '12px',
              color: permissionBlocked ? 'var(--danger)' : 'var(--text-muted)',
              fontWeight: 500,
              margin: '15px 0',
              padding: '10px',
              background: 'var(--bg-soft)',
              borderRadius: '6px',
              borderLeft: `4px solid ${permissionBlocked ? 'var(--danger)' : 'var(--accent)'}`
            }}>
              {cameraStatus || 'Checking systems...'}
            </div>

            {/* Diagnostic instructions / guide if permissionBlocked */}
            {permissionBlocked && (
              <div style={{
                background: 'rgba(239, 68, 68, 0.08)',
                padding: '12px',
                borderRadius: '6px',
                fontSize: '11px',
                color: 'var(--text)',
                border: '1px solid rgba(239, 68, 68, 0.2)',
                marginBottom: '15px',
                lineHeight: '1.4'
              }}>
                <strong>How to fix permissions:</strong>
                <ol style={{ margin: '6px 0 0 16px', padding: 0 }}>
                  <li>Click the lock icon (🔒) on the left side of your browser URL bar.</li>
                  <li>Set Camera and Microphone options to <strong>"Allow"</strong>.</li>
                  <li>Click the <strong>"Retry Check"</strong> button below.</li>
                </ol>
              </div>
            )}

            <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={handleRunCheck}
                style={{ flex: 1, padding: '10px', fontSize: '13px', fontWeight: 700 }}
              >
                🔄 Retry Check
              </button>
              <button 
                className="btn btn-success"
                onClick={handleStartTest}
                disabled={!cameraStream}
                style={{ flex: 2, padding: '10px', fontSize: '13px', fontWeight: 700 }}
              >
                🚀 Start Mock Test
              </button>
            </div>
          </div>
        )}

        {step === 'test' && (
          <div>
            {/* Simulation Proctoring Bar */}
            <div className="proctor-bar" style={{ background: '#1a1d29', color: 'white', padding: '12px 20px', borderBottom: '2px solid var(--warning)', borderRadius: '8px', margin: '-24px -24px 20px -24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
              <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '10px', position: 'relative', flexShrink: 0 }}>
                <video 
                  ref={videoRef} 
                  autoPlay 
                  playsInline 
                  muted 
                  style={{ width: '100%', height: '75px', borderRadius: 'var(--radius-sm)', border: '2px solid var(--success)', background: '#111', objectFit: 'cover' }}
                />
                <div>
                  <div style={{ fontSize: '10px', color: '#999' }}>Integrity Status:</div>
                  <span className="badge badge-success" style={{ marginTop: '4px', fontSize: '9px', background: 'var(--success)' }}>
                    Active Proctoring (Mock)
                  </span>
                </div>
              </div>

              <div className="violation-stats" style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center', flex: 1 }}>
                <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
                  🚫 Tabs: {tabViolations} / 3
                </div>
                <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
                  👤 Away: {proctoringViolations.noFace}
                </div>
                <div className="violation-item" style={{ background: 'rgba(0,0,0,0.5)', padding: '4px 12px', borderRadius: '25px', fontSize: '11px' }}>
                  👁️ Gaze: {proctoringViolations.lookingAway}
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
              <span className="badge" style={{ background: 'var(--accent)', color: 'white', fontSize: '10px' }}>
                GK Mock Test (Unrecorded Simulation)
              </span>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                Question {currentQ + 1} of {GK_QUESTIONS.length}
              </span>
            </div>

            <h3 style={{ fontSize: '15px', fontWeight: 800, color: 'var(--text)', marginBottom: '16px', lineHeight: '1.4' }}>
              Q{currentQ + 1}. {GK_QUESTIONS[currentQ].q}
            </h3>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {GK_QUESTIONS[currentQ].options.map((opt, oIdx) => {
                const isSelected = userAnswers[currentQ] === oIdx;
                return (
                  <button
                    key={opt}
                    onClick={() => handleSelectOption(oIdx)}
                    style={{
                      width: '100%',
                      padding: '10px 14px',
                      borderRadius: '6px',
                      border: `1px solid ${isSelected ? 'var(--accent)' : 'var(--border-light)'}`,
                      background: isSelected ? 'var(--accent-soft)' : 'var(--surface)',
                      color: isSelected ? 'var(--accent)' : 'var(--text)',
                      textAlign: 'left',
                      fontSize: '13px',
                      fontWeight: isSelected ? 700 : 500,
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    {String.fromCharCode(65 + oIdx)}. {opt}
                  </button>
                );
              })}
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '24px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={handlePrev} 
                disabled={currentQ === 0}
                style={{ padding: '6px 12px', fontSize: '12px' }}
              >
                ◀ Previous
              </button>
              
              {currentQ < GK_QUESTIONS.length - 1 ? (
                <button 
                  className="btn btn-primary" 
                  onClick={handleNext}
                  style={{ padding: '6px 12px', fontSize: '12px' }}
                >
                  Next ▶
                </button>
              ) : (
                <button 
                  className="btn btn-success" 
                  onClick={handleSubmitTest}
                  disabled={userAnswers.includes(-1)}
                  style={{ padding: '6px 16px', fontSize: '12px', fontWeight: 700 }}
                >
                  ✓ Submit Test
                </button>
              )}
            </div>
          </div>
        )}

        {step === 'success' && (
          <div style={{ textAlign: 'center', padding: '10px 0' }}>
            <span style={{ fontSize: '48px', display: 'block', marginBottom: '12px' }}>🎉</span>
            <h2 style={{ fontSize: '18px', fontWeight: 800, color: 'var(--success)', margin: '0 0 10px 0' }}>
              Proctoring Verification Completed!
            </h2>
            <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5', margin: '0 0 24px 0' }}>
              Your camera, microphone, screen share, and MediaPipe FaceMesh proctoring logic were verified successfully. 
              You are ready for the actual proctored exam workspace!
              <br/><br/>
              <em>Note: Since this was a simulation, no marks or integrity records were stored on the server.</em>
            </p>
            <button 
              className="btn btn-primary" 
              onClick={onClose}
              style={{ width: '100%', padding: '10px', fontSize: '13px', fontWeight: 700 }}
            >
              Close Window
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
