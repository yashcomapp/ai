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

/**
 * Distributed Firestore-backed rate limiter for serverless environments (Vercel / Cloud Functions).
 * Safely falls back to allowed if Firestore has temporary connectivity issues.
 */
export async function checkDistributedRateLimit({ key, limit, windowMs }: RateLimitOptions): Promise<RateLimitResult> {
  try {
    const sanitizedKey = key.replace(/[^a-zA-Z0-9_\-]/g, '_').slice(0, 100);
    const docRef = adminDb.collection('_rateLimits').doc(sanitizedKey);
    const now = Date.now();

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
