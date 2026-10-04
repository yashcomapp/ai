/**
 * Canonical topic equality comparison that prevents duplicate topics / subtopic key mismatches.
 */
export function isSameTopic(a: any, b: any): boolean {
  if (!a || !b) return false;
  if (a.subject && b.subject && a.subject !== b.subject) return false;
  if (a.chapterNumber && b.chapterNumber && String(a.chapterNumber) !== String(b.chapterNumber)) return false;

  // 1. Topic code exact match
  if (a.topicCode && b.topicCode && a.topicCode === b.topicCode) return true;

  // 2. Topic number exact match
  if (a.topicNumber && b.topicNumber && a.topicNumber === b.topicNumber) return true;

  // 3. Topic label exact match
  if (a.topic && b.topic && a.topic === b.topic) return true;

  // 4. Normalized topic name match (ignoring leading digits like "8.1.1 Reactivity..." vs "Reactivity...")
  const normA = (a.topicName || a.topic || '').replace(/^[\d.]+\s*/, '').trim().toLowerCase();
  const normB = (b.topicName || b.topic || '').replace(/^[\d.]+\s*/, '').trim().toLowerCase();
  if (normA && normB && normA === normB) return true;

  return false;
}

export function distributeCountsByWeight(
  totalQs: number,
  selectedTopics: any[],
  topicWeights: Record<string, number>,
  topicWeightMode: 'equal' | 'custom',
  getTopicKey: (topic: any) => string
): Record<string, number> {
  const n = selectedTopics.length;
  if (n === 0 || totalQs <= 0) return {};
  const eq = Math.floor(100 / n);
  const weights = selectedTopics.map(t => {
    if (topicWeightMode === 'equal') return eq;
    const key = getTopicKey(t);
    const w = topicWeights[key];
    return w !== undefined ? w : eq;
  });
  const totalW = weights.reduce((a, b) => a + b, 0) || 1;
  const raw = weights.map(w => (w / totalW) * totalQs);
  const counts = raw.map(Math.floor);
  let remainder = totalQs - counts.reduce((a, b) => a + b, 0);

  const order = raw.map((r, i) => ({ i, frac: r - Math.floor(r) }));
  order.sort((a, b) => b.frac - a.frac);
  for (let i = 0; i < remainder; i++) {
    const idx = order[i % n].i;
    counts[idx]++;
  }

  const result: Record<string, number> = {};
  selectedTopics.forEach((t, idx) => {
    result[getTopicKey(t)] = counts[idx];
  });
  return result;
}

export function buildObjectiveSchema(Schema: any, typeIds: string[]) {
  const DIFFICULTY_ENUM = ['easy', 'medium', 'hard'];
  const BLOOM_ENUM = ['Remember', 'Understand', 'Apply', 'Analyze', 'Evaluate', 'Create'];

  return Schema.array({
    items: Schema.object({
      properties: {
        contextId: Schema.string(),
        type: Schema.enumString({ enum: typeIds.length ? typeIds : ['single_mcq'] }),
        text: Schema.string(),
        options: Schema.array({ items: Schema.string() }),
        correctAnswer: Schema.string({ description: 'Verbatim correct answer string matching options exactly' }),
        correctAnswers: Schema.array({ items: Schema.string({ description: 'Verbatim correct answer strings matching options' }) }),
        assertion: Schema.string(),
        reason: Schema.string(),
        solution: Schema.string(),
        difficulty: Schema.enumString({ enum: DIFFICULTY_ENUM }),
        bloomLevel: Schema.enumString({ enum: BLOOM_ENUM }),
        topicOrigin: Schema.string(),
      },
      optionalProperties: ['options', 'correctAnswer', 'correctAnswers', 'assertion', 'reason', 'topicOrigin'],
    }),
  });
}

/**
 * SSOT Canonical Board Code Standard (Rule 2L & 2R)
 */
export function getCanonicalBoardCode(board: any): 'CBSE' | 'MH' {
  const b = String(board || '').toUpperCase();
  if (b.includes('CBSE')) return 'CBSE';
  return 'MH';
}

/**
 * SSOT Canonical Board Full Name Standard
 */
export function getCanonicalBoardName(board: any): 'CBSE' | 'Maharashtra Board' {
  const code = getCanonicalBoardCode(board);
  return code === 'CBSE' ? 'CBSE' : 'Maharashtra Board';
}

/**
 * SSOT Canonical Class String Standard ('8', '9', '10')
 */
