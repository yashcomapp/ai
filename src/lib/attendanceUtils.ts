/**
 * ==============================================================================
 * ATTENDANCE UTILITIES — SINGLE SOURCE OF TRUTH (SSOT)
 * ==============================================================================
 * 
 * Centralized business logic for attendance status calculation, percentages,
 * leave resolution, and streak analysis across Student, Parent, and Admin portals.
 * ==============================================================================
 */

export interface AttendanceRecord {
  status?: 'present' | 'absent' | 'leave' | 'late' | 'half_day' | string;
  remarks?: string;
  selfMarked?: boolean;
  selfMarkedBy?: string | null;
  selfMarkedAt?: any;
  [key: string]: any;
}

export interface AttendanceSummary {
  totalDays: number;
  presentDays: number;
  absentDays: number;
  leaveDays: number;
  lateDays: number;
  halfDays: number;
  effectivePresentDays: number;
  attendancePercentage: number;
  attendanceRate: number;
}

/**
 * Calculates standardized attendance summary metrics from an array of attendance records.
 * Rules:
 * - 'present' = 1.0 day
 * - 'late' = 1.0 day (present with late flag)
 * - 'half_day' = 0.5 day
 * - 'leave' = 0.0 day (counted as 0, not subtracted from totalDays)
 * - 'absent' = 0.0 day
 * Percentage: (effectivePresentDays / totalDays) * 100
 */
export function calculateAttendanceSummary(records: AttendanceRecord[]): AttendanceSummary {
  let totalDays = 0;
  let fullPresentDays = 0;
  let absentDays = 0;
  let leaveDays = 0;
  let lateDays = 0;
  let halfDays = 0;

  records.forEach(rec => {
    if (!rec || !rec.status || rec.status === 'not_marked') return;

    totalDays++;
    const status = rec.status.toLowerCase();

    if (status === 'present') {
      fullPresentDays++;
    } else if (status === 'absent') {
      absentDays++;
    } else if (status === 'late') {
      fullPresentDays++;
      lateDays++;
    } else if (status === 'leave') {
      leaveDays++;
    } else if (status === 'half_day') {
      halfDays++;
    }
  });

  const effectivePresentDays = (fullPresentDays * 1.0) + (halfDays * 0.5);
  const attendancePercentage = totalDays > 0
    ? Math.min(100, Math.max(0, Math.round((effectivePresentDays / totalDays) * 100)))
    : 100;

  return {
    totalDays,
    presentDays: fullPresentDays,
    absentDays,
    leaveDays,
    lateDays,
    halfDays,
    effectivePresentDays,
    attendancePercentage,
    attendanceRate: attendancePercentage
  };
}
