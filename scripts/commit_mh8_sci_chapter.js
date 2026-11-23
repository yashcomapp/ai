// scripts/commit_mh8_sci_chapter.js
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
  console.log(`=== COMMITTING MH-8-SCI CHAPTER ${chNum} TOP-UP TO FIRESTORE ===`);
  console.log(`===========================================================`);

  const chFile = path.join(__dirname, `mh8_sci_ch${chNum}_topup.json`);
  if (!fs.existsSync(chFile)) {
    throw new Error(`File not found: ${chFile}`);
  }

  const questions = JSON.parse(fs.readFileSync(chFile, 'utf8'));
  console.log(`Loaded ${questions.length} validated questions for Chapter ${chNum}.`);

  // 1. Query existing questions in Firestore
  const prefix = `MH-8-SCI-${chNum}-`;
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
  const snapshotId = `snapshot_${timestamp}_commit_mh8_sci_ch${chNum}`;
  const snapshotFile = path.join(targetDir, `${snapshotId}.json`);

  const existingDocs = existingSnap.docs.map(d => ({ id: d.id, ...d.data() }));
  const sylDocBefore = await adminDb.collection('syllabus').doc('mh_8_sci').get();

  fs.writeFileSync(snapshotFile, JSON.stringify({
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: `Pre-mutation backup before committing MH-8-SCI Ch ${chNum} (${questions.length} questions)`,
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
    reason: `Pre-mutation backup before committing MH-8-SCI Ch ${chNum} (${questions.length} questions)`,
    counts: {
      existingQuestions: totalExisting,
      topUpQuestions: questions.length
    },
    createdAt: new Date().toISOString()
  });

  console.log(`Pre-mutation snapshot created: ${snapshotId}`);

  // 3. Batch write questions
  const BATCH_SIZE = 400;
  for (let i = 0; i < questions.length; i += BATCH_SIZE) {
    const chunk = questions.slice(i, i + BATCH_SIZE);
    const batch = adminDb.batch();
    console.log(`  Writing questions ${i + 1} to ${i + chunk.length}...`);

    for (const q of chunk) {
      const docRef = adminDb.collection('questions').doc(q.questionCode);
      batch.set(docRef, {
        ...q,
        subjectCode: 'mh_8_sci',
        board: 'MH',
        class: '8',
        updatedAt: new Date().toISOString()
      }, { merge: true });
    }

    await commitWithRetry(batch);
  }
  console.log(`Successfully written all ${questions.length} questions.`);

  // 4. Update syllabus document counts and syllabusTopicIndex for current chapter
  const sylDocRef = adminDb.collection('syllabus').doc('mh_8_sci');
  const sylDoc = await sylDocRef.get();
  if (sylDoc.exists) {
    const sylData = sylDoc.data();
    const topicUpdates = {};

    for (const chapter of (sylData.chapters || [])) {
      const thisChNum = String(chapter.number || chapter.chapterNumber);
      if (thisChNum === String(chNum)) {
        let chCount = 0;
        for (const topic of (chapter.topics || [])) {
          if (topic.subtopics && topic.subtopics.length > 0) {
            let topCount = 0;
            for (const sub of topic.subtopics) {
              const subCode = sub.topicCode || sub.code;
              const snap = await adminDb.collection('questions')
                .where('topicCode', '==', subCode)
                .get();
              sub.objectiveCount = snap.size;
              topCount += snap.size;
              topicUpdates[subCode] = {
                topicCode: subCode,
                topicName: sub.name || sub.title,
                parentTopicCode: topic.topicCode || topic.code,
                parentTopicName: topic.name || topic.title,
                chapterNumber: chapter.number || chapter.chapterNumber,
                chapterName: chapter.name || chapter.title,
                subjectCode: 'mh_8_sci',
                boardCode: 'MH',
                class: '8',
                questionCount: snap.size
              };
            }
            topic.objectiveCount = topCount;
            chCount += topCount;
          } else {
            const topCode = topic.topicCode || topic.code;
            const snap = await adminDb.collection('questions')
              .where('topicCode', '==', topCode)
              .get();
            topic.objectiveCount = snap.size;
            chCount += snap.size;
            topicUpdates[topCode] = {
              topicCode: topCode,
              topicName: topic.name || topic.title,
              chapterNumber: chapter.number || chapter.chapterNumber,
              chapterName: chapter.name || chapter.title,
              subjectCode: 'mh_8_sci',
              boardCode: 'MH',
              class: '8',
              questionCount: snap.size
            };
          }
        }
        chapter.objectiveCount = chCount;
      }
    }

    const totalSubjectQs = (sylData.chapters || []).reduce((acc, c) => acc + (c.objectiveCount || 0), 0);
    sylData.objectiveCount = totalSubjectQs;
    sylData.updatedAt = new Date().toISOString();
    await sylDocRef.set(sylData, { merge: true });
    console.log(`Updated syllabus mh_8_sci objectiveCount -> ${totalSubjectQs}`);

    // Update syllabusTopicIndex for touched subtopics
    const touchedCodes = Object.keys(topicUpdates);
    console.log(`Updating syllabusTopicIndex for ${touchedCodes.length} topics...`);
    const indexBatch = adminDb.batch();
    for (const code of touchedCodes) {
      const idxRef = adminDb.collection('syllabusTopicIndex').doc(code);
      indexBatch.set(idxRef, topicUpdates[code], { merge: true });
    }
    await commitWithRetry(indexBatch);
    console.log(`Updated syllabusTopicIndex for all ${touchedCodes.length} topics.`);
  }

  console.log(`=== FINISHED MH-8-SCI CHAPTER ${chNum} SUCCESSFULLY ===\n`);
}

const targetChapter = process.argv[2];
if (!targetChapter) {
  console.error("Usage: node scripts/commit_mh8_sci_chapter.js <chapterNumber>");
  process.exit(1);
}

commitChapter(targetChapter).then(() => {
  process.exit(0);
}).catch(err => {
  console.error("Commit failed:", err);
  process.exit(1);
});
