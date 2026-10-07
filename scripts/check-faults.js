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
  const snap = await db.collection('systemFaults').orderBy('timestamp', 'desc').limit(15).get();
  console.log('Total faults logged:', snap.size);
  snap.docs.forEach(d => {
    const data = d.data();
    console.log('--- FAULT:', d.id, '---');
    console.log('Category:', data.category);
    console.log('Title:', data.title);
    console.log('Message:', data.errorMessage || data.message || data.error);
    console.log('Stack:', (data.stack || '').slice(0, 300));
    console.log('Context:', JSON.stringify(data.context || data.metadata || {}));
    console.log('Timestamp:', data.timestamp?.toDate ? data.timestamp.toDate().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) : data.timestamp);
  });
}
run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
