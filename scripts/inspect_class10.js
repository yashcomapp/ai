const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
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
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function check10() {
  const snap = await db.collection('questions').where('class', '==', '10').where('boardCode', '==', 'MH').get();
  console.log(`Class 10 MH questions count: ${snap.size}`);
  const subjCounts = {};
  const topicSample = {};

  snap.docs.forEach(doc => {
    const d = doc.data();
    const key = `${d.subjectCode} | ${d.subject}`;
    subjCounts[key] = (subjCounts[key] || 0) + 1;
    if (!topicSample[d.subjectCode]) {
      topicSample[d.subjectCode] = { id: doc.id, topicCode: d.topicCode, topic: d.topic, subject: d.subject };
    }
  });

  console.log('Class 10 MH Breakdown:', subjCounts);
  console.log('Sample per subjectCode:', topicSample);
}

check10().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
