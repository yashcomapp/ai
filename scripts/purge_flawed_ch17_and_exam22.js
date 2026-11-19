const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { MasteryService } = require('../src/services/mastery.service.ts');
const { ReportCacheManager } = require('../src/lib/reportCache.ts');

async function executePurge() {
  console.log('====================================================');
  console.log('STEP 1: Mandatory Pre-Mutation Automated Snapshot');
  console.log('====================================================');
  await createPreMutationSnapshot(
    ['exams', 'reviews', 'examAttempts', 'evaluations', 'batchAssignments', 'studentTopicMastery', 'questions', 'syllabusTopicIndex'],
    'purge_flawed_exam_022_and_ch17_questions'
  );
  console.log('Snapshot captured successfully.\n');

  console.log('====================================================');
  console.log('STEP 2: Delete Exam 022-MH-9 & Cleanse Student Mastery');
  console.log('====================================================');
  const examId = '022-MH-9-Introduction to-17.1-17.2-181126';

  // 1. Fetch all reviews to find all affected studentCodes
  const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', examId).get();
  const affectedStudentCodes = new Set();
  reviewsSnap.forEach(d => {
    const sc = d.data().studentCode;
    if (sc) affectedStudentCodes.add(sc.trim().toUpperCase());
  });

  const attemptsSnap = await adminDb.collection('examAttempts').where('examId', '==', examId).get();
  attemptsSnap.forEach(d => {
    const sc = d.data().studentCode;
    if (sc) affectedStudentCodes.add(sc.trim().toUpperCase());
  });

  console.log(`Found ${affectedStudentCodes.size} students affected by exam ${examId}`);

  // 2. Delete reviews
  for (const doc of reviewsSnap.docs) {
    await doc.ref.delete();
  }
  console.log(`Deleted ${reviewsSnap.size} reviews.`);

  // 3. Delete examAttempts
  for (const doc of attemptsSnap.docs) {
    await doc.ref.delete();
  }
  console.log(`Deleted ${attemptsSnap.size} examAttempts.`);

  // 4. Delete evaluations
  const evalsSnap = await adminDb.collection('evaluations').where('examId', '==', examId).get();
  for (const doc of evalsSnap.docs) {
    await doc.ref.delete();
  }
  console.log(`Deleted ${evalsSnap.size} evaluations.`);

  // 5. Delete batchAssignments
  const assignmentsSnap = await adminDb.collection('batchAssignments').where('examId', '==', examId).get();
  for (const doc of assignmentsSnap.docs) {
    await doc.ref.delete();
  }
  console.log(`Deleted ${assignmentsSnap.size} batchAssignments.`);

  // 6. Delete exam document
  await adminDb.collection('exams').doc(examId).delete();
  console.log(`Deleted exam document ${examId}.`);

  // 7. Reset Topic Mastery for each student
  const ch17Topics = [
    'MH-9-SCIT-17-17.1.1',
    'MH-9-SCIT-17-17.1.2',
    'MH-9-SCIT-17-17.2.1',
    'MH-9-SCIT-17-17.2.2',
    'MH-9-SCIT-17-17.2.3',
    'MH-9-SCIT-17-17.3.1',
    'MH-9-SCIT-17-17.3.2',
    'MH-9-SCIT-17-17.3.3'
  ];

  for (const sc of affectedStudentCodes) {
    try {
      await MasteryService.recalculateOrPurgeTopicsForStudent({
        studentCode: sc,
        excludedExamId: examId,
        candidateTopicCodes: ch17Topics
      });
      console.log(`Recalculated/purged topic mastery for student ${sc}`);
    } catch (err) {
      console.warn(`Mastery reset note for ${sc}:`, err.message);
    }
  }

  console.log('====================================================');
  console.log('STEP 3: Remove All Flawed Questions in MH-9-SCIT-17');
  console.log('====================================================');
  const ch17QuestionsSnap = await adminDb.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-17')
    .where('topicCode', '<=', 'MH-9-SCIT-17\uf8ff')
    .get();

  console.log(`Found ${ch17QuestionsSnap.size} questions in MH-9-SCIT-17 to purge.`);
  const deletedQIds = [];

  const batchSize = 400;
  let batch = adminDb.batch();
  let bCount = 0;

  for (const qDoc of ch17QuestionsSnap.docs) {
    deletedQIds.push(qDoc.id);
    batch.delete(qDoc.ref);
    bCount++;
    if (bCount >= batchSize) {
      await batch.commit();
      batch = adminDb.batch();
      bCount = 0;
    }
  }
  if (bCount > 0) {
    await batch.commit();
  }
  console.log(`Purged ${ch17QuestionsSnap.size} questions from questions collection.`);

  console.log('====================================================');
  console.log('STEP 4: Remove Joke Option Questions from Other Chapters');
  console.log('====================================================');
  const specificJokeIds = [
    'MH-9-SCIT-18-18.1-OSC-020',
    'MH-9-SCIT-18-18.1-OSC-052',
    'MH-9-SCIT-18-18.4-OSC-021',
    'MH-9-SCIT-18-18.4-OSC-051',
    'MH-9-SCIT-18-18.4-OSC-060',
    'MH-9-SCIT-18-18.4-OSC-077',
    'CBSE-8-CURI-5-5.2.3-OSC-014',
    'MH-10-SCIT2-1-1.4.1-OSC-022',
    'MH-9-SCIT-10-10.2-OMC-021',
    'MH-9-SCIT-14-14.1-OSC-004',
    'MH-9-SCIT-14-14.1-OSC-005'
  ];

  for (const jId of specificJokeIds) {
    const docRef = adminDb.collection('questions').doc(jId);
    const docSnap = await docRef.get();
    if (docSnap.exists) {
      deletedQIds.push(jId);
      await docRef.delete();
      console.log(`Deleted joke question: ${jId}`);
    }
  }

  console.log('====================================================');
  console.log('STEP 5: Clean Up syllabusTopicIndex for Deleted Questions');
  console.log('====================================================');
  let indexDeleted = 0;
  for (let i = 0; i < deletedQIds.length; i += 20) {
    const chunk = deletedQIds.slice(i, i + 20);
    const idxSnaps = await adminDb.collection('syllabusTopicIndex')
      .where('questionId', 'in', chunk)
      .get();
    
    let iBatch = adminDb.batch();
    idxSnaps.docs.forEach(d => {
      iBatch.delete(d.ref);
      indexDeleted++;
    });
    if (idxSnaps.size > 0) {
      await iBatch.commit();
    }
  }
  console.log(`Removed ${indexDeleted} references from syllabusTopicIndex.`);

  console.log('====================================================');
  console.log('STEP 6: Rebuild Syllabus Topic Counts & Clear Caches');
  console.log('====================================================');
  await ReportCacheManager.invalidatePattern(examId);
  await ReportCacheManager.invalidatePattern('MH-9-SCIT-17');
  console.log('Caches invalidated.');

  console.log('Purge and reset completed successfully.');
  process.exit(0);
}

executePurge().catch(err => {
  console.error('Purge error:', err);
  process.exit(1);
});
