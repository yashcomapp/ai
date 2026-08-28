import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { shuffleArray } from '@/lib/questionTypes';
import { ReportCacheManager } from '@/lib/reportCache';

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

    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }
    const exam = examSnap.data()!;

    const assignmentsSnap = await adminDb.collection('peerAssignments')
      .where('examId', '==', examId)
      .get();

    // Fetch student name mapping to resolve any raw student codes to actual names
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .get();
    const studentNameMap: { [code: string]: string } = {};
    studentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) {
        studentNameMap[data.studentCode] = data.name || data.studentCode;
      }
    });

    const pending: any[] = [];
    const completed: any[] = [];

    assignmentsSnap.docs.forEach(doc => {
      const data = doc.data();
      const reviewerCode = data.reviewerStudentCode || data.reviewerName;
      const revieweeCode = data.revieweeStudentCode || data.revieweeName;
      const reviewerName = studentNameMap[reviewerCode] || data.reviewerName || reviewerCode;
      const revieweeName = studentNameMap[revieweeCode] || data.revieweeName || revieweeCode;

      const item = { 
        id: doc.id, 
        ...data,
        reviewerName,
        revieweeName
      };
      if (data.status === 'pending') {
        pending.push(item);
      } else if (data.status === 'completed') {
        completed.push(item);
      }
    });

    return NextResponse.json({
      examId,
      examName: exam.name || '',
      peerReviewStatus: exam.peerReviewStatus || 'not_started',
      totalAssignments: assignmentsSnap.size,
      pendingCount: pending.length,
      completedCount: completed.length,
      pendingAssignments: pending,
      completedAssignments: completed
    });

  } catch (error: any) {
    console.error('API get lottery status error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Start classmate lottery circular peer review assignments allocation
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { examId } = body;

    if (!examId) {
      return NextResponse.json({ message: 'Missing parameters (examId).' }, { status: 400 });
    }

    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      return NextResponse.json({ message: 'Exam not found.' }, { status: 404 });
    }
    const exam = examSnap.data()!;

    let isClassroom = exam.mode === 'classroom';
    if (!isClassroom) {
      const activeAssign = await adminDb.collection('subjectiveAssignments')
        .where('examId', '==', examId)
        .get();
      isClassroom = activeAssign.docs.some(doc => doc.data().examMode === 'classroom');
    }

    if (!isClassroom) {
      return NextResponse.json({ message: 'Lottery is only supported for classroom subjective exams.' }, { status: 400 });
    }

    // Get all completed subjective attempts for this exam
    const attemptsSnap = await adminDb.collection('subjectiveAttempts')
      .where('examId', '==', examId)
      .where('status', '==', 'completed')
      .get();

    if (attemptsSnap.empty) {
      return NextResponse.json({ message: 'No completed attempts found. Students must submit before starting the lottery.' }, { status: 400 });
    }

    // Fetch student name mapping to save actual names instead of codes
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .get();
    const studentNameMap: { [code: string]: string } = {};
    studentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) {
        studentNameMap[data.studentCode] = data.name || data.studentCode;
      }
    });

    const students = attemptsSnap.docs.map(doc => {
      const data = doc.data();
      const code = data.studentCode;
      return {
        studentCode: code,
        attemptId: doc.id,
        name: studentNameMap[code] || data.studentName || code
      };
    });

    if (students.length < 2) {
      return NextResponse.json({ message: `Need at least 2 students for peer review circular assignments. Found: ${students.length}` }, { status: 400 });
    }

    // Circular lottery assignment algorithm
    let assignments: any[] = [];
    let valid = false;
    let attempts = 0;
    let currentShuffle = [...students];

    while (!valid && attempts < 100) {
      valid = true;
      assignments = [];

      for (let i = 0; i < currentShuffle.length; i++) {
        const reviewer = currentShuffle[i];
        const reviewee = currentShuffle[(i + 1) % currentShuffle.length];

        if (reviewer.studentCode === reviewee.studentCode) {
          valid = false;
          currentShuffle = shuffleArray(currentShuffle);
          break;
        }

        assignments.push({
          examId,
          reviewerStudentCode: reviewer.studentCode,
          reviewerAttemptId: reviewer.attemptId,
          reviewerName: reviewer.name,
          revieweeStudentCode: reviewee.studentCode,
          revieweeAttemptId: reviewee.attemptId,
          revieweeName: reviewee.name,
          status: 'pending',
          assignedAt: new Date(),
          completedAt: null,
          marksAwarded: null,
          maxMarks: exam.totalMarks || 0
        });
      }
      attempts++;
    }

    // If search limit exceeded, run fallback shift
    if (!valid) {
      assignments = [];
      for (let i = 0; i < students.length; i++) {
        const reviewer = students[i];
        const reviewee = students[(i + 1) % students.length];
        assignments.push({
          examId,
          reviewerStudentCode: reviewer.studentCode,
          reviewerAttemptId: reviewer.attemptId,
          reviewerName: reviewer.name,
          revieweeStudentCode: reviewee.studentCode,
          revieweeAttemptId: reviewee.attemptId,
          revieweeName: reviewee.name,
          status: 'pending',
          assignedAt: new Date(),
          completedAt: null,
          marksAwarded: null,
          maxMarks: exam.totalMarks || 0
        });
      }
    }

    // Write assignments and update student attempt statuses in transactions/batches (using ChunkedBatch)
    const dbBatch = new ChunkedBatch(adminDb);

    for (const assignment of assignments) {
      const assignmentRef = adminDb.collection('peerAssignments').doc();
      dbBatch.set(assignmentRef, assignment);

      const attemptRef = adminDb.collection('subjectiveAttempts').doc(assignment.reviewerAttemptId);
      dbBatch.update(attemptRef, {
        peerRevieweeCode: assignment.revieweeStudentCode,
        status: 'peer_review_pending'
      });
    }

    // Update subjective exam state
    const examRef = adminDb.collection('subjectiveExams').doc(examId);
    dbBatch.update(examRef, {
      peerReviewStatus: 'assigned',
      peerReviewStartedAt: new Date()
    });

    await dbBatch.commit();

    // Invalidate teacher final review report cache since attempt statuses have changed
    await ReportCacheManager.invalidateReport(`exam-report-subjective-${examId}`).catch(() => null);

    return NextResponse.json({
      success: true,
      totalStudents: students.length,
      totalAssignments: assignments.length
    });

  } catch (error: any) {
    console.error('API create lottery assignments error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
