'use client';

import React, { useEffect, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { usePathname } from 'next/navigation';
import { getDateKeyIST } from '@/lib/dateUtils';

export default function TimeTracker() {
  const { firebaseUser, user } = useAuth();
  const pathname = usePathname();
  const pendingSecondsRef = useRef(0);
  const lastFlushTimeRef = useRef(Date.now());
  const idTokenRef = useRef<string | null>(null);

  const lastActivityRef = useRef(Date.now());
  const IDLE_TIMEOUT_MS = 60000; // 60 seconds of inactivity = idle

  const pathnameRef = useRef(pathname);
  useEffect(() => {
    pathnameRef.current = pathname;
  }, [pathname]);

  const getPageTitle = () => {
    if (typeof document === 'undefined') return pathnameRef.current;
    return document.title || pathnameRef.current;
  };

  const getPresenceState = () => {
    if (typeof document === 'undefined') return 'active';
    if (document.visibilityState !== 'visible' || !document.hasFocus()) {
      return 'background';
    }
    const isIdle = (Date.now() - lastActivityRef.current) >= IDLE_TIMEOUT_MS;
    return isIdle ? 'idle' : 'active';
  };

  const flushTime = async (forcedPresence?: string) => {
    if (!firebaseUser || !user) return;
    const toFlush = pendingSecondsRef.current;
    pendingSecondsRef.current = 0;
    lastFlushTimeRef.current = Date.now();

    const currentPresence = forcedPresence || getPresenceState();

    try {
      const idToken = await firebaseUser.getIdToken();
      idTokenRef.current = idToken;
      await fetch('/api/user/time-log', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          secondsToFlush: toFlush,
          dateKey: getDateKeyIST(),
          currentPage: getPageTitle(),
          currentPagePath: pathnameRef.current,
          presenceState: currentPresence
        })
      });
    } catch (err) {
      pendingSecondsRef.current += toFlush;
      console.warn('TimeTracker flush failed:', err);
    }
  };

  useEffect(() => {
    if (!firebaseUser) return;
    firebaseUser.getIdToken().then(token => {
      idTokenRef.current = token;
    }).catch(() => {});
  }, [firebaseUser]);

  useEffect(() => {
    if (!firebaseUser || !user) return;

    pendingSecondsRef.current = 0;
    lastActivityRef.current = Date.now();

    const TICK_INTERVAL = 5000; 

    // User interaction activity listener
    const resetActivity = () => {
      lastActivityRef.current = Date.now();
    };

    const activityEvents = ['mousemove', 'mousedown', 'keydown', 'touchstart', 'scroll', 'click'];
    activityEvents.forEach(evt => {
      window.addEventListener(evt, resetActivity, { passive: true });
    });

    const handleTick = () => {
      const isVisibleAndFocused = document.hasFocus() && document.visibilityState === 'visible';
      const isInteracting = (Date.now() - lastActivityRef.current) < IDLE_TIMEOUT_MS;

      if (isVisibleAndFocused && isInteracting) {
        pendingSecondsRef.current += TICK_INTERVAL / 1000;

        // Periodically flush active time and update presence status (every 300 seconds / 5 minutes)
        const timeSinceLastFlush = Date.now() - lastFlushTimeRef.current;
        if (timeSinceLastFlush >= 300000) {
          flushTime('active');
        }
      } else if (isVisibleAndFocused && !isInteracting) {
        // User is idle on screen - update presence to idle
        const timeSinceLastFlush = Date.now() - lastFlushTimeRef.current;
        if (timeSinceLastFlush >= 300000) {
          flushTime('idle');
        }
      }
    };

    const tickTimer = setInterval(handleTick, TICK_INTERVAL);

    const handleVisibilityChange = () => {
      if (document.visibilityState === 'hidden') {
        flushTime('background');
      } else {
        resetActivity();
      }
    };

    const handleWindowBlur = () => {
      flushTime('background');
    };

    const handleWindowFocus = () => {
      resetActivity();
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('blur', handleWindowBlur);
    window.addEventListener('focus', handleWindowFocus);

    const handleBeforeUnload = () => {
      const token = idTokenRef.current;
      if (token) {
        const toFlush = pendingSecondsRef.current;
        pendingSecondsRef.current = 0;
        
        const url = '/api/user/time-log';
        fetch(url, {
          method: 'POST',
          keepalive: true,
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            secondsToFlush: toFlush,
            dateKey: getDateKeyIST(),
            currentPage: getPageTitle(),
            currentPagePath: pathnameRef.current,
            presenceState: 'offline'
          })
        }).catch(() => {});
      }
    };

    window.addEventListener('beforeunload', handleBeforeUnload);

    return () => {
      clearInterval(tickTimer);
      activityEvents.forEach(evt => {
        window.removeEventListener(evt, resetActivity);
      });
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('blur', handleWindowBlur);
      window.removeEventListener('focus', handleWindowFocus);
      window.removeEventListener('beforeunload', handleBeforeUnload);
      flushTime('background');
    };
  }, [firebaseUser, user]);

  return null;
}
