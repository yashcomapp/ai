const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

// Load environment variables
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

// SSOT Canonical Helpers
function getCanonicalBoardCode(board) {
  const b = String(board || '').toUpperCase();
  if (b.includes('CBSE')) return 'CBSE';
  return 'MH';
}

function getCanonicalBoardName(board) {
  const code = getCanonicalBoardCode(board);
  return code === 'CBSE' ? 'CBSE' : 'Maharashtra Board';
}

function getCanonicalClass(classNum) {
  const clean = String(classNum || '8').replace(/\D/g, '');
  return clean || '8';
}

function getCanonicalSubjectCode(board, classNum, subjectNameOrCode) {
  const bCode = getCanonicalBoardCode(board);
  const cls = getCanonicalClass(classNum);
  const upper = String(subjectNameOrCode || '').trim().toUpperCase();

  // 1. Direct match on known canonical subject codes
  if (bCode === 'CBSE') {
    if (cls === '8' && (upper === 'MGP1' || upper === 'MGP2' || upper === 'CURI')) return upper;
    if (cls === '9' && (upper === 'MGM' || upper === 'SCIE')) return upper;
    if (cls === '10' && (upper === 'MATH' || upper === 'SCI')) return upper;
  } else if (bCode === 'MH') {
    if (cls === '8' && (upper === 'MTH' || upper === 'SCI')) return upper;
    if (cls === '9' && (upper === 'MTH1' || upper === 'MTH2' || upper === 'SCIT')) return upper;
    if (cls === '10' && (upper === 'MTH1' || upper === 'MTH2' || upper === 'SCIT1' || upper === 'SCIT2')) return upper;
  }

  // 2. Normalized lowercase alphanumeric matching
  const s = String(subjectNameOrCode || '').toLowerCase().replace(/[\s\-_():]+/g, '');

  if (bCode === 'CBSE') {
    if (cls === '8') {
      if (s.includes('mgp2') || s.includes('part2') || s.includes('p2') || s.includes('2')) return 'MGP2';
      if (s.includes('curi') || s.includes('sci')) return 'CURI';
      return 'MGP1';
    }
    if (cls === '9') {
      if (s.includes('sci') || s.includes('scie') || s.includes('exploration')) return 'SCIE';
      return 'MGM';
    }
    if (cls === '10') {
      if (s.includes('sci')) return 'SCI';
      return 'MATH';
    }
  }

  // MH (Maharashtra Board)
  if (cls === '8') {
    if (s.includes('sci')) return 'SCI';
    return 'MTH';
  }
  if (cls === '9') {
    if (s.includes('sci') || s.includes('scit')) return 'SCIT';
    if (s.includes('geometry') || s.includes('mth2') || s.includes('part2') || s.includes('2')) return 'MTH2';
    return 'MTH1';
  }
  if (cls === '10') {
    if (s.includes('sci') || s.includes('technology') || s.includes('scit')) {
      if (s.includes('2') || s.includes('part2') || s.includes('scit2')) return 'SCIT2';
      return 'SCIT1';
    }
    if (s.includes('geometry') || s.includes('mth2') || s.includes('part2') || s.includes('2')) return 'MTH2';
    return 'MTH1';
  }

  return 'MTH';
}


function extractChapterFromTopic(topicNumber, fallbackChapter) {
  const tStr = String(topicNumber || '').trim();
  const match = tStr.match(/^(\d+)\./);
  if (match && match[1]) {
    return match[1];
  }
  const cleanFb = String(fallbackChapter || '1').replace(/\D/g, '');
  return cleanFb || '1';
}

function getCanonicalTopicCode(board, classNum, subjectNameOrCode, chapterNumber, topicNumber) {
  const bCode = getCanonicalBoardCode(board);
  const cls = getCanonicalClass(classNum);
  const sCode = getCanonicalSubjectCode(board, classNum, subjectNameOrCode);
  let tNum = String(topicNumber || '1.1').trim();
  const chNum = extractChapterFromTopic(tNum, chapterNumber);
  if (!tNum.includes('.')) {
    tNum = `${chNum}.${tNum}`;
  }
  return `${bCode}-${cls}-${sCode}-${chNum}-${tNum}`;
}

