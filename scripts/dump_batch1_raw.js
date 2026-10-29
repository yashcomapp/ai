const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const fs = require('fs');

async function dump() {
  const db = admin.firestore();
  const allQs = [];

  for (const ch of ['1', '2', '3', '11', '12']) {
    console.log(`Dumping Chapter ${ch}...`);
    const snap = await db.collection('questions')
      .where('subjectCode', '==', 'SCIT')
      .where('class', '==', '9')
      .where('chapterNumber', '==', ch)
      .get();
    
    snap.forEach(d => {
      allQs.push({ id: d.id, ...d.data() });
    });
  }

  // Sort by chapterNumber then questionCode
  allQs.sort((a,b) => {
    const cDiff = Number(a.chapterNumber) - Number(b.chapterNumber);
    if (cDiff !== 0) return cDiff;
    return (a.questionCode || '').localeCompare(b.questionCode || '');
  });

  console.log(`Total Batch 1 questions dumped: ${allQs.length}`);
  fs.writeFileSync('backups/staging/batch1_raw_dump.json', JSON.stringify(allQs, null, 2), 'utf8');
  console.log('Saved to backups/staging/batch1_raw_dump.json');
  process.exit(0);
}

dump().catch(err => {
  console.error(err);
  process.exit(1);
});
