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

async function inspect13() {
  const snap131 = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.1')
    .get();

  const snap132 = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.2')
    .get();

  console.log('1.3.1 total in DB:', snap131.size);
  const v131 = {};
  snap131.docs.forEach(d => {
    const q = d.data();
    v131[q.vault] = (v131[q.vault] || 0) + 1;
  });
  console.log('1.3.1 by vault:', v131);

  console.log('\n1.3.2 total in DB:', snap132.size);
  const v132_all = {};
  const v132_slope = {};
  const v132_nonslope = {};

  snap132.docs.forEach(d => {
    const q = d.data();
    const v = q.vault || 'unknown';
    v132_all[v] = (v132_all[v] || 0) + 1;

    const text = ((q.text || '') + ' ' + (q.explanation || '')).toLowerCase();
    const isSlope = text.includes('slope') || text.includes('gradient');
    if (isSlope) {
      v132_slope[v] = (v132_slope[v] || 0) + 1;
    } else {
      v132_nonslope[v] = (v132_nonslope[v] || 0) + 1;
    }
  });

  console.log('1.3.2 total by vault:', v132_all);
  console.log('1.3.2 SLOPE questions by vault (should move to 1.3.1):', v132_slope);
  console.log('1.3.2 NON-SLOPE (Area/displacement) by vault (stays in 1.3.2):', v132_nonslope);
}

inspect13();
