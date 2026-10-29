const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapResult = await createPreMutationSnapshot(
    ['questions'],
    'chapter_17_biotechnology_compact_and_topics_expansion'
  );
  console.log('Snapshot successfully recorded in _systemBackups');

  const db = admin.firestore();
  const allEnhanced = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_17_full_enhanced.json', 'utf8'));
  console.log(`\n=== Step 2: Committing ${allEnhanced.length} Questions to Firestore ===`);

  // Write in batches of 45 (~4 batches for 187 docs)
  const batchSize = 45;
  for (let i = 0; i < allEnhanced.length; i += batchSize) {
    const chunk = allEnhanced.slice(i, i + batchSize);
    const batch = db.batch();

    chunk.forEach(q => {
      const docRef = db.collection('questions').doc(q.id);
      batch.set(docRef, {
        ...q,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      }, { merge: true });
    });

    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / batchSize) + 1} (${chunk.length} docs)`);
  }

  console.log('\n=== Step 3: Verification Readbacks across all 3 Topics ===');
  const verifyCodes = [
    'MH-9-SCIT-17-17.1-OSC-001', // 17.1
    'MH-9-SCIT-17-17.1-OSC-056', // 17.1 totipotency
    'MH-9-SCIT-17-17.2-OSC-001', // 17.2 Bt Cotton
    'MH-9-SCIT-17-17.2-OAR-001', // 17.2 OAR
    'MH-9-SCIT-17-17.3-OSC-001', // 17.3 Gir
    'MH-9-SCIT-17-17.3-OMC-001'  // 17.3 OMC
  ];

  for (const c of verifyCodes) {
    const qSnap = await db.collection('questions').where('questionCode', '==', c).get();
    if (qSnap.empty) {
      console.error(`Verification FAILED for ${c}: Document not found in Firestore!`);
    } else {
      const d = qSnap.docs[0].data();
      console.log(`[VERIFIED] ${c} (Topic: ${d.topicCode}): isEnhanced=${d.isEnhanced}, hasKeyConcept=${d.solution && d.solution.includes('**Key Concept:**')}, hasDeprecated=${d.solution && d.solution.includes('### 1.')}`);
      console.log(`  Preview: ${d.text.slice(0, 75)}...`);
    }
  }

  // Count docs in Firestore for Chapter 17
  const countSnap = await db.collection('questions')
    .where('chapterNumber', 'in', ['17', 17])
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  const topicCounts = {};
  countSnap.forEach(d => {
    const tc = d.data().topicCode || 'NO_TOPIC';
    topicCounts[tc] = (topicCounts[tc] || 0) + 1;
  });

  console.log('\n=== Final Live Chapter 17 Topic Distribution ===');
  console.log('Total Chapter 17 Docs in Firestore:', countSnap.size);
  console.log('Counts per topic:', topicCounts);

  console.log('\nChapter 17 Firestore enhancement & curriculum expansion completed successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
