const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { validateQuestion: validateBasic } = require('./question_validator.js');
const { validateQuestion: validateFull } = require('../src/lib/questionTypes.ts');
const qs = require('./mh9_mth2_ch1_perfect.json');

const errorCounts = {};
let count = 0;
for (const q of qs) {
  const bErrs = validateBasic(q);
  const fErrs = validateFull(q, 'objective').filter(e => !e.includes('Correct answer does not match any items in options list'));
  const allErrs = [...bErrs, ...fErrs];
  if (allErrs.length > 0) {
    count++;
    for (const err of allErrs) {
      errorCounts[err] = (errorCounts[err] || 0) + 1;
    }
  }
}
console.log('Total questions with schema errors:', count);
console.log('Error breakdown:');
for (const [err, cnt] of Object.entries(errorCounts)) {
  console.log(`  [${cnt} times]: ${err}`);
}
