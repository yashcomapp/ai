/**
 * Single Source of Truth (SSOT) Validation Rules & Regular Expressions
 * Used across client forms and server API route handlers to ensure parity.
 */

// Name: Letters, spaces, dots, hyphens, and apostrophes (min 2 characters)
export const NAME_RE = /^[a-zA-Z\s.'-]+$/;

// Email: Standard email format
export const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Mobile: 10 digits starting with 6, 7, 8, or 9
export const MOBILE_RE = /^[6-9]\d{9}$/;

// Password: Min 8 chars, at least 1 lowercase, 1 uppercase, 1 digit, and 1 special character
export const PASSWORD_RE = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?`~]).{8,}$/;

export interface ValidationResult {
  valid: boolean;
  error?: string;
}

export function validateName(name: string, requireFullName = true): ValidationResult {
  const trimmed = (name || '').trim();
  if (!trimmed) {
    return { valid: false, error: 'Name is required.' };
  }
  if (!NAME_RE.test(trimmed)) {
    return { valid: false, error: 'Name contains invalid characters.' };
  }
  if (requireFullName && trimmed.split(/\s+/).length < 2) {
    return { valid: false, error: 'Provide both first and last name.' };
  }
  return { valid: true };
}

export function validateEmail(email: string): ValidationResult {
  const trimmed = (email || '').trim();
  if (!trimmed) {
    return { valid: false, error: 'Email is required.' };
  }
  if (!EMAIL_RE.test(trimmed)) {
    return { valid: false, error: 'Enter a valid email address.' };
  }
  return { valid: true };
}

export function validateMobile(mobile: string): ValidationResult {
  const trimmed = (mobile || '').trim();
  if (!trimmed) {
    return { valid: false, error: 'Mobile number is required.' };
  }
  if (!MOBILE_RE.test(trimmed)) {
    return { valid: false, error: 'Enter a valid 10-digit mobile number starting with 6-9.' };
  }
  return { valid: true };
}

export function validatePassword(password: string): ValidationResult {
  if (!password) {
    return { valid: false, error: 'Password is required.' };
  }
  if (!PASSWORD_RE.test(password)) {
    return {
      valid: false,
      error: 'Password must be at least 8 characters and include uppercase, lowercase, a number, and a special character.'
    };
  }
  return { valid: true };
}
