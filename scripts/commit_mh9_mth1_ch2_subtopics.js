// scripts/commit_mh9_mth1_ch2_subtopics.js
// Commits 720 validated questions to bring EVERY subtopic of MH-9-MTH1 Chapter 2 (Real Numbers)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation per subtopic)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const { ch2SubtopicsQuestions } = require('./mh9_mth1_ch2_subtopics_data.js');

async function main() {
  console.log(`=== Step 1: Validating ${ch2SubtopicsQuestions.length} Questions for Chapter 2 Subtopics 80Q Top-Up ===`);
  let hasErrors = false;
  ch2SubtopicsQuestions.forEach((q, idx) => {
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
  console.log(`All ${ch2SubtopicsQuestions.length} Chapter 2 subtopic questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'topup_mh9_mth1_ch2_subtopics_to_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ch2SubtopicsQuestions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ch2SubtopicsQuestions.length; i += CHUNK_SIZE) {
    const chunk = ch2SubtopicsQuestions.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ch2SubtopicsQuestions.length} questions to Firestore! Chapter 2 Real Numbers now has full 80Q packs across EVERY subtopic!`);
}

main().catch(console.error);
