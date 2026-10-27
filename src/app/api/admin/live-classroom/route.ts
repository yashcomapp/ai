import { NextResponse } from 'next/server';
import crypto from 'crypto';
import { adminDb } from '@/lib/firebase/admin';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

const SESSION_EXPIRY_MS = 100 * 60 * 1000; // 100 minutes (free public Jitsi sessions are limited to 95 minutes)

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
      const expiresMs = data.expiresAt?.toDate 
        ? data.expiresAt.toDate().getTime() 
        : (data.expiresAt ? new Date(data.expiresAt).getTime() : startMs + SESSION_EXPIRY_MS);

      if (now >= expiresMs) {
        expiredDocIds.push(doc.id);
      } else {
        validActiveDocs.push({ id: doc.id, data });
      }
    });

    // Reliably auto-expire obsolete sessions and await cleanup (no fire-and-forget)
    if (expiredDocIds.length > 0) {
      const expireBatch = new ChunkedBatch(adminDb);
      expiredDocIds.forEach(id => {
        expireBatch.update(adminDb.collection('liveClassrooms').doc(id), {
          status: 'ended',
          endedAt: new Date().toISOString(),
          endedReason: 'auto_expired'
        });
      });

      // Await finding and deleting all expired liveClassTargets using chunked in-query (max 30 per query)
      for (let i = 0; i < expiredDocIds.length; i += 30) {
        const chunk = expiredDocIds.slice(i, i + 30);
        const targetsSnap = await adminDb.collection('liveClassTargets')
          .where('sessionId', 'in', chunk)
          .get();
        targetsSnap.docs.forEach(doc => {
          expireBatch.delete(doc.ref);
        });
      }

      await expireBatch.commit();
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

      // Check existing live sessions that have overlapping batches or identical title
      const ongoingSnap = await adminDb.collection('liveClassrooms')
        .where('status', '==', 'live')
        .get();

      const startBatch = new ChunkedBatch(adminDb);

      // End overlapping sessions and delete their target documents atomically
      const replacedSessionIds: string[] = [];
      for (const doc of ongoingSnap.docs) {
        const d = doc.data();
        const hasBatchOverlap = (d.targetBatches || []).some((b: string) => targetBatches.includes(b));
        const isSameTitle = (d.title || '').trim().toLowerCase() === title.trim().toLowerCase();
        if (hasBatchOverlap || isSameTitle) {
          startBatch.update(doc.ref, {
            status: 'ended',
            endedAt: new Date().toISOString(),
            endedReason: 'replaced_by_new_session'
          });
          replacedSessionIds.push(doc.id);
        }
      }

      if (replacedSessionIds.length > 0) {
        for (let i = 0; i < replacedSessionIds.length; i += 30) {
          const chunk = replacedSessionIds.slice(i, i + 30);
          const oldTargets = await adminDb.collection('liveClassTargets')
            .where('sessionId', 'in', chunk)
            .get();
          oldTargets.docs.forEach(ot => startBatch.delete(ot.ref));
        }
      }

      const cleanTitle = sanitizeForRoom(title) || 'classroom';
      // Cryptographically secure random room name to prevent guessable public URLs
      const roomSecret = crypto.randomBytes(12).toString('hex');
      const roomName = `yc-${cleanTitle}-${roomSecret}`;
      // Cryptographically secure 6-digit numeric PIN
      const passcode = crypto.randomInt(100000, 1000000).toString();
      const teacherDisplayName = admin.userData?.name || 'Teacher (Yashcom)';
      const startedAt = new Date().toISOString();
      const expiresAtDate = new Date(Date.now() + SESSION_EXPIRY_MS);

      const newSessionData = {
        title: title.trim(),
        subject: (subject || '').trim(),
        targetType: targetType || 'batch',
        targetBatches,
        targetStudents,
        roomName,
        passcode,
        status: 'live',
        startedAt,
        expiresAt: expiresAtDate,
        endedAt: null,
        startedBy: teacherDisplayName
      };

      // Create new session document reference
      const newSessionRef = adminDb.collection('liveClassrooms').doc();
      startBatch.set(newSessionRef, newSessionData);

      // Create isolated target documents with native Timestamp expiresAt
      for (const bId of targetBatches) {
        const targetRef = adminDb.collection('liveClassTargets').doc(`batch_${bId}`);
        startBatch.set(targetRef, {
          sessionId: newSessionRef.id,
          targetType: 'batch',
          targetId: bId,
          title: newSessionData.title,
          subject: newSessionData.subject,
          roomName: newSessionData.roomName,
          passcode: newSessionData.passcode,
          startedAt: newSessionData.startedAt,
          expiresAt: expiresAtDate,
          startedBy: newSessionData.startedBy,
          status: 'live',
          updatedAt: new Date().toISOString()
        });
      }

      for (const sCode of targetStudents) {
        const targetRef = adminDb.collection('liveClassTargets').doc(`student_${sCode}`);
        startBatch.set(targetRef, {
          sessionId: newSessionRef.id,
          targetType: 'student',
          targetId: sCode,
          title: newSessionData.title,
          subject: newSessionData.subject,
          roomName: newSessionData.roomName,
          passcode: newSessionData.passcode,
          startedAt: newSessionData.startedAt,
          expiresAt: expiresAtDate,
          startedBy: newSessionData.startedBy,
          status: 'live',
          updatedAt: new Date().toISOString()
        });
      }

      // Single atomic commit: session and targets succeed or fail together
      await startBatch.commit();

      const teacherUrl = `https://meet.jit.si/${roomName}#config.channelLastN=-1&userInfo.displayName=${encodeURIComponent(teacherDisplayName)}`;

      return NextResponse.json({
        success: true,
        session: {
          id: newSessionRef.id,
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

      const endBatch = new ChunkedBatch(adminDb);
      endBatch.update(sessionRef, {
        status: 'ended',
        endedAt: new Date().toISOString(),
        endedBy: admin.userData?.name || admin.userData?.email || 'Teacher'
      });

      // Find and delete all corresponding liveClassTargets atomically
      const targetsSnap = await adminDb.collection('liveClassTargets')
        .where('sessionId', '==', sessionId)
        .get();

      targetsSnap.docs.forEach(doc => {
        endBatch.delete(doc.ref);
      });

      // Commit end and target deletion atomically
      await endBatch.commit();

      return NextResponse.json({ success: true, message: 'Live classroom ended successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (err: any) {
    console.error('Error in POST /api/admin/live-classroom:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
