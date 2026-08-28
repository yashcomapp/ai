import { ExamAttempt, Assignment } from './exam.types';
import { TopicMasteryRecord } from './practice.types';
import { WeeklyIntegrity } from './user.types';

export interface StudentObservation {
  studentCode: string;
  activeParticipation: number; // 0 - 100
  sincerity: number;           // 0 - 100
  timelyWork: number;          // 0 - 100
  observedBy: string;
  observedAt: any;
}

export interface StudentData {
  studentCode: string;
  attempts: ExamAttempt[];
  assignments: Assignment[];
  practiceRecords: TopicMasteryRecord[];
  integrityRecords: WeeklyIntegrity[];
  observations: StudentObservation[];
  [key: string]: any;
}

export interface ScoreResult {
  score: number;
  details: Record<string, any>;
}

export interface ParameterCalculator {
  id: string;
  name: string;
  weight: number;
  calculate(data: StudentData): ScoreResult;
}

export interface QuotientComponentResult {
  parameterId: string;
  parameterName: string;
  score: number;
  weight: number;
  contribution: number;
  details: Record<string, any>;
}

export interface QuotientResult {
  studentCode: string;
  overallQuotient: number;
  components: QuotientComponentResult[];
  calculatedAt: Date;
}
