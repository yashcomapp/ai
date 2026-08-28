import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyAnyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const verified = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!verified) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 401 });
    }

    const body = await req.json();
    const { localStorageDump, userAgent } = body;

    if (!localStorageDump || typeof localStorageDump !== 'object') {
      return NextResponse.json({ message: 'Invalid payload.' }, { status: 400 });
    }

    const { decodedToken, userData, role } = verified;
    const uid = decodedToken.uid;
    const studentCode = userData?.studentCode || '';
    const docId = studentCode || uid;

    await adminDb.collection('clientStorageDumps').doc(docId).set({
      userId: uid,
      studentCode: studentCode || null,
      email: decodedToken.email || userData?.email || null,
      role: userData?.role || 'student',
      userAgent: userAgent || null,
      keysCount: Object.keys(localStorageDump).length,
      storageData: localStorageDump,
      lastSyncedAt: new Date().toISOString()
    }, { merge: true });

    return NextResponse.json({ success: true, docId });
  } catch (error: any) {
    console.error('Client storage sync error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
