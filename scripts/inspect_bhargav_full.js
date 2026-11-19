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

async function inspectBhargavFull() {
  const examId = '023-MH-10-Linear Equations-1.4-1.5-181126';
  const attSnap = await db.collection('examAttempts')
    .where('examId', '==', examId)
    .where('studentName', '==', 'Bhargav Virokar')
    .get();

  const att = attSnap.docs[0].data();
  console.log('Bhargav attempt:', JSON.stringify(att, null, 2));

  const revSnap = await db.collection('reviews').doc(attSnap.docs[0].id).get();
  const rev = revSnap.data();
  console.log('Bhargav review:', JSON.stringify(rev, null, 2));
}

inspectBhargavFull().catch(console.error);
