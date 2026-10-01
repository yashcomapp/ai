'use client';

import React from 'react';
import { formatDuration } from '@/lib/dateUtils';

interface PracticeProctorBarProps {
  videoRef: React.RefObject<HTMLVideoElement | null>;
  tabViolations: number;
  noFaceCount: number;
  lookingAwayCount: number;
  totalSeconds: number;
  currentQSeconds: number;
}

export function PracticeProctorBar({
  videoRef,
  tabViolations,
  noFaceCount,
  lookingAwayCount,
  totalSeconds,
  currentQSeconds
}: PracticeProctorBarProps) {
  return (
    <div className="proctor-bar" style={{ background: 'var(--surface)', color: 'var(--text)', padding: '8px 20px', borderBottom: '2px solid var(--warning)' }}>
      <div className="proctor-top-row" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
        <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '10px', position: 'relative', flexShrink: 0 }}>
          <video 
            ref={videoRef as any} 
            autoPlay 
            playsInline 
            muted 
            style={{ width: '100px', height: '75px', borderRadius: 'var(--radius-sm)', border: '2px solid var(--success)', background: 'var(--bg-card)', objectFit: 'cover' }}
          />
          <div>
            <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Integrity Status:</div>
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
          <div>⏱️ Total: {formatDuration(totalSeconds)}</div>
          <div>❓ Q: {formatDuration(currentQSeconds)}</div>
        </div>
      </div>
    </div>
  );
}
