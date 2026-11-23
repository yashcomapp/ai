// scripts/commit_cbse9_scie_ch4.js
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
  console.log('=== COMMITTING CBSE-9-SCIE CHAPTER 4 (640 QUESTIONS) ===\n');

  const ch4File = path.join(__dirname, 'clean_cbse9_scie_ch4_questions.json');
  if (!fs.existsSync(ch4File)) {
    throw new Error('Question file clean_cbse9_scie_ch4_questions.json missing!');
  }

  const ch4Questions = JSON.parse(fs.readFileSync(ch4File, 'utf8'));
  console.log(`Loaded ${ch4Questions.length} questions for Chapter 4.`);

  if (ch4Questions.length !== 640) {
    throw new Error(`Expected strictly 640 questions, got ${ch4Questions.length}`);
  }

  // 1. Query any existing questions in Firestore for Chapter 4 of CBSE-9-SCIE
  console.log('\nStep 1: Checking for existing questions in Firestore...');
  const existingCh4 = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 4)
    .get();

  const totalExisting = existingCh4.size;
  console.log(`Existing questions found for Ch 4: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse9_scie_ch4`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: 'commit_cbse9_scie_ch4_640q',
      totalExistingDocuments: totalExisting,
      filePath: snapshotPath
    },
    existingQuestions: existingCh4.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`\nStep 2: Pre-mutation snapshot saved to: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Batch commit to Firestore
  console.log('\nStep 3: Writing 640 questions in batches...');
  const BATCH_SIZE = 100;
  let currentBatch = adminDb.batch();
  let opCount = 0;
  let batchNum = 1;

  for (let i = 0; i < ch4Questions.length; i++) {
    const q = ch4Questions[i];
    const docRef = adminDb.collection('questions').doc(q.questionCode);

    currentBatch.set(docRef, {
      ...q,
      updatedAt: new Date()
    });
    opCount++;

    if (opCount === BATCH_SIZE) {
      process.stdout.write(`  Committing batch #${batchNum} (${opCount} questions)... `);
      await commitWithRetry(currentBatch);
      console.log('Done.');
      currentBatch = adminDb.batch();
      opCount = 0;
      batchNum++;
    }
  }

  if (opCount > 0) {
    process.stdout.write(`  Committing final batch #${batchNum} (${opCount} questions)... `);
    await commitWithRetry(currentBatch);
    console.log('Done.');
  }

  console.log('\nAll 640 questions successfully written to Firestore.');

  // 4. Verification in Firestore
  console.log('\nStep 4: Verifying Firestore question counts for Chapter 4...');
  const verifySnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIE')
    .where('class', '==', '9')
    .where('chapterNumber', '==', 4)
    .get();

  console.log(`Verified count in Firestore: ${verifySnap.size} / 640 questions.`);

  const subtopicCounts = {};
  verifySnap.docs.forEach(doc => {
    const data = doc.data();
    subtopicCounts[data.topicCode] = (subtopicCounts[data.topicCode] || 0) + 1;
  });

  console.log('\nFirestore Breakdown by Subtopic:');
  for (const [tc, count] of Object.entries(subtopicCounts).sort()) {
    console.log(`  ${tc}: ${count} questions`);
  }

  if (verifySnap.size === 640) {
    console.log('\n🎉 CHAPTER 4 VERIFICATION COMPLETE: 100% SUCCESS!');
  } else {
    console.error(`\n⚠️ Mismatch in count: Expected 640, found ${verifySnap.size}`);
    process.exit(1);
  }
}

main().catch(err => {
  console.error('Fatal error committing Chapter 4:', err);
  process.exit(1);
});
