const fs = require('fs');
const d = JSON.parse(fs.readFileSync('all_boilerplate_questions.json', 'utf8'));
const nonCh5 = d.questions.filter(q => !q.topicCode.startsWith('MH-8-SCI-5'));
console.log('Non-Ch5 count:', nonCh5.length);
nonCh5.slice(0, 10).forEach(q => {
  console.log(`[${q.questionCode}] (${q.topicCode}) pattern: ${q.matchedPattern}`);
  console.log(`Snippet: ${q.explanationSnippet.replace(/\n/g, ' ')}\n`);
});
