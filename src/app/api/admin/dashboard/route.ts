import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST as getISTDateString } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const todayStr = getISTDateString();
    const adminUid = adminUser.decodedToken?.uid || 'admin';

    // Fetch counts and recent registrations in parallel
    const [
      studentsCount,
      batchesCount,
      activeExamsCount,
      overdueCountSnap,
      attendanceSnap,
      chatRoomsSnap,
      recentRegsSnap
    ] = await Promise.all([
      adminDb.collection('users').where('role', '==', 'student').count().get(),
      adminDb.collection('batches').count().get(),
      adminDb.collection('exams').where('status', '==', 'active').count().get(),
      adminDb.collection('studentFees').where('hasOverdueInstallment', '==', true).count().get(),
      adminDb.collection('attendance').where('date', '==', todayStr).get(),
      adminDb.collection('chatRooms').get(),
      adminDb.collection('registrations')
        .where('status', '==', 'pending')
        .orderBy('createdAt', 'desc')
        .limit(5)
        .get()
    ]);

    // Fetch cached cumulative practice count
    const statsDocRef = adminDb.collection('systemStats').doc('practiceStats');
    const statsDocSnap = await statsDocRef.get();
    
    let cumulativePracticeCount = 0;
    let shouldUpdate = true;

    if (statsDocSnap.exists) {
      const statsData = statsDocSnap.data()!;
      cumulativePracticeCount = statsData.cumulativeCount || 0;
      const lastUpdated = statsData.lastUpdated?.toDate ? statsData.lastUpdated.toDate() : new Date(statsData.lastUpdated || 0);
      
      const now = new Date();
      const lastUpdatedDateString = lastUpdated.toDateString();
      const nowDateString = now.toDateString();
      
      if (lastUpdatedDateString === nowDateString) {
        shouldUpdate = false;
      }
    }

    if (shouldUpdate) {
      try {
        const countSnap = await adminDb.collection('practiceSubmissions').count().get();
        cumulativePracticeCount = countSnap.data().count;
        await statsDocRef.set({
          cumulativeCount: cumulativePracticeCount,
          lastUpdated: new Date()
        }, { merge: true });
        console.log(`Successfully updated cumulative practice count: ${cumulativePracticeCount}`);
      } catch (err: any) {
        console.error('Failed to update cumulative practice count aggregation:', err.message);
      }
    }

    // Map recent registrations
    const recentRegs = recentRegsSnap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        studentName: data.studentName || '',
        studentEmail: data.studentEmail || '',
        batchName: data.batchName || '',
        createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : new Date(data.createdAt)
      };
    });

    // Calculate today's attendance rate
    let totalMarked = 0;
    let presentTotal = 0;
    attendanceSnap.docs.forEach(doc => {
      const records = doc.data().records || {};
      Object.values(records).forEach((r: any) => {
        if (r.status === 'present' || r.status === 'late') {
          presentTotal++;
          totalMarked++;
        } else if (r.status === 'absent') {
          totalMarked++;
        }
      });
    });
    const todayAttendanceRate = totalMarked > 0 ? Math.round((presentTotal / totalMarked) * 100) : null;

    // Calculate admin unread chats count
    const unreadChatsCount = chatRoomsSnap.docs.filter(doc => {
      const uCounts = doc.data().unreadCounts || {};
      return Number(uCounts[adminUid] || 0) > 0;
    }).length;

    return NextResponse.json({
      stats: {
        totalStudents: studentsCount.data().count,
        totalBatches: batchesCount.data().count,
        cumulativePractice: cumulativePracticeCount,
        activeExams: activeExamsCount.data().count,
        todayAttendanceRate,
        overdueFeesCount: overdueCountSnap.data().count,
        unreadChatsCount
      },
      recentRegistrations: recentRegs
    });

  } catch (error: any) {
    console.error('API admin dashboard error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
