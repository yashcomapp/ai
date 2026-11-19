// scripts/commit_mh8_ch5_questions.js
// Commits 140 gold-standard questions for MH-8-SCI Chapter 5 (Topics 5.2 through 5.6)
// Across all 3 vaults: exam (56 Qs), practice (56 Qs), foundation (28 Qs)

const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

// Load environment
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

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({ credential: admin.credential.cert(credential) });
  } else {
    admin.initializeApp();
  }
}

const db = admin.firestore();

// Load questions from modular parts
const { topic2Questions } = require('./mh8_ch5_topic2.js');
const { topic2Part2Questions } = require('./mh8_ch5_topic2_part2.js');
const { topic3Questions } = require('./mh8_ch5_topic3.js');
const { topic3Part2Questions } = require('./mh8_ch5_topic3_part2.js');
const { topic4Questions } = require('./mh8_ch5_topic4.js');
const { topic4Part2Questions } = require('./mh8_ch5_topic4_part2.js');
const { topic5Questions } = require('./mh8_ch5_topic5.js');
const { topic5Part2Questions } = require('./mh8_ch5_topic5_part2.js');
const { topic6Questions } = require('./mh8_ch5_topic6.js');
const { topic6Part2Questions } = require('./mh8_ch5_topic6_part2.js');

const allQuestions = [
  ...topic2Questions,
  ...topic2Part2Questions,
  ...topic3Questions,
  ...topic3Part2Questions,
  ...topic4Questions,
  ...topic4Part2Questions,
  ...topic5Questions,
  ...topic5Part2Questions,
  ...topic6Questions,
  ...topic6Part2Questions
];

