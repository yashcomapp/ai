/**
 * ==============================================================================
 * DASHBOARD METRICS — SINGLE SOURCE OF TRUTH (SSOT)
 * ==============================================================================
 * 
 * CRITICAL ARCHITECTURAL NOTE:
 * DO NOT calculate Average Marks, LQ/Mastery, or Efforts % with ad-hoc formulas
 * or hardcoded constants in separate routes.
 * 
 * Standardized Metric Definitions:
 * 1. Average Marks (`averageMarks` / `avgScore`):
 *    - The combined average percentage of ALL officially completed exams:
 *      Objective Exams (reviews) + Graded Subjective Exams (evaluations).
 *    - Excludes self-directed practice sessions from the exam marks average.
 * 
 * 2. LQ / Topic Mastery (`overallMastery` / `lqScore`):
 *    - The true holistic mastery calculated across all syllabus topics from
 *      the `studentTopicMastery` collection.
 *    - NEVER confuse or substitute `integrityScore` (proctoring score) for `lqScore`.
 * 
 * 3. Efforts % (`effortsPercent`):
 *    - Calculated as: (completedPracticeCount / totalSyllabusTopics) * 100.
 *    - Uses the student's actual syllabus topic count (minimum 20, default 24).
 * 
 * 4. Integrity Score (`integrityScore`):
 *    - Proctoring compliance metric (0 - 100%) derived from tab switches,
 *      facial presence, and gaze tracking.
 * ==============================================================================
 */

export interface UnifiedMetricsInput {
  objectiveReviews?: Array<{ percentage?: number | string; score?: number; totalMarks?: number; status?: string; [key: string]: any }>;
  subjectiveEvaluations?: Array<{ percentage?: number | string; totalMarksAwarded?: number; totalMaxMarks?: number; [key: string]: any }>;
  topicMasteries?: Array<{ mastery?: number | string; confidence?: number | string; [key: string]: any }>;
  practiceReviews?: Array<{ scorePercent?: number | string; totalQuestions?: number; [key: string]: any }>;
  integrityScore?: number;
  totalCoveredTopics?: number;
  totalSyllabusTopics?: number; // Deprecated alias, use totalCoveredTopics
}

export interface UnifiedMetricsResult {
  // 1. Average Marks
  averageMarks: number;
  examCount: number;
  objectiveAvg: number;
  subjectiveAvg: number;
  practiceAvg: number;

  // 2. Mastery / LQ Score
  overallMastery: number;
  lqScore: number;
  masteredTopicsCount: number;
  needsAttentionTopicsCount: number;

  // 3. Efforts
  effortsPercent: number;
  practicesCompletedCount: number;
  totalTopicsCount: number;
  totalQuestionsPracticed: number;

  // 4. Integrity
  integrityScore: number;
}

