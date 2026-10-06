import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { ExamReviewService } from '@/services/examReview.service';

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
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
