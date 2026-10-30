const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function inspectCh3() {
  const snap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-3-3.1')
    .get();

  console.log(`Found ${snap.size} questions for Topic 3.1`);
  snap.docs.slice(0, 15).forEach((d, i) => {
    const data = d.data();
    console.log(`${i+1}. [${d.id}] (${data.type}) [vault: ${data.vault}]: ${data.text.slice(0, 80)}...`);
  });
}

inspectCh3().catch(console.error);
