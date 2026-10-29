const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');

async function testQuery() {
  const db = admin.firestore();

  // Test what subjects exist in config/syllabusSubjects
  const sylSubSnap = await db.collection('config').doc('syllabusSubjects').get();
  if (sylSubSnap.exists) {
    console.log('syllabusSubjects keys for MH Class 9:');
    const data = sylSubSnap.data();
    console.log(Object.keys(data?.subjects?.['Maharashtra Board']?.['9'] || {}));
    console.log(Object.keys(data?.subjects?.['MH']?.['9'] || {}));
  }

  // Check what 'board' and 'subject' fields are in the questions collection for Ch 1 vs Ch 10 vs Ch 16
  const ch1Sample = await db.collection('questions').doc('MH-9-SCIT-1-1.1-OSC-001').get();
  console.log('\nCh 1 doc:');
  console.log({
    board: ch1Sample.data().board,
    boardCode: ch1Sample.data().boardCode,
    subject: ch1Sample.data().subject,
    subjectCode: ch1Sample.data().subjectCode,
    chapterNumber: ch1Sample.data().chapterNumber
  });

  const ch10Sample = await db.collection('questions').doc('MH-9-SCIT-10-10.1-OSC-001').get();
  console.log('\nCh 10 doc:');
  console.log({
    board: ch10Sample.data()?.board,
    boardCode: ch10Sample.data()?.boardCode,
    subject: ch10Sample.data()?.subject,
    subjectCode: ch10Sample.data()?.subjectCode,
    chapterNumber: ch10Sample.data()?.chapterNumber
  });

  const ch16Sample = await db.collection('questions').doc('MH-9-SCIT-16-16.1-OSC-001').get();
  console.log('\nCh 16 doc:');
  console.log({
    board: ch16Sample.data()?.board,
    boardCode: ch16Sample.data()?.boardCode,
    subject: ch16Sample.data()?.subject,
    subjectCode: ch16Sample.data()?.subjectCode,
    chapterNumber: ch16Sample.data()?.chapterNumber
  });
}

testQuery().catch(console.error);
