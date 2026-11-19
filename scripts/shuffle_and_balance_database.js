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

function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

async function run() {
  console.log('=== Step 1: Pre-Mutation Snapshot ===');
  await createPreMutationSnapshot(['questions'], 'shuffle_and_balance_all_objective_options');

  console.log('=== Step 2: Fetching All Questions ===');
  const snap = await db.collection('questions').get();
  console.log(`Fetched ${snap.size} total questions.`);

  let updatedCount = 0;
  let skippedCount = 0;
  const newDistribution = { A: 0, B: 0, C: 0, D: 0 };

  // Collect operations in batches of 400
  let batch = db.batch();
  let opCount = 0;

  for (let i = 0; i < snap.docs.length; i++) {
    const doc = snap.docs[i];
    const q = doc.data();
    const type = String(q.type || '').toUpperCase();

    // Skip subjective and Assertion-Reason (OAR has standardized choices)
    if (type === 'OAR' || type === 'ASSERTION_REASON' || type.startsWith('S') || type.includes('SUBJECTIVE') || type.includes('NUMERICAL_SHORT') || type.includes('NUMERICAL_LONG')) {
      skippedCount++;
      continue;
    }

    const options = q.options;
    if (!Array.isArray(options) || options.length < 2) {
      skippedCount++;
      continue;
    }

    const isObjectFormat = typeof options[0] === 'object' && options[0] !== null;

    let correctText = '';
    let otherOptions = [];

    const ansStr = String(q.correctAnswer || '').trim().toUpperCase();

    if (isObjectFormat) {
      const correctObj = options.find(o => o && o.isCorrect === true);
      if (correctObj && correctObj.text) {
        correctText = correctObj.text;
        otherOptions = options.filter(o => o !== correctObj).map(o => o ? o.text : '');
      } else {
        // Fallback to letter
        let idx = 0;
        if (/^[A-D]$/.test(ansStr)) {
          idx = ansStr.charCodeAt(0) - 65;
        } else if (/^[1-4]$/.test(ansStr)) {
          idx = parseInt(ansStr, 10) - 1;
        }
        if (idx < 0 || idx >= options.length) idx = 0;
        correctText = options[idx]?.text || '';
        otherOptions = options.filter((_, oi) => oi !== idx).map(o => o ? o.text : '');
      }
    } else {
      // String format
      let idx = 0;
      if (/^[A-D]$/.test(ansStr)) {
        idx = ansStr.charCodeAt(0) - 65;
      } else if (/^[1-4]$/.test(ansStr)) {
        idx = parseInt(ansStr, 10) - 1;
      }
      if (idx < 0 || idx >= options.length) idx = 0;
      correctText = String(options[idx] || '');
      otherOptions = options.filter((_, oi) => oi !== idx).map(o => String(o || ''));
    }

    if (!correctText) {
      skippedCount++;
      continue;
    }

    // Pick a target index evenly [0, options.length - 1]
    const targetIdx = Math.floor(Math.random() * options.length);
    const targetLetter = String.fromCharCode(65 + targetIdx);

    const shuffledDistractors = shuffleArray(otherOptions);
    const newOptions = [];
    let distIdx = 0;

    for (let pos = 0; pos < options.length; pos++) {
      if (pos === targetIdx) {
        newOptions.push(isObjectFormat ? { text: correctText, isCorrect: true } : correctText);
      } else {
        const dText = shuffledDistractors[distIdx++] || `Option ${String.fromCharCode(65 + pos)}`;
        newOptions.push(isObjectFormat ? { text: dText, isCorrect: false } : dText);
      }
    }

    batch.update(doc.ref, {
      options: newOptions,
      correctAnswer: targetLetter,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    opCount++;
    updatedCount++;
    if (newDistribution[targetLetter] !== undefined) {
      newDistribution[targetLetter]++;
    }

    if (opCount >= 400) {
      await batch.commit();
      console.log(`Committed batch of 400 updates (Total updated so far: ${updatedCount})...`);
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    await batch.commit();
    console.log(`Committed final batch of ${opCount} updates.`);
  }

  console.log('\n=== Database Shuffling & Balancing Complete! ===');
  console.log(`Total questions processed: ${snap.size}`);
  console.log(`Updated: ${updatedCount}`);
  console.log(`Skipped (Subjective / OAR): ${skippedCount}`);
  console.log('New Answer Distribution for Updated Questions:');
  console.log(newDistribution);
}

run().catch(console.error);
