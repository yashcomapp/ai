import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { chunkArray } from '@/lib/firestoreUtils';
import { 
  StudentData, 
  QuotientResult, 
  ParameterCalculator, 
  ScoreResult, 
  StudentObservation 
} from '@/types/quotient.types';
import { evaluateSessionSincerity } from '@/lib/practiceTimeUtils';
import { isDemoUser, getRequiredConfidence } from '@/lib/studentDb';
import { calculateSrsSchedule } from '@/lib/srsRotation';

export const MASTERY_THRESHOLDS = {
  MASTERED_MASTERY: 90,
  MASTERED_CONFIDENCE: 10,
  MEDIUM_HIGH_MASTERY: 70,
  MEDIUM_MASTERY: 50,
  WEAK_MASTERY: 50
};

// Strategy 1: Exam Performance & Absenteeism
export class ExamPerformanceCalculator implements ParameterCalculator {
  id = 'exam';
  name = 'Exam';
  weight = 0.25;

  calculate(data: StudentData): ScoreResult {
    const { assignments, attempts } = data;
    const conductedExams = (data as any).conductedExams || assignments || [];
    
    if (conductedExams.length === 0) {
      if (attempts.length > 0) {
        const totalScoreSum = attempts.reduce((sum, att) => {
          const pct = att.percentage != null && !isNaN(Number(att.percentage))
            ? Number(att.percentage)
            : (att.totalMarks > 0 ? (Number(att.score || 0) / Number(att.totalMarks)) * 100 : 0);
          return sum + pct;
        }, 0);
        return {
          score: Math.round(totalScoreSum / attempts.length),
          details: {
            totalAssigned: 0,
            completed: attempts.length,
            absent: 0,
            note: 'Calculated average of attempts since no explicit assignments exist'
          }
        };
      }
      return { score: 0, details: { totalAssigned: 0, completed: 0, absent: 0, reason: 'No exams conducted yet' } };
    }

    const attemptPercentages = new Map<string, number>();
    attempts.forEach(att => {
      if (att.examId) {
        const pct = att.percentage != null && !isNaN(Number(att.percentage))
          ? Number(att.percentage)
          : (att.totalMarks > 0 ? (Number(att.score || 0) / Number(att.totalMarks)) * 100 : 0);
        attemptPercentages.set(att.examId, pct);
      }
    });

    let completedCount = 0;
    let totalScoreSum = 0;

    conductedExams.forEach((exam: any) => {
      const eId = exam.id || exam.examId;
      if (attemptPercentages.has(eId)) {
        completedCount++;
        totalScoreSum += attemptPercentages.get(eId)!;
      }
    });

    const totalAssigned = conductedExams.length;
    const absentCount = Math.max(0, totalAssigned - completedCount);
    // Score is sum of completed exam percentages divided by total conducted exams (absent counts as 0)
    const score = totalAssigned > 0 ? Math.round(totalScoreSum / totalAssigned) : 0;

    return {
      score,
      details: {
        totalAssigned,
        completed: completedCount,
        absent: absentCount,
        attendanceRate: totalAssigned > 0 ? Math.round((completedCount / totalAssigned) * 100) : 0
      }
    };
  }
}

// Strategy 2: Practice Engagement & Quality (Coverage & Accuracy)
export class PracticeEngagementCalculator implements ParameterCalculator {
  id = 'practice';
  name = 'Practice';
  weight = 0.20;

  calculate(data: StudentData): ScoreResult {
    const { practiceRecords, assignedTopics = [] } = data;
    const parentReviews = data.parentReviews || [];
    
    if (parentReviews.length === 0) {
      return { 
        score: 0, 
        details: { 
          totalQuestionsAttempted: 0, 
          averageMastery: 0, 
          topicsAttemptedCount: 0, 
          totalAssignedTopics: assignedTopics.length,
          coveragePercent: 0,
          averageQuestionsPerTopic: 0 
        } 
      };
    }

    const totalQuestionsAttempted = parentReviews.reduce((sum: number, rev: any) => sum + (rev.totalQuestions || 0), 0);

    const topicPracticeMap = new Map<string, number>();
    const sessionScores: number[] = [];
    parentReviews.forEach((rev: any) => {
      const tCode = rev.topicCode;
      if (tCode) {
        topicPracticeMap.set(tCode, (topicPracticeMap.get(tCode) || 0) + (rev.totalQuestions || 0));
      }
      const sPercent = Number(rev.scorePercent != null ? rev.scorePercent : (rev.totalQuestions ? (rev.score / rev.totalQuestions) * 100 : 0));
      if (!isNaN(sPercent)) sessionScores.push(sPercent);
    });

    const avgPracticeScore = sessionScores.length > 0
      ? Math.round(sessionScores.reduce((sum, v) => sum + v, 0) / sessionScores.length)
      : 0;

    const totalAssignedTopics = Math.max(1, assignedTopics.length > 0 ? assignedTopics.length : topicPracticeMap.size);
    const coveragePercent = Math.min(100, Math.round((topicPracticeMap.size / totalAssignedTopics) * 100));

    // Practice Engagement is balanced between Topic Coverage (50%) and Practice Accuracy (50%)
    const score = Math.round(0.50 * coveragePercent + 0.50 * avgPracticeScore);

    const averageQuestionsPerTopic = topicPracticeMap.size > 0
      ? Math.round((totalQuestionsAttempted / topicPracticeMap.size) * 10) / 10
      : 0;

    return {
      score,
      details: {
        totalQuestionsAttempted,
        averagePracticeScore: avgPracticeScore,
        topicsAttemptedCount: topicPracticeMap.size,
        totalAssignedTopics,
        coveragePercent,
        averageQuestionsPerTopic
      }
    };
  }
}

