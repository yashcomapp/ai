import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

function sanitizeForRoom(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 30);
}

export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    // Get active live session(s)
    const activeSnap = await adminDb.collection('liveClassrooms')
      .where('status', '==', 'live')
      .get();

    let activeSession = null;
    if (!activeSnap.empty) {
      const activeDocs = activeSnap.docs.sort((a, b) => {
        const aTime = new Date(a.data().startedAt || 0).getTime();
        const bTime = new Date(b.data().startedAt || 0).getTime();
        return bTime - aTime;
      });
      const doc = activeDocs[0];
      const data = doc.data();
      activeSession = {
        id: doc.id,
        ...data,
        teacherUrl: `https://meet.jit.si/${data.roomName}#config.channelLastN=-1&userInfo.displayName=${encodeURIComponent(admin.userData?.name || 'Teacher - Yashcom')}`
      };
    }

    // Get recent ended sessions (last 10)
    const recentSnap = await adminDb.collection('liveClassrooms')
      .orderBy('startedAt', 'desc')
      .limit(15)
      .get();

    const recentSessions = recentSnap.docs
      .filter(doc => doc.data().status === 'ended')
      .slice(0, 10)
      .map(doc => ({
        id: doc.id,
        ...doc.data()
      }));

    return NextResponse.json({ activeSession, recentSessions });
  } catch (err: any) {
    console.error('Error in GET /api/admin/live-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await request.json();
    const { action } = body;

    if (action === 'start') {
      const { title, subject, targetType, targetBatches = [], targetStudents = [] } = body;

      if (!title || !title.trim()) {
        return NextResponse.json({ error: 'Session title is required.' }, { status: 400 });
      }

      if (targetType === 'batch' && targetBatches.length === 0) {
        return NextResponse.json({ error: 'Please select at least one batch.' }, { status: 400 });
      }

      if (targetType === 'student' && targetStudents.length === 0) {
        return NextResponse.json({ error: 'Please select at least one student.' }, { status: 400 });
      }

      if (targetType === 'mixed' && targetBatches.length === 0 && targetStudents.length === 0) {
        return NextResponse.json({ error: 'Please select at least one batch or student.' }, { status: 400 });
      }

      // End any existing live sessions first to avoid orphaned active sessions
      const ongoingSnap = await adminDb.collection('liveClassrooms')
        .where('status', '==', 'live')
        .get();

      const batch = adminDb.batch();
      ongoingSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'ended',
          endedAt: new Date().toISOString()
        });
      });
      await batch.commit();

      const cleanTitle = sanitizeForRoom(title) || 'classroom';
      const randomSuffix = Math.random().toString(36).substring(2, 7);
      const roomName = `yashcom-${cleanTitle}-${randomSuffix}`;
      const teacherDisplayName = admin.userData?.name || admin.userData?.email || 'Teacher (Yashcom)';

      const newSessionData = {
        title: title.trim(),
        subject: (subject || '').trim(),
        targetType: targetType || 'batch',
        targetBatches,
        targetStudents,
        roomName,
        status: 'live',
        startedAt: new Date().toISOString(),
        endedAt: null,
        startedBy: teacherDisplayName
      };

      const docRef = await adminDb.collection('liveClassrooms').add(newSessionData);

      const teacherUrl = `https://meet.jit.si/${roomName}#config.channelLastN=-1&userInfo.displayName=${encodeURIComponent(teacherDisplayName)}`;

      return NextResponse.json({
        success: true,
        session: {
          id: docRef.id,
          ...newSessionData,
          teacherUrl
        }
      });
    }

    if (action === 'end') {
      const { sessionId } = body;
      if (!sessionId) {
        return NextResponse.json({ error: 'Session ID is required to end.' }, { status: 400 });
      }

      const sessionRef = adminDb.collection('liveClassrooms').doc(sessionId);
      await sessionRef.update({
        status: 'ended',
        endedAt: new Date().toISOString()
      });

      return NextResponse.json({ success: true, message: 'Live classroom ended successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (err: any) {
    console.error('Error in POST /api/admin/live-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
