import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST, formatDateIST, formatTimeIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const dateParam = searchParams.get('date') || getDateKeyIST();
    const batchIdParam = searchParams.get('batchId') || 'all';

    // 1. Fetch active students & batches
    const [studentsSnap, batchesSnap] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      adminDb.collection('batches').get()
    ]);

    const batchNameMap = new Map<string, string>();
    const batchClassMap = new Map<string, string>();
    const batchList: { id: string; name: string; classNum: string }[] = [];

    batchesSnap.docs.forEach(doc => {
      const data = doc.data();
      batchNameMap.set(doc.id, data.name || doc.id);
      batchClassMap.set(doc.id, data.classNum || data.className || '');
      batchList.push({
        id: doc.id,
        name: data.name || doc.id,
        classNum: data.classNum || data.className || ''
      });
    });

    // Filter active students only (AGENTS.md Rule C & D)
    const activeStudents = studentsSnap.docs
      .map(doc => ({ id: doc.id, ...doc.data() as any }))
      .filter(s => s.role === 'student' && s.status !== 'inactive');

    // 2. Fetch sync records for this date
    // Query parentReviews with type == 'daily_5min_sync'
    const syncReviewsSnap = await adminDb.collection('parentReviews')
      .where('type', '==', 'daily_5min_sync')
      .get();

    // Build map of studentCode -> sync record matching target date
    const studentSyncMap = new Map<string, any>();

    syncReviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const sCode = data.studentCode || data.childStudentCode;
      if (!sCode) return;

      // Extract IST date key
      let recordDate = data.date;
      if (!recordDate) {
        const rawTime = data.reviewedAt || data.createdAt || data.timestamp;
        const d = rawTime?.toDate ? rawTime.toDate() : rawTime ? new Date(rawTime) : null;
        if (d) {
          recordDate = getDateKeyIST(d);
        }
      }

      if (recordDate === dateParam) {
        const rawTime = data.reviewedAt || data.createdAt || data.timestamp;
        const d = rawTime?.toDate ? rawTime.toDate() : rawTime ? new Date(rawTime) : null;
        const timeFormatted = d ? formatTimeIST(d) : 'Recorded';

        studentSyncMap.set(sCode, {
          id: doc.id,
          status: 'completed',
          completedAt: timeFormatted,
          rawTimestamp: d ? d.getTime() : 0,
          reviewedBy: data.reviewedBy || data.parentEmail || 'Parent',
          feedback: data.feedback || 'Daily Sync Verified'
        });
      }
    });

    // 3. Compile student attendance rows
    const attendanceRows: any[] = [];

    activeStudents.forEach(student => {
      const sCode = student.studentCode || student.id;
      const studentBatchIds: string[] = Array.isArray(student.batchIds) 
        ? student.batchIds 
        : (student.batchId ? [student.batchId] : []);

      // Check batch filter
      if (batchIdParam !== 'all' && !studentBatchIds.includes(batchIdParam)) {
        return;
      }

      const primaryBatchId = studentBatchIds[0] || '';
      const batchName = batchNameMap.get(primaryBatchId) || student.batchName || 'General Batch';
      const className = student.className || (primaryBatchId ? `Class ${batchClassMap.get(primaryBatchId)}` : 'Class 8');

      const syncInfo = studentSyncMap.get(sCode);
      const isCompleted = !!syncInfo;

      attendanceRows.push({
        studentCode: sCode,
        studentName: student.name || 'Student',
        className,
        batchId: primaryBatchId,
        batchName,
        status: isCompleted ? 'completed' : 'pending',
        completedAt: isCompleted ? syncInfo.completedAt : '—',
        reviewedBy: isCompleted ? syncInfo.reviewedBy : '—',
        feedback: isCompleted ? syncInfo.feedback : 'Pending Review'
      });
    });

    // Sort: Pending first or alphabetically by student name
    attendanceRows.sort((a, b) => a.studentName.localeCompare(b.studentName));

    const totalStudents = attendanceRows.length;
    const completedCount = attendanceRows.filter(r => r.status === 'completed').length;
    const pendingCount = totalStudents - completedCount;
    const syncPercentage = totalStudents > 0 ? Math.round((completedCount / totalStudents) * 100) : 0;

    return NextResponse.json({
      success: true,
      date: dateParam,
      batchId: batchIdParam,
      batches: batchList,
      summary: {
        totalStudents,
        completedCount,
        pendingCount,
        syncPercentage
      },
      records: attendanceRows
    });

  } catch (error: any) {
    console.error('API parent sync attendance error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
