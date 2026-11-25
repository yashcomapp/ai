const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

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

const EXAM_ID = '028-MH-10-Mensuration,-7.1-7.2-241126';
const TOPIC_CODE = 'MH-10-MTH2-7-7.1.2';
const DISPUTED_INDICES = new Set([5, 6, 12]); // Q6, Q7, Q13 (0-based)
const DISPUTED_Q_IDS = new Set([
  'MH-10-MTH2-7-7.1.2-OSC-011',
  'MH-10-MTH2-7-7.1.2-OSC-005',
  'MH-10-MTH2-7-7.1.2-OSC-006'
]);

function getBloomWeight(bloomLevel) {
  const map = { Remember: 1, Understand: 2, Apply: 3, Analyze: 4, Evaluate: 5, Create: 6 };
  return (bloomLevel && map[bloomLevel]) ? map[bloomLevel] : 2;
}

async function run() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule Q) ===');
  await createPreMutationSnapshot(
    ['examAttempts', 'reviews', 'studentTopicMastery', 'exams'],
    'fix_exam028_q6_q7_q13_and_topic_7_1_2'
  );

  // Also backup all 80 questions in MH-10-MTH2-7-7.1.2
  const topicQSnap = await db.collection('questions').where('topicCode', '==', TOPIC_CODE).get();
  const qBackupPath = path.join(__dirname, '..', 'backups', 'snapshots', `questions_${TOPIC_CODE}_${Date.now()}.json`);
  fs.writeFileSync(
    qBackupPath,
    JSON.stringify(topicQSnap.docs.map(d => ({ id: d.id, data: d.data() })), null, 2),
    'utf-8'
  );
  console.log(`  ✓ Backed up ${topicQSnap.size} ${TOPIC_CODE} questions to ${path.basename(qBackupPath)}`);

  console.log('\n=== Step 2: Fix defective slant-height questions in MH-10-MTH2-7-7.1.2 ===');
  let qFixedCount = 0;
  let qBatch = db.batch();
  let batchOps = 0;

  for (const doc of topicQSnap.docs) {
    const q = doc.data();
    const txt = q.text || '';
    const m = txt.match(/r\s*=\s*(\d+)\\text\{ cm\}.*h\s*=\s*(\d+)\\text\{ cm\}/);
    if (!m) continue;

    const r = Number(m[1]);
    const h = Number(m[2]);
    const root = Math.sqrt(r * r + h * h);
    if (Number.isInteger(root)) continue;

    let updatePayload = null;
    if (r === 5 && h === 6) {
      updatePayload = {
        text: txt.replace('r = 5\\text{ cm}', 'r = 6\\text{ cm}').replace('h = 6\\text{ cm}', 'h = 8\\text{ cm}'),
        options: [
          { id: 'A', text: '\\(l = 14\\text{ cm}\\)', isCorrect: false },
          { id: 'B', text: '\\(l = 10\\text{ cm}\\)', isCorrect: true },
          { id: 'C', text: '\\(l = 12\\text{ cm}\\)', isCorrect: false },
          { id: 'D', text: '\\(l = 15\\text{ cm}\\)', isCorrect: false }
        ],
        correctAnswer: 'B',
        solution: '**Step 1: Conceptual Principle:** By Pythagoras Theorem in the cone cross-section: \\(l = \\sqrt{r^2 + h^2}\\).\n\n**Step 2: Detailed Calculation:** \\(l = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Slant height is \\(10\\text{ cm}\\).',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      };
    } else if (r === 7 && h === 8) {
      updatePayload = {
        text: txt.replace('r = 7\\text{ cm}', 'r = 8\\text{ cm}').replace('h = 8\\text{ cm}', 'h = 15\\text{ cm}'),
        options: [
          { id: 'A', text: '\\(l = 23\\text{ cm}\\)', isCorrect: false },
          { id: 'B', text: '\\(l = 19\\text{ cm}\\)', isCorrect: false },
          { id: 'C', text: '\\(l = 17\\text{ cm}\\)', isCorrect: true },
          { id: 'D', text: '\\(l = 25\\text{ cm}\\)', isCorrect: false }
        ],
        correctAnswer: 'C',
        solution: '**Step 1: Conceptual Principle:** By Pythagoras Theorem in the cone cross-section: \\(l = \\sqrt{r^2 + h^2}\\).\n\n**Step 2: Detailed Calculation:** \\(l = \\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = \\sqrt{289} = 17\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Slant height is \\(17\\text{ cm}\\).',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      };
    } else if (r === 9 && h === 10) {
      updatePayload = {
        text: txt.replace('r = 9\\text{ cm}', 'r = 5\\text{ cm}').replace('h = 10\\text{ cm}', 'h = 12\\text{ cm}'),
        correctAnswer: 'D',
        solution: '**Step 1: Conceptual Principle:** By Pythagoras Theorem in the cone cross-section: \\(l = \\sqrt{r^2 + h^2}\\).\n\n**Step 2: Detailed Calculation:** \\(l = \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Slant height is \\(13\\text{ cm}\\).',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      };
    }

    if (updatePayload) {
      qBatch.update(doc.ref, updatePayload);
      qFixedCount++;
      batchOps++;
      if (batchOps >= 400) {
        await qBatch.commit();
        qBatch = db.batch();
        batchOps = 0;
      }
    }
  }
  if (batchOps > 0) await qBatch.commit();
  console.log(`  ✓ Fixed ${qFixedCount} defective slant-height questions in ${TOPIC_CODE}.`);

  console.log('\n=== Step 3: Re-grade Exam 028 Attempts & Reviews (Exclude Q6, Q7, Q13 Pro-Rata) ===');
  const q2Doc = await db.collection('questions').doc('MH-10-MTH2-7-7.1.2-OSC-016').get();
  const q2Data = q2Doc.exists ? q2Doc.data() : {};
  const q2DiffWeight = q2Data.difficulty === 'easy' ? 1 : (q2Data.difficulty === 'hard' ? 3 : 2);
  const q2BloomWeight = getBloomWeight(q2Data.bloomLevel || 'Understand');
  const q2Weight = q2DiffWeight * q2BloomWeight;

  const examDoc = await db.collection('exams').doc(EXAM_ID).get();
  const examData = examDoc.data() || {};
  const posMarks = Number(examData.positiveMarks) || 4;
  const negMarks = Number(examData.negativeMarks) || 1;

  const attSnap = await db.collection('examAttempts').where('examId', '==', EXAM_ID).get();
  for (const attDoc of attSnap.docs) {
    const att = attDoc.data();
    if (att.status === 'precheck' || att.status === 'in-progress') {
      console.log(`  - Skipping ${attDoc.id} (status=${att.status})`);
      continue;
    }

    const revRef = db.collection('reviews').doc(attDoc.id);
    const revSnap = await revRef.get();
    if (!revSnap.exists) {
      console.log(`  - Skipping ${attDoc.id} (no review doc)`);
      continue;
    }
    const rev = revSnap.data();
    const qDetails = Array.isArray(rev.questionDetails) ? [...rev.questionDetails] : [];

    let newScore = 0;
    let newTotalMarks = 0;
    const newWrongAnswers = [];
    const newUnattempted = [];

    for (let i = 0; i < qDetails.length; i++) {
      const qd = { ...qDetails[i] };
      if (DISPUTED_INDICES.has(i)) {
        qd.userAnswer = '[Reported / Disputed]';
        qd.marks = 0;
        qd.isCorrect = false;
        qd.isDisputed = true;
        qDetails[i] = qd;
        continue;
      }
      const qMarks = Number(qd.marks) || posMarks;
      newTotalMarks += qMarks;
      if (!qd.isAttempted) {
        newUnattempted.push({
          qIndex: i,
          questionText: qd.questionText || '',
          correctAnswer: qd.correctAnswer || ''
        });
      } else if (qd.isCorrect) {
        newScore += qMarks;
      } else {
        newScore -= negMarks;
        newWrongAnswers.push({
          qIndex: i,
          questionText: qd.questionText || '',
          userAnswer: qd.userAnswer || '',
          correctAnswer: qd.correctAnswer || ''
        });
      }
    }

    const newPct = newTotalMarks > 0 ? parseFloat(((newScore / newTotalMarks) * 100).toFixed(1)) : 0;

    // Determine review status
    let newRevStatus = rev.status;
    if (newWrongAnswers.length === 0 && newUnattempted.length === 0 && rev.status === 'student_review') {
      let isAutonomous = false;
      if (att.studentId) {
        const uSnap = await db.collection('users').doc(att.studentId).get();
        if (uSnap.exists) isAutonomous = uSnap.data()?.autonomous === true;
      }
      newRevStatus = isAutonomous ? 'approved' : 'pending';
    }

    await attDoc.ref.update({
      score: newScore,
      totalMarks: newTotalMarks,
      percentage: newPct,
      regradedAt: admin.firestore.FieldValue.serverTimestamp(),
      regradeReason: 'Excluded defective Q6, Q7, Q13 pro-rata'
    });

    await revRef.update({
      score: newScore,
      totalMarks: newTotalMarks,
      percentage: newPct,
      wrongAnswers: newWrongAnswers,
      unattemptedQuestions: newUnattempted,
      questionDetails: qDetails,
      status: newRevStatus,
      regradedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    // Update studentTopicMastery for MH-10-MTH2-7-7.1.2
    const mRef = db.collection('studentTopicMastery').doc(`${att.studentCode}_${TOPIC_CODE}`);
    const mSnap = await mRef.get();
    if (mSnap.exists) {
      const m = mSnap.data();
      const filteredHistory = (m.questionHistory || []).filter(h => !DISPUTED_Q_IDS.has(h.questionId));
      // Check Q2 (index 1)
      const q2Detail = qDetails[1];
      const q2Passed = Boolean(q2Detail && q2Detail.isCorrect);
      if (filteredHistory.length <= 1) {
        await mRef.update({
          questionsAttempted: 1,
          examQuestionsAttempted: 1,
          questionsCorrect: q2Passed ? 1 : 0,
          questionsWrong: q2Passed ? 0 : 1,
          weightedPointsPossible: q2Weight,
          weightedPointsEarned: q2Passed ? q2Weight : 0,
          mastery: q2Passed ? 100 : 0,
          confidence: 1,
          questionHistory: filteredHistory,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
      }
    }

    console.log(
      `  ✓ ${att.studentName} (${att.studentCode}): ${att.score}/${att.totalMarks} (${att.percentage}%) -> ${newScore}/${newTotalMarks} (${newPct}%)`
    );
  }

  console.log('\n=== Remediation Complete ===');
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
