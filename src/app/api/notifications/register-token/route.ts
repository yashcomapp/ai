import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { verifyAnyRole, invalidateUserCache } from '@/lib/auth';

export async function POST(req: NextRequest) {
  try {
    const verified = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!verified) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { uid } = verified.decodedToken;
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
      invalidateUserCache(uid);
      return NextResponse.json({ success: true, message: 'Token unregistered successfully' });
    }

    // Default: register token using cached userData
    const userData = verified.userData || {};
    const existingTokens = Array.isArray(userData.fcmTokens) ? userData.fcmTokens : [];
    const isNewToken = !existingTokens.includes(token);

    await userRef.set({
      fcmTokens: admin.firestore.FieldValue.arrayUnion(token),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
    invalidateUserCache(uid);

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
