// scripts/commit_scit_ch19_and_ch20.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING MH-9-SCIT CHAPTER 19 & CHAPTER 20 (1,840 QUESTIONS) ===\n');

  const ch19File = path.join(__dirname, 'clean_scit_ch19_questions.json');
  const ch20File = path.join(__dirname, 'clean_scit_ch20_questions.json');

  if (!fs.existsSync(ch19File) || !fs.existsSync(ch20File)) {
    throw new Error('Question files missing!');
  }

  const ch19Questions = JSON.parse(fs.readFileSync(ch19File, 'utf8'));
  const ch20Questions = JSON.parse(fs.readFileSync(ch20File, 'utf8'));
  const allQuestions = [...ch19Questions, ...ch20Questions];

  console.log(`Loaded ${ch19Questions.length} questions for Chapter 19.`);
  console.log(`Loaded ${ch20Questions.length} questions for Chapter 20.`);
  console.log(`Total questions to commit: ${allQuestions.length}`);

  if (allQuestions.length !== 1840) {
    throw new Error(`Expected strictly 1,840 questions, got ${allQuestions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapters 19 and 20 of MH-9-SCIT
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh19 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 19)
    .get();

  const existingCh20 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 20)
    .get();

  const totalExisting = existingCh19.size + existingCh20.size;
  console.log(`Existing questions found: Ch 19 = ${existingCh19.size}, Ch 20 = ${existingCh20.size} (Total = ${totalExisting})`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_scit_ch19_and_ch20`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_scit_ch19_and_ch20_1840q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: [
      ...existingCh19.docs.map(d => ({ id: d.id, data: d.data() })),
      ...existingCh20.docs.map(d => ({ id: d.id, data: d.data() }))
    ]
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 19 & 20 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = [...existingCh19.docs, ...existingCh20.docs];
    const BATCH_SIZE = 400;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 1,840 questions
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
  console.log('All 1,840 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh19 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 19)
    .get();

  const verifyCh20 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 20)
    .get();

  console.log(`Verification: Ch 19 = ${verifyCh19.size} / 960, Ch 20 = ${verifyCh20.size} / 880`);

  if (verifyCh19.size === 960 && verifyCh20.size === 880) {
    console.log('\n✅ SUCCESS: All 1,840 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 19 has ${verifyCh19.size}, Ch 20 has ${verifyCh20.size}`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
