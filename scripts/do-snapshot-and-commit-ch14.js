const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function commitCh14() {
  const db = admin.firestore();

  // 1. Mandatory Pre-mutation snapshot (Rule 2Q)
  console.log('--- Step 1: Creating Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(
    ['questions', 'syllabus'],
    'chapter_14_substances_in_common_use_initial_stock_160q'
  );
  console.log('Snapshot successfully recorded in _systemBackups');

  // 2. Load enhanced questions
  const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_14_enhanced.json', 'utf8'));
  console.log(`--- Step 2: Committing ${qs.length} questions to Firestore ---`);

  const BATCH_SIZE = 40;
  for (let i = 0; i < qs.length; i += BATCH_SIZE) {
    const chunk = qs.slice(i, i + BATCH_SIZE);
    const batch = db.batch();

    chunk.forEach(q => {
      const docRef = db.collection('questions').doc(q.questionCode);
      const payload = {
        questionCode: q.questionCode,
        chapterNumber: 14,
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
    const ch14 = chs.find(c => parseInt(c.number || c.id, 10) === 14);
    if (ch14) {
      let chTotal = 0;
      (ch14.topics || []).forEach(t => {
        const tc = t.topicCode || t.code;
        const topicQs = qs.filter(q => q.topicCode === tc);
        t.objectiveCount = topicQs.length;
        t.subjectiveCount = 0;
        chTotal += topicQs.length;
      });
      ch14.objectiveCount = chTotal;
      ch14.subjectiveCount = 0;
    }

    // Recalculate total subject counts
    let totalObj = 0;
    chs.forEach(c => {
      totalObj += (c.objectiveCount || 0);
    });
    sylData.objectiveCount = totalObj;
    sylData.updatedAt = admin.firestore.FieldValue.serverTimestamp();

    await sylRef.set(sylData, { merge: true });
    console.log(`Updated mh_9_scit syllabus: Chapter 14 objectiveCount = ${ch14 ? ch14.objectiveCount : 0}, total subject objectiveCount = ${totalObj}`);
  }

  // 4. Update syllabusTopicIndex for Chapter 14 topics
  console.log('--- Step 4: Updating syllabusTopicIndex for Chapter 14 ---');
  const topics14 = [
    { code: 'MH-9-SCIT-14-14.1', name: 'Important Salts: Common Salt (NaCl), Baking Soda (NaHCO3), Washing Soda (Na2CO3·10H2O)', count: 40 },
    { code: 'MH-9-SCIT-14-14.2', name: 'Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O)', count: 40 },
    { code: 'MH-9-SCIT-14-14.3', name: 'Radioactive Substances & Alpha, Beta, Gamma Rays', count: 40 },
    { code: 'MH-9-SCIT-14-14.4', name: 'Chemical Substances in Day-to-Day Life (Food Colors, Dyes, Artificial Sweeteners, Deodorants, Teflon, Ceramics)', count: 40 }
  ];

  const indexBatch = db.batch();
  topics14.forEach(t => {
    const idxRef = db.collection('syllabusTopicIndex').doc(t.code);
    indexBatch.set(idxRef, {
      topicCode: t.code,
      topicName: t.name,
      chapterNumber: 14,
      chapterName: 'Substances in Common Use',
      class: '9',
      subjectCode: 'SCIT',
      boardCode: 'MH',
      objectiveCount: t.count,
      subjectiveCount: 0,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });
  await indexBatch.commit();
  console.log('Updated 4 topics in syllabusTopicIndex.');

  console.log('\n🎉 ALL 160 CHAPTER 14 QUESTIONS COMMITTED AND SYNCED SUCCESSFULLY!');
}

commitCh14().catch(console.error);
