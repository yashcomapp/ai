const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
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

async function inspectSampleQuestion() {
  const snap = await db.collection('questions').doc('CBSE-8-MGP1-1-1.1.1-OSC-001').get();
  if (snap.exists) {
    console.log('Sample question found:');
    console.log(JSON.stringify(snap.data(), null, 2));
  } else {
    const qSnap = await db.collection('questions')
      .where('topicCode', '==', 'CBSE-8-MGP1-1-1.1.1')
      .limit(1)
      .get();
    if (!qSnap.empty) {
      console.log('Sample question by topic:');
      console.log(JSON.stringify(qSnap.docs[0].data(), null, 2));
    } else {
      console.log('No question found for topic');
    }
  }
}
inspectSampleQuestion().catch(console.error);
