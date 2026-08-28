export type UserRole = 'admin' | 'student' | 'parent';

export interface User {
  id: string;
  name: string;
  email: string;
  rollNumber?: string;
  studentCode?: string;
  mobile?: string;
  class?: string;
  role: UserRole;
  batchIds?: string[];
  status: 'active' | 'inactive';
  parentEmail?: string;
  studentId?: string;
  studentCodes?: string[];
  studentName?: string;
  createdAt: any;
}

export interface StudentProfile {
  masteredTopics: number;
  needsAttentionTopics: number;
  overallMastery: number;
  lastExamUpdatedAt?: any;
}

export interface QuestionHistoryItem {
  questionId: string;
  seenAt: any;
  wasCorrect: boolean;
}

export interface StudentTopicMastery {
  id?: string;
  studentCode: string;
  topicCode: string;
  mastery: number;
  confidence: number;
  questionsAttempted: number;
  questionsCorrect: number;
  questionsWrong: number;
  weightedPointsEarned: number;
  weightedPointsPossible: number;
  lastExamCode?: string;
  questionHistory: QuestionHistoryItem[];
  createdAt: any;
  updatedAt: any;
}

export interface WeeklyIntegrity {
  studentCode: string;
  year: number;
  week: number;
  integrityScore: number;
  violationsCount: number;
  weekStart: any;
}

export interface Registration {
  id?: string;
  studentName: string;
  studentEmail: string;
  studentMobile: string;
  dob: string;
  gender: string;
  bloodGroup: string;
  address: string;
  parentName: string;
  parentRelation: string;
  parentMobile: string;
  parentEmail: string;
  parentOccupation?: string;
  batchId: string;
  batchName: string;
  tempId: string;
  status: 'pending' | 'approved' | 'rejected';
  password?: string;
  createdAt: any;
  approvedAt?: any;
  approvedBy?: string;
  rejectedAt?: any;
  rejectedBy?: string;
  studentId?: string;
  parentId?: string;
}
