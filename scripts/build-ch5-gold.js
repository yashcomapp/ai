// scripts/build-ch5-gold.js
// Merges all 4 parts of Chapter 5 (122 questions), runs 5-Tier Quality Gate Linter, and outputs backups/staging/mh9_scit_5_enhanced.json

const fs = require('fs');
const path = require('path');

const rawFile = path.resolve(__dirname, '../backups/staging/mh9_scit_5_raw.json');
const outFile = path.resolve(__dirname, '../backups/staging/mh9_scit_5_enhanced.json');

console.log('=== Step 1: Loading all 4 parts of Chapter 5 ===');
const p1 = require('./ch5_part1.js').ch5_part1;
const p2 = require('./ch5_part2.js').ch5_part2;
const p3 = require('./ch5_part3.js').ch5_part3;
const p4 = require('./ch5_part4.js').ch5_part4;

const enhancedParts = [...p1, ...p2, ...p3, ...p4];
console.log(`Loaded ${enhancedParts.length} enhanced questions across 4 parts.`);

const enhancedMap = new Map();
for (const q of enhancedParts) {
  if (enhancedMap.has(q.questionCode)) {
    throw new Error(`FATAL: Duplicate questionCode in parts: ${q.questionCode}`);
  }
  enhancedMap.set(q.questionCode, q);
}

console.log('=== Step 2: Merging with Raw Database Metadata ===');
const rawQuestions = JSON.parse(fs.readFileSync(rawFile, 'utf8'));
console.log(`Loaded ${rawQuestions.length} raw questions from ${rawFile}`);

if (rawQuestions.length !== 122) {
  throw new Error(`Expected 122 raw questions, got ${rawQuestions.length}`);
}

const mergedQuestions = [];
for (const raw of rawQuestions) {
  const enh = enhancedMap.get(raw.questionCode);
  if (!enh) {
    throw new Error(`Missing enhanced data for questionCode: ${raw.questionCode}`);
  }

  const merged = {
    ...raw,
    text: enh.text,
    options: enh.options,
    correctAnswer: enh.correctAnswer,
    solution: enh.solution,
    isEnhanced: true,
    enhancedAt: new Date().toISOString()
  };
  mergedQuestions.push(merged);
}

console.log(`Successfully merged ${mergedQuestions.length} questions.`);

console.log('=== Step 3: Running 5-Tier Quality Gate Linter ===');
let errors = [];

// Tier 1: Completeness
if (mergedQuestions.length !== 122) {
  errors.push(`Tier 1 Error: Expected 122 questions, got ${mergedQuestions.length}`);
}

mergedQuestions.forEach((q, idx) => {
  const code = q.questionCode;

  // Tier 2: 3-Part Solution
  const sol = q.solution || '';
  const hasPart1 = sol.includes('### 1. Scientific Principle');
  const hasPart2 = sol.includes('### 2. Physical Context');
  const hasPart3 = sol.includes('### 3. Step-by-Step Option');
  if (!hasPart1 || !hasPart2 || !hasPart3) {
    errors.push(`Tier 2 Error [${code}]: Incomplete 3-part headers (P1:${hasPart1}, P2:${hasPart2}, P3:${hasPart3})`);
  }
  if (sol.length < 300) {
    errors.push(`Tier 2 Error [${code}]: Solution too short (${sol.length} chars)`);
  }

  // Tier 3: Distractor Integrity
  if (!Array.isArray(q.options) || q.options.length !== 4) {
    errors.push(`Tier 3 Error [${code}]: Invalid options array length: ${q.options ? q.options.length : 0}`);
  } else {
    q.options.forEach((opt, oIdx) => {
      const lower = opt.toLowerCase();
      if (lower.includes('none of above') || lower.includes('none of the above') || lower.includes('all of above') || lower.includes('all of the above')) {
        errors.push(`Tier 3 Error [${code}]: Option ${oIdx} contains forbidden catch-all: "${opt}"`);
      }
      if (/^option\s+[a-d]$/i.test(opt.trim())) {
        errors.push(`Tier 3 Error [${code}]: Option ${oIdx} contains placeholder: "${opt}"`);
      }
      if (opt.includes('Wrong:') || opt.includes('Right:')) {
        errors.push(`Tier 3 Error [${code}]: Option ${oIdx} contains leaked teacher notes: "${opt}"`);
      }
    });

    // Check duplicate options
    const optSet = new Set(q.options.map(o => o.trim().toLowerCase()));
    if (optSet.size !== q.options.length) {
      errors.push(`Tier 3 Error [${code}]: Contains duplicate options: ${JSON.stringify(q.options)}`);
    }
  }

  if (q.text.includes('---') || (q.text.includes('___') && !q.text.includes('\\_'))) {
    errors.push(`Tier 3 Error [${code}]: Question text contains fill-in blanks dash/underscores: "${q.text.slice(0, 40)}"`);
  }

  if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) {
    errors.push(`Tier 3 Error [${code}]: Invalid correctAnswer: "${q.correctAnswer}"`);
  }

  // Check Step 3 confirmation of correctAnswer
  const step3 = sol.slice(sol.indexOf('### 3.'));
  const lines = step3.split('\n');
  const targetLine = lines.find(l => l.includes('Option ' + q.correctAnswer));
  if (!targetLine || (!targetLine.toLowerCase().includes('correct') && !targetLine.toLowerCase().includes('true'))) {
    errors.push(`Tier 3 Error [${code}]: Step 3 does not confirm Option ${q.correctAnswer} as correct`);
  }

  // Tier 4: KaTeX Balance
  const checkKaTeX = (str, fieldName) => {
    const openInline = (str.match(/\\\(/g) || []).length;
    const closeInline = (str.match(/\\\)/g) || []).length;
    if (openInline !== closeInline) {
      errors.push(`Tier 4 Error [${code}]: Unbalanced inline KaTeX in ${fieldName} (open:${openInline}, close:${closeInline})`);
    }

    const openDisplay = (str.match(/\\\[/g) || []).length;
    const closeDisplay = (str.match(/\\\]/g) || []).length;
    if (openDisplay !== closeDisplay) {
      errors.push(`Tier 4 Error [${code}]: Unbalanced display KaTeX in ${fieldName} (open:${openDisplay}, close:${closeDisplay})`);
    }
  };

  checkKaTeX(q.text, 'text');
  q.options.forEach((opt, oIdx) => checkKaTeX(opt, `options[${oIdx}]`));
  checkKaTeX(q.solution, 'solution');
});

if (errors.length > 0) {
  console.error(`\n❌ QUALITY GATE FAILED with ${errors.length} errors:`);
  errors.slice(0, 20).forEach(e => console.error('  - ' + e));
  if (errors.length > 20) console.error(`  ... and ${errors.length - 20} more errors.`);
  process.exit(1);
}

console.log('✅ 5-Tier Quality Gate Passed 100%! Zero errors detected.');

console.log(`=== Step 4: Writing Staging File to ${outFile} ===`);
fs.writeFileSync(outFile, JSON.stringify(mergedQuestions, null, 2), 'utf8');
console.log(`✅ Written ${mergedQuestions.length} enhanced questions to ${outFile}`);
