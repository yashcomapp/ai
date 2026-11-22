// scripts/commit_cbse9_mgm_ch9.js
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const resolver = new dns.Resolver();
resolver.setServers(['8.8.8.8', '1.1.1.1']);
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  if (hostname && (hostname.endsWith('googleapis.com') || hostname.endsWith('google.com'))) {
    return resolver.resolve4(hostname, (err, ips) => {
      if (!err && ips && ips.length > 0) {
        if (options && options.all) {
          return callback(null, ips.map(ip => ({ address: ip, family: 4 })));
        }
        return callback(null, ips[0], 4);
      }
      return origLookup.call(dns, hostname, options, callback);
    });
  }
  return origLookup.call(dns, hostname, options, callback);
};
const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== COMMITTING CBSE-9-MGM CHAPTER 9 (560 QUESTIONS) ===\n');

  const ch9File = path.join(__dirname, 'clean_cbse9_mgm_ch9_questions.json');

  if (!fs.existsSync(ch9File)) {
    throw new Error('Question file clean_cbse9_mgm_ch9_questions.json missing!');
  }

  const ch9Questions = JSON.parse(fs.readFileSync(ch9File, 'utf8'));

  console.log(`Loaded ${ch9Questions.length} questions for Chapter 9.`);

  if (ch9Questions.length !== 560) {
    throw new Error(`Expected strictly 560 questions, got ${ch9Questions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapter 9 of CBSE-9-MGM
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh9 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 9)
    .get();

  const totalExisting = existingCh9.size;
  console.log(`Existing questions found for Ch 9: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_mgm_ch9`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_mgm_ch9_560q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: existingCh9.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 9 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches...`);
    const allExistingDocs = existingCh9.docs;
    const BATCH_SIZE = 400;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 560 questions
  console.log(`\nStep 3: Uploading ${ch9Questions.length} new questions in batches of 400...`);
  const BATCH_SIZE = 400;
  for (let i = 0; i < ch9Questions.length; i += BATCH_SIZE) {
    const chunk = ch9Questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await batch.commit();
    console.log(`  Committed batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions).`);
  }
  console.log('All 560 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh9 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MGM')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 9)
    .get();

  console.log(`Verification: Ch 9 = ${verifyCh9.size} / 560`);

  if (verifyCh9.size === 560) {
    console.log('\n✅ SUCCESS: All 560 questions verified in Firestore with 100% precision!');
  } else {
    throw new Error(`Verification mismatch: Ch 9 has ${verifyCh9.size} questions, expected 560`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
