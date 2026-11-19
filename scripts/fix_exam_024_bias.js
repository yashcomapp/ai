const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

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

// Target distribution for 15 questions: 4 A, 4 B, 4 C, 3 D
const TARGET_DIST = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D'];

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

async function run() {
  console.log('=== Step 1: Pre-mutation snapshot for exam 024 ===');
  await createPreMutationSnapshot(['questions', 'exams'], 'fix_exam_024_option_a_bias');

  const examId = '024-MH-10-Quadratic-2.1-2.3-191126';
  const examDoc = await db.collection('exams').doc(examId).get();
  if (!examDoc.exists) {
    throw new Error('Exam 024 not found');
  }

  const qCodes = examDoc.data().questionCodes || [];
  console.log(`Found ${qCodes.length} question codes in exam 024.`);

  // Shuffle target positions so questions don't get clustered
  const desiredAnswers = shuffleArray(TARGET_DIST);

  const batch = db.batch();
  const summary = [];

  for (let i = 0; i < qCodes.length; i++) {
    const code = qCodes[i];
    const snap = await db.collection('questions').where('questionCode', '==', code).get();
    if (snap.empty) {
      console.log(`Warning: ${code} not found in questions collection.`);
      continue;
    }

    const doc = snap.docs[0];
    const qData = doc.data();
    const desiredLetter = desiredAnswers[i];
    const desiredIndex = desiredLetter.charCodeAt(0) - 65; // A->0, B->1, C->2, D->3

    let options = qData.options || [];
    let isObjectFormat = options.length > 0 && typeof options[0] === 'object';

    let correctText = '';
    let otherOptions = [];

    if (isObjectFormat) {
      const correctObj = options.find(o => o.isCorrect) || options[0];
      correctText = correctObj.text;
      otherOptions = options.filter(o => o !== correctObj).map(o => o.text);
    } else {
      // String format
      let origIdx = 0;
      if (qData.correctAnswer && /^[A-D]$/i.test(qData.correctAnswer)) {
        origIdx = qData.correctAnswer.toUpperCase().charCodeAt(0) - 65;
      }
      correctText = options[origIdx] || options[0];
      otherOptions = options.filter((_, idx) => idx !== origIdx);
    }

    // Shuffle distractors
    const shuffledDistractors = shuffleArray(otherOptions);

    // Build new options array where correct option is placed at desiredIndex
    const newOptions = [];
    let distractorIdx = 0;
    for (let pos = 0; pos < 4; pos++) {
      if (pos === desiredIndex) {
        newOptions.push(isObjectFormat ? { text: correctText, isCorrect: true } : correctText);
      } else {
        const distText = shuffledDistractors[distractorIdx++] || `Option ${String.fromCharCode(65 + pos)}`;
        newOptions.push(isObjectFormat ? { text: distText, isCorrect: false } : distText);
      }
    }

    const updatePayload = {
      options: newOptions,
      correctAnswer: desiredLetter,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    batch.update(doc.ref, updatePayload);
    summary.push({ code, oldAns: qData.correctAnswer, newAns: desiredLetter });
  }

  await batch.commit();

  console.log('\n=== Success! Exam 024 Questions Shuffled & Balanced ===');
  summary.forEach((s, idx) => {
    console.log(`Q${idx + 1} (${s.code}): ${s.oldAns} -> ${s.newAns}`);
  });

  const counts = { A: 0, B: 0, C: 0, D: 0 };
  summary.forEach(s => counts[s.newAns]++);
  console.log('\nNew Answer Distribution:', counts);
}

run().catch(console.error);
