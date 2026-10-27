import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

// Direct read from config/liveClassrooms (SSOT maintained in real-time by admin actions, zero staleness)
const SESSION_EXPIRY_MS = 100 * 60 * 1000; // 100 minutes max session duration (public Jitsi meetings limited to 95 mins)

export async function GET(request: Request) {
  try {
    const student = await verifyRole(request, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const configSnap = await adminDb.collection('config').doc('liveClassrooms').get();
    if (!configSnap.exists) {
      return NextResponse.json({ hasLiveClass: false });
    }

    const configData = configSnap.data();
    const sessions: any[] = Array.isArray(configData?.activeSessions) ? configData.activeSessions : [];
    const now = Date.now();

    // Filter active sessions within 100 minutes expiry
    const activeSessions = sessions.filter((s: any) => {
      if (!s || s.status !== 'live') return false;
      const startMs = new Date(s.startedAt || 0).getTime();
      return now - startMs <= SESSION_EXPIRY_MS;
    });

    if (activeSessions.length === 0) {
      return NextResponse.json({ hasLiveClass: false });
    }

    const studentData = student.userData || {};
    const studentCode = studentData.studentCode || '';
    // Format student display name cleanly (never expose student email to third-party public rooms)
    const studentName = (studentData.name || 'Student').trim().replace(/[^a-zA-Z0-9\s]/g, '') || 'Student';
    const studentBatchIds: string[] = Array.isArray(studentData.batchIds) 
      ? studentData.batchIds 
      : (studentData.batchId ? [studentData.batchId] : []);

    // Check ALL active sessions to find if ANY active session targets this student
    const matchedSession = activeSessions.find((s: any) => {
      const targetType = s.targetType || 'batch';
      const targetBatches: string[] = s.targetBatches || [];
      const targetStudents: string[] = s.targetStudents || [];

      if (targetType === 'batch') {
        return studentBatchIds.some(bId => targetBatches.includes(bId));
      } else if (targetType === 'student') {
        return targetStudents.includes(studentCode);
      } else if (targetType === 'mixed') {
        return studentBatchIds.some(bId => targetBatches.includes(bId)) || targetStudents.includes(studentCode);
      }
      return false;
    });

    if (!matchedSession) {
      return NextResponse.json({ hasLiveClass: false });
    }

    // Build the Focus Mode Jitsi link:
    // channelLastN=1: Receives only 1 incoming video (Teacher) to save bandwidth and device load
    // startWithAudioMuted=true: Starts with microphone muted
    // startWithVideoMuted=false: Starts with camera ON so teacher can see them
    const studentUrl = `https://meet.jit.si/${matchedSession.roomName}#config.channelLastN=1&config.startWithAudioMuted=true&config.startWithVideoMuted=false&userInfo.displayName=${encodeURIComponent(studentName)}`;

    return NextResponse.json({
      hasLiveClass: true,
      session: {
        id: matchedSession.id,
        title: matchedSession.title,
        subject: matchedSession.subject || '',
        passcode: matchedSession.passcode || '',
        startedAt: matchedSession.startedAt,
        startedBy: matchedSession.startedBy || 'Teacher',
        studentUrl
      }
    });
  } catch (err: any) {
    console.error('Error in GET /api/student/active-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
