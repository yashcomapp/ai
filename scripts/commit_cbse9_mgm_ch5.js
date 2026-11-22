// scripts/commit_cbse9_mgm_ch5.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  return origLookup.call(dns, hostname, options, (err, address, family) => {
    if (err) return callback(err, address, family);
    if (Array.isArray(address)) {
      const ipv4Only = address.filter(a => a.family === 4);
      return callback(null, ipv4Only.length > 0 ? ipv4Only : address);
    }
    return callback(null, address, family);
  });
};
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING CBSE-9-MGM CHAPTER 5 (640 QUESTIONS) ===\n');

  const ch5File = path.join(__dirname, 'clean_cbse9_mgm_ch5_questions.json');

  if (!fs.existsSync(ch5File)) {
    throw new Error('Question file clean_cbse9_mgm_ch5_questions.json missing!');
  }

  const ch5Questions = JSON.parse(fs.readFileSync(ch5File, 'utf8'));

  console.log(`Loaded ${ch5Questions.length} questions for Chapter 5.`);

  if (ch5Questions.length !== 640) {
    throw new Error(`Expected strictly 640 questions, got ${ch5Questions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapter 5 of CBSE-9-MGM
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh5 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 5)
    .get();

  const totalExisting = existingCh5.size;
  console.log(`Existing questions found for Ch 5: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_mgm_ch5`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_mgm_ch5_640q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: existingCh5.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 5 (legacy 260 questions)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = existingCh5.docs;
    const BATCH_SIZE = 400;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 640 questions
  console.log(`\nStep 3: Uploading ${ch5Questions.length} new questions in batches of 400...`);
  const BATCH_SIZE = 400;
  for (let i = 0; i < ch5Questions.length; i += BATCH_SIZE) {
    const chunk = ch5Questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions).`);
  }
  console.log('All 640 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh5 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 5)
    .get();

  console.log(`Verification: Ch 5 = ${verifyCh5.size} / 640`);

  if (verifyCh5.size === 640) {
    console.log('\n✅ SUCCESS: All 640 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 5 has ${verifyCh5.size} questions, expected 640`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
