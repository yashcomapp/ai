import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    let studentCode = '';
    
    // 1. Authenticate user as student
    const studentSession = await verifyRole(req, 'student');
    if (studentSession) {
      studentCode = studentSession.userData?.studentCode || '';
    } else {
      // 2. Fallback: Authenticate as parent
      const parentSession = await verifyRole(req, 'parent');
      if (parentSession) {
        const { searchParams } = new URL(req.url);
        const targetStudentCode = searchParams.get('studentCode')?.trim().toUpperCase();
        
        const parentCodes = parentSession.userData?.studentCodes || (parentSession.userData?.studentCode ? [parentSession.userData?.studentCode] : []);
        const parentCodesUpper = parentCodes.map((c: string) => c.toUpperCase());

        if (targetStudentCode && parentCodesUpper.includes(targetStudentCode)) {
          studentCode = targetStudentCode;
        } else if (parentCodesUpper.length > 0) {
          studentCode = parentCodesUpper[0];
        }
      }
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Unauthorized. Student or Parent role required.' }, { status: 403 });
    }

    const sCodeUpper = studentCode.trim().toUpperCase();

    const [feeDoc, txsSnap] = await Promise.all([
      adminDb.collection('studentFees').doc(sCodeUpper).get(),
      adminDb.collection('feeTransactions')
        .where('studentCode', '==', sCodeUpper)
        .get()
    ]);

    const feeRecord = feeDoc.exists ? feeDoc.data() : null;
    const transactions = txsSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
    
    // Sort transactions in-memory by timestamp desc
    transactions.sort((a: any, b: any) => {
      const timeA = a.timestamp ? (a.timestamp.toDate ? a.timestamp.toDate().getTime() : new Date(a.timestamp).getTime()) : 0;
      const timeB = b.timestamp ? (b.timestamp.toDate ? b.timestamp.toDate().getTime() : new Date(b.timestamp).getTime()) : 0;
      return timeB - timeA;
    });

    return NextResponse.json({
      success: true,
      feeRecord,
      transactions
    }, {
      headers: {
        'Cache-Control': 'private, max-age=10, stale-while-revalidate=20'
      }
    });
  } catch (error: any) {
    console.error('API GET student/parent fees error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
