import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getDashboardData } from '@/lib/studentDb';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const { uid } = student.decodedToken;
    const userData = student.userData || {};

    const { searchParams } = new URL(req.url);
    const rangeDays = parseInt(searchParams.get('rangeDays') || '7', 10);

    const data = await getDashboardData(uid, userData, rangeDays);
    return NextResponse.json(data, {
      headers: {
        'Cache-Control': 'private, max-age=15, stale-while-revalidate=30'
      }
    });
  } catch (error: any) {
    console.error('API student dashboard route error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
