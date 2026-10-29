const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function auditChapters() {
  const db = admin.firestore();
  const qsSnap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'SCIT')
    .select('chapterNumber', 'topicCode')
    .get();

  console.log(`Total MH-9-SCIT questions: ${qsSnap.size}`);

  const chCounts = {};
  qsSnap.forEach(d => {
    const ch = d.data().chapterNumber;
    chCounts[ch] = (chCounts[ch] || 0) + 1;
  });

  console.log('Chapter question counts:');
  for (let ch = 1; ch <= 20; ch++) {
    console.log(`Chapter ${ch}: ${chCounts[ch] || 0} Qs`);
  }
}

auditChapters().catch(console.error);
