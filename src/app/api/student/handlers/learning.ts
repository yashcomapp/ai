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
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, {
        headers: {
          'Cache-Control': 'private, no-cache, no-store, max-age=0, must-revalidate'
        }
      });
    }

    const data = await getStudentLearningData(student.userData);
    if (studentCode) {
      setInCache(cacheKey, data, 60000); // 60s in-memory cache
    }
    return NextResponse.json(data, {
      headers: {
        'Cache-Control': 'private, no-cache, no-store, max-age=0, must-revalidate'
      }
    });

  } catch (error: any) {
    console.error('API get learning path error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
