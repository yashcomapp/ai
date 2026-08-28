import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

// 1. GET - Fetch all question disputes
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const status = searchParams.get('status') || 'all';

    let query: FirebaseFirestore.Query = adminDb.collection('questionDisputes');

    if (status !== 'all') {
      query = query.where('status', '==', status);
    }

    const snap = await query.limit(200).get();

    const disputes = snap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    // Sort latest first in memory
    disputes.sort((a: any, b: any) => {
      const timeA = new Date(a.createdAt || 0).getTime();
      const timeB = new Date(b.createdAt || 0).getTime();
      return timeB - timeA;
    });

    return NextResponse.json({
      success: true,
      disputes
    });
  } catch (error: any) {
    console.error('API admin get disputes error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Review and resolve a dispute (removes record & screenshot once action is taken)
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const body = await req.json();
    const { disputeId, action, notes, questionId } = body; // action: 'approve' | 'reject' | 'quarantine' | 'delete'

    if (!disputeId) {
      return NextResponse.json({ message: 'Missing disputeId' }, { status: 400 });
    }

    const disputeRef = adminDb.collection('questionDisputes').doc(disputeId);
    const disputeSnap = await disputeRef.get();
    if (!disputeSnap.exists) {
      return NextResponse.json({ message: 'Dispute record not found' }, { status: 404 });
    }

    const disputeData = disputeSnap.data()!;
    const qId = questionId || disputeData.questionId || disputeData.questionCode;

    // If approved or quarantined, update the question status in the question bank
    if ((action === 'approve' || action === 'quarantine') && qId) {
      try {
        let qRef = adminDb.collection('questions').doc(qId);
        let qSnap = await qRef.get();
        if (!qSnap.exists && disputeData.questionCode) {
          const qByCodeSnap = await adminDb.collection('questions')
            .where('questionCode', '==', disputeData.questionCode)
            .limit(1)
            .get();
          if (!qByCodeSnap.empty) {
            qRef = qByCodeSnap.docs[0].ref;
            qSnap = qByCodeSnap.docs[0];
          }
        }

        if (qSnap.exists) {
          await qRef.update({
            flaggedDefective: true,
            defectiveReason: disputeData.reason || 'Student reported issue',
            quarantinedAt: new Date().toISOString()
          });
        }
      } catch (qErr) {
        console.warn('Failed to update question status:', qErr);
      }
    }

    // Completely remove the dispute record and screenshot - no log retained
    await disputeRef.delete();

    return NextResponse.json({
      success: true,
      message: action === 'approve' || action === 'quarantine' 
        ? 'Question quarantined and dispute record & screenshot purged.' 
        : 'Dispute dismissed and record & screenshot purged.',
      actionTaken: action
    });
  } catch (error: any) {
    console.error('API admin resolve dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. DELETE - Explicitly delete dispute record
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const disputeId = searchParams.get('id') || '';

    if (!disputeId) {
      return NextResponse.json({ message: 'Missing dispute id' }, { status: 400 });
    }

    await adminDb.collection('questionDisputes').doc(disputeId).delete();

    return NextResponse.json({
      success: true,
      message: 'Dispute record and screenshot purged.'
    });
  } catch (error: any) {
    console.error('API admin delete dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
