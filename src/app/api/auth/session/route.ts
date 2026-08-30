import { NextRequest, NextResponse } from 'next/server';
import { adminAuth, adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { notifyStudentLogin, notifyStudentLogout } from '@/lib/notifications';
import { verifyToken, verifyAnyRole, invalidateUserCache } from '@/lib/auth';
import { chunkArray } from '@/lib/firestoreUtils';

async function isParentFullyAutonomous(userData: any, email?: string): Promise<boolean> {
  const parentEmail = email?.toLowerCase();
  let studentCodes: string[] = [];
  if (Array.isArray(userData?.studentCodes)) {
    studentCodes = userData.studentCodes.filter(Boolean);
  } else if (userData?.studentCode) {
    studentCodes = [userData.studentCode];
  } else if (userData?.studentId) {
    studentCodes = [userData.studentId];
  }

  let childrenDocs: any[] = [];
  if (parentEmail) {
    const querySnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('parentEmail', '==', parentEmail)
      .get();
    querySnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.studentCode && !studentCodes.includes(d.studentCode)) {
        studentCodes.push(d.studentCode);
      }
      childrenDocs.push(d);
    });
  }

  if (studentCodes.length > 0) {
    const chunks = chunkArray(studentCodes, 30);
    for (const chunk of chunks) {
      const snap = await adminDb.collection('users').where('role', '==', 'student').where('studentCode', 'in', chunk).get();
      snap.docs.forEach(doc => {
        const d = doc.data();
        if (!childrenDocs.some(c => c.studentCode === d.studentCode)) {
          childrenDocs.push(d);
        }
      });
    }
  }

  if (childrenDocs.length === 0) return false;

  const nonAutonomousCount = childrenDocs.filter(c => c.autonomous !== true).length;
  return childrenDocs.length > 0 && nonAutonomousCount === 0;
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { action } = body;

    // Fast-path for get_profile and check_role using 60s userCache
    if (action === 'get_profile' || action === 'check_role') {
      const verified = await verifyAnyRole(req, ['student', 'parent', 'admin']);
      if (!verified) {
        return NextResponse.json({ message: 'Unauthorized or profile not found.' }, { status: 401 });
      }

      const { decodedToken, userData, role } = verified;
      const { uid, email } = decodedToken;
      const studentCode = userData.studentCode || '';
      const activeSessionToken = userData.activeSessionToken || null;

      if (action === 'check_role') {
        return NextResponse.json({
          role,
          studentCode,
          activeSessionToken
        });
      }

      return NextResponse.json({
        profile: {
          uid,
          email,
          role,
          name: userData.name || userData.displayName || email || role,
          displayName: userData.name || userData.displayName || email || role,
          studentCode,
          activeSessionToken,
          hasPushRegistered: Array.isArray(userData.fcmTokens) && userData.fcmTokens.length > 0,
          curfewBypass: userData.curfewBypass || false
        },
        serverTime: Date.now()
      });
    }

    const decodedToken = await verifyToken(req);
    if (!decodedToken) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { uid, email } = decodedToken;
    const userDocRef = adminDb.collection('users').doc(uid);
    const userDoc = await userDocRef.get();

    if (!userDoc.exists && action !== 'start_session' && action !== 'end_session') {
      return NextResponse.json({ message: 'User profile not found. Please contact admin.' }, { status: 404 });
    }

    const userData = userDoc.data() || {};
    const role = (userData.role || 'pending').toLowerCase();
    const studentCode = userData.studentCode || '';
    const activeSessionToken = userData.activeSessionToken || null;

    if (userData.status === 'inactive' && role !== 'admin') {
      return NextResponse.json({ message: 'Your account has been disabled. Please contact admin.' }, { status: 403 });
    }

    if (action === 'login_session') {
      const { sessionToken, force } = body;
      
      if (role === 'pending') {
        return NextResponse.json({ message: 'Your registration is still waiting for admin approval. Please wait a little.' }, { status: 403 });
      }

      if (role === 'student') {
        const userEmail = (email || userData.email || '').toLowerCase();
        const curfewBypassEmail = (process.env.CURFEW_BYPASS_EMAIL || '').toLowerCase();
        const isBypassed = userEmail === 's@c.com' || userEmail === 'p@c.com' || userEmail === 'a@c.com' || userEmail === curfewBypassEmail || !!userData.curfewBypass || !!userData.maintenanceBypass;
        if (!isBypassed) {
          const nowUtc = Date.now();
          const istOffset = 5.5 * 60 * 60 * 1000;
          const istDate = new Date(nowUtc + istOffset);
          const hours = istDate.getUTCHours();
          const minutes = istDate.getUTCMinutes();
          const isCurfew = hours > 22 || (hours === 22 && minutes >= 30) || hours < 5;
          if (isCurfew) {
            return NextResponse.json({ message: 'Rest is crucial for conceptual mastery! Yashcom Foundation restricts student logins between 10:30 PM and 5:00 AM to promote healthy sleep. Sleep well!' }, { status: 403 });
          }
        }
      }

      if (role !== 'admin' && activeSessionToken && activeSessionToken !== sessionToken && !force) {
        return NextResponse.json({ conflict: true, message: 'Account is logged in on another device.' }, { status: 409 });
      }

      const updateData: Record<string, any> = {
        lastLoginAt: admin.firestore.FieldValue.serverTimestamp()
      };
      if (role !== 'admin' && sessionToken) {
        updateData.activeSessionToken = sessionToken;
      }

      // Fast atomic write without heavy transaction locks
      await userDocRef.set(updateData, { merge: true });
      invalidateUserCache(uid);

      // Async non-blocking session audit log
      adminDb.collection('session_logs').add({
        uid,
        email: email || userData.email || '',
        name: userData.name || userData.displayName || email || role,
        role,
        batchIds: userData.batchIds || [],
        timestamp: admin.firestore.FieldValue.serverTimestamp(),
        type: 'login'
      }).catch((e) => console.error('Session log write failed:', e));

      // Async non-blocking login notification
      if (role === 'student') {
        notifyStudentLogin(studentCode, userData.name || userData.displayName || email || 'Student').catch((e) => console.error('Login notify failed:', e));
      }

      return NextResponse.json({
        success: true,
        profile: {
          uid,
          email,
          role,
          name: userData.name || userData.displayName || email || role,
          displayName: userData.name || userData.displayName || email || role,
          studentCode,
          activeSessionToken: role !== 'admin' ? sessionToken : null,
          hasPushRegistered: Array.isArray(userData.fcmTokens) && userData.fcmTokens.length > 0,
          curfewBypass: userData.curfewBypass || false,
          maintenanceBypass: userData.maintenanceBypass || false
        },
        serverTime: Date.now()
      });
    }

    if (action === 'check_role') {
      return NextResponse.json({
        role,
        studentCode,
        activeSessionToken
      });
    }

    if (action === 'get_profile') {
      return NextResponse.json({
        profile: {
          uid,
          email,
          role,
          name: userData.name || userData.displayName || email || role,
          displayName: userData.name || userData.displayName || email || role,
          studentCode,
          activeSessionToken,
          hasPushRegistered: Array.isArray(userData.fcmTokens) && userData.fcmTokens.length > 0,
          curfewBypass: userData.curfewBypass || false
        },
        serverTime: Date.now()
      });
    }

    if (action === 'start_session') {
      const { sessionToken } = body;
      const updateData: Record<string, any> = {
        lastLoginAt: admin.firestore.FieldValue.serverTimestamp()
      };
      
      // Admin is exempt from setting activeSessionToken
      if (role !== 'admin' && sessionToken) {
        updateData.activeSessionToken = sessionToken;
      }

      await userDocRef.set(updateData, { merge: true });
      invalidateUserCache(uid);

      return NextResponse.json({ success: true });
    }

    if (action === 'end_session') {
      invalidateUserCache(uid);
      // Clear token on logout
      if (role !== 'admin') {
        await userDocRef.update({
          activeSessionToken: admin.firestore.FieldValue.delete()
        }).catch((err) => {
          // If document doesn't have activeSessionToken or doesn't exist, fail-soft
          console.warn('Silent end_session error:', err.message);
        });
      }

      if (role === 'student') {
        const studentName = userData.name || userData.displayName || email || 'Student';
        notifyStudentLogout(studentCode, studentName, uid).catch(e => console.error(e));
      }

      // Log session logout
      await adminDb.collection('session_logs').add({
        uid,
        email: email || userData.email || '',
        name: userData.name || userData.displayName || email || role,
        role,
        batchIds: userData.batchIds || [],
        timestamp: admin.firestore.FieldValue.serverTimestamp(),
        type: 'logout'
      }).catch((err) => {
        console.error('Error logging logout session:', err);
      });

      return NextResponse.json({ success: true });
    }

    return NextResponse.json({ message: 'Invalid action' }, { status: 400 });

  } catch (error: any) {
    console.error('Session API route error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
