const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function commitFinal6() {
  const db = admin.firestore();

  console.log('--- Step 1: Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(
    ['questions', 'syllabus'],
    'final_topup_6q_gmrt_iucaa'
  );
  console.log('Snapshot recorded.');

  const qs = JSON.parse(fs.readFileSync('backups/staging/final_6_questions.json', 'utf8'));
  console.log(`--- Step 2: Committing ${qs.length} questions to Firestore ---`);

  const batch = db.batch();
  qs.forEach(q => {
    const docRef = db.collection('questions').doc(q.questionCode);
    batch.set(docRef, {
      questionCode: q.questionCode,
      chapterNumber: q.chapterNumber,
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
      marks: q.marks || 4,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });
  await batch.commit();
  console.log('Committed 6 questions to Firestore.');

  console.log('--- Step 3: Updating syllabusTopicIndex ---');
  const indexBatch = db.batch();
  indexBatch.set(db.collection('syllabusTopicIndex').doc('MH-9-SCIT-18-18.3.1'), {
    objectiveCount: 40,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });

  indexBatch.set(db.collection('syllabusTopicIndex').doc('MH-9-SCIT-20-20.1'), {
    objectiveCount: 40,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });
  await indexBatch.commit();

  console.log('--- Step 4: Updating mh_9_scit document ---');
  const sylRef = db.collection('syllabus').doc('mh_9_scit');
  const sylSnap = await sylRef.get();
  if (sylSnap.exists) {
    const data = sylSnap.data();
    data.objectiveCount = (data.objectiveCount || 3887) + 6;
    data.updatedAt = admin.firestore.FieldValue.serverTimestamp();
    await sylRef.set(data, { merge: true });
    console.log(`Updated mh_9_scit total objectiveCount = ${data.objectiveCount}`);
  }

  console.log('\n✅ Successfully committed and synchronized final 6 questions!');
}

commitFinal6().catch(console.error);
