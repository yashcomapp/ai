const fs = require('fs');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
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
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

async function inspectScitLetterOnes() {
  const snap = await db.collection('questions').where('type', '==', 'ONE').get();
  const scitOnes = snap.docs.filter(d => {
    const q = d.data();
    return q.topicCode && q.topicCode.startsWith('MH-9-SCIT-');
  });

  console.log('Total MH-9-SCIT ONE questions:', scitOnes.length);
  scitOnes.forEach(d => {
    const q = d.data();
    console.log(`\nID: ${d.id} | Topic: ${q.topicCode}`);
    console.log(`Text: ${q.text}`);
    console.log(`Options:`, q.options);
    console.log(`correctAnswer: ${q.correctAnswer}`);
  });
}

inspectScitLetterOnes().then(() => process.exit(0)).catch(console.error);
