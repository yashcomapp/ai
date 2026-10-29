// scripts/build-ch2-gold.js
const fs = require('fs');
const path = require('path');

const rawQuestions = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_2_raw.json', 'utf8'));

const part1 = require('./ch2_part1.js');
const part2 = require('./ch2_part2.js');
const part3 = require('./ch2_part3.js');
const part4 = require('./ch2_part4.js');

const allEnhancedParts = [...part1, ...part2, ...part3, ...part4];

console.log(`Loaded ${rawQuestions.length} raw questions.`);
console.log(`Loaded ${allEnhancedParts.length} enhanced questions across 4 modules.`);

// Map by id
const enhancedMap = new Map();
allEnhancedParts.forEach(q => {
  enhancedMap.set(q.id, q);
});

// Also support zero-padded or slight ID variations if needed
const mergedList = [];
let missing = 0;
let errors = [];

for (let i = 0; i < rawQuestions.length; i++) {
  const raw = rawQuestions[i];
  let enhanced = enhancedMap.get(raw.id);

  // If not found by exact ID, try alternative pattern
  if (!enhanced) {
    // Try matching by index if ID had extra zero like OSC-0104
    enhanced = allEnhancedParts[i];
  }

  if (!enhanced) {
    console.error(`Missing enhancement for raw question: ${raw.id} (index ${i})`);
    missing++;
    continue;
  }

  // Strict Validation Checks
  if (!enhanced.text || enhanced.text.trim().length === 0) {
    errors.push(`[${raw.id}] Empty text!`);
  }
  if (enhanced.text.includes('---')) {
    errors.push(`[${raw.id}] Text contains placeholder dashes '---'!`);
  }
  if (!Array.isArray(enhanced.options) || enhanced.options.length !== 4) {
    errors.push(`[${raw.id}] Options count is not 4! Has: ${enhanced.options ? enhanced.options.length : 0}`);
  }
  if (!['A', 'B', 'C', 'D'].includes(enhanced.correctAnswer)) {
    errors.push(`[${raw.id}] Invalid correctAnswer: ${enhanced.correctAnswer}`);
  }
  if (!enhanced.solution || !enhanced.solution.includes('### 1.') || !enhanced.solution.includes('### 2.') || !enhanced.solution.includes('### 3.')) {
    errors.push(`[${raw.id}] Solution is missing one or more of the 3 required gold-standard sections!`);
  }
  enhanced.options.forEach((opt, optIdx) => {
    if (!opt || opt.trim().length === 0) {
      errors.push(`[${raw.id}] Option ${optIdx} is empty!`);
    }
    if (opt.includes('None of above') || opt.includes('None of the above') || opt.includes('Wrong:') || opt.includes('Right:')) {
      errors.push(`[${raw.id}] Option ${optIdx} contains banned filler or teacher note: "${opt}"`);
    }
  });

  const merged = {
    ...raw,
    text: enhanced.text.trim(),
    options: enhanced.options.map(o => o.trim()),
    correctAnswer: enhanced.correctAnswer,
    solution: enhanced.solution.trim(),
    isEnhanced: true,
    enhancedAt: new Date().toISOString()
  };

  mergedList.push(merged);
}

if (missing > 0 || errors.length > 0) {
  console.error(`Validation failed with ${missing} missing questions and ${errors.length} errors:`);
  errors.forEach(e => console.error(e));
  process.exit(1);
}

console.log(`Validation PASSED for all ${mergedList.length} questions!`);

// Save to backups/staging/mh9_scit_2_enhanced.json
fs.writeFileSync('backups/staging/mh9_scit_2_enhanced.json', JSON.stringify(mergedList, null, 2), 'utf8');
console.log(`Saved enhanced dataset to backups/staging/mh9_scit_2_enhanced.json (${fs.statSync('backups/staging/mh9_scit_2_enhanced.json').size} bytes).`);