export function getCanonicalClass(classNum: any): string {
  const clean = String(classNum || '8').replace(/\D/g, '');
  return clean || '8';
}

/**
 * SSOT Canonical Subject Code Standard (Rule 2L & 2R)
 */
export function getCanonicalSubjectCode(board: any, classNum: any, subjectNameOrCode: any): string {
  const bCode = getCanonicalBoardCode(board);
  const cls = getCanonicalClass(classNum);
  const upper = String(subjectNameOrCode || '').trim().toUpperCase();

  // 1. Direct match on known canonical subject codes
  if (bCode === 'CBSE') {
    if (cls === '8' && (upper === 'MGP1' || upper === 'MGP2' || upper === 'CURI')) return upper;
    if (cls === '9' && (upper === 'MGM' || upper === 'SCIE')) return upper;
    if (cls === '10' && (upper === 'MATH' || upper === 'SCI')) return upper;
  } else if (bCode === 'MH') {
    if (cls === '8' && (upper === 'MTH' || upper === 'SCI')) return upper;
    if (cls === '9' && (upper === 'MTH1' || upper === 'MTH2' || upper === 'SCIT')) return upper;
    if (cls === '10' && (upper === 'MTH1' || upper === 'MTH2' || upper === 'SCIT1' || upper === 'SCIT2')) return upper;
  }

  // 2. Normalized lowercase alphanumeric matching
  const s = String(subjectNameOrCode || '').toLowerCase().replace(/[\s\-_():]+/g, '');

  if (bCode === 'CBSE') {
    if (cls === '8') {
      if (s.includes('mgp2') || s.includes('part2') || s.includes('p2') || s.includes('2')) return 'MGP2';
      if (s.includes('curi') || s.includes('sci')) return 'CURI';
      return 'MGP1';
    }
    if (cls === '9') {
      if (s.includes('sci') || s.includes('scie') || s.includes('exploration')) return 'SCIE';
      return 'MGM';
    }
    if (cls === '10') {
      if (s.includes('sci')) return 'SCI';
      return 'MATH';
    }
  }

  // MH (Maharashtra Board)
  if (cls === '8') {
    if (s.includes('sci')) return 'SCI';
    return 'MTH';
  }
  if (cls === '9') {
    if (s.includes('sci') || s.includes('scit')) return 'SCIT';
    if (s.includes('geometry') || s.includes('mth2') || s.includes('part2') || s.includes('2')) return 'MTH2';
    return 'MTH1';
  }
  if (cls === '10') {
    if (s.includes('sci') || s.includes('technology') || s.includes('scit')) {
      if (s.includes('2') || s.includes('part2') || s.includes('scit2')) return 'SCIT2';
      return 'SCIT1';
    }
    if (s.includes('geometry') || s.includes('mth2') || s.includes('part2') || s.includes('2')) return 'MTH2';
    return 'MTH1';
  }

  return 'MTH';
}


/**
 * Extracts true chapter number from topicNumber prefix if present (e.g. "4.1.1" -> "4", "13.2" -> "13")
 */
export function extractChapterFromTopic(topicNumber: any, fallbackChapter?: any): string {
  const tStr = String(topicNumber || '').trim();
  const match = tStr.match(/^(\d+)\./);
  if (match && match[1]) {
    return match[1];
  }
  const cleanFb = String(fallbackChapter || '1').replace(/\D/g, '');
  return cleanFb || '1';
}

/**
 * SSOT Canonical Topic Code Standard: `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}`
 */
export function getCanonicalTopicCode(
  board: any,
  classNum: any,
  subjectNameOrCode: any,
  chapterNumber: any,
  topicNumber: any
): string {
  const bCode = getCanonicalBoardCode(board);
  const cls = getCanonicalClass(classNum);
  const sCode = getCanonicalSubjectCode(board, classNum, subjectNameOrCode);
  let tNum = String(topicNumber || '1.1').trim();
  const chNum = extractChapterFromTopic(tNum, chapterNumber);
  if (!tNum.includes('.')) {
    tNum = `${chNum}.${tNum}`;
  }
  return `${bCode}-${cls}-${sCode}-${chNum}-${tNum}`;
}

/**
 * SSOT Canonical Question Code Standard: `${topicCode}-${typeCode}-${sequence}`
 */
export function getCanonicalQuestionCode(
  topicCode: string,
  typeCode: string,
  sequence: number | string
): string {
  const seqStr = String(sequence || '1').padStart(3, '0').slice(-3);
  return `${topicCode}-${typeCode}-${seqStr}`;
}

