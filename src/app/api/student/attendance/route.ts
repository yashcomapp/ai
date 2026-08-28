import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';
import { calculateAttendanceSummary } from '@/lib/attendanceUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    let studentCode = '';
    let batchIds: string[] = [];

    // 1. Authenticate student user
    const studentSession = await verifyRole(req, 'student');
    if (studentSession) {
      studentCode = studentSession.userData?.studentCode || '';
      batchIds = studentSession.userData?.batchIds || (studentSession.userData?.batchId ? [studentSession.userData?.batchId] : []);
    } else {
      // 2. Fallback: Authenticate parent user
      const parentSession = await verifyRole(req, 'parent');
      if (parentSession) {
        const { searchParams } = new URL(req.url);
        const targetStudentCode = searchParams.get('studentCode')?.trim().toUpperCase();
        
        const parentData = parentSession.userData;
        let parentCodes: string[] = [];
        if (Array.isArray(parentData?.studentCodes)) {
          parentCodes = parentData.studentCodes.filter(Boolean);
        } else if (parentData?.studentCode) {
          parentCodes = [parentData.studentCode];
        }

        const parentEmail = parentData?.email?.toLowerCase()?.trim();
        if (parentEmail) {
          const querySnap = await adminDb.collection('users')
            .where('role', '==', 'student')
            .where('parentEmail', '==', parentEmail)
            .get();
          querySnap.docs.forEach(doc => {
            const data = doc.data();
            if (data.studentCode && !parentCodes.includes(data.studentCode)) {
              parentCodes.push(data.studentCode);
            }
          });
        }
        const parentCodesUpper = parentCodes.map((c: string) => c.toUpperCase());

        if (targetStudentCode && parentCodesUpper.includes(targetStudentCode)) {
          studentCode = targetStudentCode;
        } else if (parentCodesUpper.length > 0) {
          studentCode = parentCodesUpper[0];
        }

        if (studentCode) {
          // Fetch child batchIds with strict role == 'student' filter
          const studentQuery = await adminDb.collection('users')
            .where('role', '==', 'student')
            .where('studentCode', '==', studentCode)
            .limit(1)
            .get();
          if (!studentQuery.empty) {
            const sd = studentQuery.docs[0].data();
            batchIds = sd.batchIds || (sd.batchId ? [sd.batchId] : []);
          }
        }
      }
    }

    if (!studentCode || batchIds.length === 0) {
      return NextResponse.json({ message: 'Unauthorized or no active batches found.' }, { status: 403 });
    }

    const sCodeUpper = studentCode.trim().toUpperCase();

    // 3. Fetch all daily attendance documents for the student's batches
    const attendanceSnap = await adminDb.collection('attendance')
      .where('batchId', 'in', batchIds)
      .get();

    const recordsList: any[] = [];
    const dailyLogs = attendanceSnap.docs.map(doc => {
      const data = doc.data();
      const rec = data.records?.[sCodeUpper] || data.records?.[studentCode] || null;

      let status = 'not_marked';
      let remarks = '';
      let selfMarked = false;
      let selfMarkedBy = null;
      let selfMarkedAt = null;

      if (rec) {
        status = rec.status || 'present';
        remarks = rec.remarks || '';
        selfMarked = !!rec.selfMarked;
        selfMarkedBy = rec.selfMarkedBy || null;
        selfMarkedAt = rec.selfMarkedAt || null;
        recordsList.push(rec);
      }

      return {
        date: data.date,
        batchName: data.batchName || 'Class',
        status,
        remarks,
        selfMarked,
        selfMarkedBy,
        selfMarkedAt
      };
    }).sort((a, b) => b.date.localeCompare(a.date));

    const summary = calculateAttendanceSummary(recordsList);

    // Check if student has approved leave today
    const todayStr = getISTDateString();
    const leavesSnap = await adminDb.collection('leaveApplications')
      .where('studentCode', '==', sCodeUpper)
      .where('status', '==', 'approved')
      .get();

    let isCurrentlyOnLeaveToday = false;
    leavesSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.startDate <= todayStr && data.endDate >= todayStr) {
        isCurrentlyOnLeaveToday = true;
      }
    });

    return NextResponse.json({
      success: true,
      stats: {
        totalDays: summary.totalDays,
        presentDays: summary.presentDays,
        absentDays: summary.absentDays,
        leaveDays: summary.leaveDays,
        lateDays: summary.lateDays,
        halfDays: summary.halfDays,
        effectivePresentDays: summary.effectivePresentDays,
        attendanceRate: summary.attendancePercentage,
        attendancePercentage: summary.attendancePercentage
      },
      dailyLogs,
      isCurrentlyOnLeaveToday
    });
  } catch (error: any) {
    console.error('API GET student attendance error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    let studentCode = '';
    let batchIds: string[] = [];
    let markedBy = 'student';
    const body = await req.json().catch(() => ({}));
    const { status, remarks } = body;

    // 1. Authenticate student user
    const studentSession = await verifyRole(req, 'student');
    if (studentSession) {
      studentCode = studentSession.userData?.studentCode || '';
      batchIds = studentSession.userData?.batchIds || (studentSession.userData?.batchId ? [studentSession.userData?.batchId] : []);
      markedBy = 'student';
    } else {
      // 2. Fallback: Authenticate parent user
      const parentSession = await verifyRole(req, 'parent');
      if (parentSession) {
        const { searchParams } = new URL(req.url);
        const targetStudentCode = (body.studentCode || searchParams.get('studentCode'))?.trim().toUpperCase();
        
        const parentData = parentSession.userData;
        let parentCodes: string[] = [];
        if (Array.isArray(parentData?.studentCodes)) {
          parentCodes = parentData.studentCodes.filter(Boolean);
        } else if (parentData?.studentCode) {
          parentCodes = [parentData.studentCode];
        }

        const parentEmail = parentData?.email?.toLowerCase()?.trim();
        if (parentEmail) {
          const querySnap = await adminDb.collection('users')
            .where('role', '==', 'student')
            .where('parentEmail', '==', parentEmail)
            .get();
          querySnap.docs.forEach(doc => {
            const data = doc.data();
            if (data.studentCode && !parentCodes.includes(data.studentCode)) {
              parentCodes.push(data.studentCode);
            }
          });
        }
        const parentCodesUpper = parentCodes.map((c: string) => c.toUpperCase());

        if (targetStudentCode && parentCodesUpper.includes(targetStudentCode)) {
          studentCode = targetStudentCode;
        } else if (parentCodesUpper.length > 0) {
          studentCode = parentCodesUpper[0];
        }

        if (studentCode) {
          // Fetch child batchIds with strict role == 'student' filter
          const studentQuery = await adminDb.collection('users')
            .where('role', '==', 'student')
            .where('studentCode', '==', studentCode)
            .limit(1)
            .get();
          if (!studentQuery.empty) {
            const sd = studentQuery.docs[0].data();
            batchIds = sd.batchIds || (sd.batchId ? [sd.batchId] : []);
          }
        }
        markedBy = 'parent';
      }
    }

    if (!studentCode || batchIds.length === 0) {
      return NextResponse.json({ message: 'Unauthorized or no active batches found.' }, { status: 403 });
    }

    const sCodeUpper = studentCode.trim().toUpperCase();

    if (!status || !['present', 'half_day', 'absent', 'leave'].includes(status)) {
      return NextResponse.json({ error: 'Invalid status value.' }, { status: 400 });
    }

    const todayStr = getISTDateString();
    const dateStr = todayStr.replace(/-/g, '');

    // Check if ALREADY marked in any batch (in a single batch read)
    const docRefs = batchIds.map((bId: string) => adminDb.collection('attendance').doc(`${dateStr}_${bId}`));
    const docSnaps = docRefs.length > 0 ? await adminDb.getAll(...docRefs).catch(() => []) : [];
    const docMap = new Map(docSnaps.map((snap: any) => [snap.id, snap]));

    for (const snap of docSnaps) {
      if (snap.exists) {
        const records = snap.data()?.records || {};
        const rec = records[sCodeUpper];
        if (rec) {
          return NextResponse.json({
            error: 'Attendance has already been marked and is now locked (non-editable).'
          }, { status: 400 });
        }
      }
    }

    // Determine which batches need their names resolved
    const missingBatchesList = batchIds.filter((bId: string) => {
      const snap = docMap.get(`${dateStr}_${bId}`);
      return !snap || !snap.exists;
    });

    let batchNamesMap = new Map<string, string>();
    if (missingBatchesList.length > 0) {
      const batchRefs = missingBatchesList.map((bId: string) => adminDb.collection('batches').doc(bId));
      const batchSnaps = await adminDb.getAll(...batchRefs).catch(() => []);
      batchNamesMap = new Map(batchSnaps.map((snap: any) => [
        snap.id,
        snap.exists ? (snap.data()?.name || 'Unknown Batch') : 'Unknown Batch'
      ]));
    }

    // Batch write all records in a single transaction writeBatch
    const writeBatch = adminDb.batch();
    const recordUpdate = {
      status,
      remarks: remarks || `Voluntary marking (${markedBy})`,
      selfMarked: true,
      selfMarkedBy: markedBy,
      selfMarkedAt: new Date().toISOString()
    };

    for (const bId of batchIds) {
      const attendanceDocId = `${dateStr}_${bId}`;
      const docRef = adminDb.collection('attendance').doc(attendanceDocId);
      const snap = docMap.get(attendanceDocId);

      if (!snap || !snap.exists) {
        const batchName = batchNamesMap.get(bId) || 'Unknown Batch';
        writeBatch.set(docRef, {
          date: todayStr,
          batchId: bId,
          batchName,
          records: {
            [sCodeUpper]: recordUpdate
          },
          createdAt: new Date().toISOString()
        });
      } else {
        writeBatch.update(docRef, {
          [`records.${sCodeUpper}`]: recordUpdate
        });
      }
    }

    await writeBatch.commit();

    return NextResponse.json({ success: true, message: 'Attendance marked successfully.' });
  } catch (error: any) {
    console.error('API POST student attendance error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
