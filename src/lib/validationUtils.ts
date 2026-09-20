/**
 * Shared Input Validation Utilities (SSOT)
 * Provides strict numeric and string validation to prevent NaN propagation,
 * negative financial amounts, and data corruption in Firestore records.
 */

/**
 * Validates and converts a value to a non-negative finite number (>= 0).
 * Throws an Error with a descriptive message if the value is NaN, null, undefined, infinite, or negative.
 */
export function toNonNegativeNumber(value: any, fieldName: string = 'value'): number {
  if (value === null || value === undefined || value === '') {
    throw new Error(`Invalid ${fieldName}: value is required and must be a valid number.`);
  }
  const num = Number(value);
  if (!Number.isFinite(num) || Number.isNaN(num)) {
    throw new Error(`Invalid ${fieldName}: expected a valid number, got "${value}".`);
  }
  if (num < 0) {
    throw new Error(`Invalid ${fieldName}: value cannot be negative, got ${num}.`);
  }
  return num;
}

/**
 * Validates and converts a value to a strictly positive finite number (> 0).
 * Throws an Error if value <= 0 or not a finite number.
 */
export function toPositiveNumber(value: any, fieldName: string = 'value'): number {
  const num = toNonNegativeNumber(value, fieldName);
  if (num <= 0) {
    throw new Error(`Invalid ${fieldName}: must be greater than 0, got ${num}.`);
  }
  return num;
}

/**
 * Safe number converter for calculation aggregations.
 * Returns `fallback` if value is null, undefined, NaN, infinite, or negative.
 */
export function safeNumber(value: any, fallback: number = 0): number {
  if (value === null || value === undefined || value === '') return fallback;
  const num = Number(value);
  if (!Number.isFinite(num) || Number.isNaN(num) || num < 0) return fallback;
  return num;
}
