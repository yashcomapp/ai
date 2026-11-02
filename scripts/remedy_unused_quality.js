const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

const { createPreMutationSnapshot } = require('../scripts/pre-mutation-snapshot.js');

async function runRemediation() {
  console.log('====================================================');
  console.log('🚀 EXECUTING UNUSED QUESTION QUALITY REMEDIATION');
  console.log('====================================================');

  // STEP 1: Mandatory Pre-Mutation Snapshot (Rule 2Q)
  console.log('\n--- Step 1: Pre-Mutation Atomic Snapshot ---');
  await createPreMutationSnapshot(['questions', 'syllabusTopicIndex'], 'prune_and_repair_unused_questions_quality');
  console.log('Snapshot successfully recorded in _systemBackups.');

  // STEP 2: Repair MH-9-MTH1 Financial Planning math formatting (16 questions)
  console.log('\n--- Step 2: Repairing 16 MH-9-MTH1 questions ---');
  const mth16Ids = [
    'MH-9-MTH1-6-6.1.1-ONE-001',
    'MH-9-MTH1-6-6.1.1-ONE-002',
    'MH-9-MTH1-6-6.1.1-ONE-003',
    'MH-9-MTH1-6-6.1.1-ONE-004',
    'MH-9-MTH1-6-6.1.1-ONE-005',
    'MH-9-MTH1-6-6.1.1-ONE-006',
    'MH-9-MTH1-6-6.1.1-ONE-007',
    'MH-9-MTH1-6-6.1.2-ONE-001',
    'MH-9-MTH1-6-6.1.2-ONE-002',
    'MH-9-MTH1-6-6.1.2-ONE-003',
    'MH-9-MTH1-6-6.1.2-ONE-004',
    'MH-9-MTH1-6-6.1.2-ONE-005',
    'MH-9-MTH1-6-6.1.2-ONE-006',
    'MH-9-MTH1-6-6.1.2-ONE-007',
    'MH-9-MTH1-4-4.2.1-OTF-021',
    'MH-9-MTH1-4-4.3.4-OTF-004'
  ];

  for (const id of mth16Ids) {
    const docRef = db.collection('questions').doc(id);
    const snap = await docRef.get();
    if (!snap.exists) continue;

    const data = snap.data();
    let cleanText = String(data.text || '')
      .replace(/\\\(\\\)\s*/g, '₹')
      .replace(/\\\)\s*(\d[\d,]*)\\\)/g, '₹$1');

    let cleanSol = String(data.solution || '')
      .replace(/\\\(\\\)\s*/g, '₹')
      .replace(/\\\)\s*(\d[\d,]*)\\\)/g, '₹$1');

    const cleanOptions = (data.options || []).map(opt => {
      let str = typeof opt === 'object' && opt !== null ? (opt.text || '') : String(opt || '');
      return str
        .replace(/\\\(\\\)\s*/g, '₹')
        .replace(/\\\)\s*(\d[\d,]*)\\\)/g, '₹$1');
    });

    await docRef.update({
      text: cleanText,
      options: cleanOptions,
      solution: cleanSol,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
  }
  console.log(`Repaired ${mth16Ids.length} MH-9-MTH1 formatting issues.`);

  // STEP 3: Repair MH-10-SCIT1 and MH-10-SCIT2
  console.log('\n--- Step 3: Repairing MH-10-SCIT1 & MH-10-SCIT2 questions ---');
  // 1. MH-10-SCIT1-9-9.2.1-OTF-039
  const scit1Ref = db.collection('questions').doc('MH-10-SCIT1-9-9.2.1-OTF-039');
  await scit1Ref.update({
    text: "In a homologous series of alkanes, each successive member differs by a \\(\\ce{-CH_2-}\\) unit.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  // 2. MH-10-SCIT2 missing solutions
  await db.collection('questions').doc('MH-10-SCIT2-1-1.4.1-OSC-004').update({
    solution: "According to Charles Darwin's theory of natural selection, 'survival of the fittest' means that only those organisms that possess favorable variations best suited to the prevailing environment survive and reproduce, while others perish.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  await db.collection('questions').doc('MH-10-SCIT2-7-7.5.3-OSC-023').update({
    solution: "Biofuels obtained from biological sources like algae and sugarcane molasses are clean, renewable sources of energy that reduce greenhouse gas emissions and provide sustainable alternatives to depleting fossil fuel reserves.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  await db.collection('questions').doc('MH-10-SCIT2-8-8.1.3-OSC-007').update({
    solution: "Unlike embryonic stem cells which are pluripotent (can differentiate into almost all cell types), adult stem cells are generally multipotent with a more restricted differentiation potential limited to specific tissue lineages.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });
  console.log('Repaired MH-10-SCIT1 and MH-10-SCIT2 specific solutions & math syntax.');

  // STEP 4: Purge Non-Existent Chapters 19 & 20 in MH-9-SCIT (659 questions, used: 0)
  console.log('\n--- Step 4: Purging 659 phantom Chapter 19 & 20 questions in MH-9-SCIT ---');
  const allQsSnap = await db.collection('questions').get();
  const toDeleteIds = [];

  allQsSnap.forEach(doc => {
    const q = doc.data();
    const isUsed = q.usageCount > 0 || q.timesUsed > 0 || q.used === true;
    if (isUsed) return; // STRICT GUARD: Never delete used questions!

    const id = doc.id;
    const sub = q.subjectCode;
    const cl = String(q.class || '');
    const ch = String(q.chapterNumber || '');

    // 1. Phantom Chapter 19 & 20 in MH-9-SCIT
    if (sub === 'SCIT' && cl === '9' && (ch === '19' || ch === '20' || id.includes('-19-') || id.includes('-20-'))) {
      toDeleteIds.push(id);
      return;
    }

    // 2. MH-8-SCI duplicate "None of the above" or bogus distractor labels
    if (sub === 'SCI' && cl === '8') {
      const opts = (q.options || []).map(o => {
        return (typeof o === 'object' && o !== null ? (o.text || o.label || o.value || '') : String(o || '')).trim().toLowerCase();
      });
      const noneCount = opts.filter(o => o === 'none of the above' || o === 'none of these').length;
      const hasBogus = opts.some(o => o.startsWith('right:') || o.startsWith('wrong:') || o.startsWith('right :') || o.startsWith('wrong:'));

      if (noneCount > 1 || hasBogus) {
        toDeleteIds.push(id);
        return;
      }
    }
  });

  console.log(`Identified ${toDeleteIds.length} sub-standard / phantom unused questions to purge.`);

  // Execute chunked batch deletions
  const BATCH_SIZE = 400;
  for (let i = 0; i < toDeleteIds.length; i += BATCH_SIZE) {
    const chunk = toDeleteIds.slice(i, i + BATCH_SIZE);
    const batch = db.batch();
    chunk.forEach(id => {
      batch.delete(db.collection('questions').doc(id));
    });
    await batch.commit();
    console.log(`Deleted batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions)...`);
  }
  console.log(`Successfully purged ${toDeleteIds.length} sub-standard unused questions!`);

  // STEP 5: Re-calculate and update syllabusTopicIndex objective counts
  console.log('\n--- Step 5: Syncing syllabusTopicIndex counts ---');
  const remainingSnap = await db.collection('questions').get();
  console.log(`Remaining pristine questions in Question Bank: ${remainingSnap.size}`);

  const countsByTopic = {};
  remainingSnap.forEach(doc => {
    const q = doc.data();
    const tCode = q.topicCode;
    if (tCode) {
      countsByTopic[tCode] = (countsByTopic[tCode] || 0) + 1;
    }
  });

  const indexSnap = await db.collection('syllabusTopicIndex').get();
  let indexUpdates = 0;
  let indexBatch = db.batch();

  for (const doc of indexSnap.docs) {
    const tCode = doc.id;
    const currentCount = countsByTopic[tCode] || 0;
    const existing = doc.data().objectiveCount || 0;

    if (existing !== currentCount) {
      indexBatch.set(doc.ref, {
        objectiveCount: currentCount,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
      indexUpdates++;

      if (indexUpdates % 400 === 0) {
        await indexBatch.commit();
        indexBatch = db.batch();
      }
    }
  }

  if (indexUpdates % 400 !== 0) {
    await indexBatch.commit();
  }

  console.log(`Updated ${indexUpdates} syllabusTopicIndex records.`);
  console.log('\n====================================================');
  console.log('✅ QUESTION QUALITY REMEDIATION SUCCESSFULLY COMPLETED');
  console.log('====================================================');
}

runRemediation().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
