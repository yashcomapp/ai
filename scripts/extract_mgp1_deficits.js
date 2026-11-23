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

async function extractMgp1Deficits() {
  const doc = await db.collection('syllabus').doc('cbse_8_mgp1').get();
  const data = doc.data();
  const manifest = [];

  (data.chapters || []).forEach(ch => {
    const chNum = ch.number || ch.chapterNumber;
    const chName = ch.name || ch.title;
    const chLeafs = [];

    (ch.topics || []).forEach(top => {
      const subtopics = top.subtopics || [];
      if (subtopics.length > 0) {
        subtopics.forEach(sub => {
          const count = sub.objectiveCount || 0;
          const needed = Math.max(0, 80 - count);
          chLeafs.push({
            topicCode: sub.topicCode || sub.code,
            name: sub.name || sub.title,
            number: sub.number,
            parentTopic: top.name,
            current: count,
            needed: needed
          });
        });
      } else {
        const count = top.objectiveCount || 0;
        const needed = Math.max(0, 80 - count);
        chLeafs.push({
          topicCode: top.topicCode || top.code,
          name: top.name || top.title,
          number: top.number,
          parentTopic: chName,
          current: count,
          needed: needed
        });
      }
    });

    manifest.push({
      chapterNumber: chNum,
      chapterName: chName,
      leafCount: chLeafs.length,
      currentTotal: chLeafs.reduce((acc, l) => acc + l.current, 0),
      neededTotal: chLeafs.reduce((acc, l) => acc + l.needed, 0),
      leafs: chLeafs
    });
  });

  fs.writeFileSync(path.join(__dirname, 'cbse8_mgp1_deficit_manifest.json'), JSON.stringify(manifest, null, 2));
  console.log('cbse_8_mgp1 deficit manifest generated successfully:');
  manifest.forEach(m => {
    console.log(`Ch ${m.chapterNumber}: ${m.chapterName} -> ${m.leafCount} subtopics | current: ${m.currentTotal} | needed: ${m.neededTotal}`);
  });
}

extractMgp1Deficits().catch(console.error);
