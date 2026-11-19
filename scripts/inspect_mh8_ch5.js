const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function inspectCh5() {
  const syllSnap = await db.collection('syllabus')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '8')
    .where('subjectCode', '==', 'SCI')
    .get();

  if (syllSnap.empty) {
    console.log('No syllabus doc found for MH-8-SCI');
    return;
  }
  const syll = syllSnap.docs[0].data();
  console.log('Syllabus doc ID:', syllSnap.docs[0].id);
  console.log('Syllabus doc keys:', Object.keys(syll));
  console.log('Chapters type or length:', Array.isArray(syll.chapters) ? syll.chapters.length : typeof syll.chapters);
  const ch3 = syll.chapters.find(c => (c.chapterName || c.name || '').includes('Force and Pressure'));
  console.log('Chapter 3 vaultCounts:', JSON.stringify(ch3.vaultCounts, null, 2));
  if (ch3.topics && ch3.topics[0]) {
    console.log('Ch 3 Topic 0 vaultCounts:', JSON.stringify(ch3.topics[0].vaultCounts, null, 2));
    if (ch3.topics[0].subtopics && ch3.topics[0].subtopics[0]) {
      console.log('Ch 3 Topic 0 Subtopic 0 vaultCounts:', JSON.stringify(ch3.topics[0].subtopics[0].vaultCounts, null, 2));
    }
  }
  console.log('Topics count:', ch5.topics.length);
  ch5.topics.forEach((t) => {
    console.log(`Topic ${t.topicNumber}: ${t.topicName} (topicCode: ${t.topicCode})`);
    if (t.subtopics) {
      t.subtopics.forEach(st => {
        console.log(`  Subtopic ${st.subtopicNumber}: ${st.subtopicName} (subtopicCode: ${st.subtopicCode})`);
      });
    }
  });

  // Check syllabusTopicIndex for MH-8-SCI-3 and MH-8-SCI-5
  // Check vaults for 5.1.1 and 5.1.2
  const qSnap511 = await db.collection('questions').where('topicCode', '==', 'MH-8-SCI-5-5.1.1').get();
  const v511 = {};
  qSnap511.docs.forEach(d => {
    const q = d.data();
    v511[q.vault || 'none'] = (v511[q.vault || 'none'] || 0) + 1;
  });
  console.log('5.1.1 vaults:', v511);

  const qSnap512 = await db.collection('questions').where('topicCode', '==', 'MH-8-SCI-5-5.1.2').get();
  const v512 = {};
  qSnap512.docs.forEach(d => {
    const q = d.data();
    v512[q.vault || 'none'] = (v512[q.vault || 'none'] || 0) + 1;
  });
  console.log('5.1.2 vaults:', v512);

  // Also check syllabusTopicIndex for Ch 5
  console.log('\n--- syllabusTopicIndex for Ch 5 ---');
  const idxSnap = await db.collection('syllabusTopicIndex')
    .where('chapterNumber', '==', 5)
    .where('boardCode', '==', 'MH')
    .where('class', '==', '8')
    .where('subjectCode', '==', 'SCI')
    .get();
  idxSnap.docs.forEach(d => {
    const data = d.data();
    console.log(`- [${d.id}]: obj=${data.objectiveCount || 0}, subj=${data.subjectiveCount || 0}`);
  });
}
inspectCh5().catch(console.error);
