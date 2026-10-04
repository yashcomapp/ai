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

async function inspectMismatches() {
  const qSnap = await db.collection('questions').get();
  const summary = {};

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const docId = doc.id;
    const qCode = q.questionCode || '';
    const tCode = q.topicCode || '';
    const chNum = String(q.chapterNumber || '');
    const tNum = String(q.topicNumber || '');
    const boardCode = q.boardCode || '';
    const cls = String(q.class || '').replace(/\D/g, '');
    const subjCode = q.subjectCode || '';

    const expectedTopicCode = `${boardCode}-${cls}-${subjCode}-${chNum.replace(/\D/g, '')}-${tNum.trim()}`;
    if (tCode !== expectedTopicCode) {
      const key = `${subjCode} | ch:${chNum} vs tCode:${tCode}`;
      if (!summary[key]) summary[key] = { count: 0, samples: [] };
      summary[key].count++;
      if (summary[key].samples.length < 3) {
        summary[key].samples.push({ docId, qCode, tCode, chNum, tNum, subj: q.subject });
      }
    }
  });

  console.log('--- TOPIC MISMATCH PATTERNS ---');
  for (const [k, v] of Object.entries(summary)) {
    console.log(`Pattern: "${k}" (Total: ${v.count})`);
    console.log('  Samples:', JSON.stringify(v.samples, null, 2));
  }
}

inspectMismatches().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
