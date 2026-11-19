const fs = require('fs');
const data = JSON.parse(fs.readFileSync('audit_results.json', 'utf-8'));

console.log('=== 78 PLACEHOLDER OPTIONS SAMPLES (first 10) ===');
data.issues.placeholderOptions.slice(0, 10).forEach(p => {
  console.log(`[${p.id}] (${p.topicCode}): options =`, p.optTexts);
});

console.log('\n=== 2 DUPLICATE OPTIONS ===');
data.issues.duplicateOptions.forEach(p => {
  console.log(`[${p.id}] (${p.topicCode}): options =`, p.optTexts);
});

console.log('\n=== 12 TRIVIAL EXPLANATIONS ===');
data.issues.trivialExplanation.forEach(p => {
  console.log(`[${p.id}] (${p.topicCode}): explanation =`, p.explanation);
});

console.log('\n=== SAMPLES OF TOPICS WITH >40% OPTION A (first 15) ===');
data.issues.dominantOptionATopics.slice(0, 15).forEach(t => {
  console.log(`Topic: ${t.topicCode.padEnd(25)} | Subject: ${t.subject.padEnd(15)} | Total Obj: ${t.total} | A Count: ${t.aCount} (${t.aPct}%)`);
});
