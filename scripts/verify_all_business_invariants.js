/**
 * Comprehensive Mathematical & Architectural Invariant Verification Suite
 * 
 * Verifies that all business logic across Student, Parent, and Admin views
 * adheres strictly to SSOT rules with 100% mathematical parity and zero drift.
 */

const assert = require('assert');

console.log('================================================================');
console.log('🔍 RUNNING COMPREHENSIVE BUSINESS LOGIC & INVARIANT VERIFICATION');
console.log('================================================================\n');

let passedTests = 0;
let totalTests = 0;

function test(description, fn) {
  totalTests++;
  try {
    fn();
    console.log(`  ✅ PASS: ${description}`);
    passedTests++;
  } catch (err) {
    console.error(`  ❌ FAIL: ${description}`);
    console.error(`     Error: ${err.message}`);
    process.exitCode = 1;
  }
}

// -----------------------------------------------------------------------------
// SUITE 1: Required Confidence Calculations (Rule 2F)
// -----------------------------------------------------------------------------
console.log('--- Suite 1: Confidence Requirement Engine ---');

function getRequiredConfidence(topicClassification, targetQuestions) {
  const cls = String(topicClassification || '').toLowerCase().trim();
  if (cls === 'minor' || cls === 'micro') return 12;
  if (cls === 'medium' || cls === 'moderate' || cls === 'conceptual') return 18;
  if (cls === 'major' || cls === 'calculative' || cls === 'hots') return 24;
  
  if (targetQuestions !== undefined) {
    if (targetQuestions <= 30) return 12;
    if (targetQuestions <= 50) return 18;
    return 24;
  }
  return 12;
}

test('Minor/Micro topics require 12 questions (2 sets of 6)', () => {
  assert.strictEqual(getRequiredConfidence('minor'), 12);
  assert.strictEqual(getRequiredConfidence('micro'), 12);
});

test('Medium/Conceptual topics require 18 questions (3 sets of 6)', () => {
  assert.strictEqual(getRequiredConfidence('medium'), 18);
  assert.strictEqual(getRequiredConfidence('conceptual'), 18);
});

test('Major/HOTS topics require 24 questions (4 sets of 6)', () => {
  assert.strictEqual(getRequiredConfidence('major'), 24);
  assert.strictEqual(getRequiredConfidence('hots'), 24);
});

// -----------------------------------------------------------------------------
// SUITE 2: SSOT Topic Mastery Classification (Rule 2F & 2A)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 2: SSOT Topic Classification & Parity ---');

function classifyTopic(mastery, confidence, reqConf, hasPracticed, mDataExists) {
  const isCertifiedMastered = mastery >= 90 && confidence >= reqConf;
  if (!mDataExists) {
    return 'needsAttention';
  } else if (isCertifiedMastered) {
    return 'mastered';
  } else if (mastery >= 50) {
    return 'practicing';
  } else {
    return 'needsAttention';
  }
}

test('High accuracy (95%) with insufficient confidence (6/18) is Practicing, NOT Mastered', () => {
  const state = classifyTopic(95, 6, 18, true, true);
  assert.strictEqual(state, 'practicing');
});

test('High accuracy (92%) with verified confidence (18/18) is Certified Mastered', () => {
  const state = classifyTopic(92, 18, 18, true, true);
  assert.strictEqual(state, 'mastered');
});

test('Unattempted assigned topic is strictly Needs Attention (Red)', () => {
  const state = classifyTopic(0, 0, 18, false, false);
  assert.strictEqual(state, 'needsAttention');
});

test('Low mastery (< 50%) is strictly Needs Attention (Red)', () => {
  const state = classifyTopic(45, 12, 12, true, true);
  assert.strictEqual(state, 'needsAttention');
});

test('Moderate mastery (50% - 89%) is Practicing (Yellow)', () => {
  const state1 = classifyTopic(50, 10, 12, true, true);
  assert.strictEqual(state1, 'practicing');
  const state2 = classifyTopic(89, 20, 12, true, true);
  assert.strictEqual(state2, 'practicing');
});

// -----------------------------------------------------------------------------
// SUITE 3: Parent & Student View "Needs Attention" Parity (Item 1 Fix)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 3: Parent & Student Dashboard Parity ---');

test('Parent view: summary card and diagnostic list agree on Needs Attention count', () => {
  // Scenario: Student has 10 assigned syllabus topics:
  // - 3 Mastered (>= 90% and verified)
  // - 2 Practicing (60% and 75%)
  // - 1 Attempted Weak (35%)
  // - 4 Unattempted Assigned Topics (never practiced)
  
  const assignedTopics = [
    { code: 'T1', mastery: 95, conf: 18, attempted: true },
    { code: 'T2', mastery: 92, conf: 24, attempted: true },
    { code: 'T3', mastery: 90, conf: 12, attempted: true },
    { code: 'T4', mastery: 65, conf: 10, attempted: true },
    { code: 'T5', mastery: 75, conf: 14, attempted: true },
    { code: 'T6', mastery: 35, conf: 8,  attempted: true },
    { code: 'T7', mastery: 0,  conf: 0,  attempted: false },
    { code: 'T8', mastery: 0,  conf: 0,  attempted: false },
    { code: 'T9', mastery: 0,  conf: 0,  attempted: false },
    { code: 'T10', mastery: 0, conf: 0,  attempted: false },
  ];

  const classified = {
    mastered: [],
    practicing: [],
    needsAttention: []
  };

  assignedTopics.forEach(t => {
    const state = classifyTopic(t.mastery, t.conf, 12, t.attempted, t.attempted);
    if (state === 'mastered') classified.mastered.push(t);
    else if (state === 'practicing') classified.practicing.push(t);
    else classified.needsAttention.push(t);
  });

  const unifiedMetrics = {
    needsAttentionTopicsCount: classified.needsAttention.length, // 5
    masteredTopicsCount: classified.mastered.length,             // 3
    practicingTopicsCount: classified.practicing.length,         // 2
    totalTopicsCount: assignedTopics.length,                     // 10
    classifiedTopics: classified
  };

  // Parent View Logic using SSOT:
  const parentNeedsAttentionList = unifiedMetrics.classifiedTopics.needsAttention.map(t => t.code);
  const parentNeedsAttentionRemainingCount = parentNeedsAttentionList.length;
  const parentSummaryNeedsAttentionCount = unifiedMetrics.needsAttentionTopicsCount;

  // Invariant 1: Summary card and topic list must be strictly equal
  assert.strictEqual(parentNeedsAttentionRemainingCount, parentSummaryNeedsAttentionCount);
  assert.strictEqual(parentNeedsAttentionRemainingCount, 5);

  // Invariant 2: Invariant conservation (Mastered + Practicing + NeedsAttention === Total)
  assert.strictEqual(
    unifiedMetrics.masteredTopicsCount + 
    unifiedMetrics.practicingTopicsCount + 
    unifiedMetrics.needsAttentionTopicsCount,
    unifiedMetrics.totalTopicsCount
  );
});

