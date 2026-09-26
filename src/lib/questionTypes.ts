
export function stripOptionLabel(text: any): string {
  if (text == null) return '';
  return String(text).replace(/^\s*\(?[A-Da-d]\)?[).:]\s*/, '');
}

export const DEFAULT_ASSERTION_REASON_OPTIONS: string[] = [
  'Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).',
  'Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).',
  'Assertion (A) is true, but Reason (R) is false.',
  'Assertion (A) is false, but Reason (R) is true.'
];

const MATH_PREPROCESS_CACHE = new Map<string, string>();
const RICH_TEXT_CACHE = new Map<string, string>();
const MAX_MATH_CACHE_SIZE = 3000;

export function preprocessMathText(text: any): string {
  if (text == null) return '';
  const key = String(text);
  if (MATH_PREPROCESS_CACHE.has(key)) {
    return MATH_PREPROCESS_CACHE.get(key)!;
  }

  let str = key;

  // Heal corruptions caused by swallowed backslashes in JSON (e.g. \t -> tab + imes => \times, \t -> tab + ext => \text, \x0C -> FF + rac => \frac)
  str = str.replace(/\t\s*imes\b/g, '\\times ')
           .replace(/\t\s*ext\{/g, '\\text{')
           .replace(/\t\s*extbf\{/g, '\\textbf{')
           .replace(/\t\s*heta\b/g, '\\theta ')
           .replace(/\t\s*an\b/g, '\\tan ')
           .replace(/\t\s*au\b/g, '\\tau ')
           .replace(/\t\s*riangle\b/g, '\\triangle ')
           .replace(/\n\s*eq\b/g, '\\neq ');

  // Normalize loose FormFeed and raw rac fractions from raw AI content
  str = str.replace(/\x0Crac/g, '\\frac')
           .replace(/(^|[^a-zA-Z\\])rac\{/g, '$1\\frac{');

  // Normalize loose degree Celsius superscripts missing a valid base (like .^\circ or /^\circ or ^\circ)
  str = str.replace(/(\{\})?\^\s*\\?circ/g, (match, p1) => {
    if (p1 === '{}') return match;
    return '{}^\\circ';
  });
  str = str.replace(/(\{\})?\^{\s*\\?circ\s*}/g, (match, p1) => {
    if (p1 === '{}') return match;
    return '{}^{\\circ}';
  });

  // Normalize display math $$...$$ to \[...\]
  str = str.replace(/(?<!\\)\$\$([\s\S]+?)\$\$/g, '\\[$1\\]');

  // Normalize inline math $...$ to \(...\)
  str = str.replace(/(?<!\\)\$([^\$]+?)\$/g, '\\($1\\)');

  // Replace literal '\n' followed by a capital letter with actual newlines
  str = str.replace(/\\n(?=[A-Z])/g, '\n');

  // Replace literal '\n' strings (not part of latex command names) with actual newlines
  str = str.replace(/\\n(?![a-zA-Z])/g, '\n');

  // Clean up nested double math delimiters like \(\- to \( and \)\) to \)
  str = str.replace(/\\\(+\\\(/g, '\\(')
           .replace(/\\\)+\\\)/g, '\\)');

  // Resolve nested delimiters enclosing text: \(text1\(text2\)text3\) -> text1\(text2\)text3
  str = str.replace(/\\\(([^()]*?)\\\(([^()]*?)\\\)([^()]*?)\\\)/g, '$1\\($2\\)$3');

  // 1. Extract all math blocks to prevent modifying parentheses/brackets inside them
  const mathBlocks: string[] = [];
  const mathRegex = /(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/g;
  
  str = str.replace(mathRegex, (match) => {
    const placeholder = `§§MATHBLOCK${mathBlocks.length}§§`;
    mathBlocks.push(match);
    return placeholder;
  });

  // 2. Perform conversions only on the text outside math blocks
  // Safely replace ([ ... ]) with \([ ... ]\) to restore math delimiters for options without corrupting solutions
  str = str.replace(/(?<!\\)\(\[([^\]]+)\]\)/g, '\\([$1]\\)');

  // Identify parentheses enclosing math constructs (like \, ^, _, \frac, etc.) and convert them to inline math delimiters \( ... \)
  str = str.replace(/(?<!\\)\(([^)]*?[\\^_][^)]*?)\)/g, '\\($1\\)');

  // Extract newly created math blocks to prevent dynamic wrapping from altering them
  str = str.replace(mathRegex, (match) => {
    const placeholder = `§§MATHBLOCK${mathBlocks.length}§§`;
    mathBlocks.push(match);
    return placeholder;
  });

  // NEW DYNAMIC WRAPPING: If there are raw math constructs left (containing \, ^, or _) without delimiters, wrap them
  const latexRegex = /(?<!\\)(?<!\()([a-zA-Z0-9\.\+\-\*\/\=,]*?\\[a-zA-Z]+(?:\{[^\}]*\}|\^[a-zA-Z0-9\+\-]+|_[a-zA-Z0-9\+\-]+)*|[a-zA-Z0-9\.\+\-\*\/]+[\^_][a-zA-Z0-9\.\+\-\*\/\{\}]*)/g;
  str = str.replace(latexRegex, (match) => {
    const trimmed = match.trim();
    if (!trimmed) return match;
    // Skip if it matches the placeholder format
    if (/§§MATHBLOCK\d+§§/.test(trimmed)) return match;
    // Don't wrap if it is already wrapped
    if (trimmed.startsWith('\\(') || trimmed.endsWith('\\)')) return match;
    if (trimmed.startsWith('\\[') || trimmed.endsWith('\\]')) return match;
    // Only wrap if it contains true math indicators (like \, ^, _)
    if (!trimmed.includes('\\') && !trimmed.includes('^') && !trimmed.includes('_')) return match;
    return `\\(${trimmed}\\)`;
  });

  // 3. Restore all math blocks
  mathBlocks.forEach((block, idx) => {
    str = str.replace(`§§MATHBLOCK${idx}§§`, block);
  });

  if (MATH_PREPROCESS_CACHE.size >= MAX_MATH_CACHE_SIZE) {
    const firstKey = MATH_PREPROCESS_CACHE.keys().next().value;
    if (firstKey !== undefined) MATH_PREPROCESS_CACHE.delete(firstKey);
  }
  MATH_PREPROCESS_CACHE.set(key, str);

  return str;
}

export function formatRichText(text: any): string {
  if (text == null) return '';
  const key = String(text);
  if (RICH_TEXT_CACHE.has(key)) {
    return RICH_TEXT_CACHE.get(key)!;
  }

  const processedMath = preprocessMathText(text);
  let str = String(processedMath);

  // Convert literal newlines (\\n) and actual newlines (\n) to actual <br/> tags since this is output as HTML
  str = str.replace(/(?:\\n|\n)(?![a-zA-Z])/g, '<br/>');

  // Convert markdown bold (**text**) to HTML <strong>
  str = str.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

  // Convert markdown italic (*text*) to HTML <em>
  str = str.replace(/\*([^*]+)\*/g, '<em>$1</em>');

  // Convert markdown underline (__text__) to HTML <u>
  str = str.replace(/__([^_]+)__/g, '<u>$1</u>');

  if (RICH_TEXT_CACHE.size >= MAX_MATH_CACHE_SIZE) {
    const firstKey = RICH_TEXT_CACHE.keys().next().value;
    if (firstKey !== undefined) RICH_TEXT_CACHE.delete(firstKey);
  }
  RICH_TEXT_CACHE.set(key, str);

  return str;
}


export function normalizeOptionAnswer(value: any, options?: any[]): string {
  if (value === undefined || value === null || value === '') return '';

  // If value is a number (0, 1, 2, 3) representing option index
  if (typeof value === 'number' && Number.isInteger(value) && value >= 0 && value < 26) {
    return String.fromCharCode(65 + value);
  }

  const valueStr = String(value).trim();

  // 1. Direct letter match with optional prefix: "A", "B", "Option A", "(A)", "Option (B)", "A.", "A:"
  const prefixMatch = valueStr.match(/^(?:option\s+)?\(?([A-Z])\)?[:.\-\s]?$/i);
  if (prefixMatch) {
    const letter = prefixMatch[1].toUpperCase();
    if (!options || !options.length) return letter;
    const idx = letter.charCodeAt(0) - 65;
    if (idx >= 0 && idx < options.length) return letter;
  }

  // 2. Match against options array by exact text, stripped text, and normalized math-aware text
  if (Array.isArray(options) && options.length > 0) {
    const norm = (s: any) => String(s ?? '').trim().toLowerCase();
    const cleanValNorm = cleanStringForMatch(stripOptionLabel(valueStr));
    const rawValClean = cleanStringForMatch(valueStr);

    const idx = options.findIndex((opt) => {
      const optText = (opt && typeof opt === 'object') ? (opt.text ?? opt.value ?? opt.label ?? '') : String(opt ?? '');
      if (norm(optText) === norm(valueStr)) return true;
      if (norm(stripOptionLabel(optText)) === norm(stripOptionLabel(valueStr))) return true;
      if (rawValClean && cleanStringForMatch(optText) === rawValClean) return true;
      if (cleanValNorm && cleanStringForMatch(stripOptionLabel(optText)) === cleanValNorm) return true;
      if (isOptionMatch(optText, valueStr)) return true;
      return false;
    });
    if (idx !== -1) return String.fromCharCode(65 + idx);
  }

  // 3. Fallback for single letter A-Z only
  if (/^[A-Z]$/i.test(valueStr)) {
    return valueStr.toUpperCase();
  }

  return valueStr.trim();
}

export type CanonicalQuestionType =
  | 'OSC'
  | 'OMC'
  | 'OTF'
  | 'OAR'
  | 'OFB'
  | 'ONE'
  | 'SDF'
  | 'SLP'
  | 'SSA'
  | 'SSR'
  | 'SSN'
  | 'SLA'
  | 'SLN';

export const CANONICAL_OBJECTIVE_TYPES: CanonicalQuestionType[] = ['OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE'];
export const CANONICAL_SUBJECTIVE_TYPES: CanonicalQuestionType[] = ['SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'];

/**
 * Single Source of Truth (SSOT) Canonical Question Type Converter.
 * Deterministically normalizes any input string/alias to its canonical 3-letter uppercase code.
 */
export function toCanonicalQuestionType(type: any): CanonicalQuestionType {
  const t = String(type || '').trim().toUpperCase().replace(/[-\s]/g, '_');

  // Direct canonical codes
  if (t === 'OSC') return 'OSC';
  if (t === 'OMC') return 'OMC';
  if (t === 'OTF') return 'OTF';
  if (t === 'OAR') return 'OAR';
  if (t === 'OFB') return 'OFB';
  if (t === 'ONE') return 'ONE';
  if (t === 'SDF') return 'SDF';
  if (t === 'SLP') return 'SLP';
  if (t === 'SSA') return 'SSA';
  if (t === 'SSR') return 'SSR';
  if (t === 'SSN') return 'SSN';
  if (t === 'SLA') return 'SLA';
  if (t === 'SLN') return 'SLN';

  // Legacy & descriptive names
  if (t === 'SINGLE_MCQ' || t === 'SINGLE_CHOICE' || t === 'MCQ' || t === 'SINGLE') return 'OSC';
  if (t === 'MULTIPLE_MCQ' || t === 'MULTI_MCQ' || t === 'MULTIPLE_CHOICE' || t === 'MULTI_SELECT') return 'OMC';
  if (t === 'TRUE_FALSE' || t === 'TF' || t === 'TRUEFALSE') return 'OTF';
  if (t === 'ASSERTION_REASON' || t === 'AR' || t === 'ASSERTION') return 'OAR';
  if (t === 'FILL_BLANKS' || t === 'FILL_BLANK' || t === 'FIB') return 'OFB';
  if (t === 'NUMERICAL' || t === 'NUMERICAL_OBJ' || t === 'NUM' || t === 'NUMERICAL5') return 'ONE';
  if (t === 'NUMERICAL_SHORT' || t === 'NUM_SHORT') return 'SSN';
  if (t === 'NUMERICAL_LONG' || t === 'NUM_LONG') return 'SLN';
  if (t === 'SUBJECTIVE_SHORT' || t === 'SUB_SHORT' || t === 'SHORT_ANSWER') return 'SSA';
  if (t === 'SUBJECTIVE_LONG' || t === 'SUB_LONG' || t === 'LONG_ANSWER') return 'SLA';
  if (t === 'SUBJECTIVE_REASON' || t === 'SUBJECTIVE_NOTES' || t === 'SCI_REASONING' || t === 'SCIENTIFIC_REASONING' || t === 'SHORT_NOTES' || t === 'NOTES') return 'SSR';
  if (t === 'SUBJECTIVE_DEFINE' || t === 'DEFINITION' || t === 'DEFINE') return 'SDF';
  if (t === 'SUBJECTIVE_LAWS' || t === 'LAWS' || t === 'PRINCIPLES') return 'SLP';

  // Default fallback for unrecognized objective types
  return 'OSC';
}

export function isMultipleChoiceType(type: any): boolean {
  return toCanonicalQuestionType(type) === 'OMC';
}

export function isSingleChoiceType(type: any): boolean {
  return toCanonicalQuestionType(type) === 'OSC';
}

export function isTrueFalseType(type: any): boolean {
  return toCanonicalQuestionType(type) === 'OTF';
}

export function isAssertionReasonType(type: any): boolean {
  return toCanonicalQuestionType(type) === 'OAR';
}

export function isFillBlanksType(type: any): boolean {
  return toCanonicalQuestionType(type) === 'OFB';
}

export function isNumericalType(type: any): boolean {
  const c = toCanonicalQuestionType(type);
  return c === 'ONE' || c === 'SSN' || c === 'SLN';
}

export function isObjectiveType(type: any): boolean {
  return CANONICAL_OBJECTIVE_TYPES.includes(toCanonicalQuestionType(type));
}

export function isSubjectiveType(type: any): boolean {
  return CANONICAL_SUBJECTIVE_TYPES.includes(toCanonicalQuestionType(type));
}

export function classifyAssertionReasonAnswer(value: any): string {
  if (!value) return '';
  let v = String(value).trim();

  const letterMatch = v.match(/^([A-D])$/i);
  if (letterMatch) return letterMatch[1].toUpperCase();

  v = v.replace(/^option[:\s]*/i, '').toLowerCase();

  const mentionsBoth = /\bboth\b/.test(v);
  const notCorrectExplanation = /not\s+(the\s+)?correct explanation/.test(v);
  const isCorrectExplanation = /correct explanation/.test(v) && !notCorrectExplanation;
  const assertionFalse = /assertion[^.]*\bfalse\b/.test(v) || /\ba\s+is\s+false\b/.test(v);
  const reasonFalse = /reason[^.]*\bfalse\b/.test(v) || /\br\s+is\s+false\b/.test(v);
  const assertionTrue = /assertion[^.]*\btrue\b/.test(v) || /\ba\s+is\s+true\b/.test(v);
  const reasonTrue = /reason[^.]*\btrue\b/.test(v) || /\br\s+is\s+true\b/.test(v);

  if (mentionsBoth && isCorrectExplanation) return 'A';
  if (mentionsBoth && notCorrectExplanation) return 'B';
  if (assertionTrue && reasonFalse) return 'C';
  if (assertionFalse && reasonTrue) return 'D';

  const fallback = v.match(/^([a-d])/i);
  return fallback ? fallback[1].toUpperCase() : v.toUpperCase();
}

export function evaluateQuestionAnswer(type: string, userAnswer: any, correctAnswer: any, options?: any[]): boolean {
  if (isBlank(userAnswer)) return false;
  const canonicalType = toCanonicalQuestionType(type);

  switch (canonicalType) {
    // 1. Multiple Choice (Multi-Select)
    case 'OMC': {
      let rawCorrect = correctAnswer;
      if ((!rawCorrect || (Array.isArray(rawCorrect) && rawCorrect.length === 0)) && Array.isArray(options) && options.length > 0) {
        const fromOpts = options
          .map((opt, idx) => (opt && typeof opt === 'object' && (opt.isCorrect || opt.correct)) ? String.fromCharCode(65 + idx) : null)
          .filter(Boolean);
        if (fromOpts.length > 0) rawCorrect = fromOpts;
      }

      const userList = parseAnswerList(userAnswer);
      const correctList = parseAnswerList(rawCorrect);

      const userNorm = Array.from(new Set(userList.map(v => normalizeOptionAnswer(v, options)).filter(Boolean))).sort();
      const correctNorm = Array.from(new Set(correctList.map(v => normalizeOptionAnswer(v, options)).filter(Boolean))).sort();

      if (userNorm.length === 0 && correctNorm.length === 0) return false;
      return JSON.stringify(userNorm) === JSON.stringify(correctNorm);
    }

    // 2. Single MCQ
    case 'OSC': {
      let rawCorrect = correctAnswer;
      if (!rawCorrect && Array.isArray(options) && options.length > 0) {
        const fromOpt = options.find((opt: any) => opt && typeof opt === 'object' && (opt.isCorrect || opt.correct));
        if (fromOpt) rawCorrect = fromOpt.text || fromOpt.value || fromOpt.label || '';
      }
      const userNorm = normalizeOptionAnswer(userAnswer, options);
      const correctNorm = normalizeOptionAnswer(rawCorrect, options);
      return Boolean(userNorm && correctNorm && userNorm === correctNorm);
    }

    // 3. True / False
    case 'OTF': {
      const normTF = (val: any) => {
        const s = String(val ?? '').trim().toLowerCase();
        if (s === 'true' || s === 't' || s === '1' || s === 'yes' || s === 'correct') return 'true';
        if (s === 'false' || s === 'f' || s === '0' || s === 'no' || s === 'incorrect') return 'false';
        return s;
      };
      const userNorm = normTF(userAnswer);
      const correctNorm = normTF(correctAnswer);
      if (userNorm && correctNorm && userNorm === correctNorm) return true;
      if (Array.isArray(options) && options.length > 0) {
        const uOpt = normalizeOptionAnswer(userAnswer, options);
        const cOpt = normalizeOptionAnswer(correctAnswer, options);
        return Boolean(uOpt && cOpt && uOpt === cOpt);
      }
      return Boolean(userNorm && correctNorm && userNorm === correctNorm);
    }

    // 4. Assertion & Reason
    case 'OAR': {
      const userNorm = classifyAssertionReasonAnswer(userAnswer);
      const correctNorm = classifyAssertionReasonAnswer(correctAnswer);
      return Boolean(userNorm && correctNorm && userNorm === correctNorm);
    }

    // 5. Fill in the Blanks
    case 'OFB': {
      const cleanU = cleanStringForMatch(userAnswer);
      const cleanC = cleanStringForMatch(correctAnswer);
      if (cleanU && cleanC && cleanU === cleanC) return true;
      const userNorm = String(userAnswer || '').trim().toLowerCase();
      const correctNorm = String(correctAnswer || '').trim().toLowerCase();
      return Boolean(userNorm && correctNorm && userNorm === correctNorm);
    }

    // 6. Numerical Objective
    case 'ONE':
    case 'SSN':
    case 'SLN': {
      if (Array.isArray(options) && options.length > 0) {
        const userNorm = normalizeOptionAnswer(userAnswer, options);
        const correctNorm = normalizeOptionAnswer(correctAnswer, options);
        if (userNorm && correctNorm && userNorm === correctNorm) return true;
      }
      const u = parseFloat(String(userAnswer).replace(/[^0-9.\-]/g, ''));
      const c = parseFloat(String(correctAnswer).replace(/[^0-9.\-]/g, ''));
      if (!isNaN(u) && !isNaN(c) && Math.abs(u - c) <= 0.05) return true;
      return cleanStringForMatch(userAnswer) === cleanStringForMatch(correctAnswer);
    }

    // General fallback for any options-based question or subjective text
    default: {
      if (Array.isArray(options) && options.length > 0) {
        const userNorm = normalizeOptionAnswer(userAnswer, options);
        const correctNorm = normalizeOptionAnswer(correctAnswer, options);
        if (userNorm && correctNorm && userNorm === correctNorm) return true;
      }
      return cleanStringForMatch(userAnswer) === cleanStringForMatch(correctAnswer);
    }
  }
}

export function extractAssertionAndReason(q: any): { assertion: string; reason: string } {
  if (!q) return { assertion: '', reason: '' };

  let rawAssertion = String(q.assertion || '').trim();
  let rawReason = String(q.reason || '').trim();
  const rawText = String(q.text || '').trim();

  // If rawAssertion contains Reason text, or if both are empty and rawText exists:
  const reasonRegex = /(?:Reason\s*\((?:R)\)|Reason\s*[:\-]|(?:\b|\n)R\s*[:\-])\s*/i;
  if (rawAssertion.includes('Reason (R):') || rawAssertion.includes('Reason:') || rawAssertion.includes('(R):') || (!rawAssertion && !rawReason && rawText)) {
    const combined = rawAssertion || rawText;
    const parts = combined.split(reasonRegex);
    if (parts.length >= 2) {
      rawAssertion = parts[0];
      rawReason = parts.slice(1).join(' ');
    }
  }

  // Strip redundant leading prefixes from assertion
  const cleanAssertion = rawAssertion
    .replace(/^Assertion\s*\((?:A)\)\s*[:\-]?\s*/i, '')
    .replace(/^Assertion\s*[:\-]?\s*/i, '')
    .replace(/^\(?A\)?\s*[:\-]\s*/i, '')
    .trim();

  // Strip redundant leading prefixes from reason
  const cleanReason = rawReason
    .replace(/^Reason\s*\((?:R)\)\s*[:\-]?\s*/i, '')
    .replace(/^Reason\s*[:\-]?\s*/i, '')
    .replace(/^\(?R\)?\s*[:\-]\s*/i, '')
    .trim();

  return {
    assertion: cleanAssertion || rawAssertion || rawText,
    reason: cleanReason || rawReason
  };
}

export const CANONICAL_SUBJECT_NAMES: Record<string, string> = {
  // CBSE
  'MGP1': 'Mathematics (Ganit Prakash 1)',
  'CURI': 'Science (Curiosity)',
  'MGM': 'Mathematics (Ganita Manjari)',
  'SCIE': 'Science (Exploration)',
  'MATH': 'Mathematics',
  'SCI': 'Science',
  // Maharashtra Board
  'MTH1': 'Mathematics Part 1 (Algebra)',
  'MTH2': 'Mathematics Part 2 (Geometry)',
  'SCIT': 'Science & Technology',
  'SCIT1': 'Science & Technology Part 1',
  'SCIT2': 'Science & Technology Part 2',
};

export function getCanonicalSubjectName(subjectCode?: string, topicCode?: string, chapterName?: string): string {
  if (subjectCode) {
    const clean = subjectCode.trim().toUpperCase();
    if (CANONICAL_SUBJECT_NAMES[clean]) {
      return CANONICAL_SUBJECT_NAMES[clean];
    }
  }
  if (topicCode) {
    const parts = topicCode.split('-');
    if (parts.length >= 3) {
      const code = parts[2].trim().toUpperCase();
      if (CANONICAL_SUBJECT_NAMES[code]) {
        return CANONICAL_SUBJECT_NAMES[code];
      }
    }
  }
  return subjectCode || 'Science & Technology';
}

export const QUESTION_TYPE_MAP: { [key: string]: { id: string; label: string; code: CanonicalQuestionType; category: 'objective' | 'subjective'; defaultMarks: number } } = {
  // Canonical 3-letter codes
  OSC: { id: 'OSC', label: 'Single Choice MCQ', code: 'OSC', category: 'objective', defaultMarks: 4 },
  OMC: { id: 'OMC', label: 'Multiple Choice MCQ', code: 'OMC', category: 'objective', defaultMarks: 4 },
  OTF: { id: 'OTF', label: 'True / False', code: 'OTF', category: 'objective', defaultMarks: 4 },
  OAR: { id: 'OAR', label: 'Assertion & Reason', code: 'OAR', category: 'objective', defaultMarks: 4 },
  OFB: { id: 'OFB', label: 'Fill in the Blanks', code: 'OFB', category: 'objective', defaultMarks: 4 },
  ONE: { id: 'ONE', label: 'Numerical Objective', code: 'ONE', category: 'objective', defaultMarks: 4 },
  SDF: { id: 'SDF', label: 'Definition (1m)', code: 'SDF', category: 'subjective', defaultMarks: 1 },
  SLP: { id: 'SLP', label: 'Laws & Principles (1m)', code: 'SLP', category: 'subjective', defaultMarks: 1 },
  SSA: { id: 'SSA', label: 'Short Answer (2m)', code: 'SSA', category: 'subjective', defaultMarks: 2 },
  SSR: { id: 'SSR', label: 'Scientific Reasoning / Notes (2m)', code: 'SSR', category: 'subjective', defaultMarks: 2 },
  SSN: { id: 'SSN', label: 'Numerical Short (2m)', code: 'SSN', category: 'subjective', defaultMarks: 2 },
  SLA: { id: 'SLA', label: 'Long Answer (4m)', code: 'SLA', category: 'subjective', defaultMarks: 4 },
  SLN: { id: 'SLN', label: 'Numerical Long (4m)', code: 'SLN', category: 'subjective', defaultMarks: 4 },

  // Legacy mappings for backwards compatibility
  single_mcq: { id: 'single_mcq', label: 'Single Choice MCQ', code: 'OSC', category: 'objective', defaultMarks: 4 },
  multiple_mcq: { id: 'multiple_mcq', label: 'Multiple Choice MCQ', code: 'OMC', category: 'objective', defaultMarks: 4 },
  true_false: { id: 'true_false', label: 'True / False', code: 'OTF', category: 'objective', defaultMarks: 4 },
  assertion_reason: { id: 'assertion_reason', label: 'Assertion & Reason', code: 'OAR', category: 'objective', defaultMarks: 4 },
  fill_blanks: { id: 'fill_blanks', label: 'Fill in the Blanks', code: 'OFB', category: 'objective', defaultMarks: 4 },
  numerical: { id: 'numerical', label: 'Numerical Objective', code: 'ONE', category: 'objective', defaultMarks: 4 },
  numerical_short: { id: 'numerical_short', label: 'Numerical Short (2m)', code: 'SSN', category: 'subjective', defaultMarks: 2 },
  numerical_long: { id: 'numerical_long', label: 'Numerical Long (4m)', code: 'SLN', category: 'subjective', defaultMarks: 4 },
  subjective_short: { id: 'subjective_short', label: 'Short Answer (2m)', code: 'SSA', category: 'subjective', defaultMarks: 2 },
  subjective_long: { id: 'subjective_long', label: 'Long Answer (4m)', code: 'SLA', category: 'subjective', defaultMarks: 4 },
  subjective_reason: { id: 'subjective_reason', label: 'Scientific Reasoning (2m)', code: 'SSR', category: 'subjective', defaultMarks: 2 },
  subjective_notes: { id: 'subjective_notes', label: 'Short Notes (2m)', code: 'SSR', category: 'subjective', defaultMarks: 2 },
  subjective_define: { id: 'subjective_define', label: 'Definition (1m)', code: 'SDF', category: 'subjective', defaultMarks: 1 },
  subjective_laws: { id: 'subjective_laws', label: 'Laws & Principles (1m)', code: 'SLP', category: 'subjective', defaultMarks: 1 },
};

export const OBJECTIVE_QUESTION_TYPES = [
  { id: 'OSC', label: 'Single Choice MCQ (OSC)', code: 'OSC' },
  { id: 'OMC', label: 'Multiple Choice MCQ (OMC)', code: 'OMC' },
  { id: 'OTF', label: 'True / False (OTF)', code: 'OTF' },
  { id: 'OAR', label: 'Assertion & Reason (OAR)', code: 'OAR' },
  { id: 'OFB', label: 'Fill in the Blanks (OFB)', code: 'OFB' },
  { id: 'ONE', label: 'Numerical Objective (ONE)', code: 'ONE' }
];

export const SUBJECTIVE_QUESTION_TYPES = [
  { id: 'SDF', label: 'Definition (SDF - 1m)', code: 'SDF' },
  { id: 'SLP', label: 'Laws & Principles (SLP - 1m)', code: 'SLP' },
  { id: 'SSA', label: 'Short Answer (SSA - 2m)', code: 'SSA' },
  { id: 'SSR', label: 'Scientific Reasoning / Notes (SSR - 2m)', code: 'SSR' },
  { id: 'SSN', label: 'Numerical Short (SSN - 2m)', code: 'SSN' },
  { id: 'SLA', label: 'Long Answer (SLA - 4m)', code: 'SLA' },
  { id: 'SLN', label: 'Numerical Long (SLN - 4m)', code: 'SLN' }
];

export function deriveTopicCodeFromQuestionCode(qCode: string): string {
  if (!qCode) return '';
  const cleanCode = qCode.replace(/[-_]\d+$/, '');
  const parts = cleanCode.split(/[-_]/);
  if (parts.length >= 5) {
    if (parts[4].includes('.')) {
      return `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${parts[4]}`;
    } else if (parts.length >= 7 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5]) && /^\d+$/.test(parts[6])) {
      return `${parts[0]}-${parts[1]}-${parts[2]}-${parts[4]}-${parts[5]}.${parts[6]}`;
    } else if (parts.length === 6 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5])) {
      return `${parts[0]}-${parts[1]}-${parts[2]}-${parts[4]}-${parts[4]}.${parts[5]}`;
    } else if (/^\d+$/.test(parts[3]) && parts[4].includes('.')) {
      return `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${parts[4]}`;
    }
  }
  return '';
}

