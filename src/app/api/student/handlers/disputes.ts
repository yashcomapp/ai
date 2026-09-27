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

    // Validate screenshot size to protect Firestore document size limits (max 700KB Base64)
    let safeScreenshotData: string | null = null;
    if (screenshotData && typeof screenshotData === 'string') {
      if (screenshotData.length > 700000) {
        return NextResponse.json({ 
          message: 'Screenshot file is too large (maximum 700KB). Please upload a smaller image or compressed screenshot.' 
        }, { status: 400 });
      }
      safeScreenshotData = screenshotData;
    }

    const resolvedExamId = examId || (topicCode ? `practice_${topicCode}` : (source === 'practice' ? 'practice_self_study' : ''));
    const resolvedExamName = topicCode ? `🎯 Practice & Self-Study • ${topicCode}` : (source === 'practice' ? '🎯 Practice & Self-Study' : (examId || ''));

    // Deterministic doc ID prevents duplicate submissions on rapid click or network retries
    const safeStudent = (studentCode || 'student').trim().replace(/[^a-zA-Z0-9_-]/g, '_');
    const safeQId = (questionCode || questionId || 'q').trim().replace(/[^a-zA-Z0-9_-]/g, '_');
    const safeExam = (resolvedExamId || 'practice').trim().replace(/[^a-zA-Z0-9_-]/g, '_');
    const deterministicDocId = `disp_${safeStudent}_${safeExam}_${safeQId}`;

    const disputeRef = adminDb.collection('questionDisputes').doc(deterministicDocId);
    const disputeData = {
      disputeId: disputeRef.id,
      questionId: questionId || questionCode,
      questionCode: questionCode || questionId,
      questionText: questionText || '',
      topicCode: topicCode || '',
      source,
      examId: resolvedExamId || null,
      examName: resolvedExamName || '',
      sessionId,
      studentCode,
      studentName,
      class: className,
      board,
      reason,
      notes: notes || '',
      screenshotData: safeScreenshotData,
      status: 'pending', // 'pending' | 'approved' | 'rejected'
      createdAt: new Date().toISOString()
    };

    await disputeRef.set(disputeData, { merge: true });

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
