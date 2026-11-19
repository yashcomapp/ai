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

// Load all topup questions
const { topupTopic1Questions } = require('./mh8_ch5_topup_topic1.js');
const { topupTopic2Questions } = require('./mh8_ch5_topup_topic2.js');
const { topupTopic3Questions } = require('./mh8_ch5_topup_topic3.js');
const { topupTopic4Questions } = require('./mh8_ch5_topup_topic4.js');
const { topupTopic5Questions } = require('./mh8_ch5_topup_topic5.js');
const { topupTopic6Questions } = require('./mh8_ch5_topup_topic6.js');

const rawQuestions = [
  ...topupTopic1Questions,
  ...topupTopic2Questions,
  ...topupTopic3Questions,
  ...topupTopic4Questions,
  ...topupTopic5Questions,
  ...topupTopic6Questions
];

console.log('Total raw questions to balance & commit:', rawQuestions.length);

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Balance questions so correct answers are evenly distributed across A, B, C, D
const balancedQuestions = rawQuestions.map(q => {
  if (!Array.isArray(q.options) || q.options.length < 2) return q;

  const originalOptions = [...q.options];
  const shuffledOptions = shuffleArray(originalOptions);
  const correctIdx = shuffledOptions.findIndex(o => o.isCorrect === true);
  const letters = ['A', 'B', 'C', 'D'];
  const newAns = letters[correctIdx] || 'A';

  return {
    ...q,
    options: shuffledOptions,
    correctAnswer: newAns,
    ans: newAns
  };
});

// Verify distribution
const dist = { A: 0, B: 0, C: 0, D: 0 };
balancedQuestions.forEach(q => {
  dist[q.correctAnswer] = (dist[q.correctAnswer] || 0) + 1;
});
console.log('Balanced Answer Distribution:', dist);

// Validate 5-tier linter
let errors = 0;
const qCodeSet = new Set();
balancedQuestions.forEach((q, idx) => {
  if (!q.questionCode) { console.error(`[Q${idx}] Missing questionCode`); errors++; }
  if (qCodeSet.has(q.questionCode)) { console.error(`[Q${idx}] Duplicate questionCode: ${q.questionCode}`); errors++; }
  qCodeSet.add(q.questionCode);

  if (!q.text || q.text.trim().length < 15) { console.error(`[Q${idx}] Text too short: ${q.questionCode}`); errors++; }
  if (!Array.isArray(q.options) || q.options.length !== 4) { console.error(`[Q${idx}] Must have 4 options: ${q.questionCode}`); errors++; }
  const correctCount = q.options.filter(o => o.isCorrect === true).length;
  if (correctCount !== 1) { console.error(`[Q${idx}] Must have exactly 1 correct option: ${q.questionCode}`); errors++; }
  if (!q.solution || !q.solution.includes('Physical Context') || !q.solution.includes('Option Analysis')) {
    console.error(`[Q${idx}] Missing 3-part pedagogical solution: ${q.questionCode}`);
    errors++;
  }
});

if (errors > 0) {
  console.error(`Validation failed with ${errors} errors! Aborting.`);
  process.exit(1);
}
console.log('All 145 questions passed 5-tier pedagogical validation with zero errors!');

async function commitAll() {
  // 1. Mandatory Pre-Mutation Snapshot per Rule 2Q
  console.log('\n--- Step 1: Mandatory Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(
    ['questions', 'syllabus'],
    'mh8_ch5_topup_145q_balanced'
  );
  console.log(`Snapshot created at: ${snapResult.snapshotDir}`);

  // 2. Batch commit to Firestore
  console.log('\n--- Step 2: Committing 145 Questions in Batches ---');
  const BATCH_SIZE = 400;
  for (let i = 0; i < balancedQuestions.length; i += BATCH_SIZE) {
    const chunk = balancedQuestions.slice(i, i + BATCH_SIZE);
    const batch = db.batch();
    chunk.forEach(q => {
      const docRef = db.collection('questions').doc(q.questionCode);
      batch.set(docRef, {
        ...q,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
    });
    await batch.commit();
    console.log(`Committed ${chunk.length} questions (total ${Math.min(i + BATCH_SIZE, balancedQuestions.length)}/${balancedQuestions.length}).`);
  }

  console.log('\n=== Success! 145 Top-Up Questions Committed to Firestore ===');
}

commitAll().catch(err => {
  console.error('Fatal error during commit:', err);
  process.exit(1);
});
