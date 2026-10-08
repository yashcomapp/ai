import * as fs from 'fs';
import * as path from 'path';

// 1. Load .env.local into process.env before anything else
const envContent = fs.readFileSync('.env.local', 'utf-8');
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      process.env[k] = v;
    }
  }
});

import * as admin from 'firebase-admin';
import { preprocessMathText } from '../src/lib/questionTypes';

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

// 2. Mandatory Pre-Mutation Automated Snapshot Engine (Rule 1Q)
async function createPreMutationSnapshot(collectionNames: string[], reason: string) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const snapshotDir = path.resolve(__dirname, '..', 'backups', 'snapshots', `insert_missing_questions_${timestamp}`);
  if (!fs.existsSync(snapshotDir)) {
    fs.mkdirSync(snapshotDir, { recursive: true });
  }

  const counts: Record<string, number> = {};
  for (const cName of collectionNames) {
    console.log(`Backing up collection '${cName}'...`);
    const snap = await db.collection(cName).get();
    const docs = snap.docs.map(d => ({ id: d.id, data: d.data() }));
    counts[cName] = docs.length;
    fs.writeFileSync(path.join(snapshotDir, `${cName}.json`), JSON.stringify(docs, null, 2), 'utf-8');
    console.log(`  -> Saved ${docs.length} docs from '${cName}'`);
  }

  const manifest = {
    snapshotId: `insert_missing_questions_${timestamp}`,
    timestamp: new Date().toISOString(),
    reason,
    counts,
    snapshotDir
  };
  fs.writeFileSync(path.join(snapshotDir, 'manifest.json'), JSON.stringify(manifest, null, 2), 'utf-8');
  await db.collection('_systemBackups').doc(manifest.snapshotId).set(manifest, { merge: true });
  console.log(`Pre-mutation snapshot atomic write complete: ${manifest.snapshotId}\n`);
  return manifest;
}

