import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { adminDb } from '@/lib/firebase/admin';
import { resolveParentStudentCodes } from '@/lib/dashboardDbUtils';
import { getStudentLearningData } from '@/lib/studentDb';
import { getFromCache, setInCache } from '@/lib/firebase/cache';
import { shouldBypassCache } from '@/lib/cacheBypassGuard';
import { getStudentMode } from '@/types/user.types';

export async function GET(req: NextRequest) {
  try {
    const parentAuth = await verifyRole(req, 'parent');
    if (!parentAuth) {
      return NextResponse.json({ message: 'Unauthorized. Parent role required.' }, { status: 403 });
    }

    const parentData = parentAuth.userData || {};
    const linkedStudentCodes = await resolveParentStudentCodes(parentData);
    if (!linkedStudentCodes || linkedStudentCodes.length === 0) {
      return NextResponse.json({ message: 'No active enrolled students are linked to this parent account.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const requestedStudentCode = searchParams.get('studentCode');
    const studentCode = (requestedStudentCode && linkedStudentCodes.includes(requestedStudentCode))
      ? requestedStudentCode
      : linkedStudentCodes[0];

    // Find student document per Rule 2D (strictly verify role === 'student')
    const studentSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();

    if (studentSnap.empty) {
      return NextResponse.json({ message: `Student profile not found for code: ${studentCode}` }, { status: 404 });
    }

    const studentUserData = studentSnap.docs[0].data();

    // Enforce Rule 2Y / access boundaries
    if (studentUserData.status === 'inactive') {
      return NextResponse.json({ message: 'The linked student profile is inactive.' }, { status: 403 });
    }
    if (getStudentMode(studentUserData) === 'limited') {
      return NextResponse.json({ message: 'Access Denied: Limited Mode students do not have access to Learning OS.' }, { status: 403 });
    }
    if (studentUserData.autonomous === true || getStudentMode(studentUserData) === 'autonomous') {
      return NextResponse.json({ message: 'Access Denied: Autonomous Student profiles are not monitored via Parent Portal.' }, { status: 403 });
    }

    const bypassCache = shouldBypassCache(req, studentCode);
    const cacheKey = `parent_learning_${studentCode}`;
    const responseHeaders: Record<string, string> = {
      'Cache-Control': 'private, max-age=60, stale-while-revalidate=120'
    };
    if (parentAuth.claimsUpdated) {
      responseHeaders['x-claims-updated'] = 'true';
    }

    if (!bypassCache) {
      const cached = getFromCache<any>(cacheKey);
      if (cached) {
        return NextResponse.json(cached, { headers: responseHeaders });
      }
    }

    const data = await getStudentLearningData(studentUserData, undefined, bypassCache);
    if (studentCode) {
      setInCache(cacheKey, data, 60000); // 60s in-memory cache
    }

    return NextResponse.json(data, { headers: responseHeaders });
  } catch (error: any) {
    console.error('API parent learning error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
