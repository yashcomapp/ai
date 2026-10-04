const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
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
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function createPreMutationSnapshot(collectionNames, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const backupDir = path.resolve(__dirname, '..', 'backups', 'snapshots', `harmonize_mh8_math_${timestamp}`);
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }

  const counts = {};
  for (const cName of collectionNames) {
    const snap = await db.collection(cName).get();
    const docs = snap.docs.map(d => ({ id: d.id, ...d.data() }));
    fs.writeFileSync(path.join(backupDir, `${cName}.json`), JSON.stringify(docs, null, 2), 'utf-8');
    counts[cName] = docs.length;
  }

  console.log(`Pre-mutation snapshot created at ${backupDir}:`, counts);
}

async function harmonizeQuestions() {
  console.log('--- STARTING MH CLASS 8 MATH QUESTION HARMONIZATION ---');

  // 1. Mandatory Pre-Mutation Snapshot (Rule 1Q)
  await createPreMutationSnapshot(['questions', 'syllabusTopicIndex'], 'harmonize_mh8_math_ch13');

  // 2. Fetch all questions matching MH-8-MATH
  const allQSnap = await db.collection('questions').get();
  const targetQuestions = [];

  allQSnap.forEach(d => {
    const dt = d.data();
    const qCode = dt.questionCode || '';
    const tCode = dt.topicCode || '';
    if (qCode.startsWith('MH-8-MATH-') || tCode.startsWith('MH-8-MATH-') || d.id.startsWith('MH-8-MATH-')) {
      targetQuestions.push({ id: d.id, data: dt });
    }
  });

  console.log(`Found ${targetQuestions.length} questions to harmonize from MH-8-MATH to MH-8-MTH.`);

  let migratedCount = 0;
  // Process in batches of 50
  for (let i = 0; i < targetQuestions.length; i += 50) {
    const chunk = targetQuestions.slice(i, i + 50);
    const batch = db.batch();

    chunk.forEach(item => {
      const oldId = item.id;
      const dt = item.data;

      const newId = oldId.startsWith('MH-8-MATH-') ? oldId.replace('MH-8-MATH-', 'MH-8-MTH-') : oldId;
      const newQuestionCode = (dt.questionCode || oldId).replace('MH-8-MATH-', 'MH-8-MTH-');
      const newTopicCode = (dt.topicCode || '').replace('MH-8-MATH-', 'MH-8-MTH-');

      const updatedDocData = {
        ...dt,
        questionCode: newQuestionCode,
        topicCode: newTopicCode,
        subjectCode: 'MTH',
        subject: 'Mathematics',
        board: 'Maharashtra Board',
        boardCode: 'MH',
        class: 8,
        chapter: 13,
        chapterNumber: 13,
        chapterName: 'Congruence of Triangles',
        updatedAt: new Date().toISOString(),
        harmonizedFrom: oldId
      };

      const newRef = db.collection('questions').doc(newId);
      batch.set(newRef, updatedDocData);

      if (newId !== oldId) {
        const oldRef = db.collection('questions').doc(oldId);
        batch.delete(oldRef);
      }

      migratedCount++;
    });

    await batch.commit();
    console.log(`Migrated chunk ${i + 1} to ${Math.min(i + 50, targetQuestions.length)}`);
  }

  console.log(`Total questions harmonized: ${migratedCount}`);

  // 3. Clean up orphaned MH-8-MATH entries in syllabusTopicIndex
  console.log('\n--- CLEANING UP SYLLABUS TOPIC INDEX ---');
  const indexSnap = await db.collection('syllabusTopicIndex').get();
  let indexDeleted = 0;
  const indexBatch = db.batch();

  indexSnap.forEach(d => {
    if (d.id.startsWith('MH-8-MATH-')) {
      indexBatch.delete(d.ref);
      indexDeleted++;
    }
  });

  if (indexDeleted > 0) {
    await indexBatch.commit();
    console.log(`Deleted ${indexDeleted} obsolete MH-8-MATH entries from syllabusTopicIndex.`);
  }

  // 4. Rebuild counts in syllabusTopicIndex for MH-8-MTH
  console.log('\n--- REBUILDING TOPIC INDEX QUESTION COUNTS ---');
  const mthQuestionsSnap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', 8)
    .where('subjectCode', '==', 'MTH')
    .get();

  console.log(`Total MH-8-MTH questions now: ${mthQuestionsSnap.size}`);

  const countsByTopic = {};
  mthQuestionsSnap.forEach(d => {
    const dt = d.data();
    const tc = dt.topicCode;
    if (tc) {
      countsByTopic[tc] = (countsByTopic[tc] || 0) + 1;
      // Also increment parent topic if subtopic
      const parts = tc.split('.');
      if (parts.length > 2) {
        const parentTc = parts.slice(0, 2).join('.');
        countsByTopic[parentTc] = (countsByTopic[parentTc] || 0) + 1;
      }
    }
  });

  console.log('Computed Question Counts by Topic:', JSON.stringify(countsByTopic, null, 2));

  console.log('\n--- HARMONIZATION COMPLETE ---');
}

harmonizeQuestions().catch(console.error);
