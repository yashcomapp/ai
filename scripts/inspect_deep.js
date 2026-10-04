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

async function inspectDeep() {
  const qSnap = await db.collection('questions').get();
  console.log(`Total Question Docs: ${qSnap.size}`);

  const autoIdDocs = [];
  const autoIdWithCanonicalCode = [];
  const qCodeCount = {};

  const topicMismatches = [];

  qSnap.docs.forEach(doc => {
    const q = doc.data();
    const docId = doc.id;
    const qCode = q.questionCode || '';
    const tCode = q.topicCode || '';
    const chNum = q.chapterNumber;
    const tNum = q.topicNumber;
    const boardCode = q.boardCode;
    const cls = String(q.class || '').replace(/\D/g, '');
    const subjCode = q.subjectCode;

    if (qCode) {
      qCodeCount[qCode] = (qCodeCount[qCode] || 0) + 1;
    }

    if (docId !== qCode) {
      autoIdDocs.push({ docId, qCode });
    }

    const expectedTopicCode = `${boardCode}-${cls}-${subjCode}-${String(chNum).replace(/\D/g, '')}-${String(tNum).trim()}`;
    if (tCode !== expectedTopicCode) {
      topicMismatches.push({
        docId,
        qCode,
        tCode,
        expectedTopicCode,
        chapterNumber: chNum,
        topicNumber: tNum,
        subject: q.subject,
        subjectCode: subjCode
      });
    }
  });

  console.log(`Auto ID Docs: ${autoIdDocs.length}`);
  const duplicateQCodes = Object.entries(qCodeCount).filter(([k, v]) => v > 1);
  console.log(`Duplicate questionCodes across collection: ${duplicateQCodes.length}`);
  if (duplicateQCodes.length > 0) {
    console.log('Sample Duplicate questionCodes:', duplicateQCodes.slice(0, 10));
  }

  console.log(`\nTopic Mismatches: ${topicMismatches.length}`);
  console.log('Sample Topic Mismatches:', topicMismatches.slice(0, 15));
}

inspectDeep().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
