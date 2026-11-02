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

async function auditAllSCITChapters() {
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', 'in', ['9', 9])
    .get();

  console.log(`Auditing all ${snap.size} questions in Class 9 Science (MH-9-SCIT)...`);

  const chaptersTheory = {
    6: 'Classification of Plants',
    7: 'Energy Flow in an Ecosystem',
    8: 'Useful and Harmful Microbes',
    9: 'Environmental Management',
    15: 'Life Processes in Living Organisms',
    16: 'Heredity and Variation',
    17: 'Introduction to Biotechnology',
    18: 'Observing Space: Telescopes'
  };

  const absurdTheoryNumericals = [];
  const advancedKeywords = [
    'differential equation', 'hamiltonian', 'schrodinger', 'lorentz', 'relativistic',
    'phytoremediation', 'fluidized bed', 'hyperaccumulating', 'electrostatic precipitator',
    'anaerobic digestion', 'hydrolytic fermentative', 'methanogen', 'landfill gas',
    'psychrometric', 'vapor pressure', 'lapse rate', 'anemometer', 'hpa',
    'supercomputing', 'numerical weather', 'somatostatin', 'topoisomerase',
    'gibbs free energy', 'crystal field', 'palindromic restriction'
  ];
  const absurdAdvancedQuestions = [];

  snap.forEach(d => {
    const q = d.data();
    const ch = Number(q.chapterNumber);
    const type = q.type || '';
    const text = (q.text || '') + ' ' + (q.solution || '') + ' ' + (q.explanation || '');
    const lower = text.toLowerCase();
    const isUsed = q.used || q.usageCount > 0 || q.timesUsed > 0;

    // Check theory chapters having ONE questions
    if (chaptersTheory[ch] && type === 'ONE') {
      absurdTheoryNumericals.push({
        id: d.id,
        chapter: ch,
        chapterName: chaptersTheory[ch],
        topicCode: q.topicCode,
        text: q.text,
        sol: q.solution || q.explanation,
        isUsed
      });
    }

    // Check advanced keywords
    const matched = advancedKeywords.filter(k => lower.includes(k));
    if (matched.length > 0) {
      absurdAdvancedQuestions.push({
        id: d.id,
        chapter: ch,
        topicCode: q.topicCode,
        text: q.text,
        sol: q.solution || q.explanation,
        matched,
        isUsed
      });
    }
  });

  console.log(`\nFound ${absurdTheoryNumericals.length} numerical (ONE) questions in pure theory/biology/environmental chapters!`);
  console.log(`Found ${absurdAdvancedQuestions.length} questions matching college/engineering keywords!`);

  console.log('\n--- Sample Absurd Theory Numericals ---');
  absurdTheoryNumericals.slice(0, 15).forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} (Ch ${q.chapter}: ${q.chapterName}) | Used: ${q.isUsed}`);
    console.log(`  Q: ${q.text}`);
    console.log(`  Sol: ${q.sol}`);
    console.log('---');
  });

  console.log('\n--- Sample Absurd Advanced Questions ---');
  absurdAdvancedQuestions.slice(0, 15).forEach((q, i) => {
    console.log(`[${i+1}] ${q.id} (Ch ${q.chapter}, Keywords: ${q.matched.join(', ')}) | Used: ${q.isUsed}`);
    console.log(`  Q: ${q.text.slice(0, 120)}...`);
    console.log('---');
  });
}

auditAllSCITChapters().then(() => process.exit(0)).catch(console.error);
