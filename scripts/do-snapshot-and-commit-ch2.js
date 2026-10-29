// scripts/do-snapshot-and-commit-ch2.js
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');

async function run() {
  console.log('--- Step 1: Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_2_gold_approved');
  console.log(`Snapshot created successfully: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 2 Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_2_enhanced.json', 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  let batch = db.batch();
  let opCount = 0;
  let batchCount = 0;

  for (const q of enhancedList) {
    const docRef = db.collection('questions').doc(q.id);
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

  console.log(`\nSuccessfully committed all ${enhancedList.length} questions of Chapter 2 to Firestore!`);

  // Verify sample in Firestore
  const q4Doc = await db.collection('questions').doc('MH-9-SCIT-2-2.1-OSC-004').get();
  const q4Data = q4Doc.data();
  console.log('\nVerification of Q4 in Firestore:');
  console.log('Text:', q4Data.text);
  console.log('Options:', q4Data.options);
  console.log('isEnhanced:', q4Data.isEnhanced);
}

run()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Failed:', err);
    process.exit(1);
  });
