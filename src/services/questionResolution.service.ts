import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { EvaluationService } from './evaluation.service';
import { MasteryService } from './mastery.service';
import { QuestionRepository } from '@/repositories/question.repository';
import {
  CANONICAL_OBJECTIVE_TYPES,
  deriveTopicCodeFromQuestionCode,
  getOptionText,
  isMultipleChoiceType,
  parseAnswerList,
  toCanonicalQuestionType,
} from '@/lib/questionTypes';
import { invalidateCache } from '@/lib/firebase/cache';
import { ReportCacheManager } from '@/lib/reportCache';
import { ChunkedBatch } from '@/lib/firebase/batch';

export interface QuestionResolutionUpdates {
  text?: string;
  options?: any[];
  correctAnswer?: any;
  correctAnswers?: string[];
  solution?: string;
  type?: string;
  marks?: number;
}

export interface RescoreSummary {
  questionCode: string;
  updatedExams: number;
  updatedReviews: number;
  updatedAttempts: number;
  updatedPracticeSubmissions: number;
  updatedParentReviews: number;
  recalculatedStudents: string[];
}

/**
 * Single Source of Truth (SSOT) for resolving question issues without marking them disputed,
 * and rescoring all affected student Exam & Practice submissions while strictly preserving
 * every student's original submitted response.
 */
export class QuestionResolutionService {
  /**
   * Resolves a canonical correct answer representation from a question document.
   */
  private static resolveCanonicalCorrect(questionDoc: any): {
    qType: string;
    isMultiple: boolean;
    canonicalCorrect: any;
    correctAnsText: string;
  } {
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
          : (Array.isArray(questionDoc.correctAnswers) && questionDoc.correctAnswers.length > 0
              ? questionDoc.correctAnswers[0]
              : ''));

    if (isMultiple && Array.isArray(questionDoc.options) && questionDoc.options.length > 0) {
      const fromOpts = questionDoc.options
        .map((opt: any, idx: number) =>
          opt && typeof opt === 'object' && (opt.isCorrect || opt.correct) ? String.fromCharCode(65 + idx) : null
        )
        .filter(Boolean);
      if (fromOpts.length > 1 && (!Array.isArray(canonicalCorrect) || canonicalCorrect.length <= 1)) {
        canonicalCorrect = fromOpts;
      }
    }

