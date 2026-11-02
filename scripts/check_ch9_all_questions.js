const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

async function checkCh9() {
  const qSnap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-9')
    .where('topicCode', '<=', 'MH-9-SCIT-9\uf8ff')
    .get();

  console.log(`Found ${qSnap.size} questions under MH-9-SCIT-9`);

  const topics = {};
  qSnap.forEach(d => {
    const q = d.data();
    const t = q.topicCode || 'unknown';
    topics[t] = topics[t] || [];
    topics[t].push({ id: d.id, text: q.text, options: q.options, correctAnswer: q.correctAnswer, solution: q.solution, used: q.used || q.usageCount > 0 });
  });

  for (const [t, qs] of Object.entries(topics)) {
    console.log(`\n======================================================`);
    console.log(`Topic: ${t} (${qs.length} questions)`);
    console.log(`======================================================`);
    qs.forEach((q, idx) => {
      console.log(`[${idx+1}] ID: ${q.id} | Used: ${q.used}`);
      console.log(`  Text: ${q.text.slice(0, 100)}...`);
      console.log(`  Correct: ${JSON.stringify(q.correctAnswer)}`);
      console.log(`  Opts: ${JSON.stringify(q.options?.slice(0, 2))}`);
    });
  }
}

checkCh9().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
