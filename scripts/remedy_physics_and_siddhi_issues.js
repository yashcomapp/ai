const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const admin = require('firebase-admin');

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
    admin.initializeApp({ projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}

const db = admin.firestore();

function getDateKeyIST(date = new Date()) {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(date);
}

async function run() {
  console.log('=== STEP 1: CREATING TARGETED PRE-MUTATION SNAPSHOT ===');
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

  const now = new Date();
  const dateKey = getDateKeyIST(now);
  const timeStr = now.toTimeString().split(' ')[0].replace(/:/g, '-');
  const snapshotId = `snapshot_${dateKey}_${timeStr}_fix_physics_contradictions_and_siddhi_review`;
  const filePath = path.join(targetDir, `${snapshotId}.json`);

  // Target 1: MH-9-SCIT-1 questions
  const qSnap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-9-SCIT-1-')
    .where('topicCode', '<=', 'MH-9-SCIT-1-\uf8ff')
    .get();

  // Target 2: Siddhi Dangra's review
  const revSnap = await db.collection('reviews').doc('024-MH-9-Laws of Motion-1.6-201126_ST-2026-000026').get();
  
  // Target 3: Siddhi Dangra's examAttempt
  const attSnap = await db.collection('examAttempts').doc('024-MH-9-Laws of Motion-1.6-201126_ST-2026-000026').get();

  const snapshotData = {
    metadata: {
      snapshotId,
      timestampIST: `${dateKey} ${timeStr}`,
      createdAtISO: now.toISOString(),
      reason: 'fix_physics_contradictions_and_siddhi_review',
      collections: {
        questions: qSnap.size,
        reviews: revSnap.exists ? 1 : 0,
        examAttempts: attSnap.exists ? 1 : 0
      },
      totalDocuments: qSnap.size + (revSnap.exists ? 1 : 0) + (attSnap.exists ? 1 : 0),
      filePath
    },
    data: {
      questions: qSnap.docs.map(d => ({ id: d.id, data: d.data() })),
      reviews: revSnap.exists ? [{ id: revSnap.id, data: revSnap.data() }] : [],
      examAttempts: attSnap.exists ? [{ id: attSnap.id, data: attSnap.data() }] : []
    }
  };

  fs.writeFileSync(filePath, JSON.stringify(snapshotData, null, 2), 'utf8');
  await db.collection('_systemBackups').doc(snapshotId).set({
    ...snapshotData.metadata,
    createdAt: now
  });
  console.log(`✓ Targeted snapshot created at ${filePath} (${snapshotData.metadata.totalDocuments} docs) and recorded in _systemBackups!`);

  console.log('\n=== STEP 2: FIXING MH-9-SCIT-1-1.6-OMC-002 (Action-Reaction Third Law) ===');
  const q15Ref = db.collection('questions').doc('MH-9-SCIT-1-1.6-OMC-002');
  const q15Snap = await q15Ref.get();
  if (q15Snap.exists) {
    const q15Data = q15Snap.data();
    const updatedOptions = (q15Data.options || []).map((opt, i) => {
      // Option A: Equal in magnitude -> true
      // Option B: Opposite in direction -> true
      // Option C: 1-second delay -> false
      // Option D: Act on two different bodies and never cancel -> true
      if (i === 0) return { ...opt, isCorrect: true };
      if (i === 1) return { ...opt, isCorrect: true };
      if (i === 2) return { ...opt, isCorrect: false };
      if (i === 3) return { ...opt, isCorrect: true };
      return opt;
    });

    await q15Ref.update({
      options: updatedOptions,
      correctAnswer: 'A, B, D',
      correctAnswers: ['A', 'B', 'D'],
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    console.log('Successfully updated MH-9-SCIT-1-1.6-OMC-002 to A, B, D!');
  }

  console.log('\n=== STEP 3: HARMONIZING 124 CONTRADICTORY BOILERPLATE SOLUTIONS IN MH-9-SCIT-1 ===');
  let fixedCount = 0;
  const batch = db.batch();
  let batchOps = 0;

  for (const doc of qSnap.docs) {
    const q = doc.data();
    const cAns = q.correctAnswer || q.answer;
    let sol = q.solution || q.explanation || '';

    if (!sol || !cAns || typeof cAns !== 'string') continue;

    // Check for "Correct Choice is (X)" or "Correct Option is (X)" or "Correct choice is (X)"
    const match = sol.match(/Correct\s+(?:Choice|Option|Answer)\s+is\s+[:\(]?\s*([A-D])\)?/i);
    if (match) {
      const solLetter = match[1].toUpperCase();
      if (/^[A-D]$/i.test(cAns) && cAns.toUpperCase() !== solLetter) {
        // Replace with the true correct answer letter
        const updatedSol = sol.replace(
          /Correct\s+(?:Choice|Option|Answer)\s+is\s+[:\(]?\s*[A-D]\)?/i,
          `Correct Choice is (${cAns.toUpperCase()})`
        );
        batch.update(doc.ref, {
          solution: updatedSol,
          explanation: updatedSol,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        batchOps++;
        fixedCount++;

        if (batchOps >= 400) {
          await batch.commit();
          batchOps = 0;
        }
      }
    }
  }

  if (batchOps > 0) {
    await batch.commit();
  }
  console.log(`Successfully harmonized ${fixedCount} solutions in MH-9-SCIT-1!`);

  console.log('\n=== STEP 4: RETROACTIVELY CORRECTING SIDDHI DANGRA REVIEW (Exam 024) ===');
  const reviewRef = db.collection('reviews').doc('024-MH-9-Laws of Motion-1.6-201126_ST-2026-000026');
  const rDoc = await reviewRef.get();

  if (rDoc.exists) {
    const rd = rDoc.data();
    const qDetails = rd.questionDetails || [];

    // Helper to get all options text for an array of correct letters
    const resolveFullOptionText = (options, letters) => {
      if (!Array.isArray(options) || !Array.isArray(letters)) return '';
      return letters.map(l => {
        const idx = l.charCodeAt(0) - 65;
        const opt = options[idx];
        return (opt && typeof opt === 'object') ? (opt.text || opt.value || l) : String(opt || l);
      }).join(', ');
    };

    // Fix Q15 (Index 14) -> Mark isCorrect: true, marks: 4
    if (qDetails[14]) {
      const q15Options = [
        { text: "Action and reaction are always equal in magnitude", isCorrect: true },
        { text: "Action and reaction are always opposite in direction", isCorrect: true },
        { text: "Action occurs first and reaction occurs with a 1-second delay", isCorrect: false },
        { text: "They act on two different bodies and never cancel each other out", isCorrect: true }
      ];
      qDetails[14].isCorrect = true;
      qDetails[14].marks = 4;
      qDetails[14].correctAnswer = resolveFullOptionText(q15Options, ['A', 'B', 'D']);
      qDetails[14].options = q15Options;
      qDetails[14].solution = "Action and reaction are simultaneous, instantaneous, and act on distinct objects.";
    }

    // Fix Q24 (Index 23) -> Hydrate full correct answer text
    if (qDetails[23]) {
      const q24Options = [
        { text: "A stationary book remains at rest unless picked up", isCorrect: true },
        { text: "Mud leaves a rotating bicycle wheel along the tangent", isCorrect: true },
        { text: "A heavier object always hits the ground before a lighter object in vacuum", isCorrect: false },
        { text: "Passengers lurch sideways when a car takes a sharp turn (inertia of direction)", isCorrect: true }
      ];
      qDetails[23].correctAnswer = resolveFullOptionText(q24Options, ['A', 'B', 'D']);
      qDetails[23].options = q24Options;
      qDetails[23].solution = "Inertia of rest, direction, and motion derive from Newton's first law; free fall in vacuum is mass-independent.";
    }

    // Fix Q9 (Index 8) -> Hydrate full correct answer text
    if (qDetails[8]) {
      const q9Options = [
        { text: "Inertial mass of the object (at everyday speeds)", isCorrect: false },
        { text: "Velocity magnitude (speed)", isCorrect: true },
        { text: "Momentum", isCorrect: true },
        { text: "Direction of motion", isCorrect: true }
      ];
      qDetails[8].correctAnswer = resolveFullOptionText(q9Options, ['B', 'C', 'D']);
      qDetails[8].options = q9Options;
      qDetails[8].solution = "Force changes velocity, direction, and momentum, leaving classical mass invariant.";
    }

    // Fix Q30 (Index 29) -> Hydrate full correct answer text
    if (qDetails[29]) {
      const q30Options = [
        { text: "Collision of two billiard balls", isCorrect: true },
        { text: "Rocket propulsion in deep space", isCorrect: true },
        { text: "Free fall of a stone in vacuum", isCorrect: false },
        { text: "Recoil of a shotgun upon firing", isCorrect: true }
      ];
      qDetails[29].correctAnswer = resolveFullOptionText(q30Options, ['A', 'B', 'D']);
      qDetails[29].options = q30Options;
      qDetails[29].solution = "Recoil, rockets, and collisions demonstrate momentum conservation in isolated systems.";
    }

    // Recalculate score:
    // 22 correct questions out of 30 (+4 marks each = 88 marks).
    // 8 wrong questions (-1 mark each = -8 marks).
    // Total score = 80 / 120 (67%).
    const newScore = 80;
    const newPercentage = 67;

    await reviewRef.update({
      questionDetails: qDetails,
      score: newScore,
      percentage: newPercentage,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    // Also update examAttempts
    const attemptRef = db.collection('examAttempts').doc('024-MH-9-Laws of Motion-1.6-201126_ST-2026-000026');
    await attemptRef.update({
      score: newScore,
      percentage: newPercentage,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    console.log(`Successfully updated Siddhi Dangra Exam 024 review: score updated from 75 to ${newScore} (${newPercentage}%)!`);
  }

  console.log('\n=== ALL TASKS COMPLETED SUCCESSFULLY ===');
}

run().catch(console.error);
