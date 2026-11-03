/**
 * Single Source of Truth (SSOT) for deriving normalized score, question count, and score percentage
 * across Practice and Exam attempts/reviews.
 *
 * Repairs corrupted or legacy records where scorePercent was stored as 0 or undefined
 * despite positive correctCount or score.
 */
export function deriveScoreMetrics(data: any): {
  score: number;
  totalQuestions: number;
  scorePercent: number;
} {
  if (!data) {
    return { score: 0, totalQuestions: 1, scorePercent: 0 };
  }

  const qList = Array.isArray(data.questions)
    ? data.questions
    : (Array.isArray(data.questionDetails) ? data.questionDetails : []);

  const totalQuestions = Math.max(
    1,
    Number(data.totalQuestions || data.totalMarks || data.total || qList.length || 1)
  );

  const score = data.correctCount !== undefined && data.correctCount !== null
    ? Number(data.correctCount)
    : (data.score !== undefined && data.score !== null
        ? Number(data.score)
        : qList.filter((q: any) => q.isCorrect).length);

  let scorePercent = data.scorePercent !== undefined && data.scorePercent !== null
    ? Number(data.scorePercent)
    : (data.percentage !== undefined && data.percentage !== null
        ? Number(data.percentage)
        : (totalQuestions > 0 ? Math.round((score / totalQuestions) * 100) : 0));

  // Self-healing guard: If score > 0 but stored percentage is 0 or NaN, auto-derive true percentage
  if (isNaN(scorePercent) || (score > 0 && scorePercent === 0 && totalQuestions > 0)) {
    scorePercent = Math.min(100, Math.max(0, Math.round((score / totalQuestions) * 100)));
  }

  return {
    score,
    totalQuestions,
    scorePercent: Math.min(100, Math.max(0, scorePercent))
  };
}

export function deriveScorePercent(data: any): number {
  return deriveScoreMetrics(data).scorePercent;
}

/**
 * Single Source of Truth (SSOT) for determining whether a parent/teacher review is approved.
 * Fully backward-compatible with legacy records where only parentStatus === 'approved'
 * or status === 'approved'.
 */
export function isReviewApproved(data: any): boolean {
  if (!data) return false;
  return data.parentStatus === 'approved' || data.status === 'approved';
}

export function isReviewPending(data: any): boolean {
  if (!data) return false;
  return !isReviewApproved(data);
}
