const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function inspect(ch) {
  const snap = await db.collection('syllabusTopicIndex')
    .where('topicCode', '>=', `MH-9-SCIT-${ch}`)
    .where('topicCode', '<=', `MH-9-SCIT-${ch}\uf8ff`)
    .get();
  console.log(`=== Topics for Chapter ${ch} ===`);
  snap.docs.forEach(d => {
    const data = d.data();
    console.log(`${d.id} => code: ${data.topicCode}, name: ${data.topicName}`);
  });
  if (snap.empty) {
    console.log('No topics in syllabusTopicIndex with prefix MH-9-SCIT-' + ch);
  }
}

const chArg = parseInt(process.argv[2] || '8', 10);
inspect(chArg).then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
