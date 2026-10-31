import { NextRequest, NextResponse } from 'next/server';
import { adminAuth, adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { notifyStudentLogin, notifyStudentLogout } from '@/lib/notifications';
import { verifyToken, verifyAnyRole, invalidateUserCache, syncUserCustomClaims, areClaimsEqual, getParentDeactCache, setParentDeactCache } from '@/lib/auth';
import { chunkArray } from '@/lib/firestoreUtils';
import { isStudentBlockedByCurfew, CURFEW_RESTRICTION_MESSAGE } from '@/lib/curfew';

async function checkParentDeactivationStatus(userData: any, email?: string): Promise<{ shouldDeactivate: boolean; reason: 'student_autonomous' | 'all_students_inactive' | null }> {
  const parentEmail = email?.toLowerCase();
  if (parentEmail) {
    const cached = getParentDeactCache(parentEmail);
    if (cached) {
      return cached;
    }
  }

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
    const snaps = await Promise.all(
      chunks.map(chunk =>
        adminDb.collection('users').where('role', '==', 'student').where('studentCode', 'in', chunk).get()
      )
    );
    snaps.forEach(snap => {
      snap.docs.forEach(doc => {
        const d = doc.data();
        if (!childrenDocs.some(c => c.studentCode === d.studentCode)) {
          childrenDocs.push(d);
        }
      });
    });
  }

  // Deduplicate childrenDocs by studentCode
  const seenCodes = new Set<string>();
  childrenDocs = childrenDocs.filter(c => {
    if (!c.studentCode) return false;
    if (seenCodes.has(c.studentCode)) return false;
    seenCodes.add(c.studentCode);
    return true;
  });

  let result: { shouldDeactivate: boolean; reason: 'student_autonomous' | 'all_students_inactive' | null } = { shouldDeactivate: false, reason: null };
  if (childrenDocs.length === 0) {
    result = { shouldDeactivate: true, reason: 'all_students_inactive' };
  } else {
    // Check if ALL linked students are inactive
    const activeChildren = childrenDocs.filter(c => c.status !== 'inactive');
    if (activeChildren.length === 0) {
      result = { shouldDeactivate: true, reason: 'all_students_inactive' };
    } else {
      // Check if ALL active linked students are in Autonomous Mode
      const nonAutonomousActiveCount = activeChildren.filter(c => c.autonomous !== true).length;
      if (nonAutonomousActiveCount === 0) {
        result = { shouldDeactivate: true, reason: 'student_autonomous' };
      }
    }
  }

  if (parentEmail) {
    setParentDeactCache(parentEmail, result);
  }

  return result;
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

      const claimsUpdated = !!verified.claimsUpdated;

      const responseHeaders: Record<string, string> = {};
      if (claimsUpdated) {
        responseHeaders['x-claims-updated'] = 'true';
      }

      if (action === 'check_role') {
        return NextResponse.json({
          role,
          studentCode,
          activeSessionToken,
          claimsUpdated
        }, { headers: responseHeaders });
      }

      return NextResponse.json({
        claimsUpdated,
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
      }, { headers: responseHeaders });
    }

    const decodedToken = await verifyToken(req);
    if (!decodedToken) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { uid, email } = decodedToken;
    const userDocRef = adminDb.collection('users').doc(uid);
    const userDoc = await userDocRef.get();

    if (!userDoc.exists && action !== 'end_session') {
      return NextResponse.json({ message: 'User profile not found. Please contact admin.' }, { status: 404 });
    }

    const userData = userDoc.data() || {};
    const role = (userData.role || 'pending').toLowerCase();
    const studentCode = userData.studentCode || '';
    const activeSessionToken = userData.activeSessionToken || null;

    let claimsUpdatedFallback = false;
    if (userDoc.exists && !areClaimsEqual(decodedToken, userData)) {
      claimsUpdatedFallback = await syncUserCustomClaims(uid, userData);
    }

    if (role === 'parent') {
      const deactCheck = await checkParentDeactivationStatus(userData, email);
      if (deactCheck.shouldDeactivate) {
        if (userData.status !== 'inactive' || userData.deactivationReason !== deactCheck.reason) {
          await userDocRef.update({
            status: 'inactive',
            deactivationReason: deactCheck.reason,
            updatedAt: new Date()
          }).catch(() => null);
          invalidateUserCache(uid);
          userData.status = 'inactive';
          userData.deactivationReason = deactCheck.reason;
        }

        if (deactCheck.reason === 'student_autonomous') {
          return NextResponse.json({ 
            message: 'Parent portal access is disabled as your student is registered in Autonomous Mode (parent exam reviews are not required).' 
          }, { status: 403 });
        } else {
          return NextResponse.json({
            message: 'Parent portal access is disabled as no active students are linked to this parent account.'
          }, { status: 403 });
        }
      } else if (userData.status === 'inactive' && (userData.deactivationReason === 'all_students_inactive' || userData.deactivationReason === 'student_autonomous')) {
        // Automatically self-heal and reactivate parent account when linked students are active & non-autonomous
        await userDocRef.update({
          status: 'active',
          deactivationReason: admin.firestore.FieldValue.delete(),
          updatedAt: new Date()
        }).catch(() => null);
        invalidateUserCache(uid);
        userData.status = 'active';
        delete userData.deactivationReason;
      }
    }

    if (userData.status === 'inactive' && role !== 'admin') {
      if (role === 'parent') {
        if (userData.deactivationReason === 'student_autonomous') {
          return NextResponse.json({ 
            message: 'Parent portal access is disabled as your student is registered in Autonomous Mode (parent exam reviews are not required).' 
          }, { status: 403 });
        }
        if (userData.deactivationReason === 'all_students_inactive') {
          return NextResponse.json({ 
            message: 'Parent portal access is disabled as no active students are linked to this parent account.' 
          }, { status: 403 });
        }
      }
      return NextResponse.json({ message: 'Your account has been disabled. Please contact admin.' }, { status: 403 });
    }

    if (action === 'login_session') {
      const { sessionToken, force } = body;
      
      if (role === 'pending') {
        return NextResponse.json({ message: 'Your registration is still waiting for admin approval. Please wait a little.' }, { status: 403 });
      }

      if (role === 'student') {
        const userEmail = email || userData.email || '';
        if (isStudentBlockedByCurfew(userEmail, userData)) {
          return NextResponse.json({ message: CURFEW_RESTRICTION_MESSAGE }, { status: 403 });
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

      // Await session audit log & notification so Vercel runtime does not kill promises mid-flight
      const lastLoginTime = userData.lastLoginAt?.toMillis ? userData.lastLoginAt.toMillis() : (userData.lastLoginAt ? new Date(userData.lastLoginAt).getTime() : 0);
      const isRecentLogin = lastLoginTime > 0 && (Date.now() - lastLoginTime < 5 * 60 * 1000);

      const backgroundTasks: Promise<any>[] = [];
      if (!isRecentLogin) {
        backgroundTasks.push(adminDb.collection('session_logs').add({
          uid,
          email: email || userData.email || '',
          name: userData.name || userData.displayName || email || role,
          role,
          batchIds: userData.batchIds || [],
          timestamp: admin.firestore.FieldValue.serverTimestamp(),
          type: 'login'
        }).catch((e) => console.error('Session log write failed:', e)));
      }

      if (role === 'student') {
        backgroundTasks.push(notifyStudentLogin(studentCode, userData.name || userData.displayName || email || 'Student').catch((e) => console.error('Login notify failed:', e)));
      }

      if (backgroundTasks.length > 0) {
        await Promise.allSettled(backgroundTasks);
      }

      const responseHeaders: Record<string, string> = {};
      if (claimsUpdatedFallback) {
        responseHeaders['x-claims-updated'] = 'true';
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
      }, { headers: responseHeaders });
    }

    if (action === 'check_role') {
      return NextResponse.json({
        role,
        studentCode,
        activeSessionToken
      }, { headers: claimsUpdatedFallback ? { 'x-claims-updated': 'true' } : {} });
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
      }, { headers: claimsUpdatedFallback ? { 'x-claims-updated': 'true' } : {} });
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
        await notifyStudentLogout(studentCode, studentName, uid).catch(e => console.error(e));
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
