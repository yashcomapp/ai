import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const parentUser = await verifyRole(req, 'parent');
    if (!parentUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { uid } = parentUser.decodedToken;

    const snap = await adminDb.collection('pushNotificationsHistory')
      .where('userId', '==', uid)
      .get();

    const history = snap.docs.map(doc => {
      const d = doc.data();
      return {
        id: doc.id,
        title: d.title || 'Notification',
        body: d.body || '',
        sentAt: d.sentAt?.toDate ? d.sentAt.toDate().toISOString() : new Date().toISOString()
      };
    }).sort((a, b) => new Date(b.sentAt).getTime() - new Date(a.sentAt).getTime())
      .slice(0, 50);

    return NextResponse.json({ success: true, history });
  } catch (error: any) {
    console.error('API parent notification-history error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
