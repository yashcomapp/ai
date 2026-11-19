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
  const snap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '8')
    .where('subjectCode', '==', 'SCI')
    .where('chapterNumber', '==', '5')
    .get();
  
  console.log('Total questions found in MH-8-SCI Chapter 5:', snap.size);

  const byTopic = {};
  snap.forEach(d => {
    const q = d.data();
    // determine parent topic (5.1, 5.2, 5.3, 5.4, 5.5, 5.6)
    const tc = q.topicCode || '';
    const m = tc.match(/MH-8-SCI-5-(5\.\d)/);
    const parent = m ? m[1] : (q.topicNumber ? `5.${q.topicNumber}` : 'unknown');
    
    const vault = q.vault || (q.isFoundation ? 'foundation' : (q.isPractice ? 'practice' : 'exam'));
    if (!byTopic[parent]) byTopic[parent] = { exam: 0, practice: 0, foundation: 0, total: 0 };
    byTopic[parent].total++;
    if (vault === 'exam') byTopic[parent].exam++;
    else if (vault === 'practice') byTopic[parent].practice++;
    else if (vault === 'foundation') byTopic[parent].foundation++;
  });

  console.log('\n--- Parent Topics Status (Target: >=20 Exam, >=25 Practice, >=10 Foundation) ---');
  ['5.1', '5.2', '5.3', '5.4', '5.5', '5.6'].forEach(t => {
    const s = byTopic[t] || { exam: 0, practice: 0, foundation: 0, total: 0 };
    const defExam = Math.max(0, 20 - s.exam);
    const defPrac = Math.max(0, 25 - s.practice);
    const defFound = Math.max(0, 10 - s.foundation);
    console.log(`Topic ${t}: Total=${s.total} | Exam=${s.exam} (need +${defExam}) | Practice=${s.practice} (need +${defPrac}) | Foundation=${s.foundation} (need +${defFound})`);
  });
}

run().catch(console.error);
