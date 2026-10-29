const fs = require('fs');
const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');

async function main() {
  console.log('=== Step 1: Pre-Mutation Snapshot (Rule 2Q) ===');
  const snapResult = await createPreMutationSnapshot(
    ['questions'],
    'chapter_20_general_knowledge_compact_approved'
  );
  console.log('Snapshot successfully recorded in _systemBackups');

  const db = admin.firestore();
  const allEnhanced = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_20_curated.json', 'utf8'));
  console.log(`\n=== Step 2: Committing ${allEnhanced.length} Questions to Firestore ===`);

  // Write in batches of 45 (~10 batches for 414 docs)
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

  console.log('\n=== Step 3: Verification Readbacks across Topics 20.1, 20.2, 20.3 ===');
  const verifyCodes = [
    'MH-9-SCIT-20-20.1-OSC-006', // 20.1 Agni-V
    'MH-9-SCIT-20-20.1-OSC-014', // 20.1 Cryogenic engine
    'MH-9-SCIT-20-20.1-OSC-021', // 20.1 Mangalyaan
    'MH-9-SCIT-20-20.1-OSC-101', // 20.2 Benjamin Franklin
    'MH-9-SCIT-20-20.1-OSC-126', // 20.2 Bhatnagar award
    'MH-9-SCIT-20-20.1-OSC-001', // 20.3 Kidney stone oxalic acid
    'MH-9-SCIT-20-20.1-OSC-004', // 20.3 Bharatpur of Maharashtra
    'MH-9-SCIT-20-20.1-OSC-026', // 20.3 Stem cells regenerative medicine
    'MH-9-SCIT-20-20.1-OSC-226'  // 20.3 Epidemiology
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
      console.log(`  Preview: ${d.text.slice(0, 75)}...`);
    }
  }

  // Count docs in Firestore for Chapter 20
  const countSnap = await db.collection('questions')
    .where('chapterNumber', 'in', ['20', 20])
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

  console.log(`\n=== Chapter 20 Live DB Final Audit ===`);
  console.log(`Total Chapter 20 Docs in DB: ${countSnap.size}`);
  console.log(`Compact Gold Standard: ${compactCount} / ${countSnap.size}`);
  console.log(`Deprecated Format: ${deprecatedCount}`);

  if (compactCount === 414 && deprecatedCount === 0) {
    console.log('🎉 SUCCESS: All 414 Chapter 20 questions are verified live in Firestore in the Compact Gold Standard!');
  } else {
    console.warn(`WARNING: Verification count: compact=${compactCount}, expected=414`);
  }
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
