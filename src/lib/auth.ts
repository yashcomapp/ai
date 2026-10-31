import { adminAuth, adminDb } from '@/lib/firebase/admin';
import { UserRole } from '@/types/user.types';
import { isStudentBlockedByCurfew } from '@/lib/curfew';

export interface VerifiedUser {
  decodedToken: any;
  userData: any;
}

/**
 * Synchronizes canonical role, studentCode, batchIds, and studentCodes to Firebase Auth Custom Claims.
 * This ensures firestore.rules can read request.auth.token.role without incurring extra userDoc get() reads.
 */
export async function syncUserCustomClaims(uid: string, userData: any, revokeTokens: boolean = false): Promise<boolean> {
  if (!uid || !userData) return false;
  const role = (userData.role || '').toLowerCase();
  if (!role) return false;

  const claims: Record<string, any> = {
    role,
    studentCode: userData.studentCode || null
  };

  if (role === 'student') {
    claims.batchIds = Array.isArray(userData.batchIds)
      ? userData.batchIds.filter(Boolean)
      : (userData.batchId ? [userData.batchId] : []);
  } else if (role === 'parent') {
    claims.studentCodes = Array.isArray(userData.studentCodes)
      ? userData.studentCodes.filter(Boolean)
      : (userData.studentCode ? [userData.studentCode] : []);
  }

  try {
    await adminAuth.setCustomUserClaims(uid, claims);
    if (revokeTokens) {
      await adminAuth.revokeRefreshTokens(uid).catch(() => {});
    }
    return true;
  } catch (err) {
    console.warn(`Failed to set custom claims for user ${uid}:`, err);
    return false;
  }
}

export function areClaimsEqual(decodedToken: any, userData: any): boolean {
  if (!decodedToken || !userData) return false;
  const userRole = (userData.role || '').toLowerCase();
  const tokenRole = (decodedToken.role || '').toLowerCase();
  if (tokenRole !== userRole) return false;

  const userStudentCode = userData.studentCode || null;
  const tokenStudentCode = decodedToken.studentCode || null;
  if (tokenStudentCode !== userStudentCode) return false;

  if (userRole === 'student') {
    const userBatchIds: string[] = (
      Array.isArray(userData.batchIds)
        ? userData.batchIds.filter(Boolean)
        : (userData.batchId ? [userData.batchId] : [])
    ).map(String).sort();

    const tokenBatchIds: string[] = (
      Array.isArray(decodedToken.batchIds)
        ? decodedToken.batchIds.filter(Boolean)
        : []
    ).map(String).sort();

    if (userBatchIds.length !== tokenBatchIds.length) return false;
    for (let i = 0; i < userBatchIds.length; i++) {
      if (userBatchIds[i] !== tokenBatchIds[i]) return false;
    }
  } else if (userRole === 'parent') {
    const userStudentCodes: string[] = (
      Array.isArray(userData.studentCodes)
        ? userData.studentCodes.filter(Boolean)
        : (userData.studentCode ? [userData.studentCode] : [])
    ).map(String).sort();

    const tokenStudentCodes: string[] = (
      Array.isArray(decodedToken.studentCodes)
        ? decodedToken.studentCodes.filter(Boolean)
        : []
    ).map(String).sort();

    if (userStudentCodes.length !== tokenStudentCodes.length) return false;
    for (let i = 0; i < userStudentCodes.length; i++) {
      if (userStudentCodes[i] !== tokenStudentCodes[i]) return false;
    }
  }

  return true;
}

export async function revokeUserTokens(uid: string): Promise<boolean> {
  if (!uid) return false;
  try {
    await adminAuth.revokeRefreshTokens(uid);
    return true;
  } catch (err) {
    console.warn(`Failed to revoke refresh tokens for user ${uid}:`, err);
    return false;
  }
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

    // Proactively synchronize custom user claims if absent or stale (fully awaited)
    if (!areClaimsEqual(decodedToken, userData)) {
      await syncUserCustomClaims(uid, userData);
    }

    return { decodedToken, userData, role: userRole };
  }

  return null;
}
