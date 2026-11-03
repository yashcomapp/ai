import { NextRequest } from 'next/server';
import { getFromCache, setInCache } from '@/lib/firebase/cache';

const BYPASS_COOLDOWN_MS = 15000; // 15 seconds cooldown per user

/**
 * Validates whether a cache bypass request should be honored.
 * 
 * Invariants:
 * 1. An explicit bypass signal must be present:
 *    - Header 'x-bypass-cache' === 'true' (sent by mutateFresh after exams)
 *    - Query param 'fresh' === 'true' or 'refresh' === 'true' (explicit refresh)
 *    * Note: Standard browser 'Cache-Control: no-cache / no-store' headers from DevTools
 *      or browser hard-reloads are deliberately NOT treated as a server-side bypass
 *      to protect against cache evasion and Firestore read spikes.
 * 2. Rate-Limiting: A user can only bypass the server cache once every 15 seconds.
 *    Subsequent requests within the cooldown window will safely use the server cache.
 *    (Uses zero-overhead in-memory TTL to strictly honor Rule 2.U zero-cost cloud invariants
 *    without incurring paid external Redis clusters or burning billable Firestore writes).
 */
export function shouldBypassCache(req: NextRequest, userUidOrKey: string): boolean {
  if (!userUidOrKey) return false;

  const hasExplicitBypassHeader = req.headers.get('x-bypass-cache') === 'true';
  const hasRefreshParam = req.nextUrl.searchParams.get('fresh') === 'true' ||
    req.nextUrl.searchParams.get('refresh') === 'true';

  if (!hasExplicitBypassHeader && !hasRefreshParam) {
    return false;
  }

  const cooldownKey = `bypass_last_${userUidOrKey}`;
  const lastBypass = getFromCache<number>(cooldownKey);
  const now = Date.now();

  if (lastBypass && (now - lastBypass) < BYPASS_COOLDOWN_MS) {
    return false; // Cooldown active, serve from cache
  }

  // Register bypass timestamp
  setInCache(cooldownKey, now, BYPASS_COOLDOWN_MS);
  return true;
}
