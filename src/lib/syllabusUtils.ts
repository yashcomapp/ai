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
