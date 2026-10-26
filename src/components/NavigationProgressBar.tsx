'use client';

import React, { useEffect, useState, useTransition, Suspense } from 'react';
import { usePathname, useSearchParams } from 'next/navigation';

function ProgressBarInner() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [progress, setProgress] = useState(0);
  const [visible, setVisible] = useState(false);

  // Complete progress on pathname or searchParams change
  useEffect(() => {
    if (visible) {
      setProgress(100);
      const timer = setTimeout(() => {
        setVisible(false);
        setProgress(0);
      }, 250);
      return () => clearTimeout(timer);
    }
  }, [pathname, searchParams]);

  // Intercept internal navigation clicks to start progress bar instantly
  useEffect(() => {
    const handleAnchorClick = (e: MouseEvent) => {
      const target = (e.target as HTMLElement)?.closest('a');
      if (!target) return;

      const href = target.getAttribute('href');
      const targetAttr = target.getAttribute('target');

      // Only handle internal same-tab navigation
      if (
        href &&
        href.startsWith('/') &&
        !href.startsWith('//') &&
        targetAttr !== '_blank' &&
        !e.ctrlKey &&
        !e.metaKey &&
        !e.shiftKey &&
        !e.altKey
      ) {
        const currentUrl = window.location.pathname + window.location.search;
        if (href !== currentUrl && !href.startsWith(`${window.location.pathname}#`)) {
          setVisible(true);
          setProgress(25);
          setTimeout(() => setProgress(prev => (prev < 70 ? 70 : prev)), 120);
        }
      }
    };

    // Custom event to start progress from code (e.g. router.push)
    const handleCustomNavStart = () => {
      setVisible(true);
      setProgress(30);
      setTimeout(() => setProgress(prev => (prev < 75 ? 75 : prev)), 150);
    };

    window.addEventListener('click', handleAnchorClick, true);
    window.addEventListener('app:nav-start', handleCustomNavStart);

    return () => {
      window.removeEventListener('click', handleAnchorClick, true);
      window.removeEventListener('app:nav-start', handleCustomNavStart);
    };
  }, []);

  if (!visible && progress === 0) return null;

  return (
    <div
      aria-hidden="true"
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        height: '2.5px',
        zIndex: 999999,
        pointerEvents: 'none',
        background: 'transparent',
      }}
    >
      <div
        style={{
          height: '100%',
          width: `${progress}%`,
          background: 'linear-gradient(90deg, #d97b38, #f59e0b, #ef4444)',
          boxShadow: '0 0 10px rgba(245, 158, 11, 0.6), 0 0 4px rgba(217, 123, 56, 0.8)',
          transition: progress === 100 ? 'width 0.15s ease-out, opacity 0.2s ease-out' : 'width 0.25s cubic-bezier(0.16, 1, 0.3, 1)',
          opacity: visible ? 1 : 0,
          borderRadius: '0 2px 2px 0'
        }}
      />
    </div>
  );
}

export default function NavigationProgressBar() {
  return (
    <Suspense fallback={null}>
      <ProgressBarInner />
    </Suspense>
  );
}

/**
 * Helper to dispatch navigation start for imperative router.push calls
 */
export function triggerNavStart() {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('app:nav-start'));
  }
}
