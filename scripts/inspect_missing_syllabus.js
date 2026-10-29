const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function inspectMissingChapters() {
  const docSnap = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = docSnap.data();

  const missingChs = [7, 10, 14, 16];
  missingChs.forEach(chNum => {
    const ch = d.chapters.find(c => parseInt(c.number, 10) === chNum);
    if (!ch) {
      console.log(`Chapter ${chNum} not found in syllabus!`);
      return;
    }
    console.log(`\n======================================================`);
    console.log(`Chapter ${ch.number}: ${ch.name}`);
    console.log(`======================================================`);
    (ch.topics || []).forEach(t => {
      console.log(`  Topic ${t.topicCode || t.code}: ${t.name || t.topicName}`);
      (t.subtopics || []).forEach(st => {
        console.log(`     - ${st.topicCode || st.code}: ${st.name}`);
      });
    });
  });
}

inspectMissingChapters().catch(console.error);
