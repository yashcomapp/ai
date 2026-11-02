const fs = require('fs');
const report = JSON.parse(fs.readFileSync('scripts/chapter_by_chapter_audit_report.json', 'utf8'));
const sci8 = report.filter(r => r.board === 'MH' && r.class === '8' && r.subject === 'SCI');
const dups = [];
sci8.forEach(r => {
  r.issueDetails.duplicateOptions.forEach(d => dups.push(d));
});
console.log(`Found ${dups.length} questions with duplicate options in MH-8-SCI:`);
dups.forEach(d => console.log(JSON.stringify(d)));
