const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

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

async function harmonizeCh13Questions() {
  console.log('--- 1. Create Pre-Mutation Snapshot ---');
  const snapshotTimestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });

  const qSnap = await db.collection('questions').get();
  const backupFile = path.join(backupDir, `snapshot_before_ch13_harmonize_${snapshotTimestamp}.json`);
  const backupData = qSnap.docs
    .filter(d => d.id.includes('MH-8-MATH') || d.id.includes('MH-8-MTH-13-'))
    .map(d => ({ id: d.id, ...d.data() }));
  fs.writeFileSync(backupFile, JSON.stringify(backupData, null, 2));
  console.log(`Saved snapshot of ${backupData.length} questions to ${backupFile}`);

  console.log('\n--- 2. Migrate 60 MH-8-MATH questions to MH-8-MTH ---');
  const mathQuestions = qSnap.docs.filter(d => d.id.startsWith('MH-8-MATH-13-') || (d.data().topicCode && d.data().topicCode.startsWith('MH-8-MATH-13-')));
  console.log(`Found ${mathQuestions.length} questions to migrate.`);

  let batch = db.batch();
  let opCount = 0;

  for (const doc of mathQuestions) {
    const data = doc.data();
    const oldId = doc.id;
    const newId = oldId.replace('MH-8-MATH-', 'MH-8-MTH-');
    const newTopicCode = (data.topicCode || '').replace('MH-8-MATH-', 'MH-8-MTH-');
    const newQuestionCode = (data.questionCode || oldId).replace('MH-8-MATH-', 'MH-8-MTH-');

    const updatedData = {
      ...data,
      id: newId,
      questionCode: newQuestionCode,
      topicCode: newTopicCode,
      subjectCode: 'MTH',
      subject: 'Mathematics',
      board: 'Maharashtra Board',
      boardCode: 'MH',
      class: '8',
      chapterNumber: '13',
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    // Delete old doc if ID changed
    if (oldId !== newId) {
      batch.delete(doc.ref);
    }
    // Set new doc
    const newRef = db.collection('questions').doc(newId);
    batch.set(newRef, updatedData);
    opCount += 2;

    if (opCount >= 400) {
      await batch.commit();
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    await batch.commit();
  }
  console.log(`Successfully migrated ${mathQuestions.length} questions to canonical MH-8-MTH codes.`);

  console.log('\n--- 3. Update Syllabus counts for mh_8_mth Chapter 13 ---');
  const sylRef = db.collection('syllabus').doc('mh_8_mth');
  const sylDoc = await sylRef.get();
  if (sylDoc.exists) {
    const sylData = sylDoc.data();
    const chapters = sylData.chapters || [];
    const ch13 = chapters.find(c => String(c.number) === '13');
    if (ch13) {
      // Count all questions for Ch 13 topics in questions collection
      const ch13QuestionsSnap = await db.collection('questions')
        .where('board', '==', 'Maharashtra Board')
        .where('class', '==', '8')
        .where('chapterNumber', '==', '13')
        .get();

      console.log(`Total questions for MH-8 Ch 13 after migration: ${ch13QuestionsSnap.size}`);

      const topicCounts = {};
      ch13QuestionsSnap.forEach(d => {
        const q = d.data();
        const tc = q.topicCode || '';
        topicCounts[tc] = (topicCounts[tc] || 0) + 1;
      });
      console.log('Topic counts in DB:', topicCounts);

      // Walk topics in ch13 and update objectiveCount
      let chTotalObj = 0;
      const walk = (tList) => {
        tList.forEach(t => {
          const tCode = t.topicCode || t.subtopicCode || '';
          if (tCode && topicCounts[tCode]) {
            t.objectiveCount = topicCounts[tCode];
            t.subjectiveCount = 0;
          }
          chTotalObj += (t.objectiveCount || 0);
          if (t.subtopics && t.subtopics.length > 0) walk(t.subtopics);
        });
      };
      if (ch13.topics) walk(ch13.topics);
      ch13.objectiveCount = chTotalObj;

      await sylRef.update({ chapters });
      console.log(`Updated mh_8_mth Chapter 13 with objectiveCount: ${chTotalObj}`);
    }
  }

  console.log('\n--- 4. Update syllabusTopicIndex for 13.3.1 and 13.3.2 ---');
  const index1331 = db.collection('syllabusTopicIndex').doc('MH-8-MTH-13-13.3.1');
  const index1332 = db.collection('syllabusTopicIndex').doc('MH-8-MTH-13-13.3.2');

  await index1331.set({
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '8',
    subject: 'Mathematics',
    subjectCode: 'MTH',
    chapterNumber: '13',
    chapterName: 'Congruence of Triangles',
    topicNumber: '13.3.1',
    topicName: 'Proving triangles congruent by specific test',
    topicCode: 'MH-8-MTH-13-13.3.1',
    objectiveCount: 30,
    subjectiveCount: 0,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });

  await index1332.set({
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '8',
    subject: 'Mathematics',
    subjectCode: 'MTH',
    chapterNumber: '13',
    chapterName: 'Congruence of Triangles',
    topicNumber: '13.3.2',
    topicName: 'Stating remaining congruent angles and sides',
    topicCode: 'MH-8-MTH-13-13.3.2',
    objectiveCount: 30,
    subjectiveCount: 0,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });

  console.log('✅ Updated syllabusTopicIndex for MH-8-MTH-13-13.3.1 and MH-8-MTH-13-13.3.2.');
}

harmonizeCh13Questions().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
