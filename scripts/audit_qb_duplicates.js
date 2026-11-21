// scripts/audit_qb_duplicates.js
// Audits questions in Firestore for duplicate or plagiarized questions.
// Usage: node scripts/audit_qb_duplicates.js [subjectCode] [class] [board]

const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { areQuestionsTooSimilar } = require('../src/lib/questionSimilarity.ts');

const targetSubject = process.argv[2] || 'MTH2';
const targetClass = process.argv[3] || '9';
const targetBoard = process.argv[4] || 'MH';

async function main() {
  console.log(`=== Auditing Duplicates for ${targetBoard}-${targetClass}-${targetSubject} ===`);

  const snap = await adminDb.collection('questions')
    .where('boardCode', '==', targetBoard)
    .where('class', '==', targetClass)
    .where('subjectCode', '==', targetSubject)
    .get();

  console.log(`Fetched ${snap.size} total questions.`);
  if (snap.size === 0) return;

  const questions = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));

  // Group by topicCode
  const byTopic = {};
  questions.forEach(q => {
    const tc = q.topicCode || 'unknown';
    if (!byTopic[tc]) byTopic[tc] = [];
    byTopic[tc].push(q);
  });

  const topicCodes = Object.keys(byTopic).sort();
  console.log(`Total Topics/Subtopics: ${topicCodes.length}`);

  let totalDuplicatePairs = 0;
  let problematicTopics = 0;

  for (const tc of topicCodes) {
    const list = byTopic[tc];
    const duplicates = [];

    for (let i = 0; i < list.length; i++) {
      for (let j = i + 1; j < list.length; j++) {
        if (areQuestionsTooSimilar(list[i], list[j])) {
          duplicates.push({ q1: list[i].questionCode || list[i].id, q2: list[j].questionCode || list[j].id });
        }
      }
    }

    const uniqueCount = list.length - duplicates.length;
    const uniquenessPct = list.length > 0 ? ((uniqueCount / list.length) * 100).toFixed(1) : '100';

    if (duplicates.length > 0) {
      problematicTopics++;
      totalDuplicatePairs += duplicates.length;
      console.log(`❌ ${tc.padEnd(25)}: ${duplicates.length} duplicate pairs out of ${list.length} questions (${uniquenessPct}% unique)`);
    } else {
      console.log(`✓ ${tc.padEnd(25)}: 0 duplicates (${list.length} questions, 100% unique)`);
    }
  }

  console.log('\n================ AUDIT SUMMARY ================');
  console.log(`Total Subtopics: ${topicCodes.length}`);
  console.log(`Problematic Subtopics with duplicates: ${problematicTopics}`);
  console.log(`Total Duplicate Pairs Detected: ${totalDuplicatePairs}`);
}

main().catch(err => {
  console.error('Audit failed:', err);
  process.exit(1);
});
