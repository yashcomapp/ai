const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function checkQuestionTopicCodes() {
  const snap = await db.collection('questions')
    .where('class', 'in', ['9', 9])
    .where('subjectCode', '==', 'SCIT')
    .select('chapterNumber', 'topicCode')
    .get();

  const chTopics = {};
  snap.forEach(d => {
    const data = d.data();
    const ch = parseInt(data.chapterNumber, 10);
    const tc = data.topicCode || 'NO_TOPIC';
    if (!chTopics[ch]) chTopics[ch] = {};
    chTopics[ch][tc] = (chTopics[ch][tc] || 0) + 1;
  });

  const chs = Object.keys(chTopics).map(Number).sort((a,b) => a - b);
  for (const ch of chs) {
    console.log(`\n=== Chapter ${ch} ===`);
    for (const [tc, cnt] of Object.entries(chTopics[ch])) {
      console.log(`  ${tc.padEnd(25)} : ${cnt} Qs`);
    }
  }
}

checkQuestionTopicCodes().catch(console.error);
