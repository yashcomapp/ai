import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyAnyRole } from '@/lib/auth';
import { getFromCache, setInCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const verified = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!verified) {
      return NextResponse.json({ message: 'Unauthorized' }, { status: 401 });
    }

    const { decodedToken, userData, role } = verified;
    let parentAuth = role === 'parent' ? { decodedToken, userData } : null;
    let studentAuth = role === 'student' ? { decodedToken, userData } : null;
    if (role === 'admin') {
      studentAuth = { decodedToken, userData };
    }

    const cacheKey = 'active_notices_24h';
    let allNotices = getFromCache<any[]>(cacheKey);

    if (!allNotices) {
      const noticesSnap = await adminDb.collection('notices')
        .orderBy('createdAt', 'desc')
        .limit(50)
        .get();

      const twentyFourHoursAgo = Date.now() - 24 * 60 * 60 * 1000;
      allNotices = noticesSnap.docs.map(doc => {
        const data = doc.data();
        const createdAtMs = data.createdAt ? (data.createdAt.toMillis ? data.createdAt.toMillis() : new Date(data.createdAt).getTime()) : 0;
        return {
          id: doc.id,
          title: data.title || '',
          body: data.body || '',
          targetType: data.targetType || 'all',
          targetValues: data.targetValues || [],
          createdAt: data.createdAt ? (data.createdAt.toDate ? data.createdAt.toDate().toISOString() : new Date(data.createdAt).toISOString()) : null,
          createdAtMs,
          isOverlay: !!data.isOverlay,
          type: data.type || 'general',
          noticeDate: data.noticeDate || null
        };
      }).filter(notice => notice.createdAtMs >= twentyFourHoursAgo);

      setInCache(cacheKey, allNotices, 60000); // 60s cache
    }

    let filteredNotices: any[] = [];

    if (studentAuth) {
      const studentData = studentAuth.userData;
      const studentCode = studentData.studentCode || '';
      const batchId = studentData.batchId || null;
      const batchIds = studentData.batchIds || [];

      filteredNotices = allNotices.filter(notice => {
        if (notice.targetType === 'all') return true;
        if (notice.targetType === 'student') {
          return notice.targetValues.includes(studentCode);
        }
        if (notice.targetType === 'batch') {
          return notice.targetValues.includes(batchId) || batchIds.some((b: string) => notice.targetValues.includes(b));
        }
        return false;
      });
    } else if (parentAuth) {
      const parentData = parentAuth.userData;
      const parentEmail = parentData.email?.toLowerCase() || '';

      // Resolve children student codes and batch ids
      let childrenCodes: string[] = [];
      if (Array.isArray(parentData?.studentCodes)) {
        childrenCodes = parentData.studentCodes.filter(Boolean);
      } else if (parentData?.studentCode) {
        childrenCodes = [parentData.studentCode];
      } else if (parentData?.studentId) {
        childrenCodes = [parentData.studentId];
      }

      // Query parentEmail matching and studentCodes in parallel
      let childrenBatches: string[] = [];
      try {
        const [studsSnap, snaps] = await Promise.all([
          parentEmail
            ? adminDb.collection('users')
                .where('role', '==', 'student')
                .where('parentEmail', '==', parentEmail)
                .get()
                .catch(() => ({ docs: [] } as any))
            : Promise.resolve({ docs: [] } as any),
          childrenCodes.length > 0
            ? adminDb.collection('users')
                .where('role', '==', 'student')
                .where('studentCode', 'in', childrenCodes.slice(0, 30))
                .get()
                .catch(() => ({ docs: [] } as any))
            : Promise.resolve({ docs: [] } as any)
        ]);

        studsSnap.docs.forEach((doc: any) => {
          const d = doc.data();
          if (d.studentCode && !childrenCodes.includes(d.studentCode)) {
            childrenCodes.push(d.studentCode);
          }
          if (d.batchId && !childrenBatches.includes(d.batchId)) {
            childrenBatches.push(d.batchId);
          }
          if (Array.isArray(d.batchIds)) {
            d.batchIds.forEach((b: string) => {
              if (b && !childrenBatches.includes(b)) {
                childrenBatches.push(b);
              }
            });
          }
        });

        snaps.docs.forEach((doc: any) => {
          const d = doc.data();
          if (d.batchId && !childrenBatches.includes(d.batchId)) {
            childrenBatches.push(d.batchId);
          }
          if (Array.isArray(d.batchIds)) {
            d.batchIds.forEach((b: string) => {
              if (b && !childrenBatches.includes(b)) {
                childrenBatches.push(b);
              }
            });
          }
        });
      } catch (e) {
        console.warn('Error fetching children for parent notice matching:', e);
      }

      filteredNotices = allNotices.filter(notice => {
        if (notice.targetType === 'all') return true;
        if (notice.targetType === 'parent') {
          return notice.targetValues.some((v: string) => v.toLowerCase() === parentEmail);
        }
        if (notice.targetType === 'student') {
          return notice.targetValues.some((v: string) => childrenCodes.includes(v));
        }
        if (notice.targetType === 'batch') {
          return notice.targetValues.some((v: string) => childrenBatches.includes(v));
        }
        return false;
      });
    }

    // Fetch seen logs for this user to populate seen status
    const userCodeKey = studentAuth 
      ? (studentAuth.userData.studentCode || '') 
      : (parentAuth?.userData.email || '');

    const userSeenNoticeIds = new Set<string>();
    if (userCodeKey) {
      try {
        const logsSnap = await adminDb.collection('noticeSeenLogs')
          .where('userCode', 'in', [userCodeKey, userCodeKey.toLowerCase(), userCodeKey.toUpperCase()])
          .get();
        logsSnap.forEach(doc => {
          const data = doc.data();
          if (data.noticeId) {
            userSeenNoticeIds.add(data.noticeId);
          }
        });
      } catch (err) {
        console.warn('Failed to fetch user seen logs for notices matching:', err);
      }
    }

    const noticesWithSeen = filteredNotices.map(notice => ({
      ...notice,
      seen: userSeenNoticeIds.has(notice.id)
    }));

    return NextResponse.json({ success: true, notices: noticesWithSeen });
  } catch (error: any) {
    console.error('API GET user notices error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
