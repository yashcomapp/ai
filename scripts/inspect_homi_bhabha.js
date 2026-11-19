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

async function run() {
  const snap = await db.collection('questions').where('source', '==', 'homi_bhabha_8th_science_stage_1').get();
  console.log('Total homi_bhabha_8th_science_stage_1 questions:', snap.size);

  let badOptsCount = 0;
  snap.docs.forEach(d => {
    const data = d.data();
    const opts = (data.options || []).map(o => (typeof o === 'object' ? o.text : String(o || '')).trim());
    const hasBad = opts.some(o => !o || /^option\s*[a-d]$/i.test(o) || o.length <= 2);
    if (hasBad) badOptsCount++;
  });
  console.log('Of which have bad/truncated/placeholder options:', badOptsCount);
}
run().catch(console.error);
