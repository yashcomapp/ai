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

async function inspectLetterOnes() {
  const snap = await db.collection('questions').where('type', '==', 'ONE').get();
  const letterOnes = [];
  snap.forEach(d => {
    const q = d.data();
    const ans = String(q.correctAnswer || '').trim();
    if (ans === 'A' || ans === 'B' || ans === 'C' || ans === 'D') {
      letterOnes.push({ id: d.id, ...q });
    }
  });

  console.log(`Found ${letterOnes.length} ONE questions with letter answers.`);
  const chBreakdown = {};
  letterOnes.forEach(q => {
    const prefix = q.topicCode ? q.topicCode.split('-').slice(0, 4).join('-') : 'UNKNOWN';
    chBreakdown[prefix] = (chBreakdown[prefix] || 0) + 1;
  });
  console.log('Chapters affected:', chBreakdown);

  // Inspect first 5
  letterOnes.slice(0, 5).forEach(q => {
    console.log(`\nID: ${q.id} | Topic: ${q.topicCode}`);
    console.log(`Text: ${q.text}`);
    console.log(`Options:`, q.options);
    console.log(`correctAnswer: ${q.correctAnswer}`);
    console.log(`Solution: ${q.solution || q.explanation}`);
  });
}

inspectLetterOnes().then(() => process.exit(0)).catch(console.error);