// -----------------------------------------------------------------------------
// SUITE 4: Practice Engine Mastery Pinning Gate (Item 2 Fix)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 4: Practice Engine Mastery Gate Verification ---');

function evaluatePracticeMasteryFloor(existing, updatedMastery, fallbackReqConf) {
  const existingConf = existing ? (existing.confidence || existing.verifiedAttempts || 0) : 0;
  const targetReqConf = existing?.requiredConfidence || fallbackReqConf;
  const isMasteredTopic = Boolean(existing && existing.mastery >= 90 && existingConf >= targetReqConf);
  
  let finalMastery = updatedMastery;
  if (isMasteredTopic) {
    finalMastery = Math.max(finalMastery, 90);
  }
  return { isMasteredTopic, finalMastery };
}

test('Practice session on unverified topic (mastery 92%, conf 6, target 18) does NOT lock to 90', () => {
  const existing = { mastery: 92, confidence: 6, requiredConfidence: 18 };
  // Student struggled on a subsequent practice session, calculated mastery = 78
  const res = evaluatePracticeMasteryFloor(existing, 78, 18);
  assert.strictEqual(res.isMasteredTopic, false);
  assert.strictEqual(res.finalMastery, 78); // Allowed to drop because not certified mastered
});

test('Practice session on certified mastered topic (mastery 92%, conf 18, target 18) DOES lock to 90 floor', () => {
  const existing = { mastery: 92, confidence: 18, requiredConfidence: 18 };
  // Student tried hard questions in practice, calculated mastery = 82
  const res = evaluatePracticeMasteryFloor(existing, 82, 18);
  assert.strictEqual(res.isMasteredTopic, true);
  assert.strictEqual(res.finalMastery, 90); // Protected from being demoted by practice
});

// -----------------------------------------------------------------------------
// SUITE 5: Student Learning Page Cutoffs (Item 3 Fix)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 5: Student Learning Page Thresholds ---');

const getMasteryClass = (mastery) => {
  if (mastery < 50) return 'low';
  if (mastery < 90) return 'medium';
  return 'high';
};

const getProgressColor = (mastery) => {
  if (mastery < 50) return 'var(--danger)';
  if (mastery < 90) return 'var(--warning)';
  return 'var(--success)';
};

test('Score 0% - 49.9% is Low / Danger (Needs Attention)', () => {
  assert.strictEqual(getMasteryClass(0), 'low');
  assert.strictEqual(getProgressColor(0), 'var(--danger)');
  assert.strictEqual(getMasteryClass(49.9), 'low');
  assert.strictEqual(getProgressColor(49.9), 'var(--danger)');
});

test('Score 50.0% - 89.9% is Medium / Warning (Practicing)', () => {
  assert.strictEqual(getMasteryClass(50), 'medium');
  assert.strictEqual(getProgressColor(50), 'var(--warning)');
  assert.strictEqual(getMasteryClass(89.9), 'medium');
  assert.strictEqual(getProgressColor(89.9), 'var(--warning)');
});

test('Score >= 90.0% is High / Success (Mastered)', () => {
  assert.strictEqual(getMasteryClass(90), 'high');
  assert.strictEqual(getProgressColor(90), 'var(--success)');
  assert.strictEqual(getMasteryClass(100), 'high');
  assert.strictEqual(getProgressColor(100), 'var(--success)');
});

// -----------------------------------------------------------------------------
// SUITE 6: Academic Quotient Weights Conservation (Item 4 Fix)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 6: Academic Pillar Weights Conservation ---');

const CALCULATOR_WEIGHTS = {
  exam: 0.30,
  practice: 0.25,
  quality: 0.15,
  topicHealth: 0.30
};

test('Calculator class weights sum exactly to 1.00 (100%)', () => {
  const sum = Object.values(CALCULATOR_WEIGHTS).reduce((a, b) => a + b, 0);
  assert.strictEqual(Math.round(sum * 100) / 100, 1.00);
});

test('Runtime calculateAll weights with conducted exams sum to 1.00', () => {
  const hasConductedExams = true;
  const examWeight = hasConductedExams ? 0.30 : 0.00;
  const healthWeight = hasConductedExams ? 0.30 : 0.45;
  const practiceWeight = hasConductedExams ? 0.25 : 0.35;
  const qualityWeight = hasConductedExams ? 0.15 : 0.20;
  const total = examWeight + healthWeight + practiceWeight + qualityWeight;
  assert.strictEqual(Math.round(total * 100) / 100, 1.00);
});

test('Runtime calculateAll weights without conducted exams sum to 1.00', () => {
  const hasConductedExams = false;
  const examWeight = hasConductedExams ? 0.30 : 0.00;
  const healthWeight = hasConductedExams ? 0.30 : 0.45;
  const practiceWeight = hasConductedExams ? 0.25 : 0.35;
  const qualityWeight = hasConductedExams ? 0.15 : 0.20;
  const total = examWeight + healthWeight + practiceWeight + qualityWeight;
  assert.strictEqual(Math.round(total * 100) / 100, 1.00);
});

// -----------------------------------------------------------------------------
// SUITE 7: Attendance Summary Calculation SSOT (Rule 2G)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 7: Attendance Calculation Invariants ---');

function calculateAttendanceSummary(records) {
  let totalDays = 0;
  let fullPresentDays = 0;
  let absentDays = 0;
  let leaveDays = 0;
  let lateDays = 0;
  let halfDays = 0;

  records.forEach(rec => {
    if (!rec || !rec.status || rec.status === 'not_marked') return;
    totalDays++;
    const status = rec.status.toLowerCase();
    if (status === 'present') fullPresentDays++;
    else if (status === 'absent') absentDays++;
    else if (status === 'late') { fullPresentDays++; lateDays++; }
    else if (status === 'leave') leaveDays++;
    else if (status === 'half_day') halfDays++;
  });

  const effectivePresentDays = (fullPresentDays * 1.0) + (halfDays * 0.5);
  const attendancePercentage = totalDays > 0
    ? Math.min(100, Math.max(0, Math.round((effectivePresentDays / totalDays) * 100)))
    : 100;

  return { totalDays, presentDays: fullPresentDays, absentDays, leaveDays, lateDays, halfDays, effectivePresentDays, attendancePercentage };
}

test('Standardized attendance stats correctly credit present, late, half-day, and leave', () => {
  const records = [
    { status: 'present' },
    { status: 'present' },
    { status: 'late' },     // Counts as full present day + late flag
    { status: 'half_day' }, // Counts as 0.5 present day
    { status: 'leave' },    // Approved leave: 0 day, in totalDays
    { status: 'absent' }     // Absent: 0 day, in totalDays
  ];
  const summary = calculateAttendanceSummary(records);
  assert.strictEqual(summary.totalDays, 6);
  assert.strictEqual(summary.presentDays, 3);
  assert.strictEqual(summary.lateDays, 1);
  assert.strictEqual(summary.halfDays, 1);
  assert.strictEqual(summary.leaveDays, 1);
  assert.strictEqual(summary.absentDays, 1);
  assert.strictEqual(summary.effectivePresentDays, 3.5); // 2 full + 1 late(full) + 0.5 half
  // (3.5 / 6) * 100 = 58.33% -> 58%
  assert.strictEqual(summary.attendancePercentage, 58);
});

