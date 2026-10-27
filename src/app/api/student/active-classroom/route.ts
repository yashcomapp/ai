import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(request: Request) {
  try {
    const student = await verifyRole(request, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const liveSnap = await adminDb.collection('liveClassrooms')
      .where('status', '==', 'live')
      .orderBy('startedAt', 'desc')
      .limit(1)
      .get();

    if (liveSnap.empty) {
      return NextResponse.json({ hasLiveClass: false });
    }

    const doc = liveSnap.docs[0];
    const data = doc.data();

    const studentData = student.userData || {};
    const studentCode = studentData.studentCode || '';
    const studentName = studentData.name || studentData.email || 'Student';
    const studentBatchIds: string[] = Array.isArray(studentData.batchIds) 
      ? studentData.batchIds 
      : (studentData.batchId ? [studentData.batchId] : []);

    const targetType = data.targetType || 'batch';
    const targetBatches: string[] = data.targetBatches || [];
    const targetStudents: string[] = data.targetStudents || [];

    let isTargeted = false;

    if (targetType === 'batch') {
      isTargeted = studentBatchIds.some(bId => targetBatches.includes(bId));
    } else if (targetType === 'student') {
      isTargeted = targetStudents.includes(studentCode);
    } else if (targetType === 'mixed') {
      isTargeted = studentBatchIds.some(bId => targetBatches.includes(bId)) || targetStudents.includes(studentCode);
    }

    if (!isTargeted) {
      return NextResponse.json({ hasLiveClass: false });
    }

    // Build the Focus Mode Jitsi link:
    // channelLastN=1: Receives only 1 incoming video (Teacher) to save bandwidth and device load
    // startWithAudioMuted=true: Starts with microphone muted
    // startWithVideoMuted=false: Starts with camera ON so teacher can see them
    const studentUrl = `https://meet.jit.si/${data.roomName}#config.channelLastN=1&config.startWithAudioMuted=true&config.startWithVideoMuted=false&userInfo.displayName=${encodeURIComponent(studentName)}`;

    return NextResponse.json({
      hasLiveClass: true,
      session: {
        id: doc.id,
        title: data.title,
        subject: data.subject || '',
        startedAt: data.startedAt,
        startedBy: data.startedBy || 'Teacher',
        studentUrl
      }
    });
  } catch (err: any) {
    console.error('Error in GET /api/student/active-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
