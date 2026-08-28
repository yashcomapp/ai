export interface TopicMasteryRecord {
  studentCode: string;
  topicCode: string;
  mastery: number;
  confidence: number;
  questionsAttempted: number;
  questionsCorrect: number;
  questionsWrong: number;
  weightedPointsEarned: number;
  weightedPointsPossible: number;
  lastExamCode: string;
  questionHistory: { questionId: string; seenAt: any; wasCorrect: boolean }[];
  createdAt: any;
  updatedAt?: any;
}

export interface TopicRecommendation {
  topicCode: string;
  topicName: string;
  mastery: number;
  confidence: number;
  category: 'needsAttention' | 'continuePractice' | 'revision';
}

export interface PracticeSession {
  topicCode: string;
  questions: any[];
  masteryAtStart: number;
  idealTimeSeconds: number;
  category: string;
}
