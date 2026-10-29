const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapResult = await createPreMutationSnapshot(
    ['questions'],
    'chapter_19_foundation_core_compact_and_topics_expansion'
  );
  console.log('Snapshot successfully recorded in _systemBackups');

  const db = admin.firestore();
  const allEnhanced = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_19_full_compact.json', 'utf8'));
  console.log(`\n=== Step 2: Committing ${allEnhanced.length} Questions to Firestore ===`);

  // Write in batches of 45 (~6 batches for 245 docs)
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
    'MH-9-SCIT-19-19.1-OSC-001', // 19.1 Heat SI unit
    'MH-9-SCIT-19-19.1-OSC-007', // 19.1 Railway tracks (curated catchall)
    'MH-9-SCIT-19-19.1-OSC-029', // 19.1 Latent heat
    'MH-9-SCIT-19-19.2-OSC-001', // 19.2 Speed calculation
    'MH-9-SCIT-19-19.2-OTF-001', // 19.2 Work definition
    'MH-9-SCIT-19-19.2-OAR-001', // 19.2 Work angle 90
    'MH-9-SCIT-19-19.3-OSC-001', // 19.3 Chemical change
    'MH-9-SCIT-19-19.3-OTF-001', // 19.3 Curdling of milk
    'MH-9-SCIT-19-19.3-OAR-001'  // 19.3 Coastal rusting
  ];

  for (const c of verifyCodes) {
    const qSnap = await db.collection('questions').where('questionCode', '==', c).get();
    if (qSnap.empty) {
      console.error(`Verification FAILED for ${c}: Document not found in Firestore!`);
    } else {
      const d = qSnap.docs[0].data();
      const hasKC = d.solution && d.solution.includes('**Key Concept:**');
      const hasDep = d.solution && d.solution.includes('### 1.');
      console.log(`[VERIFIED] ${c} (Topic: ${d.topicCode}): isEnhanced=${d.isEnhanced}, hasKeyConcept=${hasKC}, hasDeprecated=${hasDep}`);
    }
  }

  // Count docs in Firestore for Chapter 19
  const countSnap = await db.collection('questions')
    .where('chapterNumber', 'in', ['19', 19])
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .get();

  let compactCount = 0;
  let deprecatedCount = 0;
  countSnap.forEach(doc => {
    const sol = doc.data().solution || '';
    if (sol.includes('**Key Concept:**') && !sol.includes('### 1.')) {
      compactCount++;
    } else if (sol.includes('### 1.')) {
      deprecatedCount++;
    }
  });

  console.log(`\n=== Chapter 19 Live DB Final Audit ===`);
  console.log(`Total Chapter 19 Docs in DB: ${countSnap.size}`);
  console.log(`Compact Gold Standard: ${compactCount} / ${countSnap.size}`);
  console.log(`Deprecated Format: ${deprecatedCount}`);

  if (compactCount === 245 && deprecatedCount === 0) {
    console.log('🎉 SUCCESS: All 245 Chapter 19 questions are verified live in Firestore in the Compact Gold Standard!');
  } else {
    console.warn(`WARNING: Verification count: compact=${compactCount}, expected=245`);
  }
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
