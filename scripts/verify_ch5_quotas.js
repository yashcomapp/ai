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

async function verifyAndRebuild() {
  console.log('--- Verifying MH-8-SCI Chapter 5 Final Vault Status in DB ---');
  const snap = await db.collection('questions')
    .where('questionCode', '>=', 'MH-8-SCI-5-')
    .where('questionCode', '<=', 'MH-8-SCI-5-\uf8ff')
    .get();

  const topics = {};
  for (let t = 1; t <= 6; t++) {
    topics[`5.${t}`] = { exam: 0, practice: 0, foundation: 0, total: 0 };
  }

  snap.forEach(d => {
    const data = d.data();
    const tCode = data.topicCode || '';
    // e.g. MH-8-SCI-5-5.1.1 -> topic is 5.1
    const match = tCode.match(/MH-8-SCI-5-5\.(\d)/);
    if (match) {
      const topNum = `5.${match[1]}`;
      const v = data.vault || 'exam';
      if (topics[topNum]) {
        topics[topNum].total++;
        if (v === 'exam') topics[topNum].exam++;
        else if (v === 'practice') topics[topNum].practice++;
        else if (v === 'foundation') topics[topNum].foundation++;
      }
    }
  });

  console.log('\nFinal Chapter 5 Vault Summary:');
  console.table(topics);

  let passed = true;
  for (let t = 1; t <= 6; t++) {
    const topKey = `5.${t}`;
    const cur = topics[topKey];
    console.log(`Topic ${topKey}: Exam=${cur.exam} (>=20: ${cur.exam >= 20 ? 'OK' : 'FAIL'}), Practice=${cur.practice} (>=25: ${cur.practice >= 25 ? 'OK' : 'FAIL'}), Foundation=${cur.foundation} (>=10: ${cur.foundation >= 10 ? 'OK' : 'FAIL'})`);
    if (cur.exam < 20 || cur.practice < 25 || cur.foundation < 10) {
      passed = false;
    }
  }

  console.log(`\nOverall Chapter 5 Quota Compliance: ${passed ? 'PASSED 100%' : 'NEEDS ADJUSTMENT'}`);
}

verifyAndRebuild().catch(console.error);
