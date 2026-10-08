import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyToken } from '@/lib/auth';

import { checkDistributedRateLimit } from '@/lib/rateLimit';

export const dynamic = 'force-dynamic';

// In-memory quick deduplicator for repeat loops in the same worker
const recentErrorDedupe = new Map<string, number>();

const MAX_UNAUTH_PER_MINUTE = 3;
const MAX_AUTH_PER_MINUTE = 15;
const DEDUPE_WINDOW_MS = 60 * 1000;
const RATE_LIMIT_WINDOW_MS = 60 * 1000;

function isDuplicate(signature: string): boolean {
  const now = Date.now();
  const lastTime = recentErrorDedupe.get(signature);
  if (lastTime && now - lastTime < DEDUPE_WINDOW_MS) {
    return true;
  }
  recentErrorDedupe.set(signature, now);

  // Periodic memory cleanup
  if (recentErrorDedupe.size > 500) {
    recentErrorDedupe.forEach((t, k) => {
      if (now - t >= DEDUPE_WINDOW_MS) recentErrorDedupe.delete(k);
    });
  }
  return false;
}

export async function POST(req: NextRequest) {
  try {
    const ip = req.headers.get('x-forwarded-for')?.split(',')[0].trim() || 'unknown-ip';

    // Verify token to prevent identity spoofing
    const decodedToken = await verifyToken(req);
    let verifiedUid: string | null = null;
    let verifiedStudentCode: string | null = null;
    let verifiedStudentName: string | null = null;
    let isVerifiedUser = false;

    if (decodedToken) {
      verifiedUid = decodedToken.uid;
      try {
        const userDoc = await adminDb.collection('users').doc(decodedToken.uid).get();
        if (userDoc.exists) {
          const uData = userDoc.data();
          verifiedStudentCode = uData?.studentCode || null;
          verifiedStudentName = uData?.name || uData?.studentName || null;
          isVerifiedUser = true;
        }
      } catch (err: any) {
        console.warn('Failed to resolve authenticated user for crash log:', err?.message);
      }
    }

    const rateLimitKey = verifiedUid ? `crash_user_${verifiedUid}` : `crash_ip_${ip}`;
    const maxLimit = isVerifiedUser ? MAX_AUTH_PER_MINUTE : MAX_UNAUTH_PER_MINUTE;

    const rateLimitResult = await checkDistributedRateLimit({
      key: rateLimitKey,
      limit: maxLimit,
      windowMs: RATE_LIMIT_WINDOW_MS
    });

    if (!rateLimitResult.allowed) {
      return NextResponse.json({ success: false, error: 'Rate limit exceeded' }, { status: 429 });
    }

    const body = await req.json().catch(() => ({}));
    if (!body || typeof body !== 'object') {
      return NextResponse.json({ success: false, error: 'Invalid payload' }, { status: 400 });
    }

    // Size-capped fields
    const message = typeof body.message === 'string' ? body.message.slice(0, 1000) : 'Unknown client crash';
    const stack = typeof body.stack === 'string' ? body.stack.slice(0, 4000) : null;
    const componentStack = typeof body.componentStack === 'string' ? body.componentStack.slice(0, 4000) : null;
    const url = typeof body.url === 'string' ? body.url.slice(0, 1000) : null;
    const userAgent = typeof body.userAgent === 'string' ? body.userAgent.slice(0, 500) : null;
    const type = typeof body.type === 'string' ? body.type.slice(0, 100) : 'Exam Client Crash';
    const examId = typeof body.examId === 'string' ? body.examId.slice(0, 100) : null;

    // Deduplicate rapid repeat crashes (e.g. infinite re-render loops or reload loops)
    const errorSignature = `${rateLimitKey}:${examId || 'general'}:${message}`;
    if (isDuplicate(errorSignature)) {
      return NextResponse.json({ success: true, deduped: true });
    }

    console.warn(`[Client Crash Registered] ${type}: ${message.slice(0, 120)} | examId=${examId} student=${verifiedStudentCode || 'unverified'}`);

    await adminDb.collection('systemFaults').add({
      category: 'client_crash',
      title: type,
      message,
      stack,
      componentStack,
      url,
      userAgent,
      context: {
        examId,
        uid: verifiedUid,
        studentCode: verifiedStudentCode,
        studentName: verifiedStudentName,
        verified: isVerifiedUser
      },
      timestamp: new Date()
    });

    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error('Failed to log client crash:', err?.message || err);
    return NextResponse.json({ success: false, error: err.message }, { status: 500 });
  }
}

// Admin-only retrieval of latest system crashes and client faults
export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const limit = Math.min(100, Math.max(1, parseInt(searchParams.get('limit') || '50', 10)));

    const snapshot = await adminDb.collection('systemFaults')
      .where('category', '==', 'client_crash')
      .orderBy('timestamp', 'desc')
      .limit(limit)
      .get();

    const faults = snapshot.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        ...data,
        timestamp: data.timestamp?.toDate ? data.timestamp.toDate().toISOString() : data.timestamp
      };
    });

    return NextResponse.json({ success: true, faults });
  } catch (err: any) {
    console.error('Failed to fetch client faults:', err?.message || err);
    return NextResponse.json({ message: err.message || 'Internal error' }, { status: 500 });
  }
}
