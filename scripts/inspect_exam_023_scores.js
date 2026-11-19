const admin = require('firebase-admin');
const fs = require('fs');
const envVars = {};
fs.readFileSync('.env.local', 'utf-8').split('\n').forEach(l => {
  const t = l.trim();
  if (t && !t.startsWith('#')) {
    const idx = t.indexOf('=');
    if (idx > 0) envVars[t.slice(0, idx).trim()] = t.slice(idx + 1).trim().replace(/^['"]|['"]$/g, '');
  }
});
admin.initializeApp({ credential: admin.credential.cert(JSON.parse(envVars.FIREBASE_SERVICE_ACCOUNT_KEY)) });
const db = admin.firestore();

async function inspectExam023() {
  const rSnap = await db.collection('reviews').where('examId', '==', '023-MH-8-Inside the Atom-5.1-181126').get();
  console.log(`Found ${rSnap.size} reviews for exam 023:`);
  
  const reviews = [];
  rSnap.forEach(d => {
    const data = d.data();
    reviews.push({
      id: d.id,
      studentCode: data.studentCode,
      studentName: data.studentName,
      score: data.score,
      totalMarks: data.totalMarks,
      percentage: data.percentage,
      obtainedMarks: data.obtainedMarks,
      correctCount: data.correctCount,
      wrongCount: data.wrongCount,
      unattemptedCount: data.unattemptedCount,
      questionDetails: (data.questionDetails || []).map(q => ({
        code: q.questionCode,
        isCorrect: q.isCorrect,
        isAttempted: q.isAttempted,
        userAnswer: q.userAnswer
      }))
    });
  });

  reviews.sort((a, b) => (b.score || 0) - (a.score || 0));
  reviews.forEach((r, idx) => {
    const c = r.questionDetails.filter(q => q.isCorrect).length;
    const att = r.questionDetails.filter(q => q.isAttempted || (q.userAnswer && q.userAnswer !== '')).length;
    const w = att - c;
    const un = r.questionDetails.length - att;
    const rawScore = c * 4 - w * 1;
    console.log(`[Rank ${idx + 1}] Code: ${r.studentCode} | Name: ${r.studentName} | Stored Score: ${r.score} | Calc (c*4 - w*1): ${rawScore} | c:${c} w:${w} un:${un} (Total Qs: ${r.questionDetails.length})`);
  });
}

inspectExam023().catch(console.error);