export interface ParsedTopicCode {
  board: string;
  boardCode: string;
  class: string;
  classNum: string;
  subject: string;
  subjectCode: string;
  chapter: string;
  chapterNumber: string;
  topic: string;
  topicNumber: string;
  canonicalTopicCode: string;
}

/**
 * Canonical Topic Code Parser: Guarantees unified parsing across all pages & services.
 * Handles both standard 5-part and reconstructed decimal formats (e.g. MH-9-SCIT-3-3.2 or MH-9-SCIT-3-3-2).
 */
export function parseTopicCode(topicCode?: string | null): ParsedTopicCode | null {
  if (!topicCode || typeof topicCode !== 'string') return null;
  const clean = topicCode.trim();
  if (!clean.includes('-')) return null;
  const parts = clean.split('-');
  if (parts.length < 3) return null;

  const boardCode = parts[0] || '';
  const board = boardCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board';
  const cls = parts[1] || '';
  const subjectCode = parts[2] || '';
  const chapterNumber = parts[3] || '';
  
  // Topic number: 5th token or reconstructed from trailing tokens (e.g. 3-2 -> 3.2)
  let topicNumber = parts[4] || '';
  if (parts.length >= 6 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5])) {
    topicNumber = `${parts[4]}.${parts[5]}`;
  } else if (parts.length >= 5 && parts[4]) {
    topicNumber = parts[4];
  }

  const canonicalTopicCode = chapterNumber && topicNumber
    ? `${boardCode}-${cls}-${subjectCode}-${chapterNumber}-${topicNumber}`
    : `${boardCode}-${cls}-${subjectCode}`;

  return {
    board,
    boardCode,
    class: cls,
    classNum: cls,
    subject: subjectCode,
    subjectCode,
    chapter: chapterNumber,
    chapterNumber,
    topic: topicNumber,
    topicNumber,
    canonicalTopicCode
  };
}

