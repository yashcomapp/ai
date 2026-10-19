import { useState, useEffect, useCallback, useMemo } from 'react';

/**
 * Utility functions for notice management and seen tracking.
 */
export async function markNoticeAsSeen(
  id: string,
  seenNoticeIds: string[],
  firebaseUser?: { getIdToken: () => Promise<string> } | null
): Promise<string[]> {
  if (seenNoticeIds.includes(id)) return seenNoticeIds;
  const updated = [...seenNoticeIds, id];
  try {
    localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
  } catch (e) {
    console.warn('Failed to save seen notices to localStorage:', e);
  }

  if (firebaseUser) {
    try {
      const idToken = await firebaseUser.getIdToken();
      fetch('/api/notices/seen', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${idToken}`,
        },
        body: JSON.stringify({ noticeId: id }),
      }).catch((err) => console.warn('Failed to report notice seen status:', err));
    } catch (e) {
      console.warn('Failed to get token for notice seen status:', e);
    }
  }

  return updated;
}

/**
 * Shared hook to manage notice seen status, localStorage persistence, backend reporting,
 * and filtering of visible notices across Student and Parent dashboards.
 */
export function useSeenNotices<T extends { id: string }>(
  notices: T[] = [],
  firebaseUser?: { getIdToken: () => Promise<string> } | null
) {
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);

  useEffect(() => {
    try {
      const stored = localStorage.getItem('yc_seenNotices');
      if (stored) {
        setSeenNoticeIds(JSON.parse(stored));
      }
    } catch (e) {
      console.warn('Failed to load seen notices:', e);
    }
  }, []);

  const handleMarkNoticeAsSeen = useCallback(
    async (id: string) => {
      const updated = await markNoticeAsSeen(id, seenNoticeIds, firebaseUser);
      setSeenNoticeIds(updated);
    },
    [seenNoticeIds, firebaseUser]
  );

  const visibleNotices = useMemo(
    () => notices.filter((n) => n && n.id && !seenNoticeIds.includes(n.id)),
    [notices, seenNoticeIds]
  );

  return {
    seenNoticeIds,
    setSeenNoticeIds,
    handleMarkNoticeAsSeen,
    visibleNotices,
  };
}
