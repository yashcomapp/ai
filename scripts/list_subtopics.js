const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const doc = await adminDb.collection('syllabus').doc('mh_9_mth2').get();
  const d = doc.data();
  d.chapters.forEach(ch => {
    console.log(`=== Chapter ${ch.number}: ${ch.name} ===`);
    ch.topics.forEach(t => {
      console.log(`  Topic: ${t.name}`);
      (t.subtopics || []).forEach(st => {
        console.log(`    ${st.topicCode}: ${st.name}`);
      });
    });
  });
  process.exit(0);
}
main();