export const KATEX_AUTO_RENDER_OPTIONS = {
  delimiters: [
    { left: '$$', right: '$$', display: true },
    { left: '$', right: '$', display: false },
    { left: '\\(', right: '\\)', display: false },
    { left: '\\[', right: '\\]', display: true }
  ],
  throwOnError: false
};

export function robustParseAIJson(rawText: string): any {
  let cleaned = rawText.trim().replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/\s*```$/i, '');

  // Clean any accidental FormFeed swallowed by JS string literal parser
  cleaned = cleaned.replace(/\x0Crac/g, '\\\\frac');
  cleaned = cleaned.replace(/\f/g, '');

  // Remove trailing commas before ] or }
  cleaned = cleaned.replace(/,\s*([\]}])/g, '$1');

  // 1. Double escape backslashes safely inside string literals without breaking valid JSON escape sequences (\", \\, \n, \t)
  let escapedStr = '';
  let inString = false;
  for (let i = 0; i < cleaned.length; i++) {
    const char = cleaned[i];
    if (char === '"' && (i === 0 || cleaned[i - 1] !== '\\')) {
      inString = !inString;
      escapedStr += char;
    } else if (inString && char === '\\') {
      const nextChar = cleaned[i + 1];
      const afterNext = cleaned[i + 2];
      if (nextChar === '"' || nextChar === '\\') {
        escapedStr += '\\' + nextChar;
        i++; // skip next char
      } else if (nextChar === 'n' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\n';
        i++;
      } else if (nextChar === 't' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\t';
        i++;
      } else if (nextChar === 'r' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\r';
        i++;
      } else {
        escapedStr += '\\\\';
      }
    } else {
      escapedStr += char;
    }
  }
  cleaned = escapedStr;

  // 2. Escape unescaped raw newlines, carriage returns, and tabs inside string literals to prevent bad control character errors
  let sanitizedStr = '';
  inString = false;
  let escaped = false;
  for (let i = 0; i < cleaned.length; i++) {
    const char = cleaned[i];
    if (inString) {
      if (escaped) {
        sanitizedStr += char;
        escaped = false;
      } else if (char === '\\') {
        sanitizedStr += char;
        escaped = true;
      } else if (char === '"') {
        sanitizedStr += char;
        inString = false;
      } else if (char === '\n') {
        sanitizedStr += '\\n';
      } else if (char === '\r') {
        sanitizedStr += '\\r';
      } else if (char === '\t') {
        sanitizedStr += '\\t';
      } else {
        const code = char.charCodeAt(0);
        if (code < 32) {
          sanitizedStr += '\\u' + code.toString(16).padStart(4, '0');
        } else {
          sanitizedStr += char;
        }
      }
    } else {
      if (char === '"') {
        inString = true;
      }
      sanitizedStr += char;
    }
  }
  cleaned = sanitizedStr;

  const arrayMatch = cleaned.match(/\[[\s\S]*\]/);
  if (arrayMatch) {
    try {
      return JSON.parse(arrayMatch[0]);
    } catch (e: any) {
      console.warn("Array parse failed in robustParseAIJson:", e.message);
    }
  }

  const objectMatch = cleaned.match(/\{[\s\S]*\}/);
  if (objectMatch) {
    try {
      const obj = JSON.parse(objectMatch[0]);
      return obj.questions || [obj];
    } catch (e: any) {
      console.warn("Object parse failed in robustParseAIJson:", e.message);
    }
  }

  throw new Error('No valid JSON array or object could be extracted from response.');
}

export function parseAiSolutionsMap(rawText: string): Record<string, string> {
  if (!rawText || typeof rawText !== 'string') {
    throw new Error('Input text is empty');
  }

  let text = rawText.trim();

  // Find the JSON object { ... } in text. If user pasted prompt + questions array + solution json + user comments,
  // extract the JSON object mapping questionCode to solution string.
  let candidateJsonStr = '';
  const lastOpenBrace = text.lastIndexOf('{');
  const lastCloseBrace = text.lastIndexOf('}');

  if (lastOpenBrace !== -1 && lastCloseBrace > lastOpenBrace) {
    candidateJsonStr = text.substring(lastOpenBrace, lastCloseBrace + 1);
  } else {
    candidateJsonStr = text;
  }

  let cleaned = candidateJsonStr.trim().replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/\s*```$/i, '');
  cleaned = cleaned.replace(/,\s*([\]}])/g, '$1');

  let escapedStr = '';
  let inString = false;
  for (let i = 0; i < cleaned.length; i++) {
    const char = cleaned[i];
    if (char === '"' && (i === 0 || cleaned[i - 1] !== '\\')) {
      inString = !inString;
      escapedStr += char;
    } else if (inString && char === '\\') {
      const nextChar = cleaned[i + 1];
      const afterNext = cleaned[i + 2];
      if (nextChar === '"' || nextChar === '\\') {
        escapedStr += '\\' + nextChar;
        i++;
      } else if (nextChar === 'n' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\n';
        i++;
      } else if (nextChar === 't' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\t';
        i++;
      } else if (nextChar === 'r' && !/[a-zA-Z]/.test(afterNext || '')) {
        escapedStr += '\\r';
        i++;
      } else {
        escapedStr += '\\\\';
      }
    } else {
      escapedStr += char;
    }
  }
  cleaned = escapedStr;

  let sanitizedStr = '';
  inString = false;
  let escaped = false;
  for (let i = 0; i < cleaned.length; i++) {
    const char = cleaned[i];
    if (inString) {
      if (escaped) {
        sanitizedStr += char;
        escaped = false;
      } else if (char === '\\') {
        sanitizedStr += char;
        escaped = true;
      } else if (char === '"') {
        sanitizedStr += char;
        inString = false;
      } else if (char === '\n') {
        sanitizedStr += '\\n';
      } else if (char === '\r') {
        sanitizedStr += '\\r';
      } else if (char === '\t') {
        sanitizedStr += '\\t';
      } else {
        const code = char.charCodeAt(0);
        if (code < 32) {
          sanitizedStr += '\\u' + code.toString(16).padStart(4, '0');
        } else {
          sanitizedStr += char;
        }
      }
    } else {
      if (char === '"') {
        inString = true;
      }
      sanitizedStr += char;
    }
  }

  let parsedObj: any = null;
  try {
    parsedObj = JSON.parse(sanitizedStr);
  } catch (e: any) {
    const map: Record<string, string> = {};
    const kvRegex = /"([A-Za-z0-9_\-\.]+)"\s*:\s*"([\s\S]*?)"(?=\s*,\s*"|\s*\}\s*$)/g;
    let match;
    while ((match = kvRegex.exec(rawText)) !== null) {
      map[match[1]] = match[2].replace(/\\n/g, '\n').replace(/\\"/g, '"');
    }
    if (Object.keys(map).length > 0) {
      return map;
    }
    throw new Error(`Failed to parse solutions JSON: ${e.message}`);
  }

  if (typeof parsedObj === 'object' && parsedObj !== null && !Array.isArray(parsedObj)) {
    return parsedObj;
  }

  throw new Error('Parsed result is not a valid key-value JSON object.');
}

export function smartJsonParse(str: string): any {
  const fixed = str.replace(/\\/g, '\\\\').replace(/\\\\\\\\/g, '\\\\');
  try {
    return JSON.parse(fixed);
  } catch (e) {
    return JSON.parse(str);
  }
}

export function restoreLatex(obj: any): any {
  if (typeof obj === 'string') {
    return obj.replace(/\\\\/g, '\\');
  }
  if (Array.isArray(obj)) {
    return obj.map(restoreLatex);
  }
  if (obj && typeof obj === 'object') {
    const copy: any = {};
    Object.keys(obj).forEach(k => {
      copy[k] = restoreLatex(obj[k]);
    });
    return copy;
  }
  return obj;
}

export function cleanOptionPrefix(str: string): string {
  return String(str || '')
    .replace(/^(?:Option\s+[A-D][:\.\-\)]\s*|\(?[A-D]\)?[\.:\-]\s*|\(?[1-4]\)?[\.:\-]\s*)/i, '')
    .trim();
}

