// scripts/commit_mh9_mth2_ch3_ch4.js
// Commits 1,120 validated questions for MH-9-MTH2 Chapters 3 & 4 (14 subtopics)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation per subtopic)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const { ch3Ch4Questions } = require('./mh9_mth2_ch3_ch4_data.js');

async function main() {
  console.log(`=== Step 1: Validating ${ch3Ch4Questions.length} Questions for MH-9-MTH2 Ch 3 & 4 ===`);
  let hasErrors = false;
  ch3Ch4Questions.forEach((q, idx) => {
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
  console.log(`All ${ch3Ch4Questions.length} questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'commit_mh9_mth2_ch3_ch4_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ch3Ch4Questions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ch3Ch4Questions.length; i += CHUNK_SIZE) {
    const chunk = ch3Ch4Questions.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ch3Ch4Questions.length} questions to Firestore! MH-9-MTH2 Ch 3 & 4 now 100% compliant!`);
}

main().catch(console.error);
