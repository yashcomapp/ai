const path = require('path');
const fs = require('fs');

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

const admin = require('firebase-admin');
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || "ai-yashcom";

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
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();

// Evaluation logic
function normalizeOptionAnswer(value, options) {
  if (!value && value !== 0) return '';
  value = String(value).trim();

  const prefixMatch = value.match(/^(?:option\s+)?\(?([A-Z])\)?[:.\-\s]?$/i);
  if (prefixMatch) {
    const letter = prefixMatch[1].toUpperCase();
    if (!options || !options.length) return letter;
    const idx = letter.charCodeAt(0) - 65;
    if (idx >= 0 && idx < options.length) return letter;
  }

  if (Array.isArray(options) && options.length) {
    const norm = (s) => String(s ?? '').trim().toLowerCase();
    const cleanNorm = (s) => String(s ?? '').toLowerCase().replace(/\\\(|\\\)|\\\[|\\\]|\$+/g, '').replace(/[^\w\d]/g, '').trim();
    const valClean = cleanNorm(value);

    const idx = options.findIndex(opt => {
      const optText = (opt && typeof opt === 'object') ? (opt.text ?? opt.value ?? '') : opt;
      if (norm(optText) === norm(value)) return true;
      if (valClean && cleanNorm(optText) === valClean) return true;
      return false;
    });
    if (idx !== -1) return String.fromCharCode(65 + idx);
  }

  const match = value.match(/^([A-D])/i);
  if (match) {
    return match[1].toUpperCase();
  }

  return value.toUpperCase();
}

function classifyAssertionReasonAnswer(value) {
  if (!value) return '';
  let v = String(value).trim();
  const letterMatch = v.match(/^([A-D])$/i);
  if (letterMatch) return letterMatch[1].toUpperCase();

  v = v.replace(/^option[:\s]*/i, '').toLowerCase();
  const mentionsBoth = /\bboth\b/.test(v);
  const notCorrectExplanation = /not\s+(the\s+)?correct explanation/.test(v);
  const isCorrectExplanation = /correct explanation/.test(v) && !notCorrectExplanation;
  const assertionFalse = /assertion[^.]*\bfalse\b/.test(v) || /\ba\s+is\s+false\b/.test(v);
  const reasonFalse = /reason[^.]*\bfalse\b/.test(v) || /\br\s+is\s+false\b/.test(v);
  const assertionTrue = /assertion[^.]*\btrue\b/.test(v) || /\ba\s+is\s+true\b/.test(v);
  const reasonTrue = /reason[^.]*\btrue\b/.test(v) || /\br\s+is\s+true\b/.test(v);

  if (mentionsBoth && isCorrectExplanation) return 'A';
  if (mentionsBoth && notCorrectExplanation) return 'B';
  if (assertionTrue && reasonFalse) return 'C';
  if (assertionFalse && reasonTrue) return 'D';

  const fallback = v.match(/^([a-d])/i);
  return fallback ? fallback[1].toUpperCase() : v.toUpperCase();
}

function evaluateQuestionAnswer(type, userAnswer, correctAnswer, options) {
  if (Array.isArray(options) && options.length > 0 && type !== 'multiple_mcq' && type !== 'multi_mcq' && type !== 'true_false' && type !== 'assertion_reason') {
    const userNorm = normalizeOptionAnswer(userAnswer, options);
    const correctNorm = normalizeOptionAnswer(correctAnswer, options);
    if (userNorm && correctNorm && userNorm === correctNorm) return true;
  }

  if (type === 'single_mcq' || type === 'mcq') {
    return normalizeOptionAnswer(userAnswer, options) === normalizeOptionAnswer(correctAnswer, options);
  }

  if (type === 'multiple_mcq' || type === 'multi_mcq') {
    let userArr = [];
    try {
      userArr = JSON.parse(userAnswer);
    } catch {
      userArr = userAnswer;
    }
    if (!Array.isArray(userArr)) {
      userArr = userArr ? [userArr] : [];
    }

    let correctArr = Array.isArray(correctAnswer)
      ? correctAnswer
      : (correctAnswer ? [correctAnswer] : []);

    userArr = Array.from(new Set(userArr.map((v) => normalizeOptionAnswer(v, options)))).sort();
    correctArr = Array.from(new Set(correctArr.map((v) => normalizeOptionAnswer(v, options)))).sort();

    return JSON.stringify(userArr) === JSON.stringify(correctArr);
  }

  if (type === 'true_false') {
    const userNorm = String(userAnswer || '').trim().toLowerCase();
    const correctNorm = String(correctAnswer || '').trim().toLowerCase();
    return userNorm === correctNorm;
  }

  if (type === 'assertion_reason') {
    return classifyAssertionReasonAnswer(userAnswer) === classifyAssertionReasonAnswer(correctAnswer);
  }

  if (type === 'fill_blanks' || type === 'fill_blank') {
    return String(userAnswer || '').trim().toLowerCase() === String(correctAnswer || '').trim().toLowerCase();
  }

  if (type === 'numerical' || type === 'numerical_short' || type === 'numerical_long') {
    if (Array.isArray(options) && options.length > 0) {
      if (normalizeOptionAnswer(userAnswer, options) === normalizeOptionAnswer(correctAnswer, options)) {
        return true;
      }
    }
    const u = parseFloat(userAnswer);
    const c = parseFloat(correctAnswer);
    return !isNaN(u) && !isNaN(c) && Math.abs(u - c) <= 0.05;
  }

  return false;
}

