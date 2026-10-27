'use client';

import React from 'react';
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
  onProceed
}: PracticeHardwareModalProps) {
  if (!isOpen) return null;

  return (
    <ModalShell
      isOpen={isOpen}
      maxWidth="520px"
      width="90%"
      align="flex-start"
      padding="32px 24px"
      backdropBlur="8px"
      zIndex={20000}
    >
      <div style={{ textAlign: 'center' }}>
        <div style={{ fontSize: '28px', marginBottom: '8px' }}>🎯</div>
        <h2 style={{ fontSize: '1.35rem', fontWeight: 800, margin: '0 0 6px' }}>Self-Paced Practice</h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '0 0 18px' }}>
          Review the topic goals and blueprint below, then start your session when you&apos;re ready.
        </p>

        {/* Topic Blueprint & Slab Transparency Card */}
        {topicData && (
          <div style={{
            background: 'var(--bg-soft)',
            border: '1.5px solid var(--border-light)',
            borderRadius: 'var(--radius-sm)',
            padding: '14px 16px',
            textAlign: 'left',
            marginBottom: '20px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '8px', marginBottom: '10px', flexWrap: 'wrap' }}>
              <div style={{ fontWeight: 800, fontSize: '13.5px', color: 'var(--text)' }}>
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
            <div style={{ marginBottom: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
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

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', fontSize: '11.5px', color: 'var(--text-muted)' }}>
              <div>🎯 <strong>This Set:</strong> {topicData.questions?.length || 6} Questions</div>
              <div>⏳ <strong>Ideal Time:</strong> {Math.round((topicData.idealTimeSeconds || 450) / 60)} Mins</div>
              <div>📈 <strong>Current Mastery:</strong> {topicData.masteryAtStart || 0}%</div>
              <div>🛡️ <strong>Pacing:</strong> Set {(topicData.dailySessions || 0) + 1} of {topicData.maxSessionsAllowed || (topicData.topicScope === 'minor' ? 2 : 3)}</div>
            </div>

            <div style={{ fontSize: '11px', color: 'var(--accent)', marginTop: '10px', fontWeight: 600, borderTop: '1px dashed var(--border-light)', paddingTop: '8px' }}>
              💡 Immediate step-by-step solutions and explanations after every answer.
            </div>
          </div>
        )}

        <button 
          className="btn btn-primary" 
          onClick={onProceed} 
          style={{ width: '100%', padding: '12px 20px', fontSize: '14px', fontWeight: 700 }}
        >
          🚀 Start Practice Set
        </button>
      </div>
    </ModalShell>
  );
}
