const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function prune() {
  const prefix = 'MH-10-MTH1-';
  const snap = await db.collection('questions')
    .where('topicCode', '>=', prefix)
    .where('topicCode', '<=', prefix + '\uf8ff')
    .get();

  console.log(`Found ${snap.size} total questions with prefix ${prefix}`);
  const toDelete = [];
  snap.forEach(d => {
    const data = d.data();
    const parts = (data.topicCode || '').split('-');
    const tCode = parts[parts.length - 1]; // e.g. "1.1" or "1.1.1"
    if (tCode.split('.').length > 2) {
      if ((data.usageCount || 0) === 0 && !data.used && data.usageStatus !== 'used') {
        toDelete.push(d.ref);
      }
    }
  });

  console.log(`Found ${toDelete.length} legacy subtopic questions to prune.`);
  for (let i = 0; i < toDelete.length; i += 400) {
    const batch = db.batch();
    toDelete.slice(i, i + 400).forEach(ref => batch.delete(ref));
    await batch.commit();
    console.log(`Deleted ${toDelete.slice(i, i + 400).length} questions.`);
  }
}

prune().then(() => {
  console.log('Legacy pruning complete.');
  process.exit(0);
}).catch(err => {
  console.error(err);
  process.exit(1);
});
