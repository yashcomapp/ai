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

import { calculateSrsSchedule } from '@/lib/srsRotation';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

export interface ExtractConductedTopicCodesInput {
  masteryList?: Array<{ topicCode?: string; [key: string]: any }>;
  classroomExams?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionIds?: string[]; questionCodes?: string[]; [key: string]: any }>;
  homePractice?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionIds?: string[]; questionCodes?: string[]; [key: string]: any }>;
  assignments?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; [key: string]: any }>;
  objectiveExams?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionCodes?: string[]; [key: string]: any }> | Map<string, any>;
  practiceReviews?: Array<{ topicCode?: string; resolvedTopicCode?: string; [key: string]: any }>;
  objectiveReviews?: Array<{ topicCode?: string; resolvedTopicCode?: string; [key: string]: any }>;
}

export function isCanonicalTopicCode(code?: string): boolean {
  if (!code || typeof code !== 'string') return false;
  const trimmed = code.trim();
  return /^(CBSE|MH)-\d+-[A-Za-z0-9]+-\d+-[\d\.]+$/.test(trimmed);
}

/**
 * Single Source of Truth (SSOT) to aggregate all unique topics on which exams/tests
 * have actually been conducted, assigned, practiced, or mastered so far.
 * Strictly filters to canonical topic codes (${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber})
 * to prevent double-counting of short subtopic fragments (e.g., '7.1.1').
 */
export function extractConductedTopicCodes(input: ExtractConductedTopicCodesInput): Set<string> {
  const conducted = new Set<string>();

  const addCode = (code?: string) => {
    if (code && typeof code === 'string') {
      const trimmed = code.trim();
      if (isCanonicalTopicCode(trimmed)) {
        conducted.add(trimmed);
      }
    }
  };

  const processItem = (item: any) => {
    if (!item) return;
    addCode(item.topicCode);
    addCode(item.resolvedTopicCode);
    if (Array.isArray(item.topicCodes)) item.topicCodes.forEach(addCode);
    if (Array.isArray(item.topics)) item.topics.forEach(addCode);
    if (Array.isArray(item.questionCodes)) {
      item.questionCodes.forEach((qc: string) => {
        addCode(deriveTopicCodeFromQuestionCode(qc));
      });
    }
    if (Array.isArray(item.questionIds)) {
      item.questionIds.forEach((qid: string) => {
        addCode(deriveTopicCodeFromQuestionCode(qid));
      });
    }
  };

  (input.masteryList || []).forEach(processItem);
  (input.classroomExams || []).forEach(processItem);
  (input.homePractice || []).forEach(processItem);
  (input.assignments || []).forEach(processItem);
  
  if (input.objectiveExams) {
    if (input.objectiveExams instanceof Map) {
      input.objectiveExams.forEach(processItem);
    } else if (Array.isArray(input.objectiveExams)) {
      input.objectiveExams.forEach(processItem);
    }
  }

  (input.practiceReviews || []).forEach(processItem);
  (input.objectiveReviews || []).forEach(processItem);

  return conducted;
}

/**
 * ATTENTION - QUERY INTEGRITY CONTRACT:
 * When querying collections passed into `calculateUnifiedMetrics`, DO NOT strip fields with partial `.select()`:
 * - `topicMasteries`: requires `mastery`, `confidence`, `requiredConfidence`, `isRecoveryMastered`,
 *   `questionsAttempted`, `totalAttempts`, `srsSchedule`, `lastRevisedAt`, `updatedAt`, `srsStage`, `lastAttempt`.
 * - `practiceReviews`: requires `scorePercent`, `totalQuestions`, `status`, `createdAt`, `topicCode`.
 * - `objectiveReviews`: requires `percentage`, `score`, `totalMarks`, `status`.
 * - `subjectiveEvaluations`: requires `percentage`, `totalMarksAwarded`, `totalMaxMarks`.
 * Partial projections will silently corrupt retention, SRS due counts, and mastery metrics.
 */
export interface UnifiedMetricsInput {
  objectiveReviews?: Array<{ percentage?: number | string; score?: number; totalMarks?: number; status?: string; [key: string]: any }>;
  subjectiveEvaluations?: Array<{ percentage?: number | string; totalMarksAwarded?: number; totalMaxMarks?: number; [key: string]: any }>;
  topicMasteries?: Array<{ 
    mastery?: number | string; 
    confidence?: number | string; 
    srsStage?: number;
    lastRevisedAt?: string | number | Date | null;
    updatedAt?: any;
    lastAttempt?: string | number | Date | null;
    srsSchedule?: {
      estimatedRetention?: number;
      isDueForRevision?: boolean;
      daysOverdue?: number;
      daysUntilDue?: number;
      srsStage?: number;
      stageLabel?: string;
    };
    [key: string]: any;
  }>;
  practiceReviews?: Array<{ scorePercent?: number | string; totalQuestions?: number; [key: string]: any }>;
  integrityScore?: number;
  totalCoveredTopics?: number;
  totalSyllabusTopics?: number; // Deprecated alias, use totalCoveredTopics
  srsEnabled?: boolean;
}

