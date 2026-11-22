// scripts/commit_all_mh9_scit_topups.js
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
try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

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

async function commitChapter(chNum) {
  console.log(`\n===========================================================`);
  console.log(`=== COMMITTING MH-9-SCIT CHAPTER ${chNum} TOP-UP TO FIRESTORE ===`);
  console.log(`===========================================================`);

  const chFile = path.join(__dirname, `mh9_scit_ch${chNum}_topup.json`);
  if (!fs.existsSync(chFile)) {
    throw new Error(`File not found: ${chFile}`);
  }

  const questions = JSON.parse(fs.readFileSync(chFile, 'utf8'));
  console.log(`Loaded ${questions.length} clean questions for Chapter ${chNum}.`);

  // 1. Query existing questions in Firestore
  const existingSnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', chNum)
    .get();

  const totalExisting = existingSnap.size;
  console.log(`Existing questions found in Firestore for Ch ${chNum}: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule 2Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_mh9_scit_ch${chNum}`;
  const snapshotPath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      createdAtISO: now.toISOString(),
      reason: `commit_mh9_scit_ch${chNum}_topup`,
      chapterNumber: chNum,
      totalExistingDocuments: totalExisting,
      newQuestionsToCommit: questions.length,
      filePath: snapshotPath
    },
    existingQuestions: existingSnap.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(snapshotPath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`Pre-mutation snapshot saved: ${snapshotPath}`);

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`Recorded snapshot in _systemBackups.`);

  // 3. Batch commit in chunks of 50
  console.log(`Writing ${questions.length} questions in batches of 50...`);
  const BATCH_SIZE = 50;
  let currentBatch = adminDb.batch();
  let opCount = 0;
  let batchNum = 1;

  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const docRef = adminDb.collection('questions').doc(q.questionCode);

    currentBatch.set(docRef, {
      code: q.questionCode,
      questionCode: q.questionCode,
      text: q.text,
      options: q.options,
      correctAnswer: q.correctAnswer,
      solution: q.solution,
      difficulty: q.difficulty,
      topicCode: q.topicCode,
      subtopic: q.subtopic || q.topicCode,
      chapterNumber: chNum,
      subjectCode: 'SCIT',
      class: '9',
      boardCode: 'MH',
      type: 'OSC',
      vault: q.vault,
      marks: 4,
      negativeMarks: 1,
      status: 'active',
      bloomsTaxonomy: q.bloomsTaxonomy || 'understand',
      estimatedTime: q.estimatedTime || 60,
      updatedAt: new Date()
    });
    opCount++;

    if (opCount === BATCH_SIZE) {
      process.stdout.write(`  Batch #${batchNum} (${opCount} Qs)... `);
      await commitWithRetry(currentBatch);
      console.log('Done.');
      currentBatch = adminDb.batch();
      opCount = 0;
      batchNum++;
    }
  }

  if (opCount > 0) {
    process.stdout.write(`  Final Batch #${batchNum} (${opCount} Qs)... `);
    await commitWithRetry(currentBatch);
    console.log('Done.');
  }

  // 4. Verify Firestore count
  const verifySnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('chapterNumber', '==', chNum)
    .get();

  console.log(`✅ Chapter ${chNum} verified in Firestore: ${verifySnap.size} questions total.`);
}

async function main() {
  const args = process.argv.slice(2);
  let chaptersToProcess = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18];

  const chArg = args.find(a => a.startsWith('--chapter='));
  if (chArg) {
    const target = parseInt(chArg.split('=')[1], 10);
    chaptersToProcess = [target];
  }

  console.log(`Starting commit pipeline for chapters: ${chaptersToProcess.join(', ')}`);

  for (const chNum of chaptersToProcess) {
    await commitChapter(chNum);
  }

  console.log('\n===========================================================');
  console.log('🎉 ALL TARGETED CHAPTERS COMMITTED SUCCESSFULLY!');
  console.log('===========================================================');
}

main().catch(err => {
  console.error('Fatal error during commit pipeline:', err);
  process.exit(1);
});
