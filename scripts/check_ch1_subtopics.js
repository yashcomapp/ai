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

async function checkCh1() {
  const snap = await db.collection('questions')
    .where('chapterNumber', '==', 1)
    .where('subjectCode', '==', 'SCIT')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .get();

  const bySubtopic = {};
  snap.docs.forEach(d => {
    const q = d.data();
    const st = q.subtopicCode || 'unknown';
    if (!bySubtopic[st]) bySubtopic[st] = { exam: 0, practice: 0, foundation: 0, total: 0 };
    bySubtopic[st][q.vault] = (bySubtopic[st][q.vault] || 0) + 1;
    bySubtopic[st].total++;
  });

  console.log('MH-9-SCIT Chapter 1 subtopic question distribution:');
  console.table(Object.entries(bySubtopic).sort((a,b) => a[0].localeCompare(b[0])).map(([st, counts]) => ({
    subtopic: st,
    practice: counts.practice,
    exam: counts.exam,
    foundation: counts.foundation,
    total: counts.total,
    neededFor20: Math.max(0, 20 - counts.practice)
  })));
}

checkCh1();
