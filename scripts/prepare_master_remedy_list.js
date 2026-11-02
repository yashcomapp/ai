const fs = require('fs');

const rawList = JSON.parse(fs.readFileSync('scripts/scit9_out_of_syllabus_remedy_list.json', 'utf8'));

// Also add the 2 MH-10-SCIT2 questions
rawList.push(
  {
    id: 'MH-10-SCIT2-7-7.5.2-OSC-010',
    subject: 'SCIT2',
    class: '10',
    topicCode: 'MH-10-SCIT2-7-7.5.2',
    chapter: 7,
    type: 'OSC',
    text: 'Which organisms are primarily responsible for the methanogenesis phase inside an anaerobic sludge digester?'
  },
  {
    id: 'MH-10-SCIT2-7-7.5.2-OSC-019',
    subject: 'SCIT2',
    class: '10',
    topicCode: 'MH-10-SCIT2-7-7.5.2',
    chapter: 7,
    type: 'OSC',
    text: 'What is the primary role of methanogenic archaea in an anaerobic digester?'
  }
);

console.log(`Total questions in master remedy list: ${rawList.length}`);
fs.writeFileSync('scripts/master_out_of_syllabus_list.json', JSON.stringify(rawList, null, 2));
