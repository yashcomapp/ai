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

async function testAllChapters() {
  const sylDoc = await db.collection('syllabus').doc('mh_8_mth').get();
  const subjectData = sylDoc.data();

  const classVariations = ['8', 8];
  const qSnap = await db.collection('questions').where('class', 'in', classVariations).get();

  console.log(`Total questions fetched for class 8 (string + number): ${qSnap.size}`);

  const questionsList = qSnap.docs.map(doc => {
    const q = doc.data();
    const b = String(q.board || '').toLowerCase();
    const s = String(q.subject || '').toLowerCase();
    const sc = String(q.subjectCode || '').toLowerCase();

    const bMatch = b.includes('mh') || b.includes('maharashtra') || String(q.boardCode || '').toLowerCase() === 'mh';
    const sMatch = s.includes('math') || sc === 'mth' || sc === 'math';
    if (!bMatch || !sMatch) return null;

    let chNum = String(q.chapterNumber || q.chapter || '').replace(/^Ch\.?\s*/i, '').trim();
    const topNum = String(q.topicNumber || '').trim();
    const subNum = String(q.subtopicNumber || '').trim();
    const tCode = String(q.topicCode || '').trim();
    const sCode = String(q.subtopicCode || '').trim();
    const tName = String(q.topic || q.topicName || '').trim();
    const sName = String(q.subtopic || q.subtopicName || '').trim();
    const cTag = String(q.conceptTag || '').trim();
    const qtype = q.type || '';
    const isObjective = !qtype.startsWith('subjective');

    if (!chNum && tCode.includes('-')) {
      const parts = tCode.split('-');
      if (parts.length >= 4) chNum = parts[3];
    }
    if (!chNum && doc.id.includes('-')) {
      const parts = doc.id.split('-');
      if (parts.length >= 4) chNum = parts[3];
    }

    return { id: doc.id, chNum, topNum, subNum, tCode, sCode, tName, sName, cTag, isObjective };
  }).filter(Boolean);

  console.log(`Matched MH Math questions: ${questionsList.length}`);

  const chapters = subjectData.chapters || [];
  const results = [];

  chapters.forEach(chap => {
    const chapNumStr = String(chap.number ?? '').trim();
    const chapQuestions = questionsList.filter(q => {
      if (!q) return false;
      if (q.chNum && q.chNum === chapNumStr) return true;
      const tParts = String(q.tCode || '').split('-');
      if (tParts.length >= 4 && tParts[3] === chapNumStr) return true;
      const idParts = String(q.id || '').split('-');
      if (idParts.length >= 4 && idParts[3] === chapNumStr) return true;
      return false;
    });

    const objCount = chapQuestions.filter(q => q.isObjective).length;
    const subjCount = chapQuestions.filter(q => !q.isObjective).length;

    if (objCount > 0 || subjCount > 0) {
      results.push({
        chapterNumber: chapNumStr,
        name: chap.name,
        objectiveCount: objCount,
        subjectiveCount: subjCount
      });
    }
  });

  console.log('Exam Generator Chapter Counts for mh_8_mth:', JSON.stringify(results, null, 2));
}

testAllChapters().catch(console.error);
