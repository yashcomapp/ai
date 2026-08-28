import { QuestionHistoryItem } from '@/types/user.types';
import { getDateKeyIST } from '@/lib/dateUtils';

export class MasteryService {
  /**
   * Helper to calculate bloom taxonomy weights
   */
  static getBloomWeight(bloomLevel: string): number {
    const bloomWeights: { [key: string]: number } = {
      Remember: 1,
      Understand: 2,
      Apply: 3,
      Analyze: 4,
      Evaluate: 5,
      Create: 6
    };
    return bloomWeights[bloomLevel] || 2;
  }

  /**
   * Aggregates points and computes updated mastery values for a topic
   */
  static calculateTopicMasteryUpdate(
    existing: any,
    evaluations: { id: string; difficulty: string; bloomLevel: string; isCorrect: boolean }[],
    examId: string
  ): any {
    const data = { ...existing };
    let questionsAttemptedDelta = 0;
    let questionsCorrectDelta = 0;
    let questionsWrongDelta = 0;
    let weightedPointsPossibleDelta = 0;
    let weightedPointsEarnedDelta = 0;

    evaluations.forEach(ev => {
      if ((ev as any).isDisputed) return;

      const diffWeight = ev.difficulty === 'easy' ? 1 : (ev.difficulty === 'hard' ? 3 : 2);
      const bloomWeight = this.getBloomWeight(ev.bloomLevel);
      const weight = diffWeight * bloomWeight;
      const isFoundation = (ev as any).examCategory === 'foundation';

      questionsAttemptedDelta += 1;

      if (ev.isCorrect) {
        questionsCorrectDelta += 1;
        weightedPointsEarnedDelta += weight;
        weightedPointsPossibleDelta += weight;
      } else {
        questionsWrongDelta += 1;
        weightedPointsPossibleDelta += isFoundation ? (weight * 0.3) : weight;
      }
    });

    const isPractice = (examId || '').toUpperCase().includes('PRACTICE') || (examId || '').startsWith('ST-');
    if (isPractice) {
      data.practiceQuestionsAttempted = (data.practiceQuestionsAttempted || 0) + questionsAttemptedDelta;
      const todayIST = getDateKeyIST(new Date());
      if (data.lastPracticeDate === todayIST) {
        data.dailyPracticeSessionsCount = (data.dailyPracticeSessionsCount || 0) + 1;
      } else {
        data.lastPracticeDate = todayIST;
        data.dailyPracticeSessionsCount = 1;
      }
    } else {
      data.examQuestionsAttempted = (data.examQuestionsAttempted || 0) + questionsAttemptedDelta;
    }

    data.questionsAttempted = (data.questionsAttempted || 0) + questionsAttemptedDelta;
    data.questionsCorrect = (data.questionsCorrect || 0) + questionsCorrectDelta;
    data.questionsWrong = (data.questionsWrong || 0) + questionsWrongDelta;
    data.weightedPointsEarned = (data.weightedPointsEarned || 0) + weightedPointsEarnedDelta;
    data.weightedPointsPossible = (data.weightedPointsPossible || 0) + weightedPointsPossibleDelta;

    data.mastery = data.weightedPointsPossible > 0
      ? Math.round((data.weightedPointsEarned / data.weightedPointsPossible) * 100)
      : 0;
    data.confidence = Math.min(data.questionsAttempted, 100);

    // Update question seen history (excluding disputed questions)
    let questionHistory: QuestionHistoryItem[] = data.questionHistory || [];
    const seenAt = new Date();
    evaluations.forEach(ev => {
      if ((ev as any).isDisputed) return;
      questionHistory = questionHistory.filter(h => h.questionId !== ev.id);
      questionHistory.push({ questionId: ev.id, seenAt, wasCorrect: ev.isCorrect });
    });

    if (questionHistory.length > 100) {
      questionHistory = questionHistory.slice(-100);
    }
    data.questionHistory = questionHistory;

    data.lastExamCode = examId;
    data.updatedAt = new Date();

    return data;
  }
}
