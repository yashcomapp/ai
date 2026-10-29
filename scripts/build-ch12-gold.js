/**
 * build-ch12-gold.js
 * 5-Tier Quality Gate Linter and Validator for Chapter 12 (Study of Sound).
 */

const fs = require('fs');

console.log('--- RUNNING CHAPTER 12 GOLD QUALITY GATE LINTER ---');

const enhancedQuestions = require('./ch12_all.js');
console.log(`Loaded ${enhancedQuestions.length} questions from ch12_all.js`);

let errors = [];
let warnings = [];

// Tier 1: Total Count Validation
if (enhancedQuestions.length !== 114) {
  errors.push(`Tier 1 Error: Expected exactly 114 questions, found ${enhancedQuestions.length}`);
}

const REQUIRED_HEADERS = [
  '### 1. Scientific Principle & Acoustic / Physical Context:',
  '### 2. Wave Dynamics & Mathematical Derivation:',
  '### 3. Step-by-Step Option & Misconception Analysis:'
];

const CATCH_ALL_PATTERNS = [
  /none of the above/i,
  /none of above/i,
  /all of the above/i,
  /all of above/i,
  /all the above/i,
  /none of these/i,
  /all of these/i,
  /option\s+[1-4]/i
];

const TEACHER_NOTE_PATTERNS = [
  /wrong\s*:/i,
  /right\s*:/i
];

enhancedQuestions.forEach((q, idx) => {
  const qNum = idx + 1;
  const qCode = q.questionCode || `Q#${qNum}`;

  // Tier 2: 3-Part Structure Validation
  const sol = q.solution || '';
  for (const header of REQUIRED_HEADERS) {
    if (!sol.includes(header)) {
      errors.push(`Tier 2 Error [${qCode}]: Missing required header: "${header}"`);
    }
  }

  // Tier 3: Quality Checks (Catch-alls, Leaked Notes, Placeholder Options)
  const opts = q.options || [];
  if (opts.length !== 4) {
    errors.push(`Tier 3 Error [${qCode}]: Expected exactly 4 options, found ${opts.length}`);
  }

  opts.forEach((opt, oi) => {
    const optStr = String(opt);
    for (const pat of CATCH_ALL_PATTERNS) {
      if (pat.test(optStr)) {
        errors.push(`Tier 3 Error [${qCode}]: Option ${String.fromCharCode(65 + oi)} contains forbidden catch-all/placeholder: "${optStr}"`);
      }
    }
    for (const pat of TEACHER_NOTE_PATTERNS) {
      if (pat.test(optStr)) {
        errors.push(`Tier 3 Error [${qCode}]: Option ${String.fromCharCode(65 + oi)} contains leaked teacher note: "${optStr}"`);
      }
    }
  });

  // KaTeX balance validation
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

  // Tier 4: Answer Alignment Validation
  const ans = q.correctAnswer;
  if (!['A', 'B', 'C', 'D'].includes(ans)) {
    errors.push(`Tier 4 Error [${qCode}]: Invalid correctAnswer "${ans}"`);
  }

  // Check Step 3 contains correct answer marker
  const step3Index = sol.indexOf('### 3. Step-by-Step Option & Misconception Analysis:');
  if (step3Index !== -1) {
    const step3Text = sol.substring(step3Index);
    const correctLetterRegex = new RegExp(`\\*\\*${ans}\\s*\\(Correct`, 'i');
    const correctLetterRegexAlt = new RegExp(`\\b${ans}\\s*\\(Correct`, 'i');
    if (!correctLetterRegex.test(step3Text) && !correctLetterRegexAlt.test(step3Text)) {
      errors.push(`Tier 4 Error [${qCode}]: Step 3 does not explicitly mark answer "${ans}" as (Correct)`);
    }
  }

  // Tier 5: Question Text & Code Integrity
  if (!q.text || q.text.trim().length < 10) {
    errors.push(`Tier 5 Error [${qCode}]: Question text too short or empty`);
  }
  if (!q.topicCode || !q.topicCode.startsWith('MH-9-SCIT-12')) {
    errors.push(`Tier 5 Error [${qCode}]: Invalid or mismatched topicCode: "${q.topicCode}"`);
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
  console.log('\n>>> ALL 114 QUESTIONS PASSED THE 5-TIER QUALITY GATE LINTER WITH 100% GOLD COMPLIANCE! <<<');
  fs.writeFileSync('backups/staging/mh9_scit_12_enhanced.json', JSON.stringify(enhancedQuestions, null, 2), 'utf8');
  console.log('Saved certified questions to backups/staging/mh9_scit_12_enhanced.json');
}
