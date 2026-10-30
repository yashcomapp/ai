const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

const SUBJECTIVE_CODES = new Set(['SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN']);

async function syncMh10Mth2() {
  console.log('=== TARGETED SYNC: MH-10-MTH2 ===');
  
  // 1. Fetch only MH Class 10 MTH2 questions
  const qSnap = await db.collection('questions')
    .where('subjectCode', '==', 'MTH2')
    .where('class', '==', '10')
    .get();

  console.log(`Fetched ${qSnap.size} questions for MH Class 10 MTH2.`);

  const topicObjCounts = {};
  const topicSubjCounts = {};
  let totalObj = 0;
  let totalSubj = 0;

  qSnap.docs.forEach(doc => {
    const data = doc.data();
    const tCode = data.topicCode;
    const isSubj = SUBJECTIVE_CODES.has(data.type);

    if (isSubj) {
      topicSubjCounts[tCode] = (topicSubjCounts[tCode] || 0) + 1;
      totalSubj++;
    } else {
      topicObjCounts[tCode] = (topicObjCounts[tCode] || 0) + 1;
      totalObj++;
    }
  });

  // 2. Update syllabus doc
  const sylRef = db.collection('syllabus').doc('mh_10_mth2');
  const sylDoc = await sylRef.get();
  if (!sylDoc.exists) {
    console.error('mh_10_mth2 syllabus doc not found!');
    return;
  }

  const sylData = sylDoc.data();
  let updatedChapters = (sylData.chapters || []).map(ch => {
    let chObj = 0;
    let chSubj = 0;
    const updatedTopics = (ch.topics || []).map(t => {
      const obj = topicObjCounts[t.topicCode] || 0;
      const subj = topicSubjCounts[t.topicCode] || 0;
      chObj += obj;
      chSubj += subj;
      return {
        ...t,
        objectiveCount: obj,
        subjectiveCount: subj
      };
    });
    return {
      ...ch,
      topics: updatedTopics,
      objectiveCount: chObj,
      subjectiveCount: chSubj
    };
  });

  await sylRef.update({
    chapters: updatedChapters,
    objectiveCount: totalObj,
    subjectiveCount: totalSubj,
    updatedAt: new Date()
  });
  console.log(`Updated syllabus/mh_10_mth2: ${totalObj} Obj / ${totalSubj} Subj`);

  // 3. Update syllabusTopicIndex for mh_10_mth2 topics
  console.log('Updating syllabusTopicIndex for MH-10-MTH2 topics...');
  const batch = db.batch();
  let batchCount = 0;

  for (const ch of updatedChapters) {
    for (const t of (ch.topics || [])) {
      const idxRef = db.collection('syllabusTopicIndex').doc(t.topicCode);
      batch.set(idxRef, {
        topicCode: t.topicCode,
        topicName: t.name || t.topicName || '',
        chapterNumber: parseInt(ch.number || ch.chapterNumber || 1),
        chapterName: ch.name || ch.chapterName || '',
        board: sylData.board || 'Maharashtra Board',
        boardCode: 'MH',
        class: '10',
        subject: sylData.subject || 'Mathematics Part - 2 (Geometry)',
        subjectCode: 'MTH2',
        objectiveCount: t.objectiveCount || 0,
        subjectiveCount: t.subjectiveCount || 0,
        updatedAt: new Date()
      }, { merge: true });
      batchCount++;
    }
  }

  await batch.commit();
  console.log(`Updated ${batchCount} syllabusTopicIndex documents for MH-10-MTH2.`);
  console.log('=== SYNC COMPLETED SUCCESSFULLY ===');
}

syncMh10Mth2().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
