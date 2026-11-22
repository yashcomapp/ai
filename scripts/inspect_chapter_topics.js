// scripts/inspect_chapter_topics.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const subjectCode = process.argv[2] || 'MGM';
  const chapterNumber = parseInt(process.argv[3] || '4', 10);

  console.log(`Querying syllabusTopicIndex for Subject: ${subjectCode}, Chapter: ${chapterNumber}...`);

  const snap = await adminDb.collection('syllabusTopicIndex')
    .where('subjectCode', '==', subjectCode)
    .get();

  console.log(`Found ${snap.size} total topics for Subject ${subjectCode}:\n`);
  const docs = snap.docs.map(d => d.data());
  docs.sort((a, b) => a.topicCode.localeCompare(b.topicCode, undefined, { numeric: true }));

  const byChapter = {};
  docs.forEach(d => {
    const ch = d.chapterNumber !== undefined ? d.chapterNumber : 'unknown';
    if (!byChapter[ch]) byChapter[ch] = [];
    byChapter[ch].push(d);
  });

  Object.keys(byChapter).sort((a, b) => Number(a) - Number(b)).forEach(ch => {
    console.log(`\n--- CHAPTER ${ch} (${byChapter[ch].length} subtopics) ---`);
    byChapter[ch].forEach(d => {
      console.log(`  ${d.topicCode} | ${d.topicName} | chField: ${typeof d.chapterNumber} ${d.chapterNumber} | count: ${d.questionCount || 0}`);
    });
  });
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
