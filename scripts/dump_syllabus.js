
const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function showAll() {
  const doc = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = doc.data();
  const res = d.chapters.map(c => ({
    num: c.number,
    name: c.name,
    topics: c.topics.map(t => ({ num: t.number, code: t.topicCode, name: t.name }))
  }));
  console.log(JSON.stringify(res, null, 2));
}
showAll().catch(console.error);
