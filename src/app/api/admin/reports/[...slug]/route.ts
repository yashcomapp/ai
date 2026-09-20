import { NextRequest, NextResponse } from 'next/server';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportService } from '@/services/report.service';
import { QuotientService } from '@/services/quotient.service';
import { ReportCacheManager } from '@/lib/reportCache';
import { adminDb } from '@/lib/firebase/admin';
import { chunkArray } from '@/lib/firestoreUtils';

export const dynamic = 'force-dynamic';

const REPORT_CACHE_HEADERS = {
  'Cache-Control': 'private, s-maxage=60, stale-while-revalidate=120'
};

// ── 1. Daily Practice Report Handler ──────────────────────────────────
async function handleDailyPractice(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const { searchParams } = new URL(req.url);
  const dateParam = searchParams.get('date');
  const targetDateStr = dateParam || getDateKeyIST();

  const report = await ReportService.getDailyPracticeReport(targetDateStr);
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
    const report = await ReportService.getSingleLearningQuotientReport(studentCode, duration);
    return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
  }

  const report = await ReportService.getBulkLearningQuotientReport(duration);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

async function handleLearningQuotientPost(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const body = await req.json();
  const { action } = body;
  const actorEmail = adminUser.userData?.email || adminUser.decodedToken?.email || 'admin';

  if (action === 'saveParameter') {
    const { parameterId, name } = body;
    if (!name) {
      return NextResponse.json({ message: 'Parameter name is required.' }, { status: 400 });
    }
    const id = parameterId || name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    await adminDb.collection('quotientParameters').doc(id).set({
      id,
      name,
      createdAt: new Date()
    });
    await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-monthly');
    await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-weekly');
    return NextResponse.json({ success: true, message: 'Parameter saved successfully.', parameter: { id, name } });
  }

  if (action === 'deleteParameter') {
    const { parameterId } = body;
    if (!parameterId) {
      return NextResponse.json({ message: 'Parameter ID is required.' }, { status: 400 });
    }
    await adminDb.collection('quotientParameters').doc(parameterId).delete();
    await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-monthly');
    await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-weekly');
    return NextResponse.json({ success: true, message: 'Parameter deleted successfully.' });
  }

  if (action === 'batchAward') {
    const { studentCodes, parameterId, score } = body;
    if (!studentCodes || !Array.isArray(studentCodes) || !parameterId || score === undefined) {
      return NextResponse.json({ message: 'Missing required parameters for batch award.' }, { status: 400 });
    }

    const codeChunks = chunkArray(studentCodes, 30);
    const deletePromises = codeChunks.map(async (chunk) => {
      const snapshot = await adminDb.collection('studentObservations')
        .where('parameterId', '==', parameterId)
        .where('studentCode', 'in', chunk)
        .get();
      
      const deleteBatch = adminDb.batch();
      snapshot.docs.forEach(doc => {
        deleteBatch.delete(doc.ref);
      });
      await deleteBatch.commit();
    });
    await Promise.all(deletePromises);

    const chunkedBatch = adminDb.batch();
    studentCodes.forEach(code => {
      const ref = adminDb.collection('studentObservations').doc();
      chunkedBatch.set(ref, {
        studentCode: code,
        parameterId,
        score: Number(score),
        observedBy: actorEmail,
        observedAt: new Date()
      });
    });
    await chunkedBatch.commit();

    return NextResponse.json({ success: true, message: 'Batch award observation logged successfully.' });
  }

  if (action === 'logSingleObservation') {
    const { studentCode, scores } = body;
    if (!studentCode || !scores || typeof scores !== 'object') {
      return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
    }

    const paramIds = Object.keys(scores);
    if (paramIds.length > 0) {
      const existingQuery = await adminDb.collection('studentObservations')
        .where('studentCode', '==', studentCode)
        .where('parameterId', 'in', paramIds)
        .get();
      
      const deleteBatch = adminDb.batch();
      existingQuery.docs.forEach(doc => {
        deleteBatch.delete(doc.ref);
      });
      await deleteBatch.commit();
    }

    const chunkedBatch = adminDb.batch();
    Object.entries(scores).forEach(([paramId, scoreVal]) => {
      const ref = adminDb.collection('studentObservations').doc();
      chunkedBatch.set(ref, {
        studentCode,
        parameterId: paramId,
        score: Number(scoreVal),
        observedBy: actorEmail,
        observedAt: new Date()
      });
    });
    await chunkedBatch.commit();

    return NextResponse.json({ success: true, message: 'Student observation logged successfully.' });
  }

  // Default action: save standard classroom observation
  const { studentCode, activeParticipation, sincerity, timelyWork } = body;

  if (!studentCode || activeParticipation === undefined || sincerity === undefined || timelyWork === undefined) {
    return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
  }

  const existingQuery = await adminDb.collection('studentObservations')
    .where('studentCode', '==', studentCode)
    .get();
  
  const deleteBatch = adminDb.batch();
  existingQuery.docs.forEach(doc => {
    deleteBatch.delete(doc.ref);
  });
  await deleteBatch.commit();

  await QuotientService.saveObservation({
    studentCode,
    activeParticipation: Number(activeParticipation),
    sincerity: Number(sincerity),
    timelyWork: Number(timelyWork),
    observedBy: actorEmail
  });

  return NextResponse.json({
    success: true,
    message: 'Classroom observation logged successfully.'
  });
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

  const report = await ReportService.getLoginRegisterReport(targetDateStr);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 4. Parent Pending Sincerity Report Handler ─────────────────────────
async function handleParentPending(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const report = await ReportService.getParentPendingReport();
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

  const report = await ReportService.getTruthTestReport(examId);
  return NextResponse.json(report, { headers: REPORT_CACHE_HEADERS });
}

// ── 6. Usage Report Handler ───────────────────────────────────────────
async function handleUsage(req: NextRequest) {
  const adminUser = await verifyRole(req, 'admin');
  if (!adminUser) {
    return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
  }

  const report = await ReportService.getUsageReport();
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