export class PracticeQualityCalculator implements ParameterCalculator {
  id = 'quality';
  name = 'Quality';
  weight = 0.10;

  calculate(data: StudentData): ScoreResult {
    const { practiceRecords } = data;
    const parentReviews = data.parentReviews || [];
    
    if (parentReviews.length === 0) {
      return { 
        score: 0, 
        details: { 
          totalQuestionsAttempted: 0, 
          topicsAttemptedCount: 0, 
          averageQuestionsPerTopic: 0,
          pacingScore: 0,
          efficiencyScore: 0,
          accuracyScore: 0
        } 
      };
    }

    const totalQuestionsAttempted = parentReviews.reduce((sum: number, rev: any) => sum + (rev.totalQuestions || 0), 0);

    // 1. Session Score Accuracy (40%)
    const sessionScores: number[] = [];
    let totalPacingScore = 0;
    let rushedCount = 0;
    let fluencyCount = 0;

    parentReviews.forEach((rev: any) => {
      const sPercent = Number(rev.scorePercent != null ? rev.scorePercent : (rev.totalQuestions ? (rev.score / rev.totalQuestions) * 100 : 0));
      if (!isNaN(sPercent)) sessionScores.push(sPercent);

      let pacing = rev.sincerityPacingScore;
      if (typeof pacing !== 'number') {
        const sincerity = evaluateSessionSincerity({
          questions: rev.questions || rev.questionDetails || [],
          durationSpent: Number(rev.durationSpent || (rev.totalQuestions ? rev.totalQuestions * 35 : 180)),
          scorePercent: Number(rev.scorePercent || 100)
        });
        pacing = sincerity.sincerityPacingScore;
        if (sincerity.isSolvedTooFast) rushedCount++;
        if (sincerity.isFastFluency) fluencyCount++;
      } else {
        if (rev.isSolvedTooFast) rushedCount++;
        if (rev.isFastFluency) fluencyCount++;
      }
      totalPacingScore += pacing;
    });

    const averageAccuracyScore = sessionScores.length > 0
      ? Math.round(sessionScores.reduce((sum, v) => sum + v, 0) / sessionScores.length)
      : 0;

    const averagePacingScore = parentReviews.length > 0
      ? Math.round(totalPacingScore / parentReviews.length)
      : 100;

    // 2. Mastery Efficiency Score per topic (30%)
    const topicPracticeMap = new Map<string, number>();
    parentReviews.forEach((rev: any) => {
      const tCode = rev.topicCode;
      if (tCode) {
        topicPracticeMap.set(tCode, (topicPracticeMap.get(tCode) || 0) + (rev.totalQuestions || 0));
      }
    });

    const masteryMap = new Map<string, number>();
    const confidenceMap = new Map<string, number>();
    const requiredConfidenceMap = new Map<string, number>();
    practiceRecords.forEach(rec => {
      if (rec.topicCode) {
        masteryMap.set(rec.topicCode, rec.mastery || 0);
        confidenceMap.set(rec.topicCode, rec.confidence || 0);
        requiredConfidenceMap.set(rec.topicCode, getRequiredConfidence(rec.topicClassification, rec.targetQuestions));
      }
    });

    let totalEfficiencyScore = 0;
    topicPracticeMap.forEach((q, topicCode) => {
      const mastery = masteryMap.get(topicCode) || 0;
      const confidence = confidenceMap.get(topicCode) || 0;
      const reqConf = requiredConfidenceMap.get(topicCode) || 10;
      
      let topicEfficiency = 0;
      if (mastery >= MASTERY_THRESHOLDS.MASTERED_MASTERY && confidence >= reqConf) {
        const excess = Math.max(0, q - 15);
        topicEfficiency = Math.max(40, 100 - excess * 1.5);
      } else {
        const excess = Math.max(0, q - 15);
        topicEfficiency = Math.max(0, mastery - excess * 1.5);
      }
      totalEfficiencyScore += topicEfficiency;
    });

    const averageEfficiencyScore = topicPracticeMap.size > 0 
      ? Math.round(totalEfficiencyScore / topicPracticeMap.size)
      : 100;

    // Quality Score = 40% Session Accuracy + 30% Pacing Sincerity + 30% Mastery Efficiency
    const qualityScore = Math.max(0, Math.min(100, Math.round(
      averageAccuracyScore * 0.40 + 
      averagePacingScore * 0.30 + 
      averageEfficiencyScore * 0.30
    )));

    const averageQuestionsPerTopic = topicPracticeMap.size > 0
      ? Math.round((totalQuestionsAttempted / topicPracticeMap.size) * 10) / 10
      : 0;

    return {
      score: qualityScore,
      details: {
        totalQuestionsAttempted,
        topicsAttemptedCount: topicPracticeMap.size,
        averageQuestionsPerTopic,
        accuracyScore: averageAccuracyScore,
        pacingScore: averagePacingScore,
        efficiencyScore: averageEfficiencyScore,
        rushedCount,
        fluencyCount
      }
    };
  }
}

// Strategy 3: Topic Health (Continuous Mastery & Retention)
export class TopicHealthCalculator implements ParameterCalculator {
  id = 'topicHealth';
  name = 'Topic Health';
  weight = 0.25;