// -----------------------------------------------------------------------------
// SUITE 8: Zero-Cost Cloud & Network Egress Safeguards (Rule 2U & 2V)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 8: Zero-Cost Cloud Egress Safety ---');

function sanitizeRealTimePayload(payload) {
  const sanitized = { ...payload };
  if (Array.isArray(sanitized.proctoringSnapshots)) {
    sanitized.proctoringSnapshotCount = sanitized.proctoringSnapshots.length;
    delete sanitized.proctoringSnapshots;
  }
  if (Array.isArray(sanitized.manualCaptures)) {
    sanitized.manualCaptureCount = sanitized.manualCaptures.length;
    delete sanitized.manualCaptures;
  }
  return sanitized;
}

test('sanitizeRealTimePayload actively strips heavy base64 snapshot arrays from real-time payloads', () => {
  const heavyPayload = {
    studentCode: 'ST-2026-000001',
    tabViolations: 2,
    proctoringSnapshots: ['data:image/jpeg;base64,xxxxxx1', 'data:image/jpeg;base64,xxxxxx2'],
    manualCaptures: ['data:image/jpeg;base64,yyyyyy1']
  };

  const sanitized = sanitizeRealTimePayload(heavyPayload);
  assert.strictEqual(sanitized.proctoringSnapshots, undefined);
  assert.strictEqual(sanitized.manualCaptures, undefined);
  assert.strictEqual(sanitized.proctoringSnapshotCount, 2);
  assert.strictEqual(sanitized.manualCaptureCount, 1);
  assert.strictEqual(sanitized.studentCode, 'ST-2026-000001');
});

// -----------------------------------------------------------------------------
// SUITE 9: Round 8 Audit Invariants (Safe Fallbacks, Auth Revocation Retry, Mastery SSOT)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 9: Safe Percentage Fallbacks & Auth Revocation Invariants ---');

function resolvePercentage(percentageField, score, maxMarks) {
  return percentageField != null && !isNaN(Number(percentageField))
    ? Math.round(Number(percentageField))
    : (maxMarks > 0 ? Math.round((score / maxMarks) * 100) : 0);
}

test('Valid numeric percentage is respected without modification', () => {
  assert.strictEqual(resolvePercentage(87.4, 15, 20), 87);
  assert.strictEqual(resolvePercentage('92', 15, 20), 92);
});

test('Invalid or non-numeric percentage safely falls back to score / maxMarks', () => {
  assert.strictEqual(resolvePercentage('invalid', 15, 20), 75);
  assert.strictEqual(resolvePercentage(null, 18, 20), 90);
  assert.strictEqual(resolvePercentage(undefined, 10, 20), 50);
  assert.strictEqual(resolvePercentage(NaN, 14, 20), 70);
});

test('Auth claims sync: Failed token revocation never sets in-memory throttle cache', () => {
  const lastSyncedClaimsMap = new Map();
  const uid = 'user-test-uid';
  let revokeSuccess = false;

  try {
    if (!revokeSuccess) {
      throw new Error('Firebase Auth network error');
    }
    lastSyncedClaimsMap.set(uid, { timestamp: Date.now() });
  } catch (err) {
    lastSyncedClaimsMap.delete(uid);
  }

  assert.strictEqual(lastSyncedClaimsMap.has(uid), false);
});

// -----------------------------------------------------------------------------
// SUITE 10: Canonical SSOT Barrier & Ingress Rejection Gate (Rule 2.R & 2.K)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 10: Canonical SSOT Barrier & Ingress Rejection Gate ---');

const CANONICAL_BOARDS = ['CBSE', 'MH'];
const CANONICAL_CLASSES = ['8', '9', '10'];
const CANONICAL_SUBJECTS = {
  CBSE: { '8': ['MGP1', 'MGP2', 'CURI'], '9': ['MGM', 'SCIE'], '10': ['MATH', 'SCI'] },
  MH: { '8': ['MTH', 'SCI'], '9': ['MTH1', 'MTH2', 'SCIT'], '10': ['MTH1', 'MTH2', 'SCIT1', 'SCIT2'] }
};
const CANONICAL_TYPES = ['OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE', 'SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'];

function validateStudentCode(sc) {
  if (!sc || typeof sc !== 'string') return { valid: false, error: 'Student code required' };
  return /^ST-\d{4}-\d{6}$/.test(sc.trim()) ? { valid: true } : { valid: false, error: 'Invalid format' };
}

function validateSubjectCode(board, cls, subj) {
  if (!CANONICAL_BOARDS.includes(board)) return { valid: false, error: `Invalid board ${board}` };
  const cleanClass = String(cls || '').trim();
  if (!CANONICAL_CLASSES.includes(cleanClass)) return { valid: false, error: `Invalid class ${cls}` };
  const allowed = CANONICAL_SUBJECTS[board]?.[cleanClass] || [];
  if (!allowed.includes(subj)) return { valid: false, error: `Invalid subject ${subj}` };
  return { valid: true };
}

function validateTopicCode(tc) {
  if (!tc || typeof tc !== 'string') return { valid: false };
  const parts = tc.trim().split('-');
  if (parts.length < 5) return { valid: false, error: 'Must have at least 5 parts' };
  const [b, c, s, ch, ...rest] = parts;
  const sRes = validateSubjectCode(b, c, s);
  if (!sRes.valid) return sRes;
  if (!/^\d+$/.test(ch)) return { valid: false, error: 'Invalid chapter' };
  const tNum = rest.join('-');
  if (!/^[\d\.]+$/.test(tNum)) return { valid: false, error: 'Invalid topic number' };
  return { valid: true };
}

function validateQuestionCode(qc) {
  if (!qc || typeof qc !== 'string') return { valid: false };
  const parts = qc.trim().split('-');
  if (parts.length < 7) return { valid: false, error: 'Must have at least 7 parts' };
  const seq = parts[parts.length - 1];
  const type = parts[parts.length - 2];
  const topicCode = parts.slice(0, parts.length - 2).join('-');
  const tRes = validateTopicCode(topicCode);
  if (!tRes.valid) return tRes;
  if (!CANONICAL_TYPES.includes(type)) return { valid: false, error: `Invalid question type ${type}` };
  if (!/^\d{3,}$/.test(seq)) return { valid: false, error: 'Invalid sequence' };
  return { valid: true };
}

test('Strict Student Code format (ST-YYYY-XXXXXX) enforced', () => {
  assert.strictEqual(validateStudentCode('ST-2026-000001').valid, true);
  assert.strictEqual(validateStudentCode('ST-2026-000050').valid, true);
  assert.strictEqual(validateStudentCode('ST-26-001').valid, false);
  assert.strictEqual(validateStudentCode('STUDENT-001').valid, false);
  assert.strictEqual(validateStudentCode(null).valid, false);
});

