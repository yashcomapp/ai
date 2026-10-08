import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { QuestionRepository } from '@/repositories/question.repository';
import { invalidateCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const disputesSnap = await adminDb.collection('disputes')
      .orderBy('createdAt', 'desc')
      .get()
      .catch(async () => {
        // Fallback without orderBy in case index is building
        return await adminDb.collection('disputes').get();
      });

    const disputes = disputesSnap.docs.map(doc => {
      const data = doc.data();
      const createdAtIso = data.createdAt?.toDate
        ? data.createdAt.toDate().toISOString()
        : (data.createdAt ? new Date(data.createdAt).toISOString() : new Date().toISOString());

      return {
        id: doc.id,
        questionCode: data.questionCode || data.questionId || '',
        questionId: data.questionId || data.questionCode || '',
        status: data.status || 'pending',
        source: data.source || 'Exam',
        studentName: data.studentName || 'Student',
        studentCode: data.studentCode || '',
        class: data.class || data.className || '',
        createdAt: createdAtIso,
        screenshotData: data.screenshotData || null,
        reason: data.reason || 'DEFECTIVE QUESTION',
        notes: data.notes || ''
      };
    });

    return NextResponse.json({ disputes });
  } catch (error: any) {
    console.error('API load disputes error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { disputeId, action } = body;

    if (!disputeId || !action) {
      return NextResponse.json({ message: 'Missing parameters (disputeId, action).' }, { status: 400 });
    }

    const disputeRef = adminDb.collection('disputes').doc(disputeId);
    const disputeSnap = await disputeRef.get();

    if (!disputeSnap.exists) {
      return NextResponse.json({ message: 'Dispute record not found.' }, { status: 404 });
    }

    const disputeData = disputeSnap.data()!;
    const qCode = disputeData.questionCode || disputeData.questionId;

    if (action === 'approve' || action === 'quarantine') {
      // Find question and mark quarantined
      if (qCode) {
        let questionRef = adminDb.collection('questions').doc(qCode);
        let qDoc = await questionRef.get();

        if (!qDoc.exists) {
          const queryByCode = await adminDb.collection('questions')
            .where('questionCode', '==', qCode)
            .limit(1)
            .get();
          if (!queryByCode.empty) {
            questionRef = queryByCode.docs[0].ref;
            qDoc = queryByCode.docs[0];
          }
        }

        if (qDoc.exists) {
          const qData = qDoc.data() || {};
          await questionRef.update({
            isQuarantined: true,
            status: 'quarantined',
            flaggedDefective: true,
            quarantinedAt: new Date().toISOString()
          });
          invalidateCache('qb_base_');
          if (qData.topicCode) {
            QuestionRepository.clearTopicCache(qData.topicCode);
          }
        }
      }

      // Delete dispute record & proof screenshot permanently
      await disputeRef.delete();
      return NextResponse.json({ success: true, message: 'Question quarantined and dispute record cleared.' });
    }

    if (action === 'reject') {
      // Dismiss dispute
      await disputeRef.delete();
      return NextResponse.json({ success: true, message: 'Dispute dismissed and record cleared.' });
    }

    return NextResponse.json({ message: 'Invalid action.' }, { status: 400 });

  } catch (error: any) {
    console.error('API resolve dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
