const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const QUESTIONS = [
  // =========================================================================
  // TOPIC 2.1: Properties of Rational Numbers & Decimal Representation
  // Subtopics: 2.1.1, 2.1.2, 2.1.3
  // =========================================================================

  // --- Subtopic 2.1.1: p/q form where q != 0 (MH-9-MTH1-2-2.1.1) ---
  {
    questionCode: 'MH-9-MTH1-2-2.1.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.1.1',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.1',
    topic: 'p/q form where q != 0',
    topicName: 'p/q form where q != 0',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Rational Number Definition',
    text: 'A number which can be written in the form \\(\\frac{p}{q}\\), where \\(p\\) and \\(q\\) are integers and \\(q \\neq 0\\), is called a:',
    options: [
      { text: 'Irrational number', isCorrect: false },
      { text: 'Rational number', isCorrect: true },
      { text: 'Natural number only', isCorrect: false },
      { text: 'Complex number only', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. By definition in algebra, any number of the form \\(\\frac{p}{q}\\) where \\(p, q \\in \\mathbb{I}\\) and \\(q \\neq 0\\) is a rational number.\n2. The set of all such numbers is denoted by \\(\\mathbb{Q}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.1.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.1.1',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.1',
    topic: 'p/q form where q != 0',
    topicName: 'p/q form where q != 0',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Zero as Rational',
    text: 'Why is \\(0\\) classified as a rational number?',
    options: [
      { text: 'Because \\(0\\) can be written as \\(\\frac{0}{1}\\) where \\(0, 1 \\in \\mathbb{I}\\) and denominator \\(1 \\neq 0\\)', isCorrect: true },
      { text: 'Because \\(0\\) is neither positive nor negative', isCorrect: false },
      { text: 'Because \\(0\\) has no factors', isCorrect: false },
      { text: 'Because dividing any number by \\(0\\) gives \\(0\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Zero can be expressed as \\(\\frac{0}{q}\\) for any non-zero integer \\(q\\) (e.g. \\(\\frac{0}{1}, \\frac{0}{5}\\)).\n2. Here numerator \\(p = 0\\) is an integer, and denominator \\(q = 1 \\neq 0\\) is an integer.\n3. Therefore, \\(0\\) strictly satisfies the definition of a rational number.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.1.1-OSC-003',
    topicCode: 'MH-9-MTH1-2-2.1.1',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.1',
    topic: 'p/q form where q != 0',
    topicName: 'p/q form where q != 0',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Simplest Form Co-prime',
    text: 'In the simplest form of a rational number \\(\\frac{p}{q}\\), the greatest common divisor \\(\\gcd(p, q)\\) must be equal to:',
    options: [
      { text: '0', isCorrect: false },
      { text: '1', isCorrect: true },
      { text: '2', isCorrect: false },
      { text: 'Any prime number', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. A rational number \\(\\frac{p}{q}\\) is in irreducible or simplest form when \\(p\\) and \\(q\\) are co-prime integers.\n2. Co-prime integers share no common factors other than 1, so \\(\\gcd(p, q) = 1\\).'
  },

  // --- Subtopic 2.1.2: Terminating vs non-terminating recurring forms (MH-9-MTH1-2-2.1.2) ---
  {
    questionCode: 'MH-9-MTH1-2-2.1.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.1.2',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.2',
    topic: 'Terminating vs non-terminating recurring forms',
    topicName: 'Terminating vs non-terminating recurring forms',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Terminating Denominator Rule',
    text: 'A rational number in simplest form \\(\\frac{p}{q}\\) has a terminating decimal representation if and only if the prime factorization of denominator \\(q\\) contains:',
    options: [
      { text: 'Only prime factors 3 and 7', isCorrect: false },
      { text: 'Only prime factors 2 and/or 5', isCorrect: true },
      { text: 'Any odd prime factors', isCorrect: false },
      { text: 'At least three distinct prime factors', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. In base 10, powers of 10 factor into \\(2 \\times 5\\).\n2. Therefore, a reduced rational fraction \\(\\frac{p}{q}\\) terminates if and only if \\(q = 2^m \\times 5^n\\) where \\(m, n\\) are non-negative integers.\n3. If any other prime factor (such as 3, 7, 11) divides \\(q\\), the decimal is non-terminating recurring.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.1.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.1.2',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.2',
    topic: 'Terminating vs non-terminating recurring forms',
    topicName: 'Terminating vs non-terminating recurring forms',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Classify Terminating',
    text: 'Which of the following rational numbers has a terminating decimal expansion?',
    options: [
      { text: '\\(\\frac{13}{5}\\)', isCorrect: true },
      { text: '\\(\\frac{2}{11}\\)', isCorrect: false },
      { text: '\\(\\frac{4}{7}\\)', isCorrect: false },
      { text: '\\(\\frac{5}{6}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In \\(\\frac{13}{5}\\), the denominator is 5, so \\(\\frac{13}{5} = 2.6\\) (terminates).\n2. For \\(\\frac{2}{11}\\), denominator 11 gives non-terminating recurring \\(0.\\overline{18}\\).\n3. For \\(\\frac{4}{7}\\), denominator 7 gives recurring \\(0.\\overline{571428}\\).\n4. For \\(\\frac{5}{6}\\), denominator \\(6 = 2 \\times 3\\) contains 3, giving recurring \\(0.8\\bar{3}\\).'
  },
  // Add questions for 2.1.2 recurring decimal conversion
  {
    questionCode: 'MH-9-MTH1-2-2.1.2-OSC-003',
    topicCode: 'MH-9-MTH1-2-2.1.2',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.2',
    topic: 'Terminating vs non-terminating recurring forms',
    topicName: 'Terminating vs non-terminating recurring forms',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Recurring to Fraction 0.6 bar',
    text: 'What is the \\(\\frac{p}{q}\\) form of the recurring decimal \\(0.\\bar{6}\\)?',
    options: [
      { text: '\\(\\frac{2}{3}\\)', isCorrect: true },
      { text: '\\(\\frac{6}{10}\\)', isCorrect: false },
      { text: '\\(\\frac{3}{5}\\)', isCorrect: false },
      { text: '\\(\\frac{6}{11}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let \\(x = 0.\\bar{6} = 0.666\\dots\\)\n2. Multiply by 10 (since 1 digit repeats): \\(10x = 6.666\\dots\\)\n3. Subtract (1) from (2): \\(10x - x = 6.666\\dots - 0.666\\dots \\implies 9x = 6\\)\n4. \\(x = \\frac{6}{9} = \\frac{2}{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.1.2-OSC-004',
    topicCode: 'MH-9-MTH1-2-2.1.2',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.2',
    topic: 'Terminating vs non-terminating recurring forms',
    topicName: 'Terminating vs non-terminating recurring forms',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Recurring to Fraction 0.37 bar',
    text: 'Express \\(0.\\overline{37}\\) in \\(\\frac{p}{q}\\) rational form:',
    options: [
      { text: '\\(\\frac{37}{99}\\)', isCorrect: true },
      { text: '\\(\\frac{37}{100}\\)', isCorrect: false },
      { text: '\\(\\frac{37}{90}\\)', isCorrect: false },
      { text: '\\(\\frac{37}{9}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let \\(x = 0.\\overline{37} = 0.373737\\dots\\)\n2. Since 2 digits repeat, multiply by 100: \\(100x = 37.3737\\dots\\)\n3. Subtract: \\(100x - x = 37 \\implies 99x = 37\\)\n4. \\(x = \\frac{37}{99}\\).'
  },

  // --- Subtopic 2.1.3: Order relation properties (Trichotomy law) [MH-9-MTH1-2-2.1.3] ---
  {
    questionCode: 'MH-9-MTH1-2-2.1.3-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.1.3',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.3',
    topic: 'Order relation properties (Trichotomy law)',
    topicName: 'Order relation properties (Trichotomy law)',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Trichotomy Law',
    text: 'According to the Law of Trichotomy, for any two rational numbers \\(a\\) and \\(b\\), which of the following is true?',
    options: [
      { text: 'Both \\(a > b\\) and \\(a = b\\) can hold simultaneously', isCorrect: false },
      { text: 'Exactly one of the relations \\(a < b\\), \\(a = b\\), or \\(a > b\\) must hold', isCorrect: true },
      { text: 'Neither relation holds if \\(a\\) and \\(b\\) are fractions', isCorrect: false },
      { text: '\\(a\\) is always strictly greater than \\(b\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. The Trichotomy Law is a fundamental axiom of ordered fields.\n2. For any real numbers \\(a, b\\), exactly one of three mutually exclusive relations holds: \\(a < b\\), \\(a = b\\), or \\(a > b\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.1.3-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.1.3',
    parentTopicCode: 'MH-9-MTH1-2-2.1',
    topicNumber: '2.1.3',
    topic: 'Order relation properties (Trichotomy law)',
    topicName: 'Order relation properties (Trichotomy law)',
    parentTopicName: 'Properties of Rational Numbers & Decimal Representation',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Cross Multiplication Comparison',
    text: 'If \\(\\frac{a}{b}\\) and \\(\\frac{c}{d}\\) are rational numbers with \\(b > 0, d > 0\\) and \\(a \\times d > b \\times c\\), then:',
    options: [
      { text: '\\(\\frac{a}{b} > \\frac{c}{d}\\)', isCorrect: true },
      { text: '\\(\\frac{a}{b} < \\frac{c}{d}\\)', isCorrect: false },
      { text: '\\(\\frac{a}{b} = \\frac{c}{d}\\)', isCorrect: false },
      { text: '\\(\\frac{a}{b} + \\frac{c}{d} = 1\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Cross-multiplication property for rational comparison:\n   - If \\(a \\times d = b \\times c\\), then \\(\\frac{a}{b} = \\frac{c}{d}\\)\n   - If \\(a \\times d > b \\times c\\), then \\(\\frac{a}{b} > \\frac{c}{d}\\)\n   - If \\(a \\times d < b \\times c\\), then \\(\\frac{a}{b} < \\frac{c}{d}\\)\n2. Therefore, \\(\\frac{a}{b} > \\frac{c}{d}\\).'
  },

  // =========================================================================
  // TOPIC 2.2: Irrational Numbers: Geometric Proof of Irrationality of √2
  // Subtopics: 2.2.1, 2.2.2
  // =========================================================================

  // --- Subtopic 2.2.1: Proof by contradiction (MH-9-MTH1-2-2.2.1) ---
  {
    questionCode: 'MH-9-MTH1-2-2.2.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.2.1',
    parentTopicCode: 'MH-9-MTH1-2-2.2',
    topicNumber: '2.2.1',
    topic: 'Proof by contradiction',
    topicName: 'Proof by contradiction',
    parentTopicName: 'Irrational Numbers: Geometric Proof of Irrationality of √2',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Proof by Contradiction Method',
    text: 'In proving that \\(\\sqrt{2}\\) is an irrational number by contradiction, what initial assumption is made?',
    options: [
      { text: 'Assume that \\(\\sqrt{2} = 0\\)', isCorrect: false },
      { text: 'Assume that \\(\\sqrt{2}\\) is a rational number \\(\\frac{a}{b}\\) where \\(a, b\\) are co-prime integers and \\(b \\neq 0\\)', isCorrect: true },
      { text: 'Assume that \\(\\sqrt{2}\\) is an integer', isCorrect: false },
      { text: 'Assume that \\(\\sqrt{2} > 2\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. In proof by contradiction (reductio ad absurdum), we assume the negation of the statement to be proved.\n2. To prove \\(\\sqrt{2}\\) is irrational, we begin by assuming \\(\\sqrt{2}\\) is rational: \\(\\sqrt{2} = \\frac{a}{b}\\) where \\(a, b\\) have no common factor other than 1.\n3. Squaring leads to \\(a^2 = 2b^2\\), implying both \\(a\\) and \\(b\\) are divisible by 2, contradicting co-primality.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.2.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.2.1',
    parentTopicCode: 'MH-9-MTH1-2-2.2',
    topicNumber: '2.2.1',
    topic: 'Proof by contradiction',
    topicName: 'Proof by contradiction',
    parentTopicName: 'Irrational Numbers: Geometric Proof of Irrationality of √2',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Even Square Implication',
    text: 'During the proof of irrationality of \\(\\sqrt{2}\\), if \\(a^2 = 2b^2\\), which lemma is used to conclude that \\(a\\) is an even number?',
    options: [
      { text: 'If a prime \\(p\\) divides \\(a^2\\), then \\(p\\) divides \\(a\\)', isCorrect: true },
      { text: 'The square of an odd number is always even', isCorrect: false },
      { text: 'Every even number is a perfect square', isCorrect: false },
      { text: 'The sum of two odd numbers is even', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Since \\(a^2 = 2b^2\\), \\(a^2\\) is divisible by prime number 2.\n2. By Euclid\'s prime divisor property, if a prime \\(p\\) divides \\(a^2\\), then \\(p\\) must divide \\(a\\).\n3. Since 2 divides \\(a^2\\), 2 divides \\(a\\), meaning \\(a\\) is even.'
  },

  // --- Subtopic 2.2.2: Representation of √5, √10 on number line (MH-9-MTH1-2-2.2.2) ---
  {
    questionCode: 'MH-9-MTH1-2-2.2.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.2.2',
    parentTopicCode: 'MH-9-MTH1-2-2.2',
    topicNumber: '2.2.2',
    topic: 'Representation of √5, √10 on number line',
    topicName: 'Representation of √5, √10 on number line',
    parentTopicName: 'Irrational Numbers: Geometric Proof of Irrationality of √2',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Root 5 Pythagoras Base',
    text: 'To locate \\(\\sqrt{5}\\) on a number line using a right-angled triangle and Pythagoras theorem, which base and perpendicular lengths are typically chosen?',
    options: [
      { text: 'Base = 2 units, Perpendicular = 1 unit', isCorrect: true },
      { text: 'Base = 1 unit, Perpendicular = 1 unit', isCorrect: false },
      { text: 'Base = 3 units, Perpendicular = 2 units', isCorrect: false },
      { text: 'Base = 4 units, Perpendicular = 1 unit', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By Pythagoras theorem: \\(\\text{Hypotenuse}^2 = \\text{Base}^2 + \\text{Perpendicular}^2\\).\n2. For Base = 2 and Perpendicular = 1:\n   \\(\\text{Hypotenuse} = \\sqrt{2^2 + 1^2} = \\sqrt{4 + 1} = \\sqrt{5}\\).\n3. Using a compass with radius equal to the hypotenuse centered at 0 locates \\(\\sqrt{5}\\) on the number line.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.2.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.2.2',
    parentTopicCode: 'MH-9-MTH1-2-2.2',
    topicNumber: '2.2.2',
    topic: 'Representation of √5, √10 on number line',
    topicName: 'Representation of √5, √10 on number line',
    parentTopicName: 'Irrational Numbers: Geometric Proof of Irrationality of √2',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Root 10 Pythagoras Base',
    text: 'To locate \\(\\sqrt{10}\\) on a number line in one step, the sides of the right-angled triangle should be:',
    options: [
      { text: 'Base = 3 units, Height = 1 unit', isCorrect: true },
      { text: 'Base = 5 units, Height = 5 units', isCorrect: false },
      { text: 'Base = 2 units, Height = 2 units', isCorrect: false },
      { text: 'Base = 4 units, Height = 2 units', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(\\text{Hypotenuse} = \\sqrt{3^2 + 1^2} = \\sqrt{9 + 1} = \\sqrt{10}\\).\n2. Taking a base of 3 units from origin and an altitude of 1 unit gives a hypotenuse of \\(\\sqrt{10}\\).'
  },

  // =========================================================================
  // TOPIC 2.3: Surds: Definition, Order, Like/Unlike Surds & Simplest Form
  // Subtopics: 2.3.1, 2.3.2, 2.3.3, 2.3.4
  // =========================================================================

  // --- Subtopic 2.3.1: Definition of surd ⁿ√a (MH-9-MTH1-2-2.3.1) ---
  {
    questionCode: 'MH-9-MTH1-2-2.3.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.3.1',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.1',
    topic: 'Definition of surd ⁿ√a',
    topicName: 'Definition of surd ⁿ√a',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Surd Definition Criteria',
    text: 'An expression \\(\\sqrt[n]{a}\\) is called a surd if:',
    options: [
      { text: '\\(n\\) is an integer greater than 1, \\(a\\) is a positive rational number, and \\(\\sqrt[n]{a}\\) is an irrational number', isCorrect: true },
      { text: '\\(a\\) is any negative integer and \\(n = 2\\)', isCorrect: false },
      { text: '\\(\\sqrt[n]{a}\\) simplifies to an integer', isCorrect: false },
      { text: '\\(a\\) is an irrational number', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By definition in Maharashtra Board curriculum:\n   - \\(n\\) is a natural number greater than 1 (order of the surd)\n   - \\(a\\) is a positive rational number (radicand)\n   - \\(\\sqrt[n]{a}\\) must be an *irrational* number.\n2. For example, \\(\\sqrt{16} = 4\\) is rational, so \\(\\sqrt{16}\\) is NOT a surd.\n3. \\(\\sqrt{7}\\) is irrational, so \\(\\sqrt{7}\\) is a surd.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.3.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.3.1',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.1',
    topic: 'Definition of surd ⁿ√a',
    topicName: 'Definition of surd ⁿ√a',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Recognize Not a Surd',
    text: 'Which of the following is NOT a surd?',
    options: [
      { text: '\\(\\sqrt[3]{8}\\)', isCorrect: true },
      { text: '\\(\\sqrt{5}\\)', isCorrect: false },
      { text: '\\(\\sqrt[3]{7}\\)', isCorrect: false },
      { text: '\\(\\sqrt{10}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Simplify \\(\\sqrt[3]{8} = \\sqrt[3]{2^3} = 2\\).\n2. Since 2 is a rational number, \\(\\sqrt[3]{8}\\) is NOT a surd.\n3. \\(\\sqrt{5}, \\sqrt[3]{7}, \\sqrt{10}\\) are all irrational roots of rational numbers, and therefore are surds.'
  },

  // --- Subtopic 2.3.2: Order of surd (n) [MH-9-MTH1-2-2.3.2] ---
  {
    questionCode: 'MH-9-MTH1-2-2.3.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.3.2',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.2',
    topic: 'Order of surd (n)',
    topicName: 'Order of surd (n)',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Order of Square Root',
    text: 'What is the order of the surd \\(\\sqrt{11}\\)?',
    options: [
      { text: '1', isCorrect: false },
      { text: '2', isCorrect: true },
      { text: '11', isCorrect: false },
      { text: '0', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. When no index is written on the radical sign \\(\\sqrt{a}\\), it represents the square root (\\(\\sqrt[2]{a}\\)).\n2. Therefore, the order of the surd \\(\\sqrt{11}\\) is 2.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.3.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.3.2',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.2',
    topic: 'Order of surd (n)',
    topicName: 'Order of surd (n)',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Order of Cube Root',
    text: 'In the surd \\(5\\sqrt[4]{17}\\), what is the order of the surd and what is the radicand?',
    options: [
      { text: 'Order = 4, Radicand = 17', isCorrect: true },
      { text: 'Order = 5, Radicand = 17', isCorrect: false },
      { text: 'Order = 17, Radicand = 4', isCorrect: false },
      { text: 'Order = 4, Radicand = 5', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In \\(p\\sqrt[n]{a}\\), \\(n\\) is the order, \\(a\\) is the radicand, and \\(p\\) is the coefficient.\n2. Here \\(n = 4\\) and radicand \\(a = 17\\).'
  },

  // --- Subtopic 2.3.3: Like / similar surds [MH-9-MTH1-2-2.3.3] ---
  {
    questionCode: 'MH-9-MTH1-2-2.3.3-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.3.3',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.3',
    topic: 'Like / similar surds',
    topicName: 'Like / similar surds',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Like Surds Definition',
    text: 'Two surds are said to be like (similar) surds if in their simplest form:',
    options: [
      { text: 'Their coefficients are identical', isCorrect: false },
      { text: 'Their order is the same and their radicands are equal', isCorrect: true },
      { text: 'Their sum is a rational number', isCorrect: false },
      { text: 'Both radicands are prime numbers', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Two surds \\(p\\sqrt[n]{a}\\) and \\(q\\sqrt[n]{a}\\) are called like or similar surds if their order \\(n\\) is identical and their radicand \\(a\\) in simplest form is equal.\n2. The rational coefficients \\(p\\) and \\(q\\) may be different.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.3.3-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.3.3',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.3',
    topic: 'Like / similar surds',
    topicName: 'Like / similar surds',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Identify Like Surds 52 and 13',
    text: 'Are \\(\\sqrt{52}\\) and \\(5\\sqrt{13}\\) like surds?',
    options: [
      { text: 'Yes, because \\(\\sqrt{52} = 2\\sqrt{13}\\), so both have order 2 and same radicand 13', isCorrect: true },
      { text: 'No, because 52 is not equal to 13', isCorrect: false },
      { text: 'No, because one has coefficient 1 and other has coefficient 5', isCorrect: false },
      { text: 'Cannot be determined without a calculator', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Reduce \\(\\sqrt{52}\\) to simplest form: \\(\\sqrt{52} = \\sqrt{4 \\times 13} = 2\\sqrt{13}\\).\n2. Both \\(2\\sqrt{13}\\) and \\(5\\sqrt{13}\\) have order 2 and the identical radical factor \\(\\sqrt{13}\\).\n3. Therefore, they are like surds.'
  },

  // --- Subtopic 2.3.4: Simplest radical form [MH-9-MTH1-2-2.3.4] ---
  {
    questionCode: 'MH-9-MTH1-2-2.3.4-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.3.4',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.4',
    topic: 'Simplest radical form',
    topicName: 'Simplest radical form',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Simplest Form 48',
    text: 'What is the simplest radical form of \\(\\sqrt{48}\\)?',
    options: [
      { text: '\\(2\\sqrt{12}\\)', isCorrect: false },
      { text: '\\(4\\sqrt{3}\\)', isCorrect: true },
      { text: '\\(3\\sqrt{4}\\)', isCorrect: false },
      { text: '\\(16\\sqrt{3}\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Find the largest square factor of 48: \\(48 = 16 \\times 3\\).\n2. \\(\\sqrt{48} = \\sqrt{16 \\times 3} = \\sqrt{16} \\times \\sqrt{3} = 4\\sqrt{3}\\).\n3. In \\(4\\sqrt{3}\\), the radicand 3 has no square factors greater than 1, so it is in simplest form.'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.3.4-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.3.4',
    parentTopicCode: 'MH-9-MTH1-2-2.3',
    topicNumber: '2.3.4',
    topic: 'Simplest radical form',
    topicName: 'Simplest radical form',
    parentTopicName: 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Simplest Form 98',
    text: 'The simplest form of \\(\\sqrt{98}\\) is:',
    options: [
      { text: '\\(7\\sqrt{2}\\)', isCorrect: true },
      { text: '\\(2\\sqrt{7}\\)', isCorrect: false },
      { text: '\\(14\\sqrt{2}\\)', isCorrect: false },
      { text: '\\(49\\sqrt{2}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Factor 98: \\(98 = 49 \\times 2 = 7^2 \\times 2\\).\n2. \\(\\sqrt{98} = \\sqrt{49 \\times 2} = 7\\sqrt{2}\\).'
  },

  // =========================================================================
  // TOPIC 2.4: Operations on Surds & Comparison of Surds
  // Subtopics: 2.4.1, 2.4.2
  // =========================================================================

  // --- Subtopic 2.4.1: Addition, subtraction, multiplication, division (MH-9-MTH1-2-2.4.1) ---
  {
    questionCode: 'MH-9-MTH1-2-2.4.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.4.1',
    parentTopicCode: 'MH-9-MTH1-2-2.4',
    topicNumber: '2.4.1',
    topic: 'Addition, subtraction, multiplication, division of surds',
    topicName: 'Addition, subtraction, multiplication, division of surds',
    parentTopicName: 'Operations on Surds & Comparison of Surds',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Addition of Like Surds',
    text: 'Simplify: \\(5\\sqrt{3} + 8\\sqrt{3}\\)',
    options: [
      { text: '\\(13\\sqrt{6}\\)', isCorrect: false },
      { text: '\\(13\\sqrt{3}\\)', isCorrect: true },
      { text: '\\(40\\sqrt{3}\\)', isCorrect: false },
      { text: '\\(39\\)', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. These are like surds with common radical \\(\\sqrt{3}\\).\n2. Factor out \\(\\sqrt{3}\\): \\((5 + 8)\\sqrt{3} = 13\\sqrt{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.4.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.4.1',
    parentTopicCode: 'MH-9-MTH1-2-2.4',
    topicNumber: '2.4.1',
    topic: 'Addition, subtraction, multiplication, division of surds',
    topicName: 'Addition, subtraction, multiplication, division of surds',
    parentTopicName: 'Operations on Surds & Comparison of Surds',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Complex Surd Simplification',
    text: 'Simplify: \\(4\\sqrt{12} - \\sqrt{75} - 7\\sqrt{48}\\)',
    options: [
      { text: '\\(-25\\sqrt{3}\\)', isCorrect: true },
      { text: '\\(-15\\sqrt{3}\\)', isCorrect: false },
      { text: '\\(10\\sqrt{3}\\)', isCorrect: false },
      { text: '\\(-31\\sqrt{3}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Convert each surd to simplest radical form:\n   - \\(4\\sqrt{12} = 4\\sqrt{4 \\times 3} = 4(2)\\sqrt{3} = 8\\sqrt{3}\\)\n   - \\(\\sqrt{75} = \\sqrt{25 \\times 3} = 5\\sqrt{3}\\)\n   - \\(7\\sqrt{48} = 7\\sqrt{16 \\times 3} = 7(4)\\sqrt{3} = 28\\sqrt{3}\\)\n2. Combine terms:\n   \\(8\\sqrt{3} - 5\\sqrt{3} - 28\\sqrt{3} = (8 - 5 - 28)\\sqrt{3} = -25\\sqrt{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.4.1-OSC-003',
    topicCode: 'MH-9-MTH1-2-2.4.1',
    parentTopicCode: 'MH-9-MTH1-2-2.4',
    topicNumber: '2.4.1',
    topic: 'Addition, subtraction, multiplication, division of surds',
    topicName: 'Addition, subtraction, multiplication, division of surds',
    parentTopicName: 'Operations on Surds & Comparison of Surds',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Multiplication of Surds',
    text: 'Multiply and simplify: \\(3\\sqrt{12} \\times 2\\sqrt{3}\\)',
    options: [
      { text: '\\(36\\)', isCorrect: true },
      { text: '\\(18\\sqrt{3}\\)', isCorrect: false },
      { text: '\\(18\\)', isCorrect: false },
      { text: '\\(72\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Multiply rational coefficients: \\(3 \\times 2 = 6\\).\n2. Multiply radicals: \\(\\sqrt{12} \\times \\sqrt{3} = \\sqrt{36} = 6\\).\n3. Product: \\(6 \\times 6 = 36\\).'
  },
  // --- Subtopic 2.4.2: Comparing pure and mixed surds [MH-9-MTH1-2-2.4.2] ---
  {
    questionCode: 'MH-9-MTH1-2-2.4.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.4.2',
    parentTopicCode: 'MH-9-MTH1-2-2.4',
    topicNumber: '2.4.2',
    topic: 'Comparing pure and mixed surds',
    topicName: 'Comparing pure and mixed surds',
    parentTopicName: 'Operations on Surds & Comparison of Surds',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Compare 7√2 and 5√3',
    text: 'Compare the two surds \\(7\\sqrt{2}\\) and \\(5\\sqrt{3}\\):',
    options: [
      { text: '\\(7\\sqrt{2} > 5\\sqrt{3}\\)', isCorrect: true },
      { text: '\\(7\\sqrt{2} < 5\\sqrt{3}\\)', isCorrect: false },
      { text: '\\(7\\sqrt{2} = 5\\sqrt{3}\\)', isCorrect: false },
      { text: 'They cannot be compared because their radicands differ', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Convert both mixed surds into pure surds:\n   \\(7\\sqrt{2} = \\sqrt{7^2 \\times 2} = \\sqrt{49 \\times 2} = \\sqrt{98}\\)\n   \\(5\\sqrt{3} = \\sqrt{5^2 \\times 3} = \\sqrt{25 \\times 3} = \\sqrt{75}\\)\n2. Since \\(98 > 75\\), \\(\\sqrt{98} > \\sqrt{75}\\).\n3. Therefore, \\(7\\sqrt{2} > 5\\sqrt{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.4.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.4.2',
    parentTopicCode: 'MH-9-MTH1-2-2.4',
    topicNumber: '2.4.2',
    topic: 'Comparing pure and mixed surds',
    topicName: 'Comparing pure and mixed surds',
    parentTopicName: 'Operations on Surds & Comparison of Surds',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Compare 4√42 and 9√2',
    text: 'Which relation correctly compares \\(2\\sqrt{7}\\) and \\(\\sqrt{28}\\)?',
    options: [
      { text: '\\(2\\sqrt{7} = \\sqrt{28}\\)', isCorrect: true },
      { text: '\\(2\\sqrt{7} > \\sqrt{28}\\)', isCorrect: false },
      { text: '\\(2\\sqrt{7} < \\sqrt{28}\\)', isCorrect: false },
      { text: '\\(2\\sqrt{7} \\times \\sqrt{28} = 1\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Convert \\(2\\sqrt{7}\\) to pure surd:\n   \\(2\\sqrt{7} = \\sqrt{2^2 \\times 7} = \\sqrt{4 \\times 7} = \\sqrt{28}\\).\n2. Both expressions represent the identical number.\n3. Therefore, \\(2\\sqrt{7} = \\sqrt{28}\\).'
  },

  // =========================================================================
  // TOPIC 2.5: Rationalisation of Surds & Conjugate Pairs
  // Subtopics: 2.5.1, 2.5.2
  // =========================================================================

  // --- Subtopic 2.5.1: Rationalising factor definition (MH-9-MTH1-2-2.5.1) ---
  {
    questionCode: 'MH-9-MTH1-2-2.5.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.5.1',
    parentTopicCode: 'MH-9-MTH1-2-2.5',
    topicNumber: '2.5.1',
    topic: 'Rationalising factor definition',
    topicName: 'Rationalising factor definition',
    parentTopicName: 'Rationalisation of Surds & Conjugate Pairs',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Rationalising Factor Definition',
    text: 'If the product of two surds is a rational number, then each surd is called a/an ________ of the other.',
    options: [
      { text: 'Rationalising factor', isCorrect: true },
      { text: 'Conjugate power', isCorrect: false },
      { text: 'Radical index', isCorrect: false },
      { text: 'Additive inverse', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By definition, if the product of two surds yields a rational number, then each surd is the rationalising factor (RF) of the other.\n2. For instance, \\(\\sqrt{2} \\times \\sqrt{2} = 2\\) (rational), so \\(\\sqrt{2}\\) is the rationalising factor of \\(\\sqrt{2}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.5.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.5.1',
    parentTopicCode: 'MH-9-MTH1-2-2.5',
    topicNumber: '2.5.1',
    topic: 'Rationalising factor definition',
    topicName: 'Rationalising factor definition',
    parentTopicName: 'Rationalisation of Surds & Conjugate Pairs',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Simplest RF of Root 8',
    text: 'What is the simplest rationalising factor of \\(\\sqrt{8}\\)?',
    options: [
      { text: '\\(\\sqrt{2}\\)', isCorrect: true },
      { text: '\\(\\sqrt{8}\\)', isCorrect: false },
      { text: '\\(2\\)', isCorrect: false },
      { text: '\\(\\sqrt{4}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. First simplify \\(\\sqrt{8}\\): \\(\\sqrt{8} = \\sqrt{4 \\times 2} = 2\\sqrt{2}\\).\n2. To make \\(2\\sqrt{2}\\) rational, multiplying by \\(\\sqrt{2}\\) gives \\(2\\sqrt{2} \\times \\sqrt{2} = 2(2) = 4\\) (rational).\n3. Although \\(\\sqrt{8}\\) also rationalises it, \\(\\sqrt{2}\\) is the simplest rationalising factor.'
  },

  // --- Subtopic 2.5.2: Conjugate pair of binomial surd (MH-9-MTH1-2-2.5.2) ---
  {
    questionCode: 'MH-9-MTH1-2-2.5.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.5.2',
    parentTopicCode: 'MH-9-MTH1-2-2.5',
    topicNumber: '2.5.2',
    topic: 'Conjugate pair of binomial surd (√a + √b)(√a - √b)',
    topicName: 'Conjugate pair of binomial surd (√a + √b)(√a - √b)',
    parentTopicName: 'Rationalisation of Surds & Conjugate Pairs',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Conjugate Pair Definition',
    text: 'What is the conjugate pair of the binomial surd \\(\\sqrt{5} + \\sqrt{3}\\)?',
    options: [
      { text: '\\(\\sqrt{5} - \\sqrt{3}\\)', isCorrect: true },
      { text: '\\(-\\sqrt{5} - \\sqrt{3}\\)', isCorrect: false },
      { text: '\\(5 - 3\\)', isCorrect: false },
      { text: '\\(\\sqrt{3} + \\sqrt{5}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The conjugate of a binomial surd \\(\\sqrt{a} + \\sqrt{b}\\) is \\(\\sqrt{a} - \\sqrt{b}\\).\n2. Their product uses the difference of squares: \\((\\sqrt{a} + \\sqrt{b})(\\sqrt{a} - \\sqrt{b}) = a - b\\), which is rational.\n3. Hence, the conjugate of \\(\\sqrt{5} + \\sqrt{3}\\) is \\(\\sqrt{5} - \\sqrt{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.5.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.5.2',
    parentTopicCode: 'MH-9-MTH1-2-2.5',
    topicNumber: '2.5.2',
    topic: 'Conjugate pair of binomial surd (√a + √b)(√a - √b)',
    topicName: 'Conjugate pair of binomial surd (√a + √b)(√a - √b)',
    parentTopicName: 'Rationalisation of Surds & Conjugate Pairs',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Rationalise Denominator Binomial',
    text: 'Rationalise the denominator of \\(\\frac{1}{\\sqrt{7} - \\sqrt{2}}\\):',
    options: [
      { text: '\\(\\frac{\\sqrt{7} + \\sqrt{2}}{5}\\)', isCorrect: true },
      { text: '\\(\\frac{\\sqrt{7} - \\sqrt{2}}{5}\\)', isCorrect: false },
      { text: '\\(\\frac{\\sqrt{7} + \\sqrt{2}}{9}\\)', isCorrect: false },
      { text: '\\(\\sqrt{7} + \\sqrt{2}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Multiply numerator and denominator by the conjugate \\(\\sqrt{7} + \\sqrt{2}\\):\n   \\(\\frac{1}{\\sqrt{7} - \\sqrt{2}} \\times \\frac{\\sqrt{7} + \\sqrt{2}}{\\sqrt{7} + \\sqrt{2}}\\)\n2. Denominator: \\((\\sqrt{7})^2 - (\\sqrt{2})^2 = 7 - 2 = 5\\).\n3. Result: \\(\\frac{\\sqrt{7} + \\sqrt{2}}{5}\\).'
  },

  // =========================================================================
  // TOPIC 2.6: Absolute Value / Modulus of Real Numbers
  // Subtopics: 2.6.1, 2.6.2
  // =========================================================================

  // --- Subtopic 2.6.1: Definition |x| [MH-9-MTH1-2-2.6.1] ---
  {
    questionCode: 'MH-9-MTH1-2-2.6.1-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.6.1',
    parentTopicCode: 'MH-9-MTH1-2-2.6',
    topicNumber: '2.6.1',
    topic: 'Definition |x|',
    topicName: 'Definition |x|',
    parentTopicName: 'Absolute Value / Modulus of Real Numbers',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Modulus Definition',
    text: 'The absolute value (modulus) of a real number \\(x\\), denoted by \\(|x|\\), is defined as:',
    options: [
      { text: '\\(|x| = x\\) if \\(x \\ge 0\\), and \\(|x| = -x\\) if \\(x < 0\\)', isCorrect: true },
      { text: '\\(|x| = -x\\) for all real numbers', isCorrect: false },
      { text: '\\(|x| = x^2\\)', isCorrect: false },
      { text: '\\(|x| = 0\\) if \\(x < 0\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The absolute value represents distance from origin on a number line, which is always non-negative.\n2. If \\(x > 0\\), \\(|x| = x\\).\n3. If \\(x = 0\\), \\(|0| = 0\\).\n4. If \\(x < 0\\), \\(|x| = -x\\) (e.g. \\(|-5| = -(-5) = 5\\)).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.6.1-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.6.1',
    parentTopicCode: 'MH-9-MTH1-2-2.6',
    topicNumber: '2.6.1',
    topic: 'Definition |x|',
    topicName: 'Definition |x|',
    parentTopicName: 'Absolute Value / Modulus of Real Numbers',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Modulus Value Calculation',
    text: 'Evaluate: \\(|15 - 21|\\)',
    options: [
      { text: '-6', isCorrect: false },
      { text: '6', isCorrect: true },
      { text: '36', isCorrect: false },
      { text: '15', isCorrect: false }
    ],
    correctAnswer: 'B',
    solution: '1. Compute the inside expression: \\(15 - 21 = -6\\).\n2. Take the absolute value: \\(|-6| = -(-6) = 6\\).'
  },

  // --- Subtopic 2.6.2: Solving modulus equations |x - a| = b [MH-9-MTH1-2-2.6.2] ---
  {
    questionCode: 'MH-9-MTH1-2-2.6.2-OSC-001',
    topicCode: 'MH-9-MTH1-2-2.6.2',
    parentTopicCode: 'MH-9-MTH1-2-2.6',
    topicNumber: '2.6.2',
    topic: 'Solving modulus equations |x - a| = b',
    topicName: 'Solving modulus equations |x - a| = b',
    parentTopicName: 'Absolute Value / Modulus of Real Numbers',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Solve Modulus Practice Set 2.5 Q2',
    text: 'Solve the equation for \\(x\\): \\(|3x - 5| = 1\\)',
    options: [
      { text: '\\(x = 2\\) or \\(x = \\frac{4}{3}\\)', isCorrect: true },
      { text: '\\(x = 2\\) or \\(x = -2\\)', isCorrect: false },
      { text: '\\(x = \\frac{4}{3}\\) only', isCorrect: false },
      { text: '\\(x = 6\\) or \\(x = 4\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(|3x - 5| = 1 \\implies 3x - 5 = 1\\) or \\(3x - 5 = -1\\).\n2. Case 1: \\(3x - 5 = 1 \\implies 3x = 6 \\implies x = 2\\).\n3. Case 2: \\(3x - 5 = -1 \\implies 3x = 4 \\implies x = \\frac{4}{3}\\).\n4. Therefore, \\(x = 2\\) or \\(x = \\frac{4}{3}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.6.2-OSC-002',
    topicCode: 'MH-9-MTH1-2-2.6.2',
    parentTopicCode: 'MH-9-MTH1-2-2.6',
    topicNumber: '2.6.2',
    topic: 'Solving modulus equations |x - a| = b',
    topicName: 'Solving modulus equations |x - a| = b',
    parentTopicName: 'Absolute Value / Modulus of Real Numbers',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Solve Modulus 7 - 2x = 5',
    text: 'What are the solutions to the equation \\(|7 - 2x| = 5\\)?',
    options: [
      { text: '\\(x = 1\\) or \\(x = 6\\)', isCorrect: true },
      { text: '\\(x = 1\\) or \\(x = -6\\)', isCorrect: false },
      { text: '\\(x = -1\\) or \\(x = 6\\)', isCorrect: false },
      { text: '\\(x = 12\\) or \\(x = 2\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. \\(|7 - 2x| = 5 \\implies 7 - 2x = 5\\) or \\(7 - 2x = -5\\).\n2. Case 1: \\(7 - 2x = 5 \\implies -2x = -2 \\implies x = 1\\).\n3. Case 2: \\(7 - 2x = -5 \\implies -2x = -12 \\implies x = 6\\).\n4. Solutions are \\(x = 1\\) and \\(x = 6\\).'
  },
  {
    questionCode: 'MH-9-MTH1-2-2.6.2-OSC-003',
    topicCode: 'MH-9-MTH1-2-2.6.2',
    parentTopicCode: 'MH-9-MTH1-2-2.6',
    topicNumber: '2.6.2',
    topic: 'Solving modulus equations |x - a| = b',
    topicName: 'Solving modulus equations |x - a| = b',
    parentTopicName: 'Absolute Value / Modulus of Real Numbers',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 2,
    chapter: 'Real Numbers',
    vault: 'foundation',
    examCategory: 'foundation',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Modulus Negative RHS',
    text: 'What is the solution set of the equation \\(|2x - 3| = -5\\) in the set of real numbers \\(\\mathbb{R}\\)?',
    options: [
      { text: '\\(\\emptyset\\) (No real solution)', isCorrect: true },
      { text: '\\(\\{-1, 4\\}\\)', isCorrect: false },
      { text: '\\(\\{4\\}\\)', isCorrect: false },
      { text: '\\(\\{-1\\}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By definition, the absolute value of any real expression is non-negative: \\(|2x - 3| \\ge 0\\) for all \\(x \\in \\mathbb{R}\\).\n2. A non-negative quantity can never equal \\(-5\\).\n3. Therefore, no real number satisfies the equation, and the solution set is empty (\\(\\emptyset\\)).'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Chapter 2 Real Numbers ===`);
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
  console.log('All Chapter 2 questions passed strict validation perfectly!');

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch2_real_numbers');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore across Chapter 2 Real Numbers!`);
}

main().catch(console.error);
