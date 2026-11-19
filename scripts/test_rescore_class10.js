const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

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

function evaluateQuestionAnswer(q, userAns) {
  if (userAns === undefined || userAns === null || userAns === '') {
    return { isCorrect: false, marksAwarded: 0, penalty: 0, status: 'unattempted' };
  }
  const qType = (q.type || 'OSC').toUpperCase();
  const marks = Number(q.marks) || 4;
  const negativeMarks = Number(q.negativeMarks) || (qType.startsWith('O') ? 1 : 0);

  if (qType === 'OSC' || qType === 'OTF' || qType === 'OAR') {
    const correctLetter = (q.correctAnswer || '').trim().toUpperCase();
    const studentLetter = String(userAns).trim().toUpperCase();
    const isCorrect = correctLetter === studentLetter;
    if (isCorrect) return { isCorrect: true, marksAwarded: marks, penalty: 0, status: 'correct' };
    return { isCorrect: false, marksAwarded: -negativeMarks, penalty: negativeMarks, status: 'wrong' };
  }
  return { isCorrect: false, marksAwarded: 0, penalty: 0, status: 'wrong' };
}

async function testRescore() {
  const examId = '023-MH-10-Linear Equations-1.4-1.5-181126';
  const examDoc = await db.collection('exams').doc(examId).get();
  const exam = examDoc.data();
  const questionCodes = exam.questionCodes;

  // Fetch all questions and sort strictly according to questionCodes
  const searchCodes = Array.from(new Set(questionCodes));
  const qMap = new Map();
  for (let i = 0; i < searchCodes.length; i += 30) {
    const chunk = searchCodes.slice(i, i + 30);
    const snap = await db.collection('questions').where('questionCode', 'in', chunk).get();
    snap.docs.forEach(doc => {
      const data = doc.data();
      qMap.set(data.questionCode, { id: doc.id, ...data });
    });
  }

  const orderedQuestions = questionCodes.map(c => qMap.get(c)).filter(Boolean);
  console.log(`Fetched ${orderedQuestions.length} ordered questions for Exam 023.`);

  const attSnap = await db.collection('examAttempts').where('examId', '==', examId).get();
  console.log(`Analyzing ${attSnap.size} attempts...`);

  const results = [];
  for (const aDoc of attSnap.docs) {
    const att = aDoc.data();
    const userAnswers = att.userAnswers || {};

    let oldScore = att.score;
    let newScore = 0;
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    orderedQuestions.forEach((q, idx) => {
      const ans = userAnswers[idx];
      const evalRes = evaluateQuestionAnswer(q, ans);
      newScore += evalRes.marksAwarded;
      if (evalRes.status === 'correct') correctCount++;
      else if (evalRes.status === 'wrong') wrongCount++;
      else unattemptedCount++;
    });

    const maxScore = orderedQuestions.length * 4;
    const newPct = Math.round((Math.max(0, newScore) / maxScore) * 1000) / 10;
    const diff = newScore - oldScore;

    results.push({
      studentName: att.studentName,
      oldScore,
      newScore,
      maxScore,
      diff,
      correctCount,
      wrongCount,
      unattemptedCount,
      newPct,
      oldPct: att.percentage
    });
  }

  console.log('\n=== RESCORE RESULTS FOR CLASS 10 EXAM 023 ===');
  results.forEach(r => {
    console.log(`${r.studentName.padEnd(25)} | Old: ${String(r.oldScore).padStart(2)}/60 (${r.oldPct}%) -> New: ${String(r.newScore).padStart(2)}/60 (${r.newPct}%) | Diff: ${r.diff > 0 ? '+' : ''}${r.diff} | C:${r.correctCount} W:${r.wrongCount} U:${r.unattemptedCount}`);
  });
}

testRescore().catch(console.error);
