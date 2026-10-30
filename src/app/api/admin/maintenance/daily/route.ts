import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { runDailyMaintenanceOpportunistic } from '@/lib/dailyMaintenance';

export const dynamic = 'force-dynamic';
export const maxDuration = 60;

export async function GET(req: NextRequest) {
  return handleDailyMaintenance(req);
}

export async function POST(req: NextRequest) {
  return handleDailyMaintenance(req);
}

async function handleDailyMaintenance(req: NextRequest) {
  try {
    const authHeader = req.headers.get('authorization') || req.headers.get('Authorization');
    const cronSecret = process.env.CRON_SECRET;
    const isCronAuthorized = Boolean(cronSecret && authHeader === `Bearer ${cronSecret}`);

    if (!isCronAuthorized) {
      const adminUser = await verifyRole(req, 'admin');
      if (!adminUser) {
        return NextResponse.json({ message: 'Unauthorized. Admin role or valid Cron Secret required.' }, { status: 403 });
      }
    }

    const result = await runDailyMaintenanceOpportunistic();
    return NextResponse.json({
      success: true,
      ...result
    });
  } catch (error: any) {
    console.error('API Daily Maintenance Error:', error);
    return NextResponse.json({
      success: false,
      message: error.message || 'Internal Server Error'
    }, { status: 500 });
  }
}
