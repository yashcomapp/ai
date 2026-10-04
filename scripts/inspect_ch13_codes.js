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
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function inspectSamples() {
  console.log('--- ALL SYLLABUS DOC IDS AND BOARDS ---');
  const sylSnap = await db.collection('syllabus').get();
  sylSnap.forEach(d => {
    const dt = d.data();
    console.log('Syllabus Doc ID:', d.id, 'board:', dt.board, 'boardCode:', dt.boardCode, 'class:', dt.class, 'className:', dt.className, 'subject:', dt.subject, 'subjectCode:', dt.subjectCode);
  });

  console.log('\n--- SAMPLE QUESTIONS CONTAINING "Congruence" OR "13" ---');
  const qSnap = await db.collection('questions').limit(10).get();
  console.log('Sample question fields:');
  qSnap.forEach(d => {
    const dt = d.data();
    console.log('Q Doc ID:', d.id, 'board:', dt.board, 'boardCode:', dt.boardCode, 'class:', dt.class, 'className:', dt.className, 'chapter:', dt.chapter, 'chapterName:', dt.chapterName, 'subject:', dt.subject, 'subjectCode:', dt.subjectCode, 'questionCode:', dt.questionCode, 'topicCode:', dt.topicCode);
  });

  console.log('\n--- FIND QUESTIONS WITH CODE CONTAINING 13.1 ---');
  const allQ = await db.collection('questions').get();
  console.log('Total questions in collection:', allQ.size);
  let countCh13 = 0;
  allQ.forEach(d => {
    const dt = d.data();
    if ((dt.questionCode && dt.questionCode.includes('13')) || (dt.topicCode && dt.topicCode.includes('13')) || (dt.text && dt.text.includes('Congruen'))) {
      countCh13++;
      if (countCh13 <= 5) {
        console.log('Ch13 Q Match:', d.id, 'code:', dt.questionCode, 'topicCode:', dt.topicCode, 'board:', dt.board, 'class:', dt.class, 'subject:', dt.subject, 'subjectCode:', dt.subjectCode);
      }
    }
  });
  console.log(`Total questions matched with 13/Congruence: ${countCh13}`);

  console.log('\n--- SAMPLE SYLLABUS TOPIC INDEX DOCS ---');
  const topSnap = await db.collection('syllabusTopicIndex').get();
  console.log('Total topic index docs:', topSnap.size);
  let topCh13Count = 0;
  topSnap.forEach(d => {
    const dt = d.data();
    if ((dt.topicCode && dt.topicCode.includes('13')) || (dt.topicName && dt.topicName.includes('Congruen'))) {
      topCh13Count++;
      console.log('Topic Index Ch13:', d.id, 'topicCode:', dt.topicCode, 'board:', dt.board, 'boardCode:', dt.boardCode, 'class:', dt.class, 'subjectCode:', dt.subjectCode, 'questionCount:', dt.questionCount, 'objectiveCount:', dt.objectiveCount);
    }
  });
  console.log(`Total topic index docs with 13/Congruence: ${topCh13Count}`);
}

inspectSamples().catch(console.error);
