const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const fs = require('fs');

const class10Subjects = [
  { id: 'cbse_10_math', board: 'CBSE', code: 'MATH', name: 'CBSE 10 Mathematics' },
  { id: 'cbse_10_sci', board: 'CBSE', code: 'SCI', name: 'CBSE 10 Science' },
  { id: 'mh_10_mth1', board: 'MH', code: 'MTH1', name: 'MH 10 Mathematics Part 1 (Algebra)' },
  { id: 'mh_10_mth2', board: 'MH', code: 'MTH2', name: 'MH 10 Mathematics Part 2 (Geometry)' },
  { id: 'mh_10_scit1', board: 'MH', code: 'SCIT1', name: 'MH 10 Science & Technology Part 1' },
  { id: 'mh_10_scit2', board: 'MH', code: 'SCIT2', name: 'MH 10 Science & Technology Part 2' }
];

async function extractClass10DeficitManifest() {
  console.log('================================================================================');
  console.log('=== EXTRACTING CLASS 10 DEFICIT MANIFEST ACROSS ALL 6 SUBJECTS ===');
  console.log('================================================================================');

  const fullManifest = [];
  let grandTotalNeeded = 0;
  let grandTotalSubtopics = 0;

  for (const subj of class10Subjects) {
    console.log(`\nAnalyzing ${subj.id} (${subj.name})...`);
    const sDoc = await adminDb.collection('syllabus').doc(subj.id).get();
    if (!sDoc.exists) {
      console.warn(`Syllabus doc ${subj.id} not found!`);
      continue;
    }

    const sData = sDoc.data();
    const chapters = sData.chapters || [];
    const subjEntry = {
      subjectId: subj.id,
      boardCode: subj.board,
      subjectCode: subj.code,
      subjectName: subj.name,
      totalChapters: chapters.length,
      totalLeafSubtopics: 0,
      totalCurrent: 0,
      totalTarget: 0,
      totalDeficit: 0,
      chapters: []
    };

    for (let cIdx = 0; cIdx < chapters.length; cIdx++) {
      const ch = chapters[cIdx];
      const chNum = ch.chapterNumber || ch.number || (cIdx + 1);
      const chName = ch.chapterName || ch.name || `Chapter ${chNum}`;

      const chEntry = {
        chapterNumber: chNum,
        chapterName: chName,
        totalLeafSubtopics: 0,
        currentQuestions: 0,
        targetQuestions: 0,
        deficitNeeded: 0,
        subtopics: []
      };

      // Traverse topics and subtopics
      for (const top of (ch.topics || [])) {
        if (top.subtopics && top.subtopics.length > 0) {
          for (const sub of top.subtopics) {
            const tc = sub.topicCode || sub.code;
            const subName = sub.name || sub.title;
            const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
            const count = qSnap.size;

            let maxSeq = 0;
            let examCount = 0;
            let practiceCount = 0;
            let foundationCount = 0;

            qSnap.forEach(d => {
              const qd = d.data();
              const qCode = qd.questionCode || '';
              const match = qCode.match(/-(\d+)$/);
              if (match) {
                const seq = parseInt(match[1], 10);
                if (seq > maxSeq) maxSeq = seq;
              }
              const v = (qd.vault || 'exam').toLowerCase();
              if (v === 'practice') practiceCount++;
              else if (v === 'foundation') foundationCount++;
              else examCount++;
            });

            const target = 80;
            const deficit = Math.max(0, target - count);

            chEntry.subtopics.push({
              topicCode: tc,
              name: subName,
              currentCount: count,
              highestSeq: maxSeq,
              targetCount: target,
              deficit,
              vaults: { exam: examCount, practice: practiceCount, foundation: foundationCount }
            });

            chEntry.totalLeafSubtopics++;
            chEntry.currentQuestions += count;
            chEntry.targetQuestions += target;
            chEntry.deficitNeeded += deficit;
          }
        } else {
          const tc = top.topicCode || top.code;
          const topName = top.name || top.title;
          const qSnap = await adminDb.collection('questions').where('topicCode', '==', tc).get();
          const count = qSnap.size;

          let maxSeq = 0;
          let examCount = 0;
          let practiceCount = 0;
          let foundationCount = 0;

          qSnap.forEach(d => {
            const qd = d.data();
            const qCode = qd.questionCode || '';
            const match = qCode.match(/-(\d+)$/);
            if (match) {
              const seq = parseInt(match[1], 10);
              if (seq > maxSeq) maxSeq = seq;
            }
            const v = (qd.vault || 'exam').toLowerCase();
            if (v === 'practice') practiceCount++;
            else if (v === 'foundation') foundationCount++;
            else examCount++;
          });

          const target = 80;
          const deficit = Math.max(0, target - count);

          chEntry.subtopics.push({
            topicCode: tc,
            name: topName,
            currentCount: count,
            highestSeq: maxSeq,
            targetCount: target,
            deficit,
            vaults: { exam: examCount, practice: practiceCount, foundation: foundationCount }
          });

          chEntry.totalLeafSubtopics++;
          chEntry.currentQuestions += count;
          chEntry.targetQuestions += target;
          chEntry.deficitNeeded += deficit;
        }
      }

      subjEntry.totalLeafSubtopics += chEntry.totalLeafSubtopics;
      subjEntry.totalCurrent += chEntry.currentQuestions;
      subjEntry.totalTarget += chEntry.targetQuestions;
      subjEntry.totalDeficit += chEntry.deficitNeeded;

      console.log(`  Ch ${String(chNum).padStart(2)}: ${chName.padEnd(45)} | Subs: ${String(chEntry.totalLeafSubtopics).padStart(2)} | Current: ${String(chEntry.currentQuestions).padStart(4)} | Deficit: ${String(chEntry.deficitNeeded).padStart(4)}`);
      subjEntry.chapters.push(chEntry);
    }

    grandTotalSubtopics += subjEntry.totalLeafSubtopics;
    grandTotalNeeded += subjEntry.totalDeficit;
    fullManifest.push(subjEntry);
    console.log(`✓ ${subj.id}: Total Subs: ${subjEntry.totalLeafSubtopics} | Current: ${subjEntry.totalCurrent} | Target: ${subjEntry.totalTarget} | Deficit: ${subjEntry.totalDeficit}`);
  }

  console.log('\n================================================================================');
  console.log('CLASS 10 MANIFEST SUMMARY:');
  console.log(`  Total Subjects:          ${fullManifest.length}`);
  console.log(`  Total Leaf Subtopics:    ${grandTotalSubtopics}`);
  console.log(`  Total Questions Needed:  ${grandTotalNeeded}`);
  console.log('================================================================================');

  fs.mkdirSync('./scripts/audit_data', { recursive: true });
  fs.writeFileSync('./scripts/audit_data/class10_deficit_manifest.json', JSON.stringify(fullManifest, null, 2));
  console.log('Saved manifest to scripts/audit_data/class10_deficit_manifest.json');
  process.exit(0);
}

extractClass10DeficitManifest().catch(err => {
  console.error(err);
  process.exit(1);
});
