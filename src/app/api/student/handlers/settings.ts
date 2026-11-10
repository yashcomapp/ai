import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode;
    if (!studentCode) {
      return NextResponse.json({ message: 'Missing student code mapping.' }, { status: 400 });
    }

    return NextResponse.json({
      profile: {
        name: student.userData?.name || '',
        email: student.decodedToken.email || '',
        parentEmail: student.userData?.parentEmail || '',
        dob: student.userData?.dob || ''
      },
      stats: {
        totalExams: 0,
        avgScore: '0.0%',
        weakTopicsCount: 0,
        masteredTopics: 0
      }
    });

  } catch (error: any) {
    console.error('API load settings error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Save user profile information
export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { name, parentEmail, dob } = body;

    if (!name) {
      return NextResponse.json({ message: 'Name is a required field.' }, { status: 400 });
    }

    const updateData = {
      name: name.trim(),
      parentEmail: parentEmail ? parentEmail.trim() : '',
      dob: dob || '',
      updatedAt: new Date()
    };

    await adminDb.collection('users').doc(student.decodedToken.uid).update(updateData);

    return NextResponse.json({ success: true, message: 'Profile updated successfully.' });

  } catch (error: any) {
    console.error('API save settings error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
