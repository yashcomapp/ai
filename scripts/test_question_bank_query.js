const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function testQbQueries() {
  const db = admin.firestore();

  // Test 1: Chapter 10
  console.log('--- Testing Question Bank API Query for Chapter 10 ---');
  let q10 = db.collection('questions')
    .where('board', '==', 'Maharashtra Board')
    .where('class', '==', '9')
    .where('subject', '==', 'Science and Technology');

  const snap10 = await q10.get();
  console.log(`Total base questions returned for MH Class 9 Science and Technology: ${snap10.size}`);

  const ch10Docs = snap10.docs
    .map(d => ({ id: d.id, ...d.data() }))
    .filter(q => {
      const qCh = String(q.chapterNumber || q.chapter || '').trim();
      return qCh === '10' || qCh.startsWith('Chapter 10') || qCh.startsWith('Ch.10');
    });

  console.log(`Matching Chapter 10 questions: ${ch10Docs.length}`);
  if (ch10Docs.length > 0) {
    console.log(`Sample Ch 10 question: ${ch10Docs[0].id} - ${ch10Docs[0].text?.slice(0, 60)}...`);
  }

  // Test 2: Chapter 16
  console.log('\n--- Testing Question Bank API Query for Chapter 16 ---');
  const ch16Docs = snap10.docs
    .map(d => ({ id: d.id, ...d.data() }))
    .filter(q => {
      const qCh = String(q.chapterNumber || q.chapter || '').trim();
      return qCh === '16' || qCh.startsWith('Chapter 16') || qCh.startsWith('Ch.16');
    });

  console.log(`Matching Chapter 16 questions: ${ch16Docs.length}`);
  if (ch16Docs.length > 0) {
    console.log(`Sample Ch 16 question: ${ch16Docs[0].id} - ${ch16Docs[0].text?.slice(0, 60)}...`);
  }

  // Test 3: Chapter 7 and 14
  const ch7Docs = snap10.docs.filter(q => String(q.data().chapterNumber).trim() === '7');
  const ch14Docs = snap10.docs.filter(q => String(q.data().chapterNumber).trim() === '14');
  console.log(`\nMatching Chapter 7 questions: ${ch7Docs.length}`);
  console.log(`Matching Chapter 14 questions: ${ch14Docs.length}`);
}

testQbQueries().catch(console.error);
