// scripts/inspect_cbse9.js
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function inspect(syllabusId) {
  const doc = await adminDb.collection('syllabus').doc(syllabusId).get();
  if (!doc.exists) {
    console.log(syllabusId, 'not found');
    return;
  }
  const data = doc.data();
  console.log(`\n======================================================`);
  console.log(`SYLLABUS: ${syllabusId} (${data.subject || data.subjectName})`);
  console.log(`Board: ${data.boardCode} | Class: ${data.class} | SubjectCode: ${data.subjectCode}`);
  console.log(`======================================================`);
  let totalLeaves = 0;
  let totalZeros = 0;
  (data.chapters || []).forEach(ch => {
    let leaves = [];
    (ch.topics || []).forEach(t => {
      if (t.subtopics && t.subtopics.length > 0) {
        t.subtopics.forEach(st => leaves.push({
          code: st.topicCode || st.subtopicCode,
          name: st.name || st.subtopicName,
          qCount: (st.objectiveCount || 0) + (st.questionCount || 0)
        }));
      } else {
        leaves.push({
          code: t.topicCode,
          name: t.name || t.topicName,
          qCount: (t.objectiveCount || 0) + (t.questionCount || 0)
        });
      }
    });
    totalLeaves += leaves.length;
    const zeroCount = leaves.filter(l => l.qCount === 0).length;
    totalZeros += zeroCount;
    console.log(`\nCh ${ch.number}: ${ch.name} | Total Leaves: ${leaves.length} | Zero Leaves: ${zeroCount} | Obj Qs: ${ch.objectiveCount || 0}`);
    leaves.forEach(l => {
      console.log(`   - ${l.code}: "${l.name}" [Qs: ${l.qCount}]`);
    });
  });
  console.log(`\nSUMMARY for ${syllabusId}: ${totalLeaves} leaf topics total, ${totalZeros} zero topics.`);
}

async function run() {
  await inspect('cbse_9_mgm');
  await inspect('cbse_9_scie');
}
run();
