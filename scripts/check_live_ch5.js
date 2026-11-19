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

async function checkLiveCh5() {
  const snap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-8-SCI-5')
    .where('topicCode', '<=', 'MH-8-SCI-5\uf8ff')
    .get();

  const advancedTerms = [
    'planck', '6.626', 'sin^4', 'larmor', 'de broglie', 'maxwell', 'schrodinger',
    'fermion', 'bohr radius', 'specific charge', 'volume ratio', '10^{15}',
    'angular momentum', 'quark', 'moseley', 'positron emission tomography',
    'heisenberg', 'decay products'
  ];

  const flagged = [];
  snap.docs.forEach(doc => {
    const q = doc.data();
    const qStr = (q.text + ' ' + JSON.stringify(q.options) + ' ' + (q.explanation || '')).toLowerCase();
    for (const t of advancedTerms) {
      if (qStr.includes(t.toLowerCase())) {
        flagged.push({
          id: doc.id,
          code: q.questionCode || doc.id,
          term: t,
          text: q.text
        });
        break;
      }
    }
  });

  console.log(`Live Ch 5 questions flagged with university/advanced physics: ${flagged.length}`);
  flagged.forEach(f => console.log(`- [${f.code}] [Term: ${f.term}]: ${f.text}`));
}

checkLiveCh5().catch(console.error);
