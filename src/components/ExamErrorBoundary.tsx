'use client';

import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallbackTitle?: string;
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
  }

  private handleReload = () => {
    if (this.props.onReset) {
      this.props.onReset();
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

            {/* Error Detail (Foldable) */}
            <details style={{
              textAlign: 'left',
              background: 'rgba(0, 0, 0, 0.25)',
              border: '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '8px',
              padding: '8px 12px',
              fontSize: '11px',
              color: '#cbd5e1'
            }}>
              <summary style={{ cursor: 'pointer', fontWeight: 600, color: '#94a3b8' }}>
                Technical Error Details
              </summary>
              <pre style={{
                margin: '8px 0 0',
                padding: '8px',
                background: 'rgba(0, 0, 0, 0.4)',
                borderRadius: '4px',
                overflowX: 'auto',
                whiteSpace: 'pre-wrap',
                wordBreak: 'break-word',
                color: '#f87171',
                fontSize: '11px'
              }}>
                {errorMessage}
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
                onClick={this.handleReturnToDashboard}
                style={{
                  width: '100%',
                  padding: '12px 18px',
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
