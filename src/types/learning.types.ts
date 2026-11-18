/**
 * Single Source of Truth (SSOT) Types for Learning Operating System (LOS)
 */

export interface LearningTopicItem {
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
  priorityScore: number;
  lastAttempt: string | null;
  attempts: number;
  lastScore: number;
  state: string;
  practiceCount: number;
  targetQuestions?: number;
  totalQuestions?: number;
  topicClassification?: string;
  requiredConfidence?: number;
  isAbsentExam?: boolean;
  isExamStrong?: boolean;
  isSrsDue?: boolean;
  srsSchedule?: {
    srsStage: number;
    intervalDays: number;
    lastRevisedAt: string | null;
    nextReviewDate: string;
    isDueForRevision: boolean;
    daysUntilDue: number;
    daysOverdue: number;
    estimatedRetention: number;
    stageLabel: string;
  };
  practiceQuestionsAttempted?: number;
  questionsAttempted?: number;
}

export interface LearningPathData {
  studentCode: string;
  needsAttention: LearningTopicItem[];
  continuePractice: LearningTopicItem[];
  revision: LearningTopicItem[];
  mastered: LearningTopicItem[];
  counts?: {
    masteredCount: number;
    practicingCount: number;
    needsAttentionCount: number;
    totalAssignedCount: number;
    uniqueTopicsPracticed?: number;
  };
  stats?: {
    masteredCount: number;
    practicingCount: number;
    needsAttentionCount: number;
    totalAssignedCount: number;
    uniqueTopicsPracticed?: number;
  };
}

export type StudentLearningTopicItem = LearningTopicItem;
