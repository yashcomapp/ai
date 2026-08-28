export type QuestionType = 
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

export interface OptionObject {
  text?: string;
  value?: string;
  isCorrect?: boolean;
  correct?: boolean;
}

export type OptionItem = string | OptionObject;

export interface QuestionItem {
  id: string;
  questionCode: string;
  qNumber?: number;
  text: string;
  type: QuestionType;
  options: OptionItem[];
  assertion?: string;
  reason?: string;
  difficulty: 'easy' | 'medium' | 'hard';
  bloomLevel: 'Remember' | 'Understand' | 'Apply' | 'Analyze' | 'Evaluate' | 'Create';
  solution?: string;
  correctAnswer?: any;
  correctAnswers?: any[];
  marks?: number;
  subject?: string;
  chapter?: string;
  topic?: string;
  topicCode?: string;
  keywords?: string[];
}
