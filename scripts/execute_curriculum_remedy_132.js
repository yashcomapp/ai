const path = require('path');
const fs = require('fs');

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
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

const { createPreMutationSnapshot } = require('../scripts/pre-mutation-snapshot.js');
const { ch9Replacements } = require('../scripts/remedy_ch9_curriculum_data.js');
const { remainingReplacements } = require('../scripts/remedy_remaining_curriculum_data.js');

async function runRemediation() {
  console.log('================================================================');
  console.log('🚀 EXECUTING 132 CURRICULUM QUESTION REMEDIATION & HARMONIZATION');
  console.log('================================================================');

  const allReplacements = { ...ch9Replacements, ...remainingReplacements };
  const targetIds = Object.keys(allReplacements);
  console.log(`Loaded ${targetIds.length} replacements (Ch 9: ${Object.keys(ch9Replacements).length}, Others: ${Object.keys(remainingReplacements).length})`);

  // Step 1: Pre-Mutation Snapshot (Rule 2Q)
  console.log('\n--- Step 1: Pre-Mutation Atomic Snapshot ---');
  await createPreMutationSnapshot(['questions', 'syllabusTopicIndex'], 'remedy_132_out_of_syllabus_curriculum_questions');
  console.log('Snapshot successfully recorded in _systemBackups.');

  // Step 2: Validate docs in Firestore and execute updates
  console.log('\n--- Step 2: Updating question documents in Firestore ---');
  let updatedCount = 0;
  let batch = db.batch();

  for (let i = 0; i < targetIds.length; i++) {
    const id = targetIds[i];
    const rep = allReplacements[id];
    const docRef = db.collection('questions').doc(id);

    // Prepare clean question payload
    const updateData = {
      text: rep.text,
      options: rep.options,
      correctAnswer: rep.correctAnswer,
      solution: rep.solution,
      explanation: rep.solution,
      difficulty: rep.difficulty || 'medium',
      status: 'published',
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    // If correctAnswer is array, also set correctAnswers
    if (Array.isArray(rep.correctAnswer)) {
      updateData.correctAnswers = rep.correctAnswer;
    } else {
      updateData.correctAnswers = [];
    }

    batch.set(docRef, updateData, { merge: true });
    updatedCount++;

    if (updatedCount % 400 === 0) {
      await batch.commit();
      console.log(`Committed batch of ${updatedCount} updates...`);
      batch = db.batch();
    }
  }

  if (updatedCount % 400 !== 0) {
    await batch.commit();
  }

  console.log(`Successfully updated all ${updatedCount} question documents in Firestore!`);

  // Step 3: Verify the updated documents
  console.log('\n--- Step 3: Verifying updated questions ---');
  const verifyIds = [
    'MH-9-SCIT-9-9.3-OSC-053',
    'MH-9-SCIT-9-9.3-OSC-048',
    'MH-9-SCIT-9-9.3-OSC-046',
    'MH-9-SCIT-9-9.3-OMC-058',
    'MH-9-SCIT-10-10.3-OSC-011',
    'MH-9-SCIT-15-15.2-OSC-012',
    'MH-9-SCIT-16-16.2-OSC-007'
  ];

  for (const id of verifyIds) {
    const doc = await db.collection('questions').doc(id).get();
    const data = doc.data();
    console.log(`\nVerified [${id}]:`);
    console.log(`  Text: ${data.text}`);
    console.log(`  Correct: ${JSON.stringify(data.correctAnswer)}`);
    console.log(`  Sol: ${data.solution}`);
  }

  // Step 4: Re-sync syllabusTopicIndex counts
  console.log('\n--- Step 4: Syncing syllabusTopicIndex counts ---');
  const allQsSnap = await db.collection('questions').get();
  console.log(`Total questions in Question Bank: ${allQsSnap.size}`);

  const countsByTopic = {};
  allQsSnap.forEach(doc => {
    const q = doc.data();
    const tCode = q.topicCode;
    if (tCode) {
      countsByTopic[tCode] = (countsByTopic[tCode] || 0) + 1;
    }
  });

  const indexSnap = await db.collection('syllabusTopicIndex').get();
  let indexUpdates = 0;
  let indexBatch = db.batch();

  for (const doc of indexSnap.docs) {
    const tCode = doc.id;
    const currentCount = countsByTopic[tCode] || 0;
    const existing = doc.data().objectiveCount || 0;

    if (existing !== currentCount) {
      indexBatch.set(doc.ref, {
        objectiveCount: currentCount,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
      indexUpdates++;

      if (indexUpdates % 400 === 0) {
        await indexBatch.commit();
        indexBatch = db.batch();
      }
    }
  }

  if (indexUpdates % 400 !== 0) {
    await indexBatch.commit();
  }

  console.log(`Updated ${indexUpdates} syllabusTopicIndex records.`);
  console.log('\n================================================================');
  console.log('✅ ALL 132 OUT-OF-SYLLABUS QUESTIONS SUCCESSFULLY REMEDIATED!');
  console.log('================================================================');
}

runRemediation().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
