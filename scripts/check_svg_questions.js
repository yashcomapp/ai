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

async function checkSvg() {
  const snap = await db.collection('questions').get();
  let svgCount = 0;
  let reqFigCount = 0;
  let imgCount = 0;
  const sampleSvg = [];

  snap.docs.forEach(doc => {
    const q = doc.data();
    const txt = q.text || q.questionText || '';
    if (txt.includes('<svg') || txt.includes('<SVG')) {
      svgCount++;
      if (sampleSvg.length < 5) sampleSvg.push({ id: doc.id, topicCode: q.topicCode, text: txt });
    }
    if (q.requiresFigure === true) reqFigCount++;
    if (q.imageUrl) imgCount++;
  });

  console.log({ total: snap.size, svgCount, reqFigCount, imgCount, sampleSvgCount: sampleSvg.length });
  if (sampleSvg.length > 0) {
    console.log('Sample SVG Question:', JSON.stringify(sampleSvg[0], null, 2));
  }
}

checkSvg().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
