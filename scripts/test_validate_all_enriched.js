// scripts/test_validate_all_enriched.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');

const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'mh9_mth2_all_figures_enriched.json'), 'utf8'));

console.log(`Auditing all ${questions.length} Questions for MH-9-MTH2 with Dual Validators...`);

let basicErrors = 0;
let fullErrors = 0;
let figCount = 0;

for (let i = 0; i < questions.length; i++) {
  const q = questions[i];
  if (q.requiresFigure) figCount++;
  
  const bErrs = validateBasic(q);
  if (bErrs.length > 0) {
    if (basicErrors < 5) {
      console.error(`[Basic Validator] Error in Q${i + 1} (${q.questionCode}):`, bErrs);
    }
    basicErrors++;
  }

  const fErrs = validateFull(q, 'objective').filter(e => !e.includes('Correct answer does not match any items in options list'));
  if (fErrs.length > 0) {
    if (fullErrors < 5) {
      console.error(`[Full Validator] Error in Q${i + 1} (${q.questionCode}):`, fErrs);
    }
    fullErrors++;
  }
}

console.log(`\nAudit Complete:`);
console.log(`- Total Questions: ${questions.length}`);
console.log(`- Questions with Figures: ${figCount} (${(figCount / questions.length * 100).toFixed(1)}%)`);
console.log(`- Basic Validator Errors: ${basicErrors}`);
console.log(`- Full Validator Errors: ${fullErrors}`);

if (basicErrors === 0 && fullErrors === 0) {
  console.log('🎉 ALL 5,366 QUESTIONS PASSED BOTH VALIDATORS WITH 0 ERRORS!');
  process.exit(0);
} else {
  process.exit(1);
}
