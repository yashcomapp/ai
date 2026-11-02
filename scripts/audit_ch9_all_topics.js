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

async function auditCh9All() {
  const snap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-9')
    .where('topicCode', '<=', 'MH-9-SCIT-9\uf8ff')
    .get();

  const byTopic = {};
  const outKeywordsByTopic = {
    'MH-9-SCIT-9-9.1': [
      'differential equation', 'non-linear', 'numerical weather', 'lapse rate', 'vapor pressure',
      'anemometer', 'hpa', 'hectopascal', 'supercomputing', 'troposphere', 'meandering', 'jet stream',
      'diurnal temperature', 'synoptic', 'hygrometer', 'mount everest'
    ],
    'MH-9-SCIT-9-9.2': [
      'pyrolysis', 'dioxin', 'supercomputing', 'numerical weather', 'differential equation',
      'radar reflectivity', 'doppler', 'c-band', 's-band', 'supercomputer'
    ],
    'MH-9-SCIT-9-9.3': [
      'fluidized bed', 'dioxin', 'activated carbon', 'hyperaccumulating', 'phytoremediation',
      'anaerobic digestion', 'hydrolytic', 'methanogen', 'landfill gas', 'methane extracted',
      'reverse osmosis', 'eisenia fetida', 'flue gas', 'iswm', 'biochar', 'refractory organics',
      'hydraulic pressure', 'leachate collection pipes', 'geomembrane', 'gizzards',
      'semi-permeable membrane', 'baghouse', 'scrubber', 'cpcb'
    ],
    'MH-9-SCIT-9-9.4': [
      'vasoconstriction', 'sternum', 'capillary', 'tourniquet', 'anatomic', 'physiological',
      'edema', 'cpr chest compression', 'heimlich'
    ]
  };

  snap.forEach(d => {
    const q = d.data();
    const t = q.topicCode || 'other';
    byTopic[t] = byTopic[t] || { total: 0, out: [], fine: [] };
    byTopic[t].total++;

    const str = ((q.text || '') + ' ' + (q.solution || '') + ' ' + (q.explanation || '')).toLowerCase();
    const kList = outKeywordsByTopic[t] || [];
    const isOut = kList.some(k => str.includes(k)) || (q.type === 'ONE' && (t.includes('9.3') || t.includes('9.4')));
    const isUsed = q.used || q.usageCount > 0 || q.timesUsed > 0;

    if (isOut) {
      byTopic[t].out.push({ id: d.id, text: q.text, isUsed });
    } else {
      byTopic[t].fine.push({ id: d.id, text: q.text, isUsed });
    }
  });

  console.log('Chapter 9 breakdown:');
  for (const [t, data] of Object.entries(byTopic)) {
    console.log(`Topic ${t}: Total = ${data.total}, Out-of-syllabus = ${data.out.length}, In-syllabus = ${data.fine.length}`);
    const usedOut = data.out.filter(x => x.isUsed);
    console.log(`  Used out-of-syllabus: ${usedOut.length}`);
  }
}

auditCh9All().then(() => process.exit(0)).catch(console.error);
