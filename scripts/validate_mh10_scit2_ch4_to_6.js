const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'audit_data', 'mh10_scit2_ch4_to_6_generated.json');
const questions = JSON.parse(fs.readFileSync(filePath, 'utf8'));

console.log(`Validating ${questions.length} questions for MH-10-SCIT2 Ch 4-6...`);

let errors = 0;
const seenCodes = new Set();
let svgCount = 0;

questions.forEach((q, idx) => {
  if (!q.questionCode || !q.topicCode || !q.text || !q.options || !q.correctAnswer || !q.solution) {
    console.error(`[Error] Missing core fields at idx ${idx}: ${q.questionCode}`);
    errors++;
  }

  if (q.text.includes('<svg')) svgCount++;

  if (seenCodes.has(q.questionCode)) {
    console.error(`[Error] Duplicate questionCode: ${q.questionCode}`);
    errors++;
  }
  seenCodes.add(q.questionCode);

  if (!Array.isArray(q.options) || q.options.length !== 4) {
    console.error(`[Error] Options length !== 4 in ${q.questionCode}`);
    errors++;
  }

  const optTexts = new Set();
  let correctCount = 0;

  q.options.forEach(opt => {
    const txt = (typeof opt === 'string' ? opt : opt.text).trim().toLowerCase();
    if (optTexts.has(txt)) {
      console.error(`[Error] Duplicate option in ${q.questionCode}: "${opt.text}"`);
      errors++;
    }
    optTexts.add(txt);
    if (opt.isCorrect) correctCount++;
  });

  if (correctCount !== 1) {
    console.error(`[Error] Question ${q.questionCode} has ${correctCount} correct options`);
    errors++;
  }

  const corrOpt = q.options.find(o => o.id === q.correctAnswer);
  if (!corrOpt || !corrOpt.isCorrect) {
    console.error(`[Error] correctAnswer mismatch in ${q.questionCode}`);
    errors++;
  }

  if (!q.solution.includes('Step 1') || !q.solution.includes('Step 2') || !q.solution.includes('Step 3')) {
    console.error(`[Error] Solution missing 3-step structure in ${q.questionCode}`);
    errors++;
  }
});

console.log(`Inline vector SVG count in questions: ${svgCount}`);

if (errors === 0) {
  console.log(`✅ All ${questions.length} questions PASSED validation with 0 errors!`);
} else {
  console.error(`❌ Validation failed with ${errors} errors.`);
  process.exit(1);
}
