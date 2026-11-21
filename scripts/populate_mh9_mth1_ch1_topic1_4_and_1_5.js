const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const QUESTIONS = [
  // =========================================================================
  // SUBTOPIC 1.4.1: John Venn diagram representations [MH-9-MTH1-1-1.4.1]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.4.1-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.4.1',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.1',
    topic: 'John Venn diagram representations',
    topicName: 'John Venn diagram representations',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Venn Origin',
    text: 'Who was the first logician and mathematician to use closed geometric figures to represent sets?',
    options: [
      { text: 'René Descartes', isCorrect: false },
      { text: 'John Venn', isCorrect: true },
      { text: 'Isaac Newton', isCorrect: false },
      { text: 'Euclid', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. The English logician John Venn (1834–1923) first introduced closed geometric figures to represent relationships between sets.\n2. Hence, these graphical representations are called "Venn Diagrams".'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.1-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.4.1',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.1',
    topic: 'John Venn diagram representations',
    topicName: 'John Venn diagram representations',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Universal Set Shape',
    text: 'In standard Venn diagrams, which geometric shape is conventionally used to represent the Universal set \\(U\\)?',
    options: [
      { text: 'Circle', isCorrect: false },
      { text: 'Rectangle', isCorrect: true },
      { text: 'Triangle', isCorrect: false },
      { text: 'Parallelogram', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. In standard Venn diagrams, a rectangle represents the Universal set \\(U\\).\n2. Subsets of \\(U\\) are drawn as circles, ovals, or closed curves inside the rectangle.'
  },

  // =========================================================================
  // SUBTOPIC 1.4.2: Intersection of sets (A ∩ B) [MH-9-MTH1-1-1.4.2]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.4.2-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.4.2',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.2',
    topic: 'Intersection of sets (A ∩ B)',
    topicName: 'Intersection of sets (A ∩ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Intersection Definition',
    text: 'The intersection of two sets \\(A\\) and \\(B\\), denoted \\(A \\cap B\\), is defined as:',
    options: [
      { text: 'The set of all elements in \\(A\\) or in \\(B\\)', isCorrect: false },
      { text: 'The set of all elements that are common to both \\(A\\) and \\(B\\)', isCorrect: true },
      { text: 'The set of elements belonging only to \\(A\\)', isCorrect: false },
      { text: 'The product of elements of \\(A\\) and \\(B\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By definition: \\(A \\cap B = \\{x \\mid x \\in A\\text{ and } x \\in B\\}\\).\n2. It contains all elements common to both sets.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.2-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.4.2',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.2',
    topic: 'Intersection of sets (A ∩ B)',
    topicName: 'Intersection of sets (A ∩ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Intersection Calculation',
    text: 'If \\(A = \\{1, 3, 5, 7\\}\\) and \\(B = \\{2, 3, 6, 7\\}\\), what is \\(A \\cap B\\)?',
    options: [
      { text: '\\(\\{1, 2, 3, 5, 6, 7\\}\\)', isCorrect: false },
      { text: '\\(\\{3, 7\\}\\)', isCorrect: true },
      { text: '\\(\\{1, 5\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Compare elements of \\(A\\) and \\(B\\):\n   - Elements in \\(A\\): 1, 3, 5, 7\n   - Elements in \\(B\\): 2, 3, 6, 7\n2. Common elements are 3 and 7.\n3. Therefore, \\(A \\cap B = \\{3, 7\\}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.2-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.4.2',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.2',
    topic: 'Intersection of sets (A ∩ B)',
    topicName: 'Intersection of sets (A ∩ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    bloomLevel: 'Understand',
    conceptTag: 'Intersection with Empty Set',
    text: 'For any set \\(A\\), what is \\(A \\cap \\emptyset\\)?',
    options: [
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: true },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\{0\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. \\(\\emptyset\\) has no elements.\n2. Since there are no elements in \\(\\emptyset\\), there can be no common elements between \\(A\\) and \\(\\emptyset\\).\n3. Therefore, \\(A \\cap \\emptyset = \\emptyset\\).'
  },

  // =========================================================================
  // SUBTOPIC 1.4.3: Disjoint sets [MH-9-MTH1-1-1.4.3]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.4.3-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.4.3',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.3',
    topic: 'Disjoint sets',
    topicName: 'Disjoint sets',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Disjoint Definition',
    text: 'Two sets \\(A\\) and \\(B\\) are said to be disjoint sets if:',
    options: [
      { text: '\\(A \\subseteq B\\)', isCorrect: false },
      { text: '\\(A \\cap B = \\emptyset\\)', isCorrect: true },
      { text: '\\(A \\cup B = U\\)', isCorrect: false },
      { text: '\\(n(A) = n(B)\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Two sets are disjoint if they have no common elements at all.\n2. In set notation: \\(A \\cap B = \\emptyset\\).\n3. In a Venn diagram, their circles do not overlap.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.3-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.4.3',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.3',
    topic: 'Disjoint sets',
    topicName: 'Disjoint sets',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Odd Even Disjoint',
    text: 'Let \\(E\\) be the set of even natural numbers and \\(O\\) be the set of odd natural numbers. What is \\(E \\cap O\\)?',
    options: [
      { text: '\\(\\{0\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\) (They are disjoint sets)', isCorrect: true },
      { text: '\\(\\mathbb{N}\\)', isCorrect: false },
      { text: '\\(\\{1, 2\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. An integer cannot be simultaneously both even and odd.\n2. No number belongs to both \\(E\\) and \\(O\\).\n3. Thus, \\(E \\cap O = \\emptyset\\), proving that even and odd numbers are disjoint sets.'
  },

  // =========================================================================
  // SUBTOPIC 1.4.4: Union of sets (A ∪ B) [MH-9-MTH1-1-1.4.4]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.4.4-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.4.4',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.4',
    topic: 'Union of sets (A ∪ B)',
    topicName: 'Union of sets (A ∪ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Union Definition',
    text: 'The union of two sets \\(A\\) and \\(B\\), written \\(A \\cup B\\), consists of:',
    options: [
      { text: 'Only elements common to both \\(A\\) and \\(B\\)', isCorrect: false },
      { text: 'All elements belonging to set \\(A\\) or set \\(B\\) or both', isCorrect: true },
      { text: 'Elements in \\(U\\) not in \\(A\\)', isCorrect: false },
      { text: 'Elements in \\(A\\) that are not in \\(B\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By definition: \\(A \\cup B = \\{x \\mid x \\in A\\text{ or } x \\in B\\}\\).\n2. In listing \\(A \\cup B\\), elements from both sets are combined, with duplicates written only once.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.4-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.4.4',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.4',
    topic: 'Union of sets (A ∪ B)',
    topicName: 'Union of sets (A ∪ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Union Calculation',
    text: 'If \\(A = \\{-1, -3, -5, 0\\}\\) and \\(B = \\{0, 3, 5\\}\\), what is \\(A \\cup B\\)?',
    options: [
      { text: '\\(\\{0\\}\\)', isCorrect: false },
      { text: '\\(\\{-5, -3, -1, 0, 3, 5\\}\\)', isCorrect: true },
      { text: '\\(\\{-5, -3, -1, 0, 0, 3, 5\\}\\)', isCorrect: false },
      { text: '\\(\\{-5, -3, 3, 5\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Combine all elements of \\(A\\) and \\(B\\):\n   \\(A = \\{-1, -3, -5, 0\\}\\)\n   \\(B = \\{0, 3, 5\\}\\)\n2. The element 0 is common, so it is listed once.\n3. In roster form: \\(A \\cup B = \\{-5, -3, -1, 0, 3, 5\\}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.4.4-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.4.4',
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    topicNumber: '1.4.4',
    topic: 'Union of sets (A ∪ B)',
    topicName: 'Union of sets (A ∪ B)',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
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
    conceptTag: 'Union with Empty Set',
    text: 'For any set \\(A\\), what is \\(A \\cup \\emptyset\\)?',
    options: [
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Since \\(\\emptyset\\) contributes no new elements, combining \\(A\\) with \\(\\emptyset\\) leaves \\(A\\) unchanged.\n2. Hence, \\(A \\cup \\emptyset = A\\).'
  },

  // =========================================================================
  // SUBTOPIC 1.5.1: Cardinality of sets [MH-9-MTH1-1-1.5.1]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.5.1-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.5.1',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.1',
    topic: 'Cardinality of sets',
    topicName: 'Cardinality of sets',
    parentTopicName: 'Number of Elements in Set Formula',
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
    conceptTag: 'Cardinality Definition',
    text: 'What does the notation \\(n(A)\\) represent in set theory?',
    options: [
      { text: 'The sum of all numbers inside set \\(A\\)', isCorrect: false },
      { text: 'The number of distinct elements in set \\(A\\)', isCorrect: true },
      { text: 'The power set of \\(A\\)', isCorrect: false },
      { text: 'The product of elements of \\(A\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. \\(n(A)\\) denotes the cardinality of set \\(A\\), which is the count of distinct elements in \\(A\\).\n2. If \\(A = \\{3, 6, 9, 12, 15\\}\\), then \\(n(A) = 5\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.5.1-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.5.1',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.1',
    topic: 'Cardinality of sets',
    topicName: 'Cardinality of sets',
    parentTopicName: 'Number of Elements in Set Formula',
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
    conceptTag: 'Cardinality Formula Calculation',
    text: 'If \\(n(A) = 15\\), \\(n(A \\cup B) = 29\\), and \\(n(A \\cap B) = 7\\), what is \\(n(B)\\)?',
    options: [
      { text: '21', isCorrect: true },
      { text: '14', isCorrect: false },
      { text: '22', isCorrect: false },
      { text: '28', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Apply the fundamental cardinality formula:\n   \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)\n2. Substitute the given values:\n   \\(29 = 15 + n(B) - 7\\)\n   \\(29 = 8 + n(B)\\)\n3. \\(n(B) = 29 - 8 = 21\\).'
  },

  // =========================================================================
  // SUBTOPIC 1.5.2: Word problems on cardinality [MH-9-MTH1-1-1.5.2]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.5.2-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.5.2',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.2',
    topic: 'Word problems on languages spoken, newspaper readers, sports participants',
    topicName: 'Word problems on languages spoken, newspaper readers, sports participants',
    parentTopicName: 'Number of Elements in Set Formula',
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
    conceptTag: 'Practice Set 1.4 Word Problem 1',
    text: 'In a class of 70 students, 45 students like to play Cricket and 52 students like to play Kho-Kho. All students play at least one of these two games. How many students play both Cricket and Kho-Kho?',
    options: [
      { text: '27', isCorrect: true },
      { text: '25', isCorrect: false },
      { text: '35', isCorrect: false },
      { text: '18', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let \\(C\\) be the set of students who play Cricket, and \\(K\\) play Kho-Kho.\n2. Given: \\(n(C \\cup K) = 70\\), \\(n(C) = 45\\), \\(n(K) = 52\\).\n3. Formula: \\(n(C \\cup K) = n(C) + n(K) - n(C \\cap K)\\)\n   \\(70 = 45 + 52 - n(C \\cap K)\\)\n   \\(70 = 97 - n(C \\cap K)\\)\n4. \\(n(C \\cap K) = 97 - 70 = 27\\).\n5. Exactly 27 students play both games.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.5.2-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.5.2',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.2',
    topic: 'Word problems on languages spoken, newspaper readers, sports participants',
    topicName: 'Word problems on languages spoken, newspaper readers, sports participants',
    parentTopicName: 'Number of Elements in Set Formula',
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
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Cricket Kho-Kho Only',
    text: 'In the above group of 70 students (45 play Cricket, 52 play Kho-Kho, 27 play both), how many students play ONLY Cricket?',
    options: [
      { text: '18', isCorrect: true },
      { text: '25', isCorrect: false },
      { text: '27', isCorrect: false },
      { text: '45', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Students playing ONLY Cricket = \\(n(C) - n(C \\cap K)\\).\n2. \\(45 - 27 = 18\\).\n3. Therefore, exactly 18 students play Cricket only.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.5.2-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.5.2',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.2',
    topic: 'Word problems on languages spoken, newspaper readers, sports participants',
    topicName: 'Word problems on languages spoken, newspaper readers, sports participants',
    parentTopicName: 'Number of Elements in Set Formula',
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
    conceptTag: 'Tea Coffee Survey',
    text: 'In a survey of 100 people, 65 drink tea and 40 drink coffee. If 20 people drink both tea and coffee, how many people drink neither tea nor coffee?',
    options: [
      { text: '15', isCorrect: true },
      { text: '5', isCorrect: false },
      { text: '25', isCorrect: false },
      { text: '10', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(n(U) = 100\\), \\(n(T) = 65\\), \\(n(C) = 40\\), \\(n(T \\cap C) = 20\\).\n2. People who drink tea or coffee = \\(n(T \\cup C) = n(T) + n(C) - n(T \\cap C) = 65 + 40 - 20 = 85\\).\n3. People who drink neither = \\(n(U) - n(T \\cup C) = 100 - 85 = 15\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.5.2-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.5.2',
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    topicNumber: '1.5.2',
    topic: 'Word problems on languages spoken, newspaper readers, sports participants',
    topicName: 'Word problems on languages spoken, newspaper readers, sports participants',
    parentTopicName: 'Number of Elements in Set Formula',
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
    conceptTag: 'Three Sets Formula Principle',
    text: 'For three finite sets \\(A, B,\\) and \\(C\\), what is the correct expansion of \\(n(A \\cup B \\cup C)\\)?',
    options: [
      { text: '\\(n(A) + n(B) + n(C) - n(A \\cap B) - n(B \\cap C) - n(A \\cap C) + n(A \\cap B \\cap C)\\)', isCorrect: true },
      { text: '\\(n(A) + n(B) + n(C) - n(A \\cap B \\cap C)\\)', isCorrect: false },
      { text: '\\(n(A) + n(B) + n(C) + n(A \\cap B) + n(B \\cap C) + n(A \\cap C)\\)', isCorrect: false },
      { text: '\\(n(A) + n(B) + n(C) - [n(A \\cap B) + n(B \\cap C) + n(A \\cap C)] - n(A \\cap B \\cap C)\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By the Principle of Inclusion-Exclusion for three sets:\n   \\(n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - n(A \\cap B) - n(B \\cap C) - n(A \\cap C) + n(A \\cap B \\cap C)\\).\n2. Pairwise intersections are subtracted because their regions were counted twice, and the triple intersection is added back because it was subtracted three times.'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Topics 1.4 and 1.5 ===`);
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
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch1_topic1_4_and_1_5');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore under Topics 1.4 & 1.5!`);
}

main().catch(console.error);
