const fs = require('fs');
const d = JSON.parse(fs.readFileSync('ch5_all_questions.json', 'utf8'));

console.log('Total questions in Ch 5:', d.total);
console.log('Flagged OOS in Ch 5:', d.flaggedOOS.length);

// Print details of flagged questions
d.flaggedOOS.forEach((q, idx) => {
  const fullQ = d.questions.find(x => x.id === q.id);
  console.log(`\n[${idx + 1}] ID: ${q.id} | Code: ${q.code} | Topic: ${q.topic}`);
  console.log(`Text: ${q.text}`);
  console.log(`Answer: ${fullQ.correctAnswer}`);
  console.log(`Options:`, fullQ.options);
  console.log(`Explanation snippet: ${(fullQ.explanation || '').slice(0, 150)}...`);
});
