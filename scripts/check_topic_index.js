const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function check() {
  const db = admin.firestore();
  const topicSnap = await db.collection('syllabusTopicIndex')
    .where('boardCode', '==', 'MH')
    .where('subjectCode', '==', 'SCIT')
    .get();

  console.log(`Found ${topicSnap.size} indexed topics for MH-9-SCIT.`);
  const topicMap = {};
  topicSnap.forEach(d => {
    topicMap[d.id] = d.data().topicName;
  });
  console.log('Sample topics:', Object.entries(topicMap).slice(0, 5));
}

check().catch(console.error);
