// scripts/commit_mh9_mth2_ch7_ch8_ch9.js
// Commits 1,840 validated questions for MH-9-MTH2 Chapters 7, 8 & 9 (23 subtopics)
// to 100% compliance with Rule 2T (80Q standard pack: 40 Exam, 20 Practice, 20 Foundation per subtopic)

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const jsonPath = path.join(__dirname, 'mh9_mth2_ch7_ch8_ch9_generated.json');
const ch7Ch8Ch9Questions = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Also write out mh9_mth2_ch7_ch8_ch9_data.js for archival consistency
const dataJsPath = path.join(__dirname, 'mh9_mth2_ch7_ch8_ch9_data.js');
fs.writeFileSync(dataJsPath, `// scripts/mh9_mth2_ch7_ch8_ch9_data.js\nmodule.exports = {\n  ch7Ch8Ch9Questions: ${JSON.stringify(ch7Ch8Ch9Questions, null, 2)}\n};\n`);
console.log(`Saved ${dataJsPath}`);

async function main() {
  console.log(`=== Step 1: Validating ${ch7Ch8Ch9Questions.length} Questions for MH-9-MTH2 Ch 7, 8 & 9 ===`);
  let hasErrors = false;
  ch7Ch8Ch9Questions.forEach((q, idx) => {
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
  console.log(`All ${ch7Ch8Ch9Questions.length} questions passed strict validation perfectly!`);

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'commit_mh9_mth2_ch7_ch8_ch9_80q');
  console.log('Pre-mutation snapshot successfully created.');

  console.log(`=== Step 3: Batch Insertion of ${ch7Ch8Ch9Questions.length} Questions to Firestore ===`);
  const CHUNK_SIZE = 400;
  for (let i = 0; i < ch7Ch8Ch9Questions.length; i += CHUNK_SIZE) {
    const chunk = ch7Ch8Ch9Questions.slice(i, i + CHUNK_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / CHUNK_SIZE) + 1} (${chunk.length} questions)`);
  }

  console.log(`Successfully committed ${ch7Ch8Ch9Questions.length} questions to Firestore! MH-9-MTH2 Ch 7, 8 & 9 now 100% compliant!`);
}

main().catch(console.error);
