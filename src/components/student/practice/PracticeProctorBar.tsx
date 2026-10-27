'use client';

import React from 'react';
import { formatDuration } from '@/lib/dateUtils';

interface PracticeProctorBarProps {
  videoRef?: React.RefObject<HTMLVideoElement | null>;
  tabViolations?: number;
  noFaceCount?: number;
  lookingAwayCount?: number;
  totalSeconds: number;
  currentQSeconds: number;
  topicCode?: string;
  topicName?: string;
}

export function PracticeProctorBar({
  totalSeconds,
  currentQSeconds,
  topicCode,
  topicName
}: PracticeProctorBarProps) {
  return (
    <div className="proctor-bar" style={{ background: 'var(--surface)', color: 'var(--text)', padding: '10px 20px', borderBottom: '1px solid var(--border-light)' }}>
      <div className="proctor-top-row" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span style={{ 
            background: 'var(--accent-soft)', 
            color: 'var(--accent)', 
            fontSize: '11px', 
            fontWeight: 700, 
            padding: '4px 10px', 
            borderRadius: '12px' 
          }}>
            🎯 Self-Paced Practice
          </span>
          {(topicName || topicCode) && (
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)' }}>
              {topicName || topicCode}
            </span>
          )}
        </div>

        <div className="proctor-timer" style={{ display: 'flex', gap: '20px', fontSize: '13px', fontWeight: 600 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '12px' }}>Total Time:</span>
            <span style={{ color: 'var(--accent)' }}>⏱️ {formatDuration(totalSeconds)}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '12px' }}>This Question:</span>
            <span>❓ {formatDuration(currentQSeconds)}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
