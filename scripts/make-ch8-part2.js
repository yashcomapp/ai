// scripts/make-ch8-part2.js
// Generates scripts/ch8_part2.js containing all 50 questions of MH-9-SCIT-8-8.1.2 (Q53 to Q102)
// with genuine 3-part gold standard pedagogical solutions.

const fs = require('fs');
const raw = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_8_raw.json', 'utf8')).slice(52, 102);

// We will construct the array of 50 enhanced questions with genuine 3-part gold standard solutions
