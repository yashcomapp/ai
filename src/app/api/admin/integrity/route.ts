import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { ReportService } from '@/services/report.service';
import { IntegrityService } from '@/services/integrity.service';
export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const url = new URL(request.url);
    const studentCode = url.searchParams.get('studentCode');

    if (studentCode) {
      // Fetch score history for this specific student
      const snap = await adminDb.collection('integrityScores')
        .where('studentCode', '==', studentCode)
        .orderBy('year', 'desc')
        .orderBy('week', 'desc')
        .get();

      const history = snap.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }));

      return NextResponse.json({ history });
    }

    // Fetch aggregate statistics AND student list via ReportService
    const data = await ReportService.getIntegrityReport();
    return NextResponse.json({
      totalScores: data.totalScores,
      reviewCount: data.reviewCount,
      avgScore: data.avgScore,
      students: data.students
    });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// POST: Generate integrity scores for selected students
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();
    const { action, studentCodes, studentCode, week, year, reason } = body;

    // Action A: Reset scores for a single week or all weeks
    if (action === 'resetWeek') {
      if (!studentCode || !week || !year) {
        return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
      }
      const standardDocId = `${studentCode}_${year}_${week}`;
      const legacyDocId = `${studentCode}_W${week}_${year}`;

      // Clean up legacy formatted document
      await adminDb.collection('integrityScores').doc(legacyDocId).delete().catch(() => null);

      await adminDb.collection('integrityScores').doc(standardDocId).set({
        studentCode,
        week: Number(week),
        year: Number(year),
        integrityScore: 100,
        score: 100,
        level: 'excellent',
        violationsCount: 0,
        totalSessions: 0,
        tabViolations: 0,
        noFaceCount: 0,
        multipleFacesCount: 0,
        resetReason: reason || 'Admin override reset',
        updatedAt: new Date()
      }, { merge: true });
      return NextResponse.json({ success: true });
    }

    if (action === 'resetAll') {
      if (!studentCode) {
        return NextResponse.json({ error: 'Missing studentCode parameter' }, { status: 400 });
      }
      const snap = await adminDb.collection('integrityScores')
        .where('studentCode', '==', studentCode)
        .get();

      const batch = new ChunkedBatch(adminDb);
      snap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });
      await batch.commit();
      return NextResponse.json({ success: true });
    }

    // Action B: Generate/Recalculate selected students' integrity scores for current week
    if (!studentCodes || !Array.isArray(studentCodes)) {
      return NextResponse.json({ error: 'Invalid studentCodes array' }, { status: 400 });
    }

    // Determine current Week / Year details
    const currentDate = new Date();
    const currentWeekDetails = IntegrityService.getWeekDetails(currentDate);
    const currentWeek = currentWeekDetails.week;
    const currentYear = currentWeekDetails.year;

    const writeBatch = new ChunkedBatch(adminDb);

    // 1. Fetch practice and exam attempts matching studentCodes using chunked bulk queries
    const reviewsByStudent = new Map<string, any[]>();
    const parentReviewsByStudent = new Map<string, any[]>();

    const chunks = [];
    const chunkSize = 30;
    for (let i = 0; i < studentCodes.length; i += chunkSize) {
      chunks.push(studentCodes.slice(i, i + chunkSize));
    }

    const [reviewsSnapList, parentReviewsSnapList] = await Promise.all([
      Promise.all(chunks.map(chunk =>
        adminDb.collection('reviews').where('studentCode', 'in', chunk).get()
      )),
      Promise.all(chunks.map(chunk =>
        adminDb.collection('parentReviews').where('studentCode', 'in', chunk).get()
      ))
    ]);

    reviewsSnapList.forEach(snap => {
      snap.docs.forEach(doc => {
        const data = doc.data() || {};
        const code = data.studentCode;
        if (code) {
          if (!reviewsByStudent.has(code)) reviewsByStudent.set(code, []);
          reviewsByStudent.get(code)!.push(data);
        }
      });
    });

    parentReviewsSnapList.forEach(snap => {
      snap.docs.forEach(doc => {
        const data = doc.data() || {};
        const code = data.studentCode;
        if (code) {
          if (!parentReviewsByStudent.has(code)) parentReviewsByStudent.set(code, []);
          parentReviewsByStudent.get(code)!.push(data);
        }
      });
    });

    studentCodes.forEach((code) => {
      const studentReviews = reviewsByStudent.get(code) || [];
      const studentParentReviews = parentReviewsByStudent.get(code) || [];

      let totalTabViolations = 0;
      let totalNoFaceCount = 0;
      let totalMultipleFacesCount = 0;
      let totalLookingAwayCount = 0;
      let percentTimeAwaySum = 0;
      let sessionsCount = 0;

      const processDoc = (docData: any) => {
        const dateVal = docData.startedAt?.toDate ? docData.startedAt.toDate() : (docData.createdAt?.toDate ? docData.createdAt.toDate() : (docData.completedAt?.toDate ? docData.completedAt.toDate() : null));
        if (!dateVal) return;
        
        const { year: wYear, week: wWeek } = IntegrityService.getWeekDetails(dateVal);
        if (wYear === currentYear && wWeek === currentWeek) {
          sessionsCount++;
          totalTabViolations += (docData.tabViolations || 0);
          const pViols = docData.proctoringViolations || docData.violations || {};
          totalNoFaceCount += (pViols.noFace || pViols.noFaceCount || 0);
          totalLookingAwayCount += (pViols.lookingAway || pViols.lookingAwayCount || 0);
          totalMultipleFacesCount += (pViols.multipleFaces || pViols.multipleFacesCount || 0);
          percentTimeAwaySum += (docData.percentTimeAway || 0);
        }
      };

      studentReviews.forEach(d => processDoc(d));
      studentParentReviews.forEach(d => processDoc(d));

      const avgPercentTimeAway = sessionsCount > 0 ? (percentTimeAwaySum / sessionsCount) : 0;

      // Calculate score using our single deduplicated IntegrityService
      const normViols = {
        noFace: totalNoFaceCount,
        lookingAway: totalLookingAwayCount,
        multipleFaces: totalMultipleFacesCount,
        headMovement: 0
      };
      
      const { integrityScore } = IntegrityService.calculateScore(totalTabViolations, normViols);

      // Determine level info
      let level = 'excellent';
      if (integrityScore < 40) level = 'review';
      else if (integrityScore < 60) level = 'poor';
      else if (integrityScore < 75) level = 'attention';
      else if (integrityScore < 90) level = 'good';

      const docId = `${code}_${currentYear}_${currentWeek}`;
      const scoreRef = adminDb.collection('integrityScores').doc(docId);

      // Clean up legacy document location to keep DB clean
      const legacyDocId = `${code}_W${currentWeek}_${currentYear}`;
      writeBatch.delete(adminDb.collection('integrityScores').doc(legacyDocId));

      writeBatch.set(scoreRef, {
        studentCode: code,
        week: currentWeek,
        year: currentYear,
        integrityScore: integrityScore,
        score: integrityScore, // Backwards compatibility fallback
        violationsCount: totalTabViolations + totalNoFaceCount + totalLookingAwayCount,
        level,
        totalSessions: sessionsCount,
        tabViolations: totalTabViolations,
        noFaceCount: totalNoFaceCount,
        multipleFacesCount: totalMultipleFacesCount,
        avgPercentTimeAway: Math.round(avgPercentTimeAway),
        createdAt: new Date(),
        updatedAt: new Date()
      }, { merge: true });
    });

    await writeBatch.commit();

    return NextResponse.json({ success: true, count: studentCodes.length });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
