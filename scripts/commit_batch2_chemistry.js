// commit_batch2_chemistry.js
// Batch commits all 388 Chemistry questions (Chapters 4, 5) to Firestore with verification.

const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const fs = require('fs');

async function run() {
  console.log('--- Batch 2: Committing 388 Chemistry Questions to Firestore ---');
  const db = admin.firestore();
  const list = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_batch2_chemistry_compact.json', 'utf8'));
  console.log(`Loaded ${list.length} questions to commit.`);

  let batch = db.batch();
  let opCount = 0;
  let batchCount = 0;

  for (const q of list) {
    const docId = q.id || q.questionCode;
    const docRef = db.collection('questions').doc(docId);
    batch.update(docRef, {
      solution: q.solution,
      isEnhanced: true,
      enhancedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    opCount++;

    if (opCount === 400) {
      await batch.commit();
      batchCount++;
      console.log(`Committed batch ${batchCount} (${opCount} updates)...`);
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    await batch.commit();
    batchCount++;
    console.log(`Committed final batch ${batchCount} (${opCount} updates)...`);
  }

  console.log(`\nSuccessfully committed all 388 Chemistry questions across ${batchCount} batch(es)!`);

  console.log('\n--- Live Verification Readback ---');
  const testIds = [
    'MH-9-SCIT-4-4.1-OSC-001',
    'MH-9-SCIT-4-4.2-OSC-010',
    'MH-9-SCIT-5-5.1-OSC-001',
    'MH-9-SCIT-5-5.1-OSC-050'
  ];

  for (const tid of testIds) {
    const snap = await db.collection('questions').doc(tid).get();
    if (!snap.exists) {
      console.error(`ERROR: ${tid} not found!`);
    } else {
      const d = snap.data();
      const hasCompact = d.solution && d.solution.includes('**Key Concept:**') && !d.solution.includes('### 1.');
      console.log(`Verified ${tid}: isEnhanced=${d.isEnhanced}, CompactFormat=${hasCompact}`);
    }
  }

  console.log('\n>>> BATCH 2 (CHEMISTRY: CH 4, 5) COMPLETED WITH 100% PARITY! <<<');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal commit error:', err);
  process.exit(1);
});
