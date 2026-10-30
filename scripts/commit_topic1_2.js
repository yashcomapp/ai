const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();
const fs = require('fs');

async function commitTopic1_2() {
  const questions = JSON.parse(fs.readFileSync('scripts/ch1_topic2.json', 'utf8'));
  console.log(`Loaded ${questions.length} questions for Topic 1.2.`);

  // Write in batches of 400 (Firestore limit is 500)
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
  }
  console.log(`Successfully committed all ${questions.length} questions for Topic 1.2!`);
}

commitTopic1_2().catch(console.error);
