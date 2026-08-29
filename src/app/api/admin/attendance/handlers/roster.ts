import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

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

    // 1. Fetch batch details, students, active leaves, and attendance concurrently in parallel
    const dateStr = date.replace(/-/g, '');
    const attendanceDocId = `${dateStr}_${batchId}`;

    const [batchDoc, studentsSnap, leavesSnap, attendanceDoc] = await Promise.all([
      adminDb.collection('batches').doc(batchId).get(),
      adminDb.collection('users')
        .where('role', '==', 'student')
        .where('batchIds', 'array-contains', batchId)
        .get(),
      adminDb.collection('leaveApplications')
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
      .filter(s => s.status === 'active');

    const activeLeaves = new Map<string, any>();
    leavesSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode && data.startDate <= date) {
        activeLeaves.set(data.studentCode.toUpperCase(), data);
      }
    });

    const existingRecords = attendanceDoc.exists ? attendanceDoc.data()?.records || {} : {};

    // 5. Merge data to compile current roster status
    const roster = students.map(student => {
      const codeUpper = student.studentCode.toUpperCase();
      const hasLeave = activeLeaves.get(codeUpper);
      
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
        remarks = `Approved Leave: ${hasLeave.remarks || hasLeave.type}`;
        isLeaveApproved = true;
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

    // 1. Get batch name
    const batchDoc = await adminDb.collection('batches').doc(batchId).get();
    const batchName = batchDoc.data()?.name || 'Unknown Batch';

    // 2. Save Daily Attendance document with self-marked validation/corrections preservation
    const attendanceRef = adminDb.collection('attendance').doc(attendanceDocId);
    const existingDoc = await attendanceRef.get();
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

    // 3. Automated Emergency Absence alerts in Direct Message Chats
    const studentCodes = Object.keys(records);
    const absentCodes = studentCodes.filter(sCode => records[sCode].status === 'absent');

    if (absentCodes.length > 0) {
      const batch = adminDb.batch();

      // Resolve all absent students with role == 'student' (chunked to respect Firestore 'in' limit of 30)
      const absentStudentsMap = new Map<string, any>();
      if (absentCodes.length > 0) {
        const chunks = [];
        for (let i = 0; i < absentCodes.length; i += 30) {
          chunks.push(absentCodes.slice(i, i + 30));
        }
        const snaps = await Promise.all(
          chunks.map(chunk =>
            adminDb.collection('users')
              .where('role', '==', 'student')
              .where('studentCode', 'in', chunk)
              .get()
          )
        );

        snaps.forEach(studentsSnap => {
          studentsSnap.docs.forEach(doc => {
            const data = doc.data();
            if (data.studentCode && data.role === 'student') {
              absentStudentsMap.set(data.studentCode.toUpperCase(), data);
            }
          });
        });
      }

      // Batch lookups of direct message rooms
      const roomRefs = absentCodes.map(sCode => adminDb.collection('chatRooms').doc(`room_${sCode}_teacher`));
      const roomSnaps = await adminDb.getAll(...roomRefs);
      const roomsMap = new Map<string, any>();
      roomSnaps.forEach(snap => {
        roomsMap.set(snap.id, snap);
      });

      absentCodes.forEach(sCode => {
        const sCodeUpper = sCode.toUpperCase();
        const studentData = absentStudentsMap.get(sCodeUpper);
        if (!studentData) return;

        const studentName = studentData.name || 'Student';
        const pEmail = studentData.parentEmail || '';

        const roomId = `room_${sCode}_teacher`;
        const roomSnap = roomsMap.get(roomId);
        const roomRef = adminDb.collection('chatRooms').doc(roomId);

        const participants = [sCode, admin.decodedToken?.uid || 'admin'];
        if (pEmail) {
          participants.push(`PR-${pEmail.toLowerCase().trim()}`);
        }

        const alertText = `⚠️ Attendance Alert: ${studentName} has been marked ABSENT for today (${date}).`;

        if (!roomSnap || !roomSnap.exists) {
          batch.set(roomRef, {
            roomId,
            type: 'dm',
            name: `${studentName} (Parent-Teacher DM)`,
            participants,
            unreadCounts: {
              [sCode]: 0,
              ...(pEmail ? { [`PR-${pEmail.toLowerCase().trim()}`]: 1 } : {}),
              [admin.decodedToken?.uid || 'admin']: 0
            },
            lastMessage: {
              text: alertText,
              senderName: 'System',
              timestamp: new Date().toISOString()
            }
          });
        } else {
          const currentUnreads = roomSnap.data()?.unreadCounts || {};
          const nextUnreads = { ...currentUnreads };
          if (pEmail) {
            const pKey = `PR-${pEmail.toLowerCase().trim()}`;
            nextUnreads[pKey] = (nextUnreads[pKey] || 0) + 1;
          }
          batch.update(roomRef, {
            unreadCounts: nextUnreads,
            lastMessage: {
              text: alertText,
              senderName: 'System',
              timestamp: new Date().toISOString()
            }
          });
        }

        // Append Message
        const msgRef = roomRef.collection('messages').doc();
        batch.set(msgRef, {
          messageId: msgRef.id,
          senderId: 'system',
          senderName: 'System Alert',
          senderRole: 'system',
          text: `⚠️ Attendance Alert: **${studentName}** has been marked **ABSENT** for today (${date}). Please contact the admin office if this is an error.`,
          type: 'text',
          createdAt: new Date().toISOString(),
          isDeleted: false,
          readBy: {}
        });
      });

      await batch.commit();
    }

    return NextResponse.json({ success: true, message: 'Attendance roster marked successfully.' });
  } catch (error: any) {
    console.error('API POST attendance error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