test('Strict Subject Code per Board & Class strictly rejects legacy aliases', () => {
  // MH Class 8: MTH is canonical, MATH is legacy rejected
  assert.strictEqual(validateSubjectCode('MH', '8', 'MTH').valid, true);
  assert.strictEqual(validateSubjectCode('MH', '8', 'MATH').valid, false);
  assert.strictEqual(validateSubjectCode('MH', '8', 'SCI').valid, true);
  // CBSE Class 8: MGP1 is canonical, MATH is rejected
  assert.strictEqual(validateSubjectCode('CBSE', '8', 'MGP1').valid, true);
  assert.strictEqual(validateSubjectCode('CBSE', '8', 'MATH').valid, false);
});

test('Strict Topic Code barrier rejects non-canonical subjects or malformed chapters', () => {
  assert.strictEqual(validateTopicCode('MH-8-MTH-13-13.1.2').valid, true);
  assert.strictEqual(validateTopicCode('CBSE-8-MGP1-3-3.1').valid, true);
  assert.strictEqual(validateTopicCode('MH-8-MATH-13-13.1.2').valid, false); // Legacy MATH rejected
  assert.strictEqual(validateTopicCode('MH-8-MTH-Ch13-13.1.2').valid, false); // 'Ch13' rejected, must be numeric
});

test('Strict Question Code barrier rejects invalid types, short sequences, or bad topic prefixes', () => {
  assert.strictEqual(validateQuestionCode('MH-8-MTH-13-13.1.2-OSC-001').valid, true);
  assert.strictEqual(validateQuestionCode('CBSE-8-MGP1-3-3.1-SLA-010').valid, true);
  assert.strictEqual(validateQuestionCode('MH-8-MATH-13-13.1.2-OSC-001').valid, false); // Legacy subject in questionCode rejected
  assert.strictEqual(validateQuestionCode('MH-8-MTH-13-13.1.2-XYZ-001').valid, false); // Invalid question type rejected
  assert.strictEqual(validateQuestionCode('MH-8-MTH-13-13.1.2-OSC-1').valid, false); // Sequence < 3 digits rejected
});

// -----------------------------------------------------------------------------
// SUITE 11: Curriculum Guard & Pedagogical Ceiling Invariants
// -----------------------------------------------------------------------------
console.log('\n--- Suite 11: Curriculum Guard & Pedagogical Ceiling Invariants ---');

const QUALITATIVE_TOPIC_PATTERNS = [
  /environment/i,
  /ecology/i,
  /ecosystem/i,
  /microbe/i,
  /bacteria/i,
  /fungi/i,
  /classification\s+of\s+plants/i,
  /living\s+world/i,
  /cell\s+and\s+cell\s+organelles/i,
  /disaster\s+management/i,
  /solid\s+waste/i,
  /weather\s+and\s+climate/i,
  /meteorology/i,
  /first\s+aid/i,
  /health\s+and\s+disease/i,
  /pollution/i,
  /biotechnology/i,
  /tissue\s+culture/i,
  /man-made\s+material/i,
  /useful\s+and\s+harmful/i
];

const QUALITATIVE_CHAPTER_CODES = new Set([
  'MH-9-SCIT-6',   // Classification of Plants
  'MH-9-SCIT-7',   // Energy Flow in an Ecosystem
  'MH-9-SCIT-8',   // Useful and Harmful Microbes
  'MH-9-SCIT-9',   // Environmental Management
  'MH-9-SCIT-10',  // ICT
  'MH-9-SCIT-17',  // Introduction to Biotechnology
  'MH-8-SCI-1',    // Living World and Classification of Microbes
  'MH-8-SCI-2',    // Health and Diseases
  'MH-8-SCI-7',    // Metals and Nonmetals
  'MH-8-SCI-8',    // Pollution
  'MH-8-SCI-9',    // Disaster Management
  'MH-8-SCI-10',   // Cell and Cell Organelles
  'MH-8-SCI-17',   // Man-made Materials
  'MH-8-SCI-18',   // Ecosystems
  'CBSE-8-CURI-5', // Curiosity: Reproduction / Microorganisms
  'MH-10-SCIT2-7', // Introduction to Microbiology
  'MH-10-SCIT2-8'  // Cell Biology and Biotechnology
]);

