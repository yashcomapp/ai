const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();
const fs = require('fs');

async function commitTopic(jsonPath, topicCode) {
  const questions = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  console.log(`Loaded ${questions.length} questions from ${jsonPath} for ${topicCode}.`);

  // 1. Check existing questions for this topicCode
  const existingSnap = await db.collection('questions')
    .where('topicCode', '==', topicCode)
    .get();

  console.log(`Found ${existingSnap.size} existing questions for ${topicCode}.`);

  // Protect used questions
  const usedCodes = new Set();
  existingSnap.docs.forEach(doc => {
    const data = doc.data();
    if (data.usageCount > 0 || 
        (data.usedInExams && data.usedInExams.length > 0) || 
        (data.usedInPractices && data.usedInPractices.length > 0) ||
        data.usageStatus === 'used' ||
        data.used === true) {
      usedCodes.add(doc.id);
    }
  });
  console.log(`Protected used questions: ${usedCodes.size}`);

  // Delete unused existing questions for this topic that are being replaced
  const newCodes = new Set(questions.map(q => q.questionCode));
  const toDelete = [];
  existingSnap.docs.forEach(doc => {
    if (!usedCodes.has(doc.id) && !newCodes.has(doc.id)) {
      toDelete.push(doc.ref);
    }
  });

  if (toDelete.length > 0) {
    console.log(`Pruning ${toDelete.length} legacy unused questions...`);
    for (let i = 0; i < toDelete.length; i += 400) {
      const batch = db.batch();
      toDelete.slice(i, i + 400).forEach(ref => batch.delete(ref));
      await batch.commit();
    }
  }

  // Write new questions
  for (let i = 0; i < questions.length; i += 400) {
    const chunk = questions.slice(i, i + 400);
    const batch = db.batch();
    chunk.forEach(q => {
      const parts = topicCode.split('-');
      const boardCode = parts[0];
      const classNum = parts[1];
      const subjectCode = parts[2];
      const chNum = parseInt(parts[3]);

      let boardName = 'CBSE';
      let subjectName = 'Mathematics';
      if (boardCode === 'MH') {
        boardName = 'Maharashtra Board';
        if (subjectCode === 'SCIT') subjectName = 'Science and Technology';
        else if (subjectCode === 'MTH1') subjectName = 'Mathematics Part - 1 (Algebra)';
        else if (subjectCode === 'MTH2') subjectName = 'Mathematics Part - 2 (Geometry)';
      } else if (boardCode === 'CBSE') {
        boardName = 'CBSE';
        if (subjectCode === 'MGP1') subjectName = 'Ganit Prakash Part 1';
        else if (subjectCode === 'CURI') subjectName = 'Curiosity Science';
        else if (subjectCode === 'MGM') subjectName = 'Mathematics (Ganita Manjari)';
      }

      const docRef = db.collection('questions').doc(q.questionCode);
      const solutionText = q.solution || q.explanation || '';
      batch.set(docRef, {
        ...q,
        solution: solutionText,
        explanation: solutionText,
        chapterNumber: chNum,
        class: classNum,
        subjectCode: subjectCode,
        boardCode: boardCode,
        board: boardName,
        subject: subjectName,
        status: 'active',
        isLegacy: false,
        createdAt: new Date(),
        updatedAt: new Date()
      }, { merge: true });
    });
    await batch.commit();
  }

  // Verify counts
  const finalSnap = await db.collection('questions').where('topicCode', '==', topicCode).get();
  const pools = { exam: 0, practice: 0, mock: 0, other: 0 };
  finalSnap.docs.forEach(d => {
    const v = d.data().vault || (d.data().examCategory === 'foundation' ? 'mock' : 'other');
    pools[v] = (pools[v] || 0) + 1;
  });
  console.log(`Final count for ${topicCode}: Total ${finalSnap.size}`, pools);
}

const file = process.argv[2] || 'scripts/ch2_topic2.json';
const topic = process.argv[3] || 'MH-9-SCIT-2-2.2';
commitTopic(file, topic).catch(console.error);
