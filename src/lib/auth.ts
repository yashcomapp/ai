import { adminAuth, adminDb } from '@/lib/firebase/admin';

export interface VerifiedUser {
  decodedToken: any;
  userData: any;
}

export async function verifyToken(req: Request): Promise<any | null> {
  const authHeader = req.headers.get('Authorization');
  if (!authHeader || !authHeader.startsWith('Bearer ')) return null;
  const token = authHeader.split('Bearer ')[1];
  try {
    const decodedToken = await adminAuth.verifyIdToken(token);
    return decodedToken;
  } catch (err) {
    return null;
  }
}

// In-memory cache for user data to avoid redundant Firestore gets on every API request
const userCache = new Map<string, { data: any; expiresAt: number }>();
const CACHE_TTL_MS = 60000; // 60 seconds

export async function verifyRole(req: Request, role: 'admin' | 'student' | 'parent'): Promise<VerifiedUser | null> {
  const result = await verifyAnyRole(req, [role]);
  if (!result) return null;
  return { decodedToken: result.decodedToken, userData: result.userData };
}

export async function verifyAnyRole(
  req: Request,
  roles: ('admin' | 'student' | 'parent')[]
): Promise<{ decodedToken: any; userData: any; role: 'admin' | 'student' | 'parent' } | null> {
  const decodedToken = await verifyToken(req);
  if (!decodedToken) return null;

  const uid = decodedToken.uid;
  const now = Date.now();
  let userData: any = null;

  const cached = userCache.get(uid);
  if (cached && cached.expiresAt > now) {
    userData = cached.data;
  } else {
    try {
      const userDoc = await adminDb.collection('users').doc(uid).get();
      if (userDoc.exists) {
        userData = userDoc.data()!;
        userCache.set(uid, { data: userData, expiresAt: now + CACHE_TTL_MS });

        // Cache cleanup sweep
        if (userCache.size > 1000) {
          for (const [k, v] of userCache.entries()) {
            if (v.expiresAt < now) userCache.delete(k);
          }
        }
      }
    } catch (err) {
      return null;
    }
  }

  if (!userData) return null;

  const userRole = (userData.role || '').toLowerCase() as 'admin' | 'student' | 'parent';
  if (roles.includes(userRole)) {
    // Curfew check for student role
    if (userRole === 'student') {
      const email = (decodedToken.email || userData.email || '').toLowerCase();
      const curfewBypassEmail = (process.env.CURFEW_BYPASS_EMAIL || '').toLowerCase();
      if (email !== curfewBypassEmail && !userData.curfewBypass) {
        const nowUtc = Date.now();
        const istOffset = 5.5 * 60 * 60 * 1000;
        const istDate = new Date(nowUtc + istOffset);
        const hours = istDate.getUTCHours();
        const minutes = istDate.getUTCMinutes();
        const isCurfew = hours > 22 || (hours === 22 && minutes >= 30) || hours < 5;
        if (isCurfew) {
          return null;
        }
      }
    }
    return { decodedToken, userData, role: userRole };
  }

  return null;
}