export function normalizeOptionText(str: string): string {
  return cleanOptionPrefix(str)
    .replace(/\\\\/g, '\\') // convert double backslashes to single
    .replace(/\s+/g, ' ')   // normalize whitespace
    .trim()
    .toLowerCase();
}

/**
 * Robustly matches an option against a target answer string.
 * Respects exact matches and case-sensitivity for short scientific units/symbols (e.g. 'n' vs 'N', 'm' vs 'M', 'Pa').
 */
export function isOptionMatch(opt: any, target: any): boolean {
  if (opt === undefined || opt === null || target === undefined || target === null) return false;
  const optStr = String(opt).trim();
  const targetStr = String(target).trim();
  if (optStr === targetStr) return true;
  
  const cleanOpt = cleanOptionPrefix(optStr).trim();
  const cleanTarget = cleanOptionPrefix(targetStr).trim();
  if (cleanOpt === cleanTarget) return true;

  // For short symbols/units (<= 3 chars, e.g. 'n' vs 'N', 'm' vs 'M', 'Pa') or LaTeX/math expressions, require exact case
  if (cleanOpt.length <= 3 || cleanTarget.length <= 3 || /[\\_{}^$]/.test(cleanOpt) || /[\\_{}^$]/.test(cleanTarget)) {
    return cleanOpt === cleanTarget;
  }

  return normalizeOptionText(cleanOpt) === normalizeOptionText(cleanTarget) || cleanStringForMatch(cleanOpt) === cleanStringForMatch(cleanTarget);
}

