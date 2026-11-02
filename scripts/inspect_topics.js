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

async function inspectTopicBreakdown() {
  const chapters = [
    'MH-9-SCIT-1',
    'MH-9-SCIT-2',
    'MH-9-SCIT-3',
    'MH-9-SCIT-4',
    'MH-9-SCIT-11',
    'MH-9-SCIT-12',
    'MH-9-SCIT-18',
    'MH-8-SCI-3'
  ];

  for (const ch of chapters) {
    const snap = await db.collection('questions')
      .where('topicCode', '>=', ch)
      .where('topicCode', '<=', ch + '-\uf8ff')
      .get();
    
    const topics = {};
    snap.forEach(d => {
      const q = d.data();
      const tc = q.topicCode || 'UNKNOWN';
      if (!topics[tc]) topics[tc] = { total: 0, one: 0, ssn: 0, title: q.topicName || q.topicTitle || '' };
      topics[tc].total++;
      if (q.type === 'ONE') topics[tc].one++;
      if (q.type === 'SSN') topics[tc].ssn++;
    });

    console.log(`\n=== Chapter ${ch} ===`);
    Object.keys(topics).sort().forEach(t => {
      console.log(`  ${t} [${topics[t].title}]: Total ${topics[t].total} (ONE: ${topics[t].one}, SSN: ${topics[t].ssn})`);
    });
  }
}

inspectTopicBreakdown().then(() => process.exit(0)).catch(console.error);
