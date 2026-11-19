const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) envVars[trimmed.slice(0, idx).trim()] = trimmed.slice(idx + 1).trim().replace(/^['"]|['"]$/g, '');
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function unclampRemaining5() {
  const targets = [
    { id: '011-MH-8-Force and Pressure-3.3-290926_ST-2026-000080', calc: -1, total: 60 },
    { id: '011-MH-8-Force and Pressure-3.3-290926_ST-2026-000081', calc: -6, total: 60 },
    { id: '013-MH-9-Circle-6.1-011026_ST-2026-000040', calc: -5, total: 60 },
    { id: '021-MH-10-Carbon Compounds-9.2+9.1-141026_ST-2026-000042', calc: -4, total: 100 },
    { id: '021-MH-10-Carbon Compounds-9.2+9.1-141026_ST-2026-000052', calc: -4, total: 100 }
  ];

  for (const t of targets) {
    const rDoc = await db.collection('reviews').doc(t.id).get();
    if (rDoc.exists) {
      const data = rDoc.data();
      const totalMarks = data.totalMarks || t.total;
      const pct = parseFloat(((t.calc / totalMarks) * 100).toFixed(1));
      await rDoc.ref.update({
        score: t.calc,
        percentage: pct,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      console.log(`Updated review ${t.id}: score=${t.calc}, pct=${pct}%`);
    }

    const aDoc = await db.collection('examAttempts').doc(t.id).get();
    if (aDoc.exists) {
      const data = aDoc.data();
      const totalMarks = data.totalMarks || t.total;
      const pct = parseFloat(((t.calc / totalMarks) * 100).toFixed(1));
      await aDoc.ref.update({
        score: t.calc,
        percentage: pct,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      console.log(`Updated examAttempt ${t.id}: score=${t.calc}, pct=${pct}%`);
    }
  }

  console.log('Done un-clamping remaining 5 reviews!');
}

unclampRemaining5().catch(console.error);
