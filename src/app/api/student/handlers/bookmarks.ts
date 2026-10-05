import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyAnyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const authResult = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 403 });
    }

    const { role } = authResult;
    const { searchParams } = new URL(req.url);
    const paramStudentCode = searchParams.get('studentCode') || '';

    let studentCode = authResult.role === 'student' ? authResult.userData?.studentCode : '';
    if (role === 'admin' && paramStudentCode) {
      studentCode = paramStudentCode;
    } else if (role === 'parent') {
      const parentData = authResult.userData;
      if (paramStudentCode && (parentData?.studentCodes?.includes(paramStudentCode) || parentData?.studentCode === paramStudentCode)) {
        studentCode = paramStudentCode;
      } else {
        studentCode = parentData?.studentCode || (parentData?.studentCodes && parentData.studentCodes[0]) || '';
      }
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Student code required.' }, { status: 400 });
    }

    const snap = await adminDb.collection('studentBookmarks')
      .where('studentCode', '==', studentCode)
      .get();

    const bookmarks = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));

    return NextResponse.json({ success: true, bookmarks });
  } catch (error: any) {
    console.error('API Student Bookmarks GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const authResult = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 403 });
    }

    const body = await req.json();
    const { questionCode, questionText, subjectCode, topicCode, chapterNumber, tag, examId, status, studentCode: bodyStudentCode } = body;

    if (!questionCode) {
      return NextResponse.json({ message: 'Missing questionCode.' }, { status: 400 });
    }

    let studentCode = authResult.role === 'student' ? authResult.userData?.studentCode : '';
    if (authResult.role === 'admin' && bodyStudentCode) {
      studentCode = bodyStudentCode;
    } else if (authResult.role === 'parent') {
      const parentData = authResult.userData;
      studentCode = bodyStudentCode || parentData?.studentCode || (parentData?.studentCodes && parentData.studentCodes[0]) || '';
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Student code required.' }, { status: 400 });
    }

    const bookmarkDocId = `${studentCode}_${questionCode}`;
    const docRef = adminDb.collection('studentBookmarks').doc(bookmarkDocId);
    const existingSnap = await docRef.get();

    if (body.action === 'remove' || (existingSnap.exists && body.action === 'toggle')) {
      await docRef.delete();
      return NextResponse.json({ success: true, isBookmarked: false });
    }

    // Save or update bookmark
    const bookmarkData: any = {
      studentCode,
      questionCode,
      questionText: questionText || '',
      subjectCode: subjectCode || '',
      topicCode: topicCode || '',
      chapterNumber: chapterNumber || '',
      tag: tag || 'Tricky Question',
      examId: examId || '',
      status: status || 'active',
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    if (!existingSnap.exists) {
      bookmarkData.createdAt = admin.firestore.FieldValue.serverTimestamp();
      bookmarkData.bookmarkedBy = authResult.role;
    }

    await docRef.set(bookmarkData, { merge: true });

    return NextResponse.json({ success: true, isBookmarked: true, bookmark: bookmarkData });
  } catch (error: any) {
    console.error('API Student Bookmarks POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
