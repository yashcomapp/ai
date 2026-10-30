const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function prune() {
  const subtopics = ['MH-9-SCIT-8-8.1.2', 'MH-9-SCIT-8-8.1.3'];
  for (const st of subtopics) {
    const snap = await db.collection('questions').where('topicCode', '==', st).get();
    console.log(`Checking ${st}: found ${snap.size} questions`);
    const batch = db.batch();
    let deleted = 0;
    snap.forEach(d => {
      const data = d.data();
      if ((data.usageCount || 0) === 0) {
        batch.delete(d.ref);
        deleted++;
      } else {
        console.warn(`WARNING: Question ${d.id} is USED! Skipping delete.`);
      }
    });
    if (deleted > 0) {
      await batch.commit();
      console.log(`Deleted ${deleted} unused questions from ${st}`);
    }
  }
}

prune().then(() => {
  console.log('Prune complete.');
  process.exit(0);
}).catch(err => {
  console.error(err);
  process.exit(1);
});
