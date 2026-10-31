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

    const body = await req.json();
    const { action, targetUid, maintenanceMode, blockedRoles, message } = body;

    // Direct Admin Deactivation Endpoint: syncs custom claims and revokes refresh tokens immediately
    if (action === 'deactivateAdmin') {
      if (!targetUid) {
        return NextResponse.json({ message: 'targetUid is required' }, { status: 400 });
      }
      const targetUserDoc = await adminDb.collection('users').doc(targetUid).get();
      if (!targetUserDoc.exists) {
        return NextResponse.json({ message: 'User not found' }, { status: 404 });
      }
      const uData = targetUserDoc.data()!;
      await targetUserDoc.ref.update({
        status: 'inactive',
        updatedAt: new Date()
      });
      invalidateUserCache(targetUid);
      await syncUserCustomClaims(targetUid, { ...uData, status: 'inactive' }, true);
      return NextResponse.json({ success: true, message: `Admin ${targetUid} deactivated and auth tokens revoked.` });
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
