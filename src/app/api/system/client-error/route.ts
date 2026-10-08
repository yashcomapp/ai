import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    console.error('[CLIENT CRASH REGISTERED]:', JSON.stringify(body, null, 2));

    await adminDb.collection('systemFaults').add({
      category: 'client_crash',
      title: body.type || 'Exam Client Crash',
      message: body.message || 'Unknown client crash',
      stack: body.stack || null,
      componentStack: body.componentStack || null,
      url: body.url || null,
      userAgent: body.userAgent || null,
      context: {
        examId: body.examId || null,
        studentCode: body.studentCode || null
      },
      timestamp: new Date()
    });

    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error('Failed to log client crash:', err);
    return NextResponse.json({ success: false, error: err.message }, { status: 500 });
  }
}
