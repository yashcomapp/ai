const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

async function audit() {
  console.log('=== CBSE 8 REALIGNMENT COMPREHENSIVE AUDIT ===\n');

  // 1. Syllabus documents
  const [s1, s2] = await Promise.all([
    db.collection('syllabus').doc('cbse_8_mgp1').get(),
    db.collection('syllabus').doc('cbse_8_mgp2').get()
  ]);
  console.log('📚 MGP1 Chapters:');
  s1.data().chapters.forEach(c => console.log(`   Ch.${c.number}: ${c.name} (Questions: ${c.objectiveCount})`));
  console.log(`   Total MGP1 Objective: ${s1.data().objectiveCount}`);

  console.log('\n📚 MGP2 Chapters:');
  s2.data().chapters.forEach(c => console.log(`   Ch.${c.number}: ${c.name} (Questions: ${c.objectiveCount})`));
  console.log(`   Total MGP2 Objective: ${s2.data().objectiveCount}`);

  // 2. Question counts in database
  const [mgp1Q, mgp2Q, oldCh5Q] = await Promise.all([
    db.collection('questions').where('subjectCode', '==', 'MGP1').get(),
    db.collection('questions').where('subjectCode', '==', 'MGP2').get(),
    db.collection('questions').where('topicCode', '>=', 'CBSE-8-MGP1-5-').where('topicCode', '<=', 'CBSE-8-MGP1-5-\uf8ff').get()
  ]);
  console.log('\n❓ Question Bank:');
  console.log(`   MGP1 Total in DB: ${mgp1Q.size}`);
  console.log(`   MGP2 Total in DB: ${mgp2Q.size}`);
  console.log(`   Stale MGP1 Ch.5 Questions: ${oldCh5Q.size} (Expected 0)`);

  // Check Ch4, Ch6, Ch7 questions
  const qByCh1 = {};
  mgp1Q.docs.forEach(d => {
    const ch = d.data().chapterNumber;
    qByCh1[ch] = (qByCh1[ch] || 0) + 1;
  });
  console.log('   MGP1 Questions by Chapter:', qByCh1);

  const qByCh2 = {};
  mgp2Q.docs.forEach(d => {
    const ch = d.data().chapterNumber;
    qByCh2[ch] = (qByCh2[ch] || 0) + 1;
  });
  console.log('   MGP2 Questions by Chapter:', qByCh2);

  // 3. Exams check
  console.log('\n📝 Exams Check:');
  const exIds = [
    '019-CBSE-8-Understanding-5.1-121026',
    '020-CBSE-8-Understanding-5.2-131026',
    '021-CBSE-8-Understanding-5.3-5.4-141026',
    '022-CBSE-8-Understanding-5.1-5.4-151026'
  ];
  for (const id of exIds) {
    const ex = await db.collection('exams').doc(id).get();
    const ed = ex.data();
    console.log(`   ${id}: chNum=${ed.chapterNumber}, ch=${ed.chapter}, qCount=${ed.questionCodes?.length}, firstQC=${ed.questionCodes?.[0]}`);
  }

  // 4. Sample Review check
  console.log('\n🔍 Reviews Check:');
  const rSnap = await db.collection('reviews').where('examId', '==', exIds[0]).limit(1).get();
  if (rSnap.size > 0) {
    const rd = rSnap.docs[0].data();
    console.log(`   Exam 019 review chapter: ${rd.chapter}`);
    console.log(`   Sample questionDetails[0].questionCode: ${rd.questionDetails?.[0]?.questionCode}`);
  }

  // 5. Topic index count
  const [idx1, idx2] = await Promise.all([
    db.collection('syllabusTopicIndex').where('subjectCode', '==', 'MGP1').get(),
    db.collection('syllabusTopicIndex').where('subjectCode', '==', 'MGP2').get()
  ]);
  console.log(`\n🗂️  Topic Index Entries: MGP1=${idx1.size}, MGP2=${idx2.size}`);

  console.log('\n=== AUDIT FINISHED ===');
}

audit().then(() => process.exit(0)).catch(e => {
  console.error(e);
  process.exit(1);
});
