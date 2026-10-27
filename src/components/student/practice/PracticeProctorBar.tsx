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
  videoRef,
  tabViolations = 0,
  noFaceCount = 0,
  lookingAwayCount = 0,
  totalSeconds,
  currentQSeconds,
  topicCode,
  topicName
}: PracticeProctorBarProps) {
  return (
    <div className="proctor-bar" style={{ background: 'var(--surface)', color: 'var(--text)', padding: '8px 20px', borderBottom: '2px solid var(--accent)' }}>
      <div className="proctor-top-row" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '15px', flexWrap: 'wrap' }}>
        <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '10px', position: 'relative', flexShrink: 0 }}>
          {videoRef && (
            <video 
              ref={videoRef as any} 
              autoPlay 
              playsInline 
              muted 
              style={{ width: '90px', height: '68px', borderRadius: 'var(--radius-sm)', border: '2px solid var(--success)', background: 'var(--bg-card)', objectFit: 'cover' }}
            />
          )}
          <div>
            <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Proctoring:</div>
            <span className="badge badge-success" style={{ marginTop: '2px', fontSize: '9.5px', background: 'var(--success)', padding: '2px 8px', borderRadius: '4px' }}>
              🟢 Live Local Monitoring
            </span>
            {(topicName || topicCode) && (
              <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text)', marginTop: '2px', maxWidth: '200px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {topicName || topicCode}
              </div>
            )}
          </div>
        </div>

        <div className="violation-stats" style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center', flex: 1, justifyContent: 'center' }}>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '3px 10px', borderRadius: '16px', fontSize: '11px' }}>
            🚫 Tabs: <strong>{tabViolations}</strong>
          </div>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '3px 10px', borderRadius: '16px', fontSize: '11px' }}>
            👤 Away: <strong>{noFaceCount}</strong>
          </div>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '3px 10px', borderRadius: '16px', fontSize: '11px' }}>
            👁️ Gaze: <strong>{lookingAwayCount}</strong>
          </div>
        </div>

        <div className="proctor-timer" style={{ display: 'flex', gap: '16px', fontSize: '13px', fontWeight: 600 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '11.5px' }}>Total:</span>
            <span style={{ color: 'var(--accent)' }}>⏱️ {formatDuration(totalSeconds)}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ color: 'var(--text-muted)', fontSize: '11.5px' }}>Question:</span>
            <span>❓ {formatDuration(currentQSeconds)}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
