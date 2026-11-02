const fs = require('fs');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
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
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

async function checkChapterCounts() {
  const formulaChapters = [
    { code: 'MH-9-SCIT-1', name: 'Laws of Motion' },
    { code: 'MH-9-SCIT-2', name: 'Work and Energy' },
    { code: 'MH-9-SCIT-3', name: 'Current Electricity' },
    { code: 'MH-9-SCIT-4', name: 'Measurement of Matter' },
    { code: 'MH-9-SCIT-11', name: 'Reflection of Light' },
    { code: 'MH-9-SCIT-12', name: 'Study of Sound' },
    { code: 'MH-8-SCI-3', name: 'Force and Pressure' }
  ];

  const snap = await db.collection('questions')
    .where('type', '==', 'ONE')
    .get();
  
  const countByCh = {};
  snap.forEach(d => {
    const tc = d.data().topicCode || '';
    for (const ch of formulaChapters) {
      if (tc.startsWith(ch.code)) {
        countByCh[ch.code] = (countByCh[ch.code] || 0) + 1;
      }
    }
  });

  console.log('Current Numerical (ONE) count per formula chapter:');
  for (const ch of formulaChapters) {
    const cnt = countByCh[ch.code] || 0;
    console.log(`  ${ch.code} (${ch.name}): ${cnt} numericals (Needs ${Math.max(0, 25 - cnt)} more to reach 25)`);
  }
}

checkChapterCounts().then(() => process.exit(0)).catch(console.error);
