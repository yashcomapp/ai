import { evaluateQuestionAnswer, normalizeOptionAnswer, stripOptionLabel, classifyAssertionReasonAnswer } from '@/lib/questionTypes';
import { QuestionType, OptionItem } from '@/types/question.types';

export class EvaluationService {
  /**
   * Evaluates if a student's answer is correct for a given question type
   */
  static evaluate(type: QuestionType, userAnswer: any, correctAnswer: any, options?: OptionItem[]): boolean {
    return evaluateQuestionAnswer(type, userAnswer, correctAnswer, options);
  }

  /**
   * Normalizes option inputs (e.g. mapping strings or indexes to option letters like A, B, C, D)
   */
  static normalizeOption(value: any, options?: OptionItem[]): string {
    return normalizeOptionAnswer(value, options);
  }

  /**
   * Strips prefix labels (e.g. "(A)", "B)") from options text
   */
  static stripLabel(text: any): string {
    return stripOptionLabel(text);
  }

  /**
   * Classifies assertion-reason responses
   */
  static classifyAssertionReason(value: any): string {
    return classifyAssertionReasonAnswer(value);
  }
}
