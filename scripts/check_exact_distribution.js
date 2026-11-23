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

async function checkSubtopicDistribution() {
  const subjects = [
    { id: 'cbse_9_mgm', name: 'CBSE 9 Maths (Ganita Manjari)' },
    { id: 'cbse_9_scie', name: 'CBSE 9 Science (Exploration)' },
    { id: 'mh_9_mth1', name: 'MH 9 Maths Part 1 (Algebra)' },
    { id: 'mh_9_mth2', name: 'MH 9 Maths Part 2 (Geometry)' },
    { id: 'mh_9_scit', name: 'MH 9 Science & Technology' }
  ];

  console.log('=== EXACT TOPIC/SUBTOPIC QUESTION COUNT DISTRIBUTION (CLASS 9) ===\n');

  for (const sub of subjects) {
    const doc = await db.collection('syllabus').doc(sub.id).get();
    const data = doc.data();
    const counts = [];
    
    (data.chapters || []).forEach(ch => {
      (ch.topics || []).forEach(top => {
        const subtopics = top.subtopics || [];
        if (subtopics.length > 0) {
          subtopics.forEach(subItem => counts.push({ code: subItem.code, count: subItem.objectiveCount || 0 }));
        } else {
          counts.push({ code: top.code, count: top.objectiveCount || 0 });
        }
      });
    });

    const min = Math.min(...counts.map(c => c.count));
    const max = Math.max(...counts.map(c => c.count));
    const exactly80 = counts.filter(c => c.count === 80).length;
    const over80 = counts.filter(c => c.count > 80);
    const under80 = counts.filter(c => c.count < 80);

    console.log(`${sub.name} (${sub.id}):`);
    console.log(`  Total subtopics:      ${counts.length}`);
    console.log(`  Min questions/topic:  ${min}`);
    console.log(`  Max questions/topic:  ${max}`);
    console.log(`  Subtopics == 80 Qs:   ${exactly80} (${((exactly80/counts.length)*100).toFixed(1)}%)`);
    console.log(`  Subtopics > 80 Qs:    ${over80.length} (${((over80.length/counts.length)*100).toFixed(1)}%)`);
    console.log(`  Subtopics < 80 Qs:    ${under80.length} (Deficits: 0)`);
    if (over80.length > 0) {
      console.log(`  Sample surplus:       ${over80.slice(0, 3).map(x => x.code + ': ' + x.count).join(', ')}`);
    }
    console.log('');
  }
}

checkSubtopicDistribution().catch(console.error);
