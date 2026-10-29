// scripts/extract-ch5-raw.js
// Extracts all Chapter 5 questions (MH-9-SCIT-5-5.1) from Firestore to backups/staging/mh9_scit_5_raw.json

require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function extract() {
  const db = admin.firestore();
  console.log('Querying Firestore for MH-9-SCIT Chapter 5 questions...');

  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', '5')
    .get();

  console.log(`Found ${snap.size} questions.`);

  const list = [];
  snap.forEach(doc => {
    list.push({ id: doc.id, ...doc.data() });
  });

  // Sort by questionCode
  list.sort((a, b) => a.questionCode.localeCompare(b.questionCode, undefined, { numeric: true, sensitivity: 'base' }));

  const outPath = path.resolve('backups/staging/mh9_scit_5_raw.json');
  fs.writeFileSync(outPath, JSON.stringify(list, null, 2), 'utf8');
  console.log(`Saved raw Chapter 5 questions to: ${outPath}`);

  // Summary diagnostics
  let emptySol = 0;
  let noneOfAbove = 0;
  let dashes = 0;
  let placeholderOpts = 0;
  let leakedNotes = 0;

  list.forEach(q => {
    if (!q.solution || q.solution.trim() === '') emptySol++;
    if (q.options) {
      q.options.forEach(opt => {
        const lower = opt.toLowerCase();
        if (lower.includes('none of above') || lower.includes('none of the above')) noneOfAbove++;
        if (/^option\s+[a-d]$/i.test(opt.trim())) placeholderOpts++;
        if (opt.includes('Wrong:') || opt.includes('Right:')) leakedNotes++;
      });
    }
    if (q.text && q.text.includes('---')) dashes++;
  });

  console.log('\n--- Raw Chapter 5 Diagnostic Audit ---');
  console.log('Total Questions:', list.length);
  console.log('Empty Solutions:', emptySol, `(${(emptySol / list.length * 100).toFixed(1)}%)`);
  console.log('"None of the above" occurrences in options:', noneOfAbove);
  console.log('Placeholder options ("Option A", etc.):', placeholderOpts);
  console.log('Leaked Teacher Notes in options:', leakedNotes);
  console.log('Fill-in Dashes ("---"):', dashes);
}

extract().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
