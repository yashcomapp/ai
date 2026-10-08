'use client';

import React, { Component, ErrorInfo, ReactNode } from 'react';
import { auth } from '@/lib/firebase/client';

interface Props {
  children: ReactNode;
  fallbackTitle?: string;
  examId?: string;
  studentCode?: string;
  onReset?: () => void;
}

interface State {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

export class ExamErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null,
    errorInfo: null
  };

  public static getDerivedStateFromError(error: Error): State {
    return {
      hasError: true,
      error,
      errorInfo: null
    };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('[ExamErrorBoundary] Caught exam interface error:', error, errorInfo);
    this.setState({
      error,
      errorInfo
    });

    // Fire-and-forget report to server for administrative visibility
    try {
      if (typeof window !== 'undefined' && window.location) {
        let examId = this.props.examId || null;
        let studentCode = this.props.studentCode || null;
        let studentName: string | null = null;

        try {
          if (!examId && window.location.search) {
            const sp = new URLSearchParams(window.location.search);
            examId = sp.get('id') || sp.get('examId') || null;
          }
          if (!studentCode && window.localStorage) {
            const sessionStr = window.localStorage.getItem('yc_user_session');
            if (sessionStr) {
              const sess = JSON.parse(sessionStr);
              studentCode = sess.studentCode || sess.code || null;
              studentName = sess.name || sess.studentName || null;
            }
          }
        } catch {}

        (async () => {
          let token: string | null = null;
          try {
            if (auth.currentUser) {
              token = await auth.currentUser.getIdToken();
            }
          } catch {}

          const headers: Record<string, string> = { 'Content-Type': 'application/json' };
          if (token) headers['Authorization'] = `Bearer ${token}`;

          fetch('/api/system/client-error', {
            method: 'POST',
            headers,
            body: JSON.stringify({
              action: 'client_crash',
              type: this.props.fallbackTitle || 'exam_error_boundary',
              url: window.location.href,
              examId,
              message: `${error?.name || 'Error'}: ${error?.message || 'Unknown error'}`,
              stack: error?.stack || null,
              componentStack: errorInfo?.componentStack || null,
              userAgent: navigator.userAgent,
              timestamp: new Date().toISOString()
            })
          }).catch(() => null);
        })();
      }
    } catch {}
  }

  private clearExamLocalCache = () => {
    try {
      if (typeof window !== 'undefined' && window.localStorage) {
        const keysToRemove: string[] = [];
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          if (k && (k.startsWith('exam_state_') || k.startsWith('subjective_exam_state_'))) {
            keysToRemove.push(k);
          }
        }
        keysToRemove.forEach(k => localStorage.removeItem(k));
      }
    } catch {}
  };

  private handleReload = () => {
    this.clearExamLocalCache();
    if (this.props.onReset) {
      try {
        this.props.onReset();
      } catch {}
    }
    window.location.reload();
  };

  private handleClearCacheAndRestart = () => {
    this.clearExamLocalCache();
    if (this.props.onReset) {
      try {
        this.props.onReset();
      } catch {}
    }
    window.location.reload();
  };

  private handleReturnToDashboard = () => {
    window.location.href = '/student';
  };

  public render() {
    if (this.state.hasError) {
      const errorMessage = this.state.error?.message || 'An unexpected rendering error occurred in the exam interface.';

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
            maxWidth: '560px',
            width: '100%',
            background: 'var(--surface-popover, #1e293b)',
            border: '1.5px solid var(--border-popover, #334155)',
            borderRadius: '16px',
            padding: '32px 24px',
            textAlign: 'center',
            boxShadow: '0 20px 40px -10px rgba(0, 0, 0, 0.5)',
            display: 'flex',
            flexDirection: 'column',
            gap: '16px'
          }}>
            <div style={{
              width: '64px',
              height: '64px',
              borderRadius: '50%',
              margin: '0 auto',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '32px',
              background: 'rgba(234, 179, 8, 0.15)',
              border: '1.5px solid #eab308'
            }}>
              🛡️
            </div>

            <h2 style={{
              fontSize: '20px',
              fontWeight: 800,
              margin: '4px 0 0',
              color: 'var(--text, #f8fafc)'
            }}>
              {this.props.fallbackTitle || 'Exam Workspace Recovery'}
            </h2>

            <div style={{
              background: 'rgba(34, 197, 94, 0.1)',
              border: '1px solid rgba(34, 197, 94, 0.3)',
              borderRadius: '10px',
              padding: '12px 14px',
              fontSize: '13px',
              color: '#86efac',
              textAlign: 'left',
              lineHeight: '1.5'
            }}>
              <strong>✓ Your answers are safe:</strong> Your exam progress, answers, and time remaining are automatically preserved in your device&apos;s local storage.
            </div>

            <p style={{
              fontSize: '13px',
              color: 'var(--text-muted, #94a3b8)',
              lineHeight: '1.6',
              margin: 0
            }}>
              A transient script or layout error was detected. You can safely reload the page to resume your exam right where you left off.
            </p>

            {/* Error Detail (Open by default with complete diagnostics) */}
            <details open style={{
              textAlign: 'left',
              background: 'rgba(239, 68, 68, 0.08)',
              border: '1.5px solid rgba(239, 68, 68, 0.35)',
              borderRadius: '8px',
              padding: '10px 14px',
              fontSize: '11px',
              color: '#cbd5e1'
            }}>
              <summary style={{ cursor: 'pointer', fontWeight: 700, color: '#f87171', marginBottom: '8px' }}>
                ⚠️ Technical Error Details ({this.state.error?.name || 'Error'})
              </summary>
              <pre style={{
                margin: '4px 0',
                padding: '8px',
                background: 'rgba(0, 0, 0, 0.5)',
                borderRadius: '4px',
                overflowX: 'auto',
                whiteSpace: 'pre-wrap',
                wordBreak: 'break-word',
                color: '#f87171',
                fontSize: '11px',
                maxHeight: '180px',
                overflowY: 'auto'
              }}>
                {this.state.error?.stack || errorMessage}
                {this.state.errorInfo?.componentStack ? `\n\nComponent Stack:\n${this.state.errorInfo.componentStack}` : ''}
              </pre>
            </details>

            {/* Action Buttons */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '8px' }}>
              <button
                onClick={this.handleReload}
                style={{
                  width: '100%',
                  padding: '14px 20px',
                  borderRadius: '10px',
                  background: 'var(--accent, #2563eb)',
                  color: '#ffffff',
                  border: 'none',
                  fontWeight: 700,
                  fontSize: '15px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  boxShadow: '0 4px 12px rgba(37, 99, 235, 0.3)'
                }}
              >
                🔄 Reload & Resume Exam
              </button>

              <button
                onClick={this.handleClearCacheAndRestart}
                style={{
                  width: '100%',
                  padding: '11px 18px',
                  borderRadius: '10px',
                  background: 'rgba(234, 179, 8, 0.1)',
                  color: '#facc15',
                  border: '1px solid rgba(234, 179, 8, 0.3)',
                  fontWeight: 600,
                  fontSize: '13px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '6px'
                }}
              >
                🧹 Clear Exam Cache & Restart Fresh
              </button>

              <button
                onClick={this.handleReturnToDashboard}
                style={{
                  width: '100%',
                  padding: '11px 18px',
                  borderRadius: '10px',
                  background: 'transparent',
                  color: 'var(--text-muted, #94a3b8)',
                  border: '1px solid var(--border-light, #334155)',
                  fontWeight: 600,
                  fontSize: '13px',
                  cursor: 'pointer'
                }}
              >
                🏠 Return to Student Dashboard
              </button>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ExamErrorBoundary;
