'use client';

import React, { useEffect } from 'react';

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error('[GlobalError] Uncaught application error:', error);
  }, [error]);

  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'var(--bg, #0f172a)',
      color: 'var(--text, #f8fafc)',
      padding: '24px',
      fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
    }}>
      <div style={{
        maxWidth: '520px',
        width: '100%',
        background: 'var(--surface, #1e293b)',
        border: '1px solid var(--border-light, #334155)',
        borderRadius: '16px',
        padding: '32px 24px',
        textAlign: 'center',
        boxShadow: '0 20px 40px -10px rgba(0, 0, 0, 0.5)',
        display: 'flex',
        flexDirection: 'column',
        gap: '16px'
      }}>
        <div style={{
          width: '56px',
          height: '56px',
          borderRadius: '50%',
          margin: '0 auto',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '28px',
          background: 'rgba(239, 68, 68, 0.15)',
          border: '1.5px solid #ef4444'
        }}>
          ⚠️
        </div>

        <h2 style={{
          fontSize: '20px',
          fontWeight: 800,
          margin: 0,
          color: 'var(--text, #f8fafc)'
        }}>
          Application Notice
        </h2>

        <p style={{
          fontSize: '14px',
          color: 'var(--text-muted, #94a3b8)',
          lineHeight: '1.6',
          margin: 0
        }}>
          An unexpected interface error occurred. Please tap below to reload the screen and restore your session.
        </p>

        {error?.message && (
          <div style={{
            fontSize: '11px',
            color: '#f87171',
            background: 'rgba(0, 0, 0, 0.3)',
            padding: '8px 12px',
            borderRadius: '6px',
            textAlign: 'left',
            fontFamily: 'monospace',
            wordBreak: 'break-word',
            maxHeight: '100px',
            overflowY: 'auto'
          }}>
            {error.message}
          </div>
        )}

        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '8px' }}>
          <button
            onClick={() => reset()}
            style={{
              width: '100%',
              padding: '12px 20px',
              borderRadius: '8px',
              background: 'var(--accent, #2563eb)',
              color: '#ffffff',
              border: 'none',
              fontWeight: 700,
              fontSize: '14px',
              cursor: 'pointer'
            }}
          >
            🔄 Try Again / Recover
          </button>

          <button
            onClick={() => window.location.reload()}
            style={{
              width: '100%',
              padding: '10px 18px',
              borderRadius: '8px',
              background: 'transparent',
              color: 'var(--text-muted, #94a3b8)',
              border: '1px solid var(--border-light, #334155)',
              fontWeight: 600,
              fontSize: '13px',
              cursor: 'pointer'
            }}
          >
            Reload Page
          </button>
        </div>
      </div>
    </div>
  );
}
