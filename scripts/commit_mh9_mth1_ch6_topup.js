// scripts/commit_mh9_mth1_ch6_topup.js
// Commits 562 validated questions to bring MH-9-MTH1 Chapter 6 (Financial Planning)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation per topic)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const { ch6Questions } = require('./mh9_mth1_ch6_data.js');

async function main() {
  console.log(`=== Step 1: Validating ${ch6Questions.length} Questions for Chapter 6 Financial Planning 80Q Top-Up ===`);
  let hasErrors = false;
  ch6Questions.forEach((q, idx) => {
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
  console.log(`All ${ch6Questions.length} Chapter 6 top-up questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'topup_mh9_mth1_ch6_to_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ch6Questions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ch6Questions.length; i += CHUNK_SIZE) {
    const chunk = ch6Questions.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ch6Questions.length} questions to Firestore! Chapter 6 Financial Planning now has full 80Q packs across all topics!`);
}

main().catch(console.error);
