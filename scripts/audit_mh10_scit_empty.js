const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const report = {};
  for (const [docId, prefix] of [['mh_10_scit1', 'MH-10-SCIT1'], ['mh_10_scit2', 'MH-10-SCIT2']]) {
    const sylSnap = await adminDb.collection('syllabus').doc(docId).get();
    if (!sylSnap.exists) throw new Error(`Missing syllabus/${docId}`);
    const syl = sylSnap.data();

    const qSnap = await adminDb.collection('questions')
      .where('topicCode', '>=', prefix + '-')
      .where('topicCode', '<=', prefix + '-\uf8ff')
      .select('topicCode', 'status', 'disputed')
      .get();

    const counts = {};
    qSnap.forEach(d => {
      const q = d.data();
      if (q.status === 'quarantined' || q.disputed) return;
      counts[q.topicCode] = (counts[q.topicCode] || 0) + 1;
    });

    const empty = [];
    const partial = [];
    let totalLeaves = 0;

    for (const ch of (syl.chapters || [])) {
      const chNum = Number(ch.number || ch.chapterNumber);
      const chName = ch.name || ch.chapterName;
      for (const t of (ch.topics || [])) {
        if (Array.isArray(t.subtopics) && t.subtopics.length > 0) {
          for (const s of t.subtopics) {
            totalLeaves++;
            const code = s.subtopicCode || s.topicCode;
            const c = counts[code] || 0;
            const entry = { ch: chNum, chName, code, name: s.name || s.subtopicName, count: c };
            if (c === 0) empty.push(entry);
            else if (c < 80) partial.push(entry);
          }
        } else {
          totalLeaves++;
          const code = t.topicCode;
          const c = counts[code] || 0;
          const entry = { ch: chNum, chName, code, name: t.name || t.topicName, count: c };
          if (c === 0) empty.push(entry);
          else if (c < 80) partial.push(entry);
        }
      }
    }

    report[docId] = {
      subjectCode: syl.subjectCode,
      subjectName: syl.subject,
      totalLeaves,
      totalActiveQuestions: Object.values(counts).reduce((a, b) => a + b, 0),
      emptyCount: empty.length,
      partialCount: partial.length,
      empty,
      partial
    };
    console.log(`${docId}: ${totalLeaves} leaves | ${empty.length} empty | ${partial.length} partial (<80)`);
  }

  const outPath = path.join(__dirname, 'audit_data', 'mh10_scit_empty_targets.json');
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify(report, null, 2), 'utf8');
  console.log('Saved audit targets to:', outPath);
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
