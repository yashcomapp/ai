const admin = require('firebase-admin');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const db = admin.firestore();

function cleanBoilerplateSolution(sol, correctAnswer) {
  let cleaned = sol;

  // 1. Strip the robotic top "Key Concept" / "The fundamental relationship dictates that" block
  cleaned = cleaned.replace(/^[\s\S]*?The fundamental relationship dictates that:\s*\\\[[\s\S]*?\\\]\s*/i, '');
  cleaned = cleaned.replace(/^\s*\*\*Key Concept:\*\*\s*/i, '');

  // 2. Strip the robotic bottom Option Analysis if it's the repetitive template
  if (cleaned.includes('**Option Analysis:**') || cleaned.includes('Option Analysis:')) {
    if (cleaned.includes('Directly satisfies the physical equations') || cleaned.includes('Does not satisfy the kinematic or dynamic conditions')) {
      cleaned = cleaned.replace(/\n*\*{0,2}Option Analysis:\*{0,2}[\s\S]*$/i, '');
    }
  }

  // 3. Normalize newlines
  cleaned = cleaned.replace(/\\n/g, '\n');
  cleaned = cleaned.trim();

  // 4. Ensure it ends with clean "Correct Choice is (X)."
  if (!cleaned.includes(`Correct Choice is (${correctAnswer})`)) {
    cleaned += `\n\nCorrect Choice is (${correctAnswer}).`;
  }

  return cleaned;
}

async function run() {
  console.log('Searching for questions with boilerplate explanations...');
  const snap = await db.collection('questions').get();

  const toUpdate = [];
  snap.forEach(d => {
    const data = d.data();
    const sol = data.solution || '';
    if (sol.includes('The fundamental relationship dictates that') || sol.includes('Correct Outcome') || sol.includes('Directly satisfies the physical equations')) {
      toUpdate.push({
        id: d.id,
        ref: d.ref,
        oldSol: sol,
        newSol: cleanBoilerplateSolution(sol, data.correctAnswer)
      });
    }
  });

  console.log(`Found ${toUpdate.length} questions to clean.`);
  if (toUpdate.length === 0) {
    console.log('None found. Exiting.');
    return;
  }

  // Mandatory Pre-Mutation Snapshot (Rule Q)
  await createPreMutationSnapshot(['questions'], 'Clean robotic Key Concept boilerplate from explanations');

  let batch = db.batch();
  let count = 0;
  for (const item of toUpdate) {
    batch.update(item.ref, {
      solution: item.newSol,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    count++;
    if (count % 400 === 0) {
      await batch.commit();
      batch = db.batch();
      console.log(`Committed batch of 400 updates.`);
    }
  }

  if (count % 400 !== 0) {
    await batch.commit();
  }

  console.log(`Successfully cleaned all ${toUpdate.length} questions in Firestore!`);
}

run().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
