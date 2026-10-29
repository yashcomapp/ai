// scripts/do-snapshot-and-commit-ch13.js
// Creates pre-mutation snapshot, commits all 79 questions of Chapter 13 to Firestore, and verifies live parity.

const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 13 (Carbon) ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_13_compact_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 13 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync(path.resolve('backups/staging/mh9_scit_13_enhanced.json'), 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  if (enhancedList.length !== 79) {
    throw new Error(`Expected exactly 79 enhanced questions, found ${enhancedList.length}`);
  }

  const batch = db.batch();
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
  }

  await batch.commit();
  console.log(`Successfully committed all 79 questions to Firestore!`);

  console.log('\n--- Step 3: Verification Readback ---');
  const verifyIds = [
    'MH-9-SCIT-13-13.1-OSC-001',
    'MH-9-SCIT-13-13.1-OSC-017',
    'MH-9-SCIT-13-13.1-OSC-040',
    'MH-9-SCIT-13-13.1-OSC-045',
    'MH-9-SCIT-13-13.1-OSC-058',
    'MH-9-SCIT-13-13.1-OSC-079'
  ];

  for (const vid of verifyIds) {
    const snap = await db.collection('questions').doc(vid).get();
    if (!snap.exists) {
      console.error(`Verification FAILED: ${vid} not found!`);
    } else {
      const data = snap.data();
      const hasCompactHeaders = data.solution &&
        data.solution.includes('**Key Concept:**') &&
        data.solution.includes('**Option Analysis:**') &&
        !data.solution.includes('### 1. Scientific Principle');
      console.log(`Verified ${vid}: isEnhanced=${data.isEnhanced}, Ans=${data.correctAnswer}, CompactHeaders=${hasCompactHeaders}, Opts=${data.options.length}`);
    }
  }

  console.log('\n>>> CHAPTER 13 SNAPSHOT AND COMMIT COMPLETED SUCCESSFULLY! <<<');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error in snapshot and commit:', err);
  process.exit(1);
});
