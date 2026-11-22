const fs = require('fs');
const path = require('path');
const { validateQuestion } = require('./question_validator.js');

const partAFile = path.join(__dirname, 'cbse9_scie_ch9_part_a.json');
const partBFile = path.join(__dirname, 'cbse9_scie_ch9_part_b.json');
const outFile = path.join(__dirname, 'clean_cbse9_scie_ch9_questions.json');

const partA = JSON.parse(fs.readFileSync(partAFile, 'utf8'));
const partB = JSON.parse(fs.readFileSync(partBFile, 'utf8'));

console.log(`Part A count: ${partA.length}`);
console.log(`Part B count: ${partB.length}`);

const allQuestions = [...partA, ...partB];
console.log(`Total questions: ${allQuestions.length}`);

let totalErrors = 0;
const topicCounts = {};
const vaultCounts = {};

allQuestions.forEach((q, idx) => {
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
  fs.writeFileSync(outFile, JSON.stringify(allQuestions, null, 2), 'utf8');
  console.log(`\nSUCCESS: All ${allQuestions.length} questions passed strict validation with 0 errors!`);
  console.log(`Saved to ${outFile}`);
} else {
  console.error(`\nFAILED: Found ${totalErrors} invalid questions!`);
  process.exit(1);
}
