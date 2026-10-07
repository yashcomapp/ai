const fs = require('fs');
const path = require('path');
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

// Rule Q: Pre-Mutation Snapshot Engine
async function createPreMutationSnapshot(collections, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}`;
  const snapshotsDir = path.resolve(process.cwd(), 'backups', 'snapshots');

  if (!fs.existsSync(snapshotsDir)) {
    fs.mkdirSync(snapshotsDir, { recursive: true });
  }

  const snapshotData = {};
  const collectionCounts = {};

  for (const colName of collections) {
    const snap = await db.collection(colName).get();
    const docs = snap.docs.map(doc => ({ _docId: doc.id, ...doc.data() }));
    snapshotData[colName] = docs;
    collectionCounts[colName] = docs.length;
  }

  const snapshotFileName = `${snapshotId}.json`;
  const snapshotFilePath = path.join(snapshotsDir, snapshotFileName);
  fs.writeFileSync(snapshotFilePath, JSON.stringify(snapshotData, null, 2), 'utf8');

  const metadata = {
    snapshotId,
    timestamp: new Date().toISOString(),
    reason,
    collections: collectionCounts,
    snapshotFilePath
  };

  try {
    await db.collection('_systemBackups').doc(snapshotId).set(metadata);
  } catch (err) {
    console.warn('Could not write snapshot record to _systemBackups:', err);
  }

  console.log(`Pre-mutation snapshot created: ${snapshotId}`, collectionCounts);
  return metadata;
}

async function run() {
  const targetExamIds = [
    '016-MH-8-Congruence of-13.3-061026',
    '016-MH-9-Financial Planning-6.1-061026',
    '016-MH-10-Space Missions-10.1-10.2-061026'
  ];

  console.log('=== Cleaning up stale attempts for reassigned exams ===');
  await createPreMutationSnapshot(
    ['examAttempts', 'reviews', 'evaluations', 'examAbsenceReasons'],
    'Pre-mutation snapshot before cleaning stale attempts for reassigned exams'
  );

  for (const examId of targetExamIds) {
    console.log(`\nProcessing exam: ${examId}`);
    const [attSnap, revSnap, evalSnap, absSnap] = await Promise.all([
      db.collection('examAttempts').where('examId', '==', examId).get(),
      db.collection('reviews').where('examId', '==', examId).get(),
      db.collection('evaluations').where('examId', '==', examId).get(),
      db.collection('examAbsenceReasons').where('examId', '==', examId).get()
    ]);

    const affectedStudents = new Set();
    const deleteBatch = db.batch();
    let count = 0;

    attSnap.docs.forEach(doc => {
      const data = doc.data();
      const sc = data.studentCode || (doc.id.includes('_') ? doc.id.split('_').slice(1).join('_') : '');
      if (sc) affectedStudents.add(sc);
      deleteBatch.delete(doc.ref);
      count++;
    });

    revSnap.docs.forEach(doc => {
      const data = doc.data();
      const sc = data.studentCode || (doc.id.includes('_') ? doc.id.split('_').slice(1).join('_') : '');
      if (sc) affectedStudents.add(sc);
      deleteBatch.delete(doc.ref);
      count++;
    });

    evalSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentCode) affectedStudents.add(data.studentCode);
      deleteBatch.delete(doc.ref);
      count++;
    });

    absSnap.docs.forEach(doc => {
      deleteBatch.delete(doc.ref);
      count++;
    });

    // Also delete any composite doc IDs
    for (const sc of Array.from(affectedStudents)) {
      deleteBatch.delete(db.collection('examAttempts').doc(`${examId}_${sc}`));
      deleteBatch.delete(db.collection('reviews').doc(`${examId}_${sc}`));
      deleteBatch.delete(db.collection('examAbsenceReasons').doc(`${sc}_${examId}`));
    }

    if (count > 0 || affectedStudents.size > 0) {
      await deleteBatch.commit();
      console.log(`Deleted ${count} records across collections for exam ${examId}. Affected students: ${affectedStudents.size}`);
    } else {
      console.log(`No records found for exam ${examId}.`);
    }

    // Verify remaining count
    const verifyAtt = await db.collection('examAttempts').where('examId', '==', examId).get();
    console.log(`Remaining attempts in Firestore for ${examId}: ${verifyAtt.size}`);
  }

  console.log('\n=== ALL TARGET EXAMS CLEANED SUCCESSFULLY ===');
}

run().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error during cleanup:', err);
  process.exit(1);
});
