import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

// In-memory sliding rate limiter & deduplicator
const ipRequestHistory = new Map<string, number[]>();
const recentErrorDedupe = new Map<string, number>();

const MAX_REQUESTS_PER_MINUTE = 10;
const DEDUPE_WINDOW_MS = 60 * 1000;
const RATE_LIMIT_WINDOW_MS = 60 * 1000;

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const timestamps = (ipRequestHistory.get(ip) || []).filter(t => now - t < RATE_LIMIT_WINDOW_MS);
  if (timestamps.length >= MAX_REQUESTS_PER_MINUTE) {
    return true;
  }
  timestamps.push(now);
  ipRequestHistory.set(ip, timestamps);
  return false;
}

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

    if (isRateLimited(ip)) {
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
    const studentCode = typeof body.studentCode === 'string' ? body.studentCode.slice(0, 50) : null;
    const studentName = typeof body.studentName === 'string' ? body.studentName.slice(0, 100) : null;

    // Deduplicate rapid repeat crashes (e.g. infinite re-render cycles or repeated reloads)
    const errorSignature = `${ip}:${examId || 'general'}:${message}`;
    if (isDuplicate(errorSignature)) {
      return NextResponse.json({ success: true, deduped: true });
    }

    console.warn(`[Client Crash Registered] ${type}: ${message.slice(0, 120)} | examId=${examId} student=${studentCode || 'unknown'}`);

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
        studentCode,
        studentName
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