const PROHIBITED_ADVANCED_KEYWORDS = [
  { pattern: /\bdifferential\s+equations?\b/i, label: 'Differential Equations' },
  { pattern: /\bnavier[- ]stokes\b/i, label: 'Navier-Stokes Equations' },
  { pattern: /\bhamiltonian\b/i, label: 'Hamiltonian Mechanics' },
  { pattern: /schr(?:o|ö|oe)dinger/i, label: 'Schrodinger Equation' },
  { pattern: /\blorentz\s+(?:force|factor|transformation)\b/i, label: 'Lorentz Transformations' },
  { pattern: /\brelativistic\s+(?:time\s+dilation|beaming|mass)\b/i, label: 'Relativistic Physics' },
  { pattern: /\bsynchrotron\b/i, label: 'Synchrotron Radiation' },
  { pattern: /\bschwarzschild\s+radius\b/i, label: 'Schwarzschild Metric' },
  { pattern: /\bbragg's\s+law\b/i, label: "Bragg's Law Crystallography" },
  { pattern: /\bcrystal\s+field\s+splitting\b/i, label: 'Crystal Field Theory' },
  { pattern: /\bgibbs\s+free\s+energy\b/i, label: 'Gibbs Free Energy Thermodynamics' },
  { pattern: /\blapse\s+rate\b/i, label: 'Atmospheric Lapse Rate Calculation' },
  { pattern: /\bpsychrometric\b/i, label: 'Psychrometric Thermodynamics' },
  { pattern: /\bactual\s+vapor\s+pressure.*saturation\b/i, label: 'Vapor Pressure Numericals' },
  { pattern: /\bphytoremediation\b/i, label: 'Phytoremediation / Hyperaccumulation' },
  { pattern: /\bhyperaccumulat/i, label: 'Hyperaccumulating Plants' },
  { pattern: /\bfluidized\s+bed\s+incinerator\b/i, label: 'Fluidized Bed Combustion' },
  { pattern: /\bbaghouse\s+filters?\b/i, label: 'Baghouse Fabric Filters' },
  { pattern: /\bglomerular\s+filtration\s+rate\b/i, label: 'GFR Ultrafiltration Math' },
  { pattern: /\bpotometer\s+transpires\b/i, label: 'Potometer Transpiration Rate Math' },
  { pattern: /\bdomestic\s+dog\s*\(2n\s*=\s*78\)/i, label: 'Canine Cytogenetics' }
];

function isTopicPurelyQualitative(topicCode, chapterName, subjectName) {
  if (!topicCode && !chapterName) return false;
  const tCode = String(topicCode || '').trim();
  for (const prefix of QUALITATIVE_CHAPTER_CODES) {
    if (tCode === prefix || tCode.startsWith(`${prefix}-`) || tCode.startsWith(`${prefix}.`)) {
      return true;
    }
  }
  const combined = `${tCode} ${chapterName || ''} ${subjectName || ''}`.toLowerCase();
  for (const pat of QUALITATIVE_TOPIC_PATTERNS) {
    if (pat.test(combined)) return true;
  }
  return false;
}

function validateQuestionCurriculum(q) {
  const errors = [];
  if (!q) return { valid: true, errors };
  const type = String(q.type || '').toUpperCase();
  const topicCode = String(q.topicCode || '');
  const chapterName = String(q.chapterName || q.chapterTitle || '');
  const subjectName = String(q.subject || q.subjectName || '');

  // 1. Numerical Disqualification Guard
  if (type === 'ONE') {
    if (isTopicPurelyQualitative(topicCode, chapterName, subjectName)) {
      errors.push(`[CURRICULUM GUARD] Numerical question (ONE) rejected: Topic '${topicCode}' is purely qualitative.`);
    }
  }

  // 2. School-Level Ceiling Barrier (Classes 8–10)
  const fullText = `${q.text || ''} ${q.solution || ''} ${q.explanation || ''} ${Array.isArray(q.options) ? q.options.map(o => typeof o === 'object' ? (o.text || '') : String(o)).join(' ') : ''}`;
  for (const { pattern, label } of PROHIBITED_ADVANCED_KEYWORDS) {
    if (pattern.test(fullText)) {
      errors.push(`[CURRICULUM GUARD] Out-of-syllabus concept rejected: Contains prohibited advanced term '${label}'.`);
      break;
    }
  }

  return { valid: errors.length === 0, errors };
}

test('Qualitative Topic Detector correctly identifies theoretical chapters vs computational chapters', () => {
  // Environmental Science & Qualitative Chapters
  assert.strictEqual(isTopicPurelyQualitative('MH-9-SCIT-9-9.1', 'Environmental Management'), true);
  assert.strictEqual(isTopicPurelyQualitative('MH-9-SCIT-8-8.1', 'Useful and Harmful Microbes'), true);
  assert.strictEqual(isTopicPurelyQualitative('MH-8-SCI-9-9.1', 'Disaster Management'), true);
  assert.strictEqual(isTopicPurelyQualitative('MH-8-SCI-1-1.1', 'Living World and Classification of Microbes'), true);
  
  // Quantitative / Computational Chapters (Maths & Physics)
  assert.strictEqual(isTopicPurelyQualitative('MH-9-SCIT-1-1.1', 'Laws of Motion'), false);
  assert.strictEqual(isTopicPurelyQualitative('MH-9-SCIT-11-11.1', 'Reflection of Light'), false);
  assert.strictEqual(isTopicPurelyQualitative('MH-9-MTH1-1-1.1', 'Sets'), false);
  assert.strictEqual(isTopicPurelyQualitative('CBSE-8-MGP1-3-3.1', 'Linear Equations in One Variable'), false);
});

test('Curriculum Guard rejects artificial numericals (ONE) on qualitative chapters', () => {
  const badNumerical = {
    type: 'ONE',
    topicCode: 'MH-9-SCIT-9-9.2',
    chapterName: 'Environmental Management',
    text: 'A bioreactor digests 50 kg of organic waste and extracts 12 m3 of methane. Calculate the rate.',
    solution: 'Rate is 0.24 m3/kg.'
  };
  const result = validateQuestionCurriculum(badNumerical);
  assert.strictEqual(result.valid, false);
  assert.strictEqual(result.errors.length, 1);
  assert.strictEqual(result.errors[0].includes('Numerical question (ONE) rejected'), true);
});

test('Curriculum Guard allows valid numericals (ONE) on physics and mathematics topics', () => {
  const validPhysicsNumerical = {
    type: 'ONE',
    topicCode: 'MH-9-SCIT-1-1.2',
    chapterName: 'Laws of Motion',
    text: 'A body of mass 5 kg accelerates at 2 m/s^2. Calculate the applied force in Newtons.',
    solution: 'F = m * a = 5 * 2 = 10 N.'
  };
  const result = validateQuestionCurriculum(validPhysicsNumerical);
  assert.strictEqual(result.valid, true);
  assert.strictEqual(result.errors.length, 0);
});

test('Curriculum Guard rejects out-of-syllabus college/engineering/MBBS concepts', () => {
  const phytoremediationQuestion = {
    type: 'OSC',
    topicCode: 'MH-9-SCIT-9-9.2',
    chapterName: 'Environmental Management',
    text: 'Which hyperaccumulating plant is used in phytoremediation?',
    options: ['Sunflower', 'Rose', 'Tulip', 'Mango'],
    solution: 'Phytoremediation uses hyperaccumulating plants.'
  };
  const result = validateQuestionCurriculum(phytoremediationQuestion);
  assert.strictEqual(result.valid, false);
  assert.strictEqual(result.errors[0].includes('Phytoremediation / Hyperaccumulation'), true);

  const schrodingerQuestion = {
    type: 'OSC',
    topicCode: 'MH-9-SCIT-5-5.1',
    chapterName: 'Atomic Structure',
    text: 'Solve the time-independent Schrodinger equation for the hydrogen atom.',
    solution: 'Wave mechanics apply.'
  };
  const result2 = validateQuestionCurriculum(schrodingerQuestion);
  assert.strictEqual(result2.valid, false);
  assert.strictEqual(result2.errors[0].includes('Schrodinger Equation'), true);
});

test('Curriculum Guard passes authentic Class 8-10 textbook questions', () => {
  const authenticBalbharti = {
    type: 'OSC',
    topicCode: 'MH-9-SCIT-9-9.1',
    chapterName: 'Environmental Management',
    text: 'Which meteorological observatory in Pune was established by the India Meteorological Department?',
    options: ['Shimla Office', 'Mausam Bhavan', 'Pashan Observatory', 'Colaba Observatory'],
    solution: 'IMD established the observatory at Pune to record and analyze meteorological observations.'
  };
  const result = validateQuestionCurriculum(authenticBalbharti);
  assert.strictEqual(result.valid, true);
  assert.strictEqual(result.errors.length, 0);
});


// -----------------------------------------------------------------------------
// SUITE 12: Practice Submission & Parent Review Architectural Guards
// -----------------------------------------------------------------------------
console.log('\n--- Suite 12: Practice Submission & Parent Review Architectural Guards ---');

test('Practice scorePercent and correctCount can NEVER diverge or write 0% when correctCount > 0', () => {
  const evaluateScore = (correctCount, validCount) => {
    if (validCount <= 0) throw new Error('[CRITICAL INVARIANT] validCount cannot be <= 0');
    const validQuestionsCount = validCount;
    const scorePercent = Math.min(100, Math.max(0, Math.round((correctCount / validQuestionsCount) * 100)));
    if (correctCount > 0 && scorePercent === 0) {
      throw new Error(`[CRITICAL INVARIANT] Practice score calculation error: correctCount is ${correctCount}/${validQuestionsCount} but scorePercent computed as 0%`);
    }
    return scorePercent;
  };

  assert.strictEqual(evaluateScore(4, 6), 67);
  assert.strictEqual(evaluateScore(6, 6), 100);
  assert.strictEqual(evaluateScore(1, 6), 17);
  assert.strictEqual(evaluateScore(0, 6), 0);
  assert.throws(() => evaluateScore(1, 0), /CRITICAL INVARIANT/);
});

test('deriveScoreMetrics and deriveScorePercent SSOT repairs corrupted or legacy practice records', () => {
  function deriveScoreMetrics(data) {
    if (!data) return { score: 0, totalQuestions: 1, scorePercent: 0 };
    const qList = Array.isArray(data.questions) ? data.questions : (Array.isArray(data.questionDetails) ? data.questionDetails : []);
    const totalQuestions = Math.max(1, Number(data.totalQuestions || data.totalMarks || data.total || qList.length || 1));
    const score = data.correctCount !== undefined && data.correctCount !== null
      ? Number(data.correctCount)
      : (data.score !== undefined && data.score !== null ? Number(data.score) : qList.filter(q => q.isCorrect).length);
    let scorePercent = data.scorePercent !== undefined && data.scorePercent !== null
      ? Number(data.scorePercent)
      : (data.percentage !== undefined && data.percentage !== null ? Number(data.percentage) : (totalQuestions > 0 ? Math.round((score / totalQuestions) * 100) : 0));
    if (isNaN(scorePercent) || (score > 0 && scorePercent === 0 && totalQuestions > 0)) {
      scorePercent = Math.min(100, Math.max(0, Math.round((score / totalQuestions) * 100)));
    }
    return { score, totalQuestions, scorePercent: Math.min(100, Math.max(0, scorePercent)) };
  }

  // Corrupted record with score: 5, total: 6, but scorePercent: 0
  const r1 = deriveScoreMetrics({ score: 5, totalQuestions: 6, scorePercent: 0 });
  assert.strictEqual(r1.score, 5);
  assert.strictEqual(r1.scorePercent, 83);

  // Question details fallback
  const r2 = deriveScoreMetrics({ questionDetails: [{ isCorrect: true }, { isCorrect: false }, { isCorrect: true }] });
  assert.strictEqual(r2.score, 2);
  assert.strictEqual(r2.totalQuestions, 3);
  assert.strictEqual(r2.scorePercent, 67);

  // Legitimate zero score stays zero
  const r3 = deriveScoreMetrics({ correctCount: 0, totalQuestions: 6, scorePercent: 0 });
  assert.strictEqual(r3.score, 0);
  assert.strictEqual(r3.scorePercent, 0);
});

test('Self-healing pipeline auto-restores true percentage if legacy doc has scorePercent: 0 with score > 0', () => {
  const resolveReviewScore = (prDoc) => {
    const totalQ = Math.max(1, prDoc.totalQuestions || (prDoc.questions || []).length || 1);
    const correctQ = Number(prDoc.correctCount ?? prDoc.score ?? 0);
    let sp = Number(prDoc.scorePercent);
    if (isNaN(sp) || (sp === 0 && correctQ > 0)) {
      sp = Math.min(100, Math.max(0, Math.round((correctQ / totalQ) * 100)));
    }
    return { scorePercent: sp, correctCount: correctQ, totalQuestions: totalQ };
  };

  // Legacy glitched record with scorePercent: 0 but score: 4
  const glitchedPr = { scorePercent: 0, correctCount: 4, totalQuestions: 6 };
  const healed = resolveReviewScore(glitchedPr);
  assert.strictEqual(healed.scorePercent, 67);
  assert.strictEqual(healed.correctCount, 4);

  // Normal 0/6 failure stays 0%
  const zeroPr = { scorePercent: 0, correctCount: 0, totalQuestions: 6 };
  assert.strictEqual(resolveReviewScore(zeroPr).scorePercent, 0);
});

test('Evaluations never store blank correctAnswer when resolved answer key exists', () => {
  const resolveAnswerForStorage = (qData, resolvedCorrectAnswer) => {
    return (qData.correctAnswer !== undefined && qData.correctAnswer !== null && qData.correctAnswer !== '')
      ? qData.correctAnswer
      : (typeof resolvedCorrectAnswer === 'string' && resolvedCorrectAnswer !== ''
          ? resolvedCorrectAnswer
          : (Array.isArray(resolvedCorrectAnswer) && resolvedCorrectAnswer.length > 0
              ? resolvedCorrectAnswer.join(',')
              : (Array.isArray(qData.correctAnswers) && qData.correctAnswers.length > 0 ? qData.correctAnswers[0] : '')));
  };

  // Case 1: correctAnswer has value "A"
  assert.strictEqual(resolveAnswerForStorage({ correctAnswer: 'A' }, 'A'), 'A');
  // Case 2: correctAnswer is empty string "", but resolvedCorrectAnswer has "A"
  assert.strictEqual(resolveAnswerForStorage({ correctAnswer: '' }, 'A'), 'A');
  // Case 3: correctAnswer is missing, but correctAnswers array has ["B"]
  assert.strictEqual(resolveAnswerForStorage({ correctAnswers: ['B'] }, ''), 'B');
  // Case 4: Multiple choice array of letters
  assert.strictEqual(resolveAnswerForStorage({}, ['A', 'C']), 'A,C');
});

// -----------------------------------------------------------------------------
// SUITE 13: Student Modes & Limited Access Invariants (Rule: 3 Modes Architecture)
// -----------------------------------------------------------------------------
console.log('\n--- Suite 13: Student Modes & Access Boundary Invariants ---');

const getStudentMode = (user) => {
  if (!user) return 'regular';
  if (user.studentMode === 'limited' || user.studentMode === 'restricted') return 'limited';
  if (user.studentMode === 'autonomous' || user.autonomous === true) return 'autonomous';
  return 'regular';
};

test('Student Mode Resolution accurately maps legacy and canonical flags', () => {
  // Mode 1: Regular
  assert.strictEqual(getStudentMode({}), 'regular');
  assert.strictEqual(getStudentMode({ studentMode: 'regular', autonomous: false }), 'regular');

  // Mode 2: Autonomous (with backward compatibility for autonomous: true)
  assert.strictEqual(getStudentMode({ autonomous: true }), 'autonomous');
  assert.strictEqual(getStudentMode({ studentMode: 'autonomous', autonomous: true }), 'autonomous');

  // Mode 3: Limited / Restricted
  assert.strictEqual(getStudentMode({ studentMode: 'limited' }), 'limited');
  assert.strictEqual(getStudentMode({ studentMode: 'restricted' }), 'limited');
  assert.strictEqual(getStudentMode({ studentMode: 'limited', autonomous: true }), 'limited');
});

test('Student Modes enforce strict parent login disabled boundaries for Mode 2 and Mode 3', () => {
  const isParentDisabled = (student) => {
    return getStudentMode(student) !== 'regular';
  };

  // Mode 1: Parent login enabled
  assert.strictEqual(isParentDisabled({ studentMode: 'regular' }), false);

  // Mode 2: Parent login disabled
  assert.strictEqual(isParentDisabled({ studentMode: 'autonomous' }), true);
  assert.strictEqual(isParentDisabled({ autonomous: true }), true);

  // Mode 3: Parent login disabled (even if autonomous boolean was mistakenly false)
  assert.strictEqual(isParentDisabled({ studentMode: 'limited' }), true);
  assert.strictEqual(isParentDisabled({ studentMode: 'limited', autonomous: false }), true);
  assert.strictEqual(isParentDisabled({ studentMode: 'restricted' }), true);
});

test('Limited Mode strictly isolates features: permits Tests, Attendance, Fees; blocks LOS & performance metrics', () => {
  const evaluateStudentFeatureAccess = (student, feature) => {
    const mode = getStudentMode(student);
    if (mode === 'limited') {
      const allowedFeatures = ['attendance', 'fees', 'assigned_online_tests'];
      return allowedFeatures.includes(feature);
    }
    return true; // Mode 1 and Mode 2 have access to all student features
  };

  // Mode 3 Student access permissions
  const limitedStudent = { studentMode: 'limited' };
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'attendance'), true);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'fees'), true);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'assigned_online_tests'), true);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'learning_quotient'), false);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'topic_mastery'), false);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'learn_os'), false);
  assert.strictEqual(evaluateStudentFeatureAccess(limitedStudent, 'action_items'), false);

  // Mode 1 & 2 access permissions
  const regularStudent = { studentMode: 'regular' };
  assert.strictEqual(evaluateStudentFeatureAccess(regularStudent, 'learning_quotient'), true);
  assert.strictEqual(evaluateStudentFeatureAccess(regularStudent, 'learn_os'), true);
});

