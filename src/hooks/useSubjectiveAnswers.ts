'use client';

import { useState, useCallback } from 'react';
import { Question } from '@/types/question.types';

export interface CompiledQuestionReview {
  questionId: string;
  maxMarks: number;
  marksAwarded: number;
  stepMarks: Array<{ stepNo: number; awarded: number }>;
  feedback: string;
}

export interface CompileResult {
  questionReviews: CompiledQuestionReview[];
  totalScore: number;
}

export function useSubjectiveAnswers() {
  const [reviewAnswers, setReviewAnswers] = useState<{ [key: string]: number | string }>({});
  const [reviewFeedback, setReviewFeedback] = useState<{ [key: string]: string }>({});

  /**
   * Validates that all questions (and steps) have explicit marks awarded.
   * Returns null if valid, or an error message string if invalid.
   */
  const validateAnswers = useCallback((questions: Question[]): string | null => {
    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      if (q.steps && q.steps.length > 0) {
        for (let s = 0; s < q.steps.length; s++) {
          const rawVal = reviewAnswers[`ps_${i}_${s}`];
          if (rawVal === undefined || rawVal === null || rawVal === '') {
            return `Please award marks for Question ${i + 1}, Step ${s + 1}.`;
          }
        }
      } else {
        const rawVal = reviewAnswers[`ps_${i}_0`];
        if (rawVal === undefined || rawVal === null || rawVal === '') {
          return `Please award marks for Question ${i + 1}.`;
        }
      }
    }
    return null;
  }, [reviewAnswers]);

  /**
   * Compiles the question reviews structure and calculates the total score.
   */
  const compileReviews = useCallback((questions: Question[]): CompileResult => {
    const questionReviews: CompiledQuestionReview[] = [];
    let totalScore = 0;

    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      let questionTotal = 0;
      const stepMarks: Array<{ stepNo: number; awarded: number }> = [];

      if (q.steps && q.steps.length > 0) {
        for (let s = 0; s < q.steps.length; s++) {
          const val = Number(reviewAnswers[`ps_${i}_${s}`]) || 0;
          stepMarks.push({ stepNo: s + 1, awarded: val });
          questionTotal += val;
        }
      } else {
        const val = Number(reviewAnswers[`ps_${i}_0`]) || 0;
        stepMarks.push({ stepNo: 1, awarded: val });
        questionTotal = val;
      }

      const feedback = reviewFeedback[`pf_${i}`] || '';
      questionReviews.push({
        questionId: q.id || q.questionCode || '',
        maxMarks: Number(q.marks || 0),
        marksAwarded: questionTotal,
        stepMarks,
        feedback
      });
      totalScore += questionTotal;
    }

    return { questionReviews, totalScore };
  }, [reviewAnswers, reviewFeedback]);

  /**
   * Calculates total marks awarded for a specific question index.
   */
  const getQuestionTotalAwarded = useCallback((q: Question, qIndex: number): number => {
    let total = 0;
    if (q.steps && q.steps.length > 0) {
      for (let si = 0; si < q.steps.length; si++) {
        total += Number(reviewAnswers[`ps_${qIndex}_${si}`]) || 0;
      }
    } else {
      total += Number(reviewAnswers[`ps_${qIndex}_0`]) || 0;
    }
    return total;
  }, [reviewAnswers]);

  const resetAnswers = useCallback(() => {
    setReviewAnswers({});
    setReviewFeedback({});
  }, []);

  return {
    reviewAnswers,
    setReviewAnswers,
    reviewFeedback,
    setReviewFeedback,
    validateAnswers,
    compileReviews,
    getQuestionTotalAwarded,
    resetAnswers
  };
}

export default useSubjectiveAnswers;
