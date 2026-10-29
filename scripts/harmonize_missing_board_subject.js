const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function harmonize() {
  const db = admin.firestore();

  // 1. Snapshot
  console.log('--- Step 1: Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['questions'], 'harmonize_board_subject_fields_690q');
  console.log('Snapshot recorded.');

  // 2. Load topic names
  const topicSnap = await db.collection('syllabusTopicIndex')
    .where('boardCode', '==', 'MH')
    .where('subjectCode', '==', 'SCIT')
    .get();

  const topicMap = {};
  topicSnap.forEach(d => {
    topicMap[d.id] = d.data().topicName;
  });

  // 3. Scan all MH SCIT questions
  console.log('--- Step 2: Scanning questions ---');
  const qsSnap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('subjectCode', '==', 'SCIT')
    .get();

  console.log(`Scanned ${qsSnap.size} total questions.`);

  const toUpdate = [];
  qsSnap.forEach(doc => {
    const data = doc.data();
    const needsBoard = data.board !== 'Maharashtra Board';
    const needsSubject = data.subject !== 'Science and Technology';
    const needsTopic = !data.topic && topicMap[data.topicCode];
    const needsTopicName = !data.topicName && topicMap[data.topicCode];
    const needsChapterStr = typeof data.chapterNumber === 'number';

    if (needsBoard || needsSubject || needsTopic || needsTopicName || needsChapterStr) {
      toUpdate.push({
        ref: doc.ref,
        id: doc.id,
        update: {
          board: 'Maharashtra Board',
          boardCode: 'MH',
          subject: 'Science and Technology',
          subjectCode: 'SCIT',
          topic: topicMap[data.topicCode] || data.topic || '',
          topicName: topicMap[data.topicCode] || data.topicName || '',
          chapterNumber: String(data.chapterNumber),
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        }
      });
    }
  });

  console.log(`Found ${toUpdate.length} questions needing field harmonization.`);

  // 4. Batch commit
  const BATCH_SIZE = 400;
  for (let i = 0; i < toUpdate.length; i += BATCH_SIZE) {
    const chunk = toUpdate.slice(i, i + BATCH_SIZE);
    const batch = db.batch();
    chunk.forEach(item => {
      batch.set(item.ref, item.update, { merge: true });
    });
    await batch.commit();
    console.log(`Committed harmonization batch ${Math.floor(i / BATCH_SIZE) + 1} (${chunk.length} docs).`);
  }

  console.log('\n✅ All questions successfully harmonized with board: "Maharashtra Board" and subject: "Science and Technology"!');
}

harmonize().catch(console.error);