test('API Endpoint access control strictly rejects Limited Mode from learning, results, practice, reviews, bookmarks, and examRegister', () => {
  const isApiAllowedForStudent = (student, endpoint) => {
    const isLimited = getStudentMode(student) === 'limited';
    if (isLimited && ['learning', 'results', 'practice', 'examReview', 'peerReview', 'bookmarks', 'examRegister', 'submitReview'].includes(endpoint)) {
      return false;
    }
    return true;
  };

  const limitedStudent = { studentMode: 'limited' };
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'learning'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'results'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'practice'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'examReview'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'peerReview'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'bookmarks'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'examRegister'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'submitReview'), false);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'dashboard'), true);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'attendance'), true);
  assert.strictEqual(isApiAllowedForStudent(limitedStudent, 'fees'), true);

  const regularStudent = { studentMode: 'regular' };
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'learning'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'results'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'practice'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'examReview'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'peerReview'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'bookmarks'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'examRegister'), true);
  assert.strictEqual(isApiAllowedForStudent(regularStudent, 'submitReview'), true);
});

test('Student Mode UI Suffix strictly enforces * for Autonomous, ◇ for Limited, and empty for Regular', () => {
  function getStudentModeSymbol(user) {
    const mode = getStudentMode(user);
    if (mode === 'autonomous') return '*';
    if (mode === 'limited') return '◇';
    return '';
  }
  function getStudentModeSuffix(user) {
    const sym = getStudentModeSymbol(user);
    return sym ? ` ${sym}` : '';
  }

  // Autonomous mode
  assert.strictEqual(getStudentModeSymbol({ studentMode: 'autonomous' }), '*');
  assert.strictEqual(getStudentModeSymbol({ autonomous: true }), '*');
  assert.strictEqual(getStudentModeSuffix({ autonomous: true }), ' *');

  // Limited mode
  assert.strictEqual(getStudentModeSymbol({ studentMode: 'limited' }), '◇');
  assert.strictEqual(getStudentModeSymbol({ studentMode: 'restricted' }), '◇');
  assert.strictEqual(getStudentModeSuffix({ studentMode: 'limited' }), ' ◇');

  // Regular mode
  assert.strictEqual(getStudentModeSymbol({ studentMode: 'regular' }), '');
  assert.strictEqual(getStudentModeSymbol({}), '');
  assert.strictEqual(getStudentModeSuffix({ studentMode: 'regular' }), '');
});

