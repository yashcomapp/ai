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

async function run() {
  console.log('--- 1. Scan all syllabus documents ---');
  const sylSnap = await db.collection('syllabus').get();
  console.log('Total syllabus docs:', sylSnap.size);
  sylSnap.forEach(doc => {
    const d = doc.data();
    console.log(doc.id, { board: d.board, class: d.class, classType: typeof d.class, subject: d.subject, subjectCode: d.subjectCode, chaptersCount: d.chapters?.length });
    if (String(d.class) === '8' && (d.board === 'MH' || d.board === 'Maharashtra')) {
      const ch13 = (d.chapters || []).find(c => String(c.number) === '13');
      if (ch13) {
        console.log('--- Chapter 13 in syllabus doc ' + doc.id + ' ---');
        console.log(JSON.stringify(ch13, null, 2));
      }
    }
  });

  console.log('\n--- 2. Scan questions matching 13.3 ---');
  const qSnap = await db.collection('questions').get();
  console.log('Total questions in DB:', qSnap.size);
  const ch13Questions = [];
  qSnap.forEach(doc => {
    const q = doc.data();
    if (doc.id.includes('-13-') || String(q.chapterNumber) === '13' || (q.topicCode && q.topicCode.includes('-13-')) || (q.questionCode && q.questionCode.includes('-13-'))) {
      ch13Questions.push({ id: doc.id, ...q });
    }
  });
  console.log('Found Ch 13 questions count:', ch13Questions.length);
  const byTopicCode = {};
  ch13Questions.forEach(q => {
    const tc = q.topicCode || 'NO_TOPIC_CODE';
    byTopicCode[tc] = (byTopicCode[tc] || 0) + 1;
  });
  console.log('Question breakdown by topicCode:', byTopicCode);

  const sample1331 = ch13Questions.filter(q => (q.topicCode && q.topicCode.includes('13.3.1')) || (q.questionCode && q.questionCode.includes('13.3.1')));
  console.log('Total 13.3.1 questions:', sample1331.length);
  if (sample1331.length > 0) {
    console.log('Sample 13.3.1 Question doc:', JSON.stringify(sample1331[0], null, 2));
  }

  const sample1332 = ch13Questions.filter(q => (q.topicCode && q.topicCode.includes('13.3.2')) || (q.questionCode && q.questionCode.includes('13.3.2')));
  console.log('Total 13.3.2 questions:', sample1332.length);
  if (sample1332.length > 0) {
    console.log('Sample 13.3.2 Question doc:', JSON.stringify(sample1332[0], null, 2));
  }
}

run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
