'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';

export interface PageShellProps {
  children: React.ReactNode;
  role?: 'student' | 'parent' | 'admin';
  maxWidth?: string;
  backHref?: string;
}

export function PageShell({
  children,
  role = 'student',
  maxWidth = '900px',
  backHref
}: PageShellProps) {
  const router = useRouter();
  const { logout } = useAuth();
  const targetBack = backHref || (role === 'parent' ? '/parent' : role === 'admin' ? '/admin' : '/student');

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Header Bar */}
      <header className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            type="button"
            onClick={() => router.push(targetBack)}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push(targetBack)}>YASHCOM</span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button type="button" className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </header>

      <main style={{ flex: 1, padding: '10px 8px', maxWidth, width: '100%', margin: '0 auto' }}>
        {children}
      </main>
    </div>
  );
}

export default PageShell;
