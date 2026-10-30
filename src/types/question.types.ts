export type CanonicalQuestionType =
  | 'OSC'
  | 'OMC'
  | 'OTF'
  | 'OAR'
  | 'OFB'
  | 'ONE'
  | 'SDF'
  | 'SLP'
  | 'SSA'
  | 'SSR'
  | 'SSN'
  | 'SLA'
  | 'SLN';

export type LegacyQuestionType =
  | 'single_mcq' 
  | 'multiple_mcq' 
  | 'true_false' 
  | 'assertion_reason' 
  | 'fill_blanks' 
  | 'numerical'
  | 'numerical_short'
  | 'numerical_long'
  | 'subjective_short' 
  | 'subjective_long'
  | 'subjective_reason'
  | 'subjective_notes'
  | 'subjective_define'
  | 'subjective_laws';

export type QuestionType = CanonicalQuestionType | LegacyQuestionType | string;

export interface OptionObject {
  text?: string;
  value?: string;
  isCorrect?: boolean;
  correct?: boolean;
}

export type OptionItem = string | OptionObject;

export interface Question {
  id?: string;
  questionCode?: string;
  code?: string;
  qNumber?: number;
  text: string;
  type?: QuestionType | string;
  questionType?: string;
  options?: any[];
  assertion?: string;
  reason?: string;
  difficulty?: 'easy' | 'medium' | 'hard' | string;
  bloomLevel?: 'Remember' | 'Understand' | 'Apply' | 'Analyze' | 'Evaluate' | 'Create' | string;
  solution?: string;
  explanation?: string;
  correctAnswer?: any;
  correctAnswers?: any[];
  marks?: number;
  subject?: string;
  subjectName?: string;
  chapter?: string;
  chapterNumber?: string | number;
  chapterName?: string;
  topic?: string;
  topicCode?: string;
  topicName?: string;
  class?: string | number;
  board?: string;
  keywords?: string[];
  answerLines?: Array<{ lineNo: number; text: string }>;
  steps?: Array<{ description: string; marks: number }>;
  metadata?: any;
  relaxProctoring?: boolean;
  isNumerical?: boolean;
  vault?: 'exam' | 'practice' | 'mock' | 'foundation' | string;
  examCategory?: 'standard' | 'foundation' | string;
  [key: string]: any;
}

export type QuestionItem = Question;
