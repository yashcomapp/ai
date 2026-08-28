import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyAnyRole } from '@/lib/auth';
import { sendPushNotification } from '@/lib/notifications';
import { chunkArray } from '@/lib/firestoreUtils';

export const dynamic = 'force-dynamic';

function getUserKey(authResult: { decodedToken: any; userData: any; role: string }): string {
  const { decodedToken, userData, role } = authResult;
  if (role === 'admin') return decodedToken?.uid || 'admin';
  if (role === 'student') return userData?.studentCode || '';
  if (role === 'parent') return `PR-${userData?.email?.toLowerCase().trim()}`;
  return '';
}

async function resolveFirebaseUidsForChatParticipants(participants: string[]): Promise<string[]> {
  try {
    const hasAdmin = participants.includes('admin');
    
    // Deduplicate parent emails
    const parentEmails = Array.from(new Set(
      participants
        .filter(p => p.startsWith('PR-'))
        .map(p => p.substring(3).toLowerCase().trim())
    ));

    // Deduplicate student codes
    const studentCodes = Array.from(new Set(
      participants
        .filter(p => p !== 'admin' && !p.startsWith('PR-'))
        .map(p => p.toUpperCase())
    ));

    let adminPromise = Promise.resolve([] as string[]);
    if (hasAdmin) {
      adminPromise = adminDb.collection('users')
        .where('role', '==', 'admin')
        .get()
        .then(snap => snap.docs.map(doc => doc.id))
        .catch(err => {
          console.error('Error resolving admin UIDs:', err);
          return [];
        });
    }

    const parentEmailChunks = chunkArray(parentEmails, 30);
    const parentPromises = parentEmailChunks.map(chunk => 
      adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('email', 'in', chunk)
        .get()
        .then(snap => snap.docs.map(doc => doc.id))
        .catch(err => {
          console.error(`Error resolving parent UIDs for chunk ${JSON.stringify(chunk)}:`, err);
          return [];
        })
    );

    const studentCodeChunks = chunkArray(studentCodes, 30);
    const studentPromises = studentCodeChunks.map(chunk => 
      adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', 'in', chunk)
        .get()
        .then(snap => snap.docs.map(doc => doc.id))
        .catch(err => {
          console.error(`Error resolving student UIDs for chunk ${JSON.stringify(chunk)}:`, err);
          return [];
        })
    );

    const allResults = await Promise.all([
      adminPromise,
      ...parentPromises,
      ...studentPromises
    ]);

    return Array.from(new Set(allResults.flat()));
  } catch (error) {
    console.error('Error resolving Firebase UIDs for chat participants:', error);
    return [];
  }
}

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const roomId = searchParams.get('roomId');

    if (!roomId) {
      return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
    }

    const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 403 });
    }

    const { userData, role } = authResult;

    // Load room doc to verify participant check
    const roomRef = adminDb.collection('chatRooms').doc(roomId);
    const roomSnap = await roomRef.get();
    if (!roomSnap.exists) {
      return NextResponse.json({ error: 'Chat room not found.' }, { status: 404 });
    }
    const roomData = roomSnap.data()!;

    if (role !== 'admin') {
      const userKey = role === 'parent' 
        ? `PR-${userData?.email?.toLowerCase().trim()}` 
        : (userData?.studentCode || '');
      
      const isParticipant = Array.isArray(roomData.participants) && roomData.participants.some((p: string) => 
        String(p).trim().toLowerCase() === String(userKey).trim().toLowerCase()
      );

      if (!isParticipant) {
        return NextResponse.json({ error: 'Forbidden. You are not a participant of this chat room.' }, { status: 403 });
      }
    }

    const messagesSnap = await roomRef
      .collection('messages')
      .orderBy('createdAt', 'desc')
      .limit(100)
      .get();

    const messages = messagesSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    })).reverse();

    // Resolve participant names
    const participantNames: Record<string, string> = {};
    const participants = roomData.participants || [];
    if (participants.length > 0) {
      const hasAdmin = participants.includes('admin');
      const parentEmails = participants
        .filter((p: string) => p.startsWith('PR-'))
        .map((p: string) => p.substring(3).toLowerCase().trim());
      const studentCodes = participants
        .filter((p: string) => p !== 'admin' && !p.startsWith('PR-'));

      const promises = [];
      if (hasAdmin) {
        promises.push(
          adminDb.collection('users')
            .where('role', '==', 'admin')
            .get()
            .then(snap => {
              snap.docs.forEach(doc => {
                const data = doc.data();
                participantNames[doc.id] = data.name || 'Admin';
                participantNames['admin'] = data.name || 'Admin';
              });
            })
            .catch(() => {})
        );
      }
      if (parentEmails.length > 0) {
        const parentChunks = chunkArray(parentEmails, 30);
        parentChunks.forEach(chunk => {
          promises.push(
            adminDb.collection('users')
              .where('role', '==', 'parent')
              .where('email', 'in', chunk)
              .get()
              .then(snap => {
                snap.docs.forEach(doc => {
                  const data = doc.data();
                  const pEmail = (data.email || '').toLowerCase().trim();
                  if (pEmail) {
                    participantNames[`PR-${pEmail}`] = data.name || 'Parent';
                  }
                });
              })
              .catch(() => {})
          );
        });
      }
      if (studentCodes.length > 0) {
        const studentChunks = chunkArray(studentCodes, 30);
        studentChunks.forEach(chunk => {
          promises.push(
            adminDb.collection('users')
              .where('role', '==', 'student')
              .where('studentCode', 'in', chunk)
              .get()
              .then(snap => {
                snap.docs.forEach(doc => {
                  const data = doc.data();
                  const sCode = data.studentCode;
                  if (sCode) {
                    participantNames[sCode] = data.name || 'Student';
                  }
                });
              })
              .catch(() => {})
          );
        });
      }
      await Promise.all(promises).catch(err => console.error('Error resolving names:', err));
    }

    return NextResponse.json({ success: true, messages, participantNames });
  } catch (error: any) {
    console.error('API GET chat messages error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { action, roomId, text, type, mediaUrl, mediaMetadata, replyToId, replyToText, replyToSenderName, pollOptions, messageId, optionIndex } = body;

    if (action === 'votePoll') {
      if (!roomId || !messageId || optionIndex === undefined) {
        return NextResponse.json({ error: 'Missing roomId, messageId, or optionIndex.' }, { status: 400 });
      }

      const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
      if (!authResult) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }
      const userKey = getUserKey(authResult);
      if (!userKey) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }

      const roomRef = adminDb.collection('chatRooms').doc(roomId);
      const messageRef = roomRef.collection('messages').doc(messageId);
      const messageSnap = await messageRef.get();
      if (!messageSnap.exists) {
        return NextResponse.json({ error: 'Message not found.' }, { status: 404 });
      }

      const messageData = messageSnap.data()!;
      if (messageData.type !== 'poll') {
        return NextResponse.json({ error: 'Message is not a poll.' }, { status: 400 });
      }

      const pollOptions = messageData.pollOptions || [];
      if (optionIndex < 0 || optionIndex >= pollOptions.length) {
        return NextResponse.json({ error: 'Invalid optionIndex.' }, { status: 400 });
      }

      const votes = messageData.pollVotes || {};
      votes[userKey] = optionIndex;

      const updatedOptions = pollOptions.map((opt: any, idx: number) => {
        const count = Object.values(votes).filter(v => v === idx).length;
        return {
          ...opt,
          votesCount: count
        };
      });

      await messageRef.update({
        pollVotes: votes,
        pollOptions: updatedOptions
      });

      return NextResponse.json({ success: true, pollOptions: updatedOptions });
    }

    if (action === 'pinMessage' || action === 'unpinMessage') {
      const authResult = await verifyAnyRole(req, ['admin']);
      if (!authResult) {
        return NextResponse.json({ message: 'Forbidden. Only administrators can pin messages.' }, { status: 403 });
      }

      if (!roomId) {
        return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
      }

      const roomRef = adminDb.collection('chatRooms').doc(roomId);
      const roomSnap = await roomRef.get();
      if (!roomSnap.exists) {
        return NextResponse.json({ error: 'Room not found.' }, { status: 404 });
      }

      if (action === 'unpinMessage') {
        await roomRef.update({
          pinnedMessage: null
        });
        return NextResponse.json({ success: true });
      }

      if (!messageId) {
        return NextResponse.json({ error: 'Missing messageId.' }, { status: 400 });
      }

      const messageSnap = await roomRef.collection('messages').doc(messageId).get();
      if (!messageSnap.exists) {
        return NextResponse.json({ error: 'Message not found.' }, { status: 404 });
      }

      const messageData = messageSnap.data()!;
      const pinnedMessagePayload = {
        messageId,
        text: messageData.text || '📊 Poll',
        senderName: messageData.senderName,
        timestamp: messageData.createdAt
      };

      await roomRef.update({
        pinnedMessage: pinnedMessagePayload
      });

      return NextResponse.json({ success: true, pinnedMessage: pinnedMessagePayload });
    }

    if (action === 'markRoomRead') {
      if (!roomId) {
        return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
      }

      const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
      if (!authResult) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }
      const { role } = authResult;
      const userKey = getUserKey(authResult);
      if (!userKey) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }

      const roomRef = adminDb.collection('chatRooms').doc(roomId);
      const roomSnap = await roomRef.get();
      if (!roomSnap.exists) {
        return NextResponse.json({ error: 'Chat room not found.' }, { status: 404 });
      }

      const roomData = roomSnap.data()!;
      if (role !== 'admin') {
        const isParticipant = Array.isArray(roomData.participants) && roomData.participants.some((p: string) => 
          String(p).trim().toLowerCase() === String(userKey).trim().toLowerCase()
        );
        if (!isParticipant) {
          return NextResponse.json({ error: 'Forbidden. You are not a participant of this chat room.' }, { status: 403 });
        }
      }

      const messagesSnap = await roomRef.collection('messages')
        .orderBy('createdAt', 'desc')
        .limit(100)
        .get();

      const timestamp = new Date().toISOString();
      const batch = adminDb.batch();
      let updatedCount = 0;

      messagesSnap.docs.forEach(doc => {
        const data = doc.data();
        const readBy = data.readBy || {};
        if (!readBy[userKey] && data.senderId !== userKey) {
          batch.update(
            doc.ref,
            new admin.firestore.FieldPath('readBy', userKey),
            timestamp
          );
          updatedCount++;
        }
      });

      if (updatedCount > 0) {
        await batch.commit();
      }

      return NextResponse.json({ success: true, updatedCount });
    }

    if (!roomId || (!text && type !== 'poll')) {
      return NextResponse.json({ error: 'Missing roomId or message content.' }, { status: 400 });
    }

    let senderId = '';
    let senderName = '';
    let senderRole = '';

    // 1. Authenticate role
    const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { userData, role } = authResult;

    const roomRef = adminDb.collection('chatRooms').doc(roomId);
    const roomSnap = await roomRef.get();
    if (!roomSnap.exists) {
      return NextResponse.json({ error: 'Chat room not found.' }, { status: 404 });
    }
    const roomData = roomSnap.data()!;

    // IDOR participant check
    if (role !== 'admin') {
      const userKey = role === 'parent' 
        ? `PR-${userData?.email?.toLowerCase().trim()}` 
        : (userData?.studentCode || '');
      
      const isParticipant = Array.isArray(roomData.participants) && roomData.participants.some((p: string) => 
        String(p).trim().toLowerCase() === String(userKey).trim().toLowerCase()
      );

      if (!isParticipant) {
        return NextResponse.json({ error: 'Forbidden. You are not a participant of this chat room.' }, { status: 403 });
      }
    }

    if (role === 'admin') {
      senderId = authResult.decodedToken?.uid || 'admin';
      senderName = userData?.name || 'Administrator';
      senderRole = 'admin';
    } else if (role === 'student') {
      // Validate student mute controls
      if (roomData.isMutedForStudents) {
        return NextResponse.json({ error: 'Sending messages in this group is restricted to admins only.' }, { status: 403 });
      }
      senderId = userData?.studentCode || '';
      senderName = userData?.name || 'Student';
      senderRole = 'student';
    } else if (role === 'parent') {
      // Validate parent mute controls
      if (roomData.isMutedForParents) {
        return NextResponse.json({ error: 'Sending messages in this group is restricted to admins only.' }, { status: 403 });
      }
      senderId = `PR-${userData?.email?.toLowerCase().trim()}`;
      senderName = userData?.name || 'Parent';
      senderRole = 'parent';
    } else {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const messageIdRef = roomRef.collection('messages').doc();
    const newMessageId = messageIdRef.id;

    const timestamp = new Date().toISOString();
    const messagePayload = {
      messageId: newMessageId,
      senderId,
      senderName,
      senderRole,
      text: text || (type === 'poll' ? '📊 Poll' : ''),
      type: type || 'text',
      mediaUrl: mediaUrl || null,
      mediaMetadata: mediaMetadata || null,
      replyToId: replyToId || null,
      replyToText: replyToText || null,
      replyToSenderName: replyToSenderName || null,
      pollOptions: type === 'poll' && Array.isArray(pollOptions)
        ? pollOptions.map((opt: string) => ({ text: opt, votesCount: 0 }))
        : null,
      pollVotes: type === 'poll' ? {} : null,
      createdAt: timestamp,
      isEdited: false,
      isDeleted: false,
      readBy: {
        [senderId]: timestamp
      }
    };

    // 2. Increment unread count for other participants
    const unreadCounts = { ...roomData.unreadCounts };
    (roomData.participants || []).forEach((p: string) => {
      if (p !== senderId) {
        unreadCounts[p] = (unreadCounts[p] || 0) + 1;
      }
    });

    const batch = adminDb.batch();
    batch.set(messageIdRef, messagePayload);
    batch.update(roomRef, {
      unreadCounts,
      lastMessage: {
        text: (text || (type === 'poll' ? '📊 Poll' : '')).substring(0, 100),
        senderName,
        timestamp
      }
    });

    await batch.commit();

    // Send push notification to other participants of the chat room
    try {
      const otherParticipants = (roomData.participants || []).filter((p: string) => p !== senderId);
      if (otherParticipants.length > 0) {
        const targetUids = await resolveFirebaseUidsForChatParticipants(otherParticipants);
        if (targetUids.length > 0) {
          const notifTitle = roomData.type === 'group'
            ? `${senderName} in ${roomData.name}`
            : senderName;
          await sendPushNotification(targetUids, notifTitle, text, {
            type: 'chat_message',
            roomId,
            senderId,
            senderRole
          });
        }
      }
    } catch (notifError) {
      console.error('Error sending chat push notification:', notifError);
    }

    return NextResponse.json({ success: true, message: messagePayload });
  } catch (error: any) {
    console.error('API POST chat messages error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function PATCH(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const roomId = searchParams.get('roomId');
    const messageId = searchParams.get('messageId');

    if (!roomId || !messageId) {
      return NextResponse.json({ error: 'Missing roomId or messageId.' }, { status: 400 });
    }

    const body = await req.json();
    const { text, action, reactionType } = body;

    // Authenticate sender
    const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { role } = authResult;
    const admin = role === 'admin' ? authResult : null;
    const userKey = getUserKey(authResult);

    if (!userKey) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const roomRef = adminDb.collection('chatRooms').doc(roomId);
    const roomSnap = await roomRef.get();
    if (!roomSnap.exists) {
      return NextResponse.json({ error: 'Chat room not found.' }, { status: 404 });
    }
    const roomData = roomSnap.data()!;

    // Check room participant permissions
    if (role !== 'admin') {
      const isParticipant = Array.isArray(roomData.participants) && roomData.participants.some((p: string) => 
        String(p).trim().toLowerCase() === String(userKey).trim().toLowerCase()
      );
      if (!isParticipant) {
        return NextResponse.json({ error: 'Forbidden. You are not a participant of this chat room.' }, { status: 403 });
      }
    }

    const msgRef = roomRef.collection('messages').doc(messageId);
    const msgSnap = await msgRef.get();
    if (!msgSnap.exists) {
      return NextResponse.json({ error: 'Message not found.' }, { status: 404 });
    }
    const msgData = msgSnap.data()!;

    // Handle Quick Reply Reaction
    if (action === 'react') {
      if (!reactionType || !['thumbsup', 'pray'].includes(reactionType)) {
        return NextResponse.json({ error: 'Invalid reaction type.' }, { status: 400 });
      }

      const reactions = msgData.reactions || {};
      let thumbsupList = Array.isArray(reactions.thumbsup) ? reactions.thumbsup : [];
      let prayList = Array.isArray(reactions.pray) ? reactions.pray : [];

      if (reactionType === 'thumbsup') {
        if (thumbsupList.includes(userKey)) {
          thumbsupList = thumbsupList.filter((u: string) => u !== userKey);
        } else {
          thumbsupList.push(userKey);
          prayList = prayList.filter((u: string) => u !== userKey);
        }
      } else if (reactionType === 'pray') {
        if (prayList.includes(userKey)) {
          prayList = prayList.filter((u: string) => u !== userKey);
        } else {
          prayList.push(userKey);
          thumbsupList = thumbsupList.filter((u: string) => u !== userKey);
        }
      }

      await msgRef.update({
        'reactions.thumbsup': thumbsupList,
        'reactions.pray': prayList
      });

      return NextResponse.json({ success: true, message: 'Reaction toggled successfully.' });
    }

    // Normal Text Edit
    if (!text) {
      return NextResponse.json({ error: 'Missing text.' }, { status: 400 });
    }

    // Enforce owner check (Admin can edit any message, others only their own)
    if (!admin && msgData.senderId !== userKey) {
      return NextResponse.json({ message: 'Forbidden. You do not own this message.' }, { status: 403 });
    }
    // Enforce 1-hour edit window for student and parent
    if (!admin) {
      const sentTime = new Date(msgData.createdAt || msgData.timestamp || 0).getTime();
      const now = Date.now();
      const diffMs = now - sentTime;
      const oneHourMs = 60 * 60 * 1000;
      if (diffMs > oneHourMs) {
        return NextResponse.json({ error: 'Editing is only allowed within 1 hour of sending.' }, { status: 400 });
      }
    }

    await msgRef.update({
      text,
      isEdited: true,
      updatedAt: new Date().toISOString()
    });

    return NextResponse.json({ success: true, message: 'Message edited successfully.' });
  } catch (error: any) {
    console.error('API PATCH chat messages error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const roomId = searchParams.get('roomId');
    const messageId = searchParams.get('messageId');

    if (!roomId || !messageId) {
      return NextResponse.json({ error: 'Missing roomId or messageId.' }, { status: 400 });
    }

    const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { role } = authResult;
    const admin = role === 'admin' ? authResult : null;
    const userKey = getUserKey(authResult);

    if (!userKey) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const msgRef = adminDb.collection('chatRooms')
      .doc(roomId)
      .collection('messages')
      .doc(messageId);

    const msgSnap = await msgRef.get();
    if (!msgSnap.exists) {
      return NextResponse.json({ error: 'Message not found.' }, { status: 404 });
    }

    const msgData = msgSnap.data()!;
    // Admin can delete any message, others only their own
    if (!admin && msgData.senderId !== userKey) {
      return NextResponse.json({ message: 'Forbidden. You do not own this message.' }, { status: 403 });
    }

    // Soft delete: keep the record but mark as deleted
    await msgRef.update({
      isDeleted: true,
      text: '🚫 This message was deleted',
      mediaUrl: null,
      mediaMetadata: null,
      deletedAt: new Date().toISOString()
    });

    return NextResponse.json({ success: true, message: 'Message soft-deleted.' });
  } catch (error: any) {
    console.error('API DELETE chat messages error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
