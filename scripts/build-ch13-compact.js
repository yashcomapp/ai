/**
 * build-ch13-compact.js
 * Quality Gate Linter for Chapter 13 (Carbon) - Compact Format.
 */

const fs = require('fs');

console.log('--- RUNNING CHAPTER 13 COMPACT QUALITY GATE LINTER ---');

const enhancedQuestions = require('./ch13_all.js');
console.log(`Loaded ${enhancedQuestions.length} questions from ch13_all.js`);

let errors = [];
let warnings = [];

// Tier 1: Count Validation
if (enhancedQuestions.length !== 79) {
  errors.push(`Tier 1 Error: Expected exactly 79 questions, found ${enhancedQuestions.length}`);
}

const REQUIRED_HEADERS = [
  '**Key Concept:**',
  '**Option Analysis:**'
];

const FORBIDDEN_HEADERS = [
  '### 1. Scientific Principle',
  '### 2. Ray Optics',
  '### 2. Wave Dynamics'
];

const CATCH_ALL_PATTERNS = [
  /none of the above/i,
  /none of above/i,
  /all of the above/i,
  /all of above/i,
  /all the above/i,
  /none of these/i,
  /all of these/i,
  /option\s+[1-4]/i,
  /option\s+[a-d]/i
];

const TEACHER_NOTE_PATTERNS = [
  /wrong\s*:/i,
  /right\s*:/i
];

enhancedQuestions.forEach((q, idx) => {
  const qNum = idx + 1;
  const qCode = q.questionCode || `Q#${qNum}`;
  const sol = q.solution || '';

  // Tier 2: Compact Format Check
  for (const header of REQUIRED_HEADERS) {
    if (!sol.includes(header)) {
      errors.push(`Tier 2 Error [${qCode}]: Missing required compact header: "${header}"`);
    }
  }

  for (const fHeader of FORBIDDEN_HEADERS) {
    if (sol.includes(fHeader)) {
      errors.push(`Tier 2 Error [${qCode}]: Contains deprecated header: "${fHeader}"`);
    }
  }

  // Tier 3: Quality Checks (Catch-alls, Leaks, Option Counts)
  const opts = q.options || [];
  if (opts.length !== 4) {
    errors.push(`Tier 3 Error [${qCode}]: Expected exactly 4 options, found ${opts.length}`);
  }

  opts.forEach((opt, oi) => {
    const optStr = String(opt);
    for (const pat of CATCH_ALL_PATTERNS) {
      if (pat.test(optStr)) {
        errors.push(`Tier 3 Error [${qCode}]: Option ${String.fromCharCode(65 + oi)} contains forbidden pattern: "${optStr}"`);
      }
    }
    for (const pat of TEACHER_NOTE_PATTERNS) {
      if (pat.test(optStr)) {
        errors.push(`Tier 3 Error [${qCode}]: Option ${String.fromCharCode(65 + oi)} contains leaked note: "${optStr}"`);
      }
    }
  });

  // KaTeX balance
  const inlineOpen = (sol.match(/\\\(/g) || []).length;
  const inlineClose = (sol.match(/\\\)/g) || []).length;
  if (inlineOpen !== inlineClose) {
    errors.push(`Tier 3 Error [${qCode}]: Unbalanced KaTeX inline math delimiters: ${inlineOpen} open vs ${inlineClose} close`);
  }
  const displayOpen = (sol.match(/\\\[/g) || []).length;
  const displayClose = (sol.match(/\\\]/g) || []).length;
  if (displayOpen !== displayClose) {
    errors.push(`Tier 3 Error [${qCode}]: Unbalanced KaTeX display math delimiters: ${displayOpen} open vs ${displayClose} close`);
  }

  // Tier 4: Answer Alignment
  const ans = q.correctAnswer;
  if (!['A', 'B', 'C', 'D'].includes(ans)) {
    errors.push(`Tier 4 Error [${qCode}]: Invalid correctAnswer "${ans}"`);
  }

  const optionAnalysisIdx = sol.indexOf('**Option Analysis:**');
  if (optionAnalysisIdx !== -1) {
    const optText = sol.substring(optionAnalysisIdx);
    const correctRegex = new RegExp(`\\*\\*\\(${ans}\\)[^\\n]*\\(Correct`, 'i');
    if (!correctRegex.test(optText)) {
      errors.push(`Tier 4 Error [${qCode}]: Option Analysis does not explicitly mark "(${ans})" as (Correct)`);
    }
  }

  // Tier 5: Integrity
  if (!q.text || q.text.trim().length < 10) {
    errors.push(`Tier 5 Error [${qCode}]: Question text too short or empty`);
  }
  if (!q.topicCode || !q.topicCode.startsWith('MH-9-SCIT-13')) {
    errors.push(`Tier 5 Error [${qCode}]: Invalid topicCode: "${q.topicCode}"`);
  }
});

console.log(`\nLinter completed.`);
console.log(`Errors found: ${errors.length}`);
console.log(`Warnings found: ${warnings.length}`);

if (errors.length > 0) {
  console.error('\nLINTER FAILED WITH ERRORS:');
  errors.forEach((err, i) => console.error(`  ${i + 1}. ${err}`));
  process.exit(1);
} else {
  console.log('\n>>> ALL 79 QUESTIONS PASSED THE COMPACT QUALITY GATE LINTER WITH 100% SUCCESS! <<<');
  fs.writeFileSync('backups/staging/mh9_scit_13_enhanced.json', JSON.stringify(enhancedQuestions, null, 2), 'utf8');
}
