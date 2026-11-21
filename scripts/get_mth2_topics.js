const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const fs = require('fs');

async function run() {
  const snap = await adminDb.collection('syllabusTopicIndex')
    .where('subjectCode', '==', 'MTH2')
    .get();
  console.log('Total found:', snap.size);
  if (snap.size > 0) {
    console.log('Sample doc:', snap.docs[0].data());
  }
  const topics = snap.docs.map(d => ({
    code: d.data().topicCode,
    name: d.data().topicName,
    ch: d.data().chapterNumber,
    class: d.data().class || d.data().classNum
  })).sort((a,b) => a.code.localeCompare(b.code));
  
  fs.writeFileSync('scripts/mth2_all_topics.json', JSON.stringify(topics, null, 2));
  console.log(`Saved ${topics.length} topics to scripts/mth2_all_topics.json`);
}

run().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
