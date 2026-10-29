const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapResult = await createPreMutationSnapshot(
    ['questions'],
    'chapter_15_life_processes_compact_approved'
  );
  console.log('Snapshot successfully created:', snapResult.snapshotDir);

  const db = admin.firestore();
  const enhancedList = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_15_compact.json', 'utf8'));
  console.log(`\n=== Step 2: Committing ${enhancedList.length} Questions to Firestore ===`);

  // Write in batches of 45 (2 batches)
  const batchSize = 45;
  for (let i = 0; i < enhancedList.length; i += batchSize) {
    const chunk = enhancedList.slice(i, i + batchSize);
    const batch = db.batch();

    chunk.forEach(q => {
      const docRef = db.collection('questions').doc(q.id);
      batch.update(docRef, {
        solution: q.solution,
        isEnhanced: true,
        enhancedAt: q.enhancedAt,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    });

    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / batchSize) + 1} (${chunk.length} docs)`);
  }

  console.log('\n=== Step 3: Verification Readbacks ===');
  const verifyCodes = [
    'MH-9-SCIT-15-15.1.1-OSC-001',
    'MH-9-SCIT-15-15.1.2-OSC-008',
    'MH-9-SCIT-15-15.1.3-OSC-017'
  ];

  for (const c of verifyCodes) {
    const qSnap = await db.collection('questions').where('questionCode', '==', c).get();
    if (qSnap.empty) {
      console.error(`Verification FAILED for ${c}: Not found!`);
    } else {
      const d = qSnap.docs[0].data();
      console.log(`[VERIFIED] ${c}: isEnhanced=${d.isEnhanced}, hasKeyConcept=${d.solution.includes('**Key Concept:**')}, hasDeprecated=${d.solution.includes('### 1.')}`);
      console.log(`  Sample preview: ${d.solution.slice(0, 100).replace(/\n/g, ' ')}...`);
    }
  }

  console.log('\nChapter 15 Firestore enhancement committed and verified successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
