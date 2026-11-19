const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function checkExam023Class10() {
  const examDoc = await db.collection('exams').doc('023-MH-10-Linear Equations-1.4-1.5-181126').get();
  const exam = examDoc.data();
  const questionCodes = exam.questionCodes;
  console.log('Exam Question Codes (ordered as in exam):');
  questionCodes.forEach((qc, i) => console.log(`  [${i}] ${qc}`));

  // Check how Firestore returns them with where('questionCode', 'in', ...)
  // Chunk into 10 (since 15 questions)
  const chunk1 = questionCodes.slice(0, 10);
  const snap1 = await db.collection('questions').where('questionCode', 'in', chunk1).get();
  const returnedCodes1 = snap1.docs.map(d => d.data().questionCode);
  console.log('\nChunk 1 (first 10) input:');
  console.log(chunk1);
  console.log('Chunk 1 returned by Firestore in query:');
  console.log(returnedCodes1);

  let chunk1OrderMatches = true;
  for (let i = 0; i < chunk1.length; i++) {
    if (chunk1[i] !== returnedCodes1[i]) {
      chunk1OrderMatches = false;
      break;
    }
  }
  console.log('Did Chunk 1 return in exact same order?', chunk1OrderMatches);

  // Check all 15 questions
  const chunk2 = questionCodes.slice(10);
  const snap2 = await db.collection('questions').where('questionCode', 'in', chunk2).get();
  const returnedCodes2 = snap2.docs.map(d => d.data().questionCode);
  const allReturned = [...returnedCodes1, ...returnedCodes2];

  console.log('\nFull comparison: input vs returned');
  let fullMatch = true;
  for (let i = 0; i < questionCodes.length; i++) {
    const isSame = questionCodes[i] === allReturned[i];
    console.log(`Q${i + 1}: expected=${questionCodes[i]} | returned=${allReturned[i]} | Match: ${isSame}`);
    if (!isSame) fullMatch = false;
  }
  console.log('\nOVERALL ORDER MATCH:', fullMatch);

  // Now let's check one or more attempts for Class 10
  const attSnap = await db.collection('examAttempts').where('examId', '==', '023-MH-10-Linear Equations-1.4-1.5-181126').get();
  console.log(`\nChecking ${attSnap.size} attempts...`);
  for (const aDoc of attSnap.docs) {
    const att = aDoc.data();
    const revSnap = await db.collection('reviews').doc(aDoc.id).get();
    const rev = revSnap.data();
    console.log(`Student: ${att.studentName} - Score recorded: ${att.score}/60`);
    if (rev && rev.questionDetails) {
      console.log(`  Review question count: ${rev.questionDetails.length}`);
      // Check questionCode in review questionDetails
      const reviewCodes = rev.questionDetails.map(qd => qd.questionCode || qd.id);
      console.log(`  First 3 reviewCodes: ${reviewCodes.slice(0, 3)}`);
      console.log(`  First 3 examCodes:   ${questionCodes.slice(0, 3)}`);
      let reviewOrderMatchesExam = true;
      for (let i = 0; i < questionCodes.length; i++) {
        if (questionCodes[i] !== reviewCodes[i]) {
          reviewOrderMatchesExam = false;
          break;
        }
      }
      console.log(`  Did review match exam questionCodes order? ${reviewOrderMatchesExam}`);
    }
  }
}

checkExam023Class10().catch(console.error);