export function validateQuestion(q: any, questionType: 'objective' | 'subjective' | 'all_in_one' | 'dual_track' | string): string[] {
  const errors: string[] = [];
  
  if (!q.text || !String(q.text).trim()) {
    errors.push('Missing question text.');
  }

  const textStr = String(q.text || '');
  const solStr = String(q.solution || '');

  // 1. Check for synthetic placeholder patterns in question text or solution
  const forbiddenPatterns = [
    /Option\s+[A-D]\s*\(/i,
    /High-rigor competitive problem/i,
    /\[OLYMPIAD\s*\/\s*FOUNDATION\s*HOTS\]/i,
    /variable\s+[A-D]\s+is/i,
    /parameter\s+[A-D]\s+is/i,
    /Calculate the resultant value when/i,
    /Given primary variable\s*=/i,
    /Given secondary parameter\s*=/i,
    /Option\s+[A-D]$/i
  ];

  for (const pat of forbiddenPatterns) {
    if (pat.test(textStr) || pat.test(solStr)) {
      errors.push(`Flagged synthetic/placeholder content detected matching pattern: ${pat.toString()}`);
      break;
    }
  }

  // Normalize type
  const rawType = q.type || q.qtype || '';
  const canonicalType = toCanonicalQuestionType(rawType);
  const isSubjective = questionType === 'subjective' || 
    (questionType === 'all_in_one' && (isSubjectiveType(canonicalType) || (q.marks && !q.options?.length && canonicalType !== 'ONE')));

  // Check for phantom diagram / figure references without image
  if (!q.imageUrl && !q.figureUrl) {
    const phantomRegex = /\b(as shown in the (figure|diagram|image|illustration|graph|circuit)|refer to the (figure|diagram|image|table)|in the given (figure|diagram|graph|circuit)|shown in the diagram below|see figure below)\b/i;
    if (phantomRegex.test(textStr)) {
      errors.push('Phantom figure reference detected without an uploaded image. Remove diagram references or attach an image.');
    }
  }

  // Check for duplicate options in MCQs (preserving case for short symbols/units like 'n' vs 'N')
  if (Array.isArray(q.options) && q.options.length >= 2) {
    const cleanedList = q.options.map((opt: any) => cleanOptionPrefix(String(opt || '')).replace(/\\\\/g, '\\').replace(/\s+/g, ' ').trim()).filter(Boolean);
    
    // Check for exact duplicates
    const exactDuplicates = cleanedList.some((item: string, idx: number) => cleanedList.indexOf(item) !== idx);
    if (exactDuplicates) {
      errors.push('Duplicate options detected: two or more options are identical.');
    } else {
      // Check for case-insensitive duplicate only for longer non-math text (> 3 chars)
      const normList = cleanedList.map((item: string) => {
        if (item.length <= 3 || /[\\_{}^$]/.test(item)) {
          return item; // preserve case for units and symbols (e.g. 'n' vs 'N')
        }
        return item.toLowerCase();
      });
      if (new Set(normList).size !== normList.length) {
        errors.push('Duplicate options detected: two or more options are identical or near-identical.');
      }
    }
  }

  if (!isSubjective) {
    if (canonicalType === 'OSC' || canonicalType === 'OTF') {
      if (!q.correctAnswer || !String(q.correctAnswer).trim()) {
        errors.push('Missing correct answer.');
      } else if (Array.isArray(q.options) && q.options.length > 0) {
        // Check for dummy placeholder strings inside options
        for (const opt of q.options) {
          const optStr = String(opt || '').trim();
          if (/^Option\s+[A-D]$/i.test(optStr) || /^Option\s+[A-D]\s*\(/i.test(optStr) || /placeholder/i.test(optStr)) {
            errors.push(`Option contains placeholder text: "${optStr}"`);
          }
        }

        const isMatched = q.options.some((opt: any) => isOptionMatch(opt, q.correctAnswer));
        if (!isMatched) {
          errors.push('Correct answer does not match any items in options list.');
        }
      }
    } else if (canonicalType === 'OMC') {
      if (!q.correctAnswers || !Array.isArray(q.correctAnswers) || q.correctAnswers.length === 0) {
        errors.push('Missing correctAnswers list.');
      } else if (Array.isArray(q.options) && q.options.length > 0) {
        q.correctAnswers.forEach((ans: any) => {
          const isMatched = q.options.some((opt: any) => isOptionMatch(opt, ans));
          if (!isMatched) {
            errors.push(`Correct answer "${ans}" not found in options list.`);
          }
        });
      }
    } else if (canonicalType === 'OAR') {
      const correctNorm = String(q.correctAnswer || '').trim().toUpperCase();
      if (!['A', 'B', 'C', 'D'].includes(correctNorm)) {
        errors.push('Correct answer for Assertion-Reason must be A, B, C, or D.');
      }
    } else if (canonicalType === 'ONE' || canonicalType === 'OFB') {
      if (!q.correctAnswer || !String(q.correctAnswer).trim()) {
        errors.push('Numerical and Fill-in-the-Blanks questions must specify a valid correct answer.');
      } else if (Array.isArray(q.options) && q.options.length > 0) {
        const isMatched = q.options.some((opt: any) => 
          isOptionMatch(opt, q.correctAnswer) ||
          (!isNaN(parseFloat(String(opt))) && !isNaN(parseFloat(String(q.correctAnswer))) && Math.abs(parseFloat(String(opt)) - parseFloat(String(q.correctAnswer))) <= 0.05)
        );
        if (!isMatched) {
          errors.push('Correct answer does not match any items in options list.');
        }
      }
    }
  } else {
    // Subjective question validation
    if (!q.solution || !String(q.solution).trim()) {
      if (!q.answerLines || q.answerLines.length === 0) {
        errors.push('Missing verbatim model answer/solution.');
      }
    }
    const marksNum = Number(q.marks);
    if (isNaN(marksNum) || marksNum <= 0) {
      errors.push('Marks must be a positive number.');
    }
  }

  return errors;
}

export function shuffleArray<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function isBlank(userAns: any): boolean {
  if (userAns === undefined || userAns === null) return true;
  if (typeof userAns === 'object' && 'isAttempted' in userAns) {
    return !userAns.isAttempted;
  }
  if (typeof userAns === 'string' && userAns.trim() === '') return true;
  if (Array.isArray(userAns) && userAns.length === 0) return true;
  return false;
}

export function parseAnswerList(ansInput: any): string[] {
  if (ansInput === undefined || ansInput === null) return [];
  if (Array.isArray(ansInput)) return ansInput.map(x => String(x).trim()).filter(Boolean);
  const str = String(ansInput).trim();
  if (!str || str === '[]' || str === '{}') return [];
  if (str.startsWith('[') && str.endsWith(']')) {
    try {
      const parsed = JSON.parse(str);
      if (Array.isArray(parsed)) return parsed.map(x => String(x).trim()).filter(Boolean);
    } catch {}
  }
  if (str.includes(',')) {
    return str.split(',').map(x => x.trim()).filter(Boolean);
  }
  return [str];
}

export function cleanStringForMatch(s: any): string {
  if (s === undefined || s === null) return '';
  return String(s)
    .replace(/\\ce\{([^}]+)\}/g, '$1')
    .replace(/\\(?:text|mathrm|mathbf|mathit|mathsf|mathtt)\{([^}]+)\}/g, '$1')
    .replace(/\\\(|\\\)|\\\[|\\\]|\$+/g, '')       // Strip math delimiter wrappers
    .replace(/[\u2212\u2013\u2014]/g, '-')         // Normalize unicode minus / en-dash / em-dash to ASCII minus
    .replace(/\\times|\\cdot|×/g, '*')
    .replace(/\\div|÷/g, '/')
    .replace(/\\pm/g, '+-')
    .replace(/\\\\/g, '\\')
    .replace(/\s+/g, '')                           // Strip whitespace
    .toLowerCase()
    .trim();
}

