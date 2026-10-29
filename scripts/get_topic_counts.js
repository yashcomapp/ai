const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function countTopics() {
  const doc = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = doc.data();
  const chapters = d.chapters || [];
  
  let majorTopicCount = 0;
  let subtopicCount = 0;
  const breakdown = [];

  chapters.forEach(ch => {
    const chNum = ch.number || ch.chapterNumber;
    const chName = ch.name || ch.chapterName;
    const topics = ch.topics || [];
    let chSubtopics = 0;

    topics.forEach(t => {
      majorTopicCount++;
      const subs = t.subtopics || [];
      chSubtopics += subs.length;
      subtopicCount += subs.length;
    });

    breakdown.push({
      chNum,
      chName,
      topicsCount: topics.length,
      subtopicsCount: chSubtopics
    });
  });

  console.log('=== MH-9-SCIT SYLLABUS TOPIC INVENTORY ===');
  console.log('Total Chapters:', chapters.length);
  console.log('Total Major Topics (Level 2, e.g. 1.1, 1.2):', majorTopicCount);
  console.log('Total Micro Subtopics (Level 3, e.g. 1.1.1, 1.1.2):', subtopicCount);
  console.log('\nChapter-wise Breakdown:');
  breakdown.forEach(b => {
    console.log('  Ch ' + String(b.chNum).padStart(2) + ': ' + b.chName.padEnd(45) + ' | ' + String(b.topicsCount).padStart(2) + ' Topics | ' + String(b.subtopicsCount).padStart(2) + ' Subtopics');
  });
}
countTopics().catch(console.error);
