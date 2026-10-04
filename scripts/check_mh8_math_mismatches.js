const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function checkAllMismatches() {
  const snap = await db.collection('questions').get();
  console.log('Total questions:', snap.size);
  const mhMathQuestions = [];
  
  snap.docs.forEach(doc => {
    const q = doc.data();
    if (doc.id.includes('MH-8-MATH') || (q.topicCode && q.topicCode.includes('MH-8-MATH')) || (q.subjectCode === 'MATH' && (q.boardCode === 'MH' || String(q.board).includes('Maharashtra')) && String(q.class) === '8')) {
      mhMathQuestions.push({ id: doc.id, topicCode: q.topicCode, questionCode: q.questionCode });
    }
  });

  console.log('Found MH-8 questions with MATH instead of MTH:', mhMathQuestions.length);
  if (mhMathQuestions.length > 0) {
    console.log(JSON.stringify(mhMathQuestions.slice(0, 10), null, 2));
  }
}

checkAllMismatches().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
