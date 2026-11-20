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
if (sa) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
}
const db = admin.firestore();

// Pre-mutation snapshot (Rule 1Q)
async function createSnapshot(collections, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const snapshotDir = path.resolve(__dirname, '..', 'backups', 'snapshots', `remedy_issues_${timestamp}`);
  if (!fs.existsSync(snapshotDir)) {
    fs.mkdirSync(snapshotDir, { recursive: true });
  }

  const counts = {};
  for (const cName of collections) {
    console.log(`Backing up collection '${cName}'...`);
    const snap = await db.collection(cName).get();
    const docs = snap.docs.map(d => ({ id: d.id, data: d.data() }));
    counts[cName] = docs.length;
    fs.writeFileSync(path.join(snapshotDir, `${cName}.json`), JSON.stringify(docs, null, 2), 'utf-8');
    console.log(`  -> Saved ${docs.length} docs from '${cName}'`);
  }

  const manifest = {
    snapshotId: `remedy_issues_${timestamp}`,
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

async function execute() {
  console.log('=== Step 1: Pre-mutation Snapshot ===');
  await createSnapshot(['questions', 'reviews', 'examAttempts'], 'fix_q29_otf_and_difficulties');

  console.log('=== Step 2: Fixing Question 29 (MH-9-SCIT-1-1.5-ONE-001) ===');
  // Check both MH-9-SCIT-1-1.5-ONE-001 and MH-9-SCIT-1-1.5.1-ONE-001
  const q29Ids = ['MH-9-SCIT-1-1.5-ONE-001', 'MH-9-SCIT-1-1.5.1-ONE-001'];
  for (const id of q29Ids) {
    const docRef = db.collection('questions').doc(id);
    const snap = await docRef.get();
    if (snap.exists) {
      await docRef.update({
        correctAnswer: 'B',
        numericalValue: 2,
        difficulty: 'medium',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      console.log(`Updated Q29 (${id}): correctAnswer='B', numericalValue=2, difficulty='medium'`);
    }
  }

  console.log('\n=== Step 3: Rescoring Exam 023 (Class 9) Attempts & Reviews ===');
  const examId = '023-MH-9-Laws of Motion-1.2-1.5-191126';
  const reviewsSnap = await db.collection('reviews').where('examId', '==', examId).get();
  console.log(`Found ${reviewsSnap.size} reviews to rescore.`);

  for (const revDoc of reviewsSnap.docs) {
    const r = revDoc.data();
    const details = [...(r.questionDetails || [])];
    
    // Q29 is index 28 (or questionCode MH-9-SCIT-1-1.5.1-ONE-001)
    const q29Idx = details.findIndex(qd => 
      qd.questionCode === 'MH-9-SCIT-1-1.5.1-ONE-001' || 
      (qd.questionText && qd.questionText.includes('rotates in a circle of radius'))
    );

    if (q29Idx !== -1) {
      const qd = details[q29Idx];
      const uAns = String(qd.userAnswer || '').trim();
      const isAttempted = qd.isAttempted !== false && uAns !== '';
      
      // Correct answer is "2" or Option "B"
      const isCorrect = isAttempted && (uAns === '2' || uAns === 'B');
      details[q29Idx] = {
        ...qd,
        correctAnswer: '2',
        isAttempted,
        isCorrect,
        marks: 4
      };
    }

    // Recalculate overall score for this review
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    details.forEach(qd => {
      const isAttempted = qd.isAttempted !== false && qd.userAnswer !== undefined && qd.userAnswer !== null && qd.userAnswer !== '';
      if (!isAttempted) {
        unattemptedCount++;
      } else if (qd.isCorrect) {
        correctCount++;
      } else {
        wrongCount++;
      }
    });

    const earnedMarks = correctCount * 4;
    const penaltyLost = wrongCount * 1;
    const newScore = earnedMarks - penaltyLost;
    const totalMarks = r.totalMarks || (details.length * 4);
    const newPercentage = parseFloat(((newScore / totalMarks) * 100).toFixed(1));

    console.log(`  Rescored ${r.studentName} (${r.studentCode}): Old Score: ${r.score} -> New Score: ${newScore}/${totalMarks} (${newPercentage}%) [${correctCount}C, ${wrongCount}W, ${unattemptedCount}U]`);

    await revDoc.ref.update({
      questionDetails: details,
      score: newScore,
      percentage: newPercentage,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    // Also update examAttempts
    const attSnap = await db.collection('examAttempts').doc(revDoc.id).get();
    if (attSnap.exists) {
      await attSnap.ref.update({
        score: newScore,
        percentage: newPercentage,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    }
  }

  console.log('\n=== Step 4: Fixing All 126 Non-Standard Difficulty Questions ===');
  const allQSnap = await db.collection('questions').get();
  let diffFixedCount = 0;
  let batch = db.batch();
  let count = 0;

  for (const doc of allQSnap.docs) {
    const q = doc.data();
    const rawDiff = String(q.difficulty || '').trim().toLowerCase();
    if (!['easy', 'medium', 'hard'].includes(rawDiff)) {
      // Determine appropriate difficulty
      let targetDiff = 'medium';
      if (q.bloomLevel) {
        const bl = String(q.bloomLevel).toLowerCase();
        if (bl === 'remember' || bl === 'understand') targetDiff = 'easy';
        else if (bl === 'apply') targetDiff = 'medium';
        else if (bl === 'analyze' || bl === 'evaluate' || bl === 'create') targetDiff = 'hard';
      }
      batch.update(doc.ref, {
        difficulty: targetDiff,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      diffFixedCount++;
      count++;
      if (count % 400 === 0) {
        await batch.commit();
        batch = db.batch();
        console.log(`  Committed ${count} difficulty fixes...`);
      }
    }
  }
  if (count % 400 !== 0) {
    await batch.commit();
  }
  console.log(`✓ Fixed difficulty for all ${diffFixedCount} questions.`);

  console.log('\n=== Step 5: Fixing All 570 Mismatched OTF Questions (including Rhombus) ===');
  let otfFixedCount = 0;
  batch = db.batch();
  count = 0;

  for (const doc of allQSnap.docs) {
    const q = doc.data();
    if ((q.type || '').toUpperCase() === 'OTF') {
      const opts = Array.isArray(q.options) ? q.options : [];
      const cAns = String(q.correctAnswer || '').trim();
      const cAnsList = Array.isArray(q.correctAnswers) ? q.correctAnswers : [];

      if (opts.length === 2 && cAnsList.length > 0) {
        const opt0 = typeof opts[0] === 'object' ? (opts[0].text || opts[0].value) : String(opts[0]);
        const opt1 = typeof opts[1] === 'object' ? (opts[1].text || opts[1].value) : String(opts[1]);
        const target = String(cAnsList[0]).trim().toLowerCase();
        let correctLetter = '';
        if (opt0.toLowerCase() === target) correctLetter = 'A';
        else if (opt1.toLowerCase() === target) correctLetter = 'B';

        if (correctLetter && cAns !== correctLetter && ['A', 'B'].includes(cAns.toUpperCase())) {
          batch.update(doc.ref, {
            correctAnswer: correctLetter,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          });
          otfFixedCount++;
          count++;
          if (count % 400 === 0) {
            await batch.commit();
            batch = db.batch();
            console.log(`  Committed ${count} OTF fixes...`);
          }
        }
      }
    }
  }
  if (count % 400 !== 0) {
    await batch.commit();
  }
  console.log(`✓ Fixed ${otfFixedCount} OTF questions to match correct truth option letter.`);

  console.log('\n=== All Database Remedies Completed Successfully! ===');
}

execute().catch(console.error);
