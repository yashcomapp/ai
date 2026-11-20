const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

async function runAudit() {
  console.log('=== AUDITING PRACTICE VAULT QUESTIONS ACROSS ALL CLASSES & SUBJECTS ===\n');

  // Fetch all questions
  console.log('Fetching all questions from Firestore...');
  const questionsSnap = await db.collection('questions').get();
  console.log(`Total questions in Question Bank: ${questionsSnap.size}`);

  // Group questions by topicCode, subtopicCode, parentTopicCode, and vault
  // Notice: practice vault includes: q.vault === 'practice'
  const practiceByCode = {};
  const totalByCode = {};

  questionsSnap.docs.forEach(doc => {
    const q = doc.data();
    const vault = String(q.vault || '').trim().toLowerCase();
    const isPractice = (vault === 'practice');

    const codes = new Set();
    if (q.topicCode) codes.add(q.topicCode);
    if (q.subtopicCode) codes.add(q.subtopicCode);
    if (q.parentTopicCode) codes.add(q.parentTopicCode);

    codes.forEach(c => {
      totalByCode[c] = (totalByCode[c] || 0) + 1;
      if (isPractice) {
        practiceByCode[c] = (practiceByCode[c] || 0) + 1;
      }
    });
  });

  // Fetch all syllabus documents
  console.log('Fetching all syllabus documents...');
  const syllabusSnap = await db.collection('syllabus').get();
  console.log(`Found ${syllabusSnap.size} syllabus documents.`);

  const deficitReport = [];

  syllabusSnap.docs.forEach(sylDoc => {
    const sdata = sylDoc.data();
    const boardCode = sdata.boardCode || sdata.board;
    const classNum = sdata.class;
    const subjectCode = sdata.subjectCode;
    const subjectName = sdata.subject;

    (sdata.chapters || []).forEach(ch => {
      (ch.topics || []).forEach(t => {
        const topCode = t.topicCode;
        const topPractice = practiceByCode[topCode] || 0;
        const topTotal = totalByCode[topCode] || 0;

        const subtopics = t.subtopics || [];

        if (subtopics.length > 0) {
          // Check each subtopic
          subtopics.forEach(st => {
            const stCode = st.topicCode;
            const stPractice = practiceByCode[stCode] || 0;
            const stTotal = totalByCode[stCode] || 0;

            if (stPractice < 20) {
              deficitReport.push({
                level: 'subtopic',
                boardCode,
                classNum,
                subjectCode,
                subjectName,
                chapterNumber: ch.number,
                chapterName: ch.name,
                parentTopicCode: topCode,
                parentTopicName: t.name,
                code: stCode,
                number: st.number,
                name: st.name,
                practiceCount: stPractice,
                totalCount: stTotal,
                deficit: 20 - stPractice
              });
            }
          });
        } else {
          // No subtopics, check topic directly
          if (topPractice < 20) {
            deficitReport.push({
              level: 'topic',
              boardCode,
              classNum,
              subjectCode,
              subjectName,
              chapterNumber: ch.number,
              chapterName: ch.name,
              parentTopicCode: topCode,
              parentTopicName: t.name,
              code: topCode,
              number: t.number,
              name: t.name,
              practiceCount: topPractice,
              totalCount: topTotal,
              deficit: 20 - topPractice
            });
          }
        }
      });
    });
  });

  console.log(`\n======================================================`);
  console.log(`TOTAL TOPICS/SUBTOPICS WITH < 20 PRACTICE QUESTIONS: ${deficitReport.length}`);
  console.log(`======================================================\n`);

  // Group by Subject
  const bySubject = {};
  deficitReport.forEach(d => {
    const key = `${d.boardCode} Class ${d.classNum} - ${d.subjectName} (${d.subjectCode})`;
    if (!bySubject[key]) bySubject[key] = [];
    bySubject[key].push(d);
  });

  Object.entries(bySubject).forEach(([subj, items]) => {
    console.log(`\n📘 ${subj}: ${items.length} items with < 20 practice questions:`);
    items.forEach(it => {
      console.log(`   - [${it.code}] Ch.${it.chapterNumber} ${it.number} "${it.name}" -> Practice: ${it.practiceCount}/20 (Total Qs: ${it.totalCount}, Deficit: +${it.deficit})`);
    });
  });

  fs.writeFileSync(path.join(__dirname, 'practice_deficits_report.json'), JSON.stringify(deficitReport, null, 2));
  console.log(`\nSaved detailed deficit report to scripts/practice_deficits_report.json`);
}

runAudit().then(() => process.exit(0)).catch(e => {
  console.error(e);
  process.exit(1);
});
