const fs = require('fs');
const report = JSON.parse(fs.readFileSync('scripts/chapter_by_chapter_audit_report.json', 'utf8'));

console.log('--- Inspecting issues in MH_Class9_SCIT ---');
const scit9 = report.filter(r => r.board === 'MH' && r.class === '9' && r.subject === 'SCIT' && r.status !== '🟢 PRISTINE');
scit9.forEach(r => {
  console.log(`\n${r.chapterKey}:`);
  console.log('Issues:', JSON.stringify(r.issueDetails, null, 2));
});

console.log('\n--- Inspecting issues in MH_Class8_SCI ---');
const sci8 = report.filter(r => r.board === 'MH' && r.class === '8' && r.subject === 'SCI');
let totalSci8MissingSols = 0;
let totalSci8Dups = 0;
let totalSci8Used = 0;
sci8.forEach(r => {
  totalSci8MissingSols += r.issueDetails.missingSolution.length;
  totalSci8Dups += r.issueDetails.duplicateOptions.length;
  totalSci8Used += r.usedQuestions;
});
console.log(`MH_Class8_SCI summary:`);
console.log(`  Total Chapters: ${sci8.length}`);
console.log(`  Used Questions: ${totalSci8Used}`);
console.log(`  Missing Solutions: ${totalSci8MissingSols}`);
console.log(`  Duplicate Options: ${totalSci8Dups}`);
