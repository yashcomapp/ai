const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function audit() {
  const db = admin.firestore();
  console.log('Auditing question counts across all chapters and topics of MH-9-SCIT...');

  const qsSnap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'SCIT')
    .select('topicCode', 'chapterNumber')
    .get();

  console.log(`Total MH-9-SCIT questions found in Firestore: ${qsSnap.size}`);

  const countsByTopic = {};
  qsSnap.forEach(doc => {
    const data = doc.data();
    const tc = data.topicCode || 'UNKNOWN';
    countsByTopic[tc] = (countsByTopic[tc] || 0) + 1;
  });

  const sylSnap = await db.collection('syllabus').doc('mh_9_scit').get();
  const sylData = sylSnap.data();

  const deficientTopics = [];
  let totalTopics = 0;

  (sylData.chapters || []).forEach(ch => {
    (ch.topics || []).forEach(t => {
      totalTopics++;
      const tc = t.topicCode || t.code;
      const count = countsByTopic[tc] || 0;
      if (count < 40) {
        deficientTopics.push({
          chapter: ch.number || ch.id,
          chapterName: ch.name || ch.title,
          topicCode: tc,
          topicName: t.name || t.title,
          count: count,
          needed: 40 - count
        });
      }
    });
  });

  console.log(`\nAudit Results:`);
  console.log(`Total Topics checked: ${totalTopics}`);
  console.log(`Deficient Topics (< 40 questions): ${deficientTopics.length}`);

  if (deficientTopics.length > 0) {
    console.log('\nList of Deficient Topics:');
    deficientTopics.forEach(dt => {
      console.log(`  - Ch ${dt.chapter} | ${dt.topicCode}: ${dt.count}/40 Qs (Needs +${dt.needed}) - ${dt.topicName}`);
    });
  } else {
    console.log('\n🎉 ALL topics in MH-9-SCIT have at least 40 questions!');
  }
}

audit().catch(console.error);
