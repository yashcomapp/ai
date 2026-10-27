const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot');

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

async function main() {
  console.log('====================================================');
  console.log('   STARTING MASTERY HARMONIZATION & REBUILD        ');
  console.log('====================================================');

  // Step 1: Pre-mutation Snapshot
  console.log('\n--- Step 1: Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['studentTopicMastery', 'syllabusTopicIndex'], 'harmonize_mastery_and_rebuild');

  // Step 2: Harmonize studentTopicMastery
  console.log('\n--- Step 2: Harmonizing studentTopicMastery ---');
  const masterySnap = await db.collection('studentTopicMastery').get();
  console.log(`Loaded ${masterySnap.size} total studentTopicMastery documents.`);

  const candidateDocs = masterySnap.docs.filter(d => {
    const tc = d.data().topicCode || '';
    return tc.startsWith('MH-8-MATH-') || tc === 'MH-9-SCIT-8-1.1';
  });
  console.log(`Found ${candidateDocs.length} orphaned mastery documents to harmonize.`);

  let mergedCount = 0;
  let copiedCount = 0;
  let deletedCount = 0;

  for (const doc of candidateDocs) {
    const oldData = doc.data();
    const oldDocId = doc.id;
    const oldTopic = oldData.topicCode;
    const sCode = oldData.studentCode;

    let newTopic = oldTopic;
    if (oldTopic.startsWith('MH-8-MATH-')) {
      newTopic = oldTopic.replace('MH-8-MATH-', 'MH-8-MTH-');
    } else if (oldTopic === 'MH-9-SCIT-8-1.1') {
      newTopic = 'MH-9-SCIT-8-8.1.1';
    }

    const targetDocId = `${sCode}_${newTopic}`;
    const targetRef = db.collection('studentTopicMastery').doc(targetDocId);
    const targetDoc = await targetRef.get();

    if (targetDoc.exists) {
      // Merge into existing target document
      const targetData = targetDoc.data();
      const oldHistory = Array.isArray(oldData.questionHistory) ? oldData.questionHistory : [];
      const targetHistory = Array.isArray(targetData.questionHistory) ? targetData.questionHistory : [];

      const seenQIds = new Set(targetHistory.map(h => h.questionId));
      const mergedHistory = [...targetHistory];
      for (const h of oldHistory) {
        if (!seenQIds.has(h.questionId)) {
          mergedHistory.push(h);
          seenQIds.add(h.questionId);
        }
      }

      // Reconcile mastery metrics
      const newAttempted = Math.max(targetData.questionsAttempted || 0, oldData.questionsAttempted || 0, mergedHistory.length);
      const newCorrect = Math.max(targetData.questionsCorrect || 0, oldData.questionsCorrect || 0, mergedHistory.filter(h => h.wasCorrect).length);
      const newPracticeAttempted = Math.max(targetData.practiceQuestionsAttempted || 0, oldData.practiceQuestionsAttempted || 0);
      const newExamAttempted = Math.max(targetData.examQuestionsAttempted || 0, oldData.examQuestionsAttempted || 0);
      
      // Keep highest mastery
      const newMastery = Math.max(targetData.mastery || 0, oldData.mastery || 0);
      const newConfidence = Math.max(targetData.confidence || 0, oldData.confidence || 0);

      await targetRef.set({
        topicCode: newTopic,
        studentCode: sCode,
        mastery: newMastery,
        confidence: newConfidence,
        questionsAttempted: newAttempted,
        questionsCorrect: newCorrect,
        practiceQuestionsAttempted: newPracticeAttempted,
        examQuestionsAttempted: newExamAttempted,
        questionHistory: mergedHistory,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });

      // Delete old doc
      await doc.ref.delete();
      mergedCount++;
      deletedCount++;
    } else {
      // Create canonical document and delete old
      await targetRef.set({
        ...oldData,
        topicCode: newTopic,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      await doc.ref.delete();
      copiedCount++;
      deletedCount++;
    }
  }

  console.log(`Harmonization complete:`);
  console.log(`  ✓ Merged into existing canonical docs: ${mergedCount}`);
  console.log(`  ✓ Migrated to new canonical docs: ${copiedCount}`);
  console.log(`  ✓ Deleted obsolete/orphaned docs: ${deletedCount}`);

  // Step 3: Rebuild syllabusTopicIndex
  console.log('\n--- Step 3: Rebuilding syllabusTopicIndex ---');
  const syllabusSnap = await db.collection('syllabus').get();
  console.log(`Loaded ${syllabusSnap.size} syllabus documents.`);

  const boardCodesSnap = await db.collection('config').doc('boardCodes').get();
  const subjectCodesSnap = await db.collection('config').doc('subjectCodes').get();
  const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data() : {};
  const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data() : {};

  const validCodes = new Set();
  const syllabusSubjectsTree = {};
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

    if (!syllabusSubjectsTree[board]) syllabusSubjectsTree[board] = {};
    if (!syllabusSubjectsTree[board][classNum]) syllabusSubjectsTree[board][classNum] = {};
    syllabusSubjectsTree[board][classNum][subjectName] = { docId: doc.id };

    const boardCode = data.boardCode || boardCodes[board] || board.substring(0, 4).toUpperCase();
    const subjectCode = data.subjectCode || subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

    const chapters = Array.isArray(data.chapters) ? data.chapters : [];
    for (const chapter of chapters) {
      const chapterNum = chapter.number;
      if (!chapterNum) continue;
      const chapterName = chapter.name || '';

      const topics = Array.isArray(chapter.topics) ? chapter.topics : [];
      for (const topic of topics) {
        const topicNum = topic.number;
        if (!topicNum) continue;
        const topicName = topic.name || '';

        const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${topicNum}`;
        validCodes.add(topicCode);

        const subtopics = Array.isArray(topic.subtopics) ? topic.subtopics : [];
        const hasSubs = subtopics.length > 0;
        const subtopicsSum = hasSubs
          ? subtopics.reduce((acc, s) => acc + (Number(s.targetQuestions) || 30), 0)
          : 0;
        const topicTarget = hasSubs ? subtopicsSum : (Number(topic.targetQuestions) || 50);
        const topicClassification = topic.topicClassification || (topicTarget <= 35 ? 'minor' : (topicTarget >= 55 ? 'major' : 'medium'));

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

        // Subtopics indexing
        for (let sIdx = 0; sIdx < subtopics.length; sIdx++) {
          const subtopic = subtopics[sIdx];
          let subNum = '';
          let subName = '';
          let subTarget = 30;
          let subClassification = 'minor';

          if (typeof subtopic === 'string') {
            subNum = `${topicNum}.${sIdx + 1}`;
            subName = subtopic.trim();
          } else if (subtopic && typeof subtopic === 'object') {
            subNum = subtopic.number ? String(subtopic.number) : `${topicNum}.${sIdx + 1}`;
            subName = subtopic.name || subtopic.title || '';
            subTarget = Number(subtopic.targetQuestions) || 30;
            subClassification = subtopic.topicClassification || (subTarget <= 35 ? 'minor' : (subTarget >= 55 ? 'major' : 'medium'));
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
            parentTopicCode: topicCode,
            topicCode: subCode,
            targetQuestions: subTarget,
            topicClassification: subClassification,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          }, { merge: true });

          ops++;
          if (ops >= 400) await flush();
        }
      }
    }
  }

  await flush();
  console.log(`Indexed ${validCodes.size} total valid topics & subtopics in syllabusTopicIndex.`);

  // Purge any truly stale index records
  const existingIdx = await db.collection('syllabusTopicIndex').get();
  let staleRemoved = 0;
  for (const doc of existingIdx.docs) {
    if (!validCodes.has(doc.id)) {
      batch.delete(doc.ref);
      ops++;
      staleRemoved++;
      if (ops >= 400) await flush();
    }
  }
  await flush();
  console.log(`Purged ${staleRemoved} stale index records.`);

  // Step 4: Verification of Adhira
  console.log('\n--- Step 4: Verifying Adhira (ST-2026-000065) ---');
  const adhiraMastery = await db.collection('studentTopicMastery')
    .where('studentCode', '==', 'ST-2026-000065')
    .get();
  
  const adhira1323 = adhiraMastery.docs.filter(d => (d.data().topicCode || '').includes('13.2.3'));
  adhira1323.forEach(d => {
    console.log(`Adhira Ch13.2.3 doc: ${d.id} -> topicCode: ${d.data().topicCode}, mastery: ${d.data().mastery}%, confidence: ${d.data().confidence}`);
  });

  console.log('\n====================================================');
  console.log('   MIGRATION & HARMONIZATION COMPLETED SUCCESSFULLY');
  console.log('====================================================');
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal Migration Error:', err);
  process.exit(1);
});
