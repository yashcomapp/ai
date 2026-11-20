const fs = require('fs');
const path = require('path');

const report = JSON.parse(fs.readFileSync(path.join(__dirname, 'practice_deficits_report.json'), 'utf-8'));

const bySubject = {};
report.forEach(item => {
  const key = `${item.boardCode} Class ${item.classNum} - ${item.subjectName} (${item.subjectCode})`;
  if (!bySubject[key]) {
    bySubject[key] = {
      totalDeficits: 0,
      hasSomeQuestions: 0,
      zeroQuestions: 0,
      itemsWithSomeQuestions: []
    };
  }
  bySubject[key].totalDeficits++;
  if (item.totalCount > 0) {
    bySubject[key].hasSomeQuestions++;
    bySubject[key].itemsWithSomeQuestions.push(item);
  } else {
    bySubject[key].zeroQuestions++;
  }
});

console.log('=== SUMMARY OF TOPICS/SUBTOPICS WITH < 20 PRACTICE QUESTIONS ===\n');
Object.entries(bySubject).forEach(([subj, data]) => {
  console.log(`📌 ${subj}:`);
  console.log(`   - Total deficits: ${data.totalDeficits}`);
  console.log(`   - Items that ALREADY have questions (partially filled): ${data.hasSomeQuestions}`);
  console.log(`   - Items with 0 questions (unpopulated/future syllabus): ${data.zeroQuestions}`);
  if (data.itemsWithSomeQuestions.length > 0) {
    console.log(`   - Partially filled items:`);
    data.itemsWithSomeQuestions.forEach(it => {
      console.log(`     * [${it.code}] Ch.${it.chapterNumber} ${it.number} "${it.name}": Practice=${it.practiceCount}/20, Total=${it.totalCount}, Deficit=+${it.deficit}`);
    });
  }
  console.log('');
});
