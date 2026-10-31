import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getDashboardData } from '@/lib/studentDb';
import { getFromCache, setInCache } from '@/lib/firebase/cache';


export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const { uid } = student.decodedToken;
    const userData = student.userData || {};
    const studentCode = userData.studentCode || uid;

    const { searchParams } = new URL(req.url);
    const rangeDays = parseInt(searchParams.get('rangeDays') || '7', 10);

    const responseHeaders: Record<string, string> = {
      'Cache-Control': 'private, max-age=45, stale-while-revalidate=90'
    };
    if (student.claimsUpdated) {
      responseHeaders['x-claims-updated'] = 'true';
    }

    const cacheKey = `student_dashboard_${studentCode}_${rangeDays}`;
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, { headers: responseHeaders });
    }

    const data = await getDashboardData(uid, userData, rangeDays);
    setInCache(cacheKey, data, 60000); // 60s in-memory cache

    return NextResponse.json(data, { headers: responseHeaders });
  } catch (error: any) {
    console.error('API student dashboard route error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
