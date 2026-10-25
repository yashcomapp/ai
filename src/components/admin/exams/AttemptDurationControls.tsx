'use client';

import React from 'react';

interface AttemptDurationControlsProps {
  maxAttempts: number;
  onChangeMaxAttempts: (attempts: number) => void;
  showDuration?: boolean;
  overrideDuration?: boolean;
  examDuration?: number | string;
  onChangeOverrideDuration?: (override: boolean) => void;
  onChangeExamDuration?: (dur: number | string) => void;
  onBlurExamDuration?: () => void;
  durationHelperText?: React.ReactNode;
}

export function AttemptDurationControls({
  maxAttempts,
  onChangeMaxAttempts,
  showDuration = true,
  overrideDuration = false,
  examDuration = '',
  onChangeOverrideDuration,
  onChangeExamDuration,
  onBlurExamDuration,
  durationHelperText,
}: AttemptDurationControlsProps) {
  return (
    <div style={{ display: 'flex', gap: '15px' }}>
      <div style={{ flex: 1 }}>
        <label
          style={{
            display: 'block',
            fontSize: '11px',
            fontWeight: 600,
            color: 'var(--text-muted)',
            marginBottom: '4px',
          }}
        >
          Attempt Limit
        </label>
        <select
          value={maxAttempts}
          onChange={(e) => onChangeMaxAttempts(Number(e.target.value))}
          style={{
            width: '100%',
            padding: '5px 6px',
            background: 'var(--surface)',
            color: 'var(--text)',
            border: '1px solid var(--border-light)',
            borderRadius: 'var(--radius-sm)',
          }}
        >
          <option value={1}>1 Attempt</option>
          <option value={2}>2 Attempts</option>
          <option value={3}>3 Attempts</option>
          <option value={-1}>Unlimited</option>
        </select>
      </div>

      {showDuration && (
        <div style={{ flex: 1 }}>
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              marginBottom: '4px',
            }}
          >
            <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
              Duration (Minutes)
            </label>
            <label
              style={{
                fontSize: '11px',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
                cursor: 'pointer',
                color: overrideDuration ? 'var(--primary)' : 'var(--text-muted)',
              }}
            >
              <input
                type="checkbox"
                checked={overrideDuration}
                onChange={(e) => onChangeOverrideDuration?.(e.target.checked)}
                style={{ cursor: 'pointer' }}
              />
              <span>Override</span>
            </label>
          </div>
          <input
            type="number"
            value={examDuration === undefined || examDuration === null ? '' : examDuration}
            disabled={!overrideDuration}
            onChange={(e) => {
              const raw = e.target.value;
              onChangeExamDuration?.(raw === '' ? '' : (isNaN(Number(raw)) ? '' : Number(raw)));
            }}
            onBlur={onBlurExamDuration}
            style={{
              width: '100%',
              padding: '5px 6px',
              background: overrideDuration ? 'var(--surface)' : 'var(--surface-muted, rgba(255, 255, 255, 0.05))',
              color: overrideDuration ? 'var(--text)' : 'var(--text-muted)',
              border: '1px solid var(--border-light)',
              borderRadius: 'var(--radius-sm)',
              cursor: overrideDuration ? 'text' : 'not-allowed',
              opacity: overrideDuration ? 1 : 0.8,
            }}
          />
          {durationHelperText}
        </div>
      )}
    </div>
  );
}
