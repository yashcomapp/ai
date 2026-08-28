import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { getDateKeyIST } from '@/lib/dateUtils';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';
import { 
  StudentData, 
  QuotientResult, 
  ParameterCalculator, 
  ScoreResult, 
  StudentObservation 
} from '@/types/quotient.types';

export const MASTERY_THRESHOLDS = {
  MASTERED_MASTERY: 90,
  MASTERED_CONFIDENCE: 20,
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
    if (assignments.length === 0) {
      if (attempts.length > 0) {
        const totalScoreSum = attempts.reduce((sum, att) => sum + (att.percentage ?? 0), 0);
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
      return { score: 0, details: { totalAssigned: 0, completed: 0, absent: 0, reason: 'No exams assigned yet' } };
    }

    let completedCount = 0;
    let totalScoreSum = 0;

    assignments.forEach(assignment => {
      // Find a matching completed exam attempt
      const attempt = attempts.find(att => att.examId === assignment.examId);
      if (assignment.status === 'completed' || attempt) {
        completedCount++;
        totalScoreSum += attempt?.percentage ?? 100;
      }
    });

    const totalAssigned = assignments.length;
    const absentCount = totalAssigned - completedCount;
    // Score is sum of completed exam percentages divided by total assigned exams (absent counts as 0)
    const score = Math.round(totalScoreSum / totalAssigned);

    return {
      score,
      details: {
        totalAssigned,
        completed: completedCount,
        absent: absentCount,
        attendanceRate: Math.round((completedCount / totalAssigned) * 100)
      }
    };
  }
}

// Strategy 2: Practice Engagement & Quality (Mastery Efficiency)
export class PracticeEngagementCalculator implements ParameterCalculator {
  id = 'practice';
  name = 'Practice';
  weight = 0.20;

  calculate(data: StudentData): ScoreResult {
    const { practiceRecords } = data;
    const parentReviews = data.parentReviews || [];
    
    if (parentReviews.length === 0) {
      const avgMast = practiceRecords.length > 0 
        ? Math.round(practiceRecords.reduce((sum: number, rec: any) => sum + (rec.mastery || 0), 0) / practiceRecords.length)
        : 0;
      return { 
        score: 0, 
        details: { 
          totalQuestionsAttempted: 0, 
          averageMastery: avgMast, 
          topicsAttemptedCount: 0, 
          averageQuestionsPerTopic: 0 
        } 
      };
    }

    const totalQuestionsAttempted = parentReviews.reduce((sum: number, rev: any) => sum + (rev.totalQuestions || 0), 0);

    const topicPracticeMap = new Map<string, number>();
    parentReviews.forEach((rev: any) => {
      const tCode = rev.topicCode;
      if (tCode) {
        topicPracticeMap.set(tCode, (topicPracticeMap.get(tCode) || 0) + (rev.totalQuestions || 0));
      }
    });

    const averageMastery = practiceRecords.length > 0 
      ? Math.round(practiceRecords.reduce((sum: number, rec: any) => sum + (rec.mastery || 0), 0) / practiceRecords.length)
      : 0;
    
    const averageQuestionsPerTopic = topicPracticeMap.size > 0
      ? Math.round((totalQuestionsAttempted / topicPracticeMap.size) * 10) / 10
      : 0;

    return {
      score: averageMastery,
      details: {
        totalQuestionsAttempted,
        averageMastery,
        topicsAttemptedCount: topicPracticeMap.size,
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
          averageQuestionsPerTopic: 0 
        } 
      };
    }

    const totalQuestionsAttempted = parentReviews.reduce((sum: number, rev: any) => sum + (rev.totalQuestions || 0), 0);

    const topicPracticeMap = new Map<string, number>();
    parentReviews.forEach((rev: any) => {
      const tCode = rev.topicCode;
      if (tCode) {
        topicPracticeMap.set(tCode, (topicPracticeMap.get(tCode) || 0) + (rev.totalQuestions || 0));
      }
    });

