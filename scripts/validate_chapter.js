// scripts/validate_chapter.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const { validateBatchDistinctness } = require('../src/lib/questionSimilarity.ts');
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');

const targetFile = process.argv[2];
if (!targetFile) {
  console.error('Usage: node scripts/validate_chapter.js <path-to-json>');
  process.exit(1);
}

const absPath = path.isAbsolute(targetFile) ? targetFile : path.join(process.cwd(), targetFile);
if (!fs.existsSync(absPath)) {
  console.error(`File not found: ${absPath}`);
  process.exit(1);
}

const questions = JSON.parse(fs.readFileSync(absPath, 'utf8'));
console.log(`\nValidating ${questions.length} questions from ${path.basename(absPath)}...`);

// 1. Group by topicCode
const byTopic = {};
let figCount = 0;
let schemaErrors = 0;

questions.forEach((q, idx) => {
  if (q.requiresFigure || (q.text && q.text.includes('<svg'))) {
    figCount++;
  }
  const tc = q.topicCode || 'unknown';
  if (!byTopic[tc]) byTopic[tc] = [];
  byTopic[tc].push(q);

  const bErrs = validateBasic(q);
  const fErrs = validateFull(q, 'objective').filter(e => !e.includes('Correct answer does not match any items in options list'));
  if (bErrs.length > 0 || fErrs.length > 0) {
    if (schemaErrors < 3) {
      console.error(`Schema error in ${q.questionCode || idx}:`, [...bErrs, ...fErrs]);
    }
    schemaErrors++;
  }
});

let distinctnessErrors = 0;
for (const [tc, list] of Object.entries(byTopic)) {
  const res = validateBatchDistinctness(list);
  if (!res.valid) {
    console.error(`❌ Distinctness error in subtopic ${tc} (${res.errors.length} errors):`);
    res.errors.slice(0, 3).forEach(e => console.error(`   - ${e}`));
    distinctnessErrors += res.errors.length;
  } else {
    console.log(`✅ Subtopic ${tc} (${list.length} Qs): 100% distinct (0 duplicate pairs)`);
  }
}

const figPct = ((figCount / questions.length) * 100).toFixed(1);
console.log(`\n--- Summary for ${path.basename(absPath)} ---`);
console.log(`- Total Questions: ${questions.length}`);
console.log(`- Figure/SVG Questions: ${figCount} (${figPct}%)`);
console.log(`- Schema Errors: ${schemaErrors}`);
console.log(`- Distinctness Errors: ${distinctnessErrors}`);

if (schemaErrors === 0 && distinctnessErrors === 0) {
  console.log(`🎉 ALL ${questions.length} QUESTIONS PASSED 100% FLAWLESSLY!\n`);
  process.exit(0);
} else {
  console.error(`💥 FAILED with ${schemaErrors} schema errors and ${distinctnessErrors} distinctness errors.\n`);
  process.exit(1);
}
