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
