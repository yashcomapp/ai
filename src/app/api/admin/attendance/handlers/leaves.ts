import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const leavesSnap = await adminDb.collection('leaveApplications')
      .orderBy('createdAt', 'desc')
      .get();

    const leaves = leavesSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    return NextResponse.json({ success: true, leaves });
  } catch (error: any) {
    console.error('API GET leave requests error:', error);
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
    const { action, leaveId, leaveData } = body;

    if (action === 'create') {
      const { studentCode, studentName, startDate, endDate, type, remarks } = leaveData;
      if (!studentCode || !startDate || !endDate || !type) {
        return NextResponse.json({ error: 'Missing required leave fields.' }, { status: 400 });
      }

      const newLeaveRef = adminDb.collection('leaveApplications').doc();
      const newLeave = {
        applicationId: newLeaveRef.id,
        studentCode,
        studentName: studentName || 'Student',
        startDate, // YYYY-MM-DD
        endDate,   // YYYY-MM-DD
        type,      // "sick" | "planned"
        remarks: remarks || '',
        status: 'approved',
        approvedBy: admin.decodedToken?.email || 'admin',
        createdAt: new Date().toISOString()
      };

      await newLeaveRef.set(newLeave);
      return NextResponse.json({ success: true, leave: { id: newLeaveRef.id, ...newLeave } });
    }

    if (action === 'delete') {
      if (!leaveId) {
        return NextResponse.json({ error: 'Missing leaveId to delete.' }, { status: 400 });
      }
      await adminDb.collection('leaveApplications').doc(leaveId).delete();
      return NextResponse.json({ success: true, message: 'Leave application deleted successfully.' });
    }

    if (action === 'approve') {
      if (!leaveId) {
        return NextResponse.json({ error: 'Missing leaveId to approve.' }, { status: 400 });
      }
      await adminDb.collection('leaveApplications').doc(leaveId).update({
        status: 'approved',
        approvedBy: admin.decodedToken?.email || 'admin',
        approvedAt: new Date().toISOString()
      });
      return NextResponse.json({ success: true, message: 'Leave application approved successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST leave requests error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
