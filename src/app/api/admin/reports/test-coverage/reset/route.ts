import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyAnyRole } from '@/lib/auth';
import { ReportCacheManager } from '@/lib/reportCache';
import { chunkArray } from '@/lib/firestoreUtils';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const authResult = await verifyAnyRole(req, ['admin']);
    if (!authResult) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { subjectId, topicCode, examId } = body;

    if (!subjectId) {
      return NextResponse.json({ error: 'Missing subjectId.' }, { status: 400 });
    }

    // 1. Fetch the syllabus subject document to get class and subject name
    const subjectDoc = await adminDb.collection('syllabus').doc(subjectId).get();
    if (!subjectDoc.exists) {
      return NextResponse.json({ message: 'Subject syllabus not found.' }, { status: 404 });
    }

    const subjectData = subjectDoc.data()!;
    const subjectName = subjectData.subject || '';
    const classVal = subjectData.class || '';

    // 2. Fetch all exams and subjectiveExams matching class & subject
    const [examsSnap, subjectiveExamsSnap] = await Promise.all([
      adminDb.collection('exams')
        .where('class', '==', classVal)
        .where('subjectName', '==', subjectName)
        .get(),
      adminDb.collection('subjectiveExams')
        .where('class', '==', classVal)
        .where('subject', '==', subjectName)
        .get()
    ]);

    let examsList = examsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
    let subjectiveExamsList = subjectiveExamsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));

    // 3. Filter by examId or topicCode if provided
    if (examId) {
      examsList = examsList.filter(exam => exam.id === examId);
      subjectiveExamsList = subjectiveExamsList.filter(exam => exam.id === examId);
    } else if (topicCode) {
      examsList = examsList.filter(exam => 
        Array.isArray(exam.topicCodes) && exam.topicCodes.includes(topicCode)
      );
      
      subjectiveExamsList = subjectiveExamsList.filter(exam => {
        const topicCodes = exam.topicCodes || [];
        if (topicCodes.includes(topicCode)) return true;
        
        // Match by first question topic derivation as fallback
        const qIds = exam.questionIds || [];
        if (qIds.length > 0) {
          const qId = qIds[0];
          const cleanCode = qId.replace(/[-_]\d+$/, '');
          const parts = cleanCode.split(/[-_]/);
          if (parts.length >= 5) {
            let derived = '';
            if (parts[4].includes('.')) {
              derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${parts[4]}`;
            } else if (parts.length >= 7 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5]) && /^\d+$/.test(parts[6])) {
              derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[4]}-${parts[5]}.${parts[6]}`;
            }
            if (derived === topicCode) return true;
          }
        }

        // Match by topic name matching as fallback
        const examTopics = exam.topics || [];
        // We find the topic name in syllabus chapters
        let topicName = '';
        const chapters = subjectData.chapters || [];
        chapters.forEach((chap: any) => {
          (chap.topics || []).forEach((top: any) => {
            if (top.topicCode === topicCode) {
              topicName = top.name;
            }
          });
        });

        if (topicName && examTopics.some((tName: string) => String(tName).toLowerCase() === String(topicName).toLowerCase())) {
          return true;
        }

        return false;
      });
    }

    const objExamIds = examsList.map(e => e.id).filter(Boolean);
    const subjExamIds = subjectiveExamsList.map(e => e.id).filter(Boolean);

    let deletedReviewsCount = 0;
    let deletedSubjAttemptsCount = 0;
    // 4. Delete objective reviews in batches (parallel queries, safe 500-sized batch commits)
    if (objExamIds.length > 0) {
      const chunks = chunkArray(objExamIds, 10);
      const snaps = await Promise.all(
        chunks.map(chunk => 
          adminDb.collection('reviews')
            .where('examId', 'in', chunk)
            .get()
        )
      );

      const allDocs = snaps.flatMap(snap => snap.docs);
      deletedReviewsCount = allDocs.length;

      for (let i = 0; i < allDocs.length; i += 500) {
        const batch = adminDb.batch();
        const docChunk = allDocs.slice(i, i + 500);
        docChunk.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
      }
    }

    // 5. Delete subjective attempts in batches (parallel queries, safe 500-sized batch commits)
    if (subjExamIds.length > 0) {
      const chunks = chunkArray(subjExamIds, 10);

      const snaps = await Promise.all(
        chunks.map(chunk => 
          adminDb.collection('subjectiveAttempts')
            .where('examId', 'in', chunk)
            .get()
        )
      );

      const allDocs = snaps.flatMap(snap => snap.docs);
      deletedSubjAttemptsCount = allDocs.length;

      for (let i = 0; i < allDocs.length; i += 500) {
        const batch = adminDb.batch();
        const docChunk = allDocs.slice(i, i + 500);
        docChunk.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
      }
    }    // 6. Invalidate report cache
    const cacheKey = `test-coverage-report-${subjectId}`;
    await ReportCacheManager.invalidateReport(cacheKey);

    return NextResponse.json({
      success: true,
      message: 'Test attempts reset successfully.',
      details: {
        objExamsClearedCount: objExamIds.length,
        subjExamsClearedCount: subjExamIds.length,
        deletedReviewsCount,
        deletedSubjAttemptsCount
      }
    });

  } catch (error: any) {
    console.error('API POST test reset error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
