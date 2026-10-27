import { NextResponse } from 'next/server';
import crypto from 'crypto';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

const SESSION_EXPIRY_MS = 100 * 60 * 1000; // 100 minutes (free public Jitsi sessions are limited to 95 minutes)

async function createLiveClassTargets(sessionId: string, sessionData: any) {
  try {
    const batch = adminDb.batch();
    const expiresAt = new Date(new Date(sessionData.startedAt).getTime() + SESSION_EXPIRY_MS).toISOString();
    
    const targetBatches: string[] = sessionData.targetBatches || [];
    const targetStudents: string[] = sessionData.targetStudents || [];
    
    for (const bId of targetBatches) {
      const ref = adminDb.collection('liveClassTargets').doc(`batch_${bId}`);
      batch.set(ref, {
        sessionId,
        targetType: 'batch',
        targetId: bId,
        title: sessionData.title,
        subject: sessionData.subject || '',
        roomName: sessionData.roomName,
        passcode: sessionData.passcode,
        startedAt: sessionData.startedAt,
        expiresAt,
        startedBy: sessionData.startedBy,
        status: 'live',
        updatedAt: new Date().toISOString()
      });
    }

    for (const sCode of targetStudents) {
      const ref = adminDb.collection('liveClassTargets').doc(`student_${sCode}`);
      batch.set(ref, {
        sessionId,
        targetType: 'student',
        targetId: sCode,
        title: sessionData.title,
        subject: sessionData.subject || '',
        roomName: sessionData.roomName,
        passcode: sessionData.passcode,
        startedAt: sessionData.startedAt,
        expiresAt,
        startedBy: sessionData.startedBy,
        status: 'live',
        updatedAt: new Date().toISOString()
      });
    }

    await batch.commit();
  } catch (err) {
    console.warn('Failed to write liveClassTargets:', err);
  }
}

async function removeLiveClassTargets(sessionIds: string[]) {
  if (!sessionIds.length) return;
  try {
    for (const sId of sessionIds) {
      const snap = await adminDb.collection('liveClassTargets').where('sessionId', '==', sId).get();
      if (!snap.empty) {
        const batch = adminDb.batch();
        snap.docs.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
      }
    }
  } catch (err) {
    console.warn('Failed to remove liveClassTargets:', err);
  }
}

async function syncActiveSessionsToConfig() {
  try {
    const liveSnap = await adminDb.collection('liveClassrooms')
      .where('status', '==', 'live')
      .get();

    const now = Date.now();
    const activeSessions = liveSnap.docs
      .map(doc => ({ id: doc.id, ...doc.data() }))
      .filter((s: any) => now - new Date(s.startedAt || 0).getTime() <= SESSION_EXPIRY_MS);

    await adminDb.collection('config').doc('liveClassrooms').set({
      activeSessions,
      updatedAt: new Date().toISOString()
    });
  } catch (err) {
    console.warn('Failed to sync active sessions to config/liveClassrooms:', err);
  }
}

function sanitizeForRoom(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 24);
}

