const fs = require('fs');
const data = JSON.parse(fs.readFileSync('audit_results.json', 'utf-8'));

console.log('Total placeholder questions:', data.issues.placeholderOptions.length);
const topics = {};
data.issues.placeholderOptions.forEach(p => {
  topics[p.topicCode] = (topics[p.topicCode] || 0) + 1;
});
console.log('Distribution by topic:', topics);

// Print all 78 IDs
console.log('All 78 IDs:', data.issues.placeholderOptions.map(p => p.id));
