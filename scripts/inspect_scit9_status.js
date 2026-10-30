const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const adminDb = admin.firestore();

async function check() {
  const qs = await adminDb.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-')
    .where('topicCode', '<=', 'MH-9-SCIT-\uf8ff')
    .get();

  const chMap = {};
  qs.forEach(doc => {
    const d = doc.data();
    const ch = d.chapterNumber || (d.topicCode ? d.topicCode.split('-')[3] : 'unknown');
    if (!chMap[ch]) chMap[ch] = { total: 0, exam: 0, practice: 0, mock: 0, unassigned: 0, used: 0 };
    chMap[ch].total++;
    if (d.vault === 'exam') chMap[ch].exam++;
    else if (d.vault === 'practice') chMap[ch].practice++;
    else if (d.vault === 'mock') chMap[ch].mock++;
    else chMap[ch].unassigned++;
    if (d.usageStatus === 'used' || d.used) chMap[ch].used++;
  });

  console.log('MH-9-SCIT Chapters breakdown:');
  Object.keys(chMap).sort((a,b)=>Number(a)-Number(b)).forEach(k => {
    const item = chMap[k];
    console.log(`Ch ${k}: total=${item.total}, exam=${item.exam}, practice=${item.practice}, mock=${item.mock}, unassigned=${item.unassigned}, used=${item.used}`);
  });
}

check().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
