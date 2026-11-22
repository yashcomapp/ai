// scripts/commit_cbse9_mgm_ch1_and_ch2.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING CBSE-9-MGM CHAPTER 1 & CHAPTER 2 (1,040 QUESTIONS) ===\n');

  const ch1File = path.join(__dirname, 'clean_cbse9_mgm_ch1_questions.json');
  const ch2File = path.join(__dirname, 'clean_cbse9_mgm_ch2_questions.json');

  if (!fs.existsSync(ch1File) || !fs.existsSync(ch2File)) {
    throw new Error('Question files missing!');
  }

  const ch1Questions = JSON.parse(fs.readFileSync(ch1File, 'utf8'));
  const ch2Questions = JSON.parse(fs.readFileSync(ch2File, 'utf8'));
  const allQuestions = [...ch1Questions, ...ch2Questions];

  console.log(`Loaded ${ch1Questions.length} questions for Chapter 1.`);
  console.log(`Loaded ${ch2Questions.length} questions for Chapter 2.`);
  console.log(`Total questions to commit: ${allQuestions.length}`);

  if (allQuestions.length !== 1040) {
    throw new Error(`Expected strictly 1,040 questions, got ${allQuestions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapters 1 and 2 of CBSE-9-MGM
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh1 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 1)
    .get();

  const existingCh2 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 2)
    .get();

  const totalExisting = existingCh1.size + existingCh2.size;
  console.log(`Existing questions found: Ch 1 = ${existingCh1.size}, Ch 2 = ${existingCh2.size} (Total = ${totalExisting})`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_mgm_ch1_and_ch2`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_mgm_ch1_and_ch2_1040q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: [
      ...existingCh1.docs.map(d => ({ id: d.id, data: d.data() })),
      ...existingCh2.docs.map(d => ({ id: d.id, data: d.data() }))
    ]
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 1 & 2 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = [...existingCh1.docs, ...existingCh2.docs];
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
  const verifyCh1 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 1)
    .get();

  const verifyCh2 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 2)
    .get();

  console.log(`Verification: Ch 1 = ${verifyCh1.size} / 560, Ch 2 = ${verifyCh2.size} / 480`);

  if (verifyCh1.size === 560 && verifyCh2.size === 480) {
    console.log('\n✅ SUCCESS: All 1,040 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 1 has ${verifyCh1.size}, Ch 2 has ${verifyCh2.size}`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