async function main() {
  console.log('--- STARTING MISSING QUESTIONS INSERTION ---');

  // Load the 75 pasted questions
  const allPasted = JSON.parse(fs.readFileSync('temp_pasted_questions_clean.json', 'utf8'));
  console.log(`Loaded ${allPasted.length} total questions from pasted array.`);

  // Load existing questions in MH-9-MTH1-4
  const existingSnap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-MTH1-4')
    .where('topicCode', '<=', 'MH-9-MTH1-4\uf8ff')
    .get();

  console.log(`Currently stored in MH-9-MTH1-4: ${existingSnap.size} questions.`);
  const existingDocMap = new Map<string, any>();
  const normalize = (t: string) => (t || '').trim().replace(/\s+/g, ' ').toLowerCase();

  existingSnap.forEach(d => {
    existingDocMap.set(normalize(d.data().text), d.data());
  });

  // Extract the exact 28 missing questions:
  // Q46 (OSC), Q49 (OSC), Q50 (ONE) from CTX-002 -> MH-9-MTH1-4-4.1.2
  // Q51 to Q75 (all 25 questions) from CTX-003 -> MH-9-MTH1-4-4.1.3
  const missing412 = [allPasted[45], allPasted[48], allPasted[49]]; // indices 46, 49, 50 (0-indexed: 45, 48, 49)
  const missing413 = allPasted.slice(50, 75); // indices 51..75 (0-indexed: 50..74)

  console.log(`Targeting ${missing412.length} questions for MH-9-MTH1-4-4.1.2 ("Order of terms")`);
  console.log(`Targeting ${missing413.length} questions for MH-9-MTH1-4-4.1.3 ("Multiplying/dividing terms by non-zero scalar")`);
  const totalToInsert = missing412.length + missing413.length;
  console.log(`Total questions to insert: ${totalToInsert}`);

  // Create Snapshot before mutating
  await createPreMutationSnapshot(['questions', 'questionCounters', 'syllabusTopicIndex'], 'Insert 28 dropped questions for MH-9-MTH1-4.1.2 and 4.1.3');

  const batch = db.batch();
  const counterUpdates: Record<string, number> = {};

  // Process 4.1.2 (Q46, Q49, Q50)
  const seq412: Record<string, number> = {
    OSC: 15,
    ONE: 14
  };

  const topicName412 = 'Order of terms';
  const topicCode412 = 'MH-9-MTH1-4-4.1.2';

  for (const q of missing412) {
    const qType = q.type;
    const seq = seq412[qType]++;
    counterUpdates[`${topicCode412}-${qType}`] = seq + 1;
    const qCode = `${topicCode412}-${qType}-${String(seq).padStart(3, '0')}`;

    let options = (q.options || []).map((o: any) => preprocessMathText(String(o).trim()));
    let correctAnswer = preprocessMathText(String(q.correctAnswer || '').trim());
    let correctAnswers = (q.correctAnswers || []).map((a: any) => preprocessMathText(String(a).trim()));
    if (!correctAnswer && correctAnswers.length > 0) correctAnswer = correctAnswers[0];
    if (correctAnswer && correctAnswers.length === 0) correctAnswers = [correctAnswer];

    const docData: any = {
      questionCode: qCode,
      type: qType,
      text: preprocessMathText(q.text),
      options,
      correctAnswer,
      correctAnswers,
      assertion: preprocessMathText(q.assertion || ''),
      reason: preprocessMathText(q.reason || ''),
      solution: preprocessMathText(q.solution || ''),
      difficulty: q.difficulty || 'medium',
      bloomLevel: q.bloomLevel || 'Remember',
      board: 'Maharashtra Board',
      boardCode: 'MH',
      class: '9',
      subject: 'Mathematics Part - 1 (Algebra)',
      subjectCode: 'MTH1',
      chapterNumber: '4',
      topicNumber: '4.1.2',
      topicCode: topicCode412,
      topic: topicName412,
      topicName: topicName412,
      conceptTag: q.conceptTag || topicName412,
      marks: 4,
      vault: q.vault || 'practice',
      examCategory: q.examCategory || 'standard',
      isTheorem: false,
      isSolvedExample: false,
      requiresFigure: false,
      imageUrl: '',
      keywords: [],
      textbookPracticeSet: '',
      textbookProblemSet: '',
      timesUsed: 0,
      usedInClassroomTest: true,
      createdBy: 'admin@yashcom.com',
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    console.log(`Preparing: ${qCode} - ${docData.text.slice(0, 50)}`);
    batch.set(db.collection('questions').doc(qCode), docData);
  }

  // Process 4.1.3 (Q51 through Q75)
  const seq413: Record<string, number> = {
    OSC: 1,
    OMC: 1,
    OTF: 1,
    OAR: 1,
    ONE: 1
  };

  const topicName413 = 'Multiplying/dividing terms by non-zero scalar';
  const topicCode413 = 'MH-9-MTH1-4-4.1.3';

  for (const q of missing413) {
    const qType = q.type;
    const seq = seq413[qType]++;
    counterUpdates[`${topicCode413}-${qType}`] = seq + 1;
    const qCode = `${topicCode413}-${qType}-${String(seq).padStart(3, '0')}`;

    let options = (q.options || []).map((o: any) => preprocessMathText(String(o).trim()));
    let correctAnswer = preprocessMathText(String(q.correctAnswer || '').trim());
    let correctAnswers = (q.correctAnswers || []).map((a: any) => preprocessMathText(String(a).trim()));
    if (!correctAnswer && correctAnswers.length > 0) correctAnswer = correctAnswers[0];
    if (correctAnswer && correctAnswers.length === 0) correctAnswers = [correctAnswer];

    const docData: any = {
      questionCode: qCode,
      type: qType,
      text: preprocessMathText(q.text),
      options,
      correctAnswer,
      correctAnswers,
      assertion: preprocessMathText(q.assertion || ''),
      reason: preprocessMathText(q.reason || ''),
      solution: preprocessMathText(q.solution || ''),
      difficulty: q.difficulty || 'medium',
      bloomLevel: q.bloomLevel || 'Remember',
      board: 'Maharashtra Board',
      boardCode: 'MH',
      class: '9',
      subject: 'Mathematics Part - 1 (Algebra)',
      subjectCode: 'MTH1',
      chapterNumber: '4',
      topicNumber: '4.1.3',
      topicCode: topicCode413,
      topic: topicName413,
      topicName: topicName413,
      conceptTag: q.conceptTag || topicName413,
      marks: 4,
      vault: q.vault || 'practice',
      examCategory: q.examCategory || 'standard',
      isTheorem: false,
      isSolvedExample: false,
      requiresFigure: false,
      imageUrl: '',
      keywords: [],
      textbookPracticeSet: '',
      textbookProblemSet: '',
      timesUsed: 0,
      usedInClassroomTest: true,
      createdBy: 'admin@yashcom.com',
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    console.log(`Preparing: ${qCode} - ${docData.text.slice(0, 50)}`);
    batch.set(db.collection('questions').doc(qCode), docData);
  }

  // Update question counters in batch
  for (const [cid, nextSeq] of Object.entries(counterUpdates)) {
    console.log(`Updating counter ${cid} -> nextSequence: ${nextSeq}`);
    batch.set(db.collection('questionCounters').doc(cid), { nextSequence: nextSeq }, { merge: true });
  }

  // Commit batch write
  console.log('Committing batch to Firestore...');
  await batch.commit();
  console.log('Batch commit successfully completed!');

  // Dynamically import syllabusSync after Firebase Admin is initialized
  console.log('Synchronizing topic counts to syllabus...');
  const { syncTopicCountsToSyllabus } = await import('../src/lib/syllabusSync');
  await syncTopicCountsToSyllabus([topicCode412, topicCode413]);
  console.log('Syllabus count synchronization completed!');

  // Final verification
  const finalSnap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-MTH1-4')
    .where('topicCode', '<=', 'MH-9-MTH1-4\uf8ff')
    .get();

  const finalCounts: Record<string, number> = {};
  finalSnap.forEach(d => {
    const tc = d.data().topicCode;
    finalCounts[tc] = (finalCounts[tc] || 0) + 1;
  });

  console.log('\n--- FINAL VERIFICATION ---');
  console.log('Total questions now in MH-9-MTH1-4:', finalSnap.size);
  console.log('Breakdown by topic:', finalCounts);

  const idx411 = await db.collection('syllabusTopicIndex').doc('MH-9-MTH1-4-4.1.1').get();
  const idx412 = await db.collection('syllabusTopicIndex').doc('MH-9-MTH1-4-4.1.2').get();
  const idx413 = await db.collection('syllabusTopicIndex').doc('MH-9-MTH1-4-4.1.3').get();

  console.log('\nsyllabusTopicIndex counts:');
  console.log('4.1.1 ("Units consistency"):', idx411.data()?.objectiveCount, 'questions');
  console.log('4.1.2 ("Order of terms"):', idx412.data()?.objectiveCount, 'questions');
  console.log('4.1.3 ("Multiplying/dividing terms by non-zero scalar"):', idx413.data()?.objectiveCount, 'questions');

  process.exit(0);
}

main().catch(err => {
  console.error('Fatal error during insertion:', err);
  process.exit(1);
});