function getCanonicalQuestionCode(topicCode, typeCode, sequence) {
  const seqStr = String(sequence || '1').padStart(3, '0').slice(-3);
  return `${topicCode}-${typeCode}-${seqStr}`;
}

// Pre-mutation snapshot (Rule 1Q)
async function createPreMutationSnapshot(collections, reason) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const snapshotDir = path.resolve(__dirname, '..', 'backups', 'snapshots', `harmonize_all_questions_${timestamp}`);
  if (!fs.existsSync(snapshotDir)) {
    fs.mkdirSync(snapshotDir, { recursive: true });
  }

  const counts = {};
  for (const cName of collections) {
    console.log(`Backing up collection '${cName}'...`);
    const snap = await db.collection(cName).get();
    const docs = snap.docs.map(d => ({ id: d.id, data: d.data() }));
    counts[cName] = docs.length;
    fs.writeFileSync(path.join(snapshotDir, `${cName}.json`), JSON.stringify(docs, null, 2), 'utf-8');
    console.log(`  -> Saved ${docs.length} docs from '${cName}'`);
  }

  const manifest = {
    snapshotId: `harmonize_all_questions_${timestamp}`,
    timestamp: new Date().toISOString(),
    reason,
    counts,
    snapshotDir
  };
  fs.writeFileSync(path.join(snapshotDir, 'manifest.json'), JSON.stringify(manifest, null, 2), 'utf-8');
  await db.collection('_systemBackups').doc(manifest.snapshotId).set(manifest, { merge: true });
  console.log(`Pre-mutation snapshot atomic write complete: ${manifest.snapshotId}\n`);
  return manifest;
}

// Chunked batch helper
class ChunkedBatchWriter {
  constructor(db, maxChunkSize = 400) {
    this.db = db;
    this.maxChunkSize = maxChunkSize;
    this.operations = [];
  }

  set(docRef, data, options = {}) {
    this.operations.push({ type: 'set', docRef, data, options });
  }

  delete(docRef) {
    this.operations.push({ type: 'delete', docRef });
  }

  async commit() {
    console.log(`Committing total ${this.operations.length} operations in chunks of ${this.maxChunkSize}...`);
    for (let i = 0; i < this.operations.length; i += this.maxChunkSize) {
      const chunk = this.operations.slice(i, i + this.maxChunkSize);
      const batch = this.db.batch();
      for (const op of chunk) {
        if (op.type === 'set') {
          batch.set(op.docRef, op.data, op.options);
        } else if (op.type === 'delete') {
          batch.delete(op.docRef);
        }
      }
      await batch.commit();
      console.log(`  Committed ops ${i + 1} to ${Math.min(i + chunk.length, this.operations.length)}`);
    }
  }
}

