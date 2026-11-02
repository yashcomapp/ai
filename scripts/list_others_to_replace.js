const fs = require('fs');
const list = JSON.parse(fs.readFileSync('scripts/master_out_of_syllabus_list.json', 'utf8'));
const others = list.filter(q => q.chapter !== 9);
console.log(`Remaining questions to replace: ${others.length}`);
const byCh = {};
others.forEach(q => {
  byCh[q.chapter] = byCh[q.chapter] || [];
  byCh[q.chapter].push(q);
});
Object.keys(byCh).forEach(ch => {
  console.log(`\n--- Chapter ${ch} (${byCh[ch].length} questions) ---`);
  byCh[ch].forEach((q, i) => console.log(`  [${i+1}] ${q.id} (${q.type}): ${q.text.slice(0, 60)}...`));
});
