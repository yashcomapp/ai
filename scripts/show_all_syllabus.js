const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function showAllSyllabus() {
  const docSnap = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = docSnap.data();
  console.log('Class:', d.class, 'Subject:', d.subject, 'Chapters:', d.chapters.length);
  d.chapters.forEach(c => {
    console.log(`\nChapter ${c.chapterNumber}: ${c.chapterName}`);
    (c.topics || []).forEach(t => {
      console.log(`   ${t.topicCode || t.code} : ${t.topicName || t.name}`);
    });
  });
}
showAllSyllabus().catch(console.error);