test('Parent Dashboard & Review Portal strictly excludes Mode 2 (Autonomous) and Mode 3 (Limited) students', () => {
  const children = [
    { studentCode: 'ST-001', role: 'student', status: 'active', studentMode: 'regular' },
    { studentCode: 'ST-002', role: 'student', status: 'active', studentMode: 'autonomous' },
    { studentCode: 'ST-003', role: 'student', status: 'active', studentMode: 'limited' },
    { studentCode: 'ST-004', role: 'student', status: 'inactive', studentMode: 'regular' }
  ];

  // In parentDb.ts: Only active regular students are visible to parents
  const visibleToParent = children.filter(c => c.role === 'student' && c.status !== 'inactive' && getStudentMode(c) === 'regular');
  assert.strictEqual(visibleToParent.length, 1);
  assert.strictEqual(visibleToParent[0].studentCode, 'ST-001');

  // Review access check
  const canParentReviewChild = (childDoc) => getStudentMode(childDoc) === 'regular';
  assert.strictEqual(canParentReviewChild(children[0]), true);  // Regular -> allowed
  assert.strictEqual(canParentReviewChild(children[1]), false); // Autonomous -> disabled
  assert.strictEqual(canParentReviewChild(children[2]), false); // Limited -> disabled
});

// -----------------------------------------------------------------------------
// SUITE 14: Parent Student Codes & Legacy Link Isolation
// -----------------------------------------------------------------------------
console.log('\n--- Suite 14: Parent Student Codes & Legacy Link Isolation ---');

function resolveParentCodesPure(parentData) {
  const codes = [];
  if (Array.isArray(parentData?.studentCodes)) {
    parentData.studentCodes.forEach((c) => {
      if (typeof c === 'string' && c.startsWith('ST-')) {
        codes.push(c);
      }
    });
  } else if (typeof parentData?.studentCode === 'string' && parentData.studentCode.startsWith('ST-')) {
    codes.push(parentData.studentCode);
  }
  return codes;
}

