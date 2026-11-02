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

async function checkAllChapters() {
  const snap = await db.collection('questions').where('subjectCode', '==', 'SCIT').where('class', 'in', ['9', 9]).get();
  const byCh = {};
  snap.forEach(d => {
    const q = d.data();
    const ch = q.chapterNumber || 'none';
    byCh[ch] = (byCh[ch] || 0) + 1;
  });
  console.log('Class 9 Science chapters question distribution:');
  Object.keys(byCh).sort((a,b) => Number(a) - Number(b)).forEach(ch => {
    console.log(`Chapter ${ch}: ${byCh[ch]} questions`);
  });
}

checkAllChapters().then(() => process.exit(0)).catch(console.error);