    const correctAnsText = getOptionText(questionDoc, canonicalCorrect ?? '');
    return { qType, isMultiple, canonicalCorrect, correctAnsText };
  }

  /**
   * Updates a question in the Question Bank (clearing any accidental dispute/quarantine flags
   * unless explicitly disabled, and never marking it disputed) and rescores all affected
   * Exam and Practice submissions.
   */
  static async resolveAndRescoreQuestion(params: {
    questionCode: string;
    updates?: QuestionResolutionUpdates;
    clearDisputed?: boolean;
    resolvedBy?: string;
  }): Promise<RescoreSummary> {
    const { questionCode, updates, clearDisputed = true, resolvedBy = 'admin' } = params;
    const trimmedCode = String(questionCode || '').trim();
    if (!trimmedCode) {
      throw new Error('questionCode is required');
    }

    let questionRef = adminDb.collection('questions').doc(trimmedCode);
    let questionSnap = await questionRef.get();

    if (!questionSnap.exists) {
      const byCode = await adminDb
        .collection('questions')
        .where('questionCode', '==', trimmedCode)
        .limit(1)
        .get();
      if (byCode.empty) {
        throw new Error(`Question not found: ${trimmedCode}`);
      }
      questionSnap = byCode.docs[0];
      questionRef = questionSnap.ref;
    }

    const existingData = questionSnap.data() || {};
    const mergedData: Record<string, any> = {
      ...existingData,
      ...(updates || {}),
    };

    // Synchronize correctAnswer and correctAnswers if options or answers were updated
    const qType = mergedData.type || 'OSC';
    const isMulti = isMultipleChoiceType(qType);
    const opts = Array.isArray(mergedData.options) ? mergedData.options : [];

    if (updates?.correctAnswer !== undefined && updates?.correctAnswers === undefined) {
      if (isMulti) {
        const list = Array.isArray(updates.correctAnswer)
          ? updates.correctAnswer.map((s: any) => String(s).trim()).filter(Boolean)
          : parseAnswerList(updates.correctAnswer);
        mergedData.correctAnswer = list.join(', ');
        mergedData.correctAnswers = list;
      } else {
        const ansStr = String(updates.correctAnswer).trim();
        mergedData.correctAnswer = ansStr;
        const resolvedText = getOptionText({ options: opts, type: qType }, ansStr);
        mergedData.correctAnswers = resolvedText ? [resolvedText] : [ansStr];
      }
    } else if (updates?.correctAnswers !== undefined && updates?.correctAnswer === undefined && !isMulti) {
      const firstText = Array.isArray(updates.correctAnswers) ? String(updates.correctAnswers[0] || '').trim() : '';
      if (firstText && opts.length > 0) {
        const idx = opts.findIndex((o: any) => {
          const txt = typeof o === 'object' && o !== null ? String(o.text || o.label || o.value || '').trim() : String(o).trim();
          return txt === firstText;
        });
        if (idx !== -1) {
          mergedData.correctAnswer = String.fromCharCode(65 + idx);
        }
      }
    }

    const firestoreUpdates: Record<string, any> = {
      ...(updates || {}),
      correctAnswer: mergedData.correctAnswer,
      correctAnswers: mergedData.correctAnswers,
      resolvedAt: admin.firestore.FieldValue.serverTimestamp(),
      resolvedBy,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    };

    if (clearDisputed) {
      firestoreUpdates.isQuarantined = false;
      firestoreUpdates.flaggedDefective = false;
      if (existingData.status === 'quarantined' || existingData.status === 'disputed') {
        firestoreUpdates.status = 'active';
      }
    }

    await questionRef.set(firestoreUpdates, { merge: true });

    const finalQuestionDoc: Record<string, any> = {
      ...mergedData,
      ...firestoreUpdates,
      id: questionRef.id,
      questionCode: mergedData.questionCode || questionRef.id,
    };

    invalidateCache('qb_base_');
    const topicCode = finalQuestionDoc.topicCode || deriveTopicCodeFromQuestionCode(finalQuestionDoc.questionCode);
    if (topicCode) {
      QuestionRepository.clearTopicCache(topicCode);
    }

    return await this.rescoreQuestionAcrossAllSubmissions(finalQuestionDoc);
  }

  /**
   * Re-grades and updates all existing Exam submissions (`exams`, `reviews`, `examAttempts`),
   * Practice submissions (`practiceSubmissions`, `parentReviews`), and `studentTopicMastery`
   * for a given question without ever modifying or deleting original student responses.
   */
  static async rescoreQuestionAcrossAllSubmissions(
    questionDoc: any,
    previousId?: string
  ): Promise<RescoreSummary> {
    const finalCode = String(questionDoc?.questionCode || questionDoc?.id || '').trim();
    if (!finalCode) {
      return {
        questionCode: '',
        updatedExams: 0,
        updatedReviews: 0,
        updatedAttempts: 0,
        updatedPracticeSubmissions: 0,
        updatedParentReviews: 0,
        recalculatedStudents: [],
      };
    }

    const matchCodes = new Set<string>([finalCode]);
    if (previousId && previousId !== finalCode) {
      matchCodes.add(String(previousId).trim());
    }
    const matchCodesLower = new Set(Array.from(matchCodes).map(c => c.toLowerCase()));

    const { qType, isMultiple, canonicalCorrect, correctAnsText } = this.resolveCanonicalCorrect(questionDoc);
    const isObj = !qType || CANONICAL_OBJECTIVE_TYPES.includes(toCanonicalQuestionType(qType));
    const topicCode = questionDoc.topicCode || deriveTopicCodeFromQuestionCode(finalCode);

    const batch = new ChunkedBatch(adminDb);
    let updatedExams = 0;
    let updatedReviews = 0;
    let updatedAttempts = 0;
    let updatedPracticeSubmissions = 0;
    let updatedParentReviews = 0;
    const studentsToRecalcMastery = new Set<string>();
    const cachePatternsToInvalidate = new Set<string>();

    // =========================================================================
    // PART 1: EXAM SUBMISSIONS (`exams`, `reviews`, `examAttempts`)
    // =========================================================================
    const examQueries = Array.from(matchCodes).map(code =>
      adminDb.collection('exams').where('questionCodes', 'array-contains', code).get()
    );
    const examSnaps = await Promise.all(examQueries);
    const examDocsMap = new Map<string, FirebaseFirestore.QueryDocumentSnapshot>();
    examSnaps.forEach(snap => snap.docs.forEach(d => examDocsMap.set(d.id, d)));

    for (const [examId, examSnap] of examDocsMap.entries()) {
      const examData = examSnap.data() || {};
      const examPos = Number(examData.positiveMarks);
      const negativePerWrong = Number(examData.negativeMarks) || 0;
      const qMarks = isObj && examPos > 0 ? examPos : questionDoc.marks || examPos || 4;

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

          // Strictly preserve student's original response (rawAnswer)
          const hasRaw = qd.rawAnswer !== undefined && qd.rawAnswer !== null && String(qd.rawAnswer).trim() !== '';
          const hasDisplayAns =
            qd.userAnswer && qd.userAnswer !== '[Reported / Disputed]' && String(qd.userAnswer).trim() !== '';
          const ansToEval = hasRaw ? qd.rawAnswer : hasDisplayAns ? qd.userAnswer : '';

          let nextIsDisputed = prevIsDisputed;
          let nextIsCorrect = false;
          let nextUserAnswer = qd.userAnswer || '';
          let nextMarks = qMarks;

          if (prevIsDisputed && !hasRaw && !hasDisplayAns) {
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
            // Preserve rawAnswer untouched; only refresh display userAnswer if rawAnswer exists
            userAnswer: nextUserAnswer,
            isCorrect: nextIsCorrect,
            isDisputed: nextIsDisputed,
            marks: nextMarks,
          };
        });

        if (!matchedThisReview) continue;

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
              qIndex: idx,
              questionText: qd.questionText || '',
              userAnswer: qd.userAnswer || '',
              correctAnswer: qd.correctAnswer,
            });
          }
        });

        const newPercentage =
          newTotalMarks > 0 ? parseFloat(((newScore / newTotalMarks) * 100).toFixed(1)) : 0;

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
          batch.set(
            attemptRef,
            {
              score: newScore,
              totalMarks: newTotalMarks,
              percentage: newPercentage,
              regradedAt: admin.firestore.FieldValue.serverTimestamp(),
            },
            { merge: true }
          );
          updatedAttempts++;
        }
      }
    }

    // =========================================================================
    // PART 2: PRACTICE SUBMISSIONS (`practiceSubmissions` & `parentReviews`)
    // =========================================================================
    if (topicCode) {
      const [pracSnap, parentRevSnap] = await Promise.all([
        adminDb.collection('practiceSubmissions').where('topicCode', '==', topicCode).get(),
        adminDb.collection('parentReviews').where('topicCode', '==', topicCode).get(),
      ]);

      const rescorePracticeDoc = (docSnap: FirebaseFirestore.QueryDocumentSnapshot, isParentReview: boolean) => {
        const data = docSnap.data() || {};
        const questionsArr: any[] = Array.isArray(data.questions)
          ? data.questions
          : Array.isArray(data.evaluations)
          ? data.evaluations
          : [];
        const qDetailsArr: any[] = Array.isArray(data.questionDetails) ? data.questionDetails : [];
        const answersArr: any[] = Array.isArray(data.answers) ? data.answers : [];

        const matchesItem = (item: any) => {
          const ids = [item?.questionCode, item?.questionId, item?.id]
            .filter(Boolean)
            .map((v: any) => String(v).trim().toLowerCase());
          return ids.some(v => matchCodesLower.has(v));
        };

        const hasMatch = questionsArr.some(matchesItem) || qDetailsArr.some(matchesItem);
        if (!hasMatch) return;

        let masteryRelevantChange = false;

        // Helper to evaluate one practice item without altering student's original response
        const evaluatePracticeItem = (item: any) => {
          const prevCorrect = !!item.isCorrect;
          const prevDisputed = !!item.isDisputed;
          const itemIds = [item.questionCode, item.questionId, item.id]
            .filter(Boolean)
            .map((v: any) => String(v).trim().toLowerCase());
          const origAnsObj = answersArr.find((a: any) =>
            itemIds.includes(String(a?.questionId || a?.questionCode || '').trim().toLowerCase())
          );

          const rawAns = origAnsObj?.answer ?? item.rawAnswer ?? item.userAnswer ?? item.studentAnswer ?? '';
          const selectedOptText = origAnsObj?.selectedOptionText ?? item.userAnswer ?? '';
          const optsSnapshot =
            Array.isArray(origAnsObj?.optionsSnapshot) && origAnsObj.optionsSnapshot.length > 0
              ? origAnsObj.optionsSnapshot
              : Array.isArray(item.options) && item.options.length > 0
              ? item.options
              : questionDoc.options || [];

          let nextIsCorrect = false;
          if (!prevDisputed) {
            nextIsCorrect = EvaluationService.evaluate(qType, rawAns, canonicalCorrect, questionDoc.options);
            if (!nextIsCorrect && selectedOptText) {
              nextIsCorrect = EvaluationService.evaluate(qType, selectedOptText, canonicalCorrect, questionDoc.options);
            }
            if (!nextIsCorrect && optsSnapshot.length > 0) {
              if (isMultiple) {
                try {
                  const letters = parseAnswerList(rawAns);
                  const mappedTexts = letters.map((l: string) => {
                    if (/^[A-Z]$/i.test(l)) {
                      const idx = l.toUpperCase().charCodeAt(0) - 65;
                      if (idx >= 0 && idx < optsSnapshot.length) {
                        const opt = optsSnapshot[idx];
                        return typeof opt === 'object' && opt ? opt.text || opt.value || '' : String(opt);
                      }
                    }
                    return l;
                  });
                  nextIsCorrect = EvaluationService.evaluate(qType, mappedTexts, canonicalCorrect, questionDoc.options);
                } catch {}
              } else if (typeof rawAns === 'string' && /^[A-Z]$/i.test(rawAns.trim())) {
                const idx = rawAns.trim().toUpperCase().charCodeAt(0) - 65;
                if (idx >= 0 && idx < optsSnapshot.length) {
                  const opt = optsSnapshot[idx];
                  const optText = typeof opt === 'object' && opt ? opt.text || opt.value || '' : String(opt);
                  if (optText) {
                    nextIsCorrect = EvaluationService.evaluate(qType, optText, canonicalCorrect, questionDoc.options);
                  }
                }
              }
            }
          }

          if (prevCorrect !== nextIsCorrect) {
            masteryRelevantChange = true;
          }

          return {
            ...item,
            questionCode: finalCode,
            text: questionDoc.text || item.text || item.questionText || '',
            ...(item.questionText !== undefined ? { questionText: questionDoc.text || item.questionText } : {}),
            type: qType,
            options: optsSnapshot,
            solution: questionDoc.solution || item.solution || '',
            correctAnswer: questionDoc.correctAnswer ?? correctAnsText,
            correctAnswers: questionDoc.correctAnswers || (correctAnsText ? [correctAnsText] : []),
            isCorrect: nextIsCorrect,
          };
        };

        const updatedQuestions = questionsArr.map(item => (matchesItem(item) ? evaluatePracticeItem(item) : item));
        const updatedQDetails = qDetailsArr.map(item => (matchesItem(item) ? evaluatePracticeItem(item) : item));

        const evalSource = updatedQuestions.length > 0 ? updatedQuestions : updatedQDetails;
        const validItems = evalSource.filter((it: any) => !it.isDisputed);
        const newCorrectCount = validItems.filter((it: any) => !!it.isCorrect).length;
        const validCount = Math.max(1, validItems.length);
        const newScorePercent = Math.round((newCorrectCount / validCount) * 100);

        const updatedResults: Record<string, boolean> = { ...(data.results || {}) };
        evalSource.forEach((ev: any) => {
          const key = ev.code || ev.questionCode || ev.id;
          if (key) updatedResults[key] = !!ev.isCorrect;
        });

        const docUpdates: Record<string, any> = {
          ...(updatedQuestions.length > 0 ? { questions: updatedQuestions } : {}),
          ...(Array.isArray(data.evaluations) ? { evaluations: updatedQuestions } : {}),
          ...(updatedQDetails.length > 0 ? { questionDetails: updatedQDetails } : {}),
          results: updatedResults,
          correctCount: newCorrectCount,
          score: newCorrectCount,
          scorePercent: newScorePercent,
          percentage: newScorePercent,
          regradedAt: admin.firestore.FieldValue.serverTimestamp(),
        };

        batch.update(docSnap.ref, docUpdates);
        if (isParentReview) {
          updatedParentReviews++;
        } else {
          updatedPracticeSubmissions++;
        }

        const sCode = data.studentCode;
        if (sCode) {
          cachePatternsToInvalidate.add(sCode);
          if (masteryRelevantChange) {
            studentsToRecalcMastery.add(sCode);
          }
        }
      };

      pracSnap.docs.forEach(d => rescorePracticeDoc(d, false));
      parentRevSnap.docs.forEach(d => rescorePracticeDoc(d, true));
    }

    await batch.commit();

    // =========================================================================
    // PART 3: RECALCULATE `studentTopicMastery`
    // =========================================================================
    const recalculatedStudents = Array.from(studentsToRecalcMastery);
    if (topicCode && recalculatedStudents.length > 0) {
      await Promise.all(
        recalculatedStudents.map(sCode =>
          MasteryService.recalculateOrPurgeTopicsForStudent({
            studentCode: sCode,
            excludedExamId: '__none__',
            candidateTopicCodes: [topicCode],
          }).catch(err => console.warn(`Mastery recalc failed for ${sCode}:`, err))
        )
      );
    }

    // =========================================================================
    // PART 4: INVALIDATE CACHES
    // =========================================================================
    try {
      invalidateCache('admin_dashboard_');
      invalidateCache('topic-coverage');
      for (const pattern of cachePatternsToInvalidate) {
        invalidateCache(pattern);
        await ReportCacheManager.invalidatePattern(pattern);
      }
    } catch {}

    return {
      questionCode: finalCode,
      updatedExams,
      updatedReviews,
      updatedAttempts,
      updatedPracticeSubmissions,
      updatedParentReviews,
      recalculatedStudents,
    };
  }
}
