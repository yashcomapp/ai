const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

async function analyzeVaults() {
  console.log('Fetching all questions from Firestore...');
  const snap = await db.collection('questions').get();
  console.log(`Total questions in DB: ${snap.size}`);

  // Count by parent topicCode: { exam: 0, practice: 0, foundation: 0, total: 0 }
  const topicStats = {};
  // Count by subtopicCode: { exam: 0, practice: 0, foundation: 0, total: 0 }
  const subtopicStats = {};

  snap.docs.forEach(doc => {
    const d = doc.data();
    const tCode = d.topicCode || d.parentTopicCode || 'unknown';
    const stCode = d.subtopicCode || d.topicNumber || tCode;
    const vault = d.vault || 'unknown';

    if (!topicStats[tCode]) topicStats[tCode] = { exam: 0, practice: 0, foundation: 0, total: 0, subject: d.subjectCode, class: d.class };
    topicStats[tCode][vault] = (topicStats[tCode][vault] || 0) + 1;
    topicStats[tCode].total++;

    if (!subtopicStats[stCode]) subtopicStats[stCode] = { exam: 0, practice: 0, foundation: 0, total: 0, parent: tCode };
    subtopicStats[stCode][vault] = (subtopicStats[stCode][vault] || 0) + 1;
    subtopicStats[stCode].total++;
  });

  console.log('\n======================================================');
  console.log('  PARENT TOPIC LEVEL ANALYSIS (e.g. MH-9-SCIT-1-1.1)');
  console.log('======================================================');
  const parentTopics = Object.entries(topicStats).filter(([k]) => k !== 'unknown');
  const parentWith20PlusPractice = parentTopics.filter(([, s]) => s.practice >= 20);
  const parentWithLessThan20Practice = parentTopics.filter(([, s]) => s.practice < 20);

  console.log(`Total populated parent topics: ${parentTopics.length}`);
  console.log(`Parent topics with >= 20 practice questions: ${parentWith20PlusPractice.length} (${((parentWith20PlusPractice.length / parentTopics.length) * 100).toFixed(1)}%)`);
  console.log(`Parent topics with < 20 practice questions: ${parentWithLessThan20Practice.length}`);
  if (parentWithLessThan20Practice.length > 0) {
    console.log('Parent topics with < 20 practice:');
    parentWithLessThan20Practice.forEach(([k, s]) => {
      console.log(`  * ${k}: Practice=${s.practice}, Exam=${s.exam}, Foundation=${s.foundation}, Total=${s.total}`);
    });
  }

  console.log('\n======================================================');
  console.log('  SUBTOPIC LEVEL ANALYSIS (e.g. MH-9-SCIT-1-1.1.1)');
  console.log('======================================================');
  const subtopics = Object.entries(subtopicStats).filter(([k]) => k !== 'unknown' && k.split('-').length >= 5 && k.split('-')[4].includes('.'));
  const subWith20Plus = subtopics.filter(([, s]) => s.practice >= 20);
  const subWithLessThan20 = subtopics.filter(([, s]) => s.practice < 20);

  console.log(`Total populated subtopics: ${subtopics.length}`);
  console.log(`Subtopics with >= 20 practice questions: ${subWith20Plus.length}`);
  console.log(`Subtopics with < 20 practice questions: ${subWithLessThan20.length}`);
}

analyzeVaults().catch(console.error);
