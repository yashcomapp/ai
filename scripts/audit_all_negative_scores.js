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

async function auditAllExamScores() {
  console.log('Auditing all reviews for clamped negative scores or student codes in names...');
  const snap = await db.collection('reviews').get();
  console.log(`Total reviews in DB: ${snap.size}`);

  const clampedNegative = [];
  const codeInName = [];

  snap.docs.forEach(d => {
    const r = d.data();
    const name = String(r.studentName || '');
    if (/^ST-\d+/i.test(name.trim())) {
      codeInName.push({ id: d.id, examId: r.examId, code: r.studentCode, name });
    }

    const qDetails = r.questionDetails || [];
    if (qDetails.length > 0 && r.score === 0) {
      let c = 0;
      let w = 0;
      qDetails.forEach(q => {
        const isAtt = q.isAttempted !== undefined ? Boolean(q.isAttempted) : Boolean(q.isCorrect || (q.userAnswer && q.userAnswer !== ''));
        if (isAtt) {
          if (q.isCorrect) c++;
          else w++;
        }
      });
      const calc = c * 4 - w * 1;
      if (calc < 0) {
        clampedNegative.push({ id: d.id, examId: r.examId, student: r.studentName, c, w, calc, stored: r.score });
      }
    }
  });

  console.log(`Reviews with studentCode as studentName: ${codeInName.length}`);
  codeInName.forEach(c => console.log(`- [${c.id}] (Exam: ${c.examId}): "${c.name}"`));

  console.log(`\nReviews with negative scores clamped to 0: ${clampedNegative.length}`);
  clampedNegative.forEach(c => console.log(`- [${c.id}] (Exam: ${c.examId}) Student: ${c.student} | Calc: ${c.calc} vs Stored: ${c.stored} (c:${c.c}, w:${c.w})`));
}

auditAllExamScores().catch(console.error);
