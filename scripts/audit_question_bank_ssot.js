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

async function runAudit() {
  console.log('=== 1. AUDIT SYLLABUS COLLECTION ===');
  const syllSnap = await db.collection('syllabus').get();
  console.log(`Total Syllabus Docs: ${syllSnap.size}`);
  const syllabusMap = {}; // key: `${boardCode}-${classNum}-${subjectCode}` -> doc
  const syllabusByBoardClassSubjName = {}; // key: `${boardCode}-${classNum}-${subjectName.toLowerCase()}` -> canonical subjectCode

  syllSnap.docs.forEach(doc => {
    const d = doc.data();
    console.log(`- Doc [${doc.id}]: board='${d.board}', boardCode='${d.boardCode}', class='${d.class}', subject='${d.subject}', subjectCode='${d.subjectCode}', chapters=${(d.chapters||[]).length}`);
    const key = `${d.boardCode}-${d.class}-${d.subjectCode}`;
    syllabusMap[key] = { id: doc.id, ...d };
    const nameKey = `${d.boardCode}-${String(d.class).replace(/\D/g,'')}-${String(d.subject).trim().toLowerCase()}`;
    syllabusByBoardClassSubjName[nameKey] = d.subjectCode;
  });

  console.log('\n=== 2. AUDIT ALL QUESTIONS IN QUESTION BANK ===');
  const qSnap = await db.collection('questions').get();
  console.log(`Total Question Docs: ${qSnap.size}`);

  const discrepancies = [];
  const subjectCodeHistogram = {};
  const boardHistogram = {};
  const classHistogram = {};
  const codePatternIssues = [];
  const topicCodeMismatches = [];

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const docId = doc.id;
    const qCode = q.questionCode || '';
    const tCode = q.topicCode || '';
    const board = q.board || '';
    const boardCode = q.boardCode || '';
    const cls = q.class;
    const subj = q.subject || '';
    const subjCode = q.subjectCode || '';
    const chNum = q.chapterNumber;
    const tNum = q.topicNumber;
    const qType = q.type || '';

    // Histograms
    boardHistogram[boardCode || board || 'MISSING'] = (boardHistogram[boardCode || board || 'MISSING'] || 0) + 1;
    classHistogram[String(cls)] = (classHistogram[String(cls)] || 0) + 1;
    const scKey = `${boardCode || 'NO_BOARD'}-${cls}-${subjCode || 'NO_SUBJ_CODE'}`;
    subjectCodeHistogram[scKey] = (subjectCodeHistogram[scKey] || 0) + 1;

    // Check if docId != questionCode
    if (docId !== qCode) {
      discrepancies.push({ type: 'DOCID_MISMATCH', docId, qCode });
    }

    // Check class type (string vs number)
    if (typeof cls !== 'string') {
      discrepancies.push({ type: 'CLASS_TYPE_NOT_STRING', docId, class: cls, typeofClass: typeof cls });
    }

    // Check if boardCode is canonical ('CBSE' or 'MH')
    if (boardCode !== 'CBSE' && boardCode !== 'MH') {
      discrepancies.push({ type: 'NON_CANONICAL_BOARD_CODE', docId, boardCode, board });
    }

    // Check questionCode format: ${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}
    const qCodeParts = qCode.split('-');
    if (qCodeParts.length < 7) {
      codePatternIssues.push({ docId, qCode, reason: 'Less than 7 hyphen-separated segments' });
    } else {
      const [bPart, cPart, sPart, chPart, tPart, typePart, seqPart] = qCodeParts;
      if (bPart !== boardCode) {
        codePatternIssues.push({ docId, qCode, reason: `Board code mismatch in qCode: '${bPart}' vs '${boardCode}'` });
      }
      if (cPart !== String(cls).replace(/\D/g, '')) {
        codePatternIssues.push({ docId, qCode, reason: `Class mismatch in qCode: '${cPart}' vs '${cls}'` });
      }
      if (sPart !== subjCode) {
        codePatternIssues.push({ docId, qCode, reason: `SubjectCode mismatch in qCode: '${sPart}' vs '${subjCode}'` });
      }
    }

    // Check topicCode format: ${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}
    const expectedTopicCode = `${boardCode}-${String(cls).replace(/\D/g, '')}-${subjCode}-${String(chNum).replace(/\D/g, '')}-${String(tNum).trim()}`;
    if (tCode !== expectedTopicCode) {
      topicCodeMismatches.push({ docId, tCode, expectedTopicCode, qCode });
    }
  });

  console.log('\n--- Board Histogram ---', boardHistogram);
  console.log('\n--- Class Histogram ---', classHistogram);
  console.log('\n--- Board-Class-SubjectCode Histogram ---', subjectCodeHistogram);
  console.log(`\nDiscrepancies Count: ${discrepancies.length}`);
  console.log(`Code Pattern Issues Count: ${codePatternIssues.length}`);
  console.log(`Topic Code Mismatches Count: ${topicCodeMismatches.length}`);

  if (discrepancies.length > 0) {
    console.log('Sample Discrepancies (first 10):', discrepancies.slice(0, 10));
  }
  if (codePatternIssues.length > 0) {
    console.log('Sample Code Pattern Issues (first 10):', codePatternIssues.slice(0, 10));
  }
  if (topicCodeMismatches.length > 0) {
    console.log('Sample Topic Code Mismatches (first 10):', topicCodeMismatches.slice(0, 10));
  }

  // Check syllabusTopicIndex count and compare with questions
  console.log('\n=== 3. AUDIT SYLLABUS TOPIC INDEX ===');
  const indexSnap = await db.collection('syllabusTopicIndex').get();
  console.log(`Total syllabusTopicIndex Docs: ${indexSnap.size}`);
  const indexSample = indexSnap.docs.slice(0, 5).map(d => ({ id: d.id, ...d.data() }));
  console.log('Sample index docs:', indexSample);
}

runAudit().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
