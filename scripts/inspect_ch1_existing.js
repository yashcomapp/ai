// scripts/inspect_ch1_existing.js
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function checkCodes() {
  const snap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 1)
    .select('topicCode', 'code', 'vault')
    .get();

  console.log('Ch 1 questions total:', snap.size);
  const maxSeq = {};
  const vaultDistribution = {};

  snap.docs.forEach(d => {
    const q = d.data();
    const code = q.code || d.id;
    const parts = code.split('-');
    const seq = parseInt(parts[parts.length - 1], 10);
    const tc = q.topicCode;
    if (!isNaN(seq)) {
      maxSeq[tc] = Math.max(maxSeq[tc] || 0, seq);
    }
    if (!vaultDistribution[tc]) {
      vaultDistribution[tc] = { exam: 0, practice: 0, foundation: 0, total: 0 };
    }
    vaultDistribution[tc].total++;
    const v = q.vault || 'exam';
    if (vaultDistribution[tc][v] !== undefined) vaultDistribution[tc][v]++;
  });

  console.log('Subtopic status and max sequence:');
  Object.keys(vaultDistribution).sort().forEach(tc => {
    const vd = vaultDistribution[tc];
    console.log(`${tc}: Total ${vd.total} (Exam: ${vd.exam}, Practice: ${vd.practice}, Foundation: ${vd.foundation}) | MaxSeq: ${maxSeq[tc]}`);
  });
}

checkCodes().catch(console.error);
