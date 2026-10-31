import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getStudentLearningData } from '@/lib/studentDb';
import { getFromCache, setInCache } from '@/lib/firebase/cache';

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode || '';
    const cacheKey = `student_learning_${studentCode}`;
    const responseHeaders: Record<string, string> = {
      'Cache-Control': 'private, max-age=60, stale-while-revalidate=120'
    };
    if (student.claimsUpdated) {
      responseHeaders['x-claims-updated'] = 'true';
    }

    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, { headers: responseHeaders });
    }

    const data = await getStudentLearningData(student.userData);
    if (studentCode) {
      setInCache(cacheKey, data, 60000); // 60s in-memory cache
    }
    return NextResponse.json(data, { headers: responseHeaders });

  } catch (error: any) {
    console.error('API get learning path error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
