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

async function checkExam024() {
  const examId = '024-MH-10-Quadratic-2.1-2.3-191126';
  const examDoc = await db.collection('exams').doc(examId).get();
  const ex = examDoc.data();
  const qCodes = ex.questionCodes;

  console.log('QuestionCodes:', qCodes);

  // In ExamRepository.getQuestionsForExam, it does fallback to where in chunk:
  const questions = [];
  for (let i = 0; i < qCodes.length; i += 10) {
    const chunk = qCodes.slice(i, i + 10);
    const snap = await db.collection('questions').where('questionCode', 'in', chunk).get();
    snap.docs.forEach(d => questions.push({ id: d.id, ...d.data() }));
  }

  console.log(`Fetched ${questions.length} questions by questionCode query.`);
  const qMap = new Map();
  questions.forEach(q => {
    qMap.set(q.questionCode, q);
    qMap.set(q.id, q);
  });

  const dist = { A: 0, B: 0, C: 0, D: 0, other: 0 };
  qCodes.forEach((code, idx) => {
    const q = qMap.get(code);
    if (!q) {
      console.log(`Q${idx+1}: [${code}] NOT FOUND`);
      return;
    }
    const ans = (q.correctAnswer || '').trim().toUpperCase();
    if (dist[ans] !== undefined) dist[ans]++;
    else dist.other++;

    const opts = (q.options || []).map(o => typeof o === 'object' ? o.text : String(o));
    console.log(`Q${idx+1} [${q.questionCode}]: Ans=${ans} | Options=${JSON.stringify(opts)} | Text=${(q.text||'').slice(0, 45)}...`);
  });

  console.log('\nAnswer Distribution for Exam 024:', dist);
}

checkExam024().catch(console.error);
