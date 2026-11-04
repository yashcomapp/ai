/**
 * ==============================================================================
 * CANONICAL SSOT VALIDATION & STRICT ENTRY BARRIER (Rule 2.R & 2.K)
 * ==============================================================================
 * 
 * Strict barrier to reject ANY non-canonical entity identifier across all ingress
 * points (Question Bank, Exam Generator, Manual Exam Creation, Registration).
 * 
 * Invariants:
 * 1. studentCode: Strictly ST-YYYY-XXXXXX (e.g. ST-2026-000001)
 * 2. boardCode: Strictly CBSE or MH
 * 3. class: Strictly 8, 9, 10
 * 4. subjectCode: Strictly official curriculum codes
 *    - CBSE 8: MGP1, MGP2, CURI
 *    - CBSE 9: MGM, SCIE
 *    - CBSE 10: MATH, SCI
 *    - MH 8: MTH, SCI
 *    - MH 9: MTH1, MTH2, SCIT
 *    - MH 10: MTH1, MTH2, SCIT1, SCIT2
 * 5. topicCode: ${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}
 * 6. questionCode: ${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}
 * ==============================================================================
 */

export const CANONICAL_BOARDS = ['CBSE', 'MH'] as const;
export type CanonicalBoard = typeof CANONICAL_BOARDS[number];

export const CANONICAL_CLASSES = ['8', '9', '10'] as const;
export type CanonicalClass = typeof CANONICAL_CLASSES[number];

export const CANONICAL_SUBJECT_CODES: Record<CanonicalBoard, Record<CanonicalClass, readonly string[]>> = {
  CBSE: {
    '8': ['MGP1', 'MGP2', 'CURI'] as const,
    '9': ['MGM', 'SCIE'] as const,
    '10': ['MATH', 'SCI'] as const,
  },
  MH: {
    '8': ['MTH', 'SCI'] as const,
    '9': ['MTH1', 'MTH2', 'SCIT'] as const,
    '10': ['MTH1', 'MTH2', 'SCIT1', 'SCIT2'] as const,
  }
};

export const CANONICAL_QUESTION_TYPES = [
  'OSC', // Single Choice MCQ
  'OMC', // Multiple Choice MCQ
  'OTF', // True / False
  'OAR', // Assertion & Reason
  'OFB', // Fill in the Blanks
  'ONE', // Numerical Objective
  'SDF', // Definition
  'SLP', // Laws & Principles
  'SSA', // Short Answer
  'SSR', // Scientific Reasoning / Notes
  'SSN', // Numerical Short
  'SLA', // Long Answer
  'SLN', // Numerical Long
] as const;
export type CanonicalQuestionType = typeof CANONICAL_QUESTION_TYPES[number];

export interface ValidationResult {
  valid: boolean;
  error?: string;
}

/**
 * Validates studentCode format strictly (ST-YYYY-XXXXXX).
 */
export function validateStudentCode(studentCode?: string | null): ValidationResult {
  if (!studentCode || typeof studentCode !== 'string') {
    return { valid: false, error: 'Student code is required and must be a string.' };
  }
  const trimmed = studentCode.trim();
  const regex = /^ST-\d{4}-\d{6}$/;
  if (!regex.test(trimmed)) {
    return {
      valid: false,
      error: `Invalid studentCode "${studentCode}". Must strictly match format "ST-YYYY-XXXXXX" (e.g. ST-2026-000001).`
    };
  }
  return { valid: true };
}

export function assertCanonicalStudentCode(studentCode?: string | null): void {
  const result = validateStudentCode(studentCode);
  if (!result.valid) {
    throw new Error(`[CANONICAL BARRIER VIOLATION] ${result.error}`);
  }
}

/**
 * Validates boardCode strictly ('CBSE' or 'MH').
 */
export function validateBoardCode(boardCode?: string | null): ValidationResult {
  if (!boardCode || typeof boardCode !== 'string') {
    return { valid: false, error: 'Board code is required and must be a string.' };
  }
  const trimmed = boardCode.trim();
  if (!CANONICAL_BOARDS.includes(trimmed as CanonicalBoard)) {
    return {
      valid: false,
      error: `Invalid boardCode "${boardCode}". Must strictly be "CBSE" or "MH".`
    };
  }
  return { valid: true };
}

/**
 * Validates subjectCode strictly against the given board and class.
 */
