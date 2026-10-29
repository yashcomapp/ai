// scripts/build-ch6-gold.js
// Merges all 6 parts of Chapter 6 (MH-9-SCIT-6-6.1, 211 Questions)
// Runs 5-Tier Quality Gate Linter and saves to backups/staging/mh9_scit_6_enhanced.json

const fs = require('fs');
const path = require('path');

const { ch6_part1 } = require('./ch6_part1.js');
const { ch6_part2 } = require('./ch6_part2.js');
const { ch6_part3 } = require('./ch6_part3.js');
const { ch6_part4 } = require('./ch6_part4.js');
const { ch6_part5 } = require('./ch6_part5.js');
const { ch6_part6 } = require('./ch6_part6.js');

console.log('Loading raw Chapter 6 questions...');
const rawPath = path.join(__dirname, '..', 'backups', 'staging', 'mh9_scit_6_raw.json');
const rawQuestions = JSON.parse(fs.readFileSync(rawPath, 'utf8'));
console.log(`Loaded ${rawQuestions.length} raw questions.`);

const allEnhanced = [
  ...ch6_part1,
  ...ch6_part2,
  ...ch6_part3,
  ...ch6_part4,
  ...ch6_part5,
  ...ch6_part6
];

console.log(`Loaded ${allEnhanced.length} enhanced questions across parts 1 to 6.`);

if (allEnhanced.length !== rawQuestions.length) {
  console.error(`FATAL: Count mismatch! Raw: ${rawQuestions.length}, Enhanced: ${allEnhanced.length}`);
  process.exit(1);
}

// Map enhanced by questionCode
const enhancedMap = new Map();
allEnhanced.forEach(q => {
  if (enhancedMap.has(q.questionCode)) {
    console.error(`FATAL: Duplicate questionCode in parts: ${q.questionCode}`);
    process.exit(1);
  }
  enhancedMap.set(q.questionCode, q);
});

// Run 5-Tier Quality Gate Linter
console.log('\n--- EXECUTING 5-TIER QUALITY GATE LINTER ---');
let linterErrors = 0;

const catchAllRegex = /\b(none of the above|none of above|all of the above|all of above|option\s+[a-d]\b)/i;
const leakedPromptRegex = /\b(wrong\s*:|right\s*:)/i;

const finalQuestions = rawQuestions.map((raw, idx) => {
  const enhanced = enhancedMap.get(raw.questionCode);
  if (!enhanced) {
    console.error(`[Linter Error] Missing enhanced object for ${raw.questionCode}`);
    linterErrors++;
    return raw;
  }

  // Tier 1: Check 3-part headers
  const hasH1 = enhanced.solution.includes('### 1.');
  const hasH2 = enhanced.solution.includes('### 2.');
  const hasH3 = enhanced.solution.includes('### 3.');
  if (!hasH1 || !hasH2 || !hasH3) {
    console.error(`[Tier 1 Error] ${raw.questionCode} missing required 3-part header: h1=${hasH1}, h2=${hasH2}, h3=${hasH3}`);
    linterErrors++;
  }

  // Tier 2: Check forbidden catch-alls, leaked teacher prompts, placeholders, dashes
  enhanced.options.forEach((opt, oIdx) => {
    if (catchAllRegex.test(opt)) {
      console.error(`[Tier 2 Error] ${raw.questionCode} Option ${String.fromCharCode(65 + oIdx)} contains catch-all: "${opt}"`);
      linterErrors++;
    }
    if (leakedPromptRegex.test(opt)) {
      console.error(`[Tier 2 Error] ${raw.questionCode} Option ${String.fromCharCode(65 + oIdx)} contains leaked prompt: "${opt}"`);
      linterErrors++;
    }
  });
  if (enhanced.text.includes('---')) {
    console.error(`[Tier 2 Error] ${raw.questionCode} contains fill-in dashes: "${enhanced.text}"`);
    linterErrors++;
  }

  // Tier 3: Option uniqueness and exactly 4 options
  if (!Array.isArray(enhanced.options) || enhanced.options.length !== 4) {
    console.error(`[Tier 3 Error] ${raw.questionCode} has ${enhanced.options ? enhanced.options.length : 0} options (must be 4).`);
    linterErrors++;
  }
  const uniqueOpts = new Set(enhanced.options.map(o => o.trim().toLowerCase()));
  if (uniqueOpts.size !== enhanced.options.length) {
    console.error(`[Tier 3 Error] ${raw.questionCode} has duplicate options: ${JSON.stringify(enhanced.options)}`);
    linterErrors++;
  }

  // Tier 4: KaTeX balance check
  const mathInlineOpen = (enhanced.solution.match(/\\\(/g) || []).length;
  const mathInlineClose = (enhanced.solution.match(/\\\)/g) || []).length;
  if (mathInlineOpen !== mathInlineClose) {
    console.error(`[Tier 4 Error] ${raw.questionCode} unbalanced inline KaTeX: \\( (${mathInlineOpen}) vs \\) (${mathInlineClose})`);
    linterErrors++;
  }
  const mathDispOpen = (enhanced.solution.match(/\\\[/g) || []).length;
  const mathDispClose = (enhanced.solution.match(/\\\]/g) || []).length;
  if (mathDispOpen !== mathDispClose) {
    console.error(`[Tier 4 Error] ${raw.questionCode} unbalanced display KaTeX: \\[ (${mathDispOpen}) vs \\] (${mathDispClose})`);
    linterErrors++;
  }

  // Tier 5: Step 3 option confirmation
  const targetAns = enhanced.correctAnswer;
  if (!['A', 'B', 'C', 'D'].includes(targetAns)) {
    console.error(`[Tier 5 Error] ${raw.questionCode} invalid correctAnswer: "${targetAns}"`);
    linterErrors++;
  }
  const step3Check = enhanced.solution.includes(`Option ${targetAns}`);
  if (!step3Check) {
    console.error(`[Tier 5 Error] ${raw.questionCode} Step 3 does not reference Option ${targetAns}`);
    linterErrors++;
  }

  return {
    ...raw,
    text: enhanced.text,
    options: enhanced.options,
    correctAnswer: targetAns,
    answer: targetAns,
    solution: enhanced.solution,
    isEnhanced: true,
    enhancedAt: new Date().toISOString(),
    enhancementLevel: "gold_standard_3_part"
  };
});

if (linterErrors > 0) {
  console.error(`\n❌ QUALITY GATE FAILED with ${linterErrors} errors. Aborting build.`);
  process.exit(1);
}

console.log('\n✅ 5-TIER QUALITY GATE PASSED! 0 errors detected across all 211 questions.');

// Save enhanced questions
const outPath = path.join(__dirname, '..', 'backups', 'staging', 'mh9_scit_6_enhanced.json');
fs.writeFileSync(outPath, JSON.stringify(finalQuestions, null, 2), 'utf8');
console.log(`Successfully saved ${finalQuestions.length} enhanced questions to ${outPath}`);
