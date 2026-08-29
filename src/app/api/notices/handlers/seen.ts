import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { verifyAnyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const verified = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!verified) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { decodedToken, userData, role: roleVal } = verified;
    let parentAuth = roleVal === 'parent' ? { decodedToken, userData } : null;
    let studentAuth = roleVal === 'student' ? { decodedToken, userData } : null;
    if (roleVal === 'admin') {
      studentAuth = { decodedToken, userData };
    }

    const { noticeId, remove, reason, remarks } = await req.json();
    if (!noticeId) {
      return NextResponse.json({ message: 'Missing noticeId' }, { status: 400 });
    }

    let userCode = '';
    let userName = '';
    let role: 'student' | 'parent' = 'student';
    let batchId: string | null = null;
    let batchName: string | null = null;

    if (studentAuth) {
      const studentData = studentAuth.userData;
      userCode = studentData.studentCode || '';
      userName = studentData.name || 'Student';
      role = 'student';
      batchId = studentData.batchId || null;
      
      if (batchId) {
        const batchSnap = await adminDb.collection('batches').doc(batchId).get();
        if (batchSnap.exists) {
          batchName = batchSnap.data()?.name || null;
        }
      }
    } else if (parentAuth) {
      const parentData = parentAuth.userData;
      userCode = parentData.email?.toLowerCase() || '';
      userName = parentData.name || 'Parent';
      role = 'parent';
    }

    if (!userCode) {
      return NextResponse.json({ message: 'Missing user identifier profile.' }, { status: 400 });
    }

    const logId = `${noticeId}_${userCode}`;

    if (remove) {
      await adminDb.collection('noticeSeenLogs').doc(logId).delete();
      return NextResponse.json({ success: true, message: 'Notice marked as unseen successfully' });
    }

    const logData: any = {
      noticeId,
      userCode,
      userName,
      role,
      seenAt: admin.firestore.FieldValue.serverTimestamp(),
      batchId,
      batchName
    };

    const finalReasonText = (reason === 'other' || reason === '💬 Other Reason' || reason === '💬 Other (Custom Note)' || reason === 'Other') 
      ? (remarks || 'Other Reason') 
      : (reason || remarks || '');

    if (reason || remarks) {
      logData.reason = reason;
      logData.reasonLabel = finalReasonText;
    }
    if (remarks) {
      logData.remarks = remarks;
    }

    await adminDb.collection('noticeSeenLogs').doc(logId).set(logData, { merge: true });

    // Also update response summary inside the notice document and sync to examAbsenceReasons for Exam Register
    if (reason || remarks) {
      const noticeSnap = await adminDb.collection('notices').doc(noticeId).get().catch(() => null);
      const noticeData = noticeSnap && noticeSnap.exists ? noticeSnap.data() : null;

      await adminDb.collection('notices').doc(noticeId).set({
        responses: {
          [userCode]: {
            userName,
            role,
            reason: finalReasonText,
            remarks: remarks || '',
            respondedAt: new Date().toISOString()
          }
        }
      }, { merge: true }).catch(() => null);

      // Sync reason to Exam Register (examAbsenceReasons collection)
      if (noticeData) {
        const examId = noticeData.examId;
        const targetStudentCode = noticeData.studentCode || (Array.isArray(noticeData.targetValues) && noticeData.targetValues[0]) || (role === 'student' ? userCode : '');

        if (examId && targetStudentCode) {
          await adminDb.collection('examAbsenceReasons').doc(`${targetStudentCode}_${examId}`).set({
            studentCode: targetStudentCode,
            examId,
            reason: finalReasonText,
            updatedBy: `${userName} (${role})`,
            updatedAt: new Date()
          }, { merge: true }).catch(err => console.error('Error syncing absence reason to Exam Register:', err));
        }
      }
    }

    return NextResponse.json({ success: true, message: 'Notice marked as seen successfully' });
  } catch (error: any) {
    console.error('API POST notices seen error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
