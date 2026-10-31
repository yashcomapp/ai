import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, syncUserCustomClaims, invalidateUserCache } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const docSnap = await adminDb.collection('config').doc('systemAccess').get();
    const data = docSnap.exists ? docSnap.data() : { maintenanceMode: false, blockedRoles: [], message: '' };

    return NextResponse.json({ success: true, config: data });
  } catch (error: any) {
    console.error('API GET system access error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const callerUid = adminUser.decodedToken?.uid || '';
    const callerEmail = adminUser.decodedToken?.email || adminUser.userData?.email || '';

    const body = await req.json();
    const { action, targetUid, maintenanceMode, blockedRoles, message } = body;

    // Direct Admin Deactivation Endpoint: syncs custom claims and revokes refresh tokens immediately
    if (action === 'deactivateAdmin') {
      if (!targetUid) {
        return NextResponse.json({ message: 'targetUid is required' }, { status: 400 });
      }
      if (targetUid === callerUid) {
        return NextResponse.json({ message: 'Cannot deactivate your own administrator account' }, { status: 400 });
      }
      const targetUserDoc = await adminDb.collection('users').doc(targetUid).get();
      if (!targetUserDoc.exists) {
        return NextResponse.json({ message: 'User not found' }, { status: 404 });
      }
      const uData = targetUserDoc.data()!;
      if (uData.role !== 'admin') {
        return NextResponse.json({ message: 'Target user is not an administrator' }, { status: 400 });
      }

      // Guard: Ensure at least one other active admin remains
      const adminUsersSnap = await adminDb.collection('users').where('role', '==', 'admin').get();
      const activeOtherAdmins = adminUsersSnap.docs.filter(
        d => d.id !== targetUid && d.data().status !== 'inactive'
      );
      if (activeOtherAdmins.length === 0) {
        return NextResponse.json({ message: 'Cannot deactivate the last active administrator' }, { status: 400 });
      }

      await targetUserDoc.ref.update({
        status: 'inactive',
        updatedAt: new Date()
      });
      invalidateUserCache(targetUid);
      await syncUserCustomClaims(targetUid, { ...uData, status: 'inactive' }, true);

      // Audit log entry
      try {
        await adminDb.collection('systemAuditLogs').add({
          action: 'deactivateAdmin',
          performedBy: callerUid,
          performedByEmail: callerEmail,
          targetUid,
          targetEmail: uData.email || '',
          timestamp: new Date()
        });
      } catch (logErr) {
        console.error('Audit log error for deactivateAdmin:', logErr);
      }

      return NextResponse.json({ success: true, message: `Admin ${targetUid} deactivated and auth tokens revoked.` });
    }

    // Direct Admin Reactivation Endpoint
    if (action === 'reactivateAdmin') {
      if (!targetUid) {
        return NextResponse.json({ message: 'targetUid is required' }, { status: 400 });
      }
      const targetUserDoc = await adminDb.collection('users').doc(targetUid).get();
      if (!targetUserDoc.exists) {
        return NextResponse.json({ message: 'User not found' }, { status: 404 });
      }
      const uData = targetUserDoc.data()!;
      if (uData.role !== 'admin') {
        return NextResponse.json({ message: 'Target user is not an administrator' }, { status: 400 });
      }

      await targetUserDoc.ref.update({
        status: 'active',
        updatedAt: new Date()
      });
      invalidateUserCache(targetUid);
      await syncUserCustomClaims(targetUid, { ...uData, status: 'active' }, true);

      try {
        await adminDb.collection('systemAuditLogs').add({
          action: 'reactivateAdmin',
          performedBy: callerUid,
          performedByEmail: callerEmail,
          targetUid,
          targetEmail: uData.email || '',
          timestamp: new Date()
        });
      } catch (logErr) {
        console.error('Audit log error for reactivateAdmin:', logErr);
      }

      return NextResponse.json({ success: true, message: `Admin ${targetUid} reactivated and auth tokens refreshed.` });
    }

    await adminDb.collection('config').doc('systemAccess').set({
      maintenanceMode: !!maintenanceMode,
      blockedRoles: blockedRoles || [],
      message: message || 'System is undergoing scheduled maintenance. Access will be restored shortly.',
      updatedAt: new Date()
    }, { merge: true });

    return NextResponse.json({ success: true });
  } catch (error: any) {
    console.error('API POST system access error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
