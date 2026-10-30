const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function prune() {
  const chNum = process.argv[2] || '11';
  const prefix = `MH-9-SCIT-${chNum}-`;
  
  // Find all questions in this chapter
  const snap = await db.collection('questions')
    .where('topicCode', '>=', prefix)
    .where('topicCode', '<=', prefix + '\uf8ff')
    .get();

  console.log(`Found ${snap.size} total questions in Chapter ${chNum}`);

  const toDelete = [];
  snap.forEach(d => {
    const data = d.data();
    const parts = (data.topicCode || '').split('-');
    const tCode = parts[parts.length - 1]; // e.g. "11.1" or "11.1.1"
    
    // Subtopics have 3 numbers, e.g. "11.1.1", "11.1.2"
    if (tCode.split('.').length > 2) {
      if ((data.usageCount || 0) === 0 && !data.used && data.usageStatus !== 'used') {
        toDelete.push(d.ref);
      } else {
        console.warn(`WARNING: Question ${d.id} is USED! Skipping delete.`);
      }
    }
  });

  console.log(`Found ${toDelete.length} legacy subtopic questions to prune.`);
  for (let i = 0; i < toDelete.length; i += 400) {
    const batch = db.batch();
    toDelete.slice(i, i + 400).forEach(ref => batch.delete(ref));
    await batch.commit();
    console.log(`Deleted batch ${Math.floor(i / 400) + 1} (${toDelete.slice(i, i + 400).length} questions).`);
  }
}

prune().then(() => {
  console.log('Prune complete.');
  process.exit(0);
}).catch(err => {
  console.error(err);
  process.exit(1);
});
