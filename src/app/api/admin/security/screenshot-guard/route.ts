import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export interface ExamSecurityConfig {
  screenshotGuardEnabled: boolean;
  blurOnFocusLoss: boolean;
  forensicWatermark: boolean;
  clearClipboardOnPrint: boolean;
  updatedAt?: any;
  updatedBy?: string;
}

const DEFAULT_CONFIG: ExamSecurityConfig = {
  screenshotGuardEnabled: true,
  blurOnFocusLoss: true,
  forensicWatermark: true,
  clearClipboardOnPrint: true
};

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const docSnap = await adminDb.collection('config').doc('examSecurity').get();
    const config: ExamSecurityConfig = docSnap.exists
      ? { ...DEFAULT_CONFIG, ...docSnap.data() }
      : DEFAULT_CONFIG;

    return NextResponse.json({ success: true, config });
  } catch (error: any) {
    console.error('API GET screenshot-guard security config error:', error);
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
    const {
      screenshotGuardEnabled = true,
      blurOnFocusLoss = true,
      forensicWatermark = true,
      clearClipboardOnPrint = true
    } = body;

    const updatedConfig: ExamSecurityConfig = {
      screenshotGuardEnabled: Boolean(screenshotGuardEnabled),
      blurOnFocusLoss: Boolean(blurOnFocusLoss),
      forensicWatermark: Boolean(forensicWatermark),
      clearClipboardOnPrint: Boolean(clearClipboardOnPrint),
      updatedAt: new Date(),
      updatedBy: adminUser.decodedToken.email || 'admin'
    };

    await adminDb.collection('config').doc('examSecurity').set(updatedConfig, { merge: true });

    return NextResponse.json({ success: true, config: updatedConfig });
  } catch (error: any) {
    console.error('API POST screenshot-guard security config error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
