import { adminDb } from '@/lib/firebase/admin';
import { getCachedSyllabus, getFromCache, setInCache } from '@/lib/firebase/cache';
import { getDateKeyIST } from '@/lib/dateUtils';
import { calculateUnifiedMetrics } from '@/lib/dashboardMetrics';
import { deriveTopicCodeFromQuestionCode, getCanonicalSubjectName } from '@/lib/questionTypes';

function resolveTopicNames(syllabusList: any, examData: any) {
  const targetTopicCodes = examData.topicCodes || [];
  const targetChapterNum = examData.chapterNumber || '';
  const topicNames: string[] = [];

  if (syllabusList && syllabusList.docs) {
    syllabusList.docs.forEach((doc: any) => {
      const sylData = doc.data();
      const matchesBoard = String(sylData.board || '').toLowerCase() === String(examData.board || '').toLowerCase() || doc.id.startsWith(String(examData.boardCode || '').toLowerCase());
      const matchesClass = String(sylData.class || '') === String(examData.class || '');
      const matchesSubject = String(sylData.subjectCode || '').toLowerCase() === String(examData.subjectCode || '').toLowerCase();
      
      if (matchesBoard && matchesClass && matchesSubject && sylData.chapters) {
        Object.values(sylData.chapters).forEach((ch: any) => {
          if (String(ch.number) === String(targetChapterNum) && ch.topics) {
            ch.topics.forEach((t: any) => {
              if (targetTopicCodes.includes(String(t.number))) {
                topicNames.push(t.name);
              }
            });
          }
        });
      }
    });

    if (topicNames.length === 0) {
      syllabusList.docs.forEach((doc: any) => {
        const sylData = doc.data();
        const matchesSubject = String(sylData.subjectCode || '').toLowerCase() === String(examData.subjectCode || '').toLowerCase();
        if (matchesSubject && sylData.chapters) {
          Object.values(sylData.chapters).forEach((ch: any) => {
            if (ch.topics) {
              ch.topics.forEach((t: any) => {
                if (targetTopicCodes.includes(String(t.number))) {
                  topicNames.push(t.name);
                }
              });
            }
          });
        }
      });
    }
  }

  return topicNames.join(', ');
}

function resolveFullTopicCodesToNames(syllabusList: any, fullTopicCodes: string[]): string[] {
  if (!fullTopicCodes || !fullTopicCodes.length || !syllabusList || !syllabusList.docs) {
    return [];
  }
  const resolvedNames: string[] = [];
  syllabusList.docs.forEach((doc: any) => {
    const sylData = doc.data();
    if (sylData.chapters) {
      Object.values(sylData.chapters).forEach((ch: any) => {
        if (ch.topics) {
          ch.topics.forEach((t: any) => {
            if (t.topicCode && fullTopicCodes.includes(t.topicCode)) {
              resolvedNames.push(t.name);
            }
          });
        }
      });
    }
  });
  return resolvedNames;
}

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


