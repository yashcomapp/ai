// scripts/audit_mh9_scit_gaps.js
const fs = require('fs');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function audit() {
  console.log('Auditing MH-9-SCIT existing questions and deficits...');
  const doc = await adminDb.collection('syllabus').doc('mh_9_scit').get();
  const d = doc.data();

  // Fetch all existing questions for MH-9-SCIT
  const qSnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .select('topicCode', 'vault', 'difficulty', 'questionCode')
    .get();

  console.log('Total questions in Firestore for MH-9-SCIT:', qSnap.size);

  const qMap = {};
  qSnap.docs.forEach(docSnap => {
    const q = docSnap.data();
    const tc = q.topicCode;
    if (!qMap[tc]) {
      qMap[tc] = { total: 0, exam: 0, practice: 0, foundation: 0, codes: [] };
    }
    qMap[tc].total++;
    const v = q.vault || 'exam';
    if (qMap[tc][v] !== undefined) qMap[tc][v]++;
    qMap[tc].codes.push(q.questionCode || docSnap.id);
  });

  const auditReport = [];
  let totalDeficit = 0;

  d.chapters.forEach(ch => {
    const chData = {
      chapterNumber: ch.number,
      chapterName: ch.name,
      subtopics: [],
      chapterTotal: 0,
      chapterTarget: 0,
      chapterDeficit: 0
    };

    if (ch.topics) {
      ch.topics.forEach(t => {
        if (t.subtopics) {
          t.subtopics.forEach(st => {
            const tc = st.topicCode;
            const stats = qMap[tc] || { total: 0, exam: 0, practice: 0, foundation: 0, codes: [] };
            const neededTotal = Math.max(0, 80 - stats.total);
            const neededExam = Math.max(0, 40 - stats.exam);
            const neededPractice = Math.max(0, 20 - stats.practice);
            const neededFoundation = Math.max(0, 20 - stats.foundation);

            chData.chapterTotal += stats.total;
            chData.chapterTarget += 80;
            chData.chapterDeficit += neededTotal;
            totalDeficit += neededTotal;

            chData.subtopics.push({
              topicCode: tc,
              name: st.name,
              current: stats.total,
              currentBreakdown: { exam: stats.exam, practice: stats.practice, foundation: stats.foundation },
              needed: neededTotal,
              neededBreakdown: { exam: neededExam, practice: neededPractice, foundation: neededFoundation }
            });
          });
        }
      });
    }

    auditReport.push(chData);
  });

  const outFile = 'scripts/mh9_scit_audit_report.json';
  fs.writeFileSync(outFile, JSON.stringify({ totalDeficit, chapters: auditReport }, null, 2), 'utf8');
  console.log('Audit complete! Total deficit across all subtopics:', totalDeficit);
  console.log(`Detailed matrix saved to ${outFile}`);

  auditReport.forEach(ch => {
    const status = ch.chapterDeficit === 0 ? 'COMPLETE' : `DEFICIT: ${ch.chapterDeficit}`;
    console.log(`Ch ${ch.chapterNumber} (${ch.chapterName}): Current ${ch.chapterTotal} / ${ch.chapterTarget} -> [${status}]`);
  });
}

audit().catch(err => {
  console.error('Audit failed:', err);
  process.exit(1);
});
