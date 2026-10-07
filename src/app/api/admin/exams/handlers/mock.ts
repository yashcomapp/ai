import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const user = await verifyRole(req, 'admin');
    if (!user) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || searchParams.get('id');
    const examType = searchParams.get('type') || 'objective';

    if (!examId) {
      return NextResponse.json({ message: 'Missing exam ID' }, { status: 400 });
    }

    // 1. Fetch exam metadata
    let examData: any = null;
    if (examType === 'subjective') {
      const snap = await adminDb.collection('subjectiveExams').doc(examId).get();
      if (snap.exists) examData = { id: snap.id, ...snap.data() };
    } else {
      const snap = await adminDb.collection('exams').doc(examId).get();
      if (snap.exists) examData = { id: snap.id, ...snap.data() };
    }

    if (!examData) {
      // Fallback cross-check
      const snapObj = await adminDb.collection('exams').doc(examId).get();
      if (snapObj.exists) {
        examData = { id: snapObj.id, ...snapObj.data() };
      } else {
        const snapSub = await adminDb.collection('subjectiveExams').doc(examId).get();
        if (snapSub.exists) examData = { id: snapSub.id, ...snapSub.data() };
      }
    }

    if (!examData) {
      return NextResponse.json({ message: 'Exam not found' }, { status: 404 });
    }

    // 2. Gather question IDs / codes
    const candidateCodes: string[] = [];
    if (Array.isArray(examData.questionCodes) && examData.questionCodes.length > 0) {
      candidateCodes.push(...examData.questionCodes);
    }
    if (Array.isArray(examData.questionIds) && examData.questionIds.length > 0) {
      candidateCodes.push(...examData.questionIds);
    }
    if (Array.isArray(examData.questions) && examData.questions.length > 0) {
      examData.questions.forEach((q: any) => {
        if (typeof q === 'string') candidateCodes.push(q);
        else if (q && typeof q === 'object') {
          if (q.id) candidateCodes.push(q.id);
          if (q.questionCode) candidateCodes.push(q.questionCode);
        }
      });
    }

    const questionCodes = Array.from(new Set(candidateCodes.filter(Boolean)));

    // 3. Hydrate questions from questions collection
    const questionMap = new Map<string, any>();

    // Check embedded questions
    if (Array.isArray(examData.questions) && examData.questions.length > 0) {
      examData.questions.forEach((q: any) => {
        if (q && typeof q === 'object' && (q.text || q.questionText)) {
          const key = q.id || q.questionCode;
          if (key) questionMap.set(key, q);
        }
      });
    }

    // Lookup in database
    if (questionCodes.length > 0) {
      const lookupIds = new Set<string>();
      questionCodes.forEach(id => {
        lookupIds.add(id);
        const norm = id.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
        lookupIds.add(norm);
      });

      const refs = Array.from(lookupIds).map(id => adminDb.collection('questions').doc(id));
      const snaps = await adminDb.getAll(...refs).catch(() => []);
      snaps.forEach(snap => {
        if (snap && snap.exists) {
          const data = snap.data()!;
          const fullQ = { id: snap.id, ...data };
          questionMap.set(snap.id, fullQ);
          if (data.questionCode) {
            questionMap.set(data.questionCode, fullQ);
          }
        }
      });

      // Secondary fallback query for any remaining missing codes
      const missing = questionCodes.filter(c => !questionMap.has(c));
      if (missing.length > 0) {
        for (let i = 0; i < missing.length; i += 30) {
          const chunk = missing.slice(i, i + 30);
          const qSnap = await adminDb.collection('questions').where('questionCode', 'in', chunk).get().catch(() => ({ docs: [] } as any));
          qSnap.docs.forEach((doc: any) => {
            const data = doc.data();
            const fullQ = { id: doc.id, ...data };
            questionMap.set(doc.id, fullQ);
            if (data.questionCode) questionMap.set(data.questionCode, fullQ);
          });
        }
      }
    }

    // 4. Assemble ordered questions list
    let finalQuestions: any[] = [];
    if (questionCodes.length > 0) {
      finalQuestions = questionCodes.map(code => questionMap.get(code)).filter(Boolean);
    }
    if (finalQuestions.length === 0 && questionMap.size > 0) {
      finalQuestions = Array.from(questionMap.values());
    }
    if (finalQuestions.length === 0 && Array.isArray(examData.questions) && examData.questions.length > 0) {
      finalQuestions = examData.questions;
    }

    return NextResponse.json({
      success: true,
      exam: {
        ...examData,
        questions: finalQuestions
      }
    });

  } catch (error: any) {
    console.error('Error fetching mock exam:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
