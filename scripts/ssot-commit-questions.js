// scripts/ssot-commit-questions.js
// Foolproof SSOT Question Bank Committer & Guardrail Gate
// Usage: node scripts/ssot-commit-questions.js <path-to-questions.json> [--dry-run]
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const { adminDb } = require('../src/lib/firebase/admin.ts');
const { areQuestionsTooSimilar, validateBatchDistinctness } = require('../src/lib/questionSimilarity.ts');
const { toCanonicalQuestionType, stripCitations, canonicalizeQuestionAnswers, validateQuestion } = require('../src/lib/questionTypes.ts');
const { validateQuestionCurriculum } = require('../src/lib/curriculumGuard.ts');
const { syncTopicCountsToSyllabus } = require('../src/lib/syllabusSync.ts');

const PLACEHOLDER_REGEX = /\b(todo|tbd|placeholder|lorem ipsum|sample question|dummy question|test question|coming soon|insert text)\b/i;
const BAD_TEMPLATE_REGEX = /(recall the established principles|scientifically accurate conclusion when|identify the scientifically verified fact concerning|which principle governs .+ regarding|accurately applied when|correct scientific outcome is|in maharashtra state board class \d+|in balbharti class \d+)/i;

async function commitQuestionsFoolproof(questions, { dryRun = false, sourceLabel = 'manual' } = {}) {
  if (!Array.isArray(questions) || questions.length === 0) {
    throw new Error('Empty or invalid questions array.');
  }

  console.log(`\n=== FOOLPROOF SSOT QUESTION GATE (${dryRun ? 'DRY RUN' : 'LIVE'}) ===`);
  console.log(`Incoming batch size: ${questions.length} (${sourceLabel})`);

  // 1. Placeholder & structural sanity check
  const errors = [];
  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const text = String(q.text || q.assertion || '').trim();
    if (!text || text.length < 15) {
      errors.push(`#${i + 1} (${q.questionCode || '?'}): Missing or too-short question text.`);
      continue;
    }
    if (PLACEHOLDER_REGEX.test(text) || PLACEHOLDER_REGEX.test(String(q.solution || ''))) {
      errors.push(`#${i + 1} (${q.questionCode || '?'}): Placeholder text detected.`);
      continue;
    }
    if (BAD_TEMPLATE_REGEX.test(text) || BAD_TEMPLATE_REGEX.test(String(q.solution || q.explanation || ''))) {
      errors.push(`#${i + 1} (${q.questionCode || '?'}): Prohibited synthetic template/board-prefix wording detected.`);
      continue;
    }
    if (!q.topicCode || !q.boardCode || !q.class || !q.subjectCode) {
      errors.push(`#${i + 1}: Missing canonical topicCode/boardCode/class/subjectCode.`);
      continue;
    }

    const typeCode = toCanonicalQuestionType(q.type || 'OSC');
    const isObjective = !['SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'].includes(typeCode);
    const { correctAnswer, correctAnswers } = canonicalizeQuestionAnswers({ ...q, type: typeCode });
    const normalizedQ = {
      ...q,
      type: typeCode,
      text: stripCitations(text),
      solution: stripCitations(q.solution || q.explanation || ''),
      correctAnswer,
      correctAnswers
    };

    const valErrs = validateQuestion(normalizedQ, isObjective ? 'objective' : 'subjective');
    if (valErrs.length > 0) {
      errors.push(`#${i + 1} (${q.questionCode || q.topicCode}): ${valErrs.join('; ')}`);
    }

    const currErrs = validateQuestionCurriculum({
      ...normalizedQ,
      type: typeCode,
      chapterName: q.chapterName || q.chapterTitle || q.topicName || q.topic || ''
    });
    if (!currErrs.valid) {
      errors.push(`#${i + 1} (${q.questionCode || q.topicCode}): Curriculum guard: ${currErrs.errors.join('; ')}`);
    }

    // Check SVG figure integrity if <svg is present
    if (text.includes('<svg') && !text.includes('</svg>')) {
      errors.push(`#${i + 1} (${q.questionCode || q.topicCode}): Unclosed <svg> tag.`);
    }
  }

  if (errors.length > 0) {
    throw new Error(`Structural/Validation failures (${errors.length}):\n  - ${errors.slice(0, 10).join('\n  - ')}`);
  }

  // 2. Intra-batch distinctness (catches exact, near-duplicate, and numeric-loop templates)
  const batchCheck = validateBatchDistinctness(questions);
  if (!batchCheck.valid) {
    throw new Error(`Intra-batch Deduplication Violation (${batchCheck.errors.length}):\n  - ${batchCheck.errors.slice(0, 10).join('\n  - ')}`);
  }

  // 3. Database distinctness against existing questions in the same topicCodes
  const topicCodes = Array.from(new Set(questions.map(q => q.topicCode)));
  const existingByTopic = new Map();
  for (let i = 0; i < topicCodes.length; i += 10) {
    const chunk = topicCodes.slice(i, i + 10);
    const snap = await adminDb.collection('questions')
      .where('topicCode', 'in', chunk)
      .select('questionCode', 'text', 'assertion', 'reason', 'type', 'options', 'correctAnswer', 'correctAnswers', 'topicCode')
      .get();
    for (const d of snap.docs) {
      const data = d.data();
      const tc = data.topicCode || '';
      if (!existingByTopic.has(tc)) existingByTopic.set(tc, []);
      existingByTopic.get(tc).push({ id: d.id, ...data });
    }
  }

  const dbDupErrors = [];
  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const existing = existingByTopic.get(q.topicCode) || [];
    const match = existing.find(ex => areQuestionsTooSimilar(q, ex));
    if (match) {
      dbDupErrors.push(`#${i + 1} (${q.topicCode}) collides with existing ${match.questionCode || match.id}`);
    }
  }
  if (dbDupErrors.length > 0) {
    throw new Error(`Database Deduplication Violation (${dbDupErrors.length}):\n  - ${dbDupErrors.slice(0, 10).join('\n  - ')}`);
  }

  console.log('All structural, curriculum, anti-placeholder, intra-batch, and DB deduplication checks PASSED.');
  if (dryRun) {
    console.log('Dry run complete. 0 writes performed.');
    return { committed: 0 };
  }

  // 4. Allocate canonical sequence numbers transactionally via questionCounters
  const counterNeeds = {};
  for (const q of questions) {
    const typeCode = toCanonicalQuestionType(q.type || 'OSC');
    const cid = `${q.topicCode}-${typeCode}`;
    counterNeeds[cid] = (counterNeeds[cid] || 0) + 1;
  }

  const startSeqMap = {};
  const cids = Object.keys(counterNeeds);
  for (let i = 0; i < cids.length; i += 50) {
    const chunkCids = cids.slice(i, i + 50);
    await adminDb.runTransaction(async (tx) => {
      const refs = chunkCids.map(cid => adminDb.collection('questionCounters').doc(cid));
      const snaps = await tx.getAll(...refs);
      for (const s of snaps) {
        const current = s.exists && s.data() ? (s.data().nextSequence || 1) : 1;
        startSeqMap[s.id] = current;
        tx.set(s.ref, { nextSequence: current + counterNeeds[s.id] }, { merge: true });
      }
    });
  }

  // 5. Rule Q Pre-Mutation Snapshot
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_ssot_commit_${sourceLabel.replace(/[^a-zA-Z0-9_-]/g, '_')}`;
  const snapshotFile = path.join(targetDir, `${snapshotId}.json`);
  fs.writeFileSync(snapshotFile, JSON.stringify({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q backup before committing ${questions.length} validated questions (${sourceLabel})`,
    topicCodes,
    count: questions.length
  }, null, 2));
  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q backup before committing ${questions.length} validated questions (${sourceLabel})`,
    count: questions.length,
    snapshotFile
  });

  // 6. Commit in batches of 400
  const seqOffset = { ...startSeqMap };
  let committed = 0;
  for (let i = 0; i < questions.length; i += 400) {
    const chunk = questions.slice(i, i + 400);
    const batch = adminDb.batch();
    for (const q of chunk) {
      const typeCode = toCanonicalQuestionType(q.type || 'OSC');
      const cid = `${q.topicCode}-${typeCode}`;
      const seq = seqOffset[cid]++;
      const qCode = `${cid}-${String(seq).padStart(3, '0')}`;
      const docRef = adminDb.collection('questions').doc(qCode);
      batch.set(docRef, {
        ...q,
        type: typeCode,
        questionCode: qCode,
        timesUsed: 0,
        createdBy: 'ssot-committer@yashcom.com',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
      });
    }
    await batch.commit();
    committed += chunk.length;
    console.log(`Committed ${committed} / ${questions.length}...`);
  }

  // 7. Sync syllabus counts
  for (let i = 0; i < topicCodes.length; i += 100) {
    await syncTopicCountsToSyllabus(topicCodes.slice(i, i + 100));
  }
  console.log(`Synced syllabus counts for ${topicCodes.length} topics.`);
  return { committed };
}

if (require.main === module) {
  const fileArg = process.argv[2];
  const dryRun = process.argv.includes('--dry-run');
  if (!fileArg || !fs.existsSync(fileArg)) {
    console.error('Usage: node scripts/ssot-commit-questions.js <questions.json> [--dry-run]');
    process.exit(1);
  }
  const data = JSON.parse(fs.readFileSync(fileArg, 'utf8'));
  const label = path.basename(fileArg, '.json');
  commitQuestionsFoolproof(data, { dryRun, sourceLabel: label })
    .then(() => process.exit(0))
    .catch(err => {
      console.error('COMMIT REJECTED:', err.message);
      process.exit(1);
    });
}

module.exports = { commitQuestionsFoolproof };
