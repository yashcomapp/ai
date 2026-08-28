import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { verifyAnyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const caller = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!caller) {
      return NextResponse.json({ message: 'Unauthorized. Valid student, parent, or admin session required.' }, { status: 401 });
    }

    const { searchParams } = new URL(req.url);
    let studentCode = searchParams.get('studentCode');
    const callerRole = caller.role;

    // Authorization checks
    if (callerRole === 'student') {
      const ownCode = caller.userData?.studentCode;
      if (!studentCode) {
        studentCode = ownCode;
      } else if (studentCode !== ownCode) {
        return NextResponse.json({ message: 'Forbidden. Students can only view their own register.' }, { status: 403 });
      }
    } else if (callerRole === 'parent') {
      const parentData = caller.userData;
      let childrenCodes: string[] = [];
      if (Array.isArray(parentData?.studentCodes)) {
        childrenCodes = parentData.studentCodes.filter(Boolean);
      } else if (parentData?.studentCode) {
        childrenCodes = [parentData.studentCode];
      }
      
      const parentEmail = parentData?.email?.toLowerCase();
      if (parentEmail) {
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
      }

      if (!studentCode) {
        return NextResponse.json({ message: 'Missing studentCode parameter.' }, { status: 400 });
      }
      if (!childrenCodes.includes(studentCode)) {
        return NextResponse.json({ message: 'Forbidden. Student is not linked to this parent.' }, { status: 403 });
      }
    } else if (callerRole !== 'admin' && callerRole !== 'teacher') {
      return NextResponse.json({ message: 'Forbidden. Insufficient permissions.' }, { status: 403 });
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Missing studentCode parameter.' }, { status: 400 });
    }

    // 2. Fetch target student details
    const studentQuerySnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();

    if (studentQuerySnap.empty) {
      return NextResponse.json({ message: 'Student profile not found.' }, { status: 404 });
    }

    const studentUser = studentQuerySnap.docs[0].data();
    const studentName = studentUser.name || 'Student';
    const batchIds: string[] = studentUser.batchIds || (studentUser.batchId ? [studentUser.batchId] : []);
    const studentClassRaw = studentUser.classNum || studentUser.class || studentUser.grade;
    const studentClassStr = String(studentClassRaw || '').trim().replace(/[^0-9]/g, '');
    const studentClassNum = studentClassStr ? Number(studentClassStr) : null;

    // 3. Fetch all potential sources of exams and attempts in parallel
    const [
      batchAssignmentsSnap,
      studentAssignmentsSnap,
      subAssignmentsSnap,
      subStudentAssignmentsSnap,
      subjectiveExamsSnap,
      reviewsSnap,
      subjectiveAttemptsSnap,
      examsSnap,
      absenceReasonsSnap
    ] = await Promise.all([
      // Objective batch assignments
      batchIds.length > 0
        ? adminDb.collection('batchAssignments')
            .where('targetBatches', 'array-contains-any', batchIds)
            .where('status', '==', 'active')
            .get()
        : Promise.resolve({ docs: [] } as any),

      // Objective student specific assignments
      adminDb.collection('batchAssignments')
        .where('targetStudents', 'array-contains', studentCode)
        .where('status', '==', 'active')
        .get(),

      // Subjective batch assignments
      batchIds.length > 0
        ? adminDb.collection('subjectiveAssignments')
            .where('targetBatches', 'array-contains-any', batchIds)
            .where('status', '==', 'active')
            .get()
        : Promise.resolve({ docs: [] } as any),

      // Subjective student specific assignments
      adminDb.collection('subjectiveAssignments')
        .where('targetStudents', 'array-contains', studentCode)
        .where('status', '==', 'active')
        .get(),

      // Subjective exams (classroom tests + home practices)
      adminDb.collection('subjectiveExams')
        .where('status', '==', 'active')
        .get(),

      // Objective attempts (reviews collection is the source of truth)
      adminDb.collection('reviews')
        .where('studentCode', '==', studentCode)
        .get(),

      // Subjective attempts
      adminDb.collection('subjectiveAttempts')
        .where('studentCode', '==', studentCode)
        .get(),

      // Objective exams
      adminDb.collection('exams').get(),

      // Exam absence reasons
      adminDb.collection('examAbsenceReasons')
        .where('studentCode', '==', studentCode)
        .get()
    ]);

    // Map absence reasons by examId
    const absenceReasonMap = new Map<string, string>();
    absenceReasonsSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      if (data.examId && data.reason) {
        absenceReasonMap.set(data.examId, data.reason);
      }
    });

    // Map objective exams metadata
    const examsMetadata = new Map<string, any>();
    examsSnap.docs.forEach(doc => {
      examsMetadata.set(doc.id, doc.data());
    });

    // Map subjective exams metadata
    const subjectiveExamsMetadata = new Map<string, any>();
    subjectiveExamsSnap.docs.forEach(doc => {
      subjectiveExamsMetadata.set(doc.id, doc.data());
    });

    // Map objective attempts (from reviews collection)
    const objectiveAttemptsMap = new Map<string, any>();
    reviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.examId) {
        objectiveAttemptsMap.set(data.examId, data);
      }
    });

    // Map subjective attempts
    const subjectiveAttemptsMap = new Map<string, any>();
    subjectiveAttemptsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.examId) {
        subjectiveAttemptsMap.set(data.examId, data);
      }
    });

    const now = new Date();
    const todayStr = getDateKeyIST();

    // Track processed exams to avoid duplicates
    const processedExams = new Map<string, any>();

    // A. Process Formal Assignments (Type A: assignments collection)
    const allAssignments = [
      ...batchAssignmentsSnap.docs.map((d: any) => ({ ...d.data(), id: d.id })),
      ...studentAssignmentsSnap.docs.map((d: any) => ({ ...d.data(), id: d.id })),
      ...subAssignmentsSnap.docs.map((d: any) => ({ ...d.data(), id: d.id })),
      ...subStudentAssignmentsSnap.docs.map((d: any) => ({ ...d.data(), id: d.id }))
    ];

    allAssignments.forEach(assignment => {
      const examId = assignment.examId;
      if (!examId) return;

      const endAt = assignment.endAt?.toDate ? assignment.endAt.toDate() : new Date(assignment.endAt || assignment.createdAt);
      const isPast = now > endAt;
      const isSubjective = assignment.examType === 'subjective';

      // Find if attempt exists
      const attempt = isSubjective
        ? subjectiveAttemptsMap.get(examId)
        : objectiveAttemptsMap.get(examId);

      if (assignment.examType === 'entrance' || attempt?.examType === 'entrance') return;

      const hasAttempt = !!attempt;

      let topicCode = '';
      const examMeta = isSubjective ? subjectiveExamsMetadata.get(examId) : examsMetadata.get(examId);
      if (examMeta) {
        if (Array.isArray(examMeta.topicCodes) && examMeta.topicCodes.length > 0) {
          topicCode = examMeta.topicCodes[0];
        } else {
          const qCodes = examMeta.questionCodes || examMeta.questionIds || [];
          if (qCodes.length > 0) {
            topicCode = deriveTopicCodeFromQuestionCode(qCodes[0]);
          }
        }
      }

      if (hasAttempt) {
        const score = isSubjective
          ? (attempt.finalScore ?? attempt.score ?? 0)
          : (attempt.score ?? 0);
        const maxMarks = isSubjective
          ? (subjectiveExamsMetadata.get(examId)?.totalMarks || 100)
          : (attempt.totalMarks ?? examsMetadata.get(examId)?.totalMarks ?? 100);
        const percentage = maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0;
        const examName = isSubjective
          ? (subjectiveExamsMetadata.get(examId)?.name || assignment.name || 'Subjective Test')
          : (examsMetadata.get(examId)?.name || attempt.examName || 'Objective Test');

        processedExams.set(examId, {
          examId,
          name: examName,
          date: formatDate(attempt.completedAt || attempt.startedAt || assignment.endAt),
          maxMarks,
          score,
          percentage,
          status: 'present',
          topicCode
        });
      } else if (isPast) {
        // Mark as absent if no attempt and end date is past
        const maxMarks = isSubjective
          ? (subjectiveExamsMetadata.get(examId)?.totalMarks || 100)
          : (examsMetadata.get(examId)?.totalMarks || 100);
        const examName = isSubjective
          ? (subjectiveExamsMetadata.get(examId)?.name || assignment.name || 'Subjective Test')
          : (examsMetadata.get(examId)?.name || 'Objective Test');

        processedExams.set(examId, {
          examId,
          name: examName,
          date: formatDate(endAt),
          maxMarks,
          score: 0,
          percentage: 0,
          status: 'absent',
          topicCode
        });
      }
    });

    // B. Process Classroom Tests & Home Practices (Type B: subjectiveExams directly assigned)
    subjectiveExamsSnap.docs.forEach(doc => {
      const examData = doc.data();
      const examId = doc.id;

      // Skip if already processed via formal assignments
      if (processedExams.has(examId)) return;

      const examClassRaw = examData.classNum || examData.class;
      const examClassStr = String(examClassRaw || '').trim().replace(/[^0-9]/g, '');

      // 1. If exam has explicit class specified, enforce class matching
      if (studentClassStr && examClassStr && studentClassStr !== examClassStr) {
        return;
      }

      // 2. Target student check
      if (Array.isArray(examData.targetStudents) && examData.targetStudents.length > 0) {
        if (!examData.targetStudents.includes(studentCode)) return;
      }

      // 3. Batch matching check
      const examBatches = Array.isArray(examData.targetBatches)
        ? examData.targetBatches
        : (examData.batchId ? [examData.batchId] : []);

      if (examBatches.length > 0) {
        const matchesBatch = batchIds.some(bId => examBatches.includes(bId));
        if (!matchesBatch) return;
      }

      const scheduledDateStr = examData.scheduledDate || todayStr;
      let isPast = false;
      if (examData.type === 'home_practice') {
        const untilDate = examData.availableUntil?.toDate 
          ? examData.availableUntil.toDate() 
          : examData.availableUntil 
            ? new Date(examData.availableUntil) 
            : new Date(`${scheduledDateStr}T23:00:00.000Z`);
        isPast = now > untilDate;
      } else {
        isPast = scheduledDateStr < todayStr;
      }

      const attempt = subjectiveAttemptsMap.get(examId);
      const hasAttempt = !!attempt;

      let topicCode = '';
      if (Array.isArray(examData.topicCodes) && examData.topicCodes.length > 0) {
        topicCode = examData.topicCodes[0];
      } else {
        const qIds = examData.questionIds || [];
        if (qIds.length > 0) {
          topicCode = deriveTopicCodeFromQuestionCode(qIds[0]);
        }
      }

      if (hasAttempt) {
        const score = attempt.finalScore ?? attempt.score ?? 0;
        const maxMarks = examData.totalMarks || 100;
        const percentage = maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0;

        processedExams.set(examId, {
          examId,
          name: examData.name || 'Classroom Test',
          date: formatDate(attempt.completedAt || attempt.startedAt || scheduledDateStr),
          maxMarks,
          score,
          percentage,
          status: 'present',
          topicCode
        });
      } else if (isPast) {
        processedExams.set(examId, {
          examId,
          name: examData.name || 'Classroom Test',
          date: formatDate(scheduledDateStr),
          maxMarks: examData.totalMarks || 100,
          score: 0,
          percentage: 0,
          status: 'absent',
          topicCode
        });
      }
    });

    // C. Add any completed attempts/reviews that were not covered by active assignments/exams
    // This handles deleted/inactive assignments or previous batches so that counts match dashboard
    reviewsSnap.docs.forEach(doc => {
      const data = doc.data();
      const examId = data.examId || data.examCode;
      if (examId && !processedExams.has(examId)) {
        if (data.examType === 'entrance') return;
        const score = data.score ?? 0;
        const maxMarks = data.totalMarks ?? data.totalQuestions ?? 100;
        const percentage = maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0;
        let topicCode = '';
        if (Array.isArray(data.topicCodes) && data.topicCodes.length > 0) {
          topicCode = data.topicCodes[0];
        } else if (data.questionDetails && data.questionDetails.length > 0) {
          const firstQ = data.questionDetails[0];
          if (firstQ.questionCode) {
            topicCode = deriveTopicCodeFromQuestionCode(firstQ.questionCode);
          }
        }
        processedExams.set(examId, {
          examId,
          name: data.examName || data.examCode || 'Objective Test',
          date: formatDate(data.submittedAt || data.completedAt || data.processedAt || now),
          maxMarks,
          score,
          percentage,
          status: 'present',
          topicCode
        });
      }
    });

    subjectiveAttemptsSnap.docs.forEach(doc => {
      const data = doc.data();
      const examId = data.examId;
      if (examId && !processedExams.has(examId)) {
        // Only include completed subjective attempts
        const finishedStatuses = ['completed', 'peer_review_pending', 'peer_reviewed', 'parent_reviewed', 'approved'];
        if (finishedStatuses.includes(data.status)) {
          const score = data.finalScore !== undefined ? data.finalScore : (data.peerScore !== undefined ? data.peerScore : (data.parentScore !== undefined ? data.parentScore : 0));
          const maxMarks = data.totalMarks || 100;
          const percentage = maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0;
          let topicCode = '';
          const qDetails = data.questionSnapshot || [];
          if (qDetails.length > 0 && qDetails[0].questionCode) {
            topicCode = deriveTopicCodeFromQuestionCode(qDetails[0].questionCode);
          }
          processedExams.set(examId, {
            examId,
            name: data.examName || 'Subjective Test',
            date: formatDate(data.completedAt || data.startedAt || now),
            maxMarks,
            score,
            percentage,
            status: 'present',
            topicCode
          });
        }
      }
    });

    // Resolve topic metadata for all unique topic codes
    const uniqueTopicCodes = Array.from(new Set(
      Array.from(processedExams.values()).map(e => e.topicCode).filter(Boolean)
    ));
    const topicMetadata = new Map<string, { chapterName: string; topicName: string }>();
    if (uniqueTopicCodes.length > 0) {
      const refs = uniqueTopicCodes.map(code => adminDb.collection('syllabusTopicIndex').doc(code));
      const snaps = await adminDb.getAll(...refs).catch(() => []);
      snaps.forEach(snap => {
        if (snap && snap.exists) {
          const data = snap.data()!;
          topicMetadata.set(snap.id, {
            chapterName: data.chapterName || '',
            topicName: data.topicName || ''
          });
        }
      });
    }

    const examsWithDisplay = Array.from(processedExams.values()).map(e => {
      const resolved = e.topicCode ? topicMetadata.get(e.topicCode) : null;
      const examMeta = subjectiveExamsMetadata.get(e.examId) || examsMetadata.get(e.examId);
      
      const chapterName = resolved?.chapterName || examMeta?.chapter || examMeta?.chapterName || '';
      const topicName = resolved?.topicName || examMeta?.topicName || '';
      const canonicalName = examMeta?.name || examMeta?.examName || (e.name && e.name !== 'Objective Test' ? e.name : '') || (chapterName ? `${chapterName} — ${topicName || 'Test'}` : 'Objective Test');

      const { topicCode, ...rest } = e;
      const absenceReason = e.status === 'absent' ? (absenceReasonMap.get(e.examId) || '') : '';

      return {
        ...rest,
        name: canonicalName,
        chapterName,
        topicName,
        absenceReason
      };
    });

    // Convert map to sorted array
    const sortedExams = examsWithDisplay.sort((a, b) => {
      return new Date(a.date).getTime() - new Date(b.date).getTime();
    });

    // Calculate Summary Stats
    const total = sortedExams.length;
    const present = sortedExams.filter(e => e.status === 'present').length;
    const absent = total - present;

    const presentExams = sortedExams.filter(e => e.status === 'present');
    const averagePercentage = present > 0
      ? Math.round(presentExams.reduce((sum, e) => sum + e.percentage, 0) / present)
      : 0;

    // Resolve active batches name
    const batchRefs = batchIds.map((id: string) => adminDb.collection('batches').doc(id));
    const batchSnaps = batchRefs.length > 0 ? await adminDb.getAll(...batchRefs).catch(() => []) : [];
    const activeBatchNames = batchSnaps.map((snap: any) => snap.exists ? (snap.data()?.name || snap.id) : snap.id).join(', ') || 'General';

    return NextResponse.json({
      studentName,
      studentCode,
      batchName: activeBatchNames,
      exams: sortedExams,
      summary: {
        total,
        present,
        absent,
        averagePercentage
      }
    });

  } catch (error: any) {
    console.error('Error fetching exam register:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Save/update reason for exam absence
export async function POST(req: NextRequest) {
  try {
    const caller = await verifyAnyRole(req, ['student', 'parent', 'admin']);
    if (!caller) {
      return NextResponse.json({ message: 'Unauthorized. Valid student, parent, or admin session required.' }, { status: 401 });
    }

    const body = await req.json();
    const { studentCode, examId, reason } = body;

    if (!studentCode || !examId) {
      return NextResponse.json({ message: 'Missing required parameters (studentCode, examId)' }, { status: 400 });
    }

    const docRef = adminDb.collection('examAbsenceReasons').doc(`${studentCode}_${examId}`);
    await docRef.set({
      studentCode,
      examId,
      reason: reason ? reason.trim() : '',
      updatedBy: caller.userData?.email || caller.decodedToken?.email || 'User',
      updatedAt: new Date()
    }, { merge: true });

    return NextResponse.json({ success: true, message: 'Absence reason saved successfully.' });
  } catch (error: any) {
    console.error('Error saving exam absence reason:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// Helpers
function shortenName(name: string): string {
  if (!name) return '—';
  // Truncate long names to keep tables clean on mobile
  if (name.length > 20) {
    return name.slice(0, 18) + '...';
  }
  return name;
}

const formatDate = (dateObj: any): string => dateObj ? getDateKeyIST(dateObj) : '';
