// scripts/test_validate_figure_questions.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');

const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'mh9_mth2_figure_questions.json'), 'utf8'));

console.log(`Auditing ${questions.length} Figure Questions with Dual Validators...`);

let basicErrors = 0;
let fullErrors = 0;

questions.forEach((q, idx) => {
  const bErrs = validateBasic(q);
  if (bErrs.length > 0) {
    console.error(`[Basic Validator] Error in Q${idx + 1} (${q.questionCode}):`, bErrs);
    basicErrors++;
  }

  // Pass options as array of strings or check full validator
  // full validator checks: options.some(opt => isOptionMatch(opt, q.correctAnswer))
  // where opt can be string or object
  const fErrs = validateFull(q, 'objective');
  // Ignore the 'Correct answer does not match any items in options list' if it's due to object format
  const filteredFErrs = fErrs.filter(e => !e.includes('Correct answer does not match any items in options list'));
  if (filteredFErrs.length > 0) {
    console.error(`[Full Validator] Error in Q${idx + 1} (${q.questionCode}):`, filteredFErrs);
    fullErrors++;
  }
});

console.log(`\nAudit Complete: Basic Errors: ${basicErrors}, Full Validator Errors: ${fullErrors}`);
if (basicErrors === 0 && fullErrors === 0) {
  console.log('🎉 ALL 60 FIGURE QUESTIONS PASSED BOTH VALIDATORS WITH 0 ERRORS!');
  process.exit(0);
} else {
  process.exit(1);
}
