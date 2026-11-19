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

async function run() {
  const revSnap = await db.collection('reviews').doc('023-MH-10-Linear Equations-1.4-1.5-181126_ST-2026-000016').get();
  const r = revSnap.data();
  console.log('Review summary:', {
    score: r.score,
    totalMarks: r.totalMarks,
    percentage: r.percentage,
    correctCount: r.correctCount,
    wrongCount: r.wrongCount,
    unattemptedCount: r.unattemptedCount,
    qDetailsCount: r.questionDetails ? r.questionDetails.length : 0
  });
  if (r.questionDetails) {
    r.questionDetails.forEach((qd, i) => {
      console.log(`Q${i+1}: userAns="${qd.userAnswer}" isCorrect=${qd.isCorrect} marksAwarded=${qd.marksAwarded} text="${(qd.text||'').slice(0,25)}"`);
    });
  }
}
run().catch(console.error);