    const masteryMap = new Map<string, number>();
    const confidenceMap = new Map<string, number>();
    practiceRecords.forEach(rec => {
      if (rec.topicCode) {
        masteryMap.set(rec.topicCode, rec.mastery || 0);
        confidenceMap.set(rec.topicCode, rec.confidence || 0);
      }
    });

    let totalQualityScore = 0;
    topicPracticeMap.forEach((q, topicCode) => {
      const mastery = masteryMap.get(topicCode) || 0;
      const confidence = confidenceMap.get(topicCode) || 0;
      
      let topicQuality = 0;
      if (mastery >= MASTERY_THRESHOLDS.MASTERED_MASTERY && confidence >= MASTERY_THRESHOLDS.MASTERED_CONFIDENCE) {
        const excess = Math.max(0, q - 20);
        topicQuality = Math.max(30, 100 - excess * 1.5);
      } else {
        const excess = Math.max(0, q - 20);
        topicQuality = Math.max(0, mastery - excess * 1.5);
      }
      totalQualityScore += topicQuality;
    });

    const qualityScore = topicPracticeMap.size > 0 
      ? Math.round(totalQualityScore / topicPracticeMap.size)
      : 0;

    const averageQuestionsPerTopic = topicPracticeMap.size > 0
      ? Math.round((totalQuestionsAttempted / topicPracticeMap.size) * 10) / 10
      : 0;

    return {
      score: qualityScore,
      details: {
        totalQuestionsAttempted,
        topicsAttemptedCount: topicPracticeMap.size,
        averageQuestionsPerTopic
      }
    };
  }
}

// Strategy 3: Topic Health (Mastery Ratios)
export class TopicHealthCalculator implements ParameterCalculator {
  id = 'topicHealth';
  name = 'Topic Health';
  weight = 0.20;

  calculate(data: StudentData): ScoreResult {
    const { practiceRecords, assignedTopics } = data;
    
    // If no assigned topics are resolved, fallback to the old behavior using practiceRecords
    if (!assignedTopics || assignedTopics.length === 0) {
      if (practiceRecords.length === 0) {
        return { score: 0, details: { totalTopics: 0, masteredCount: 0, attentionCount: 0 } };
      }
      const totalTopics = Math.max(15, practiceRecords.length);
      let weightedMasteredCount = 0;
      let attentionCount = 0;
      practiceRecords.forEach(rec => {
        const mastery = rec.mastery || 0;
        const confidence = rec.confidence || 0;
        if (mastery >= MASTERY_THRESHOLDS.MASTERED_MASTERY && confidence >= MASTERY_THRESHOLDS.MASTERED_CONFIDENCE) {
          weightedMasteredCount += 1.0;
        } else if (mastery >= MASTERY_THRESHOLDS.MEDIUM_HIGH_MASTERY) {
          weightedMasteredCount += 0.8;
        } else if (mastery >= MASTERY_THRESHOLDS.MEDIUM_MASTERY) {
          weightedMasteredCount += 0.5;
        } else {
          attentionCount++;
        }
      });

      // Compensate attentionCount for unattempted baseline topics (if practiceRecords.length < 15)
      if (practiceRecords.length < 15) {
        attentionCount += (15 - practiceRecords.length);
      }

      const masteryRatio = weightedMasteredCount / totalTopics;
      const attentionRatio = attentionCount / totalTopics;
      const score = Math.max(0, Math.round((masteryRatio - 0.25 * attentionRatio) * 100));
      return {
        score,
        details: {
          totalTopics,
          weightedMasteredCount: Math.round(weightedMasteredCount * 10) / 10,
          attentionCount,
          masteryRatio: Math.round(masteryRatio * 100),
          attentionRatio: Math.round(attentionRatio * 100),
          fallbackUsed: true
        }
      };
    }

    const totalTopics = assignedTopics.length;
    let weightedMasteredCount = 0;
    let attentionCount = 0;

    // Create a lookup map of attempted practice records by topicCode using all-time practice records (fallback to filtered if not provided)
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
        const mastery = record.mastery || 0;
        const confidence = record.confidence || 0;
        if (mastery >= MASTERY_THRESHOLDS.MASTERED_MASTERY && confidence >= MASTERY_THRESHOLDS.MASTERED_CONFIDENCE) {
          weightedMasteredCount += 1.0;
        } else if (mastery >= MASTERY_THRESHOLDS.MEDIUM_HIGH_MASTERY) {
          weightedMasteredCount += 0.8;
        } else if (mastery >= MASTERY_THRESHOLDS.MEDIUM_MASTERY) {
          weightedMasteredCount += 0.5;
        } else {
          attentionCount++;
        }
      } else {
        // Not even started or opened: counts as 0% mastery, so it needs attention!
        attentionCount++;
      }
    });

    const masteryRatio = weightedMasteredCount / totalTopics;
    const attentionRatio = attentionCount / totalTopics;

    // Deduct penalty of 0.25 * attentionRatio (discourages leaving topics below 50% / unattempted)
    const score = Math.max(0, Math.round((masteryRatio - 0.25 * attentionRatio) * 100));

    return {
      score,
      details: {
        totalTopics,
        weightedMasteredCount: Math.round(weightedMasteredCount * 10) / 10,
        attentionCount,
        masteryRatio: Math.round(masteryRatio * 100),
        attentionRatio: Math.round(attentionRatio * 100),
        fallbackUsed: false
      }
    };
  }
}

