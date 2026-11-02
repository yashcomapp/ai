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

async function checkTopicDepth() {
  const topics = ['MH-9-SCIT-9-9.1', 'MH-9-SCIT-9-9.2', 'MH-9-SCIT-9-9.3', 'MH-9-SCIT-9-9.4', 'MH-9-SCIT-10-10.1', 'MH-9-SCIT-10-10.2', 'MH-9-SCIT-10-10.3'];
  for (const t of topics) {
    const snap = await db.collection('questions').where('topicCode', '==', t).get();
    console.log(t, 'total questions:', snap.size);
  }
}
checkTopicDepth().then(() => process.exit(0)).catch(console.error);
