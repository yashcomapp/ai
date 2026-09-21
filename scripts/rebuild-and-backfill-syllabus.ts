import * as path from 'path';
import * as fs from 'fs';

const envPath = path.join(process.cwd(), '.env.local');
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

function parseTopicCode(topicCode: string) {
  if (!topicCode) return null;
  const parts = topicCode.split('-');
  if (parts.length < 5) return null;
  return {
    boardCode: parts[0],
    classNum: parts[1],
    subjectCode: parts[2],
    chapterNumber: parts[3],
    topicNumber: parts[4]
  };
}

async function main() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const admin = await import('firebase-admin');
  const { createPreMutationSnapshot } = await import('../src/lib/backupUtils');

  console.log('--- Step 1: Creating Pre-Mutation Snapshot ---');
  const snapshot = await createPreMutationSnapshot(
    ['syllabus', 'syllabusTopicIndex', 'parentReviews', 'practiceSubmissions', 'reviews'],
    'Rebuild syllabus subtopic index and backfill reviews/submissions metadata'
  );
  console.log(`Snapshot created successfully: ${snapshot.snapshotId}`);

  console.log('\n--- Step 2: Rebuilding syllabusTopicIndex ---');
  const syllabusSnap = await adminDb.collection('syllabus').get();
  const boardCodesSnap = await adminDb.collection('config').doc('boardCodes').get();
  const subjectCodesSnap = await adminDb.collection('config').doc('subjectCodes').get();
  
  const boardCodes = boardCodesSnap.exists ? boardCodesSnap.data()! : {};
  const subjectCodes = subjectCodesSnap.exists ? subjectCodesSnap.data()! : {};

  const validCodes = new Set<string>();
  const syllabusSubjectsTree: any = {};

  let batch = adminDb.batch();
  let opsInBatch = 0;
  const MAX_BATCH_OPS = 400;

  async function flushBatch() {
    if (opsInBatch > 0) {
      await batch.commit();
      batch = adminDb.batch();
      opsInBatch = 0;
    }
  }

  let totalTopicsIndexed = 0;

  for (const doc of syllabusSnap.docs) {
    const data = doc.data();
    const board = data.board || '';
    const classNum = String(data.class || '');
    const subjectName = data.subject || '';

    if (!board || !classNum || !subjectName) continue;

    if (!syllabusSubjectsTree[board]) syllabusSubjectsTree[board] = {};
    if (!syllabusSubjectsTree[board][classNum]) syllabusSubjectsTree[board][classNum] = {};
    syllabusSubjectsTree[board][classNum][subjectName] = { docId: doc.id };

    const boardCode = boardCodes[board] || board.substring(0, 4).toUpperCase();
    const subjectCode = subjectCodes[subjectName] || subjectName.substring(0, 4).toUpperCase();

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
          ? subtopics.reduce((acc: number, s: any) => acc + (Number(s.targetQuestions) || 30), 0)
          : 0;
        const topicTarget = hasSubs ? subtopicsSum : (Number(topic.targetQuestions) || 50);
        const topicClassification = topic.topicClassification || (topicTarget <= 35 ? 'minor' : (topicTarget >= 55 ? 'major' : 'medium'));

        const docRef = adminDb.collection('syllabusTopicIndex').doc(topicCode);
        batch.set(docRef, {
          boardCode,
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

        opsInBatch++;
        totalTopicsIndexed++;
        if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();

        // Subtopics indexing (handling both string arrays and object arrays)
        for (let sIdx = 0; sIdx < subtopics.length; sIdx++) {
          const subtopic = subtopics[sIdx];
          let subNum = '';
          let subName = '';
          let subTarget = 30;
          let subClassification = 'minor';

          if (typeof subtopic === 'string') {
            subNum = `${topicNum}.${sIdx + 1}`;
            subName = subtopic.trim();
            subTarget = 30;
            subClassification = 'minor';
          } else if (subtopic && typeof subtopic === 'object') {
            subNum = subtopic.number ? String(subtopic.number) : `${topicNum}.${sIdx + 1}`;
            subName = subtopic.name || subtopic.title || '';
            subTarget = Number(subtopic.targetQuestions) || 30;
            subClassification = subtopic.topicClassification || (subTarget <= 35 ? 'minor' : (subTarget >= 55 ? 'major' : 'medium'));
          }

          if (!subNum || !subName) continue;

          const subCode = `${boardCode}-${classNum}-${subjectCode}-${chapterNum}-${subNum}`;
          validCodes.add(subCode);

          const subRef = adminDb.collection('syllabusTopicIndex').doc(subCode);
          batch.set(subRef, {
            boardCode,
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

          opsInBatch++;
          totalTopicsIndexed++;
          if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
        }
      }
    }
  }

  await flushBatch();
  console.log(`Rebuild completed: Indexed ${totalTopicsIndexed} topics & subtopics.`);

  // Update syllabusSubjects config
  await adminDb.collection('config').doc('syllabusSubjects').set({
    subjects: syllabusSubjectsTree,
    version: 1,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });

  console.log('\n--- Step 3: Verifying syllabusTopicIndex entries ---');
  const testSubtopic = await adminDb.collection('syllabusTopicIndex').doc('MH-10-SCIT2-7-7.1.2').get();
  console.log('MH-10-SCIT2-7-7.1.2 exists?', testSubtopic.exists, testSubtopic.data());

  console.log('\n--- Step 4: Loading complete syllabusTopicIndex in memory for backfill ---');
  const allIndexDocs = await adminDb.collection('syllabusTopicIndex').get();
  const indexMap = new Map<string, any>();
  allIndexDocs.docs.forEach(d => indexMap.set(d.id, d.data()));
  console.log(`Loaded ${indexMap.size} index entries in memory.`);

  function resolveTopicMeta(topicCode: string) {
    if (!topicCode) return null;
    let sData = indexMap.get(topicCode);
    if (!sData) {
      const parsed = parseTopicCode(topicCode);
      if (parsed && parsed.topicNumber.includes('.')) {
        const parts = parsed.topicNumber.split('.');
        if (parts.length > 2) {
          const parentNum = parts.slice(0, 2).join('.');
          const parentCode = `${parsed.boardCode}-${parsed.classNum}-${parsed.subjectCode}-${parsed.chapterNumber}-${parentNum}`;
          sData = indexMap.get(parentCode);
        }
      }
    }
    return sData;
  }

  console.log('\n--- Step 5: Backfilling parentReviews ---');
  const parentReviewsSnap = await adminDb.collection('parentReviews').get();
  let parentReviewsUpdated = 0;

  for (const doc of parentReviewsSnap.docs) {
    const data = doc.data();
    const topicCode = data.topicCode || '';
    const sData = resolveTopicMeta(topicCode);

    if (sData) {
      const resolvedSubject = sData.subjectName || sData.subject || data.subjectName;
      const resolvedChapter = sData.chapterName || sData.chapter || data.chapterName;
      const resolvedTopic = sData.topicName || sData.title || sData.name || data.topicName;

      const needsUpdate = 
        !data.subjectName || data.subjectName === 'General' ||
        !data.chapterName || data.chapterName === 'General' || data.chapterName === 'General Chapter' ||
        !data.topicName || data.topicName === topicCode || data.topicName === 'Practice Set';

      if (needsUpdate || data.subjectName !== resolvedSubject || data.chapterName !== resolvedChapter || data.topicName !== resolvedTopic) {
        batch.update(doc.ref, {
          subjectName: resolvedSubject,
          chapterName: resolvedChapter,
          topicName: resolvedTopic,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        opsInBatch++;
        parentReviewsUpdated++;
        if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
      }
    }
  }
  await flushBatch();
  console.log(`Updated ${parentReviewsUpdated} parentReviews documents.`);

  console.log('\n--- Step 6: Backfilling practiceSubmissions ---');
  const practiceSubmissionsSnap = await adminDb.collection('practiceSubmissions').get();
  let practiceSubmissionsUpdated = 0;

  for (const doc of practiceSubmissionsSnap.docs) {
    const data = doc.data();
    const topicCode = data.topicCode || '';
    const sData = resolveTopicMeta(topicCode);

    if (sData) {
      const resolvedSubject = sData.subjectName || sData.subject || data.subjectName;
      const resolvedChapter = sData.chapterName || sData.chapter || data.chapterName;
      const resolvedTopic = sData.topicName || sData.title || sData.name || data.topicName;

      const needsUpdate = 
        !data.subjectName || data.subjectName === 'General' ||
        !data.chapterName || data.chapterName === 'General' || data.chapterName === 'General Chapter' ||
        !data.topicName || data.topicName === topicCode || data.topicName === 'Practice Set';

      if (needsUpdate || data.subjectName !== resolvedSubject || data.chapterName !== resolvedChapter || data.topicName !== resolvedTopic) {
        batch.update(doc.ref, {
          subjectName: resolvedSubject,
          chapterName: resolvedChapter,
          topicName: resolvedTopic,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        opsInBatch++;
        practiceSubmissionsUpdated++;
        if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
      }
    }
  }
  await flushBatch();
  console.log(`Updated ${practiceSubmissionsUpdated} practiceSubmissions documents.`);

  console.log('\n--- Step 7: Backfilling reviews (practice sessions) ---');
  const reviewsSnap = await adminDb.collection('reviews').where('examType', '==', 'practice').get();
  let reviewsUpdated = 0;

  for (const doc of reviewsSnap.docs) {
    const data = doc.data();
    const topicCode = data.topicCode || data.examCode || data.examName || '';
    const sData = resolveTopicMeta(topicCode);

    if (sData) {
      const resolvedSubject = sData.subjectName || sData.subject || data.subject;
      const resolvedChapter = sData.chapterName || sData.chapter || data.chapter;
      const resolvedTopic = sData.topicName || sData.title || sData.name || data.topicName;

      const needsUpdate = 
        !data.subject || data.subject === 'General' ||
        !data.chapter || data.chapter === 'General' ||
        !data.examName || data.examName === topicCode;

      if (needsUpdate) {
        batch.update(doc.ref, {
          subject: resolvedSubject,
          chapter: resolvedChapter,
          examName: resolvedTopic,
          topicName: resolvedTopic,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        opsInBatch++;
        reviewsUpdated++;
        if (opsInBatch >= MAX_BATCH_OPS) await flushBatch();
      }
    }
  }
  await flushBatch();
  console.log(`Updated ${reviewsUpdated} reviews documents.`);

  console.log('\nAll steps completed successfully!');
}

main().catch(err => {
  console.error('Migration failed:', err);
  process.exit(1);
});
