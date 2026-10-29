// scripts/extract-ch11-raw.js
// Extracts all Chapter 11 questions from Firestore to backups/staging/mh9_scit_11_raw.json

require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function extract() {
  const db = admin.firestore();
  console.log('Querying Chapter 11 questions from MH-9-SCIT...');

  const snap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'SCIT')
    .where('chapterNumber', '==', '11')
    .get();

  console.log(`Found ${snap.size} documents for Chapter 11.`);

  const list = [];
  snap.forEach(doc => {
    list.push({
      id: doc.id,
      ...doc.data()
    });
  });

  // Sort by topicCode and questionCode
  list.sort((a, b) => (a.questionCode || '').localeCompare(b.questionCode || ''));

  const outDir = path.resolve('backups/staging');
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  const outPath = path.join(outDir, 'mh9_scit_11_raw.json');
  fs.writeFileSync(outPath, JSON.stringify(list, null, 2), 'utf8');
  console.log(`Successfully saved ${list.length} raw questions to ${outPath}`);
  process.exit(0);
}

extract().catch(err => {
  console.error('Extraction failed:', err);
  process.exit(1);
});
