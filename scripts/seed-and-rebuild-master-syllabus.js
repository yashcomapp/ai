const path = require('path');
const fs = require('fs');

// 1. Load .env.local
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

// 2. Init Firebase Admin
const admin = require('firebase-admin');
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom';

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();
db.settings({ ignoreUndefinedProperties: true });

async function clearCollection(colName) {
  const snap = await db.collection(colName).get();
  if (snap.empty) return 0;
  
  let deleted = 0;
  const chunks = [];
  for (let i = 0; i < snap.docs.length; i += 450) {
    chunks.push(snap.docs.slice(i, i + 450));
  }

  for (const chunk of chunks) {
    const batch = db.batch();
    chunk.forEach(doc => batch.delete(doc.ref));
    await batch.commit();
    deleted += chunk.length;
  }
  return deleted;
}

async function seedMasterSyllabusAndReset() {
  console.log('======================================================');
  console.log('🚀 SEEDING 16 OFFICIAL MASTER SYLLABI & CLEAN SLATE RESET');
  console.log('======================================================\n');

  // Load TypeScript master data
  const tsContent = fs.readFileSync(path.join(__dirname, '..', 'src', 'lib', 'masterSyllabusData.ts'), 'utf8');
  // Transpile on the fly
  const ts = require('typescript');
  const jsCode = ts.transpileModule(tsContent, { compilerOptions: { module: ts.ModuleKind.CommonJS } }).outputText;
  
  const m = new module.constructor();
  m._compile(jsCode, 'masterSyllabusData.js');
  const MASTER_SYLLABUS_SUBJECTS = m.exports.MASTER_SYLLABUS_SUBJECTS;

  console.log(`Loaded ${MASTER_SYLLABUS_SUBJECTS.length} official textbook subjects from masterSyllabusData.ts\n`);

  // Step 1: Clear old syllabus and topic index
  console.log('1. Clearing old syllabus and syllabusTopicIndex...');
  const oldSyllabusCount = await clearCollection('syllabus');
  const oldIndexCount = await clearCollection('syllabusTopicIndex');
  console.log(`   Deleted ${oldSyllabusCount} old syllabus docs and ${oldIndexCount} old topic index docs.\n`);

  // Step 2: Seed new 16 syllabus documents & syllabusTopicIndex
  console.log('2. Writing 16 Official Master Syllabi into Firestore...');
  const syllabusSubjectsConfig = { subjects: {} };
  const subjectCodesMap = {};
  const boardCodesMap = {
    'CBSE': 'CBSE',
    'Maharashtra Board': 'MH',
    'MH': 'MH'
  };

  let totalTopicsIndexed = 0;
  const topicDocsBatch = [];

  for (const subj of MASTER_SYLLABUS_SUBJECTS) {
    const docRef = db.collection('syllabus').doc(subj.docId);
    await docRef.set({
      board: subj.board,
      boardCode: subj.boardCode,
      class: subj.class,
      subject: subj.subject,
      subjectCode: subj.subjectCode,
      chapters: subj.chapters,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    // Populate dynamic config maps
    if (!syllabusSubjectsConfig.subjects[subj.boardCode]) {
      syllabusSubjectsConfig.subjects[subj.boardCode] = {};
    }
    if (!syllabusSubjectsConfig.subjects[subj.boardCode][subj.class]) {
      syllabusSubjectsConfig.subjects[subj.boardCode][subj.class] = {};
    }
    syllabusSubjectsConfig.subjects[subj.boardCode][subj.class][subj.subject] = {
      subjectCode: subj.subjectCode,
      chapters: subj.chapters.map(ch => ({
        chapterNumber: ch.number,
        number: ch.number,
        chapterName: ch.name,
        name: ch.name,
        topics: ch.topics.map(top => ({
          topicNumber: top.number,
          number: top.number,
          topicName: top.name,
          name: top.name,
          topicCode: top.topicCode,
          subtopics: top.subtopics || [],
          practiceSet: top.practiceSet || '',
          theorems: top.theorems || [],
          problemSet: top.problemSet || ''
        }))
      }))
    };

    subjectCodesMap[subj.subject] = subj.subjectCode;

    // Flatten for syllabusTopicIndex
    subj.chapters.forEach(ch => {
      ch.topics.forEach(top => {
        topicDocsBatch.push({
          topicCode: top.topicCode,
          board: subj.board,
          boardCode: subj.boardCode,
          class: subj.class,
          subject: subj.subject,
          subjectCode: subj.subjectCode,
          chapterNumber: ch.number,
          chapterName: ch.name,
          topicNumber: top.number,
          topicName: top.name,
          subtopics: top.subtopics || [],
          practiceSet: top.practiceSet || '',
          theorems: top.theorems || [],
          problemSet: top.problemSet || ''
        });
      });
    });

    console.log(`   ✓ Seeded ${subj.docId.padEnd(35)} (${subj.chapters.length} chapters, ${subj.subjectCode})`);
  }

  // Step 3: Write syllabusTopicIndex in batches of 450
  console.log(`\n3. Building syllabusTopicIndex with ${topicDocsBatch.length} canonical topics...`);
  for (let i = 0; i < topicDocsBatch.length; i += 450) {
    const chunk = topicDocsBatch.slice(i, i + 450);
    const batch = db.batch();
    chunk.forEach(item => {
      const ref = db.collection('syllabusTopicIndex').doc(item.topicCode);
      batch.set(ref, {
        ...item,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    });
    await batch.commit();
    totalTopicsIndexed += chunk.length;
  }
  console.log(`   ✓ Indexed ${totalTopicsIndexed} canonical topics into syllabusTopicIndex.\n`);

  // Step 4: Update live Firestore config
  console.log('4. Syncing config documents (syllabusSubjects, subjectCodes, boardCodes)...');
  await db.collection('config').doc('syllabusSubjects').set(syllabusSubjectsConfig, { merge: true });
  await db.collection('config').doc('subjectCodes').set(subjectCodesMap, { merge: true });
  await db.collection('config').doc('boardCodes').set(boardCodesMap, { merge: true });
  console.log('   ✓ Config synced.\n');

  // Step 5: Reset transactional & operational test data (Preserving users & batches)
  console.log('5. Resetting transactional collections to fresh clean slate...');
  const collectionsToReset = [
    'examAttempts', 'reviews', 'subjectiveAttempts',
    'studentTopicMastery', 'parentReviews', 'assignments',
    'exams', 'subjectiveExams', 'practiceSubmissions',
    'questionRequests', 'noticeSeenLogs'
  ];

  for (const col of collectionsToReset) {
    const count = await clearCollection(col);
    console.log(`   ✓ Cleared ${col.padEnd(25)} : ${count} docs deleted`);
  }

  // Step 6: Verify users collection remains untouched
  const usersSnap = await db.collection('users').get();
  console.log(`\n✅ PROTECTED USERS VERIFICATION: ${usersSnap.docs.length} student/parent user accounts preserved.\n`);

  console.log('======================================================');
  console.log('🎉 MASTER CURRICULUM SEEDED & CLEAN SLATE COMPLETE!');
  console.log('======================================================\n');
}

seedMasterSyllabusAndReset()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Fatal seed error:', err);
    process.exit(1);
  });
