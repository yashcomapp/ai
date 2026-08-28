const path = require('path');
const fs = require('fs');

// 1. Load .env.local
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

// 2. Init Firebase Admin
const admin = require('firebase-admin');
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom';

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();
db.settings({ ignoreUndefinedProperties: true });

// Collections that MUST be 100% PRESERVED
const PRESERVED_COLLECTIONS = new Set([
  'users',
  'batches',
  'syllabus',
  'syllabusTopicIndex',
  'config',
  '_systemBackups'
]);

// Collections to completely purge to ZERO
const COLLECTIONS_TO_PURGE = [
  'questions',
  'exams',
  'subjectiveExams',
  'examAttempts',
  'subjectiveAttempts',
  'studentTopicMastery',
  'reviews',
  'parentReviews',
  'practiceSubmissions',
  'attendance',
  'attendanceLogs',
  'attendanceDeclarations',
  'leaves',
  'notices',
  'noticeSeenLogs',
  'chats',
  'messages',
  'directMessages',
  'channels',
  'disputes',
  'questionRequests',
  'integrityLogs',
  'proctoringLogs',
  'timeLogs',
  'clientStorageSync',
  'feeTransactions',
  'subjectiveAssignments',
  'parentDMs',
  'studentDMs',
  'notifications',
  'pushTokens',
  'studyPlans',
  'studentActivity'
];

async function deleteCollection(collectionName, batchSize = 400) {
  const colRef = db.collection(collectionName);
  let totalDeleted = 0;

  while (true) {
    const snapshot = await colRef.limit(batchSize).get();
    if (snapshot.empty) break;

    const batch = db.batch();
    snapshot.docs.forEach(doc => {
      batch.delete(doc.ref);
    });
    await batch.commit();
    totalDeleted += snapshot.size;
    console.log(`  [${collectionName}] Deleted batch of ${snapshot.size} docs (Total: ${totalDeleted})...`);
  }

  return totalDeleted;
}

async function runPristinePurge() {
  console.log('====================================================');
  console.log('🚀 EXECUTING COMPLETE PRISTINE PURGE TO ZERO');
  console.log('Preserving ONLY: users, batches, syllabus, syllabusTopicIndex, config');
  console.log('====================================================\n');

  const results = {};

  for (const colName of COLLECTIONS_TO_PURGE) {
    console.log(`\n🧹 Purging collection: ${colName}...`);
    try {
      const deleted = await deleteCollection(colName);
      results[colName] = deleted;
      console.log(`✅ ${colName}: Successfully deleted ${deleted} documents (Now 0).`);
    } catch (err) {
      console.error(`❌ Error purging ${colName}:`, err.message);
    }
  }

  // Also check all collections in the database dynamically to catch any untracked collections
  console.log('\n🔍 Scanning for any other untracked collections...');
  const allCollections = await db.listCollections();
  for (const col of allCollections) {
    const colId = col.id;
    if (!PRESERVED_COLLECTIONS.has(colId) && !COLLECTIONS_TO_PURGE.includes(colId)) {
      console.log(`⚠️ Found untracked collection: ${colId}. Purging...`);
      const deleted = await deleteCollection(colId);
      results[colId] = deleted;
      console.log(`✅ ${colId}: Successfully deleted ${deleted} documents.`);
    }
  }

  console.log('\n====================================================');
  console.log('📊 FINAL DATABASE STATE VERIFICATION');
  console.log('====================================================');

  const verifyCols = await db.listCollections();
  for (const col of verifyCols) {
    const snap = await col.count().get();
    const count = snap.data().count;
    const isPreserved = PRESERVED_COLLECTIONS.has(col.id);
    console.log(`• ${col.id}: ${count} docs ${isPreserved ? '(🟢 PRESERVED)' : count === 0 ? '(✅ 0 - PURGED)' : '(⚠️ NON-ZERO)'}`);
  }

  console.log('\n🎉 PRISTINE CLEAN SLATE COMPLETE! 0 questions, 0 practices, 0 exams, 0 attendance, 0 mastery.');
}

runPristinePurge().catch(err => {
  console.error('Fatal purge error:', err);
  process.exit(1);
});
