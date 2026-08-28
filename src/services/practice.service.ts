import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { evaluateQuestionAnswer, parseTopicCode } from '@/lib/questionTypes';
import { QuestionRepository } from '@/repositories/question.repository';
import { PracticeRepository } from '@/repositories/practice.repository';
import { TopicMasteryRecord, TopicRecommendation } from '@/types/practice.types';
import { IntegrityService } from '@/services/integrity.service';
import { MasteryService } from '@/services/mastery.service';
import { notifyReviewPending } from '@/lib/notifications';

const DIFFICULTY_WEIGHTS: Record<string, number> = { easy: 1, medium: 2, hard: 3 };
const BLOOM_WEIGHTS: Record<string, number> = {
  Remember: 1, Understand: 2, Apply: 3, Analyze: 4, Evaluate: 5, Create: 6
};

export class PracticeService {
  /**
   * Evaluates student mastery and topic data to recommend practice sets.
   */
  static getDifficultyDistribution(mastery: number, revisionMode: boolean, questionsAttempted?: number) {
    if (revisionMode) {
      return { easy: 20, medium: 30, hard: 50 };
    }
    // Challenging questions (100% hard) for practice should be given to any student who achieves mastery (>= 80) in less than 15 questions
    if (mastery >= 80 && questionsAttempted !== undefined && questionsAttempted < 15) {
      return { easy: 0, medium: 0, hard: 100 };
    }
    if (mastery < 30) return { easy: 70, medium: 30, hard: 0 };
    if (mastery < 60) return { easy: 50, medium: 50, hard: 0 };
    if (mastery < 85) return { easy: 20, medium: 50, hard: 30 };
    return { easy: 10, medium: 40, hard: 50 };
  }

  static getCategoryDistribution(category: string) {
    switch (category) {
      case 'needsAttention':
        return { new: 70, wrong: 30, correct: 0 };
      case 'continuePractice':
        return { new: 50, wrong: 50, correct: 0 };
      case 'revision':
        return { new: 20, wrong: 0, correct: 80 };
      default:
        return { new: 50, wrong: 50, correct: 0 };
    }
  }

  static getQuestionPriority(questionId: string, questionHistory: any[]) {
    const record = questionHistory.find(h => h.questionId === questionId);
    if (!record) return 1; // Never seen
    const seenAt = record.seenAt?.toDate ? record.seenAt.toDate() : new Date(record.seenAt);
    const seenDaysAgo = (Date.now() - seenAt.getTime()) / (1000 * 60 * 60 * 24);
    if (seenDaysAgo > 30) return 2; // Seen long ago
    if (!record.wasCorrect) return 3; // Seen recently but wrong
    return 4; // Seen recently and correct
  }

  static isQuestionEligible(questionId: string, questionHistory: any[]) {
    const record = questionHistory.find(h => h.questionId === questionId);
    if (!record) return true;
    const lastSeen = record.seenAt?.toDate ? record.seenAt.toDate() : new Date(record.seenAt);
    const daysSince = (Date.now() - lastSeen.getTime()) / (1000 * 60 * 60 * 24);
    return daysSince >= 30; // Cooldown days
  }

  static parseTopicCode = parseTopicCode;

