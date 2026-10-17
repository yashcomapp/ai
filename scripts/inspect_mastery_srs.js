const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

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

async function inspect() {
  console.log('Fetching studentTopicMastery, users, and practice submissions...');
  const [masterySnap, usersSnap, parentReviewsSnap, practiceSubmissionsSnap] = await Promise.all([
    db.collection('studentTopicMastery').get(),
    db.collection('users').where('role', '==', 'student').get(),
    db.collection('parentReviews').get(),
    db.collection('practiceSubmissions').get()
  ]);

  console.log(`Total students: ${usersSnap.size}`);
  console.log(`Total studentTopicMastery docs: ${masterySnap.size}`);
  console.log(`Total parentReviews docs: ${parentReviewsSnap.size}`);
  console.log(`Total practiceSubmissions docs: ${practiceSubmissionsSnap.size}`);

  let srsStageCount = 0;
  let srsScheduleCount = 0;
  let nextReviewDateCount = 0;
  let recoveryMasteredCount = 0;
  let recoveryBelow90Count = 0;
  let demotedOr85Count = 0;
  let candidatesForRebalancing = [];

  // Group practice submissions by studentCode and topicCode
  const topicSubmissionsMap = new Map();
  practiceSubmissionsSnap.docs.forEach(doc => {
    const d = doc.data();
    if (!d.studentCode || !d.topicCode) return;
    const key = `${d.studentCode}_${d.topicCode}`;
    if (!topicSubmissionsMap.has(key)) topicSubmissionsMap.set(key, []);
    topicSubmissionsMap.get(key).push(d);
  });

  parentReviewsSnap.docs.forEach(doc => {
    const d = doc.data();
    if (!d.studentCode || !d.topicCode) return;
    const key = `${d.studentCode}_${d.topicCode}`;
    if (!topicSubmissionsMap.has(key)) topicSubmissionsMap.set(key, []);
    topicSubmissionsMap.get(key).push(d);
  });

  masterySnap.docs.forEach(doc => {
    const d = doc.data();
    const docId = doc.id;
    const studentCode = d.studentCode;
    const topicCode = d.topicCode;
    const currentMastery = Number(d.mastery || 0);
    const confidence = Number(d.confidence || 0);

    if (d.srsStage !== undefined && d.srsStage !== null) srsStageCount++;
    if (d.srsSchedule) srsScheduleCount++;
    if (d.nextReviewDate) nextReviewDateCount++;

    if (d.isRecoveryMastered) {
      recoveryMasteredCount++;
      if (currentMastery < 90) {
        recoveryBelow90Count++;
        candidatesForRebalancing.push({
          id: docId,
          studentCode,
          topicCode,
          reason: 'isRecoveryMastered is true but mastery is below 90',
          currentMastery,
          targetMastery: 90
        });
      }
    }

    // Check if historical submissions had reached >= 90% or masteryBefore was >= 90 but current is < 90
    const key = `${studentCode}_${topicCode}`;
    const subs = topicSubmissionsMap.get(key) || [];
    let hadEverReached90 = false;
    let highestPastMastery = currentMastery;

    subs.forEach(s => {
      const mb = Number(s.masteryBefore || 0);
      const ma = Number(s.finalMastery || s.masteryAfter || 0);
      if (mb >= 90 || ma >= 90) hadEverReached90 = true;
      if (mb > highestPastMastery) highestPastMastery = mb;
      if (ma > highestPastMastery) highestPastMastery = ma;
    });

    if (hadEverReached90 && currentMastery < 90) {
      demotedOr85Count++;
      candidatesForRebalancing.push({
        id: docId,
        studentCode,
        topicCode,
        reason: 'Previously reached >=90% mastery but demoted to <90%',
        currentMastery,
        highestPastMastery: Math.max(90, highestPastMastery),
        targetMastery: Math.max(90, highestPastMastery)
      });
    }
  });

  console.log('\n--- AUDIT SUMMARY ---');
  console.log({
    srsStageCount,
    srsScheduleCount,
    nextReviewDateCount,
    recoveryMasteredCount,
    recoveryBelow90Count,
    demotedOr85Count,
    totalCandidatesForRebalancing: candidatesForRebalancing.length
  });

  if (candidatesForRebalancing.length > 0) {
    console.log('\nSample Candidates for Rebalancing:');
    console.log(candidatesForRebalancing.slice(0, 10));
  }
}

inspect().catch(console.error);
