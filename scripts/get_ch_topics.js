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

async function main() {
  const chNum = process.argv[2] || '14';
  const doc = await db.collection('syllabus').doc('mh_9_scit').get();
  const data = doc.data();
  const ch = (data.chapters || []).find(c => String(c.number) === String(chNum));
  if (ch) {
    console.log(`\nChapter ${ch.number}: ${ch.name}`);
    (ch.topics || []).forEach(t => {
      console.log(`  ${t.topicCode || t.code}: ${t.name || t.title}`);
    });
  }
}

main().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
