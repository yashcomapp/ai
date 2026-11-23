// scripts/commit_cbse9_scie_ch2.js
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

async function commitWithRetry(batch, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await batch.commit();
      return;
    } catch (err) {
      console.warn(`    Batch commit attempt ${attempt} failed: ${err.message}. Retrying...`);
      if (attempt === retries) throw err;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
}

async function main() {
  console.log('=== COMMITTING CBSE-9-SCIE CHAPTER 2 (720 QUESTIONS) ===\n');

  const ch2File = path.join(__dirname, 'clean_cbse9_scie_ch2_questions.json');
  if (!fs.existsSync(ch2File)) {
    throw new Error('Question file clean_cbse9_scie_ch2_questions.json missing!');
  }

  const ch2Questions = JSON.parse(fs.readFileSync(ch2File, 'utf8'));
  console.log(`Loaded ${ch2Questions.length} questions for Chapter 2.`);

  if (ch2Questions.length !== 720) {
    throw new Error(`Expected strictly 720 questions, got ${ch2Questions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapter 2 of CBSE-9-SCIE
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh2 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 2)
    .get();

  const totalExisting = existingCh2.size;
  console.log(`Existing questions found for Ch 2: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_scie_ch2`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_scie_ch2_720q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: existingCh2.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Delete any stale existing questions in Ch 2 (if any)
  if (totalExisting > 0) {
    console.log(`Deleting ${totalExisting} existing questions in batches of 100...`);
    const allExistingDocs = existingCh2.docs;
    const BATCH_SIZE = 100;
    for (let i = 0; i < allExistingDocs.length; i += BATCH_SIZE) {
      const chunk = allExistingDocs.slice(i, i + BATCH_SIZE);
      const batch = adminDb.batch();
      chunk.forEach(doc => batch.delete(doc.ref));
      await commitWithRetry(batch);
    }
    console.log('Stale questions deleted.');
  }

  // 4. Batch write all 720 questions in batches of 100
  console.log(`\nStep 3: Uploading ${ch2Questions.length} new questions in batches of 100...`);
  const BATCH_SIZE = 100;
  for (let i = 0; i < ch2Questions.length; i += BATCH_SIZE) {
    const chunk = ch2Questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, q);
    });
    await commitWithRetry(batch);
    console.log(`  Committed batch ${Math.floor(i / BATCH_SIZE) + 1} / ${Math.ceil(ch2Questions.length / BATCH_SIZE)} (${chunk.length} questions).`);
  }
  console.log('All 720 questions successfully written to Firestore.');

  // 5. Verification
  console.log('\nStep 4: Verifying upload in Firestore...');
  const verifyCh2 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 2)
    .get();

  console.log(`Verified count in Firestore for Chapter 2: ${verifyCh2.size} / 720`);

  const subtopicMap = {};
  verifyCh2.forEach(doc => {
    const data = doc.data();
    subtopicMap[data.topicCode] = (subtopicMap[data.topicCode] || 0) + 1;
  });

  console.log('\nPer-subtopic distribution in Firestore:');
  Object.keys(subtopicMap).sort().forEach(st => {
    console.log(`  ${st}: ${subtopicMap[st]} questions`);
  });

  if (verifyCh2.size !== 720) {
    throw new Error(`Verification mismatch: expected 720, found ${verifyCh2.size}`);
  }

  console.log('\n=== CBSE-9-SCIE CHAPTER 2 FULLY COMMITTED AND 100% VERIFIED ===');
}

main().catch(err => {
  console.error('Error committing CBSE-9-SCIE Chapter 2:', err);
  process.exit(1);
});
