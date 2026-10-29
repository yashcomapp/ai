// scripts/do-snapshot-and-commit-ch3.js
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 3 ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_3_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 3 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_3_enhanced.json', 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

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

  console.log(`\nSuccessfully committed all ${enhancedList.length} questions of Chapter 3 to Firestore!`);

  // Verify sample questions in Firestore
  console.log('\n--- Step 3: Verification of Committed Questions in Firestore ---');
  const testIds = ['MH-9-SCIT-3-3.1-OSC-028', 'MH-9-SCIT-3-3.1-OSC-053', 'MH-9-SCIT-3-3.1-OSC-082', 'MH-9-SCIT-3-3.1-OSC-108'];
  for (const tid of testIds) {
    const doc = await db.collection('questions').doc(tid).get();
    const data = doc.data();
    console.log(`\nDoc ${tid}:`);
    console.log(`  Text: ${data.text.substring(0, 60)}...`);
    console.log(`  Options: ${JSON.stringify(data.options)}`);
    console.log(`  Correct Answer: ${data.correctAnswer}`);
    console.log(`  isEnhanced: ${data.isEnhanced}`);
    console.log(`  Solution header check: ${data.solution.includes('### 1. Scientific Principle') && data.solution.includes('### 2. Physical Context') && data.solution.includes('### 3. Step-by-Step Option')}`);
  }
}

run()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Fatal Error during Chapter 3 commit:', err);
    process.exit(1);
  });
