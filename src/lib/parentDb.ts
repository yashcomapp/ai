import { adminDb } from '@/lib/firebase/admin';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { getDateKeyIST } from '@/lib/dateUtils';
import { chunkArray } from '@/lib/firestoreUtils';
import { calculateUnifiedMetrics } from '@/lib/dashboardMetrics';
import { calculateProctoringIntegrityScore } from '@/lib/proctoring';

export async function getParentDashboardData(
  parentEmail: string,
  parentData: any,
  selectedStudentCode: string | null,
  rangeDays: number = 7
) {
  // Resolve child list
  let studentCodes: string[] = [];
  if (Array.isArray(parentData?.studentCodes)) {
    studentCodes = parentData.studentCodes.filter(Boolean);
  } else if (parentData?.studentCode) {
    studentCodes = [parentData.studentCode];
  } else if (parentData?.studentId) {
    studentCodes = [parentData.studentId];
  }

  // Query students matching parent email or parent phone in parallel to discover all children/siblings
  const parentPhone = parentData?.phone || parentData?.parentPhone;
  if (parentEmail || parentPhone) {
    const [emailSnap, phoneSnap] = await Promise.all([
      parentEmail
        ? adminDb.collection('users')
            .where('role', '==', 'student')
            .where('parentEmail', '==', parentEmail)
            .get()
            .catch(() => ({ docs: [] } as any))
        : Promise.resolve({ docs: [] } as any),
      parentPhone
        ? adminDb.collection('users')
            .where('role', '==', 'student')
            .where('parentPhone', '==', parentPhone)
            .get()
            .catch(() => ({ docs: [] } as any))
        : Promise.resolve({ docs: [] } as any)
    ]);

    emailSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      if (data.studentCode && !studentCodes.includes(data.studentCode)) {
        studentCodes.push(data.studentCode);
      }
    });

    phoneSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      if (data.studentCode && !studentCodes.includes(data.studentCode)) {
        studentCodes.push(data.studentCode);
      }
    });
  }

  let childrenDocs: any[] = [];
  // Fetch children profiles to build child lists
  if (studentCodes.length > 0) {
    const chunks = chunkArray(studentCodes, 30);
    const results = await Promise.all(chunks.map(chunk => 
      adminDb.collection('users')
        .where('role', '==', 'student')
        .where('studentCode', 'in', chunk)
        .get()
    ));

    results.forEach(snap => {
      snap.docs.forEach(doc => {
        const data = doc.data();
        if (data.role === 'student') {
          childrenDocs.push({
            uid: doc.id,
            ...data
          });
        }
      });
    });

    // Deduplicate children list by studentCode
    const seen = new Set();
    childrenDocs = childrenDocs.filter(c => {
      if (!c.studentCode) return false;
      if (seen.has(c.studentCode)) return false;
      seen.add(c.studentCode);
      return true;
    });
  }

  const childrenList = childrenDocs.map(c => ({
    studentCode: c.studentCode,
    name: c.name || c.displayName || 'Child',
    uid: c.uid,
    batchId: c.batchId || null,
    batchIds: c.batchIds || [],
    className: c.class ? (String(c.class).startsWith('Class') ? String(c.class) : `Class ${c.class}`) : (c.classNum ? `Class ${c.classNum}` : (c.className || 'Student'))
  }));

  // If no specific child is requested, default to the first child
  let targetStudentCode = selectedStudentCode;
  if (!targetStudentCode && childrenList.length > 0) {
    targetStudentCode = childrenList[0].studentCode;
  }

  if (!targetStudentCode) {
    return {
      children: childrenList
    };
  }

  // Resolve the active child doc
  let childUser = childrenDocs.find(c => c.studentCode === targetStudentCode);
  let childUid = childUser ? childUser.uid : null;

  if (!childUid) {
    throw new Error('Access denied: student does not belong to parent profile.');
  }

  // Aggregations for the child
  const dateKeyOf = (d: Date) => getDateKeyIST(d);
  const thirtyDaysAgo = new Date();
  thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);
  const thirtyDaysAgoStr = dateKeyOf(thirtyDaysAgo);

  const timeLogSnapshot = await adminDb.collection('userTimeLog')
    .where('uid', '==', childUid)
    .where('date', '>=', thirtyDaysAgoStr)
    .get();
  
  let todaySeconds = 0;
  let todayExamSeconds = 0;
  let todayPracticeSeconds = 0;
  let todayReviewSeconds = 0;
  let todayGeneralSeconds = 0;

  let weekSeconds = 0;
  let weekExamSeconds = 0;
  let weekPracticeSeconds = 0;
  let weekReviewSeconds = 0;
  let weekGeneralSeconds = 0;

  const todayStr = dateKeyOf(new Date());

  timeLogSnapshot.docs.forEach(doc => {
    const d = doc.data();
    const s = Number(d.seconds) || 0;
    const ex = Number(d.examSeconds) || 0;
    const pr = Number(d.practiceSeconds) || 0;
    const rv = Number(d.reviewSeconds) || 0;
    const gen = Math.max(0, s - (ex + pr + rv));

    if (d.date === todayStr) {
      todaySeconds = s;
      todayExamSeconds = ex;
      todayPracticeSeconds = pr;
      todayReviewSeconds = rv;
      todayGeneralSeconds = gen;
    }
  });

  for (let i = 0; i < 7; i++) {
    const dateObj = new Date(); dateObj.setDate(dateObj.getDate() - i);
    const k = dateKeyOf(dateObj);
    const match = timeLogSnapshot.docs.find(doc => doc.data().date === k);
    if (match) {
      const data = match.data();
      const s = Number(data.seconds) || 0;
      const ex = Number(data.examSeconds) || 0;
      const pr = Number(data.practiceSeconds) || 0;
      const rv = Number(data.reviewSeconds) || 0;
      const gen = Math.max(0, s - (ex + pr + rv));
      weekSeconds += s;
      weekExamSeconds += ex;
      weekPracticeSeconds += pr;
      weekReviewSeconds += rv;
      weekGeneralSeconds += gen;
    }
  }

  let streakDays = 0;
  const d = new Date();
  while (streakDays < 100) {
    const key = dateKeyOf(d);
    const matchDoc = timeLogSnapshot.docs.find(doc => doc.data().date === key);
    if (!matchDoc || !(matchDoc.data().seconds > 0)) break;
    streakDays++;
    d.setDate(d.getDate() - 1);
  }

  // 2. Fetch statistics, targeted assignments, and weekly tests in parallel
  const childBatchIds: string[] = [...(childUser?.batchIds || [])];
  if (childUser?.batchId && !childBatchIds.includes(childUser.batchId)) {
    childBatchIds.push(childUser.batchId);
  }

  // Limit subjectiveExams to rangeDays threshold
  const timeLimitMs = rangeDays * 24 * 60 * 60 * 1000;
  const thresholdDate = new Date(Date.now() - timeLimitMs);
  const thresholdDateStr = getDateKeyIST(thresholdDate); // "YYYY-MM-DD" in IST

  const [
    reviewsSnapshot,
    parentReviewsSnapshot,
    subjectiveAttemptsSnapshot,
    batchAssignmentsSnapshot,
    studentAssignmentsSnapshot,
    subAssignmentsSnapshot,
    subStudentAssignmentsSnapshot,
    classroomExamsSnap,
    homePracticeSnap,
    integritySnapshot,
    masterySnapshot,
    evaluationsSnapshot
  ] = await Promise.all([
    adminDb.collection('reviews')
      .where('studentCode', '==', targetStudentCode)
      .select('examId', 'examType', 'percentage', 'score', 'totalMarks', 'createdAt', 'completedAt', 'startedAt', 'name', 'subjectName', 'status', 'wrongAnswerReasons', 'examName', 'examCode', 'tabViolations', 'proctoringViolations', 'questionCodes', 'questionDetails')
      .get(),
    adminDb.collection('parentReviews')
      .where('studentCode', '==', targetStudentCode)
      .select('scorePercent', 'createdAt', 'startedAt', 'name', 'subjectName', 'status', 'correctCount', 'totalQuestions', 'masteryBefore', 'masteryAfter', 'topicCode', 'topicName', 'tabViolations', 'violations')
      .get(),
    adminDb.collection('subjectiveAttempts')
      .where('studentCode', '==', targetStudentCode)
      .select('examId', 'examName', 'completedAt', 'createdAt', 'startedAt', 'totalMarks', 'score', 'tabViolations', 'noFaceCount', 'multipleFacesCount', 'awayTimeTotal')
      .get(),

    // Batch Assignments (by batch list)
    childBatchIds.length > 0
      ? adminDb.collection('batchAssignments')
          .where('targetBatches', 'array-contains-any', childBatchIds)
          .where('status', '==', 'active')
          .get()
      : Promise.resolve({ docs: [] } as any),

    // Batch Assignments (by student specific)
    adminDb.collection('batchAssignments')
      .where('targetStudents', 'array-contains', targetStudentCode)
      .where('status', '==', 'active')
      .get(),

    // Subjective Assignments (by batch list)
    childBatchIds.length > 0
      ? adminDb.collection('subjectiveAssignments')
          .where('targetBatches', 'array-contains-any', childBatchIds)
          .where('status', '==', 'active')
          .get()
      : Promise.resolve({ docs: [] } as any),

    // Subjective Assignments (by student specific)
    adminDb.collection('subjectiveAssignments')
      .where('targetStudents', 'array-contains', targetStudentCode)
      .where('status', '==', 'active')
      .get(),

    // Classroom Tests scoped by student's batchIds (entire history for correct absent stats)
    childBatchIds.length > 0
      ? adminDb.collection('subjectiveExams')
          .where('type', '==', 'classroom_test')
          .where('batchId', 'in', childBatchIds)
          .get()
      : Promise.resolve({ docs: [] } as any),

    // Home Practices scoped by student's batchIds (entire history for correct absent stats)
    childBatchIds.length > 0
      ? adminDb.collection('subjectiveExams')
          .where('type', '==', 'home_practice')
          .where('batchId', 'in', childBatchIds)
          .get()
      : Promise.resolve({ docs: [] } as any),

    // Integrity Scores
    adminDb.collection('integrityScores')
      .where('studentCode', '==', targetStudentCode)
      .get(),

    // Topics Mastery
    adminDb.collection('studentTopicMastery')
      .where('studentCode', '==', targetStudentCode)
      .select('mastery', 'topicCode')
      .get(),

    // Evaluations
    adminDb.collection('evaluations')
      .where('studentCode', '==', targetStudentCode)
      .where('evaluatorType', '==', 'parent')
      .get()
  ]);

  const allExamResults = reviewsSnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
  const examResults = allExamResults.filter((e: any) => e.examType !== 'entrance');
  const entranceResults = allExamResults.filter((e: any) => e.examType === 'entrance');
  const parentReviews = parentReviewsSnapshot.docs.map(doc => ({ id: doc.id, ...(doc.data() as any) }));
  const subjectiveAttemptsList = subjectiveAttemptsSnapshot.docs.map(doc => ({ id: doc.id, ...(doc.data() as any) }));

  const now = new Date();

  // Deduplicate assignments by examId to prevent double counting
  const uniqueAssignments = new Map();
  const allAssignmentsList = [
    ...batchAssignmentsSnapshot.docs,
    ...studentAssignmentsSnapshot.docs,
    ...subAssignmentsSnapshot.docs,
    ...subStudentAssignmentsSnapshot.docs
  ];

  allAssignmentsList.forEach(doc => {
    const d = doc.data();
    const examId = d.examId;
    if (examId) {
      if (d.examType === 'entrance') return; // Skip entrance exams from absent statistics
      const currentEndAt = d.endAt?.toDate ? d.endAt.toDate() : new Date(d.endAt);
      const existing = uniqueAssignments.get(examId);
      if (!existing || currentEndAt > existing.endAt) {
        uniqueAssignments.set(examId, {
          examId,
          endAt: currentEndAt,
          examType: d.examType || (doc.ref.parent.id.includes('subjective') ? 'subjective' : 'objective')
        });
      }
    }
  });

  const subjectiveExamsMap = new Map<string, any>();
  const objectiveExamsMap = new Map<string, any>();

  // Pre-populate subjectiveExamsMap from classroom and home practice snapshots we already fetched
  classroomExamsSnap.docs.forEach((doc: any) => {
    subjectiveExamsMap.set(doc.id, doc.data());
  });
  homePracticeSnap.docs.forEach((doc: any) => {
    subjectiveExamsMap.set(doc.id, doc.data());
  });

  // Only fetch subjective metadata for attempts or assignments not already in the map
  const neededSubjectiveIds = Array.from(new Set([
    ...subjectiveAttemptsList.map((a: any) => a.examId).filter(Boolean),
    ...Array.from(uniqueAssignments.values()).filter((a: any) => a.examType === 'subjective').map((a: any) => a.examId)
  ])).filter(id => !subjectiveExamsMap.has(id));

  // Only fetch objective metadata for recent completed exams (top 15) or active assignments
  // to avoid fetching the entire historical catalog on every page load
  const recentExamResults = examResults.slice(0, 15);
  const neededObjectiveIds = Array.from(new Set([
    ...recentExamResults.map((r: any) => r.examId || r.id).filter(Boolean),
    ...Array.from(uniqueAssignments.values()).filter((a: any) => a.examType !== 'subjective').map((a: any) => a.examId)
  ]));

  const [subExamsSnaps, objExamsSnaps] = await Promise.all([
    neededSubjectiveIds.length > 0 ? adminDb.getAll(...neededSubjectiveIds.map(id => adminDb.collection('subjectiveExams').doc(id))).catch(() => []) : Promise.resolve([]),
    neededObjectiveIds.length > 0 ? adminDb.getAll(...neededObjectiveIds.map(id => adminDb.collection('exams').doc(id))).catch(() => []) : Promise.resolve([])
  ]);

  subExamsSnaps.forEach(snap => {
    if (snap && snap.exists) {
      subjectiveExamsMap.set(snap.id, snap.data());
    }
  });
  objExamsSnaps.forEach(snap => {
    if (snap && snap.exists) {
      objectiveExamsMap.set(snap.id, snap.data());
    }
  });

  const allTopicCodes = new Set<string>();
  const objectiveTopicCodes = new Set<string>();

  // Extract topic codes from objective exams
  objectiveExamsMap.forEach((examData, id) => {
    let topicCode = '';
    if (Array.isArray(examData.topicCodes) && examData.topicCodes.length > 0) {
      topicCode = examData.topicCodes[0];
    } else {
      const qCodes = examData.questionCodes || [];
      if (qCodes.length > 0) {
        topicCode = deriveTopicCodeFromQuestionCode(qCodes[0]);
      }
    }
    if (topicCode) {
      allTopicCodes.add(topicCode);
      objectiveTopicCodes.add(topicCode);
      examData.resolvedTopicCode = topicCode;
    }
  });

  // Extract topic codes from subjective exams
  subjectiveExamsMap.forEach((examData, id) => {
    let topicCode = '';
    if (Array.isArray(examData.topicCodes) && examData.topicCodes.length > 0) {
      topicCode = examData.topicCodes[0];
    } else {
      const qIds = examData.questionIds || [];
      if (qIds.length > 0) {
        topicCode = deriveTopicCodeFromQuestionCode(qIds[0]);
      }
    }
    if (topicCode) {
      allTopicCodes.add(topicCode);
      examData.resolvedTopicCode = topicCode;
    }
  });

  const uniqueTopicCodes = Array.from(allTopicCodes);
  const refs = uniqueTopicCodes.map(code => adminDb.collection('syllabusTopicIndex').doc(code));
  const syllabusSnaps = refs.length > 0 ? await adminDb.getAll(...refs).catch(() => []) : [];

  const syllabusMap = new Map<string, any>();
  syllabusSnaps.forEach(snap => {
    if (snap && snap.exists) {
      syllabusMap.set(snap.id, snap.data());
    }
  });

  // Distinct stats for Exams vs Self-Directed Practice
  const completedExams = examResults.filter((e: any) => e.percentage != null || e.score != null);
  const completedPractice = parentReviews.filter((p: any) => p.scorePercent != null);

  const examScores = completedExams.map((e: any) => parseFloat(e.percentage) || 0);
  const practiceScores = completedPractice.map((p: any) => parseFloat(p.scorePercent) || 0);

  const examAvgScore = completedExams.length ? Math.round(examScores.reduce((s, v) => s + v, 0) / completedExams.length) : 0;
  const practiceAvgScore = completedPractice.length ? Math.round(practiceScores.reduce((s, v) => s + v, 0) / completedPractice.length) : 0;
  
  const totalSessions = completedExams.length + completedPractice.length;
  const allScores = [...examScores, ...practiceScores];
  const avgScore = totalSessions ? Math.round(allScores.reduce((s, v) => s + v, 0) / totalSessions) : 0;

  // Helper to resolve dates from diverse schemas
  const getResolvedDate = (item: any) => {
    const fireDate = item.completedAt || item.submittedAt || item.createdAt || item.startedAt || item.date;
    if (!fireDate) return new Date(0);
    if (fireDate.toDate) return fireDate.toDate();
    const parsed = new Date(fireDate);
    return isNaN(parsed.getTime()) ? new Date(0) : parsed;
  };

  // Recent activity list
  const recentActivity = [
    ...examResults.map((e: any) => {
      const examData = objectiveExamsMap.get(e.examId || e.id);
      const tCode = examData?.resolvedTopicCode || '';
      const sData = tCode ? syllabusMap.get(tCode) : null;
      const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData?.chapter || e.name || 'Exam');
      return {
        type: 'exam',
        id: e.id,
        name: resolvedName,
        score: e.percentage || 0,
        date: getResolvedDate(e),
        subject: e.subjectName || 'General',
        status: e.status
      };
    }),
    ...parentReviews.map((p: any) => ({
      type: 'practice',
      id: p.id,
      name: p.name || 'Practice',
      score: p.scorePercent || 0,
      date: getResolvedDate(p),
      subject: p.subjectName || 'General',
      status: p.status
    }))
  ].sort((a, b) => b.date.getTime() - a.date.getTime()).slice(0, 10);

  // 3. Integrity Score
  let integrityScore = 100;
  let integrityRecord = null;
  if (!integritySnapshot.empty) {
    const records = integritySnapshot.docs.map(doc => doc.data());
    records.sort((a, b) => {
      const ad = a.weekStart?.toDate ? a.weekStart.toDate() : new Date(a.weekStart || 0);
      const bd = b.weekStart?.toDate ? b.weekStart.toDate() : new Date(b.weekStart || 0);
      return bd.getTime() - ad.getTime();
    });
    integrityRecord = records[0];
    integrityScore = integrityRecord.integrityScore ?? 100;
  }

  // 4. Topics Needing Attention
  let needsAttentionCount = 0;
  masterySnapshot.docs.forEach(doc => {
    if (Number(doc.data().mastery || 0) < 50) {
      needsAttentionCount += 1;
    }
  });

  let absentExamsCount = 0;
  
  // Calculate absences from formal assignments (Type A)
  uniqueAssignments.forEach(ass => {
    if (now > ass.endAt) {
      const attemptedObj = examResults.some((r: any) => r.examId === ass.examId);
      const attemptedSub = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === ass.examId);
      if (!attemptedObj && !attemptedSub) {
        absentExamsCount++;
      }
    }
  });

  // Calculate absences from 1-Click Weekly Suite subjectiveExams (Type B)
  const todayDateStr = getDateKeyIST(new Date());
  
  // Classroom Tests
  classroomExamsSnap.docs.forEach((doc: any) => {
    const examData = doc.data();
    const matchBatch = !examData.batchId || childBatchIds.includes(examData.batchId);
    if (matchBatch) {
      const scheduledDateStr = examData.scheduledDate || todayDateStr;
      const isPast = scheduledDateStr < todayDateStr;
      if (isPast) {
        const attempted = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === doc.id);
        if (!attempted) {
          absentExamsCount++;
        }
      }
    }
  });

  // Home Practices
  homePracticeSnap.docs.forEach((doc: any) => {
    const examData = doc.data();
    const matchBatch = !examData.batchId || childBatchIds.includes(examData.batchId);
    if (matchBatch) {
      const untilDate = examData.availableUntil?.toDate 
        ? examData.availableUntil.toDate() 
        : examData.availableUntil 
          ? new Date(examData.availableUntil) 
          : new Date(`${examData.scheduledDate}T23:00:00.000Z`);
      const isPast = now > untilDate;
      if (isPast) {
        const attempted = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === doc.id);
        if (!attempted) {
          absentExamsCount++;
        }
      }
    }
  });

  // 5. Compile line chart data showing exam marks & integrity over time
  const conductedTopicCodes = new Set<string>(objectiveTopicCodes);
  masterySnapshot.docs.forEach(doc => {
    const tc = doc.data().topicCode;
    if (tc) conductedTopicCodes.add(tc);
  });
  const totalCoveredTopics = conductedTopicCodes.size > 0 ? conductedTopicCodes.size : (masterySnapshot.docs.length > 0 ? masterySnapshot.docs.length : 1);

  const unifiedMetrics = calculateUnifiedMetrics({
    objectiveReviews: examResults,
    subjectiveEvaluations: evaluationsSnapshot.docs.map(doc => doc.data()),
    topicMasteries: masterySnapshot.docs.map(doc => doc.data()),
    practiceReviews: parentReviews,
    integrityScore,
    totalCoveredTopics: totalCoveredTopics
  });
  
  const evalsMap = new Map();
  evaluationsSnapshot.docs.forEach(doc => {
    const data = doc.data();
    if (data.attemptId) evalsMap.set(data.attemptId, data);
  });

  const examChartData: any[] = [];

  // Add completed objective exams
  examResults.forEach((r: any) => {
    if (r.examType === 'practice') return;
    const integrity = calculateProctoringIntegrityScore(r);
    
    const examData = objectiveExamsMap.get(r.examId || r.id);
    const tCode = examData?.resolvedTopicCode || '';
    const sData = tCode ? syllabusMap.get(tCode) : null;
    const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData?.chapter || r.name || r.examName || r.examCode || 'Objective Exam');

    examChartData.push({
      id: r.examId || r.id,
      name: resolvedName,
      date: getResolvedDate(r),
      marks: Math.round(parseFloat(r.percentage) || 0),
      integrity,
      status: 'completed'
    });
  });

  // Add completed/graded subjective exams
  subjectiveAttemptsList.forEach((a: any) => {
    const evaluation = evalsMap.get(a.id);
    const integrity = calculateProctoringIntegrityScore(a);
    
    if (evaluation) {
      const examData = subjectiveExamsMap.get(a.examId);
      const tCode = examData?.resolvedTopicCode || '';
      const sData = tCode ? syllabusMap.get(tCode) : null;
      const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData?.chapter || examData?.chapterName || a.examName || 'Subjective Exam');

      examChartData.push({
        id: a.examId || a.id,
        name: resolvedName,
        date: getResolvedDate(a),
        marks: Math.round(evaluation.percentage || 0),
        integrity,
        status: 'completed'
      });
    }
  });

  // Add absent Type A exams to chart
  uniqueAssignments.forEach(ass => {
    if (now > ass.endAt) {
      const attemptedObj = examResults.some((r: any) => r.examId === ass.examId);
      const attemptedSub = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === ass.examId);
      if (!attemptedObj && !attemptedSub) {
        const assDoc = allAssignmentsList.find(doc => doc.data().examId === ass.examId);
        const assData = assDoc?.data() || {};
        
        const examData = ass.examType === 'subjective' 
          ? subjectiveExamsMap.get(ass.examId) 
          : objectiveExamsMap.get(ass.examId);
        const tCode = examData?.resolvedTopicCode || '';
        const sData = tCode ? syllabusMap.get(tCode) : null;
        const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData?.chapter || examData?.chapterName || assData.examName || assData.name || 'Missed Exam');

        examChartData.push({
          id: ass.examId,
          name: resolvedName,
          date: ass.endAt,
          marks: 0,
          integrity: 100,
          status: 'absent'
        });
      }
    }
  });

  // Add absent Type B Weekly classroom tests to chart
  classroomExamsSnap.docs.forEach((doc: any) => {
    const examData = doc.data();
    const matchBatch = !examData.batchId || childBatchIds.includes(examData.batchId);
    if (matchBatch) {
      const scheduledDateStr = examData.scheduledDate || todayDateStr;
      const isPast = scheduledDateStr < todayDateStr;
      if (isPast) {
        const attempted = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === doc.id);
        if (!attempted) {
          const scheduledDate = new Date(`${scheduledDateStr}T23:59:59.000Z`);
          
          const tCode = examData.resolvedTopicCode || '';
          const sData = tCode ? syllabusMap.get(tCode) : null;
          const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData.chapter || examData.chapterName || examData.name || 'Missed Classroom Test');

          examChartData.push({
            id: doc.id,
            name: resolvedName,
            date: scheduledDate,
            marks: 0,
            integrity: 100,
            status: 'absent'
          });
        }
      }
    }
  });

  // Add absent Type B Weekly home practices to chart
  homePracticeSnap.docs.forEach((doc: any) => {
    const examData = doc.data();
    const matchBatch = !examData.batchId || childBatchIds.includes(examData.batchId);
    if (matchBatch) {
      const untilDate = examData.availableUntil?.toDate 
        ? examData.availableUntil.toDate() 
        : examData.availableUntil 
          ? new Date(examData.availableUntil) 
          : new Date(`${examData.scheduledDate}T23:00:00.000Z`);
      const isPast = now > untilDate;
      if (isPast) {
        const attempted = subjectiveAttemptsSnapshot.docs.some(a => a.data().examId === doc.id);
        if (!attempted) {
          const tCode = examData.resolvedTopicCode || '';
          const sData = tCode ? syllabusMap.get(tCode) : null;
          const resolvedName = sData ? `${sData.chapterName} — ${sData.topicName}` : (examData.chapter || examData.chapterName || examData.name || 'Missed Home Practice');

          examChartData.push({
            id: doc.id,
            name: resolvedName,
            date: untilDate,
            marks: 0,
            integrity: 100,
            status: 'absent'
          });
        }
      }
    }
  });

  // Sort chronologically
  examChartData.sort((a, b) => a.date.getTime() - b.date.getTime());

  const formattedChartData = examChartData.map(item => ({
    id: item.id,
    name: item.name,
    marks: item.marks,
    integrity: item.integrity,
    status: item.status,
    dateStr: item.date.toLocaleDateString('en-IN', { month: 'short', day: 'numeric', timeZone: 'Asia/Kolkata' }),
    date: item.date.toISOString()
  }));

  // --- Today's Specific Activity and Diagnostic Movement Computation ---
  const todayISTStr = getDateKeyIST(new Date());

  const examsToday = examResults.filter((e: any) => {
    const itemDate = getResolvedDate(e);
    return getDateKeyIST(itemDate) === todayISTStr;
  });

  const practicesToday = parentReviews.filter((p: any) => {
    const itemDate = getResolvedDate(p);
    return getDateKeyIST(itemDate) === todayISTStr;
  });

  const subjectiveToday = evaluationsSnapshot.docs.filter(doc => {
    const d = doc.data();
    const itemDate = d.createdAt?.toDate ? d.createdAt.toDate() : new Date(d.createdAt || 0);
    return getDateKeyIST(itemDate) === todayISTStr;
  });

  const allScoresToday: number[] = [
    ...examsToday.map((e: any) => Number(e.percentage) || 0),
    ...practicesToday.map((p: any) => Number(p.scorePercent) || 0),
    ...subjectiveToday.map(doc => Number(doc.data().percentage) || 0)
  ];

  const todayCompletedSessionsCount = examsToday.length + practicesToday.length + subjectiveToday.length;
  const todayAverageScore = allScoresToday.length > 0 
    ? Math.round(allScoresToday.reduce((a, b) => a + b, 0) / allScoresToday.length)
    : 0;

  let todayQuestionsAnswered = 0;
  examsToday.forEach((e: any) => { todayQuestionsAnswered += (e.totalQuestions || e.questionCodes?.length || 10); });
  practicesToday.forEach((p: any) => { todayQuestionsAnswered += (p.totalQuestions || p.questionsCount || 10); });
  subjectiveToday.forEach(doc => { todayQuestionsAnswered += (doc.data().totalQuestions || 5); });

  // Topic Diagnostics: Needs Attention Yesterday vs Practiced & Removed Today
  const masteriesList = masterySnapshot.docs.map(doc => doc.data());
  const needsAttentionTopicCodes = new Set<string>();
  const needsAttentionTopicsList: string[] = [];
  const masteredTopicCodes = new Set<string>();
  const inProgressTopicCodes = new Set<string>();

  masteriesList.forEach(m => {
    const mLevel = Number(m.masteryLevel) || 0;
    const conf = Number(m.confidence) || 0;
    const isMastered = (mLevel >= 90 && conf >= 20) || m.isRecoveryMastered === true;
    const sData = syllabusMap.get(m.topicCode);
    const displayName = sData ? `${sData.chapterName} — ${sData.topicName}` : (m.topicName || m.topicCode || 'Topic');

    if (isMastered) {
      masteredTopicCodes.add(m.topicCode);
    } else if (mLevel >= 50) {
      inProgressTopicCodes.add(m.topicCode);
    } else {
      needsAttentionTopicCodes.add(m.topicCode);
      needsAttentionTopicsList.push(displayName);
    }
  });

  const topicsPracticedTodayCodes = new Set<string>();
  const topicsPracticedTodayList: string[] = [];

  [...examsToday, ...practicesToday].forEach((item: any) => {
    const tCode = item.topicCode || item.resolvedTopicCode;
    if (tCode && !topicsPracticedTodayCodes.has(tCode)) {
      topicsPracticedTodayCodes.add(tCode);
      const sData = syllabusMap.get(tCode);
      topicsPracticedTodayList.push(sData ? `${sData.chapterName} — ${sData.topicName}` : (item.name || tCode));
    }
  });

  const recoveredTodayTopicsList: string[] = [];
  topicsPracticedTodayCodes.forEach(tCode => {
    if (masteredTopicCodes.has(tCode) || inProgressTopicCodes.has(tCode)) {
      const sData = syllabusMap.get(tCode);
      recoveredTodayTopicsList.push(sData ? `${sData.chapterName} — ${sData.topicName}` : tCode);
    }
  });

  const needsAttentionYesterdayCount = needsAttentionTopicsList.length + recoveredTodayTopicsList.length;

  return {
    childInfo: {
      uid: childUid,
      studentCode: targetStudentCode,
      name: childUser?.name || 'Child'
    },
    todayStats: {
      todayMinutes: Math.round(todaySeconds / 60),
      todayPracticeMinutes: Math.round(todayPracticeSeconds / 60),
      todayExamMinutes: Math.round(todayExamSeconds / 60),
      todaySessionsCount: todayCompletedSessionsCount,
      todayQuestionsCount: todayQuestionsAnswered,
      todayAverageScore,
      streakDays
    },
    topicDiagnostics: {
      needsAttentionYesterdayCount,
      needsAttentionYesterdayTopics: [...needsAttentionTopicsList, ...recoveredTodayTopicsList],
      practicedTodayCount: topicsPracticedTodayList.length,
      practicedTodayTopics: topicsPracticedTodayList,
      recoveredTodayCount: recoveredTodayTopicsList.length,
      recoveredTodayTopics: recoveredTodayTopicsList,
      needsAttentionRemainingCount: needsAttentionTopicsList.length,
      needsAttentionRemainingTopics: needsAttentionTopicsList
    },
    snapshot: {
      todaySeconds,
      todayExamSeconds,
      todayPracticeSeconds,
      todayReviewSeconds,
      todayGeneralSeconds,
      weekSeconds,
      weekExamSeconds,
      weekPracticeSeconds,
      weekReviewSeconds,
      weekGeneralSeconds,
      streakDays,
      avgScore: unifiedMetrics.averageMarks, // Unified composite exam average (Objective + Graded Subjective)
      overallExamAverage: unifiedMetrics.averageMarks,
      objectiveAvgScore: unifiedMetrics.objectiveAvg,
      subjectiveAvgScore: unifiedMetrics.subjectiveAvg,
      practiceAvgScore: unifiedMetrics.practiceAvg,
      overallMastery: unifiedMetrics.overallMastery,
      lqScore: unifiedMetrics.lqScore, // Unified true LQ/Mastery score
      effortsPercent: unifiedMetrics.effortsPercent, // Unified efforts percentage
      totalSessions: unifiedMetrics.examCount + unifiedMetrics.practicesCompletedCount,
      practicesCompletedCount: unifiedMetrics.practicesCompletedCount,
      totalTopicsCount: unifiedMetrics.totalTopicsCount,
      totalQuestionsPracticed: unifiedMetrics.totalQuestionsPracticed || (childUser?.totalQuestionsPracticed || 0),
      absentExamsCount,
      integrityScore: unifiedMetrics.integrityScore,
      needsAttentionCount: unifiedMetrics.needsAttentionTopicsCount,
      masteredTopicsCount: unifiedMetrics.masteredTopicsCount
    },
    recentActivity,
    chartData: formattedChartData,
    children: childrenList,
    entranceResults: entranceResults.map((e: any) => {
      const examData = objectiveExamsMap.get(e.examId || e.id) || {};
      return {
        id: e.id,
        examId: e.examId,
        examName: e.examName || examData.name || 'Mock Exam',
        score: e.score ?? 0,
        totalMarks: e.totalMarks ?? 360,
        percentage: e.percentage ?? 0,
        durationSpent: e.durationSpent || 0,
        date: getResolvedDate(e).toISOString(),
        subject: e.subjectName || 'General',
        status: e.status
      };
    })
  };
}
