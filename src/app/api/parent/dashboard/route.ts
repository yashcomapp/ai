import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getParentDashboardData } from '@/lib/parentDb';

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
    const selectedStudentCode = searchParams.get('studentCode');
    const rangeDays = parseInt(searchParams.get('rangeDays') || '7', 10);

    const data = await getParentDashboardData(parentEmail, parentData, selectedStudentCode, rangeDays);

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
