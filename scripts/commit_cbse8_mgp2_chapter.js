// scripts/commit_cbse8_mgp2_chapter.js
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
  console.log(`=== COMMITTING CBSE-8-MGP2 CHAPTER ${chNum} TOP-UP TO FIRESTORE ===`);
  console.log(`===========================================================`);

  const chFile = path.join(__dirname, `cbse8_mgp2_ch${chNum}_topup.json`);
  if (!fs.existsSync(chFile)) {
    throw new Error(`File not found: ${chFile}`);
  }

  const questions = JSON.parse(fs.readFileSync(chFile, 'utf8'));
  console.log(`Loaded ${questions.length} validated questions for Chapter ${chNum}.`);

  // 1. Query existing questions in Firestore
  const prefix = `CBSE-8-MGP2-${chNum}-`;
  const existingSnap = await adminDb.collection('questions')
    .where('topicCode', '>=', prefix)
    .where('topicCode', '<=', prefix + '\uf8ff')
    .get();

  const totalExisting = existingSnap.size;
  console.log(`Existing questions found in Firestore for Ch ${chNum}: ${totalExisting}`);

  // 2. Pre-mutation snapshot (Rule Q)
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}_commit_cbse8_mgp2_ch${chNum}`;
  const snapshotFile = path.join(targetDir, `${snapshotId}.json`);

  const existingDocs = existingSnap.docs.map(d => ({ id: d.id, ...d.data() }));
  const sylDocBefore = await adminDb.collection('syllabus').doc('cbse_8_mgp2').get();

  fs.writeFileSync(snapshotFile, JSON.stringify({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Pre-mutation backup before committing CBSE-8-MGP2 Ch ${chNum} (${questions.length} questions)`,
    counts: {
      existingQuestions: totalExisting,
      topUpQuestions: questions.length
    },
    syllabusDocBefore: sylDocBefore.data(),
    existingQuestions: existingDocs
  }, null, 2));

  await adminDb.collection('_systemBackups').doc(snapshotId).set({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Pre-mutation backup before committing CBSE-8-MGP2 Ch ${chNum} (${questions.length} questions)`,
    counts: {
      existingQuestions: totalExisting,
      topUpQuestions: questions.length
    },
    filePath: snapshotFile
  });
  console.log(`Pre-mutation snapshot created: ${snapshotId}`);

  // 3. Batch write questions
  const now = new Date();
  const BATCH_SIZE = 400;
  for (let i = 0; i < questions.length; i += BATCH_SIZE) {
    const chunk = questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();

    chunk.forEach(q => {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      const payload = {
        ...q,
        subjectCode: 'MGP2',
        boardCode: 'CBSE',
        board: 'CBSE',
        class: '8',
        chapterNumber: Number(chNum),
        createdAt: now,
        updatedAt: now
      };
      batch.set(docRef, payload, { merge: true });
    });

    console.log(`  Writing questions ${i + 1} to ${i + chunk.length}...`);
    await commitWithRetry(batch);
  }
  console.log(`Successfully written all ${questions.length} questions.`);

  // 4. Update syllabus document
  const sylRef = adminDb.collection('syllabus').doc('cbse_8_mgp2');
  const sylSnap = await sylRef.get();
  if (sylSnap.exists) {
    const data = sylSnap.data();
    const chapters = data.chapters || [];
    const ch = chapters.find(c => String(c.number || c.chapterNumber) === String(chNum));
    if (ch) {
      (ch.topics || []).forEach(top => {
        const subtopics = top.subtopics || [];
        if (subtopics.length > 0) {
          subtopics.forEach(sub => {
            const count = questions.filter(q => q.topicCode === (sub.topicCode || sub.code)).length;
            sub.objectiveCount = (sub.objectiveCount || 0) + count;
          });
        } else {
          const count = questions.filter(q => q.topicCode === (top.topicCode || top.code)).length;
          top.objectiveCount = (top.objectiveCount || 0) + count;
        }
      });
      data.objectiveCount = (data.objectiveCount || 0) + questions.length;
      data.updatedAt = now;
      await sylRef.update({ chapters, objectiveCount: data.objectiveCount, updatedAt: now });
      console.log(`Updated syllabus cbse_8_mgp2 objectiveCount -> ${data.objectiveCount}`);
    }
  }

  // 5. Update syllabusTopicIndex
  const uniqueTopics = [...new Set(questions.map(q => q.topicCode))];
  console.log(`Updating syllabusTopicIndex for ${uniqueTopics.length} topics...`);
  const indexBatch = adminDb.batch();
  for (const tCode of uniqueTopics) {
    const idxRef = adminDb.collection('syllabusTopicIndex').doc(tCode);
    const addedCount = questions.filter(q => q.topicCode === tCode).length;
    const docSnap = await idxRef.get();
    if (docSnap.exists) {
      const cur = docSnap.data().objectiveCount || 0;
      indexBatch.update(idxRef, { objectiveCount: cur + addedCount, updatedAt: now });
    }
  }
  await commitWithRetry(indexBatch);
  console.log(`Updated syllabusTopicIndex for all ${uniqueTopics.length} topics.`);

  console.log(`=== FINISHED CBSE-8-MGP2 CHAPTER ${chNum} SUCCESSFULLY ===\n`);
}

const targetCh = process.argv[2];
if (!targetCh) {
  console.error('Usage: node scripts/commit_cbse8_mgp2_chapter.js <chapterNumber>');
  process.exit(1);
}

commitChapter(targetCh).catch(err => {
  console.error(`Fatal error during Chapter ${targetCh} commit:`, err);
  process.exit(1);
});
