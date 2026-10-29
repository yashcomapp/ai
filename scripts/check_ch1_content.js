const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

async function checkCh1Questions() {
  const snap = await db.collection('questions')
    .where('class', 'in', ['9', 9])
    .where('subjectCode', '==', 'SCIT')
    .where('chapterNumber', 'in', ['1', 1])
    .select('questionCode', 'text', 'topicCode')
    .get();

  console.log(`Chapter 1 has ${snap.size} questions.`);
  let countAccel = 0;
  let countGraph = 0;
  let countNewton = 0;
  let countCircular = 0;
  let countKinematic = 0;
  let countDistance = 0;

  snap.forEach(d => {
    const text = (d.data().text || '').toLowerCase();
    if (text.includes('newton') || text.includes('momentum') || text.includes('inertia') || text.includes('recoil')) {
      countNewton++;
    } else if (text.includes('acceleration') || text.includes('retardation') || text.includes('deceleration')) {
      countAccel++;
    } else if (text.includes('graph') || text.includes('slope') || text.includes('area under')) {
      countGraph++;
    } else if (text.includes('v = u') || text.includes('v²') || text.includes('kinematic') || text.includes('equation of motion')) {
      countKinematic++;
    } else if (text.includes('circular') || text.includes('centripetal')) {
      countCircular++;
    } else {
      countDistance++;
    }
  });

  console.log('Content Breakdown of Chapter 1 Questions:');
  console.log('  Newton Laws / Momentum / Inertia:', countNewton);
  console.log('  Acceleration / Deceleration:', countAccel);
  console.log('  Graphs (Distance-time / Velocity-time):', countGraph);
  console.log('  Equations of Motion:', countKinematic);
  console.log('  Circular Motion / Centripetal:', countCircular);
  console.log('  Distance / Displacement / Speed / Velocity:', countDistance);
}

checkCh1Questions().catch(console.error);
