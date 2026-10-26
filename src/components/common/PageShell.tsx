'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';

export interface PageHeaderBarProps {
  role?: 'student' | 'parent' | 'admin';
  backHref?: string;
  background?: string;
  zIndex?: number;
  logoutIcon?: 'door' | 'svg';
  children?: React.ReactNode;
}

export function PageHeaderBar({
  role = 'student',
  backHref,
  background,
  zIndex = 10,
  logoutIcon = 'door',
  children
}: PageHeaderBarProps) {
  const router = useRouter();
  const { logout } = useAuth();
  const targetBack = backHref || (role === 'parent' ? '/parent' : role === 'admin' ? '/admin' : '/student');

  return (
    <header
      className="page-header glass"
      style={{
        padding: '8px 16px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        borderRadius: '0',
        borderBottom: '1px solid var(--border-light)',
        background: background || undefined,
        zIndex
      }}
    >
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
        <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push(targetBack)}>
          YASHCOM
        </span>
      </div>
      <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        {children}
        {logoutIcon === 'door' ? (
          <button type="button" className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">
            🚪
          </button>
        ) : (
          <button 
            type="button"
            className="page-header-btn" 
            onClick={() => logout()} 
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              color: 'var(--danger)', 
              cursor: 'pointer',
              flexShrink: 0
            }} 
            title="Logout"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
          </button>
        )}
      </div>
    </header>
  );
}

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
  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <PageHeaderBar role={role} backHref={backHref} logoutIcon="door" />

      <main style={{ flex: 1, padding: '10px 8px', maxWidth, width: '100%', margin: '0 auto' }}>
        {children}
      </main>
    </div>
  );
}

export default PageShell;