  /**
   * Orchestrates the grading transaction and updates mastery states.
   */
  static async submitPracticeGrade(params: {
    studentCode: string;
    studentName: string;
    topicCode: string;
    category: string;
    answers: any[];
    durationSpent?: number;
    violations?: any;
    sessionId?: string;
    proctoringViolationTriggered?: boolean;
    isRecoveryMode?: boolean;
    disputedQuestionIds?: string[];
  }) {
    const { studentCode, studentName, topicCode, category, answers, durationSpent, violations, sessionId, proctoringViolationTriggered, isRecoveryMode, disputedQuestionIds = [] } = params;
    const disputedSet = new Set((disputedQuestionIds || []).map(id => String(id).trim().toLowerCase()));

    const questionIds = answers.map(a => a.questionId).filter(Boolean);
    if (!questionIds.length) {
      throw new Error('No questions submitted.');
    }
    const questionRefs = questionIds.map(id => adminDb.collection('questions').doc(id));
    const questionSnaps = questionRefs.length > 0 ? await adminDb.getAll(...questionRefs) : [];

    const questionsMap = new Map<string, any>();
    questionSnaps.forEach(snap => {
      if (snap.exists) {
        questionsMap.set(snap.id, snap.data());
      }
    });

    const evaluations: any[] = [];
    let correctCount = 0;
    let disputedCount = 0;
    let questionsAttemptedDelta = 0;
    let questionsCorrectDelta = 0;
    let questionsWrongDelta = 0;
    let weightedPointsEarnedDelta = 0;
    let weightedPointsPossibleDelta = 0;

    answers.forEach(ans => {
      const qData = questionsMap.get(ans.questionId);
      if (!qData) return;

      const isDisputed = disputedSet.has(String(ans.questionId).toLowerCase()) || (qData.questionCode && disputedSet.has(String(qData.questionCode).toLowerCase()));
      if (isDisputed) disputedCount++;

      const isCorrect = isDisputed ? false : evaluateQuestionAnswer(
        qData.type || 'single_mcq',
        ans.answer,
        qData.correctAnswer || qData.correctAnswers || '',
        qData.options
      );

      evaluations.push({
        id: ans.questionId,
        questionCode: qData.questionCode,
        text: qData.text || qData.assertion || '',
        type: qData.type || 'single_mcq',
        options: qData.options || [],
        assertion: qData.assertion || '',
        reason: qData.reason || '',
        solution: qData.solution || qData.explanation || qData.solutionText || qData.explanationText || '',
        difficulty: qData.difficulty || 'medium',
        bloomLevel: qData.bloomLevel || 'Understand',
        userAnswer: ans.answer,
        correctAnswer: qData.correctAnswer || '',
        correctAnswers: qData.correctAnswers || [],
        isCorrect,
        isDisputed,
        examCategory: qData.examCategory || 'standard'
      });

      if (!isDisputed) {
        if (isCorrect) correctCount++;

        const diffWeight = DIFFICULTY_WEIGHTS[qData.difficulty || 'medium'] || 1;
        const bloomWeight = BLOOM_WEIGHTS[qData.bloomLevel || 'Understand'] || 1;
        const questionWeight = diffWeight * bloomWeight;

        questionsAttemptedDelta++;
        weightedPointsPossibleDelta += questionWeight;

        if (isCorrect) {
          questionsCorrectDelta++;
          weightedPointsEarnedDelta += questionWeight;
        } else {
          questionsWrongDelta++;
        }
      }
    });

    const sessionIdToUse = sessionId || `sess_${Date.now()}`;
    const practiceExamCode = `PRACTICE_${topicCode}_${sessionIdToUse}`;
    const logId = `${studentCode}_${practiceExamCode}`;

    const submissionRef = adminDb.collection('practiceSubmissions').doc(logId);
    const docId = `${studentCode}_${topicCode}`;
    const docRef = adminDb.collection('studentTopicMastery').doc(docId);

    let finalMastery = 0;
    let finalConfidence = 0;
    let existingMastery = 0;
    let isAlreadySubmitted = false;

    await adminDb.runTransaction(async (tx) => {
      const subSnap = await tx.get(submissionRef);
      if (subSnap.exists) {
        const subData = subSnap.data()!;
        finalMastery = subData.finalMastery || 0;
        finalConfidence = subData.finalConfidence || 0;
        correctCount = subData.score || 0;
        existingMastery = subData.masteryBefore || 0;
        
        evaluations.length = 0;
        evaluations.push(...(subData.questions || []));
        isAlreadySubmitted = true;
        return;
      }

      const snap = await tx.get(docRef);
      const existing = snap.exists ? snap.data()! : null;
      existingMastery = existing ? (existing.mastery || 0) : 0;

      const defaultRecord = {
        studentCode,
        topicCode,
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
      const recordToUpdate = existing || defaultRecord;
      const updatedData = MasteryService.calculateTopicMasteryUpdate(recordToUpdate, evaluations, practiceExamCode);

      const recoverySessionAccuracy = evaluations.length > 0 ? (correctCount / evaluations.length) * 100 : 0;
      if (isRecoveryMode && (recoverySessionAccuracy >= 80 || updatedData.mastery >= 90)) {
        updatedData.isRecoveryMastered = true;
        updatedData.mastery = Math.max(updatedData.mastery, 90);
        updatedData.confidence = Math.max(updatedData.confidence, 20);
        updatedData.recoveryCompletedAt = new Date();
      }

      finalMastery = updatedData.mastery;
      finalConfidence = updatedData.confidence;

      tx.set(docRef, updatedData, { merge: true });

      // Save submission lock document in the transaction
      tx.set(submissionRef, {
        studentCode,
        topicCode,
        finalMastery,
        finalConfidence,
        score: correctCount,
        questions: evaluations,
        masteryBefore: existingMastery,
        submittedAt: new Date(),
        violations: violations || null
      });
    });

    if (!isAlreadySubmitted) {
      // Write a masteryExamLog document for audit trail
      await adminDb.collection('masteryExamLog').doc(logId).set({
        studentCode,
        examCode: practiceExamCode,
        examType: 'practice',
        topicsUpdated: 1,
        topicsFailed: 0,
        topicDeltas: {
          [topicCode]: {
            questionsAttemptedDelta,
            questionsCorrectDelta,
            questionsWrongDelta,
            weightedPointsEarnedDelta,
            weightedPointsPossibleDelta
          }
        },
        reversed: false,
        processedAt: new Date()
      });

      // Write to parentReviews collection for parents & admin history popup
      try {
        let topicName = topicCode;
        let subjectName = 'General';
        let chapterName = 'General';
        
        const syllabusSnap = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
        if (syllabusSnap.exists) {
          const sData = syllabusSnap.data()!;
          topicName = sData.topicName || topicName;
          subjectName = sData.subjectName || subjectName;
          chapterName = sData.chapterName || chapterName;
        }

        const strengths: string[] = [];
        const needsAttention: string[] = [];
        evaluations.forEach(ev => {
          if (ev.isCorrect) {
            strengths.push(ev.text);
          } else {
            needsAttention.push(ev.text);
          }
        });

        let suspiciousLevel = 'green';
        let integrityScore = 100;
        if (violations) {
          const { integrityScore: calcScore } = IntegrityService.calculateScore(
            violations.tabOutCount || 0,
            {
              noFace: violations.noFaceCount || 0,
              lookingAway: violations.lookingAwayCount || 0,
              multipleFaces: violations.multipleFacesCount || 0,
              headMovement: violations.headMovementCount || 0
            }
          );
          integrityScore = calcScore;

          const tabOut = violations.tabOutCount || 0;
          const otherViolations = (violations.noFaceCount || 0) + 
                                 (violations.lookingAwayCount || 0) + 
                                 (violations.multipleFacesCount || 0) + 
                                 (violations.headMovementCount || 0);
          if (tabOut > 2 || (violations.noFaceCount || 0) > 3 || (violations.lookingAwayCount || 0) > 3 || (tabOut + otherViolations) > 4 || proctoringViolationTriggered) {
            suspiciousLevel = 'red';
          } else if (tabOut > 0 || otherViolations > 0) {
            suspiciousLevel = 'yellow';
          }
        }

        const validQuestionsCount = Math.max(1, evaluations.length - disputedCount);
        const scorePercent = Math.round((correctCount / validQuestionsCount) * 100);

        // Query existing parentReviews count for this student to determine the sequential practiceNumber
        let practiceNumber = 1;
        try {
          const countSnap = await adminDb.collection('parentReviews')
            .where('studentCode', '==', studentCode)
            .count()
            .get();
          practiceNumber = (countSnap.data().count || 0) + 1;
        } catch (cErr) {
          console.warn('Failed to calculate practice test sequence number:', cErr);
        }

        await adminDb.collection('parentReviews').doc(logId).set({
          studentCode,
          practiceSessionId: logId,
          type: 'practice',
          topicCode,
          topicName,
          subjectName,
          chapterName,
          scorePercent,
          correctCount,
          totalQuestions: evaluations.length - disputedCount,
          disputedCount,
          masteryBefore: existingMastery,
          masteryAfter: finalMastery,
          masteryChange: finalMastery - existingMastery,
          suspiciousLevel,
          strengths: strengths.slice(0, 3),
          needsAttention: needsAttention.slice(0, 3),
          startedAt: new Date(Date.now() - (durationSpent || 0) * 1000),
          createdAt: new Date(),
          parentStatus: 'pending',
          practiceNumber: practiceNumber,
          questions: evaluations,
          questionDetails: evaluations.map(e => ({
            questionId: e.questionId || e.id || '',
            questionCode: e.questionCode || '',
            questionText: e.text || e.assertion || '',
            text: e.text || e.assertion || '',
            type: e.type || 'single_mcq',
            options: e.options || [],
            userAnswer: e.userAnswer ?? '',
            correctAnswer: e.correctAnswer ?? '',
            correctAnswers: e.correctAnswers || [],
            isCorrect: !!e.isCorrect,
            solution: e.solution || '',
            difficulty: e.difficulty || 'medium',
            bloomLevel: e.bloomLevel || 'Understand',
            marks: e.marks || 1
          }))
        });

        // Trigger push notification to Parent
        const studentDocSnap = await adminDb.collection('users')
          .where('studentCode', '==', studentCode)
          .where('role', '==', 'student')
          .limit(1)
          .get();
        const studentName = !studentDocSnap.empty 
          ? (studentDocSnap.docs[0].data().name || studentDocSnap.docs[0].data().displayName || studentCode) 
          : studentCode;
        
        notifyReviewPending({
          studentCode,
          studentName,
          topicName,
          scorePercent,
          reviewId: logId,
          startedAt: new Date(Date.now() - (durationSpent || 0) * 1000),
          completedAt: new Date(),
          durationSpentSec: durationSpent || 0,
          tabViolations: violations?.tabOutCount || 0,
          gazeViolations: violations?.lookingAwayCount || 0
        }).catch(err => {
          console.error('Error sending review pending notification:', err);
        });
      } catch (err) {
        console.warn('Failed to write to parentReviews collection:', err);
      }
    }

    return {
      score: correctCount,
      totalQuestions: evaluations.length - disputedCount,
      disputedCount,
      mastery: finalMastery,
      confidence: finalConfidence,
      questions: evaluations
    };
  }
}
