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

async function run() {
  const batchesSnap = await db.collection('batches').get();
  const batchMap = {};
  batchesSnap.forEach(doc => {
    const d = doc.data();
    batchMap[doc.id] = d.name || d.batchName || doc.id;
  });

  const studentsSnap = await db.collection('users').where('role', '==', 'student').get();
  const students = [];

  studentsSnap.forEach(doc => {
    const d = doc.data();
    const batchName = batchMap[d.batchId] || d.batch || d.batchName || d.className || 'Unassigned';
    students.push({
      id: doc.id,
      studentCode: d.studentCode || doc.id,
      name: d.name || d.displayName || d.studentName || 'Unknown',
      email: d.email || '',
      phone: d.phone || d.mobile || '',
      batchId: d.batchId || '',
      batchName: batchName,
      autonomous: d.autonomous === true,
      mode: d.autonomous === true ? 'Autonomous' : 'Regular',
      status: d.status || 'active',
      rollNo: d.rollNo || d.rollNumber || '',
      parentName: d.parentName || '',
      parentPhone: d.parentPhone || d.parentMobile || ''
    });
  });

  console.log(`Total students fetched: ${students.length}`);
  
  // Group by batch
  const byBatch = {};
  students.forEach(s => {
    if (!byBatch[s.batchName]) {
      byBatch[s.batchName] = { autonomous: [], regular: [], all: [] };
    }
    byBatch[s.batchName].all.push(s);
    if (s.autonomous) {
      byBatch[s.batchName].autonomous.push(s);
    } else {
      byBatch[s.batchName].regular.push(s);
    }
  });

  console.log('Batch Summary:');
  Object.keys(byBatch).sort().forEach(bName => {
    const b = byBatch[bName];
    console.log(`- ${bName}: Total = ${b.all.length} | Autonomous = ${b.autonomous.length} | Regular = ${b.regular.length}`);
  });

  fs.writeFileSync('scripts/students_dump.json', JSON.stringify({ students, byBatch, batchMap }, null, 2));
}

run().catch(console.error);
