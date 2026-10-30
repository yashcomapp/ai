const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();
const fs = require('fs');

async function commitRemaining() {
  const files = [
    'scripts/ch1_topic3.json',
    'scripts/ch1_topic4.json',
    'scripts/ch1_topic5.json',
    'scripts/ch1_topic6.json'
  ];

  for (const file of files) {
    const questions = JSON.parse(fs.readFileSync(file, 'utf8'));
    console.log(`Processing ${file} with ${questions.length} questions...`);

    // In chunks of 400
    for (let i = 0; i < questions.length; i += 400) {
      const chunk = questions.slice(i, i + 400);
      const batch = db.batch();
      chunk.forEach(q => {
        const docRef = db.collection('questions').doc(q.questionCode);
        batch.set(docRef, {
          ...q,
          createdAt: new Date(),
          updatedAt: new Date()
        });
      });
      await batch.commit();
      console.log(`  Committed batch of ${chunk.length} questions.`);
    }
  }

  console.log('Successfully committed all remaining topics for Chapter 1!');
}

commitRemaining().catch(console.error);
