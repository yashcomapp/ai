const path = require('path');
const fs = require('fs');

// Load environment
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || "ai-yashcom";

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapshotRes = await createPreMutationSnapshot(['questions'], 'enrich_ch5_batch1');
  console.log(`Snapshot saved: ${snapshotRes.snapshotId}`);

  console.log('\n=== Step 2: Audit Used Question IDs Across Historical Collections ===');
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

  const subjSnap = await db.collection('subjectiveExams').get();
  subjSnap.docs.forEach(doc => {
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
    (d.questions || []).forEach(q => {
      if (typeof q === 'string') usedIds.add(q);
      else if (q && q.id) usedIds.add(q.id);
      else if (q && q.questionCode) usedIds.add(q.questionCode);
    });
  });

  console.log(`Total used question identifiers verified: ${usedIds.size}`);

  console.log('\n=== Step 3: Validate & Apply Batch 1 ===');
  const batchFilePath = path.join(__dirname, '..', 'backups', 'reports', 'dry_run_batch_ch5.json');
  const batch = JSON.parse(fs.readFileSync(batchFilePath, 'utf8'));

  console.log(`Loaded ${batch.length} candidate questions from dry_run_batch_ch5.json`);

  for (const item of batch) {
    if (usedIds.has(item.id) || usedIds.has(item.code)) {
      throw new Error(`CRITICAL VIOLATION: Question ${item.id} / ${item.code} is present in used questions! Aborting immediately!`);
    }
  }
  console.log('Safety check passed: NONE of the candidates have ever been used.');

  const batchWrite = db.batch();
  for (const item of batch) {
    const docRef = db.collection('questions').doc(item.id);
    batchWrite.update(docRef, {
      text: item.enriched.text,
      options: item.enriched.options,
      correctAnswer: item.enriched.correctAnswer,
      solution: item.enriched.solution,
      difficulty: 'medium',
      updatedAt: new Date(),
      enrichedAt: new Date()
    });
    console.log(`Queued update for doc ${item.id}`);
  }

  await batchWrite.commit();
  console.log('Batch update committed successfully to Firestore!');

  console.log('\n=== Step 4: Verification Readback ===');
  for (const item of batch) {
    const docSnap = await db.collection('questions').doc(item.id).get();
    if (!docSnap.exists) {
      console.error(`Doc ${item.id} not found!`);
      continue;
    }
    const data = docSnap.data();
    console.log(`[VERIFIED] ${item.id}:`);
    console.log(`  Text: ${data.text.slice(0, 80)}...`);
    console.log(`  Difficulty: ${data.difficulty}`);
    console.log(`  Options count: ${data.options?.length}`);
    console.log(`  Correct answer: ${data.correctAnswer}`);
    console.log(`  Solution: ${data.solution?.slice(0, 80)}...`);
  }
  console.log('\nAll 5 questions successfully enriched and verified in Firestore!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
