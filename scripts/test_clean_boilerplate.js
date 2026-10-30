const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

function cleanBoilerplateSolution(sol, correctAnswer) {
  let cleaned = sol;

  // 1. Strip the robotic top "Key Concept" / "The fundamental relationship dictates that" block
  // Pattern: matches from start (or after **Key Concept:**) through \[ ... \text{Correct Outcome} ... \]
  cleaned = cleaned.replace(/^[\s\S]*?The fundamental relationship dictates that:\s*\\\[[\s\S]*?\\\]\s*/i, '');
  cleaned = cleaned.replace(/^\s*\*\*Key Concept:\*\*\s*/i, '');

  // 2. Strip the robotic bottom Option Analysis if it's the repetitive template
  // Check if it ends with the robotic Option Analysis
  if (cleaned.includes('**Option Analysis:**') || cleaned.includes('Option Analysis:')) {
    // Check if the Option Analysis is the robotic template
    if (cleaned.includes('Directly satisfies the physical equations') || cleaned.includes('Does not satisfy the kinematic or dynamic conditions')) {
      // Split off the robotic Option Analysis block completely
      cleaned = cleaned.replace(/\n*\*{0,2}Option Analysis:\*{0,2}[\s\S]*$/i, '');
    }
  }

  // 3. Remove any remaining "\n\n\n" or trailing/leading junk
  cleaned = cleaned.replace(/\\n/g, '\n'); // fix escaped newlines if any
  cleaned = cleaned.trim();

  // 4. Ensure it ends with clean "Correct Choice is (X)."
  if (!cleaned.includes(`Correct Choice is (${correctAnswer})`)) {
    cleaned += `\n\nCorrect Choice is (${correctAnswer}).`;
  }

  return cleaned;
}

async function testClean() {
  const snap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-1-1.1')
    .limit(3)
    .get();

  snap.forEach(d => {
    const data = d.data();
    console.log('=== BEFORE (ID: ' + d.id + ') ===');
    console.log(data.solution);
    console.log('\n=== AFTER ===');
    console.log(cleanBoilerplateSolution(data.solution, data.correctAnswer));
    console.log('====================================\n');
  });
}

testClean().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
