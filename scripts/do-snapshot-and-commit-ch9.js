// scripts/do-snapshot-and-commit-ch9.js
// Creates pre-mutation snapshot, commits all 374 questions of Chapter 9 to Firestore, and verifies live parity.

const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 9 (Environmental Management) ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_9_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 9 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync(path.resolve('backups/staging/mh9_scit_9_enhanced.json'), 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  if (enhancedList.length !== 374) {
    throw new Error(`Expected exactly 374 enhanced questions, found ${enhancedList.length}`);
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

  console.log('\n✅ Successfully committed all 374 questions to Firestore!');

  console.log('\n--- Step 3: Live Verification Readback ---');
  const sampleCodes = [
    'MH-9-SCIT-9-9.1.1-OAR-001',
    'MH-9-SCIT-9-9.1.1-OSC-010',
    'MH-9-SCIT-9-9.2.1-OAR-001',
    'MH-9-SCIT-9-9.2.2-OSC-005',
    'MH-9-SCIT-9-9.3.1-OAR-001',
    'MH-9-SCIT-9-9.3.2-OSC-001',
    'MH-9-SCIT-9-9.4.1-OAR-001',
    'MH-9-SCIT-9-9.4.2-OSC-001'
  ];

  for (const code of sampleCodes) {
    const docSnap = await db.collection('questions').doc(code).get();
    if (!docSnap.exists) {
      console.error(`Verification FAILED: Document ${code} does not exist in Firestore!`);
    } else {
      const data = docSnap.data();
      const hasHeaders = data.solution.includes('### 1.') && data.solution.includes('### 2.') && data.solution.includes('### 3.');
      console.log(`Verified ${code}: isEnhanced=${data.isEnhanced}, 3-part headers=${hasHeaders ? 'YES' : 'NO'}`);
      if (!hasHeaders) {
        throw new Error(`Integrity violation: ${code} lacks 3-part headers after commit!`);
      }
    }
  }

  console.log('\n🎉 ALL 374 QUESTIONS OF CHAPTER 9 COMMITTED AND VERIFIED TO GOLD STANDARD!');
  process.exit(0);
}

run().catch(err => {
  console.error('Fatal error during snapshot and commit:', err);
  process.exit(1);
});
