const path = require('path');
const fs = require('fs');

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
if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(serviceAccount.startsWith('{') ? serviceAccount : Buffer.from(serviceAccount, 'base64').toString('utf8'));
    admin.initializeApp({ credential: admin.credential.cert(credential) });
  }
}
const db = admin.firestore();

async function run() {
  const qSnap = await db.collection('questions').where('usedInClassroomTest', '==', true).get();
  console.log('Total questions marked with usedInClassroomTest: true =', qSnap.size);

  const [examsSnap, subjExamsSnap] = await Promise.all([
    db.collection('exams').get(),
    db.collection('subjectiveExams').get()
  ]);
  console.log('Total active objective exams =', examsSnap.size);
  console.log('Total active subjective exams =', subjExamsSnap.size);

  const activeUsedCodes = new Set();
  examsSnap.docs.forEach(d => {
    const data = d.data();
    (data.questionCodes || data.questionIds || []).forEach(c => activeUsedCodes.add(String(c).trim()));
    if (Array.isArray(data.questions)) {
      data.questions.forEach(q => {
        if (q.id) activeUsedCodes.add(String(q.id).trim());
        if (q.questionCode) activeUsedCodes.add(String(q.questionCode).trim());
      });
    }
  });
  subjExamsSnap.docs.forEach(d => {
    const data = d.data();
    (data.questionCodes || data.questionIds || []).forEach(c => activeUsedCodes.add(String(c).trim()));
    if (Array.isArray(data.questions)) {
      data.questions.forEach(q => {
        if (q.id) activeUsedCodes.add(String(q.id).trim());
        if (q.questionCode) activeUsedCodes.add(String(q.questionCode).trim());
      });
    }
  });

  const orphanedDocs = [];
  qSnap.docs.forEach(d => {
    const qData = d.data();
    const id = d.id;
    const code = String(qData.questionCode || '').trim();
    if (!activeUsedCodes.has(id) && !activeUsedCodes.has(code)) {
      orphanedDocs.push(d);
    }
  });

  console.log('Questions locked by deleted exams (orphaned) =', orphanedDocs.length);
  
  if (orphanedDocs.length > 0) {
    console.log('Sample locked questions to release:');
    orphanedDocs.slice(0, 10).forEach(d => {
      console.log(`- ID: ${d.id}, Code: ${d.data().questionCode}, Topic: ${d.data().topicCode}`);
    });

    // Release them in batch
    let batch = db.batch();
    let count = 0;
    for (const doc of orphanedDocs) {
      batch.update(doc.ref, { usedInClassroomTest: false });
      count++;
      if (count % 450 === 0) {
        await batch.commit();
        batch = db.batch();
      }
    }
    if (count % 450 !== 0) {
      await batch.commit();
    }
    console.log(`Successfully released ${count} locked questions back into the vault!`);
  }
}

run().catch(console.error);
