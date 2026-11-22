// scripts/replace_mh9_mth1_all.js
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const jsonPath = path.join(__dirname, 'mh9_mth1_all_flawless.json');
  if (!fs.existsSync(jsonPath)) {
    throw new Error('mh9_mth1_all_flawless.json not found!');
  }
  const newQuestions = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  console.log(`Loaded ${newQuestions.length} flawless questions from mh9_mth1_all_flawless.json`);

  if (newQuestions.length !== 6080) {
    throw new Error(`Expected strictly 6080 questions, found ${newQuestions.length}`);
  }

  // 1. Fetch current MH-9-MTH1 questions from Firestore
  console.log('Querying existing MH-9-MTH1 questions from Firestore...');
  const existingSnap = await adminDb.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'MTH1')
    .get();

  console.log(`Found ${existingSnap.size} existing questions in Firestore.`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_replace_mh9_mth1_all`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'replace_mh9_mth1_flawless_6080',
      totalDocuments: existingSnap.size,
      filePath: snapshotPath
    },
    data: existingSnap.docs.map(doc => ({ id: doc.id, data: doc.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Batch delete existing questions
  console.log(`Deleting ${existingSnap.size} existing questions in batches...`);
  const BATCH_SIZE = 400;
  const existingDocs = existingSnap.docs;
  for (let i = 0; i < existingDocs.length; i += BATCH_SIZE) {
    const chunk = existingDocs.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(doc => {
      batch.delete(doc.ref);
    });
    await batch.commit();
    console.log(`  Deleted batch ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(existingDocs.length / BATCH_SIZE)} (${chunk.length} docs)`);
  }

  // 4. Batch insert new questions
  console.log(`Inserting ${newQuestions.length} flawless questions in batches...`);
  for (let i = 0; i < newQuestions.length; i += BATCH_SIZE) {
    const chunk = newQuestions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Inserted batch ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(newQuestions.length / BATCH_SIZE)} (${chunk.length} docs)`);
  }

  console.log('🎉 All 6,080 questions successfully written to Firestore for MH-9-MTH1!');
}

main().catch(err => {
  console.error('Fatal error during replacement:', err);
  process.exit(1);
});
