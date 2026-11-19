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

async function inspect() {
  const snap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-8-SCI-5')
    .where('topicCode', '<=', 'MH-8-SCI-5\uf8ff')
    .get();

  console.log(`Total questions in MH-8-SCI-5: ${snap.size}`);
  const byTopic = {};
  const questions = [];
  snap.docs.forEach(d => {
    const q = d.data();
    byTopic[q.topicCode] = (byTopic[q.topicCode] || 0) + 1;
    questions.push({
      id: d.id,
      code: q.questionCode || d.id,
      topicCode: q.topicCode,
      difficulty: q.difficulty,
      text: q.text,
      options: q.options,
      correctAnswer: q.correctAnswer,
      explanation: q.explanation || q.solution || ''
    });
  });

  console.log('By topic:', JSON.stringify(byTopic, null, 2));

  // Check out of syllabus keywords
  const outOfSyllabusKeywords = [
    'planck', '6.626', 'bohr radius', '0.529', 'wavelength', 'photon', 'joule',
    '\\hbar', 'angular momentum mvr', 'cross-section', 'sin^4', 'quantum',
    'spectroscopy', 'balmer', 'lyman', 'rydberg', 'orbital subshell',
    'photoelectric', 'volume ratio', '10^{-15}'
  ];

  const flaggedOOS = [];
  questions.forEach(q => {
    const full = (q.text + ' ' + JSON.stringify(q.options) + ' ' + q.explanation).toLowerCase();
    for (const kw of outOfSyllabusKeywords) {
      if (full.includes(kw.toLowerCase())) {
        flaggedOOS.push({ id: q.id, code: q.code, topic: q.topicCode, kw, text: q.text });
        break;
      }
    }
  });

  console.log(`\nFlagged potentially Out-Of-Syllabus questions in Ch 5: ${flaggedOOS.length}`);
  flaggedOOS.slice(0, 10).forEach(f => {
    console.log(`- [${f.code}] (${f.topic}) [kw: ${f.kw}]: ${f.text}`);
  });

  fs.writeFileSync('ch5_all_questions.json', JSON.stringify({
    total: questions.length,
    byTopic,
    flaggedOOS,
    questions
  }, null, 2));
}

inspect().catch(console.error);
