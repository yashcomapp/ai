import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

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
    const { maintenanceMode, blockedRoles, message } = body;

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
