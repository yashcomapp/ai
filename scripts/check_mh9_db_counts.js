const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function checkAllCounts() {
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  console.log(`Total questions for MH-9-SCIT: ${snap.size}`);

  const chapterMap = {};
  snap.docs.forEach(d => {
    const data = d.data();
    const ch = data.chapterNumber || (data.topicCode ? data.topicCode.split('-')[3] : 'unknown');
    const topic = data.topicCode || 'unknown';
    const vault = data.vault || (data.examCategory === 'foundation' ? 'mock' : 'unassigned');
    const isUsed = (data.usageCount > 0 || (data.usedInExams && data.usedInExams.length > 0) || (data.usedInPractices && data.usedInPractices.length > 0));

    if (!chapterMap[ch]) chapterMap[ch] = { total: 0, used: 0, topics: {} };
    chapterMap[ch].total++;
    if (isUsed) chapterMap[ch].used++;

    if (!chapterMap[ch].topics[topic]) chapterMap[ch].topics[topic] = { total: 0, exam: 0, practice: 0, mock: 0, unassigned: 0, used: 0 };
    chapterMap[ch].topics[topic].total++;
    if (isUsed) chapterMap[ch].topics[topic].used++;
    chapterMap[ch].topics[topic][vault] = (chapterMap[ch].topics[topic][vault] || 0) + 1;
  });

  const sortedCh = Object.keys(chapterMap).sort((a,b) => parseInt(a) - parseInt(b));
  sortedCh.forEach(ch => {
    const cData = chapterMap[ch];
    console.log(`\n--- Chapter ${ch}: Total ${cData.total} (Used: ${cData.used}) ---`);
    Object.keys(cData.topics).sort().forEach(t => {
      const top = cData.topics[t];
      console.log(`   ${t}: Total ${top.total} (Exam: ${top.exam}, Practice: ${top.practice}, Mock: ${top.mock}, Unassigned: ${top.unassigned}, Used: ${top.used})`);
    });
  });
}

checkAllCounts().catch(console.error);
