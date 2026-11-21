// scripts/commit_all_enriched_figures.js
// Commits 5,366 validated questions to MH-9-MTH2 (Chapters 1 to 9)
// Enriches Geometry with 3,220 (60.0%) inline SVG figure questions across all 68 subtopics.

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');

const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'mh9_mth2_all_figures_enriched.json'), 'utf8'));

async function main() {
  console.log(`=== Step 1: Pre-Flight Validation of all ${questions.length} Questions ===`);
  let hasErrors = false;
  let figCount = 0;

  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    if (q.requiresFigure) figCount++;

    const bErrs = validateBasic(q);
    const fErrs = validateFull(q, 'objective');

    if (bErrs.length > 0 || fErrs.length > 0) {
      console.error(`Validation Error in Q${i + 1} (${q.questionCode}):`, [...bErrs, ...fErrs]);
      hasErrors = true;
      break;
    }
  }

  if (hasErrors) {
    console.error('Validation failed. Aborting commit.');
    process.exit(1);
  }
  console.log(`✓ All ${questions.length} questions passed dual validation with 0 errors!`);
  console.log(`✓ Questions with inline figures: ${figCount} (${((figCount / questions.length) * 100).toFixed(1)}%)`);

  console.log('\n=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'enrich_mh9_mth2_3220_figures');
  console.log('✓ Pre-mutation snapshot created successfully.');

  console.log(`\n=== Step 3: Batch Committing ${questions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 450;
  const totalChunks = Math.ceil(questions.length / CHUNK_SIZE);

  for (let c = 0; c < totalChunks; c++) {
    const chunk = questions.slice(c * CHUNK_SIZE, (c + 1) * CHUNK_SIZE);
    const batch = adminDb.batch();

    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q, { merge: true });
    });

    await batch.commit();
    console.log(`  ✓ Committed batch ${c + 1}/${totalChunks} (${chunk.length} questions, total so far: ${(c + 1) * CHUNK_SIZE > questions.length ? questions.length : (c + 1) * CHUNK_SIZE})`);
  }

  console.log('\n=== Step 4: Verification in Firestore ===');
  const snap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MTH2')
    .where('class', '==', '9')
    .where('requiresFigure', '==', true)
    .get();

  console.log(`✓ Firestore verified: ${snap.size} figure-based questions now active for MH-9-MTH2!`);
}

main().catch(err => {
  console.error('Commit failed:', err);
  process.exit(1);
});
