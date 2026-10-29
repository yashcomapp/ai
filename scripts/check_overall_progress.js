require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');

async function check() {
  const db = admin.firestore();
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  const chapters = {};
  snap.forEach(doc => {
    const d = doc.data();
    const ch = String(d.chapterNumber || 'Unknown');
    if (!chapters[ch]) chapters[ch] = { total: 0, enhanced: 0 };
    chapters[ch].total++;
    if (d.isEnhanced) chapters[ch].enhanced++;
  });

  console.log('MH-9-SCIT Chapter Status:');
  const sortedKeys = Object.keys(chapters).sort((a,b) => Number(a) - Number(b));
  let totalAll = 0;
  let enhancedAll = 0;
  for (const ch of sortedKeys) {
    const c = chapters[ch];
    totalAll += c.total;
    enhancedAll += c.enhanced;
    const pct = ((c.enhanced / c.total) * 100).toFixed(1);
    const status = c.enhanced === c.total ? 'COMPLETE' : 'PENDING';
    console.log(`  Chapter ${ch.padStart(2)}: ${String(c.enhanced).padStart(3)}/${String(c.total).padStart(3)} enhanced (${pct.padStart(5)}%) [${status}]`);
  }
  const overallPct = ((enhancedAll / totalAll) * 100).toFixed(1);
  console.log(`\nOverall MH-9-SCIT: ${enhancedAll}/${totalAll} enhanced (${overallPct}%)`);
  process.exit(0);
}

check().catch(err => {
  console.error(err);
  process.exit(1);
});
