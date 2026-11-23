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

async function checkMaxSeq() {
  const prefixes = [
    { prefix: 'CBSE-8-MGP1', name: 'cbse_8_mgp1' },
    { prefix: 'CBSE-8-MGP2', name: 'cbse_8_mgp2' },
    { prefix: 'CBSE-8-CURI', name: 'cbse_8_curi' },
    { prefix: 'MH-8-MTH', name: 'mh_8_mth' },
    { prefix: 'MH-8-SCI', name: 'mh_8_sci' }
  ];

  for (const s of prefixes) {
    const snaps = await db.collection('questions')
      .where('topicCode', '>=', s.prefix)
      .where('topicCode', '<=', s.prefix + '-\uf8ff')
      .select('questionCode')
      .get();

    let maxSeq = 0;
    snaps.forEach(doc => {
      const qc = doc.data().questionCode || '';
      const parts = qc.split('-');
      const seq = parseInt(parts[parts.length - 1], 10);
      if (!isNaN(seq) && seq > maxSeq) maxSeq = seq;
    });
    console.log(`${s.name} (${s.prefix}): ${snaps.size} questions, max sequence = ${maxSeq}`);
  }
}

checkMaxSeq().catch(console.error);
