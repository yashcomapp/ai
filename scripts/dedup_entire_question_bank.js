// scripts/dedup_entire_question_bank.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const { adminDb } = require('../src/lib/firebase/admin.ts');
const { areQuestionsTooSimilar } = require('../src/lib/questionSimilarity.ts');
const { syncTopicCountsToSyllabus } = require('../src/lib/syllabusSync.ts');

const DRY_RUN = process.argv.includes('--dry-run');

function vaultRank(vault) {
  const v = String(vault || 'practice').toLowerCase();
  if (v === 'exam' || v === 'standard') return 0;
  if (v === 'practice') return 1;
  if (v === 'foundation' || v === 'mock') return 2;
  return 3;
}

async function commitWithRetry(batch, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await batch.commit();
      return;
    } catch (err) {
      console.warn(`  Batch commit attempt ${attempt} failed: ${err.message}`);
      if (attempt === retries) throw err;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
}

async function run() {
  console.log(`=== FULL QUESTION BANK DEDUPLICATION (${DRY_RUN ? 'DRY RUN' : 'LIVE'}) ===`);

  // 1. Collect all question IDs/codes referenced in existing exams so we prioritize keeping them
  const usedInExamsSet = new Set();
  const [objExamsSnap, subjExamsSnap] = await Promise.all([
    adminDb.collection('exams').select('questionCodes', 'questionIds', 'questions').get(),
    adminDb.collection('subjectiveExams').select('questionCodes', 'questionIds', 'questions').get()
  ]);

  for (const doc of [...objExamsSnap.docs, ...subjExamsSnap.docs]) {
    const edata = doc.data();
    const codes = edata.questionCodes || edata.questionIds || [];
    for (const c of codes) if (c) usedInExamsSet.add(String(c).trim());
    if (Array.isArray(edata.questions)) {
      for (const q of edata.questions) {
        if (q?.id) usedInExamsSet.add(String(q.id).trim());
        if (q?.questionCode) usedInExamsSet.add(String(q.questionCode).trim());
      }
    }
  }
  console.log(`Referenced question codes/IDs in existing exams: ${usedInExamsSet.size}`);

  // 2. Fetch all questions in paginated chunks of 10,000 for fast, reliable gRPC streaming
  console.log('Fetching question metadata & text from Firestore in chunks of 10,000...');
  const allDocs = [];
  let lastDoc = null;
  while (true) {
    let q = adminDb.collection('questions')
      .select('questionCode', 'boardCode', 'class', 'subjectCode', 'topicCode', 'vault', 'usedInClassroomTest', 'text', 'assertion', 'reason', 'type', 'correctAnswer', 'correctAnswers')
      .orderBy('__name__')
      .limit(10000);
    if (lastDoc) q = q.startAfter(lastDoc);
    const page = await q.get();
    if (page.empty) break;
    allDocs.push(...page.docs);
    lastDoc = page.docs[page.docs.length - 1];
    console.log(`  Fetched ${allDocs.length} questions...`);
    if (page.size < 10000) break;
  }
  const snap = { size: allDocs.length, docs: allDocs };
  console.log(`Total questions fetched: ${snap.size}`);

  // Group by topicCode (fallback to boardCode-class-subjectCode)
  const byTopic = new Map();
  for (const doc of snap.docs) {
    const data = doc.data();
    const key = data.topicCode || `${data.boardCode || '?'}-${data.class || '?'}-${data.subjectCode || '?'}`;
    if (!byTopic.has(key)) byTopic.set(key, []);
    byTopic.get(key).push({ id: doc.id, ...data });
  }
  console.log(`Grouped into ${byTopic.size} topic buckets.`);

  const toDelete = [];
  const affectedTopicCodes = new Set();
  const subjectStats = new Map();

  for (const [topicKey, list] of byTopic.entries()) {
    // Sort so we keep the highest-value canonical question first:
    // 1. Used in an existing exam or classroom test
    // 2. Exam vault > Practice vault > Foundation vault
    // 3. Lowest questionCode (earliest sequence)
    list.sort((a, b) => {
      const aUsed = (a.usedInClassroomTest === true || usedInExamsSet.has(a.id) || usedInExamsSet.has(a.questionCode || '')) ? 0 : 1;
      const bUsed = (b.usedInClassroomTest === true || usedInExamsSet.has(b.id) || usedInExamsSet.has(b.questionCode || '')) ? 0 : 1;
      if (aUsed !== bUsed) return aUsed - bUsed;

      const aVault = vaultRank(a.vault);
      const bVault = vaultRank(b.vault);
      if (aVault !== bVault) return aVault - bVault;

      return String(a.questionCode || a.id).localeCompare(String(b.questionCode || b.id));
    });

    const kept = [];
    const keptNormSet = new Set();
    const keptSkelSet = new Set();

    const fastNorm = (q) => {
      const raw = (q.type === 'OAR' || q.type === 'assertion_reason' || (q.assertion && q.reason))
        ? `${q.assertion || ''} ${q.reason || ''}`
        : (q.text || q.questionText || q.question || '');
      return raw.replace(/<svg[\s\S]*?<\/svg>/gi, ' ').replace(/<[^>]+>/g, ' ').toLowerCase().replace(/\\([a-zA-Z]+)/g, '$1').replace(/[$_{}\\^~`"']/g, '').replace(/[^\w\s]/g, ' ').replace(/\s+/g, ' ').trim();
    };

    for (const q of list) {
      const subjKey = `${q.boardCode || '?'}-${q.class || '?'}-${q.subjectCode || '?'}`;
      if (!subjectStats.has(subjKey)) subjectStats.set(subjKey, { total: 0, kept: 0, deleted: 0 });
      const st = subjectStats.get(subjKey);
      st.total++;

      // Never delete a question that is actively referenced by an existing exam
      const isReferenced = q.usedInClassroomTest === true || usedInExamsSet.has(q.id) || usedInExamsSet.has(q.questionCode || '');
      const norm = fastNorm(q);
      const skel = norm.replace(/\b\d+(?:\.\d+)?\b/g, '#');
      let isDup = false;
      if (norm && keptNormSet.has(norm)) {
        isDup = true;
      } else if (skel.includes('#') && keptSkelSet.has(skel)) {
        isDup = true;
      } else {
        isDup = kept.some(k => areQuestionsTooSimilar(q, k));
      }

      if (isDup && !isReferenced) {
        toDelete.push(q);
        st.deleted++;
        if (q.topicCode) affectedTopicCodes.add(q.topicCode);
      } else {
        kept.push(q);
        if (norm) keptNormSet.add(norm);
        if (skel.includes('#')) keptSkelSet.add(skel);
        st.kept++;
      }
    }
  }

  console.log('\n--- Per-Subject Deduplication Summary ---');
  for (const [subj, st] of Array.from(subjectStats.entries()).sort((a, b) => b[1].deleted - a[1].deleted)) {
    if (st.deleted > 0) {
      console.log(`${subj.padEnd(20)} total: ${String(st.total).padStart(6)} | kept: ${String(st.kept).padStart(6)} | toDelete: ${String(st.deleted).padStart(6)}`);
    }
  }
  console.log(`\nTotal to keep: ${snap.size - toDelete.length} | Total to delete: ${toDelete.length}`);

  if (DRY_RUN || toDelete.length === 0) {
    console.log(DRY_RUN ? 'Dry run complete. No changes made.' : 'No duplicates found.');
    process.exit(0);
  }

  // 3. Rule Q: Pre-Mutation Automated Snapshot
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_dedup_entire_question_bank`;
  const snapshotFile = path.join(targetDir, `${snapshotId}.json`);

  console.log(`\nFetching & streaming full documents for Rule Q pre-mutation snapshot (${toDelete.length} docs) to ${snapshotFile}...`);
  const ws = fs.createWriteStream(snapshotFile, { encoding: 'utf8' });
  ws.write(JSON.stringify({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q pre-mutation backup before deduplicating entire questions collection (${toDelete.length} duplicate/loop-variant docs)`,
    counts: {
      totalBefore: snap.size,
      deletedCount: toDelete.length,
      keptCount: snap.size - toDelete.length
    }
  }).slice(0, -1) + ',"deletedQuestions":[\n');

  let snapCount = 0;
  for (let i = 0; i < toDelete.length; i += 400) {
    const chunk = toDelete.slice(i, i + 400);
    const refs = chunk.map(q => adminDb.collection('questions').doc(q.id));
    const fullSnaps = await adminDb.getAll(...refs);
    for (const s of fullSnaps) {
      if (s.exists) {
        if (snapCount > 0) ws.write(',\n');
        ws.write(JSON.stringify({ id: s.id, ...s.data() }));
        snapCount++;
      }
    }
    if (snapCount % 10000 === 0 || i + 400 >= toDelete.length) {
      console.log(`Snapshotted ${snapCount} / ${toDelete.length} docs...`);
    }
  }
  ws.write('\n]}\n');
  await new Promise((resolve, reject) => {
    ws.on('finish', resolve);
    ws.on('error', reject);
    ws.end();
  });
  console.log(`Snapshot written (${snapCount} docs).`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Rule Q pre-mutation backup before deduplicating entire questions collection (${toDelete.length} duplicate/loop-variant docs)`,
    counts: {
      totalBefore: snap.size,
      deletedCount: toDelete.length,
      keptCount: snap.size - toDelete.length
    },
    snapshotFile
  });
  console.log('Snapshot logged in _systemBackups.');

  // 4. Delete duplicates in chunks of 450
  const CHUNK_SIZE = 450;
  let deleted = 0;
  for (let i = 0; i < toDelete.length; i += CHUNK_SIZE) {
    const chunk = toDelete.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    for (const q of chunk) {
      batch.delete(adminDb.collection('questions').doc(q.id));
    }
    await commitWithRetry(batch);
    deleted += chunk.length;
    if (deleted % 4500 === 0 || deleted === toDelete.length) {
      console.log(`Deleted ${deleted} / ${toDelete.length}...`);
    }
  }

  // 5. Sync syllabus topic counts
  const topicList = Array.from(affectedTopicCodes);
  console.log(`\nSyncing syllabus counts for ${topicList.length} affected topicCodes...`);
  for (let i = 0; i < topicList.length; i += 200) {
    await syncTopicCountsToSyllabus(topicList.slice(i, i + 200));
  }
  console.log('Syllabus counts synced. Deduplication complete!');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
