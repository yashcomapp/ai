const path = require('path');
const fs = require('fs');
const envPath = path.join(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}
const admin = require('firebase-admin');
const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

async function run() {
  const ids = [
    '016-MH-8-Congruence of-13.3-061026',
    '016-MH-9-Financial Planning-6.1-061026',
    '016-MH-10-Space Missions-10.1-10.2-061026'
  ];
  for (const id of ids) {
    const doc = await db.collection('exams').doc(id).get();
    const data = doc.data();
    console.log(id, 'topicCode:', data?.topicCode, 'topicCodes:', data?.topicCodes);
  }
}
run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