  calculate(data: StudentData): ScoreResult {
    const { practiceRecords, assignedTopics } = data;
    
    // Helper to calculate retention factor
    const getRetentionFactor = (rec: any): { retention: number; factor: number; isDue: boolean } => {
      const lastTime = rec.lastRevisedAt || (rec.updatedAt?.toDate ? rec.updatedAt.toDate() : rec.updatedAt) || rec.lastAttempt;
      const sched = calculateSrsSchedule(lastTime, Number(rec.srsStage || 0));
      const retention = sched.estimatedRetention;
      const factor = 0.70 + 0.30 * (retention / 100);
      return { retention, factor, isDue: sched.isDueForRevision };
    };

    // If no assigned topics are resolved, fallback using practiceRecords
    if (!assignedTopics || assignedTopics.length === 0) {
      if (practiceRecords.length === 0) {
        return { score: 0, details: { totalTopics: 0, masteredCount: 0, attentionCount: 0, srsDueCount: 0, averageRetention: 100 } };
      }
      const totalTopics = practiceRecords.length;
      let totalMasteryEarned = 0;
      let attentionCount = 0;
      let masteredCount = 0;
      let srsDueCount = 0;
      let totalRetentionSum = 0;

      practiceRecords.forEach(rec => {
        const mastery = Number(rec.mastery || 0);
        const confidence = Number(rec.confidence || 0);
        const isRecovery = Boolean(rec.isRecoveryMastered);
        const reqConf = getRequiredConfidence(rec.topicClassification, rec.targetQuestions);
        const { retention, factor, isDue } = getRetentionFactor(rec);
        if (isDue) srsDueCount++;
        totalRetentionSum += retention;

        if (isRecovery || (mastery >= 90 && confidence >= reqConf)) {
          masteredCount++;
        }
        if (mastery < 50) attentionCount++;
        const confidenceFactor = Math.min(1, Math.max(0.5, confidence / reqConf));
        totalMasteryEarned += mastery * confidenceFactor * factor;
      });
      const score = Math.max(0, Math.min(100, Math.round(totalMasteryEarned / totalTopics)));
      return {
        score,
        details: {
          totalTopics,
          masteredCount,
          attentionCount,
          srsDueCount,
          averageRetention: Math.round(totalRetentionSum / totalTopics),
          masteryRatio: totalTopics > 0 ? Math.round((masteredCount / totalTopics) * 100) : 0,
          attentionRatio: totalTopics > 0 ? Math.round((attentionCount / totalTopics) * 100) : 0,
          fallbackUsed: true
        }
      };
    }

    const totalTopics = assignedTopics.length;
    let totalMasteryEarned = 0;
    let attentionCount = 0;
    let masteredCount = 0;
    let srsDueCount = 0;
    let totalRetentionSum = 0;

    // Create a lookup map of attempted practice records by topicCode using all-time practice records
    const practiceMap = new Map();
    const recordsToUse = data.allPracticeRecords || practiceRecords;
    recordsToUse.forEach((rec: any) => {
      const topicKey = rec.topicCode;
      if (topicKey) {
        practiceMap.set(topicKey, rec);
      }
    });

    assignedTopics.forEach((topicCode: string) => {
      const record = practiceMap.get(topicCode);
      if (record) {
        const mastery = Number(record.mastery || 0);
        const confidence = Number(record.confidence || 0);
        const isRecovery = Boolean(record.isRecoveryMastered);
        const reqConf = getRequiredConfidence(record.topicClassification, record.targetQuestions);
        const { retention, factor, isDue } = getRetentionFactor(record);
        if (isDue) srsDueCount++;
        totalRetentionSum += retention;

        if (isRecovery || (mastery >= 90 && confidence >= reqConf)) {
          masteredCount++;
        }

        if (mastery < 50) {
          attentionCount++;
        }

        // Continuous confidence & SRS retention scaling
        const confidenceFactor = Math.min(1, Math.max(0.5, confidence / reqConf));
        const effectiveTopicScore = mastery * confidenceFactor * factor;
        totalMasteryEarned += effectiveTopicScore;
      } else {
        // Not even started or opened: counts as 0% mastery, needs attention
        attentionCount++;
        totalRetentionSum += 100;
      }
    });

    const averageTopicHealth = totalTopics > 0 ? (totalMasteryEarned / totalTopics) : 0;
    const attentionRatio = totalTopics > 0 ? (attentionCount / totalTopics) : 0;
    
    // Penalize heavily unattempted topics proportionally
    const penalty = attentionRatio > 0.5 ? (attentionRatio - 0.5) * 20 : 0;
    const score = Math.max(0, Math.min(100, Math.round(averageTopicHealth - penalty)));

    return {
      score,
      details: {
        totalTopics,
        masteredCount,
        attentionCount,
        srsDueCount,
        averageRetention: totalTopics > 0 ? Math.round(totalRetentionSum / totalTopics) : 100,
        masteryRatio: totalTopics > 0 ? Math.round((masteredCount / totalTopics) * 100) : 0,
        attentionRatio: totalTopics > 0 ? Math.round((attentionRatio) * 100) : 0,
        averageMastery: Math.round(averageTopicHealth),
        fallbackUsed: false
      }
    };
  }
}

// Strategy 4: Proctoring Integrity Average
export class IntegrityScoreCalculator implements ParameterCalculator {
  id = 'integrity';
  name = 'Proctoring Integrity';
  weight = 0.00;

  calculate(data: StudentData): ScoreResult {
    const { integrityRecords } = data;
    if (integrityRecords.length === 0) {
      return { score: 100, details: { weeksLogged: 0, reason: 'No integrity scores logged yet' } };
    }

    const totalScoreSum = integrityRecords.reduce((sum, rec) => sum + (rec.integrityScore ?? 100), 0);
    const score = Math.round(totalScoreSum / integrityRecords.length);

    return {
      score,
      details: {
        weeksLogged: integrityRecords.length,
        averageWeeklyViolations: Math.round(
          (integrityRecords.reduce((sum, rec) => sum + (rec.violationsCount || 0), 0) / integrityRecords.length) * 10
        ) / 10
      }
    };
  }
}

// Strategy 5: Classroom Observations (Dynamic Parameters support)
export class ClassObservationsCalculator implements ParameterCalculator {
  id = 'observations';
  name = 'Obs';
  weight = 0.20;

