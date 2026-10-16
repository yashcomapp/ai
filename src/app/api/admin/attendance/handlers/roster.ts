import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';
import { isDemoUser } from '@/lib/studentDb';
import { invalidateCache } from '@/lib/firebase/cache';


export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const batchId = searchParams.get('batchId');
    const date = searchParams.get('date'); // YYYY-MM-DD

    if (!batchId || !date) {
      return NextResponse.json({ error: 'Missing batchId or date.' }, { status: 400 });
    }

    // 1. Fetch batch details, students, active leaves, declarations, and attendance concurrently in parallel
    const dateStr = date.replace(/-/g, '');
    const attendanceDocId = `${dateStr}_${batchId}`;

    const [batchDoc, studentsSnap, leavesSnap, declsSnap, attendanceDoc] = await Promise.all([
      adminDb.collection('batches').doc(batchId).get(),
      adminDb.collection('users')
        .where('role', '==', 'student')
        .where('batchIds', 'array-contains', batchId)
        .get(),
      adminDb.collection('leaveApplications')
        .where('endDate', '>=', date)
        .get(),
      adminDb.collection('attendanceDeclarations')
        .where('endDate', '>=', date)
        .get(),
      adminDb.collection('attendance').doc(attendanceDocId).get()
    ]);

    if (!batchDoc.exists) {
      return NextResponse.json({ error: 'Batch not found.' }, { status: 404 });
    }
    const batchName = batchDoc.data()?.name || 'Unknown Batch';

    const students = studentsSnap.docs
      .map(doc => {
        const d = doc.data();
        return {
          studentCode: d.studentCode || '',
          name: d.name || 'Student',
          email: d.email || '',
          parentEmail: d.parentEmail || '',
          batchId: d.batchId || '',
          batchIds: d.batchIds || [],
          status: d.status || 'active'
        };
      })
      .filter(s => s.status === 'active' && !isDemoUser(s));

    const activeLeaves = new Map<string, any>();
    leavesSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode && data.startDate <= date) {
        activeLeaves.set(data.studentCode.toUpperCase(), data);
      }
    });

    const activeDeclarations = new Map<string, any>();
    declsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode && data.startDate <= date) {
        activeDeclarations.set(data.studentCode.toUpperCase(), data);
      }
    });

    const existingRecords = attendanceDoc.exists ? attendanceDoc.data()?.records || {} : {};

    // 5. Merge data to compile current roster status
    const roster = students.map(student => {
      const codeUpper = student.studentCode.toUpperCase();
      const hasLeave = activeLeaves.get(codeUpper);
      const hasDecl = activeDeclarations.get(codeUpper);
      
      let status = 'present';
      let remarks = '';
      let isLeaveApproved = false;
      let pendingLeave = null;
      let selfMarked = false;
      let selfMarkedBy = null;
      let selfMarkedAt = null;

      const rec = existingRecords[student.studentCode] || existingRecords[codeUpper];

      if (hasLeave && hasLeave.status === 'approved') {
        status = 'leave';
        remarks = `Approved Leave: ${hasLeave.remarks || hasLeave.type || 'Leave'}`;
        isLeaveApproved = true;
      } else if (hasDecl && (hasDecl.status === 'leave' || hasDecl.status === 'absent')) {
        status = hasDecl.status;
        remarks = `Parent Declared: ${hasDecl.remarks || (hasDecl.status === 'leave' ? 'Leave' : 'Absent')}`;
        isLeaveApproved = hasDecl.status === 'leave';
        selfMarked = true;
        selfMarkedBy = hasDecl.declaredBy || 'parent';
        selfMarkedAt = hasDecl.createdAt || null;
      } else {
        if (hasLeave && hasLeave.status === 'pending') {
          pendingLeave = {
            id: hasLeave.applicationId || hasLeave.id,
            startDate: hasLeave.startDate,
            endDate: hasLeave.endDate,
            remarks: hasLeave.remarks || '',
            status: hasLeave.status
          };
        }
        if (hasDecl && !rec) {
          status = hasDecl.status || 'present';
          remarks = `Parent Declared: ${hasDecl.remarks || ''}`;
          selfMarked = true;
          selfMarkedBy = hasDecl.declaredBy || 'parent';
          selfMarkedAt = hasDecl.createdAt || null;
        }
        if (rec) {
          status = rec.status || 'present';
          remarks = rec.remarks || '';
          selfMarked = !!rec.selfMarked;
          selfMarkedBy = rec.selfMarkedBy || null;
          selfMarkedAt = rec.selfMarkedAt || null;
        }
      }

      return {
        ...student,
        status,
        remarks,
        isLeaveApproved,
        pendingLeave,
        selfMarked,
        selfMarkedBy,
        selfMarkedAt
      };
    });

    return NextResponse.json({
      success: true,
      batchName,
      date,
      roster,
      isMarked: attendanceDoc.exists
    });
  } catch (error: any) {
    console.error('API GET attendance error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { batchId, date, records } = body; // records: { studentCode: { status, remarks } }

    if (!batchId || !date || !records) {
      return NextResponse.json({ error: 'Missing batchId, date, or records.' }, { status: 400 });
    }

    // ALLOW HISTORICAL EDITS
    const todayStr = getISTDateString();

    const dateStr = date.replace(/-/g, '');
    const attendanceDocId = `${dateStr}_${batchId}`;
    const attendanceRef = adminDb.collection('attendance').doc(attendanceDocId);

    // 1. Fetch batch details and existing attendance in parallel
    const [batchDoc, existingDoc] = await Promise.all([
      adminDb.collection('batches').doc(batchId).get(),
      attendanceRef.get()
    ]);
    const batchName = batchDoc.data()?.name || 'Unknown Batch';
    const existingRecords = existingDoc.exists ? existingDoc.data()?.records || {} : {};

    const updatedRecords: Record<string, any> = {};
    for (const sCode of Object.keys(records)) {
      const sCodeUpper = sCode.toUpperCase();
      const submitted = records[sCode];
      const existing = existingRecords[sCode] || existingRecords[sCodeUpper];

      if (existing && existing.selfMarked && existing.status === submitted.status) {
        // Teacher preserved the self-marked status
        updatedRecords[sCode] = {
          ...submitted,
          selfMarked: true,
          selfMarkedBy: existing.selfMarkedBy || 'student',
          selfMarkedAt: existing.selfMarkedAt || null
        };
      } else {
        // Teacher changed/validated it explicitly, so we clear the voluntary flag
        updatedRecords[sCode] = {
          ...submitted,
          selfMarked: false
        };
      }
    }

    await attendanceRef.set({
      date,
      batchId,
      batchName,
      className: batchDoc.data()?.classNum || '',
      markedBy: admin.decodedToken?.email || 'admin',
      records: updatedRecords,
      updatedAt: new Date().toISOString()
    }, { merge: true });



    const studentCodes = Object.keys(records);
    studentCodes.forEach(code => invalidateCache(`student_attendance_${code.toUpperCase()}`));

    return NextResponse.json({ success: true, message: 'Attendance roster marked successfully.' });
  } catch (error: any) {
    console.error('API POST attendance error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
