const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot');

// Load environment variables from .env.local
const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

function stripCitations(text) {
  if (!text || typeof text !== 'string') return text;
  return text
    .replace(/\[cite:\s*[^\]]+\]/gi, '')
    .replace(/\[cite\b[^\]]*\]/gi, '')
    .replace(/\s+([?,.!;:])/g, '$1')
    .replace(/[ \t]{2,}/g, ' ')
    .trim();
}

async function cleanAllCitations() {
  console.log('--- Step 1: Mandatory Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['questions'], 'cleanup_citations_from_all_questions');

  console.log('\n--- Step 2: Fetching questions to clean ---');
  const snap = await db.collection('questions').get();
  console.log(`Fetched ${snap.size} total questions.`);

  const toUpdate = [];

  snap.docs.forEach(doc => {
    const d = doc.data();
    let hasCitation = false;
    const updates = {};

    // text
    if (d.text && /\[cite[:\s\d]/i.test(d.text)) {
      const cleaned = stripCitations(d.text);
      if (cleaned !== d.text) {
        hasCitation = true;
        updates.text = cleaned;
      }
    }

    // solution
    if (d.solution && /\[cite[:\s\d]/i.test(d.solution)) {
      const cleaned = stripCitations(d.solution);
      if (cleaned !== d.solution) {
        hasCitation = true;
        updates.solution = cleaned;
      }
    }

    // explanation
    if (d.explanation && /\[cite[:\s\d]/i.test(d.explanation)) {
      const cleaned = stripCitations(d.explanation);
      if (cleaned !== d.explanation) {
        hasCitation = true;
        updates.explanation = cleaned;
      }
    }

    // assertion
    if (d.assertion && /\[cite[:\s\d]/i.test(d.assertion)) {
      const cleaned = stripCitations(d.assertion);
      if (cleaned !== d.assertion) {
        hasCitation = true;
        updates.assertion = cleaned;
      }
    }

    // reason
    if (d.reason && /\[cite[:\s\d]/i.test(d.reason)) {
      const cleaned = stripCitations(d.reason);
      if (cleaned !== d.reason) {
        hasCitation = true;
        updates.reason = cleaned;
      }
    }

    // correctAnswer
    if (d.correctAnswer && /\[cite[:\s\d]/i.test(d.correctAnswer)) {
      const cleaned = stripCitations(d.correctAnswer);
      if (cleaned !== d.correctAnswer) {
        hasCitation = true;
        updates.correctAnswer = cleaned;
      }
    }

    // options
    if (Array.isArray(d.options) && d.options.some(opt => /\[cite[:\s\d]/i.test(String(opt)))) {
      const cleanedOptions = d.options.map(opt => stripCitations(opt));
      if (JSON.stringify(cleanedOptions) !== JSON.stringify(d.options)) {
        hasCitation = true;
        updates.options = cleanedOptions;
      }
    }

    // correctAnswers
    if (Array.isArray(d.correctAnswers) && d.correctAnswers.some(ans => /\[cite[:\s\d]/i.test(String(ans)))) {
      const cleanedAns = d.correctAnswers.map(ans => stripCitations(ans));
      if (JSON.stringify(cleanedAns) !== JSON.stringify(d.correctAnswers)) {
        hasCitation = true;
        updates.correctAnswers = cleanedAns;
      }
    }

    if (hasCitation) {
      toUpdate.push({ ref: doc.ref, id: doc.id, code: d.questionCode, updates });
    }
  });

  console.log(`Found ${toUpdate.length} questions to clean.`);
  if (toUpdate.length === 0) {
    console.log('No questions need citation cleanup.');
    return;
  }

  console.log('\n--- Step 3: Committing updates in atomic batches ---');
  const batchSize = 400;
  for (let i = 0; i < toUpdate.length; i += batchSize) {
    const chunk = toUpdate.slice(i, i + batchSize);
    const batch = db.batch();
    chunk.forEach(item => {
      console.log(`Cleaning ${item.id} (${item.code}):`);
      Object.entries(item.updates).forEach(([k, v]) => {
        console.log(`  - ${k}: ${typeof v === 'string' ? v.slice(0, 80) : JSON.stringify(v)}`);
      });
      batch.update(item.ref, item.updates);
    });
    await batch.commit();
    console.log(`✓ Committed batch of ${chunk.length} updates (${i + chunk.length}/${toUpdate.length})`);
  }

  console.log('\n✅ Successfully cleaned citations from all affected questions in Firestore!');
}

cleanAllCitations().then(() => process.exit(0)).catch(err => {
  console.error('Error during cleanup:', err);
  process.exit(1);
});
