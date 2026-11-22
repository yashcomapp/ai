const fs = require('fs');

const chFiles = [
  'scripts/mh9_mth1_ch1_perfect.json',
  'scripts/mh9_mth1_ch2_perfect.json',
  'scripts/mh9_mth1_ch3_perfect.json',
  'scripts/mh9_mth1_ch4_perfect.json',
  'scripts/mh9_mth1_ch5_perfect.json',
  'scripts/mh9_mth1_ch6_perfect.json',
  'scripts/mh9_mth1_ch7_perfect.json'
];

let allQs = [];
chFiles.forEach((file, idx) => {
  const qs = JSON.parse(fs.readFileSync(file, 'utf8'));
  console.log(`Chapter ${idx + 1} (${file}): ${qs.length} questions`);
  allQs = allQs.concat(qs);
});

console.log(`\nTotal questions merged: ${allQs.length}`);

// Count unique leaf subtopics
const subtopics = new Set(allQs.map(q => q.topicCode));
console.log(`Total unique leaf subtopics: ${subtopics.size}`);

// Verify that every subtopic has strictly 80 questions
const counts = {};
allQs.forEach(q => {
  counts[q.topicCode] = (counts[q.topicCode] || 0) + 1;
});

let symmetric = true;
for (const tc of subtopics) {
  if (counts[tc] !== 80) {
    console.error(`Subtopic ${tc} has ${counts[tc]} questions instead of 80!`);
    symmetric = false;
  }
}

if (symmetric) {
  console.log('✅ Symmetrical validation passed: Every single subtopic has strictly 80 questions!');
} else {
  console.error('❌ Symmetrical validation failed!');
  process.exit(1);
}

fs.writeFileSync('scripts/mh9_mth1_all_flawless.json', JSON.stringify(allQs, null, 2), 'utf8');
console.log('Saved to scripts/mh9_mth1_all_flawless.json');
