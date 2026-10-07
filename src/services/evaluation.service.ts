import { evaluateQuestionAnswer } from '@/lib/questionTypes';
import { QuestionType, OptionItem } from '@/types/question.types';

export class EvaluationService {
  /**
   * Evaluates if a student's answer is correct for a given question type
   */
  static evaluate(type: QuestionType, userAnswer: any, correctAnswer: any, options?: OptionItem[]): boolean {
    return evaluateQuestionAnswer(type, userAnswer, correctAnswer, options);
  }
}
