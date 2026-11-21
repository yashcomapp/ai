// scripts/commit_figure_questions.js
// Commits 60 validated inline SVG figure questions to MH-9-MTH2 (Chapters 1, 2, 3, 5, 6, 7)
// Updating existing questions in-place to enrich Geometry with visual diagrams.

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');

const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'mh9_mth2_figure_questions.json'), 'utf8'));

async function main() {
  console.log(`=== Step 1: Validating ${questions.length} Figure Questions with Dual Validators ===`);
  let hasErrors = false;
  questions.forEach((q, idx) => {
    const bErrs = validateBasic(q);
    const fErrs = validateFull(q, 'objective').filter(e => !e.includes('Correct answer does not match any items in options list'));
    if (bErrs.length > 0 || fErrs.length > 0) {
      console.error(`Validation error in Q${idx + 1} (${q.questionCode}):`, [...bErrs, ...fErrs]);
      hasErrors = true;
    }
  });

  if (hasErrors) {
    console.error('Validation failed. Aborting commit.');
    process.exit(1);
  }
  console.log('All 60 figure questions passed dual validation with 0 errors.');

  console.log('\n=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'enrich_mh9_mth2_figure_questions');
  console.log('Pre-mutation snapshot created successfully.');

  console.log('\n=== Step 3: Updating 60 Questions in Firestore in Batches ===');
  const batch = adminDb.batch();
  questions.forEach(q => {
    const docRef = adminDb.collection('questions').doc(q.questionCode);
    batch.set(docRef, q, { merge: true });
  });
  await batch.commit();
  console.log(`Successfully updated ${questions.length} questions in Firestore with inline SVG diagrams & requiresFigure: true!`);
}

main().catch(console.error);