export function getQuestionCorrectAnswer(q: any): any {
  if (!q) return null;
  if (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0) return q.correctAnswers;
  if (Array.isArray(q.correctAnswer) && q.correctAnswer.length > 0) return q.correctAnswer;
  if (q.correctAnswer !== undefined && q.correctAnswer !== null && q.correctAnswer !== '') return q.correctAnswer;
  if (q.answer !== undefined && q.answer !== null && q.answer !== '') return q.answer;
  if (q.correct_answer !== undefined && q.correct_answer !== null && q.correct_answer !== '') return q.correct_answer;
  if (q.correctOption !== undefined && q.correctOption !== null && q.correctOption !== '') return q.correctOption;
  return null;
}

export function isOptionSelectedByUser(userAns: any, optKey: string, optIndex: number, optText?: string, allOptions?: any[]): boolean {
  const list = parseAnswerList(userAns);
  if (list.length === 0) return false;
  const charCode = String.fromCharCode(65 + optIndex);
  const cleanKey = cleanStringForMatch(optKey);
  const cleanText = cleanStringForMatch(optText);

  return list.some(item => {
    if (item === undefined || item === null) return false;
    const itemStr = String(item).trim();
    const itemUpper = itemStr.toUpperCase();
    const cleanItem = cleanStringForMatch(itemStr);

    if (itemStr === optKey || (optText && itemStr === optText)) return true;
    if (optKey && String(optKey).toLowerCase() === itemStr.toLowerCase()) return true;
    if (optText && String(optText).toLowerCase() === itemStr.toLowerCase()) return true;
    if (cleanKey && cleanItem === cleanKey) return true;
    if (cleanText && cleanItem === cleanText) return true;

    if (itemUpper === charCode) return true;
    if (optKey && (itemStr.toLowerCase() === 'option_' + charCode.toLowerCase() || itemStr.toLowerCase() === 'option_' + String(optKey).toLowerCase())) return true;

    if (allOptions && Array.isArray(allOptions) && allOptions.length > 0) {
      const normLetter = normalizeOptionAnswer(item, allOptions);
      if (normLetter && normLetter === charCode) return true;
    } else {
      const idxStr = String(optIndex);
      const oneBasedIdxStr = String(optIndex + 1);
      if (itemStr === idxStr || itemStr === oneBasedIdxStr) return true;
      if (itemUpper.length === 1 && itemUpper.charCodeAt(0) - 65 === optIndex) return true;
    }

    return false;
  });
}

