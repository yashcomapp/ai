const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function runRemedy() {
  console.log('--- Step 1: Pre-mutation Snapshot ---');
  await createPreMutationSnapshot(
    ['exams', 'reviews', 'examAttempts', 'questions'],
    'remedy_exam_023_scoring_and_ch5_marks'
  );
  console.log('Snapshot successfully captured.');

  const examId = '023-MH-8-Inside the Atom-5.1-181126';
  
  console.log('--- Step 2: Update Exam Document totalMarks to 120 ---');
  const examRef = adminDb.collection('exams').doc(examId);
  await examRef.update({
    totalMarks: 120,
    positiveMarks: 4,
    negativeMarks: 1,
    updatedAt: new Date()
  });
  console.log(`Updated ${examId} totalMarks = 120.`);

  console.log('--- Step 3: Rescore Reviews & ExamAttempts ---');
  const reviewsSnap = await adminDb.collection('reviews').where('examId', '==', examId).get();
  console.log(`Found ${reviewsSnap.size} reviews to rescore.`);

  for (const doc of reviewsSnap.docs) {
    const r = doc.data();
    const details = r.questionDetails || [];
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    const updatedDetails = details.map((qd) => {
      const isAttempted = qd.isAttempted !== undefined
        ? Boolean(qd.isAttempted)
        : Boolean(qd.isCorrect || (qd.userAnswer !== undefined && qd.userAnswer !== null && qd.userAnswer !== ''));
      const isCorrect = isAttempted && Boolean(qd.isCorrect);

      if (!isAttempted) unattemptedCount++;
      else if (isCorrect) correctCount++;
      else wrongCount++;

      return {
        ...qd,
        isAttempted,
        isCorrect,
        marks: 4 // Standard canonical 4 marks for OSC
      };
    });

    const earnedMarks = correctCount * 4;
    const penaltyLost = wrongCount * 1;
    const newScore = Math.max(0, earnedMarks - penaltyLost);
    const newPercentage = parseFloat(((newScore / 120) * 100).toFixed(1));

    console.log(`Student ${r.studentName}: ${correctCount} correct (+${earnedMarks}), ${wrongCount} wrong (-${penaltyLost}) -> Score: ${newScore}/120 (${newPercentage}%)`);

    // Update review
    await doc.ref.update({
      questionDetails: updatedDetails,
      score: newScore,
      totalMarks: 120,
      percentage: newPercentage,
      updatedAt: new Date()
    });

    // Update matching examAttempt
    const attemptRef = adminDb.collection('examAttempts').doc(doc.id);
    const attemptSnap = await attemptRef.get();
    if (attemptSnap.exists) {
      await attemptRef.update({
        score: newScore,
        totalMarks: 120,
        percentage: newPercentage,
        updatedAt: new Date()
      });
    }
  }

  console.log('--- Step 4: Update Question Bank MH-8-SCI-5 OSC marks to 4 ---');
  const qSnap = await adminDb.collection('questions')
    .where('topicCode', '>=', 'MH-8-SCI-5')
    .where('topicCode', '<=', 'MH-8-SCI-5\uf8ff')
    .get();
  
  let qUpdated = 0;
  const batchSize = 400;
  let batch = adminDb.batch();
  let count = 0;

  for (const qDoc of qSnap.docs) {
    const q = qDoc.data();
    if (q.type === 'OSC' || q.typeCode === 'OSC') {
      batch.update(qDoc.ref, { marks: 4, updatedAt: new Date() });
      qUpdated++;
      count++;
      if (count >= batchSize) {
        await batch.commit();
        batch = adminDb.batch();
        count = 0;
      }
    }
  }
  if (count > 0) {
    await batch.commit();
  }
  console.log(`Updated ${qUpdated} questions in MH-8-SCI-5 to marks: 4.`);

  console.log('--- Step 5: Invalidate Report Caches ---');
  const { ReportCacheManager } = require('../src/lib/reportCache.ts');
  await ReportCacheManager.invalidatePattern(examId);
  await ReportCacheManager.invalidatePattern('022-MH-9-Introduction to-17.1-17.2-181126');
  console.log('Report caches invalidated.');

  console.log('--- Remediation Complete ---');
  process.exit(0);
}

runRemedy().catch(err => {
  console.error('Remediation error:', err);
  process.exit(1);
});
