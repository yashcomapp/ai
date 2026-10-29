const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function auditAll() {
  const db = admin.firestore();
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  let total = 0;
  let compactCount = 0;
  let deprecatedCount = 0;
  const chStats = {};

  snap.forEach(d => {
    const data = d.data();
    const ch = String(data.chapterNumber);
    if (!chStats[ch]) chStats[ch] = { total: 0, compact: 0, deprecated: 0 };
    chStats[ch].total++;

    if (data.solution) {
      if (data.solution.includes('**Key Concept:**') && !data.solution.includes('### 1.')) {
        chStats[ch].compact++;
        compactCount++;
      } else if (data.solution.includes('### 1.')) {
        chStats[ch].deprecated++;
        deprecatedCount++;
      }
    }
  });

  console.log('=== FULL AUDIT OF MH-9-SCIT COMPACT FORMAT ===');
  Object.keys(chStats).sort((a,b) => Number(a) - Number(b)).forEach(ch => {
    const s = chStats[ch];
    const status = s.compact === s.total ? 'ALL COMPACT' : (s.compact > 0 ? 'PARTIAL' : 'PENDING');
    console.log('  Chapter ' + ch.padStart(2) + ': ' + String(s.compact).padStart(3) + '/' + String(s.total).padStart(3) + ' Compact (' + s.deprecated + ' Deprecated) [' + status + ']');
  });
  console.log('\nTotal Compact Enhanced Questions: ' + compactCount);
  console.log('Total Deprecated 3-Part Remaining: ' + deprecatedCount);
  process.exit(0);
}

auditAll().catch(err => {
  console.error(err);
  process.exit(1);
});
