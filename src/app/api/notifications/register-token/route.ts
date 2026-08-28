import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { verifyToken } from '@/lib/auth';

export async function POST(req: NextRequest) {
  try {
    const decodedToken = await verifyToken(req);
    if (!decodedToken) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { uid } = decodedToken;
    const body = await req.json();
    const { token, action } = body;

    if (!token) {
      return NextResponse.json({ message: 'Missing FCM token' }, { status: 400 });
    }

    const userRef = adminDb.collection('users').doc(uid);

    if (action === 'unregister') {
      await userRef.update({
        fcmTokens: admin.firestore.FieldValue.arrayRemove(token),
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }).catch((e) => {
        console.warn('Soft fail unregistering token:', e.message);
      });
      return NextResponse.json({ success: true, message: 'Token unregistered successfully' });
    }

    // Default: register token
    const userDoc = await userRef.get();
    const userData = userDoc.exists ? userDoc.data() || {} : {};
    const existingTokens = Array.isArray(userData.fcmTokens) ? userData.fcmTokens : [];
    const isNewToken = !existingTokens.includes(token);

    await userRef.set({
      fcmTokens: admin.firestore.FieldValue.arrayUnion(token),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });

    if (isNewToken) {
      // Send a readiness/welcome push notification to confirm it works!
      try {
        const { sendPushNotification } = await import('@/lib/notifications');
        await sendPushNotification(
          [uid],
          'YASHCOM',
          '🔔 Aapka device notification ke liye ready hai! You will receive live updates and alerts here.'
        );
      } catch (pushErr) {
        console.warn('Failed to send welcome/readiness notification:', pushErr);
      }
    }

    return NextResponse.json({ success: true, message: 'Token registered successfully' });

  } catch (error: any) {
    console.error('API register-token error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
