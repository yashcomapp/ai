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
  const boilerplateData = JSON.parse(fs.readFileSync('boilerplate_questions.json', 'utf-8'));
  const ids = boilerplateData.questions.map(q => q.id);

  const fullQuestions = [];
  for (let i = 0; i < ids.length; i += 30) {
    const chunk = ids.slice(i, i + 30);
    const refs = chunk.map(id => db.collection('questions').doc(id));
    const snaps = await db.getAll(...refs);
    snaps.forEach(s => {
      if (s.exists) {
        const d = s.data();
        fullQuestions.push({
          id: s.id,
          questionCode: d.questionCode,
          topicCode: d.topicCode,
          text: d.text,
          options: d.options,
          correctAnswer: d.correctAnswer,
          solution: d.solution
        });
      }
    });
  }

  console.log(`Fetched ${fullQuestions.length} full question documents.`);
  fs.writeFileSync('ch5_140_questions.json', JSON.stringify(fullQuestions, null, 2));
}

run().catch(console.error);
