const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

// Topic 1.3: Equal Sets, Subsets & Universal Set
// Subtopics: 1.3.1, 1.3.2, 1.3.3
const QUESTIONS = [
  // =========================================================================
  // SUBTOPIC 1.3.1: Equal sets condition (same elements) [MH-9-MTH1-1-1.3.1]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.3.1-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.3.1',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.1',
    topic: 'Equal sets condition (same elements)',
    topicName: 'Equal sets condition (same elements)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Equal Sets Definition',
    text: 'Two sets \\(A\\) and \\(B\\) are said to be equal (written as \\(A = B\\)) if:',
    options: [
      { text: 'They have the same number of elements', isCorrect: false },
      { text: 'Every element of \\(A\\) is in \\(B\\) and every element of \\(B\\) is in \\(A\\)', isCorrect: true },
      { text: 'Their elements are written in the exact same order', isCorrect: false },
      { text: 'Both sets are infinite', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By definition, two sets \\(A\\) and \\(B\\) are equal if and only if they contain exactly the same elements: \\(A \\subseteq B\\) and \\(B \\subseteq A\\).\n2. Having the same number of elements makes them equivalent, but not necessarily equal.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.1-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.3.1',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.1',
    topic: 'Equal sets condition (same elements)',
    topicName: 'Equal sets condition (same elements)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Equal Sets Verification',
    text: 'Let \\(A = \\{x \\mid x\\text{ is a letter in \"LISTEN\"}\\}\\) and \\(B = \\{y \\mid y\\text{ is a letter in \"SILENT\"}\\}\\). Are \\(A\\) and \\(B\\) equal sets?',
    options: [
      { text: 'Yes, because both sets contain the exact same letters \\(\\{\\text{L, I, S, T, E, N}\\}\\)', isCorrect: true },
      { text: 'No, because the letters are arranged in a different sequence', isCorrect: false },
      { text: 'No, because \"LISTEN\" and \"SILENT\" have different meanings', isCorrect: false },
      { text: 'Cannot be determined without a Venn diagram', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In roster form:\n   \\(A = \\{\\text{L, I, S, T, E, N}\\}\\)\n   \\(B = \\{\\text{S, I, L, E, N, T}\\}\\)\n2. Both sets have identical elements; the order of listing does not matter.\n3. Therefore, \\(A = B\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.1-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.3.1',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.1',
    topic: 'Equal sets condition (same elements)',
    topicName: 'Equal sets condition (same elements)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Even Prime and Solved Equation',
    text: 'Let \\(A = \\{x \\mid 3x - 1 = 2\\}\\) and \\(B = \\{x \\mid x \\in \\mathbb{N},\\ x\\text{ is neither prime nor composite}\\}\\). Which statement is true?',
    options: [
      { text: '\\(A = B = \\{1\\}\\)', isCorrect: true },
      { text: '\\(A \\neq B\\)', isCorrect: false },
      { text: '\\(A = \\emptyset\\)', isCorrect: false },
      { text: '\\(B = \\{0, 1\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Solve for \\(A\\): \\(3x - 1 = 2 \\implies 3x = 3 \\implies x = 1\\). Thus \\(A = \\{1\\}\\).\n2. For \\(B\\): The only natural number that is neither prime nor composite is 1. Thus \\(B = \\{1\\}\\).\n3. Since both contain the single identical element 1, \\(A = B = \\{1\\}\\).'
  },

  // =========================================================================
  // SUBTOPIC 1.3.2: Subset definition (A ⊆ B) [MH-9-MTH1-1-1.3.2]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.3.2-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.3.2',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.2',
    topic: 'Subset definition (A ⊆ B)',
    topicName: 'Subset definition (A ⊆ B)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Subset Symbol',
    text: 'If every element of set \\(A\\) is also an element of set \\(B\\), then \\(A\\) is called a:',
    options: [
      { text: 'Universal set of \\(B\\)', isCorrect: false },
      { text: 'Subset of \\(B\\), denoted as \\(A \\subseteq B\\)', isCorrect: true },
      { text: 'Complement of \\(B\\)', isCorrect: false },
      { text: 'Disjoint set to \\(B\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. If every member of \\(A\\) is present in \\(B\\), then \\(A\\) is a subset of \\(B\\), written \\(A \\subseteq B\\).\n2. Here \\(B\\) is also called the superset of \\(A\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.2-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.3.2',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.2',
    topic: 'Subset definition (A ⊆ B)',
    topicName: 'Subset definition (A ⊆ B)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Subsets Count Formula',
    text: 'How many total subsets can be formed from the set \\(A = \\{1, 2, 3\\}\\)?',
    options: [
      { text: '3', isCorrect: false },
      { text: '6', isCorrect: false },
      { text: '8', isCorrect: true },
      { text: '9', isCorrect: false }
    ],
    correctAnswer: 'C',
    solution: '1. For a set with \\(n\\) elements, the total number of possible subsets is given by the formula \\(2^n\\).\n2. Here \\(n(A) = 3\\), so total subsets = \\(2^3 = 8\\).\n3. The 8 subsets are: \\(\\emptyset, \\{1\\}, \\{2\\}, \\{3\\}, \\{1, 2\\}, \\{2, 3\\}, \\{1, 3\\}, \\{1, 2, 3\\}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.2-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.3.2',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.2',
    topic: 'Subset definition (A ⊆ B)',
    topicName: 'Subset definition (A ⊆ B)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Every Set Subset of Itself',
    text: 'Which of the following properties of subsets is FALSE?',
    options: [
      { text: 'Every set is a subset of itself (\\(A \\subseteq A\\))', isCorrect: false },
      { text: 'Empty set is a subset of every set (\\(\\emptyset \\subseteq A\\))', isCorrect: false },
      { text: 'If \\(A \\subseteq B\\) and \\(B \\subseteq A\\), then \\(A = B\\)', isCorrect: false },
      { text: 'Every set has only one subset', isCorrect: true }
    ],
    correctAnswer: 'D',
    solution: '1. Standard subset properties: (i) \\(A \\subseteq A\\), (ii) \\(\\emptyset \\subseteq A\\), (iii) \\(A \\subseteq B\\) and \\(B \\subseteq A \\implies A = B\\).\n2. Any set with \\(n\\) elements has \\(2^n\\) subsets (e.g. 1 element has 2 subsets, 2 elements have 4 subsets).\n3. Statement D is completely false.'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.2-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.3.2',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.2',
    topic: 'Subset definition (A ⊆ B)',
    topicName: 'Subset definition (A ⊆ B)',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Proper Subsets Count',
    text: 'The number of proper subsets of a non-empty set with \\(n\\) elements is:',
    options: [
      { text: '\\(2^n\\)', isCorrect: false },
      { text: '\\(2^n - 1\\)', isCorrect: true },
      { text: '\\(2^n - 2\\)', isCorrect: false },
      { text: '\\(n^2 - 1\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. A subset \\(S\\) of \\(A\\) is a "proper subset" if \\(S \\neq A\\) (the set itself is excluded).\n2. Total subsets = \\(2^n\\).\n3. Excluding \\(A\\) gives exactly \\(2^n - 1\\) proper subsets.'
  },

  // =========================================================================
  // SUBTOPIC 1.3.3: Universal set (U) and Complement of a set (A') [MH-9-MTH1-1-1.3.3]
  // =========================================================================
  {
    questionCode: 'MH-9-MTH1-1-1.3.3-OSC-001',
    topicCode: 'MH-9-MTH1-1-1.3.3',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Universal Set Definition',
    text: 'A suitably chosen large set of which all sets under consideration are subsets is called the:',
    options: [
      { text: 'Empty set', isCorrect: false },
      { text: 'Universal set, denoted by \\(U\\)', isCorrect: true },
      { text: 'Power set', isCorrect: false },
      { text: 'Singleton set', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. In any specific mathematical discussion, a comprehensive set containing all relevant objects as elements is designated as the Universal Set, conventionally denoted by capital \\(U\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.3-OSC-002',
    topicCode: 'MH-9-MTH1-1-1.3.3',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Complement Calculation',
    text: 'Let Universal set \\(U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}\\) and \\(A = \\{2, 4, 6, 8, 10\\}\\). What is the complement set \\(A\'\\)?',
    options: [
      { text: '\\(\\{1, 3, 5, 7, 9\\}\\)', isCorrect: true },
      { text: '\\(\\{2, 4, 6, 8, 10\\}\\)', isCorrect: false },
      { text: '\\(\\{1, 2, 3, 4, 5\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The complement of set \\(A\\) (denoted \\(A\'\\) or \\(A^c\\)) contains all elements of universal set \\(U\\) that do NOT belong to \\(A\\):\n   \\(A\' = \\{x \\in U \\mid x \\notin A\\}\\).\n2. Removing even numbers \\(\\{2, 4, 6, 8, 10\\}\\) from \\(U\\) leaves odd numbers \\(\\{1, 3, 5, 7, 9\\}\\).\n3. Thus, \\(A\' = \\{1, 3, 5, 7, 9\\}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.3-OSC-003',
    topicCode: 'MH-9-MTH1-1-1.3.3',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Double Complement Law',
    text: 'What is the complement of the complement of a set, i.e., \\((A\')\'\\)?',
    options: [
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By the law of double complementation (involution law):\n   \\(A\' = \\{x \\in U \\mid x \\notin A\\}\\).\n2. The elements of \\(U\\) not in \\(A\'\\) are precisely the elements in \\(A\\).\n3. Hence, \\((A\')\' = A\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.3-OSC-004',
    topicCode: 'MH-9-MTH1-1-1.3.3',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Universal and Empty Complements',
    text: 'What are the complements of the Universal set \\(U\\) and the Empty set \\(\\emptyset\\) respectively?',
    options: [
      { text: '\\(U\' = \\emptyset\\) and \\(\\emptyset\' = U\\)', isCorrect: true },
      { text: '\\(U\' = U\\) and \\(\\emptyset\' = \\emptyset\\)', isCorrect: false },
      { text: '\\(U\' = A\\) and \\(\\emptyset\' = A\'\\)', isCorrect: false },
      { text: '\\(U\' = \\emptyset\\) and \\(\\emptyset\' = \\emptyset\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(U\' = \\{x \\in U \\mid x \\notin U\\} = \\emptyset\\) (no element can be not in \\(U\\)).\n2. \\(\\emptyset\' = \\{x \\in U \\mid x \\notin \\emptyset\\} = U\\) (every element of \\(U\\) is not in \\(\\emptyset\\)).\n3. Therefore, \\(U\' = \\emptyset\\) and \\(\\emptyset\' = U\\).'
  },
  {
    questionCode: 'MH-9-MTH1-1-1.3.3-OSC-005',
    topicCode: 'MH-9-MTH1-1-1.3.3',
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
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
    conceptTag: 'Complement Disjoint Property',
    text: 'Which of the following is true regarding a set \\(A\\) and its complement \\(A\'\\)?',
    options: [
      { text: '\\(A \\cap A\' = \\emptyset\\) and \\(A \\cup A\' = U\\)', isCorrect: true },
      { text: '\\(A \\cap A\' = U\\) and \\(A \\cup A\' = \\emptyset\\)', isCorrect: false },
      { text: '\\(A \\cap A\' = A\\)', isCorrect: false },
      { text: '\\(A \\cup A\' = A\'\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. No element can simultaneously belong to \\(A\\) and not belong to \\(A\\), so \\(A \\cap A\' = \\emptyset\\) (they are disjoint).\n2. Every element in \\(U\\) either belongs to \\(A\\) or does not belong to \\(A\\), so \\(A \\cup A\' = U\\).'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Topic 1.3 ===`);
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
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch1_topic1_3');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore under Topic 1.3!`);
}

main().catch(console.error);
