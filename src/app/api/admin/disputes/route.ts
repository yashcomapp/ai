import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ExamReviewService } from '@/services/examReview.service';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId');
    const status = searchParams.get('status') || 'all';

    let query: FirebaseFirestore.Query = adminDb.collection('questionDisputes');

    if (examId) {
      query = query.where('examId', '==', examId);
    }
    if (status !== 'all') {
      query = query.where('status', '==', status);
    }

    const snap = await query.limit(300).get();

    const rawDisputes = snap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    // Hydrate student metadata (class, batchName, name)
    const studentCodes = Array.from(new Set(rawDisputes.map((d: any) => (d.studentCode || '').toUpperCase()).filter(Boolean)));
    const usersMap = new Map<string, { className: string; classNum: string; name: string }>();

    if (studentCodes.length > 0) {
      try {
        const usersSnap = await adminDb.collection('users').where('role', '==', 'student').get();
        usersSnap.docs.forEach(doc => {
          const u = doc.data();
          const code = (u.studentCode || '').toUpperCase();
          if (code) {
            const cNum = u.classNum || u.class || '';
            const cName = cNum ? `Class ${cNum}` : (u.className || u.batchName || '');
            usersMap.set(code, {
              className: cName,
              classNum: String(cNum),
              name: u.name || 'Student'
            });
          }
        });
      } catch (err) {
        console.warn('Failed to hydrate student profiles for disputes:', err);
      }
    }

    const disputes = rawDisputes.map((d: any) => {
      const sCode = (d.studentCode || '').toUpperCase();
      const uInfo = usersMap.get(sCode);
      const cName = uInfo?.className || (d.classNum ? `Class ${d.classNum}` : (d.batchName || d.className || ''));
      const sName = uInfo?.name || d.studentName || 'Student';
      return {
        ...d,
        studentName: sName,
        className: cName,
        classNum: uInfo?.classNum || d.classNum || ''
      };
    });

    // Sort by submittedAt ascending so ranking is chronological
    disputes.sort((a: any, b: any) => {
      const timeA = new Date(a.submittedAt || a.createdAt || 0).getTime();
      const timeB = new Date(b.submittedAt || b.createdAt || 0).getTime();
      return timeA - timeB;
    });

    // Group disputes by examId and questionId
    const grouped: Record<string, Record<string, any[]>> = {};
    const questionIdSet = new Set<string>();

    disputes.forEach((d: any) => {
      const eId = d.examId || 'unassigned_exam';
      const qId = d.questionId || d.questionCode || 'unknown_q';
      if (!grouped[eId]) grouped[eId] = {};
      if (!grouped[eId][qId]) grouped[eId][qId] = [];
      grouped[eId][qId].push(d);

      if (qId && qId !== 'unknown_q') {
        questionIdSet.add(qId);
      }
      if (d.questionCode) {
        questionIdSet.add(d.questionCode);
      }
    });

    // Hydrate Question details from Question Bank
    const questionsMap: Record<string, any> = {};
    const codeList = Array.from(questionIdSet);

    if (codeList.length > 0) {
      const refs = codeList.map(code => adminDb.collection('questions').doc(code));
      const directSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];
      const missingCodes: string[] = [];

      directSnaps.forEach((snap, idx) => {
        if (snap && snap.exists) {
          const qData = snap.data();
          const qObj = { id: codeList[idx], questionCode: codeList[idx], ...qData };
          questionsMap[codeList[idx]] = qObj;
          if (qData?.questionCode) questionsMap[qData.questionCode] = qObj;
        } else {
          missingCodes.push(codeList[idx]);
        }
      });

      if (missingCodes.length > 0) {
        const chunkSize = 30;
        const chunks = [];
        for (let i = 0; i < missingCodes.length; i += chunkSize) {
          chunks.push(missingCodes.slice(i, i + chunkSize));
        }

        const querySnaps = await Promise.all(
          chunks.map(chunk =>
            adminDb.collection('questions').where('questionCode', 'in', chunk).get()
          )
        );

        querySnaps.forEach(s => {
          s.docs.forEach(doc => {
            const qData = doc.data();
            const qObj = { id: doc.id, ...qData };
            questionsMap[doc.id] = qObj;
            if (qData?.questionCode) questionsMap[qData.questionCode] = qObj;
          });
        });
      }
    }

    return NextResponse.json({
      success: true,
      disputes,
      grouped,
      questionsMap
    });
  } catch (error: any) {
    console.error('API admin get exam disputes error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const body = await req.json();
    const {
      examId,
      questionId,
      newCorrectOption,
      action = 'correct_key', // 'correct_key' | 'bonus_all' | 'quarantine'
      notes = ''
    } = body;

    if (!examId || !questionId) {
      return NextResponse.json({ message: 'Missing required parameters (examId, questionId).' }, { status: 400 });
    }

    const adminEmail = adminUser.decodedToken?.email || 'Admin';

    const result = await ExamReviewService.batchReevaluateExam({
      examId,
      questionId,
      newCorrectOption,
      action,
      notes,
      adminEmail
    });

    return NextResponse.json({
      success: true,
      ...result
    });
  } catch (error: any) {
    console.error('API admin batch reevaluate dispute error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
