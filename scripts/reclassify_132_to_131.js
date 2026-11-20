const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

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

async function reclassify() {
  console.log('--- Step 1: Taking Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['questions', 'syllabus'], 'reclassify_slope_questions_from_132_to_131');

  console.log('--- Step 2: Fetching 1.3.2 questions ---');
  const snap = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.2')
    .get();

  const toMove = [];
  snap.docs.forEach(d => {
    const q = d.data();
    const text = ((q.text || '') + ' ' + (q.explanation || '')).toLowerCase();
    const isSlope = text.includes('slope') || text.includes('gradient');
    if (isSlope) {
      toMove.push({ id: d.id, ...q });
    }
  });

  console.log(`Found ${toMove.length} slope questions to reclassify to 1.3.1.`);

  // Get existing 1.3.1 questions to avoid code collision
  const snap131 = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.1')
    .get();
  
  const existingCodes131 = new Set(snap131.docs.map(d => d.data().questionCode));
  console.log('Existing 1.3.1 codes:', Array.from(existingCodes131));

  // Determine sequential numbering per question type
  const typeCounters = {};
  existingCodes131.forEach(code => {
    // format: MH-9-SCIT-1-1.3.1-TYPE-NUM
    const parts = (code || '').split('-');
    if (parts.length >= 7) {
      const type = parts[parts.length - 2];
      const num = parseInt(parts[parts.length - 1], 10);
      if (!isNaN(num)) {
        typeCounters[type] = Math.max(typeCounters[type] || 0, num);
      }
    }
  });

  const batch = db.batch();
  let updatedCount = 0;

  toMove.forEach(q => {
    const type = q.questionType || 'OSC';
    typeCounters[type] = (typeCounters[type] || 0) + 1;
    const newSeq = String(typeCounters[type]).padStart(3, '0');
    const newQuestionCode = `MH-9-SCIT-1-1.3.1-${type}-${newSeq}`;

    const ref = db.collection('questions').doc(q.id);
    batch.update(ref, {
      subtopicCode: 'MH-9-SCIT-1-1.3.1',
      subtopicName: 'Interpreting slopes for velocity and acceleration',
      topicNumber: '1.3.1',
      questionCode: newQuestionCode,
      updatedAt: new Date().toISOString()
    });
    updatedCount++;
  });

  console.log(`Committing batch update of ${updatedCount} questions...`);
  await batch.commit();
  console.log('Successfully moved questions to MH-9-SCIT-1-1.3.1!');

  // Update syllabus/mh_9_scit subtopic counts
  console.log('Updating syllabus/mh_9_scit document...');
  const sylRef = db.collection('syllabus').doc('mh_9_scit');
  const sylDoc = await sylRef.get();
  if (sylDoc.exists) {
    const data = sylDoc.data();
    const ch1 = (data.chapters || []).find(c => String(c.number) === '1');
    if (ch1) {
      const t13 = (ch1.topics || []).find(t => t.number === '1.3');
      if (t13 && t13.subtopics) {
        const st131 = t13.subtopics.find(st => st.number === '1.3.1');
        const st132 = t13.subtopics.find(st => st.number === '1.3.2');
        if (st131 && st132) {
          st131.objectiveCount = (st131.objectiveCount || 0) + updatedCount;
          st132.objectiveCount = Math.max(0, (st132.objectiveCount || 0) - updatedCount);
          console.log(`Updated syllabus counts: 1.3.1 obj = ${st131.objectiveCount}, 1.3.2 obj = ${st132.objectiveCount}`);
          await sylRef.update({ chapters: data.chapters });
          console.log('Syllabus updated successfully.');
        }
      }
    }
  }
}

reclassify().catch(err => {
  console.error('Error reclassifying:', err);
  process.exit(1);
});
