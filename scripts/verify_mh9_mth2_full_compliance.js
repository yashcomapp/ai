// scripts/verify_mh9_mth2_full_compliance.js
// Audits all 68 subtopics of MH-9-MTH2 (Chapters 1 to 9)
// Verifies Rule 2T: >= 40 Exam, >= 20 Practice, >= 20 Foundation, >= 80 Total per subtopic.

const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function main() {
  console.log('=== Verifying 100% Full Subject Compliance for MH-9-MTH2 ===');
  
  // 1. Fetch syllabus structure for mh_9_mth2
  const sylDoc = await adminDb.collection('syllabus').doc('mh_9_mth2').get();
  if (!sylDoc.exists) {
    console.error('Syllabus document mh_9_mth2 not found!');
    process.exit(1);
  }
  const sylData = sylDoc.data();
  
  const allSubtopics = [];
  sylData.chapters.forEach(ch => {
    ch.topics.forEach(t => {
      (t.subtopics || []).forEach(st => {
        allSubtopics.push({
          chapterNumber: ch.number,
          chapterName: ch.name,
          topicCode: st.topicCode,
          subtopicNumber: st.number,
          subtopicName: st.name
        });
      });
    });
  });
  console.log(`Total subtopics registered in syllabus: ${allSubtopics.length}`);

  // 2. Fetch all questions in MH-9-MTH2 from Firestore
  const qSnap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'MTH2')
    .where('class', '==', '9')
    .get();

  console.log(`Total questions in Firestore for MH-9-MTH2: ${qSnap.size}`);

  const countsByTopic = {};
  qSnap.forEach(d => {
    const q = d.data();
    const tc = q.topicCode;
    if (!tc) return;
    if (!countsByTopic[tc]) {
      countsByTopic[tc] = { exam: 0, practice: 0, foundation: 0, total: 0 };
    }
    const vault = q.vault || q.source || 'exam';
    if (vault === 'exam') countsByTopic[tc].exam++;
    else if (vault === 'practice') countsByTopic[tc].practice++;
    else if (vault === 'foundation') countsByTopic[tc].foundation++;
    countsByTopic[tc].total++;
  });

  // 3. Evaluate each subtopic against Rule 2T
  let compliantCount = 0;
  let nonCompliantCount = 0;
  const nonCompliantList = [];

  allSubtopics.forEach(st => {
    const counts = countsByTopic[st.topicCode] || { exam: 0, practice: 0, foundation: 0, total: 0 };
    const isCompliant = counts.exam >= 40 && counts.practice >= 20 && counts.foundation >= 20 && counts.total >= 80;
    if (isCompliant) {
      compliantCount++;
    } else {
      nonCompliantCount++;
      nonCompliantList.push({
        topicCode: st.topicCode,
        chapter: st.chapterNumber,
        name: st.subtopicName,
        counts
      });
    }
  });

  console.log('\n================ AUDIT SUMMARY ================');
  console.log(`Total Subtopics Checked : ${allSubtopics.length}`);
  console.log(`Compliant Subtopics     : ${compliantCount}`);
  console.log(`Non-Compliant Subtopics : ${nonCompliantCount}`);

  if (nonCompliantCount > 0) {
    console.error('\nNON-COMPLIANT SUBTOPICS DETECTED:');
    nonCompliantList.forEach(item => {
      console.error(`- [${item.topicCode}] Ch ${item.chapter} (${item.name}): Exam=${item.counts.exam}/40, Practice=${item.counts.practice}/20, Foundation=${item.counts.foundation}/20, Total=${item.counts.total}/80`);
    });
    process.exit(1);
  } else {
    console.log('\n🎉 ALL 68 SUBTOPICS IN MH-9-MTH2 ARE 100% COMPLIANT WITH RULE 2T!');
    process.exit(0);
  }
}

main().catch(console.error);