export function validateSubjectCode(boardCode?: string | null, classNum?: string | number | null, subjectCode?: string | null): ValidationResult {
  const boardRes = validateBoardCode(boardCode);
  if (!boardRes.valid) return boardRes;

  const cleanClass = String(classNum || '').trim();
  if (!CANONICAL_CLASSES.includes(cleanClass as CanonicalClass)) {
    return {
      valid: false,
      error: `Invalid class "${classNum}". Must strictly be "8", "9", or "10".`
    };
  }

  if (!subjectCode || typeof subjectCode !== 'string') {
    return { valid: false, error: 'Subject code is required.' };
  }
  const cleanSubject = subjectCode.trim();
  const allowed = CANONICAL_SUBJECT_CODES[boardCode as CanonicalBoard][cleanClass as CanonicalClass];
  if (!allowed.includes(cleanSubject)) {
    return {
      valid: false,
      error: `Invalid subjectCode "${subjectCode}" for ${boardCode} Class ${cleanClass}. Allowed canonical codes: ${allowed.join(', ')}.`
    };
  }

  return { valid: true };
}

export interface ParsedCanonicalTopic {
  boardCode: CanonicalBoard;
  classNum: CanonicalClass;
  subjectCode: string;
  chapterNumber: string;
  topicNumber: string;
  canonicalTopicCode: string;
}

/**
 * Validates topicCode strictly (${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}).
 */
export function validateTopicCode(topicCode?: string | null): ValidationResult & { parsed?: ParsedCanonicalTopic } {
  if (!topicCode || typeof topicCode !== 'string') {
    return { valid: false, error: 'Topic code is required.' };
  }
  const trimmed = topicCode.trim();
  const parts = trimmed.split('-');
  if (parts.length < 5) {
    return {
      valid: false,
      error: `Invalid topicCode "${topicCode}". Must have 5 parts separated by hyphens (e.g. MH-8-MTH-13-13.1.2).`
    };
  }

  const [bCode, cls, subjCode, chNum, ...rest] = parts;
  const tNum = rest.join('-'); // handles any sub-decimal notation

  const boardRes = validateBoardCode(bCode);
  if (!boardRes.valid) return boardRes;

  const subjRes = validateSubjectCode(bCode, cls, subjCode);
  if (!subjRes.valid) return subjRes;

  if (!/^\d+$/.test(chNum)) {
    return {
      valid: false,
      error: `Invalid chapter number "${chNum}" in topicCode "${topicCode}". Chapter must be a positive integer.`
    };
  }

  if (!/^[\d\.]+$/.test(tNum)) {
    return {
      valid: false,
      error: `Invalid topic number "${tNum}" in topicCode "${topicCode}". Topic number must be numeric/decimal (e.g. 1.1 or 13.1.2).`
    };
  }

  return {
    valid: true,
    parsed: {
      boardCode: bCode as CanonicalBoard,
      classNum: cls as CanonicalClass,
      subjectCode: subjCode,
      chapterNumber: chNum,
      topicNumber: tNum,
      canonicalTopicCode: `${bCode}-${cls}-${subjCode}-${chNum}-${tNum}`
    }
  };
}

function assertCanonicalTopicCode(topicCode?: string | null): ParsedCanonicalTopic {
  const result = validateTopicCode(topicCode);
  if (!result.valid || !result.parsed) {
    throw new Error(`[CANONICAL BARRIER VIOLATION] ${result.error}`);
  }
  return result.parsed;
}

export interface ParsedCanonicalQuestion {
  boardCode: CanonicalBoard;
  classNum: CanonicalClass;
  subjectCode: string;
  chapterNumber: string;
  topicNumber: string;
  topicCode: string;
  typeCode: CanonicalQuestionType;
  sequence: string;
  canonicalQuestionCode: string;
}

/**
 * Validates questionCode strictly (${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}).
 */
