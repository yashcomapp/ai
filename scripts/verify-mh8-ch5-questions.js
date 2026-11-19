// scripts/verify-mh8-ch5-questions.js
const { topic2Questions } = require('./mh8_ch5_topic2.js');
const { topic2Part2Questions } = require('./mh8_ch5_topic2_part2.js');
const { topic3Questions } = require('./mh8_ch5_topic3.js');
const { topic3Part2Questions } = require('./mh8_ch5_topic3_part2.js');
const { topic4Questions } = require('./mh8_ch5_topic4.js');
const { topic4Part2Questions } = require('./mh8_ch5_topic4_part2.js');
const { topic5Questions } = require('./mh8_ch5_topic5.js');
const { topic5Part2Questions } = require('./mh8_ch5_topic5_part2.js');
const { topic6Questions } = require('./mh8_ch5_topic6.js');
const { topic6Part2Questions } = require('./mh8_ch5_topic6_part2.js');

const allQuestions = [
  ...topic2Questions,
  ...topic2Part2Questions,
  ...topic3Questions,
  ...topic3Part2Questions,
  ...topic4Questions,
  ...topic4Part2Questions,
  ...topic5Questions,
  ...topic5Part2Questions,
  ...topic6Questions,
  ...topic6Part2Questions
];

console.log(`=== Total Questions to verify: ${allQuestions.length} ===`);

let errors = [];
const seenCodes = new Set();
const vaultCounts = { exam: 0, practice: 0, foundation: 0 };
const subtopicCounts = {};

allQuestions.forEach((q, idx) => {
  const code = q.questionCode;

  // Check unique code
  if (seenCodes.has(code)) {
    errors.push(`Duplicate questionCode: ${code}`);
  }
  seenCodes.add(code);

  // Vault count
  const v = q.vault;
  if (!['exam', 'practice', 'foundation'].includes(v)) {
    errors.push(`[${code}] Invalid vault: ${v}`);
  } else {
    vaultCounts[v]++;
  }

  // Subtopic count
  subtopicCounts[q.subtopicCode] = (subtopicCounts[q.subtopicCode] || 0) + 1;

  // Tier 2: 3-Part Solution
  const sol = q.solution || '';
  const hasPart1 = sol.includes('### 1. Scientific Principle');
  const hasPart2 = sol.includes('### 2. Physical Context');
  const hasPart3 = sol.includes('### 3. Step-by-Step Option');
  if (!hasPart1 || !hasPart2 || !hasPart3) {
    errors.push(`Tier 2 Error [${code}]: Incomplete 3-part headers (P1:${hasPart1}, P2:${hasPart2}, P3:${hasPart3})`);
  }
  if (sol.length < 250) {
    errors.push(`Tier 2 Error [${code}]: Solution too short (${sol.length} chars)`);
  }

  // Tier 3: Options Integrity
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
  }

  if (q.text.includes('---') || (q.text.includes('___') && !q.text.includes('\\_'))) {
    errors.push(`Tier 3 Error [${code}]: Question text contains fill-in blanks dash/underscores: "${q.text.slice(0, 40)}"`);
  }

  if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) {
    errors.push(`Tier 3 Error [${code}]: Invalid correctAnswer: "${q.correctAnswer}"`);
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
  errors.forEach(e => console.error('  - ' + e));
  process.exit(1);
} else {
  console.log('✅ 5-Tier Quality Gate Passed 100%! Zero errors detected.');
  console.log('Vault Counts:', vaultCounts);
  console.log('Subtopic Counts:', subtopicCounts);
}
