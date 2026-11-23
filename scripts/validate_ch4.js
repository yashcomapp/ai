const fs = require('fs');
const path = require('path');
const { validateQuestion } = require('./question_validator.js');

const ch4File = path.join(__dirname, 'clean_cbse9_scie_ch4_questions.json');
const questions = JSON.parse(fs.readFileSync(ch4File, 'utf8'));

console.log(`Validating ${questions.length} questions for Chapter 4...`);

let totalErrors = 0;
const topicCounts = {};

questions.forEach((q, idx) => {
  const errs = validateQuestion(q);
  topicCounts[q.topicCode] = (topicCounts[q.topicCode] || 0) + 1;
  if (errs.length > 0) {
    totalErrors++;
    console.error(`Question ${idx + 1} (${q.questionCode}) errors:`, errs);
  }
});

console.log('\nSubtopic Question Counts:');
for (const [tc, cnt] of Object.entries(topicCounts).sort()) {
  console.log(`  ${tc}: ${cnt}`);
}

if (totalErrors === 0) {
  console.log(`\nSUCCESS: All ${questions.length} questions passed strict validation with 0 errors!`);
} else {
  console.error(`\nFAILED: Found ${totalErrors} invalid questions!`);
  process.exit(1);
}
