const fs = require('fs');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
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
if (sa) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
}
const db = admin.firestore();

async function checkCollections() {
  const collections = [
    'disputes',
    'peerAssignments',
    'faultEvents',
    'faultCategories',
    'classroomTests',
    'proctoringLogs',
    'evaluations',
    'leaveApplications',
    'attendanceDeclarations',
    'session_logs',
    'userTimeLogs',
    'parentReviews',
    'reviews',
    'subjectiveAttempts',
    'studentTopicMastery'
  ];

  const results = {};
  for (const c of collections) {
    try {
      const snap = await db.collection(c).get();
      results[c] = snap.size;
    } catch (e) {
      results[c] = 'Error: ' + e.message;
    }
  }
  console.log('Collection document counts:', JSON.stringify(results, null, 2));

  // Check honesty alerts
  const masterySnap = await db.collection('studentTopicMastery').get();
  let honestyAlertCount = 0;
  masterySnap.docs.forEach(doc => {
    const d = doc.data();
    if (d.honestyAlerts && Array.isArray(d.honestyAlerts) && d.honestyAlerts.length > 0) {
      honestyAlertCount += d.honestyAlerts.length;
    }
  });
  console.log('Total Honesty Alerts in Topic Masteries:', honestyAlertCount);

  // Check peer review usage
  const peerSnap = await db.collection('peerAssignments').get();
  console.log('Peer Assignments sample:', peerSnap.docs.map(d => d.data()));

  // Check disputes usage
  const disputesSnap = await db.collection('disputes').get();
  console.log('Disputes sample:', disputesSnap.docs.map(d => d.data()));

  // Check fault events
  const faultsSnap = await db.collection('faultEvents').get();
  console.log('Fault events sample:', faultsSnap.docs.map(d => d.data()));
}

checkCollections().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
