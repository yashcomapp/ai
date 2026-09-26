import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ExamReviewService } from '@/services/examReview.service';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId');
    const status = searchParams.get('status') || 'all';

    let query: FirebaseFirestore.Query = adminDb.collection('questionDisputes');

    if (examId) {
      query = query.where('examId', '==', examId);
    }
    if (status !== 'all') {
      query = query.where('status', '==', status);
    }

    const snap = await query.limit(300).get();

    const disputes = snap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    // Sort by submittedAt ascending so ranking is chronological
    disputes.sort((a: any, b: any) => {
      const timeA = new Date(a.submittedAt || a.createdAt || 0).getTime();
      const timeB = new Date(b.submittedAt || b.createdAt || 0).getTime();
      return timeA - timeB;
    });

    // Group disputes by examId and questionId
    const grouped: Record<string, Record<string, any[]>> = {};
    disputes.forEach((d: any) => {
      const eId = d.examId || 'unassigned_exam';
      const qId = d.questionId || d.questionCode || 'unknown_q';
      if (!grouped[eId]) grouped[eId] = {};
      if (!grouped[eId][qId]) grouped[eId][qId] = [];
      grouped[eId][qId].push(d);
    });

    return NextResponse.json({
      success: true,
      disputes,
      grouped
    });
  } catch (error: any) {
    console.error('API admin get exam disputes error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const body = await req.json();
    const {
      examId,
      questionId,
      newCorrectOption,
      action = 'correct_key', // 'correct_key' | 'bonus_all' | 'quarantine'
      notes = ''
    } = body;

    if (!examId || !questionId) {
      return NextResponse.json({ message: 'Missing required parameters (examId, questionId).' }, { status: 400 });
    }

    const adminEmail = adminUser.decodedToken?.email || 'Admin';

    const result = await ExamReviewService.batchReevaluateExam({
      examId,
      questionId,
      newCorrectOption,
      action,
      notes,
      adminEmail
    });

    return NextResponse.json({
      success: true,
      ...result
    });
  } catch (error: any) {
    console.error('API admin batch reevaluate dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