function getBloomWeight(level) {
  const map = {
    'Remember': 1.0,
    'Understand': 1.2,
    'Apply': 1.5,
    'Analyze': 1.8,
    'Evaluate': 2.0,
    'Create': 2.2
  };
  return map[level] || 1.2;
}

async function createPreMutationSnapshot(collections, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const snapshotId = `snapshot_${timestamp}`;
  const snapshotsDir = path.resolve(__dirname, '..', 'backups', 'snapshots');

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

  console.log(`✅ Pre-mutation snapshot created: ${snapshotId} (${Object.entries(collectionCounts).map(([k,v]) => `${k}:${v}`).join(', ')})`);
  return metadata;
}

async function reconcileAllPracticeAndMastery() {
  console.log('🚀 Starting Full Practice & Topic Mastery Reconciliation Engine...\n');

  // STEP 1: Pre-mutation Snapshot
  await createPreMutationSnapshot(
    ['practiceSubmissions', 'parentReviews', 'studentTopicMastery'],
    'Pre-reconciliation snapshot before fixing practice evaluation flaw & topic mastery'
  );

  // STEP 2: Reconcile practiceSubmissions
  console.log('\n--- Step 2: Reconciling practiceSubmissions ---');
  const pracSnap = await db.collection('practiceSubmissions').get();
  let updatedPracCount = 0;
  const pracBatchSize = 300;
  let currentBatch = db.batch();
  let batchOps = 0;

  const correctedPracticeMap = new Map(); // id -> corrected doc data

  for (const doc of pracSnap.docs) {
    const d = doc.data();
    const questions = d.questions || [];
    let correctCount = 0;
    let modified = false;

    const updatedQuestions = questions.map(q => {
      const isMultiple = q.type === 'multiple_mcq' || q.type === 'multi_mcq';
      const resolvedCorrectAnswer = isMultiple
        ? (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 ? q.correctAnswers : (q.correctAnswer ? [q.correctAnswer] : []))
        : (q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : ''));

      const isCorrect = evaluateQuestionAnswer(
        q.type || 'single_mcq',
        q.userAnswer,
        resolvedCorrectAnswer,
        q.options
      );

      if (isCorrect) correctCount++;
      if (Boolean(q.isCorrect) !== Boolean(isCorrect)) {
        modified = true;
      }

      return {
        ...q,
        isCorrect
      };
    });

    const totalQs = updatedQuestions.length || d.totalQuestions || 6;
    const newScore = correctCount;
    const newPercentage = totalQs > 0 ? Math.round((newScore / totalQs) * 100) : 0;

    if (modified || d.score !== newScore) {
      updatedPracCount++;
      const updatePayload = {
        questions: updatedQuestions,
        score: newScore,
        correctCount: newScore,
        percentage: newPercentage,
        scorePercent: newPercentage,
        reconciledAt: new Date()
      };

      correctedPracticeMap.set(doc.id, { ...d, ...updatePayload });
      currentBatch.update(doc.ref, updatePayload);
      batchOps++;

      if (batchOps >= pracBatchSize) {
        await currentBatch.commit();
        currentBatch = db.batch();
        batchOps = 0;
      }
    } else {
      correctedPracticeMap.set(doc.id, d);
    }
  }

  if (batchOps > 0) {
    await currentBatch.commit();
    currentBatch = db.batch();
    batchOps = 0;
  }
  console.log(`✅ Corrected ${updatedPracCount} practiceSubmissions documents.`);

  // STEP 3: Reconcile parentReviews for practice
  console.log('\n--- Step 3: Reconciling parentReviews (practice type) ---');
  const parentReviewsSnap = await db.collection('parentReviews').where('type', '==', 'practice').get();
  let updatedReviewsCount = 0;

  for (const doc of parentReviewsSnap.docs) {
    const rData = doc.data();
    // Try matching practice submission by doc ID, submissionId, logId, or reviewId
    const candidateIds = [doc.id, rData.submissionId, rData.practiceSubmissionId, rData.logId, rData.reviewId, rData.id].filter(Boolean);
    let matchedPrac = null;
    for (const cId of candidateIds) {
      if (correctedPracticeMap.has(cId)) {
        matchedPrac = correctedPracticeMap.get(cId);
        break;
      }
    }

    if (!matchedPrac) {
      // Find by studentCode and topicCode and approximate timestamp
      for (const [pId, pData] of correctedPracticeMap.entries()) {
        if (pData.studentCode === rData.studentCode && pData.topicCode === rData.topicCode) {
          matchedPrac = pData;
          break;
        }
      }
    }

    if (matchedPrac) {
      const newScore = matchedPrac.score;
      const totalQs = (matchedPrac.questions || []).length || matchedPrac.totalQuestions || 6;
      const newPct = totalQs > 0 ? Math.round((newScore / totalQs) * 100) : 0;

      if (rData.score !== newScore || rData.percentage !== newPct) {
        updatedReviewsCount++;
        currentBatch.update(doc.ref, {
          score: newScore,
          correctCount: newScore,
          percentage: newPct,
          scorePercent: newPct,
          questions: matchedPrac.questions || rData.questions || [],
          reconciledAt: new Date()
        });
        batchOps++;

        if (batchOps >= pracBatchSize) {
          await currentBatch.commit();
          currentBatch = db.batch();
          batchOps = 0;
        }
      }
    }
  }

  if (batchOps > 0) {
    await currentBatch.commit();
    currentBatch = db.batch();
    batchOps = 0;
  }
  console.log(`✅ Corrected ${updatedReviewsCount} parentReviews documents.`);

  // STEP 4: Rebuild studentTopicMastery from all sources
  console.log('\n--- Step 4: Rebuilding studentTopicMastery ---');
  // 4a. Gather all exam attempts
  const examSnap = await db.collection('examAttempts').get();
  // Map of `${studentCode}_${topicCode}` -> array of evaluation events
  const topicEventsMap = new Map();

  function addEvent(studentCode, topicCode, event) {
    if (!studentCode || !topicCode) return;
    const key = `${studentCode}_${topicCode}`;
    if (!topicEventsMap.has(key)) {
      topicEventsMap.set(key, []);
    }
    topicEventsMap.get(key).push(event);
  }

  examSnap.forEach(doc => {
    const d = doc.data();
    const sCode = d.studentCode;
    const qDetails = d.questionDetails || [];
    const qEvals = d.questionEvaluations || [];
    const createdAt = d.submittedAt ? (d.submittedAt.toDate ? d.submittedAt.toDate() : new Date(d.submittedAt)) : new Date();

    if (qEvals && qEvals.length > 0) {
      qEvals.forEach(ev => {
        if (ev.topicCode) {
          addEvent(sCode, ev.topicCode, {
            id: ev.id || ev.questionCode,
            difficulty: ev.difficulty || 'medium',
            bloomLevel: ev.bloomLevel || 'Understand',
            isCorrect: !!ev.isCorrect,
            isDisputed: !!ev.isDisputed,
            isExam: true,
            createdAt
          });
        }
      });
    }
  });

  // 4b. Gather all practice submissions
  for (const [pId, pData] of correctedPracticeMap.entries()) {
    const sCode = pData.studentCode;
    const tCode = pData.topicCode;
    const createdAt = pData.createdAt ? (pData.createdAt.toDate ? pData.createdAt.toDate() : new Date(pData.createdAt)) : new Date();
    const questions = pData.questions || [];

    questions.forEach(q => {
      addEvent(sCode, tCode, {
        id: q.id || q.questionCode,
        difficulty: q.difficulty || 'medium',
        bloomLevel: q.bloomLevel || 'Understand',
        isCorrect: !!q.isCorrect,
        isDisputed: !!q.isDisputed,
        isExam: false,
        createdAt
      });
    });
  }

  // 4c. Load existing studentTopicMastery documents
  const masterySnap = await db.collection('studentTopicMastery').get();
  const existingMasteryDocs = new Map();
  masterySnap.forEach(d => existingMasteryDocs.set(d.id, d.data()));

  // Process all keys
  const allMasteryKeys = new Set([...existingMasteryDocs.keys(), ...topicEventsMap.keys()]);
  console.log(`Recomputing mastery for ${allMasteryKeys.size} student-topic pairs...`);

  let updatedMasteryCount = 0;
  for (const docId of allMasteryKeys) {
    const parts = docId.split('_');
    const sCode = parts[0];
    const tCode = parts.slice(1).join('_');
    const existing = existingMasteryDocs.get(docId) || {};
    const events = topicEventsMap.get(docId) || [];

    // Sort events chronologically
    events.sort((a, b) => (a.createdAt?.getTime?.() || 0) - (b.createdAt?.getTime?.() || 0));

    let questionsAttempted = 0;
    let questionsCorrect = 0;
    let questionsWrong = 0;
    let examQuestionsAttempted = 0;
    let practiceQuestionsAttempted = 0;
    let weightedPointsEarned = 0;
    let weightedPointsPossible = 0;
    let questionHistory = [];

    events.forEach(ev => {
      if (ev.isDisputed) return;

      const diffWeight = ev.difficulty === 'easy' ? 1 : (ev.difficulty === 'hard' ? 3 : 2);
      const bloomWeight = getBloomWeight(ev.bloomLevel || 'Understand');
      const weight = diffWeight * bloomWeight;

      questionsAttempted++;
      if (ev.isExam) examQuestionsAttempted++;
      else practiceQuestionsAttempted++;

      if (ev.isCorrect) {
        questionsCorrect++;
        weightedPointsEarned += weight;
      } else {
        questionsWrong++;
      }
      weightedPointsPossible += weight;

      // Update question history
      questionHistory = questionHistory.filter(h => h.questionId !== ev.id);
      questionHistory.push({
        questionId: ev.id,
        seenAt: ev.createdAt,
        wasCorrect: ev.isCorrect
      });
    });

    if (questionHistory.length > 100) {
      questionHistory = questionHistory.slice(-100);
    }

    const calculatedMastery = weightedPointsPossible > 0
      ? Math.round((weightedPointsEarned / weightedPointsPossible) * 100)
      : (existing.mastery || 0);

    const calculatedConfidence = Math.min(questionsAttempted, 100);

    const newDocData = {
      ...existing,
      studentCode: sCode,
      topicCode: tCode,
      questionsAttempted,
      questionsCorrect,
      questionsWrong,
      examQuestionsAttempted,
      practiceQuestionsAttempted,
      weightedPointsEarned,
      weightedPointsPossible,
      mastery: calculatedMastery,
      confidence: calculatedConfidence,
      questionHistory,
      lastUpdated: new Date()
    };

    // If existing had recovery status preserved
    if (existing.isRecoveryMastered !== undefined) {
      newDocData.isRecoveryMastered = existing.isRecoveryMastered;
    }

    currentBatch.set(db.collection('studentTopicMastery').doc(docId), newDocData);
    updatedMasteryCount++;
    batchOps++;

    if (batchOps >= pracBatchSize) {
      await currentBatch.commit();
      currentBatch = db.batch();
      batchOps = 0;
    }
  }

  if (batchOps > 0) {
    await currentBatch.commit();
    currentBatch = db.batch();
    batchOps = 0;
  }

  console.log(`✅ Successfully updated ${updatedMasteryCount} studentTopicMastery records!`);
  console.log('\n🎉 ALL PRACTICE RECORDS AND TOPIC MASTERY DATA RECONCILED CLEANLY!');
}

reconcileAllPracticeAndMastery().catch(console.error).then(() => process.exit(0));
