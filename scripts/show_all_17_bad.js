const fs = require('fs');
const d = JSON.parse(fs.readFileSync('ch5_classification.json', 'utf8'));
d.badQuestions.forEach((b, i) => {
  console.log(`[${i+1}] ID: ${b.id} | Code: ${b.code} | Topic: ${b.topic}`);
  console.log(`Question: ${b.text}`);
  console.log(`Forbidden Term: ${b.forbiddenTerm}`);
  console.log(`Options:`, b.options);
  console.log(`Answer: ${b.correctAnswer}`);
  console.log('-'.repeat(60));
});
