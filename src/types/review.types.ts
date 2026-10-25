export interface SubjectiveReview {
  id?: string;
  attemptId: string;
  examId: string;
  reviewerId: string;
  reviewerType: 'peer' | 'parent' | 'teacher';
  revieweeCode: string;
  questionReviews: any;
  totalScore: number;
  isFinal: boolean;
  submittedAt: any;
  createdAt: any;
}

export interface PeerAssignment {
  id: string;
  examId: string;
  reviewerStudentCode: string;
  revieweeCode: string;
  status: 'pending' | 'completed';
  completedAt?: any;
  marksAwarded?: number;
}

export interface ReviewItem {
  id: string;
  examId?: string;
  practiceId?: string;
  name: string;
  examName?: string;
  subject?: string;
  type: 'objective' | 'practice' | 'subjective' | 'entrance' | 'absent_exam' | string;
  date: string;
  scorePercent?: number;
  percentage?: number;
  status: 'pending' | 'approved' | string;
  wrongCount?: number;
  unansweredCount?: number;
  correctCount?: number;
  durationSpent?: number;
  topicsCovered?: string[];
  submittedAt?: string;
  reviewedByActor?: string;
  [key: string]: any;
}
