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

const SUBJECTIVE_CODES = new Set(['SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN']);

async function syncAllSyllabusCounts() {
  console.log('=== SYNCING ALL 16 SYLLABUS DOCUMENTS & TOPIC COUNTS ===\n');

  console.log('1. Fetching all questions...');
  const qSnap = await db.collection('questions').get();
  console.log(`Fetched ${qSnap.size} questions.`);

  const topicObjCounts = {};
  const topicSubjCounts = {};

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const tCode = q.topicCode;
    const type = q.type || '';
    if (!tCode) return;

    if (SUBJECTIVE_CODES.has(type)) {
      topicSubjCounts[tCode] = (topicSubjCounts[tCode] || 0) + 1;
    } else {
      topicObjCounts[tCode] = (topicObjCounts[tCode] || 0) + 1;
    }
  });

  console.log('2. Fetching and updating all 16 syllabus documents...');
  const sylSnap = await db.collection('syllabus').get();

  for (const doc of sylSnap.docs) {
    const data = doc.data();
    const bCode = data.boardCode || (data.board === 'CBSE' ? 'CBSE' : 'MH');
    const classNum = String(data.class);
    const subjectCode = data.subjectCode;
    const chapters = data.chapters || [];

    let docTotalObj = 0;
    let docTotalSubj = 0;

    chapters.forEach(ch => {
      const chNum = String(ch.number);
      let chObj = 0;
      let chSubj = 0;

      const topics = ch.topics || [];
      topics.forEach((t, tIdx) => {
        const isObj = t && typeof t === 'object';
        const tNum = isObj ? String(t.number || `${chNum}.${tIdx + 1}`) : `${chNum}.${tIdx + 1}`;
        const tName = isObj ? (t.name || t.title || '') : String(t);
        const tCode = isObj && t.topicCode ? t.topicCode : `${bCode}-${classNum}-${subjectCode}-${chNum}-${tNum}`;

        let topObj = topicObjCounts[tCode] || 0;
        let topSubj = topicSubjCounts[tCode] || 0;

        // Process subtopics if present
        if (isObj && Array.isArray(t.subtopics) && t.subtopics.length > 0) {
          const updatedSubtopics = [];
          t.subtopics.forEach((st, stIdx) => {
            const isStObj = st && typeof st === 'object';
            const stNum = isStObj ? String(st.number || `${tNum}.${stIdx + 1}`) : `${tNum}.${stIdx + 1}`;
            const stName = isStObj ? (st.name || st.title || '') : String(st);
            const stCode = isStObj && st.topicCode ? st.topicCode : `${bCode}-${classNum}-${subjectCode}-${chNum}-${stNum}`;

            const subObj = topicObjCounts[stCode] || 0;
            const subSubj = topicSubjCounts[stCode] || 0;

            topObj += subObj;
            topSubj += subSubj;

            updatedSubtopics.push({
              number: stNum,
              name: stName,
              topicCode: stCode,
              objectiveCount: subObj,
              subjectiveCount: subSubj
            });
          });
          t.subtopics = updatedSubtopics;
        }

        if (isObj) {
          t.number = tNum;
          t.name = tName;
          t.topicCode = tCode;
          t.objectiveCount = topObj;
          t.subjectiveCount = topSubj;
        }

        chObj += topObj;
        chSubj += topSubj;
      });

      ch.objectiveCount = chObj;
      ch.subjectiveCount = chSubj;

      docTotalObj += chObj;
      docTotalSubj += chSubj;
    });

    await doc.ref.update({
      chapters,
      objectiveCount: docTotalObj,
      subjectiveCount: docTotalSubj,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });

    console.log(`Updated ${doc.id} (${bCode} Class ${classNum} ${data.subject}): ${docTotalObj} Obj / ${docTotalSubj} Subj`);
  }

  console.log('\n3. Rebuilding syllabusTopicIndex...');
  const indexSnap = await db.collection('syllabusTopicIndex').get();
  const indexBatch = db.batch();
  let bCount = 0;

  indexSnap.docs.forEach(doc => {
    const tCode = doc.id;
    const objCount = topicObjCounts[tCode] || 0;
    const subjCount = topicSubjCounts[tCode] || 0;
    const totalCount = objCount + subjCount;

    indexBatch.update(doc.ref, {
      objectiveCount: objCount,
      subjectiveCount: subjCount,
      questionCount: totalCount,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    bCount++;
  });

  if (bCount > 0) {
    await indexBatch.commit();
  }

  console.log(`Rebuilt ${indexSnap.size} syllabusTopicIndex documents.`);
  console.log('\n=== ALL SYLLABUS COUNTS AND TOPIC INDEXES ARE 100% SYNCHRONIZED ===');
}

syncAllSyllabusCounts().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
