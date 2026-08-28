import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const noticeId = searchParams.get('noticeId');
    if (!noticeId) {
      return NextResponse.json({ message: 'Missing noticeId' }, { status: 400 });
    }

    // 1. Fetch the notice details
    const noticeSnap = await adminDb.collection('notices').doc(noticeId).get();
    if (!noticeSnap.exists) {
      return NextResponse.json({ message: 'Notice not found' }, { status: 404 });
    }
    const noticeData = noticeSnap.data()!;
    const targetType = noticeData.targetType || 'all';
    const targetValues = noticeData.targetValues || [];

    // 2. Fetch all student profiles, parent profiles, batches, and seen logs
    const [studentsSnap, parentsSnap, batchesSnap, seenLogsSnap] = await Promise.all([
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('users').where('role', '==', 'parent').get(),
      adminDb.collection('batches').get(),
      adminDb.collection('noticeSeenLogs').where('noticeId', '==', noticeId).get()
    ]);

    // Map batches for name resolution
    const batchesMap = new Map<string, string>();
    batchesSnap.docs.forEach(doc => {
      batchesMap.set(doc.id, doc.data().name || 'Unknown Batch');
    });

    // Map parent emails to push status
    const parentsMapByEmail = new Map<string, boolean>();
    parentsSnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.email) {
        parentsMapByEmail.set(d.email.toLowerCase().trim(), Array.isArray(d.fcmTokens) && d.fcmTokens.length > 0);
      }
    });

    const getParentPushStatus = (email: string) => {
      return parentsMapByEmail.get(email.toLowerCase().trim()) || false;
    };

    // Parse seen logs
    const seenMap = new Map<string, Date>();
    seenLogsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.userCode && data.seenAt) {
        seenMap.set(data.userCode.toLowerCase(), data.seenAt.toDate ? data.seenAt.toDate() : new Date(data.seenAt));
      }
    });

    // 3. Resolve targeted students and parents
    const targetStudents: any[] = [];
    const targetParents: any[] = [];

    const studentsList = studentsSnap.docs.map(doc => {
      const d = doc.data();
      return {
        uid: doc.id,
        studentCode: d.studentCode || '',
        name: d.name || 'Student',
        email: d.email || '',
        parentEmail: d.parentEmail?.toLowerCase() || '',
        batchId: d.batchId || '',
        batchIds: d.batchIds || [],
        autonomous: d.autonomous || false,
        hasPushRegistered: Array.isArray(d.fcmTokens) && d.fcmTokens.length > 0,
        status: d.status || 'active'
      };
    }).filter(s => s.status !== 'inactive');

    const parentDetailsMap = new Map<string, { studentNames: string[], autonomous: boolean, studentCodes: string[] }>();
    parentsSnap.docs.forEach(doc => {
      const d = doc.data();
      const pEmail = d.email?.toLowerCase().trim();
      if (!pEmail) return;

      const pCodes = d.studentCodes || (d.studentCode ? [d.studentCode] : []);
      const matchedStuds = studentsList.filter(s => pCodes.includes(s.studentCode) || pCodes.includes(s.uid));
      
      if (matchedStuds.length > 0) {
        parentDetailsMap.set(pEmail, {
          studentNames: matchedStuds.map(s => s.name),
          autonomous: matchedStuds.some(s => s.autonomous),
          studentCodes: matchedStuds.map(s => s.studentCode)
        });
      }
    });

    const getParentDetails = (email: string) => {
      const clean = email.toLowerCase().trim();
      const details = parentDetailsMap.get(clean);
      if (details) {
        return {
          studentName: details.studentNames.join(', ') || 'Unknown Student',
          autonomous: details.autonomous,
          studentCodes: details.studentCodes
        };
      }
      return null;
    };

    if (targetType === 'all') {
      // Everyone is targeted
      studentsList.forEach(s => {
        targetStudents.push(s);
      });
      parentsSnap.docs.forEach(pDoc => {
        const pd = pDoc.data();
        const pEmail = pd.email?.toLowerCase().trim();
        if (pEmail) {
          const details = getParentDetails(pEmail);
          if (details) {
            targetParents.push({
              email: pEmail,
              studentName: details.studentName,
              autonomous: details.autonomous,
              studentCodes: details.studentCodes,
              hasPushRegistered: Array.isArray(pd.fcmTokens) && pd.fcmTokens.length > 0
            });
          }
        }
      });
    } else if (targetType === 'batch') {
      studentsList.forEach(s => {
        const matchesBatch = targetValues.includes(s.batchId) || s.batchIds.some((id: string) => targetValues.includes(id));
        if (matchesBatch) {
          targetStudents.push(s);
        }
      });
      parentsSnap.docs.forEach(pDoc => {
        const pd = pDoc.data();
        const pEmail = pd.email?.toLowerCase().trim();
        if (pEmail) {
          const details = getParentDetails(pEmail);
          if (details) {
            const hasChildInBatch = studentsList.some(s => 
              details.studentCodes.includes(s.studentCode) && 
              (targetValues.includes(s.batchId) || s.batchIds.some((id: string) => targetValues.includes(id)))
            );
            if (hasChildInBatch) {
              targetParents.push({
                email: pEmail,
                studentName: details.studentName,
                autonomous: details.autonomous,
                studentCodes: details.studentCodes,
                hasPushRegistered: Array.isArray(pd.fcmTokens) && pd.fcmTokens.length > 0
              });
            }
          }
        }
      });
    } else if (targetType === 'student') {
      studentsList.forEach(s => {
        if (targetValues.includes(s.studentCode)) {
          targetStudents.push(s);
        }
      });
      parentsSnap.docs.forEach(pDoc => {
        const pd = pDoc.data();
        const pEmail = pd.email?.toLowerCase().trim();
        if (pEmail) {
          const details = getParentDetails(pEmail);
          if (details) {
            const hasChildInTarget = details.studentCodes.some(code => targetValues.includes(code));
            if (hasChildInTarget) {
              targetParents.push({
                email: pEmail,
                studentName: details.studentName,
                autonomous: details.autonomous,
                studentCodes: details.studentCodes,
                hasPushRegistered: Array.isArray(pd.fcmTokens) && pd.fcmTokens.length > 0
              });
            }
          }
        }
      });
    } else if (targetType === 'parent') {
      targetValues.forEach((email: string) => {
        const lowerEmail = email.toLowerCase().trim();
        const details = getParentDetails(lowerEmail);
        if (details) {
          targetParents.push({
            email: lowerEmail,
            studentName: details.studentName,
            autonomous: details.autonomous,
            studentCodes: details.studentCodes,
            hasPushRegistered: getParentPushStatus(lowerEmail)
          });
        }
      });
    }

    // 4. Construct response log lists grouped by batch
    const studentGroups: Record<string, any[]> = {};
    const parentGroups: Record<string, any[]> = {};
    const unassignedName = 'Unassigned Students';
    
    targetStudents.forEach(s => {
      const studentBatches = Array.isArray(s.batchIds) ? s.batchIds.filter(Boolean) : [];
      if (studentBatches.length === 0) {
        if (!studentGroups[unassignedName]) {
          studentGroups[unassignedName] = [];
        }
        const seenTime = seenMap.get(s.studentCode.toLowerCase());
        studentGroups[unassignedName].push({
          studentCode: s.studentCode,
          name: s.name,
          seen: !!seenTime,
          seenAt: seenTime ? seenTime.toISOString() : null,
          autonomous: s.autonomous || false,
          hasPushRegistered: s.hasPushRegistered
        });
      } else {
        studentBatches.forEach((bId: string) => {
          if (targetType === 'batch' && !targetValues.includes(bId)) {
            return;
          }
          const bName = batchesMap.get(bId) || bId;
          if (!studentGroups[bName]) {
            studentGroups[bName] = [];
          }
          const seenTime = seenMap.get(s.studentCode.toLowerCase());
          if (!studentGroups[bName].some(st => st.studentCode === s.studentCode)) {
            studentGroups[bName].push({
              studentCode: s.studentCode,
              name: s.name,
              seen: !!seenTime,
              seenAt: seenTime ? seenTime.toISOString() : null,
              autonomous: s.autonomous || false,
              hasPushRegistered: s.hasPushRegistered
            });
          }
        });
      }
    });

    targetParents.forEach(p => {
      const childBatches = new Set<string>();
      (p.studentCodes || []).forEach((code: string) => {
        const stud = studentsList.find(s => s.studentCode === code || s.uid === code);
        if (stud) {
          const studentBatches = Array.isArray(stud.batchIds) ? stud.batchIds.filter(Boolean) : [];
          studentBatches.forEach((bId: string) => {
            if (targetType === 'batch' && !targetValues.includes(bId)) {
              return;
            }
            const bName = batchesMap.get(bId) || bId;
            childBatches.add(bName);
          });
        }
      });

      if (childBatches.size === 0) {
        if (!parentGroups[unassignedName]) {
          parentGroups[unassignedName] = [];
        }
        const seenTime = seenMap.get(p.email.toLowerCase());
        parentGroups[unassignedName].push({
          email: p.email,
          studentName: p.studentName,
          seen: !!seenTime,
          seenAt: seenTime ? seenTime.toISOString() : null,
          autonomous: p.autonomous || false,
          hasPushRegistered: p.hasPushRegistered
        });
      } else {
        Array.from(childBatches).forEach(bName => {
          if (!parentGroups[bName]) {
            parentGroups[bName] = [];
          }
          const seenTime = seenMap.get(p.email.toLowerCase());
          if (!parentGroups[bName].some(pr => pr.email === p.email)) {
            parentGroups[bName].push({
              email: p.email,
              studentName: p.studentName,
              seen: !!seenTime,
              seenAt: seenTime ? seenTime.toISOString() : null,
              autonomous: p.autonomous || false,
              hasPushRegistered: p.hasPushRegistered
            });
          }
        });
      }
    });

    const parentsLog = targetParents.map(p => {
      const seenTime = seenMap.get(p.email.toLowerCase());
      return {
        email: p.email,
        studentName: p.studentName,
        seen: !!seenTime,
        seenAt: seenTime ? seenTime.toISOString() : null,
        autonomous: p.autonomous || false,
        hasPushRegistered: p.hasPushRegistered
      };
    });

    // Sort students and parents in each group alphabetically by name
    Object.keys(studentGroups).forEach(groupName => {
      studentGroups[groupName].sort((a, b) => a.name.localeCompare(b.name));
    });
    Object.keys(parentGroups).forEach(groupName => {
      parentGroups[groupName].sort((a, b) => a.studentName.localeCompare(b.studentName));
    });

    return NextResponse.json({
      success: true,
      title: noticeData.title || 'Notice',
      targetType,
      studentGroups,
      parentGroups,
      parentsLog
    });
  } catch (error: any) {
    console.error('API GET admin notices logs error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
