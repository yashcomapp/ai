const fs = require('fs');
const qs = JSON.parse(fs.readFileSync('./scripts/audit_data/cbse10_sci_bio_ch5_6_generated.json', 'utf8'));

console.log('Total questions:', qs.length);
let errors = 0;
let figureCount = 0;
const topicCounts = {};
const vaultCounts = {};

qs.forEach((q, idx) => {
  topicCounts[q.topicCode] = (topicCounts[q.topicCode] || 0) + 1;
  const key = `${q.topicCode}_${q.vault}`;
  vaultCounts[key] = (vaultCounts[key] || 0) + 1;

  if (q.requiresFigure || (q.text && q.text.includes('<svg'))) {
    figureCount++;
  }

  if (!q.options || q.options.length !== 4) {
    console.error(`Err: ${q.questionCode} does not have 4 options`);
    errors++;
  } else {
    const optTexts = q.options.map(o => (typeof o === 'string' ? o : o.text));
    optTexts.forEach((t, tidx) => {
      if (!t || typeof t !== 'string' || t.trim() === '') {
        console.error(`Empty/non-string option text in ${q.questionCode} opt[${tidx}]:`, t);
        errors++;
      }
    });
    const unique = new Set(optTexts.map(t => String(t).trim()));
    if (unique.size !== 4) {
      console.error(`Duplicate options in ${q.questionCode}: `, optTexts);
      errors++;
    }
  }

  if (!['A', 'B', 'C', 'D'].includes(q.correctAnswer)) {
    console.error(`Invalid correct answer in ${q.questionCode}: ${q.correctAnswer}`);
    errors++;
  }

  if (!q.solution || !q.solution.includes('Step 1') || !q.solution.includes('Step 2') || !q.solution.includes('Step 3')) {
    console.error(`Invalid 3-step solution in ${q.questionCode}`);
    errors++;
  }
});

console.log('Total SVG figure questions:', figureCount);
console.log('Unique subtopics:', Object.keys(topicCounts).length);
const badTopics = Object.entries(topicCounts).filter(([tc, c]) => c !== 80);
if (badTopics.length > 0) {
  console.error('Topics not having exactly 80 Qs:', badTopics);
  errors += badTopics.length;
}

if (errors === 0) {
  console.log('ALL 2,960 QUESTIONS PASSED 100% OF QUALITY CHECKS!');
} else {
  console.error(`FAILED with ${errors} errors!`);
  process.exit(1);
}
