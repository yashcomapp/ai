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

async function createPreMutationSnapshot(collectionNames, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const backupDir = path.resolve(__dirname, '..', 'backups', 'snapshots', `sweep_autonomous_${timestamp}`);
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }

  const counts = {};
  for (const cName of collectionNames) {
    const snap = await db.collection(cName).get();
    const docs = snap.docs.map(d => ({ id: d.id, ...d.data() }));
    fs.writeFileSync(path.join(backupDir, `${cName}.json`), JSON.stringify(docs, null, 2), 'utf-8');
    counts[cName] = docs.length;
  }

  console.log(`Pre-mutation snapshot created at ${backupDir}:`, counts);
}

async function sweepAllAutonomousStudents() {
  console.log('--- STARTING AUTONOMOUS REVIEWS SWEEP ---');
  
  // 1. Snapshot targeted collections per Rule 1Q
  await createPreMutationSnapshot(['reviews', 'examAttempts', 'parentReviews'], 'sweep_all_autonomous_pending');

  // 2. Fetch all autonomous students
  const autoStudentsSnap = await db.collection('users')
    .where('role', '==', 'student')
    .where('autonomous', '==', true)
    .get();

  const autoStudents = autoStudentsSnap.docs.map(d => {
    const data = d.data();
    return {
      id: d.id,
      studentCode: data.studentCode,
      name: data.name || data.displayName,
      status: data.status || 'active'
    };
  }).filter(s => s.studentCode);

  console.log(`Found ${autoStudents.length} autonomous students in the system.`);

  let totalReviewsApproved = 0;
  let totalAttemptsApproved = 0;
  let totalParentReviewsApproved = 0;

  for (const student of autoStudents) {
    const { studentCode, name } = student;

    // A. Sweep 'reviews' collection where status in ['pending', 'student_review']
    const revSnap = await db.collection('reviews')
      .where('studentCode', '==', studentCode)
      .where('status', 'in', ['pending', 'student_review'])
      .get();

    if (!revSnap.empty) {
      const batch = db.batch();
      revSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'approved',
          updatedAt: new Date(),
          autoApprovedAutonomous: true,
          sweepTimestamp: new Date().toISOString()
        });
        totalReviewsApproved++;
      });
      await batch.commit();
      console.log(`[REVIEWS] Auto-approved ${revSnap.size} pending reviews for student: ${name} (${studentCode})`);
    }

    // B. Sweep 'examAttempts' collection where status == 'pending'
    const attSnap = await db.collection('examAttempts')
      .where('studentCode', '==', studentCode)
      .where('status', '==', 'pending')
      .get();

    if (!attSnap.empty) {
      const batch = db.batch();
      attSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'approved',
          updatedAt: new Date(),
          autoApprovedAutonomous: true,
          sweepTimestamp: new Date().toISOString()
        });
        totalAttemptsApproved++;
      });
      await batch.commit();
      console.log(`[ATTEMPTS] Auto-approved ${attSnap.size} pending attempts for student: ${name} (${studentCode})`);
    }

    // C. Sweep 'parentReviews' collection where status == 'pending'
    const pRevSnap = await db.collection('parentReviews')
      .where('studentCode', '==', studentCode)
      .where('status', '==', 'pending')
      .get();

    if (!pRevSnap.empty) {
      const batch = db.batch();
      pRevSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'approved',
          updatedAt: new Date(),
          autoApprovedAutonomous: true,
          sweepTimestamp: new Date().toISOString()
        });
        totalParentReviewsApproved++;
      });
      await batch.commit();
      console.log(`[PARENT_REVIEWS] Auto-approved ${pRevSnap.size} pending parentReviews for student: ${name} (${studentCode})`);
    }
  }

  console.log('\n--- SWEEP COMPLETE ---');
  console.log(`Total Reviews Approved: ${totalReviewsApproved}`);
  console.log(`Total Exam Attempts Approved: ${totalAttemptsApproved}`);
  console.log(`Total Parent Reviews Approved: ${totalParentReviewsApproved}`);
  console.log('All autonomous students are 100% clean and unblocked from taking exams.');
}

sweepAllAutonomousStudents().catch(console.error);
