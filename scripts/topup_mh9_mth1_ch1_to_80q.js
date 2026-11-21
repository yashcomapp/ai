const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

// Helper to shuffle options and ensure deterministic correctAnswer
function makeQ(data) {
  const letters = ['A', 'B', 'C', 'D'];
  const correctIdx = data.options.findIndex(o => o.isCorrect === true);
  if (correctIdx === -1) {
    throw new Error(`Question ${data.questionCode} has no correct option`);
  }
  return {
    ...data,
    correctAnswer: letters[correctIdx],
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 1,
    chapter: 'Sets',
    type: 'OSC',
    marks: 4,
    timesUsed: 0,
    usedInClassroomTest: false,
    requiresFigure: false,
    createdAt: new Date(),
    updatedAt: new Date()
  };
}

const QUESTIONS = [];

// =========================================================================
// TOPIC 1.1: 5 Foundation Questions to reach 20 Foundation
// =========================================================================
const t11Fnd = [
  {
    num: '1.1.1', subName: 'Well-defined collection of objects', tag: 'Well Defined Objects',
    text: 'Which of the following is a well-defined collection of objects?',
    opts: [
      { text: 'The collection of all vowels in the English alphabet', isCorrect: true },
      { text: 'The collection of good students in a school', isCorrect: false },
      { text: 'The collection of tasty fruits in the market', isCorrect: false },
      { text: 'The collection of rich merchants in a town', isCorrect: false }
    ],
    sol: '1. A collection is well-defined if it is universally definite whether an object belongs to it.\n2. Vowels in the English alphabet are strictly \\(\\{A, E, I, O, U\\}\\).\n3. Concepts like "good", "tasty", or "rich" are subjective opinions.'
  },
  {
    num: '1.1.1', subName: 'Well-defined collection of objects', tag: 'Not Well Defined Example',
    text: 'Which of the following collections is NOT a set?',
    opts: [
      { text: 'The collection of courageous persons in a village', isCorrect: true },
      { text: 'The collection of days in a week', isCorrect: false },
      { text: 'The collection of prime numbers less than 20', isCorrect: false },
      { text: 'The collection of planets in the solar system', isCorrect: false }
    ],
    sol: '1. "Courageous persons" is a subjective quality with no exact mathematical criteria.\n2. Therefore, it is not a well-defined collection and cannot form a set.'
  },
  {
    num: '1.1.2', subName: 'Roster / Listing method', tag: 'Roster Method Natural Numbers',
    text: 'Write the set of natural numbers between 10 and 15 in listing (roster) form:',
    opts: [
      { text: '\\(\\{11, 12, 13, 14\\}\\)', isCorrect: true },
      { text: '\\(\\{10, 11, 12, 13, 14, 15\\}\\)', isCorrect: false },
      { text: '\\(\\{11, 13\\}\\)', isCorrect: false },
      { text: '\\(\\{10, 15\\}\\)', isCorrect: false }
    ],
    sol: '1. Natural numbers strictly between 10 and 15 exclude the boundaries 10 and 15.\n2. The elements are 11, 12, 13, 14.\n3. In roster form: \\(\\{11, 12, 13, 14\\}\\).'
  },
  {
    num: '1.1.3', subName: 'Set-builder / Rule method', tag: 'Rule Method Square Numbers',
    text: 'Express the set \\(A = \\{1, 4, 9, 16, 25\\}\\) in rule (set-builder) form:',
    opts: [
      { text: '\\(A = \\{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 5\\}\\)', isCorrect: true },
      { text: '\\(A = \\{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 5\\}\\)', isCorrect: false },
      { text: '\\(A = \\{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 5\\}\\)', isCorrect: false },
      { text: '\\(A = \\{x \\mid x = n + 3, n \\in \\mathbb{N}\\}\\)', isCorrect: false }
    ],
    sol: '1. The elements are \\(1^2, 2^2, 3^2, 4^2, 5^2\\).\n2. Each element is the square of a natural number from 1 to 5.\n3. In set-builder form: \\(A = \\{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 5\\}\\).'
  },
  {
    num: '1.1.3', subName: 'Set-builder / Rule method', tag: 'Rule Method Multiples',
    text: 'Express the set \\(B = \\{5, 10, 15, 20, 25\\}\\) in set-builder form:',
    opts: [
      { text: '\\(B = \\{x \\mid x = 5n, n \\in \\mathbb{N}, 1 \\le n \\le 5\\}\\)', isCorrect: true },
      { text: '\\(B = \\{x \\mid x = 5 + n, n \\in \\mathbb{N}\\}\\)', isCorrect: false },
      { text: '\\(B = \\{x \\mid x = n^5, n \\in \\mathbb{N}\\}\\)', isCorrect: false },
      { text: '\\(B = \\{x \\mid x \\text{ is any multiple of 5}\\}\\)', isCorrect: false }
    ],
    sol: '1. The elements are multiples of 5: \\(5 \\times 1, 5 \\times 2, \\dots, 5 \\times 5\\).\n2. Therefore \\(x = 5n\\) where \\(n \\in \\mathbb{N}\\) and \\(1 \\le n \\le 5\\).'
  }
];

