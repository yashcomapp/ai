const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (serviceAccount) {
  const cred = JSON.parse(serviceAccount.startsWith('{') ? serviceAccount : Buffer.from(serviceAccount, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: 'ai-yashcom' });
}

const db = admin.firestore();

async function main() {
  console.log('=== Step 1: Loading Enriched Questions for Subtopic 5.1.3 ===');
  const enrichedFilePath = path.join(__dirname, '..', 'backups', 'reports', 'enriched_subtopic_5_1_3.json');
  const enrichedMap = JSON.parse(fs.readFileSync(enrichedFilePath, 'utf8'));
  const candidateIds = Object.keys(enrichedMap);
  console.log(`Loaded ${candidateIds.length} candidate questions to update.`);

  console.log('=== Step 2: Safety Audit Against Used Questions ===');
  const usedIds = new Set();
  const examsSnap = await db.collection('exams').get();
  examsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.questions || []).forEach(q => {
      if (typeof q === 'string') usedIds.add(q);
      else if (q && q.id) usedIds.add(q.id);
      else if (q && q.questionCode) usedIds.add(q.questionCode);
    });
    (d.questionIds || []).forEach(id => usedIds.add(id));
  });

  const attemptsSnap = await db.collection('attempts').get();
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  const parentReviewsSnap = await db.collection('parentReviews').get();
  parentReviewsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  for (const id of candidateIds) {
    if (usedIds.has(id)) {
      throw new Error(`CRITICAL SAFETY ABORT: Question ${id} is present in used questions!`);
    }
  }
  console.log('✓ All 30 candidate questions verified 100% UNUSED.');

  console.log('=== Step 3: Writing Batch Update to Firestore ===');
  const batch = db.batch();
  for (const [id, data] of Object.entries(enrichedMap)) {
    const ref = db.collection('questions').doc(id);
    const updatePayload = {
      text: data.text,
      options: data.options,
      correctAnswer: data.correctAnswer,
      solution: data.solution,
      difficulty: data.difficulty || 'medium',
      enrichedAt: new Date(),
      updatedAt: new Date()
    };
    if (data.correctAnswers) {
      updatePayload.correctAnswers = data.correctAnswers;
    }
    batch.update(ref, updatePayload);
  }

  await batch.commit();
  console.log('✓ Firestore batch committed successfully!');

  console.log('=== Step 4: Verification Readback ===');
  let successCount = 0;
  for (const id of candidateIds) {
    const snap = await db.collection('questions').doc(id).get();
    if (snap.exists && snap.data().solution) {
      successCount++;
    }
  }
  console.log(`✓ Readback verified: ${successCount}/${candidateIds.length} questions successfully updated with solutions in Firestore.`);
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
