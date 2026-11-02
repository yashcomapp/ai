const fs = require('fs');
const list = JSON.parse(fs.readFileSync('scripts/scit9_out_of_syllabus_remedy_list.json', 'utf8'));
const ch9 = list.filter(q => q.chapter === 9);
console.log(`Chapter 9 questions to replace: ${ch9.length}`);
ch9.forEach((q, i) => {
  console.log(`[${i+1}] ${q.id} (${q.type}) [${q.topicCode}]: ${q.text.slice(0, 70)}...`);
});
