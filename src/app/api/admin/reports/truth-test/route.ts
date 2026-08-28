import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ReportCacheManager } from '@/lib/reportCache';
import { chunkArray } from '@/lib/firestoreUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || '';

    if (!examId) {
      return NextResponse.json({ message: 'Missing parameters (examId).' }, { status: 400 });
    }

    const cacheKey = `truth-test-report-${examId}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached);
    }

    // 1. Fetch Saturday Classroom Test doc
    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Classroom Test not found.' }, { status: 404 });
    }
    const classroomExam = examSnap.data()!;
    if (classroomExam.type !== 'classroom_test') {
      return NextResponse.json({ message: 'Selected exam is not a Saturday Classroom Test.' }, { status: 400 });
    }

    // 2. Resolve associated home practices scheduled for same week
    let homeExamIds = classroomExam.sampledFromHomeExamIds || [];
    if (homeExamIds.length === 0) {
      // Fallback matching: Find home practices in same week sharing at least one question
      const classQIds = classroomExam.questionIds || [];
      if (classQIds.length > 0) {
        const homePracticesSnap = await adminDb.collection('subjectiveExams')
          .where('type', '==', 'home_practice')
          .where('class', '==', classroomExam.class)
          .get();
        
        homePracticesSnap.docs.forEach(doc => {
          const hData = doc.data();
          const hQIds = hData.questionIds || [];
          const hasCommon = hQIds.some((id: string) => classQIds.includes(id));
          if (hasCommon) {
            homeExamIds.push(doc.id);
          }
        });
      }
    }

    // Deduplicate homeExamIds
    homeExamIds = Array.from(new Set(homeExamIds));

    // 3. Fetch student users, classroom test reviews, parent reviews, and questions in parallel
    const queries: Promise<any>[] = [
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('subjectiveReviews').where('examId', '==', examId).get()
    ];

    if (homeExamIds.length > 0) {
      const chunks = chunkArray(homeExamIds, 30);
      const parentReviewsQueries = chunks.map(chunk => 
        adminDb.collection('subjectiveReviews')
          .where('examId', 'in', chunk)
          .where('reviewerType', '==', 'parent')
          .get()
      );
      queries.push(Promise.all(parentReviewsQueries));
    } else {
      queries.push(Promise.resolve([]));
    }

    // Fetch Saturday classroom test question texts
    const classroomQuestionIds = classroomExam.questionIds || [];
    if (classroomQuestionIds.length > 0) {
      const refs = classroomQuestionIds.map((qid: string) => adminDb.collection('questions').doc(qid));
      queries.push(adminDb.getAll(...refs).catch(() => []));
    } else {
      queries.push(Promise.resolve([]));
    }

    const [studentsSnap, classReviewsSnap, parentReviewsResult, questionsResult] = await Promise.all(queries);

    // Map student display names without exposing studentCode directly
    const studentsMap = new Map<string, string>();
    studentsSnap.docs.forEach((doc: any) => {
      const d = doc.data();
      if (d.status === 'inactive') return; // Exclude inactive students
      const sCode = d.studentCode || doc.id;
      const isAuto = d.autonomous === true || d.isAutonomous === true || d.mode === 'autonomous';
      const displayName = isAuto ? `# ${d.name || 'Student'}` : (d.name || 'Student');
      studentsMap.set(sCode, displayName);
    });

    // Map question text lookup
    const questionTextMap = new Map<string, string>();
    if (Array.isArray(questionsResult)) {
      questionsResult.forEach((snap: any) => {
        if (snap && snap.exists) {
          const q = snap.data();
          questionTextMap.set(snap.id, q.text || q.questionText || snap.id);
        }
      });
    }

    // Map classmate peer reviews for Saturday Classroom Test
    // Map key: `${studentCode}_${questionId}` -> awarded marks
    const peerMarksMap = new Map<string, number>();
    classReviewsSnap.docs.forEach((doc: any) => {
      const rev = doc.data();
      const sCode = rev.revieweeCode || rev.studentCode;
      if (!sCode || !Array.isArray(rev.questionReviews)) return;
      rev.questionReviews.forEach((qr: any) => {
        const qId = qr.questionId;
        if (qId && qr.marksAwarded !== undefined && qr.marksAwarded !== null) {
          peerMarksMap.set(`${sCode}_${qId}`, Number(qr.marksAwarded));
        }
      });
    });

    // Map parent reviews for daily home practices
    // Map key: `${studentCode}_${questionId}` -> parent marks
    const parentMarksMap = new Map<string, number>();
    const processParentReviewDoc = (doc: any) => {
      const rev = doc.data();
      const sCode = rev.revieweeCode || rev.studentCode;
      if (!sCode || !Array.isArray(rev.questionReviews)) return;
      rev.questionReviews.forEach((qr: any) => {
        const qId = qr.questionId;
        if (qId && qr.marksAwarded !== undefined && qr.marksAwarded !== null) {
          parentMarksMap.set(`${sCode}_${qId}`, Number(qr.marksAwarded));
        }
      });
    };

    if (homeExamIds.length > 0 && Array.isArray(parentReviewsResult)) {
      parentReviewsResult.forEach((snap: any) => {
        snap.docs.forEach((doc: any) => processParentReviewDoc(doc));
      });
    }

    // 4. Align and compute compared pairs
    const items: any[] = [];
    let totalMatched = 0;
    let alignedCount = 0;
    let parentHigherCount = 0;
    let peerHigherCount = 0;
    let totalParentOverestimatePoints = 0;

    // Loop through students
    studentsMap.forEach((studentName, studentCode) => {
      // Loop through Saturday classroom test questions
      classroomQuestionIds.forEach((qId: string) => {
        const peerKey = `${studentCode}_${qId}`;
        const parentKey = `${studentCode}_${qId}`;

        const hasPeer = peerMarksMap.has(peerKey);
        const hasParent = parentMarksMap.has(parentKey);

        // List only those questions for which BOTH parent and peer reviews are available (truth is available)
        if (hasPeer && hasParent) {
          totalMatched++;
          const peerMarks = peerMarksMap.get(peerKey)!;
          const parentMarks = parentMarksMap.get(parentKey)!;

          // Find max marks for the question
          const qSnap = questionsResult.find((s: any) => s && s.id === qId);
          const maxMarks = qSnap && qSnap.exists ? Number(qSnap.data().marks) || 2 : 2;

          const variance = parentMarks - peerMarks;
          const variancePercent = (variance / (maxMarks || 1)) * 100;

          let status: 'aligned' | 'parent_higher' | 'peer_higher' = 'aligned';
          if (Math.abs(variance) <= 0.5) {
            status = 'aligned';
            alignedCount++;
          } else if (variance > 0.5) {
            status = 'parent_higher';
            parentHigherCount++;
            totalParentOverestimatePoints += variance;
          } else {
            status = 'peer_higher';
            peerHigherCount++;
          }

          items.push({
            id: `${studentCode}_${qId}`,
            studentName,
            questionId: qId,
            questionText: questionTextMap.get(qId) || qId,
            parentMarks,
            peerMarks,
            maxMarks,
            variance: Math.round(variance * 10) / 10,
            variancePercent: Math.round(variancePercent),
            status
          });
        }
      });
    });

    const alignmentRate = totalMatched > 0 ? Math.round((alignedCount / totalMatched) * 100) : 100;
    const avgParentOverestimate = parentHigherCount > 0 ? Math.round((totalParentOverestimatePoints / parentHigherCount) * 10) / 10 : 0;

    const result = {
      metrics: {
        totalQuestionsAnalyzed: totalMatched,
        alignedCount,
        parentHigherCount,
        peerHigherCount,
        alignmentRate,
        avgParentOverestimate
      },
      items
    };

    await ReportCacheManager.setReport(cacheKey, result, 300); // Cache for 5 minutes

    return NextResponse.json(result);
  } catch (err: any) {
    console.error('Error fetching inline Truth Test Report:', err);
    return NextResponse.json({ message: err.message || 'Internal Server Error' }, { status: 500 });
  }
}
