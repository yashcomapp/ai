const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  const sylSnap = await adminDb.collection('syllabus').get();
  console.log(`Loaded ${sylSnap.size} syllabus documents.`);

  const summary = [];
  const allEmpty = [];

  for (const doc of sylSnap.docs) {
    const syl = doc.data();
    const docId = doc.id;
    const board = syl.board || '';
    const cls = syl.class || '';
    const subject = syl.subject || '';
    const subjectCode = syl.subjectCode || '';

    const leaves = [];
    for (const ch of (syl.chapters || [])) {
      const chNum = Number(ch.number || ch.chapterNumber);
      const chName = ch.name || ch.chapterName;
      for (const t of (ch.topics || [])) {
        if (Array.isArray(t.subtopics) && t.subtopics.length > 0) {
          for (const s of t.subtopics) {
            leaves.push({
              ch: chNum,
              chName,
              code: s.subtopicCode || s.topicCode,
              name: s.name || s.subtopicName,
              type: 'subtopic',
            });
          }
        } else {
          leaves.push({
            ch: chNum,
            chName,
            code: t.topicCode,
            name: t.name || t.topicName,
            type: 'topic',
          });
        }
      }
    }

    // Run count() in parallel chunks of 40 to stay fast and low-cost
    const emptyLeaves = [];
    const partialLeaves = [];
    let totalQuestions = 0;

    for (let i = 0; i < leaves.length; i += 40) {
      const chunk = leaves.slice(i, i + 40);
      const counts = await Promise.all(
        chunk.map(async (leaf) => {
          if (!leaf.code) return 0;
          const snap = await adminDb
            .collection('questions')
            .where('topicCode', '==', leaf.code)
            .count()
            .get();
          return snap.data().count;
        })
      );
      chunk.forEach((leaf, idx) => {
        const c = counts[idx];
        totalQuestions += c;
        if (c === 0) {
          emptyLeaves.push({ ...leaf, count: 0 });
        } else if (c < 80) {
          partialLeaves.push({ ...leaf, count: c });
        }
      });
    }

    summary.push({
      docId,
      board,
      class: cls,
      subjectCode,
      subject,
      totalLeaves: leaves.length,
      totalQuestions,
      emptyCount: emptyLeaves.length,
      partialCount: partialLeaves.length,
      emptyLeaves,
    });

    if (emptyLeaves.length > 0) {
      allEmpty.push({ docId, board, class: cls, subject, emptyCount: emptyLeaves.length, emptyLeaves });
    }

    console.log(
      `${docId.padEnd(16)} | ${board.padEnd(4)} Cl.${String(cls).padEnd(2)} | ${subject.padEnd(36)} | leaves: ${String(leaves.length).padStart(3)} | Qs: ${String(totalQuestions).padStart(5)} | empty: ${String(emptyLeaves.length).padStart(3)} | partial(<80): ${partialLeaves.length}`
    );
  }

  const outPath = path.join(__dirname, 'audit_data', 'all_subjects_empty_audit.json');
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify({ summary, allEmpty }, null, 2), 'utf8');
  console.log('\nSaved full audit to:', outPath);
  process.exit(0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
