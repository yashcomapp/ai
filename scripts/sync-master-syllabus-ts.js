const fs = require('fs');
const path = require('path');
const { MASTER_SYLLABUS_SUBJECTS } = require('./curriculum_data');

console.log(`Aggregated ${MASTER_SYLLABUS_SUBJECTS.length} subjects from curriculum_data modules.`);

let totalChapters = 0;
let totalTopics = 0;

MASTER_SYLLABUS_SUBJECTS.forEach(subj => {
  totalChapters += subj.chapters.length;
  subj.chapters.forEach(ch => {
    totalTopics += ch.topics.length;
  });
});

console.log(`Summary: ${MASTER_SYLLABUS_SUBJECTS.length} Subjects | ${totalChapters} Chapters | ${totalTopics} Atomic Topics.`);

const tsHeader = `/**
 * Master Syllabus Data SSOT (Official NCERT & Balbharti Curricula)
 * Contains the complete 16 baseline subjects with canonical deep atomic topic codes,
 * subtopics micro-concepts, practice sets, problem sets, and named theorems.
 */

export interface MasterTopic {
  number: string;
  name: string;
  topicCode: string;
  subtopics?: string[];
  practiceSet?: string;
  theorems?: string[];
  problemSet?: string;
}

export interface MasterChapter {
  number: string;
  name: string;
  topics: MasterTopic[];
}

export interface MasterSyllabusSubject {
  docId: string;
  board: 'CBSE' | 'Maharashtra Board';
  boardCode: 'CBSE' | 'MH';
  class: string;
  subject: string;
  subjectCode: string;
  chapters: MasterChapter[];
}

export const MASTER_SYLLABUS_SUBJECTS: MasterSyllabusSubject[] = `;

const tsContent = tsHeader + JSON.stringify(MASTER_SYLLABUS_SUBJECTS, null, 2) + ';\n';

const targetPath = path.join(__dirname, '..', 'src', 'lib', 'masterSyllabusData.ts');
fs.writeFileSync(targetPath, tsContent, 'utf8');

console.log(`✓ Successfully updated ${targetPath}`);
