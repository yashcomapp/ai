/**
 * Generic SSOT Question Committer for MH-10-SCIT1 and MH-10-SCIT2.
 * Usage: node scripts/commit_mh10_scit_questions.js <jsonPath1> [jsonPath2 ...]
 */
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

async function commitWithRetry(batch, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await batch.commit();
      return;
    } catch (err) {
      console.warn(`Batch commit attempt ${attempt} failed: ${err.message}`);
      if (attempt === retries) throw err;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
}

async function syncSubjectCounts(docId, prefix) {
  const qSnap = await adminDb.collection('questions')
    .where('topicCode', '>=', prefix + '-')
    .where('topicCode', '<=', prefix + '-\uf8ff')
    .select('topicCode', 'status', 'disputed')
    .get();

  const counts = {};
  qSnap.forEach(d => {
    const q = d.data();
    if (q.status === 'quarantined' || q.disputed) return;
    counts[q.topicCode] = (counts[q.topicCode] || 0) + 1;
  });

  const sylRef = adminDb.collection('syllabus').doc(docId);
  const sylSnap = await sylRef.get();
  if (!sylSnap.exists) return;

  const syl = sylSnap.data();
  const chapters = syl.chapters || [];
  let totalSubjectObj = 0;

  for (const ch of chapters) {
    let chObj = 0;
    for (const t of (ch.topics || [])) {
      if (Array.isArray(t.subtopics) && t.subtopics.length > 0) {
        for (const s of t.subtopics) {
          const code = s.subtopicCode || s.topicCode;
          const c = counts[code] || 0;
          s.objectiveCount = c;
          chObj += c;
        }
        t.objectiveCount = 0;
      } else {
        const code = t.topicCode;
        const c = counts[code] || 0;
        t.objectiveCount = c;
        chObj += c;
      }
    }
    ch.objectiveCount = chObj;
    totalSubjectObj += chObj;
  }

  await sylRef.update({
    chapters,
    objectiveCount: totalSubjectObj,
    totalObjectiveQuestions: totalSubjectObj,
    updatedAt: new Date().toISOString()
  });

  console.log(`Synced syllabus/${docId}: totalObjectiveQuestions = ${totalSubjectObj}`);
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error('Usage: node scripts/commit_mh10_scit_questions.js <jsonPath1> [jsonPath2 ...]');
    process.exit(1);
  }

  let allQuestions = [];
  for (const arg of args) {
    const resolved = path.isAbsolute(arg) ? arg : path.join(process.cwd(), arg);
    const data = JSON.parse(fs.readFileSync(resolved, 'utf8'));
    allQuestions = allQuestions.concat(data);
    console.log(`Loaded ${data.length} questions from ${resolved}`);
  }

  if (allQuestions.length === 0) {
    console.log('No questions to commit.');
    process.exit(0);
  }

  // Rule Q: Mandatory pre-mutation snapshot
  await createPreMutationSnapshot(['syllabus', 'syllabusTopicIndex'], 'mh10_scit_empty_fill');

  const nowIso = new Date().toISOString();
  for (let i = 0; i < allQuestions.length; i += 400) {
    const chunk = allQuestions.slice(i, i + 400);
    const batch = adminDb.batch();
    for (const q of chunk) {
      const ref = adminDb.collection('questions').doc(q.questionCode);
      batch.set(ref, {
        ...q,
        createdAt: nowIso,
        updatedAt: nowIso
      });
    }
    await commitWithRetry(batch);
    console.log(`Committed batch ${Math.floor(i / 400) + 1} (${chunk.length} questions)`);
  }

  const prefixes = new Set(allQuestions.map(q => `${q.boardCode}-${q.class}-${q.subjectCode}`));
  if (prefixes.has('MH-10-SCIT1')) await syncSubjectCounts('mh_10_scit1', 'MH-10-SCIT1');
  if (prefixes.has('MH-10-SCIT2')) await syncSubjectCounts('mh_10_scit2', 'MH-10-SCIT2');

  console.log('Done! Run `node scripts/rebuild_syllabus_index.js` to refresh syllabusTopicIndex.');
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
