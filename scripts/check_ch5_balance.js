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

async function checkCh5Balance() {
  const snap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-8-SCI-5')
    .where('topicCode', '<=', 'MH-8-SCI-5\uf8ff')
    .get();

  const dist = { A: 0, B: 0, C: 0, D: 0, other: 0 };
  snap.docs.forEach(d => {
    const ans = d.data().correctAnswer;
    if (dist[ans] !== undefined) dist[ans]++;
    else dist.other++;
  });

  console.log(`Total questions in MH-8-SCI-5: ${snap.size}`);
  console.log('Answer distribution:', dist);
  const total = snap.size;
  console.log({
    A: (dist.A / total * 100).toFixed(1) + '%',
    B: (dist.B / total * 100).toFixed(1) + '%',
    C: (dist.C / total * 100).toFixed(1) + '%',
    D: (dist.D / total * 100).toFixed(1) + '%'
  });
}

checkCh5Balance().catch(console.error);
