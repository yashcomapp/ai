const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

// Scientific explanations for the 12 questions that previously had "Fact"
const scientificExplanations = {
  'MH-8-SCI-10-10.1-OSC-002': 'Cell organelles like the nucleus, mitochondria, and endoplasmic reticulum perform vital metabolic and reproductive functions essential for cellular homeostasis and survival.',
  'MH-8-SCI-10-10.1-OSC-010': 'The plasma membrane is a selectively permeable phospholipid bilayer with embedded proteins, regulating the entry and exit of ions and nutrients into the cell.',
  'MH-8-SCI-10-10.1-OSC-026': 'The nucleus contains chromosomes composed of DNA and proteins, which store genetic instructions for protein synthesis and heredity.',
  'MH-8-SCI-10-10.1-OSC-122': 'Endoplasmic reticulum forms an interconnected network of membranes facilitating the synthesis, folding, and transport of proteins and lipids.',
  'MH-8-SCI-10-10.2-OSC-016': 'Golgi apparatus modifies, sorts, and packages macromolecules into vesicles for secretion or delivery to cellular destinations.',
  'MH-8-SCI-11-11.1-OSC-007': 'A human red blood cell (erythrocyte) has an approximate diameter of 7 micrometers (µm) and lacks a nucleus at maturity to maximize hemoglobin carrying capacity.',
  'MH-8-SCI-11-11.1-OSC-010': 'Blood consists of 55% liquid plasma and 45% formed cellular elements including erythrocytes, leukocytes, and thrombocytes.',
  'MH-8-SCI-11-11.1-OSC-013': 'Hemoglobin contains iron (Fe²⁺) which reversibly binds to oxygen molecules, forming oxyhemoglobin to transport oxygen from lungs to body tissues.',
  'MH-8-SCI-13-13.1-OSC-012': 'Chemical change involves the breaking of existing chemical bonds and formation of new bonds, resulting in products with fundamentally different chemical properties.',
  'MH-8-SCI-19-19.1-OSC-019': 'Stars are gigantic celestial spheres of hot, ionized plasma that generate energy through nuclear fusion of hydrogen into helium in their core.',
  'MH-8-SCI-19-19.1-OSC-024': 'The Sun is an average main-sequence star situated in the Orion Arm of the Milky Way galaxy, orbiting the galactic center at approximately 220 km/s.',
  'MH-8-SCI-2-2.1-OSC-022': 'Pathogenic microorganisms produce toxins or directly invade host tissues, compromising normal physiological functioning and causing infectious diseases.'
};

async function executeFix() {
  console.log('=== STARTING QUESTION BANK PERMANENT PURGE & BALANCING ===');

  const auditData = JSON.parse(fs.readFileSync('audit_results.json', 'utf-8'));
  const placeholderIds = new Set(auditData.issues.placeholderOptions.map(p => p.id));
  console.log(`Found ${placeholderIds.size} corrupted/placeholder questions to delete.`);

  // --- Step 1: Delete corrupted questions ---
  let deleteBatch = db.batch();
  let deleteCount = 0;
  for (const id of placeholderIds) {
    deleteBatch.delete(db.collection('questions').doc(id));
    deleteCount++;
    if (deleteCount % 400 === 0) {
      await deleteBatch.commit();
      deleteBatch = db.batch();
      console.log(`Committed ${deleteCount} deletions...`);
    }
  }
  if (deleteCount % 400 !== 0) {
    await deleteBatch.commit();
  }
  console.log(`✓ Successfully deleted ${deleteCount} corrupted/placeholder questions from Firestore.`);

  // --- Step 2: Fetch all remaining questions and group by topic ---
  console.log('\nFetching all remaining questions to balance per topic...');
  const snap = await db.collection('questions').get();
  console.log(`Total active questions: ${snap.size}`);

  const topicMap = {};
  snap.docs.forEach(doc => {
    const d = doc.data();
    const id = doc.id;
    const qCode = d.questionCode || id;
    const topicCode = d.topicCode || qCode.split('-').slice(0, 5).join('-');
    if (!topicMap[topicCode]) topicMap[topicCode] = [];
    topicMap[topicCode].push({ id, ...d });
  });

  console.log(`Grouped into ${Object.keys(topicMap).length} topics.`);

  // --- Step 3: Balance each topic in Firestore ---
  let updateBatch = db.batch();
  let updateCount = 0;

  for (const [tCode, questions] of Object.entries(topicMap)) {
    // Filter objective questions
    const objectives = questions.filter(q => {
      const t = (q.type || 'OSC').toUpperCase();
      return ['OSC', 'OMC', 'OTF', 'OAR'].includes(t) && Array.isArray(q.options) && q.options.length >= 4;
    });

    if (objectives.length < 4) continue;

    // Check explanation updates first
    questions.forEach(q => {
      if (scientificExplanations[q.id]) {
        updateBatch.update(db.collection('questions').doc(q.id), {
          explanation: scientificExplanations[q.id],
          solution: scientificExplanations[q.id],
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        updateCount++;
      }
    });

    // Count answer distribution in this topic
    const dist = { A: 0, B: 0, C: 0, D: 0 };
    objectives.forEach(q => {
      const a = (q.correctAnswer || '').trim().toUpperCase();
      if (dist[a] !== undefined) dist[a]++;
    });

    const targetPerLetter = Math.ceil(objectives.length / 4);

    // If Option A is over-represented in this topic (> targetPerLetter + 1)
    const excessA = objectives.filter(q => (q.correctAnswer || '').trim().toUpperCase() === 'A');

    if (excessA.length > targetPerLetter) {
      // Letters that need more questions
      const neededLetters = ['B', 'C', 'D'];
      let targetIdx = 0;

      for (let i = targetPerLetter; i < excessA.length; i++) {
        const q = excessA[i];
        const newLetter = neededLetters[targetIdx % neededLetters.length];
        targetIdx++;

        const newTargetIndex = newLetter.charCodeAt(0) - 65;
        const currentOptions = [...q.options];

        // Format could be string or object { text, isCorrect }
        const isObjectFormat = typeof currentOptions[0] === 'object' && currentOptions[0] !== null;

        // Current correct is at index 0 (A)
        // Swap index 0 with newTargetIndex
        const temp = currentOptions[0];
        currentOptions[0] = currentOptions[newTargetIndex];
        currentOptions[newTargetIndex] = temp;

        if (isObjectFormat) {
          currentOptions.forEach((opt, idx) => {
            opt.isCorrect = (idx === newTargetIndex);
          });
        }

        const updateData = {
          options: currentOptions,
          correctAnswer: newLetter,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        };

        updateBatch.update(db.collection('questions').doc(q.id), updateData);
        updateCount++;

        if (updateCount % 400 === 0) {
          await updateBatch.commit();
          updateBatch = db.batch();
          console.log(`Committed ${updateCount} topic-balancing updates...`);
        }
      }
    }
  }

  if (updateCount % 400 !== 0) {
    await updateBatch.commit();
  }

  console.log(`✓ Completed balancing! Total updates committed: ${updateCount}`);
}

executeFix().catch(console.error);
