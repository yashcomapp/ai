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

async function auditCh9Details() {
  const qSnap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-9')
    .where('topicCode', '<=', 'MH-9-SCIT-9\uf8ff')
    .get();

  console.log(`Auditing all ${qSnap.size} questions in Chapter 9...`);

  const complexKeywords = [
    'differential equation', 'non-linear', 'psychrometric', 'vapor pressure', 'lapse rate',
    'phytoremediation', 'fluidized bed', 'dioxin', 'hyperaccumulating', 'electrostatic precipitator',
    'anaerobic digestion', 'hydrolytic', 'methanogen', 'landfill gas', 'anemometer', 'hpa',
    'supercomputing', 'numerical weather', 'troposphere', 'meandering', 'jet stream',
    'vasoconstriction', 'sternum', 'heimlich', 'tourniquet', 'pyrolysis', 'capillary'
  ];

  const flagged = [];
  const fine = [];

  qSnap.forEach(d => {
    const q = d.data();
    const text = (q.text || '') + ' ' + (q.solution || '') + ' ' + (q.explanation || '');
    const lower = text.toLowerCase();
    const matched = complexKeywords.filter(k => lower.includes(k));
    const isUsed = q.used || q.usageCount > 0 || q.timesUsed > 0;

    if (matched.length > 0) {
      flagged.push({ id: d.id, topicCode: q.topicCode, text: q.text, sol: q.solution || q.explanation, matched, isUsed });
    } else {
      fine.push({ id: d.id, topicCode: q.topicCode, text: q.text, sol: q.solution || q.explanation, isUsed });
    }
  });

  console.log(`Flagged as advanced/out-of-syllabus: ${flagged.length}`);
  console.log(`Standard textbook questions: ${fine.length}`);

  console.log('\n--- Sample Flagged Questions ---');
  flagged.slice(0, 20).forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} (Keywords: ${q.matched.join(', ')}) | Used: ${q.isUsed}`);
    console.log(`  Text: ${q.text.slice(0, 120)}...`);
    console.log(`  Sol: ${(q.sol || '').slice(0, 120)}...`);
  });

  console.log('\n--- Sample Fine Questions ---');
  fine.slice(0, 10).forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} | Used: ${q.isUsed}`);
    console.log(`  Text: ${q.text.slice(0, 120)}...`);
  });
}

auditCh9Details().then(() => process.exit(0)).catch(console.error);