export function validateQuestionCode(questionCode?: string | null): ValidationResult & { parsed?: ParsedCanonicalQuestion } {
  if (!questionCode || typeof questionCode !== 'string') {
    return { valid: false, error: 'Question code is required.' };
  }
  const trimmed = questionCode.trim();
  const parts = trimmed.split('-');
  if (parts.length < 7) {
    return {
      valid: false,
      error: `Invalid questionCode "${questionCode}". Must strictly follow: {board}-{class}-{subject}-{chapter}-{topic}-{type}-{seq} (e.g. MH-8-MTH-13-13.1.2-OSC-001).`
    };
  }

  const seq = parts[parts.length - 1];
  const typeCode = parts[parts.length - 2];
  const topicParts = parts.slice(0, parts.length - 2);
  const derivedTopicCode = topicParts.join('-');

  const topicRes = validateTopicCode(derivedTopicCode);
  if (!topicRes.valid || !topicRes.parsed) {
    return {
      valid: false,
      error: `Invalid topic prefix in questionCode "${questionCode}": ${topicRes.error}`
    };
  }

  if (!CANONICAL_QUESTION_TYPES.includes(typeCode as CanonicalQuestionType)) {
    return {
      valid: false,
      error: `Invalid question type code "${typeCode}" in "${questionCode}". Allowed canonical types: ${CANONICAL_QUESTION_TYPES.join(', ')}.`
    };
  }

  if (!/^\d{3,}$/.test(seq)) {
    return {
      valid: false,
      error: `Invalid sequence "${seq}" in questionCode "${questionCode}". Sequence must be at least 3 digits (e.g. 001).`
    };
  }

  return {
    valid: true,
    parsed: {
      ...topicRes.parsed,
      topicCode: topicRes.parsed.canonicalTopicCode,
      typeCode: typeCode as CanonicalQuestionType,
      sequence: seq,
      canonicalQuestionCode: `${topicRes.parsed.canonicalTopicCode}-${typeCode}-${seq}`
    }
  };
}

function assertCanonicalQuestionCode(questionCode?: string | null): ParsedCanonicalQuestion {
  const result = validateQuestionCode(questionCode);
  if (!result.valid || !result.parsed) {
    throw new Error(`[CANONICAL BARRIER VIOLATION] ${result.error}`);
  }
  return result.parsed;
}

/**
 * Gatekeeper for Exam Creation/Generation Payload
 * Rejects any non-canonical exam payload before writing to Firestore.
 */
export function assertCanonicalExamPayload(examData: any): void {
  if (!examData || typeof examData !== 'object') {
    throw new Error('[CANONICAL BARRIER VIOLATION] Exam payload must be a non-null object.');
  }

  if (examData.topicCode) {
    assertCanonicalTopicCode(examData.topicCode);
  }

  if (Array.isArray(examData.topicCodes)) {
    for (const tc of examData.topicCodes) {
      assertCanonicalTopicCode(tc);
    }
  }

  if (Array.isArray(examData.questionCodes)) {
    for (const qc of examData.questionCodes) {
      assertCanonicalQuestionCode(qc);
    }
  }

  if (Array.isArray(examData.questionIds)) {
    for (const qc of examData.questionIds) {
      if (typeof qc === 'string' && qc.split('-').length >= 7) {
        assertCanonicalQuestionCode(qc);
      }
    }
  }

  const bCode = examData.boardCode || (examData.board === 'Maharashtra Board' ? 'MH' : examData.board);
  if (bCode) {
    const bRes = validateBoardCode(bCode);
    if (!bRes.valid) throw new Error(`[CANONICAL BARRIER VIOLATION] ${bRes.error}`);
  }

  const cls = examData.class;
  if (examData.subjectCode && bCode && cls) {
    const sRes = validateSubjectCode(bCode, cls, examData.subjectCode);
    if (!sRes.valid) throw new Error(`[CANONICAL BARRIER VIOLATION] ${sRes.error}`);
  }
}

/**
 * Gatekeeper for Question Bank Ingestion/Save Payload
 * Rejects any non-canonical question document before writing to Firestore.
 */
export function assertCanonicalQuestionPayload(questionData: any): void {
  if (!questionData || typeof questionData !== 'object') {
    throw new Error('[CANONICAL BARRIER VIOLATION] Question payload must be a non-null object.');
  }

  if (questionData.questionCode) {
    assertCanonicalQuestionCode(questionData.questionCode);
  }

  if (questionData.topicCode) {
    assertCanonicalTopicCode(questionData.topicCode);
  }

  const bCode = questionData.boardCode || (questionData.board === 'Maharashtra Board' ? 'MH' : questionData.board);
  const cls = questionData.class || questionData.classNum;
  if (bCode && cls && questionData.subjectCode) {
    const sRes = validateSubjectCode(bCode, cls, questionData.subjectCode);
    if (!sRes.valid) throw new Error(`[CANONICAL BARRIER VIOLATION] ${sRes.error}`);
  }
}
