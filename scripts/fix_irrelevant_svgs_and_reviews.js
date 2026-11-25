const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
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

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

function stripSvgWrapper(str) {
  if (typeof str !== 'string') return str;
  return str
    .replace(/<div[^>]*>[\s\S]*?<\/svg>\s*<\/div>\s*/gi, '')
    .replace(/<svg[\s\S]*?<\/svg>\s*/gi, '')
    .trim();
}

async function run() {
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });

  // 1. Fix MH-10-MTH2-4-4.2.1 questions with Tangent-to-Circle SVG
  const qSnap = await db.collection('questions').where('topicCode', '==', 'MH-10-MTH2-4-4.2.1').get();
  const qUpdates = [];
  const qBackups = [];
  qSnap.forEach(doc => {
    const q = doc.data();
    const txt = String(q.text || '');
    if (txt.includes('Tangent to a Circle') && !txt.toLowerCase().includes('tangent')) {
      qBackups.push({ id: doc.id, data: q });
      qUpdates.push({
        ref: doc.ref,
        text: stripSvgWrapper(txt)
      });
    }
  });

  if (qUpdates.length > 0) {
    fs.writeFileSync(
      path.join(backupDir, `snapshot_svg_4_2_1_${Date.now()}.json`),
      JSON.stringify(qBackups, null, 2),
      'utf-8'
    );
    const batch = db.batch();
    qUpdates.forEach(u => batch.update(u.ref, { text: u.text, updatedAt: admin.firestore.FieldValue.serverTimestamp() }));
    await batch.commit();
  }
  console.log(`✓ Stripped irrelevant Tangent-to-Circle SVG from ${qUpdates.length} questions in MH-10-MTH2-4-4.2.1.`);

  // 2. Fix saved reviews for Exam 028 where Q8/Q9 still had the Frustum SVG snapshot
  const revSnap = await db.collection('reviews').where('examId', '==', '028-MH-10-Mensuration,-7.1-7.2-241126').get();
  const revBackups = [];
  let revUpdated = 0;
  for (const doc of revSnap.docs) {
    const r = doc.data();
    const qd = Array.isArray(r.questionDetails) ? [...r.questionDetails] : [];
    let changed = false;
    for (let i = 0; i < qd.length; i++) {
      const qt = String(qd[i]?.questionText || '');
      if (qt.includes('Frustum of a Cone') && qt.toLowerCase().includes('sphere')) {
        qd[i] = { ...qd[i], questionText: stripSvgWrapper(qt) };
        changed = true;
      }
    }
    if (changed) {
      revBackups.push({ id: doc.id, data: r });
      await doc.ref.update({ questionDetails: qd });
      revUpdated++;
    }
  }
  if (revBackups.length > 0) {
    fs.writeFileSync(
      path.join(backupDir, `snapshot_reviews_028_svg_${Date.now()}.json`),
      JSON.stringify(revBackups, null, 2),
      'utf-8'
    );
  }
  console.log(`✓ Stripped irrelevant Frustum SVG from ${revUpdated} saved review documents for Exam 028.`);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
