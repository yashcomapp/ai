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

// Evaluation logic mirroring questionTypes.ts
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

async function auditAllRecords() {
  console.log('=== AUDITING ALL PRACTICE SUBMISSIONS ===');
  const pracSnap = await db.collection('practiceSubmissions').get();
  console.log(`Total practice submissions: ${pracSnap.size}`);

  let practiceMismatches = 0;
  pracSnap.forEach(doc => {
    const d = doc.data();
    const questions = d.questions || [];
    let recomputedScore = 0;
    let hasDiscrepancy = false;

    questions.forEach((q, idx) => {
      const isMultiple = q.type === 'multiple_mcq' || q.type === 'multi_mcq';
      const resolvedCorrectAnswer = isMultiple
        ? (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0 ? q.correctAnswers : (q.correctAnswer ? [q.correctAnswer] : []))
        : (q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : ''));

      const isCorrectNow = evaluateQuestionAnswer(
        q.type || 'single_mcq',
        q.userAnswer,
        resolvedCorrectAnswer,
        q.options
      );

      if (isCorrectNow) recomputedScore++;

      if (Boolean(q.isCorrect) !== Boolean(isCorrectNow)) {
        hasDiscrepancy = true;
        console.log(`[DISCREPANCY] Practice ${doc.id} Q${idx + 1} (${q.questionCode || q.id}): stored=${q.isCorrect}, computed=${isCorrectNow}`);
        console.log(`  type=${q.type}, userAns=${JSON.stringify(q.userAnswer)}, correctAns=${JSON.stringify(resolvedCorrectAnswer)}`);
        console.log(`  options=${JSON.stringify(q.options)}`);
      }
    });

    if (d.score !== recomputedScore || hasDiscrepancy) {
      practiceMismatches++;
      console.log(`[MISMATCH SUMMARY] Practice ${doc.id} (Student: ${d.studentCode}, Topic: ${d.topicCode}): Stored Score = ${d.score}, Recomputed Score = ${recomputedScore}`);
    }
  });

  console.log(`\nTotal practice submissions with score discrepancies: ${practiceMismatches}`);

  console.log('\n=== AUDITING ALL EXAM ATTEMPTS ===');
  const examSnap = await db.collection('examAttempts').get();
  console.log(`Total exam attempts: ${examSnap.size}`);

  let examMismatches = 0;
  examSnap.forEach(doc => {
    const d = doc.data();
    const questionDetails = d.questionDetails || [];
    let recomputedCorrect = 0;
    let hasDiscrepancy = false;

    questionDetails.forEach((qd, idx) => {
      if (!qd.isAttempted) return;
      // In exam attempts, userAns and correctAns are option texts or strings
      const isCorrect = qd.isCorrect;
      // Check if user answer text matches correct answer text
      const norm = (s) => String(s || '').trim().toLowerCase().replace(/\\\(|\\\)|\\\[|\\\]|\$+/g, '').replace(/[^\w\d]/g, '');
      const uNorm = norm(qd.userAnswer);
      const cNorm = norm(qd.correctAnswer);
      const textsMatch = uNorm === cNorm && uNorm.length > 0;

      if (isCorrect && !textsMatch) {
        // Maybe numerical or other tolerance
        // console.log(`Exam ${doc.id} Q${idx+1}: marked correct but text diff: user="${qd.userAnswer}" vs correct="${qd.correctAnswer}"`);
      } else if (!isCorrect && textsMatch) {
        hasDiscrepancy = true;
        console.log(`[EXAM DISCREPANCY] Exam ${doc.id} Q${idx + 1} (${qd.questionCode}): marked FALSE but userAns matched correctAns!`);
        console.log(`  userAns="${qd.userAnswer}", correctAns="${qd.correctAnswer}"`);
      }
    });

    if (hasDiscrepancy) {
      examMismatches++;
    }
  });

  console.log(`\nTotal exam attempts with discrepancy: ${examMismatches}`);
}

auditAllRecords().catch(console.error).then(() => process.exit(0));
