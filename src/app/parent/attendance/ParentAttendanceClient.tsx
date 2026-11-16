'use client';

import React, { Component, ErrorInfo, ReactNode, Suspense } from 'react';
import dynamic from 'next/dynamic';

const AttendanceManager = dynamic(() => import('@/components/AttendanceManager'), { 
  ssr: false,
  loading: () => (
    <div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>
      <div style={{ fontSize: '24px', marginBottom: '8px' }}>⏳</div>
      <div>Loading Attendance...</div>
    </div>
  )
});

interface ErrorBoundaryProps {
  children: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

class AttendanceErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('[ParentAttendanceErrorBoundary] Caught error:', error, errorInfo);
  }

  handleReload = () => {
    if (typeof window !== 'undefined') {
      window.location.reload();
    }
  };

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '60vh', padding: '24px', textAlign: 'center' }}>
          <div className="card glass" style={{ maxWidth: '420px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border)' }}>
            <span style={{ fontSize: '2.5rem' }}>⚠️</span>
            <h3 style={{ margin: '12px 0 8px', fontSize: '16px', fontWeight: 800, color: 'var(--text)' }}>
              Attendance Tab Refresh Needed
            </h3>
            <p style={{ margin: '0 0 16px', fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
              Your attendance page encountered an unexpected display issue. Please tap below to refresh the page.
            </p>
            <button 
              className="btn btn-primary" 
              onClick={this.handleReload}
              style={{ width: '100%', padding: '10px', fontWeight: 700 }}
            >
              🔄 Refresh Attendance Page
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}

export default function ParentAttendanceClient() {
  return (
    <AttendanceErrorBoundary>
      <Suspense fallback={
        <div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>
          <div style={{ fontSize: '24px', marginBottom: '8px' }}>⏳</div>
          <div>Loading Attendance...</div>
        </div>
      }>
        <AttendanceManager role="parent" />
      </Suspense>
    </AttendanceErrorBoundary>
  );
}
