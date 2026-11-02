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

async function categorize9_3() {
  const snap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-9-9.3')
    .get();

  const outOfSyllabus = [];
  const inSyllabus = [];

  const outKeywords = [
    'fluidized bed', 'dioxin', 'activated carbon', 'hyperaccumulating', 'phytoremediation',
    'anaerobic digestion', 'hydrolytic', 'methanogen', 'landfill gas', 'methane extracted',
    'reverse osmosis', 'eisenia fetida', 'flue gas', 'iswm', 'biochar', 'refractory organics',
    'hydraulic pressure', 'leachate collection pipes', 'geomembrane', 'gizzards',
    'semi-permeable membrane', 'baghouse', 'scrubber'
  ];

  snap.forEach(d => {
    const q = d.data();
    const str = ((q.text || '') + ' ' + (q.solution || '') + ' ' + (q.explanation || '')).toLowerCase();
    const isOut = outKeywords.some(k => str.includes(k));
    const isUsed = q.used || q.usageCount > 0 || q.timesUsed > 0;

    if (isOut) {
      outOfSyllabus.push({ id: d.id, text: q.text, isUsed });
    } else {
      inSyllabus.push({ id: d.id, text: q.text, isUsed });
    }
  });

  console.log(`Topic MH-9-SCIT-9-9.3: Total: ${snap.size}`);
  console.log(`Out of syllabus: ${outOfSyllabus.length}`);
  console.log(`In syllabus: ${inSyllabus.length}`);

  console.log('\n--- Out of syllabus questions ---');
  outOfSyllabus.forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} (Used: ${q.isUsed}) -> ${q.text.slice(0, 100)}...`);
  });
}

categorize9_3().then(() => process.exit(0)).catch(console.error);
