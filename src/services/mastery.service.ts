import { QuestionHistoryItem } from '@/types/user.types';
import { getDateKeyIST } from '@/lib/dateUtils';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { parseTopicCode, deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { invalidateCache } from '@/lib/firebase/cache';

export class MasteryService {
  /**
   * Helper to check if a class or topic code belongs to Class 10
   */
  static isClass10(studentClass?: string | number | null, topicCode?: string | null): boolean {
    if (studentClass !== undefined && studentClass !== null) {
      if (String(studentClass).replace(/\D/g, '') === '10') {
        return true;
      }
    }
    if (topicCode) {
      const parsed = parseTopicCode(topicCode);
      if (parsed && (parsed.class === '10' || parsed.classNum === '10')) {
        return true;
      }
    }
    return false;
  }

  /**
   * Helper to calculate bloom taxonomy weights
   */
  static getBloomWeight(bloomLevel?: string): number {
    const bloomWeights: { [key: string]: number } = {
      Remember: 1,
      Understand: 2,
      Apply: 3,
      Analyze: 4,
      Evaluate: 5,
      Create: 6
    };
    return (bloomLevel && bloomWeights[bloomLevel]) ? bloomWeights[bloomLevel] : 2;
  }

  /**
   * Aggregates points and computes updated mastery values for a topic
   */
  static calculateTopicMasteryUpdate(
    existing: any,
    evaluations: {
      id: string;
      difficulty?: string;
      bloomLevel?: string;
      isCorrect?: boolean;
      marksAwarded?: number;
      maxMarks?: number;
      isDisputed?: boolean;
      examCategory?: string;
    }[],
    examId: string
  ): any {
    const data = { ...existing };
    let questionsAttemptedDelta = 0;
    let questionsCorrectDelta = 0;
    let questionsWrongDelta = 0;
    let weightedPointsPossibleDelta = 0;
    let weightedPointsEarnedDelta = 0;

    evaluations.forEach(ev => {
      if ((ev as any).isDisputed) return;

      const diffWeight = ev.difficulty === 'easy' ? 1 : (ev.difficulty === 'hard' ? 3 : 2);
      const bloomWeight = this.getBloomWeight(ev.bloomLevel || 'Understand');
      const weight = diffWeight * bloomWeight;
      const isFoundation = (ev as any).examCategory === 'foundation';

      questionsAttemptedDelta += 1;

      // Handle subjective partial credit or objective boolean isCorrect
      let earnedRatio: number;
      let isPassed: boolean;
      if (ev.marksAwarded !== undefined && ev.maxMarks !== undefined && ev.maxMarks > 0) {
        earnedRatio = Math.max(0, Math.min(1, ev.marksAwarded / ev.maxMarks));
        isPassed = earnedRatio >= 0.5;
      } else {
        isPassed = !!ev.isCorrect;
        earnedRatio = isPassed ? 1 : 0;
      }

      if (isPassed) {
        questionsCorrectDelta += 1;
      } else {
        questionsWrongDelta += 1;
      }

      weightedPointsEarnedDelta += weight * earnedRatio;
      if (isPassed || !isFoundation) {
        weightedPointsPossibleDelta += weight;
      } else {
        weightedPointsPossibleDelta += weight * 0.3;
      }
    });

    const isPractice = (examId || '').toUpperCase().includes('PRACTICE') || (examId || '').startsWith('ST-');
    if (isPractice) {
      data.practiceQuestionsAttempted = (data.practiceQuestionsAttempted || 0) + questionsAttemptedDelta;
      const todayIST = getDateKeyIST(new Date());
      if (data.lastPracticeDate === todayIST) {
        data.dailyPracticeSessionsCount = (data.dailyPracticeSessionsCount || 0) + 1;
      } else {
        data.lastPracticeDate = todayIST;
        data.dailyPracticeSessionsCount = 1;
      }
    } else {
      data.examQuestionsAttempted = (data.examQuestionsAttempted || 0) + questionsAttemptedDelta;
    }

    data.questionsAttempted = (data.questionsAttempted || 0) + questionsAttemptedDelta;
    data.questionsCorrect = (data.questionsCorrect || 0) + questionsCorrectDelta;
    data.questionsWrong = (data.questionsWrong || 0) + questionsWrongDelta;
    data.weightedPointsEarned = (data.weightedPointsEarned || 0) + weightedPointsEarnedDelta;
    data.weightedPointsPossible = (data.weightedPointsPossible || 0) + weightedPointsPossibleDelta;

    data.mastery = data.weightedPointsPossible > 0
      ? Math.round((data.weightedPointsEarned / data.weightedPointsPossible) * 100)
      : 0;
    data.confidence = Math.min(data.questionsAttempted, 100);

    // Update question seen history (excluding disputed questions)
    let questionHistory: QuestionHistoryItem[] = data.questionHistory || [];
    const seenAt = new Date();
    evaluations.forEach(ev => {
      if ((ev as any).isDisputed) return;
      const isPassed = (ev.marksAwarded !== undefined && ev.maxMarks !== undefined && ev.maxMarks > 0)
        ? (ev.marksAwarded / ev.maxMarks >= 0.5)
        : !!ev.isCorrect;
      questionHistory = questionHistory.filter(h => h.questionId !== ev.id);
      questionHistory.push({ questionId: ev.id, seenAt, wasCorrect: isPassed });
    });

    if (questionHistory.length > 100) {
      questionHistory = questionHistory.slice(-100);
    }
    data.questionHistory = questionHistory;

    data.lastExamCode = examId;
    data.updatedAt = new Date();

    return data;
  }

  /**
   * Processes and updates topic mastery for subjective exams, specifically for Class 10 students.
   */
  static async processSubjectiveMasteryUpdate(params: {
    studentCode: string;
    examId: string;
    questions: any[];
    questionReviews: { questionId: string; marksAwarded: number; maxMarks: number; feedback?: string }[];
    studentClass?: string;
    tx?: admin.firestore.Transaction;
  }): Promise<{ updatedCount: number; isClass10: boolean }> {
    const { studentCode, examId, questions, questionReviews, studentClass, tx } = params;
    if (!studentCode || !questionReviews || questionReviews.length === 0) {
      return { updatedCount: 0, isClass10: false };
    }

    // 1. Resolve student class if not provided
    let resolvedClass = studentClass;
    if (!resolvedClass) {
      try {
        const userSnap = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('studentCode', '==', studentCode)
          .limit(1)
          .get();
        if (!userSnap.empty) {
          resolvedClass = userSnap.docs[0].data()?.class;
        }
      } catch (err) {
        console.warn('Could not resolve student class for mastery:', err);
      }
    }

    // 2. Map questions for rapid lookup
    const questionMap = new Map<string, any>();
    if (Array.isArray(questions)) {
      questions.forEach((q: any) => {
        if (q) {
          if (q.id) questionMap.set(String(q.id), q);
          if (q.questionCode) questionMap.set(String(q.questionCode), q);
        }
      });
    }

    // 3. Filter and group evaluations by topicCode for Class 10
    const topicBuckets: { [topicCode: string]: any[] } = {};
    let studentOrTopicIsClass10 = MasteryService.isClass10(resolvedClass);

    questionReviews.forEach(qr => {
      const q = questionMap.get(String(qr.questionId)) || {};
      const qCode = q.questionCode || qr.questionId;
      let topicCode = q.topicCode || deriveTopicCodeFromQuestionCode(qCode);

      if (topicCode) {
        const isTopicClass10 = MasteryService.isClass10(resolvedClass, topicCode);
        if (isTopicClass10) {
          studentOrTopicIsClass10 = true;
          if (!topicBuckets[topicCode]) {
            topicBuckets[topicCode] = [];
          }
          topicBuckets[topicCode].push({
            id: qr.questionId,
            questionCode: qCode,
            topicCode: topicCode,
            difficulty: q.difficulty || 'medium',
            bloomLevel: q.bloomLevel || (q.type === 'subjective_long' ? 'Analyze' : 'Apply'),
            marksAwarded: Number(qr.marksAwarded) || 0,
            maxMarks: Number(qr.maxMarks) || q.marks || 2,
            isCorrect: (Number(qr.marksAwarded) || 0) >= ((Number(qr.maxMarks) || 2) * 0.5)
          });
        }
      }
    });

    if (!studentOrTopicIsClass10 || Object.keys(topicBuckets).length === 0) {
      return { updatedCount: 0, isClass10: studentOrTopicIsClass10 };
    }

    // 4. Update studentTopicMastery for each topic
    const topicCodes = Object.keys(topicBuckets);
    if (tx) {
      // Run inside existing Firestore Transaction
      const docRefs = topicCodes.map(tCode => ({
        tCode,
        ref: adminDb.collection('studentTopicMastery').doc(`${studentCode}_${tCode}`)
      }));
      const docSnaps = await Promise.all(docRefs.map(m => tx.get(m.ref)));

      docRefs.forEach((m, idx) => {
        const snap = docSnaps[idx];
        const existing = snap.exists ? snap.data()! : null;
        const initialData = existing ? { ...existing } : {
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
        };

        const updatedData = MasteryService.calculateTopicMasteryUpdate(
          initialData,
          topicBuckets[m.tCode],
          examId
        );

        tx.set(m.ref, updatedData, { merge: true });
      });
    } else {
      // Run in standalone batch write with batched read
      const docRefs = topicCodes.map(tCode => adminDb.collection('studentTopicMastery').doc(`${studentCode}_${tCode}`));
      const snaps = docRefs.length > 0 ? await adminDb.getAll(...docRefs) : [];
      const batch = adminDb.batch();

      snaps.forEach((snap, idx) => {
        const tCode = topicCodes[idx];
        const ref = docRefs[idx];
        const existing = snap.exists ? snap.data()! : null;
        const initialData = existing ? { ...existing } : {
          studentCode,
          topicCode: tCode,
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
        };

        const updatedData = MasteryService.calculateTopicMasteryUpdate(
          initialData,
          topicBuckets[tCode],
          examId
        );

        batch.set(ref, updatedData, { merge: true });
      });
      await batch.commit();
    }

    return { updatedCount: topicCodes.length, isClass10: true };
  }

  /**
   * Recalculates or completely purges studentTopicMastery records for a student when an exam is deleted or an attempt is reset.
   * If there are 0 surviving exam attempts or practice sessions for that topic, the studentTopicMastery document is DELETED.
   * If surviving attempts exist, the topic mastery is cleanly recalculated using only the surviving records.
   */
  static async recalculateOrPurgeTopicsForStudent(params: {
    studentCode: string;
    excludedExamId: string;
    candidateTopicCodes: string[];
  }): Promise<{ deletedCount: number; updatedCount: number }> {
    const { studentCode, excludedExamId, candidateTopicCodes } = params;
    if (!studentCode) return { deletedCount: 0, updatedCount: 0 };

    let deletedCount = 0;
    let updatedCount = 0;

    // 1. Fetch student's existing studentTopicMastery documents
    const masterySnap = await adminDb.collection('studentTopicMastery')
      .where('studentCode', '==', studentCode)
      .get();

    if (masterySnap.empty && candidateTopicCodes.length === 0) {
      return { deletedCount: 0, updatedCount: 0 };
    }

    // Identify candidate topics to inspect
    const targetTopics = new Set<string>(candidateTopicCodes.filter(Boolean));
    masterySnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.lastExamCode === excludedExamId) {
        if (data.topicCode) targetTopics.add(data.topicCode);
      }
    });

    if (targetTopics.size === 0) {
      return { deletedCount: 0, updatedCount: 0 };
    }

    // 2. Fetch all surviving objective reviews, subjective evaluations, and practice reviews in parallel
    const [objReviewsSnap, subjEvalsSnap, practicesSnap] = await Promise.all([
      adminDb.collection('reviews').where('studentCode', '==', studentCode).get(),
      adminDb.collection('evaluations').where('studentCode', '==', studentCode).get(),
      adminDb.collection('parentReviews').where('studentCode', '==', studentCode).where('type', '==', 'practice').get()
    ]);

    const survivingObjReviews = objReviewsSnap.docs
      .filter(d => d.data().examId !== excludedExamId && d.id !== `${excludedExamId}_${studentCode}`)
      .map(d => d.data());

    const survivingSubjEvals = subjEvalsSnap.docs
      .filter(d => d.data().examId !== excludedExamId && !d.id.startsWith(`${excludedExamId}_`))
      .map(d => d.data());

    const survivingPractices = practicesSnap.docs
      .filter(d => d.data().examId !== excludedExamId)
      .map(d => d.data());

    const existingMasteryByTopic = new Map<string, any>();
    masterySnap.docs.forEach(doc => {
      const d = doc.data();
      if (d.topicCode) existingMasteryByTopic.set(d.topicCode, { ref: doc.ref, data: d });
    });

    // 3. For each candidate topic, check for surviving evaluations
    for (const tCode of Array.from(targetTopics)) {
      const survivingEvaluations: Array<{
        id: string;
        difficulty?: string;
        bloomLevel?: string;
        isCorrect?: boolean;
        marksAwarded?: number;
        maxMarks?: number;
        isDisputed?: boolean;
        examCategory?: string;
      }> = [];

      let latestExamCode = '';

      // Check surviving objective reviews
      survivingObjReviews.forEach(rev => {
        const details = rev.questionDetails || [];
        details.forEach((qd: any) => {
          const qTopic = qd.topicCode || deriveTopicCodeFromQuestionCode(qd.questionCode);
          if (qTopic === tCode || (qTopic && qTopic.startsWith(tCode + '.'))) {
            survivingEvaluations.push({
              id: qd.id || qd.questionCode || `qd_${Math.random()}`,
              difficulty: qd.difficulty || 'medium',
              bloomLevel: qd.bloomLevel || 'Understand',
              isCorrect: !!qd.isCorrect,
              marksAwarded: qd.marks,
              maxMarks: qd.marks,
              isDisputed: !!qd.isDisputed,
              examCategory: rev.examCategory || 'standard'
            });
            if (rev.examId) latestExamCode = rev.examId;
          }
        });
      });

      // Check surviving subjective evaluations
      survivingSubjEvals.forEach(ev => {
        const qReviews = ev.questionReviews || [];
        qReviews.forEach((qr: any) => {
          const qTopic = qr.topicCode || deriveTopicCodeFromQuestionCode(qr.questionCode || qr.questionId);
          if (qTopic === tCode || (qTopic && qTopic.startsWith(tCode + '.'))) {
            const earnedRatio = (qr.maxMarks > 0) ? (qr.marksAwarded / qr.maxMarks) : 0;
            survivingEvaluations.push({
              id: qr.questionId || qr.questionCode || `qr_${Math.random()}`,
              difficulty: qr.difficulty || 'medium',
              bloomLevel: qr.bloomLevel || 'Understand',
              isCorrect: earnedRatio >= 0.5,
              marksAwarded: qr.marksAwarded,
              maxMarks: qr.maxMarks,
              isDisputed: false,
              examCategory: 'standard'
            });
            if (ev.examId) latestExamCode = ev.examId;
          }
        });
      });

      // Check surviving practice reviews
      survivingPractices.forEach(pr => {
        if (pr.topicCode === tCode || (pr.topicCode && pr.topicCode.startsWith(tCode + '.'))) {
          if (Array.isArray(pr.questionDetails) && pr.questionDetails.length > 0) {
            pr.questionDetails.forEach((qd: any) => {
              survivingEvaluations.push({
                id: qd.id || qd.questionCode || `pr_${Math.random()}`,
                difficulty: qd.difficulty || 'medium',
                bloomLevel: qd.bloomLevel || 'Understand',
                isCorrect: !!qd.isCorrect,
                marksAwarded: qd.marksAwarded ?? (qd.isCorrect ? 4 : 0),
                maxMarks: qd.maxMarks || 4,
                isDisputed: !!qd.isDisputed,
                examCategory: 'standard'
              });
            });
          } else {
            const qCount = Number(pr.questionsCount || pr.totalQuestions || 0);
            const scorePct = Number(pr.scorePercent || 0);
            const correctCount = Math.round((scorePct / 100) * qCount);
            for (let i = 0; i < qCount; i++) {
              survivingEvaluations.push({
                id: `pr_syn_${tCode}_${i}`,
                difficulty: 'medium',
                bloomLevel: 'Understand',
                isCorrect: i < correctCount,
                marksAwarded: i < correctCount ? 4 : 0,
                maxMarks: 4,
                isDisputed: false,
                examCategory: 'standard'
              });
            }
          }
        }
      });

      const existingEntry = existingMasteryByTopic.get(tCode);
      const masteryRef = existingEntry ? existingEntry.ref : adminDb.collection('studentTopicMastery').doc(`${studentCode}_${tCode}`);

      if (survivingEvaluations.length === 0) {
        // Zero surviving records: DELETE the document so the topic completely disappears
        if (existingEntry) {
          await masteryRef.delete();
          deletedCount++;
        }
      } else {
        // Recalculate using only surviving evaluations
        const existingData = existingEntry ? existingEntry.data : {};
        const baseline = {
          studentCode,
          topicCode: tCode,
          mastery: 0,
          confidence: 0,
          questionsAttempted: 0,
          questionsCorrect: 0,
          questionsWrong: 0,
          weightedPointsEarned: 0,
          weightedPointsPossible: 0,
          practiceQuestionsAttempted: 0,
          examQuestionsAttempted: 0,
          lastExamCode: latestExamCode,
          questionHistory: [] as any[],
          createdAt: existingData.createdAt || new Date(),
          topicName: existingData.topicName || '',
          chapterName: existingData.chapterName || '',
          topicClassification: existingData.topicClassification || 'medium'
        };

        const updated = MasteryService.calculateTopicMasteryUpdate(baseline, survivingEvaluations, latestExamCode);
        await masteryRef.set(updated, { merge: false });
        updatedCount++;
      }
    }

    // Invalidate caches for this student
    try {
      invalidateCache(studentCode);
      invalidateCache(`learning_data_${studentCode}`);
      invalidateCache(`student_dashboard_fn_${studentCode}`);
      invalidateCache(`student_results_${studentCode}`);
      invalidateCache(`parent_reviews_${studentCode}`);
    } catch {}

    return { deletedCount, updatedCount };
  }
}
