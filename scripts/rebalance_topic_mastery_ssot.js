const path = require('path');
const fs = require('fs');

// Load environment variables
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

const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot');

const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom';
if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({ credential: admin.credential.cert(credential) });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();

function getCanonicalRequiredConfidence(classification, targetQuestions) {
  const cls = String(classification || '').toLowerCase().trim();
  if (cls === 'minor' || cls === 'micro') return 12;
  if (cls === 'medium' || cls === 'moderate' || cls === 'conceptual') return 18;
  if (cls === 'major' || cls === 'calculative' || cls === 'hots') return 24;

  if (targetQuestions !== undefined) {
    const tq = Number(targetQuestions);
    if (tq <= 30) return 12;
    if (tq <= 50) return 18;
    return 24;
  }
  return 12;
}

async function runTopicMasteryRebalance() {
  console.log('===============================================================');
  console.log('SSOT TOPIC MASTERY HISTORICAL REBALANCE & HARMONIZATION (12/18/24)');
  console.log('===============================================================\n');

  // STEP 1: Mandatory Pre-Mutation Snapshot
  console.log('--- Step 1: Taking Pre-Mutation Snapshot ---');
  const snapshotRes = await createPreMutationSnapshot(
    ['studentTopicMastery', '_systemCaches'],
    'rebalance_topic_mastery_ssot_12_18_24'
  );
  console.log(`Snapshot saved: ${snapshotRes.snapshotId}\n`);

  // STEP 2: Load Topic Index for Canonical Classifications
  console.log('--- Step 2: Indexing Topic Metadata ---');
  const indexSnap = await db.collection('syllabusTopicIndex').get();
  const topicIndexMap = new Map();
  indexSnap.docs.forEach(doc => {
    topicIndexMap.set(doc.id, doc.data());
  });
  console.log(`Indexed ${topicIndexMap.size} topics from syllabusTopicIndex.\n`);

  // STEP 3: Audit and Harmonize studentTopicMastery Records
  console.log('--- Step 3: Auditing studentTopicMastery Collection ---');
  const masterySnap = await db.collection('studentTopicMastery').get();
  console.log(`Found ${masterySnap.size} studentTopicMastery documents.\n`);

  let updatedCount = 0;
  let remainingMastered = 0;
  let shiftedToInProgress = 0;
  let alreadyUpToDate = 0;

  const batchOperations = [];

  masterySnap.docs.forEach(doc => {
    const data = doc.data();
    const docId = doc.id;
    const topicCode = data.topicCode || (docId.includes('_') ? docId.slice(docId.indexOf('_') + 1) : '');

    const indexInfo = topicIndexMap.get(topicCode);
    const classification = indexInfo?.topicClassification || data.topicClassification || 'minor';
    const targetQuestions = indexInfo?.targetQuestions || data.targetQuestions;

    const newReqConf = getCanonicalRequiredConfidence(classification, targetQuestions);
    const oldReqConf = Number(data.requiredConfidence || 6);

    const confidence = Number(data.confidence || data.questionsAttempted || 0);
    const mastery = Number(data.mastery || 0);
    const isRecovery = Boolean(data.isRecoveryMastered);

    const wasMastered = isRecovery || (mastery >= 90 && confidence >= oldReqConf);
    const isNowMastered = isRecovery || (mastery >= 90 && confidence >= newReqConf);

    if (wasMastered && !isNowMastered) {
      shiftedToInProgress++;
    } else if (isNowMastered) {
      remainingMastered++;
    }

    if (oldReqConf !== newReqConf) {
      batchOperations.push({
        ref: doc.ref,
        update: {
          requiredConfidence: newReqConf,
          topicClassification: classification,
          targetQuestions: targetQuestions || (newReqConf === 12 ? 12 : (newReqConf === 18 ? 18 : 24)),
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        }
      });
      updatedCount++;
    } else {
      alreadyUpToDate++;
    }
  });

  console.log(`Audit Summary:`);
  console.log(`- Documents requiring requiredConfidence update: ${updatedCount}`);
  console.log(`- Topics remaining 🟢 Mastered (completed >= ${12}+ Qs with >=90%): ${remainingMastered}`);
  console.log(`- Topics transitioning to 🟡 In Progress (under 2 sets completed): ${shiftedToInProgress}`);
  console.log(`- Documents already matching new standard: ${alreadyUpToDate}\n`);

  // STEP 4: Commit batch updates in chunks of 450
  if (batchOperations.length > 0) {
    console.log(`--- Step 4: Committing ${batchOperations.length} updates in chunked transactions ---`);
    const chunkSize = 450;
    for (let i = 0; i < batchOperations.length; i += chunkSize) {
      const chunk = batchOperations.slice(i, i + chunkSize);
      const batch = db.batch();
      chunk.forEach(op => {
        batch.update(op.ref, op.update);
      });
      await batch.commit();
      console.log(`  Committed batch ${Math.floor(i / chunkSize) + 1} (${chunk.length} docs)`);
    }
    console.log(`All updates written successfully!\n`);
  }

  // STEP 5: Clear Stale Dashboard & Metrics Caches
  console.log('--- Step 5: Invalidating System Caches ---');
  const cacheSnap = await db.collection('_systemCaches').get();
  if (!cacheSnap.empty) {
    const cacheBatch = db.batch();
    cacheSnap.docs.forEach(doc => {
      cacheBatch.delete(doc.ref);
    });
    await cacheBatch.commit();
    console.log(`Cleared ${cacheSnap.size} cached metric documents from _systemCaches.\n`);
  }

  console.log('===============================================================');
  console.log('HARMONIZATION COMPLETE: All student topic masteries are now SSOT compliant!');
  console.log('===============================================================');
}

runTopicMasteryRebalance()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Migration failed:', err);
    process.exit(1);
  });
