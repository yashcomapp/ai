const path = require('path');
const fs = require('fs');

// 1. Load environment variables from .env.local
const envPath = path.join(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
if (!admin.apps.length) admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

const targetExamConfigs = [
  {
    examId: '016-MH-8-Congruence of-13.3-061026',
    duration: 27,
    batchName: 'Class 8th Foundation'
  },
  {
    examId: '016-MH-9-Financial Planning-6.1-061026',
    duration: 30,
    batchName: 'Class 9th Foundation'
  },
  {
    examId: '016-MH-10-Space Missions-10.1-10.2-061026',
    duration: 30,
    batchName: 'Class 10 State Board'
  }
];

async function run() {
  console.log('--- Step 1: Creating Pre-Mutation Snapshot per Rule 2.Q ---');
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}`;
  const snapshotsDir = path.resolve(process.cwd(), 'backups', 'snapshots');
  if (!fs.existsSync(snapshotsDir)) fs.mkdirSync(snapshotsDir, { recursive: true });

  const collectionsToSnapshot = ['batchAssignments', 'examAttempts', 'examAbsenceReasons', 'parentReviews'];
  const snapshotData = {};
  const collectionCounts = {};

  for (const colName of collectionsToSnapshot) {
    const snap = await db.collection(colName).get();
    const docs = snap.docs.map(doc => ({ _docId: doc.id, ...doc.data() }));
    snapshotData[colName] = docs;
    collectionCounts[colName] = docs.length;
  }

  const snapshotFilePath = path.join(snapshotsDir, `${snapshotId}.json`);
  fs.writeFileSync(snapshotFilePath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`Snapshot saved to ${snapshotFilePath}`);

  const metadata = {
    snapshotId,
    timestamp: new Date().toISOString(),
    reason: 'Reassign 3 exams to 2026-10-08 06:00 IST and clean slate past attempts/absences',
    collections: collectionCounts,
    snapshotFilePath
  };
  try {
    await db.collection('_systemBackups').doc(snapshotId).set(metadata);
  } catch (e) {
    console.warn('Warning saving backup doc:', e.message);
  }

  console.log('\n--- Step 2: Purging Past Data Points for Target Exams ---');
  const targetIds = targetExamConfigs.map(c => c.examId);
  const affectedStudentCodes = new Set();

  for (const examId of targetIds) {
    console.log(`Processing clean slate for [${examId}]...`);

    // A. examAttempts
    const attSnap = await db.collection('examAttempts').where('examId', '==', examId).get();
    for (const doc of attSnap.docs) {
      if (doc.data().studentCode) affectedStudentCodes.add(doc.data().studentCode);
      await doc.ref.delete();
      console.log(`  Deleted examAttempt: ${doc.id}`);
    }

    // B. attempts
    const oldAttSnap = await db.collection('attempts').where('examId', '==', examId).get();
    for (const doc of oldAttSnap.docs) {
      if (doc.data().studentCode) affectedStudentCodes.add(doc.data().studentCode);
      await doc.ref.delete();
      console.log(`  Deleted attempt: ${doc.id}`);
    }

    // C. subjectiveAttempts
    const subAttSnap = await db.collection('subjectiveAttempts').where('examId', '==', examId).get();
    for (const doc of subAttSnap.docs) {
      if (doc.data().studentCode) affectedStudentCodes.add(doc.data().studentCode);
      await doc.ref.delete();
      console.log(`  Deleted subjectiveAttempt: ${doc.id}`);
    }

    // D. reviews & subjectiveReviews
    const revSnap = await db.collection('reviews').where('examId', '==', examId).get();
    for (const doc of revSnap.docs) {
      await doc.ref.delete();
      console.log(`  Deleted review: ${doc.id}`);
    }
    const subRevSnap = await db.collection('subjectiveReviews').where('examId', '==', examId).get();
    for (const doc of subRevSnap.docs) {
      await doc.ref.delete();
      console.log(`  Deleted subjectiveReview: ${doc.id}`);
    }

    // E. evaluations
    const evalSnap = await db.collection('evaluations').where('examId', '==', examId).get();
    for (const doc of evalSnap.docs) {
      await doc.ref.delete();
      console.log(`  Deleted evaluation: ${doc.id}`);
    }

    // F. examAbsenceReasons
    const absSnap = await db.collection('examAbsenceReasons').where('examId', '==', examId).get();
    for (const doc of absSnap.docs) {
      if (doc.data().studentCode) affectedStudentCodes.add(doc.data().studentCode);
      await doc.ref.delete();
      console.log(`  Deleted examAbsenceReason: ${doc.id}`);
    }

    // Scan examAbsenceReasons by docId ending with examId
    const allAbsSnap = await db.collection('examAbsenceReasons').get();
    for (const doc of allAbsSnap.docs) {
      if (doc.id.includes(examId)) {
        await doc.ref.delete();
        console.log(`  Deleted examAbsenceReason by ID match: ${doc.id}`);
      }
    }

    // G. parentReviews
    const prSnap = await db.collection('parentReviews').where('examId', '==', examId).get();
    for (const doc of prSnap.docs) {
      await doc.ref.delete();
      console.log(`  Deleted parentReview: ${doc.id}`);
    }
    const allPrSnap = await db.collection('parentReviews').get();
    for (const doc of allPrSnap.docs) {
      if (doc.id.includes(examId) || doc.data().examId === examId) {
        await doc.ref.delete();
        console.log(`  Deleted parentReview by ID/field match: ${doc.id}`);
      }
    }

    // H. liveExamSessions
    const liveSnap = await db.collection('liveExamSessions').where('examId', '==', examId).get();
    for (const doc of liveSnap.docs) {
      await doc.ref.delete();
      console.log(`  Deleted liveExamSession: ${doc.id}`);
    }
  }

  console.log('\n--- Step 3: Reassigning to Tomorrow Morning 06:00 AM IST (2026-10-08) ---');
  // 6:00 AM IST on 2026-10-08
  const startAt = new Date('2026-10-08T06:00:00+05:30');

  for (const cfg of targetExamConfigs) {
    const endAt = new Date(startAt.getTime() + cfg.duration * 60 * 1000);
    console.log(`Updating batch assignment for [${cfg.examId}]...`);
    console.log(`  Start IST: ${startAt.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}`);
    console.log(`  End IST:   ${endAt.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}`);

    const baSnap = await db.collection('batchAssignments').where('examId', '==', cfg.examId).get();
    if (baSnap.empty) {
      console.warn(`  Warning: No batchAssignment found for ${cfg.examId}`);
    } else {
      for (const doc of baSnap.docs) {
        await doc.ref.update({
          startAt: admin.firestore.Timestamp.fromDate(startAt),
          endAt: admin.firestore.Timestamp.fromDate(endAt),
          openMode: 'scheduled',
          status: 'active',
          lateEntryRestriction: false,
          attemptLimit: 1,
          examDuration: cfg.duration,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        console.log(`  Updated batchAssignment doc [${doc.id}] successfully.`);
      }
    }
  }

  console.log('\n--- Step 4: Verification of Assignments and Clean Counts ---');
  for (const cfg of targetExamConfigs) {
    const ba = await db.collection('batchAssignments').where('examId', '==', cfg.examId).get();
    const att = await db.collection('examAttempts').where('examId', '==', cfg.examId).get();
    const abs = await db.collection('examAbsenceReasons').where('examId', '==', cfg.examId).get();
    const pr = await db.collection('parentReviews').where('examId', '==', cfg.examId).get();

    console.log(`Exam [${cfg.examId}]:`);
    console.log(`  batchAssignments count: ${ba.size}`);
    ba.docs.forEach(d => {
      const dat = d.data();
      console.log(`    Status: ${dat.status}, Mode: ${dat.openMode}, Start: ${dat.startAt?.toDate().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}, End: ${dat.endAt?.toDate().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}`);
    });
    console.log(`  examAttempts count: ${att.size}`);
    console.log(`  examAbsenceReasons count: ${abs.size}`);
    console.log(`  parentReviews count: ${pr.size}`);
  }

  console.log('\n--- Done! ---');
}

run().then(() => process.exit(0)).catch(err => {
  console.error('Error during execution:', err);
  process.exit(1);
});
