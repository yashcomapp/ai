const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

async function main() {
  const jsonPath = path.join(__dirname, 'audit_data', 'mh10_scit1_ch9_missing.json');
  const questions = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  console.log(`Loaded ${questions.length} validated questions from ${jsonPath}`);

  // Rule Q: Mandatory pre-mutation snapshot
  await createPreMutationSnapshot(['syllabus', 'syllabusTopicIndex'], 'mh10_scit1_ch9_missing_questions');

  // 1. Batch write questions (chunks of 400)
  const nowIso = new Date().toISOString();
  for (let i = 0; i < questions.length; i += 400) {
    const chunk = questions.slice(i, i + 400);
    const batch = adminDb.batch();
    for (const q of chunk) {
      const ref = adminDb.collection('questions').doc(q.questionCode);
      batch.set(ref, {
        ...q,
        createdAt: nowIso,
        updatedAt: nowIso
      });
    }
    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / 400) + 1} (${chunk.length} questions)`);
  }

  // 2. Recompute exact question counts for MH-10-SCIT1-9-* and update syllabus/mh_10_scit1
  const qSnap = await adminDb.collection('questions')
    .where('topicCode', '>=', 'MH-10-SCIT1-9-')
    .where('topicCode', '<=', 'MH-10-SCIT1-9-\uf8ff')
    .select('topicCode', 'type', 'status', 'disputed')
    .get();

  const countsByTc = {};
  qSnap.forEach(d => {
    const data = d.data();
    if (data.status === 'quarantined' || data.disputed) return;
    const tc = data.topicCode;
    countsByTc[tc] = (countsByTc[tc] || 0) + 1;
  });

  const sylRef = adminDb.collection('syllabus').doc('mh_10_scit1');
  const sylSnap = await sylRef.get();
  if (!sylSnap.exists) {
    throw new Error('syllabus/mh_10_scit1 not found');
  }
  const sylData = sylSnap.data();
  const chapters = sylData.chapters || [];
  let totalSubjectObj = 0;

  for (const ch of chapters) {
    if (String(ch.number || ch.chapterNumber) === '9') {
      let chObj = 0;
      for (const topic of (ch.topics || [])) {
        if (Array.isArray(topic.subtopics) && topic.subtopics.length > 0) {
          for (const sub of topic.subtopics) {
            const code = sub.subtopicCode || sub.topicCode;
            const c = countsByTc[code] || 0;
            sub.objectiveCount = c;
            chObj += c;
          }
          topic.objectiveCount = 0;
        } else {
          const code = topic.topicCode;
          const c = countsByTc[code] || 0;
          topic.objectiveCount = c;
          chObj += c;
        }
      }
      ch.objectiveCount = chObj;
    }
    totalSubjectObj += Number(ch.objectiveCount || 0);
  }

  await sylRef.update({
    chapters,
    objectiveCount: totalSubjectObj,
    totalObjectiveQuestions: totalSubjectObj,
    updatedAt: nowIso
  });

  console.log('Updated syllabus/mh_10_scit1! Ch.9 counts:', JSON.stringify(countsByTc, null, 2));
  console.log('Total subject objectiveCount:', totalSubjectObj);
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
