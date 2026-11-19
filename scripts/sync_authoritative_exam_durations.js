const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

const envContent = fs.readFileSync(path.join(process.cwd(), '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});

const serviceAccount = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
const projectId = envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || envVars.FIREBASE_PROJECT_ID || 'ai-yashcom';

if (!admin.apps.length) {
  if (serviceAccount) {
    const cred = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(cred),
      databaseURL: `https://${projectId}-default-rtdb.asia-southeast1.firebasedatabase.app/`
    });
  } else {
    admin.initializeApp({ projectId });
  }
}
const db = admin.firestore();

async function main() {
  console.log('--- Step 1: Mandatory Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['exams', 'batchAssignments'], 'sync_authoritative_exam_durations');

  console.log('--- Step 2: Querying all batchAssignments ---');
  const assignsSnap = await db.collection('batchAssignments').get();
  console.log(`Found ${assignsSnap.size} assignments.`);

  let updatedCount = 0;

  for (const assignDoc of assignsSnap.docs) {
    const assignData = assignDoc.data();
    const examId = assignData.examId;
    const assignedDuration = Number(assignData.examDuration);

    if (!examId || !assignedDuration || assignedDuration <= 0) continue;

    const examRef = db.collection('exams').doc(examId);
    const examSnap = await examRef.get();

    if (examSnap.exists) {
      const examData = examSnap.data();
      const currentDuration = Number(examData.duration);

      if (currentDuration !== assignedDuration) {
        console.log(`Updating exam [${examId}] ("${examData.name || examData.title}"): duration ${currentDuration} -> ${assignedDuration} mins (Assignment: ${assignDoc.id})`);
        await examRef.update({
          duration: assignedDuration,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        updatedCount++;
      }
    }
  }

  // Also verify subjectiveAssignments
  const subjAssignsSnap = await db.collection('subjectiveAssignments').get();
  console.log(`Found ${subjAssignsSnap.size} subjective assignments.`);

  for (const assignDoc of subjAssignsSnap.docs) {
    const assignData = assignDoc.data();
    const examId = assignData.examId;
    const assignedDuration = Number(assignData.classroomDuration || assignData.examDuration);

    if (!examId || !assignedDuration || assignedDuration <= 0) continue;

    const examRef = db.collection('subjectiveExams').doc(examId);
    const examSnap = await examRef.get();

    if (examSnap.exists) {
      const examData = examSnap.data();
      const currentDuration = Number(examData.duration);

      if (currentDuration !== assignedDuration) {
        console.log(`Updating subjective exam [${examId}] ("${examData.name || examData.title}"): duration ${currentDuration} -> ${assignedDuration} mins`);
        await examRef.update({
          duration: assignedDuration,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        updatedCount++;
      }
    }
  }

  console.log(`\nSuccessfully synchronized ${updatedCount} exams to match their authoritative assignment modal duration.`);
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error during sync:', err);
  process.exit(1);
});
