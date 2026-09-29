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

const { MASTER_SYLLABUS_SUBJECTS } = require('./curriculum_data');

async function updateSyllabusInFirestore() {
  console.log('======================================================');
  console.log('📚 UPDATING SYLLABUS, TOPIC INDEX & CONFIG IN FIRESTORE');
  console.log('======================================================\n');

  console.log(`Loaded ${MASTER_SYLLABUS_SUBJECTS.length} subjects from curriculum_data.\n`);

  // Step 1: Pre-mutation snapshot
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots', `pre_syllabus_sync_${timestamp}`);
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }
  
  const currentSyllabus = await db.collection('syllabus').get();
  const currentSyllabusData = {};
  currentSyllabus.forEach(doc => { currentSyllabusData[doc.id] = doc.data(); });
  fs.writeFileSync(path.join(backupDir, 'syllabus.json'), JSON.stringify(currentSyllabusData, null, 2), 'utf8');
  console.log(`✓ Created backup snapshot of ${currentSyllabus.size} syllabus docs at ${backupDir}\n`);

  // Step 2: Write all subjects into 'syllabus' collection
  const syllabusSubjectsConfig = { subjects: {} };
  const subjectCodesMap = {};
  const boardCodesMap = {
    'CBSE': 'CBSE',
    'Maharashtra Board': 'MH',
    'MH': 'MH'
  };

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

    console.log(`   ✓ Seeded ${subj.docId.padEnd(30)} | ${subj.boardCode} Class ${subj.class} - ${subj.subject} (${subj.subjectCode}) [${subj.chapters.length} chapters]`);
  }

  // Step 3: Write syllabusTopicIndex in batches of 450
  console.log(`\nWriting syllabusTopicIndex with ${topicDocsBatch.length} canonical topics...`);
  let totalTopicsIndexed = 0;
  for (let i = 0; i < topicDocsBatch.length; i += 450) {
    const chunk = topicDocsBatch.slice(i, i + 450);
    const batch = db.batch();
    chunk.forEach(item => {
      const ref = db.collection('syllabusTopicIndex').doc(item.topicCode);
      batch.set(ref, {
        ...item,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
    });
    await batch.commit();
    totalTopicsIndexed += chunk.length;
  }
  console.log(`   ✓ Indexed ${totalTopicsIndexed} canonical topics into syllabusTopicIndex.\n`);

  // Step 4: Sync config documents
  console.log('Syncing config documents (syllabusSubjects, subjectCodes, boardCodes)...');
  await db.collection('config').doc('syllabusSubjects').set(syllabusSubjectsConfig, { merge: true });
  await db.collection('config').doc('subjectCodes').set(subjectCodesMap, { merge: true });
  await db.collection('config').doc('boardCodes').set(boardCodesMap, { merge: true });
  console.log('   ✓ Config collections synced successfully.\n');

  console.log('======================================================');
  console.log('🎉 SYLLABUS UPDATE COMPLETED SUCCESSFULLY!');
  console.log('======================================================\n');
}

updateSyllabusInFirestore()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Fatal error updating syllabus:', err);
    process.exit(1);
  });
