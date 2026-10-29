const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function fullAudit() {
  const docSnap = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = docSnap.data();

  // Get all questions
  const qSnap = await db.collection('questions')
    .where('class', 'in', ['9', 9])
    .where('subjectCode', '==', 'SCIT')
    .select('chapterNumber', 'topicCode')
    .get();

  const countByCh = {};
  const countByTopic = {};

  qSnap.forEach(doc => {
    const data = doc.data();
    const ch = parseInt(data.chapterNumber, 10);
    const tc = data.topicCode || 'unknown';
    countByCh[ch] = (countByCh[ch] || 0) + 1;
    countByTopic[tc] = (countByTopic[tc] || 0) + 1;
  });

  console.log('=== MH-9-SCIT CHAPTER-LEVEL SUMMARY ===');
  d.chapters.forEach(c => {
    const chNum = parseInt(c.number, 10);
    const totalQ = countByCh[chNum] || 0;
    const topicCount = (c.topics || []).length;
    console.log(`Chapter ${String(chNum).padStart(2)}: ${(c.name || '').padEnd(40)} | Topics: ${topicCount} | Total Qs: ${totalQ}`);
  });
}

fullAudit().catch(console.error);
