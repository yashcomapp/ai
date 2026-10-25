'use client';

import React from 'react';
import ModalShell from '@/components/common/ModalShell';

export interface ExamHardwareCheckModalProps {
  isOpen: boolean;
  diagnosticRunning: boolean;
  cameraStream: MediaStream | null;
  audioLevel?: number;
  cameraStatus?: string;
  permissionBlocked?: boolean;
  micAttemptsRemaining?: number;
  isStartingExam?: boolean;
  examBlueprint?: React.ReactNode;
  adminBypassNode?: React.ReactNode;
  onRunCheck: () => any;
  onProceed: () => any;
}

export default function ExamHardwareCheckModal({
  isOpen,
  diagnosticRunning,
  cameraStream,
  audioLevel = 0,
  cameraStatus = '',
  permissionBlocked = false,
  micAttemptsRemaining = 3,
  isStartingExam = false,
  examBlueprint,
  adminBypassNode,
  onRunCheck,
  onProceed,
}: ExamHardwareCheckModalProps) {
  if (!isOpen) return null;

  return (
    <ModalShell
      isOpen={isOpen}
      maxWidth="480px"
      width="90%"
      align="flex-start"
      padding="40px 20px"
      backdropBlur="8px"
      zIndex={20000}
    >
      <div style={{ textAlign: 'center' }}>
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
            {examBlueprint}
            <h2 style={{ fontSize: '1.4rem', marginBottom: '10px' }}>Hardware Diagnostic Check</h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '0 0 16px' }}>Verify your camera and microphone are functioning before entering the proctored workspace.</p>

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
            
            <div className="camera-preview" style={{ width: '100%', height: '230px', background: 'var(--bg-card)', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative' }}>
              {cameraStream ? (
                <video 
                  ref={(el) => {
                    if (el && el.srcObject !== cameraStream) {
                      el.srcObject = cameraStream;
                      try {
                        const p = el.play();
                        if (p !== undefined) p.catch(() => {});
                      } catch {}
                    }
                  }}
                  autoPlay
                  playsInline
                  muted
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              ) : (
                <div style={{ color: 'var(--text-muted)', fontSize: '12px' }}>Webcam Feed Offline</div>
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
                onClick={onRunCheck} 
                style={{ marginTop: '15px', width: '100%' }}
                disabled={permissionBlocked && micAttemptsRemaining === 0}
              >
                {permissionBlocked ? '❌ Hardware Blocked (Retry)' : 'Test Camera & Microphone'}
              </button>
            ) : (
              <button 
                className="btn btn-success" 
                onClick={onProceed} 
                disabled={isStartingExam}
                style={{ marginTop: '15px', width: '100%' }}
              >
                {isStartingExam ? 'Starting Exam...' : 'Start Exam / Proceed'}
              </button>
            )}

            {adminBypassNode}
          </>
        )}
      </div>
    </ModalShell>
  );
}
