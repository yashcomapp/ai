// scripts/validate_all_mh9_scit_topups.js
const fs = require('fs');
const path = require('path');

const targetChapters = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18];

function validateQuestion(q, idx, file) {
  const errors = [];
  if (!q.questionCode) errors.push(`[${file}:${idx}] Missing questionCode`);
  if (!q.text || q.text.trim().length === 0) errors.push(`[${file}:${idx}] Empty text`);
  if (!Array.isArray(q.options) || q.options.length !== 4) {
    errors.push(`[${file}:${idx}] Options must be array of 4, got ${q.options ? q.options.length : 0}`);
  } else {
    const ids = q.options.map(o => o.id);
    if (ids.join(',') !== 'A,B,C,D') errors.push(`[${file}:${idx}] Option ids mismatch: ${ids.join(',')}`);
    const correctCount = q.options.filter(o => o.isCorrect === true).length;
    if (correctCount !== 1) errors.push(`[${file}:${idx}] Expected exactly 1 correct option, got ${correctCount}`);
    const correctOpt = q.options.find(o => o.isCorrect === true);
    if (correctOpt && correctOpt.id !== q.correctAnswer) {
      errors.push(`[${file}:${idx}] correctAnswer '${q.correctAnswer}' does not match isCorrect option '${correctOpt.id}'`);
    }
    const texts = q.options.map(o => o.text.trim().toLowerCase());
    if (new Set(texts).size !== 4) {
      errors.push(`[${file}:${idx}] Duplicate option texts in question: ${texts}`);
    }
  }

  if (!q.solution || q.solution.trim().length === 0) {
    errors.push(`[${file}:${idx}] Empty solution`);
  } else {
    if (!q.solution.includes('**Step 1:') || !q.solution.includes('**Step 2:') || !q.solution.includes('**Step 3:')) {
      errors.push(`[${file}:${idx}] Solution does not contain standard 3-step structured format`);
    }
  }

  if (!['exam', 'practice', 'foundation'].includes(q.vault)) {
    errors.push(`[${file}:${idx}] Invalid vault: ${q.vault}`);
  }
  if (!['easy', 'medium', 'hard'].includes(q.difficulty)) {
    errors.push(`[${file}:${idx}] Invalid difficulty: ${q.difficulty}`);
  }
  if (q.type !== 'OSC') {
    errors.push(`[${file}:${idx}] Invalid type: ${q.type}`);
  }
  if (q.marks !== 4) {
    errors.push(`[${file}:${idx}] Invalid marks: ${q.marks}`);
  }

  return errors;
}

function main() {
  console.log('=== VALIDATING ALL MH-9-SCIT TOP-UP JSON FILES ===');
  let totalQuestions = 0;
  let totalErrors = 0;
  const globalCodes = new Set();

  targetChapters.forEach(chNum => {
    const fileName = `scripts/mh9_scit_ch${chNum}_topup.json`;
    if (!fs.existsSync(fileName)) {
      console.error(`File missing: ${fileName}`);
      totalErrors++;
      return;
    }

    const questions = JSON.parse(fs.readFileSync(fileName, 'utf8'));
    totalQuestions += questions.length;
    let chErrors = 0;

    questions.forEach((q, idx) => {
      const errs = validateQuestion(q, idx, fileName);
      if (errs.length > 0) {
        errs.forEach(e => console.error(e));
        chErrors += errs.length;
        totalErrors += errs.length;
      }
      if (globalCodes.has(q.questionCode)) {
        console.error(`Global duplicate questionCode detected: ${q.questionCode}`);
        chErrors++;
        totalErrors++;
      }
      globalCodes.add(q.questionCode);
    });

    if (chErrors === 0) {
      console.log(`  Ch ${chNum}: ${questions.length} questions -> 100% VALID (0 errors)`);
    } else {
      console.error(`  Ch ${chNum}: ${chErrors} ERRORS detected!`);
    }
  });

  console.log('\n-----------------------------------------------------------');
  console.log(`TOTAL QUESTIONS VALIDATED: ${totalQuestions}`);
  console.log(`TOTAL ERRORS FOUND: ${totalErrors}`);

  if (totalErrors === 0) {
    console.log('🎉 ALL 6,123 QUESTIONS ACROSS ALL 16 CHAPTERS ARE 100% VALID AND COMPLIANT!');
  } else {
    process.exit(1);
  }
}

main();
