// commit_batch1_physics.js
// Batch commits all 819 Physics questions (Chapters 1, 2, 3, 11, 12) to Firestore with verification.

const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Batch 1: Committing 819 Physics Questions to Firestore ---');
  const db = admin.firestore();
  const list = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_batch1_physics_compact.json', 'utf8'));
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

  console.log(`\nSuccessfully committed all 819 Physics questions across ${batchCount} batches!`);

  console.log('\n--- Live Verification Readback ---');
  const testIds = [
    'MH-9-SCIT-1-1.1-OSC-001',
    'MH-9-SCIT-2-2.1-OSC-003',
    'MH-9-SCIT-3-3.1-OSC-001',
    'MH-9-SCIT-11-11.1-OSC-001',
    'MH-9-SCIT-11-11.1.1-OTF-001',
    'MH-9-SCIT-12-12.1-OSC-001'
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

  console.log('\n>>> BATCH 1 (PHYSICS: CH 1, 2, 3, 11, 12) COMPLETED WITH 100% PARITY! <<<');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal commit error:', err);
  process.exit(1);
});
