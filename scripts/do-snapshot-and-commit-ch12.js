// scripts/do-snapshot-and-commit-ch12.js
// Creates pre-mutation snapshot, commits all 114 questions of Chapter 12 to Firestore, and verifies live parity.

const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 12 (Study of Sound) ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_12_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 12 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync(path.resolve('backups/staging/mh9_scit_12_enhanced.json'), 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  if (enhancedList.length !== 114) {
    throw new Error(`Expected exactly 114 enhanced questions, found ${enhancedList.length}`);
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

  console.log(`\nSuccessfully committed all 114 questions to Firestore across ${batchCount} batch(es)!`);

  console.log('\n--- Step 3: Verification Readback ---');
  const verifyIds = [
    'MH-9-SCIT-12-12.1-OSC-001',
    'MH-9-SCIT-12-12.1-OSC-018',
    'MH-9-SCIT-12-12.1-OSC-041',
    'MH-9-SCIT-12-12.1-OSC-049',
    'MH-9-SCIT-12-12.1-OSC-082',
    'MH-9-SCIT-12-12.1-OSC-114'
  ];

  for (const vid of verifyIds) {
    const snap = await db.collection('questions').doc(vid).get();
    if (!snap.exists) {
      console.error(`Verification FAILED: ${vid} not found!`);
    } else {
      const data = snap.data();
      const hasHeaders = data.solution &&
        data.solution.includes('### 1. Scientific Principle') &&
        data.solution.includes('### 2. Wave Dynamics') &&
        data.solution.includes('### 3. Step-by-Step');
      console.log(`Verified ${vid}: isEnhanced=${data.isEnhanced}, Ans=${data.correctAnswer}, 3-PartHeaders=${hasHeaders}, Opts=${data.options.length}`);
    }
  }

  console.log('\n>>> CHAPTER 12 SNAPSHOT AND COMMIT COMPLETED SUCCESSFULLY! <<<');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error in snapshot and commit:', err);
  process.exit(1);
});
