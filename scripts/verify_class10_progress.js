const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

const subjId = process.argv[2] || 'cbse_10_math';

async function verify() {
  console.log(`=== SYLLABUS AUDIT FOR ${subjId} ===`);
  const sDoc = await adminDb.collection('syllabus').doc(subjId).get();
  if (!sDoc.exists) {
    console.error(`Syllabus ${subjId} not found`);
    process.exit(1);
  }
  const sData = sDoc.data();
  const chs = sData.chapters || [];
  
  let totalSubs = 0;
  let totalQs = 0;
  let totalTarget = 0;
  let totalDeficit = 0;
  
  for (let c = 0; c < chs.length; c++) {
    const ch = chs[c];
    const chNum = ch.chapterNumber || ch.number || (c + 1);
    const chName = ch.chapterName || ch.name || `Chapter ${chNum}`;
    let chSubs = 0;
    let chQs = 0;
    let chDeficit = 0;

    for (const top of (ch.topics || [])) {
      if (top.subtopics && top.subtopics.length > 0) {
        for (const sub of top.subtopics) {
          chSubs++;
          const tc = sub.topicCode || sub.code;
          const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
          const count = qSnap.size;
          chQs += count;
          if (count < 80) chDeficit += (80 - count);
        }
      } else {
        chSubs++;
        const tc = top.topicCode || top.code;
        const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
        const count = qSnap.size;
        chQs += count;
        if (count < 80) chDeficit += (80 - count);
      }
    }

    const chTarget = chSubs * 80;
    totalSubs += chSubs;
    totalQs += chQs;
    totalTarget += chTarget;
    totalDeficit += chDeficit;

    const status = chDeficit === 0 ? '✅ 100% (0 deficit)' : (chQs > 0 ? `🟡 ${((chQs/chTarget)*100).toFixed(1)}% (${chDeficit} deficit)` : `🔴 0% (${chDeficit} deficit)`);
    console.log(`Ch ${String(chNum).padStart(2)}: ${chName.padEnd(45)} -> ${String(chQs).padStart(4)} Qs / ${String(chTarget).padStart(4)} target [${status}]`);
  }

  console.log('--------------------------------------------------------------------------------');
  console.log(`TOTAL: ${totalQs} / ${totalTarget} Qs across ${totalSubs} leaf subtopics [Deficit: ${totalDeficit}]`);
  process.exit(0);
}

verify();
