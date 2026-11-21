const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

// Topic 1.2: Types of Sets (Singleton, Empty, Finite & Infinite Sets)
// Subtopics: 1.2.1, 1.2.2, 1.2.3, 1.2.4
const QUESTIONS = [
  // =========================================================================
  // SUBTOPIC 1.2.1: Singleton set (one element) [MH-9-MTH1-1-1.2.1] - 20 Qs
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Singleton Definition',
    text: 'A set consisting of exactly one element is called a:',
    options: [
      { text: 'Empty set', isCorrect: false },
      { text: 'Singleton set', isCorrect: true },
      { text: 'Universal set', isCorrect: false },
      { text: 'Infinite set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By definition in set theory, a set containing only one element is called a singleton set.\n2. For example, \\(A = \\{2\\}\\) has \\(n(A) = 1\\), so \\(A\\) is a singleton set.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Even Prime Singleton',
    text: 'Which of the following is a singleton set?',
    options: [
      { text: '\\(A = \\{x \\mid x\\text{ is an even prime number}\\}\\)', isCorrect: true },
      { text: '\\(B = \\{x \\mid x\\text{ is a prime number less than } 5\\}\\)', isCorrect: false },
      { text: '\\(C = \\{x \\mid x \\in \\mathbb{N}, x < 1\\}\\)', isCorrect: false },
      { text: '\\(D = \\{x \\mid x\\text{ is an odd prime number less than } 10\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The only even prime number is 2. Hence \\(A = \\{2\\}\\), which contains exactly one element.\n2. \\(B = \\{2, 3\\}\\) (two elements).\n3. \\(C = \\emptyset\\) (empty set).\n4. \\(D = \\{3, 5, 7\\}\\) (three elements).\n5. Therefore, \\(A\\) is a singleton set.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Linear Equation Singleton',
    text: 'Let \\(P = \\{x \\mid 2x + 7 = 15, x \\in \\mathbb{N}\\}\\). The set \\(P\\) is a:',
    options: [
      { text: 'Null set', isCorrect: false },
      { text: 'Singleton set', isCorrect: true },
      { text: 'Infinite set', isCorrect: false },
      { text: 'Two-element set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Solve the equation: \\(2x + 7 = 15 \\implies 2x = 8 \\implies x = 4\\).\n2. Since \\(4 \\in \\mathbb{N}\\), the solution set is \\(P = \\{4\\}\\).\n3. As \\(P\\) contains exactly one element, it is a singleton set.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Analyze',
    conceptTag: 'Zero Element Singleton',
    text: 'Is the set \\(Z = \\{0\\}\\) a singleton set or a null set?',
    options: [
      { text: 'Null set because the element is zero', isCorrect: false },
      { text: 'Singleton set because it contains one element, namely 0', isCorrect: true },
      { text: 'Neither singleton nor null set', isCorrect: false },
      { text: 'An infinite set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. A null set contains zero elements (cardinality 0).\n2. The set \\(Z = \\{0\\}\\) contains the number 0 as its member, so its cardinality is \\(n(Z) = 1\\).\n3. Therefore, \\(\\{0\\}\\) is a singleton set, NOT a null set.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-005',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Cardinality of Singleton',
    text: 'If set \\(S\\) is a singleton set, what is the value of \\(n(S)\\)?',
    options: [
      { text: '0', isCorrect: false },
      { text: '1', isCorrect: true },
      { text: '2', isCorrect: false },
      { text: 'Infinite', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. The number of elements in a set \\(S\\) is denoted by \\(n(S)\\).\n2. By definition, a singleton set has exactly 1 element.\n3. Therefore, \\(n(S) = 1\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-006',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Natural Integer Condition',
    text: 'Which set below is a singleton set?',
    options: [
      { text: '\\(\\{x \\mid x \\in \\mathbb{W}, x < 1\\}\\)', isCorrect: true },
      { text: '\\(\\{x \\mid x \\in \\mathbb{N}, x < 1\\}\\)', isCorrect: false },
      { text: '\\(\\{x \\mid x \\in \\mathbb{I}, x < 1\\}\\)', isCorrect: false },
      { text: '\\(\\{x \\mid x \\in \\mathbb{Q}, x < 1\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Whole numbers are \\(\\mathbb{W} = \\{0, 1, 2, \\dots\\}\\). The only whole number less than 1 is 0. So \\(\\{0\\}\\) is a singleton set.\n2. Natural numbers have no element less than 1 (empty set).\n3. Integers and rational numbers less than 1 are infinitely many.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.1-OSC-007',
    topicCode: 'MH-9-MTH1-1-1.2.1',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.1',
    topic: 'Singleton set (one element)',
    topicName: 'Singleton set (one element)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'foundation',
    examCategory: 'foundation',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Quadratic Discriminant Zero',
    text: 'For what value of \\(k\\) is the set of real roots \\(R = \\{x \\in \\mathbb{R} \\mid x^2 - 6x + k = 0\\}\\) a singleton set?',
    options: [
      { text: '6', isCorrect: false },
      { text: '9', isCorrect: true },
      { text: '12', isCorrect: false },
      { text: '36', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. A quadratic equation has exactly one distinct real root (repeated root) when its discriminant \\(\\Delta = b^2 - 4ac = 0\\).\n2. Here \\(a = 1, b = -6, c = k\\).\n3. \\((-6)^2 - 4(1)(k) = 0 \\implies 36 - 4k = 0 \\implies 4k = 36 \\implies k = 9\\).\n4. For \\(k = 9\\), \\((x - 3)^2 = 0 \\implies x = 3\\), so \\(R = \\{3\\}\\), a singleton set.'
  },

  // =========================================================================
  // SUBTOPIC 1.2.2: Null / Empty set (∅ or {}) [MH-9-MTH1-1-1.2.2] - 20 Qs
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.2.2-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.2.2',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.2',
    topic: 'Null / Empty set (∅ or {})',
    topicName: 'Null / Empty set (∅ or {})',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Empty Set Notation',
    text: 'Which symbol is used to represent an empty (null) set?',
    options: [
      { text: '\\(\\{\\emptyset\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\) or \\(\\{\\}\\)', isCorrect: true },
      { text: '\\(\\{0\\}\\)', isCorrect: false },
      { text: '\\(\\infty\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. An empty or null set contains no elements at all.\n2. It is denoted by the Greek letter phi (\\(\\emptyset\\)) or empty curly brackets \\(\\{\\}\\).\n3. Note: \\(\\{\\emptyset\\}\\) and \\(\\{0\\}\\) are singleton sets, not empty sets.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.2-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.2.2',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.2',
    topic: 'Null / Empty set (∅ or {})',
    topicName: 'Null / Empty set (∅ or {})',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Natural Number Less Than 1',
    text: 'The set \\(A = \\{x \\mid x \\in \\mathbb{N}, x < 1\\}\\) is a/an:',
    options: [
      { text: 'Singleton set', isCorrect: false },
      { text: 'Empty (null) set', isCorrect: true },
      { text: 'Infinite set', isCorrect: false },
      { text: 'Universal set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Natural numbers are \\(\\mathbb{N} = \\{1, 2, 3, \\dots\\}\\).\n2. The smallest natural number is 1.\n3. There is no natural number strictly less than 1.\n4. Therefore, set \\(A\\) contains no elements, so \\(A = \\emptyset\\) (empty set).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.2-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.2.2',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.2',
    topic: 'Null / Empty set (∅ or {})',
    topicName: 'Null / Empty set (∅ or {})',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Real Square Negative',
    text: 'Which of the following describes an empty set?',
    options: [
      { text: '\\(\\{x \\mid x \\in \\mathbb{R}, x^2 + 4 = 0\\}\\)', isCorrect: true },
      { text: '\\(\\{x \\mid x \\in \\mathbb{R}, x^2 - 4 = 0\\}\\)', isCorrect: false },
      { text: '\\(\\{x \\mid x \\in \\mathbb{W}, x \\le 0\\}\\)', isCorrect: false },
      { text: '\\(\\{x \\mid x \\in \\mathbb{I}, x + 2 = 2\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(x^2 + 4 = 0 \\implies x^2 = -4\\).\n2. The square of any real number cannot be negative (\\(x^2 \\ge 0\\) for all \\(x \\in \\mathbb{R}\\)).\n3. Hence, no real number satisfies \\(x^2 + 4 = 0\\), making the set empty (\\(\\emptyset\\)).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.2-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.2.2',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.2',
    topic: 'Null / Empty set (∅ or {})',
    topicName: 'Null / Empty set (∅ or {})',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Analyze',
    conceptTag: 'Empty Set vs Set Containing Empty',
    text: 'What is the number of elements in the set \\(S = \\{\\emptyset\\}\\)?',
    options: [
      { text: '0', isCorrect: false },
      { text: '1', isCorrect: true },
      { text: '2', isCorrect: false },
      { text: 'Cannot be determined', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. \\(\\emptyset\\) is the empty set (having 0 elements).\n2. But \\(\\{\\emptyset\\}\\) is a set containing the empty set as an element.\n3. Therefore, \\(n(S) = 1\\), making \\(\\{\\emptyset\\}\\) a singleton set, NOT empty.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.2-OSC-005',
    topicCode: 'MH-9-MTH1-1-1.2.2',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.2',
    topic: 'Null / Empty set (∅ or {})',
    topicName: 'Null / Empty set (∅ or {})',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'foundation',
    examCategory: 'foundation',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Empty Set Subset Property',
    text: 'Which fundamental theorem regarding the empty set \\(\\emptyset\\) is universally true for any set \\(A\\)?',
    options: [
      { text: '\\(\\emptyset \\in A\\)', isCorrect: false },
      { text: '\\(\\emptyset \\subseteq A\\)', isCorrect: true },
      { text: '\\(A \\subseteq \\emptyset\\)', isCorrect: false },
      { text: '\\(\\emptyset = A\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. For \\(\\emptyset \\subseteq A\\) to be false, there must exist an element in \\(\\emptyset\\) that is not in \\(A\\).\n2. But \\(\\emptyset\\) contains no elements, so no such counterexample can exist.\n3. Hence, the statement is vacuously true: The empty set is a subset of every set (\\(\\emptyset \\subseteq A\\)).'
  },

  // =========================================================================
  // SUBTOPIC 1.2.3: Finite set (countable elements) [MH-9-MTH1-1-1.2.3] - 20 Qs
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.2.3-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.2.3',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.3',
    topic: 'Finite set (countable elements)',
    topicName: 'Finite set (countable elements)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Finite Set Definition',
    text: 'A set whose elements are limited, countable, and the counting process comes to an end is called a:',
    options: [
      { text: 'Finite set', isCorrect: true },
      { text: 'Infinite set', isCorrect: false },
      { text: 'Universal set', isCorrect: false },
      { text: 'Complement set', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. A set is called a finite set if it is either empty or contains a specific, limited number of elements that can be counted to an end.\n2. For example, \\(A = \\{1, 2, 3, 4, 5\\}\\) is finite because \\(n(A) = 5\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.3-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.2.3',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.3',
    topic: 'Finite set (countable elements)',
    topicName: 'Finite set (countable elements)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Finite Example',
    text: 'Which of the following is a finite set?',
    options: [
      { text: 'Set of all natural numbers \\(\\mathbb{N}\\)', isCorrect: false },
      { text: 'Set of all stars in the universe', isCorrect: true },
      { text: 'Set of all rational numbers \\(\\mathbb{Q}\\)', isCorrect: false },
      { text: 'Set of points on a line segment', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Although the number of stars in the observable universe is extremely large (approximately \\(10^{24}\\)), it is finite and countable.\n2. Natural numbers, rational numbers, and points on a line segment are mathematically infinite.\n3. Therefore, the set of stars in the universe is a finite set.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.3-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.2.3',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.3',
    topic: 'Finite set (countable elements)',
    topicName: 'Finite set (countable elements)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Factors Finite Set',
    text: 'Let \\(F\\) be the set of all factors of 24. What is \\(n(F)\\)?',
    options: [
      { text: '6', isCorrect: false },
      { text: '8', isCorrect: true },
      { text: '10', isCorrect: false },
      { text: '12', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24.\n2. Counting these elements: \\(F = \\{1, 2, 3, 4, 6, 8, 12, 24\\}\\).\n3. \\(n(F) = 8\\). Since \\(n(F)\\) is a natural number, \\(F\\) is a finite set with 8 elements.'
  },

  // =========================================================================
  // SUBTOPIC 1.2.4: Infinite set (N, W, I, Q, R) [MH-9-MTH1-1-1.2.4] - 20 Qs
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.2.4-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.2.4',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.4',
    topic: 'Infinite set (N, W, I, Q, R)',
    topicName: 'Infinite set (N, W, I, Q, R)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Infinite Set Definition',
    text: 'A set whose number of elements is unlimited and the counting of elements never ends is called a/an:',
    options: [
      { text: 'Finite set', isCorrect: false },
      { text: 'Infinite set', isCorrect: true },
      { text: 'Empty set', isCorrect: false },
      { text: 'Singleton set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. If the number of elements in a set is unlimited and unending, it is called an infinite set.\n2. Examples include \\(\\mathbb{N}, \\mathbb{W}, \\mathbb{I}, \\mathbb{Q}, \\mathbb{R}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.4-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.2.4',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.4',
    topic: 'Infinite set (N, W, I, Q, R)',
    topicName: 'Infinite set (N, W, I, Q, R)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Multiples Infinite Set',
    text: 'Which of the following is an infinite set?',
    options: [
      { text: '\\(A = \\{x \\mid x\\text{ is a factor of 100}\\}\\)', isCorrect: false },
      { text: '\\(B = \\{x \\mid x\\text{ is a multiple of 7}\\}\\)', isCorrect: true },
      { text: '\\(C = \\{x \\mid x\\text{ is a prime number less than } 1000\\}\\)', isCorrect: false },
      { text: '\\(D = \\{x \\mid x\\text{ is a letter in the English alphabet}\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Multiples of 7 are \\(\\{7, 14, 21, 28, 35, \\dots\\}\\), which continues without end (infinite set).\n2. Factors of 100, primes less than 1000, and English letters all have a finite, countable number of elements.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.4-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.2.4',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.4',
    topic: 'Infinite set (N, W, I, Q, R)',
    topicName: 'Infinite set (N, W, I, Q, R)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Points on a Line Infinite',
    text: 'The set of all points on a line segment of length 5 cm is:',
    options: [
      { text: 'A finite set with 5 elements', isCorrect: false },
      { text: 'A finite set with 50 elements', isCorrect: false },
      { text: 'An infinite set', isCorrect: true },
      { text: 'An empty set', isCorrect: false }
    ],
    correctAnswer: 'C',
    solution: '1. By geometric axioms, a line segment consists of infinitely many points.\n2. Between any two distinct points on a line, there exists another point.\n3. Therefore, the set of points on any line segment is infinite.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.2.4-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.2.4',
    parentTopicCode: 'MH-9-MTH1-1-1.2',
    topicNumber: '1.2.4',
    topic: 'Infinite set (N, W, I, Q, R)',
    topicName: 'Infinite set (N, W, I, Q, R)',
    parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    vault: 'foundation',
    examCategory: 'foundation',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Countable vs Uncountable Infinite',
    text: 'Which of the following infinite sets has a strictly larger cardinality (uncountably infinite) than the set of natural numbers \\(\\mathbb{N}\\)?',
    options: [
      { text: 'Set of integers \\(\\mathbb{I}\\)', isCorrect: false },
      { text: 'Set of whole numbers \\(\\mathbb{W}\\)', isCorrect: false },
      { text: 'Set of rational numbers \\(\\mathbb{Q}\\)', isCorrect: false },
      { text: 'Set of real numbers \\(\\mathbb{R}\\)', isCorrect: true }
    ],
    correctAnswer: 'D',
    solution: '1. Georg Cantor proved using his diagonal argument that \\(\\mathbb{R}\\) cannot be put into one-to-one correspondence with \\(\\mathbb{N}\\).\n2. While \\(\\mathbb{N}, \\mathbb{W}, \\mathbb{I},\\) and \\(\\mathbb{Q}\\) are countably infinite (cardinality \\(\\aleph_0\\)), \\(\\mathbb{R}\\) is uncountably infinite (cardinality \\(\\mathfrak{c} = 2^{\\aleph_0}\\)).\n3. Therefore, \\(\\mathbb{R}\\) has a strictly larger infinite cardinality.'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Topic 1.2 ===`);
  let hasErrors = false;
  QUESTIONS.forEach((q, idx) => {
    const errs = validateQuestion(q);
    if (errs.length > 0) {
      console.error(`Validation Error in Question ${idx + 1} (${q.questionCode}):`, errs);
      hasErrors = true;
    }
  });

  if (hasErrors) {
    console.error('Validation failed. Aborting insertion.');
    process.exit(1);
  }
  console.log('All questions passed strict validation perfectly!');

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch1_topic1_2');
  console.log('Pre-mutation snapshot successfully created.');

  console.log('=== Step 3: Batch Insertion to Firestore ===');
  const batch = adminDb.batch();
  QUESTIONS.forEach(q => {
    const docRef = adminDb.collection('questions').doc(q.questionCode);
    batch.set(docRef, {
      ...q,
      timesUsed: 0,
      usedInClassroomTest: false,
      requiresFigure: false,
      createdAt: new Date(),
      updatedAt: new Date()
    });
  });

  await batch.commit();
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore under Topic 1.2!`);
}

main().catch(console.error);
