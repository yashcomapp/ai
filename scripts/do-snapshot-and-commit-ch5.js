// scripts/do-snapshot-and-commit-ch5.js
// Creates pre-mutation snapshot, commits all 122 questions of Chapter 5 to Firestore, and verifies live parity.

const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot for Chapter 5 ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_5_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 5 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync(path.resolve('backups/staging/mh9_scit_5_enhanced.json'), 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  if (enhancedList.length !== 122) {
    throw new Error(`Expected exactly 122 enhanced questions, found ${enhancedList.length}`);
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

  console.log(`\nSuccessfully committed all ${enhancedList.length} questions of Chapter 5 to Firestore!`);

  // Verify sample questions in Firestore
  console.log('\n--- Step 3: Verification of Committed Questions in Firestore ---');
  const testIds = [
    'MH-9-SCIT-5-5.1-OSC-001',
    'MH-9-SCIT-5-5.1-OSC-033',
    'MH-9-SCIT-5-5.1-OSC-060',
    'MH-9-SCIT-5-5.1-OSC-080',
    'MH-9-SCIT-5-5.1-OSC-122'
  ];

  for (const tid of testIds) {
    const doc = await db.collection('questions').doc(tid).get();
    if (!doc.exists) {
      console.error(`❌ Verification failed: ${tid} does not exist in Firestore!`);
    } else {
      const data = doc.data();
      const hasPart1 = data.solution && data.solution.includes('### 1. Scientific Principle');
      const hasPart2 = data.solution && data.solution.includes('### 2. Physical Context');
      const hasPart3 = data.solution && data.solution.includes('### 3. Step-by-Step Option');
      console.log(`✅ [${tid}] isEnhanced: ${data.isEnhanced} | Headers: P1=${hasPart1}, P2=${hasPart2}, P3=${hasPart3} | Ans: ${data.correctAnswer}`);
    }
  }

  console.log('\n--- Step 4: Verification of isEnhanced across all 122 questions in Chapter 5 ---');
  const qSnap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-5-5.1')
    .get();

  let enhancedCount = 0;
  qSnap.forEach(d => {
    if (d.data().isEnhanced === true) enhancedCount++;
  });

  console.log(`Firestore Live Count: ${qSnap.size} total questions found for Chapter 5.`);
  console.log(`Firestore Enhanced Count: ${enhancedCount} / ${qSnap.size} marked isEnhanced: true.`);

  if (enhancedCount === 122) {
    console.log('🎉 100% of Chapter 5 questions are verified enhanced live in Firestore!');
  } else {
    console.warn(`⚠️ Warning: Expected 122 enhanced, found ${enhancedCount}`);
  }
}

run().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
