import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode || '';
    const studentName = student.userData?.name || 'Student';
    const className = student.userData?.className || student.userData?.class || '';
    const board = student.userData?.board || '';

    const body = await req.json();
    const {
      questionId,
      questionCode,
      topicCode,
      source = 'practice',
      examId = null,
      sessionId = null,
      reason = 'missing_options',
      notes = '',
      screenshotData = null,
      questionText = ''
    } = body;

    if (!questionId && !questionCode) {
      return NextResponse.json({ message: 'Missing question identifier.' }, { status: 400 });
    }

    const disputeRef = adminDb.collection('questionDisputes').doc();
    const disputeData = {
      disputeId: disputeRef.id,
      questionId: questionId || questionCode,
      questionCode: questionCode || questionId,
      questionText: questionText || '',
      topicCode: topicCode || '',
      source,
      examId,
      sessionId,
      studentCode,
      studentName,
      class: className,
      board,
      reason,
      notes: notes || '',
      screenshotData: screenshotData || null, // Base64 image
      status: 'pending', // 'pending' | 'approved' | 'rejected'
      createdAt: new Date().toISOString()
    };

    await disputeRef.set(disputeData);

    return NextResponse.json({
      success: true,
      message: 'Question dispute submitted successfully.',
      disputeId: disputeRef.id
    });
  } catch (error: any) {
    console.error('API student dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
