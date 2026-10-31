import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getParentDashboardData } from '@/lib/parentDb';
import { getFromCache, setInCache } from '@/lib/firebase/cache';


export async function GET(req: NextRequest) {
  try {
    const parentAuth = await verifyRole(req, 'parent');
    if (!parentAuth) {
      return NextResponse.json({ message: 'Unauthorized. Parent role required.' }, { status: 403 });
    }

    const parentData = parentAuth.userData;
    const parentEmail = parentData?.email?.toLowerCase() || '';

    const { searchParams } = new URL(req.url);
    const selectedStudentCode = searchParams.get('studentCode') || 'all';
    const rangeDays = parseInt(searchParams.get('rangeDays') || '7', 10);

    const responseHeaders: Record<string, string> = {
      'Cache-Control': 'private, max-age=45, stale-while-revalidate=90'
    };
    if (parentAuth.claimsUpdated) {
      responseHeaders['x-claims-updated'] = 'true';
    }

    const cacheKey = `parent_dashboard_${parentEmail}_${selectedStudentCode}_${rangeDays}`;
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, { headers: responseHeaders });
    }

    const data = await getParentDashboardData(parentEmail, parentData, selectedStudentCode === 'all' ? null : selectedStudentCode, rangeDays);
    if (!data.children || data.children.length === 0) {
      return NextResponse.json({ message: 'No active enrolled students are linked to this parent account. Access is restricted.' }, { status: 403 });
    }
    setInCache(cacheKey, data, 60000); // 60s in-memory cache

    return NextResponse.json(data, { headers: responseHeaders });

  } catch (error: any) {
    console.error('API parent dashboard error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