  calculate(data: StudentData): ScoreResult {
    const { observations, activeParameters } = data;
    const parameters = activeParameters || [
      { id: 'activeParticipation', name: 'Active Participation', weight: 0.20 },
      { id: 'sincerity', name: 'Sincerity & Behavior', weight: 0.20 },
      { id: 'timelyWork', name: 'Timely Work', weight: 0.20 },
      { id: 'parentScore', name: 'Parent Score (Strict)', weight: 0.40 }
    ];

    if (parameters.length === 0) {
      return { score: 100, details: { observationCount: 0, parameters: [] } };
    }

    const scoresMap: Record<string, number[]> = {};
    parameters.forEach((p: any) => {
      scoresMap[p.id] = [];
    });

    observations.forEach((obs: any) => {
      if (obs.parameterId && obs.score !== undefined) {
        if (scoresMap[obs.parameterId]) {
          scoresMap[obs.parameterId].push(Number(obs.score));
        }
      } else {
        // Legacy support
        if (obs.activeParticipation !== undefined && scoresMap['activeParticipation']) {
          scoresMap['activeParticipation'].push(Number(obs.activeParticipation));
        }
        if (obs.sincerity !== undefined && scoresMap['sincerity']) {
          scoresMap['sincerity'].push(Number(obs.sincerity));
        }
        if (obs.timelyWork !== undefined && scoresMap['timelyWork']) {
          scoresMap['timelyWork'].push(Number(obs.timelyWork));
        }
        if (obs.parentScore !== undefined && scoresMap['parentScore']) {
          scoresMap['parentScore'].push(Number(obs.parentScore));
        }
      }
    });

    const parameterDetails: any[] = [];
    let weightedScoreSum = 0;
    let totalWeightSum = 0;

    parameters.forEach((p: any) => {
      const scores = scoresMap[p.id] || [];
      let avg = 50; // Neutral baseline fallback
      if (scores.length > 0) {
        avg = Math.round(scores.reduce((sum, val) => sum + val, 0) / scores.length);
      }

      let paramWeight = 0.20;
      if (p.weight !== undefined && p.weight !== null && Number(p.weight) > 0) {
        paramWeight = Number(p.weight);
      } else if (p.id === 'parentScore') {
        paramWeight = 0.40;
      } else {
        paramWeight = 0.20;
      }

      weightedScoreSum += avg * paramWeight;
      totalWeightSum += paramWeight;

      parameterDetails.push({
        id: p.id,
        name: p.name,
        average: avg,
        weight: paramWeight,
        logsCount: scores.length
      });
    });

    const score = totalWeightSum > 0 ? Math.round(weightedScoreSum / totalWeightSum) : 50;

    return {
      score,
      details: {
        observationCount: observations.length,
        parameters: parameterDetails
      }
    };
  }
}

const getTopicCodeFromQuestionCode = deriveTopicCodeFromQuestionCode;

export function resolveSubjectCode(subjectName: string, classNum?: string | number): string {
  const s = String(subjectName || '').toLowerCase();
  const c = String(classNum || '');
  if (s.includes('science and tech') && (s.includes('2') || s.includes('part 2') || s.includes('part - 2'))) return 'SCIT2';
  if (s.includes('science and tech') && (s.includes('1') || s.includes('part 1') || s.includes('part - 1'))) return 'SCIT1';
  if (s.includes('curiosity') || (s.includes('science') && c === '8')) return 'CURI';
  if (s.includes('exploration') || (s.includes('science') && c === '9')) return 'SCIE';
  if (s.includes('science')) return 'SCIT';
  if (s.includes('algebra') || (s.includes('math') && (s.includes('1') || s.includes('part 1') || s.includes('part - 1')))) return 'MTH1';
  if (s.includes('geometry') || (s.includes('math') && (s.includes('2') || s.includes('part 2') || s.includes('part - 2')))) return 'MTH2';
  if (s.includes('ganit') || (s.includes('math') && c === '8')) return 'MGP1';
  if (s.includes('math')) return 'MTH';
  return 'SCIT2';
}

export function getObjectiveExamTopics(exam: any): string[] {
  const topics = new Set<string>();
  if (!exam) return [];

  const rawId = String(exam.id || '');
  const idParts = rawId.split('-');

  const board = exam.boardCode || (idParts.length > 2 && /^(MH|CBSE)$/i.test(idParts[1]) ? idParts[1] : (idParts.length > 1 && /^(MH|CBSE)$/i.test(idParts[0]) ? idParts[0] : 'MH'));
  const classCode = String(exam.class || (idParts.length > 2 && /^\d+$/.test(idParts[2]) ? idParts[2] : (idParts.length > 1 && /^\d+$/.test(idParts[1]) ? idParts[1] : '10')));
  const subjectCode = exam.subjectCode || resolveSubjectCode((exam.subjects || [])[0] || exam.subjectName || rawId, classCode);

  const tCodes = exam.topicCodes || (exam.topicCode ? [exam.topicCode] : []);
  tCodes.forEach((t: string) => {
    if (!t) return;
    if (t.includes('-') && t.split('-').length >= 4) {
      topics.add(t);
    } else {
      const chapterNumber = t.includes('.') ? t.split('.')[0] : (exam.chapterNumber || '1');
      topics.add(`${board}-${classCode}-${subjectCode}-${chapterNumber}-${t}`);
    }
  });

  const qIds = exam.questionIds || [];
  qIds.forEach((qCode: string) => {
    const tc = deriveTopicCodeFromQuestionCode(qCode);
    if (tc) topics.add(tc);
  });

  return Array.from(topics);
}

