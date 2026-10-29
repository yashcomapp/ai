// scripts/commit-ch1-gold.js
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');

async function commitChapter1Gold() {
  console.log('--- Step 1: Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(['questions'], 'chapter_1_gold_remediated');
  console.log(`Snapshot created: ${snapResult.snapshotId}`);

  console.log('\n--- Step 2: Commit Chapter 1 Remediated Questions to Firestore ---');
  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_1_enhanced_gold.json', 'utf8'));
  console.log(`Found ${enhancedList.length} questions to commit.`);

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

  console.log(`\nSuccessfully committed all ${enhancedList.length} questions of Chapter 1 to Firestore!`);

  // Verify sample questions in Firestore
  console.log('\n--- Step 3: Verification Readbacks in Firestore ---');
  const q26 = (await db.collection('questions').doc('MH-9-SCIT-1-1.1-OSC-026').get()).data();
  console.log('Q26 Options:', q26.options);
  console.log('Q26 Has 3-part headers:', q26.solution.includes('### 1.') && q26.solution.includes('### 2.') && q26.solution.includes('### 3.'));

  const q70 = (await db.collection('questions').doc('MH-9-SCIT-1-1.1-OSC-070').get()).data();
  console.log('Q70 Options:', q70.options);
  console.log('Q70 Correct Answer:', q70.correctAnswer);
}

commitChapter1Gold()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Commit failed:', err);
    process.exit(1);
  });
