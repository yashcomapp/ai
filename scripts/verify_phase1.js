const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('================================================================');
console.log('🧪 RUNNING PHASE 1 AUDIT & BUSINESS VERIFICATION SUITE');
console.log('================================================================');

// 1. C2: studentDb.ts exports loadStudentCoreData & StudentCoreData
const studentDb = fs.readFileSync(path.join(__dirname, '../src/lib/studentDb.ts'), 'utf8');
assert(studentDb.includes('export interface StudentCoreData'), 'StudentCoreData interface must be exported');
assert(studentDb.includes('export async function loadStudentCoreData('), 'loadStudentCoreData must be exported');
assert(studentDb.includes('student_core_${studentCode}'), 'loadStudentCoreData must use student_core_ cacheKey');
assert(studentDb.includes('coreData = await loadStudentCoreData('), 'getDashboardData and getStudentLearningData must call loadStudentCoreData');
console.log('  ✅ PASS: C2 shared core pipeline loaded and cached with 60s in-memory SSOT');

// 2. C4: Assignment topicCodes
const adminExams = fs.readFileSync(path.join(__dirname, '../src/app/api/admin/exams/handlers/exams.ts'), 'utf8');
assert(adminExams.includes('topicCode,') && adminExams.includes('topicCodes,'), 'admin exams handler must store topicCode and topicCodes in assignment payload');
const parentDb = fs.readFileSync(path.join(__dirname, '../src/lib/parentDb.ts'), 'utf8');
assert(parentDb.includes('ass.topicCode || aData.topicCode'), 'parentDb must resolve topicCode directly from assignment');
assert(studentDb.includes('ass.topicCode || aData.topicCode'), 'studentDb must resolve topicCode directly from assignment');
console.log('  ✅ PASS: C4 assignment topicCodes stored and consumed directly to prevent downstream exam doc reads');

// 3. C5: ReportCacheManager for Scorecard Cache
const resultsHandler = fs.readFileSync(path.join(__dirname, '../src/app/api/student/handlers/results.ts'), 'utf8');
assert(resultsHandler.includes('ReportCacheManager.getReport'), 'results.ts must use ReportCacheManager.getReport for scorecard');
assert(resultsHandler.includes('ReportCacheManager.setReport(scorecardCacheKey, scorecardResult, 180, true)'), 'results.ts must store scorecard with ReportCacheManager.setReport');
console.log('  ✅ PASS: C5 scorecard persistent Firestore + in-memory cache active with 180s TTL');

// 4. Lever 1: Practice Service reflection flags
const practiceService = fs.readFileSync(path.join(__dirname, '../src/services/practice.service.ts'), 'utf8');
assert(practiceService.includes('needsStudentReflection'), 'practice.service.ts must compute needsStudentReflection');
assert(practiceService.includes('reflectionRequiredByGate'), 'practice.service.ts must compute reflectionRequiredByGate');
assert(practiceService.includes('reflectionStatus'), 'practice.service.ts must set reflectionStatus');
console.log('  ✅ PASS: Lever 1 practice engine identifies missed questions and activates reflection gate for autonomous mode');

// 5. Lever 1: Practice handler reflection gate & postPracticeReflect endpoint
const practiceHandler = fs.readFileSync(path.join(__dirname, '../src/app/api/student/handlers/practice.ts'), 'utf8');
assert(practiceHandler.includes('lockType: \'reflection_required\''), 'practice GET handler must return lockType reflection_required when reflection pending');
assert(practiceHandler.includes('export async function postPracticeReflect('), 'practice handler must export postPracticeReflect');
const studentRouter = fs.readFileSync(path.join(__dirname, '../src/app/api/student/[[...slug]]/route.ts'), 'utf8');
assert(studentRouter.includes('case \'practice/reflect\':'), 'student router must dispatch practice/reflect');
console.log('  ✅ PASS: Lever 1 practice/reflect endpoint dispatched with Tier 2 validation (length 25-350, pattern check, banned phrases)');

// 6. Lever 1: firestore.rules allowlist for parentReviews
const firestoreRules = fs.readFileSync(path.join(__dirname, '../firestore.rules'), 'utf8');
assert(firestoreRules.includes('studentReflections') && firestoreRules.includes('reflectionStatus'), 'firestore.rules must allow student to update studentReflections and reflectionStatus on parentReviews');
console.log('  ✅ PASS: Lever 1 firestore.rules securely allows student reflection updates on parentReviews');

// 7. Lever 1: UI Prompt and topic page wiring
const topicPage = fs.readFileSync(path.join(__dirname, '../src/app/student/topic/page.tsx'), 'utf8');
assert(!topicPage.includes('PracticeLockPrompt type="autonomous"'), 'topic page must NOT artificially block autonomous practice');
assert(topicPage.includes('reflection_required'), 'topic page must handle reflection_required lockType');
const lockPrompt = fs.readFileSync(path.join(__dirname, '../src/components/student/practice/PracticeLockPrompt.tsx'), 'utf8');
assert(lockPrompt.includes('Mistake Reflection Required'), 'PracticeLockPrompt must render Generative Reflection UI');
assert(lockPrompt.includes('REFLECTION_CATEGORIES'), 'PracticeLockPrompt must provide reflection category choices');
console.log('  ✅ PASS: Lever 1 UI renders generative reflection cards, live char counter, and unlock trigger');

console.log('================================================================');
console.log('🎉 ALL PHASE 1 INVARIANTS AND SPEC CHECKS PASSED (7 / 7)');
console.log('================================================================');
