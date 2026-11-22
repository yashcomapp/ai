// scripts/assemble_and_validate_ch12.js
const fs = require('fs');
const path = require('path');

function validateQuestion(q, idx) {
  const errors = [];
  if (!q.questionCode) errors.push(`[${idx}] Missing questionCode`);
  if (!q.text || q.text.trim().length === 0) errors.push(`[${idx}] Empty text`);
  if (!Array.isArray(q.options) || q.options.length !== 4) {
    errors.push(`[${idx}] Options must be array of 4, got ${q.options ? q.options.length : 0}`);
  } else {
    const ids = q.options.map(o => o.id);
    if (ids.join(',') !== 'A,B,C,D') errors.push(`[${idx}] Option ids mismatch: ${ids.join(',')}`);
    const correctCount = q.options.filter(o => o.isCorrect === true).length;
    if (correctCount !== 1) errors.push(`[${idx}] Expected exactly 1 correct option, got ${correctCount}`);
    const correctOpt = q.options.find(o => o.isCorrect === true);
    if (correctOpt && correctOpt.id !== q.correctAnswer) {
      errors.push(`[${idx}] correctAnswer '${q.correctAnswer}' does not match isCorrect option '${correctOpt.id}'`);
    }
    const texts = q.options.map(o => o.text.trim().toLowerCase());
    if (new Set(texts).size !== 4) {
      errors.push(`[${idx}] Duplicate option texts in question: ${texts}`);
    }
  }

  if (!q.solution || q.solution.trim().length === 0) {
    errors.push(`[${idx}] Empty solution`);
  } else {
    if (!q.solution.includes('**Step 1:') || !q.solution.includes('**Step 2:') || !q.solution.includes('**Step 3:')) {
      errors.push(`[${idx}] Solution does not contain standard 3-step structured format`);
    }
  }

  if (!['exam', 'practice', 'foundation'].includes(q.vault)) {
    errors.push(`[${idx}] Invalid vault: ${q.vault}`);
  }
  if (!['easy', 'medium', 'hard'].includes(q.difficulty)) {
    errors.push(`[${idx}] Invalid difficulty: ${q.difficulty}`);
  }
  if (q.type !== 'OSC') {
    errors.push(`[${idx}] Invalid type: ${q.type}`);
  }
  if (q.marks !== 4) {
    errors.push(`[${idx}] Invalid marks: ${q.marks}`);
  }

  return errors;
}

function main() {
  console.log('=== ASSEMBLING AND VALIDATING CBSE-9-SCIE CHAPTER 12 QUESTIONS ===');

  const partA = JSON.parse(fs.readFileSync('scripts/cbse9_scie_ch12_part_a.json', 'utf-8'));
  const partB = JSON.parse(fs.readFileSync('scripts/cbse9_scie_ch12_part_b.json', 'utf-8'));

  console.log(`Loaded Part A: ${partA.length} questions`);
  console.log(`Loaded Part B: ${partB.length} questions`);

  const allQuestions = [...partA, ...partB];
  console.log(`Total questions assembled: ${allQuestions.length}`);

  if (allQuestions.length !== 560) {
    throw new Error(`Expected exactly 560 questions, got ${allQuestions.length}`);
  }

  let totalErrors = 0;
  const codes = new Set();
  const subtopicCounts = {};
  const vaultCounts = {};

  allQuestions.forEach((q, idx) => {
    const errs = validateQuestion(q, idx);
    if (errs.length > 0) {
      errs.forEach(e => console.error(e));
      totalErrors += errs.length;
    }
    if (codes.has(q.questionCode)) {
      console.error(`Duplicate questionCode: ${q.questionCode}`);
      totalErrors++;
    }
    codes.add(q.questionCode);

    subtopicCounts[q.topicCode] = (subtopicCounts[q.topicCode] || 0) + 1;
    const vKey = `${q.topicCode}-${q.vault}`;
    vaultCounts[vKey] = (vaultCounts[vKey] || 0) + 1;
  });

  console.log('\n--- SUBTOPIC BREAKDOWN (Target: 80 each, 40 exam / 20 practice / 20 foundation) ---');
  let quotaOk = true;
  Object.keys(subtopicCounts).sort().forEach(st => {
    const total = subtopicCounts[st];
    const exam = vaultCounts[`${st}-exam`] || 0;
    const practice = vaultCounts[`${st}-practice`] || 0;
    const foundation = vaultCounts[`${st}-foundation`] || 0;
    console.log(`${st}: ${total} Qs (Exam: ${exam}, Practice: ${practice}, Foundation: ${foundation})`);
    if (total !== 80 || exam !== 40 || practice !== 20 || foundation !== 20) {
      quotaOk = false;
      console.error(`❌ Quota mismatch for ${st}!`);
    }
  });

  if (!quotaOk) {
    throw new Error('Subtopic quota verification failed!');
  }

  if (totalErrors > 0) {
    throw new Error(`Validation failed with ${totalErrors} errors.`);
  }

  console.log('\n✅ ALL 560 QUESTIONS PASSED VALIDATION WITH 0 ERRORS!');

  const outFile = 'clean_cbse9_scie_ch12_questions.json';
  fs.writeFileSync(outFile, JSON.stringify(allQuestions, null, 2), 'utf-8');
  console.log(`Saved assembled questions to ${outFile}`);
}

main();
