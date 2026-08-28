
export function stripOptionLabel(text: any): string {
  if (text == null) return '';
  return String(text).replace(/^\s*\(?[A-Da-d]\)?[).:]\s*/, '');
}

export function preprocessMathText(text: any): string {
  if (text == null) return '';
  let str = String(text);

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

  return str;
}

export function formatRichText(text: any): string {
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

  return str;
}


export function normalizeOptionAnswer(value: any, options?: any[]): string {
  if (!value && value !== 0) return '';
  value = String(value).trim();

  if (Array.isArray(options) && options.length) {
    const letterMatch = value.match(/^([A-Z])$/i);
    if (letterMatch) {
      const idx = letterMatch[1].toUpperCase().charCodeAt(0) - 65;
      if (idx >= 0 && idx < options.length) return letterMatch[1].toUpperCase();
    }
    const norm = (s: any) => String(s ?? '').trim().toLowerCase();
    const idx = options.findIndex(opt => {
      const optText = (opt && typeof opt === 'object') ? (opt.text ?? opt.value ?? '') : opt;
      return norm(optText) === norm(value);
    });
    if (idx !== -1) return String.fromCharCode(65 + idx);
  }

  const match = value.match(/^([A-D])/i);
  if (match) {
    return match[1].toUpperCase();
  }

  return value.toUpperCase();
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
  // If options are provided and non-empty, and it's not a multi-mcq, true_false, or assertion_reason, check option match
  if (Array.isArray(options) && options.length > 0 && type !== 'multiple_mcq' && type !== 'multi_mcq' && type !== 'true_false' && type !== 'assertion_reason') {
    const userNorm = normalizeOptionAnswer(userAnswer, options);
    const correctNorm = normalizeOptionAnswer(correctAnswer, options);
    if (userNorm && correctNorm && userNorm === correctNorm) return true;
  }

  if (type === 'single_mcq' || type === 'mcq') {
    return normalizeOptionAnswer(userAnswer, options) === normalizeOptionAnswer(correctAnswer, options);
  }

  if (type === 'multiple_mcq' || type === 'multi_mcq') {
    let userArr: any = [];
    try {
      userArr = JSON.parse(userAnswer);
    } catch {
      userArr = userAnswer;
    }
    if (!Array.isArray(userArr)) {
      userArr = userArr ? [userArr] : [];
    }

    let correctArr = Array.isArray(correctAnswer)
      ? correctAnswer
      : (correctAnswer ? [correctAnswer] : []);

    userArr = Array.from(new Set(userArr.map((v: any) => normalizeOptionAnswer(v, options)))).sort();
    correctArr = Array.from(new Set(correctArr.map((v: any) => normalizeOptionAnswer(v, options)))).sort();

    return JSON.stringify(userArr) === JSON.stringify(correctArr);
  }

  if (type === 'true_false') {
    const userNorm = String(userAnswer || '').trim().toLowerCase();
    const correctNorm = String(correctAnswer || '').trim().toLowerCase();
    return userNorm === correctNorm;
  }

  if (type === 'assertion_reason') {
    return classifyAssertionReasonAnswer(userAnswer) === classifyAssertionReasonAnswer(correctAnswer);
  }

  if (type === 'fill_blanks' || type === 'fill_blank') {
    return String(userAnswer || '').trim().toLowerCase() === String(correctAnswer || '').trim().toLowerCase();
  }

  if (type === 'numerical' || type === 'numerical_short' || type === 'numerical_long') {
    if (Array.isArray(options) && options.length > 0) {
      if (normalizeOptionAnswer(userAnswer, options) === normalizeOptionAnswer(correctAnswer, options)) {
        return true;
      }
    }
    const u = parseFloat(userAnswer);
    const c = parseFloat(correctAnswer);
    return !isNaN(u) && !isNaN(c) && Math.abs(u - c) <= 0.05; // 0.05 tolerance
  }

  // Subjective types have no auto grading
  return false;
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

export const QUESTION_TYPE_MAP: { [key: string]: { id: string; label: string; code: string; category: 'objective' | 'subjective'; defaultMarks: number } } = {
  single_mcq: { id: 'single_mcq', label: 'Single MCQ', code: 'OSC', category: 'objective', defaultMarks: 4 },
  multiple_mcq: { id: 'multiple_mcq', label: 'Multiple MCQ', code: 'OMC', category: 'objective', defaultMarks: 4 },
  true_false: { id: 'true_false', label: 'True/False', code: 'OTF', category: 'objective', defaultMarks: 4 },
  assertion_reason: { id: 'assertion_reason', label: 'Assertion-Reason', code: 'OAR', category: 'objective', defaultMarks: 4 },
  fill_blanks: { id: 'fill_blanks', label: 'Fill Blanks', code: 'OFB', category: 'objective', defaultMarks: 4 },
  numerical: { id: 'numerical', label: 'Numerical (Obj)', code: 'ONE', category: 'objective', defaultMarks: 4 },
  numerical_short: { id: 'numerical_short', label: 'Num Short (2m)', code: 'SSN', category: 'subjective', defaultMarks: 2 },
  numerical_long: { id: 'numerical_long', label: 'Num Long (4m)', code: 'SLN', category: 'subjective', defaultMarks: 4 },
  subjective_short: { id: 'subjective_short', label: 'Sub Short (2m)', code: 'SSA', category: 'subjective', defaultMarks: 2 },
  subjective_long: { id: 'subjective_long', label: 'Sub Long (4m)', code: 'SLA', category: 'subjective', defaultMarks: 4 },
  subjective_reason: { id: 'subjective_reason', label: 'Sci Reasoning (2m)', code: 'SSR', category: 'subjective', defaultMarks: 2 },
  subjective_notes: { id: 'subjective_notes', label: 'Notes (2m)', code: 'SSR', category: 'subjective', defaultMarks: 2 },
  subjective_define: { id: 'subjective_define', label: 'Define (1m)', code: 'SDF', category: 'subjective', defaultMarks: 1 },
  subjective_laws: { id: 'subjective_laws', label: 'Laws (1m)', code: 'SLP', category: 'subjective', defaultMarks: 1 },
};

export const OBJECTIVE_QUESTION_TYPES = [
  { id: 'single_mcq', label: 'Single MCQ', code: 'OSC' },
  { id: 'multiple_mcq', label: 'Multiple MCQ', code: 'OMC' },
  { id: 'true_false', label: 'True/False', code: 'OTF' },
  { id: 'assertion_reason', label: 'Assertion-Reason', code: 'OAR' },
  { id: 'fill_blanks', label: 'Fill Blanks', code: 'OFB' },
  { id: 'numerical', label: 'Numerical (Obj)', code: 'ONE' }
];

export const SUBJECTIVE_QUESTION_TYPES = [
  { id: 'numerical_short', label: 'Num Short (2m)', code: 'SSN' },
  { id: 'numerical_long', label: 'Num Long (4m)', code: 'SLN' },
  { id: 'subjective_short', label: 'Sub Short (2m)', code: 'SSA' },
  { id: 'subjective_long', label: 'Sub Long (4m)', code: 'SLA' },
  { id: 'subjective_reason', label: 'Sci Reasoning (2m)', code: 'SSR' },
  { id: 'subjective_notes', label: 'Notes (2m)', code: 'SSR' },
  { id: 'subjective_define', label: 'Define (1m)', code: 'SDF' },
  { id: 'subjective_laws', label: 'Laws (1m)', code: 'SLP' }
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
      if (nextChar === '"' || nextChar === '\\') {
        escapedStr += '\\' + nextChar;
        i++; // skip next char
      } else if (nextChar === 'n') {
        escapedStr += '\\n';
        i++;
      } else if (nextChar === 't') {
        escapedStr += '\\t';
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
      if (nextChar === '"' || nextChar === '\\') {
        escapedStr += '\\' + nextChar;
        i++;
      } else if (nextChar === 'n') {
        escapedStr += '\\n';
        i++;
      } else if (nextChar === 't') {
        escapedStr += '\\t';
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

export function validateQuestion(q: any, questionType: 'objective' | 'subjective' | 'all_in_one'): string[] {
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
  const type = q.type || q.qtype || '';
  const isSubjective = questionType === 'subjective' || 
    (questionType === 'all_in_one' && (QUESTION_TYPE_MAP[type]?.category === 'subjective' || (q.marks && !q.options?.length && q.type !== 'numerical')));

  if (!isSubjective) {
    if (type === 'single_mcq' || type === 'true_false') {
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

        const isMatched = q.options.some((opt: any) => 
          normalizeOptionText(opt) === normalizeOptionText(q.correctAnswer) ||
          cleanStringForMatch(opt) === cleanStringForMatch(q.correctAnswer)
        );
        if (!isMatched) {
          errors.push('Correct answer does not match any items in options list.');
        }
      }
    } else if (type === 'multiple_mcq') {
      if (!q.correctAnswers || !Array.isArray(q.correctAnswers) || q.correctAnswers.length === 0) {
        errors.push('Missing correctAnswers list.');
      } else if (Array.isArray(q.options) && q.options.length > 0) {
        q.correctAnswers.forEach((ans: any) => {
          const isMatched = q.options.some((opt: any) => 
            normalizeOptionText(opt) === normalizeOptionText(ans) ||
            cleanStringForMatch(opt) === cleanStringForMatch(ans)
          );
          if (!isMatched) {
            errors.push(`Correct answer "${ans}" not found in options list.`);
          }
        });
      }
    } else if (type === 'assertion_reason') {
      const correctNorm = String(q.correctAnswer || '').trim().toUpperCase();
      if (!['A', 'B', 'C', 'D'].includes(correctNorm)) {
        errors.push('Correct answer for Assertion-Reason must be A, B, C, or D.');
      }
    } else if (type === 'numerical') {
      if (!q.correctAnswer || isNaN(parseFloat(String(q.correctAnswer)))) {
        errors.push('Numerical questions must specify a valid numeric correct answer (e.g. "42" or "3.14").');
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
  return String(s || '')
    .toLowerCase()
    .replace(/\\ce\{([^}]+)\}/g, '$1')
    .replace(/\\\(|\\\)|\\\[|\\\]|\$+/g, '')
    .replace(/[^\w\d]/g, '')
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

export function isOptionSelectedByUser(userAns: any, optKey: string, optIndex: number, optText?: string): boolean {
  const list = parseAnswerList(userAns);
  if (list.length === 0) return false;
  const charCode = String.fromCharCode(65 + optIndex);
  const idxStr = String(optIndex);
  const oneBasedIdxStr = String(optIndex + 1);
  const cleanKey = cleanStringForMatch(optKey);
  const cleanText = cleanStringForMatch(optText);

  return list.some(item => {
    if (item === undefined || item === null) return false;
    const itemStr = String(item).trim();
    const itemUpper = itemStr.toUpperCase();
    const itemLower = itemStr.toLowerCase();
    const cleanItem = cleanStringForMatch(itemStr);

    return (
      itemStr === optKey ||
      itemLower === String(optKey || '').toLowerCase() ||
      (cleanKey && cleanItem === cleanKey) ||
      (optText && (itemStr === optText || itemLower === String(optText || '').toLowerCase())) ||
      (cleanText && cleanItem === cleanText) ||
      itemStr === idxStr ||
      itemStr === oneBasedIdxStr ||
      itemUpper === charCode ||
      (itemUpper.length === 1 && itemUpper.charCodeAt(0) - 65 === optIndex) ||
      (optKey && (itemLower === `option_${String(optKey).toLowerCase()}` || itemLower === `option_${charCode.toLowerCase()}`))
    );
  });
}

export function isOptionCorrect(correctAns: any, optKey: string, optIndex: number, optText?: string): boolean {
  const list = parseAnswerList(correctAns);
  if (list.length === 0) return false;
  const charCode = String.fromCharCode(65 + optIndex);
  const idxStr = String(optIndex);
  const oneBasedIdxStr = String(optIndex + 1);
  const cleanKey = cleanStringForMatch(optKey);
  const cleanText = cleanStringForMatch(optText);

  return list.some(item => {
    if (item === undefined || item === null) return false;
    const itemStr = String(item).trim();
    const itemUpper = itemStr.toUpperCase();
    const itemLower = itemStr.toLowerCase();
    const cleanItem = cleanStringForMatch(itemStr);

    return (
      itemStr === optKey ||
      itemLower === String(optKey || '').toLowerCase() ||
      (cleanKey && cleanItem === cleanKey) ||
      (optText && (itemStr === optText || itemLower === String(optText || '').toLowerCase())) ||
      (cleanText && cleanItem === cleanText) ||
      itemStr === idxStr ||
      itemStr === oneBasedIdxStr ||
      itemUpper === charCode ||
      (itemUpper.length === 1 && itemUpper.charCodeAt(0) - 65 === optIndex) ||
      (optKey && (itemLower === `option_${String(optKey).toLowerCase()}` || itemLower === `option_${charCode.toLowerCase()}`))
    );
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
  const list = parseAnswerList(userAns);
  if (list.length === 0) return '(blank)';
  if (!options || !Array.isArray(options) || options.length === 0) return list.join(', ');

  const matchedTexts: string[] = [];
  list.forEach(item => {
    let foundText = '';
    if (item.length === 1 && item.toUpperCase() >= 'A' && item.toUpperCase() <= 'Z') {
      const codeIndex = item.toUpperCase().charCodeAt(0) - 65;
      if (codeIndex >= 0 && codeIndex < options.length) {
        const optVal = options[codeIndex];
        foundText = (optVal && typeof optVal === 'object') ? ((optVal as any).text || (optVal as any).code || item) : String(optVal);
      }
    }
    if (!foundText && /^\d+$/.test(item)) {
      const codeIndex = parseInt(item, 10);
      if (codeIndex >= 0 && codeIndex < options.length) {
        const optVal = options[codeIndex];
        foundText = (optVal && typeof optVal === 'object') ? ((optVal as any).text || (optVal as any).code || item) : String(optVal);
      }
    }
    if (!foundText) {
      const opt = options.find((o: any) => {
        if (o && typeof o === 'object') return o.code === item || o.text === item;
        return String(o) === item;
      });
      if (opt) {
        foundText = (opt && typeof opt === 'object') ? ((opt as any).text || (opt as any).code || item) : String(opt);
      }
    }
    matchedTexts.push(foundText || item);
  });

  return matchedTexts.join(', ');
}
