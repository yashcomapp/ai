import { NextRequest, NextResponse } from 'next/server';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportService } from '@/services/report.service';
import { QuotientService } from '@/services/quotient.service';
import { getFromCache, setInCache, invalidateCache } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';

export const dynamic = 'force-dynamic';

const REPORT_CACHE_HEADERS = {
  'Cache-Control': 'private, s-maxage=60, stale-while-revalidate=120'
};

const NO_CACHE_HEADERS = {
  'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate'
};

const REPORT_CACHE_TTL_MS = 60000; // 60 seconds

// ── 1. Daily Practice Report Handler ──────────────────────────────────
async function handleDailyPractice(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const { searchParams } = new URL(req.url);
  const dateParam = searchParams.get('date');
  const targetDateStr = dateParam || getDateKeyIST();

  const cacheKey = `admin_report_daily_practice_${targetDateStr}`;
  const cached = getFromCache<any>(cacheKey);
  if (cached) {
    return NextResponse.json(cached, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getDailyPracticeReport(targetDateStr);
  setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 2. Learning Quotient Report Handler (GET & POST) ──────────────────
async function handleLearningQuotientGet(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const { searchParams } = new URL(req.url);
  const studentCode = searchParams.get('studentCode') || '';
  const duration = searchParams.get('duration') || 'monthly';

  if (studentCode) {
    const cacheKey = `admin_report_lq_single_${studentCode}_${duration}`;
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, { headers: NO_CACHE_HEADERS });
    }

    const report = await ReportService.getSingleLearningQuotientReport(studentCode, duration);
    setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
    return NextResponse.json(report, { headers: NO_CACHE_HEADERS });
  }

  const bulkCacheKey = `admin_report_lq_bulk_${duration}`;
  const cachedBulk = getFromCache<any>(bulkCacheKey);
  if (cachedBulk) {
    return NextResponse.json(cachedBulk, { headers: NO_CACHE_HEADERS });
  }

  const report = await ReportService.getBulkLearningQuotientReport(duration);
  setInCache(bulkCacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: NO_CACHE_HEADERS });
}

async function handleLearningQuotientPost(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const body = await req.json();
  const { action } = body;
  const actorEmail = adminUser.userData?.email || adminUser.decodedToken?.email || 'admin';

  const invalidateAllLQCaches = async () => {
    invalidateCache('admin_report_lq_');
    await ReportCacheManager.invalidatePattern('lq');
    await ReportCacheManager.invalidatePattern('quotient');
    await ReportCacheManager.invalidatePattern('single-lq-');
    await ReportCacheManager.invalidatePattern('bulk-');
  };

  if (action === 'saveParameter') {
    const { parameterId, name } = body;
    if (!name) {
      return NextResponse.json({ message: 'Parameter name is required.' }, { status: 400 });
    }
    const parameter = await QuotientService.saveParameter(name, parameterId);
    await invalidateAllLQCaches();
    return NextResponse.json({ success: true, message: 'Parameter saved successfully.', parameter }, { headers: NO_CACHE_HEADERS });
  }

  if (action === 'deleteParameter') {
    const { parameterId } = body;
    if (!parameterId) {
      return NextResponse.json({ message: 'Parameter ID is required.' }, { status: 400 });
    }
    await QuotientService.deleteParameter(parameterId);
    await invalidateAllLQCaches();
    return NextResponse.json({ success: true, message: 'Parameter deleted successfully.' }, { headers: NO_CACHE_HEADERS });
  }

  if (action === 'batchAward') {
    const { studentCodes, parameterId, score } = body;
    if (!studentCodes || !Array.isArray(studentCodes) || !parameterId || score === undefined) {
      return NextResponse.json({ message: 'Missing required parameters for batch award.' }, { status: 400 });
    }
    await QuotientService.batchAward(studentCodes, parameterId, score, actorEmail);
    invalidateCache('admin_report_lq_');
    await ReportService.updateBatchAwardInCache(studentCodes, parameterId, Number(score));
    return NextResponse.json({ success: true, message: 'Batch award observation logged successfully.' }, { headers: NO_CACHE_HEADERS });
  }

  if (action === 'logSingleObservation') {
    const { studentCode, scores } = body;
    if (!studentCode || !scores || typeof scores !== 'object') {
      return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
    }
    await QuotientService.logSingleObservation(studentCode, scores, actorEmail);
    invalidateCache('admin_report_lq_');
    await ReportService.updateStudentObservationInCache(studentCode, scores);
    return NextResponse.json({ success: true, message: 'Student observation logged successfully.' }, { headers: NO_CACHE_HEADERS });
  }

  // Default action: save standard classroom observation
  const { studentCode, activeParticipation, sincerity, timelyWork, parentScore } = body;
  if (!studentCode || activeParticipation === undefined || sincerity === undefined || timelyWork === undefined) {
    return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
  }

  await QuotientService.saveObservation({
    studentCode,
    activeParticipation: Number(activeParticipation),
    sincerity: Number(sincerity),
    timelyWork: Number(timelyWork),
    parentScore: parentScore !== undefined ? Number(parentScore) : 50,
    observedBy: actorEmail
  });
  invalidateCache('admin_report_lq_');
  await ReportService.updateStudentObservationInCache(studentCode, {
    activeParticipation: Number(activeParticipation),
    sincerity: Number(sincerity),
    timelyWork: Number(timelyWork),
    parentScore: parentScore !== undefined ? Number(parentScore) : 50
  });

  return NextResponse.json({
    success: true,
    message: 'Classroom observation logged successfully.'
  }, { headers: NO_CACHE_HEADERS });
}

