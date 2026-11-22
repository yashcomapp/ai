const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function main() {
  console.log('Fetching questions...');
  const qSnap = await db.collection('questions').get();
  console.log(`Total questions in questions collection: ${qSnap.size}`);

  const sample = qSnap.docs.slice(0, 5).map(d => ({
    id: d.id,
    questionCode: d.data().questionCode,
    topicCode: d.data().topicCode,
    board: d.data().board,
    class: d.data().class,
    subjectCode: d.data().subjectCode,
    subject: d.data().subject
  }));
  console.log('Sample questions:', JSON.stringify(sample, null, 2));

  const questionsByTopic = new Map();
  const questionsBySubjectKey = new Map();

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const tCode = q.topicCode;
    if (tCode) {
      questionsByTopic.set(tCode, (questionsByTopic.get(tCode) || 0) + 1);

      // Canonical topicCode: ${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}
      const parts = tCode.split('-');
      if (parts.length >= 3) {
        const canonicalSubjKey = `${parts[0]}-${parts[1]}-${parts[2]}`;
        questionsBySubjectKey.set(canonicalSubjKey, (questionsBySubjectKey.get(canonicalSubjKey) || 0) + 1);
      }
    }
  });

  console.log('Fetching syllabus documents...');
  const sylSnap = await db.collection('syllabus').get();
  console.log(`Total syllabus documents: ${sylSnap.size}`);

  const subjectSummary = [];
  const zeroTopicsBySubject = [];

  for (const doc of sylSnap.docs) {
    const data = doc.data();
    const bCode = data.boardCode || (data.board === 'CBSE' ? 'CBSE' : 'MH');
    const classNum = String(data.class);
    const subjectCode = data.subjectCode;
    const subjectName = data.subject || data.name || subjectCode;
    const subjKey = `${bCode}-${classNum}-${subjectCode}`;

    const chapters = data.chapters || [];
    let totalTopics = 0;
    let topicsWithQuestions = 0;
    let topicsWithZeroQuestions = 0;
    let totalQuestionsCount = questionsBySubjectKey.get(subjKey) || 0;

    const zeroTopics = [];
    const partialTopics = [];

    chapters.forEach(ch => {
      const chNum = String(ch.number);
      const chTitle = ch.title || ch.name || `Chapter ${chNum}`;
      const topics = ch.topics || [];

      topics.forEach((t, tIdx) => {
        const isObj = t && typeof t === 'object';
        const tNum = isObj ? String(t.number || `${chNum}.${tIdx + 1}`) : `${chNum}.${tIdx + 1}`;
        const tName = isObj ? (t.name || t.title || '') : String(t);
        const tCode = isObj && t.topicCode ? t.topicCode : `${bCode}-${classNum}-${subjectCode}-${chNum}-${tNum}`;

        // Check if topic has subtopics
        const subtopics = (isObj && Array.isArray(t.subtopics) && t.subtopics.length > 0) ? t.subtopics : null;

        if (subtopics) {
          subtopics.forEach((st, stIdx) => {
            totalTopics++;
            const isStObj = st && typeof st === 'object';
            const stNum = isStObj ? String(st.number || `${tNum}.${stIdx + 1}`) : `${tNum}.${stIdx + 1}`;
            const stName = isStObj ? (st.name || st.title || '') : String(st);
            const stCode = isStObj && st.topicCode ? st.topicCode : `${bCode}-${classNum}-${subjectCode}-${chNum}-${stNum}`;

            const qCount = questionsByTopic.get(stCode) || 0;
            if (qCount === 0) {
              topicsWithZeroQuestions++;
              zeroTopics.push({
                topicCode: stCode,
                chapterNumber: chNum,
                chapterTitle: chTitle,
                topicNumber: stNum,
                name: stName,
                questionsCount: 0
              });
            } else {
              topicsWithQuestions++;
              if (qCount < 80) {
                partialTopics.push({
                  topicCode: stCode,
                  chapterNumber: chNum,
                  chapterTitle: chTitle,
                  topicNumber: stNum,
                  name: stName,
                  questionsCount: qCount
                });
              }
            }
          });
        } else {
          totalTopics++;
          const qCount = questionsByTopic.get(tCode) || 0;
          if (qCount === 0) {
            topicsWithZeroQuestions++;
            zeroTopics.push({
              topicCode: tCode,
              chapterNumber: chNum,
              chapterTitle: chTitle,
              topicNumber: tNum,
              name: tName,
              questionsCount: 0
            });
          } else {
            topicsWithQuestions++;
            if (qCount < 80) {
              partialTopics.push({
                topicCode: tCode,
                chapterNumber: chNum,
                chapterTitle: chTitle,
                topicNumber: tNum,
                name: tName,
                questionsCount: qCount
              });
            }
          }
        }
      });
    });

    subjectSummary.push({
      subjKey,
      board: bCode,
      classNum,
      subjectCode,
      subjectName,
      totalChapters: chapters.length,
      totalTopics,
      topicsWithQuestions,
      topicsWithZeroQuestions,
      totalQuestionsCount,
      zeroTopics,
      partialTopics
    });
  }

  // Also check if there are topics in syllabusTopicIndex
  console.log('\n--- SUBJECT-LEVEL QUESTION COVERAGE ---');
  subjectSummary.sort((a, b) => a.subjKey.localeCompare(b.subjKey));
  
  const subjectsWithZeroQuestions = [];
  const subjectsWithPartialQuestions = [];
  const subjectsWithFullQuestions = [];

  subjectSummary.forEach(s => {
    console.log(`\n📚 [${s.subjKey}] ${s.subjectName}:`);
    console.log(`   Total Chapters: ${s.totalChapters}, Total Topics/Subtopics: ${s.totalTopics}`);
    console.log(`   Total Questions in Bank: ${s.totalQuestionsCount}`);
    console.log(`   Topics with Questions: ${s.topicsWithQuestions} / ${s.totalTopics}`);
    console.log(`   Topics with 0 Questions: ${s.topicsWithZeroQuestions} / ${s.totalTopics}`);
    if (s.totalQuestionsCount === 0) {
      subjectsWithZeroQuestions.push(s);
    } else if (s.topicsWithZeroQuestions > 0 || s.partialTopics.length > 0) {
      subjectsWithPartialQuestions.push(s);
    } else {
      subjectsWithFullQuestions.push(s);
    }
  });

  console.log('\n======================================================');
  console.log(`TOTAL SUBJECTS: ${subjectSummary.length}`);
  console.log(`SUBJECTS WITH ZERO QUESTIONS AT ALL: ${subjectsWithZeroQuestions.length}`);
  subjectsWithZeroQuestions.forEach(s => {
    console.log(` - ${s.subjKey}: ${s.subjectName} (${s.totalTopics} topics)`);
  });

  console.log(`\nSUBJECTS WITH SOME ZERO-QUESTION TOPICS:`);
  subjectsWithPartialQuestions.forEach(s => {
    if (s.topicsWithZeroQuestions > 0) {
      console.log(` - ${s.subjKey}: ${s.subjectName} -> ${s.topicsWithZeroQuestions}/${s.totalTopics} topics have 0 questions`);
    }
  });

  // Write detailed JSON for exact topic-level inspection
  fs.writeFileSync(
    path.join(__dirname, 'zero_questions_audit_result.json'),
    JSON.stringify(subjectSummary, null, 2),
    'utf-8'
  );
  console.log('\nFull detailed audit saved to scripts/zero_questions_audit_result.json');
}

main().catch(console.error);
