const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

const chNum = process.argv[2] || '5';

async function check() {
  const prefix = `MH-9-SCIT-${chNum}-`;
  const snap = await db.collection('questions')
    .where('topicCode', '>=', prefix)
    .where('topicCode', '<=', prefix + '\uf8ff')
    .get();

  const topicMap = {};
  let badChapterCount = 0;
  const expectedChapterNum = parseInt(chNum);

  snap.forEach(d => {
    const data = d.data();
    const t = data.topicCode || 'unknown';
    if (!topicMap[t]) topicMap[t] = { total: 0, exam: 0, practice: 0, mock: 0, other: 0 };
    topicMap[t].total++;
    const v = data.vault;
    if (v === 'exam') topicMap[t].exam++;
    else if (v === 'practice') topicMap[t].practice++;
    else if (v === 'mock') topicMap[t].mock++;
    else topicMap[t].other++;

    if (data.chapterNumber !== expectedChapterNum) {
      badChapterCount++;
    }
  });

  console.log(`\n=== Verification for Chapter ${chNum} (Total questions: ${snap.size}) ===`);
  const topics = Object.keys(topicMap).sort();
  for (const t of topics) {
    const s = topicMap[t];
    console.log(`${t}: Total ${s.total} => Exam: ${s.exam}, Practice: ${s.practice}, Mock: ${s.mock}, Other: ${s.other}`);
  }
  console.log(`Questions with wrong chapterNumber: ${badChapterCount}`);
}

check().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
