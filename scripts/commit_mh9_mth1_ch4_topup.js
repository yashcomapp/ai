// scripts/commit_mh9_mth1_ch4_topup.js
// Commits 754 validated questions to bring MH-9-MTH1 Chapter 4 (Ratio and Proportion)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation per topic)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const { ch4Questions } = require('./mh9_mth1_ch4_data.js');

async function main() {
  console.log(`=== Step 1: Validating ${ch4Questions.length} Questions for Chapter 4 Ratio and Proportion 80Q Top-Up ===`);
  let hasErrors = false;
  ch4Questions.forEach((q, idx) => {
    const errs = validateQuestion(q);
    if (errs.length > 0) {
      console.error(`Validation Error in Question ${idx + 1} (${q.questionCode}):`, errs);
      hasErrors = true;
    }
  });

  if (hasErrors) {
    console.error('Validation failed. Aborting insertion.');
    process.exit(1);
  }
  console.log(`All ${ch4Questions.length} Chapter 4 top-up questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'topup_mh9_mth1_ch4_to_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ch4Questions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ch4Questions.length; i += CHUNK_SIZE) {
    const chunk = ch4Questions.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ch4Questions.length} questions to Firestore! Chapter 4 Ratio and Proportion now has full 80Q packs across all topics!`);
}

main().catch(console.error);
