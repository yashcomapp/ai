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
