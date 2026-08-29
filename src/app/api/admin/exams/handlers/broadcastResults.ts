import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { generateAndDispatchExamNotices } from '@/lib/examNotices';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { examId } = body;

    if (!examId) {
      return NextResponse.json({ message: 'Missing examId' }, { status: 400 });
    }

    const result = await generateAndDispatchExamNotices(examId, true);

    if (!result.success) {
      return NextResponse.json({ message: result.message }, { status: 500 });
    }

    return NextResponse.json({
      success: true,
      message: result.message,
      totalNoticesSent: result.totalNoticesSent
    });

  } catch (error: any) {
    console.error('API POST broadcast-results error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
