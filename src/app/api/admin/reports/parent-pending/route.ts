import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ReportCacheManager } from '@/lib/reportCache';

export const dynamic = 'force-dynamic';

export interface SincerityRecord {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  batchIds: string[];
  examName: string;
  type: string;
  reviewedByActor: 'parent' | 'student';
  reviewedByEmail?: string;
  photoThumbnail?: string | null;
  photoPurged?: boolean;
  expiresAt?: number | null;
  timestamp: string;
}

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const cacheKey = 'parent-pending-report';
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    // 1. Fetch active students and batches
    const [studentsSnap, batchesSnap, sinceritySnap, evalSnap] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      adminDb.collection('batches')
        .get(),
      adminDb.collection('parentSincerityLogs')
        .orderBy('createdAt', 'desc')
        .limit(300)
        .get()
        .catch(() => ({ docs: [] } as any)),
      adminDb.collection('evaluations')
        .orderBy('createdAt', 'desc')
        .limit(200)
        .get()
        .catch(() => ({ docs: [] } as any))
    ]);

    const activeStudentsMap = new Map<string, any>();
    studentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.status !== 'inactive' && data.studentCode) {
        activeStudentsMap.set(data.studentCode, {
          studentCode: data.studentCode,
          name: data.name || '',
          className: data.className || data.class || '',
          batchIds: data.batchIds || (data.batchId ? [data.batchId] : [])
        });
      }
    });

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    const nowMs = Date.now();
    const records: SincerityRecord[] = [];
    const purgeBatch = adminDb.batch();
    let purgeCount = 0;

    // 2. Process parentSincerityLogs (Exam reviews & Sync Sessions only)
    sinceritySnap.docs.forEach((doc: any) => {
      const data = doc.data();
      const rawType = data.type || '';

      // Strictly exclude individual or bulk practice reviews
      if (rawType === 'practice' || rawType === 'bulk_practice') {
        return;
      }

      const studentInfo = activeStudentsMap.get(data.studentCode);
      if (!studentInfo) return; // Exclude inactive accounts

      let photo = data.photoThumbnail || null;
      let isPurged = Boolean(data.photoPurged);

      // Auto-purge photos older than 24 hours
      if (data.expiresAt && data.expiresAt < nowMs && photo) {
        purgeBatch.update(doc.ref, {
          photoThumbnail: null,
          photoPurged: true
        });
        purgeCount++;
        photo = null;
        isPurged = true;
      }

      let displayType = 'Exam Review';
      let displayExamName = data.examName || 'Exam Paper Review';

      if (rawType === 'daily_5min_sync' || rawType === 'sync') {
        displayType = 'Sync Session';
        displayExamName = data.examName || 'Daily 5-Min Parent-Kid Sync';
      } else if (rawType === 'objective') {
        displayType = 'Objective Exam';
        displayExamName = data.examName || 'Objective Exam Paper Review';
      } else if (rawType === 'subjective') {
        displayType = 'Subjective Exam';
        displayExamName = data.examName || 'Subjective Exam Paper Review';
      } else if (rawType === 'entrance' || rawType === 'mock') {
        displayType = 'Mock Exam';
        displayExamName = data.examName || 'Mock Entrance Exam Review';
      }

      records.push({
        id: doc.id,
        studentCode: data.studentCode,
        studentName: studentInfo.name || data.studentName || 'Student',
        className: studentInfo.className,
        batchIds: studentInfo.batchIds,
        examName: displayExamName,
        type: displayType,
        reviewedByActor: data.reviewedByActor === 'student' ? 'student' : 'parent',
        reviewedByEmail: data.reviewedByEmail || '',
        photoThumbnail: photo,
        photoPurged: isPurged,
        expiresAt: data.expiresAt || null,
        timestamp: data.timestamp || (data.createdAt?.toDate?.()?.toISOString?.()) || new Date().toISOString()
      });
    });

    // 3. Fallback: Include exam evaluations not already logged in parentSincerityLogs
    const existingExamIds = new Set(records.map(r => `${r.studentCode}_${r.id}`));
    evalSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      
      // Strictly ignore practice review approvals from eval logs
      if (data.source?.includes('practice') || data.modelAnswerVersion === 'practice') {
        return;
      }

      const studentInfo = activeStudentsMap.get(data.studentCode);
      if (!studentInfo) return;

      const actor = (data.reviewedByActor === 'student' || data.evaluatorType === 'student') ? 'student' : 'parent';
      const key = `${data.studentCode}_${doc.id}`;
      if (!existingExamIds.has(key)) {
        records.push({
          id: doc.id,
          studentCode: data.studentCode,
          studentName: studentInfo.name || data.studentName || 'Student',
          className: studentInfo.className,
          batchIds: studentInfo.batchIds,
          examName: data.examName || (data.modelAnswerVersion === 'objective' ? 'Objective Exam Review' : 'Subjective Exam Review'),
          type: data.modelAnswerVersion === 'objective' ? 'Objective Exam' : 'Subjective Exam',
          reviewedByActor: actor,
          reviewedByEmail: data.evaluatorName || '',
          photoThumbnail: null,
          photoPurged: false,
          expiresAt: null,
          timestamp: data.createdAt?.toDate?.()?.toISOString?.() || new Date().toISOString()
        });
      }
    });

    // Commit auto-purges if any expired photos were detected
    if (purgeCount > 0) {
      purgeBatch.commit().catch(err => console.warn('Purge batch commit warning:', err));
    }

    // Sort latest first
    records.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

    // 4. Compute Summary Statistics
    const totalReviews = records.length;
    const parentVerifiedCount = records.filter(r => r.reviewedByActor === 'parent').length;
    const studentSoloCount = records.filter(r => r.reviewedByActor === 'student').length;
    const parentSincerityRate = totalReviews > 0 ? Math.round((parentVerifiedCount / totalReviews) * 100) : 100;
    const oneDayAgo = nowMs - 24 * 60 * 60 * 1000;
    const verifiedTodayCount = records.filter(r => r.reviewedByActor === 'parent' && new Date(r.timestamp).getTime() >= oneDayAgo).length;

    const result = {
      success: true,
      batches,
      records,
      summary: {
        totalReviews,
        parentVerifiedCount,
        studentSoloCount,
        parentSincerityRate,
        verifiedTodayCount
      }
    };

    await ReportCacheManager.setReport(cacheKey, result, 60); // Cache for 1 minute

    return NextResponse.json(result);
  } catch (error: any) {
    console.error('Failed to generate parent sincerity reviews report:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
