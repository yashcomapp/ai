const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapResult = await createPreMutationSnapshot(
    ['questions'],
    'chapter_18_observing_space_telescopes_compact_approved'
  );
  console.log('Snapshot successfully created and logged in _systemBackups');

  const db = admin.firestore();
  const allEnhanced = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_18_compact.json', 'utf8'));
  console.log(`\n=== Step 2: Committing ${allEnhanced.length} Questions to Firestore ===`);

  // Write in batches of 45 (~8 batches for 317 docs)
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

  console.log('\n=== Step 3: Verification Readbacks across all 6 Topics ===');
  const verifyCodes = [
    'MH-9-SCIT-18-18.1.1-OSC-001', // 18.1.1 EM spectrum
    'MH-9-SCIT-18-18.1.1-OAR-001', // 18.1.1 OAR
    'MH-9-SCIT-18-18.2.1-OSC-001', // 18.2.1 Refractor
    'MH-9-SCIT-18-18.2.1-OAR-001', // 18.2.1 Chromatic aberration
    'MH-9-SCIT-18-18.2.2-OSC-001', // 18.2.2 Reflector
    'MH-9-SCIT-18-18.2.2-OMC-001', // 18.2.2 OMC
    'MH-9-SCIT-18-18.3.1-OSC-001', // 18.3.1 GMRT
    'MH-9-SCIT-18-18.3.1-OAR-001', // 18.3.1 GMRT mesh
    'MH-9-SCIT-18-18.4.1-OSC-001', // 18.4.1 Twinkling
    'MH-9-SCIT-18-18.4.1-OAR-001', // 18.4.1 Atmospheric blur
    'MH-9-SCIT-18-18.4.2-OSC-001', // 18.4.2 Chandra
    'MH-9-SCIT-18-18.4.2-OMC-001'  // 18.4.2 Chandrasekhar limit
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

  // Count docs in Firestore for Chapter 18
  const countSnap = await db.collection('questions')
    .where('chapterNumber', 'in', ['18', 18])
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

  console.log(`\n=== Chapter 18 Live DB Final Audit ===`);
  console.log(`Total Chapter 18 Docs: ${countSnap.size}`);
  console.log(`Compact Gold Standard: ${compactCount} / ${countSnap.size}`);
  console.log(`Deprecated Format: ${deprecatedCount}`);

  if (compactCount === 317 && deprecatedCount === 0) {
    console.log('🎉 SUCCESS: All 317 Chapter 18 questions are verified live in Firestore in the Compact Gold Standard!');
  } else {
    console.warn(`WARNING: Verification count mismatch: compact=${compactCount}, expected=317`);
  }
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
