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
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function checkClassTypes() {
  const allQSnap = await db.collection('questions').get();
  let stringCount = 0;
  let numberCount = 0;
  let missingCount = 0;

  const toUpdate = [];

  allQSnap.forEach(d => {
    const dt = d.data();
    const c = dt.class;
    if (typeof c === 'string') {
      stringCount++;
      const numVal = parseInt(c.replace(/\D/g, ''), 10);
      if (!isNaN(numVal)) {
        toUpdate.push({ id: d.id, classNum: numVal });
      }
    } else if (typeof c === 'number') {
      numberCount++;
    } else {
      missingCount++;
      const match = (dt.questionCode || dt.topicCode || '').match(/-(8|9|10)-/);
      if (match) {
        toUpdate.push({ id: d.id, classNum: parseInt(match[1], 10) });
      }
    }
  });

  console.log('Class field types across 9,557 questions:');
  console.log(`- Number: ${numberCount}`);
  console.log(`- String: ${stringCount}`);
  console.log(`- Missing: ${missingCount}`);
  console.log(`- Needs Normalization: ${toUpdate.length}`);
}

checkClassTypes().catch(console.error);
