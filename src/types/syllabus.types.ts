/**
 * Canonical Syllabus Type Definitions (SSOT).
 */

export interface Subtopic {
  number: string;
  name: string;
  subtopicCode?: string;
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  targetQuestions?: number;
  topicClassification?: 'minor' | 'medium' | 'major' | string;
  [key: string]: any;
}

export interface Topic {
  number: string;
  name: string;
  topicNumber?: string;
  topic?: string;
  topicCode?: string;
  subject?: string;
  subtopics?: Subtopic[];
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  textbookSets?: any[];
  targetQuestions?: number;
  [key: string]: any;
}

export interface Chapter {
  number: string | number;
  name: string;
  chapterNumber?: string | number;
  chapterName?: string;
  chapterCode?: string;
  topics?: Topic[];
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  chapterExercises?: any[];
  [key: string]: any;
}

export interface SyllabusSubject {
  id: string;
  board: string;
  class: string | number;
  subject: string;
  subjectCode: string;
  chapters?: Chapter[];
  [key: string]: any;
}
