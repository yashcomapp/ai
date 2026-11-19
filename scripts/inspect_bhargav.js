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

async function inspectBhargav() {
  const examId = '023-MH-10-Linear Equations-1.4-1.5-181126';
  const attSnap = await db.collection('examAttempts')
    .where('examId', '==', examId)
    .where('studentName', '==', 'Bhargav Virokar')
    .get();

  const att = attSnap.docs[0].data();
  console.log('Bhargav attempt data:', {
    score: att.score,
    maxScore: att.maxScore,
    userAnswers: att.userAnswers
  });

  const revSnap = await db.collection('reviews').doc(attSnap.docs[0].id).get();
  const rev = revSnap.data();
  console.log('Bhargav review questionDetails:');
  if (rev && rev.questionDetails) {
    rev.questionDetails.forEach((qd, idx) => {
      console.log(`Q${idx+1}: code=${qd.questionCode} ans=${qd.userAnswer} correct=${qd.correctAnswer} isCorrect=${qd.isCorrect} text=${(qd.text||'').slice(0, 30)}`);
    });
  }

  // Let's also check the questions in the exam
  const examDoc = await db.collection('exams').doc(examId).get();
  const exam = examDoc.data();
  console.log('\nExam data questions field exists?', !!exam.questions, 'Array?', Array.isArray(exam.questions));
  if (exam.questions && Array.isArray(exam.questions)) {
    console.log('exam.questions length:', exam.questions.length);
    console.log('exam.questions[0]:', typeof exam.questions[0] === 'object' ? exam.questions[0].questionCode : exam.questions[0]);
  }
}

inspectBhargav().catch(console.error);
