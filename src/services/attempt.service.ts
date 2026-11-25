import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { EvaluationService } from './evaluation.service';
import { MasteryService } from './mastery.service';
import { IntegrityService } from './integrity.service';
import { AttemptRepository } from '@/repositories/attempt.repository';
import { ProctoringViolations, QuestionDetail, ExamAttempt } from '@/types/attempt.types';
import { deriveTopicCodeFromQuestionCode, isMultipleChoiceType, parseAnswerList, resolveOptionDisplayText, getOptionText, toCanonicalQuestionType, CANONICAL_OBJECTIVE_TYPES } from '@/lib/questionTypes';
import { invalidateCache } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { getMidnightIST } from '@/lib/dateUtils';

export class AttemptService {
  /**
   * Evaluates and submits a student exam attempt. Orchestrates grading, mastery calculations,
   * proctoring integrity scores, and class assignment completions within a transaction.
   */
  static async submitAttempt(params: {
    studentCode: string;
    studentId: string;
    studentName: string;
    examId: string;
    examData: any;
    questions: any[];
    userAnswers: any[];
    durationSpent: number;
    tabViolations: number;
    proctoringViolations: ProctoringViolations;
    startedAt: string | null;
    assignmentsSnap: admin.firestore.QuerySnapshot | null;
    proctoringViolationTriggered?: boolean;
    micBypassed?: boolean;
    violations?: any;
    abandoned?: boolean;
    disputedQuestionIds?: string[];
    isLate?: boolean;
    proctoringSnapshots?: any[];
  }): Promise<{
    alreadySubmitted: boolean;
    score: number;
    totalMarks: number;
    percentage: number;
    examSubject: string;
    examChapter: string;
    wrongAnswers: any[];
    unattemptedQuestions: any[];
    questionDetails?: any[];
    status: string;
  }> {
    const {
      studentCode,
      studentId,
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
      proctoringViolationTriggered,
      micBypassed,
      violations,
      abandoned,
      disputedQuestionIds = [],
      isLate: passedIsLate,
      proctoringSnapshots: incomingSnapshots
    } = params;

    const disputedSet = new Set((disputedQuestionIds || []).map(id => String(id).trim().toLowerCase()));

    let score = 0;
    let totalMarks = 0;
    const negativePerWrong = Number(examData.negativeMarks) || 0;
    const wrongAnswers: any[] = [];
    const unattempted: any[] = [];
    const questionDetails: QuestionDetail[] = [];
    const questionEvaluations: any[] = [];

    // 1. Evaluate answers using EvaluationService
    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      const submitted = userAnswers[i];
      const ans = submitted?.answer || '';
      
      const isDisputed = disputedSet.has(String(q.id || '').toLowerCase()) || 
                         disputedSet.has(String(q.questionCode || '').toLowerCase());

      const isMultiple = isMultipleChoiceType(q.type);
      let correctAnswer = isMultiple
        ? (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 
            ? q.correctAnswers 
            : (Array.isArray(q.correctAnswer) ? q.correctAnswer : (q.correctAnswer !== undefined && q.correctAnswer !== null ? parseAnswerList(q.correctAnswer) : [])))
        : (q.correctAnswer !== undefined && q.correctAnswer !== null && q.correctAnswer !== ''
            ? q.correctAnswer 
            : (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 ? q.correctAnswers[0] : ''));

      // Invariant: In multi-choice questions, if correctAnswer in DB has fewer options than options marked isCorrect, infer from options
      if (isMultiple && Array.isArray(q.options) && q.options.length > 0) {
        const fromOpts = q.options
          .map((opt: any, idx: number) => (opt && typeof opt === 'object' && (opt.isCorrect || opt.correct)) ? String.fromCharCode(65 + idx) : null)
          .filter(Boolean);
        if (fromOpts.length > 1 && (!Array.isArray(correctAnswer) || correctAnswer.length <= 1)) {
          correctAnswer = fromOpts;
        }
      }

      const isAttempted = ans && ans !== '' && ans !== '[]' && ans !== '{}';
      
      let isCorrect = false;
      if (isAttempted && !isDisputed) {
        isCorrect = EvaluationService.evaluate(q.type || 'OSC', ans, correctAnswer, q.options);
      }

      const timeSpentSeconds = submitted?.timeSpentSeconds || 0;
      const isObj = !q.type || CANONICAL_OBJECTIVE_TYPES.includes(toCanonicalQuestionType(q.type));
      const examPos = Number(examData.positiveMarks);
      const qMarks = (isObj && examPos > 0) ? examPos : (q.marks || examPos || 4);

      const userAnsText = isAttempted ? getOptionText(q, ans) : '';
      const correctAnsText = getOptionText(q, correctAnswer ?? '');

      questionDetails.push({
        id: q.id || '',
        questionId: q.id || '',
        questionCode: q.questionCode || '',
        questionText: q.text || '',
        type: q.type || 'OSC',
        options: q.options || [],
        solution: q.solution || q.explanation || '',
        userAnswer: userAnsText,
        rawAnswer: isAttempted ? ans : '',
        isDisputed,
        correctAnswer: correctAnsText,
        isAttempted: !!isAttempted,
        isCorrect: isCorrect,
        timeSpentSeconds: timeSpentSeconds,
        marks: isDisputed ? 0 : qMarks
      });

      if (q.questionCode) {
        let topicCode = q.topicCode || '';
        if (!topicCode) {
          topicCode = deriveTopicCodeFromQuestionCode(String(q.questionCode));
        }

        questionEvaluations.push({
          id: q.id,
          questionCode: q.questionCode,
          topicCode: topicCode,
          difficulty: q.difficulty ?? 'medium',
          bloomLevel: q.bloomLevel ?? 'Understand',
          isCorrect: isCorrect,
          isDisputed: isDisputed
        });
      }

      if (isDisputed) {
        // Excluded from scoring and unattempted/wrong lists completely
        continue;
      }

      totalMarks += qMarks;

      if (!isAttempted) {
        unattempted.push({ qIndex: i, questionText: q.text || '', correctAnswer: correctAnsText });
      } else if (isCorrect) {
        score += qMarks;
      } else {
        wrongAnswers.push({ qIndex: i, questionText: q.text || '', userAnswer: userAnsText, correctAnswer: correctAnsText });
        score -= negativePerWrong;
      }
    }

