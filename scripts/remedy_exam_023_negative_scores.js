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

async function fixExam023() {
  const examId = '023-MH-8-Inside the Atom-5.1-181126';
  console.log(`=== FIXING EXAM 023 NEGATIVE SCORES & STUDENT NAMES ===`);

  // 1. Load users to get canonical names
  const usersSnap = await db.collection('users').where('role', '==', 'student').get();
  const studentMap = new Map();
  usersSnap.docs.forEach(d => {
    const data = d.data();
    if (data.studentCode) {
      studentMap.set(data.studentCode, data.name || data.studentName || 'Student');
    }
  });

  // 2. Load reviews for exam 023
  const reviewsSnap = await db.collection('reviews').where('examId', '==', examId).get();
  console.log(`Found ${reviewsSnap.size} reviews to process.`);

  const updates = [];

  for (const doc of reviewsSnap.docs) {
    const r = doc.data();
    const studentCode = r.studentCode;
    const trueName = studentMap.get(studentCode) || r.studentName;
    const qDetails = r.questionDetails || [];

    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    qDetails.forEach(qd => {
      const isAtt = qd.isAttempted !== undefined
        ? Boolean(qd.isAttempted)
        : Boolean(qd.isCorrect || (qd.userAnswer && qd.userAnswer !== ''));
      if (!isAtt) {
        unattemptedCount++;
      } else if (qd.isCorrect) {
        correctCount++;
      } else {
        wrongCount++;
      }
    });

    const earned = correctCount * 4;
    const penalty = wrongCount * 1;
    // ALLOW NEGATIVE SCORE! NO Math.max(0, ...)
    const trueScore = earned - penalty;
    const totalMarks = r.totalMarks || 120;
    const truePercentage = parseFloat(((trueScore / totalMarks) * 100).toFixed(1));

    console.log(`Student: ${trueName} (${studentCode})`);
    console.log(`  Current DB: score=${r.score}, pct=${r.percentage}%, name="${r.studentName}"`);
    console.log(`  TRUE VALUE: score=${trueScore}, pct=${truePercentage}%, name="${trueName}" (Correct: ${correctCount}, Wrong: ${wrongCount}, Unatt: ${unattemptedCount})\n`);

    updates.push({
      reviewRef: doc.ref,
      attemptRef: db.collection('examAttempts').doc(doc.id),
      data: {
        score: trueScore,
        percentage: truePercentage,
        studentName: trueName,
        correctCount,
        wrongCount,
        unattemptedCount,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }
    });
  }

  // 3. Create Pre-Mutation Snapshot per Rule 2Q
  console.log('Creating Pre-Mutation Snapshot...');
  const now = new Date();
  const dateStr = now.toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });
  const backupFile = path.join(backupDir, `snapshot_${dateStr}_fix_exam_023_negative_scores.json`);

  const backupData = reviewsSnap.docs.map(d => ({ id: d.id, data: d.data() }));
  fs.writeFileSync(backupFile, JSON.stringify({
    timestamp: now.toISOString(),
    reason: 'Fix negative scores and restore student name for Exam 023',
    reviews: backupData
  }, null, 2));

  await db.collection('_systemBackups').doc(`backup_${dateStr}`).set({
    timestamp: admin.firestore.FieldValue.serverTimestamp(),
    reason: 'Fix negative scores and restore student name for Exam 023',
    backupFile: path.relative(path.join(__dirname, '..'), backupFile)
  });
  console.log(`Snapshot saved to ${backupFile}`);

  // 4. Commit updates
  const batch = db.batch();
  for (const u of updates) {
    batch.update(u.reviewRef, u.data);
    // Check if examAttempts doc exists before updating
    const attSnap = await u.attemptRef.get();
    if (attSnap.exists) {
      batch.update(u.attemptRef, {
        score: u.data.score,
        percentage: u.data.percentage,
        studentName: u.data.studentName,
        updatedAt: u.data.updatedAt
      });
    }
  }

  await batch.commit();
  console.log(`Successfully committed all updates to Firestore!`);
}

fixExam023().catch(console.error);
