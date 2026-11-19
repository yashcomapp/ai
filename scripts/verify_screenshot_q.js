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
  const doc = await db.collection('questions').doc('MH-8-SCI-5-5.2.2-OSC-001').get();
  const d = doc.data();
  console.log('ID:', doc.id);
  console.log('Text:', d.text);
  console.log('Options:', d.options);
  console.log('CorrectAnswer:', d.correctAnswer);
  console.log('Explanation:', d.explanation);
  console.log('Solution:', d.solution);
}

run().catch(console.error);
