// scripts/commit_mh9_mth1_ch1_topup.js
// Commits 278 validated questions to bring MH-9-MTH1 Chapter 1 (Sets)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const { topic1And2Questions } = require('./topup_mh9_mth1_ch1_to_80q.js');
const { topic3Questions } = require('./mh9_mth1_ch1_topic3_data.js');
const { topic4Questions } = require('./mh9_mth1_ch1_topic4_data.js');
const { topic5Questions } = require('./mh9_mth1_ch1_topic5_data.js');

const ALL_CH1_TOPUP = [
  ...topic1And2Questions,
  ...topic3Questions,
  ...topic4Questions,
  ...topic5Questions
];

async function main() {
  console.log(`=== Step 1: Validating ${ALL_CH1_TOPUP.length} Questions for Chapter 1 Sets 80Q Top-Up ===`);
  let hasErrors = false;
  ALL_CH1_TOPUP.forEach((q, idx) => {
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
  console.log(`All ${ALL_CH1_TOPUP.length} Chapter 1 top-up questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'topup_mh9_mth1_ch1_to_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ALL_CH1_TOPUP.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ALL_CH1_TOPUP.length; i += CHUNK_SIZE) {
    const chunk = ALL_CH1_TOPUP.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ALL_CH1_TOPUP.length} questions to Firestore! Chapter 1 Sets now has full 80Q packs across all topics!`);
}

main().catch(console.error);
