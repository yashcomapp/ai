const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function commitCh16() {
  const db = admin.firestore();

  // 1. Mandatory Pre-mutation snapshot (Rule 2Q)
  console.log('--- Step 1: Creating Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(
    ['questions', 'syllabus'],
    'chapter_16_heredity_and_variation_initial_stock_200q'
  );
  console.log('Snapshot successfully recorded in _systemBackups');

  // 2. Load enhanced questions
  const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_16_enhanced.json', 'utf8'));
  console.log(`--- Step 2: Committing ${qs.length} questions to Firestore ---`);

  const BATCH_SIZE = 40;
  for (let i = 0; i < qs.length; i += BATCH_SIZE) {
    const chunk = qs.slice(i, i + BATCH_SIZE);
    const batch = db.batch();

    chunk.forEach(q => {
      const docRef = db.collection('questions').doc(q.questionCode);
      const payload = {
        questionCode: q.questionCode,
        chapterNumber: 16,
        class: '9',
        subjectCode: 'SCIT',
        boardCode: 'MH',
        topicCode: q.topicCode,
        type: q.typeCode || q.type,
        difficulty: q.difficulty || 'Medium',
        text: q.text,
        options: q.options || [],
        correctAnswer: q.correctOption !== undefined ? q.correctOption : q.correctAnswer,
        solution: q.solution,
        status: 'active',
        isLegacy: false,
        isDisputed: false,
        marks: q.marks || (['OAR', 'OSC', 'OMC', 'OTF'].includes(q.typeCode || q.type) ? 4 : 2),
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
    const ch16 = chs.find(c => parseInt(c.number || c.id, 10) === 16);
    if (ch16) {
      let chTotal = 0;
      (ch16.topics || []).forEach(t => {
        const tc = t.topicCode || t.code;
        const topicQs = qs.filter(q => q.topicCode === tc);
        t.objectiveCount = topicQs.length;
        t.subjectiveCount = 0;
        chTotal += topicQs.length;
      });
      ch16.objectiveCount = chTotal;
      ch16.subjectiveCount = 0;
    }

    // Recalculate total subject counts
    let totalObj = 0;
    chs.forEach(c => {
      totalObj += (c.objectiveCount || 0);
    });
    sylData.objectiveCount = totalObj;
    sylData.updatedAt = admin.firestore.FieldValue.serverTimestamp();

    await sylRef.set(sylData, { merge: true });
    console.log(`Updated mh_9_scit syllabus: Chapter 16 objectiveCount = ${ch16 ? ch16.objectiveCount : 0}, total subject objectiveCount = ${totalObj}`);
  }

  // 4. Update syllabusTopicIndex for Chapter 16 topics
  console.log('--- Step 4: Updating syllabusTopicIndex for Chapter 16 ---');
  const topics16 = [
    { code: 'MH-9-SCIT-16-16.1', name: 'Inheritance, Chromosomes Types (Metacentric, Submetacentric, Acrocentric, Telocentric)', count: 40 },
    { code: 'MH-9-SCIT-16-16.2', name: 'DNA (Deoxyribonucleic Acid) - Watson & Crick Double Helix Model', count: 40 },
    { code: 'MH-9-SCIT-16-16.3', name: 'Mendel Laws of Inheritance: Monohybrid Cross (3:1 Phenotype, 1:2:1 Genotype)', count: 40 },
    { code: 'MH-9-SCIT-16-16.4', name: 'Mendel Dihybrid Cross (9:3:3:1 Ratio) & Law of Independent Assortment', count: 40 },
    { code: 'MH-9-SCIT-16-16.5', name: 'Genetic Disorders: Chromosomal (Down, Turner, Klinefelter) & Monogenic (Sickle Cell Anemia, Hemophilia)', count: 40 }
  ];

  const indexBatch = db.batch();
  topics16.forEach(t => {
    const idxRef = db.collection('syllabusTopicIndex').doc(t.code);
    indexBatch.set(idxRef, {
      topicCode: t.code,
      topicName: t.name,
      chapterNumber: 16,
      chapterName: 'Heredity and Variation',
      class: '9',
      subjectCode: 'SCIT',
      boardCode: 'MH',
      objectiveCount: t.count,
      subjectiveCount: 0,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });
  await indexBatch.commit();
  console.log('Updated 5 topics in syllabusTopicIndex.');

  console.log('\n✅ ALL 200 CHAPTER 16 QUESTIONS COMMITTED AND SYNCED SUCCESSFULLY!');
}

commitCh16().catch(console.error);
