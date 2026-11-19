const fs = require('fs');
const data = JSON.parse(fs.readFileSync('boilerplate_questions.json', 'utf-8'));
console.log('Total:', data.count);
data.questions.slice(0, 5).forEach(q => {
  console.log(`[${q.id}] (${q.topicCode}): ${q.text}`);
});
