import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { ReviewService } from '@/services/review.service';
import { ReportCacheManager } from '@/lib/reportCache';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { attemptId, examId, revieweeCode, questionReviews, totalScore } = body;
    const studentCode = student.userData?.studentCode;

    if (!attemptId || !examId || !revieweeCode || !questionReviews || totalScore === undefined || !studentCode) {
      return NextResponse.json({ message: 'Missing parameters (attemptId, examId, revieweeCode, questionReviews, totalScore).' }, { status: 400 });
    }

    await ReviewService.submitPeerReview({
      studentCode,
      attemptId,
      examId,
      revieweeCode,
      questionReviews,
      totalScore
    });

    // Invalidate the cache report for the teacher final review list to prevent showing a stale empty list
    await ReportCacheManager.invalidateReport(`exam-report-subjective-${examId}`).catch(() => null);
    await ReportCacheManager.invalidateReport(`truth-test-report-${examId}`).catch(() => null);

    return NextResponse.json({ success: true, message: 'Peer review submitted successfully.' });

  } catch (error: any) {
    console.error('API subjective peer review submit error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