export function getSubjectiveExamTopics(exam: any): string[] {
  const topics = new Set<string>();
  if (!exam) return [];

  const questionIds = exam.questionIds || [];
  questionIds.forEach((qCode: string) => {
    const tc = deriveTopicCodeFromQuestionCode(qCode);
    if (tc) topics.add(tc);
  });

  const questions = exam.questions || [];
  questions.forEach((q: any) => {
    if (q.questionCode) {
      const tc = deriveTopicCodeFromQuestionCode(q.questionCode);
      if (tc) topics.add(tc);
    }
  });

  const tCodes = exam.topicCodes || [];
  tCodes.forEach((tc: string) => {
    if (tc) topics.add(tc);
  });

  return Array.from(topics);
}

export function getExamDateKey(exam: any): string {
  if (exam.scheduledDate) return String(exam.scheduledDate);
  if (exam.dateKey) return String(exam.dateKey);
  if (exam.createdAt) {
    if (typeof exam.createdAt.toDate === 'function') {
      return getDateKeyIST(exam.createdAt.toDate());
    }
    const d = new Date(exam.createdAt);
    if (!isNaN(d.getTime())) return getDateKeyIST(d);
  }
  const idStr = String(exam.id || '');
  const idMatch = idStr.match(/(\d{2})(\d{2})(\d{2})$/);
  if (idMatch) {
    const day = idMatch[1];
    const month = idMatch[2];
    const year = '20' + idMatch[3];
    return `${year}-${month}-${day}`;
  }
  return '';
}

export function isExamForStudent(exam: any, studentCode: string, bIds: string[], studentClass?: string): boolean {
  if (!exam) return false;
  if (exam.targetStudents && Array.isArray(exam.targetStudents) && exam.targetStudents.includes(studentCode)) {
    return true;
  }
  if (exam.batchId && bIds.includes(exam.batchId)) {
    return true;
  }
  if (Array.isArray(exam.batchIds) && exam.batchIds.some((b: string) => bIds.includes(b))) {
    return true;
  }
  if (Array.isArray(exam.targetBatches) && exam.targetBatches.some((b: string) => bIds.includes(b))) {
    return true;
  }
  if (studentClass) {
    const normStudent = String(studentClass).replace(/\D/g, '');
    const normExam = String(exam.class || exam.className || '').replace(/\D/g, '');
    if (normExam && normStudent && normExam === normStudent) {
      const hasSpecificBatches = (Array.isArray(exam.batchIds) && exam.batchIds.length > 0) ||
                                (Array.isArray(exam.targetBatches) && exam.targetBatches.length > 0) ||
                                (exam.batchId);
      if (!hasSpecificBatches) {
        return true;
      }
    }
  }
  return false;
}

export class QuotientService {
  private static calculators: ParameterCalculator[] = [
    new ExamPerformanceCalculator(),
    new PracticeEngagementCalculator(),
    new PracticeQualityCalculator(),
    new TopicHealthCalculator(),
    new IntegrityScoreCalculator(),
    new ClassObservationsCalculator()
  ];

