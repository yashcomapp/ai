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

async function checkAllClass10Attempts() {
  const examId = '023-MH-10-Linear Equations-1.4-1.5-181126';
  const attSnap = await db.collection('examAttempts').where('examId', '==', examId).get();
  
  console.log(`=== CLASS 10 EXAM 023 ATTEMPTS (${attSnap.size} students) ===`);
  for (const doc of attSnap.docs) {
    const att = doc.data();
    const revSnap = await db.collection('reviews').doc(doc.id).get();
    const rev = revSnap.data();
    
    // Check userAnswers
    const rawAnswers = att.userAnswers || [];
    const answersSummary = rawAnswers.map(a => typeof a === 'object' ? a.answer : a).join(',');
    
    // Check if questions were in exam.questionCodes order
    const examDoc = await db.collection('exams').doc(examId).get();
    const examQCodes = examDoc.data().questionCodes;
    const reviewQCodes = (rev && rev.questionDetails) ? rev.questionDetails.map(q => q.questionCode) : [];
    
    let orderMatched = true;
    for (let i = 0; i < examQCodes.length; i++) {
      if (examQCodes[i] !== reviewQCodes[i]) {
        orderMatched = false;
        break;
      }
    }
    
    console.log(`Student: ${att.studentName.padEnd(25)} | Score: ${String(att.score).padStart(2)}/60 | Correct: ${rev ? rev.correctCount : '?'} | Wrong: ${rev ? rev.wrongCount : '?'} | Answers: [${answersSummary}] | OrderMatched: ${orderMatched}`);
  }
}

checkAllClass10Attempts().catch(console.error);
