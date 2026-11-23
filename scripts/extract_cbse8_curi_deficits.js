// scripts/extract_cbse8_curi_deficits.js
const fs = require('fs');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function extractDeficits() {
  console.log('--- EXTRACTING CBSE-8-CURI DEFICIT MANIFEST ---');
  const sylSnap = await adminDb.collection('syllabus').doc('cbse_8_curi').get();
  if (!sylSnap.exists) {
    console.error('Syllabus cbse_8_curi not found!');
    process.exit(1);
  }
  const sylData = sylSnap.data();
  console.log('Subject:', sylData.subjectName, '| Chapters:', sylData.chapters.length);

  const manifest = [];
  let totalLeafs = 0;
  let totalCurrent = 0;
  let totalNeeded = 0;

  for (let cIdx = 0; cIdx < sylData.chapters.length; cIdx++) {
    const ch = sylData.chapters[cIdx];
    const chNum = ch.chapterNumber;
    const chName = ch.chapterName;
    const chItem = {
      chapterIndex: cIdx,
      chapterNumber: chNum,
      chapterName: chName,
      leafCount: 0,
      currentTotal: 0,
      neededTotal: 0,
      leafs: []
    };

    for (const top of (ch.topics || [])) {
      if (top.subtopics && top.subtopics.length > 0) {
        for (const sub of top.subtopics) {
          const tc = sub.topicCode;
          const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
          const curr = qSnap.size;
          const target = 80;
          const needed = Math.max(0, target - curr);

          chItem.leafs.push({
            topicCode: tc,
            name: sub.subtopicName || sub.name || tc,
            number: sub.subtopicNumber || sub.number || '',
            parentTopic: top.topicName || '',
            current: curr,
            needed: needed
          });

          chItem.currentTotal += curr;
          chItem.neededTotal += needed;
          totalCurrent += curr;
          totalNeeded += needed;
          totalLeafs++;
        }
      } else {
        const tc = top.topicCode;
        const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
        const curr = qSnap.size;
        const target = 80;
        const needed = Math.max(0, target - curr);

        chItem.leafs.push({
          topicCode: tc,
          name: top.topicName || tc,
          number: top.topicNumber || '',
          parentTopic: chName,
          current: curr,
          needed: needed
        });

        chItem.currentTotal += curr;
        chItem.neededTotal += needed;
        totalCurrent += curr;
        totalNeeded += needed;
        totalLeafs++;
      }
    }

    chItem.leafCount = chItem.leafs.length;
    manifest.push(chItem);
    console.log(`Ch ${chNum} (${chName}): ${chItem.leafCount} leafs, current: ${chItem.currentTotal}, needed: ${chItem.neededTotal}`);
  }

  console.log('==============================================');
  console.log(`TOTAL LEAFS: ${totalLeafs} | CURRENT: ${totalCurrent} | TARGET: ${totalLeafs * 80} | NEEDED: ${totalNeeded}`);
  console.log('==============================================');

  fs.writeFileSync('scripts/cbse8_curi_deficit_manifest.json', JSON.stringify(manifest, null, 2));
  console.log('Saved manifest to scripts/cbse8_curi_deficit_manifest.json');
  process.exit(0);
}

extractDeficits().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
