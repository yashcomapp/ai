const fs = require('fs');
const d = JSON.parse(fs.readFileSync('all_boilerplate_questions.json', 'utf8'));
const scit9 = d.questions.filter(q => q.topicCode.startsWith('MH-9-SCIT'));
console.log('MH-9-SCIT boilerplate count:', scit9.length);
scit9.slice(0, 3).forEach(q => {
  console.log('='.repeat(60));
  console.log(`[${q.questionCode}] (${q.topicCode}): ${q.text}`);
  console.log('Full Explanation:');
  console.log(q.fullExplanation || q.fullSolution);
});
