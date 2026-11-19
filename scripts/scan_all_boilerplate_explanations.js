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

async function scan() {
  console.log('Fetching all questions from Firestore...');
  const snap = await db.collection('questions').get();
  console.log(`Total questions fetched: ${snap.size}`);

  const boilerplateList = [];
  const patterns = [
    /###\s*1\./i,
    /###\s*2\./i,
    /###\s*3\./i,
    /Scientific Principle/i,
    /Physical Context/i,
    /Core Calculation/i,
    /Option Analysis/i,
    /Option [A-D] is correct/i,
    /Option [A-D] is incorrect/i,
    /Misconception Analysis/i,
    /Step-by-Step Option/i
  ];

  const bySubject = {};
  const byTopic = {};

  snap.docs.forEach(doc => {
    const q = doc.data();
    const exp = (q.explanation || '') + ' ' + (q.solution || '');
    let matchedPattern = null;
    for (const p of patterns) {
      if (p.test(exp)) {
        matchedPattern = p.toString();
        break;
      }
    }

    if (matchedPattern) {
      const topicCode = q.topicCode || 'NO_TOPIC';
      const subject = topicCode.split('-').slice(0, 3).join('-') || 'OTHER';
      bySubject[subject] = (bySubject[subject] || 0) + 1;
      byTopic[topicCode] = (byTopic[topicCode] || 0) + 1;
      boilerplateList.push({
        id: doc.id,
        questionCode: q.questionCode || doc.id,
        topicCode: q.topicCode,
        matchedPattern,
        explanationSnippet: exp.slice(0, 150),
        fullExplanation: q.explanation || '',
        fullSolution: q.solution || '',
        text: q.text
      });
    }
  });

  console.log(`\n=== SCAN RESULTS ===`);
  console.log(`Total questions with boilerplate explanations: ${boilerplateList.length}`);
  console.log('\nBreakdown by Subject Prefix:');
  console.log(JSON.stringify(bySubject, null, 2));

  console.log('\nBreakdown by Topic Code:');
  console.log(JSON.stringify(byTopic, null, 2));

  fs.writeFileSync('all_boilerplate_questions.json', JSON.stringify({
    count: boilerplateList.length,
    bySubject,
    byTopic,
    questions: boilerplateList
  }, null, 2));
  console.log('\nSaved full details to all_boilerplate_questions.json');
}

scan().catch(console.error);
