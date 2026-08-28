import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ExamRepository } from '@/repositories/exam.repository';
import { ExamService } from '@/services/exam.service';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { generateAndDispatchExamNotices } from '@/lib/examNotices';
export const dynamic = 'force-dynamic';



export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const examId = searchParams.get('id');

    if (!examId) {
      return NextResponse.json({ message: 'Missing exam ID' }, { status: 400 });
    }

    const examSnap = await adminDb.collection('exams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found' }, { status: 404 });
    }

    const examData = examSnap.data() || {};
    
    // 1. Gather candidate question IDs/codes from all possible fields (questionCodes, questionIds, questions)
    let candidateCodes: string[] = [];
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

    // Generate lookup variants (original + standardized e.g. -GANI- -> -MGP1-, -SCIE- -> -CURI-)
    const lookupIds = new Set<string>();
    questionCodes.forEach(id => {
      lookupIds.add(id);
      const normalized = id.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-');
      lookupIds.add(normalized);
    });

    const refs = Array.from(lookupIds).map((id: string) => adminDb.collection('questions').doc(id));
    const questionSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];
    
    const questionMap = new Map<string, any>();
    questionSnaps.forEach((snap: any) => {
      if (snap && snap.exists) {
        const data = snap.data();
        const docId = snap.id;
        const qCode = data.questionCode || docId;
        const fullQ = { id: docId, ...data };
        questionMap.set(docId, fullQ);
        questionMap.set(qCode, fullQ);
        if (qCode.includes('-MGP1-')) questionMap.set(qCode.replace('-MGP1-', '-GANI-'), fullQ);
        if (qCode.includes('-CURI-')) questionMap.set(qCode.replace('-CURI-', '-SCIE-'), fullQ);
      }
    });

    // Check if any question was already embedded in examData.questions as full objects
    if (Array.isArray(examData.questions) && examData.questions.length > 0) {
      examData.questions.forEach((q: any) => {
        if (q && typeof q === 'object' && (q.text || q.questionText)) {
          const qKey = q.id || q.questionCode;
          if (qKey && !questionMap.has(qKey)) {
            questionMap.set(qKey, q);
          }
        }
      });
    }

    // Fallback: If still missing, query by questionCode
    const missingCodes = questionCodes.filter(c => !questionMap.has(c) && !questionMap.has(c.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-')));
    if (missingCodes.length > 0) {
      const searchCodes = new Set<string>();
      missingCodes.forEach(c => {
        searchCodes.add(c);
        searchCodes.add(c.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-'));
      });
      const searchList = Array.from(searchCodes);
      for (let i = 0; i < searchList.length; i += 30) {
        const chunk = searchList.slice(i, i + 30);
        const qSnap = await adminDb.collection('questions')
          .where('questionCode', 'in', chunk)
          .get();
        qSnap.docs.forEach(doc => {
          const data = doc.data();
          const qCode = data.questionCode || doc.id;
          const fullQ = { id: doc.id, ...data };
          questionMap.set(doc.id, fullQ);
          questionMap.set(qCode, fullQ);
          if (qCode.includes('-MGP1-')) questionMap.set(qCode.replace('-MGP1-', '-GANI-'), fullQ);
          if (qCode.includes('-CURI-')) questionMap.set(qCode.replace('-CURI-', '-SCIE-'), fullQ);
        });
      }
    }

    // Assemble rawQuestions based on questionCodes order
    let rawQuestions: any[] = [];
    const addedIds = new Set<string>();
    questionCodes.forEach(code => {
      const q = questionMap.get(code) || 
                questionMap.get(code.replace('-GANI-', '-MGP1-').replace('-SCIE-', '-CURI-'));
      if (q && !addedIds.has(q.id || q.questionCode)) {
        rawQuestions.push(q);
        addedIds.add(q.id || q.questionCode);
      }
    });

    if (rawQuestions.length === 0 && questionMap.size > 0) {
      rawQuestions = Array.from(new Set(Array.from(questionMap.values())));
    }

    // Strip correct answers to prevent client-side cheating inspection
    const secureQuestions = rawQuestions.map((q: any) => {
      const { correctAnswer, correctAnswers, explanation, ...secureQ } = q;
      return secureQ;
    });

    let topicName = null;
    const firstQCode = secureQuestions[0]?.questionCode || '';
    if (firstQCode) {
      const topicCode = deriveTopicCodeFromQuestionCode(firstQCode);
      if (topicCode) {
        try {
          const tSnap = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
          if (tSnap.exists) {
            topicName = tSnap.data()?.topicName || null;
          }
        } catch {}
      }
    }

    const secureExam = {
      id: examSnap.id,
      name: examData.name || 'Untitled Exam',
      duration: examData.duration || 30, // in minutes
      negativeMarks: examData.negativeMarks || 0,
      totalMarks: examData.totalMarks || secureQuestions.reduce((acc: number, q: any) => acc + (q.marks || 1), 0),
      subject: examData.subject || null,
      chapter: examData.chapter || null,
      topicName: topicName,
      questions: secureQuestions
    };

    const studentCode = student.userData?.studentCode || '';

    // Validate if student is assigned to this objective exam
    const studentBatchIds = student.userData?.batchIds || [];
    const assignmentQuery = await adminDb.collection('batchAssignments')
      .where('examId', '==', examId)
      .where('status', '==', 'active')
      .get();

    const isAssigned = assignmentQuery.docs.some(doc => {
      const data = doc.data();
      const targetType = data.targetType;
      if (targetType === 'student') {
        return Array.isArray(data.targetStudents) && data.targetStudents.includes(studentCode);
      } else {
        return Array.isArray(data.targetBatches) && data.targetBatches.some((b: string) => studentBatchIds.includes(b));
      }
    });

    if (!isAssigned) {
      return NextResponse.json({ message: 'Access Denied: You are not assigned to take this exam.' }, { status: 403 });
    }

    // Strict block if there are pending reviews (either objective self-reflection or classmate peer reviews)
    const [pendingObj, pendingSub] = await Promise.all([
      adminDb.collection('reviews')
        .where('studentCode', '==', studentCode)
        .where('status', '==', 'student_review')
        .limit(1)
        .get(),
      adminDb.collection('subjectiveAttempts')
        .where('studentCode', '==', studentCode)
        .where('status', '==', 'peer_review_pending')
        .limit(1)
        .get()
    ]);

    if (!pendingObj.empty || !pendingSub.empty) {
      return NextResponse.json({
        status: 'blocked_by_pending_review',
        message: 'You have pending exam reviews (either an objective exam self-reflection or a classmate peer-grading assignment) that need your attention. Please complete all pending reviews before starting your next exam.'
      }, { status: 403 });
    }

    // Enforce re-attempt prevention on close/reload for Objective exams
    const attemptRef = adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`);
    const attemptSnap = await attemptRef.get();

    if (attemptSnap.exists) {
      const attemptData = attemptSnap.data() || {};
      if (attemptData.status === 'precheck') {
        // Still in precheck modal, let them reload/retry diagnostics safely
      } else if (attemptData.status === 'in-progress') {
        // Allow re-entry if within duration limit (+5 mins buffer) and refreshes < 3
        const startedAt = attemptData.startedAt;
        if (startedAt) {
          const startedDate = startedAt.toDate ? startedAt.toDate() : new Date(startedAt);
          const elapsedMs = Date.now() - startedDate.getTime();
          const durationMin = examData.duration || 30;
          const maxBufferMs = (durationMin + 5) * 60 * 1000;
          
          const refreshCount = attemptData.refreshCount || 0;
          
          if (elapsedMs < maxBufferMs && refreshCount < 3) {
            // Increment the refresh count and allow re-entry
            await attemptRef.update({
              refreshCount: admin.firestore.FieldValue.increment(1)
            });
          } else {
            // Closed/force closed: auto submit and grade their saved answers!
            const userAnswers = attemptData.userAnswers || [];
            const studentName = student.userData?.name || 'Student';
            
            let assignmentsSnap: admin.firestore.QuerySnapshot | null = null;
            try {
              assignmentsSnap = await adminDb.collection('batchAssignments')
                .where('examId', '==', examId)
                .get();
            } catch (err: any) {
              console.warn('Pre-fetching assignments failed:', err.message);
            }

            await ExamService.submitExam({
              studentCode,
              studentId: student.decodedToken.uid,
              studentName,
              examId,
              examData,
              questions: secureQuestions,
              userAnswers,
              durationSpent: Math.floor(elapsedMs / 1000),
              tabViolations: attemptData.tabViolations || 0,
              proctoringViolations: attemptData.proctoringViolations || { noFace: 0, multipleFaces: 0, lookingAway: 0, headMovement: 0 },
              startedAt: startedDate.toISOString(),
              assignmentsSnap,
              proctoringViolationTriggered: false,
              micBypassed: attemptData.micBypassed || false,
              violations: attemptData.violations || null,
              abandoned: true
            });

            const blockReason = refreshCount >= 3 
              ? 'Re-entry denied. You have exceeded the maximum of 3 page refreshes allowed during this exam.'
              : 'Re-entry denied. Your exam session duration has expired.';

            return NextResponse.json({
              status: 'blocked',
              message: blockReason
            }, { status: 403 });
          }
        }
      } else {
        return NextResponse.json({
          status: 'blocked',
          message: 'Exam already submitted. Re-attempt is not allowed.'
        }, { status: 403 });
      }
    } else {
      // First time starting: set placeholder status 'precheck'
      await attemptRef.set({
        examId: examId,
        studentCode: studentCode,
        status: 'precheck',
        startedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    }

    const studentBatches = student.userData?.batchIds || (student.userData?.batchId ? [student.userData.batchId] : []);

    let assignment: any = null;

    // Check studentAssignments first
    if (studentCode) {
      const saSnap = await adminDb.collection('studentAssignments')
        .where('examId', '==', examId)
        .where('studentCode', '==', studentCode)
        .where('status', '==', 'active')
        .limit(1)
        .get();
      if (!saSnap.empty) {
        assignment = saSnap.docs[0].data();
      }
    }

    // If no student assignment found, check batchAssignments
    if (!assignment) {
      const baSnap = await adminDb.collection('batchAssignments')
        .where('examId', '==', examId)
        .where('status', '==', 'active')
        .get();
      
      // First check for student-specific assignment in batchAssignments
      let matched = baSnap.docs.find(doc => {
        const data = doc.data();
        return data.targetType === 'student' && 
               Array.isArray(data.targetStudents) && 
               data.targetStudents.includes(studentCode);
      });

      // If not found, check for batch assignments
      if (!matched && studentBatches.length > 0) {
        matched = baSnap.docs.find(doc => {
          const data = doc.data();
          const targetBatches = data.targetBatches || [];
          return targetBatches.some((b: string) => studentBatches.includes(b));
        });
      }

      if (matched) {
        assignment = matched.data();
      }
    }

    const startAtDate = assignment?.startAt?.toDate ? assignment.startAt.toDate() : assignment?.startAt ? new Date(assignment.startAt) : null;
    const endAtDate = assignment?.endAt?.toDate ? assignment.endAt.toDate() : assignment?.endAt ? new Date(assignment.endAt) : null;

    return NextResponse.json({
      exam: secureExam,
      assignment: assignment ? {
        openMode: assignment.openMode || 'immediate',
        startAt: startAtDate ? startAtDate.toISOString() : null,
        endAt: endAtDate ? endAtDate.toISOString() : null,
        lateEntryRestriction: assignment.lateEntryRestriction === true
      } : null
    });
  } catch (error: any) {
    console.error('API get secure exam error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Server-side evaluation and exam submission
export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, examId } = body;
    const studentCode = student.userData?.studentCode || '';

    if (action === 'start') {
      if (!examId || !studentCode) {
        return NextResponse.json({ message: 'Missing examId or studentCode' }, { status: 400 });
      }
      const attemptRef = adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`);
      await attemptRef.update({
        status: 'in-progress',
        startedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      return NextResponse.json({ success: true, message: 'Exam started successfully.' });
    }

    if (action === 'autosave') {
      if (!examId || !studentCode) {
        return NextResponse.json({ message: 'Missing examId or studentCode' }, { status: 400 });
      }
      const { userAnswers } = body;
      const attemptRef = adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`);
      await attemptRef.update({
        userAnswers: userAnswers || [],
        lastAutosavedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      return NextResponse.json({ success: true, message: 'Exam answers autosaved.' });
    }

    const { userAnswers, durationSpent, tabViolations, proctoringViolations, startedAt, proctoringViolationTriggered, micBypassed, disputedQuestionIds } = body;

    if (!examId || !userAnswers) {
      return NextResponse.json({ message: 'Missing exam ID or user answers.' }, { status: 400 });
    }

    // 1. Fetch the exam document
    const examData = await ExamRepository.getById(examId);
    if (!examData) {
      return NextResponse.json({ message: 'Exam not found' }, { status: 404 });
    }

    const questionCodes = examData.questionCodes || [];

    // 2. Fetch all question documents
    const questions = await ExamRepository.getQuestionsForExam(questionCodes);

    const studentName = student.userData?.name || 'Student';

    // 3. Pre-fetch assignments matching examId
    let assignmentsSnap: admin.firestore.QuerySnapshot | null = null;
    if (studentCode) {
      try {
        assignmentsSnap = await adminDb.collection('batchAssignments')
          .where('examId', '==', examId)
          .get();
      } catch (err: any) {
        console.warn('Pre-fetching assignments failed:', err.message);
      }
    }

    // 4. Orchestrate scoring writes via ExamService
    const txResult = await ExamService.submitExam({
      studentCode,
      studentId: student.decodedToken.uid,
      studentName,
      examId,
      examData,
      questions,
      userAnswers,
      durationSpent,
      tabViolations,
      proctoringViolations,
      startedAt,
      assignmentsSnap,
      proctoringViolationTriggered: !!proctoringViolationTriggered,
      micBypassed: micBypassed !== undefined ? !!micBypassed : undefined,
      violations: body.violations || null,
      disputedQuestionIds: Array.isArray(disputedQuestionIds) ? disputedQuestionIds : []
    });

    return NextResponse.json({
      success: true,
      score: txResult.score,
      totalMarks: txResult.totalMarks,
      percentage: txResult.percentage,
      examSubject: txResult.examSubject,
      examChapter: txResult.examChapter,
      wrongAnswers: txResult.wrongAnswers || [],
      unattemptedQuestions: txResult.unattemptedQuestions || [],
      status: txResult.status,
      message: txResult.alreadySubmitted ? 'Already submitted. Returned cached score.' : 'Exam submission processed successfully.'
    });

  } catch (error: any) {
    console.error('API submit exam error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function PUT(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { examId, wrongAnswerReasons } = body;
    const studentCode = student.userData?.studentCode || '';

    if (!examId || !studentCode) {
      return NextResponse.json({ message: 'Missing examId or studentCode' }, { status: 400 });
    }

    const reviewRef = adminDb.collection('reviews').doc(`${examId}_${studentCode}`);
    const reviewSnap = await reviewRef.get();

    if (!reviewSnap.exists) {
      return NextResponse.json({ message: 'Review doc not found' }, { status: 404 });
    }

    const currentStatus = reviewSnap.data()?.status;
    const isAutonomous = student.userData?.autonomous === true;
    if (currentStatus === 'student_review') {
      await reviewRef.update({
        status: isAutonomous ? 'approved' : 'pending',
        studentReviewedAt: admin.firestore.FieldValue.serverTimestamp(),
        ...(wrongAnswerReasons ? { wrongAnswerReasons } : {})
      });
    }

    return NextResponse.json({ success: true, message: isAutonomous ? 'Status updated to approved' : 'Status updated to pending' });
  } catch (error: any) {
    console.error('API update review status error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
