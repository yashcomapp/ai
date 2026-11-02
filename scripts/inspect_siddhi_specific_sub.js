const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

async function inspectDoc() {
  const pDoc = await db.collection('practiceSubmissions').doc('ST-2026-000026_PRACTICE_MH-9-SCIT-9-9.3.1_sess_1793579286185_1dyjel4pm').get();
  if (pDoc.exists) {
    console.log('practiceSubmission data:', JSON.stringify(pDoc.data(), null, 2));
  } else {
    console.log('Not in practiceSubmissions, checking parentReviews...');
    const rDoc = await db.collection('parentReviews').doc('ST-2026-000026_PRACTICE_MH-9-SCIT-9-9.3.1_sess_1793579286185_1dyjel4pm').get();
    if (rDoc.exists) {
      console.log('parentReviews data:', JSON.stringify(rDoc.data(), null, 2));
    }
  }
}
inspectDoc().then(() => process.exit(0));
