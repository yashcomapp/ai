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

async function checkSubject(subId = 'cbse_8_mgp1') {
  const doc = await db.collection('syllabus').doc(subId).get();
  const data = doc.data();
  console.log(`=== SYLLABUS AUDIT FOR ${subId} ===`);
  (data.chapters || []).forEach(ch => {
    let chTotal = 0;
    let chDeficits = 0;
    let chLeafs = 0;
    (ch.topics || []).forEach(t => {
      const subtopics = t.subtopics || [];
      if (subtopics.length > 0) {
        subtopics.forEach(s => {
          chLeafs++;
          const cnt = s.objectiveCount || 0;
          chTotal += cnt;
          if (cnt < 80) chDeficits++;
        });
      } else {
        chLeafs++;
        const cnt = t.objectiveCount || 0;
        chTotal += cnt;
        if (cnt < 80) chDeficits++;
      }
    });
    const status = chDeficits === 0 ? '✅ 100% (0 deficit)' : `❌ ${chDeficits} deficit subtopics`;
    console.log(`Ch ${ch.number || ch.chapterNumber}: ${ch.name || ch.title} -> ${chTotal} Qs / ${chLeafs * 80} target [${status}]`);
  });
}

checkSubject(process.argv[2] || 'cbse_8_mgp1').catch(console.error);
