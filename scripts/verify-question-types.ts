import { 
  evaluateQuestionAnswer, 
  toCanonicalQuestionType, 
  isObjectiveType, 
  isSubjectiveType, 
  isMultipleChoiceType, 
  isSingleChoiceType, 
  isTrueFalseType, 
  isAssertionReasonType, 
  isNumericalType, 
  isFillBlanksType, 
  QUESTION_TYPE_MAP 
} from '../src/lib/questionTypes';

console.log('--- 1. Testing Canonical Types ---');
const canonicals = ['OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE', 'SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'];
for (const c of canonicals) {
  if (toCanonicalQuestionType(c) !== c) throw new Error(`Mismatch on ${c}`);
  console.log(`✓ Canonical type ${c} verified`);
}

console.log('--- 2. Testing Legacy Aliases ---');
const legacyTests = [
  ['single_mcq', 'OSC'],
  ['multiple_mcq', 'OMC'],
  ['true_false', 'OTF'],
  ['assertion_reason', 'OAR'],
  ['numerical', 'ONE'],
  ['numerical_short', 'SSN'],
  ['numerical_long', 'SLN'],
  ['subjective_short', 'SSA'],
  ['subjective_long', 'SLA'],
  ['subjective_reason', 'SSR'],
  ['subjective_notes', 'SSR'],
  ['subjective_define', 'SDF'],
  ['subjective_laws', 'SLP']
];

for (const [legacy, canonical] of legacyTests) {
  if (toCanonicalQuestionType(legacy) !== canonical) {
    throw new Error(`Legacy alias ${legacy} -> expected ${canonical}, got ${toCanonicalQuestionType(legacy)}`);
  }
  console.log(`✓ Legacy alias "${legacy}" mapped to ${canonical}`);
}

console.log('--- 3. Testing evaluateQuestionAnswer ---');
// OSC (Single Choice)
const oscPass = evaluateQuestionAnswer('OSC', 'B', 'Option B', ['Option A', 'Option B', 'Option C', 'Option D']);
if (!oscPass) throw new Error('OSC evaluation failed');
console.log('✓ OSC (Single Choice) evaluation passed');

// OMC (Multiple Choice)
const omcPass = evaluateQuestionAnswer('OMC', ['A', 'C'], ['Option A', 'Option C'], ['Option A', 'Option B', 'Option C', 'Option D']);
if (!omcPass) throw new Error('OMC evaluation passed');
console.log('✓ OMC (Multiple Choice) evaluation passed');

// OTF (True / False)
const otfPass1 = evaluateQuestionAnswer('OTF', 'True', 'true');
const otfPass2 = evaluateQuestionAnswer('OTF', 'T', 'true');
if (!otfPass1 || !otfPass2) throw new Error('OTF evaluation failed');
console.log('✓ OTF (True/False) evaluation passed');

// OAR (Assertion & Reason)
const oarPass = evaluateQuestionAnswer('OAR', 'A', 'A');
if (!oarPass) throw new Error('OAR evaluation failed');
console.log('✓ OAR (Assertion & Reason) evaluation passed');

// OFB (Fill in the Blanks)
const ofbPass = evaluateQuestionAnswer('OFB', 'Photosynthesis', 'photosynthesis');
if (!ofbPass) throw new Error('OFB evaluation failed');
console.log('✓ OFB (Fill in Blanks) evaluation passed');

// ONE (Numerical Objective)
const onePass = evaluateQuestionAnswer('ONE', '9.80', '9.81');
if (!onePass) throw new Error('ONE evaluation failed');
console.log('✓ ONE (Numerical Objective) evaluation passed');

console.log('\n======================================');
console.log('ALL QUESTION TYPE SSOT TESTS PASSED!');
console.log('======================================');