export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const now = Date.now();

    // Get active live session(s)
    const activeSnap = await adminDb.collection('liveClassrooms')
      .where('status', '==', 'live')
      .get();

    const validActiveDocs: Array<{ id: string; data: any }> = [];
    const expiredDocIds: string[] = [];

    activeSnap.docs.forEach(doc => {
      const data = doc.data();
      const startMs = new Date(data.startedAt || 0).getTime();
      if (now - startMs > SESSION_EXPIRY_MS) {
        expiredDocIds.push(doc.id);
      } else {
        validActiveDocs.push({ id: doc.id, data });
      }
    });

    // Auto-expire obsolete sessions
    if (expiredDocIds.length > 0) {
      const batch = adminDb.batch();
      expiredDocIds.forEach(id => {
        batch.update(adminDb.collection('liveClassrooms').doc(id), {
          status: 'ended',
          endedAt: new Date().toISOString(),
          endedReason: 'auto_expired'
        });
      });
      batch.commit()
        .then(() => {
          syncActiveSessionsToConfig();
          removeLiveClassTargets(expiredDocIds);
        })
        .catch(e => console.warn('Failed to auto-expire sessions:', e));
    }

    // Sort active sessions (newest first)
    validActiveDocs.sort((a, b) => {
      const aTime = new Date(a.data.startedAt || 0).getTime();
      const bTime = new Date(b.data.startedAt || 0).getTime();
      return bTime - aTime;
    });

    let activeSession = null;
    if (validActiveDocs.length > 0) {
      const doc = validActiveDocs[0];
      const data = doc.data;
      const teacherName = admin.userData?.name || 'Teacher';
      activeSession = {
        id: doc.id,
        ...data,
        teacherUrl: `https://meet.jit.si/${data.roomName}#config.channelLastN=-1&userInfo.displayName=${encodeURIComponent(teacherName)}`
      };
    }

    // Get recent ended sessions (last 10) directly via composite index
    const recentSnap = await adminDb.collection('liveClassrooms')
      .where('status', '==', 'ended')
      .orderBy('startedAt', 'desc')
      .limit(10)
      .get();

    const recentSessions = recentSnap.docs.map(doc => ({
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

      // End only existing live sessions that have overlapping batches or identical title,
      // avoiding killing independent live classes for other batches platform-wide
      const ongoingSnap = await adminDb.collection('liveClassrooms')
        .where('status', '==', 'live')
        .get();

      const batch = adminDb.batch();
      let hadOverlap = false;
      const replacedSessionIds: string[] = [];

      ongoingSnap.docs.forEach(doc => {
        const d = doc.data();
        const hasBatchOverlap = (d.targetBatches || []).some((b: string) => targetBatches.includes(b));
        const isSameTitle = (d.title || '').trim().toLowerCase() === title.trim().toLowerCase();
        if (hasBatchOverlap || isSameTitle) {
          batch.update(doc.ref, {
            status: 'ended',
            endedAt: new Date().toISOString(),
            endedReason: 'replaced_by_new_session'
          });
          replacedSessionIds.push(doc.id);
          hadOverlap = true;
        }
      });
      if (hadOverlap) {
        await batch.commit();
        await removeLiveClassTargets(replacedSessionIds);
      }

      const cleanTitle = sanitizeForRoom(title) || 'classroom';
      // Cryptographically secure random room name to prevent guessable public URLs
      const roomSecret = crypto.randomBytes(12).toString('hex');
      const roomName = `yc-${cleanTitle}-${roomSecret}`;
      // Cryptographically secure 6-digit numeric PIN
      const passcode = crypto.randomInt(100000, 1000000).toString();
      const teacherDisplayName = admin.userData?.name || 'Teacher (Yashcom)';

      const newSessionData = {
        title: title.trim(),
        subject: (subject || '').trim(),
        targetType: targetType || 'batch',
        targetBatches,
        targetStudents,
        roomName,
        passcode,
        status: 'live',
        startedAt: new Date().toISOString(),
        endedAt: null,
        startedBy: teacherDisplayName
      };

      const docRef = await adminDb.collection('liveClassrooms').add(newSessionData);
      await Promise.all([
        createLiveClassTargets(docRef.id, newSessionData),
        syncActiveSessionsToConfig()
      ]);

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
      const sessionDoc = await sessionRef.get();

      if (!sessionDoc.exists) {
        return NextResponse.json({ error: 'Live classroom session not found.' }, { status: 404 });
      }

      const sessionData = sessionDoc.data()!;
      if (sessionData.status === 'ended') {
        return NextResponse.json({ success: true, message: 'Session is already ended.' });
      }

      await sessionRef.update({
        status: 'ended',
        endedAt: new Date().toISOString(),
        endedBy: admin.userData?.name || admin.userData?.email || 'Teacher'
      });
      await Promise.all([
        removeLiveClassTargets([sessionId]),
        syncActiveSessionsToConfig()
      ]);

      return NextResponse.json({ success: true, message: 'Live classroom ended successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (err: any) {
    console.error('Error in POST /api/admin/live-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
