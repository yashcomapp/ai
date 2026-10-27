import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

// In-memory server cache to eliminate continuous Firestore reads on student polling (TTL: 15s)
let liveSessionsCache: { timestamp: number; sessions: Array<{ id: string; data: any }> } = {
  timestamp: 0,
  sessions: []
};

const SESSION_EXPIRY_MS = 100 * 60 * 1000; // 100 minutes max session duration (public Jitsi meetings limited to 95 mins)

export async function GET(request: Request) {
  try {
    const student = await verifyRole(request, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const now = Date.now();
    let activeSessions = liveSessionsCache.sessions;

    // Refresh cache if stale (> 15 seconds)
    if (now - liveSessionsCache.timestamp > 15000) {
      const liveSnap = await adminDb.collection('liveClassrooms')
        .where('status', '==', 'live')
        .get();

      const validSessions: Array<{ id: string; data: any }> = [];
      const expiredSessionIds: string[] = [];

      liveSnap.docs.forEach(doc => {
        const data = doc.data();
        const startMs = new Date(data.startedAt || 0).getTime();
        if (now - startMs > SESSION_EXPIRY_MS) {
          expiredSessionIds.push(doc.id);
        } else {
          validSessions.push({ id: doc.id, data });
        }
      });

      // Sort newest first
      validSessions.sort((a, b) => {
        const aTime = new Date(a.data.startedAt || 0).getTime();
        const bTime = new Date(b.data.startedAt || 0).getTime();
        return bTime - aTime;
      });

      liveSessionsCache = {
        timestamp: now,
        sessions: validSessions
      };
      activeSessions = validSessions;

      // Opportunistically auto-end expired sessions in background
      if (expiredSessionIds.length > 0) {
        const batch = adminDb.batch();
        expiredSessionIds.forEach(id => {
          batch.update(adminDb.collection('liveClassrooms').doc(id), {
            status: 'ended',
            endedAt: new Date().toISOString(),
            endedReason: 'auto_expired'
          });
        });
        batch.commit().catch(e => console.warn('Failed to auto-expire live sessions:', e));
      }
    }

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
    const matchedSession = activeSessions.find(({ data }) => {
      const targetType = data.targetType || 'batch';
      const targetBatches: string[] = data.targetBatches || [];
      const targetStudents: string[] = data.targetStudents || [];

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

    const { id, data } = matchedSession;

    // Build the Focus Mode Jitsi link:
    // channelLastN=1: Receives only 1 incoming video (Teacher) to save bandwidth and device load
    // startWithAudioMuted=true: Starts with microphone muted
    // startWithVideoMuted=false: Starts with camera ON so teacher can see them
    const studentUrl = `https://meet.jit.si/${data.roomName}#config.channelLastN=1&config.startWithAudioMuted=true&config.startWithVideoMuted=false&userInfo.displayName=${encodeURIComponent(studentName)}`;

    return NextResponse.json({
      hasLiveClass: true,
      session: {
        id,
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
