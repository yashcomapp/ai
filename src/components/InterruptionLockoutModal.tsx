'use client';

import React, { useState, useEffect } from 'react';

interface InterruptionLockoutModalProps {
  isOpen: boolean;
  tabViolations: number;
  maxViolations?: number;
  isSubmitting?: boolean;
  onManualResume: () => void;
  onTimeoutAutoSubmit?: () => void;
}

export function InterruptionLockoutModal({
  isOpen,
  tabViolations,
  maxViolations = 3,
  isSubmitting = false,
  onManualResume,
  onTimeoutAutoSubmit
}: InterruptionLockoutModalProps) {
  const [secondsRemaining, setSecondsRemaining] = useState<number>(45);

  const isFinalViolation = tabViolations >= maxViolations;
  const isSecondViolation = tabViolations === 2 && maxViolations === 3;

  useEffect(() => {
    if (!isOpen) {
      setSecondsRemaining(45);
      return;
    }

    if (isFinalViolation || isSubmitting) {
      return;
    }

    setSecondsRemaining(45);
    const interval = setInterval(() => {
      setSecondsRemaining(prev => {
        if (prev <= 1) {
          clearInterval(interval);
          if (onTimeoutAutoSubmit) {
            onTimeoutAutoSubmit();
          }
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isOpen, tabViolations, isFinalViolation, isSubmitting, onTimeoutAutoSubmit]);

  if (!isOpen) return null;

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 999999,
        background: 'rgba(15, 23, 42, 0.88)',
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
          background: 'var(--surface-popover, #1e293b)',
          border: isFinalViolation 
            ? '2px solid #ef4444' 
            : isSecondViolation 
              ? '2px solid #f97316' 
              : '2px solid #eab308',
          borderRadius: '16px',
          padding: '28px 24px',
          maxWidth: '480px',
          width: '100%',
          textAlign: 'center',
          boxShadow: '0 20px 40px -15px rgba(0, 0, 0, 0.6)',
          color: 'var(--foreground, #f8fafc)'
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
                ? 'rgba(239, 68, 68, 0.15)'
                : isSecondViolation
                  ? 'rgba(249, 115, 22, 0.15)'
                  : 'rgba(234, 179, 8, 0.15)',
              border: `1px solid ${
                isFinalViolation
                  ? '#ef4444'
                  : isSecondViolation
                    ? '#f97316'
                    : '#eab308'
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
                ? '#ef4444'
                : isSecondViolation
                  ? '#f97316'
                  : '#eab308',
              color: '#0f172a',
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
              color: 'var(--foreground, #ffffff)'
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
            color: 'var(--text-muted, #cbd5e1)',
            marginBottom: '20px',
            textAlign: 'left',
            background: 'rgba(0, 0, 0, 0.25)',
            padding: '14px',
            borderRadius: '10px',
            border: '1px solid rgba(255, 255, 255, 0.08)'
          }}
        >
          {isFinalViolation ? (
            <p style={{ margin: 0, color: '#fca5a5' }}>
              The maximum allowed tab/window departures (<strong>3/3</strong>) have been reached. 
              Your exam is being automatically submitted. All answered questions are saved.
            </p>
          ) : isSecondViolation ? (
            <>
              <p style={{ margin: '0 0 8px', fontWeight: 600, color: '#fed7aa' }}>
                ⚠️ <strong>This was your second violation.</strong>
              </p>
              <p style={{ margin: 0 }}>
                A window switch, phone call, or screen focus loss was detected. 
                <strong> ONE more interruption of any kind will immediately and permanently submit your exam.</strong>
              </p>
            </>
          ) : (
            <>
              <p style={{ margin: '0 0 8px', fontWeight: 600, color: '#fef08a' }}>
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
                color: '#94a3b8',
                marginBottom: '12px'
              }}
            >
              Auto-submits in <strong style={{ color: secondsRemaining <= 10 ? '#ef4444' : '#f8fafc' }}>{secondsRemaining}s</strong> if not resumed
            </div>

            <button
              onClick={onManualResume}
              style={{
                width: '100%',
                padding: '14px 20px',
                borderRadius: '10px',
                background: isSecondViolation ? '#f97316' : '#22c55e',
                color: '#ffffff',
                border: 'none',
                fontWeight: 700,
                fontSize: '16px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
                boxShadow: isSecondViolation
                  ? '0 4px 14px rgba(249, 115, 22, 0.4)'
                  : '0 4px 14px rgba(34, 197, 94, 0.4)',
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
                border: '3px solid rgba(239, 68, 68, 0.3)',
                borderTop: '3px solid #ef4444',
                borderRadius: '50%',
                animation: 'spin 0.8s linear infinite',
                margin: '0 auto 10px'
              }}
            />
            <p style={{ fontSize: '13px', color: '#f8fafc', fontWeight: 600, margin: 0 }}>
              Saving and submitting your responses...
            </p>
          </div>
        )}

        {/* Helpful Mobile Tip */}
        <div
          style={{
            marginTop: '16px',
            paddingTop: '12px',
            borderTop: '1px solid rgba(255, 255, 255, 0.08)',
            fontSize: '11px',
            color: '#94a3b8'
          }}
        >
          💡 <strong>Tip for Mobile:</strong> Turn on <em>&quot;Do Not Disturb&quot; (DND)</em> or block incoming calls to prevent unintentional interruptions.
        </div>
      </div>
    </div>
  );
}
