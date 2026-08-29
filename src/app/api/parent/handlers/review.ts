import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { ReportCacheManager } from '@/lib/reportCache';
import { chunkArray } from '@/lib/firestoreUtils';
import { getDateKeyIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

async function resolveChildrenCodes(parentData: any): Promise<string[]> {
  const childrenCodes: string[] = [];
  if (Array.isArray(parentData?.studentCodes)) {
    childrenCodes.push(...parentData.studentCodes.filter(Boolean));
  } else if (parentData?.studentCode) {
    childrenCodes.push(parentData.studentCode);
  } else if (parentData?.studentId) {
    childrenCodes.push(parentData.studentId);
  }

  const parentEmail = parentData?.email?.toLowerCase();
  if (parentEmail) {
    try {
      const querySnap = await adminDb.collection('users')
        .where('role', '==', 'student')
        .where('parentEmail', '==', parentEmail)
        .get();
      querySnap.docs.forEach(doc => {
        const data = doc.data();
        if (data.studentCode && !childrenCodes.includes(data.studentCode)) {
          childrenCodes.push(data.studentCode);
        }
      });
    } catch (e) {
      console.warn('Error fetching children by email:', e);
    }
  }

  if (childrenCodes.length > 0) {
    const activeChildrenCodes: string[] = [];
    const chunks = chunkArray(childrenCodes, 30);
    const results = await Promise.all(chunks.map(chunk => 
      adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', 'in', chunk)
        .get()
    ));
    results.forEach(snap => {
      snap.docs.forEach(doc => {
        const data = doc.data();
        if (data.studentCode && data.role === 'student') {
          activeChildrenCodes.push(data.studentCode);
        }
      });
    });
    return activeChildrenCodes;
  }

  return childrenCodes;
}

// 1. GET - Load reviews for child student
export async function GET(req: NextRequest) {
  try {
    const parent = await verifyRole(req, 'parent').catch(() => null);
    const admin = !parent ? await verifyRole(req, 'admin').catch(() => null) : null;
    if (!parent && !admin) {
      return NextResponse.json({ message: 'Unauthorized. Parent or Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const attemptId = searchParams.get('attemptId');
    const studentCode = searchParams.get('studentCode') || '';

    if (attemptId) {
      const attemptSnap = await adminDb.collection('subjectiveAttempts').doc(attemptId).get();
      if (!attemptSnap.exists) {
        return NextResponse.json({ message: 'Attempt not found.' }, { status: 404 });
      }
      const attemptData = attemptSnap.data()!;
      
      if (parent) {
        const childrenCodes = await resolveChildrenCodes(parent.userData);
        if (!childrenCodes.includes(attemptData.studentCode)) {
          return NextResponse.json({ message: 'Access denied.' }, { status: 403 });
        }
      }

      const examSnap = await adminDb.collection('subjectiveExams').doc(attemptData.examId).get();
      const examData = examSnap.exists ? examSnap.data()! : {};

      let questions = attemptData.questionSnapshot || [];
      if (questions.length === 0) {
        const questionIds = attemptData.questionIds || examData.questionIds || [];
        if (questionIds.length > 0) {
          const refs = questionIds.map((qid: string) => adminDb.collection('questions').doc(qid));
          const snaps = await adminDb.getAll(...refs).catch(() => []);
          questions = snaps
            .filter((s: any) => !!s && s.exists)
            .map(s => ({ id: s.id, ...s.data() }));
        }
      }

      const reviewSnap = await adminDb.collection('subjectiveReviews')
        .where('attemptId', '==', attemptId)
        .limit(1)
        .get();
      const existingReview = !reviewSnap.empty ? reviewSnap.docs[0].data() : null;

      return NextResponse.json({
        attempt: { id: attemptSnap.id, ...attemptData },
        exam: { id: examSnap.id, ...examData },
        questions,
        existingReview
      });
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Missing studentCode parameter.' }, { status: 400 });
    }

    if (parent) {
      const childrenCodes = await resolveChildrenCodes(parent.userData);
      if (!childrenCodes.includes(studentCode)) {
        return NextResponse.json({ message: 'Access denied. Student is not mapped to parent.' }, { status: 403 });
      }
    }

    // Fetch student profile to see if they are autonomous
    const studentUserSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();
    
    const isAutonomous = !studentUserSnap.empty && studentUserSnap.docs[0].data()?.autonomous === true;

    // Fetch parent reviews info
    const [objSnaps, pracSnaps, subjSnaps, evalSnaps] = await Promise.all([
      // Objective Reviews
      adminDb.collection('reviews')
        .where('studentCode', '==', studentCode)
        .get(),
      // Practice Reviews (skipped for autonomous children)
      isAutonomous 
        ? Promise.resolve({ docs: [] })
        : adminDb.collection('parentReviews').where('studentCode', '==', studentCode).get(),
      // Subjective Reviews (skipped for autonomous children)
      isAutonomous 
        ? Promise.resolve({ docs: [] })
        : adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).get(),
      // Existing Parent Evaluations (source of truth for approvals)
      adminDb.collection('evaluations')
        .where('studentCode', '==', studentCode)
        .where('evaluatorType', '==', 'parent')
        .get()
    ]);

    // Map parent evaluations by attempt/legacy/exam id
    const evalMap = new Map<string, any>();
    evalSnaps.docs.forEach(doc => {
      const data = doc.data();
      if (data.attemptId) evalMap.set(data.attemptId, data);
      if (data.legacyId) evalMap.set(data.legacyId, data);
      if (data.examId) evalMap.set(data.examId, data);
      if (doc.id) evalMap.set(doc.id, data);
    });

    const subjectiveExamsIds = Array.from(new Set(subjSnaps.docs.map(doc => doc.data().examId).filter(Boolean)));
    const examRefs = subjectiveExamsIds.map(id => adminDb.collection('subjectiveExams').doc(id));
    const examSnaps = examRefs.length > 0 ? await adminDb.getAll(...examRefs).catch(() => []) : [];

    const examsMap = new Map<string, any>();
    examSnaps.forEach(snap => {
      if (snap && snap.exists) examsMap.set(snap.id, snap.data());
    });

    // Gather all unique topic codes across objective reviews, practice reviews, and subjective exams
    const allTopicCodes = new Set<string>();

    // Topic codes from practice reviews
    pracSnaps.docs.forEach(doc => {
      const tc = doc.data().topicCode;
      if (tc) allTopicCodes.add(tc);
    });

    // Topic codes from objective reviews (derived from questionCodes / questionDetails)
    objSnaps.docs.forEach(doc => {
      const data = doc.data();
      if (data.examType === 'practice') return;
      const qCodes = data.questionCodes || [];
      const qDetails = data.questionDetails || [];
      const uniqueCodes = Array.from(new Set<string>([
        ...qCodes,
        ...qDetails.map((qd: any) => qd.questionCode).filter(Boolean)
      ]));
      uniqueCodes.forEach(code => {
        const tCode = deriveTopicCodeFromQuestionCode(code);
        if (tCode) allTopicCodes.add(tCode);
      });
    });

    // Topic codes from subjective exams
    examsMap.forEach((examData: any) => {
      const codes = examData.topicCodes || [];
      codes.forEach((c: string) => {
        if (c) allTopicCodes.add(c);
      });
    });

    // Batch query syllabusTopicIndex for all resolved topic codes
    const syllabusMap = new Map<string, any>();
    const uniqueTopicCodes = Array.from(allTopicCodes);
    if (uniqueTopicCodes.length > 0) {
      const chunks = chunkArray(uniqueTopicCodes, 30);
      const snaps = await Promise.all(
        chunks.map(chunk =>
          adminDb.collection('syllabusTopicIndex')
            .where('topicCode', 'in', chunk)
            .get()
        )
      );
      snaps.forEach(syllabusSnap => {
        syllabusSnap.docs.forEach(doc => {
          const d = doc.data();
          if (d.topicCode) {
            syllabusMap.set(d.topicCode, d);
          }
        });
      });
    }

    // 1. Map Objective reviews
    const allObjectiveMapped = objSnaps.docs
      .map(doc => {
        const data = doc.data();
        // Skip practice sessions stored in reviews collection
        if (data.examType === 'practice') return null;

        let topicName = '';
        const examTopics = new Set<string>();
        const qCodes = data.questionCodes || [];
        const qDetails = data.questionDetails || [];
        const uniqueCodes = Array.from(new Set<string>([
          ...qCodes,
          ...qDetails.map((qd: any) => qd.questionCode).filter(Boolean)
        ]));
        uniqueCodes.forEach(code => {
          const tCode = deriveTopicCodeFromQuestionCode(code);
          if (tCode) {
            const sData = syllabusMap.get(tCode);
            if (sData && sData.topicName) examTopics.add(sData.topicName);
          }
        });
        if (examTopics.size > 0) {
          topicName = Array.from(examTopics).join(', ');
        }

        const isReviewed = data.status === 'approved' || 
                           data.parentStatus === 'approved' || 
                           evalMap.has(doc.id) || 
                           (data.examId && evalMap.has(data.examId)) || 
                           (data.examCode && evalMap.has(data.examCode)) ||
                           (data.examId && evalMap.has(`${data.examId}_${studentCode}`));
        const resolvedActor = data.reviewedByActor || evalMap.get(doc.id)?.reviewedByActor || (isReviewed ? 'parent' : null);
        return {
          id: doc.id,
          type: 'objective',
          examType: data.examType || 'objective',
          name: topicName || data.examName || data.examCode || 'Objective Exam',
          subject: data.subjectName || data.subject || 'General',
          chapter: data.chapterName || data.chapter || '-',
          date: data.completedAt?.toDate ? data.completedAt.toDate().toISOString() : data.completedAt || data.submittedAt?.toDate ? data.submittedAt.toDate().toISOString() : data.submittedAt || null,
          startedAt: data.startedAt?.toDate ? data.startedAt.toDate().toISOString() : data.startedAt || null,
          completedAt: data.completedAt?.toDate ? data.completedAt.toDate().toISOString() : data.completedAt || null,
          score: data.score || 0,
          totalMarks: data.totalMarks || data.totalQuestions || 0,
          percentage: data.percentage || 0,
          tabViolations: data.tabViolations || 0,
          proctoringViolations: data.proctoringViolations || data.violations || {},
          status: isReviewed ? 'approved' : 'pending',
          reviewedByActor: resolvedActor,
          proctoringViolationTriggered: data.proctoringViolationTriggered || false,
          wrongAnswers: data.wrongAnswers || [],
          unattemptedQuestions: data.unattemptedQuestions || [],
          wrongAnswerReasons: data.wrongAnswerReasons || {}
        };
      })
      .filter(Boolean) as any[];

    const objectiveReviews = allObjectiveMapped.filter(r => r.examType !== 'entrance');
    const entranceReviews = allObjectiveMapped.filter(r => r.examType === 'entrance');

    // 2. Map Practice reviews
    const mappedPracticeReviews = pracSnaps.docs.map(doc => {
      const data = doc.data();
      const status = data.parentStatus || (evalMap.has(doc.id) ? 'approved' : 'pending');
      const resolvedActor = data.reviewedByActor || evalMap.get(doc.id)?.reviewedByActor || (status === 'approved' ? 'parent' : null);
      
      const sData = syllabusMap.get(data.topicCode || '');
      let displayName = data.topicName || 'Practice Set';
      if (!displayName || displayName === data.topicCode) {
        displayName = sData?.topicName || displayName;
      }
      let displaySubject = data.subjectName || 'General';
      if (!displaySubject || displaySubject === 'General') {
        displaySubject = sData?.subjectName || displaySubject;
      }
      let displayChapter = data.chapterName || 'General';
      if (!displayChapter || displayChapter === 'General') {
        displayChapter = sData?.chapterName || displayChapter;
      }

      const start = data.startedAt?.toDate ? data.startedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null);
      const end = data.createdAt?.toDate ? data.createdAt.toDate() : (data.updatedAt?.toDate ? data.updatedAt.toDate() : null);
      const rawTimestamp = start ? start.getTime() : (end ? end.getTime() : 0);

      return {
        id: doc.id,
        type: 'practice',
        name: displayName,
        topicCode: data.topicCode || null,
        subject: displaySubject,
        chapter: displayChapter,
        date: data.startedAt?.toDate ? data.startedAt.toDate().toISOString() : data.createdAt?.toDate ? data.createdAt.toDate().toISOString() : data.startedAt || null,
        rawTimestamp,
        scorePercent: data.scorePercent || 0,
        correctCount: data.correctCount || 0,
        totalQuestions: data.totalQuestions || 1,
        masteryBefore: data.masteryBefore || 0,
        masteryAfter: data.masteryAfter || 0,
        masteryChange: data.masteryChange || 0,
        strengths: data.strengths || [],
        needsAttention: data.needsAttention || [],
        suspiciousLevel: data.suspiciousLevel || 'none',
        status,
        reviewedByActor: resolvedActor,
        proctoringViolationTriggered: data.proctoringViolationTriggered || false
      };
    });

    // Sort chronologically (oldest first) to compute stable sequential numbers
    const chronologicalPrac = [...mappedPracticeReviews].sort((a, b) => a.rawTimestamp - b.rawTimestamp);
    const pracSequenceMap = new Map<string, number>();
    const pracTopicCounts = new Map<string, number>();

    chronologicalPrac.forEach(r => {
      const tCode = r.topicCode || 'unknown';
      const nextSeq = (pracTopicCounts.get(tCode) || 0) + 1;
      pracTopicCounts.set(tCode, nextSeq);
      pracSequenceMap.set(r.id, nextSeq);
    });

    const practiceReviews = mappedPracticeReviews.map(r => {
      const seqNum = pracSequenceMap.get(r.id) || 1;
      return {
        ...r,
        name: `${r.name} #${seqNum}`
      };
    });

    // 3. Map Subjective reviews
    const subjectiveReviews = subjSnaps.docs.map(doc => {
      const data = doc.data();
      const exam = examsMap.get(data.examId) || {};
      const isReviewed = data.status === 'approved' || 
                         data.parentStatus === 'approved' || 
                         evalMap.has(doc.id) || 
                         (data.examId && evalMap.has(data.examId)) || 
                         (data.examId && evalMap.has(`${data.examId}_${studentCode}`));
      const resolvedActor = data.reviewedByActor || evalMap.get(doc.id)?.reviewedByActor || (isReviewed ? 'parent' : null);

      let topicName = '';
      const examTopics = new Set<string>();
      const codes = exam.topicCodes || [];
      codes.forEach((c: string) => {
        if (c) {
          const sData = syllabusMap.get(c);
          if (sData && sData.topicName) examTopics.add(sData.topicName);
        }
      });
      if (examTopics.size > 0) {
        topicName = Array.from(examTopics).join(', ');
      }

      return {
        id: doc.id,
        attemptId: doc.id,
        examId: data.examId,
        type: 'subjective',
        name: topicName || exam.name || 'Subjective Exam',
        subject: exam.subjects?.[0] || exam.subjectName || 'General',
        chapter: exam.chapter || exam.chapterName || '-',
        date: data.completedAt?.toDate ? data.completedAt.toDate().toISOString() : data.createdAt?.toDate ? data.createdAt.toDate().toISOString() : null,
        startedAt: data.startedAt?.toDate ? data.startedAt.toDate().toISOString() : null,
        completedAt: data.completedAt?.toDate ? data.completedAt.toDate().toISOString() : null,
        tabViolations: data.tabViolations || 0,
        noFaceCount: data.noFaceCount || 0,
        multipleFacesCount: data.multipleFacesCount || 0,
        awayTimeTotal: data.awayTimeTotal || 0,
        timeSpentSeconds: data.timeSpentSeconds || 0,
        mode: data.mode || 'home',
        status: isReviewed ? 'approved' : 'pending',
        reviewedByActor: resolvedActor,
        proctoringViolationTriggered: data.proctoringViolationTriggered || false
      };
    });

    return NextResponse.json({
      objectiveReviews,
      practiceReviews,
      subjectiveReviews,
      entranceReviews,
      isAutonomousChild: isAutonomous
    });

  } catch (error: any) {
    console.error('API parent get reviews error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Approve review
export async function POST(req: NextRequest) {
  try {
    const parent = await verifyRole(req, 'parent');
    if (!parent) {
      return NextResponse.json({ message: 'Unauthorized. Parent role required.' }, { status: 403 });
    }

    const parentEmail = parent.userData?.email || 'parent@yashcom.com';
    const parentReviewerCode = parent.userData?.reviewerCode || 'PARENT_REV';

    const body = await req.json();
    const { reviewId, type, childStudentCode, reviewedByActor, reviewIds, photoThumbnail } = body;

    const isBulk = type === 'bulk_practice';
    if ((isBulk ? (!reviewIds || !Array.isArray(reviewIds)) : !reviewId) || !type || !childStudentCode) {
      return NextResponse.json({ message: 'Missing parameters (reviewId or reviewIds, type, childStudentCode).' }, { status: 400 });
    }

    const actor = reviewedByActor === 'student' ? 'student' : 'parent';
    const expiresAt = actor === 'parent' && photoThumbnail ? (Date.now() + 24 * 60 * 60 * 1000) : null;

    // Verify access
    const childrenCodes = await resolveChildrenCodes(parent.userData);
    if (!childrenCodes.includes(childStudentCode)) {
      return NextResponse.json({ message: 'Access denied to this student review.' }, { status: 403 });
    }

    // Fetch child user details using queries since user docs are keyed by uid
    const studentQuerySnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', childStudentCode)
      .limit(1)
      .get()
      .catch(() => null);
    const childName = studentQuerySnap && !studentQuerySnap.empty
      ? (studentQuerySnap.docs[0].data()?.name || childStudentCode)
      : childStudentCode;

    let success = false;

    if (type === 'objective') {
      const reviewRef = adminDb.collection('reviews').doc(reviewId);
      const snap = await reviewRef.get();
      if (!snap.exists) {
        return NextResponse.json({ message: 'Objective review doc not found.' }, { status: 404 });
      }
      const rData = snap.data()!;

      // IDOR Protection: Verify review belongs to childStudentCode
      if (rData.studentCode !== childStudentCode) {
        return NextResponse.json({ message: 'Access Denied. Review document does not match this child.' }, { status: 403 });
      }

      if (rData.status === 'approved') {
        return NextResponse.json({ success: true, message: 'Review successfully approved!' });
      }

      // 1. Update review status across both reviews and examAttempts collections
      const approvalUpdates = {
        status: 'approved',
        reviewedAt: new Date(),
        reviewedBy: parentEmail,
        reviewedByActor: actor
      };

      await reviewRef.update(approvalUpdates).catch(() => null);
      await adminDb.collection('examAttempts').doc(reviewId).update(approvalUpdates).catch(() => null);

      if (rData.examId && childStudentCode) {
        const altId = `${rData.examId}_${childStudentCode}`;
        await adminDb.collection('reviews').doc(altId).update(approvalUpdates).catch(() => null);
        await adminDb.collection('examAttempts').doc(altId).update(approvalUpdates).catch(() => null);
      }

      // 2. Create parent evaluation record
      const evaluationData = {
        studentCode: childStudentCode,
        studentName: childName,
        questionId: null,
        evaluatorType: 'parent',
        evaluatorId: parentReviewerCode,
        evaluatorName: parentEmail,
        marksAwarded: rData.score || 0,
        maxMarks: rData.totalMarks || rData.totalQuestions || 0,
        feedback: `Objective review approved by parent`,
        rubricUsed: null,
        modelAnswerVersion: 'objective',
        examId: rData.examData?.id || null,
        attemptId: null,
        createdAt: new Date(),
        updatedAt: new Date(),
        source: 'objective_review_approval',
        legacyId: reviewId,
        reviewedByActor: actor
      };

      await adminDb.collection('evaluations').add(evaluationData);
      
      const targetExamId = rData.examId || rData.examData?.id;
      if (targetExamId) {
        await ReportCacheManager.invalidateReport(`exam-report-objective-${targetExamId}`).catch(() => null);
        await ReportCacheManager.invalidateReport(`exam-report-subjective-${targetExamId}`).catch(() => null);
        await ReportCacheManager.invalidateReport(`truth-test-report-${targetExamId}`).catch(() => null);
      }

      success = true;

    } else if (type === 'practice') {
      const reviewRef = adminDb.collection('parentReviews').doc(reviewId);
      const snap = await reviewRef.get();
      if (!snap.exists) {
        return NextResponse.json({ message: 'Practice review doc not found.' }, { status: 404 });
      }
      const rData = snap.data()!;

      // IDOR Protection: Verify review belongs to childStudentCode
      if (rData.studentCode !== childStudentCode) {
        return NextResponse.json({ message: 'Access Denied. Review document does not match this child.' }, { status: 403 });
      }

      if (rData.parentStatus === 'approved') {
        return NextResponse.json({ success: true, message: 'Review successfully approved!' });
      }

      // 1. Update review parentStatus
      await reviewRef.update({
        parentStatus: 'approved',
        reviewedAt: new Date(),
        reviewedBy: parentEmail,
        reviewedByActor: actor
      });

      // 2. Create evaluation
      const evaluationData = {
        studentCode: childStudentCode,
        studentName: childName,
        questionId: null,
        evaluatorType: 'parent',
        evaluatorId: parentReviewerCode,
        evaluatorName: parentEmail,
        marksAwarded: rData.scorePercent || 0,
        maxMarks: 100,
        feedback: `Practice review approved by parent: ${rData.strengths?.join(', ') || ''} | Needs attention: ${rData.needsAttention?.join(', ') || ''}`,
        rubricUsed: null,
        modelAnswerVersion: 'practice',
        examId: null,
        attemptId: reviewId,
        createdAt: new Date(),
        updatedAt: new Date(),
        source: 'practice_review_approval',
        legacyId: reviewId,
        reviewedByActor: actor
      };

      await adminDb.collection('evaluations').add(evaluationData);
      success = true;

    } else if (type === 'bulk_practice') {
      const { reviewIds } = body;
      if (!Array.isArray(reviewIds) || reviewIds.length === 0) {
        return NextResponse.json({ message: 'Missing or empty reviewIds list.' }, { status: 400 });
      }
      
      const refs = reviewIds.map(rId => adminDb.collection('parentReviews').doc(rId));
      const snaps = await adminDb.getAll(...refs).catch(() => []);

      const batch = adminDb.batch();
      for (const snap of snaps) {
        if (snap && snap.exists) {
          const ref = snap.ref;
          const rId = snap.id;
          const rData = snap.data()!;
          if (rData.studentCode === childStudentCode && rData.parentStatus !== 'approved') {
            batch.update(ref, {
              parentStatus: 'approved',
              reviewedAt: new Date(),
              reviewedBy: parentEmail,
              reviewedByActor: actor
            });
            
            // Create evaluation
            const evalRef = adminDb.collection('evaluations').doc();
            batch.set(evalRef, {
              studentCode: childStudentCode,
              studentName: childName,
              questionId: null,
              evaluatorType: 'parent',
              evaluatorId: parentReviewerCode,
              evaluatorName: parentEmail,
              marksAwarded: rData.scorePercent || 0,
              maxMarks: 100,
              feedback: `Bulk practice review approved by parent`,
              rubricUsed: null,
              modelAnswerVersion: 'practice',
              examId: null,
              attemptId: rId,
              createdAt: new Date(),
              updatedAt: new Date(),
              source: 'practice_review_approval',
              legacyId: rId,
              reviewedByActor: actor
            });
          }
        }
      }
      await batch.commit();
      success = true;

    } else if (type === 'subjective') {
      const { questionReviews, totalScore } = body;
      if (!questionReviews || totalScore === undefined) {
        return NextResponse.json({ message: 'Missing parameters (questionReviews, totalScore).' }, { status: 400 });
      }

      const attemptRef = adminDb.collection('subjectiveAttempts').doc(reviewId);
      const snap = await attemptRef.get();
      if (!snap.exists) {
        return NextResponse.json({ message: 'Subjective attempt doc not found.' }, { status: 404 });
      }
      const aData = snap.data()!;

      // IDOR Protection: Verify attempt belongs to childStudentCode
      if (aData.studentCode !== childStudentCode) {
        return NextResponse.json({ message: 'Access Denied. Attempt document does not match this child.' }, { status: 403 });
      }

      const batch = adminDb.batch();

      for (const qr of questionReviews) {
        const evalRef = adminDb.collection('evaluations').doc();
        const evalData = {
          studentCode: childStudentCode,
          studentName: childName,
          questionId: qr.questionId,
          evaluatorType: 'parent',
          evaluatorId: parentReviewerCode,
          evaluatorName: parentEmail,
          marksAwarded: Number(qr.marksAwarded) || 0,
          maxMarks: Number(qr.maxMarks) || 0,
          feedback: qr.feedback || '',
          rubricUsed: qr.questionId,
          modelAnswerVersion: 'model_v1.0',
          examId: aData.examId || null,
          attemptId: reviewId,
          createdAt: new Date(),
          updatedAt: new Date(),
          source: 'parent_subjective_review',
          reviewedByActor: actor
        };
        batch.set(evalRef, evalData);
      }

      // Save to subjectiveReviews collection
      const reviewDocRef = adminDb.collection('subjectiveReviews').doc();
      const reviewDocData = {
        attemptId: reviewId,
        examId: aData.examId || null,
        reviewerId: parentEmail,
        reviewerType: 'parent',
        revieweeCode: childStudentCode,
        questionReviews: questionReviews,
        totalScore: Number(totalScore) || 0,
        isFinal: true,
        submittedAt: new Date(),
        createdAt: new Date(),
        reviewedByActor: actor
      };
      batch.set(reviewDocRef, reviewDocData);

      // Update attempt document
      batch.update(attemptRef, {
        status: 'approved',
        parentReviewedAt: new Date(),
        parentScore: Number(totalScore) || 0,
        reviewedBy: parentEmail,
        reviewedByActor: actor
      });

      await batch.commit();

      if (aData.examId) {
        await ReportCacheManager.invalidateReport(`exam-report-objective-${aData.examId}`).catch(() => null);
        await ReportCacheManager.invalidateReport(`exam-report-subjective-${aData.examId}`).catch(() => null);
        await ReportCacheManager.invalidateReport(`truth-test-report-${aData.examId}`).catch(() => null);
      }

      success = true;
    } else if (type === 'daily_5min_sync') {
      const syncDocId = reviewId || `sync-${childStudentCode}-${Date.now()}`;
      const reviewDocRef = adminDb.collection('parentReviews').doc(syncDocId);
      const syncData = {
        id: syncDocId,
        type: 'daily_5min_sync',
        childStudentCode,
        studentCode: childStudentCode,
        studentName: childName,
        parentEmail,
        reviewedBy: parentEmail,
        reviewedByActor: actor,
        feedback: body.feedback || 'Daily 5-Min Parent-Child Sync Completed',
        photoThumbnail: body.photoThumbnail || photoThumbnail || null,
        parentStatus: 'approved',
        status: 'completed',
        reviewedAt: new Date(),
        createdAt: new Date(),
        date: getDateKeyIST()
      };

      await reviewDocRef.set(syncData, { merge: true });
      success = true;
    }

    if (success) {
      // Invalidate parent pending / sincerity report caches
      await ReportCacheManager.invalidateReport('parent-pending-report').catch(() => null);
      await ReportCacheManager.invalidateReport('parent-sincerity-report').catch(() => null);

      // Write parent sincerity log
      const sincerityLog = {
        reviewId: reviewId || (Array.isArray(reviewIds) ? reviewIds.join(',') : 'bulk'),
        type,
        studentCode: childStudentCode,
        studentName: childName,
        reviewedByActor: actor,
        reviewedByEmail: parentEmail,
        photoThumbnail: actor === 'parent' ? (photoThumbnail || null) : null,
        expiresAt: actor === 'parent' && photoThumbnail ? expiresAt : null,
        photoPurged: false,
        timestamp: new Date().toISOString(),
        createdAt: new Date()
      };

      await adminDb.collection('parentSincerityLogs').add(sincerityLog).catch(err => {
        console.warn('Failed to log parent sincerity record:', err);
      });
    }

    return NextResponse.json({ success, message: 'Review successfully approved!' });

  } catch (error: any) {
    console.error('API parent approve error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
