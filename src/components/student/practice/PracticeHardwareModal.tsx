'use client';

import React from 'react';
import Script from 'next/script';

interface PracticeHardwareModalProps {
  isOpen: boolean;
  topicData: {
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
    questions: any[];
    masteryAtStart: number;
    idealTimeSeconds: number;
    totalAttemptedCount?: number;
  } | null;
  cameraStream: MediaStream | null;
  audioLevel: number;
  cameraStatus: string;
  onRunCheck: () => void;
  onProceed: () => void;
}

export function PracticeHardwareModal({
  isOpen,
  topicData,
  cameraStream,
  audioLevel,
  cameraStatus,
  onRunCheck,
  onProceed
}: PracticeHardwareModalProps) {
  if (!isOpen) return null;

  return (
    <>
      <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
      <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />

      <div className="camera-modal" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'flex-start', justifyContent: 'center', padding: '40px 20px', overflowY: 'auto' }}>
        <div className="camera-modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius)', padding: '30px', maxWidth: '500px', width: '90%', textAlign: 'center', boxShadow: 'var(--shadow-lg)', margin: '0 auto' }}>
          <h2>System Hardware Pre-Check</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '10px 0 16px' }}>
            Verify your camera and microphone are working correctly before starting this proctored practice session.
          </p>

          {/* Topic Blueprint & Slab Transparency Card */}
          {topicData && (
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
                  📍 {topicData.topicName || topicData.topicCode}
                </div>
                <span style={{
                  fontSize: '10px',
                  fontWeight: 700,
                  textTransform: 'uppercase',
                  padding: '2px 8px',
                  borderRadius: '4px',
                  background: (topicData.topicScope === 'minor' || topicData.topicClassification === 'minor' || topicData.topicClassification === 'micro') ? 'var(--success-bg)' : (topicData.topicScope === 'major' || topicData.topicClassification === 'major' || topicData.topicClassification === 'calculative' || topicData.topicClassification === 'hots') ? 'var(--danger-bg)' : 'var(--info-bg)',
                  color: (topicData.topicScope === 'minor' || topicData.topicClassification === 'minor' || topicData.topicClassification === 'micro') ? 'var(--success)' : (topicData.topicScope === 'major' || topicData.topicClassification === 'major' || topicData.topicClassification === 'calculative' || topicData.topicClassification === 'hots') ? 'var(--danger)' : 'var(--info)',
                  border: `1px solid ${(topicData.topicScope === 'minor' || topicData.topicClassification === 'minor' || topicData.topicClassification === 'micro') ? 'rgba(52, 211, 153, 0.3)' : (topicData.topicScope === 'major' || topicData.topicClassification === 'major' || topicData.topicClassification === 'calculative' || topicData.topicClassification === 'hots') ? 'rgba(248, 113, 113, 0.3)' : 'rgba(56, 189, 248, 0.3)'}`
                }}>
                  {(topicData.topicScope === 'minor' || topicData.topicClassification === 'minor' || topicData.topicClassification === 'micro') && '📘 Minor (6 Qs to Master • Max 2 Sets)'}
                  {(topicData.topicScope === 'medium' || topicData.topicClassification === 'medium' || topicData.topicClassification === 'moderate' || topicData.topicClassification === 'conceptual') && '📙 Medium (10 Qs to Master • Max 3 Sets)'}
                  {(topicData.topicScope === 'major' || topicData.topicClassification === 'major' || topicData.topicClassification === 'calculative' || topicData.topicClassification === 'hots') && '📕 Major (15 Qs to Master • Max 3 Sets)'}
                  {!topicData.topicScope && !topicData.topicClassification && '📙 Standard (10 Qs to Master • Max 3 Sets)'}
                </span>
              </div>

              {/* Progress bar towards Required Slab */}
              <div style={{ marginBottom: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>
                  <span>Confidence Progress (Score ≥ 90% Needed)</span>
                  <strong>{topicData.totalAttemptedCount || 0} / {topicData.requiredConfidence || (topicData.topicScope === 'minor' ? 6 : topicData.topicScope === 'major' ? 15 : 10)} Qs Practiced</strong>
                </div>
                <div style={{ height: '6px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                  <div style={{
                    height: '100%',
                    background: 'var(--accent)',
                    width: `${Math.min(100, Math.round(((topicData.totalAttemptedCount || 0) / Math.max(1, topicData.requiredConfidence || (topicData.topicScope === 'minor' ? 6 : topicData.topicScope === 'major' ? 15 : 10))) * 100))}%`,
                    transition: 'width 0.3s ease'
                  }}></div>
                </div>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', fontSize: '11px', color: 'var(--text-muted)' }}>
                <div>🎯 <strong>This Set:</strong> {topicData.questions?.length || 6} Questions</div>
                <div>⏳ <strong>Ideal Time:</strong> {Math.round((topicData.idealTimeSeconds || 450) / 60)} Mins</div>
                <div>📈 <strong>Current Mastery:</strong> {topicData.masteryAtStart || 0}%</div>
                <div>🛡️ <strong>Pacing:</strong> Set {(topicData.dailySessions || 0) + 1} of {topicData.maxSessionsAllowed || (topicData.topicScope === 'minor' ? 2 : 3)}</div>
              </div>

              <div style={{ fontSize: '10.5px', color: 'var(--accent)', marginTop: '8px', fontWeight: 600, borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                🔒 Dedicated Practice Vault (0% Exam Leakage) • Score ≥90% &amp; reach slab to earn Mastered!
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
            <button className="btn btn-primary" onClick={onRunCheck} style={{ width: '100%' }}>
              Test Camera & Microphone
            </button>
          ) : (
            <button className="btn btn-success" onClick={onProceed} style={{ width: '100%' }}>
              Start Practice / Proceed
            </button>
          )}
        </div>
      </div>
    </>
  );
}
