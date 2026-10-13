import { adminAuth, adminDb } from '@/lib/firebase/admin';
import { UserRole } from '@/types/user.types';
import { isStudentBlockedByCurfew } from '@/lib/curfew';

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

export function invalidateUserCache(uid?: string) {
  if (uid) {
    userCache.delete(uid);
  } else {
    userCache.clear();
  }
}

export async function verifyRole(req: Request, role: UserRole): Promise<VerifiedUser | null> {
  const result = await verifyAnyRole(req, [role]);
  if (!result) return null;
  return { decodedToken: result.decodedToken, userData: result.userData };
}

export async function verifyAnyRole(
  req: Request,
  roles: UserRole[]
): Promise<{ decodedToken: any; userData: any; role: UserRole } | null> {
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

  // Rule: Inactive non-admin accounts must be blocked centrally at the authorization boundary
  if (userData.status === 'inactive' && (userData.role || '').toLowerCase() !== 'admin') {
    return null;
  }

  const userRole = (userData.role || '').toLowerCase() as UserRole;
  if (roles.includes(userRole)) {
    // Curfew check for student role (SSOT)
    if (userRole === 'student') {
      const email = decodedToken.email || userData.email || '';
      if (isStudentBlockedByCurfew(email, userData)) {
        return null;
      }
    }
    return { decodedToken, userData, role: userRole };
  }

  return null;
}
