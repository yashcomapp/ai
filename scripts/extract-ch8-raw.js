// scripts/extract-ch8-raw.js
// Extracts all Chapter 8 questions from Firestore to backups/staging/mh9_scit_8_raw.json

require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function extract() {
  const db = admin.firestore();
  console.log('Querying Chapter 8 questions from MH-9-SCIT...');

  const snap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'SCIT')
    .where('chapterNumber', '==', '8')
    .get();

  console.log(`Found ${snap.size} documents for Chapter 8.`);

  const list = [];
  snap.forEach(doc => {
    list.push({
      id: doc.id,
      ...doc.data()
    });
  });

  // Sort by questionCode
  list.sort((a, b) => (a.questionCode || a.id).localeCompare(b.questionCode || b.id, undefined, { numeric: true }));

  const outDir = path.resolve('backups/staging');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const outFile = path.join(outDir, 'mh9_scit_8_raw.json');
  fs.writeFileSync(outFile, JSON.stringify(list, null, 2), 'utf8');
  console.log(`Saved ${list.length} raw questions to ${outFile}`);

  // Summary analysis
  let emptySol = 0;
  let catchAlls = 0;
  let leaked = 0;
  list.forEach(q => {
    if (!q.solution || q.solution.trim() === '') emptySol++;
    (q.options || []).forEach(opt => {
      if (/\b(none of the above|none of above|all of the above|all of above)\b/i.test(opt)) catchAlls++;
      if (/\b(wrong\s*:|right\s*:)/i.test(opt)) leaked++;
    });
  });

  console.log('\n--- Chapter 8 Raw Defect Analysis ---');
  console.log(`Total questions: ${list.length}`);
  console.log(`Empty solutions: ${emptySol} (${((emptySol/list.length)*100).toFixed(1)}%)`);
  console.log(`Catch-all options ("None of...", "All of..."): ${catchAlls}`);
  console.log(`Leaked teacher notes ("Wrong:", "Right:"): ${leaked}`);

  console.log('\nSample question codes:');
  list.slice(0, 5).forEach((q, i) => console.log(`  ${i+1}. ${q.questionCode || q.id} - ${q.text.slice(0, 60)}...`));
  console.log(`  ...`);
  list.slice(-5).forEach((q, i) => console.log(`  ${list.length - 4 + i}. ${q.questionCode || q.id} - ${q.text.slice(0, 60)}...`));

  process.exit(0);
}

extract().catch(err => {
  console.error(err);
  process.exit(1);
});