export async function getDashboardData(uid: string, userData: any, rangeDays: number = 7) {
  try {
    let studentCode = userData.studentCode || '';
    const batchIds: string[] = [...(userData.batchIds || [])];
    if (userData.batchId && !batchIds.includes(userData.batchId)) {
      batchIds.push(userData.batchId);
    }

    if (!studentCode) {
      // Auto-generate a fallback studentCode for testing/legacy users on the fly
      const year = new Date().getFullYear();
      const randomSuffix = Math.floor(1000 + Math.random() * 9000);
      studentCode = `ST-${year}-TEMP-${randomSuffix}`;
      await adminDb.collection('users').doc(uid).update({ studentCode });
      console.log(`Auto-generated studentCode ${studentCode} for user ${uid}`);
    }

    // Limit subjectiveExams queries to the specified date range (default 7 days / 1 week)
    const timeLimitMs = rangeDays * 24 * 60 * 60 * 1000;
    const thresholdDate = new Date(Date.now() - timeLimitMs);
    const thresholdDateStr = getDateKeyIST(thresholdDate); // "YYYY-MM-DD" in IST

    // 2. Fetch student statistics and other items in parallel
    const [
      reviewsSnapshot,
      peerReviewsSnapshot,
      batchAssignmentsSnapshot,
      studentAssignmentsSnapshot,
      subAssignmentsSnapshot,
      subStudentAssignmentsSnapshot,
      masterySnapshot,
      attemptsSnapshot,
      evaluationsSnapshot,
      syllabusList,
      classroomExamsSnap,
      homePracticeSnap,
      parentReviewsSnapshot
    ] = await Promise.all([
      adminDb.collection('reviews').where('studentCode', '==', studentCode).get(),
      adminDb.collection('peerAssignments').where('reviewerStudentCode', '==', studentCode).where('status', '==', 'pending').get(),
      
      // Batch Assignments (by batch list)
      batchIds.length > 0
        ? adminDb.collection('batchAssignments')
            .where('targetBatches', 'array-contains-any', batchIds)
            .where('status', '==', 'active')
            .get()
        : Promise.resolve({ docs: [] } as any),

      // Batch Assignments (by student specific)
      adminDb.collection('batchAssignments')
        .where('targetStudents', 'array-contains', studentCode)
        .where('status', '==', 'active')
        .get(),

      // Subjective Assignments (by batch list)
      batchIds.length > 0
        ? adminDb.collection('subjectiveAssignments')
            .where('targetBatches', 'array-contains-any', batchIds)
            .where('status', '==', 'active')
            .get()
        : Promise.resolve({ docs: [] } as any),

      // Subjective Assignments (by student specific)
      adminDb.collection('subjectiveAssignments')
        .where('targetStudents', 'array-contains', studentCode)
        .where('status', '==', 'active')
        .get(),

      // studentTopicMastery snapshot
      adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCode).get(),

      // Fetch student's attempts to filter out completed subjective exams
      adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).get(),

      // Fetch evaluations
      adminDb.collection('evaluations')
        .where('studentCode', '==', studentCode)
        .where('evaluatorType', '==', 'parent')
        .get(),

      // Load syllabus mapping cache
      getCachedSyllabus(),

      // Classroom Tests scoped by student's batchIds (entire history for correct absent stats)
      batchIds.length > 0
        ? adminDb.collection('subjectiveExams')
            .where('type', '==', 'classroom_test')
            .where('batchId', 'in', batchIds)
            .get()
        : Promise.resolve({ docs: [] } as any),

      // Home Practices scoped by student's batchIds (entire history for correct absent stats)
      batchIds.length > 0
        ? adminDb.collection('subjectiveExams')
            .where('type', '==', 'home_practice')
            .where('batchId', 'in', batchIds)
            .get()
        : Promise.resolve({ docs: [] } as any),

      // parentReviews snapshot
      adminDb.collection('parentReviews')
        .where('studentCode', '==', studentCode)
        .select('totalQuestions')
        .get()
    ]);

    // 3. Compile profile statistics (dynamically calculated from studentTopicMastery)
    let masteredTopicsCount = 0;
    let needsAttentionTopicsCount = 0;
    let overallMasterySum = 0;

    masterySnapshot.docs.forEach(doc => {
      const mData = doc.data();
      const mastery = Number(mData.mastery || 0);
      const confidence = Number(mData.confidence || 0);
      overallMasterySum += mastery;

      if (mastery < 50) {
        needsAttentionTopicsCount += 1;
      } else if (mastery >= 90 && confidence >= 20) {
        masteredTopicsCount += 1;
      }
    });

    let absentExamsCount = 0;
    const now = new Date();
    const todayDateStr = getDateKeyIST(new Date());
    const reviews = reviewsSnapshot.docs.map(doc => ({ id: doc.id, ...(doc.data() as any) }));
    
    // Deduplicate assignments by examId to prevent double-counting of multiple assignments (e.g. batch + student-specific)
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
            examType: d.examType
          });
        }
      }
    });

    // 1. Calculate absences from formal assignments (Type A)
    uniqueAssignments.forEach(ass => {
      if (now > ass.endAt) {
        const attemptedInObj = reviews.some((r: any) => r.examId === ass.examId);
        const attemptedInSub = attemptsSnapshot.docs.some((a: any) => a.data().examId === ass.examId);
        const attemptedInEval = evaluationsSnapshot.docs.some((d: any) => {
          const e = d.data();
          return e.examId === ass.examId || 
                 (e.legacyId && e.legacyId.startsWith(ass.examId)) || 
                 (e.attemptId && e.attemptId.startsWith(ass.examId));
        });
        if (!attemptedInObj && !attemptedInSub && !attemptedInEval) {
          absentExamsCount++;
        }
      }
    });

    // 2. Calculate absences from 1-Click Weekly Suite subjectiveExams (Type B)
    
    // Classroom Tests
    classroomExamsSnap.docs.forEach((doc: any) => {
      const examData = doc.data();
      const matchBatch = !examData.batchId || batchIds.includes(examData.batchId);
      if (matchBatch) {
        const scheduledDateStr = examData.scheduledDate || todayDateStr;
        const isPast = scheduledDateStr < todayDateStr;
        if (isPast) {
          const attempted = attemptsSnapshot.docs.some(a => a.data().examId === doc.id);
          if (!attempted) {
            absentExamsCount++;
          }
        }
      }
    });

    // Home Practices
    homePracticeSnap.docs.forEach((doc: any) => {
      const examData = doc.data();
      const matchBatch = !examData.batchId || batchIds.includes(examData.batchId);
      if (matchBatch) {
        const untilDate = examData.availableUntil?.toDate 
          ? examData.availableUntil.toDate() 
          : examData.availableUntil 
            ? new Date(examData.availableUntil) 
            : new Date(`${examData.scheduledDate}T23:00:00.000Z`);
        const isPast = now > untilDate;
        if (isPast) {
          const attempted = attemptsSnapshot.docs.some(a => a.data().examId === doc.id);
          if (!attempted) {
            absentExamsCount++;
          }
        }
      }
    });

    // Fetch subjective evaluations for this student
    const subjectiveEvaluationsList = evaluationsSnapshot.docs.map(doc => doc.data());
    const objectiveReviewsList = reviews;
    const topicMasteriesList = masterySnapshot.docs.map(doc => doc.data());
    const practiceReviewsList = parentReviewsSnapshot.docs.map(doc => doc.data());

    // Calculate total unique topics on which tests/exams have been conducted/assigned
    const conductedTopicCodes = new Set<string>();

    masterySnapshot.docs.forEach(doc => {
      const tc = doc.data().topicCode;
      if (tc) conductedTopicCodes.add(tc);
    });

    classroomExamsSnap.docs.forEach((doc: any) => {
      const d = doc.data();
      if (d.topicCode) conductedTopicCodes.add(d.topicCode);
      (d.topicCodes || d.topics || []).forEach((tc: string) => conductedTopicCodes.add(tc));
    });

    homePracticeSnap.docs.forEach((doc: any) => {
      const d = doc.data();
      if (d.topicCode) conductedTopicCodes.add(d.topicCode);
      (d.topicCodes || d.topics || []).forEach((tc: string) => conductedTopicCodes.add(tc));
    });

    allAssignmentsList.forEach(doc => {
      const d = doc.data();
      if (d.topicCode) conductedTopicCodes.add(d.topicCode);
      (d.topicCodes || d.topics || []).forEach((tc: string) => conductedTopicCodes.add(tc));
    });

    const totalCoveredTopicsCount = conductedTopicCodes.size > 0 
      ? conductedTopicCodes.size 
      : (topicMasteriesList.length > 0 ? topicMasteriesList.length : 1);

    const unifiedMetrics = calculateUnifiedMetrics({
      objectiveReviews: objectiveReviewsList,
      subjectiveEvaluations: subjectiveEvaluationsList,
      topicMasteries: topicMasteriesList,
      practiceReviews: practiceReviewsList,
      totalCoveredTopics: totalCoveredTopicsCount
    });

    const profile = {
      overallMastery: unifiedMetrics.overallMastery,
      lqScore: unifiedMetrics.lqScore,
      masteredTopics: unifiedMetrics.masteredTopicsCount,
      needsAttentionTopics: unifiedMetrics.needsAttentionTopicsCount,
      absentExamsCount,
      practicesCompletedCount: unifiedMetrics.practicesCompletedCount,
      totalTopicsCount: unifiedMetrics.totalTopicsCount,
      effortsPercent: unifiedMetrics.effortsPercent,
      totalQuestionsPracticed: unifiedMetrics.totalQuestionsPracticed,
      name: userData.name || 'Student',
      studentCode,
      autonomous: userData.autonomous || false,
      batchId: userData.batchId || null,
      batchIds: userData.batchIds || []
    };

    // 4. Compile reviews and results summary
    const completedObjective = objectiveReviewsList.filter((r: any) => r.percentage != null || r.score != null);
    const objPercentages = completedObjective.map((r: any) => parseFloat(r.percentage) || 0);
    const evalPercentages = subjectiveEvaluationsList.map((e: any) => parseFloat(e.percentage) || 0);
    const allPercentages = [...objPercentages, ...evalPercentages];
    
    const evalMap = new Set(
      evaluationsSnapshot.docs.map(doc => {
        const d = doc.data();
        return d.attemptId || d.legacyId;
      }).filter(Boolean)
    );

    const resultsSummary = {
      examCount: unifiedMetrics.examCount,
      averageScore: unifiedMetrics.averageMarks, // Unified composite exam average
      bestScore: allPercentages.length ? Math.round(Math.max(...allPercentages)) : 0,
      objectiveAvg: unifiedMetrics.objectiveAvg,
      subjectiveAvg: unifiedMetrics.subjectiveAvg,
      pendingReviewCount: reviews.filter((r: any) => {
        const isApproved = r.status === 'approved' || evalMap.has(r.id);
        return !isApproved && r.status === 'pending';
      }).length
    };

    // 5. Compile peer reviews
    const peerReviewsCount = peerReviewsSnapshot.docs.length;
    const firstPeerReviewExamId = peerReviewsCount > 0 ? (peerReviewsSnapshot.docs[0].data()?.examId || null) : null;

    // 6. Process Objective Exams (Combine batch-wide & student-specific assignments)
    const rawObjAssignments = [...batchAssignmentsSnapshot.docs, ...studentAssignmentsSnapshot.docs];
    const objAssignmentsMap = new Map();
    rawObjAssignments.forEach(doc => {
      objAssignmentsMap.set(doc.id, { id: doc.id, ...doc.data() });
    });

    const activeObjAssignments = [];
    const scheduledObjAssignments = [];

    for (const assignment of objAssignmentsMap.values()) {
      if (assignment.examType === 'subjective') continue;

      const startAt = assignment.startAt?.toDate ? assignment.startAt.toDate() : new Date(assignment.startAt);
      const endAt = assignment.endAt?.toDate ? assignment.endAt.toDate() : new Date(assignment.endAt);

      if (now > endAt) continue; // Expired
      if (now >= startAt) {
        activeObjAssignments.push(assignment);
      } else {
        scheduledObjAssignments.push({ ...assignment, _startAt: startAt });
      }
    }

    // Batch resolve all unique objective exam details
    const uniqueObjectiveIds = Array.from(new Set([
      ...activeObjAssignments.map(a => a.examId),
      ...scheduledObjAssignments.map(a => a.examId)
    ]));

    const objExamsMap = new Map();
    if (uniqueObjectiveIds.length > 0) {
      const objRefs = uniqueObjectiveIds.map(id => adminDb.collection('exams').doc(id));
      const objDocs = await adminDb.getAll(...objRefs);
      objDocs.forEach(doc => {
        if (doc.exists) {
          objExamsMap.set(doc.id, doc.data());
        }
      });
    }

    // Resolve details of active objective exams (if not already completed)
    const pendingObjectiveExams = [];
    const scheduledObjectiveExams = [];
    const pendingEntranceExams = [];
    const scheduledEntranceExams = [];

    for (const assignment of activeObjAssignments) {
      if (assignment.examType === 'entrance') continue;
      const examId = assignment.examId;
      // Check if student already has a review document for this exam
      const alreadyReviewed = reviews.some((r: any) => r.examId === examId);
      if (!alreadyReviewed) {
        const examData = objExamsMap.get(examId);
        if (examData && examData.status === 'active') {
          pendingObjectiveExams.push({
            id: examId,
            name: resolveTopicNames(syllabusList, examData) || examData.name || 'Objective Exam',
            subject: examData.subjects?.[0] || examData.subject || 'General',
            questionsCount: examData.questionCount || examData.questions?.length || 0,
            duration: assignment.examDuration || examData.duration || 30,
            totalMarks: examData.totalMarks || 0,
            chapterNumber: examData.chapterNumber,
            chapter: examData.chapter,
            topicCode: examData.topicCode || ''
          });
        }
      }
    }

    for (const assignment of scheduledObjAssignments) {
      if (assignment.examType === 'entrance') continue;
      const examData = objExamsMap.get(assignment.examId);
      if (examData) {
        scheduledObjectiveExams.push({
          id: assignment.examId,
          name: resolveTopicNames(syllabusList, examData) || examData.name || 'Objective Exam',
          subject: examData.subjects?.[0] || examData.subject || 'General',
          questionsCount: examData.questionCount || examData.questions?.length || 0,
          duration: assignment.examDuration || examData.duration || 30,
          totalMarks: examData.totalMarks || 0,
          chapterNumber: examData.chapterNumber,
          chapter: examData.chapter,
          topicCode: examData.topicCode || '',
          startAt: assignment._startAt
        });
      }
    }

    for (const assignment of activeObjAssignments) {
      if (assignment.examType !== 'entrance') continue;
      const examId = assignment.examId;
      const alreadyReviewed = reviews.some((r: any) => r.examId === examId);
      if (!alreadyReviewed) {
        const examData = objExamsMap.get(examId);
        if (examData && examData.status === 'active') {
          pendingEntranceExams.push({
            id: examId,
            name: resolveTopicNames(syllabusList, examData) || examData.name || 'Mock Exam',
            subject: examData.subjects?.[0] || examData.subject || 'General',
            questionsCount: examData.questionCount || examData.questions?.length || 0,
            duration: assignment.examDuration || examData.duration || 180,
            totalMarks: examData.totalMarks || 0,
            chapterNumber: examData.chapterNumber,
            chapter: examData.chapter,
            topicCode: examData.topicCode || '',
            examType: 'entrance'
          });
        }
      }
    }

    for (const assignment of scheduledObjAssignments) {
      if (assignment.examType !== 'entrance') continue;
      const examData = objExamsMap.get(assignment.examId);
      if (examData) {
        scheduledEntranceExams.push({
          id: assignment.examId,
          name: resolveTopicNames(syllabusList, examData) || examData.name || 'Mock Exam',
          subject: examData.subjects?.[0] || examData.subject || 'General',
          questionsCount: examData.questionCount || examData.questions?.length || 0,
          duration: assignment.examDuration || examData.duration || 180,
          totalMarks: examData.totalMarks || 0,
          chapterNumber: examData.chapterNumber,
          chapter: examData.chapter,
          topicCode: examData.topicCode || '',
          startAt: assignment._startAt,
          examType: 'entrance'
        });
      }
    }

    // 7. Process Subjective Exams
    const rawSubAssignments = [...subAssignmentsSnapshot.docs, ...subStudentAssignmentsSnapshot.docs];
    const subAssignmentsMap = new Map();
    rawSubAssignments.forEach(doc => {
      subAssignmentsMap.set(doc.id, { id: doc.id, ...doc.data() });
    });

    const activeSubAssignments = [];
    const scheduledSubAssignments = [];

    for (const assignment of subAssignmentsMap.values()) {
      const startAt = assignment.startAt?.toDate ? assignment.startAt.toDate() : new Date(assignment.startAt);
      const endAt = assignment.endAt?.toDate ? assignment.endAt.toDate() : new Date(assignment.endAt);

      if (now > endAt) continue; // Expired
      if (now >= startAt) {
        activeSubAssignments.push(assignment);
      } else {
        scheduledSubAssignments.push({ ...assignment, _startAt: startAt });
      }
    }

    const attempts = attemptsSnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));

    // Batch resolve all unique subjective exam details
    const uniqueSubjectiveIds = Array.from(new Set([
      ...activeSubAssignments.map(a => a.examId),
      ...scheduledSubAssignments.map(a => a.examId)
    ]));

    const subExamsMap = new Map();
    if (uniqueSubjectiveIds.length > 0) {
      const subRefs = uniqueSubjectiveIds.map(id => adminDb.collection('subjectiveExams').doc(id));
      const subDocs = await adminDb.getAll(...subRefs);
      subDocs.forEach(doc => {
        if (doc.exists) {
          subExamsMap.set(doc.id, doc.data());
        }
      });
    }

    const pendingSubjectiveExams: any[] = [];
    const scheduledSubjectiveExams: any[] = [];

    for (const assignment of activeSubAssignments) {
      const examId = assignment.examId;
      const attempt = attempts.find((a: any) => a.examId === examId);
      
      let isCompleted = false;
      if (attempt) {
        const attemptStatus = (attempt as any).status;
        isCompleted = attemptStatus === 'completed' ||
                      attemptStatus === 'peer_reviewed' ||
                      attemptStatus === 'parent_reviewed';
      }

      if (!isCompleted) {
        const examData = subExamsMap.get(examId);
        if (examData && examData.status === 'active') {
          pendingSubjectiveExams.push({
            id: examId,
            name: cleanSubjectiveExamName(examData) || resolveTopicNames(syllabusList, examData) || examData.name || 'Subjective Exam',
            subject: examData.subjects?.[0] || 'General',
            questionsCount: examData.questionCount || examData.questionIds?.length || 0,
            totalTime: Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60,
            totalMarks: examData.totalMarks || 0,
            mode: examData.mode || assignment.examMode || 'home',
            chapterNumber: examData.chapterNumber,
            chapter: examData.chapter,
            topicCode: examData.topicCode || ''
          });
        }
      }
    }

    for (const assignment of scheduledSubAssignments) {
      const examData = subExamsMap.get(assignment.examId);
      if (examData) {
        scheduledSubjectiveExams.push({
          id: assignment.examId,
          name: cleanSubjectiveExamName(examData) || resolveTopicNames(syllabusList, examData) || examData.name || 'Subjective Exam',
          subject: examData.subjects?.[0] || 'General',
          questionsCount: examData.questionCount || examData.questionIds?.length || 0,
          totalTime: Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60,
          totalMarks: examData.totalMarks || 0,
          mode: examData.mode || assignment.examMode || 'home',
          chapterNumber: examData.chapterNumber,
          chapter: examData.chapter,
          topicCode: examData.topicCode || '',
          startAt: assignment._startAt
        });
      }
    }

    // 7.5 Process 1-Click Weekly Suite Classroom Tests directly from subjectiveExams (avoiding assignment dependencies)

    classroomExamsSnap.docs.forEach((doc: any) => {
      const examData = doc.data();
      const matchBatch = examData.batchId 
        ? batchIds.includes(examData.batchId) 
        : (examData.class && String(examData.class) === String(userData.class));
      if (matchBatch) {
        const alreadyAttempted = attempts.some((a: any) => {
          return a.examId === doc.id && (
            a.status === 'completed' ||
            a.status === 'peer_reviewed' ||
            a.status === 'parent_reviewed'
          );
        });

        if (!alreadyAttempted) {
          const scheduledDateStr = examData.scheduledDate || todayDateStr;
          
          // Calculate day difference to only show exam on the day or one day before
          const todayDate = new Date(todayDateStr + 'T00:00:00Z');
          const scheduledDate = new Date(scheduledDateStr + 'T00:00:00Z');
          const diffTime = scheduledDate.getTime() - todayDate.getTime();
          const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24));

          // diffDays <= 0 covers today and any past uncompleted tests
          // diffDays === 1 covers one day before (Friday for Saturday test)
          const shouldShow = diffDays <= 1;

          if (shouldShow) {
            const isAlreadyAdded = pendingSubjectiveExams.some(e => e.id === doc.id) || 
                                   scheduledSubjectiveExams.some(e => e.id === doc.id);
            
            if (!isAlreadyAdded) {
              const isPending = diffDays <= 0;
              const examItem = {
                id: doc.id,
                name: cleanSubjectiveExamName(examData) || resolveTopicNames(syllabusList, examData) || examData.name || 'Classroom Test',
                subject: examData.subjects?.[0] || examData.subject || 'General',
                questionsCount: examData.questionCount || examData.questionIds?.length || 0,
                totalTime: Number(examData.totalTime) || (Number(examData.totalMarks) * 2) || 60,
                totalMarks: examData.totalMarks || 0,
                mode: examData.mode || 'classroom',
                chapterNumber: examData.chapterNumber,
                chapter: examData.chapter || examData.chapterName,
                topicCode: examData.topicCode || '',
                scheduledDate: scheduledDateStr,
                startAt: examData.startAt?.toDate ? examData.startAt.toDate() : (examData.startAt || new Date(`${scheduledDateStr}T00:00:00.000Z`))
              };

              if (isPending) {
                pendingSubjectiveExams.push(examItem);
              } else {
                scheduledSubjectiveExams.push(examItem);
              }
            }
          }
        }
      }
    });



    // Fetch Daily Home Practice sheets scheduled for today (active between 7:00 AM and 11:00 PM)
    const todayIST = getDateKeyIST(new Date()); // YYYY-MM-DD
    const tomorrowIST = getDateKeyIST(new Date(Date.now() + 24 * 60 * 60 * 1000)); // YYYY-MM-DD
    const dailyHomePractices: any[] = [];
    const studyChips: any[] = [];

    homePracticeSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      const matchBatch = !data.batchId || batchIds.includes(data.batchId);
      if (matchBatch) {
        const isMathHP = /math|algebra|geometry|ganit/i.test(data.subject || data.subjects?.[0] || '');
        let defaultFrom = `${data.scheduledDate}T15:00:00.000Z`; // 8:30 PM IST
        let defaultUntil = `${data.scheduledDate}T17:00:00.000Z`; // 10:30 PM IST
        if (isMathHP) {
          const prevDate = getDateKeyIST(new Date(new Date(data.scheduledDate).getTime() - 24 * 60 * 60 * 1000));
          defaultFrom = `${prevDate}T23:30:00.000Z`; // 5:00 AM IST next day
          defaultUntil = `${data.scheduledDate}T01:30:00.000Z`; // 7:00 AM IST
        }
        const fromDate = data.availableFrom ? new Date(data.availableFrom) : new Date(defaultFrom);
        const untilDate = data.availableUntil ? new Date(data.availableUntil) : new Date(defaultUntil);
        const hasStarted = now >= fromDate;
        const isActiveTime = now >= fromDate && now <= untilDate;

        const alreadyAttempted = attempts.some((a: any) => {
          return a.examId === doc.id && (
            a.status === 'completed' ||
            a.status === 'peer_review_pending' ||
            a.status === 'peer_reviewed' ||
            a.status === 'parent_reviewed' ||
            a.status === 'approved'
          );
        });

        // 1. If it's active and not attempted, add to pendingSubjectiveExams
        if (isActiveTime && !alreadyAttempted) {
          const isAlreadyAdded = pendingSubjectiveExams.some(e => e.id === doc.id);
          if (!isAlreadyAdded) {
            pendingSubjectiveExams.push({
              id: doc.id,
              name: cleanSubjectiveExamName(data) || resolveTopicNames(syllabusList, data) || data.name || 'Home Practice',
              subject: data.subjects?.[0] || data.subject || 'General',
              questionsCount: data.questionCount || data.questionIds?.length || 0,
              totalTime: Number(data.totalTime) || (Number(data.totalMarks) * 2) || 60,
              totalMarks: data.totalMarks || 0,
              mode: 'home',
              chapterNumber: data.chapterNumber,
              chapter: data.chapter || data.chapterName,
              topicCode: data.topicCode || '',
              scheduledDate: data.scheduledDate
            });
          }
        }

        // Today's learning sheet (Study Chip)
        const isMathSubject = /math|algebra|geometry|ganit/i.test(data.subject || '');
        const isAvailableStudy = data.scheduledDate === todayIST || (isMathSubject && data.scheduledDate === tomorrowIST);
        if (isAvailableStudy) {
          const resolvedTopicNames = resolveFullTopicCodesToNames(syllabusList, data.topics || []);
          studyChips.push({
            id: doc.id,
            examId: data.examId,
            name: data.name,
            subject: data.subject,
            chapterNumber: data.chapterNumber,
            chapterName: data.chapterName,
            topics: resolvedTopicNames.length > 0 ? resolvedTopicNames : (data.topics || []),
            dayName: data.dayName || '',
            scheduledDate: data.scheduledDate,
            totalQuestions: data.learningQuestions ? data.learningQuestions.length : (data.totalQuestions || 0),
            questions: data.learningQuestions || data.questions || [],
            isTomorrow: data.scheduledDate === tomorrowIST
          });
        }

        // Show daily home practice on its scheduled day (active status is time-dependent: 8:30 PM - 10:30 PM)
        if (data.scheduledDate === todayIST) {
          const resolvedTopicNames = resolveFullTopicCodesToNames(syllabusList, data.topics || []);
          dailyHomePractices.push({
            id: doc.id,
            examId: data.examId,
            name: data.name,
            subject: data.subject,
            chapterNumber: data.chapterNumber,
            chapterName: data.chapterName,
            topics: resolvedTopicNames.length > 0 ? resolvedTopicNames : (data.topics || []),
            scheduledDate: data.scheduledDate,
            dayName: data.dayName || '',
            totalMarks: data.totalMarks || 10,
            totalQuestions: data.totalQuestions || 0,
            questions: data.questions || [],
            isActive: isActiveTime,
            isExpired: now > untilDate
          });
        }
      }
    });

    // 7.8 Fetch Zoom Meeting Details for Student
    let zoomMeetingNumber = '89216852281';
    let zoomMeetingPasscode = '123456';
    let zoomMeetingTitle = 'Yashcom Virtual Classroom';
    let isMeetingActive = false;

    if (batchIds.length > 0) {
      try {
        const firstBatchDoc = await adminDb.collection('batches').doc(batchIds[0]).get();
        if (firstBatchDoc.exists) {
          const batchData = firstBatchDoc.data()!;
          if (batchData.zoomMeetingNumber && String(batchData.zoomMeetingNumber).trim() !== '') {
            zoomMeetingNumber = String(batchData.zoomMeetingNumber).trim();
            zoomMeetingPasscode = String(batchData.zoomMeetingPasscode || '').trim();
            zoomMeetingTitle = `${batchData.name || 'Yashcom'} Live Class`;
            isMeetingActive = batchData.zoomMeetingActive === true;
          }
        }
      } catch (err) {
        console.warn('Failed to query batch details for Zoom configuration:', err);
      }
    }

    const zoomClass = {
      meetingNumber: zoomMeetingNumber,
      passcode: zoomMeetingPasscode,
      title: zoomMeetingTitle,
      active: isMeetingActive
    };

    // 8. Return aggregated response
    return {
      profile,
      resultsSummary,
      peerReviews: {
        count: peerReviewsCount,
        firstExamId: firstPeerReviewExamId
      },
      exams: {
        pendingObjectiveExams,
        scheduledObjectiveExams,
        pendingSubjectiveExams,
        scheduledSubjectiveExams,
        pendingEntranceExams,
        scheduledEntranceExams,
        dailyHomePractices,
        studyChips
      },
      zoomClass
    };
  } catch (error: any) {
    console.error('getDashboardData error:', error);
    throw error;
  }
}

