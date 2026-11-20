const fs = require('fs');
const path = require('path');

const report = JSON.parse(fs.readFileSync(path.join(__dirname, 'practice_deficits_report.json'), 'utf-8'));

const summary = {};

report.forEach(item => {
  const subjKey = `${item.boardCode}-${item.classNum}-${item.subjectCode}`;
  if (!summary[subjKey]) {
    summary[subjKey] = {
      board: item.boardCode,
      class: item.classNum,
      subject: item.subjectCode,
      name: item.subjectName,
      totalSubtopicsWithDeficits: 0,
      partiallyFilledSubtopics: [],
      zeroQuestionSubtopics: []
    };
  }
  summary[subjKey].totalSubtopicsWithDeficits++;
  if (item.totalCount > 0) {
    summary[subjKey].partiallyFilledSubtopics.push(item);
  } else {
    summary[subjKey].zeroQuestionSubtopics.push(item);
  }
});

console.log('=== BREAKDOWN BY SUBJECT ===');
Object.values(summary).forEach(s => {
  console.log(`\n📚 [${s.board} Class ${s.class} ${s.subject}] ${s.name}:`);
  console.log(`   - Partially populated subtopics (<20 practice): ${s.partiallyFilledSubtopics.length}`);
  console.log(`   - Unpopulated subtopics (0 questions): ${s.zeroQuestionSubtopics.length}`);
  
  if (s.partiallyFilledSubtopics.length > 0) {
    const chapters = {};
    s.partiallyFilledSubtopics.forEach(item => {
      chapters[item.chapterNumber] = (chapters[item.chapterNumber] || 0) + 1;
    });
    console.log(`   - Active chapters with partial deficits:`, chapters);
  }
});
