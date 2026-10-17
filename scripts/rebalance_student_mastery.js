const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot');

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

async function runMasteryRebalance() {
  console.log('=== STEP 1: MANDATORY PRE-MUTATION SNAPSHOT ===');
  const snapshotResult = await createPreMutationSnapshot(
    ['studentTopicMastery', '_systemCaches'],
    'rebalance_mastery_srs_exempt'
  );
  console.log(`Snapshot created successfully: ${snapshotResult.snapshotId}\n`);

  console.log('=== STEP 2: AUDITING HISTORICAL PRACTICE & MASTERY ===');
  const [masterySnap, usersSnap, parentReviewsSnap, practiceSubmissionsSnap] = await Promise.all([
    db.collection('studentTopicMastery').get(),
    db.collection('users').where('role', '==', 'student').get(),
    db.collection('parentReviews').get(),
    db.collection('practiceSubmissions').get()
  ]);

  const studentsMap = new Map();
  usersSnap.docs.forEach(doc => {
    const d = doc.data();
    studentsMap.set(d.studentCode || doc.id, { id: doc.id, ...d });
  });

  // Track historical highest mastery reached per student & topic
  const historyMap = new Map();

  practiceSubmissionsSnap.docs.forEach(doc => {
    const d = doc.data();
    if (!d.studentCode || !d.topicCode) return;
    const key = `${d.studentCode}_${d.topicCode}`;
    const mb = Number(d.masteryBefore || 0);
    const ma = Number(d.finalMastery || d.masteryAfter || 0);
    const highest = Math.max(mb, ma);
    const currentBest = historyMap.get(key) || 0;
    if (highest > currentBest) historyMap.set(key, highest);
  });

  parentReviewsSnap.docs.forEach(doc => {
    const d = doc.data();
    if (!d.studentCode || !d.topicCode) return;
    const key = `${d.studentCode}_${d.topicCode}`;
    const mb = Number(d.masteryBefore || 0);
    const ma = Number(d.masteryAfter || d.finalMastery || 0);
    const highest = Math.max(mb, ma);
    const currentBest = historyMap.get(key) || 0;
    if (highest > currentBest) historyMap.set(key, highest);
  });

  console.log(`Auditing ${masterySnap.size} studentTopicMastery documents...`);

  const updatesToApply = [];
  let srsFieldsCleaned = 0;
  let demotedMasteryRestored = 0;
  let recoveryMasteryRestored = 0;
  const studentRestorations = {};

  masterySnap.docs.forEach(doc => {
    const d = doc.data();
    const docId = doc.id;
    const studentCode = d.studentCode;
    const topicCode = d.topicCode;
    const student = studentsMap.get(studentCode);
    const isSrsEnabled = Boolean(student?.srsEnabled);

    const currentMastery = Number(d.mastery || 0);
    const isRecoveryMastered = Boolean(d.isRecoveryMastered);
    const key = `${studentCode}_${topicCode}`;
    const historicalBest = historyMap.get(key) || 0;

    let targetMastery = currentMastery;
    let needsMasteryUpdate = false;
    let updateReason = '';

    // Rule 1: If isRecoveryMastered, guaranteed mastery >= 90
    if (isRecoveryMastered && currentMastery < 90) {
      targetMastery = Math.max(90, historicalBest);
      needsMasteryUpdate = true;
      recoveryMasteryRestored++;
      updateReason = `Guided Recovery passed (was ${currentMastery}%, restored to ${targetMastery}%)`;
    }

    // Rule 2: If student had reached >= 90% previously but was reduced to < 90% by SRS decay/penalty
    if (historicalBest >= 90 && currentMastery < 90) {
      targetMastery = Math.max(90, historicalBest);
      needsMasteryUpdate = true;
      demotedMasteryRestored++;
      updateReason = `Previously achieved ${historicalBest}% mastery, restored from degraded ${currentMastery}%`;
    }

    // Rule 3: For students exempted from SRS, remove stale SRS decay and countdown fields
    const hasSrsFields = d.srsStage !== undefined || d.nextReviewDate !== undefined || d.srsSchedule !== undefined;
    let needsSrsCleanup = false;
    if (!isSrsEnabled && hasSrsFields) {
      needsSrsCleanup = true;
      srsFieldsCleaned++;
    }

    if (needsMasteryUpdate || needsSrsCleanup) {
      const updatePayload = {
        updatedAt: new Date()
      };

      if (needsMasteryUpdate) {
        updatePayload.mastery = targetMastery;
      }

      if (needsSrsCleanup) {
        updatePayload.srsStage = admin.firestore.FieldValue.delete();
        updatePayload.nextReviewDate = admin.firestore.FieldValue.delete();
        updatePayload.srsSchedule = admin.firestore.FieldValue.delete();
      }

      updatesToApply.push({
        ref: doc.ref,
        docId,
        studentCode,
        studentName: student?.name || studentCode,
        topicCode,
        beforeMastery: currentMastery,
        afterMastery: targetMastery,
        needsMasteryUpdate,
        needsSrsCleanup,
        reason: updateReason
      });

      if (needsMasteryUpdate) {
        if (!studentRestorations[studentCode]) {
          studentRestorations[studentCode] = {
            studentName: student?.name || studentCode,
            restoredTopics: []
          };
        }
        studentRestorations[studentCode].restoredTopics.push({
          topicCode,
          before: currentMastery,
          after: targetMastery,
          reason: updateReason
        });
      }
    }
  });

  console.log('\n=== STEP 3: SUMMARY OF DETECTED REBALANCINGS ===');
  console.log(`Total documents requiring updates: ${updatesToApply.length}`);
  console.log(`  - Degraded masteries restored to ≥90%: ${demotedMasteryRestored + recoveryMasteryRestored}`);
  console.log(`    (Guided Recovery restored: ${recoveryMasteryRestored}, SRS demotions restored: ${demotedMasteryRestored})`);
  console.log(`  - Stale SRS countdown/decay fields neutralized: ${srsFieldsCleaned}`);
  console.log(`Total students benefiting from mastery restoration: ${Object.keys(studentRestorations).length}`);

  console.log('\n=== STEP 4: EXECUTING ATOMIC BATCH WRITES ===');
  const batchSize = 400;
  for (let i = 0; i < updatesToApply.length; i += batchSize) {
    const chunk = updatesToApply.slice(i, i + batchSize);
    const batch = db.batch();
    chunk.forEach(item => {
      const updateData = { updatedAt: new Date() };
      if (item.needsMasteryUpdate) {
        updateData.mastery = item.afterMastery;
      }
      if (item.needsSrsCleanup) {
        updateData.srsStage = admin.firestore.FieldValue.delete();
        updateData.nextReviewDate = admin.firestore.FieldValue.delete();
        updateData.srsSchedule = admin.firestore.FieldValue.delete();
      }
      batch.update(item.ref, updateData);
    });
    await batch.commit();
    console.log(`  ✓ Committed batch ${Math.floor(i / batchSize) + 1} (${chunk.length} documents)`);
  }

  console.log('\n=== STEP 5: INVALIDATING STALE SYSTEM CACHES ===');
  const cacheDocs = await db.collection('_systemCaches').get();
  console.log(`Found ${cacheDocs.size} documents in _systemCaches.`);
  const cacheBatch = db.batch();
  cacheDocs.docs.forEach(doc => {
    cacheBatch.delete(doc.ref);
  });
  if (cacheDocs.size > 0) {
    await cacheBatch.commit();
    console.log(`  ✓ Successfully purged ${cacheDocs.size} stale cache entries (including bulk-lq-v2 caches)`);
  }

  console.log('\n=== STEP 6: VERIFICATION OF RESTORED STUDENTS ===');
  for (const [code, info] of Object.entries(studentRestorations)) {
    console.log(`\n📌 Student: ${info.studentName} (${code}) — Restored Topics: ${info.restoredTopics.length}`);
    info.restoredTopics.slice(0, 5).forEach(t => {
      console.log(`   • ${t.topicCode}: ${t.before}% -> 🟢 ${t.after}% (${t.reason})`);
    });
    if (info.restoredTopics.length > 5) {
      console.log(`   ... and ${info.restoredTopics.length - 5} more topics`);
    }
  }

  console.log('\n✅ MASTERY REBALANCING COMPLETED SUCCESSFULLY!');
}

runMasteryRebalance().catch(console.error);
