import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { ExamReviewService } from '@/services/examReview.service';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const caller = await verifyRole(req, 'student');
    if (!caller) {
      return NextResponse.json({ message: 'Unauthorized. Student session required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId');
    const studentCode = caller.userData?.studentCode || '';

    if (!examId || !studentCode) {
      return NextResponse.json({ message: 'Missing examId or studentCode.' }, { status: 400 });
    }

    const status = await ExamReviewService.getReviewStatus(studentCode, examId);

    return NextResponse.json({
      success: true,
      reviewStatus: status
    });
  } catch (error: any) {
    console.error('API student get exam review status error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const caller = await verifyRole(req, 'student');
    if (!caller) {
      return NextResponse.json({ message: 'Unauthorized. Student session required.' }, { status: 403 });
    }

    const studentCode = caller.userData?.studentCode || '';
    const studentName = caller.userData?.name || 'Student';
    const batchId = caller.userData?.batchId || (Array.isArray(caller.userData?.batchIds) ? caller.userData.batchIds[0] : '');

    const body = await req.json();
    const {
      examId,
      examName,
      reviewedQuestionIds = [],
      challenges = [],
      timeSpentSeconds = 0
    } = body;

    if (!examId || !studentCode) {
      return NextResponse.json({ message: 'Missing examId or studentCode.' }, { status: 400 });
    }

    const result = await ExamReviewService.submitReview({
      studentCode,
      studentName,
      examId,
      examName,
      batchId,
      reviewedQuestionIds,
      challenges,
      timeSpentSeconds
    });

    return NextResponse.json({
      success: true,
      ...result
    });
  } catch (error: any) {
    console.error('API student submit exam review error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
