import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { getStudentLearningData } from '@/lib/studentDb';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    if (student.userData?.autonomous === true) {
      return NextResponse.json({ message: 'Access Denied: Autonomous mode students do not have access to Learning OS.' }, { status: 403 });
    }

    const data = await getStudentLearningData(student.userData);
    return NextResponse.json(data);

  } catch (error: any) {
    console.error('API get learning path error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
