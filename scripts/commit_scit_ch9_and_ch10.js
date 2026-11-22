// scripts/commit_scit_ch9_and_ch10.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING MH-9-SCIT CHAPTER 9 & CHAPTER 10 (1,040 QUESTIONS) ===\n');

  const ch9File = path.join(__dirname, 'mh9_scit_ch9_all_560.json');
  const ch10File = path.join(__dirname, 'mh9_scit_ch10_all_480.json');

  if (!fs.existsSync(ch9File) || !fs.existsSync(ch10File)) {
    throw new Error('Question files missing!');
  }

  const ch9Questions = JSON.parse(fs.readFileSync(ch9File, 'utf8'));
  const ch10Questions = JSON.parse(fs.readFileSync(ch10File, 'utf8'));
  const allQuestions = [...ch9Questions, ...ch10Questions];

  console.log(`Loaded ${ch9Questions.length} questions for Chapter 9.`);
  console.log(`Loaded ${ch10Questions.length} questions for Chapter 10.`);
  console.log(`Total questions to commit: ${allQuestions.length}`);

  if (allQuestions.length !== 1040) {
    throw new Error(`Expected strictly 1,040 questions, got ${allQuestions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapters 9 and 10 of MH-9-SCIT
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh9 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 9)
    .get();

  const existingCh10 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 10)
    .get();

  const totalExisting = existingCh9.size + existingCh10.size;
  console.log(`Existing questions found: Ch 9 = ${existingCh9.size}, Ch 10 = ${existingCh10.size} (Total = ${totalExisting})`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_scit_ch9_and_ch10`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_scit_ch9_and_ch10_1040q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: [
      ...existingCh9.docs.map(d => ({ id: d.id, data: d.data() })),
      ...existingCh10.docs.map(d => ({ id: d.id, data: d.data() }))
    ]
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 9 & 10 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = [...existingCh9.docs, ...existingCh10.docs];
    const BATCH_SIZE = 400;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 1,040 questions
  console.log(`\nStep 3: Uploading ${allQuestions.length} new questions in batches of 400...`);
  const BATCH_SIZE = 400;
  for (let i = 0; i < allQuestions.length; i += BATCH_SIZE) {
    const chunk = allQuestions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions).`);
  }
  console.log('All 1,040 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh9 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 9)
    .get();

  const verifyCh10 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 10)
    .get();

  console.log(`Verification: Ch 9 = ${verifyCh9.size} / 560, Ch 10 = ${verifyCh10.size} / 480`);

  if (verifyCh9.size === 560 && verifyCh10.size === 480) {
    console.log('\n✅ SUCCESS: All 1,040 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 9 has ${verifyCh9.size}, Ch 10 has ${verifyCh10.size}`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