function getTopicState(mastery: number, confidence: number): string {
  if (mastery < 25) return 'Started';
  if (mastery < 50) return 'Learning';
  if (mastery < 90) return 'Practicing';
  if (mastery >= 90 && confidence >= 20) return 'Mastered';
  return 'Practicing';
}

function calculatePriority(mastery: number, confidence: number): number {
  return (100 - mastery) + Math.max(0, (20 - confidence) * 2);
}

export async function getStudentLearningData(userData: any) {
  const studentCode = userData.studentCode;
  if (!studentCode) {
    throw new Error('Missing student identifier profile.');
  }

  const cacheKey = `learning_data_${studentCode}`;
  const cached = getFromCache<any>(cacheKey);
  if (cached) return cached;

  const batchIds: string[] = userData.batchIds || (userData.batchId ? [userData.batchId] : []);

  // 1. Fetch batches to get all associated class codes (for multi-class enrolled students) in 1 batch RPC
  const batchRefs = batchIds.map((id: string) => adminDb.collection('batches').doc(id));
  const batchSnaps = batchRefs.length > 0 ? await adminDb.getAll(...batchRefs).catch(() => []) : [];
  const allClasses = new Set<string>();
  if (userData.class) {
    const m = String(userData.class).match(/\d+/);
    if (m) allClasses.add(m[0]);
    else allClasses.add(String(userData.class));
  }
  batchSnaps.forEach((snap: any) => {
    if (snap && snap.exists) {
      const d = snap.data();
      const cls = d.class || d.classCode;
      if (cls) {
        const m = String(cls).match(/\d+/);
        if (m) allClasses.add(m[0]);
        else allClasses.add(String(cls));
      }
    }
  });

  // 2. Fetch studentTopicMastery, practice reviews, attempts, and assignments in parallel
  const [masterySnaps, parentReviewsSnap, attemptsSnap, reviewsSnap, subAttemptsSnap, objAssignmentsSnap, subAssignmentsSnap, evalsSnap] = await Promise.all([
    adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCode).get(),
    adminDb.collection('parentReviews')
      .where('studentCode', '==', studentCode)
      .where('type', '==', 'practice')
      .select('topicCode')
      .get(),
    adminDb.collection('examAttempts').where('studentCode', '==', studentCode).get(),
    adminDb.collection('reviews').where('studentCode', '==', studentCode).get(),
    adminDb.collection('subjectiveAttempts').where('studentCode', '==', studentCode).get(),
    batchIds.length > 0
      ? adminDb.collection('batchAssignments').where('targetBatches', 'array-contains-any', batchIds).get()
      : Promise.resolve({ docs: [] } as any),
    batchIds.length > 0
      ? adminDb.collection('subjectiveAssignments').where('targetBatches', 'array-contains-any', batchIds).get()
      : Promise.resolve({ docs: [] } as any),
    adminDb.collection('evaluations').where('studentCode', '==', studentCode).get()
  ]);

  // Identify absent exams and collect their topics
  const attemptedExamIds = new Set([
    ...attemptsSnap.docs.map((d: any) => d.data().examId),
    ...reviewsSnap.docs.map((d: any) => d.data().examId),
    ...subAttemptsSnap.docs.map((d: any) => d.data().examId),
    ...evalsSnap.docs.map((d: any) => {
      const dt = d.data();
      if (dt.examId) return dt.examId;
      if (dt.legacyId && dt.legacyId.includes('_ST-')) return dt.legacyId.split('_ST-')[0];
      if (dt.attemptId && dt.attemptId.includes('_ST-')) return dt.attemptId.split('_ST-')[0];
      return null;
    })
  ].filter(Boolean));

  const now = new Date();
  const absentExamIds = new Set<string>();

  objAssignmentsSnap.docs.forEach((d: any) => {
    const data = d.data();
    const eid = data.examId;
    if (!eid || attemptedExamIds.has(eid)) return;
    if (data.examType === 'entrance') return;

    let endAt: Date | null = null;
    if (data.endAt) {
      endAt = data.endAt?.toDate ? data.endAt.toDate() : new Date(data.endAt);
    } else if (data.startAt) {
      const startAt = data.startAt?.toDate ? data.startAt.toDate() : new Date(data.startAt);
      endAt = new Date(startAt.getTime() + (data.duration || 60) * 60000);
    }

    // Only consider absent if the exam window has already closed in the past
    if (endAt && now > endAt) {
      absentExamIds.add(eid);
    }
  });

  subAssignmentsSnap.docs.forEach((d: any) => {
    const data = d.data();
    const eid = data.examId;
    if (!eid || attemptedExamIds.has(eid)) return;

    let endAt: Date | null = null;
    if (data.endAt) {
      endAt = data.endAt?.toDate ? data.endAt.toDate() : new Date(data.endAt);
    } else if (data.availableUntil) {
      endAt = data.availableUntil?.toDate ? data.availableUntil.toDate() : new Date(data.availableUntil);
    } else if (data.scheduledDate) {
      const todayDateStr = getDateKeyIST(now);
      if (data.scheduledDate < todayDateStr) {
        absentExamIds.add(eid);
      }
      return;
    }

    if (endAt && now > endAt) {
      absentExamIds.add(eid);
    }
  });

  const absentTopicCodes = new Set<string>();
  if (absentExamIds.size > 0) {
    const examIdsArr = Array.from(absentExamIds);
    const chunks = [];
    for (let i = 0; i < examIdsArr.length; i += 30) {
      chunks.push(examIdsArr.slice(i, i + 30));
    }
    const chunkResults = await Promise.all(chunks.map(chunk =>
      Promise.all([
        adminDb.collection('exams').where('__name__', 'in', chunk).get(),
        adminDb.collection('subjectiveExams').where('__name__', 'in', chunk).get().catch(() => ({ docs: [] } as any))
      ])
    ));

    chunkResults.forEach(([examsSnap, subExamsSnap]) => {
      examsSnap.docs.forEach((doc: any) => {
        const data = doc.data();
        if (data.questionCodes && Array.isArray(data.questionCodes)) {
          data.questionCodes.forEach((qc: string) => {
            const tc = deriveTopicCodeFromQuestionCode(qc);
            if (tc && tc.includes('-')) absentTopicCodes.add(tc);
          });
        }
        if (data.topicCode && data.topicCode.includes('-')) absentTopicCodes.add(data.topicCode);
        if (data.topicCodes && Array.isArray(data.topicCodes)) {
          data.topicCodes.forEach((tc: string) => {
            if (tc.includes('-')) {
              absentTopicCodes.add(tc);
            } else if (data.boardCode && data.class && data.subjectCode && data.chapterNumber) {
              absentTopicCodes.add(`${data.boardCode}-${data.class}-${data.subjectCode}-${data.chapterNumber}-${tc}`);
            }
          });
        }
      });
      subExamsSnap.docs.forEach((doc: any) => {
        const data = doc.data();
        if (data.topicCode && data.topicCode.includes('-')) absentTopicCodes.add(data.topicCode);
        (data.topicCodes || data.topics || []).forEach((tc: string) => {
          if (tc && tc.includes('-')) absentTopicCodes.add(tc);
        });
      });
    });
  }

  // 3. Fetch standard syllabus topic index docs for all enrolled student classes (In-Memory Cached)
  let syllabusTopics: any[] = [];
  const classesArr = Array.from(allClasses).sort();
  const classKey = `syllabus_topics_${classesArr.join('_')}`;
  let cachedTopics = getFromCache<any[]>(classKey);

  if (cachedTopics) {
    syllabusTopics = cachedTopics;
  } else {
    if (classesArr.length > 0) {
      const classChunks = [];
      for (let i = 0; i < classesArr.length; i += 10) {
        classChunks.push(classesArr.slice(i, i + 10));
      }
      const sSnaps = await Promise.all(classChunks.map(chunk =>
        adminDb.collection('syllabusTopicIndex')
          .where('classCode', 'in', chunk)
          .get()
      ));
      sSnaps.forEach(sSnap => {
        sSnap.docs.forEach((doc: any) => syllabusTopics.push(doc.data()));
      });
    }

    // Fallback if no topics match
    if (syllabusTopics.length === 0) {
      const syllabusTopicsSnap = await adminDb.collection('syllabusTopicIndex').limit(500).get();
      syllabusTopics = syllabusTopicsSnap.docs.map((doc: any) => doc.data());
    }

    if (syllabusTopics.length > 0) {
      setInCache(classKey, syllabusTopics, 300000); // 5 minutes in-memory cache
    }
  }

  // Populate masteryMap
  const masteryMap = new Map<string, any>();
  masterySnaps.docs.forEach(doc => {
    const data = doc.data();
    if (data.topicCode) {
      masteryMap.set(data.topicCode, data);
    }
  });

  // Check for topic codes present in mastery or absent exams but missing in syllabus topics
  const currentTopicCodes = new Set(syllabusTopics.map((t: any) => t.topicCode).filter(Boolean));
  const missingTopicCodes: string[] = [];
  masteryMap.forEach((_, tCode) => {
    if (!currentTopicCodes.has(tCode)) {
      missingTopicCodes.push(tCode);
    }
  });
  absentTopicCodes.forEach(tCode => {
    if (!currentTopicCodes.has(tCode)) {
      missingTopicCodes.push(tCode);
    }
  });

  if (missingTopicCodes.length > 0) {
    // Fetch missing syllabus details in chunks of 30 (Firestore IN operator limit) in parallel
    const missingChunks = [];
    for (let i = 0; i < missingTopicCodes.length; i += 30) {
      missingChunks.push(missingTopicCodes.slice(i, i + 30));
    }
    const extraSnaps = await Promise.all(missingChunks.map(chunk =>
      adminDb.collection('syllabusTopicIndex')
        .where('topicCode', 'in', chunk)
        .get()
    ));
    extraSnaps.forEach(extraSnap => {
      extraSnap.docs.forEach((doc: any) => {
        syllabusTopics.push(doc.data());
      });
    });
  }

  const practiceCountMap = new Map<string, number>();
  parentReviewsSnap.docs.forEach(doc => {
    const tCode = doc.data().topicCode;
    if (tCode) {
      practiceCountMap.set(tCode, (practiceCountMap.get(tCode) || 0) + 1);
    }
  });

  const needsAttention: any[] = [];
  const continuePractice: any[] = [];
  const revision: any[] = [];
  const mastered: any[] = [];
  const processedTopics = new Set<string>();

  syllabusTopics.forEach(sData => {
    const topicCode = sData.topicCode;
    if (!topicCode || processedTopics.has(topicCode)) return;
    processedTopics.add(topicCode);

    const isAbsentExam = absentTopicCodes.has(topicCode);
    const mData = masteryMap.get(topicCode);
    if (!mData && !isAbsentExam) return;

    const mastery = mData?.hasOwnProperty('mastery') ? Number(mData.mastery || 0) : 0;
    const confidence = mData?.hasOwnProperty('confidence') ? Number(mData.confidence || 0) : 0;
    const priorityScore = isAbsentExam ? 999 : calculatePriority(mastery, confidence);
    const state = getTopicState(mastery, confidence);
    const practiceCount = practiceCountMap.get(topicCode) || 0;
    const isRecoveryMastered = !!mData?.isRecoveryMastered;
    const attempts = mData?.questionsAttempted || mData?.attempts || 0;
    const subCode = sData.subjectCode || (topicCode ? topicCode.split('-')[2] : '') || '';
    const subName = sData.subjectName || getCanonicalSubjectName(subCode, topicCode, sData.chapterName);

    const targetQuestions = Number(sData.targetQuestions || sData.totalQuestions || sData.questionCount || 30);

    const topicItem = {
      topicCode,
      topicName: sData.topicName || mData?.topicName || '',
      topicNumber: sData.topicNumber || mData?.topicNumber || '',
      chapterCode: sData.chapterCode || '',
      chapterName: sData.chapterName || 'General',
      chapterNumber: sData.chapterNumber || '',
      subjectCode: subCode,
      subjectName: subName,
      mastery,
      confidence,
      priorityScore,
      isAbsentExam,
      isRecoveryMastered,
      lastAttempt: mData?.updatedAt?.toDate ? mData.updatedAt.toDate().toISOString() : mData?.updatedAt || mData?.lastAttempt || null,
      attempts,
      lastScore: mData?.lastScore || 0,
      practiceCount,
      targetQuestions,
      totalQuestions: targetQuestions
    };

    // A topic is truly in Focus only if mastery is low (<50) or if the student has never attempted it (attempts === 0) and missed an assigned exam.
    // If a student already has >=50% mastery on a topic, historical absent exams do not override their progress.
    if (mastery < 50 || (attempts === 0 && isAbsentExam)) {
      needsAttention.push({ ...topicItem, state: 'needsAttention' });
    } else if (mastery < 90) {
      continuePractice.push({ ...topicItem, state: 'continuePractice' });
    } else {
      if ((mastery >= 90 && confidence >= 20) || isRecoveryMastered) {
        mastered.push({ ...topicItem, state: 'mastered' });
      } else {
        revision.push({ ...topicItem, state: 'revision' });
      }
    }
  });

  const sortFn = (a: any, b: any) => b.priorityScore - a.priorityScore;
  needsAttention.sort(sortFn);
  continuePractice.sort(sortFn);
  revision.sort(sortFn);
  mastered.sort(sortFn);

  const result = {
    studentCode,
    needsAttention,
    continuePractice,
    revision,
    mastered
  };

  setInCache(cacheKey, result, 120000); // 2 mins cache
  return result;
}