    // Negative marks awarded across all classes per grading policy
    const finalTotalMarks = totalMarks > 0 ? totalMarks : (examData.totalMarks || 1);
    const percentage = parseFloat(((score / finalTotalMarks) * 100).toFixed(1));

    const examSubject = examData.subject || questions[0]?.subject || 'General';
    const examChapter = examData.chapter || questions[0]?.chapter || 'General Chapter';

    // Setup Document references
    const attemptRef = adminDb.collection('examAttempts').doc(`${examId}_${studentCode}`);
    const reviewRef = adminDb.collection('reviews').doc(`${examId}_${studentCode}`);
    const userRef = studentId ? adminDb.collection('users').doc(studentId) : null;

    // Group topic masteries
    const topicBuckets: { [key: string]: any[] } = {};
    questionEvaluations.forEach(ev => {
      if (ev.topicCode) {
        if (!topicBuckets[ev.topicCode]) topicBuckets[ev.topicCode] = [];
        topicBuckets[ev.topicCode].push(ev);
      }
    });

    const now = new Date();
    const { year, week } = IntegrityService.getWeekDetails(now);
    const integrityRef = studentCode
      ? adminDb.collection('integrityScores').doc(`${studentCode}_${year}_${week}`)
      : null;

    // Execute atomic transaction
    const result = await adminDb.runTransaction(async (tx) => {
      // Step A: Idempotency Lock Check
      const attemptSnap = await tx.get(attemptRef);
      if (attemptSnap.exists) {
        const data = attemptSnap.data()!;
        if (data.status !== 'in-progress' && data.status !== 'precheck') {
          return {
            alreadySubmitted: true,
            score: data.score,
            totalMarks: data.totalMarks,
            percentage: data.percentage,
            examSubject: data.subject,
            examChapter: data.chapter,
            wrongAnswers: [],
            unattemptedQuestions: [],
            questionDetails: data.questionDetails || [],
            status: data.status || 'approved'
          };
        }
      }

      // Step A.1: Authoritative Server-Side Duration Verification
      let effectiveStartedAt: Date | null = null;
      const docStartedAt = attemptSnap.exists ? attemptSnap.data()?.startedAt : null;
      if (docStartedAt) {
        effectiveStartedAt = docStartedAt.toDate ? docStartedAt.toDate() : new Date(docStartedAt);
      } else if (startedAt) {
        effectiveStartedAt = new Date(startedAt);
      }

      let authoritativeDurationMinutes = Number(examData.duration) || 30;
      if (assignmentsSnap && !assignmentsSnap.empty) {
        const aData = assignmentsSnap.docs[0].data();
        if (aData?.examDuration && Number(aData.examDuration) > 0) {
          authoritativeDurationMinutes = Number(aData.examDuration);
        } else if (aData?.classroomDuration && Number(aData.classroomDuration) > 0) {
          authoritativeDurationMinutes = Number(aData.classroomDuration);
        }
      }
      const examDurationSeconds = authoritativeDurationMinutes * 60;
      let authoritativeDurationSpent = durationSpent || 0;
      let isOvertime = false;

      if (effectiveStartedAt && !isNaN(effectiveStartedAt.getTime())) {
        const serverElapsedSeconds = Math.max(0, Math.round((Date.now() - effectiveStartedAt.getTime()) / 1000));
        const maxAllowableSeconds = examDurationSeconds + 120; // 120s grace period for client network/rendering
        
        if (serverElapsedSeconds > maxAllowableSeconds) {
          isOvertime = true;
          authoritativeDurationSpent = examDurationSeconds;
        } else {
          authoritativeDurationSpent = Math.min(serverElapsedSeconds, Math.max(durationSpent || 0, serverElapsedSeconds));
        }
      } else {
        authoritativeDurationSpent = Math.min(durationSpent || examDurationSeconds, examDurationSeconds);
      }

      // Step B: Read student profile to check for autonomous mode setting
      let isAutonomous = false;
      if (userRef) {
        const userSnap = await tx.get(userRef);
        if (userSnap.exists) {
          isAutonomous = userSnap.data()?.autonomous === true;
        }
      }

      // Step C: Read Topic Masteries in parallel (skip for entrance, mock, foundation, or exempt exams)
      const isMasteryExempt = examData.examType === 'entrance' ||
                              examData.examCategory === 'mock' ||
                              examData.examCategory === 'foundation' ||
                              examData.vault === 'mock' ||
                              examData.vault === 'foundation' ||
                              examData.isMasteryExempt === true ||
                              examData.isMock === true;

      const topicMasteryRefs = isMasteryExempt ? [] : Object.keys(topicBuckets).map(tCode => ({
        tCode,
        ref: adminDb.collection('studentTopicMastery').doc(`${studentCode}_${tCode}`)
      }));
      const topicMasterySnaps = await Promise.all(topicMasteryRefs.map(m => tx.get(m.ref)));

      // Step D: Read Integrity Scores
      let integrityData: any = null;
      if (integrityRef) {
        const integritySnap = await tx.get(integrityRef);
        if (integritySnap.exists) {
          integrityData = integritySnap.data();
        }
      }

      // --- WRITES CASCADE ---
      const { integrityScore } = IntegrityService.calculateScore(tabViolations, proctoringViolations);
      const suspiciousLevel = (integrityScore < 70 || proctoringViolationTriggered) ? 'red' : (integrityScore < 90 ? 'yellow' : 'green');

      // Check if student started late (> 2 minutes after scheduled startAt)
      let isLate = Boolean(passedIsLate);
      let lateMinutes = 0;

      if (assignmentsSnap && !assignmentsSnap.empty) {
        const assignDoc = assignmentsSnap.docs.find(d => {
          const aData = d.data();
          return aData && (aData.openMode === 'scheduled' || aData.startAt);
        });
        if (assignDoc) {
          const aData = assignDoc.data();
          const scheduledStart = aData.startAt?.toDate ? aData.startAt.toDate() : (aData.startAt ? new Date(aData.startAt) : null);
          if (effectiveStartedAt && scheduledStart && !isNaN(effectiveStartedAt.getTime()) && !isNaN(scheduledStart.getTime())) {
            const delayMs = effectiveStartedAt.getTime() - scheduledStart.getTime();
            if (delayMs > 2 * 60 * 1000) {
              isLate = true;
              lateMinutes = Math.floor(delayMs / 60000);
            }
          }
        }
      }

      // Normalize and sanitize proctoring snapshots (max 5, <= 80KB each, supporting both object and string base64)
      let sanitizedViolations = violations;
      const candidateSnaps = (Array.isArray(incomingSnapshots) && incomingSnapshots.length > 0)
        ? incomingSnapshots
        : (violations?.screenshots || violations?.proctoringSnapshots || []);

      const rawSnapshots = (Array.isArray(candidateSnaps) ? candidateSnaps : [])
        .slice(-5)
        .map((s: any, idx: number) => {
          if (!s) return null;
          if (typeof s === 'string') {
            if (s.length > 80000) return null;
            return {
              id: `snap_${Date.now()}_${idx}`,
              timestamp: new Date().toISOString(),
              type: 'audit',
              reason: 'Proctoring snapshot',
              imageBase64: s,
              imageData: s
            };
          }
          if (typeof s === 'object') {
            const img = s.imageBase64 || s.imageData;
            if (typeof img !== 'string' || img.length > 80000) return null;
            return {
              id: s.id || `snap_${Date.now()}_${idx}`,
              timestamp: s.timestamp || new Date().toISOString(),
              type: s.type || 'audit',
              reason: s.reason || 'Proctoring snapshot',
              imageBase64: img,
              imageData: img
            };
          }
          return null;
        })
        .filter(Boolean);

      if (sanitizedViolations && typeof sanitizedViolations === 'object') {
        const { screenshots, proctoringSnapshots: vSnaps, ...restViolations } = sanitizedViolations;
        sanitizedViolations = restViolations;
      }

      // Write 1. Create Exam Attempt using AttemptRepository in tx
      const attemptData = {
        examId: examId,
        examName: examData.name || 'Untitled Exam',
        examType: examData.examType || 'obj',
        examCategory: examData.examCategory || (isMasteryExempt ? 'mock' : 'standard'),
        isMasteryExempt: !!isMasteryExempt,
        subject: examSubject,
        chapter: examChapter,
        studentCode: studentCode,
        studentId: studentId,
        studentName: studentName,
        score: score,
        totalMarks: totalMarks,
        percentage: percentage,
        durationSpent: authoritativeDurationSpent,
        isOvertime: isOvertime,
        isLate: isLate,
        lateMinutes: lateMinutes,
        lateRemark: isLate ? 'LATE' : null,
        integrityScore: integrityScore,
        suspiciousLevel: suspiciousLevel,
        tabViolations: tabViolations || 0,
        status: 'completed',
        proctoringViolationTriggered: !!proctoringViolationTriggered,
        micAvailable: micBypassed !== undefined ? !micBypassed : true,
        violations: sanitizedViolations || null,
        ...(rawSnapshots.length > 0 ? {
          proctoringSnapshots: rawSnapshots,
          proctoringSnapshotsExpiresAt: getMidnightIST(new Date()).toISOString(),
          proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.delete()
        } : {}),
        completedAt: admin.firestore.FieldValue.serverTimestamp(),
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
        abandoned: abandoned ? true : admin.firestore.FieldValue.delete()
      };
      AttemptRepository.saveAttempt(examId, studentCode, attemptData, tx);

      // Write 2. Create Review results doc
      const reviewData = {
        examId: examId,
        examName: examData.name || 'Untitled Exam',
        examType: examData.examType || 'obj',
        examCategory: examData.examCategory || (isMasteryExempt ? 'mock' : 'standard'),
        isMasteryExempt: !!isMasteryExempt,
        subject: examSubject,
        chapter: examChapter,
        studentCode: studentCode,
        studentId: studentId,
        studentName: studentName,
        score: score,
        totalMarks: totalMarks,
        percentage: percentage,
        durationSpent: authoritativeDurationSpent,
        isOvertime: isOvertime,
        isLate: isLate,
        lateMinutes: lateMinutes,
        lateRemark: isLate ? 'LATE' : null,
        tabViolations: tabViolations || 0,
        proctoringViolations: proctoringViolations || { noFace: 0, multipleFaces: 0, lookingAway: 0, headMovement: 0 },
        wrongAnswers: wrongAnswers,
        unattemptedQuestions: unattempted,
        questionDetails: questionDetails,
        integrityScore: integrityScore,
        suspiciousLevel: suspiciousLevel,
        startedAt: startedAt ? new Date(startedAt) : null,
        completedAt: admin.firestore.FieldValue.serverTimestamp(),
        status: (wrongAnswers.length === 0 && unattempted.length === 0) ? (isAutonomous ? 'approved' : 'pending') : 'student_review',
        proctoringViolationTriggered: !!proctoringViolationTriggered,
        micAvailable: micBypassed !== undefined ? !micBypassed : true,
        violations: sanitizedViolations || null,
        ...(rawSnapshots.length > 0 ? {
          proctoringSnapshots: rawSnapshots,
          proctoringSnapshotsExpiresAt: getMidnightIST(new Date()).toISOString(),
          proctoringSnapshotsPurgedAt: admin.firestore.FieldValue.delete()
        } : {}),
        abandoned: abandoned ? true : admin.firestore.FieldValue.delete()
      };
      tx.set(reviewRef, reviewData, { merge: true });

      // Write 3. Update User lastExamUpdatedAt
      if (userRef) {
        tx.set(userRef, {
          lastExamUpdatedAt: admin.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
      }

      // Write 4. Update Topic Masteries
      topicMasteryRefs.forEach((m, idx) => {
        const snap = topicMasterySnaps[idx];
        const existing = snap.exists ? snap.data()! : null;
        
        const data = MasteryService.calculateTopicMasteryUpdate(
          existing ? { ...existing } : {
            studentCode,
            topicCode: m.tCode,
            mastery: 0,
            confidence: 0,
            questionsAttempted: 0,
            questionsCorrect: 0,
            questionsWrong: 0,
            weightedPointsEarned: 0,
            weightedPointsPossible: 0,
            lastExamCode: '',
            questionHistory: [] as any[],
            createdAt: new Date()
          },
          topicBuckets[m.tCode],
          examId
        );

        tx.set(m.ref, data, { merge: true });
      });

      // Write 5. Update Proctoring Integrity Score
      if (integrityRef) {
        const { integrityScore } = IntegrityService.calculateScore(tabViolations, proctoringViolations);

        tx.set(integrityRef, {
          studentCode,
          year,
          week,
          integrityScore: integrityScore,
          violationsCount: (tabViolations || 0) + (proctoringViolations?.noFace || 0) + (proctoringViolations?.lookingAway || 0) + (proctoringViolations?.multipleFaces || 0) + (proctoringViolations?.headMovement || 0),
          weekStart: admin.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
      }

      // Write 6. Update Assignment doc statuses to completed (only if student-specific assignment)
      if (assignmentsSnap) {
        assignmentsSnap.docs.forEach(doc => {
          const data = doc.data();
          const isStudentSpecific = Array.isArray(data.targetStudents) && data.targetStudents.includes(studentCode) && data.targetStudents.length === 1;
          if (isStudentSpecific) {
            tx.update(doc.ref, {
              status: 'completed',
              completedAt: admin.firestore.FieldValue.serverTimestamp()
            });
          }
        });
      }

      return {
        alreadySubmitted: false,
        score,
        totalMarks,
        percentage,
        examSubject,
        examChapter,
        wrongAnswers,
        unattemptedQuestions: unattempted,
        questionDetails,
        status: (wrongAnswers.length === 0 && unattempted.length === 0) ? (isAutonomous ? 'approved' : 'pending') : 'student_review'
      };
    });

    // Invalidate caches for this student & admin dashboard stats
    try {
      invalidateCache(studentCode);
      invalidateCache('admin_dashboard_');
      invalidateCache('topic-coverage');
    } catch (e) {}

    return result;
  }

  /**
   * Automatically re-grades and updates existing reviews, examAttempts, and topic mastery
   * whenever a question in the Question Bank is edited.
   */
  static async regradeQuestionAcrossSubmissions(
    questionDoc: any,
    previousId?: string
  ): Promise<{ updatedExams: number; updatedReviews: number; updatedAttempts: number }> {
    const finalCode = String(questionDoc?.questionCode || '').trim();
    if (!finalCode) return { updatedExams: 0, updatedReviews: 0, updatedAttempts: 0 };

    const matchCodes = new Set<string>([finalCode]);
    if (previousId && previousId !== finalCode) {
      matchCodes.add(String(previousId).trim());
    }
    const matchCodesLower = new Set(Array.from(matchCodes).map(c => c.toLowerCase()));

    // 1. Find all exams referencing this question via questionCodes
    const examQueries = Array.from(matchCodes).map(code =>
      adminDb.collection('exams').where('questionCodes', 'array-contains', code).get()
    );
    const examSnaps = await Promise.all(examQueries);
    const examDocsMap = new Map<string, FirebaseFirestore.QueryDocumentSnapshot>();
    examSnaps.forEach(snap => snap.docs.forEach(d => examDocsMap.set(d.id, d)));

    if (examDocsMap.size === 0) {
      return { updatedExams: 0, updatedReviews: 0, updatedAttempts: 0 };
    }

    const qType = questionDoc.type || 'OSC';
    const isMultiple = isMultipleChoiceType(qType);
    let canonicalCorrect: any = isMultiple
      ? (Array.isArray(questionDoc.correctAnswers) && questionDoc.correctAnswers.length > 0
          ? questionDoc.correctAnswers
          : (Array.isArray(questionDoc.correctAnswer)
              ? questionDoc.correctAnswer
              : (questionDoc.correctAnswer ? parseAnswerList(questionDoc.correctAnswer) : [])))
      : (questionDoc.correctAnswer !== undefined && questionDoc.correctAnswer !== null && questionDoc.correctAnswer !== ''
          ? questionDoc.correctAnswer
          : (Array.isArray(questionDoc.correctAnswers) && questionDoc.correctAnswers.length > 0 ? questionDoc.correctAnswers[0] : ''));

    if (isMultiple && Array.isArray(questionDoc.options) && questionDoc.options.length > 0) {
      const fromOpts = questionDoc.options
        .map((opt: any, idx: number) => (opt && typeof opt === 'object' && (opt.isCorrect || opt.correct)) ? String.fromCharCode(65 + idx) : null)
        .filter(Boolean);
      if (fromOpts.length > 1 && (!Array.isArray(canonicalCorrect) || canonicalCorrect.length <= 1)) {
        canonicalCorrect = fromOpts;
      }
    }

    const correctAnsText = getOptionText(questionDoc, canonicalCorrect ?? '');
    const isObj = !qType || CANONICAL_OBJECTIVE_TYPES.includes(toCanonicalQuestionType(qType));
    const topicCode = questionDoc.topicCode || deriveTopicCodeFromQuestionCode(finalCode);

    const batch = new ChunkedBatch(adminDb);
    let updatedExams = 0;
    let updatedReviews = 0;
    let updatedAttempts = 0;
    const studentsToRecalcMastery = new Set<string>();
    const cachePatternsToInvalidate = new Set<string>();

    for (const [examId, examSnap] of examDocsMap.entries()) {
      const examData = examSnap.data() || {};
      const examPos = Number(examData.positiveMarks);
      const negativePerWrong = Number(examData.negativeMarks) || 0;
      const qMarks = (isObj && examPos > 0) ? examPos : (questionDoc.marks || examPos || 4);

      // Update exam document if questionCode was renamed or embedded questions exist
      const examUpdates: Record<string, any> = {};
      if (previousId && previousId !== finalCode && Array.isArray(examData.questionCodes)) {
        examUpdates.questionCodes = examData.questionCodes.map((c: string) => (c === previousId ? finalCode : c));
      }
      if (Array.isArray(examData.questions)) {
        let embeddedChanged = false;
        const updatedEmbedded = examData.questions.map((eq: any) => {
          const eqId = String(eq?.questionCode || eq?.id || '').trim().toLowerCase();
          if (matchCodesLower.has(eqId)) {
            embeddedChanged = true;
            return {
              ...eq,
              id: finalCode,
              questionCode: finalCode,
              text: questionDoc.text,
              type: qType,
              options: questionDoc.options || [],
              correctAnswer: questionDoc.correctAnswer,
              correctAnswers: questionDoc.correctAnswers || [],
              solution: questionDoc.solution || '',
              marks: qMarks,
            };
          }
          return eq;
        });
        if (embeddedChanged) examUpdates.questions = updatedEmbedded;
      }
      if (Object.keys(examUpdates).length > 0) {
        examUpdates.updatedAt = admin.firestore.FieldValue.serverTimestamp();
        batch.update(examSnap.ref, examUpdates);
        updatedExams++;
      }

      // 2. Fetch and re-grade all reviews for this exam
      const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', examId).get();
      if (reviewsSnap.empty) continue;

      cachePatternsToInvalidate.add(examId);

      for (const revDoc of reviewsSnap.docs) {
        const revData = revDoc.data() || {};
        const qDetails: any[] = Array.isArray(revData.questionDetails) ? revData.questionDetails : [];
        let matchedThisReview = false;
        let masteryRelevantChange = false;

        const updatedDetails = qDetails.map((qd: any) => {
          const qdIds = [qd.questionCode, qd.questionId, qd.id]
            .filter(Boolean)
            .map((v: any) => String(v).trim().toLowerCase());
          if (!qdIds.some(v => matchCodesLower.has(v))) {
            return qd;
          }

          matchedThisReview = true;
          const prevIsCorrect = !!qd.isCorrect;
          const prevIsDisputed = !!qd.isDisputed;

          const hasRaw = qd.rawAnswer !== undefined && qd.rawAnswer !== null && String(qd.rawAnswer).trim() !== '';
          const hasDisplayAns = qd.userAnswer && qd.userAnswer !== '[Reported / Disputed]' && String(qd.userAnswer).trim() !== '';
          const ansToEval = hasRaw ? qd.rawAnswer : (hasDisplayAns ? qd.userAnswer : '');

          let nextIsDisputed = prevIsDisputed;
          let nextIsCorrect = false;
          let nextUserAnswer = qd.userAnswer || '';
          let nextMarks = qMarks;

          if (prevIsDisputed && !hasRaw) {
            // Legacy disputed question without preserved rawAnswer: keep excluded, refresh text/options/solution
            nextIsDisputed = true;
            nextIsCorrect = false;
            nextMarks = 0;
          } else {
            nextIsDisputed = false;
            if (ansToEval !== '' && ansToEval !== '[]' && ansToEval !== '{}') {
              nextIsCorrect = EvaluationService.evaluate(qType, ansToEval, canonicalCorrect, questionDoc.options);
              nextUserAnswer = hasRaw ? getOptionText(questionDoc, ansToEval) : qd.userAnswer;
            } else {
              nextIsCorrect = false;
            }
          }

          if (prevIsCorrect !== nextIsCorrect || prevIsDisputed !== nextIsDisputed) {
            masteryRelevantChange = true;
          }

          return {
            ...qd,
            id: finalCode,
            questionId: finalCode,
            questionCode: finalCode,
            questionText: questionDoc.text || qd.questionText || '',
            type: qType,
            options: questionDoc.options || [],
            solution: questionDoc.solution || '',
            correctAnswer: correctAnsText,
            userAnswer: nextUserAnswer,
            isCorrect: nextIsCorrect,
            isDisputed: nextIsDisputed,
            marks: nextMarks,
          };
        });

        if (!matchedThisReview) continue;

        // Recompute review totals from updatedDetails
        let newScore = 0;
        let newTotalMarks = 0;
        const newWrongAnswers: any[] = [];
        const newUnattempted: any[] = [];

        updatedDetails.forEach((qd: any, idx: number) => {
          if (qd.isDisputed) return;
          const m = Number(qd.marks) || qMarks;
          newTotalMarks += m;
          if (!qd.isAttempted) {
            newUnattempted.push({ qIndex: idx, questionText: qd.questionText || '', correctAnswer: qd.correctAnswer });
          } else if (qd.isCorrect) {
            newScore += m;
          } else {
            if (negativePerWrong > 0) newScore -= negativePerWrong;
            newWrongAnswers.push({
              questionText: qd.questionText || '',
              userAnswer: qd.userAnswer || '',
              correctAnswer: qd.correctAnswer,
            });
          }
        });

        const newPercentage = newTotalMarks > 0 ? Math.max(0, Math.round((newScore / newTotalMarks) * 100)) : 0;

        batch.update(revDoc.ref, {
          questionDetails: updatedDetails,
          score: newScore,
          totalMarks: newTotalMarks,
          percentage: newPercentage,
          wrongAnswers: newWrongAnswers,
          unattemptedQuestions: newUnattempted,
          regradedAt: admin.firestore.FieldValue.serverTimestamp(),
        });
        updatedReviews++;

        const sCode = revData.studentCode;
        if (sCode) {
          cachePatternsToInvalidate.add(sCode);
          if (masteryRelevantChange) {
            studentsToRecalcMastery.add(sCode);
          }
          const attemptRef = adminDb.collection('examAttempts').doc(`${examId}_${sCode}`);
          batch.set(attemptRef, {
            score: newScore,
            totalMarks: newTotalMarks,
            percentage: newPercentage,
            regradedAt: admin.firestore.FieldValue.serverTimestamp(),
          }, { merge: true });
          updatedAttempts++;
        }
      }
    }

    await batch.commit();

    // 3. Recalculate studentTopicMastery for students whose correctness/dispute status changed
    if (topicCode && studentsToRecalcMastery.size > 0) {
      await Promise.all(
        Array.from(studentsToRecalcMastery).map(sCode =>
          MasteryService.recalculateOrPurgeTopicsForStudent({
            studentCode: sCode,
            excludedExamId: '__none__',
            candidateTopicCodes: [topicCode],
          }).catch(err => console.warn(`Mastery recalc failed for ${sCode}:`, err))
        )
      );
    }

    // 4. Invalidate report & dashboard caches
    try {
      invalidateCache('admin_dashboard_');
      invalidateCache('topic-coverage');
      for (const pattern of cachePatternsToInvalidate) {
        invalidateCache(pattern);
        await ReportCacheManager.invalidatePattern(pattern);
      }
    } catch (e) {}

    return { updatedExams, updatedReviews, updatedAttempts };
  }
}