export interface UnifiedMetricsResult {
  // 1. Average Marks
  averageMarks: number;
  examCount: number;
  objectiveAvg: number;
  subjectiveAvg: number;
  practiceAvg: number;

  // 2. Mastery / LQ Score (SRS Retention Integrated)
  overallMastery: number;       // Nominal Curriculum Mastery (0-100%)
  lqScore: number;              // True Retained Learning Quotient (0-100%)
  averageRetention: number;     // Average Memory Retention Index (0-100%)
  masteredTopicsCount: number;
  practicingTopicsCount?: number;
  needsAttentionTopicsCount: number;
  unattemptedTopicsCount?: number;
  uniqueTopicsPracticed?: number;
  coveragePercent?: number;
  srsDueTopicsCount: number;
  srsOverdueTopicsCount: number;

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
    // Explicitly exclude entrance/placement exams and informal practice sessions from primary curriculum average
    if (r.examType === 'entrance' || r.type === 'entrance' || r.isEntrance === true || r.examCategory === 'entrance') return;
    if (r.examType === 'practice' || r.isPractice === true || r.status === 'practice' || r.type === 'practice') return;

    if (r.percentage != null && !isNaN(Number(r.percentage))) {
      objPercentages.push(Number(r.percentage));
    } else if (r.score != null && r.totalMarks && r.totalMarks > 0) {
      objPercentages.push((r.score / r.totalMarks) * 100);
    }
  });

  const subPercentages: number[] = [];
  subjectiveEvaluations.forEach(e => {
    // Explicitly exclude entrance/placement exams and informal practice sessions from primary curriculum average
    if (e.examType === 'entrance' || e.type === 'entrance' || e.isEntrance === true || e.examCategory === 'entrance') return;
    if (e.examType === 'practice' || e.isPractice === true || e.status === 'practice' || e.type === 'practice') return;

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
    } else if (p.percentage != null && !isNaN(Number(p.percentage))) {
      practicePercentages.push(Number(p.percentage));
    }
    if (p.totalQuestions != null) {
      totalQuestionsPracticed += Number(p.totalQuestions) || 0;
    } else if (p.questionsCount != null) {
      totalQuestionsPracticed += Number(p.questionsCount) || 0;
    }
  });

  const practiceAvg = practicePercentages.length > 0
    ? Math.round(practicePercentages.reduce((sum, p) => sum + p, 0) / practicePercentages.length)
    : 0;

  // --- 2. Topic Mastery / LQ Score (With SRS Retention Modulation) ---
  let masteredTopicsCount = 0;
  let practicingTopicsCount = 0;
  let needsAttentionTopicsCount = 0;
  let srsDueTopicsCount = 0;
  let srsOverdueTopicsCount = 0;

  let certifiedNominalSum = 0;
  let certifiedEffectiveSum = 0;
  let certifiedTopicsCount = 0;
  let totalRetentionSum = 0;

  topicMasteries.forEach(t => {
    const mastery = Number(t.mastery || 0);
    const confidence = Number(t.confidence || 0);
    const isRecovery = !!t.isRecoveryMastered;
    const reqConf = Number(t.requiredConfidence || 10);
    const isFullConfidence = confidence >= reqConf;
    const hasPracticed = Number(t.confidence || 0) > 0 || Number(t.questionsAttempted || 0) > 0 || Number(t.totalAttempts || 0) > 0 || isRecovery;
    const isSrsEnabled = Boolean(input.srsEnabled);

    // Resolve SRS retention and review status (ONLY when SRS is explicitly enabled)
    let retention = 100;
    let isDue = false;
    let isOverdue = false;

    if (isSrsEnabled && hasPracticed) {
      if (t.srsSchedule) {
        retention = typeof t.srsSchedule.estimatedRetention === 'number' ? t.srsSchedule.estimatedRetention : 100;
        isDue = Boolean(t.srsSchedule.isDueForRevision);
        isOverdue = Number(t.srsSchedule.daysOverdue || 0) > 0;
      } else {
        const lastTime = t.lastRevisedAt || (t.updatedAt?.toDate ? t.updatedAt.toDate() : t.updatedAt) || t.lastAttempt;
        const sched = calculateSrsSchedule(lastTime, Number(t.srsStage || 0));
        retention = sched.estimatedRetention;
        isDue = sched.isDueForRevision;
        isOverdue = sched.daysOverdue > 0;
      }
    }

    if (isSrsEnabled) {
      if (isDue) srsDueTopicsCount++;
      if (isOverdue) srsOverdueTopicsCount++;
    }
    totalRetentionSum += retention;

    // Pedagogical Retention Modulation: Only active when SRS is enabled.
    // When SRS is off (default), nominal syllabus mastery = effective mastery without artificial decay.
    const retentionFactor = isSrsEnabled ? (0.70 + 0.30 * (retention / 100)) : 1.0;
    const effectiveMastery = isSrsEnabled ? Math.round(mastery * retentionFactor) : mastery;

    // Regular Topic Mastery System:
    // 🟢 Mastered: contributes full earned accuracy (e.g. 90-100%)
    // 🟡 In Progress: contributes earned accuracy scaled by confidence progress (confidence / reqConf)
    // 🔴 Needs Attention / Unattempted: 0 credit
    let topicMasteryProgress = 0;
    if (isRecovery || (mastery >= 90 && isFullConfidence)) {
      masteredTopicsCount += 1;
      topicMasteryProgress = mastery;
    } else if (mastery >= 50) {
      practicingTopicsCount += 1;
      const confRatio = Math.min(1.0, Math.max(0.05, confidence / reqConf));
      topicMasteryProgress = mastery * confRatio;
    } else {
      needsAttentionTopicsCount += 1;
      topicMasteryProgress = 0;
    }

    const effectiveProgress = isSrsEnabled ? Math.round(topicMasteryProgress * retentionFactor) : topicMasteryProgress;

    certifiedNominalSum += topicMasteryProgress;
    certifiedEffectiveSum += effectiveProgress;
    certifiedTopicsCount += 1;
  });

  const coveredCount = totalCoveredTopics ?? totalSyllabusTopics ?? (topicMasteries.length > 0 ? topicMasteries.length : 1);
  const safeTotalTopics = Math.max(1, coveredCount);

  // Unattempted topics in the conducted/assigned curriculum default to Needs Attention
  const unattemptedTopicsCount = Math.max(0, safeTotalTopics - (masteredTopicsCount + practicingTopicsCount + needsAttentionTopicsCount));
  needsAttentionTopicsCount += unattemptedTopicsCount;

  // Nominal Curriculum Mastery: Across the entire assigned syllabus
  // (Unattempted topics contribute 0% mastery to the curriculum total)
  const overallMastery = safeTotalTopics > 0
    ? Math.min(100, Math.round(certifiedNominalSum / safeTotalTopics))
    : (certifiedTopicsCount > 0 ? Math.round(certifiedNominalSum / certifiedTopicsCount) : (averageMarks > 0 ? averageMarks : 0));

  // True Retained LQ: When SRS is enabled, modulated by retention; when SRS is off, equals overallMastery
  const lqScore = Boolean(input.srsEnabled)
    ? (safeTotalTopics > 0 ? Math.min(100, Math.round(certifiedEffectiveSum / safeTotalTopics)) : overallMastery)
    : overallMastery;

  const averageRetention = Boolean(input.srsEnabled)
    ? (topicMasteries.length > 0 ? Math.round(totalRetentionSum / topicMasteries.length) : 0)
    : 100;

  // --- 3. Efforts Calculation ---
  // Collect unique topics practiced via self-practice (practiceReviews)
  const practicedTopicCodes = new Set<string>();
  practiceReviews.forEach(p => {
    if (p.topicCode && typeof p.topicCode === 'string') {
      practicedTopicCodes.add(p.topicCode.trim());
    }
  });
  const uniqueTopicsPracticed = practicedTopicCodes.size;

  const practicesCompletedCount = practiceReviews.length;
  const coveragePercent = safeTotalTopics > 0
    ? Math.min(100, Math.round((uniqueTopicsPracticed / safeTotalTopics) * 100))
    : 0;

  const volumePercent = safeTotalTopics > 0
    ? Math.min(100, Math.round((practicesCompletedCount / safeTotalTopics) * 100))
    : 0;

  // True Practice Effort: 60% Topic Breadth (Coverage) + 40% Session Volume (Depth)
  const effortsPercent = safeTotalTopics > 0 && practicesCompletedCount > 0
    ? Math.min(100, Math.round(0.60 * coveragePercent + 0.40 * volumePercent))
    : 0;

  return {
    averageMarks,
    examCount,
    objectiveAvg,
    subjectiveAvg,
    practiceAvg,
    overallMastery,
    lqScore,
    averageRetention,
    masteredTopicsCount,
    practicingTopicsCount,
    needsAttentionTopicsCount,
    unattemptedTopicsCount,
    uniqueTopicsPracticed,
    coveragePercent,
    srsDueTopicsCount,
    srsOverdueTopicsCount,
    effortsPercent,
    practicesCompletedCount,
    totalTopicsCount: safeTotalTopics,
    totalQuestionsPracticed,
    integrityScore: Math.min(100, Math.max(0, Math.round(integrityScore)))
  };
}

/**
 * Single Source of Truth (SSOT) for UI score color coding across Student, Parent, and Admin views.
 * - Score >= 85%: Mastered / High (var(--success))
 * - Score >= 60%: In Progress / Moderate (var(--warning))
 * - Score < 60%:  Needs Attention / Low (var(--danger))
 */
export function getScoreColor(score: number): string {
  if (score >= 85) return 'var(--success)';
  if (score >= 60) return 'var(--warning)';
  return 'var(--danger)';
}
