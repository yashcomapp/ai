import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
export const dynamic = 'force-dynamic';

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

    // A. Query reviews to compute exams taken & average score
    const reviewsSnap = await adminDb.collection('reviews')
      .where('studentCode', '==', studentCode)
      .where('status', 'in', ['pending', 'approved'])
      .get();

    const reviews = reviewsSnap.docs.map(doc => doc.data());
    const totalExams = reviews.length;
    let avgScore = 'N/A';

    if (totalExams > 0) {
      const sum = reviews.reduce((s, r) => s + parseFloat(r.percentage || 0), 0);
      avgScore = (sum / totalExams).toFixed(1) + '%';
    }

    // Query studentTopicMastery for dynamic stats
    const masterySnap = await adminDb.collection('studentTopicMastery')
      .where('studentCode', '==', studentCode)
      .get();
      
    let masteredTopics = 0;
    let weakTopicsCount = 0;
    masterySnap.docs.forEach(doc => {
      const mData = doc.data();
      const mastery = Number(mData.mastery || 0);
      const confidence = Number(mData.confidence || 0);
      if (mastery >= 90 && confidence >= 20) {
        masteredTopics += 1;
      } else if (mastery < 50) {
        weakTopicsCount += 1;
      }
    });

    return NextResponse.json({
      profile: {
        name: student.userData?.name || '',
        email: student.decodedToken.email || '',
        parentEmail: student.userData?.parentEmail || '',
        dob: student.userData?.dob || ''
      },
      stats: {
        totalExams,
        avgScore,
        weakTopicsCount,
        masteredTopics
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
