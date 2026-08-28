import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { ReportService } from '@/services/report.service';
import { ReportCacheManager } from '@/lib/reportCache';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const cacheKey = 'usage-report';
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    const data = await ReportService.getUsageReport();

    const result = {
      success: true,
      stats: data.stats,
      evaluations: data.evaluations
    };

    await ReportCacheManager.setReport(cacheKey, result, 60); // cache for 1 minute

    return NextResponse.json(result);

  } catch (error: any) {
    console.error('API load usage stats error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
