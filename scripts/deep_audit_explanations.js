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

async function auditLongExplanations() {
  console.log('Fetching all questions...');
  const snap = await db.collection('questions').get();
  console.log(`Total questions: ${snap.size}`);

  const byLength = {
    under150: 0,
    between150and300: 0,
    between300and500: 0,
    over500: 0
  };

  const over300BySubject = {};
  const longSamples = [];

  snap.docs.forEach(d => {
    const q = d.data();
    const exp = (q.explanation || q.solution || '').trim();
    const len = exp.length;
    if (len < 150) byLength.under150++;
    else if (len <= 300) byLength.between150and300++;
    else if (len <= 500) byLength.between300and500++;
    else byLength.over500++;

    if (len > 300) {
      const subj = (q.topicCode || 'OTHER').split('-').slice(0, 3).join('-');
      over300BySubject[subj] = (over300BySubject[subj] || 0) + 1;
      if (longSamples.length < 15) {
        longSamples.push({
          id: d.id,
          code: q.questionCode || d.id,
          topic: q.topicCode,
          len,
          snippet: exp.slice(0, 200)
        });
      }
    }
  });

  console.log('Length distribution:', byLength);
  console.log('Questions > 300 chars by subject:', over300BySubject);
  console.log('Samples of long explanations:');
  longSamples.forEach(s => {
    console.log(`[${s.code}] (${s.topic}) len=${s.len}: ${s.snippet.replace(/\n/g, ' ')}`);
  });
}

auditLongExplanations().catch(console.error);