export function isOptionCorrect(correctAns: any, optKey: string, optIndex: number, optText?: string, allOptions?: any[]): boolean {
  const list = parseAnswerList(correctAns);
  if (list.length === 0) return false;
  const charCode = String.fromCharCode(65 + optIndex);
  const cleanKey = cleanStringForMatch(optKey);
  const cleanText = cleanStringForMatch(optText);

  return list.some(item => {
    if (item === undefined || item === null) return false;
    const itemStr = String(item).trim();
    const itemUpper = itemStr.toUpperCase();
    const cleanItem = cleanStringForMatch(itemStr);

    if (itemStr === optKey || (optText && itemStr === optText)) return true;
    if (optKey && String(optKey).toLowerCase() === itemStr.toLowerCase()) return true;
    if (optText && String(optText).toLowerCase() === itemStr.toLowerCase()) return true;
    if (cleanKey && cleanItem === cleanKey) return true;
    if (cleanText && cleanItem === cleanText) return true;

    if (itemUpper === charCode) return true;
    if (optKey && (itemStr.toLowerCase() === 'option_' + charCode.toLowerCase() || itemStr.toLowerCase() === 'option_' + String(optKey).toLowerCase())) return true;

    if (allOptions && Array.isArray(allOptions) && allOptions.length > 0) {
      const normLetter = normalizeOptionAnswer(item, allOptions);
      if (normLetter && normLetter === charCode) return true;
    } else {
      const idxStr = String(optIndex);
      const oneBasedIdxStr = String(optIndex + 1);
      if (itemStr === idxStr || itemStr === oneBasedIdxStr) return true;
      if (itemUpper.length === 1 && itemUpper.charCodeAt(0) - 65 === optIndex) return true;
    }

    return false;
  });
}