// ── 3. Login Register Report Handler ──────────────────────────────────
async function handleLoginRegister(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const url = new URL(req.url);
  const dateParam = url.searchParams.get('date');
  const targetDateStr = dateParam || getDateKeyIST();

  const cacheKey = `admin_report_login_register_${targetDateStr}`;
  const cached = getFromCache<any>(cacheKey);
  if (cached) {
    return NextResponse.json(cached, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getLoginRegisterReport(targetDateStr);
  setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 4. Parent Pending Sincerity Report Handler ─────────────────────────
async function handleParentPending(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const cacheKey = 'admin_report_parent_pending';
  const cached = getFromCache<any>(cacheKey);
  if (cached) {
    return NextResponse.json(cached, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getParentPendingReport();
  setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 5. Truth Test Report Handler ──────────────────────────────────────
async function handleTruthTest(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const { searchParams } = new URL(req.url);
  const examId = searchParams.get('examId') || '';

  if (!examId) {
    return NextResponse.json({ message: 'Missing parameters (examId).' }, { status: 400 });
  }

  const cacheKey = `admin_report_truth_test_${examId}`;
  const cached = getFromCache<any>(cacheKey);
  if (cached) {
    return NextResponse.json(cached, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getTruthTestReport(examId);
  setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 6. Usage Report Handler ───────────────────────────────────────────
async function handleUsage(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const cacheKey = 'admin_report_usage';
  const cached = getFromCache<any>(cacheKey);
  if (cached) {
    return NextResponse.json(cached, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getUsageReport();
  setInCache(cacheKey, report, REPORT_CACHE_TTL_MS);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 7. Test Coverage Reset Handler (POST) ─────────────────────────────
async function handleTestCoverageReset(req: NextRequest) {
  const authResult = await verifyAnyRole(req, ['admin']);
  if (!authResult) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const body = await req.json();
  const { subjectId, topicCode, examId } = body;

  if (!subjectId) {
    return NextResponse.json({ error: 'Missing subjectId.' }, { status: 400 });
  }

  const result = await ReportService.resetTestCoverage(subjectId, topicCode, examId);
  invalidateCache('admin_report_');
  return NextResponse.json(result);
}

// ── Main Catch-All Route Dispatcher ──────────────────────────────────
export async function GET(req: NextRequest, { params }: { params: { slug: string[] } | Promise<{ slug: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'daily-practice':
        return await handleDailyPractice(req);
      case 'learning-quotient':
        return await handleLearningQuotientGet(req);
      case 'login-register':
        return await handleLoginRegister(req);
      case 'parent-pending':
        return await handleParentPending(req);
      case 'truth-test':
        return await handleTruthTest(req);
      case 'usage':
        return await handleUsage(req);
      default:
        return NextResponse.json({ message: `Unknown report route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Reports Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug: string[] } | Promise<{ slug: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'learning-quotient':
        return await handleLearningQuotientPost(req);
      case 'test-coverage/reset':
        return await handleTestCoverageReset(req);
      default:
        return NextResponse.json({ message: `Unknown report route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Reports Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
