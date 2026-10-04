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
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function run() {
  console.log('Finding all autonomous students...');
  const autoStudentsSnap = await db.collection('users')
    .where('role', '==', 'student')
    .where('autonomous', '==', true)
    .get();

  const autoStudentCodes = autoStudentsSnap.docs
    .map(d => d.data().studentCode)
    .filter(Boolean);

  console.log(`Found ${autoStudentCodes.length} autonomous students:`, autoStudentCodes);

  let updatedReviews = 0;
  let updatedAttempts = 0;

  for (const sCode of autoStudentCodes) {
    // 1. Check reviews collection for status == 'pending'
    const pendingRevSnap = await db.collection('reviews')
      .where('studentCode', '==', sCode)
      .where('status', '==', 'pending')
      .get();

    if (!pendingRevSnap.empty) {
      const batch = db.batch();
      pendingRevSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'approved',
          updatedAt: new Date(),
          autoApprovedAutonomous: true
        });
        updatedReviews++;
      });
      await batch.commit();
      console.log(`- Student ${sCode}: approved ${pendingRevSnap.size} pending reviews`);
    }

    // 2. Check examAttempts collection for status == 'pending'
    const pendingAttSnap = await db.collection('examAttempts')
      .where('studentCode', '==', sCode)
      .where('status', '==', 'pending')
      .get();

    if (!pendingAttSnap.empty) {
      const batch = db.batch();
      pendingAttSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'approved',
          updatedAt: new Date(),
          autoApprovedAutonomous: true
        });
        updatedAttempts++;
      });
      await batch.commit();
      console.log(`- Student ${sCode}: approved ${pendingAttSnap.size} pending examAttempts`);
    }
  }

  console.log(`Migration Complete: Updated ${updatedReviews} reviews and ${updatedAttempts} examAttempts to 'approved'.`);
}

run().catch(console.error);
