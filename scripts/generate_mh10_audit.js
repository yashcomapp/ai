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
      return origLookup(hostname, options, callback);
    });
  }
  return origLookup(hostname, options, callback);
};

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

const SUBJECT_DOCS = [
  { docId: 'mh_10_mth1', code: 'MH-10-MTH1', name: 'Mathematics Part - 1 (Algebra)' },
  { docId: 'mh_10_mth2', code: 'MH-10-MTH2', name: 'Mathematics Part - 2 (Geometry)' },
  { docId: 'mh_10_scit1', code: 'MH-10-SCIT1', name: 'Science and Technology Part - 1' },
  { docId: 'mh_10_scit2', code: 'MH-10-SCIT2', name: 'Science and Technology Part - 2' }
];

async function auditSubject(sub) {
  console.log(`\n================================================================`);
  console.log(`Auditing ${sub.code} (${sub.name})...`);
  const sylDoc = await adminDb.collection('syllabus').doc(sub.docId).get();
  if (!sylDoc.exists) {
    console.error(`Syllabus doc ${sub.docId} NOT FOUND!`);
    return null;
  }
  const sylData = sylDoc.data();
  const leafSubtopics = [];

  function traverse(chNumber, chName, tNumber, tName, item) {
    if (item.subtopics && item.subtopics.length > 0) {
      for (const st of item.subtopics) {
        traverse(chNumber, chName, item.number || tNumber, item.name || tName, st);
      }
    } else {
      leafSubtopics.push({
        chapterNumber: chNumber,
        chapterName: chName,
        topicNumber: tNumber,
        topicName: tName,
        subtopicNumber: item.number,
        subtopicName: item.name,
        topicCode: item.topicCode || `${sub.code}-${chNumber}-${item.number}`
      });
    }
  }

  if (sylData.chapters) {
    for (const ch of sylData.chapters) {
      if (ch.topics) {
        for (const t of ch.topics) {
          traverse(ch.number, ch.name, t.number, t.name, t);
        }
      }
    }
  }

  console.log(`Found ${leafSubtopics.length} leaf subtopics in syllabus.`);

  // Now query questions in Firestore for this subject
  console.log(`Fetching questions from Firestore for ${sub.code}...`);
  const snap = await adminDb.collection('questions')
    .where('topicCode', '>=', sub.code)
    .where('topicCode', '<=', sub.code + '\uf8ff')
    .select('topicCode', 'questionCode', 'vault')
    .get();

  console.log(`Total questions in Firestore for ${sub.code}: ${snap.size}`);

  const questionsByTopic = {};
  snap.forEach(d => {
    const data = d.data();
    const tc = data.topicCode;
    if (!questionsByTopic[tc]) {
      questionsByTopic[tc] = {
        count: 0,
        examCount: 0,
        practiceCount: 0,
        foundationCount: 0,
        maxSeq: 0,
        codes: []
      };
    }
    const item = questionsByTopic[tc];
    item.count++;
    const v = data.vault || 'exam';
    if (v === 'exam') item.examCount++;
    else if (v === 'practice') item.practiceCount++;
    else if (v === 'foundation') item.foundationCount++;

    const qc = data.questionCode || '';
    item.codes.push(qc);
    const m = qc.match(/-(\d{3})$/);
    if (m) {
      const seq = parseInt(m[1], 10);
      if (seq > item.maxSeq) item.maxSeq = seq;
    }
  });

  const auditReport = [];
  let totalCurrent = 0;
  let totalDeficit = 0;

  for (const leaf of leafSubtopics) {
    const qData = questionsByTopic[leaf.topicCode] || {
      count: 0,
      examCount: 0,
      practiceCount: 0,
      foundationCount: 0,
      maxSeq: 0
    };
    const needed = Math.max(0, 80 - qData.count);
    totalCurrent += qData.count;
    totalDeficit += needed;

    // Calculate vault needs
    // Ideal: 40 exam, 20 practice, 20 foundation
    const examNeeded = Math.max(0, 40 - qData.examCount);
    const practiceNeeded = Math.max(0, 20 - qData.practiceCount);
    const foundationNeeded = Math.max(0, 20 - qData.foundationCount);

    auditReport.push({
      chapterNumber: leaf.chapterNumber,
      chapterName: leaf.chapterName,
      topicNumber: leaf.topicNumber,
      topicName: leaf.topicName,
      subtopicNumber: leaf.subtopicNumber,
      subtopicName: leaf.subtopicName,
      topicCode: leaf.topicCode,
      current: qData.count,
      needed: needed,
      maxSeq: qData.maxSeq,
      examCurrent: qData.examCount,
      practiceCurrent: qData.practiceCount,
      foundationCurrent: qData.foundationCount,
      examNeeded,
      practiceNeeded,
      foundationNeeded
    });
  }

  console.log(`Summary for ${sub.code}:`);
  console.log(`  Leaf subtopics: ${leafSubtopics.length}`);
  console.log(`  Total questions currently in Firestore: ${totalCurrent}`);
  console.log(`  Total target (80 * ${leafSubtopics.length}): ${leafSubtopics.length * 80}`);
  console.log(`  Total deficit: ${totalDeficit}`);

  const outPath = path.join(__dirname, 'audit_data', `${sub.docId}_audit.json`);
  fs.writeFileSync(outPath, JSON.stringify(auditReport, null, 2));
  console.log(`Saved audit report to ${outPath}`);

  return { sub, leafCount: leafSubtopics.length, current: totalCurrent, deficit: totalDeficit, auditReport };
}

async function main() {
  const results = [];
  for (const sub of SUBJECT_DOCS) {
    const res = await auditSubject(sub);
    results.push(res);
  }
  console.log(`\n================================================================`);
  console.log(`OVERALL MAHARASHTRA CLASS 10 AUDIT SUMMARY:`);
  let grandTarget = 0;
  let grandCurrent = 0;
  let grandDeficit = 0;
  for (const r of results) {
    if (r) {
      const target = r.leafCount * 80;
      grandTarget += target;
      grandCurrent += r.current;
      grandDeficit += r.deficit;
      console.log(`  ${r.sub.code.padEnd(14)}: ${r.current.toString().padStart(5)} / ${target.toString().padStart(5)} (Deficit: ${r.deficit.toString().padStart(5)}) across ${r.leafCount} subtopics`);
    }
  }
  console.log(`  -------------------------------------------------------------`);
  console.log(`  TOTAL         : ${grandCurrent.toString().padStart(5)} / ${grandTarget.toString().padStart(5)} (Deficit: ${grandDeficit.toString().padStart(5)})`);
  console.log(`================================================================`);
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
