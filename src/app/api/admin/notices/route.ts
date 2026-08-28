import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { verifyRole } from '@/lib/auth';
import { notifyNotice } from '@/lib/notifications';

export const dynamic = 'force-dynamic';

// 1. GET - Load notices history for admin
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const noticesSnap = await adminDb.collection('notices')
      .orderBy('createdAt', 'desc')
      .limit(100)
      .get();

    // Identify all exam notice documents (results and absent alerts) to clean up from history
    const docsToDelete: string[] = [];

    const notices = noticesSnap.docs
      .filter(doc => {
        const data = doc.data();
        const t = data.type || '';
        const title = data.title || '';

        const isExamNotice = t.startsWith('exam_') || 
          title.includes('EXAM RESULT') || 
          title.includes('EXAM ABSENCE');

        if (isExamNotice) {
          docsToDelete.push(doc.id);
          return false;
        }

        return true;
      })
      .map(doc => {
        const data = doc.data();
        return {
          id: doc.id,
          title: data.title || '',
          body: data.body || '',
          targetType: data.targetType || 'all',
          targetValues: data.targetValues || [],
          createdAt: data.createdAt ? (data.createdAt.toDate ? data.createdAt.toDate().toISOString() : new Date(data.createdAt).toISOString()) : null,
          createdBy: data.createdBy || '',
          isOverlay: !!data.isOverlay,
          type: data.type || 'general',
          noticeDate: data.noticeDate || null
        };
      });

    // Delete existing result notices from Firestore history in background
    if (docsToDelete.length > 0) {
      const batch = adminDb.batch();
      docsToDelete.forEach(id => {
        batch.delete(adminDb.collection('notices').doc(id));
      });
      batch.commit().catch(err => console.error('Error purging exam result notices:', err));
    }

    return NextResponse.json({ success: true, notices });
  } catch (error: any) {
    console.error('API GET admin notices error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Publish a new notice
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const body = await req.json();
    const { title, bodyText, targetType, targetValues, isOverlay, type, noticeDate } = body;

    if (!title || !bodyText || !targetType) {
      return NextResponse.json({ message: 'Missing parameters (title, bodyText, targetType)' }, { status: 400 });
    }

    const payload: any = {
      title,
      body: bodyText,
      targetType,
      targetValues: targetValues || [],
      isOverlay: !!isOverlay,
      type: type || 'general',
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      createdBy: adminUser.decodedToken?.email || adminUser.userData?.email || 'admin@yashcom.com'
    };

    if (type === 'schedule') {
      payload.noticeDate = noticeDate || null;
    }

    const docRef = await adminDb.collection('notices').add(payload);

    // Broadcast push notifications
    await notifyNotice(title, bodyText, targetType, targetValues || []).catch(err => {
      console.error('Failed to broadcast notice notifications:', err);
    });

    return NextResponse.json({ success: true, id: docRef.id });
  } catch (error: any) {
    console.error('API POST admin notices error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. DELETE - Remove a notice
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json({ message: 'Missing parameters (id)' }, { status: 400 });
    }

    await adminDb.collection('notices').doc(id).delete();
    return NextResponse.json({ success: true, message: 'Notice deleted successfully' });
  } catch (error: any) {
    console.error('API DELETE admin notices error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
