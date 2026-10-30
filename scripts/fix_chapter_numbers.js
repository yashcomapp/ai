const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function fixChapterNumbers() {
  console.log('Scanning for mismatched chapterNumbers in MH-9-SCIT...');
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  let fixedCount = 0;
  const batchSize = 400;
  let batch = db.batch();
  let countInBatch = 0;

  for (const doc of snap.docs) {
    const data = doc.data();
    if (data.topicCode && data.topicCode.startsWith('MH-9-SCIT-')) {
      const parts = data.topicCode.split('-');
      const correctChapter = parseInt(parts[3], 10);
      if (!isNaN(correctChapter) && data.chapterNumber !== correctChapter) {
        batch.update(doc.ref, { chapterNumber: correctChapter });
        fixedCount++;
        countInBatch++;
        if (countInBatch >= batchSize) {
          await batch.commit();
          batch = db.batch();
          countInBatch = 0;
          console.log(`Committed batch, total fixed so far: ${fixedCount}`);
        }
      }
    }
  }

  if (countInBatch > 0) {
    await batch.commit();
  }

  console.log(`Done! Fixed ${fixedCount} questions with incorrect chapterNumber.`);
}

fixChapterNumbers().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
