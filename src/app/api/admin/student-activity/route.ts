import { NextRequest, NextResponse } from 'next/server';
import { adminDb, adminAuth } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    // 1. Fetch both student and parent users
    const [studentsSnap, parentsSnap] = await Promise.all([
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('users').where('role', '==', 'parent').get()
    ]);

    // 2. Map students data
    const studentsActivity = studentsSnap.docs.map(doc => {
      const data = doc.data();
      const uid = doc.id;
      const baseName = data.name || data.displayName || 'Unknown';
      return {
        uid,
        name: `${baseName} (S)${data.autonomous ? ' ⭐' : ''}`,
        email: data.email || '',
        studentCode: data.studentCode || '',
        status: data.status || 'active',
        lastLoginAt: data.lastLoginAt?.toDate ? data.lastLoginAt.toDate().toISOString() : data.lastLoginAt || null,
        currentPage: data.currentPage || 'Offline / Out of app',
        currentPagePath: data.currentPagePath || '',
        currentPageAt: data.currentPageAt?.toDate ? data.currentPageAt.toDate().toISOString() : data.currentPageAt || null,
        cumulativeSeconds: data.cumulativeSeconds || 0
      };
    }).filter(s => s.status !== 'inactive');

    const activeStudentCodes = new Set(studentsActivity.map(s => s.studentCode.toLowerCase()));

    // 3. Map parents data
    const parentsActivity = parentsSnap.docs.map(doc => {
      const data = doc.data();
      const uid = doc.id;
      const baseName = data.name || data.displayName || 'Unknown';
      const pCodes = data.studentCodes || (data.studentCode ? [data.studentCode] : []);
      const hasActiveChild = pCodes.some((code: string) => activeStudentCodes.has(code.toLowerCase()));
      if (!hasActiveChild) return null;

      return {
        uid,
        name: `${baseName} (P)`,
        email: data.email || '',
        studentCode: data.studentCode || data.studentId || '',
        lastLoginAt: data.lastLoginAt?.toDate ? data.lastLoginAt.toDate().toISOString() : data.lastLoginAt || null,
        currentPage: data.currentPage || 'Offline / Out of app',
        currentPagePath: data.currentPagePath || '',
        currentPageAt: data.currentPageAt?.toDate ? data.currentPageAt.toDate().toISOString() : data.currentPageAt || null,
        cumulativeSeconds: data.cumulativeSeconds || 0
      };
    }).filter(p => p !== null) as any[];

    const combinedActivity = [...studentsActivity, ...parentsActivity];

    // Sort by lastLoginAt desc by default
    combinedActivity.sort((a, b) => {
      const aTime = a.lastLoginAt ? new Date(a.lastLoginAt).getTime() : 0;
      const bTime = b.lastLoginAt ? new Date(b.lastLoginAt).getTime() : 0;
      return bTime - aTime;
    });

    return NextResponse.json({ studentsActivity: combinedActivity });
  } catch (error: any) {
    console.error('Student activity API error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
