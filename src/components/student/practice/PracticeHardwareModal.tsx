'use client';

import React from 'react';
import Script from 'next/script';
import ModalShell from '@/components/common/ModalShell';

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
  cameraStream?: MediaStream | null;
  audioLevel?: number;
  cameraStatus?: string;
  onRunCheck?: () => void;
  onProceed: () => void;
}

export function PracticeHardwareModal({
  isOpen,
  topicData,
  cameraStream,
  audioLevel = 0,
  cameraStatus,
  onRunCheck,
  onProceed
}: PracticeHardwareModalProps) {
  if (!isOpen) return null;

  return (
    <>
      <Script src="/libs/mediapipe/face_mesh.js" strategy="lazyOnload" />
      <Script src="/libs/mediapipe/camera_utils.js" strategy="lazyOnload" />

      <ModalShell
        isOpen={isOpen}
        maxWidth="500px"
        width="90%"
        align="flex-start"
        padding="32px 20px"
        backdropBlur="8px"
        zIndex={20000}
      >
        <div style={{ textAlign: 'center' }}>
          <h2 style={{ fontSize: '1.35rem', fontWeight: 800, margin: '0 0 6px' }}>Practice Hardware Check</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '0 0 16px' }}>
            Verify your camera and microphone for live client-side integrity monitoring before starting.
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
                  padding: '2px 8px',
                  borderRadius: '12px',
                  background: 'rgba(59, 130, 246, 0.12)',
                  color: 'var(--accent)',
                  border: '1px solid rgba(59, 130, 246, 0.3)'
                }}>
                  🎯 2 Sets to Master
                </span>
              </div>

              {/* Progress bar towards Required Slab */}
              <div style={{ marginBottom: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>
                  <span>Confidence Progress (Score ≥ 90% Needed)</span>
                  <strong>{topicData.totalAttemptedCount || 0} / 12 Qs Practiced</strong>
                </div>
                <div style={{ height: '6px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                  <div style={{
                    height: '100%',
                    background: 'var(--accent)',
                    width: `${Math.min(100, Math.round(((topicData.totalAttemptedCount || 0) / 12) * 100))}%`,
                    transition: 'width 0.3s ease'
                  }}></div>
                </div>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', fontSize: '11px', color: 'var(--text-muted)' }}>
                <div>🎯 <strong>This Set:</strong> {topicData.questions?.length || 6} Questions</div>
                <div>⏳ <strong>Ideal Time:</strong> {Math.round((topicData.idealTimeSeconds || 450) / 60)} Mins</div>
                <div>📈 <strong>Current Mastery:</strong> {topicData.masteryAtStart || 0}%</div>
                <div>🛡️ <strong>Pacing:</strong> Set {(topicData.dailySessions || 0) + 1} of {topicData.maxSessionsAllowed || 2}</div>
              </div>

              <div style={{ fontSize: '10.5px', color: 'var(--accent)', marginTop: '8px', fontWeight: 600, borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                🔒 Zero Cloud Egress • Client-Side Live Proctoring &amp; Immediate Explanations
              </div>
            </div>
          )}

          <div className="camera-preview" style={{ width: '100%', height: '220px', background: 'var(--bg-card)', borderRadius: 'var(--radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', position: 'relative', marginBottom: '14px' }}>
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
              <div style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Webcam Feed Offline</div>
            )}
          </div>

          {cameraStream && (
            <div style={{ margin: '12px 0 10px', textAlign: 'left' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                <span>🎙️ Microphone Input detection</span>
                <strong>{audioLevel > 0 ? `${audioLevel}%` : 'Silent'}</strong>
              </div>
              <div style={{ height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{ height: '100%', background: 'var(--success)', width: `${audioLevel}%`, transition: 'width 0.1s ease' }}></div>
              </div>
            </div>
          )}

          {cameraStatus && <div className="status-msg" style={{ display: 'block', margin: '8px 0', fontSize: '12px', color: 'var(--text-muted)' }}>{cameraStatus}</div>}
          
          {!cameraStream ? (
            <button className="btn btn-primary" onClick={onRunCheck} style={{ width: '100%', padding: '12px', fontWeight: 700 }}>
              Test Camera &amp; Microphone
            </button>
          ) : (
            <button className="btn btn-success" onClick={onProceed} style={{ width: '100%', padding: '12px', fontWeight: 700 }}>
              🚀 Start Practice Set
            </button>
          )}
        </div>
      </ModalShell>
    </>
  );
}
