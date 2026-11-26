/**
 * Question Similarity & Deduplication Utility
 * Prevents questions that are near-duplicates or differ by only 1-2 words
 * from being included in the same exam.
 */

const STOP_WORDS = new Set([
  'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
  'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
  'to', 'was', 'were', 'will', 'with', 'what', 'which', 'who', 'whom',
  'this', 'these', 'those', 'how', 'why', 'where', 'when', 'can', 'could',
  'should', 'would', 'does', 'did', 'having', 'into', 'each', 'all', 'both',
  'called', 'known', 'named', 'termed', 'defined', 'considered', 'given', 'following'
]);

function normalizeQuestionText(text: string): string {
  if (!text) return '';
  return text
    .replace(/<svg[\s\S]*?<\/svg>/gi, ' ') // Strip embedded SVG diagrams
    .replace(/<[^>]+>/g, ' ')             // Strip HTML tags
    .toLowerCase()
    .replace(/\\([a-zA-Z]+)/g, '$1')          // Keep command names like sin, cos, sqrt, frac
    .replace(/[$_{}\\^~`"']/g, '')         // Remove LaTeX & formatting
    .replace(/[^\w\s]/g, ' ')              // Replace punctuation with space
    .replace(/\s+/g, ' ')                 // Collapse multiple whitespace
    .trim();
}

function normalizeTemplateSkeleton(normText: string): string {
  if (!normText) return '';
  return normText.replace(/\b\d+(?:\.\d+)?\b/g, '#');
}

function extractTokens(text: string, removeStopWords = true): string[] {
  const norm = normalizeQuestionText(text);
  if (!norm) return [];
  const words = norm.split(' ').filter(w => w.length > 0);
  if (!removeStopWords) return words;
  return words.filter(w => !STOP_WORDS.has(w));
}

function levenshtein<T>(a: T[], b: T[]): number {
  const m = a.length;
  const n = b.length;
  if (m === 0) return n;
  if (n === 0) return m;

  const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      dp[i][j] = Math.min(
        dp[i - 1][j] + 1,
        dp[i][j - 1] + 1,
        dp[i - 1][j - 1] + cost
      );
    }
  }

  return dp[m][n];
}

function calculateDiceSimilarity(tokensA: string[], tokensB: string[]): number {
  if (tokensA.length === 0 && tokensB.length === 0) return 1.0;
  if (tokensA.length === 0 || tokensB.length === 0) return 0.0;

  const setA = new Set(tokensA);
  const setB = new Set(tokensB);

  let intersection = 0;
  setA.forEach(w => {
    if (setB.has(w)) intersection++;
  });

  return (2 * intersection) / (tokensA.length + tokensB.length);
}

function calculateWordSequenceSimilarity(wordsA: string[], wordsB: string[]): number {
  if (wordsA.length === 0 && wordsB.length === 0) return 1.0;
  if (wordsA.length === 0 || wordsB.length === 0) return 0.0;

  const maxLen = Math.max(wordsA.length, wordsB.length);
  const dist = levenshtein(wordsA, wordsB);
  return 1 - dist / maxLen;
}

function getQuestionComparableText(q: any): string {
  if (!q) return '';
  if (q.type === 'assertion_reason' || (q.assertion && q.reason)) {
    return `${q.assertion || ''} ${q.reason || ''}`.trim();
  }
  return (q.text || q.questionText || q.question || '').trim();
}

function getResolvedCorrectAnswerText(q: any): string {
  if (!q) return '';
  if (q.correctAnswerText) return q.correctAnswerText.trim().toLowerCase();
  
  // If correctAnswer is letter ('A', 'B', etc.) and options array exists
  const ans = q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : '');
  if (typeof ans === 'string' && ans.length === 1 && ans.toUpperCase() >= 'A' && ans.toUpperCase() <= 'Z' && Array.isArray(q.options)) {
    const idx = ans.toUpperCase().charCodeAt(0) - 65;
    if (idx >= 0 && idx < q.options.length) {
      const opt = q.options[idx];
      return (typeof opt === 'object' ? (opt.text || opt.code || '') : String(opt)).trim().toLowerCase();
    }
  }
  return String(ans || '').trim().toLowerCase();
}

/**
 * Checks if two questions are duplicates or near-identical variants (differing by only 1-2 words).
 */
export function areQuestionsTooSimilar(
  q1: any,
  q2: any
): boolean {
  if (!q1 || !q2) return false;
  if (q1.id && q2.id && q1.id === q2.id) return true;
  if (q1.questionCode && q2.questionCode && q1.questionCode === q2.questionCode) return true;

  const text1 = getQuestionComparableText(q1);
  const text2 = getQuestionComparableText(q2);
  if (!text1 || !text2) return false;

  const norm1 = normalizeQuestionText(text1);
  const norm2 = normalizeQuestionText(text2);

  // 1. Exact normalized text match
  if (norm1 === norm2) return true;

  const fullWords1 = norm1.split(' ').filter(Boolean);
  const fullWords2 = norm2.split(' ').filter(Boolean);
  const wordSeqSim = calculateWordSequenceSimilarity(fullWords1, fullWords2);

  // 1b. Template/loop-based numeric variant check (e.g. "5 pipes... 7 pipes" vs "7 pipes... 9 pipes")
  const skel1 = normalizeTemplateSkeleton(norm1);
  const skel2 = normalizeTemplateSkeleton(norm2);
  if (skel1.includes('#') && skel2.includes('#')) {
    if (skel1 === skel2) return true;
    const skelWords1 = skel1.split(' ').filter(Boolean);
    const skelWords2 = skel2.split(' ').filter(Boolean);
    if (skelWords1.length >= 6 && calculateWordSequenceSimilarity(skelWords1, skelWords2) >= 0.92) {
      return true;
    }
  }

  // Core content word overlap
  const contentTokens1 = extractTokens(text1, true);
  const contentTokens2 = extractTokens(text2, true);
  const diceSim = calculateDiceSimilarity(contentTokens1, contentTokens2);

  // Check if answers are identical or distinct
  const ans1 = getResolvedCorrectAnswerText(q1).trim().toLowerCase();
  const ans2 = getResolvedCorrectAnswerText(q2).trim().toLowerCase();
  const hasBothAnswers = Boolean(ans1 && ans2);
  const words1 = ans1.split(/\s+/).filter(Boolean);
  const words2 = ans2.split(/\s+/).filter(Boolean);
  const isWordSubset = words1.length > 1 && words2.length > 1 && (
    words1.every(w => words2.includes(w)) || words2.every(w => words1.includes(w))
  );
  const sameAnswer = hasBothAnswers && (ans1 === ans2 || isWordSubset);
  const distinctAnswers = hasBothAnswers && !sameAnswer;

  // 2. If answers are provided and distinct (e.g. Xylem = Water vs Phloem = Food)
  if (distinctAnswers) {
    return wordSeqSim >= 0.95;
  }

  // 3. If answers are the same (e.g. Q4 & Q5 both have answer 'Solar radiation')
  if (sameAnswer) {
    return wordSeqSim >= 0.65 || diceSim >= 0.65;
  }

  // 4. If answers are not available (e.g. subjective questions or raw pool)
  if (wordSeqSim >= 0.80 || diceSim >= 0.80) {
    return true;
  }

  return false;
}

/**
 * Filters a pool of candidate questions so that no near-duplicate questions are chosen.
 */
export function filterDistinctCandidates<T>(
  candidates: T[],
  alreadySelected: T[] = []
): T[] {
  const chosen: T[] = [...alreadySelected];
  const distinct: T[] = [];

  for (const c of candidates) {
    const duplicate = chosen.some(sel => areQuestionsTooSimilar(c, sel));
    if (!duplicate) {
      chosen.push(c);
      distinct.push(c);
    }
  }

  return distinct;
}

/**
 * Validates that all questions in a batch/set are mutually distinct and non-plagiarized.
 * Rejects exact normalized text duplicates and near-identical questions.
 */
export function validateBatchDistinctness(questions: any[]): { valid: boolean; errors: string[] } {
  const errors: string[] = [];
  const textMap = new Map<string, string>();

  for (let i = 0; i < questions.length; i++) {
    const qA = questions[i];
    const codeA = qA.questionCode || qA.id || `Item #${i + 1}`;
    const textA = getQuestionComparableText(qA);
    const normA = normalizeQuestionText(textA);

    if (!normA) continue;

    if (textMap.has(normA)) {
      const priorCode = textMap.get(normA);
      errors.push(`Identical question text detected: ${codeA} is a verbatim duplicate of ${priorCode}.`);
      continue;
    }
    textMap.set(normA, codeA);

    for (let j = 0; j < i; j++) {
      const qB = questions[j];
      const codeB = qB.questionCode || qB.id || `Item #${j + 1}`;
      if (areQuestionsTooSimilar(qA, qB)) {
        errors.push(`Near-duplicate question detected: ${codeA} is too similar to ${codeB}. Each question must test a distinct scenario.`);
        break;
      }
    }
  }

  return { valid: errors.length === 0, errors };
}

