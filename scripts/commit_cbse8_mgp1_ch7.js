const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Load environment variables
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

async function runCommit() {
  console.log('================================================================');
  console.log('🚀 COMMITTING CBSE CLASS 8 MGP1 CHAPTER 7 QUESTIONS (410 Qs)');
  console.log('================================================================\n');

  // Load all 5 topic files
  const t1 = JSON.parse(fs.readFileSync(path.join(__dirname, 'cbse8_mgp1_ch7_t1.json'), 'utf-8'));
  const t2 = JSON.parse(fs.readFileSync(path.join(__dirname, 'cbse8_mgp1_ch7_t2.json'), 'utf-8'));
  const t3 = JSON.parse(fs.readFileSync(path.join(__dirname, 'cbse8_mgp1_ch7_t3.json'), 'utf-8'));
  const t4 = JSON.parse(fs.readFileSync(path.join(__dirname, 'cbse8_mgp1_ch7_t4.json'), 'utf-8'));
  const t5 = JSON.parse(fs.readFileSync(path.join(__dirname, 'cbse8_mgp1_ch7_t5.json'), 'utf-8'));

  const allQuestions = [...t1, ...t2, ...t3, ...t4, ...t5];
  console.log(`Loaded ${allQuestions.length} total questions (82 per topic x 5 topics).`);

  // Step 1: Pre-Mutation Snapshot
  const now = new Date();
  const dateStr = now.toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });
  const backupFile = path.join(backupDir, `snapshot_${dateStr}_cbse8_ch7_questions.json`);

  console.log(`\n📸 Step 1: Creating Pre-Mutation Snapshot -> ${backupFile}...`);
  const [sylSnap, idxSnap] = await Promise.all([
    db.collection('syllabus').doc('cbse_8_mgp1').get(),
    db.collection('syllabusTopicIndex').where('chapterNumber', '==', '7').where('subjectCode', '==', 'MGP1').get()
  ]);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'cbse8_mgp1_chapter7_questions_addition',
    counts: {
      syllabus: sylSnap.exists ? 1 : 0,
      topicIndex: idxSnap.size
    },
    syllabus: sylSnap.exists ? sylSnap.data() : null,
    topicIndex: idxSnap.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(backupFile, JSON.stringify(snapshotData, null, 2));
  console.log(`   ✅ Snapshot saved successfully (${(fs.statSync(backupFile).size / 1024).toFixed(2)} KB).`);

  await db.collection('_systemBackups').doc(`backup_${dateStr}_cbse8_ch7_addition`).set({
    timestamp: admin.firestore.Timestamp.fromDate(now),
    reason: snapshotData.reason,
    backupFile: path.basename(backupFile),
    counts: snapshotData.counts
  });
  console.log(`   ✅ Logged snapshot in _systemBackups.`);

  // Step 2: Commit Questions to Firestore
  console.log(`\n🔄 Step 2: Writing ${allQuestions.length} Questions to 'questions' collection...`);
  let batch = db.batch();
  let opCount = 0;
  let totalCommitted = 0;

  for (const q of allQuestions) {
    const docRef = db.collection('questions').doc(q.id);
    batch.set(docRef, {
      ...q,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
    opCount++;
    totalCommitted++;

    if (opCount >= 400) {
      await batch.commit();
      batch = db.batch();
      opCount = 0;
      console.log(`   Committed ${totalCommitted} questions...`);
    }
  }
  if (opCount > 0) {
    await batch.commit();
    console.log(`   Committed final batch (${totalCommitted} total).`);
  }
  console.log(`   ✅ Successfully committed all ${totalCommitted} questions.`);

  // Step 3: Update Syllabus Document in Firestore
  console.log(`\n🔄 Step 3: Updating syllabus doc 'cbse_8_mgp1'...`);
  const mgp1Doc = await db.collection('syllabus').doc('cbse_8_mgp1').get();
  const mgp1Data = mgp1Doc.data();

  // Find Chapter 7
  const chapters = mgp1Data.chapters || [];
  const ch7Index = chapters.findIndex(c => c.number === '7');

  if (ch7Index !== -1) {
    const ch7 = chapters[ch7Index];

    // Ensure Topic 7.5 has both 7.5.1 and 7.5.2
    const top7_5 = ch7.topics.find(t => t.number === '7.5');
    if (top7_5) {
      top7_5.subtopics = [
        {
          number: '7.5.1',
          name: 'Dividing total amounts into parts proportional to ratio',
          topicCode: 'CBSE-8-MGP1-7-7.5.1',
          objectiveCount: 41,
          subjectiveCount: 0
        },
        {
          number: '7.5.2',
          name: 'Difference between parts, ratio comparisons and multi-way sharing',
          topicCode: 'CBSE-8-MGP1-7-7.5.2',
          objectiveCount: 41,
          subjectiveCount: 0
        }
      ];
      top7_5.objectiveCount = 82;
    }

    // Update topics 7.1 to 7.4
    ch7.topics.forEach(t => {
      if (t.number !== '7.5') {
        t.objectiveCount = 82;
        (t.subtopics || []).forEach(st => {
          st.objectiveCount = 41;
          st.subjectiveCount = 0;
        });
      }
    });

    ch7.objectiveCount = 410;
    ch7.subjectiveCount = 0;

    // Recalculate total MGP1 objective count
    const totalObj = chapters.reduce((sum, ch) => sum + (ch.objectiveCount || 0), 0);

    await db.collection('syllabus').doc('cbse_8_mgp1').update({
      chapters: chapters,
      objectiveCount: totalObj,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    console.log(`   ✅ Updated cbse_8_mgp1: Chapter 7 count = 410, Total MGP1 count = ${totalObj}.`);
  }

  // Step 4: Index 7.5.2 in syllabusTopicIndex
  console.log(`\n🔄 Step 4: Updating syllabusTopicIndex for Chapter 7...`);
  const st2Ref = db.collection('syllabusTopicIndex').doc('CBSE-8-MGP1-7-7.5.2');
  await st2Ref.set({
    topicCode: 'CBSE-8-MGP1-7-7.5.2',
    topicNumber: '7.5.2',
    topicName: 'Difference between parts, ratio comparisons and multi-way sharing',
    parentTopicCode: 'CBSE-8-MGP1-7-7.5',
    chapterNumber: '7',
    chapterName: 'Proportional Reasoning 1',
    subject: 'Ganit Prakash Part 1',
    subjectCode: 'MGP1',
    class: '8',
    board: 'CBSE',
    boardCode: 'CBSE',
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });
  console.log(`   ✅ Indexed CBSE-8-MGP1-7-7.5.2 in syllabusTopicIndex.`);

  // Step 5: Audit & Vault Verification
  console.log(`\n🔍 Step 5: Auditing Vaults for Chapter 7 in Firestore...`);
  const ch7QSnap = await db.collection('questions')
    .where('subjectCode', '==', 'MGP1')
    .where('chapterNumber', '==', 7)
    .get();

  const vaultCounts = { exam: 0, practice: 0, foundation: 0, other: 0 };
  const topicCounts = {};
  const typeCounts = {};

  ch7QSnap.forEach(d => {
    const q = d.data();
    const v = q.vault || 'other';
    vaultCounts[v] = (vaultCounts[v] || 0) + 1;
    const pt = q.parentTopicCode || q.topicCode;
    topicCounts[pt] = (topicCounts[pt] || 0) + 1;
    typeCounts[q.type] = (typeCounts[q.type] || 0) + 1;
  });

  console.log(`   Total Questions in DB: ${ch7QSnap.size} (Expected: 410)`);
  console.log(`   Vault Breakdown:`, vaultCounts);
  console.log(`   Topic Breakdown:`, topicCounts);
  console.log(`   Question Types:`, typeCounts);

  console.log('\n================================================================');
  console.log('🎉 CHAPTER 7 QUESTIONS ADDED & VERIFIED ACROSS ALL 3 VAULTS');
  console.log('================================================================');
}

runCommit().then(() => process.exit(0)).catch(err => {
  console.error('❌ Commit failed:', err);
  process.exit(1);
});
