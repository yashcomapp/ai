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

async function checkEnv() {
  console.log('--- Checking Syllabus for Class 9 Environmental Management ---');
  const syl = await db.collection('syllabus').where('class', 'in', ['9', 9]).get();
  syl.forEach(d => {
    const data = d.data();
    (data.chapters || []).forEach(ch => {
      if ((ch.title && ch.title.toLowerCase().includes('environment')) || ch.chapterNumber == 9) {
        console.log(`Syllabus: ${data.boardCode} Class ${data.class} ${data.subjectCode} - Ch ${ch.chapterNumber}: ${ch.title}`);
        (ch.topics || []).forEach(t => console.log(`   Topic: ${t.topicCode} -> ${t.title}`));
      }
    });
  });

  console.log('\n--- Querying Questions for Class 9 Science Chapter 9 ---');
  const qSnap = await db.collection('questions')
    .where('class', 'in', ['9', 9])
    .get();

  const ch9Qs = [];
  const phytoQs = [];

  qSnap.forEach(d => {
    const q = d.data();
    const tCode = q.topicCode || '';
    const ch = String(q.chapterNumber || '');
    const sub = q.subjectCode || '';
    const text = q.text || '';
    const sol = q.solution || '';

    if (text.toLowerCase().includes('phytoremediation') || sol.toLowerCase().includes('phytoremediation')) {
      phytoQs.push({ id: d.id, topicCode: tCode, chapterNumber: ch, text, sol, options: q.options, used: q.used || q.usageCount > 0 });
    }

    if ((sub === 'SCIT' || sub === 'SCI') && (ch === '9' || tCode.startsWith('MH-9-SCIT-9') || tCode.startsWith('CBSE-9-SCIE-9'))) {
      ch9Qs.push({ id: d.id, topicCode: tCode, chapterNumber: ch, text, sol, options: q.options, used: q.used || q.usageCount > 0 });
    }
  });

  console.log(`Found ${phytoQs.length} questions mentioning phytoremediation:`);
  phytoQs.forEach(q => {
    console.log(`ID: ${q.id} | Topic: ${q.topicCode} | Ch: ${q.chapterNumber} | Used: ${q.used}`);
    console.log(`Text: ${q.text}`);
    console.log(`Sol: ${q.sol}`);
    console.log(`Opts:`, JSON.stringify(q.options));
    console.log('---');
  });

  console.log(`\nFound ${ch9Qs.length} total questions in Class 9 Science Chapter 9.`);
  console.log('\nLet us sample 25 questions from Ch 9:');
  ch9Qs.slice(0, 25).forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} | ${q.topicCode} | Used: ${q.used}`);
    console.log(`  Q: ${q.text}`);
    console.log(`  Ans/Sol: ${q.sol}`);
  });
}

checkEnv().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
