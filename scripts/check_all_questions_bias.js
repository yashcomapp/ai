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
  console.log('Querying questions collection...');
  const snap = await db.collection('questions').get();
  console.log('Total questions in DB:', snap.size);

  const answerDist = { A: 0, B: 0, C: 0, D: 0, other: 0, subjective: 0 };
  const biasedBySubject = {};

  snap.forEach(doc => {
    const q = doc.data();
    const type = q.type || '';
    if (type.startsWith('S') || type.includes('subjective') || type.includes('numerical_short') || type.includes('numerical_long')) {
      answerDist.subjective++;
      return;
    }
    const ans = (q.correctAnswer || '').trim().toUpperCase();
    if (ans === 'A' || ans === 'B' || ans === 'C' || ans === 'D') {
      answerDist[ans]++;
    } else {
      answerDist.other++;
    }

    const sub = `${q.boardCode || q.board || 'unknown'}-${q.class || 'unknown'}-${q.subjectCode || q.subject || 'unknown'}`;
    if (!biasedBySubject[sub]) biasedBySubject[sub] = { total: 0, A: 0, B: 0, C: 0, D: 0 };
    biasedBySubject[sub].total++;
    if (['A', 'B', 'C', 'D'].includes(ans)) {
      biasedBySubject[sub][ans]++;
    }
  });

  console.log('Overall Answer Distribution:');
  console.log(answerDist);
  console.log('\nBreakdown by Subject:');
  Object.keys(biasedBySubject).forEach(k => {
    const s = biasedBySubject[k];
    const pctA = s.total > 0 ? Math.round((s.A / s.total) * 100) : 0;
    console.log(`${k.padEnd(25)}: Total=${String(s.total).padStart(5)} | A=${String(s.A).padStart(5)} (${pctA}%) | B=${String(s.B).padStart(4)} | C=${String(s.C).padStart(4)} | D=${String(s.D).padStart(4)}`);
  });
}

run().catch(console.error);
