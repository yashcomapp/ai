import crypto from 'crypto';
import { adminDb } from '@/lib/firebase/admin';

export interface RateLimitOptions {
  key: string;
  limit: number;
  windowMs: number;
}

export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
}

// In-memory hot cache to avoid Firestore transaction hits when blocked
const localMemoryLimits = new Map<string, { blockedUntil: number }>();

/**
 * Distributed Firestore-backed rate limiter for serverless environments (Vercel / Cloud Functions).
 * Safely falls back to allowed if Firestore has temporary connectivity issues.
 */
export async function checkDistributedRateLimit({ key, limit, windowMs }: RateLimitOptions): Promise<RateLimitResult> {
  const now = Date.now();
  const cachedBlocked = localMemoryLimits.get(key);
  if (cachedBlocked && cachedBlocked.blockedUntil > now) {
    return { allowed: false, remaining: 0 };
  }

  try {
    const rawClean = key.replace(/[^a-zA-Z0-9_\-]/g, '_');
    const sanitizedKey = rawClean.length <= 64 
      ? rawClean 
      : `${rawClean.slice(0, 32)}_${crypto.createHash('sha256').update(key).digest('hex').slice(0, 24)}`;

    const docRef = adminDb.collection('_rateLimits').doc(sanitizedKey);

    return await adminDb.runTransaction(async (transaction) => {
      const snap = await transaction.get(docRef);
      if (!snap.exists) {
        transaction.set(docRef, { timestamps: [now], expiresAt: new Date(now + windowMs) });
        return { allowed: true, remaining: limit - 1 };
      }

      const data = snap.data() || {};
      const timestamps = Array.isArray(data.timestamps) ? data.timestamps : [];
      const validTimestamps = timestamps.filter((t: number) => typeof t === 'number' && now - t < windowMs);

      if (validTimestamps.length >= limit) {
        localMemoryLimits.set(key, { blockedUntil: now + Math.min(windowMs, 60000) });
        return { allowed: false, remaining: 0 };
      }

      validTimestamps.push(now);
      transaction.set(docRef, { timestamps: validTimestamps, expiresAt: new Date(now + windowMs) }, { merge: true });
      return { allowed: true, remaining: limit - validTimestamps.length };
    });
  } catch (err) {
    console.error('Rate limit transaction error, failing open:', err);
    return { allowed: true, remaining: limit };
  }
}
