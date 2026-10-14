/**
 * Single Source of Truth (SSOT) for Sleep Curfew & Maintenance Bypass Logic
 * Operating Hours for Students: 5:00 AM to 10:30 PM (Asia/Kolkata, IST).
 * Curfew Period: 10:30 PM (22:30) to 5:00 AM (05:00) IST.
 */

import { parseDateInput, getISTTimeComponents } from './dateUtils';

export const CURFEW_RESTRICTION_MESSAGE =
  'Rest is crucial for conceptual mastery! Yashcom Foundation restricts student logins between 10:30 PM and 5:00 AM to promote healthy sleep. Sleep well!';

/**
 * Checks whether an email or user profile qualifies for Curfew or Maintenance Bypass.
 */
export function isCurfewBypassed(
  email?: string | null,
  userData?: { curfewBypass?: boolean; maintenanceBypass?: boolean } | null
): boolean {
  const cleanEmail = (email || '').toLowerCase().trim();
  const envBypassEmail = (
    process.env.NEXT_PUBLIC_CURFEW_BYPASS_EMAIL ||
    (typeof process !== 'undefined' && process.env ? process.env.CURFEW_BYPASS_EMAIL : '') ||
    ''
  ).toLowerCase().trim();

  // Test / System accounts - excluded in production client bundles
  if (process.env.NODE_ENV !== 'production') {
    if (
      cleanEmail === 's@c.com' ||
      cleanEmail === 'p@c.com' ||
      cleanEmail === 'a@c.com'
    ) {
      return true;
    }
  }

  // Environment-configured bypass email
  if (envBypassEmail && cleanEmail === envBypassEmail) {
    return true;
  }

  // Database-flagged bypass overrides
  if (userData?.curfewBypass || userData?.maintenanceBypass) {
    return true;
  }

  return false;
}

/**
 * Evaluates whether the current IST time falls within the sleep curfew period (10:30 PM - 5:00 AM IST).
 */
export function isCurrentlyCurfewHours(currentTimeInput?: any): boolean {
  const dateObj = currentTimeInput ? parseDateInput(currentTimeInput) : new Date();
  if (!dateObj) return false;

  const { hours, minutes } = getISTTimeComponents(dateObj);
  return hours > 22 || (hours === 22 && minutes >= 30) || hours < 5;
}

/**
 * Authoritative curfew check for a student user.
 * Returns true if the user is strictly blocked by curfew.
 */
export function isStudentBlockedByCurfew(
  email?: string | null,
  userData?: { curfewBypass?: boolean; maintenanceBypass?: boolean } | null,
  currentTimeInput?: any
): boolean {
  if (isCurfewBypassed(email, userData)) {
    return false;
  }
  return isCurrentlyCurfewHours(currentTimeInput);
}
