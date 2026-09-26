import * as fs from 'fs';
import * as path from 'path';

const envPath = path.resolve(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const key = trimmed.slice(0, idx).trim();
      let val = trimmed.slice(idx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      process.env[key] = val;
    }
  });
}

async function inspectAndProcess() {
  const snapshotFile = path.resolve(process.cwd(), 'backups/snapshots/snapshot_2026-09-26T17-47-23-960Z.json');
  if (!fs.existsSync(snapshotFile)) {
    console.error('Snapshot not found');
    return;
  }
  const data = JSON.parse(fs.readFileSync(snapshotFile, 'utf8'));
  const docId = '009-MH-8-Force and Pressure-3.3-3.4-260926_ST-2026-000069';
  
  const attemptDoc = data.examAttempts?.find((d: any) => d._docId === docId);
  const reviewDoc = data.reviews?.find((d: any) => d._docId === docId);

  console.log('Found attempt in snapshot:', !!attemptDoc);
  console.log('Attempt doc keys:', attemptDoc ? Object.keys(attemptDoc) : 'null');
  console.log('Review doc keys:', reviewDoc ? Object.keys(reviewDoc) : 'null');
  if (attemptDoc) {
    console.log('Attempt details:', JSON.stringify({
      score: attemptDoc.score,
      percentage: attemptDoc.percentage,
      totalMarks: attemptDoc.totalMarks,
      durationSpent: attemptDoc.durationSpent,
      answers: attemptDoc.answers,
      userAnswers: attemptDoc.userAnswers,
      status: attemptDoc.status
    }, null, 2));
  }
  if (reviewDoc) {
    console.log('Review details:', JSON.stringify({
      score: reviewDoc.score,
      percentage: reviewDoc.percentage,
      totalMarks: reviewDoc.totalMarks,
      answers: reviewDoc.answers,
      userAnswers: reviewDoc.userAnswers,
      questionEvaluations: reviewDoc.questionEvaluations,
      questionDetails: reviewDoc.questionDetails?.length,
      status: reviewDoc.status
    }, null, 2));
  }

  const { adminDb } = await import('../lib/firebase/admin');

  // Fetch Exam Data
  const examSnap = await adminDb.collection('exams').doc('009-MH-8-Force and Pressure-3.3-3.4-260926').get();
  const examData = examSnap.data() || {};
  console.log('Exam Data keys:', Object.keys(examData));
  if (examData.questionIds) console.log('Exam questionIds count:', examData.questionIds.length);
  if (examData.questions) console.log('Exam questions count:', examData.questions.length);
  console.log('Exam Data fetched:', examData.name);

  // Fetch Student Profile
  const userSnap = await adminDb.collection('users')
    .where('studentCode', '==', 'ST-2026-000069')
    .where('role', '==', 'student')
    .limit(1)
    .get();

  if (userSnap.empty) {
    console.error('Student user not found in firestore!');
    return;
  }
  const studentDoc = userSnap.docs[0];
  const studentData = studentDoc.data();
  console.log('Student Data fetched:', studentData.name, 'userId:', studentDoc.id);

  // Fetch assignments snap
  const assignmentsSnap = await adminDb.collection('classAssignments')
    .where('examId', '==', '009-MH-8-Force and Pressure-3.3-3.4-260926')
    .where('batchId', '==', studentData.batchId || '')
    .get();

  console.log('Assignments count:', assignmentsSnap.size);

  const { AttemptService } = await import('../services/attempt.service');

  const questionDetails = reviewDoc?.questionDetails || [];
  console.log('Total questionDetails found:', questionDetails.length);

  // Reconstruct questions and userAnswers arrays from questionDetails
  const questions = questionDetails.map((qd: any) => ({
    id: qd.id || qd.questionCode,
    questionCode: qd.questionCode,
    text: qd.text,
    type: qd.type || 'OSC',
    options: qd.options || [],
    correctAnswer: qd.correctAnswer,
    correctAnswers: qd.correctAnswers,
    marks: qd.marks || 4,
    bloomLevel: qd.bloomLevel || 'Understand',
    difficulty: qd.difficulty || 'medium',
    topicCode: qd.topicCode
  }));

  const userAnswers = questionDetails.map((qd: any) => ({
    answer: qd.userAnswer !== undefined ? qd.userAnswer : (qd.selectedOption !== undefined ? qd.selectedOption : ''),
    timeSpentSeconds: qd.timeSpentSeconds || 40
  }));

  console.log('Sample user answer:', JSON.stringify(userAnswers[0]), 'Sample question:', questions[0]?.questionCode);

  await adminDb.collection('examAttempts').doc(docId).delete();
  await adminDb.collection('reviews').doc(docId).delete();
  console.log('Cleared existing attempt/review docs to allow full transaction processing...');

  const result = await AttemptService.submitAttempt({
    studentCode: 'ST-2026-000069',
    studentId: studentDoc.id,
    studentName: studentData.name || 'Anushka Pravin Itware',
    examId: '009-MH-8-Force and Pressure-3.3-3.4-260926',
    examData: {
      ...examData,
      positiveMarks: examData.positiveMarks || 4,
      negativeMarks: examData.negativeMarks || 1
    },
    questions,
    userAnswers,
    durationSpent: reviewDoc?.durationSpent || attemptDoc?.durationSpent || 1305,
    tabViolations: 1, // Normalized to 1 strike per new coalescing standard
    proctoringViolations: {
      noFace: reviewDoc?.noFaceViolations || 0,
      multipleFaces: reviewDoc?.multipleFacesViolations || 0,
      lookingAway: reviewDoc?.lookingAwayViolations || 0,
      headMovement: 0
    },
    startedAt: reviewDoc?.startedAt ? (reviewDoc.startedAt._seconds ? new Date(reviewDoc.startedAt._seconds * 1000).toISOString() : new Date(reviewDoc.startedAt).toISOString()) : new Date(1790437366 * 1000).toISOString(),
    assignmentsSnap: assignmentsSnap.empty ? null : assignmentsSnap,
    proctoringViolationTriggered: false,
    micBypassed: false
  });

  console.log('[Success] Anushka Pravin Itware exam attempt processed and submitted successfully!');
  console.log('Result:', JSON.stringify(result, null, 2));
}

inspectAndProcess().catch(err => {
  console.error('Processing error:', err);
  process.exit(1);
});
