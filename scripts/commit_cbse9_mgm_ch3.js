// scripts/commit_cbse9_mgm_ch3.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING CBSE-9-MGM CHAPTER 3 (800 QUESTIONS) ===\n');

  const ch3File = path.join(__dirname, 'clean_cbse9_mgm_ch3_questions.json');

  if (!fs.existsSync(ch3File)) {
    throw new Error('Question file clean_cbse9_mgm_ch3_questions.json missing!');
  }

  const ch3Questions = JSON.parse(fs.readFileSync(ch3File, 'utf8'));

  console.log(`Loaded ${ch3Questions.length} questions for Chapter 3.`);

  if (ch3Questions.length !== 800) {
    throw new Error(`Expected strictly 800 questions, got ${ch3Questions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapter 3 of CBSE-9-MGM
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh3 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 3)
    .get();

  const totalExisting = existingCh3.size;
  console.log(`Existing questions found for Ch 3: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_mgm_ch3`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_mgm_ch3_800q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: existingCh3.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 3 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = existingCh3.docs;
    const BATCH_SIZE = 400;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 800 questions
  console.log(`\nStep 3: Uploading ${ch3Questions.length} new questions in batches of 400...`);
  const BATCH_SIZE = 400;
  for (let i = 0; i < ch3Questions.length; i += BATCH_SIZE) {
    const chunk = ch3Questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions).`);
  }
  console.log('All 800 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh3 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 3)
    .get();

  console.log(`Verification: Ch 3 = ${verifyCh3.size} / 800`);

  if (verifyCh3.size === 800) {
    console.log('\n✅ SUCCESS: All 800 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 3 has ${verifyCh3.size} questions, expected 800`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