async function main() {
  console.log(`=== Step 1: Pre-Mutation Snapshot for 140 questions ===`);
  const snapshotRes = await createPreMutationSnapshot(
    ['questions', 'syllabus', 'syllabusTopicIndex'],
    'mh8_sci_ch5_remaining_topics_140q_3vaults'
  );
  console.log('Snapshot successfully created:', snapshotRes.snapshotPath);

  console.log(`\n=== Step 2: Committing ${allQuestions.length} Questions to Firestore ===`);
  // Firestore batches have a 500 operation limit; 140 questions easily fit in one or two batches
  const batch = db.batch();
  allQuestions.forEach(q => {
    const docRef = db.collection('questions').doc(q.questionCode);
    batch.set(docRef, {
      ...q,
      isEnhanced: true,
      status: 'active',
      isLegacy: false,
      isDisputed: false,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });

  await batch.commit();
  console.log(`Committed ${allQuestions.length} questions to 'questions' collection.`);

  console.log(`\n=== Step 3: Synchronizing Syllabus Document (mh_8_sci) & syllabusTopicIndex ===`);
  const sylRef = db.collection('syllabus').doc('mh_8_sci');
  const sylSnap = await sylRef.get();
  if (!sylSnap.exists) {
    throw new Error('Syllabus doc mh_8_sci not found!');
  }
  const sylData = sylSnap.data();

  // Compute live subtopic and topic counts from all questions in Chapter 5
  const qSnap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '8')
    .where('subjectCode', '==', 'SCI')
    .where('chapterNumber', '==', '5')
    .get();

  console.log(`Total live questions in MH-8-SCI Chapter 5 now: ${qSnap.size}`);

  // Tally counts by subtopic and by vault
  const subtopicCounts = {};
  const topicCounts = {};
  const chVaultCounts = {
    exam: { objective: 0, subjective: 0 },
    practice: { objective: 0, subjective: 0 },
    foundation: { objective: 0, subjective: 0 }
  };

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const stCode = q.subtopicCode || q.topicCode;
    const parentCode = q.parentTopicCode || (stCode ? stCode.split('.').slice(0, 2).join('.') : '');
    const v = q.vault || 'exam';
    const isSubj = q.type && q.type.startsWith('S');

    // Ch vault count
    if (chVaultCounts[v]) {
      if (isSubj) chVaultCounts[v].subjective++;
      else chVaultCounts[v].objective++;
    }

    // Subtopic count
    if (stCode) {
      if (!subtopicCounts[stCode]) {
        subtopicCounts[stCode] = {
          totalObj: 0, totalSubj: 0,
          vaultCounts: {
            exam: { objective: 0, subjective: 0 },
            practice: { objective: 0, subjective: 0 },
            foundation: { objective: 0, subjective: 0 }
          }
        };
      }
      if (isSubj) {
        subtopicCounts[stCode].totalSubj++;
        if (subtopicCounts[stCode].vaultCounts[v]) subtopicCounts[stCode].vaultCounts[v].subjective++;
      } else {
        subtopicCounts[stCode].totalObj++;
        if (subtopicCounts[stCode].vaultCounts[v]) subtopicCounts[stCode].vaultCounts[v].objective++;
      }
    }

    // Topic count
    if (parentCode) {
      if (!topicCounts[parentCode]) {
        topicCounts[parentCode] = {
          totalObj: 0, totalSubj: 0,
          vaultCounts: {
            exam: { objective: 0, subjective: 0 },
            practice: { objective: 0, subjective: 0 },
            foundation: { objective: 0, subjective: 0 }
          }
        };
      }
      if (isSubj) {
        topicCounts[parentCode].totalSubj++;
        if (topicCounts[parentCode].vaultCounts[v]) topicCounts[parentCode].vaultCounts[v].subjective++;
      } else {
        topicCounts[parentCode].totalObj++;
        if (topicCounts[parentCode].vaultCounts[v]) topicCounts[parentCode].vaultCounts[v].objective++;
      }
    }
  });

  // Update syllabus document chapters array
  const updatedChapters = sylData.chapters.map(ch => {
    if (String(ch.number) !== '5') return ch;

    let chObjTotal = 0;
    let chSubjTotal = 0;

    const updatedTopics = (ch.topics || []).map(t => {
      const tCode = t.topicCode;
      let topObj = 0;
      let topSubj = 0;
      const topVault = {
        exam: { objective: 0, subjective: 0 },
        practice: { objective: 0, subjective: 0 },
        foundation: { objective: 0, subjective: 0 }
      };

      const updatedSubtopics = (t.subtopics || []).map(st => {
        const stCode = st.topicCode;
        const stStats = subtopicCounts[stCode] || {
          totalObj: 0, totalSubj: 0,
          vaultCounts: { exam: { objective: 0, subjective: 0 }, practice: { objective: 0, subjective: 0 }, foundation: { objective: 0, subjective: 0 } }
        };

        topObj += stStats.totalObj;
        topSubj += stStats.totalSubj;
        ['exam', 'practice', 'foundation'].forEach(v => {
          topVault[v].objective += stStats.vaultCounts[v].objective;
          topVault[v].subjective += stStats.vaultCounts[v].subjective;
        });

        return {
          ...st,
          objectiveCount: stStats.totalObj,
          subjectiveCount: stStats.totalSubj,
          vaultCounts: stStats.vaultCounts
        };
      });

      chObjTotal += topObj;
      chSubjTotal += topSubj;

      return {
        ...t,
        objectiveCount: topObj,
        subjectiveCount: topSubj,
        vaultCounts: topVault,
        subtopics: updatedSubtopics
      };
    });

    return {
      ...ch,
      objectiveCount: chObjTotal,
      subjectiveCount: chSubjTotal,
      vaultCounts: chVaultCounts,
      topics: updatedTopics
    };
  });

  await sylRef.update({
    chapters: updatedChapters,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });
  console.log('Updated syllabus document mh_8_sci with enriched chapter 5 topic/subtopic counts.');

  // Update syllabusTopicIndex documents
  console.log(`\n=== Step 4: Updating syllabusTopicIndex for all Chapter 5 Topics & Subtopics ===`);
  const idxBatch = db.batch();

  Object.entries(subtopicCounts).forEach(([code, stats]) => {
    const docRef = db.collection('syllabusTopicIndex').doc(code);
    idxBatch.set(docRef, {
      objectiveCount: stats.totalObj,
      subjectiveCount: stats.totalSubj,
      vaultCounts: stats.vaultCounts,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });

  Object.entries(topicCounts).forEach(([code, stats]) => {
    const docRef = db.collection('syllabusTopicIndex').doc(code);
    idxBatch.set(docRef, {
      objectiveCount: stats.totalObj,
      subjectiveCount: stats.totalSubj,
      vaultCounts: stats.vaultCounts,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });

  await idxBatch.commit();
  console.log('Updated syllabusTopicIndex for all Chapter 5 topics and subtopics.');
  console.log('Ch 5 Vault Totals:', chVaultCounts);
  console.log('✅ ALL 140 QUESTIONS COMMITTED AND SYNCED SUCCESSFULLY!');
}

main().catch(err => {
  console.error('Fatal error committing questions:', err);
  process.exit(1);
});
