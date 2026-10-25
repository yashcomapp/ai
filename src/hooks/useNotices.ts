'use client';

import { useState, useEffect, useCallback, useMemo } from 'react';
import { Notice } from '@/types/notice.types';

export interface UseNoticesOptions {
  role: 'student' | 'parent';
  firebaseUser?: { uid?: string; getIdToken: () => Promise<string> } | null;
}

export function useNotices({ role, firebaseUser }: UseNoticesOptions) {
  const [notices, setNotices] = useState<Notice[]>([]);
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);
  const [showSeenNotices, setShowSeenNotices] = useState(false);
  const [activeOverlayNotice, setActiveOverlayNotice] = useState<Notice | null>(null);

  // Load notices and sync seen/dismissed state
  useEffect(() => {
    if (!firebaseUser) return;

    let isMounted = true;
    const loadNotices = async () => {
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch('/api/notices', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        if (res.ok) {
          const resData = await res.json();
          if (isMounted) {
            const filtered: Notice[] = resData.notices || [];
            setNotices(filtered);

            const userId = firebaseUser?.uid || role;
            const serverSeenIds: string[] = filtered.filter((n: any) => n.seen).map((n: any) => n.id);

            // Synchronize seen status from server
            const stored = localStorage.getItem('yc_seenNotices');
            let seenIds: string[] = [];
            if (stored) {
              try {
                seenIds = JSON.parse(stored);
              } catch (e) {}
            }
            const mergedSeen = Array.from(new Set([...seenIds, ...serverSeenIds]));
            const validSeenIds = mergedSeen.filter((id: string) => filtered.some((n: any) => n.id === id));
            localStorage.setItem('yc_seenNotices', JSON.stringify(validSeenIds));
            setSeenNoticeIds(validSeenIds);
            window.dispatchEvent(new Event('yc_seen_notices_changed'));

            // Check for overlay notices that are not dismissed yet
            const dismissedStored = localStorage.getItem(`yc_dismissed_overlays_${userId}`);
            let dismissedIds: string[] = [];
            if (dismissedStored) {
              try {
                dismissedIds = JSON.parse(dismissedStored);
              } catch (e) {}
            }
            const mergedDismissed = Array.from(new Set([...dismissedIds, ...serverSeenIds]));
            localStorage.setItem(`yc_dismissed_overlays_${userId}`, JSON.stringify(mergedDismissed));

            const activeOverlay = filtered.find((n: any) => n.isOverlay && !mergedDismissed.includes(n.id));
            if (activeOverlay) {
              setActiveOverlayNotice(activeOverlay);
            }
          }
        }
      } catch (err) {
        console.warn(`Failed to fetch ${role} notices via API:`, err);
      }
    };

    loadNotices();

    const handleSeenChange = () => {
      const stored = localStorage.getItem('yc_seenNotices');
      if (stored) {
        try {
          setSeenNoticeIds(JSON.parse(stored));
        } catch (e) {}
      }
    };
    window.addEventListener('yc_seen_notices_changed', handleSeenChange);

    return () => {
      isMounted = false;
      window.removeEventListener('yc_seen_notices_changed', handleSeenChange);
    };
  }, [firebaseUser, role]);

  // Dismiss overlay notice handler
  const handleDismissOverlayNotice = useCallback(
    async (noticeId: string, reason?: string, remarks?: string) => {
      const userId = firebaseUser?.uid || role;
      const dismissedStored = localStorage.getItem(`yc_dismissed_overlays_${userId}`);
      let dismissedIds: string[] = [];
      if (dismissedStored) {
        try {
          dismissedIds = JSON.parse(dismissedStored);
        } catch (e) {}
      }
      if (!dismissedIds.includes(noticeId)) {
        dismissedIds.push(noticeId);
        localStorage.setItem(`yc_dismissed_overlays_${userId}`, JSON.stringify(dismissedIds));
      }

      // Mark as seen locally
      const alreadySeen = seenNoticeIds.includes(noticeId);
      if (!alreadySeen) {
        const updated = [...seenNoticeIds, noticeId];
        setSeenNoticeIds(updated);
        localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
        window.dispatchEvent(new Event('yc_seen_notices_changed'));
      }

      // Report to server if not seen or reason provided
      if ((!alreadySeen || reason || remarks) && firebaseUser) {
        try {
          const token = await firebaseUser.getIdToken();
          await fetch('/api/notices/seen', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({
              noticeId,
              reason: reason || undefined,
              remarks: remarks || undefined
            })
          });
        } catch (err) {
          console.warn('Failed to report notice seen status:', err);
        }
      }

      // Check if there are other unread overlay notices and display them sequentially
      const nextOverlay = notices.find((n: any) => n.isOverlay && n.id !== noticeId && !dismissedIds.includes(n.id));
      if (nextOverlay) {
        setActiveOverlayNotice(nextOverlay);
      } else {
        setActiveOverlayNotice(null);
      }
    },
    [firebaseUser, role, seenNoticeIds, notices]
  );

  // Mark normal notice as seen
  const handleMarkNoticeAsSeen = useCallback(
    async (noticeId: string) => {
      if (seenNoticeIds.includes(noticeId)) return;
      const updated = [...seenNoticeIds, noticeId];
      setSeenNoticeIds(updated);
      try {
        localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
        window.dispatchEvent(new Event('yc_seen_notices_changed'));
      } catch (e) {
        console.warn('Failed to save seen notices to localStorage:', e);
      }

      if (firebaseUser) {
        try {
          const token = await firebaseUser.getIdToken();
          await fetch('/api/notices/seen', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({ noticeId })
          });
        } catch (e) {
          console.warn('Failed to get token for notice seen status:', e);
        }
      }
    },
    [firebaseUser, seenNoticeIds]
  );

  const visibleNotices = useMemo(
    () => notices.filter((n) => n && n.id && !seenNoticeIds.includes(n.id)),
    [notices, seenNoticeIds]
  );

  return {
    notices,
    setNotices,
    seenNoticeIds,
    setSeenNoticeIds,
    visibleNotices,
    showSeenNotices,
    setShowSeenNotices,
    activeOverlayNotice,
    setActiveOverlayNotice,
    handleDismissOverlayNotice,
    handleMarkNoticeAsSeen
  };
}
