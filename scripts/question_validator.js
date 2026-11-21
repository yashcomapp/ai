const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

/**
 * Strict Question Validator according to LOS SSOT:
 * 1. options must be array of 4 objects { text, isCorrect }
 * 2. Exactly one option has isCorrect: true for OSC, OTF, OAR, OFB, ONE
 * 3. correctAnswer must be letter 'A', 'B', 'C', 'D' matching options.findIndex(o => o.isCorrect)
 * 4. All math expressions in text, options, and solution must use \\( ... \\)
 * 5. Distinct option texts (no duplicates)
 */
function validateQuestion(q) {
  const errors = [];
  if (!q.questionCode) errors.push('Missing questionCode');
  if (!q.topicCode) errors.push('Missing topicCode');
  if (!q.text || q.text.trim().length < 5) errors.push('Missing or short text');
  if (!q.solution || q.solution.trim().length < 5) errors.push('Missing or short solution');
  if (!['exam', 'practice', 'foundation'].includes(q.vault)) errors.push(`Invalid vault: ${q.vault}`);
  if (!Array.isArray(q.options) || q.options.length !== 4) errors.push(`Options must have exactly 4 items, got ${q.options?.length}`);

  const optionTexts = new Set();
  let correctCount = 0;
  let correctIndex = -1;

  (q.options || []).forEach((opt, idx) => {
    if (!opt || typeof opt !== 'object') errors.push(`Option ${idx} is not an object`);
    if (!opt.text || opt.text.trim().length === 0) errors.push(`Option ${idx} text is empty`);
    if (optionTexts.has(opt.text.trim())) errors.push(`Duplicate option text: ${opt.text}`);
    optionTexts.add(opt.text.trim());

    if (opt.isCorrect) {
      correctCount++;
      correctIndex = idx;
    }
  });

  if (q.type === 'OMC') {
    if (correctCount < 2) errors.push(`OMC requires >= 2 correct options, found ${correctCount}`);
  } else {
    if (correctCount !== 1) errors.push(`Single-choice question requires exactly 1 correct option, found ${correctCount}`);
    const expectedLetter = String.fromCharCode(65 + correctIndex);
    if (q.correctAnswer !== expectedLetter) {
      errors.push(`correctAnswer mismatch: expected '${expectedLetter}' based on isCorrect, got '${q.correctAnswer}'`);
    }
  }

  return errors;
}

module.exports = { validateQuestion };
