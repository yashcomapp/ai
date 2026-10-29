// scripts/build-ch9-gold.js
// Merges Part 1 (89), Part 2 (99), Part 3 (92), and Part 4 (94) for Chapter 9 Environmental Management (374 questions)
// and runs full 5-Tier Quality Gate Linter before saving to staging.

const fs = require('fs');
const { ch9_part1 } = require('./ch9_part1.js');
const { ch9_part2 } = require('./ch9_part2.js');
const { ch9_part3 } = require('./ch9_part3.js');
const { ch9_part4 } = require('./ch9_part4.js');

console.log('--- Merging Chapter 9 Questions ---');
console.log(`Part 1: ${ch9_part1.length} questions`);
console.log(`Part 2: ${ch9_part2.length} questions`);
console.log(`Part 3: ${ch9_part3.length} questions`);
console.log(`Part 4: ${ch9_part4.length} questions`);

const allQuestions = [...ch9_part1, ...ch9_part2, ...ch9_part3, ...ch9_part4];
console.log(`Total Merged: ${allQuestions.length} questions`);

if (allQuestions.length !== 374) {
  console.error(`ERROR: Expected 374 questions, got ${allQuestions.length}`);
  process.exit(1);
}

// 5-Tier Quality Gate Linter
console.log('\n--- Running 5-Tier Quality Gate Linter ---');
let errorCount = 0;
const prohibitedPhrases = [
  /none of the above/i,
  /all of the above/i,
  /all of these/i,
  /none of these/i,
  /both a and b above/i
];

allQuestions.forEach((q, idx) => {
  const qNum = idx + 1;
  const prefix = `[Q${qNum} - ${q.questionCode}]`;

  // 1. Structure Check
  if (!q.questionCode || !q.type || !q.text || !q.solution || !q.options) {
    console.error(`${prefix} Missing fundamental fields`);
    errorCount++;
  }

  // 2. 3-Part Solution Headers
  if (!q.solution.includes('### 1.') || !q.solution.includes('### 2.') || !q.solution.includes('### 3.')) {
    console.error(`${prefix} Missing one or more required 3-part headers`);
    errorCount++;
  }

  // 3. Prohibited Catch-All Phrases in Options
  q.options.forEach((opt, optIdx) => {
    prohibitedPhrases.forEach(p => {
      if (p.test(opt)) {
        console.error(`${prefix} Option ${optIdx} contains prohibited catch-all: "${opt}"`);
        errorCount++;
      }
    });
  });

  // 4. Leaked Teacher Notes Check
  if (/Wrong:/i.test(q.solution) || /Right:/i.test(q.solution) || /Placeholder/i.test(q.solution)) {
    console.error(`${prefix} Leaked teacher notes detected`);
    errorCount++;
  }

  // 5. KaTeX Balance Check
  const openParen = (q.solution.match(/\\\(/g) || []).length;
  const closeParen = (q.solution.match(/\\\)/g) || []).length;
  if (openParen !== closeParen) {
    console.error(`${prefix} Unbalanced inline KaTeX: ${openParen} open vs ${closeParen} close`);
    errorCount++;
  }

  const openBracket = (q.solution.match(/\\\[/g) || []).length;
  const closeBracket = (q.solution.match(/\\\]/g) || []).length;
  if (openBracket !== closeBracket) {
    console.error(`${prefix} Unbalanced display KaTeX: ${openBracket} open vs ${closeBracket} close`);
    errorCount++;
  }

  // 6. Step 3 Answer Alignment
  if (q.type === 'OSC' || q.type === 'OAR') {
    const letter = q.correctAnswer;
    const regex = new RegExp(`Option ${letter} is correct`, 'i');
    if (!regex.test(q.solution)) {
      console.warn(`${prefix} Step 3 might not explicitly reference "Option ${letter} is correct"`);
    }
  } else if (q.type === 'OTF') {
    const isTrue = q.correctAnswer === 'True';
    const expected = isTrue ? /True/i : /False/i;
    if (!expected.test(q.solution)) {
      console.warn(`${prefix} Step 3 might not explicitly reference "${q.correctAnswer}"`);
    }
  }
});

if (errorCount > 0) {
  console.error(`\nFAILED: Quality Gate detected ${errorCount} errors. Staging aborted.`);
  process.exit(1);
}

console.log('SUCCESS: All 374 questions passed 5-Tier Quality Gate with 0 errors!\n');

// Save to staging
const stagingPath = 'backups/staging/mh9_scit_9_enhanced.json';
fs.writeFileSync(stagingPath, JSON.stringify(allQuestions, null, 2), 'utf8');
console.log(`Saved enhanced dataset to: ${stagingPath}`);