async function main() {
  console.log('=== STARTING COMPLETE QUESTION BANK SSOT HARMONIZATION ===\n');

  // Step 1: Pre-mutation snapshot
  await createPreMutationSnapshot(['questions', 'syllabusTopicIndex'], 'Complete SSOT harmonization of all questions and topic codes');

  // Step 2: Fetch all questions and syllabus topic index
  console.log('Fetching questions and syllabusTopicIndex...');
  const [questionsSnap, topicIndexSnap] = await Promise.all([
    db.collection('questions').get(),
    db.collection('syllabusTopicIndex').get()
  ]);
  console.log(`Fetched ${questionsSnap.size} questions and ${topicIndexSnap.size} syllabusTopicIndex docs.\n`);

  const topicNameMap = new Map();
  topicIndexSnap.docs.forEach(doc => {
    topicNameMap.set(doc.id, doc.data()?.topicName || doc.data()?.name || doc.data()?.title || '');
  });

  const batchWriter = new ChunkedBatchWriter(db);
  const docsToDelete = new Set();
  const idMigrationMap = new Map();

  let modifiedCount = 0;
  let autoIdMigratedCount = 0;
  let topicCodeFixedCount = 0;
  let chapterFixedCount = 0;

  for (const doc of questionsSnap.docs) {
    const data = doc.data();
    const currentDocId = doc.id;
    let isModified = false;

    const rawBoard = data.board || data.boardCode || 'MH';
    const boardCode = getCanonicalBoardCode(rawBoard);
    const finalBoard = getCanonicalBoardName(rawBoard);
    const classNum = getCanonicalClass(data.class || data.classNum || '8');
    const rawSubject = data.subject || data.subjectName || data.subjectCode || 'Mathematics';
    const subjectCode = getCanonicalSubjectCode(boardCode, classNum, rawSubject);

    let topicNumber = String(data.topicNumber || data.subtopicNumber || '1.1').trim();
    const chapterNumber = extractChapterFromTopic(topicNumber, data.chapterNumber || data.chapter);
    if (!topicNumber.includes('.')) {
      topicNumber = `${chapterNumber}.${topicNumber}`;
    }

    if (String(data.chapterNumber) !== chapterNumber) {
      chapterFixedCount++;
      isModified = true;
    }

    const canonicalTopicCode = getCanonicalTopicCode(boardCode, classNum, subjectCode, chapterNumber, topicNumber);
    let topicCode = data.topicCode || canonicalTopicCode;

    if (topicCode !== canonicalTopicCode) {
      topicCode = canonicalTopicCode;
      topicCodeFixedCount++;
      isModified = true;
    }

    // Determine question type code
    let typeCode = data.type || 'OSC';
    if (typeCode.length > 3 || typeCode.includes('_')) {
      const qtype = typeCode.toLowerCase();
      if (qtype.includes('single') || qtype === 'osc') typeCode = 'OSC';
      else if (qtype.includes('multi') || qtype === 'omc') typeCode = 'OMC';
      else if (qtype.includes('true') || qtype.includes('false') || qtype === 'otf') typeCode = 'OTF';
      else if (qtype.includes('assert') || qtype === 'oar') typeCode = 'OAR';
      else if (qtype.includes('blank') || qtype === 'ofb') typeCode = 'OFB';
      else if (qtype === 'numerical' || qtype === 'one') typeCode = 'ONE';
      else if (qtype === 'subjective_define' || qtype === 'sdf') typeCode = 'SDF';
      else if (qtype === 'subjective_laws' || qtype === 'slp') typeCode = 'SLP';
      else if (qtype === 'subjective_short' || qtype === 'ssa') typeCode = 'SSA';
      else if (qtype === 'subjective_reason' || qtype === 'subjective_notes' || qtype === 'ssr') typeCode = 'SSR';
      else if (qtype === 'numerical_short' || qtype === 'ssn') typeCode = 'SSN';
      else if (qtype === 'subjective_long' || qtype === 'sla') typeCode = 'SLA';
      else if (qtype === 'numerical_long' || qtype === 'sln') typeCode = 'SLN';
      else typeCode = 'SSA';
    }

    // Sequence
    let seqStr = '001';
    if (data.questionCode) {
      const parts = String(data.questionCode).split('-');
      const last = parts[parts.length - 1];
      if (/^\d{3}$/.test(last)) {
        seqStr = last;
      }
    } else if (/^\d+$/.test(currentDocId)) {
      seqStr = String(currentDocId).padStart(3, '0');
    }

    const canonicalQuestionCode = getCanonicalQuestionCode(canonicalTopicCode, typeCode, seqStr);
    const targetDocId = canonicalQuestionCode;
    const isAutoId = currentDocId !== targetDocId;

    if (isAutoId) {
      autoIdMigratedCount++;
      isModified = true;
      idMigrationMap.set(currentDocId, targetDocId);
      if (data.questionCode && data.questionCode !== targetDocId) {
        idMigrationMap.set(data.questionCode, targetDocId);
      }
    }

    if (data.boardCode !== boardCode || data.board !== finalBoard || data.class !== classNum || data.subjectCode !== subjectCode || data.questionCode !== targetDocId) {
      isModified = true;
    }

    const finalTopicName = topicNameMap.get(canonicalTopicCode) || data.topicName || data.topic || '';

    if (isModified || isAutoId) {
      modifiedCount++;
      const updatedData = {
        ...data,
        board: finalBoard,
        boardCode,
        class: classNum,
        subject: data.subject || rawSubject,
        subjectCode,
        chapterNumber,
        topicNumber,
        topicCode: canonicalTopicCode,
        topic: finalTopicName,
        topicName: finalTopicName,
        type: typeCode,
        questionCode: targetDocId,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      };

      const targetRef = db.collection('questions').doc(targetDocId);
      batchWriter.set(targetRef, updatedData, { merge: true });

      if (isAutoId && currentDocId !== targetDocId) {
        docsToDelete.add(currentDocId);
      }
    }
  }

  console.log(`Scan Summary:`);
  console.log(`- Total Questions: ${questionsSnap.size}`);
  console.log(`- Questions Modified: ${modifiedCount}`);
  console.log(`- Auto-IDs Migrated to Canonical Doc IDs: ${autoIdMigratedCount}`);
  console.log(`- Topic Codes Corrected: ${topicCodeFixedCount}`);
  console.log(`- Chapter Numbers Corrected: ${chapterFixedCount}`);
  console.log(`- Orphan Auto-ID Docs to Delete: ${docsToDelete.size}\n`);

  for (const oldId of Array.from(docsToDelete)) {
    const oldRef = db.collection('questions').doc(oldId);
    batchWriter.delete(oldRef);
  }

  // Commit question batch
  await batchWriter.commit();
  console.log('\nAll question updates and auto-ID cleanups committed successfully!');

  // Step 3: Rebuild syllabusTopicIndex counts
  console.log('\n=== REBUILDING SYLLABUS TOPIC INDEX QUESTION COUNTS ===');
  const freshQuestionsSnap = await db.collection('questions').get();
  console.log(`Fresh question count after cleanup: ${freshQuestionsSnap.size}`);

  const topicObjectiveCounts = {};
  const topicSubjectiveCounts = {};

  const SUBJECTIVE_CODES = new Set(['SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN']);

  freshQuestionsSnap.docs.forEach(doc => {
    const q = doc.data();
    const tCode = q.topicCode;
    const type = q.type || '';
    if (!tCode) return;

    if (SUBJECTIVE_CODES.has(type)) {
      topicSubjectiveCounts[tCode] = (topicSubjectiveCounts[tCode] || 0) + 1;
    } else {
      topicObjectiveCounts[tCode] = (topicObjectiveCounts[tCode] || 0) + 1;
    }
  });

  const indexBatch = new ChunkedBatchWriter(db);
  const freshIndexSnap = await db.collection('syllabusTopicIndex').get();

  freshIndexSnap.docs.forEach(doc => {
    const tCode = doc.id;
    const objCount = topicObjectiveCounts[tCode] || 0;
    const subjCount = topicSubjectiveCounts[tCode] || 0;
    const totalCount = objCount + subjCount;

    indexBatch.set(doc.ref, {
      objectiveCount: objCount,
      subjectiveCount: subjCount,
      questionCount: totalCount,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    }, { merge: true });
  });

  await indexBatch.commit();
  console.log(`SyllabusTopicIndex successfully rebuilt across ${freshIndexSnap.size} topics!\n`);

  console.log('=== HARMONIZATION AND INDEX REBUILD COMPLETED SUCCESSFULLY ===');
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal Error during harmonization:', err);
  process.exit(1);
});
