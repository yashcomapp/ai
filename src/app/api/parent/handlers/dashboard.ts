import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getParentDashboardData } from '@/lib/parentDb';
import { getFromCache, setInCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

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

    const cacheKey = `parent_dashboard_${parentEmail}_${selectedStudentCode}_${rangeDays}`;
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, {
        headers: {
          'Cache-Control': 'private, max-age=15, stale-while-revalidate=30'
        }
      });
    }

    const data = await getParentDashboardData(parentEmail, parentData, selectedStudentCode === 'all' ? null : selectedStudentCode, rangeDays);
    setInCache(cacheKey, data, 20000); // 20s in-memory cache

    return NextResponse.json(data, {
      headers: {
        'Cache-Control': 'private, max-age=15, stale-while-revalidate=30'
      }
    });

  } catch (error: any) {
    console.error('API parent dashboard error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
