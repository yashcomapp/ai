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

export const PracticeProctorBar = React.memo(function PracticeProctorBar({
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
    <div className="practice-proctor-bar" style={{ background: 'var(--surface)', color: 'var(--text)', borderBottom: '2px solid var(--accent)' }}>
      <style>{`
        .practice-proctor-bar {
          padding: 6px 16px;
        }
        .proctor-top-row {
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 12px;
          flex-wrap: wrap;
        }
        .camera-video-el {
          width: 80px;
          height: 60px;
          border-radius: var(--radius-sm);
          border: 2px solid var(--success);
          background: var(--bg-card);
          object-fit: cover;
        }
        @media (max-width: 640px) {
          .practice-proctor-bar {
            padding: 4px 8px !important;
          }
          .proctor-top-row {
            gap: 6px !important;
            flex-wrap: nowrap !important;
          }
          .camera-video-el {
            width: 44px !important;
            height: 33px !important;
          }
          .proctor-label-text {
            display: none !important;
          }
          .proctor-topic-title {
            max-width: 90px !important;
            font-size: 10px !important;
          }
          .violation-stats {
            gap: 4px !important;
          }
          .violation-item {
            padding: 2px 6px !important;
            font-size: 10px !important;
          }
          .proctor-timer {
            gap: 6px !important;
            font-size: 11px !important;
          }
        }
      `}</style>
      <div className="proctor-top-row">
        <div className="camera-feed" style={{ display: 'flex', alignItems: 'center', gap: '8px', position: 'relative', flexShrink: 0 }}>
          {videoRef && (
            <video 
              ref={videoRef as any} 
              autoPlay 
              playsInline 
              muted 
              className="camera-video-el"
            />
          )}
          <div>
            <span className="badge badge-success proctor-label-text" style={{ fontSize: '9px', background: 'var(--success)', padding: '1px 6px', borderRadius: '4px', display: 'inline-block' }}>
              🟢 Live
            </span>
            {(topicName || topicCode) && (
              <div className="proctor-topic-title" style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text)', maxWidth: '180px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {topicName || topicCode}
              </div>
            )}
          </div>
        </div>

        <div className="violation-stats" style={{ display: 'flex', gap: '6px', alignItems: 'center', flexShrink: 0 }}>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '2px 8px', borderRadius: '14px', fontSize: '11px' }}>
            🚫 <strong>{tabViolations}</strong>
          </div>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '2px 8px', borderRadius: '14px', fontSize: '11px' }}>
            👤 <strong>{noFaceCount}</strong>
          </div>
          <div className="violation-item" style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '2px 8px', borderRadius: '14px', fontSize: '11px' }}>
            👁️ <strong>{lookingAwayCount}</strong>
          </div>
        </div>

        <div className="proctor-timer" style={{ display: 'flex', gap: '10px', fontSize: '12px', fontWeight: 600, flexShrink: 0 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
            <span style={{ color: 'var(--accent)' }}>⏱️ {formatDuration(totalSeconds)}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
            <span>❓ {formatDuration(currentQSeconds)}</span>
          </div>
        </div>
      </div>
    </div>
  );
});
