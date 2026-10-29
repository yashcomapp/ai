const fs = require('fs');
const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function extractCh20() {
  const db = admin.firestore();
  console.log('Extracting Chapter 20 questions from Firestore...');
  
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', 'in', ['20', 20])
    .get();

  const qs = [];
  snap.forEach(d => {
    qs.push({ id: d.id, ...d.data() });
  });

  // Sort by questionCode
  qs.sort((a, b) => (a.questionCode || '').localeCompare(b.questionCode || ''));

  fs.writeFileSync('backups/staging/mh9_scit_20_raw.json', JSON.stringify(qs, null, 2), 'utf8');
  console.log(`Extracted ${qs.length} questions to backups/staging/mh9_scit_20_raw.json`);
}

extractCh20().catch(err => {
  console.error(err);
  process.exit(1);
});
