import { ProctoringViolations } from '@/types/exam.types';
import { calculateProctoringIntegrityScore } from '@/lib/proctoring';

export class IntegrityService {
  /**
   * Calculates the ISO week number for a given date
   */
  static getWeekDetails(date: Date): { year: number; week: number } {
    const year = date.getFullYear();
    const start = new Date(date.getFullYear(), 0, 1);
    const diff = date.getTime() - start.getTime() + (start.getTimezoneOffset() - date.getTimezoneOffset()) * 60 * 1000;
    const oneDay = 1000 * 60 * 60 * 24;
    const day = Math.floor(diff / oneDay);
    const week = Math.ceil((day + start.getDay() + 1) / 7);

    return { year, week };
  }

  /**
   * Calculates weekly integrity scores based on proctoring infractions
   * Unified SSOT: Tab switch (-10), Multiple faces (-15), No face (-10), Looking away (-5), Head movement (-5)
   */
  static calculateScore(tabViolations: number, violations: ProctoringViolations): { integrityScore: number; deductions: number } {
    const score = calculateProctoringIntegrityScore({
      tabViolations,
      proctoringViolations: violations
    });
    const deductions = 100 - score;
    return { integrityScore: score, deductions };
  }
}

