import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { StudentRepository } from '@/repositories/student.repository';
import { ReportCacheManager } from '@/lib/reportCache';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    // 1. Fetch batches, students, parents, and session logs in parallel
    const url = new URL(req.url);
    const dateParam = url.searchParams.get('date'); // e.g. "2026-07-24"

    const cacheKey = `login-register-report-${dateParam || 'today'}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }
    
    let startDate = new Date();
    if (dateParam) {
      const parts = dateParam.split('-');
      if (parts.length === 3) {
        // parse as local date to avoid timezone shifts
        startDate = new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
      }
    }
    startDate.setHours(0, 0, 0, 0);

    const endDate = new Date(startDate);
    endDate.setDate(startDate.getDate() + 1);

    const [batchesSnap, students, parents, logsSnap] = await Promise.all([
      adminDb.collection('batches').get(),
      StudentRepository.listStudents(),
      StudentRepository.listParents(),
      adminDb.collection('session_logs')
        .where('timestamp', '>=', startDate)
        .where('timestamp', '<', endDate)
        .orderBy('timestamp', 'desc')
        .get()
    ]);

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    // 2. Group by batches
    const groupedMap = new Map<string, any[]>();
    batches.forEach(b => groupedMap.set(b.id, []));
    
    // Catch-all for unassigned students/parents
    const unassignedMembers: any[] = [];

    students.forEach(s => {
      const memberObj = {
        id: s.id,
        name: s.name,
        email: s.email,
        role: s.role,
        studentCode: s.studentCode,
        lastActiveAt: s.lastActiveAt,
        presenceState: s.presenceState,
        currentPage: s.currentPage,
        currentPagePath: s.currentPagePath
      };

      if (s.batchIds && s.batchIds.length > 0) {
        s.batchIds.forEach((bId: string) => {
          if (groupedMap.has(bId)) {
            groupedMap.get(bId)!.push(memberObj);
          }
        });
      } else {
        unassignedMembers.push(memberObj);
      }

      // Find parents of this student
      parents.forEach(p => {
        const isLinkedByCode = s.studentCode && p.studentCodes.includes(s.studentCode);
        const isLinkedByEmail = s.parentEmail && p.email === s.parentEmail;
        
        if (isLinkedByCode || isLinkedByEmail) {
          const parentMemberObj = {
            id: p.id,
            name: p.name,
            email: p.email,
            role: p.role,
            linkedStudentName: s.name,
            lastActiveAt: p.lastActiveAt,
            presenceState: p.presenceState,
            currentPage: p.currentPage,
            currentPagePath: p.currentPagePath
          };

          if (s.batchIds && s.batchIds.length > 0) {
            s.batchIds.forEach((bId: string) => {
              if (groupedMap.has(bId)) {
                const list = groupedMap.get(bId)!;
                // Avoid duplicating parent in the same batch if they have multiple children (or verify deduplication)
                if (!list.some(existing => existing.id === p.id)) {
                  list.push(parentMemberObj);
                }
              }
            });
          } else {
            if (!unassignedMembers.some(existing => existing.id === p.id)) {
              unassignedMembers.push(parentMemberObj);
            }
          }
        }
      });
    });

    // Handle parents who aren't mapped to any active students
    parents.forEach(p => {
      const isAlreadyAdded = Array.from(groupedMap.values()).some(list => list.some(m => m.id === p.id)) ||
                             unassignedMembers.some(m => m.id === p.id);
      if (!isAlreadyAdded) {
        unassignedMembers.push({
          id: p.id,
          name: p.name,
          email: p.email,
          role: p.role,
          lastActiveAt: p.lastActiveAt,
          presenceState: p.presenceState,
          currentPage: p.currentPage,
          currentPagePath: p.currentPagePath
        });
      }
    });

    const reportData = batches.map(b => ({
      batchId: b.id,
      batchName: b.name,
      members: groupedMap.get(b.id) || []
    }));

    if (unassignedMembers.length > 0) {
      reportData.push({
        batchId: 'unassigned',
        batchName: 'Unassigned Students & Parents',
        members: unassignedMembers
      });
    }

    const logs = logsSnap.docs.map(doc => {
      const d = doc.data();
      return {
        id: doc.id,
        uid: d.uid,
        name: d.name || 'Unknown',
        email: d.email || '',
        role: d.role || 'student',
        batchIds: d.batchIds || [],
        type: d.type || 'login',
        timestamp: d.timestamp ? (d.timestamp.toDate ? d.timestamp.toDate() : d.timestamp) : null
      };
    });

    const result = {
      success: true,
      batches: reportData,
      logs: logs
    };

    await ReportCacheManager.setReport(cacheKey, result, 60); // Cache for 1 minute

    return NextResponse.json(result);

  } catch (error: any) {
    console.error('API load login register report error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
