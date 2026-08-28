import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole, verifyAnyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    
    const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 403 });
    }

    const { userData, role } = authResult;
    const admin = role === 'admin' ? authResult : null;
    const student = role === 'student' ? authResult : null;
    const parent = role === 'parent' ? authResult : null;

    // Helper to get all inactive studentCodes and emails
    const inactiveUsersSnap = await adminDb.collection('users').where('status', '==', 'inactive').get();
    const inactiveCodes = new Set<string>();
    const inactiveEmails = new Set<string>();
    inactiveUsersSnap.docs.forEach(d => {
      const data = d.data();
      if (data.studentCode) inactiveCodes.add(data.studentCode.trim().toUpperCase());
      if (data.email) inactiveEmails.add(data.email.toLowerCase().trim());
      if (data.parentEmail) inactiveEmails.add(data.parentEmail.toLowerCase().trim());
    });

    if (admin) {
      // Admin gets active chat rooms
      const roomsSnap = await adminDb.collection('chatRooms').limit(300).get();
      let rooms = roomsSnap.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      })) as any[];

      // Filter out inactive participants and empty DMs for admin
      rooms = rooms.filter(room => {
        const parts: string[] = room.participants || [];
        const hasInactive = parts.some(p => {
          const upper = p.toUpperCase();
          if (inactiveCodes.has(upper)) return true;
          if (p.startsWith('PR-')) {
            const email = p.replace('PR-', '').toLowerCase().trim();
            if (inactiveEmails.has(email)) return true;
          }
          return false;
        });
        if (hasInactive) return false;

        // For DM rooms: ONLY include existent communications (rooms with a lastMessage and message text)
        if (room.type === 'dm') {
          if (!room.lastMessage || !room.lastMessage.text) return false;
        }
        return true;
      });

      // Sort with latest communication on top
      rooms.sort((a, b) => {
        const timeA = a.lastMessage?.timestamp ? new Date(a.lastMessage.timestamp).getTime() : (a.createdAt ? new Date(a.createdAt).getTime() : 0);
        const timeB = b.lastMessage?.timestamp ? new Date(b.lastMessage.timestamp).getTime() : (b.createdAt ? new Date(b.createdAt).getTime() : 0);
        return timeB - timeA;
      });

      return NextResponse.json({ success: true, rooms });
    }

    if (student) {
      if (student.userData?.status === 'inactive') {
        return NextResponse.json({ message: 'Access Denied: Inactive account' }, { status: 403 });
      }

      const sCode = student.userData?.studentCode || '';
      const sName = student.userData?.name || 'Student';
      const sBatches = student.userData?.batchIds || (student.userData?.batchId ? [student.userData?.batchId] : []);
      const pEmail = student.userData?.parentEmail || '';

      if (sCode) {
        const sCodeUpper = sCode.trim().toUpperCase();

        // 1. Gather group and DM room document references
        const dmRoomId = `room_${sCodeUpper}_teacher`;
        const groupRoomIds = sBatches.map((bId: string) => `room_batch_${bId}`);
        const roomIds = [dmRoomId, ...groupRoomIds];
        
        const roomRefs = roomIds.map((id: string) => adminDb.collection('chatRooms').doc(id));
        const roomSnaps = await adminDb.getAll(...roomRefs).catch(() => []);
        
        const existingRoomIds = roomSnaps.filter(s => s.exists).map(s => s.id);
        const batchPromises: Promise<any>[] = [];

        // 2. DM Room Creation only if it doesn't exist
        if (!existingRoomIds.includes(dmRoomId)) {
          batchPromises.push(adminDb.collection('chatRooms').doc(dmRoomId).set({
            roomId: dmRoomId,
            type: 'dm',
            name: `${sName} (Student)`,
            participants: [sCodeUpper, 'admin'],
            unreadCounts: {
              [sCodeUpper]: 0,
              'admin': 0
            },
            createdAt: new Date().toISOString()
          }));
        }

        // 3. Batch Group Rooms initialization/sync
        for (const gRoomId of groupRoomIds) {
          const batchId = gRoomId.replace('room_batch_', '');
          const snap = roomSnaps.find(s => s.id === gRoomId);
          
          if (!snap || !snap.exists) {
            batchPromises.push(adminDb.collection('chatRooms').doc(gRoomId).set({
              roomId: gRoomId,
              type: 'group',
              name: `Class Batch ${batchId}`,
              participants: [sCodeUpper, 'admin'],
              unreadCounts: {
                [sCodeUpper]: 0,
                'admin': 0
              },
              createdAt: new Date().toISOString()
            }));
          } else {
            const gData = snap.data();
            if (gData) {
              const currentParts = gData.participants || [];
              const unreads = gData.unreadCounts || {};
              let updated = false;
              if (!currentParts.includes(sCodeUpper)) {
                currentParts.push(sCodeUpper);
                unreads[sCodeUpper] = 0;
                updated = true;
              }
              if (updated) {
                batchPromises.push(adminDb.collection('chatRooms').doc(gRoomId).update({
                  participants: currentParts,
                  unreadCounts: unreads
                }));
              }
            }
          }
        }

        // 4. Handle parent auto-reconciliation
        if (pEmail && !inactiveEmails.has(pEmail.toLowerCase().trim())) {
          const pKey = `PR-${pEmail.toLowerCase().trim()}`;
          const parentSnap = await adminDb.collection('users')
            .where('role', '==', 'parent')
            .where('email', '==', pEmail.toLowerCase().trim())
            .limit(1)
            .get();

          if (!parentSnap.empty && parentSnap.docs[0].data().status !== 'inactive') {
            for (const gRoomId of groupRoomIds) {
              const snap = roomSnaps.find(s => s.id === gRoomId);
              if (snap && snap.exists) {
                const gData = snap.data();
                if (gData) {
                  const currentParts = gData.participants || [];
                  const unreads = gData.unreadCounts || {};
                  let updated = false;
                  if (!currentParts.includes(pKey)) {
                    currentParts.push(pKey);
                    unreads[pKey] = 0;
                    updated = true;
                  }
                  if (updated) {
                    batchPromises.push(adminDb.collection('chatRooms').doc(gRoomId).update({
                      participants: currentParts,
                      unreadCounts: unreads
                    }));
                  }
                }
              }
            }
          }
        }

        if (batchPromises.length > 0) {
          await Promise.all(batchPromises);
        }
      }

      // Query rooms where student is a participant
      const roomsQuery = await adminDb.collection('chatRooms')
        .where('participants', 'array-contains', sCode.trim().toUpperCase())
        .get();
      
      let rooms = roomsQuery.docs.map(doc => ({ id: doc.id, ...doc.data() })) as any[];
      rooms.sort((a, b) => {
        const timeA = a.lastMessage?.timestamp ? new Date(a.lastMessage.timestamp).getTime() : (a.createdAt ? new Date(a.createdAt).getTime() : 0);
        const timeB = b.lastMessage?.timestamp ? new Date(b.lastMessage.timestamp).getTime() : (b.createdAt ? new Date(b.createdAt).getTime() : 0);
        return timeB - timeA;
      });

      return NextResponse.json({ success: true, rooms });
    }

    // Try parent authentication
    if (parent) {
      if (parent.userData?.status === 'inactive') {
        return NextResponse.json({ message: 'Access Denied: Inactive account' }, { status: 403 });
      }

      const pEmail = parent.userData?.email?.toLowerCase().trim() || '';
      const pKey = `PR-${pEmail}`;
      const pCodes = parent.userData?.studentCodes || (parent.userData?.studentCode ? [parent.userData?.studentCode] : []);

      if (pKey && pCodes.length > 0) {
        const uCodes = pCodes.map((sc: string) => sc.trim().toUpperCase()).filter((c: string) => !inactiveCodes.has(c));
        if (uCodes.length === 0) {
          return NextResponse.json({ success: true, rooms: [] });
        }

        // 1. Fetch all student profiles at once in a single query
        const studentQuery = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('studentCode', 'in', uCodes)
          .get();

        const studentDocs = studentQuery.docs;
        const dmRoomIds: string[] = [];
        const groupRoomIds: string[] = [];
        
        const studentBatchesMap: Record<string, string[]> = {};
        const studentNamesMap: Record<string, string> = {};

        for (const doc of studentDocs) {
          const sd = doc.data();
          const scUpper = sd.studentCode.trim().toUpperCase();
          const sName = sd.name || 'Student';
          const sB = sd.batchIds || (sd.batchId ? [sd.batchId] : []);
          
          studentBatchesMap[scUpper] = sB;
          studentNamesMap[scUpper] = sName;
          
          dmRoomIds.push(`room_${scUpper}_teacher`);
          sB.forEach((bId: string) => {
            groupRoomIds.push(`room_batch_${bId}`);
          });
        }

        const uniqueRoomIds = Array.from(new Set([...dmRoomIds, ...groupRoomIds]));
        
        // 2. Fetch all rooms in a single getAll call
        const roomRefs = uniqueRoomIds.map((id: string) => adminDb.collection('chatRooms').doc(id));
        const roomSnaps = roomRefs.length > 0 ? await adminDb.getAll(...roomRefs).catch(() => []) : [];
        const roomsMap = new Map(roomSnaps.map((snap: any) => [snap.id, snap]));

        const batchPromises: Promise<any>[] = [];
        const missingBatchIds: string[] = [];

        // Check which batch group rooms are missing
        for (const [scUpper, sB] of Object.entries(studentBatchesMap)) {
          for (const bId of sB) {
            const gRoomId = `room_batch_${bId}`;
            const gSnap = roomsMap.get(gRoomId);
            if (!gSnap || !gSnap.exists) {
              missingBatchIds.push(bId);
            }
          }
        }

        // Fetch missing batches
        let batchNamesMap = new Map<string, string>();
        if (missingBatchIds.length > 0) {
          const uniqueMissingBatches = Array.from(new Set(missingBatchIds));
          const batchRefs = uniqueMissingBatches.map((bId: string) => adminDb.collection('batches').doc(bId));
          const batchSnaps = await adminDb.getAll(...batchRefs).catch(() => []);
          batchNamesMap = new Map(batchSnaps.map((snap: any) => [
            snap.id,
            snap.exists ? snap.data()?.name : 'Class Group'
          ]));
        }

        // Reconcile rooms
        for (const doc of studentDocs) {
          const sd = doc.data();
          const scUpper = sd.studentCode.trim().toUpperCase();
          const sName = sd.name || 'Student';
          const sB = sd.batchIds || (sd.batchId ? [sd.batchId] : []);

          // Reconcile DM
          const dmRoomId = `room_${scUpper}_teacher`;
          const dmSnap = roomsMap.get(dmRoomId);
          if (!dmSnap || !dmSnap.exists) {
            const participants = [scUpper, 'admin', pKey];
            const unreadCounts: Record<string, number> = {
              [scUpper]: 0,
              'admin': 0,
              [pKey]: 0
            };
            batchPromises.push(adminDb.collection('chatRooms').doc(dmRoomId).set({
              roomId: dmRoomId,
              type: 'dm',
              name: `${sName} (Direct Message)`,
              participants,
              unreadCounts,
              lastMessage: {
                text: 'Private direct message channel established with Teacher.',
                senderName: 'System',
                timestamp: new Date().toISOString()
              },
              createdAt: new Date().toISOString()
            }));
          } else {
            const dmData = dmSnap.data()!;
            const currentParts = dmData.participants || [];
            const unreads = dmData.unreadCounts || {};
            let updated = false;
            if (!currentParts.includes(pKey)) {
              currentParts.push(pKey);
              unreads[pKey] = 0;
              updated = true;
            }
            if (updated) {
              batchPromises.push(adminDb.collection('chatRooms').doc(dmRoomId).update({
                participants: currentParts,
                unreadCounts: unreads
              }));
            }
          }

          // Reconcile class groups
          for (const bId of sB) {
            const gRoomId = `room_batch_${bId}`;
            const gSnap = roomsMap.get(gRoomId);
            if (!gSnap || !gSnap.exists) {
              const batchName = batchNamesMap.get(bId) || 'Class Group';
              batchPromises.push(adminDb.collection('chatRooms').doc(gRoomId).set({
                roomId: gRoomId,
                type: 'group',
                name: batchName,
                participants: [scUpper, 'admin', pKey],
                unreadCounts: {
                  [scUpper]: 0,
                  'admin': 0,
                  [pKey]: 0
                },
                isMutedForStudents: false,
                isMutedForParents: false,
                lastMessage: {
                  text: 'Welcome to the class group chat!',
                  senderName: 'System',
                  timestamp: new Date().toISOString()
                },
                createdAt: new Date().toISOString()
              }));
            } else {
              const gData = gSnap.data()!;
              const currentParts = gData.participants || [];
              const unreads = gData.unreadCounts || {};
              let updated = false;
              if (!currentParts.includes(pKey)) {
                currentParts.push(pKey);
                unreads[pKey] = 0;
                updated = true;
              }
              if (updated) {
                batchPromises.push(adminDb.collection('chatRooms').doc(gRoomId).update({
                  participants: currentParts,
                  unreadCounts: unreads
                }));
              }
            }
          }
        }

        if (batchPromises.length > 0) {
          await Promise.all(batchPromises);
        }
      }

      // Query only rooms where parent is a participant - NO FULL SCAN!
      const roomsQuery = await adminDb.collection('chatRooms')
        .where('participants', 'array-contains', pKey)
        .get();
      
      const rooms = roomsQuery.docs.map((doc: any) => ({ id: doc.id, ...doc.data() }));
      return NextResponse.json({ success: true, rooms });
    }

    return NextResponse.json({ message: 'Unauthorized.' }, { status: 403 });
  } catch (error: any) {
    console.error('API GET chat rooms error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { action, roomId } = body;

    if (action === 'resetUnread') {
      if (!roomId) {
        return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
      }
      
      const authResult = await verifyAnyRole(req, ['admin', 'student', 'parent']);
      if (!authResult) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }

      const { userData, role } = authResult;
      let userKey = '';
      if (role === 'admin') {
        userKey = authResult.decodedToken?.uid || 'admin';
      } else if (role === 'student') {
        userKey = userData?.studentCode || '';
      } else if (role === 'parent') {
        userKey = `PR-${userData?.email?.toLowerCase().trim()}`;
      }

      if (!userKey) {
        return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
      }

      // Reset specific unread counter map element
      const roomRef = adminDb.collection('chatRooms').doc(roomId);
      const roomSnap = await roomRef.get();

      if (roomSnap.exists) {
        const roomData = roomSnap.data()!;
        if (role !== 'admin') {
          const isParticipant = Array.isArray(roomData.participants) && roomData.participants.some((p: string) => 
            String(p).trim().toLowerCase() === String(userKey).trim().toLowerCase()
          );

          if (!isParticipant) {
            return NextResponse.json({ error: 'Forbidden. You are not a participant of this chat room.' }, { status: 403 });
          }
        }

        const unreadCounts = roomData.unreadCounts || {};
        if (unreadCounts[userKey] !== 0) {
          unreadCounts[userKey] = 0;
          await roomRef.update({ unreadCounts });
        }
      }

      return NextResponse.json({ success: true, message: 'Unread count reset successfully.' });
    }

    // Admin Group creation
    if (action === 'createGroup') {
      const admin = await verifyRole(req, 'admin');
      if (!admin) {
        return NextResponse.json({ message: 'Unauthorized. Admin required to create groups.' }, { status: 403 });
      }
      
      const { batchId, name } = body;
      if (!batchId || !name) {
        return NextResponse.json({ error: 'Missing batchId or name.' }, { status: 400 });
      }

      const gRoomId = `room_batch_${batchId}`;
      const roomRef = adminDb.collection('chatRooms').doc(gRoomId);
      const roomSnap = await roomRef.get();

      if (roomSnap.exists) {
        return NextResponse.json({ success: true, roomId: gRoomId, message: 'Group room already exists.' });
      }

      // Fetch all students in batch to pre-set unread counts
      const studentsSnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .get();

      const participants = [admin.decodedToken?.uid || 'admin'];
      const unreadCounts: Record<string, number> = {
        [admin.decodedToken?.uid || 'admin']: 0
      };

      studentsSnap.docs.forEach(doc => {
        const d = doc.data();
        const sc = d.studentCode;
        const sB = d.batchIds || (d.batchId ? [d.batchId] : []);
        
        if (sc && sB.includes(batchId)) {
          participants.push(sc);
          unreadCounts[sc] = 0;
          
          if (d.parentEmail) {
            const pKey = `PR-${d.parentEmail.toLowerCase().trim()}`;
            participants.push(pKey);
            unreadCounts[pKey] = 0;
          }
        }
      });

      const newGroup = {
        roomId: gRoomId,
        type: 'group',
        name,
        participants,
        unreadCounts,
        isMutedForStudents: false,
        isMutedForParents: false,
        lastMessage: {
          text: 'Welcome to the class group chat!',
          senderName: 'System',
          timestamp: new Date().toISOString()
        },
        createdAt: new Date().toISOString()
      };

      await roomRef.set(newGroup);
      return NextResponse.json({ success: true, roomId: gRoomId, room: newGroup });
    }

    // Admin Group mute management
    if (action === 'updateMute') {
      if (!roomId) {
        return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
      }
      const admin = await verifyRole(req, 'admin');
      if (!admin) {
        return NextResponse.json({ message: 'Unauthorized. Admin required to toggle group mutes.' }, { status: 403 });
      }

      const { isMutedForStudents, isMutedForParents } = body;
      const roomRef = adminDb.collection('chatRooms').doc(roomId);
      await roomRef.update({
        isMutedForStudents: !!isMutedForStudents,
        isMutedForParents: !!isMutedForParents,
        updatedAt: new Date().toISOString()
      });

      return NextResponse.json({ success: true, message: 'Group mute settings updated.' });
    }

    // Initialize DM Room (for admin to start chat with student/parent)
    if (action === 'createDM') {
      const admin = await verifyRole(req, 'admin');
      if (!admin) {
        return NextResponse.json({ message: 'Unauthorized. Admin required to initialize DMs.' }, { status: 403 });
      }

      const { targetUserCode, targetUserName } = body; // e.g. studentCode or PR-email
      if (!targetUserCode || !targetUserName) {
        return NextResponse.json({ error: 'Missing targetUserCode or targetUserName.' }, { status: 400 });
      }

      const adminUid = admin.decodedToken?.uid || 'admin';
      const cleanCode = targetUserCode.trim();
      const dmRoomId = `room_${cleanCode}_${adminUid}`;

      const roomRef = adminDb.collection('chatRooms').doc(dmRoomId);
      const roomSnap = await roomRef.get();

      if (roomSnap.exists) {
        return NextResponse.json({ success: true, roomId: dmRoomId, room: roomSnap.data() });
      }

      const newDm = {
        roomId: dmRoomId,
        type: 'dm',
        name: `${targetUserName} (Direct Message)`,
        participants: [adminUid, cleanCode],
        unreadCounts: {
          [adminUid]: 0,
          [cleanCode]: 0
        },
        lastMessage: {
          text: 'Private direct message channel established.',
          senderName: 'System',
          timestamp: new Date().toISOString()
        },
        createdAt: new Date().toISOString()
      };

      await roomRef.set(newDm);
      return NextResponse.json({ success: true, roomId: dmRoomId, room: newDm });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST chat rooms error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const roomId = searchParams.get('roomId');

    if (!roomId) {
      return NextResponse.json({ error: 'Missing roomId.' }, { status: 400 });
    }

    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin required to delete chat rooms.' }, { status: 403 });
    }

    const roomRef = adminDb.collection('chatRooms').doc(roomId);
    
    // 1. Delete all messages inside the subcollection in chunks of 450 to stay within Firestore batch limits
    const messagesSnap = await roomRef.collection('messages').get();
    const messageIds = messagesSnap.docs.map(doc => doc.id);
    const chunks: string[][] = [];
    for (let i = 0; i < messageIds.length; i += 450) {
      chunks.push(messageIds.slice(i, i + 450));
    }

    for (const chunk of chunks) {
      const batch = adminDb.batch();
      chunk.forEach(msgId => {
        batch.delete(roomRef.collection('messages').doc(msgId));
      });
      await batch.commit();
    }

    // 2. Delete the chat room document itself
    await roomRef.delete();

    return NextResponse.json({ success: true, message: 'Chat room and all messages deleted successfully.' });
  } catch (error: any) {
    console.error('API DELETE chat room error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
