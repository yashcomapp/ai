import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { ExamReviewService } from '@/services/examReview.service';

export async function GET(req: NextRequest) {
  try {
    const authHeader = req.headers.get('authorization') || req.headers.get('Authorization');
    const cronSecret = process.env.CRON_SECRET;
    const isCronAuthorized = Boolean(cronSecret && authHeader === `Bearer ${cronSecret}`);

    if (!isCronAuthorized) {
      const adminUser = await verifyRole(req, 'admin');
      if (!adminUser) {
        return NextResponse.json({ message: 'Unauthorized. Admin role or valid Cron Secret required.' }, { status: 403 });
      }
    }

    const studentCode = req.nextUrl?.searchParams?.get('studentCode') || undefined;
    const result = await ExamReviewService.sweepAutonomousReviews(studentCode);
    return NextResponse.json(result);
  } catch (error: any) {
    console.error('API sweep autonomous reviews GET error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const authHeader = req.headers.get('authorization') || req.headers.get('Authorization');
    const cronSecret = process.env.CRON_SECRET;
    const isCronAuthorized = Boolean(cronSecret && authHeader === `Bearer ${cronSecret}`);

    if (!isCronAuthorized) {
      const adminUser = await verifyRole(req, 'admin');
      if (!adminUser) {
        return NextResponse.json({ message: 'Unauthorized. Admin role or valid Cron Secret required.' }, { status: 403 });
      }
    }

    let studentCode: string | undefined = undefined;
    try {
      const body = await req.json();
      if (body && typeof body.studentCode === 'string') {
        studentCode = body.studentCode;
      }
    } catch {
      // Body may be empty if sweeping all students
    }

    const result = await ExamReviewService.sweepAutonomousReviews(studentCode);
    return NextResponse.json(result);
  } catch (error: any) {
    console.error('API sweep autonomous reviews error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
