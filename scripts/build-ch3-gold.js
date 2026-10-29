// scripts/build-ch3-gold.js - Assembles Chapter 3 enhancements and runs 5-Tier Quality Gate Linter
const fs = require('fs');
const path = require('path');

const p1Raw = require('./ch3_part1');
const ch3_part1 = Array.isArray(p1Raw) ? p1Raw : (p1Raw.ch3_part1 || Object.values(p1Raw));
const { ch3_part2 } = require('./ch3_part2');
const { ch3_part3 } = require('./ch3_part3');
const { ch3_part4 } = require('./ch3_part4');

console.log('--- Step 1: Merging Parts ---');
console.log(`Part 1: ${ch3_part1.length} questions`);
console.log(`Part 2: ${ch3_part2.length} questions`);
console.log(`Part 3: ${ch3_part3.length} questions`);
console.log(`Part 4: ${ch3_part4.length} questions`);

const allEnhanced = [...ch3_part1, ...ch3_part2, ...ch3_part3, ...ch3_part4];
console.log(`Total Merged Questions: ${allEnhanced.length}`);

// Load raw questions to preserve metadata (subject, boardCode, chapterNumber, bloomLevel, etc.)
const rawPath = path.resolve('backups/staging/mh9_scit_3_raw.json');
const rawQuestions = JSON.parse(fs.readFileSync(rawPath, 'utf8'));
console.log(`Raw Questions Loaded: ${rawQuestions.length}`);

if (allEnhanced.length !== rawQuestions.length) {
  throw new Error(`Count mismatch! Enhanced: ${allEnhanced.length}, Raw: ${rawQuestions.length}`);
}

const enhancedMap = new Map();
allEnhanced.forEach(q => {
  const code = q.questionCode || q.id;
  enhancedMap.set(code, q);
});

// Clean KaTeX helper
function cleanKaTeX(text) {
  if (!text) return '';
  let cleaned = text;
  // Replace double nested tags
  cleaned = cleaned.replace(/\\\(\\text\{\\\(/g, '\\(');
  cleaned = cleaned.replace(/\\\)\}\\\)/g, '\\)');
  return cleaned;
}

const finalQuestions = rawQuestions.map(raw => {
  const enh = enhancedMap.get(raw.questionCode);
  if (!enh) {
    throw new Error(`Missing enhancement for ${raw.questionCode}`);
  }

  return {
    ...raw,
    text: cleanKaTeX(enh.text),
    options: enh.options.map(opt => cleanKaTeX(opt)),
    correctAnswer: enh.correctAnswer,
    solution: cleanKaTeX(enh.solution),
    isEnhanced: true,
    enhancedAt: new Date().toISOString()
  };
});

console.log('\n--- Step 2: Executing 5-Tier Quality Gate Linter ---');
let linterErrors = [];