export function calculateUnifiedMetrics(input: UnifiedMetricsInput): UnifiedMetricsResult {
  const {
    objectiveReviews = [],
    subjectiveEvaluations = [],
    topicMasteries = [],
    practiceReviews = [],
    integrityScore = 100,
    totalCoveredTopics,
    totalSyllabusTopics
  } = input;

  // --- 1. Average Marks Calculation ---
  const objPercentages: number[] = [];
  objectiveReviews.forEach(r => {
    if (r.percentage != null && !isNaN(Number(r.percentage))) {
      objPercentages.push(Number(r.percentage));
    } else if (r.score != null && r.totalMarks && r.totalMarks > 0) {
      objPercentages.push((r.score / r.totalMarks) * 100);
    }
  });

  const subPercentages: number[] = [];
  subjectiveEvaluations.forEach(e => {
    if (e.percentage != null && !isNaN(Number(e.percentage))) {
      subPercentages.push(Number(e.percentage));
    } else if (e.totalMarksAwarded != null && e.totalMaxMarks && e.totalMaxMarks > 0) {
      subPercentages.push((e.totalMarksAwarded / e.totalMaxMarks) * 100);
    }
  });

  const allExamPercentages = [...objPercentages, ...subPercentages];
  const examCount = allExamPercentages.length;
  const averageMarks = examCount > 0
    ? Math.round(allExamPercentages.reduce((sum, p) => sum + p, 0) / examCount)
    : 0;

  const objectiveAvg = objPercentages.length > 0
    ? Math.round(objPercentages.reduce((sum, p) => sum + p, 0) / objPercentages.length)
    : 0;

  const subjectiveAvg = subPercentages.length > 0
    ? Math.round(subPercentages.reduce((sum, p) => sum + p, 0) / subPercentages.length)
    : 0;

  // Practice score average
  const practicePercentages: number[] = [];
  let totalQuestionsPracticed = 0;
  practiceReviews.forEach(p => {
    if (p.scorePercent != null && !isNaN(Number(p.scorePercent))) {
      practicePercentages.push(Number(p.scorePercent));
    }
    if (p.totalQuestions != null) {
      totalQuestionsPracticed += Number(p.totalQuestions) || 0;
    }
  });

  const practiceAvg = practicePercentages.length > 0
    ? Math.round(practicePercentages.reduce((sum, p) => sum + p, 0) / practicePercentages.length)
    : 0;

  // --- 2. Topic Mastery / LQ Score ---
  let certifiedMasteredCount = 0;
  let recoveryMasteredCount = 0;
  let needsAttentionTopicsCount = 0;
  let certifiedMasterySum = 0;
  let certifiedTopicsCount = 0;

  topicMasteries.forEach(t => {
    const mastery = Number(t.mastery || 0);
    const confidence = Number(t.confidence || 0);
    const isRecovery = !!t.isRecoveryMastered;

    if (isRecovery && mastery >= 90) {
      recoveryMasteredCount += 1;
    } else {
      certifiedMasterySum += mastery;
      certifiedTopicsCount += 1;

      if (mastery < 50) {
        needsAttentionTopicsCount += 1;
      } else if (mastery >= 90 && confidence >= 20) {
        certifiedMasteredCount += 1;
      }
    }
  });

  const masteredTopicsCount = certifiedMasteredCount + recoveryMasteredCount;

  // Official Institutional LQ is derived from Certified Masteries & Exams (0 inflation from brute-force recovery)
  const overallMastery = certifiedTopicsCount > 0
    ? Math.round(certifiedMasterySum / certifiedTopicsCount)
    : (topicMasteries.length > 0 ? Math.round(topicMasteries.reduce((s, t) => s + Number(t.mastery || 0), 0) / topicMasteries.length) : (averageMarks > 0 ? averageMarks : 0));

  const lqScore = overallMastery;

  // --- 3. Efforts Calculation ---
  // Denominator: number of topics on which exams/tests have actually been conducted/assigned
  const practicesCompletedCount = practiceReviews.length;
  const coveredCount = totalCoveredTopics ?? totalSyllabusTopics ?? (topicMasteries.length > 0 ? topicMasteries.length : 1);
  const safeTotalTopics = Math.max(1, coveredCount);
  const effortsPercent = practicesCompletedCount > 0
    ? Math.min(100, Math.round((practicesCompletedCount / safeTotalTopics) * 100))
    : 0;

  return {
    averageMarks,
    examCount,
    objectiveAvg,
    subjectiveAvg,
    practiceAvg,
    overallMastery,
    lqScore,
    masteredTopicsCount,
    needsAttentionTopicsCount,
    effortsPercent,
    practicesCompletedCount,
    totalTopicsCount: safeTotalTopics,
    totalQuestionsPracticed,
    integrityScore: Math.min(100, Math.max(0, Math.round(integrityScore)))
  };
}

/**
 * Single Source of Truth (SSOT) for UI score color coding across Student, Parent, and Admin views.
 * - Score >= 85%: Green (#10b981) - Mastered / High
 * - Score >= 60%: Amber (#f59e0b) - In Progress / Moderate
 * - Score < 60%:  Red (#ef4444)   - Needs Attention / Low
 */
export function getScoreColor(score: number): string {
  if (score >= 85) return '#10b981';
  if (score >= 60) return '#f59e0b';
  return '#ef4444';
}
