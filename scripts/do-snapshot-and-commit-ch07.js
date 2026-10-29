const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function commitCh07() {
  const db = admin.firestore();

  // 1. Mandatory Pre-mutation snapshot (Rule 2Q)
  console.log('--- Step 1: Creating Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(
    ['questions', 'syllabus'],
    'chapter_7_energy_flow_in_ecosystem_initial_stock_120q'
  );
  console.log(`Snapshot created at: ${snapResult.snapshotPath}`);

  // 2. Load enhanced questions
  const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_07_enhanced.json', 'utf8'));
  console.log(`--- Step 2: Committing ${qs.length} questions to Firestore ---`);

  const BATCH_SIZE = 40;
  for (let i = 0; i < qs.length; i += BATCH_SIZE) {
    const chunk = qs.slice(i, i + BATCH_SIZE);
    const batch = db.batch();

    chunk.forEach(q => {
      // Document ID: by questionCode
      const docRef = db.collection('questions').doc(q.questionCode);
      const payload = {
        questionCode: q.questionCode,
        chapterNumber: 7,
        class: '9',
        subjectCode: 'SCIT',
        boardCode: 'MH',
        topicCode: q.topicCode,
        type: q.type,
        difficulty: q.difficulty || 'Medium',
        text: q.text,
        options: q.options || [],
        correctAnswer: q.correctAnswer,
        solution: q.solution,
        status: 'active',
        isLegacy: false,
        isDisputed: false,
        marks: q.marks || (q.type === 'OAR' || q.type === 'OSC' || q.type === 'OMC' || q.type === 'OTF' ? 4 : 2),
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        createdAt: admin.firestore.FieldValue.serverTimestamp()
      };
      batch.set(docRef, payload, { merge: true });
    });

    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} questions).`);
  }

  // 3. Update syllabus document mh_9_scit
  console.log('--- Step 3: Updating mh_9_scit syllabus document ---');
  const sylRef = db.collection('syllabus').doc('mh_9_scit');
  const sylSnap = await sylRef.get();
  if (sylSnap.exists) {
    const sylData = sylSnap.data();
    const chs = sylData.chapters || [];
    const ch7 = chs.find(c => parseInt(c.number || c.id, 10) === 7);
    if (ch7) {
      let chTotal = 0;
      (ch7.topics || []).forEach(t => {
        const tc = t.topicCode || t.code;
        const topicQs = qs.filter(q => q.topicCode === tc);
        t.objectiveCount = topicQs.length;
        t.subjectiveCount = 0;
        chTotal += topicQs.length;
      });
      ch7.objectiveCount = chTotal;
      ch7.subjectiveCount = 0;
    }

    // Recalculate total subject counts
    let totalObj = 0;
    chs.forEach(c => {
      totalObj += (c.objectiveCount || 0);
    });
    sylData.objectiveCount = totalObj;
    sylData.updatedAt = admin.firestore.FieldValue.serverTimestamp();

    await sylRef.set(sylData, { merge: true });
    console.log(`Updated mh_9_scit syllabus: Chapter 7 objectiveCount = ${ch7 ? ch7.objectiveCount : 0}, total subject objectiveCount = ${totalObj}`);
  }

  // 4. Update syllabusTopicIndex for Chapter 7 topics
  console.log('--- Step 4: Updating syllabusTopicIndex for Chapter 7 ---');
  const topics7 = [
    { code: 'MH-9-SCIT-7-7.1', name: 'Food Chain, Food Web & Trophic Levels', count: 40 },
    { code: 'MH-9-SCIT-7-7.2', name: 'The Energy Pyramid & Lindeman 10% Energy Rule', count: 40 },
    { code: 'MH-9-SCIT-7-7.3', name: 'Biogeochemical Cycles: Carbon Cycle, Oxygen Cycle, Nitrogen Cycle', count: 40 }
  ];

  const indexBatch = db.batch();
  topics7.forEach(t => {
    const idxRef = db.collection('syllabusTopicIndex').doc(t.code);
    indexBatch.set(idxRef, {
      topicCode: t.code,
      topicName: t.name,
      chapterNumber: 7,
      chapterName: 'Energy Flow in an Ecosystem',
      class: '9',
      subjectCode: 'SCIT',
      boardCode: 'MH',
      objectiveCount: t.count,
      subjectiveCount: 0,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });
  await indexBatch.commit();
  console.log('Updated 3 topics in syllabusTopicIndex.');

  console.log('\n🎉 ALL 120 CHAPTER 7 QUESTIONS COMMITTED AND SYNCED SUCCESSFULLY!');
}

commitCh07().catch(console.error);