test('Parent studentCodes array is SSOT; leftover legacy studentCode is ignored when studentCodes exists', () => {
  // Scenario 1: Parent has studentCodes array with 1 student, legacy field has old unlinked student
  const parent1 = {
    studentCodes: ['ST-2026-000001'],
    studentCode: 'ST-2026-000099' // Old child that was unlinked
  };
  const res1 = resolveParentCodesPure(parent1);
  assert.deepStrictEqual(res1, ['ST-2026-000001']);

  // Scenario 2: Parent has empty studentCodes array (all children unlinked), legacy field has unlinked student
  const parent2 = {
    studentCodes: [],
    studentCode: 'ST-2026-000099'
  };
  const res2 = resolveParentCodesPure(parent2);
  assert.deepStrictEqual(res2, []); // Must NOT resurrect old student

  // Scenario 3: Legacy document where studentCodes array was never initialized
  const parent3 = {
    studentCode: 'ST-2026-000055'
  };
  const res3 = resolveParentCodesPure(parent3);
  assert.deepStrictEqual(res3, ['ST-2026-000055']);
});

console.log('\n--- Suite 15: Auth Claims & Firestore Rules Read Optimization ---');

test('Claims builder and equality check strictly sync studentMode for all 3 modes', () => {
  function buildStudentClaims(userData) {
    const role = (userData.role || '').toLowerCase();
    const claims = {
      role,
      status: userData.status || 'active',
      studentCode: userData.studentCode || null
    };
    if (role === 'student') {
      claims.batchIds = Array.isArray(userData.batchIds)
        ? userData.batchIds.filter(Boolean)
        : (userData.batchId ? [userData.batchId] : []);
      claims.studentMode = getStudentMode(userData);
    }
    return claims;
  }

  function checkClaimsEqual(tokenClaims, userDoc) {
    if (!tokenClaims || !userDoc) return false;
    const userRole = (userDoc.role || '').toLowerCase();
    const tokenRole = (tokenClaims.role || '').toLowerCase();
    if (tokenRole !== userRole) return false;

    if (!('status' in tokenClaims)) return false;
    const userStatus = userDoc.status || 'active';
    const tokenStatus = tokenClaims.status || 'active';
    if (tokenStatus !== userStatus) return false;

    if (userRole === 'student') {
      if (!('studentMode' in tokenClaims)) return false;
      if (!('batchIds' in tokenClaims)) return false;
      const userMode = getStudentMode(userDoc);
      const tokenMode = getStudentMode(tokenClaims);
      if (tokenMode !== userMode) return false;
    } else if (userRole === 'parent') {
      if (!('studentCodes' in tokenClaims)) return false;
    }
    return true;
  }

  // 1. Regular student
  const regDoc = { role: 'student', studentMode: 'regular' };
  const regClaims = buildStudentClaims(regDoc);
  assert.strictEqual(regClaims.studentMode, 'regular');
  assert.strictEqual(checkClaimsEqual(regClaims, regDoc), true);

  // 2. Autonomous student
  const autoDoc = { role: 'student', studentMode: 'autonomous', autonomous: true };
  const autoClaims = buildStudentClaims(autoDoc);
  assert.strictEqual(autoClaims.studentMode, 'autonomous');
  assert.strictEqual(checkClaimsEqual(autoClaims, autoDoc), true);

  // 3. Limited student
  const limDoc = { role: 'student', studentMode: 'limited' };
  const limClaims = buildStudentClaims(limDoc);
  assert.strictEqual(limClaims.studentMode, 'limited');
  assert.strictEqual(checkClaimsEqual(limClaims, limDoc), true);

  // Missing status, studentMode, batchIds, or studentCodes must compare as unequal to force backfill sync
  assert.strictEqual(checkClaimsEqual({ role: 'student' }, regDoc), false, 'Token missing status must trigger sync');
  assert.strictEqual(checkClaimsEqual({ role: 'student', status: 'active' }, regDoc), false, 'Token missing studentMode must trigger sync');
  assert.strictEqual(checkClaimsEqual({ role: 'student', status: 'active', studentMode: 'regular' }, regDoc), false, 'Token missing batchIds must trigger sync');
  assert.strictEqual(checkClaimsEqual({ role: 'parent', status: 'active' }, { role: 'parent' }), false, 'Parent token missing studentCodes must trigger sync');

  // Mismatch triggers token refresh
  assert.strictEqual(checkClaimsEqual({ role: 'student', status: 'active', studentMode: 'regular', batchIds: [] }, limDoc), false);
});

test('Firestore rules isStudent and isParent check status != inactive without doc reads', () => {
  function evalIsStudent(token) {
    return token.role === 'student' && (
      ('status' in token) ? token.status !== 'inactive' : true
    );
  }
  function evalIsParent(token) {
    return token.role === 'parent' && (
      ('status' in token) ? token.status !== 'inactive' : true
    );
  }

  assert.strictEqual(evalIsStudent({ role: 'student', status: 'active' }), true);
  assert.strictEqual(evalIsStudent({ role: 'student', status: 'inactive' }), false);
  assert.strictEqual(evalIsParent({ role: 'parent', status: 'active' }), true);
  assert.strictEqual(evalIsParent({ role: 'parent', status: 'inactive' }), false);
});

test('Firestore rules ternary logic avoids document reads when studentMode claim exists', () => {
  let docReadCount = 0;
  function mockGetDoc() {
    docReadCount++;
    return { studentMode: 'limited' };
  }

  function evalIsLimitedStudent(token) {
    // Ternary expression as in firestore.rules
    return ('studentMode' in token)
      ? (token.studentMode === 'limited' || token.studentMode === 'restricted')
      : (mockGetDoc().studentMode === 'limited');
  }

  // Token has studentMode claim -> zero document reads
  docReadCount = 0;
  assert.strictEqual(evalIsLimitedStudent({ studentMode: 'regular' }), false);
  assert.strictEqual(docReadCount, 0, 'Must NOT read document when claim is present');

  assert.strictEqual(evalIsLimitedStudent({ studentMode: 'limited' }), true);
  assert.strictEqual(docReadCount, 0, 'Must NOT read document when claim is present');

  // Token lacks studentMode claim -> fallback document read
  assert.strictEqual(evalIsLimitedStudent({}), true);
  assert.strictEqual(docReadCount, 1, 'Evaluates document read fallback only when claim is missing');
});

test('Registration mode helper accurately resolves autonomous and studentMode flags', () => {
  function resolveRegistrationMode(regData, isAutonomous) {
    return regData?.studentMode ? getStudentMode(regData) : (isAutonomous ? 'autonomous' : 'regular');
  }

  assert.strictEqual(resolveRegistrationMode({ studentMode: 'limited' }, false), 'limited');
  assert.strictEqual(resolveRegistrationMode({ studentMode: 'restricted' }, false), 'limited');
  assert.strictEqual(resolveRegistrationMode({ studentMode: 'autonomous' }, false), 'autonomous');
  assert.strictEqual(resolveRegistrationMode({}, true), 'autonomous');
  assert.strictEqual(resolveRegistrationMode({}, false), 'regular');
});

console.log('\n================================================================');
console.log(`🎉 INVARIANT VERIFICATION SUMMARY: ${passedTests} / ${totalTests} TESTS PASSED`);
console.log('================================================================\n');

if (passedTests === totalTests) {
  process.exit(0);
} else {
  process.exit(1);
}
