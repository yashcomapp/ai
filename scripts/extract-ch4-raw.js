// scripts/extract-ch4-raw.js - Extract Chapter 4 (Measurement of Matter) raw questions
require('./pre-mutation-snapshot.js');
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

async function extract() {
  const db = admin.firestore();
  console.log('Fetching Chapter 4 questions from Firestore...');
  
  const snap = await db.collection('questions')
    .where('boardCode', '==', 'MH')
    .where('class', '==', '9')
    .where('subjectCode', '==', 'SCIT')
    .where('chapterNumber', '==', '4')
    .get();

  console.log(`Found ${snap.size} questions for Chapter 4.`);

  const questions = [];
  snap.forEach(doc => {
    questions.push({
      id: doc.id,
      ...doc.data()
    });
  });

  // Sort questions naturally by questionCode
  questions.sort((a, b) => (a.questionCode || a.id).localeCompare(b.questionCode || b.id));

  const outDir = path.resolve('backups/staging');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const outFile = path.join(outDir, 'mh9_scit_4_raw.json');
  fs.writeFileSync(outFile, JSON.stringify(questions, null, 2), 'utf8');
  console.log(`Raw questions saved to ${outFile}`);

  // Topic breakdown
  const topicBreakdown = {};
  questions.forEach(q => {
    const t = q.topicCode || 'unknown';
    topicBreakdown[t] = (topicBreakdown[t] || 0) + 1;
  });
  console.log('Topic Breakdown:', topicBreakdown);

  // Quick flaw scan
  let noneOfAboveCount = 0;
  let missingSolutionCount = 0;
  let dashesCount = 0;
  let alreadyEnhancedCount = 0;

  questions.forEach(q => {
    if (q.isEnhanced) alreadyEnhancedCount++;
    if (!q.solution || q.solution.trim().length === 0) missingSolutionCount++;
    if (/---/.test(q.text)) dashesCount++;
    if (q.options && q.options.some(opt => /none of/i.test(opt))) noneOfAboveCount++;
  });

  console.log('\n--- Initial Flaw Audit ---');
  console.log(`Already Enhanced: ${alreadyEnhancedCount} / ${questions.length}`);
  console.log(`Missing Solutions: ${missingSolutionCount} / ${questions.length}`);
  console.log(`'None of above' in options: ${noneOfAboveCount} questions`);
  console.log(`Fill-in dashes '---': ${dashesCount} questions`);
}

extract()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Error extracting Chapter 4:', err);
    process.exit(1);
  });
