import json

# Let's inspect chapters via node script that dumps to json or prints cleanly
const_script = """
const admin = require('firebase-admin');
require('./scripts/pre-mutation-snapshot.js');
const db = admin.firestore();

async function showAll() {
  const doc = await db.collection('syllabus').doc('mh_9_scit').get();
  const d = doc.data();
  const res = d.chapters.map(c => ({
    num: c.number,
    name: c.name,
    topics: c.topics.map(t => ({ num: t.number, code: t.topicCode, name: t.name }))
  }));
  console.log(JSON.stringify(res, null, 2));
}
showAll().catch(console.error);
"""
with open('scripts/dump_syllabus.js', 'w', encoding='utf-8') as f:
    f.write(const_script)
