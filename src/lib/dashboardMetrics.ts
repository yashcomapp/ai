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
import { deriveTopicCodeFromQuestionCode, parseTopicCode, getCanonicalSubjectName } from '@/lib/questionTypes';

export interface ExtractConductedTopicCodesInput {
  masteryList?: Array<{ topicCode?: string; [key: string]: any }>;
  classroomExams?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionIds?: string[]; questionCodes?: string[]; [key: string]: any }>;
  homePractice?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionIds?: string[]; questionCodes?: string[]; [key: string]: any }>;
  assignments?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; [key: string]: any }>;
  objectiveExams?: Array<{ topicCode?: string; resolvedTopicCode?: string; topicCodes?: string[]; topics?: string[]; questionCodes?: string[]; [key: string]: any }> | Map<string, any>;
  practiceReviews?: Array<{ topicCode?: string; resolvedTopicCode?: string; [key: string]: any }>;
  objectiveReviews?: Array<{ topicCode?: string; resolvedTopicCode?: string; [key: string]: any }>;
}

function isCanonicalTopicCode(code?: string): boolean {
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

  // Strictly from assigned/conducted exams, homework, and practice sessions
  // (Do not include masteryList directly to prevent stale legacy mastery records from inflating the assigned syllabus)
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
 * Single Source of Truth (SSOT) Topic Confidence Requirement:
 * - Minor / Micro: 12 questions (2 sets of 6 Qs)
 * - Medium / Conceptual: 18 questions (3 sets of 6 Qs)
 * - Major / HOTS: 24 questions (4 sets of 6 Qs)
 */
export function getRequiredConfidence(topicClassification?: string, targetQuestions?: number): number {
  const cls = String(topicClassification || '').toLowerCase().trim();
  if (cls === 'minor' || cls === 'micro') return 12;
  if (cls === 'medium' || cls === 'moderate' || cls === 'conceptual') return 18;
  if (cls === 'major' || cls === 'calculative' || cls === 'hots') return 24;
  
  if (targetQuestions !== undefined) {
    if (targetQuestions <= 30) return 12;
    if (targetQuestions <= 50) return 18;
    return 24;
  }
  // Baseline default for granular subtopics is 12 questions (2 full sets of 6)
  return 12;
}

export interface ClassifyAssignedTopicsInput {
  assignedTopicCodes: Set<string> | string[];
  topicMasteries?: Array<any>;
  syllabusTopicsMap?: Map<string, any>;
  absentTopicCodes?: Set<string>;
  practiceReviews?: Array<any>;
  srsEnabled?: boolean;
}

export interface ClassifiedTopicItem {
  topicCode: string;
  topicName: string;
  topicNumber: string;
  chapterCode: string;
  chapterName: string;
  chapterNumber: string;
  subjectCode: string;
  subjectName: string;
  mastery: number;
  confidence: number;
  requiredConfidence: number;
  topicClassification: string;
  targetQuestions: number;
  state: 'mastered' | 'practicing' | 'needsAttention';
  isUnattempted: boolean;
  isAbsentExam: boolean;
  isRecoveryMastered: boolean;
  topicMasteryProgress: number;
  priorityScore: number;
  attempts: number;
  lastAttempt: string | null;
  lastScore: number;
  practiceCount: number;
  practiceQuestionsAttempted: number;
  srsSchedule?: any;
  mData?: any;
  sData?: any;
}

export interface ClassifyAssignedTopicsResult {
  topics: ClassifiedTopicItem[];
  mastered: ClassifiedTopicItem[];
  practicing: ClassifiedTopicItem[];
  needsAttention: ClassifiedTopicItem[];
  masteredCount: number;
  practicingCount: number;
  needsAttentionCount: number;
  unattemptedCount: number;
  totalAssignedCount: number;
  overallMastery: number;
  lqScore: number;
  averageRetention: number;
  srsDueTopicsCount: number;
  srsOverdueTopicsCount: number;
}

function calculateTopicPriority(mastery: number, confidence: number, reqConf: number): number {
  if (mastery < 50) return 100 - mastery;
  if (mastery < 90) return 50 + (90 - mastery);
  if (confidence < reqConf) return 20 + (reqConf - confidence);
  return 0;
}

/**
 * Single Source of Truth (SSOT) Topic Classification Engine
 *
 * Guarantees:
 * 1. Starts strictly from the canonical assigned syllabus set (the N conducted topics).
 * 2. Unifies parent/child resolution: only leaf topics are counted (never parent + child double-counted).
 * 3. Enforces confidence requirements strictly from syllabus metadata (reqConf).
 * 4. Places all unattempted topics in needsAttention (Red) with 0% mastery.
 * 5. Invariant: masteredCount + practicingCount + needsAttentionCount === totalAssignedCount.
 */
export function classifyAssignedTopics(input: ClassifyAssignedTopicsInput): ClassifyAssignedTopicsResult {
  const {
    assignedTopicCodes,
    topicMasteries = [],
    syllabusTopicsMap = new Map(),
    absentTopicCodes = new Set(),
    practiceReviews = [],
    srsEnabled = false
  } = input;

  // 1. Index student's mastery records by canonical topicCode
  const masteryMap = new Map<string, any>();
  topicMasteries.forEach(t => {
    if (t && t.topicCode) {
      masteryMap.set(String(t.topicCode).trim(), t);
    }
  });

  // 2. Canonical filtering of assigned codes
  const rawCodes = Array.isArray(assignedTopicCodes) ? assignedTopicCodes : Array.from(assignedTopicCodes || []);
  const validCodes = rawCodes.map(c => String(c || '').trim()).filter(isCanonicalTopicCode);

  // 3. Parent / Child Topic Code Resolution:
  // If both parent (e.g. CBSE-8-CURI-5-5.1) and subtopic (e.g. CBSE-8-CURI-5-5.1.1) exist in the assigned set,
  // the subtopic is the atomic unit. Omit the parent container so it is never double-counted.
  const leafCodes = validCodes.filter(c => !validCodes.some(other => other !== c && other.startsWith(c + '.')));
  // Deduplicate leaf codes
  const uniqueLeafCodes = Array.from(new Set(leafCodes)).sort();

  // 4. Index practice reviews for practiceCount and questions
  const practiceCountMap = new Map<string, number>();
  const practiceQuestionsMap = new Map<string, number>();
  practiceReviews.forEach(r => {
    const tCode = r.topicCode;
    if (tCode) {
      practiceCountMap.set(tCode, (practiceCountMap.get(tCode) || 0) + 1);
      const qCount = Number(
        r.questionsCount ?? 
        (Array.isArray(r.questions) ? r.questions.length : (Array.isArray(r.questionDetails) ? r.questionDetails.length : (r.totalQuestions || 6)))
      );
      practiceQuestionsMap.set(tCode, (practiceQuestionsMap.get(tCode) || 0) + qCount);
    }
  });

  const mastered: ClassifiedTopicItem[] = [];
  const practicing: ClassifiedTopicItem[] = [];
  const needsAttention: ClassifiedTopicItem[] = [];
  const allClassified: ClassifiedTopicItem[] = [];

  let certifiedNominalSum = 0;
  let certifiedEffectiveSum = 0;
  let totalRetentionSum = 0;
  let srsDueTopicsCount = 0;
  let srsOverdueTopicsCount = 0;
  let unattemptedCount = 0;

  uniqueLeafCodes.forEach(tCode => {
    // Resolve syllabus metadata: exact match first, then fall back to parent topic code
    let sData = syllabusTopicsMap.get(tCode);
    if (!sData) {
      for (const [sCode, val] of syllabusTopicsMap.entries()) {
        if (tCode.startsWith(sCode + '.')) {
          sData = val;
          break;
        }
      }
    }

    // Resolve mastery record: exact match first, then fall back to parent topic code
    let mData = masteryMap.get(tCode);
    if (!mData) {
      for (const [mCode, val] of masteryMap.entries()) {
        if (tCode.startsWith(mCode + '.')) {
          mData = val;
          break;
        }
      }
    }

    const isAbsentExam = absentTopicCodes.has(tCode);

    const targetQuestions = Number(sData?.targetQuestions || sData?.totalQuestions || sData?.questionCount || 30);
    const topicClassification = sData?.topicClassification || sData?.classification || mData?.topicClassification || (targetQuestions <= 35 ? 'minor' : (targetQuestions >= 55 ? 'major' : 'medium'));
    const reqConf = getRequiredConfidence(topicClassification, targetQuestions);

    const parsed = parseTopicCode(tCode);
    const subCode = sData?.subjectCode || mData?.subjectCode || parsed?.subjectCode || (tCode.includes('-') ? tCode.split('-')[2] : '') || '';
    const subName = sData?.subjectName || mData?.subjectName || getCanonicalSubjectName(subCode, tCode, sData?.chapterName);
    const chapName = sData?.chapterName || mData?.chapterName || (parsed?.chapterNumber ? `Chapter ${parsed.chapterNumber}` : 'General');
    const chapNum = sData?.chapterNumber || parsed?.chapterNumber || '';
    const topName = sData?.topicName || mData?.topicName || (parsed?.topicNumber ? `Topic ${parsed.topicNumber}` : tCode);

    const mastery = mData?.hasOwnProperty('mastery') ? Number(mData.mastery || 0) : 0;
    const confidence = mData?.hasOwnProperty('confidence') ? Number(mData.confidence || 0) : 0;
    const attempts = Number(mData?.attempts || mData?.attemptCount || mData?.totalAttempts || 0);
    const isRecoveryMastered = Boolean(mData?.isRecoveryMastered);
    const hasPracticed = Boolean(
      mData && (
        confidence > 0 ||
        Number(mData.questionsAttempted || 0) > 0 ||
        attempts > 0 ||
        isRecoveryMastered
      )
    );

    // Practice aggregations
    let practiceCount = practiceCountMap.get(tCode) || 0;
    let practiceQuestionsAttempted = Number(mData?.practiceQuestionsAttempted || practiceQuestionsMap.get(tCode) || 0);
    practiceCountMap.forEach((cnt, k) => {
      if (k !== tCode && (k.startsWith(tCode + '.') || tCode.startsWith(k + '.'))) {
        practiceCount += cnt;
      }
    });
    practiceQuestionsMap.forEach((cnt, k) => {
      if (k !== tCode && (k.startsWith(tCode + '.') || tCode.startsWith(k + '.'))) {
        practiceQuestionsAttempted += cnt;
      }
    });

    const priorityScore = isAbsentExam ? 999 : (!hasPracticed ? 995 : calculateTopicPriority(mastery, confidence, reqConf));

    // SRS calculation
    let retention = 100;
    let isDue = false;
    let isOverdue = false;
    let srsSchedule = null;

    if (srsEnabled && hasPracticed) {
      if (mData?.srsSchedule) {
        srsSchedule = mData.srsSchedule;
        retention = typeof srsSchedule.estimatedRetention === 'number' ? srsSchedule.estimatedRetention : 100;
        isDue = Boolean(srsSchedule.isDueForRevision);
        isOverdue = Number(srsSchedule.daysOverdue || 0) > 0;
      } else {
        const lastTime = mData?.lastRevisedAt || (mData?.updatedAt?.toDate ? mData.updatedAt.toDate() : mData?.updatedAt) || mData?.lastAttempt;
        srsSchedule = calculateSrsSchedule(lastTime, Number(mData?.srsStage || 0));
        retention = srsSchedule.estimatedRetention;
        isDue = srsSchedule.isDueForRevision;
        isOverdue = srsSchedule.daysOverdue > 0;
      }
      if (isDue) srsDueTopicsCount++;
      if (isOverdue) srsOverdueTopicsCount++;
    }
    totalRetentionSum += retention;

    const retentionFactor = srsEnabled ? (0.70 + 0.30 * (retention / 100)) : 1.0;

    let state: 'mastered' | 'practicing' | 'needsAttention';
    let topicMasteryProgress = 0;
    const isCertifiedMastered = isRecoveryMastered || (mastery >= 90 && confidence >= reqConf);

    if (!mData) {
      // Unattempted in the assigned syllabus -> strictly Needs Attention (0% score)
      state = 'needsAttention';
      topicMasteryProgress = 0;
      unattemptedCount++;
    } else if (isCertifiedMastered) {
      state = 'mastered';
      topicMasteryProgress = mastery;
    } else if (mastery >= 50) {
      state = 'practicing';
      const confRatio = Math.min(1.0, Math.max(0.05, confidence / reqConf));
      topicMasteryProgress = mastery * confRatio;
    } else {
      state = 'needsAttention';
      topicMasteryProgress = 0;
    }

    const effectiveProgress = srsEnabled ? Math.round(topicMasteryProgress * retentionFactor) : topicMasteryProgress;
    certifiedNominalSum += topicMasteryProgress;
    certifiedEffectiveSum += effectiveProgress;

    const item: ClassifiedTopicItem = {
      topicCode: tCode,
      topicName: topName,
      topicNumber: sData?.topicNumber || parsed?.topicNumber || '',
      chapterCode: sData?.chapterCode || (chapNum ? `${parsed?.boardCode || ''}-${parsed?.classNum || ''}-${subCode}-${chapNum}` : ''),
      chapterName: chapName,
      chapterNumber: chapNum,
      subjectCode: subCode,
      subjectName: subName,
      mastery,
      confidence,
      requiredConfidence: reqConf,
      topicClassification,
      targetQuestions,
      state,
      isUnattempted: !mData,
      isAbsentExam,
      isRecoveryMastered,
      topicMasteryProgress,
      priorityScore,
      attempts,
      lastAttempt: mData?.updatedAt?.toDate ? mData.updatedAt.toDate().toISOString() : mData?.updatedAt || mData?.lastAttempt || null,
      lastScore: mData?.lastScore || 0,
      practiceCount,
      practiceQuestionsAttempted,
      srsSchedule,
      mData,
      sData
    };

    allClassified.push(item);
    if (state === 'mastered') mastered.push(item);
    else if (state === 'practicing') practicing.push(item);
    else needsAttention.push(item);
  });

  const totalAssignedCount = uniqueLeafCodes.length;
  const overallMastery = totalAssignedCount > 0 ? Math.min(100, Math.round(certifiedNominalSum / totalAssignedCount)) : 0;
  const lqScore = srsEnabled
    ? (totalAssignedCount > 0 ? Math.min(100, Math.round(certifiedEffectiveSum / totalAssignedCount)) : overallMastery)
    : overallMastery;
  const averageRetention = srsEnabled
    ? (totalAssignedCount > 0 ? Math.round(totalRetentionSum / totalAssignedCount) : 100)
    : 100;

  return {
    topics: allClassified,
    mastered,
    practicing,
    needsAttention,
    masteredCount: mastered.length,
    practicingCount: practicing.length,
    needsAttentionCount: needsAttention.length,
    unattemptedCount,
    totalAssignedCount,
    overallMastery,
    lqScore,
    averageRetention,
    srsDueTopicsCount,
    srsOverdueTopicsCount
  };
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
  assignedTopicCodes?: Set<string> | string[];
  syllabusTopicsMap?: Map<string, any>;
  absentTopicCodes?: Set<string> | string[];
}

export interface UnifiedMetricsResult {
  // 1. Average Marks
  averageMarks: number;
  examCount: number;
  objectiveAvg: number;
  subjectiveAvg: number;
  practiceAvg: number;

  // 2. Mastery / LQ Score (SRS Retention Integrated via classifyAssignedTopics)
  overallMastery: number;       // Nominal Curriculum Mastery (0-100%)
  lqScore: number;              // True Retained Learning Quotient (0-100%)
  averageRetention: number;     // Average Memory Retention Index (0-100%)
  masteredTopicsCount: number;
  practicingTopicsCount: number;
  needsAttentionTopicsCount: number;
  unattemptedTopicsCount: number;
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

  // 5. Canonical Classified Topics (Full Breakdown)
  classifiedTopics?: ClassifyAssignedTopicsResult;
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

  // --- 2. Topic Mastery / LQ Score via Single Source of Truth (classifyAssignedTopics) ---
  const assignedCodes = input.assignedTopicCodes 
    ? (input.assignedTopicCodes instanceof Set ? input.assignedTopicCodes : new Set(input.assignedTopicCodes))
    : extractConductedTopicCodes({
        masteryList: topicMasteries,
        practiceReviews,
        objectiveReviews
      });

  const classified = classifyAssignedTopics({
    assignedTopicCodes: assignedCodes,
    topicMasteries,
    syllabusTopicsMap: input.syllabusTopicsMap,
    absentTopicCodes: input.absentTopicCodes instanceof Set ? input.absentTopicCodes : new Set(input.absentTopicCodes || []),
    practiceReviews,
    srsEnabled: Boolean(input.srsEnabled)
  });

  const masteredTopicsCount = classified.masteredCount;
  const practicingTopicsCount = classified.practicingCount;
  const needsAttentionTopicsCount = classified.needsAttentionCount;
  const unattemptedTopicsCount = classified.unattemptedCount;
  const overallMastery = classified.overallMastery;
  const lqScore = classified.lqScore;
  const averageRetention = classified.averageRetention;
  const srsDueTopicsCount = classified.srsDueTopicsCount;
  const srsOverdueTopicsCount = classified.srsOverdueTopicsCount;
  const safeTotalTopics = Math.max(1, classified.totalAssignedCount);

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
    integrityScore: Math.min(100, Math.max(0, Math.round(integrityScore))),
    classifiedTopics: classified
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
