import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
export const dynamic = 'force-dynamic';

function cleanSubjectiveExamName(examData: any) {
  if (!examData) return '';
  const name = examData.name || '';
  if (!name.includes('—')) return name;

  const parts = name.split('—');
  const prefix = parts[0].trim(); // e.g. "Monday Home Practice"
  const suffix = parts[1].trim(); // e.g. "Gravitation, Periodic Classification of Elements, ..."

  if (suffix.includes(',') && examData.chapterName && examData.chapterNumber) {
    const allChapters = String(examData.chapterName).split(',').map((c: string) => c.trim());
    const chNums = String(examData.chapterNumber).split(',').map((c: string) => parseInt(c.trim())).filter(num => !isNaN(num));
    
    const activeChapters = chNums.map(num => allChapters[num - 1]).filter(Boolean);
    if (activeChapters.length > 0) {
      return `${prefix} — ${activeChapters.join(', ')}`;
    }
  }
  return name;
}

async function getAttemptQuestions(attempt: any, exam: any): Promise<any[]> {
  if (attempt && Array.isArray(attempt.questionSnapshot) && attempt.questionSnapshot.length > 0) {
    return attempt.questionSnapshot;
  }
  
  let candidateIds: string[] = [];
  if (Array.isArray(attempt?.questionIds) && attempt.questionIds.length > 0) {
    candidateIds.push(...attempt.questionIds);
  }
  if (Array.isArray(exam?.questionIds) && exam.questionIds.length > 0) {
    candidateIds.push(...exam.questionIds);
  }
  if (Array.isArray(exam?.questionCodes) && exam.questionCodes.length > 0) {
    candidateIds.push(...exam.questionCodes);
  }
  if (Array.isArray(exam?.questions) && exam.questions.length > 0) {
    exam.questions.forEach((q: any) => {
      if (typeof q === 'string') candidateIds.push(q);
      else if (q && typeof q === 'object') {
        if (q.id) candidateIds.push(q.id);
        if (q.questionCode) candidateIds.push(q.questionCode);
      }
    });
  }

  const questionIds = Array.from(new Set(candidateIds.filter(Boolean)));
  if (questionIds.length === 0) return [];
  
  const lookupIds = new Set<string>();
  questionIds.forEach(id => {
    lookupIds.add(id);
    const normalized = id.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
    lookupIds.add(normalized);
  });

  const refs = Array.from(lookupIds).map((qid: string) => adminDb.collection('questions').doc(qid));
  const snaps = await adminDb.getAll(...refs).catch(() => []);
  
  const questionMap = new Map<string, any>();
  snaps.forEach((s: any) => {
    if (s && s.exists) {
      const data = s.data();
      const docId = s.id;
      const qCode = data.questionCode || docId;
      const fullQ = { id: docId, ...data };
      questionMap.set(docId, fullQ);
      questionMap.set(qCode, fullQ);
      if (qCode.includes('-MGP1-')) questionMap.set(qCode.replace('-MGP1-', '-GANI-'), fullQ);
      if (qCode.includes('-CURI-')) questionMap.set(qCode.replace('-CURI-', '-SCIE-'), fullQ);
    }
  });

  if (Array.isArray(exam?.questions) && exam.questions.length > 0) {
    exam.questions.forEach((q: any) => {
      if (q && typeof q === 'object' && (q.text || q.questionText)) {
        const qKey = q.id || q.questionCode;
        if (qKey && !questionMap.has(qKey)) {
          questionMap.set(qKey, q);
        }
      }
    });
  }

  const result: any[] = [];
  const added = new Set<string>();
  questionIds.forEach(id => {
    const q = questionMap.get(id) || questionMap.get(id.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-'));
    if (q && !added.has(q.id || q.questionCode)) {
      result.push(q);
      added.add(q.id || q.questionCode);
    }
  });

  return result.length > 0 ? result : Array.from(questionMap.values());
}

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }
    if (student.userData?.autonomous === true) {
      return NextResponse.json({ message: 'Access Denied. Subjective exams are restricted for this student account.' }, { status: 403 });
    }
    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('examId') || '';
    const mode = searchParams.get('mode') || 'home';
    const studentCode = student.userData?.studentCode;

    if (!examId || !studentCode) {
      return NextResponse.json({ message: 'Missing parameters (examId, studentCode).' }, { status: 400 });
    }

    // A. Peer Review Mode
    if (mode === 'peer-review') {
      const myAttemptsSnap = await adminDb.collection('subjectiveAttempts')
        .where('examId', '==', examId)
        .where('studentCode', '==', studentCode)
        .get();

      if (myAttemptsSnap.empty) {
        return NextResponse.json({ message: 'No peer review assignment found.' }, { status: 404 });
      }

      const myAttempt = myAttemptsSnap.docs[0].data();
      const myAttemptId = myAttemptsSnap.docs[0].id;

      // Verify the assignment status from peerAssignments
      const peerAssignsSnap = await adminDb.collection('peerAssignments')
        .where('examId', '==', examId)
        .where('reviewerStudentCode', '==', studentCode)
        .get();

      if (peerAssignsSnap.empty) {
        return NextResponse.json({ status: 'not_ready', message: 'Peer review is not ready yet.' });
      }

      const assignment = peerAssignsSnap.docs[0].data();
      if (assignment.status === 'completed') {
        return NextResponse.json({ status: 'already_reviewed', message: 'Peer review already submitted.' });
      }

      const revieweeCode = assignment.revieweeStudentCode;
      if (!revieweeCode) {
        return NextResponse.json({ message: 'Review assignment missing.' }, { status: 400 });
      }

      const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
      if (!examSnap.exists) {
        return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
      }
      const examData = examSnap.data()!;

      const revieweeAttemptsSnap = await adminDb.collection('subjectiveAttempts')
        .where('examId', '==', examId)
        .where('studentCode', '==', revieweeCode)
        .get();

      if (revieweeAttemptsSnap.empty) {
        return NextResponse.json({ message: 'Classmate attempt not found.' }, { status: 404 });
      }
      const revieweeAttempt = revieweeAttemptsSnap.docs[0].data();

      // Retrieve full questions (solutions/steps needed for grading)
      const questions = await getAttemptQuestions(revieweeAttempt, examData);

      // Fetch reviewee classmate name
      let revieweeName = 'Classmate';
      try {
        const revieweeUserSnap = await adminDb.collection('users')
          .where('studentCode', '==', revieweeCode)
          .limit(1)
          .get();
        if (!revieweeUserSnap.empty) {
          revieweeName = revieweeUserSnap.docs[0].data().name || 'Classmate';
        }
      } catch (err) {
        console.warn('Failed to resolve reviewee name:', err);
      }

      return NextResponse.json({
        mode,
        examData: { id: examSnap.id, ...examData, name: cleanSubjectiveExamName(examData) },
        questions,
        myAttempt: { id: myAttemptId, ...myAttempt, peerRevieweeCode: revieweeCode },
        revieweeCode,
        revieweeName,
        status: 'ready'
      });
    }

    // B. Standard Exam Taking Mode
    const [pendingObj, pendingSub] = await Promise.all([
      adminDb.collection('reviews')
        .where('studentCode', '==', studentCode)
        .where('status', '==', 'student_review')
        .limit(1)
        .get(),
      adminDb.collection('peerAssignments')
        .where('reviewerStudentCode', '==', studentCode)
        .where('status', '==', 'pending')
        .limit(1)
        .get()
    ]);

    if (!pendingObj.empty || !pendingSub.empty) {
      return NextResponse.json({
        status: 'blocked',
        message: 'You have pending exam reviews (either an objective exam self-reflection or a classmate peer-grading assignment) that need your attention. Please complete all pending reviews before starting your next exam.'
      });
    }

    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }
    const examData = examSnap.data()!;

    // Validate if student is assigned to this subjective exam
    const studentBatchIds = student.userData?.batchIds || [];
    const assignmentQuery = await adminDb.collection('subjectiveAssignments')
      .where('examId', '==', examId)
      .where('status', '==', 'active')
      .get();

    let isAssigned = assignmentQuery.docs.some(doc => {
      const data = doc.data();
      const targetType = data.targetType;
      if (targetType === 'student') {
        return Array.isArray(data.targetStudents) && data.targetStudents.includes(studentCode);
      } else {
        return Array.isArray(data.targetBatches) && data.targetBatches.some((b: string) => studentBatchIds.includes(b));
      }
    });

    if (!isAssigned && examData.type === 'home_practice') {
      const matchBatch = !examData.batchId || studentBatchIds.includes(examData.batchId);
      if (matchBatch) {
        isAssigned = true;
      }
    }

    if (!isAssigned) {
      return NextResponse.json({ message: 'Access Denied: You are not assigned to take this exam.' }, { status: 403 });
    }

    // Check attempt limits
    const rawLimit = examData.attemptLimit;
    const attemptLimit = (rawLimit === -1 || rawLimit === '-1') ? Infinity : (Number(rawLimit) || 1);

    const attemptDocsSnap = await adminDb.collection('subjectiveAttempts')
      .where('examId', '==', examId)
      .where('studentCode', '==', studentCode)
      .get();

    const attemptsList = attemptDocsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() } as any));

    const finishedStatuses = ['completed', 'peer_review_pending', 'peer_reviewed', 'parent_reviewed', 'approved'];
    const finishedAttempt = attemptsList.find(a => finishedStatuses.includes(a.status || ''));
    const precheckAttempt = attemptsList.find(a => a.status === 'precheck');
    const inProgressAttempt = attemptsList.find(a => a.status === 'in-progress');
    const finishedCount = attemptsList.filter(a => finishedStatuses.includes(a.status || '')).length;

    if (finishedAttempt && finishedCount >= attemptLimit) {
      return NextResponse.json({
        status: 'blocked',
        finishedAttempt,
        message: 'Exam already submitted. Re-attempt is not allowed.'
      });
    }

    let remainingSeconds = 0;
    let startedAt = new Date().toISOString();
    let finalAttemptId = '';

    if (inProgressAttempt) {
      const startedAtDate = inProgressAttempt.startedAt ? (inProgressAttempt.startedAt.toDate ? inProgressAttempt.startedAt.toDate() : new Date(inProgressAttempt.startedAt)) : new Date();
      const elapsedMs = Date.now() - startedAtDate.getTime();
      const totalTime = Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60;
      const maxBufferMs = (totalTime + 5) * 60 * 1000;
      
      const refreshCount = inProgressAttempt.refreshCount || 0;
      
      if (elapsedMs < maxBufferMs && refreshCount < 3) {
        finalAttemptId = inProgressAttempt.id;
        remainingSeconds = Math.max(0, Math.floor((maxBufferMs - elapsedMs) / 1000));
        startedAt = startedAtDate.toISOString();
        
        await adminDb.collection('subjectiveAttempts').doc(inProgressAttempt.id).update({
          refreshCount: admin.firestore.FieldValue.increment(1)
        });
      } else {
        await adminDb.collection('subjectiveAttempts').doc(inProgressAttempt.id).update({
          status: 'completed',
          completedAt: new Date(),
          abandoned: true
        });
        
        const blockReason = refreshCount >= 3 
          ? 'Re-entry denied. You have exceeded the maximum of 3 page refreshes allowed during this exam.'
          : 'Re-entry denied. Your exam session duration has expired.';
          
        return NextResponse.json({
          status: 'blocked',
          message: blockReason
        });
      }
    } else if (precheckAttempt) {
      const totalTime = Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60;
      finalAttemptId = precheckAttempt.id;
      remainingSeconds = totalTime * 60;
      startedAt = precheckAttempt.startedAt ? (precheckAttempt.startedAt.toDate ? precheckAttempt.startedAt.toDate().toISOString() : new Date(precheckAttempt.startedAt).toISOString()) : new Date().toISOString();
    } else {
      const totalTime = Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60;
      const startedAtDate = new Date();
      const endsAtDate = new Date(startedAtDate.getTime() + totalTime * 60 * 1000);

      const newAttempt = {
        examId: examId,
        examName: cleanSubjectiveExamName(examData) || examData.name || 'Subjective Exam',
        studentCode: studentCode,
        studentId: student.decodedToken.uid,
        studentName: student.userData?.name || 'Student',
        status: 'precheck',
        mode: examData.mode || mode,
        questionIds: examData.questionIds || [],
        totalMarks: examData.totalMarks || 0,
        startedAt: startedAtDate,
        endsAt: endsAtDate,
        createdAt: new Date()
      };

      const docRef = await adminDb.collection('subjectiveAttempts').add(newAttempt);
      finalAttemptId = docRef.id;
      remainingSeconds = totalTime * 60;
      startedAt = startedAtDate.toISOString();
    }

    if (remainingSeconds <= 0) {
      // Auto-submit if time is already up
      await adminDb.collection('subjectiveAttempts').doc(finalAttemptId).update({
        status: 'completed',
        completedAt: new Date()
      });
      return NextResponse.json({
        status: 'blocked',
        message: 'Time limit reached. Attempt auto-submitted.'
      });
    }

    // Retrieve questions and strip solution details for security
    const rawQuestions = await getAttemptQuestions(inProgressAttempt, examData);
    const questions = rawQuestions.map(q => {
      // Clean solution, answerLines, and steps
      const { solution, answerLines, steps, ...safeQuestion } = q;
      return safeQuestion;
    });

    return NextResponse.json({
      status: 'active',
      mode,
      examData: { id: examSnap.id, ...examData, name: cleanSubjectiveExamName(examData) },
      questions,
      attemptId: finalAttemptId,
      remainingSeconds,
      startedAt
    });

  } catch (error: any) {
    console.error('API subjective load error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Submit subjective exam
export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, attemptId } = body;
    const studentCode = student.userData?.studentCode;

    if (action === 'start') {
      if (!attemptId || !studentCode) {
        return NextResponse.json({ message: 'Missing parameters (attemptId, studentCode).' }, { status: 400 });
      }
      const attemptRef = adminDb.collection('subjectiveAttempts').doc(attemptId);
      await attemptRef.update({
        status: 'in-progress',
        startedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      return NextResponse.json({ success: true, message: 'Subjective exam started successfully.' });
    }

    const { tabViolations, noFaceCount, multipleFacesCount, awayTimeTotal, timeSpentSeconds, proctoringViolationTriggered, micBypassed, violations } = body;

    if (!attemptId || !studentCode) {
      return NextResponse.json({ message: 'Missing parameters (attemptId, studentCode).' }, { status: 400 });
    }

    const attemptRef = adminDb.collection('subjectiveAttempts').doc(attemptId);
    const snap = await attemptRef.get();

    if (!snap.exists) {
      return NextResponse.json({ message: 'Attempt document not found.' }, { status: 404 });
    }

    const attemptData = snap.data()!;
    if (attemptData.studentCode !== studentCode) {
      return NextResponse.json({ message: 'Access denied to this attempt.' }, { status: 403 });
    }

    const finishedStatuses = ['completed', 'peer_review_pending', 'peer_reviewed', 'parent_reviewed', 'approved'];
    if (finishedStatuses.includes(attemptData.status)) {
      return NextResponse.json({ message: 'Exam attempt already submitted.' }, { status: 400 });
    }

    // Fetch full questions to save in the snapshot
    const examSnap = await adminDb.collection('subjectiveExams').doc(attemptData.examId).get();
    const examData = examSnap.exists ? examSnap.data()! : {};
    const questions = await getAttemptQuestions(attemptData, examData);

    const submissionUpdates = {
      status: 'completed',
      completedAt: new Date(),
      questionSnapshot: questions,
      tabViolations: Number(tabViolations) || 0,
      noFaceCount: Number(noFaceCount) || 0,
      multipleFacesCount: Number(multipleFacesCount) || 0,
      awayTimeTotal: Number(awayTimeTotal) || 0,
      timeSpentSeconds: Number(timeSpentSeconds) || 0,
      proctoringViolationTriggered: !!proctoringViolationTriggered,
      micAvailable: micBypassed !== undefined ? !micBypassed : true,
      violations: violations || null
    };

    await attemptRef.update(submissionUpdates);

    // Mark questions as used in database for safety
    if (examData.mode === 'home' && Array.isArray(attemptData.questionIds)) {
      await Promise.all(
        attemptData.questionIds.map((qid: string) =>
          adminDb.collection('questions').doc(qid).update({
            usedInHome: true,
            updatedAt: new Date()
          }).catch(() => null)
        )
      );
    }

    return NextResponse.json({ success: true, message: 'Exam submitted successfully.' });

  } catch (error: any) {
    console.error('API subjective submit error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
