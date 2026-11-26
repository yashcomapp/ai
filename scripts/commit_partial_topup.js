/**
 * SSOT Top-Up Committer for Partial Leaves (<80 Qs -> exact 80 Qs)
 * Usage: node scripts/commit_partial_topup.js <json1> [<json2> ...]
 *
 * For each topicCode present in the input JSON(s):
 *  - Fetches existing active questions for that topicCode
 *  - Deduplicates candidate questions against existing normalized texts
 *  - Selects exact (80 - existingCount) questions, prioritizing underrepresented types
 *  - Assigns unique canonical questionCodes starting after max existing sequence
 *  - Rebalances vaults across all 80 questions to exact: 40 exam, 20 practice, 20 foundation
 *  - Creates ONE atomic pre-mutation snapshot of ['syllabus', 'syllabusTopicIndex']
 */
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

function normText(t) {
  return String(t || '').trim().toLowerCase().replace(/\s+/g, ' ');
}

function getSeq(qCode, docId) {
  const m = String(qCode || docId || '').match(/-(\d+)$/);
  return m ? Number(m[1]) : 0;
}

async function main() {
  const files = process.argv.slice(2);
  if (files.length === 0) {
    console.error('Usage: node scripts/commit_partial_topup.js <json1> [<json2> ...]');
    process.exit(1);
  }

  const candidatesByTopic = new Map();
  for (const f of files) {
    const abs = path.resolve(f);
    const data = JSON.parse(fs.readFileSync(abs, 'utf8'));
    console.log(`Loaded ${data.length} candidate questions from ${abs}`);
    for (const q of data) {
      if (!candidatesByTopic.has(q.topicCode)) candidatesByTopic.set(q.topicCode, []);
      candidatesByTopic.get(q.topicCode).push(q);
    }
  }

  console.log(`Targeting ${candidatesByTopic.size} partial topicCodes...`);
  await createPreMutationSnapshot(['syllabus', 'syllabusTopicIndex'], 'mh10_partial_topup');

  const typeTarget = { OSC: 44, OMC: 10, OTF: 10, OAR: 10, ONE: 3, OFB: 3 };
  const vaultTargets = [
    ...Array(40).fill('exam'),
    ...Array(20).fill('practice'),
    ...Array(20).fill('foundation'),
  ];

  const writeOps = []; // { type: 'set'|'update', ref, data }
  const subjectDocsToSync = new Set();

  for (const [tc, candidates] of candidatesByTopic.entries()) {
    const qSnap = await adminDb
      .collection('questions')
      .where('topicCode', '==', tc)
      .get();

    const existing = [];
    const seenTexts = new Set();
    const typeCounts = {};
    let maxSeq = 0;

    qSnap.forEach((d) => {
      const q = d.data();
      if (q.status === 'quarantined' || q.disputed) return;
      existing.push({ ref: d.ref, id: d.id, data: q });
      seenTexts.add(normText(q.text));
      const t = q.type || 'OSC';
      typeCounts[t] = (typeCounts[t] || 0) + 1;
      maxSeq = Math.max(maxSeq, getSeq(q.questionCode, d.id));
    });

    const needed = 80 - existing.length;
    if (needed <= 0) {
      console.log(`  [SKIP] ${tc}: already has ${existing.length}/80`);
      continue;
    }

    const uniqueCands = [];
    for (const c of candidates) {
      const nt = normText(c.text);
      if (!seenTexts.has(nt)) {
        seenTexts.add(nt);
        uniqueCands.push(c);
      }
    }

    // Score candidates by type deficit (most underrepresented type first)
    const selected = [];
    const pool = [...uniqueCands];
    while (selected.length < needed && pool.length > 0) {
      let bestIdx = 0;
      let bestNeed = -999;
      for (let i = 0; i < pool.length; i++) {
        const t = pool[i].type || 'OSC';
        const need = (typeTarget[t] || 0) - (typeCounts[t] || 0);
        if (need > bestNeed) {
          bestNeed = need;
          bestIdx = i;
        }
      }
      const chosen = pool.splice(bestIdx, 1)[0];
      const t = chosen.type || 'OSC';
      typeCounts[t] = (typeCounts[t] || 0) + 1;
      selected.push(chosen);
    }

    if (selected.length < needed) {
      throw new Error(`${tc}: needed ${needed} non-duplicate questions, only found ${selected.length}`);
    }

    // Assign sequential questionCodes starting after maxSeq
    const newDocs = selected.map((c, idx) => {
      const seqNum = maxSeq + idx + 1;
      const seqStr = String(seqNum).padStart(3, '0');
      const qCode = `${tc}-${c.type}-${seqStr}`;
      return {
        ...c,
        questionCode: qCode,
        id: qCode,
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      };
    });

    // Combine existing + newDocs to ensure exact 40 exam, 20 practice, 20 foundation
    const combined = [
      ...existing.map((e) => ({ isNew: false, ref: e.ref, curVault: e.data.vault })),
      ...newDocs.map((n) => ({ isNew: true, doc: n })),
    ];
    if (combined.length !== 80) {
      throw new Error(`${tc}: combined length ${combined.length} !== 80`);
    }

    // Keep existing vault assignments where within quota, reassign overflow/new
    const quota = { exam: 40, practice: 20, foundation: 20 };
    const assigned = Array(80).fill(null);

    combined.forEach((item, i) => {
      if (!item.isNew && item.curVault && quota[item.curVault] > 0) {
        assigned[i] = item.curVault;
        quota[item.curVault]--;
      }
    });

    const remainingVaults = [
      ...Array(quota.exam).fill('exam'),
      ...Array(quota.practice).fill('practice'),
      ...Array(quota.foundation).fill('foundation'),
    ];
    let rvIdx = 0;
    combined.forEach((item, i) => {
      if (!assigned[i]) assigned[i] = remainingVaults[rvIdx++];
    });

    combined.forEach((item, i) => {
      const targetVault = assigned[i];
      if (item.isNew) {
        const docData = { ...item.doc, vault: targetVault };
        const ref = adminDb.collection('questions').doc(docData.questionCode);
        writeOps.push({ type: 'set', ref, data: docData });
      } else if (item.curVault !== targetVault) {
        writeOps.push({ type: 'update', ref: item.ref, data: { vault: targetVault } });
      }
    });

    // Track syllabus doc ID (e.g. mh_10_mth1, mh_10_scit1, mh_10_scit2)
    const parts = tc.split('-');
    if (parts.length >= 3) {
      subjectDocsToSync.add(`${parts[0].toLowerCase()}_${parts[1]}_${parts[2].toLowerCase()}`);
    }
    console.log(`  [TOPUP] ${tc}: ${existing.length} -> 80 (+${selected.length} new)`);
  }

  // Commit in batches of 400
  for (let i = 0; i < writeOps.length; i += 400) {
    const chunk = writeOps.slice(i, i + 400);
    const batch = adminDb.batch();
    for (const op of chunk) {
      if (op.type === 'set') batch.set(op.ref, op.data, { merge: true });
      else batch.update(op.ref, op.data);
    }
    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / 400) + 1} (${chunk.length} ops)`);
  }

  // Sync syllabus totalObjectiveQuestions
  for (const docId of subjectDocsToSync) {
    const prefix = docId.toUpperCase().replace(/_/g, '-');
    const countSnap = await adminDb
      .collection('questions')
      .where('topicCode', '>=', prefix + '-')
      .where('topicCode', '<=', prefix + '-\uf8ff')
      .count()
      .get();
    await adminDb.collection('syllabus').doc(docId).set(
      { totalObjectiveQuestions: countSnap.data().count },
      { merge: true }
    );
    console.log(`Synced syllabus/${docId}: totalObjectiveQuestions = ${countSnap.data().count}`);
  }

  console.log('Done! Run `node scripts/rebuild_syllabus_index.js` when all top-ups finish.');
  process.exit(0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
