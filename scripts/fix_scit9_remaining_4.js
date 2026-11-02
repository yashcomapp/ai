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
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

async function fixSCIT9Items() {
  console.log('Fixing 4 remaining SCIT 9 questions...');

  // 1. Ch 10 Navier-Stokes question -> Replace with clean RAM question
  await db.collection('questions').doc('MH-9-SCIT-10-10.3-OSC-020').update({
    text: "Which computer memory component temporarily holds the operating system, running applications, and current data being processed by the CPU?",
    options: [
      "RAM (Random Access Memory)",
      "CD-ROM",
      "Magnetic Tape",
      "Printer Buffer"
    ],
    correctAnswer: "A",
    correctAnswers: [],
    solution: "RAM is the temporary high-speed working memory that stores programs and data currently in active use by the central processor.",
    explanation: "RAM is the temporary high-speed working memory that stores programs and data currently in active use by the central processor.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  // 2. Ch 4 Avogadro formula
  await db.collection('questions').doc('MH-9-SCIT-4-4.3-OFB-066').update({
    text: "Fill in the blank: The formula for calculating the total number of particles (atoms/molecules) from the number of moles \\(n\\) is \\(N = n \\times\\) ________.",
    options: [
      "Avogadro's constant (\\(N_A\\))",
      "Molar mass (\\(M\\))",
      "Volume in liters (\\(V\\))",
      "Mass of sample in grams (\\(m\\))"
    ],
    correctAnswer: "A",
    correctAnswers: [],
    solution: "The total number of particles is given by multiplying the number of moles by Avogadro's number: \\(N = n \\times N_A\\).",
    explanation: "The total number of particles is given by multiplying the number of moles by Avogadro's number: \\(N = n \\times N_A\\).",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  // 3. Ch 16 parental dihybrid genotypes
  await db.collection('questions').doc('MH-9-SCIT-16-16.4-OSC-003').update({
    text: "What are the genotypes of the pure-breeding parental plants (P1) in Mendel's classic dihybrid seed cross?",
    options: [
      "RRYY (Round Yellow) and rryy (Wrinkled Green)",
      "RrYy (Round Yellow) and RrYy (Round Yellow)",
      "RRyy (Round Green) and rrYY (Wrinkled Yellow)",
      "RRYy (Round Yellow) and rrYy (Wrinkled Yellow)"
    ],
    correctAnswer: "A",
    correctAnswers: [],
    solution: "The true-breeding parents have homozygous dominant genotype RRYY (Round Yellow) and homozygous recessive genotype rryy (Wrinkled Green).",
    explanation: "The true-breeding parents have homozygous dominant genotype RRYY (Round Yellow) and homozygous recessive genotype rryy (Wrinkled Green).",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  // 4. Ch 16 dihybrid F2 most frequent genotype
  await db.collection('questions').doc('MH-9-SCIT-16-16.4-OSC-077').update({
    text: "In the F2 generation of Mendel's dihybrid cross with 16 combinations, which genotype is the most frequent, appearing in 4 out of 16 squares (25%)?",
    options: [
      "RrYy (Heterozygous at both loci)",
      "RRYY (Homozygous dominant)",
      "rryy (Homozygous recessive)",
      "RRyy (Recombinant homozygous)"
    ],
    correctAnswer: "A",
    correctAnswers: [],
    solution: "The double heterozygous genotype RrYy is formed in 4 out of 16 combinations (25%), making it the most frequent genotype in the F2 generation.",
    explanation: "The double heterozygous genotype RrYy is formed in 4 out of 16 combinations (25%), making it the most frequent genotype in the F2 generation.",
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  });

  console.log('Successfully updated all 4 SCIT 9 questions!');
}

fixSCIT9Items().then(() => process.exit(0)).catch(console.error);