export function getReasonForQuestion(targetQ: any, scorecard: any): string | null {
  if (!scorecard || !scorecard.wrongAnswerReasons) return null;
  const wrongList = scorecard.questions.filter((x: any) => !x.isCorrect && !isBlank(x.userAnswer));
  const unattemptedList = scorecard.questions.filter((x: any) => isBlank(x.userAnswer));
  
  let globalIndex = -1;
  if (!targetQ.isCorrect && !isBlank(targetQ.userAnswer)) {
    globalIndex = wrongList.findIndex((x: any) => x.questionCode === targetQ.questionCode);
  } else if (isBlank(targetQ.userAnswer)) {
    globalIndex = wrongList.length + unattemptedList.findIndex((x: any) => x.questionCode === targetQ.questionCode);
  }
  
  if (globalIndex !== -1) {
    return scorecard.wrongAnswerReasons[globalIndex] || null;
  }
  return null;
}

export function getRawOptionKey(opt: any): string {
  return (opt && typeof opt === 'object') ? (opt.code || opt.text || '') : String(opt);
}

export function getRawOptionText(opt: any): string {
  return (opt && typeof opt === 'object') ? (opt.text || '') : String(opt);
}

/**
 * Resolves the clean display text for an answer input given an options array.
 * Prioritizes direct text/code matching before considering letter indices or fallbacks.
 */
export function resolveOptionDisplayText(options: any[], answerInput: any): string {
  const list = parseAnswerList(answerInput);
  if (list.length === 0) return '(blank)';
  if (!Array.isArray(options) || options.length === 0) return list.join(', ');

  const matchedTexts: string[] = [];
  list.forEach(item => {
    if (item === undefined || item === null || item === '') return;
    const itemStr = String(item).trim();

    // 1. First priority: Exact match against option text or option code
    const exactOpt = options.find((o: any) => {
      const optText = (o && typeof o === 'object') ? (o.text ?? o.value ?? o.label ?? '') : String(o ?? '');
      const optCode = (o && typeof o === 'object') ? (o.code ?? '') : '';
      return optText === itemStr || (optCode && optCode === itemStr);
    });
    if (exactOpt) {
      const text = (exactOpt && typeof exactOpt === 'object') ? (exactOpt.text ?? exactOpt.value ?? itemStr) : String(exactOpt);
      matchedTexts.push(text);
      return;
    }

    // 2. Second priority: Math-aware normalized match
    const cleanItem = cleanStringForMatch(stripOptionLabel(itemStr));
    const normalizedOpt = options.find((o: any) => {
      const optText = (o && typeof o === 'object') ? (o.text ?? o.value ?? o.label ?? '') : String(o ?? '');
      return cleanItem && cleanStringForMatch(stripOptionLabel(optText)) === cleanItem;
    });
    if (normalizedOpt) {
      const text = (normalizedOpt && typeof normalizedOpt === 'object') ? (normalizedOpt.text ?? normalizedOpt.value ?? itemStr) : String(normalizedOpt);
      matchedTexts.push(text);
      return;
    }

    // 3. Third priority: Explicit letter prefix like "Option A", "A.", "(B)"
    const prefixMatch = itemStr.match(/^(?:option\s+)?\(?([A-Z])\)?[:.\-\s]?$/i);
    if (prefixMatch) {
      const letterIndex = prefixMatch[1].toUpperCase().charCodeAt(0) - 65;
      if (letterIndex >= 0 && letterIndex < options.length) {
        const opt = options[letterIndex];
        const text = (opt && typeof opt === 'object') ? (opt.text ?? opt.value ?? itemStr) : String(opt);
        matchedTexts.push(text);
        return;
      }
    }

    // 4. Fourth priority: Explicit option index like "option_0", "option_1"
    const optionIndexMatch = itemStr.match(/^option_?([0-9]+)$/i);
    if (optionIndexMatch) {
      const idx = parseInt(optionIndexMatch[1], 10);
      if (idx >= 0 && idx < options.length) {
        const opt = options[idx];
        const text = (opt && typeof opt === 'object') ? (opt.text ?? opt.value ?? itemStr) : String(opt);
        matchedTexts.push(text);
        return;
      }
    }

    // Default fallback: return raw item string
    matchedTexts.push(itemStr);
  });

  return matchedTexts.length > 0 ? matchedTexts.join(', ') : '(blank)';
}

export const BLOOM_TAXONOMY_MAP: Record<string, 'Remember' | 'Understand' | 'Apply' | 'Analyze' | 'Evaluate' | 'Create'> = {
  r: 'Remember', remember: 'Remember', Remember: 'Remember',
  u: 'Understand', understand: 'Understand', Understand: 'Understand',
  ap: 'Apply', apply: 'Apply', Apply: 'Apply',
  an: 'Analyze', analyze: 'Analyze', Analyze: 'Analyze',
  e: 'Evaluate', evaluate: 'Evaluate', Evaluate: 'Evaluate',
  c: 'Create', create: 'Create', Create: 'Create'
};

export function normalizeBloomLevel(val: any, difficulty?: string, type?: string): 'Remember' | 'Understand' | 'Apply' | 'Analyze' | 'Evaluate' | 'Create' {
  if (val && typeof val === 'string') {
    const clean = val.trim();
    if (BLOOM_TAXONOMY_MAP[clean]) return BLOOM_TAXONOMY_MAP[clean];
    const lower = clean.toLowerCase();
    if (BLOOM_TAXONOMY_MAP[lower]) return BLOOM_TAXONOMY_MAP[lower];
    if (lower !== 'undefined' && lower !== 'null' && lower !== '') {
      if (lower.startsWith('rememb')) return 'Remember';
      if (lower.startsWith('under')) return 'Understand';
      if (lower.startsWith('appl')) return 'Apply';
      if (lower.startsWith('analy')) return 'Analyze';
      if (lower.startsWith('eval')) return 'Evaluate';
      if (lower.startsWith('creat')) return 'Create';
    }
  }

  // Intelligent derivation based on question type & difficulty if missing/undefined
  const diff = String(difficulty || '').toLowerCase();
  const qtype = String(type || '').toLowerCase();

  if (qtype === 'assertion_reason' || qtype === 'subjective_reason' || qtype === 'scientific_reasoning') return 'Analyze';
  if (qtype === 'numerical' || qtype === 'numerical_short' || qtype === 'numerical_long') return 'Apply';
  if (qtype === 'subjective_define' || qtype === 'subjective_laws' || qtype === 'true_false') return 'Remember';
  if (qtype === 'subjective_long' || qtype === 'hots' || qtype === 'case_study') return diff === 'hard' ? 'Evaluate' : 'Analyze';

  if (diff === 'hard') return 'Analyze';
  if (diff === 'medium') return 'Apply';
  return 'Remember';
}

export function formatUserAnswerSummary(options: any[], userAns: any): string {
  return resolveOptionDisplayText(options, userAns);
}