finalQuestions.forEach((q, idx) => {
  const qNum = idx + 1;
  const qCode = q.questionCode;

  // Tier 1: Question Integrity
  if (!q.text || q.text.trim().length < 10) {
    linterErrors.push(`[Tier 1] Q${qNum} (${qCode}): Question text is too short or missing.`);
  }
  if (!Array.isArray(q.options) || q.options.length !== 4) {
    linterErrors.push(`[Tier 1] Q${qNum} (${qCode}): Must have exactly 4 options. Found: ${q.options ? q.options.length : 0}`);
  }
  if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) {
    linterErrors.push(`[Tier 1] Q${qNum} (${qCode}): Invalid correctAnswer '${q.correctAnswer}'.`);
  }

  // Tier 2: 3-Part Gold Standard Headers
  const hasPart1 = q.solution.includes('### 1. Scientific Principle & Mathematical Derivation:');
  const hasPart2 = q.solution.includes('### 2. Physical Context & Practical Illustration:');
  const hasPart3 = q.solution.includes('### 3. Step-by-Step Option & Misconception Analysis:');

  if (!hasPart1 || !hasPart2 || !hasPart3) {
    linterErrors.push(`[Tier 2] Q${qNum} (${qCode}): Missing mandatory 3-part header(s). P1: ${hasPart1}, P2: ${hasPart2}, P3: ${hasPart3}`);
  }

  // Tier 3: Distractor Hygiene
  const forbiddenPatterns = [
    /none of (the )?above/i,
    /remains undetermined/i,
    /distinct alternative/i,
    /---/,
    /wrong\s*:/i,
    /right\s*:/i
  ];

  q.options.forEach((opt, oIdx) => {
    forbiddenPatterns.forEach(pat => {
      if (pat.test(opt)) {
        linterErrors.push(`[Tier 3] Q${qNum} (${qCode}) Option ${String.fromCharCode(65 + oIdx)} matches forbidden pattern ${pat}: "${opt}"`);
      }
    });
  });

  // Check question text for dashes
  if (/---/.test(q.text)) {
    linterErrors.push(`[Tier 3] Q${qNum} (${qCode}) Question text contains forbidden dash placeholder '---': "${q.text}"`);
  }

  // Tier 4: KaTeX Formatting & Balance
  const checkKaTeXBalance = (str, label) => {
    if (!str) return;
    if (/\\\(\\text\{\\\(/.test(str) || /\\\)\}\\\)/.test(str)) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Nested KaTeX text tag detected in ${label}.`);
    }
    if (/\${2,}/.test(str)) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Multiple raw dollar signs detected in ${label}.`);
    }
    if (/\\\([^\)]*\\\(/.test(str)) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Nested inline KaTeX \\( detected in ${label}.`);
    }
    if (/\\\[[^\]]*\\\[/.test(str)) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Nested display KaTeX \\[ detected in ${label}.`);
    }
    const openParen = (str.match(/\\\(/g) || []).length;
    const closeParen = (str.match(/\\\)/g) || []).length;
    if (openParen !== closeParen) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Mismatched \\( (${openParen}) and \\) (${closeParen}) in ${label}.`);
    }
    const openBracket = (str.match(/\\\[/g) || []).length;
    const closeBracket = (str.match(/\\\]/g) || []).length;
    if (openBracket !== closeBracket) {
      linterErrors.push(`[Tier 4] Q${qNum} (${qCode}): Mismatched \\[ (${openBracket}) and \\] (${closeBracket}) in ${label}.`);
    }
  };

  checkKaTeXBalance(q.text, 'text');
  checkKaTeXBalance(q.solution, 'solution');
  q.options.forEach((opt, oIdx) => checkKaTeXBalance(opt, `Option ${String.fromCharCode(65 + oIdx)}`));

  // Tier 5: Correct Answer Alignment
  const correctOpt = q.options[q.correctAnswer.charCodeAt(0) - 65];
  if (!correctOpt || correctOpt.trim().length === 0) {
    linterErrors.push(`[Tier 5] Q${qNum} (${qCode}): Correct option for answer '${q.correctAnswer}' is empty.`);
  }
});

if (linterErrors.length > 0) {
  console.error(`\n❌ QUALITY GATE FAILED with ${linterErrors.length} errors:`);
  linterErrors.forEach(err => console.error(`  - ${err}`));
  process.exit(1);
} else {
  console.log('✅ ALL 5 TIERS PASSED PERFECTLY!');
  console.log(`- Total Questions: ${finalQuestions.length}`);
  console.log(`- 100% 3-Part Gold Standard Solutions Present`);
  console.log(`- Zero 'None of above' / Zero Placeholders / Zero '---'`);
  console.log(`- Clean KaTeX formatting verified`);
}

// Save enhanced questions
const outPath = path.resolve('backups/staging/mh9_scit_3_enhanced.json');
fs.writeFileSync(outPath, JSON.stringify(finalQuestions, null, 2), 'utf8');
console.log(`\nEnhanced dataset saved successfully to: ${outPath}`);