t11Fnd.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  QUESTIONS.push(makeQ({
    questionCode: `MH-9-MTH1-1-${item.num}-OSC-F${seq}`,
    topicCode: `MH-9-MTH1-1-${item.num}`,
    parentTopicCode: 'MH-9-MTH1-1-1.1',
    topicNumber: item.num,
    topic: item.subName,
    topicName: item.subName,
    parentTopicName: 'Sets: Definition, Elements & Methods of Writing (Listing & Rule Form)',
    vault: 'foundation',
    examCategory: 'foundation',
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: item.tag,
    text: item.text,
    options: item.opts,
    solution: item.sol
  }));
});

// =========================================================================
// TOPIC 1.2: Types of Sets (61 questions: 29 Exam, 15 Practice, 17 Foundation)
// Subtopics: 1.2.1, 1.2.2, 1.2.3, 1.2.4
// =========================================================================
const t12Data = [
  // 1.2.1: Singleton Set (16 questions: 8 Exam, 4 Practice, 4 Foundation)
  {
    sub: '1.2.1', name: 'Singleton set (one element)',
    items: [
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Even Prime Singleton',
        text: 'The set of all even prime numbers is an example of a:',
        opts: [{ text: 'Singleton set \\(\\{2\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Infinite set', isCorrect: false }, { text: 'Universal set only', isCorrect: false }],
        sol: '1. 2 is the only even prime number.\n2. Hence the set contains exactly one element: \\(\\{2\\}\\).\n3. A set with exactly one element is called a singleton set.' },
      { v: 'exam', d: 'easy', b: 'Apply', tag: 'Linear Equation Singleton',
        text: 'What type of set is \\(A = \\{x \\mid x \\in \\mathbb{I}, 2x + 7 = 13\\}\\)?',
        opts: [{ text: 'Singleton set \\(\\{3\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Infinite set', isCorrect: false }, { text: 'Two-element set', isCorrect: false }],
        sol: '1. \\(2x + 7 = 13 \\implies 2x = 6 \\implies x = 3\\).\n2. Since 3 is an integer, \\(A = \\{3\\}\\).\n3. It contains exactly one element, so it is a singleton set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Whole Number Before 1',
        text: 'The set \\(W_0 = \\{x \\mid x \\in \\mathbb{W}, x < 1\\}\\) is:',
        opts: [{ text: 'A singleton set \\(\\{0\\}\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A non-defined set', isCorrect: false }],
        sol: '1. The whole numbers are \\(\\{0, 1, 2, \\dots\\}\\).\n2. The only whole number strictly less than 1 is 0.\n3. Hence \\(W_0 = \\{0\\}\\), which is a singleton set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Zero Element Singleton',
        text: 'Is the set \\(S = \\{0\\}\\) an empty set?',
        opts: [{ text: 'No, it is a singleton set containing the element 0', isCorrect: true }, { text: 'Yes, because 0 means nothing', isCorrect: false }, { text: 'Yes, because \\(n(S) = 0\\)', isCorrect: false }, { text: 'No, it is an infinite set', isCorrect: false }],
        sol: '1. The set \\(\\{0\\}\\) contains one element, which is the number 0.\n2. Cardinality \\(n(S) = 1\\).\n3. Hence it is a singleton set, NOT an empty set.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Quadratic Singleton',
        text: 'Find the nature of the set \\(P = \\{x \\mid x \\in \\mathbb{R}, x^2 - 6x + 9 = 0\\}\\):',
        opts: [{ text: 'Singleton set \\(\\{3\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Two-element set \\(\\{-3, 3\\}\\)', isCorrect: false }, { text: 'Infinite set', isCorrect: false }],
        sol: '1. \\(x^2 - 6x + 9 = (x - 3)^2 = 0 \\implies x = 3\\).\n2. Both roots are equal to 3.\n3. The set of solutions is \\(\\{3\\}\\), which is a singleton set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Odd Prime Less than 4',
        text: 'The set \\(T = \\{x \\mid x \\text{ is an odd prime number}, x < 5\\}\\) is:',
        opts: [{ text: 'Singleton set \\(\\{3\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Set with two elements \\(\\{1, 3\\}\\)', isCorrect: false }, { text: 'Infinite set', isCorrect: false }],
        sol: '1. Prime numbers less than 5 are 2 and 3.\n2. Among these, the only odd prime is 3 (1 is not prime).\n3. Thus \\(T = \\{3\\}\\), a singleton set.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Modulus Singleton',
        text: 'What type of set is \\(M = \\{x \\mid x \\in \\mathbb{R}, |x| = 0\\}\\)?',
        opts: [{ text: 'Singleton set \\(\\{0\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Two-element set', isCorrect: false }, { text: 'Infinite set', isCorrect: false }],
        sol: '1. The equation \\(|x| = 0\\) has only one real solution, \\(x = 0\\).\n2. Therefore, \\(M = \\{0\\}\\), which is a singleton set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Capital of India Singleton',
        text: 'The set \\(C = \\{x \\mid x \\text{ is the capital city of India}\\}\\) is:',
        opts: [{ text: 'A singleton set \\(\\{\\text{New Delhi}\\}\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'A finite set with 28 elements', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. India has exactly one official national capital city: New Delhi.\n2. Hence the set contains exactly one element, making it a singleton set.' },

      // Practice (4)
      { v: 'practice', d: 'easy', b: 'Remember', tag: 'Singleton Definition',
        text: 'A set having only one element is formally termed as a:',
        opts: [{ text: 'Singleton set', isCorrect: true }, { text: 'Null set', isCorrect: false }, { text: 'Disjoint set', isCorrect: false }, { text: 'Universal set', isCorrect: false }],
        sol: '1. By mathematical definition, any set \\(S\\) with cardinality \\(n(S) = 1\\) is called a singleton set.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Square Equals 4 Natural',
        text: 'The set \\(A = \\{x \\mid x \\in \\mathbb{N}, x^2 = 4\\}\\) is:',
        opts: [{ text: 'A singleton set \\(\\{2\\}\\)', isCorrect: true }, { text: 'A two-element set \\(\\{-2, 2\\}\\)', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. \\(x^2 = 4 \\implies x = 2\\) or \\(x = -2\\).\n2. But \\(x \\in \\mathbb{N}\\) (natural numbers are positive integers), so \\(-2 \\notin \\mathbb{N}\\).\n3. Hence \\(A = \\{2\\}\\), which is a singleton set.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Negative Integer Greater than -2',
        text: 'The set \\(K = \\{x \\mid x \\in \\mathbb{I}^-, x > -2\\}\\) of negative integers greater than -2 is:',
        opts: [{ text: 'Singleton set \\(\\{-1\\}\\)', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Set \\(\\{0, -1\\}\\)', isCorrect: false }, { text: 'Infinite set', isCorrect: false }],
        sol: '1. Negative integers are \\(\\{-1, -2, -3, \\dots\\}\\).\n2. The only negative integer strictly greater than \\(-2\\) is \\(-1\\).\n3. Hence \\(K = \\{-1\\}\\), a singleton set.' },
      { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Cubic Singleton',
        text: 'The set \\(B = \\{x \\mid x \\in \\mathbb{R}, x^3 = -27\\}\\) is:',
        opts: [{ text: 'A singleton set \\(\\{-3\\}\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'A three-element set in real numbers', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. In the set of real numbers \\(\\mathbb{R}\\), \\(x^3 = -27\\) has exactly one real solution: \\(x = -3\\).\n2. Therefore \\(B = \\{-3\\}\\), which is a singleton set.' },

      // Foundation (4)
      { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Cardinality of Singleton',
        text: 'If set \\(S\\) is a singleton set, what is the value of \\(n(S)\\)?',
        opts: [{ text: '\\(1\\)', isCorrect: true }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(2\\)', isCorrect: false }, { text: '\\(\\infty\\)', isCorrect: false }],
        sol: '1. A singleton set contains exactly one element.\n2. Hence its cardinality \\(n(S) = 1\\).' },
      { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Notation of Singleton',
        text: 'Which of the following notations represents a singleton set?',
        opts: [{ text: '\\(\\{a\\}\\)', isCorrect: true }, { text: '\\(\\{\\}\\)', isCorrect: false }, { text: '\\(\\emptyset\\)', isCorrect: false }, { text: '\\(\\{a, b\\}\\)', isCorrect: false }],
        sol: '1. \\(\\{a\\}\\) contains exactly one element \\(a\\).\n2. \\(\\{\\}\\) and \\(\\emptyset\\) represent the empty set.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Integer Neither Pos Nor Neg',
        text: 'The set of all integers that are neither positive nor negative is:',
        opts: [{ text: 'A singleton set \\(\\{0\\}\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A two-element set', isCorrect: false }],
        sol: '1. The only integer that is neither positive nor negative is 0.\n2. Therefore the set is \\(\\{0\\}\\), a singleton set.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Linear Equation 5x = 0',
        text: 'The solution set of \\(5x = 0\\) in whole numbers \\(\\mathbb{W}\\) is:',
        opts: [{ text: 'A singleton set \\(\\{0\\}\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'The entire set \\(\\mathbb{W}\\)', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
        sol: '1. \\(5x = 0 \\implies x = 0\\).\n2. Since \\(0 \\in \\mathbb{W}\\), the set is \\(\\{0\\}\\), which is a singleton set.' }
    ]
  },

  // 1.2.2: Empty / Null Set (15 questions: 7 Exam, 4 Practice, 4 Foundation)
  {
    sub: '1.2.2', name: 'Null / Empty set (∅ or {})',
    items: [
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Empty Set Natural Between 1 and 2',
        text: 'The set \\(A = \\{x \\mid x \\in \\mathbb{N}, 1 < x < 2\\}\\) is:',
        opts: [{ text: 'An empty set (\\(\\emptyset\\))', isCorrect: true }, { text: 'A singleton set \\(\\{1.5\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A universal set', isCorrect: false }],
        sol: '1. Natural numbers are integers \\(1, 2, 3, \\dots\\)\n2. There is no natural number between 1 and 2.\n3. Therefore, \\(A\\) contains no elements: \\(A = \\emptyset\\).' },
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Empty Set Symbol',
        text: 'An empty set is denoted by the Greek letter:',
        opts: [{ text: '\\(\\emptyset\\) (phi) or \\(\\{\\}\\)', isCorrect: true }, { text: '\\(\\pi\\) (pi)', isCorrect: false }, { text: '\\(\\theta\\) (theta)', isCorrect: false }, { text: '\\(\\alpha\\) (alpha)', isCorrect: false }],
        sol: '1. An empty set contains no elements and is denoted by \\(\\emptyset\\) (phi) or a pair of empty braces \\(\\{\\}\\).' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Even Prime Greater than 2',
        text: 'The set of all even prime numbers greater than 2 is:',
        opts: [{ text: 'An empty set \\(\\emptyset\\)', isCorrect: true }, { text: 'A singleton set \\(\\{4\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A finite set of 3 elements', isCorrect: false }],
        sol: '1. 2 is the ONLY even prime number.\n2. Any even number greater than 2 is divisible by 2, hence composite.\n3. Therefore, no even prime greater than 2 exists, so the set is empty.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Natural Less than 1',
        text: 'The set \\(B = \\{x \\mid x \\in \\mathbb{N}, x < 1\\}\\) is:',
        opts: [{ text: 'An empty set \\(\\emptyset\\)', isCorrect: true }, { text: 'A singleton set \\(\\{0\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A set containing \\(-1\\)', isCorrect: false }],
        sol: '1. The set of natural numbers begins from 1: \\(\\mathbb{N} = \\{1, 2, 3, \\dots\\}\\).\n2. There is no natural number less than 1.\n3. Hence \\(B = \\emptyset\\).' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Negative Square Real',
        text: 'The set \\(S = \\{x \\mid x \\in \\mathbb{R}, x^2 + 1 = 0\\}\\) is:',
        opts: [{ text: 'An empty set in \\(\\mathbb{R}\\)', isCorrect: true }, { text: 'A singleton set \\(\\{-1\\}\\)', isCorrect: false }, { text: 'A two-element set \\(\\{-1, 1\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. \\(x^2 + 1 = 0 \\implies x^2 = -1\\).\n2. In the set of real numbers \\(\\mathbb{R}\\), the square of any real number is non-negative (\\(x^2 \\ge 0\\)).\n3. No real number satisfies \\(x^2 = -1\\), so \\(S = \\emptyset\\).' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Parallel Lines Intersection',
        text: 'The set of points of intersection of two distinct parallel lines in a plane is:',
        opts: [{ text: 'An empty set', isCorrect: true }, { text: 'A singleton set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A two-point set', isCorrect: false }],
        sol: '1. By geometric definition, parallel lines in a plane never intersect.\n2. Therefore, they share 0 common points.\n3. The set of intersection points is empty.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Odd Divisible by 2',
        text: 'The set of all odd natural numbers divisible by 2 is:',
        opts: [{ text: 'An empty set', isCorrect: true }, { text: 'A singleton set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'All natural numbers', isCorrect: false }],
        sol: '1. By definition, an odd number is never divisible by 2.\n2. Hence no odd number satisfies this condition, making the set empty.' },

      // Practice (4)
      { v: 'practice', d: 'easy', b: 'Remember', tag: 'Cardinality of Empty Set',
        text: 'If set \\(A\\) is an empty set, what is the number of elements \\(n(A)\\)?',
        opts: [{ text: '\\(0\\)', isCorrect: true }, { text: '\\(1\\)', isCorrect: false }, { text: '\\(-1\\)', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
        sol: '1. An empty set contains no elements at all.\n2. Hence \\(n(A) = 0\\).' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Empty Set Identification',
        text: 'Which of the following represents an empty set?',
        opts: [{ text: '\\(\\{x \\mid x \\in \\mathbb{W}, x < 0\\}\\)', isCorrect: true }, { text: '\\(\\{0\\}\\)', isCorrect: false }, { text: '\\(\\{\\emptyset\\}\\)', isCorrect: false }, { text: '\\(\\{x \\mid x \\in \\mathbb{I}, x = 0\\}\\)', isCorrect: false }],
        sol: '1. Whole numbers \\(\\mathbb{W} = \\{0, 1, 2, \\dots\\}\\) contain no negative numbers.\n2. Hence \\(\\{x \\mid x \\in \\mathbb{W}, x < 0\\} = \\emptyset\\).\n3. Note: \\(\\{0\\}\\) and \\(\\{\\emptyset\\}\\) both have 1 element and are singleton sets.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Square Smaller than Zero Real',
        text: 'The set \\(C = \\{x \\mid x \\in \\mathbb{R}, x^2 < 0\\}\\) is:',
        opts: [{ text: 'An empty set', isCorrect: true }, { text: 'A singleton set', isCorrect: false }, { text: 'All negative real numbers', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. For every real number \\(x\\), \\(x^2 \\ge 0\\).\n2. No real number has a negative square.\n3. Therefore, \\(C = \\emptyset\\).' },
      { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Natural Divisible by Zero',
        text: 'The set \\(D = \\{x \\mid x \\in \\mathbb{N}, x / 0 = 5\\}\\) is:',
        opts: [{ text: 'An empty set (division by zero is undefined)', isCorrect: true }, { text: '\\(\\{0\\}\\)', isCorrect: false }, { text: '\\(\\{5\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. Division by zero is mathematically undefined.\n2. No natural number satisfies \\(x / 0 = 5\\).\n3. Hence \\(D = \\emptyset\\).' },

      // Foundation (4)
      { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Null Set Synonym',
        text: 'Another commonly used mathematical term for an empty set is a:',
        opts: [{ text: 'Null set or void set', isCorrect: true }, { text: 'Unit set', isCorrect: false }, { text: 'Universal set', isCorrect: false }, { text: 'Cardinal set', isCorrect: false }],
        sol: '1. An empty set is also called a null set or a void set.' },
      { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Braces with Phi',
        text: 'What type of set is \\(\\{\\emptyset\\}\\)?',
        opts: [{ text: 'A singleton set containing the element \\(\\emptyset\\)', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'An invalid notation', isCorrect: false }],
        sol: '1. \\(\\{\\emptyset\\}\\) has one element inside the braces, namely the symbol \\(\\emptyset\\).\n2. Since \\(n(\\{\\emptyset\\}) = 1\\), it is a singleton set, not an empty set.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Triangle with 4 Sides',
        text: 'The set of all triangles having 4 sides is:',
        opts: [{ text: 'An empty set', isCorrect: true }, { text: 'A singleton set', isCorrect: false }, { text: 'A quadrilateral set', isCorrect: false }, { text: 'An infinite set', isCorrect: false }],
        sol: '1. By definition, every triangle has exactly 3 sides.\n2. A polygon with 4 sides cannot be a triangle.\n3. Hence the set is empty.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Months with 32 Days',
        text: 'The set of months in a calendar year having 32 days is:',
        opts: [{ text: 'An empty set', isCorrect: true }, { text: 'A singleton set', isCorrect: false }, { text: 'A set of 7 elements', isCorrect: false }, { text: 'A finite set', isCorrect: false }],
        sol: '1. No calendar month has 32 days (months have 28, 29, 30, or 31 days).\n2. Therefore the set is empty.' }
    ]
  },

  // 1.2.3: Finite Set (15 questions: 7 Exam, 4 Practice, 4 Foundation)
  {
    sub: '1.2.3', name: 'Finite set (countable elements)',
    items: [
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Finite Set Definition',
        text: 'A set is called a finite set if it is empty or if the counting of its elements:',
        opts: [{ text: 'Terminates at a certain natural number', isCorrect: true }, { text: 'Continues indefinitely without end', isCorrect: false }, { text: 'Cannot be determined', isCorrect: false }, { text: 'Is greater than one million', isCorrect: false }],
        sol: '1. If a set has a countable number of elements where the counting process terminates, it is a finite set.\n2. The empty set \\(\\emptyset\\) is also classified as a finite set with cardinality 0.' },
      { v: 'exam', d: 'easy', b: 'Apply', tag: 'Letters of Word Finite',
        text: 'The set of distinct letters in the word "DIVISION" is a:',
        opts: [{ text: 'Finite set with 6 elements \\(\\{D, I, V, S, O, N\\}\\)', isCorrect: true }, { text: 'Infinite set', isCorrect: false }, { text: 'Finite set with 8 elements', isCorrect: false }, { text: 'Empty set', isCorrect: false }],
        sol: '1. Distinct letters: D, I, V, S, O, N.\n2. The number of elements is 6, which is countable.\n3. Hence it is a finite set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Divisors of 36',
        text: 'What is the cardinality of the finite set of all positive factors of 36?',
        opts: [{ text: '\\(9\\)', isCorrect: true }, { text: '\\(8\\)', isCorrect: false }, { text: '\\(6\\)', isCorrect: false }, { text: '\\(10\\)', isCorrect: false }],
        sol: '1. Factors of 36: \\(1, 2, 3, 4, 6, 9, 12, 18, 36\\).\n2. Count of elements \\(= 9\\).\n3. It is a finite set with \\(n(A) = 9\\).' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Days of Week Finite',
        text: 'The set \\(D = \\{x \\mid x \\text{ is a day of the week}\\}\\) has cardinality:',
        opts: [{ text: '\\(n(D) = 7\\), making it a finite set', isCorrect: true }, { text: '\\(n(D) = 365\\)', isCorrect: false }, { text: 'Infinite', isCorrect: false }, { text: '\\(n(D) = 1\\)', isCorrect: false }],
        sol: '1. There are 7 days in a week.\n2. Since the elements can be counted and terminate at 7, it is a finite set.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Quadratic Finite Set',
        text: 'The solution set of \\(x^2 - 5x + 6 = 0\\) in real numbers is:',
        opts: [{ text: 'A finite set \\(\\{2, 3\\}\\)', isCorrect: true }, { text: 'An infinite set', isCorrect: false }, { text: 'A singleton set \\(\\{5\\}\\)', isCorrect: false }, { text: 'An empty set', isCorrect: false }],
        sol: '1. \\(x^2 - 5x + 6 = (x - 2)(x - 3) = 0 \\implies x = 2\\) or \\(x = 3\\).\n2. The set is \\(\\{2, 3\\}\\), which has 2 elements and is finite.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Primes Less than 10',
        text: 'The set \\(P = \\{x \\mid x \\text{ is a prime number}, x < 10\\}\\) is:',
        opts: [{ text: 'A finite set \\(\\{2, 3, 5, 7\\}\\)', isCorrect: true }, { text: 'A finite set \\(\\{1, 2, 3, 5, 7, 9\\}\\)', isCorrect: false }, { text: 'An infinite set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Prime numbers less than 10 are 2, 3, 5, and 7.\n2. It has exactly 4 elements, so it is a finite set.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Empty Set is Finite',
        text: 'Why is the empty set \\(\\emptyset\\) mathematically classified as a finite set?',
        opts: [{ text: 'Because its number of elements is 0, which is a definite non-infinite integer', isCorrect: true }, { text: 'Because it has no definition', isCorrect: false }, { text: 'It is actually classified as infinite', isCorrect: false }, { text: 'Because it contains zero as an element', isCorrect: false }],
        sol: '1. By mathematical set theory, a set is finite if its cardinality is a non-negative integer \\(n \\in \\{0, 1, 2, \\dots\\}\\).\n2. Since \\(n(\\emptyset) = 0\\), the empty set is strictly finite.' },

      // Practice (4)
      { v: 'practice', d: 'easy', b: 'Remember', tag: 'Classify Finite',
        text: 'Which of the following is an example of a finite set?',
        opts: [{ text: 'The set of students in Class 9 of a school', isCorrect: true }, { text: 'The set of all points on a straight line', isCorrect: false }, { text: 'The set of all natural numbers \\(\\mathbb{N}\\)', isCorrect: false }, { text: 'The set of all circles passing through origin', isCorrect: false }],
        sol: '1. The number of students in a class is a definite countable number.\n2. Points on a line and natural numbers are infinite.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Two Digit Primes Finite',
        text: 'The set of all two-digit prime numbers is:',
        opts: [{ text: 'A finite set', isCorrect: true }, { text: 'An infinite set', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Two-digit numbers range from 10 to 99.\n2. There are 21 prime numbers in this range (from 11 to 97).\n3. Since the count terminates, it is a finite set.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Natural Multiples Less than 50',
        text: 'The set \\(M = \\{x \\mid x = 7n, n \\in \\mathbb{N}, x < 50\\}\\) is:',
        opts: [{ text: 'A finite set \\(\\{7, 14, 21, 28, 35, 42, 49\\}\\)', isCorrect: true }, { text: 'An infinite set', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Multiples of 7 less than 50 are 7, 14, 21, 28, 35, 42, 49.\n2. Count \\(= 7\\), so it is a finite set.' },
      { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Factors of Prime',
        text: 'For any prime number \\(p\\), the set of its positive factors is always a finite set with cardinality:',
        opts: [{ text: '\\(2\\) (elements are \\(1\\) and \\(p\\))', isCorrect: true }, { text: '\\(1\\)', isCorrect: false }, { text: '\\(p\\)', isCorrect: false }, { text: 'Infinite', isCorrect: false }],
        sol: '1. A prime number has exactly two positive factors: 1 and itself.\n2. Thus the set of factors is \\(\\{1, p\\}\\), which is finite with cardinality 2.' },

      // Foundation (4)
      { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Cardinal Number of Finite',
        text: 'The number of distinct elements present in a finite set \\(A\\) is called its:',
        opts: [{ text: 'Cardinal number \\(n(A)\\)', isCorrect: true }, { text: 'Index number', isCorrect: false }, { text: 'Degree of set', isCorrect: false }, { text: 'Power value', isCorrect: false }],
        sol: '1. The count of distinct elements in a finite set is called its cardinal number or cardinality, denoted \\(n(A)\\).' },
      { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Finite Set Identification',
        text: 'Is the set \\(\\{1, 2, 3, 4, 5\\}\\) finite or infinite?',
        opts: [{ text: 'Finite, because it contains exactly 5 elements', isCorrect: true }, { text: 'Infinite, because it contains numbers', isCorrect: false }, { text: 'Singleton', isCorrect: false }, { text: 'Empty', isCorrect: false }],
        sol: '1. The set has a fixed count of 5 elements, making it finite.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Letters of ALGEBRA',
        text: 'What is the cardinality \\(n(S)\\) of the set of letters in the word "ALGEBRA"?',
        opts: [{ text: '\\(6\\) (distinct letters: A, L, G, E, B, R)', isCorrect: true }, { text: '\\(7\\)', isCorrect: false }, { text: '\\(5\\)', isCorrect: false }, { text: '\\(8\\)', isCorrect: false }],
        sol: '1. In set notation, duplicate elements are listed only once.\n2. The letter A appears twice, so distinct letters are A, L, G, E, B, R.\n3. Cardinality \\(= 6\\).' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Whole Numbers Under 10',
        text: 'How many elements are in the set \\(W_{10} = \\{x \\mid x \\in \\mathbb{W}, x < 10\\}\\)?',
        opts: [{ text: '\\(10\\) (from 0 to 9)', isCorrect: true }, { text: '\\(9\\)', isCorrect: false }, { text: '\\(11\\)', isCorrect: false }, { text: 'Infinite', isCorrect: false }],
        sol: '1. Whole numbers start from 0: \\(0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\).\n2. Total count is 10.' }
    ]
  },

  // 1.2.4: Infinite Set (15 questions: 7 Exam, 3 Practice, 5 Foundation)
  {
    sub: '1.2.4', name: 'Infinite set (N, W, I, Q, R)',
    items: [
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Infinite Set Definition',
        text: 'A set whose process of counting elements does not terminate and continues without end is called an:',
        opts: [{ text: 'Infinite set', isCorrect: true }, { text: 'Finite set', isCorrect: false }, { text: 'Empty set', isCorrect: false }, { text: 'Singleton set', isCorrect: false }],
        sol: '1. If the number of elements in a set is unlimited and unending, it is called an infinite set.' },
      { v: 'exam', d: 'easy', b: 'Remember', tag: 'Natural Numbers Set Infinite',
        text: 'Which of the following standard number systems is an infinite set?',
        opts: [{ text: 'The set of natural numbers \\(\\mathbb{N} = \\{1, 2, 3, \\dots\\}\\)', isCorrect: true }, { text: 'The set of numbers on a standard six-sided die', isCorrect: false }, { text: 'The set of letters in the English alphabet', isCorrect: false }, { text: 'The set of hours in a day', isCorrect: false }],
        sol: '1. The sequence of natural numbers goes on endlessly.\n2. Therefore \\(\\mathbb{N}\\) is an infinite set.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Multiples of 3 Infinite',
        text: 'The set \\(M = \\{x \\mid x = 3n, n \\in \\mathbb{N}\\}\\) is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }, { text: 'An empty set', isCorrect: false }],
        sol: '1. Multiples of 3 are \\(\\{3, 6, 9, 12, 15, \\dots\\}\\).\n2. Since natural numbers \\(\\mathbb{N}\\) are endless, the multiples continue indefinitely.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Points on Line Infinite',
        text: 'The set of all points on a geometric straight line segment of length 5 cm is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set of 5 elements', isCorrect: false }, { text: 'A finite set of 50 elements', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Between any two distinct points on a real line, there are infinitely many points.\n2. Hence any line segment contains an infinite set of points.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Rational Between 2 and 3',
        text: 'The set of all rational numbers between 2 and 3 is:',
        opts: [{ text: 'An infinite set (by density property of \\(\\mathbb{Q}\\))', isCorrect: true }, { text: 'An empty set', isCorrect: false }, { text: 'A finite set with 10 elements', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Between any two distinct rational numbers, infinitely many rational numbers can be found.\n2. Hence the set of rational numbers between 2 and 3 is infinite.' },
      { v: 'exam', d: 'medium', b: 'Apply', tag: 'Integers Set Infinite',
        text: 'The set of integers \\(\\mathbb{I} = \\{\\dots, -3, -2, -1, 0, 1, 2, 3, \\dots\\}\\) is:',
        opts: [{ text: 'An infinite set extending in both positive and negative directions', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }, { text: 'An empty set', isCorrect: false }],
        sol: '1. The set of integers is unbounded on both sides and has an infinite number of elements.' },
      { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Concentric Circles Infinite',
        text: 'The set of all concentric circles drawn with a common centre \\(O\\) in a plane is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }, { text: 'An empty set', isCorrect: false }],
        sol: '1. Circles can be drawn with any positive real radius \\(r > 0\\).\n2. Since there are infinitely many positive real numbers, the set of concentric circles is infinite.' },

      // Practice (3)
      { v: 'practice', d: 'easy', b: 'Remember', tag: 'Ellipsis Notation Infinite',
        text: 'In the listing method, an infinite set is indicated by writing three dots \\((\\dots)\\) called an:',
        opts: [{ text: 'Ellipsis', isCorrect: true }, { text: 'Asterisk', isCorrect: false }, { text: 'Hyphen', isCorrect: false }, { text: 'Exponent', isCorrect: false }],
        sol: '1. The symbol \\(\\dots\\) is called an ellipsis and indicates that the pattern continues endlessly.' },
      { v: 'practice', d: 'medium', b: 'Apply', tag: 'Odd Numbers Infinite',
        text: 'The set \\(O = \\{1, 3, 5, 7, \\dots\\}\\) is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Odd numbers proceed endlessly, so it is an infinite set.' },
      { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Real Numbers Uncountable Infinite',
        text: 'The set of all real numbers \\(\\mathbb{R}\\) between 0 and 1 is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. Real numbers in any interval \\((0, 1)\\) are infinite and continuous.' },

      // Foundation (5)
      { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Standard Sets N and W',
        text: 'Both \\(\\mathbb{N}\\) (Natural numbers) and \\(\\mathbb{W}\\) (Whole numbers) are classified as:',
        opts: [{ text: 'Infinite sets', isCorrect: true }, { text: 'Finite sets', isCorrect: false }, { text: 'Empty sets', isCorrect: false }, { text: 'Singleton sets', isCorrect: false }],
        sol: '1. Both sets contain infinitely many elements.' },
      { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Can Infinite Set Cardinality be Counted',
        text: 'Can the cardinal number \\(n(A)\\) of an infinite set be expressed as a natural number?',
        opts: [{ text: 'No, because its elements cannot be completely counted', isCorrect: true }, { text: 'Yes, it is always 1000', isCorrect: false }, { text: 'Yes, it is always 0', isCorrect: false }, { text: 'Yes, it equals 1', isCorrect: false }],
        sol: '1. The elements of an infinite set are endless, so cardinality cannot be written as a finite number.' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Fraction Denominator Infinite',
        text: 'The set \\(\\{\\frac{1}{2}, \\frac{1}{3}, \\frac{1}{4}, \\frac{1}{5}, \\dots\\}\\) is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set', isCorrect: false }, { text: 'An empty set', isCorrect: false }, { text: 'A singleton set', isCorrect: false }],
        sol: '1. The denominators continue infinitely through all natural numbers \\(n \\ge 2\\).' },
      { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Lines Through Point Infinite',
        text: 'The set of all straight lines passing through a single given point in a plane is:',
        opts: [{ text: 'An infinite set', isCorrect: true }, { text: 'A finite set of 360 lines', isCorrect: false }, { text: 'A singleton set', isCorrect: false }, { text: 'An empty set', isCorrect: false }],
        sol: '1. Through a single point in a plane, infinitely many distinct lines can be drawn.' },
      { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Whole Numbers Notation',
        text: 'In set notation, \\(\\mathbb{W} = \\{0, 1, 2, 3, \\dots\\}\\) represents:',
        opts: [{ text: 'The infinite set of whole numbers', isCorrect: true }, { text: 'The finite set of digits', isCorrect: false }, { text: 'The set of negative numbers', isCorrect: false }, { text: 'The empty set', isCorrect: false }],
        sol: '1. \\(\\mathbb{W}\\) denotes whole numbers, which is an infinite set starting from 0.' }
    ]
  }
];

t12Data.forEach(subObj => {
  subObj.items.forEach((item, idx) => {
    const seq = String(idx + 1).padStart(3, '0');
    const vPrefix = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
    QUESTIONS.push(makeQ({
      questionCode: `MH-9-MTH1-1-${subObj.sub}-OSC-${vPrefix}${seq}`,
      topicCode: `MH-9-MTH1-1-${subObj.sub}`,
      parentTopicCode: 'MH-9-MTH1-1-1.2',
      topicNumber: subObj.sub,
      topic: subObj.name,
      topicName: subObj.name,
      parentTopicName: 'Types of Sets: Singleton, Empty, Finite & Infinite Sets',
      vault: item.v,
      examCategory: item.v === 'foundation' ? 'foundation' : 'standard',
      difficulty: item.d,
      bloomLevel: item.b,
      conceptTag: item.tag,
      text: item.text,
      options: item.opts,
      solution: item.sol
    }));
  });
});

console.log(`Generated ${QUESTIONS.length} questions so far (Topics 1.1 and 1.2 complete).`);

module.exports = { topic1And2Questions: QUESTIONS };
