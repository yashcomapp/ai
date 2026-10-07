'use client';

import React, { useEffect } from 'react';
import Link from 'next/link';

export default function StudentSectionError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error('[StudentSectionError] Error in student portal:', error);
  }, [error]);

  return (
    <div style={{
      minHeight: '80vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'var(--bg, #0f172a)',
      color: 'var(--text, #f8fafc)',
      padding: '24px'
    }}>
      <div style={{
        maxWidth: '500px',
        width: '100%',
        background: 'var(--surface, #1e293b)',
        border: '1px solid var(--border-light, #334155)',
        borderRadius: '16px',
        padding: '32px 24px',
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'column',
        gap: '16px',
        boxShadow: '0 20px 40px -10px rgba(0, 0, 0, 0.5)'
      }}>
        <div style={{ fontSize: '40px' }}>⚠️</div>
        <h2 style={{ fontSize: '18px', fontWeight: 800, margin: 0 }}>
          Student Portal Notice
        </h2>
        <p style={{ fontSize: '13px', color: 'var(--text-muted, #94a3b8)', lineHeight: '1.6', margin: 0 }}>
          Something unexpected happened while loading this page. Your progress and saved data remain secure.
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
            maxHeight: '80px',
            overflowY: 'auto'
          }}>
            {error.message}
          </div>
        )}

        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '8px' }}>
          <button
            onClick={() => reset()}
            className="btn btn-primary"
            style={{
              padding: '12px',
              borderRadius: '8px',
              fontWeight: 700,
              fontSize: '14px',
              cursor: 'pointer'
            }}
          >
            🔄 Try Again
          </button>

          <Link
            href="/student"
            className="btn btn-secondary"
            style={{
              padding: '10px',
              borderRadius: '8px',
              fontWeight: 600,
              fontSize: '13px',
              textAlign: 'center',
              textDecoration: 'none'
            }}
          >
            🏠 Return to Dashboard
          </Link>
        </div>
      </div>
    </div>
  );
}
