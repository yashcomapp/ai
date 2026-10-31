import { mutate } from 'swr';

export class FetchError extends Error {
  status?: number;
  info?: any;

  constructor(message: string, status?: number, info?: any) {
    super(message);
    this.name = 'FetchError';
    this.status = status;
    this.info = info;
  }
}

export async function fetchWithToken(url: string, firebaseUser: any, options?: RequestInit) {
  if (!firebaseUser) return null;
  const idToken = await firebaseUser.getIdToken();
  const res = await fetch(url, {
    ...options,
    headers: {
      'Authorization': `Bearer ${idToken}`,
      ...(options?.headers || {})
    }
  });

  // If server signaled that custom claims were newly synchronized, refresh client ID token
  if (res.headers.get('x-claims-updated') === 'true' && typeof firebaseUser.getIdToken === 'function') {
    firebaseUser.getIdToken(true).catch(() => {});
  }

  if (!res.ok) {
    const errData = await res.json().catch(() => ({}));
    const errorMessage = errData.message || errData.error || `Failed to fetch data from ${url} (Status: ${res.status})`;
    throw new FetchError(errorMessage, res.status, errData);
  }
  return res.json();
}

/**
 * Creates a standard SWR fetcher bound to the provided Firebase user instance.
 */
export function createTokenFetcher(firebaseUser: any) {
  return (url: string) => fetchWithToken(url, firebaseUser);
}

/**
 * Performs a fresh fetch bypassing the browser HTTP cache and immediately
 * updates the SWR in-memory cache without triggering another redundant request.
 */
export async function mutateFresh(key: string, firebaseUser: any) {
  if (!firebaseUser) return;
  try {
    const data = await fetchWithToken(key, firebaseUser, { cache: 'no-store' });
    if (data !== undefined && data !== null) {
      await mutate(key, data, { revalidate: false });
    }
  } catch (err) {
    console.warn(`Failed to mutate fresh data for key ${key}:`, err);
  }
}

