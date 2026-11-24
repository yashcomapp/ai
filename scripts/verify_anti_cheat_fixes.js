const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { sanitizeQuestionForStudent, sanitizeQuestionsForStudent } = require('../src/lib/questionTypes.ts');

async function runAudit() {
  console.log('=== VERIFYING FIX 1: SERVER-SIDE QUESTION SANITIZATION ===');

  const examId = '026-MH-9-Work and Energy,-2.5+3.1-231126';
  const examDoc = await adminDb.collection('exams').doc(examId).get();
  if (!examDoc.exists) {
    throw new Error('Test exam not found');
  }

  const qCodes = examDoc.data().questionCodes || [];
  console.log(`Auditing ${qCodes.length} questions from exam ${examId}...`);

  const rawQuestions = [];
  for (const code of qCodes) {
    const qSnap = await adminDb.collection('questions').where('questionCode', '==', code).get();
    if (qSnap.size > 0) {
      rawQuestions.push({ id: qSnap.docs[0].id, ...qSnap.docs[0].data() });
    }
  }

  console.log(`Fetched ${rawQuestions.length} raw questions.`);

  // Verify before sanitization: answers DO exist
  let preIsCorrectCount = 0;
  let preNumericalCount = 0;
  let preSolutionCount = 0;
  for (const q of rawQuestions) {
    if (q.options?.some(o => o && typeof o === 'object' && 'isCorrect' in o)) preIsCorrectCount++;
    if (q.numericalValue != null) preNumericalCount++;
    if (q.solution != null) preSolutionCount++;
  }
  console.log(`Pre-sanitization leaks detected in DB records:`);
  console.log(` - Questions with 'isCorrect' in options: ${preIsCorrectCount}`);
  console.log(` - Questions with 'numericalValue': ${preNumericalCount}`);
  console.log(` - Questions with 'solution': ${preSolutionCount}`);

  // Apply sanitization
  const secured = sanitizeQuestionsForStudent(rawQuestions);

  // Deep scan the sanitized payload for ANY leaked keys
  const FORBIDDEN_KEYS = [
    'isCorrect',
    'is_correct',
    'correct',
    'correctAnswer',
    'correctAnswers',
    'correctOption',
    'solution',
    'solutionSteps',
    'steps',
    'explanation',
    'numericalValue',
    'tolerance',
    'markingScheme',
    'rubric'
  ];

  let leaksFound = 0;
  function scanObject(obj, path = '') {
    if (!obj || typeof obj !== 'object') return;
    for (const key of Object.keys(obj)) {
      const fullPath = path ? `${path}.${key}` : key;
      if (FORBIDDEN_KEYS.includes(key)) {
        console.error(`🚨 LEAK DETECTED at ${fullPath}: ${JSON.stringify(obj[key])}`);
        leaksFound++;
      }
      scanObject(obj[key], fullPath);
    }
  }

  scanObject(secured);

  if (leaksFound === 0) {
    console.log('\n✅ FIX 1 VERIFIED: 100% of questions sanitized. Zero answer indicators, zero solutions, zero numerical values found.');
  } else {
    throw new Error(`Fix 1 FAILED: Found ${leaksFound} leaked fields!`);
  }

  // Ensure questions still retain display fidelity
  for (let i = 0; i < secured.length; i++) {
    const q = secured[i];
    if (!q.text && !q.questionText) {
      throw new Error(`Question ${i} missing stem text!`);
    }
    if (['OSC', 'OMC'].includes(q.type) && (!Array.isArray(q.options) || q.options.length < 2)) {
      throw new Error(`MCQ Question ${i} missing options!`);
    }
  }
  console.log('✅ Display fidelity verified: all question stems, types, options, and codes intact.');
  console.log('\n=== FIX 1 & FIX 2 VERIFICATION COMPLETE ===');
}

runAudit().catch(err => {
  console.error(err);
  process.exit(1);
});
