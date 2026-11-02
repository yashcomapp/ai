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

async function show12() {
  const ids = [
    'MH-8-SCI-1-1.1-OSC-083',
    'MH-8-SCI-1-1.1-OSC-094',
    'MH-8-SCI-1-1.1-OSC-096',
    'MH-8-SCI-1-1.1-OSC-102',
    'MH-8-SCI-1-1.1-OSC-146',
    'MH-8-SCI-1-1.1-OSC-151',
    'MH-8-SCI-10-10.1-OSC-106',
    'MH-8-SCI-10-10.2-OSC-055',
    'MH-8-SCI-11-11.1-OSC-024',
    'MH-8-SCI-13-13.1-OSC-154',
    'MH-8-SCI-17-17.1-OSC-055',
    'MH-8-SCI-5-5.1-OSC-102'
  ];

  for (const id of ids) {
    const doc = await db.collection('questions').doc(id).get();
    if (doc.exists) {
      console.log('ID:', id);
      console.log('Text:', doc.data().text);
      console.log('Opts:', doc.data().options);
      console.log('Used:', doc.data().used || doc.data().usageCount > 0);
      console.log('---');
    }
  }
}

show12().then(() => process.exit(0)).catch(console.error);
