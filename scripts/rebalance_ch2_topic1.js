const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();
const { execSync } = require('child_process');

async function rebalanceTopic2_1() {
  const tc = 'MH-9-SCIT-2-2.1';
  console.log(`=== Rebalancing ${tc} ===`);

  const qSnap = await db.collection('questions').where('topicCode', '==', tc).get();
  console.log(`Found ${qSnap.size} existing questions in ${tc}.`);

  // Sort by questionCode
  const docs = qSnap.docs.sort((a,b) => a.id.localeCompare(b.id));

  // Partition:
  // First 40 -> Exam
  // Next 30 -> Practice
  // Remaining -> Surplus to prune (safe because 0 used)
  const examDocs = docs.slice(0, 40);
  const practiceDocs = docs.slice(40, 70);
  const surplusDocs = docs.slice(70);

  console.log(`Assigning ${examDocs.length} to 'exam', ${practiceDocs.length} to 'practice', and pruning ${surplusDocs.length} surplus unused questions.`);

  const batch = db.batch();

  examDocs.forEach(d => {
    batch.update(d.ref, {
      vault: 'exam',
      examCategory: 'standard',
      chapterNumber: 2,
      updatedAt: new Date()
    });
  });

  practiceDocs.forEach(d => {
    batch.update(d.ref, {
      vault: 'practice',
      examCategory: 'standard',
      chapterNumber: 2,
      updatedAt: new Date()
    });
  });

  surplusDocs.forEach(d => {
    batch.delete(d.ref);
  });

  await batch.commit();
  console.log(`Updated exam/practice and pruned surplus.`);

  // Now insert 12 foundation questions
  console.log('Generating 12 foundation questions with SVG diagrams...');
  const pyCode = 'import json; from scripts.ch2_foundation_data import get_foundation_questions; print(json.dumps(get_foundation_questions()))';
  const rawJson = execSync(`python -c "${pyCode}"`, { encoding: 'utf8', maxBuffer: 10 * 1024 * 1024 });
  const fQuestions = JSON.parse(rawJson);

  const fBatch = db.batch();
  fQuestions.forEach((item, idx) => {
    const qCode = `${tc}-OSC-5${String(idx + 1).padStart(2, '0')}`;
    const docRef = db.collection('questions').doc(qCode);
    fBatch.set(docRef, {
      topicCode: tc,
      boardCode: 'MH',
      class: '9',
      subjectCode: 'SCIT',
      board: 'Maharashtra Board',
      subject: 'Science and Technology',
      chapterNumber: 2,
      chapter: 'Work and Energy',
      topic: 'Work: Positive, Negative and Zero Work (W = F * s * cosθ)',
      topicName: 'Work: Positive, Negative and Zero Work (W = F * s * cosθ)',
      type: 'OSC',
      vault: 'mock',
      examCategory: 'foundation',
      requiresFigure: true,
      difficulty: 'hard',
      bloomLevel: 'Analyze',
      marks: 4,
      text: item.text,
      options: item.options,
      correctAnswer: item.correctAnswer,
      solution: item.solution,
      timesUsed: 0,
      usedInClassroomTest: false,
      questionCode: qCode,
      createdAt: new Date(),
      updatedAt: new Date()
    });
  });

  await fBatch.commit();
  console.log(`Successfully committed 12 Foundation questions for ${tc}!`);
}

rebalanceTopic2_1().catch(console.error);
