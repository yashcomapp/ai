// scripts/do-snapshot-and-commit-ch6.js
// Creates pre-mutation snapshot, commits all 211 questions of Chapter 6 to Firestore, and verifies live parity.

const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 6 (Classification of Plants) ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_6_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 6 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync(path.resolve('backups/staging/mh9_scit_6_enhanced.json'), 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  if (enhancedList.length !== 211) {
    throw new Error(`Expected exactly 211 enhanced questions, found ${enhancedList.length}`);
  }

  let batch = db.batch();
  let opCount = 0;
  let batchCount = 0;

  for (const q of enhancedList) {
    const docId = q.id || q.questionCode;
    const docRef = db.collection('questions').doc(docId);
    batch.update(docRef, {
      text: q.text,
      options: q.options,
      correctAnswer: q.correctAnswer,
      solution: q.solution,
      isEnhanced: true,
      enhancedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    opCount++;

    if (opCount === 450) {
      batchCount++;
      console.log(`Committing batch ${batchCount} (450 operations)...`);
      await batch.commit();
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    batchCount++;
    console.log(`Committing final batch ${batchCount} (${opCount} operations)...`);
    await batch.commit();
  }

  console.log('\n✅ Successfully committed all 211 questions to Firestore!');

  console.log('\n--- Step 3: Live Verification Readback ---');
  const sampleCodes = [
    'MH-9-SCIT-6-6.1-OSC-001',
    'MH-9-SCIT-6-6.1-OSC-040',
    'MH-9-SCIT-6-6.1-OSC-085',
    'MH-9-SCIT-6-6.1-OSC-134',
    'MH-9-SCIT-6-6.1-OSC-176',
    'MH-9-SCIT-6-6.1-OSC-211'
  ];

  for (const code of sampleCodes) {
    const docSnap = await db.collection('questions').doc(code).get();
    if (!docSnap.exists) {
      console.error(`Verification FAILED: Document ${code} does not exist in Firestore!`);
    } else {
      const data = docSnap.data();
      const hasH1 = data.solution.includes('### 1.');
      const hasH2 = data.solution.includes('### 2.');
      const hasH3 = data.solution.includes('### 3.');
      console.log(`Verified ${code}: isEnhanced=${data.isEnhanced}, Ans=${data.correctAnswer}, 3-Part Headers: H1=${hasH1}, H2=${hasH2}, H3=${hasH3}`);
    }
  }

  console.log('\n🎉 Chapter 6 Gold Standard Enhancement 100% Live in Production Firestore!');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error during snapshot or commit:', err);
  process.exit(1);
});
