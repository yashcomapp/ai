const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

async function inspect132() {
  const snap = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.2')
    .get();
  console.log('1.3.2 questions count:', snap.size);

  let slopeCount = 0;
  let areaCount = 0;
  const slopeQs = [];
  snap.docs.forEach(d => {
    const q = d.data();
    const text = ((q.text || '') + ' ' + (q.explanation || '')).toLowerCase();
    if (text.includes('slope') || text.includes('gradient')) {
      slopeCount++;
      slopeQs.push({ id: d.id, qcode: q.questionCode, vault: q.vault, text: q.text.slice(0, 90) });
    }
    if (text.includes('area') || text.includes('displacement')) areaCount++;
  });
  console.log('Mentions slope/gradient in 1.3.2:', slopeCount);
  console.log('Mentions area/displacement in 1.3.2:', areaCount);

  console.log('\nSample slope questions in 1.3.2 (first 10):');
  console.log(JSON.stringify(slopeQs.slice(0, 10), null, 2));

  // Count slopeQs by vault
  const vaultBreak = {};
  slopeQs.forEach(q => {
    vaultBreak[q.vault] = (vaultBreak[q.vault] || 0) + 1;
  });
  console.log('\nSlope questions by vault in 1.3.2:', vaultBreak);
}

inspect132().then(() => process.exit(0)).catch(e => {
  console.error(e);
  process.exit(1);
});
