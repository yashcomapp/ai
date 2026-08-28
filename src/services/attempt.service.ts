import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { EvaluationService } from './evaluation.service';
import { MasteryService } from './mastery.service';
import { IntegrityService } from './integrity.service';
import { AttemptRepository } from '@/repositories/attempt.repository';
import { ProctoringViolations, QuestionDetail, ExamAttempt } from '@/types/attempt.types';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

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
  }): Promise<{
    alreadySubmitted: boolean;
    score: number;
    totalMarks: number;
    percentage: number;
    examSubject: string;
    examChapter: string;
    wrongAnswers: any[];
    unattemptedQuestions: any[];
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
      disputedQuestionIds = []
    } = params;

    const disputedSet = new Set((disputedQuestionIds || []).map(id => String(id).trim().toLowerCase()));

    let score = 0;
    let totalMarks = 0;
    const negativePerWrong = Number(examData.negativeMarks) || 0;
    const wrongAnswers: any[] = [];
    const unattempted: any[] = [];
    const questionDetails: QuestionDetail[] = [];
    const questionEvaluations: any[] = [];

    const getOptionTextHelper = (q: any, code: string) => {
      if (!q || !q.options || !Array.isArray(q.options)) return code;
      let cleanCode = code;
      try {
        if (code.startsWith('[') && code.endsWith(']')) {
          const parsed = JSON.parse(code);
          if (Array.isArray(parsed) && parsed.length > 0) {
            cleanCode = parsed[0];
          }
        }
      } catch {}
      const opt = q.options.find((o: any) => o.code === cleanCode || o.text === cleanCode);
      return opt ? opt.text : code;
    };

    // 1. Evaluate answers using EvaluationService
    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      const submitted = userAnswers[i];
      const ans = submitted?.answer || '';
      
      const isDisputed = disputedSet.has(String(q.id || '').toLowerCase()) || 
                         disputedSet.has(String(q.questionCode || '').toLowerCase());

      const correctAnswer = q.correctAnswer || q.correctAnswers;
      const isAttempted = ans && ans !== '' && ans !== '[]' && ans !== '{}';
      
      let isCorrect = false;
      if (isAttempted && !isDisputed) {
        isCorrect = EvaluationService.evaluate(q.type || 'single_mcq', ans, correctAnswer, q.options);
      }

      const timeSpentSeconds = submitted?.timeSpentSeconds || 0;
      const qMarks = q.marks || Number(examData.positiveMarks) || 4;

      const userAnsText = isAttempted ? getOptionTextHelper(q, ans) : '';
      const correctAnsText = getOptionTextHelper(q, correctAnswer ?? '');

      questionDetails.push({
        questionCode: q.questionCode || '',
        questionText: q.text || '',
        userAnswer: isDisputed ? '[Reported / Disputed]' : userAnsText,
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

    if (examData.examType !== 'entrance') {
      score = Math.max(0, score);
    }
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
    return await adminDb.runTransaction(async (tx) => {
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
            status: data.status || 'approved'
          };
        }
      }

      // Step B: Read student profile to check for autonomous mode setting
      let isAutonomous = false;
      if (userRef) {
        const userSnap = await tx.get(userRef);
        if (userSnap.exists) {
          isAutonomous = userSnap.data()?.autonomous === true;
        }
      }

      // Step C: Read Topic Masteries in parallel (skip for entrance exams)
      const topicMasteryRefs = examData.examType === 'entrance' ? [] : Object.keys(topicBuckets).map(tCode => ({
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

      // Write 1. Create Exam Attempt using AttemptRepository in tx
      const attemptData = {
        examId: examId,
        examName: examData.name || 'Untitled Exam',
        examType: examData.examType || 'obj',
        subject: examSubject,
        chapter: examChapter,
        studentCode: studentCode,
        studentId: studentId,
        studentName: studentName,
        score: score,
        totalMarks: totalMarks,
        percentage: percentage,
        durationSpent: durationSpent || 0,
        integrityScore: integrityScore,
        suspiciousLevel: suspiciousLevel,
        tabViolations: tabViolations || 0,
        status: 'completed',
        proctoringViolationTriggered: !!proctoringViolationTriggered,
        micAvailable: micBypassed !== undefined ? !micBypassed : true,
        violations: violations || null,
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
        subject: examSubject,
        chapter: examChapter,
        studentCode: studentCode,
        studentId: studentId,
        studentName: studentName,
        score: score,
        totalMarks: totalMarks,
        percentage: percentage,
        durationSpent: durationSpent || 0,
        tabViolations: tabViolations || 0,
        proctoringViolations: proctoringViolations || { noFace: 0, multipleFaces: 0, lookingAway: 0, headMovement: 0 },
        wrongAnswers: wrongAnswers,
        unattemptedQuestions: unattempted,
        questionDetails: questionDetails,
        integrityScore: integrityScore,
        suspiciousLevel: suspiciousLevel,
        startedAt: startedAt ? new Date(startedAt) : null,
        completedAt: admin.firestore.FieldValue.serverTimestamp(),
        status: isAutonomous ? 'approved' : ((wrongAnswers.length === 0 && unattempted.length === 0) ? 'pending' : 'student_review'),
        proctoringViolationTriggered: !!proctoringViolationTriggered,
        micAvailable: micBypassed !== undefined ? !micBypassed : true,
        violations: violations || null,
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
          violationsCount: (tabViolations || 0) + (proctoringViolations?.noFace || 0) + (proctoringViolations?.lookingAway || 0),
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
        status: (wrongAnswers.length === 0 && unattempted.length === 0) ? 'pending' : 'student_review'
      };
    });
  }
}
