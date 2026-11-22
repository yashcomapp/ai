const fs = require('fs');
const path = require('path');
const { validateQuestion } = require('./question_validator.js');

const ch6File = path.join(__dirname, 'clean_cbse9_scie_ch6_questions.json');
const questions = JSON.parse(fs.readFileSync(ch6File, 'utf8'));

console.log(`Validating ${questions.length} questions for Chapter 6...`);

let totalErrors = 0;
const topicCounts = {};
const vaultCounts = {};

questions.forEach((q, idx) => {
  const errs = validateQuestion(q);
  topicCounts[q.topicCode] = (topicCounts[q.topicCode] || 0) + 1;
  const vKey = `${q.topicCode}::${q.vault}`;
  vaultCounts[vKey] = (vaultCounts[vKey] || 0) + 1;

  if (errs.length > 0) {
    totalErrors++;
    console.error(`Question ${idx + 1} (${q.questionCode}) errors:`, errs);
  }
});

console.log('\nSubtopic Question Counts:');
for (const [tc, cnt] of Object.entries(topicCounts).sort()) {
  console.log(`  ${tc}: ${cnt}`);
  console.log(`    Exam: ${vaultCounts[`${tc}::exam`] || 0}, Practice: ${vaultCounts[`${tc}::practice`] || 0}, Foundation: ${vaultCounts[`${tc}::foundation`] || 0}`);
}

if (totalErrors === 0) {
  console.log(`\nSUCCESS: All ${questions.length} questions passed strict validation with 0 errors!`);
} else {
  console.error(`\nFAILED: Found ${totalErrors} invalid questions!`);
  process.exit(1);
}