// Strategy 4: Proctoring Integrity Average
export class IntegrityScoreCalculator implements ParameterCalculator {
  id = 'integrity';
  name = 'Proctoring Integrity';
  weight = 0.10;

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
  weight = 0.15;

  calculate(data: StudentData): ScoreResult {
    const { observations, activeParameters } = data;
    const parameters = activeParameters || [
      { id: 'activeParticipation', name: 'Active Participation' },
      { id: 'sincerity', name: 'Sincerity & Behavior' },
      { id: 'timelyWork', name: 'Timely Work' }
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
      }
    });

    const parameterDetails: any[] = [];
    let totalScoreSum = 0;

    parameters.forEach((p: any) => {
      const scores = scoresMap[p.id] || [];
      let avg = 50; // Neutral baseline fallback
      if (scores.length > 0) {
        avg = Math.round(scores.reduce((sum, val) => sum + val, 0) / scores.length);
      }
      totalScoreSum += avg;
      parameterDetails.push({
        id: p.id,
        name: p.name,
        average: avg,
        logsCount: scores.length
      });
    });

    const score = Math.round(totalScoreSum / parameters.length);

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

function getObjectiveExamTopics(exam: any): string[] {
  const topics = new Set<string>();
  if (!exam) return [];
  const idParts = (exam.id || '').split('-');
  const board = exam.boardCode || idParts[0] || '';
  const classCode = exam.class || idParts[1] || '';
  const subjectCode = exam.subjectCode || idParts[2] || '';
  const chapterNumber = exam.chapterNumber || (idParts[4] ? idParts[4].split('_')[0] : '');

  const tCodes = exam.topicCodes || (exam.topicCode ? [exam.topicCode] : []);
  tCodes.forEach((t: string) => {
    if (!t) return;
    if (t.includes('-')) {
      topics.add(t);
    } else if (board && classCode && subjectCode && chapterNumber) {
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

function getSubjectiveExamTopics(exam: any): string[] {
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
    if (parameters.length === 0) {
      const defaults = [
        { id: 'activeParticipation', name: 'Active Participation', createdAt: new Date() },
        { id: 'sincerity', name: 'Sincerity & Behavior', createdAt: new Date() },
        { id: 'timelyWork', name: 'Timely Work', createdAt: new Date() }
      ];
      const batch = adminDb.batch();
      defaults.forEach(p => {
        const ref = adminDb.collection('quotientParameters').doc(p.id);
        batch.set(ref, p);
      });
      await batch.commit();
      return defaults;
    }
    return parameters;
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
    subjectiveExamsList: any[]
  ): QuotientResult {
    const todayDateStr = getDateKeyIST();
    const startDate = duration ? this.getStartDateForDuration(duration) : null;

    const filteredAttempts = this.filterByDate(rawAttempts, ['timestamp', 'createdAt', 'completedAt'], startDate);
    const filteredAssignments = this.filterByDate(rawAssignments, ['createdAt', 'dueDate'], startDate);
    const filteredSubjectiveExams = this.filterByDate(subjectiveExamsList, ['scheduledDate', 'createdAt'], startDate);

    const topicsSet = new Set<string>();

    // 1. Sourcing from objective exam attempts
    filteredAttempts.forEach((attData: any) => {
      const exam = examsMap.get(attData.examId);
      if (exam) {
        getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
      }
    });

    // 2. Sourcing from assignments
    filteredAssignments.forEach((assData: any) => {
      const exam = examsMap.get(assData.examId);
      if (exam) {
        getObjectiveExamTopics(exam).forEach(t => topicsSet.add(t));
      }
    });

    // 3. Sourcing from subjective exams
    filteredSubjectiveExams.forEach((subExam: any) => {
      const isAssigned = subExam.batchId && bIds.includes(subExam.batchId);
      const scheduledDateStr = subExam.scheduledDate || todayDateStr;
      const isPastOrToday = scheduledDateStr <= todayDateStr;
      
      if (isAssigned && isPastOrToday) {
        getSubjectiveExamTopics(subExam).forEach(t => topicsSet.add(t));
      }
    });

    const assignedTopics = Array.from(topicsSet);
    const filteredIntegrity = this.filterByDate(rawIntegrity, ['timestamp', 'createdAt'], startDate);
    const filteredObservations = this.filterByDate(rawObservations, ['observedAt', 'timestamp'], startDate);
    const filteredReviews = this.filterByDate(rawReviews, ['timestamp', 'createdAt'], startDate);

    const practicedTopics = new Set(filteredReviews.map((r: any) => r.topicCode).filter(Boolean));
    const filteredPractice = startDate 
      ? rawPractice.filter((rec: any) => rec.topicCode && practicedTopics.has(rec.topicCode))
      : rawPractice;

    const studentData: StudentData = {
      studentCode,
      attempts: filteredAttempts,
      assignments: filteredAssignments,
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
        if (calc.id === 'exam' && studentData.attempts.length === 0) {
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

    // 1. Fetch user doc first to resolve batchIds
    const studentUserQuery = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();

    let bIds: string[] = [];
    if (!studentUserQuery.empty) {
      const userData = studentUserQuery.docs[0].data();
      bIds = userData.batchIds || (userData.batchId ? [userData.batchId] : []);
    }

    // 2. Fetch student specific records in parallel
    const queries: Promise<any>[] = [
      adminDb.collection('examAttempts').where('studentCode', '==', studentCode).get(),
      adminDb.collection('assignments').where('studentCode', '==', studentCode).get(),
      adminDb.collection('studentTopicMastery').where('studentCode', '==', studentCode).get(),
      adminDb.collection('integrityScores').where('studentCode', '==', studentCode).get(),
      adminDb.collection('studentObservations').where('studentCode', '==', studentCode).get(),
      adminDb.collection('parentReviews').where('studentCode', '==', studentCode).get()
    ];

    // Only query subjectiveExams if student is assigned batches (using 'in' operator chunked to max 30)
    if (bIds.length > 0) {
      const batchChunks = [];
      for (let i = 0; i < bIds.length; i += 30) {
        batchChunks.push(bIds.slice(i, i + 30));
      }
      const subjectiveExamsPromise = Promise.all(
        batchChunks.map(chunk =>
          adminDb.collection('subjectiveExams').where('batchId', 'in', chunk).get()
        )
      ).then(snaps => {
        const allDocs: admin.firestore.QueryDocumentSnapshot[] = [];
        snaps.forEach(s => allDocs.push(...s.docs));
        return { docs: allDocs } as any;
      });
      queries.push(subjectiveExamsPromise);
    } else {
      queries.push(Promise.resolve({ docs: [] }));
    }

    const [
      attemptsSnap,
      assignmentsSnap,
      practiceSnap,
      integritySnap,
      observationsSnap,
      parentReviewsSnap,
      subjectiveExamsSnap
    ] = await Promise.all(queries);

    // 3. Compile unique exam IDs referenced by attempts and assignments
    const examIds = new Set<string>();
    attemptsSnap.docs.forEach((doc: any) => {
      const examId = doc.data().examId;
      if (examId) examIds.add(examId);
    });
    assignmentsSnap.docs.forEach((doc: any) => {
      const examId = doc.data().examId;
      if (examId) examIds.add(examId);
    });

    // 4. Fetch only the referenced exams in chunks of 30
    let examsSnapDocs: admin.firestore.QueryDocumentSnapshot[] = [];
    if (examIds.size > 0) {
      const idsArray = Array.from(examIds);
      const chunks = [];
      for (let i = 0; i < idsArray.length; i += 30) {
        chunks.push(idsArray.slice(i, i + 30));
      }
      const snaps = await Promise.all(
        chunks.map(chunk =>
          adminDb.collection('exams').where(admin.firestore.FieldPath.documentId(), 'in', chunk).get()
        )
      );
      snaps.forEach(s => examsSnapDocs.push(...s.docs));
    }

    const examsMap = new Map();
    examsSnapDocs.forEach(doc => {
      examsMap.set(doc.id, { id: doc.id, ...doc.data() });
    });

    const rawAttempts = attemptsSnap.docs.map((doc: any) => doc.data() as any).filter((att: any) => att.examType !== 'entrance');
    const rawAssignments = assignmentsSnap.docs.map((doc: any) => doc.data() as any).filter((ass: any) => ass.examType !== 'entrance');
    const rawPractice = practiceSnap.docs.map((doc: any) => doc.data() as any);
    const rawIntegrity = integritySnap.docs.map((doc: any) => doc.data() as any);
    const rawObservations = observationsSnap.docs.map((doc: any) => doc.data() as any);
    const rawReviews = parentReviewsSnap.docs.map((doc: any) => doc.data() as any);
    const subjectiveExamsList = subjectiveExamsSnap.docs.map((doc: any) => doc.data() as any);

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
      subjectiveExamsList
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
    usersSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) {
        const bIds = data.batchIds || (data.batchId ? [data.batchId] : []);
        studentBatchesMap.set(data.studentCode, bIds);
      }
    });

    const rawAttempts = attemptsSnap.docs.map((doc: any) => doc.data()).filter((att: any) => att.examType !== 'entrance');
    const rawAssignments = assignmentsSnap.docs.map((doc: any) => doc.data()).filter((ass: any) => ass.examType !== 'entrance');
    const rawPractice = practiceSnap.docs.map((doc: any) => doc.data());
    const rawIntegrity = integritySnap.docs.map((doc: any) => doc.data());
    const rawObservations = observationsSnap.docs.map((doc: any) => doc.data());
    const rawReviews = parentReviewsSnap.docs.map((doc: any) => doc.data());

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
        subjectiveExamsList
      );
    });

    return resultsMap;
  }

  /**
   * Logs a new classroom observation assessment for a student in Firestore.
   */
  static async saveObservation(obs: Omit<StudentObservation, 'observedAt'>): Promise<void> {
    const docRef = adminDb.collection('studentObservations').doc();
    await docRef.set({
      ...obs,
      observedAt: admin.firestore.FieldValue.serverTimestamp()
    });
  }
}
