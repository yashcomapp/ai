const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

async function rebuildIndex() {
  console.log('--- Starting syllabusTopicIndex Rebuild ---');
  const syllabusSnap = await db.collection('syllabus').get();
  console.log(`Loaded ${syllabusSnap.size} syllabus documents.`);

  const boardCodesSnap = await db.collection('config').doc('boardCodes').get();
  const subjectCodesSnap = await db.collection('config').doc('subjectCodes').get();
  const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data() : {};
  const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data() : {};

  const validCodes = new Set();
  let ops = 0;
  let batch = db.batch();

  async function flush() {
    if (ops > 0) {
      await batch.commit();
      batch = db.batch();
      ops = 0;
    }
  }

  for (const doc of syllabusSnap.docs) {
    const data = doc.data();
    const board = data.board || '';
    const classNum = String(data.class || '');
    const subjectName = data.subject || '';

    if (!board || !classNum || !subjectName) continue;

    const boardCode = data.boardCode || boardCodes[board] || (board.toUpperCase().includes('CBSE') ? 'CBSE' : 'MH');
    const subjectCode = data.subjectCode || subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

    const chapters = Array.isArray(data.chapters) ? data.chapters : [];
    for (const chapter of chapters) {
      const chapterNum = chapter.number || chapter.chapterNumber;
      if (!chapterNum) continue;
      const chapterName = chapter.name || '';

      const topics = Array.isArray(chapter.topics) ? chapter.topics : [];
      for (const topic of topics) {
        const topicNum = topic.number || topic.topicNumber;
        if (!topicNum) continue;
        const topicName = topic.name || '';

        const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${topicNum}`;
        validCodes.add(topicCode);

        const subtopics = Array.isArray(topic.subtopics) ? topic.subtopics : [];
        const hasSubs = subtopics.length > 0;
        const subtopicsSum = hasSubs
          ? subtopics.reduce((acc, s) => acc + (Number(s.targetQuestions) || 65), 0)
          : 0;
        const topicTarget = hasSubs ? subtopicsSum : (Number(topic.targetQuestions) || 65);
        const topicClassification = 'standard';

        const docRef = db.collection('syllabusTopicIndex').doc(topicCode);
        batch.set(docRef, {
          board: boardCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board',
          boardCode,
          class: String(classNum),
          classCode: String(classNum),
          subjectCode,
          subjectName,
          subject: subjectName,
          chapterNumber: String(chapterNum),
          chapterName,
          chapter: chapterName,
          chapterTitle: chapterName,
          topicNumber: String(topicNum),
          topicName,
          title: topicName,
          name: topicName,
          topicCode,
          targetQuestions: topicTarget,
          topicClassification,
          hasSubtopics: hasSubs,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        ops++;
        if (ops >= 400) await flush();

        for (let sIdx = 0; sIdx < subtopics.length; sIdx++) {
          const subtopic = subtopics[sIdx];
          let subNum = '';
          let subName = '';
          let subTarget = 65;
          let subClassification = 'standard';

          if (typeof subtopic === 'string') {
            subNum = `${topicNum}.${sIdx + 1}`;
            subName = subtopic.trim();
          } else if (subtopic && typeof subtopic === 'object') {
            subNum = subtopic.number ? String(subtopic.number) : `${topicNum}.${sIdx + 1}`;
            subName = subtopic.name || subtopic.title || '';
            subTarget = Number(subtopic.targetQuestions) || 65;
            subClassification = 'standard';
          }

          if (!subNum || !subName) continue;

          const subCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${subNum}`;
          validCodes.add(subCode);

          const subRef = db.collection('syllabusTopicIndex').doc(subCode);
          batch.set(subRef, {
            board: boardCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board',
            boardCode,
            class: String(classNum),
            classCode: String(classNum),
            subjectCode,
            subjectName,
            subject: subjectName,
            chapterNumber: String(chapterNum),
            chapterName,
            chapter: chapterName,
            chapterTitle: chapterName,
            topicNumber: String(subNum),
            topicName: subName,
            title: subName,
            name: subName,
            topicCode: subCode,
            parentTopicCode: topicCode,
            parentTopicName: topicName,
            targetQuestions: subTarget,
            topicClassification: subClassification,
            hasSubtopics: false,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          }, { merge: true });

          ops++;
          if (ops >= 400) await flush();
        }
      }
    }
  }

  await flush();
  console.log(`Rebuilt syllabusTopicIndex with ${validCodes.size} valid entries.`);
}

rebuildIndex().catch(err => {
  console.error('Rebuild failed:', err);
  process.exit(1);
});
