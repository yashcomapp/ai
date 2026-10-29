// scripts/commit-ch2-enhanced.js
const admin = require('firebase-admin');
const fs = require('fs');

if (!admin.apps.length) {
  const serviceAccount = require('../firebase-service-account.json');
  admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
  });
}

const db = admin.firestore();

async function commitChapter2() {
  console.log('Loading enhanced questions from backups/staging/mh9_scit_2_enhanced.json...');
  const enhancedList = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_2_enhanced.json', 'utf8'));
  console.log(`Found ${enhancedList.length} enhanced questions to commit.`);

  let batch = db.batch();
  let opCount = 0;
  let batchCount = 0;

  for (const q of enhancedList) {
    const docRef = db.collection('questions').doc(q.id);
    batch.update(docRef, {
      text: q.text,
      options: q.options,
      correctAnswer: q.correctAnswer,
      solution: q.solution,
      isEnhanced: true,
      enhancedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    opCount++;

    if (opCount === 450) {
      batchCount++;
      console.log(`Committing batch ${batchCount} (450 operations)...`);
      await batch.commit();
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    batchCount++;
    console.log(`Committing final batch ${batchCount} (${opCount} operations)...`);
    await batch.commit();
  }

  console.log(`Successfully committed all ${enhancedList.length} questions to Firestore!`);

  // Verify sample in Firestore
  console.log('Verifying Q4 in Firestore...');
  const q4Doc = await db.collection('questions').doc('MH-9-SCIT-2-2.1-OSC-004').get();
  const q4Data = q4Doc.data();
  console.log('Q4 Text:', q4Data.text);
  console.log('Q4 Options:', q4Data.options);
  console.log('Q4 isEnhanced:', q4Data.isEnhanced);
}

commitChapter2()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Commit failed:', err);
    process.exit(1);
  });
