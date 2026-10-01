export interface Child {
  studentCode: string;
  name: string;
  uid: string;
  className?: string;
  batchName?: string;
}

export interface ActivityItem {
  type: 'exam' | 'practice';
  id: string;
  name: string;
  score: number;
  date: string;
  subject: string;
  status: string;
}

export interface ParentDashboardData {
  childInfo?: {
    uid: string;
    studentCode: string;
    name: string;
  };
  todayStats?: {
    todayMinutes: number;
    todayPracticeMinutes: number;
    todayExamMinutes: number;
    todaySessionsCount: number;
    todayQuestionsCount: number;
    todayAverageScore: number;
    streakDays: number;
  };
  topicDiagnostics?: {
    needsAttentionYesterdayCount: number;
    needsAttentionYesterdayTopics: string[];
    practicedTodayCount: number;
    practicedTodayTopics: string[];
    recoveredTodayCount: number;
    recoveredTodayTopics: string[];
    needsAttentionRemainingCount: number;
    needsAttentionRemainingTopics: string[];
  };
  srsStats?: {
    retentionScore: number;
    srsDueTopicsCount: number;
    srsOverdueTopicsCount?: number;
    srsDueTopics: Array<{
      topicCode: string;
      topicName: string;
      subjectName: string;
      stageLabel: string;
      estimatedRetention: number;
      daysOverdue: number;
    }>;
  };
  snapshot?: {
    todaySeconds: number;
    weekSeconds: number;
    streakDays: number;
    avgScore: number;
    overallExamAverage?: number;
    objectiveAvgScore?: number;
    subjectiveAvgScore?: number;
    practiceAvgScore?: number;
    overallMastery?: number;
    lqScore?: number;
    averageRetention?: number;
    srsDueTopicsCount?: number;
    effortsPercent?: number;
    practicesCompletedCount?: number;
    totalTopicsCount?: number;
    totalQuestionsPracticed?: number;
    totalSessions: number;
    integrityScore: number;
    needsAttentionCount: number;
    masteredTopicsCount?: number;
    absentExamsCount?: number;
  };
  recentActivity?: ActivityItem[];
  children: Child[];
  chartData?: any[];
  entranceResults?: any[];
  stats?: {
    attendanceRate?: number;
  };
  profile?: {
    attendanceRate?: number;
  };
}

export interface ReviewItem {
  id: string;
  examId?: string;
  practiceId?: string;
  name: string;
  examName?: string;
  subject?: string;
  type: 'objective' | 'practice' | 'subjective' | 'entrance' | 'absent_exam';
  date: string;
  scorePercent?: number;
  percentage?: number;
  status: 'pending' | 'approved';
  wrongCount?: number;
  unansweredCount?: number;
  correctCount?: number;
  durationSpent?: number;
  topicsCovered?: string[];
  submittedAt?: string;
  reviewedByActor?: string;
}

export interface ParentNotice {
  id: string;
  title: string;
  body: string;
  createdAt: string | null;
  isOverlay?: boolean;
  type?: string;
  noticeDate?: string | null;
  seen?: boolean;
}
