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
  const snap = await db.collection('questions').get();
  console.log(`Auditing explanations across ${snap.size} questions...`);

  let boilerplateCount = 0;
  const topicCounts = {};
  const boilerplateQuestions = [];

  snap.docs.forEach(doc => {
    const d = doc.data();
    const id = doc.id;
    const sol = d.explanation || d.solution || '';
    if (sol.includes('### 1. Scientific Principle') || sol.includes('### 2. Physical Context') || sol.includes('### 3. Step-by-Step Option') || sol.includes('### 1.')) {
      boilerplateCount++;
      const tCode = d.topicCode || d.chapter || 'unknown';
      topicCounts[tCode] = (topicCounts[tCode] || 0) + 1;
      boilerplateQuestions.push({ id, topicCode: tCode, questionCode: d.questionCode, text: d.text });
    }
  });

  console.log(`Found ${boilerplateCount} questions with oversized 3-section boilerplate explanations.`);
  console.log('Breakdown by topic:', topicCounts);

  fs.writeFileSync('boilerplate_questions.json', JSON.stringify({ count: boilerplateCount, topicCounts, questions: boilerplateQuestions }, null, 2));
}

run().catch(console.error);
