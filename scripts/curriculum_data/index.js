const { cbse8Subjects } = require('./cbse_8');
const { mh8Subjects } = require('./mh_8');
const { cbse9Subjects } = require('./cbse_9');
const { mh9Subjects } = require('./mh_9');
const { cbse10Subjects } = require('./cbse_10');
const { mh10Subjects } = require('./mh_10');

const MASTER_SYLLABUS_SUBJECTS = [
  ...cbse8Subjects,
  ...mh8Subjects,
  ...cbse9Subjects,
  ...mh9Subjects,
  ...cbse10Subjects,
  ...mh10Subjects
];

module.exports = { MASTER_SYLLABUS_SUBJECTS };
