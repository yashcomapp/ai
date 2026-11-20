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

async function runFix() {
  console.log('🔧 Starting fix for CBSE 8 questionCodes, exams, and reviews...');

  // 1. Fix questionCodes for MGP1 Chapter 4 (Quadrilaterals)
  const q4Snap = await db.collection('questions')
    .where('subjectCode', '==', 'MGP1')
    .where('chapterNumber', '==', 4)
    .get();

  console.log(`Found ${q4Snap.size} questions in MGP1 Chapter 4 (Quadrilaterals)`);
  let qBatch = db.batch();
  let qCount = 0;
  let qFixed = 0;

  for (const doc of q4Snap.docs) {
    const data = doc.data();
    let currentQC = data.questionCode || '';
    // If it was mistakenly set to MGP2-6-6 or still had MGP1-5-5
    if (currentQC.includes('CBSE-8-MGP2-6-6.') || currentQC.includes('CBSE-8-MGP1-5-5.')) {
      const parts = currentQC.split('-');
      // format: CBSE-8-MGP2-6-6.1.1-OSC-001 -> topicCode is parts[0..4], type is parts[5], seq is parts[6]
      const type = parts[parts.length - 2];
      const seq = parts[parts.length - 1];
      const correctQC = `${data.topicCode}-${type}-${seq}`;

      qBatch.update(doc.ref, {
        questionCode: correctQC,
        chapterName: 'Quadrilaterals',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      qCount++;
      qFixed++;

      if (qCount >= 400) {
        await qBatch.commit();
        qBatch = db.batch();
        qCount = 0;
      }
    }
  }
  if (qCount > 0) {
    await qBatch.commit();
  }
  console.log(`✅ Fixed questionCode for ${qFixed} Quadrilaterals questions in MGP1.`);

  // 2. Fix the 4 exams
  const examIds = [
    '019-CBSE-8-Understanding-5.1-121026',
    '020-CBSE-8-Understanding-5.2-131026',
    '021-CBSE-8-Understanding-5.3-5.4-141026',
    '022-CBSE-8-Understanding-5.1-5.4-151026'
  ];

  for (const exId of examIds) {
    const exDoc = await db.collection('exams').doc(exId).get();
    if (exDoc.exists) {
      const data = exDoc.data();
      const currentQCodes = data.questionCodes || [];
      const updatedQCodes = currentQCodes.map(code => code.replace('CBSE-8-MGP1-5-5.', 'CBSE-8-MGP1-4-4.'));

      await exDoc.ref.update({
        chapterNumber: 4,
        chapter: 'Quadrilaterals',
        questionCodes: updatedQCodes,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      console.log(`✅ Updated Exam ${exId}: chapter=4, questionCodes mapped (${updatedQCodes.length} questions).`);
    }
  }

  // 3. Fix the 53 reviews for these 4 exams
  let revCount = 0;
  let revBatch = db.batch();
  let revOps = 0;

  for (const exId of examIds) {
    const rSnap = await db.collection('reviews').where('examId', '==', exId).get();
    for (const rDoc of rSnap.docs) {
      const data = rDoc.data();
      const updates = {
        chapter: 'Quadrilaterals',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      };

      if (Array.isArray(data.questionDetails)) {
        updates.questionDetails = data.questionDetails.map(qd => {
          let qCode = qd.questionCode || '';
          if (qCode.includes('CBSE-8-MGP1-5-5.')) {
            qCode = qCode.replace('CBSE-8-MGP1-5-5.', 'CBSE-8-MGP1-4-4.');
          }
          return {
            ...qd,
            questionCode: qCode
          };
        });
      }

      revBatch.update(rDoc.ref, updates);
      revOps++;
      revCount++;

      if (revOps >= 400) {
        await revBatch.commit();
        revBatch = db.batch();
        revOps = 0;
      }
    }
  }
  if (revOps > 0) {
    await revBatch.commit();
  }
  console.log(`✅ Updated ${revCount} review documents across the 4 CBSE 8 exams.`);

  console.log('🎉 Fix completed successfully.');
}

runFix().then(() => process.exit(0)).catch(e => {
  console.error(e);
  process.exit(1);
});
