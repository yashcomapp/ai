const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

const { evaluateQuestionAnswer, getOptionText } = require('../src/lib/questionTypes.ts');

async function run() {
  const examId = '023-MH-8-Inside the Atom-5.1-181126';

  // Load the 8:36 AM snapshot to get the EXACT questions and options as they existed when students took the test
  const snapPath = path.join(__dirname, '..', 'backups', 'snapshots', 'snapshot_2026-11-19_08-36-09_remedy_exam_023_scoring_and_ch.json');
  console.log('Loading 8:36 AM snapshot for morning questions & options state...');
  const snapshotContent = JSON.parse(fs.readFileSync(snapPath, 'utf-8'));

  const examDocFromSnap = snapshotContent.data?.exams?.find(e => e.id === examId);
  const questionCodes = examDocFromSnap?.data?.questionCodes || [];
  console.log(`Exam 023 has ${questionCodes.length} questionCodes.`);

  const snapQuestions = snapshotContent.data?.questions || [];
  const qMap = new Map();
  snapQuestions.forEach(q => {
    const d = q.data || q;
    const id = q.id || d.id;
    const code = d.questionCode || id;
    qMap.set(id, d);
    qMap.set(code, d);
  });

  // Assemble true ordered exam questions
  const orderedQuestions = questionCodes.map((code, idx) => {
    const q = qMap.get(code);
    return {
      examIndex: idx + 1,
      questionCode: code,
      text: q?.text || '',
      options: q?.options || [],
      correctAnswer: q?.correctAnswer || 'A',
      marks: 4
    };
  });

  // Fetch all attempts for exam 023 currently in Firestore
  const attemptsSnap = await db.collection('examAttempts')
    .where('examId', '==', examId)
    .get();
  
  console.log(`Found ${attemptsSnap.size} attempts in Firestore for exam 023.`);

  // 1. Mandatory Pre-Mutation Snapshot per Rule 2Q
  console.log('\n--- Step 1: Pre-Mutation Snapshot ---');
  const snapResult = await createPreMutationSnapshot(
    ['examAttempts', 'reviews'],
    'rescore_exam_023_correct_order'
  );
  console.log(`Snapshot created at: ${snapResult.snapshotDir}`);

  // 2. Process each student attempt and review
  console.log('\n--- Step 2: Re-evaluating Each Attempt in True Exam Order ---');
  for (const doc of attemptsSnap.docs) {
    const att = doc.data();
    const studentCode = att.studentCode;
    const studentName = att.studentName || studentCode;
    const userAnswers = att.userAnswers || [];

    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;
    const questionDetails = [];
    const wrongAnswers = [];
    const unattemptedQuestions = [];

    orderedQuestions.forEach((q, idx) => {
      const u = userAnswers[idx];
      const letter = u?.answer || '';
      const isAttempted = Boolean(letter && letter.trim() !== '');

      let userSelectedText = '';
      if (isAttempted && Array.isArray(q.options)) {
        const optIdx = letter.toUpperCase().charCodeAt(0) - 65;
        if (optIdx >= 0 && optIdx < q.options.length) {
          const opt = q.options[optIdx];
          userSelectedText = typeof opt === 'object' ? (opt.text || opt.value) : String(opt);
        } else {
          userSelectedText = letter;
        }
      }

      let correctText = '';
      if (Array.isArray(q.options)) {
        const cIdx = String(q.correctAnswer).toUpperCase().charCodeAt(0) - 65;
        if (cIdx >= 0 && cIdx < q.options.length) {
          const opt = q.options[cIdx];
          correctText = typeof opt === 'object' ? (opt.text || opt.value) : String(opt);
        } else {
          correctText = String(q.correctAnswer);
        }
      }

      const isCorrect = isAttempted && (letter.toUpperCase() === String(q.correctAnswer).toUpperCase());

      if (!isAttempted) {
        unattemptedCount++;
        unattemptedQuestions.push({
          questionId: q.questionCode,
          qIdx: idx,
          marks: 4
        });
      } else if (isCorrect) {
        correctCount++;
      } else {
        wrongCount++;
        wrongAnswers.push({
          questionId: q.questionCode,
          qIdx: idx,
          marks: 4,
          userAnswer: letter,
          userAnswerText: userSelectedText,
          correctAnswer: q.correctAnswer,
          correctAnswerText: correctText
        });
      }

      questionDetails.push({
        questionCode: q.questionCode,
        questionText: q.text,
        userAnswer: userSelectedText || (isAttempted ? letter : ''),
        userAnswerLetter: letter,
        correctAnswer: correctText || q.correctAnswer,
        correctAnswerLetter: q.correctAnswer,
        isAttempted: !!isAttempted,
        isCorrect: isCorrect,
        timeSpentSeconds: u?.timeSpentSeconds || 0,
        marks: 4,
        options: q.options
      });
    });

    const earnedMarks = correctCount * 4;
    const penaltyLost = wrongCount * 1;
    // Allow negative score per grading policy (no clamping to 0)
    const newScore = earnedMarks - penaltyLost;
    const newPercentage = parseFloat(((newScore / 120) * 100).toFixed(1));

    console.log(`\n======================================================`);
    console.log(`Student: ${studentName} (${studentCode})`);
    console.log(`  OLD Score: ${att.score}/120 (${att.percentage}%)`);
    console.log(`  NEW Score: ${newScore}/120 (${newPercentage}%) [Correct: ${correctCount}, Wrong: ${wrongCount}, Unattempted: ${unattemptedCount}]`);

    // Update examAttempts document
    await doc.ref.update({
      score: newScore,
      totalMarks: 120,
      percentage: newPercentage,
      wrongAnswers: wrongAnswers,
      unattemptedQuestions: unattemptedQuestions,
      updatedAt: new Date()
    });

    // Update reviews document
    const revRef = db.collection('reviews').doc(doc.id);
    const revSnap = await revRef.get();
    if (revSnap.exists) {
      await revRef.update({
        questionDetails: questionDetails,
        wrongAnswers: wrongAnswers,
        unattemptedQuestions: unattemptedQuestions,
        score: newScore,
        totalMarks: 120,
        percentage: newPercentage,
        updatedAt: new Date()
      });
      console.log(`  ✓ Updated reviews/${doc.id}`);
    } else {
      // Create if missing
      await revRef.set({
        examId: examId,
        studentCode: studentCode,
        studentName: studentName,
        questionDetails: questionDetails,
        wrongAnswers: wrongAnswers,
        unattemptedQuestions: unattemptedQuestions,
        score: newScore,
        totalMarks: 120,
        percentage: newPercentage,
        updatedAt: new Date()
      }, { merge: true });
      console.log(`  ✓ Created reviews/${doc.id}`);
    }
  }

  console.log('\n=== All Exam 023 attempts and reviews successfully rescored with true question alignment! ===');
}

run().catch(console.error);
