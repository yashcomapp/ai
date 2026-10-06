'use client';

import React, { useState, useEffect } from 'react';

interface InterruptionLockoutModalProps {
  isOpen: boolean;
  tabViolations: number;
  maxViolations?: number;
  durationSeconds?: number;
  isSubmitting?: boolean;
  onManualResume: () => void;
  onTimeoutAutoSubmit?: () => void;
}

export function InterruptionLockoutModal({
  isOpen,
  tabViolations,
  maxViolations = 3,
  durationSeconds = 45,
  isSubmitting = false,
  onManualResume,
  onTimeoutAutoSubmit
}: InterruptionLockoutModalProps) {
  const [secondsRemaining, setSecondsRemaining] = useState<number>(durationSeconds);

  const isFinalViolation = tabViolations >= maxViolations;
  const isSecondViolation = tabViolations === 2 && maxViolations === 3;

  useEffect(() => {
    if (!isOpen || isFinalViolation || isSubmitting) {
      setSecondsRemaining(durationSeconds);
      return;
    }

    const targetEndTime = Date.now() + durationSeconds * 1000;
    setSecondsRemaining(durationSeconds);

    const updateTimer = () => {
      const diffMs = targetEndTime - Date.now();
      const remaining = Math.max(0, Math.ceil(diffMs / 1000));
      setSecondsRemaining(remaining);
      if (remaining <= 0) {
        clearInterval(interval);
        if (onTimeoutAutoSubmit) {
          onTimeoutAutoSubmit();
        }
      }
    };

    // 500ms tick prevents timer drift even if backgrounded or throttled
    const interval = setInterval(updateTimer, 500);

    return () => clearInterval(interval);
  }, [isOpen, tabViolations, isFinalViolation, isSubmitting, durationSeconds, onTimeoutAutoSubmit]);

  if (!isOpen) return null;

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 999999,
        background: 'rgba(17, 19, 24, 0.88)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
        animation: 'fadeInModal 0.2s ease-out'
      }}
    >
      <style dangerouslySetInnerHTML={{
        __html: `
          @keyframes fadeInModal {
            from { opacity: 0; transform: scale(0.96); }
            to { opacity: 1; transform: scale(1); }
          }
          @keyframes pulseWarning {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.08); opacity: 0.85; }
          }
        `
      }} />

      <div
        style={{
          background: 'var(--surface-popover, var(--surface))',
          border: isFinalViolation 
            ? '2px solid var(--danger)' 
            : isSecondViolation 
              ? '2px solid var(--warning)' 
              : '2px solid var(--warning)',
          borderRadius: 'var(--radius-lg, 16px)',
          padding: '28px 24px',
          maxWidth: '480px',
          width: '100%',
          textAlign: 'center',
          boxShadow: 'var(--shadow-lg, 0 20px 40px -15px rgba(0, 0, 0, 0.6))',
          color: 'var(--text)'
        }}
      >
        {/* Icon & Status Header */}
        <div style={{ marginBottom: '16px' }}>
          <div
            style={{
              width: '64px',
              height: '64px',
              borderRadius: '50%',
              margin: '0 auto 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '32px',
              background: isFinalViolation
                ? 'var(--danger-bg)'
                : isSecondViolation
                  ? 'var(--warning-bg)'
                  : 'var(--warning-bg)',
              border: `1px solid ${
                isFinalViolation
                  ? 'var(--danger)'
                  : isSecondViolation
                    ? 'var(--warning)'
                    : 'var(--warning)'
              }`,
              animation: 'pulseWarning 1.5s infinite ease-in-out'
            }}
          >
            {isFinalViolation ? '🛑' : isSecondViolation ? '🚨' : '⚠️'}
          </div>

          <span
            style={{
              display: 'inline-block',
              padding: '4px 12px',
              borderRadius: '999px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.05em',
              background: isFinalViolation
                ? 'var(--danger)'
                : isSecondViolation
                  ? 'var(--warning)'
                  : 'var(--warning)',
              color: 'var(--bg)',
              marginBottom: '8px'
            }}
          >
            {isFinalViolation
              ? 'Limit Reached (3 of 3)'
              : isSecondViolation
                ? 'Final Warning: Strike 2 of 3'
                : 'Interruption: Strike 1 of 3'}
          </span>

          <h2
            style={{
              fontSize: '20px',
              fontWeight: 800,
              margin: '8px 0 4px',
              color: 'var(--text)'
            }}
          >
            {isFinalViolation
              ? 'Exam Auto-Submitting'
              : isSecondViolation
                ? 'Critical Interruption Alert'
                : 'Exam Window Interrupted'}
          </h2>
        </div>

        {/* Informative Body Text */}
        <div
          style={{
            fontSize: '14px',
            lineHeight: 1.55,
            color: 'var(--text-muted)',
            marginBottom: '20px',
            textAlign: 'left',
            background: 'var(--surface-2)',
            padding: '14px',
            borderRadius: 'var(--radius-md, 10px)',
            border: '1px solid var(--border-light)'
          }}
        >
          {isFinalViolation ? (
            <p style={{ margin: 0, color: 'var(--danger-muted, var(--danger))' }}>
              The maximum allowed tab/window departures (<strong>3/3</strong>) have been reached. 
              Your exam is being automatically submitted. All answered questions are saved.
            </p>
          ) : isSecondViolation ? (
            <>
              <p style={{ margin: '0 0 8px', fontWeight: 600, color: 'var(--warning)' }}>
                ⚠️ <strong>This was your second violation.</strong>
              </p>
              <p style={{ margin: 0 }}>
                A window switch, phone call, or screen focus loss was detected. 
                <strong> ONE more interruption of any kind will immediately and permanently submit your exam.</strong>
              </p>
            </>
          ) : (
            <>
              <p style={{ margin: '0 0 8px', fontWeight: 600, color: 'var(--warning)' }}>
                A phone call, notification, or window change was detected.
              </p>
              <p style={{ margin: 0 }}>
                Your exam progress is preserved. Please tap <strong>Resume Exam</strong> below to continue. 
                Reaching 3 strikes will force-submit your test.
              </p>
            </>
          )}
        </div>

        {/* Countdown & Action Area */}
        {!isFinalViolation && !isSubmitting && (
          <div>
            <div
              style={{
                fontSize: '12px',
                color: 'var(--text-muted)',
                marginBottom: '12px'
              }}
            >
              Auto-submits in <strong style={{ color: secondsRemaining <= 10 ? 'var(--danger)' : 'var(--text)' }}>{secondsRemaining}s</strong> if not resumed
            </div>

            <button
              onClick={() => {
                try {
                  window.focus();
                } catch {}
                try {
                  if (!document.fullscreenElement && document.documentElement.requestFullscreen) {
                    document.documentElement.requestFullscreen().catch(() => {});
                  }
                } catch {}
                onManualResume();
              }}
              style={{
                width: '100%',
                padding: '14px 20px',
                borderRadius: 'var(--radius-md, 10px)',
                background: isSecondViolation ? 'var(--warning)' : 'var(--success)',
                color: 'var(--bg)',
                border: 'none',
                fontWeight: 700,
                fontSize: '16px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
                boxShadow: isSecondViolation
                  ? '0 4px 14px var(--accent-ring)'
                  : '0 4px 14px rgba(42, 166, 106, 0.35)',
                transition: 'all 0.15s ease'
              }}
            >
              <span>▶</span> Resume Exam
            </button>
          </div>
        )}

        {(isFinalViolation || isSubmitting) && (
          <div style={{ padding: '10px 0' }}>
            <div
              style={{
                display: 'inline-block',
                width: '28px',
                height: '28px',
                border: '3px solid var(--danger-bg)',
                borderTop: '3px solid var(--danger)',
                borderRadius: '50%',
                animation: 'spin 0.8s linear infinite',
                margin: '0 auto 10px'
              }}
            />
            <p style={{ fontSize: '13px', color: 'var(--text)', fontWeight: 600, margin: 0 }}>
              Saving and submitting your responses...
            </p>
          </div>
        )}

        {/* Helpful Mobile Tip */}
        <div
          style={{
            marginTop: '16px',
            paddingTop: '12px',
            borderTop: '1px solid var(--border-light)',
            fontSize: '11px',
            color: 'var(--text-faint)'
          }}
        >
          💡 <strong>Tip for Mobile:</strong> Turn on <em>&quot;Do Not Disturb&quot; (DND)</em> or block incoming calls to prevent unintentional interruptions.
        </div>
      </div>
    </div>
  );
}
