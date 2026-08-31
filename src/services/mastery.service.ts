import { QuestionHistoryItem } from '@/types/user.types';
import { getDateKeyIST } from '@/lib/dateUtils';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { parseTopicCode, deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

export class MasteryService {
  /**
   * Helper to check if a class or topic code belongs to Class 10
   */
  static isClass10(studentClass?: string | number | null, topicCode?: string | null): boolean {
    if (studentClass !== undefined && studentClass !== null) {
      const str = String(studentClass).trim().toLowerCase();
      if (str === '10' || str === 'class 10' || str === 'class 10th' || str === '10th' || str === 'x' || str.includes('10')) {
        return true;
      }
    }
    if (topicCode) {
      const parsed = parseTopicCode(topicCode);
      if (parsed && (parsed.cls === '10' || parsed.classNum === '10')) {
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
      // Run in standalone batch write
      const batch = adminDb.batch();
      for (const tCode of topicCodes) {
        const ref = adminDb.collection('studentTopicMastery').doc(`${studentCode}_${tCode}`);
        const snap = await ref.get();
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
      }
      await batch.commit();
    }

    return { updatedCount: topicCodes.length, isClass10: true };
  }
}