  /**
   * Fetches active parameters from Firestore or seeds defaults.
   */
  static async getParameters(): Promise<any[]> {
    const parametersSnap = await adminDb.collection('quotientParameters').orderBy('createdAt', 'asc').get();
    let parameters = parametersSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));

    const defaultStandardParams = [
      { id: 'activeParticipation', name: 'Active Participation', weight: 0.20, createdAt: new Date() },
      { id: 'sincerity', name: 'Sincerity & Behavior', weight: 0.20, createdAt: new Date() },
      { id: 'timelyWork', name: 'Timely Work', weight: 0.20, createdAt: new Date() },
      { id: 'parentScore', name: 'Parent Score (Strict)', weight: 0.40, createdAt: new Date() }
    ];

    if (parameters.length === 0) {
      const batch = adminDb.batch();
      defaultStandardParams.forEach(p => {
        const ref = adminDb.collection('quotientParameters').doc(p.id);
        batch.set(ref, p);
      });
      await batch.commit();
      return defaultStandardParams;
    }

    // Ensure Parent Score (Strict) exists in Firestore
    const hasParentScore = parameters.some(p => p.id === 'parentScore');
    if (!hasParentScore) {
      const parentScoreParam = { id: 'parentScore', name: 'Parent Score (Strict)', weight: 0.40, createdAt: new Date() };
      await adminDb.collection('quotientParameters').doc('parentScore').set(parentScoreParam, { merge: true });
      parameters.push(parentScoreParam);
    }

    return parameters.map((p: any) => {
      let weight = p.weight;
      if (weight === undefined || weight === null) {
        weight = p.id === 'parentScore' ? 0.40 : 0.20;
      }
      return { ...p, weight };
    });
  }

  /**
   * Fetches all records from Firestore and calculates the overall student LQ scorecard.
   */
  static getStartDateForDuration(duration: string): Date | null {
    const now = new Date();
    const istOffset = 5.5 * 60 * 60 * 1000;
    const nowIst = new Date(Date.now() + istOffset);
    
    if (duration === 'all') {
      return null;
    }
    if (duration === 'weekly') {
      const day = nowIst.getUTCDay();
      const diff = nowIst.getUTCDate() - day + (day === 0 ? -6 : 1);
      const startOfWeek = new Date(nowIst);
      startOfWeek.setUTCDate(diff);
      startOfWeek.setUTCHours(0, 0, 0, 0);
      return new Date(startOfWeek.getTime() - istOffset);
    } else if (duration === 'monthly') {
      const startOfMonth = new Date(nowIst);
      startOfMonth.setUTCDate(1);
      startOfMonth.setUTCHours(0, 0, 0, 0);
      return new Date(startOfMonth.getTime() - istOffset);
    }

    // Parse customized values: e.g. "7d", "30d", "2w", "3m", "6m"
    const match = duration.match(/^(\d+)([dwm])$/);
    if (match) {
      const value = parseInt(match[1], 10);
      const unit = match[2];
      const targetDate = new Date(nowIst);

      if (unit === 'd') {
        targetDate.setUTCDate(targetDate.getUTCDate() - value);
      } else if (unit === 'w') {
        targetDate.setUTCDate(targetDate.getUTCDate() - (value * 7));
      } else if (unit === 'm') {
        targetDate.setUTCMonth(targetDate.getUTCMonth() - value);
      }

      targetDate.setUTCHours(0, 0, 0, 0);
      return new Date(targetDate.getTime() - istOffset);
    }

    return null;
  }

  static isWithinDateRange(timestampVal: any, startDate: Date | null): boolean {
    if (!startDate) return true;
    if (!timestampVal) return false;
    try {
      let d: Date;
      if (typeof timestampVal.toDate === 'function') {
        d = timestampVal.toDate();
      } else {
        d = new Date(timestampVal);
      }
      return d.getTime() >= startDate.getTime();
    } catch (e) {
      return false;
    }
  }

  static filterByDate(list: any[], dateFieldNames: string[], startDate: Date | null): any[] {
    if (!startDate) return list;
    return list.filter((item: any) => {
      for (const field of dateFieldNames) {
        if (this.isWithinDateRange(item[field], startDate)) {
          return true;
        }
      }
      return false;
    });
  }

  static computeStudentQuotientScore(
    studentCode: string,
    duration: string,
    activeParameters: any[],
    bIds: string[],
    rawAttempts: any[],
    rawAssignments: any[],
    rawPractice: any[],
    rawIntegrity: any[],
    rawObservations: any[],
    rawReviews: any[],
    examsMap: Map<string, any>,
    subjectiveExamsList: any[],
    studentClass?: string
  ): QuotientResult {
    const todayDateStr = getDateKeyIST();
    const startDate = duration ? this.getStartDateForDuration(duration) : null;

    const filteredAttempts = this.filterByDate(rawAttempts, ['timestamp', 'createdAt', 'completedAt'], startDate);
    const filteredAssignments = this.filterByDate(rawAssignments, ['createdAt', 'dueDate'], startDate);
    const filteredSubjectiveExams = this.filterByDate(subjectiveExamsList, ['scheduledDate', 'createdAt'], startDate);

    const topicsSet = new Set<string>();
    const conductedObjectiveExams: any[] = [];

    // 1. Gather all conducted objective exams matching student batch or class
    examsMap.forEach((exam: any) => {
      const isMatch = isExamForStudent(exam, studentCode, bIds, studentClass);
      const examDateStr = getExamDateKey(exam) || todayDateStr;
      const isPastOrToday = examDateStr <= todayDateStr;
      const withinDate = this.isWithinDateRange(exam.scheduledDate || exam.createdAt || examDateStr, startDate);

      if (isMatch && isPastOrToday && withinDate) {
        conductedObjectiveExams.push(exam);
        getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
      }
    });

    // 2. Sourcing from actual objective exam attempts (including ad-hoc/direct)
    filteredAttempts.forEach((attData: any) => {
      const exam = examsMap.get(attData.examId);
      if (exam) {
        getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
        const eId = exam.id || exam.examId;
        if (!conductedObjectiveExams.some(e => (e.id || e.examId) === eId)) {
          conductedObjectiveExams.push(exam);
        }
      }
    });

    // 3. Sourcing from assignments
    filteredAssignments.forEach((assData: any) => {
      const exam = examsMap.get(assData.examId);
      if (exam) {
        getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
        const eId = exam.id || exam.examId;
        if (!conductedObjectiveExams.some(e => (e.id || e.examId) === eId)) {
          conductedObjectiveExams.push(exam);
        }
      }
    });

    // 4. Gather all conducted subjective exams matching student batch or class
    const conductedSubjectiveExams: any[] = [];
    filteredSubjectiveExams.forEach((subExam: any) => {
      const isMatch = isExamForStudent(subExam, studentCode, bIds, studentClass);
      const scheduledDateStr = subExam.scheduledDate || getExamDateKey(subExam) || todayDateStr;
      const isPastOrToday = scheduledDateStr <= todayDateStr;
      
      if (isMatch && isPastOrToday) {
        conductedSubjectiveExams.push(subExam);
        getSubjectiveExamTopics(subExam).forEach(t => topicsSet.add(t));
      }
    });

    // 5. Add practiced topics from parentReviews
    const filteredReviews = this.filterByDate(rawReviews, ['timestamp', 'createdAt'], startDate);
    filteredReviews.forEach((rev: any) => {
      if (rev.topicCode) topicsSet.add(rev.topicCode);
    });

    const assignedTopics = Array.from(topicsSet);
    const conductedExams = [...conductedObjectiveExams, ...conductedSubjectiveExams];

    const filteredIntegrity = this.filterByDate(rawIntegrity, ['timestamp', 'createdAt'], startDate);
    const filteredObservations = this.filterByDate(rawObservations, ['observedAt', 'timestamp'], startDate);

    const practicedTopics = new Set(filteredReviews.map((r: any) => r.topicCode).filter(Boolean));
    const filteredPractice = startDate 
      ? rawPractice.filter((rec: any) => rec.topicCode && practicedTopics.has(rec.topicCode))
      : rawPractice;

    const studentData: StudentData = {
      studentCode,
      attempts: filteredAttempts,
      assignments: filteredAssignments,
      conductedExams,
      practiceRecords: filteredPractice,
      integrityRecords: filteredIntegrity,
      observations: filteredObservations,
      activeParameters,
      assignedTopics,
      parentReviews: filteredReviews,
      allPracticeRecords: rawPractice
    };

    const components = this.calculators.map(calc => {
      const result = calc.calculate(studentData);
      let score = result.score;

      if (startDate) {
        if (calc.id === 'exam' && studentData.attempts.length === 0 && conductedExams.length === 0) {
          score = null as any;
        }
        if (calc.id === 'integrity' && studentData.integrityRecords.length === 0) {
          score = 100;
        }
        if (calc.id === 'practice' && filteredReviews.length === 0) {
          score = 0;
        }
        if (calc.id === 'quality' && filteredReviews.length === 0) {
          score = 0;
        }
      }

      return {
        parameterId: calc.id,
        parameterName: calc.name,
        score,
        weight: calc.weight,
        details: result.details
      };
    });

    let totalWeight = 0;
    let weightedScoreSum = 0;

    components.forEach(comp => {
      if (comp.score !== null) {
        totalWeight += comp.weight;
        weightedScoreSum += comp.score * comp.weight;
      }
    });

    let finalLQ = totalWeight > 0 
      ? Math.min(100, Math.round(weightedScoreSum / totalWeight)) 
      : 0;

    if (startDate) {
      const practicedCount = filteredReviews.reduce((sum, r) => sum + (r.totalQuestions || 0), 0);
      const examsCount = filteredAttempts.length;
      if (practicedCount === 0 && examsCount === 0) {
        finalLQ = 0;
      }
    }

    const finalComponents = components.map(comp => {
      const contribution = comp.score !== null ? Math.round(comp.score * comp.weight * 10) / 10 : 0;
      return {
        ...comp,
        contribution
      };
    });

    return {
      studentCode,
      overallQuotient: finalLQ,
      components: finalComponents,
      calculatedAt: new Date()
    };
  }

  static async calculateStudentQuotient(studentCode: string, duration: string = 'monthly'): Promise<QuotientResult> {
    const activeParameters = await this.getParameters();

    // 1. Fetch user doc first to resolve batchIds and class
    const studentUserQuery = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();

    let bIds: string[] = [];
    let studentClass = '';
    if (!studentUserQuery.empty) {
      const userData = studentUserQuery.docs[0].data();
      bIds = userData.batchIds || (userData.batchId ? [userData.batchId] : []);
      studentClass = userData.class || userData.className || '';
    }

    // 2. Fetch student specific records and all exams in parallel
    const [
      attemptsSnap,
      assignmentsSnap,
      practiceSnap,
      integritySnap,
      observationsSnap,
      parentReviewsSnap,
      examsSnap,
      subjectiveExamsSnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').where('studentCode', '==', studentCode).get(),
      adminDb.collection('assignments').where('studentCode', '==', studentCode).get(),
      adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCode).get(),
      adminDb.collection('integrityScores').where('studentCode', '==', studentCode).get(),
      adminDb.collection('studentObservations').where('studentCode', '==', studentCode).get(),
      adminDb.collection('parentReviews').where('studentCode', '==', studentCode).get(),
      adminDb.collection('exams').get(),
      adminDb.collection('subjectiveExams').get()
    ]);

    const examsMap = new Map();
    examsSnap.docs.forEach(doc => {
      examsMap.set(doc.id, { id: doc.id, ...doc.data() });
    });

    const rawAttempts = attemptsSnap.docs.map((doc: any) => doc.data() as any).filter((att: any) => att.examType !== 'entrance');
    const rawAssignments = assignmentsSnap.docs.map((doc: any) => doc.data() as any).filter((ass: any) => ass.examType !== 'entrance');
    const rawPractice = practiceSnap.docs.map((doc: any) => doc.data() as any);
    const rawIntegrity = integritySnap.docs.map((doc: any) => doc.data() as any);
    const rawObservations = observationsSnap.docs.map((doc: any) => doc.data() as any);
    const rawReviews = parentReviewsSnap.docs.map((doc: any) => doc.data() as any);
    const subjectiveExamsList = subjectiveExamsSnap.docs.map((doc: any) => ({ id: doc.id, ...doc.data() }));

    return this.computeStudentQuotientScore(
      studentCode,
      duration,
      activeParameters,
      bIds,
      rawAttempts,
      rawAssignments,
      rawPractice,
      rawIntegrity,
      rawObservations,
      rawReviews,
      examsMap,
      subjectiveExamsList,
      studentClass
    );
  }

  static async calculateBulkQuotients(studentCodes: string[], duration: string = 'monthly'): Promise<Record<string, QuotientResult>> {
    const activeParameters = await this.getParameters();

    const [
      attemptsSnap,
      assignmentsSnap,
      practiceSnap,
      integritySnap,
      observationsSnap,
      usersSnap,
      examsSnap,
      subjectiveExamsSnap,
      batchesSnap,
      parentReviewsSnap
    ] = await Promise.all([
      adminDb.collection('examAttempts').get(),
      adminDb.collection('assignments').get(),
      adminDb.collection('studentTopicMastery').get(),
      adminDb.collection('integrityScores').get(),
      adminDb.collection('studentObservations').get(),
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('exams').get(),
      adminDb.collection('subjectiveExams').get(),
      adminDb.collection('batches').get(),
      adminDb.collection('parentReviews').get()
    ]);

    const examsMap = new Map();
    examsSnap.docs.forEach(doc => {
      examsMap.set(doc.id, { id: doc.id, ...doc.data() });
    });

    const subjectiveExamsList = subjectiveExamsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() }));

    const studentBatchesMap = new Map<string, string[]>();
    const studentClassMap = new Map<string, string>();
    usersSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode && !isDemoUser(data)) {
        const bIds = data.batchIds || (data.batchId ? [data.batchId] : []);
        studentBatchesMap.set(data.studentCode, bIds);
        studentClassMap.set(data.studentCode, data.class || data.className || '');
      }
    });

    const rawAttempts = attemptsSnap.docs.map((doc: any) => doc.data()).filter((att: any) => att.examType !== 'entrance' && !isDemoUser(att));
    const rawAssignments = assignmentsSnap.docs.map((doc: any) => doc.data()).filter((ass: any) => ass.examType !== 'entrance' && !isDemoUser(ass));
    const rawPractice = practiceSnap.docs.map((doc: any) => doc.data()).filter((p: any) => !isDemoUser(p));
    const rawIntegrity = integritySnap.docs.map((doc: any) => doc.data()).filter((i: any) => !isDemoUser(i));
    const rawObservations = observationsSnap.docs.map((doc: any) => doc.data()).filter((o: any) => !isDemoUser(o));
    const rawReviews = parentReviewsSnap.docs.map((doc: any) => doc.data()).filter((r: any) => !isDemoUser(r));

    const groupByStudent = (list: any[]) => {
      const map: Record<string, any[]> = {};
      list.forEach(item => {
        const code = item.studentCode;
        if (code) {
          if (!map[code]) map[code] = [];
          map[code].push(item);
        }
      });
      return map;
    };

    const attemptsMap = groupByStudent(rawAttempts);
    const assignmentsMap = groupByStudent(rawAssignments);
    const practiceMap = groupByStudent(rawPractice);
    const integrityMap = groupByStudent(rawIntegrity);
    const observationsMap = groupByStudent(rawObservations);
    const parentReviewsMap = groupByStudent(rawReviews);

    const resultsMap: Record<string, QuotientResult> = {};

    studentCodes.forEach(code => {
      const bIds = studentBatchesMap.get(code) || [];
      const studentClass = studentClassMap.get(code) || '';
      const sAttempts = attemptsMap[code] || [];
      const sAssignments = assignmentsMap[code] || [];
      const sPractice = practiceMap[code] || [];
      const sIntegrity = integrityMap[code] || [];
      const sObservations = observationsMap[code] || [];
      const sReviews = parentReviewsMap[code] || [];

      resultsMap[code] = this.computeStudentQuotientScore(
        code,
        duration,
        activeParameters,
        bIds,
        sAttempts,
        sAssignments,
        sPractice,
        sIntegrity,
        sObservations,
        sReviews,
        examsMap,
        subjectiveExamsList,
        studentClass
      );
    });

    return resultsMap;
  }

  /**
   * Saves or creates a quotient evaluation parameter.
   */
  static async saveParameter(name: string, parameterId?: string): Promise<{ id: string; name: string }> {
    const id = parameterId || name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    await adminDb.collection('quotientParameters').doc(id).set({
      id,
      name,
      createdAt: new Date()
    });
    return { id, name };
  }

  /**
   * Deletes a quotient evaluation parameter.
   */
  static async deleteParameter(parameterId: string): Promise<void> {
    await adminDb.collection('quotientParameters').doc(parameterId).delete();
  }

  /**
   * Logs a batch award observation across multiple students atomically.
   */
  static async batchAward(studentCodes: string[], parameterId: string, score: number, actorEmail: string): Promise<void> {
    const codeChunks = chunkArray(studentCodes, 30);
    const chunkPromises = codeChunks.map(async (chunk) => {
      const snapshot = await adminDb.collection('studentObservations')
        .where('parameterId', '==', parameterId)
        .where('studentCode', 'in', chunk)
        .get();
      
      const batch = adminDb.batch();
      snapshot.docs.forEach(doc => {
        batch.delete(doc.ref);
      });
      chunk.forEach(code => {
        const ref = adminDb.collection('studentObservations').doc();
        batch.set(ref, {
          studentCode: code,
          type: 'custom',
          parameterId,
          score: Number(score),
          observedBy: actorEmail,
          observedAt: new Date()
        });
      });
      await batch.commit();
    });
    await Promise.all(chunkPromises);
  }

  /**
   * Logs single observation scores across multiple parameters for a student atomically.
   */
  static async logSingleObservation(studentCode: string, scores: Record<string, number>, actorEmail: string): Promise<void> {
    const batch = adminDb.batch();

    const existingQuery = await adminDb.collection('studentObservations')
      .where('studentCode', '==', studentCode)
      .get();
    
    existingQuery.docs.forEach(doc => {
      const data = doc.data();
      // Delete legacy standard docs or docs matching any of the submitted parameter IDs
      if (!data.parameterId || Object.prototype.hasOwnProperty.call(scores, data.parameterId)) {
        batch.delete(doc.ref);
      }
    });

    Object.entries(scores).forEach(([paramId, scoreVal]) => {
      const ref = adminDb.collection('studentObservations').doc();
      batch.set(ref, {
        studentCode,
        type: 'custom',
        parameterId: paramId,
        score: Number(scoreVal),
        observedBy: actorEmail,
        observedAt: new Date()
      });
    });

    await batch.commit();
  }

  /**
   * Logs a standard classroom observation assessment for a student in Firestore atomically.
   * Scoped strictly to standard observations without modifying or deleting custom parameter observations.
   */
  static async saveObservation(obs: Omit<StudentObservation, 'observedAt'>): Promise<void> {
    const existingQuery = await adminDb.collection('studentObservations')
      .where('studentCode', '==', obs.studentCode)
      .get();
    
    const batch = adminDb.batch();

    existingQuery.docs.forEach(doc => {
      const data = doc.data();
      const isStandardObs = data.type === 'standard' || (!data.parameterId && data.activeParticipation !== undefined);
      if (isStandardObs) {
        batch.delete(doc.ref);
      }
    });

    const docRef = adminDb.collection('studentObservations').doc();
    batch.set(docRef, {
      studentCode: obs.studentCode,
      type: 'standard',
      activeParticipation: Number(obs.activeParticipation ?? 0),
      sincerity: Number(obs.sincerity ?? 0),
      timelyWork: Number(obs.timelyWork ?? 0),
      parentScore: Number(obs.parentScore ?? 0),
      observedBy: obs.observedBy,
      observedAt: new Date()
    });

    await batch.commit();
  }
}
