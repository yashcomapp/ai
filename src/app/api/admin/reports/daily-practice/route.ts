import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ReportCacheManager } from '@/lib/reportCache';
import { getDateKeyIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const dateParam = searchParams.get('date');
    const targetDateStr = dateParam || getDateKeyIST(); // YYYY-MM-DD

    const cacheKey = `daily-practice-report-${targetDateStr}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    // Setup date boundaries in IST (UTC+5:30)
    const startOfISTDay = new Date(`${targetDateStr}T00:00:00+05:30`);
    const endOfISTDay = new Date(`${targetDateStr}T23:59:59.999+05:30`);

    const now = new Date();

    // 1. Fetch active students, batches, and active locks in parallel
    const [studentsSnap, batchesSnap, rawReviewsSnap, masterySnapWithDailyLock, masterySnapWithCooldown] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      adminDb.collection('batches')
        .get(),
      adminDb.collection('parentReviews')
        .where('createdAt', '>=', startOfISTDay)
        .where('createdAt', '<=', endOfISTDay)
        .get(),
      adminDb.collection('studentTopicMastery')
        .where('dailyLockedUntil', '>', now)
        .get(),
      adminDb.collection('studentTopicMastery')
        .where('cooldownUntil', '>', now)
        .get()
    ]);

    const activeStudents = studentsSnap.docs
      .map(doc => {
        const data = doc.data();
        return {
          id: doc.id,
          studentCode: data.studentCode || '',
          name: data.name || 'Unknown Student',
          status: data.status || 'active',
          batchIds: data.batchIds || (data.batchId ? [data.batchId] : []),
          className: data.className || data.class || '',
          isAutonomous: data.autonomous === true
        };
      })
      .filter(s => s.status !== 'inactive');

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    // Filter reviews in memory to avoid composite index requirement
    const reviewsDocs = rawReviewsSnap.docs.filter(doc => doc.data().type === 'practice');

    // Group practice sessions by studentCode
    const practiceSessionsByStudent: Record<string, any[]> = {};
    reviewsDocs.forEach(doc => {
      const data = doc.data();
      const studentCode = data.studentCode;
      if (!studentCode) return;

      if (!practiceSessionsByStudent[studentCode]) {
        practiceSessionsByStudent[studentCode] = [];
      }
      practiceSessionsByStudent[studentCode].push({
        id: doc.id,
        ...data,
        createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : (data.createdAt ? new Date(data.createdAt) : null),
        startedAt: data.startedAt?.toDate ? data.startedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null)
      });
    });

    // Merge and compile student topic mastery locks duplicate-free
    const activeMasteryDocs = new Map<string, any>();
    masterySnapWithDailyLock.docs.forEach(doc => activeMasteryDocs.set(doc.id, doc.data()));
    masterySnapWithCooldown.docs.forEach(doc => activeMasteryDocs.set(doc.id, doc.data()));

    const locksByStudent: Record<string, string[]> = {};
    for (const data of activeMasteryDocs.values()) {
      const studentCode = data.studentCode;
      if (!studentCode) continue;

      const topicCode = data.topicCode || 'Unknown Topic';
      const dailyLockedUntil = data.dailyLockedUntil?.toDate ? data.dailyLockedUntil.toDate() : (data.dailyLockedUntil ? new Date(data.dailyLockedUntil) : null);
      const cooldownUntil = data.cooldownUntil?.toDate ? data.cooldownUntil.toDate() : (data.cooldownUntil ? new Date(data.cooldownUntil) : null);

      if (!locksByStudent[studentCode]) {
        locksByStudent[studentCode] = [];
      }

      if (dailyLockedUntil && dailyLockedUntil > now) {
        locksByStudent[studentCode].push(`${topicCode}: Daily Lock`);
      }
      if (cooldownUntil && cooldownUntil > now) {
        locksByStudent[studentCode].push(`${topicCode}: Cooldown Lock`);
      }
    }

    // Compile daily summary for each student
    const studentSummaries = activeStudents.map(student => {
      const studentCode = student.studentCode;
      const sessions = practiceSessionsByStudent[studentCode] || [];

      let totalSessions = sessions.length;
      let totalAccuracy = 0;
      let totalHonesty = 0;
      let totalMastery = 0;
      let totalQuestions = 0;
      let totalTimeSpent = 0;

      sessions.forEach(sess => {
        // Accuracy (scorePercent)
        totalAccuracy += sess.scorePercent !== undefined ? Number(sess.scorePercent) : 0;

        // Honesty (integrityScore)
        totalHonesty += sess.integrityScore !== undefined ? Number(sess.integrityScore) : 100;

        // Mastery (masteryAfter)
        totalMastery += sess.masteryAfter !== undefined ? Number(sess.masteryAfter) : 0;

        // Questions solved
        totalQuestions += sess.totalQuestions !== undefined ? Number(sess.totalQuestions) : 0;

        // Time spent calculation (difference between createdAt and startedAt in seconds)
        if (sess.createdAt && sess.startedAt) {
          const duration = Math.max(0, Math.floor((sess.createdAt.getTime() - sess.startedAt.getTime()) / 1000));
          totalTimeSpent += duration;
        }
      });

      const avgAccuracy = totalSessions > 0 ? parseFloat((totalAccuracy / totalSessions).toFixed(1)) : 0;
      const avgHonesty = totalSessions > 0 ? parseFloat((totalHonesty / totalSessions).toFixed(1)) : 100;
      const avgMastery = totalSessions > 0 ? parseFloat((totalMastery / totalSessions).toFixed(1)) : 0;

      return {
        studentCode,
        name: student.name,
        batchIds: student.batchIds,
        className: student.className,
        isAutonomous: student.isAutonomous,
        activeLocks: locksByStudent[studentCode] || [],
        sessionsCount: totalSessions,
        avgAccuracy,
        avgHonesty, // Keep legacy key name for compatibility
        avgMastery,
        totalQuestions,
        totalTimeSpent
      };
    });

    const result = {
      success: true,
      date: targetDateStr,
      batches,
      students: studentSummaries
    };

    await ReportCacheManager.setReport(cacheKey, result, 60); // Cache for 1 minute

    return NextResponse.json(result);

  } catch (error: any) {
    console.error('API load daily practice report error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
