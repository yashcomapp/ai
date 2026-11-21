const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const QUESTIONS = [
  // =========================================================================
  // CHAPTER 5: Linear Equations in Two Variables
  // Topics: 5.1, 5.2, 5.3
  // =========================================================================

  // --- Subtopic 5.1.1: Standard form ax + by = c [MH-9-MTH1-5-5.1.1] ---
  {
    questionCode: 'MH-9-MTH1-5-5.1.1-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.1.1',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.1',
    topic: 'Standard form ax + by = c',
    topicName: 'Standard form ax + by = c',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Standard Form Condition',
    text: 'An equation of the form \\(ax + by + c = 0\\) is called a linear equation in two variables \\(x\\) and \\(y\\) if and only if \\(a, b, c\\) are real numbers and:',
    options: [
      { text: '\\(a \\neq 0\\) and \\(b \\neq 0\\) simultaneously', isCorrect: true },
      { text: '\\(a = 0\\) and \\(b = 0\\)', isCorrect: false },
      { text: '\\(c \\neq 0\\) only', isCorrect: false },
      { text: 'Degree of each variable is 2', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. A linear equation in two variables has degree 1 for each variable.\n2. In \\(ax + by + c = 0\\), if \\(a = 0\\) and \\(b = 0\\), it ceases to be an equation in two variables.\n3. Therefore, \\(a\\) and \\(b\\) cannot both be zero simultaneously (\\(a^2 + b^2 \\neq 0\\)).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.1.1-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.1.1',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.1',
    topic: 'Standard form ax + by = c',
    topicName: 'Standard form ax + by = c',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Identify Linear in Two Variables',
    text: 'Which of the following equations is a linear equation in two variables?',
    options: [
      { text: '\\(4m + 3n = 12\\)', isCorrect: true },
      { text: '\\(3x^2 - 7y = 13\\)', isCorrect: false },
      { text: '\\(\\frac{4}{x} + \\frac{5}{y} = 4\\)', isCorrect: false },
      { text: '\\(4xy - 5y - 8 = 0\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In \\(4m + 3n = 12\\), the variables are \\(m\\) and \\(n\\), both having degree 1, and coefficients are non-zero.\n2. In \\(3x^2 - 7y = 13\\), degree is 2 (quadratic).\n3. In \\(\\frac{4}{x} + \\frac{5}{y} = 4\\), powers are \\(-1\\).\n4. In \\(4xy - 5y - 8 = 0\\), degree of term \\(4xy\\) is \\(1 + 1 = 2\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.1.1-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.1.1',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.1',
    topic: 'Standard form ax + by = c',
    topicName: 'Standard form ax + by = c',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Write in Standard Form',
    text: 'Express \\(y = \\frac{2}{3}x - 5\\) in standard form \\(ax + by = c\\) with integer coefficients (where \\(a > 0\\)):',
    options: [
      { text: '\\(2x - 3y = 15\\)', isCorrect: true },
      { text: '\\(2x + 3y = 15\\)', isCorrect: false },
      { text: '\\(3x - 2y = 15\\)', isCorrect: false },
      { text: '\\(2x - 3y = -15\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Multiply both sides by 3 to clear the denominator: \\(3y = 2x - 15\\).\n2. Rearrange terms to the standard \\(ax + by = c\\) format: \\(2x - 3y = 15\\).\n3. Here \\(a = 2, b = -3, c = 15\\).'
  },

  // --- Subtopic 5.1.2: Eliminating variable by equating coefficients [MH-9-MTH1-5-5.1.2] ---
  {
    questionCode: 'MH-9-MTH1-5-5.1.2-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.1.2',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.2',
    topic: 'Eliminating variable by equating coefficients',
    topicName: 'Eliminating variable by equating coefficients',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Elimination Method Solve',
    text: 'Solve the simultaneous equations by elimination method: \\(x + y = 14\\) and \\(x - y = 4\\). The solution \\((x, y)\\) is:',
    options: [
      { text: '\\((9, 5)\\)', isCorrect: true },
      { text: '\\((10, 4)\\)', isCorrect: false },
      { text: '\\((8, 6)\\)', isCorrect: false },
      { text: '\\((7, 7)\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Add the two equations: \\((x + y) + (x - y) = 14 + 4 \\implies 2x = 18 \\implies x = 9\\).\n2. Substitute \\(x = 9\\) into \\(x + y = 14\\): \\(9 + y = 14 \\implies y = 5\\).\n3. Therefore, the solution is \\((x, y) = (9, 5)\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.1.2-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.1.2',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.2',
    topic: 'Eliminating variable by equating coefficients',
    topicName: 'Eliminating variable by equating coefficients',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Equating Coefficients',
    text: 'To eliminate \\(y\\) from \\(2x + 3y = 11\\) and \\(3x - y = 5\\) by addition, by what number should the second equation be multiplied?',
    options: [
      { text: '\\(3\\)', isCorrect: true },
      { text: '\\(2\\)', isCorrect: false },
      { text: '\\(-2\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Coefficient of \\(y\\) in first equation is \\(+3\\).\n2. Coefficient of \\(y\\) in second equation is \\(-1\\).\n3. Multiplying the second equation by 3 gives \\(9x - 3y = 15\\).\n4. Adding both equations eliminates \\(y\\) directly.'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.1.2-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.1.2',
    parentTopicCode: 'MH-9-MTH1-5-5.1',
    topicNumber: '5.1.2',
    topic: 'Eliminating variable by equating coefficients',
    topicName: 'Eliminating variable by equating coefficients',
    parentTopicName: 'Simultaneous Linear Equations & Elimination Method',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Interchanged Coefficients Shortcut',
    text: 'If \\(15x + 17y = 21\\) and \\(17x + 15y = 11\\), what is the value of \\(x + y\\)?',
    options: [
      { text: '\\(1\\)', isCorrect: true },
      { text: '\\(2\\)', isCorrect: false },
      { text: '\\(-1\\)', isCorrect: false },
      { text: '\\(0\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Add both equations: \\((15 + 17)x + (17 + 15)y = 21 + 11\\).\n2. \\(32x + 32y = 32\\).\n3. Divide by 32: \\(x + y = 1\\).'
  },

  // --- Subtopic 5.2.1: Substitution method [MH-9-MTH1-5-5.2.1] ---
  {
    questionCode: 'MH-9-MTH1-5-5.2.1-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.2.1',
    parentTopicCode: 'MH-9-MTH1-5-5.2',
    topicNumber: '5.2.1',
    topic: 'Expressing one variable in terms of other and substituting',
    topicName: 'Substitution method for simultaneous equations',
    parentTopicName: 'Substitution Method for Simultaneous Equations',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Substitution Method Step',
    text: 'In solving \\(2x + y = 7\\) and \\(3x + 2y = 12\\) by substitution, if \\(y\\) is expressed in terms of \\(x\\) from the first equation, what is the resulting equation in \\(x\\)?',
    options: [
      { text: '\\(3x + 2(7 - 2x) = 12\\)', isCorrect: true },
      { text: '\\(3x + 2(2x - 7) = 12\\)', isCorrect: false },
      { text: '\\(3x + (7 - 2x) = 12\\)', isCorrect: false },
      { text: '\\(2x + 2(7 - 3x) = 12\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. From equation 1: \\(2x + y = 7 \\implies y = 7 - 2x\\).\n2. Substitute \\(y = 7 - 2x\\) into equation 2: \\(3x + 2(7 - 2x) = 12\\).\n3. Solving this linear equation in one variable yields \\(x\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.2.1-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.2.1',
    parentTopicCode: 'MH-9-MTH1-5-5.2',
    topicNumber: '5.2.1',
    topic: 'Expressing one variable in terms of other and substituting',
    topicName: 'Substitution method for simultaneous equations',
    parentTopicName: 'Substitution Method for Simultaneous Equations',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Apply',
    conceptTag: 'Solve by Substitution',
    text: 'Solve by substitution: \\(x = 2y\\) and \\(3x + 4y = 20\\). The value of \\(y\\) is:',
    options: [
      { text: '\\(2\\)', isCorrect: true },
      { text: '\\(4\\)', isCorrect: false },
      { text: '\\(1\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Substitute \\(x = 2y\\) directly into \\(3x + 4y = 20\\):\n   \\(3(2y) + 4y = 20\\)\n2. \\(6y + 4y = 20 \\implies 10y = 20\\).\n3. \\(y = \\frac{20}{10} = 2\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.2.1-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.2.1',
    parentTopicCode: 'MH-9-MTH1-5-5.2',
    topicNumber: '5.2.1',
    topic: 'Expressing one variable in terms of other and substituting',
    topicName: 'Substitution method for simultaneous equations',
    parentTopicName: 'Substitution Method for Simultaneous Equations',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Full Solution Pair',
    text: 'Find the solution pair \\((x, y)\\) for the system \\(x - 2y = -1\\) and \\(2x - y = 7\\):',
    options: [
      { text: '\\((5, 3)\\)', isCorrect: true },
      { text: '\\((3, 5)\\)', isCorrect: false },
      { text: '\\((1, 1)\\)', isCorrect: false },
      { text: '\\((7, 4)\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. From first equation: \\(x = 2y - 1\\).\n2. Substitute into second equation: \\(2(2y - 1) - y = 7 \\implies 4y - 2 - y = 7 \\implies 3y = 9 \\implies y = 3\\).\n3. Then \\(x = 2(3) - 1 = 5\\). Solution is \\((5, 3)\\).'
  },

  // --- Subtopic 5.3.1: Two-digit reversal problems [MH-9-MTH1-5-5.3.1] ---
  {
    questionCode: 'MH-9-MTH1-5-5.3.1-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.3.1',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.1',
    topic: 'Two-digit reversal problems',
    topicName: 'Two-digit reversal problems',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Two Digit Number Algebraic Form',
    text: 'If \\(t\\) is the tens digit and \\(u\\) is the units digit of a two-digit number, what is the value of the number formed by reversing its digits?',
    options: [
      { text: '\\(10u + t\\)', isCorrect: true },
      { text: '\\(10t + u\\)', isCorrect: false },
      { text: '\\(u + t\\)', isCorrect: false },
      { text: '\\(ut\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The original number with tens digit \\(t\\) and units digit \\(u\\) is \\(10t + u\\).\n2. When digits are reversed, \\(u\\) becomes the tens digit and \\(t\\) becomes the units digit.\n3. Hence the reversed number is \\(10u + t\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.1-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.3.1',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.1',
    topic: 'Two-digit reversal problems',
    topicName: 'Two-digit reversal problems',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Find Two Digit Number',
    text: 'The sum of the digits of a two-digit number is \\(9\\). If \\(27\\) is added to the number, its digits interchange. What is the original number?',
    options: [
      { text: '\\(36\\)', isCorrect: true },
      { text: '\\(63\\)', isCorrect: false },
      { text: '\\(27\\)', isCorrect: false },
      { text: '\\(45\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let tens digit be \\(x\\) and units digit be \\(y\\). Sum of digits: \\(x + y = 9\\).\n2. Original number = \\(10x + y\\). Reversed number = \\(10y + x\\).\n3. Given: \\((10x + y) + 27 = 10y + x \\implies 9y - 9x = 27 \\implies y - x = 3\\).\n4. Adding \\(x + y = 9\\) and \\(y - x = 3\\) gives \\(2y = 12 \\implies y = 6\\), so \\(x = 3\\).\n5. Original number is \\(36\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.1-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.3.1',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.1',
    topic: 'Two-digit reversal problems',
    topicName: 'Two-digit reversal problems',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Sum of Number and Reversal',
    text: 'The sum of a two-digit number and the number obtained by reversing its digits is always divisible by:',
    options: [
      { text: '\\(11\\)', isCorrect: true },
      { text: '\\(9\\)', isCorrect: false },
      { text: '\\(7\\)', isCorrect: false },
      { text: '\\(13\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let the number be \\(10x + y\\). Reversed number is \\(10y + x\\).\n2. Sum: \\((10x + y) + (10y + x) = 11x + 11y = 11(x + y)\\).\n3. Since \\(11\\) is a factor, the sum is always divisible by 11.'
  },

  // --- Subtopic 5.3.2: Numerator and denominator modifications [MH-9-MTH1-5-5.3.2] ---
  {
    questionCode: 'MH-9-MTH1-5-5.3.2-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.3.2',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.2',
    topic: 'Numerator and denominator modifications',
    topicName: 'Numerator and denominator modifications',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Fraction Modification Problem',
    text: 'A fraction becomes \\(\\frac{1}{2}\\) if \\(1\\) is subtracted from the numerator and \\(1\\) is added to the denominator. If the denominator is \\(4\\) more than the numerator, find the original fraction:',
    options: [
      { text: '\\(\\frac{7}{11}\\)', isCorrect: true },
      { text: '\\(\\frac{5}{9}\\)', isCorrect: false },
      { text: '\\(\\frac{3}{7}\\)', isCorrect: false },
      { text: '\\(\\frac{4}{8}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let the fraction be \\(\\frac{x}{y}\\). Given \\(y = x + 4\\).\n2. When 1 is subtracted from numerator and 1 added to denominator:\n   \\(\\frac{x - 1}{y + 1} = \\frac{1}{2} \\implies 2(x - 1) = y + 1\\).\n3. Substitute \\(y = x + 4\\): \\(2x - 2 = (x + 4) + 1 \\implies 2x - 2 = x + 5 \\implies x = 7\\).\n4. Then \\(y = 7 + 4 = 11\\). The original fraction is \\(\\frac{7}{11}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.2-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.3.2',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.2',
    topic: 'Numerator and denominator modifications',
    topicName: 'Numerator and denominator modifications',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Fraction Dual Conditions',
    text: 'If \\(2\\) is added to both the numerator and the denominator of a fraction, it becomes \\(\\frac{9}{11}\\). If \\(3\\) is added to both, it becomes \\(\\frac{5}{6}\\). Find the fraction:',
    options: [
      { text: '\\(\\frac{7}{9}\\)', isCorrect: true },
      { text: '\\(\\frac{5}{7}\\)', isCorrect: false },
      { text: '\\(\\frac{9}{11}\\)', isCorrect: false },
      { text: '\\(\\frac{3}{5}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let fraction be \\(\\frac{x}{y}\\).\n2. Condition 1: \\(\\frac{x + 2}{y + 2} = \\frac{9}{11} \\implies 11x + 22 = 9y + 18 \\implies 11x - 9y = -4\\).\n3. Condition 2: \\(\\frac{x + 3}{y + 3} = \\frac{5}{6} \\implies 6x + 18 = 5y + 15 \\implies 6x - 5y = -3\\).\n4. Solving this linear system gives \\(x = 7\\) and \\(y = 9\\).\n5. The fraction is \\(\\frac{7}{9}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.2-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.3.2',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.2',
    topic: 'Numerator and denominator modifications',
    topicName: 'Numerator and denominator modifications',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'Fraction Denominator Multiples',
    text: 'The denominator of a fraction is \\(4\\) more than twice its numerator. Denominator becomes \\(12\\) times the numerator if both numerator and denominator are reduced by \\(6\\). Find the fraction:',
    options: [
      { text: '\\(\\frac{7}{18}\\)', isCorrect: true },
      { text: '\\(\\frac{5}{14}\\)', isCorrect: false },
      { text: '\\(\\frac{9}{22}\\)', isCorrect: false },
      { text: '\\(\\frac{3}{10}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let numerator be \\(x\\) and denominator be \\(y\\). Given \\(y = 2x + 4\\).\n2. Reduced by 6: \\(y - 6 = 12(x - 6)\\).\n3. Substitute \\(y = 2x + 4\\): \\((2x + 4) - 6 = 12x - 72 \\implies 2x - 2 = 12x - 72\\).\n4. \\(10x = 70 \\implies x = 7\\), so \\(y = 2(7) + 4 = 18\\).\n5. The fraction is \\(\\frac{7}{18}\\).'
  },

  // --- Subtopic 5.3.3: Speed and time variations [MH-9-MTH1-5-5.3.3] ---
  {
    questionCode: 'MH-9-MTH1-5-5.3.3-OSC-001',
    topicCode: 'MH-9-MTH1-5-5.3.3',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.3',
    topic: 'Speed and time variations',
    topicName: 'Speed and time variations',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Upstream Downstream Speeds',
    text: 'If the speed of a boat in still water is \\(x\\text{ km/h}\\) and the speed of the water current is \\(y\\text{ km/h}\\) (where \\(x > y\\)), then the speeds downstream and upstream are respectively:',
    options: [
      { text: '\\((x + y)\\text{ km/h}\\) and \\((x - y)\\text{ km/h}\\)', isCorrect: true },
      { text: '\\((x - y)\\text{ km/h}\\) and \\((x + y)\\text{ km/h}\\)', isCorrect: false },
      { text: '\\(xy\\text{ km/h}\\) and \\(\\frac{x}{y}\\text{ km/h}\\)', isCorrect: false },
      { text: '\\((2x + y)\\text{ km/h}\\) and \\((x - 2y)\\text{ km/h}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Travelling downstream (with the flow), the water current aids the boat: Speed \\(= x + y\\).\n2. Travelling upstream (against the flow), the water current opposes the boat: Speed \\(= x - y\\).\n3. Hence speeds are \\((x + y)\\) and \\((x - y)\\) km/h respectively.'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.3-OSC-002',
    topicCode: 'MH-9-MTH1-5-5.3.3',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.3',
    topic: 'Speed and time variations',
    topicName: 'Speed and time variations',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Boat and Stream Problem',
    text: 'A boat goes \\(30\\text{ km}\\) upstream and \\(44\\text{ km}\\) downstream in \\(10\\text{ hours}\\). In \\(13\\text{ hours}\\), it can go \\(40\\text{ km}\\) upstream and \\(55\\text{ km}\\) downstream. Determine the speed of the boat in still water:',
    options: [
      { text: '\\(8\\text{ km/h}\\)', isCorrect: true },
      { text: '\\(6\\text{ km/h}\\)', isCorrect: false },
      { text: '\\(10\\text{ km/h}\\)', isCorrect: false },
      { text: '\\(12\\text{ km/h}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let upstream speed be \\(u = x - y\\) and downstream speed be \\(v = x + y\\).\n2. Equations: \\(\\frac{30}{u} + \\frac{44}{v} = 10\\) and \\(\\frac{40}{u} + \\frac{55}{v} = 13\\).\n3. Solving gives \\(u = 5\\) and \\(v = 11\\).\n4. Then \\(x - y = 5\\) and \\(x + y = 11 \\implies 2x = 16 \\implies x = 8\\text{ km/h}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-5-5.3.3-OSC-003',
    topicCode: 'MH-9-MTH1-5-5.3.3',
    parentTopicCode: 'MH-9-MTH1-5-5.3',
    topicNumber: '5.3.3',
    topic: 'Speed and time variations',
    topicName: 'Speed and time variations',
    parentTopicName: 'Word Problems on Ages, Numbers, Speed-Distance & Fractions',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 5,
    chapter: 'Linear Equations in Two Variables',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Two Cars Highway Problem',
    text: 'Two places A and B are \\(100\\text{ km}\\) apart. Two cars start from A and B at the same time. If they travel in the same direction, they meet in \\(5\\text{ hours}\\). If they travel towards each other, they meet in \\(1\\text{ hour}\\). What are their speeds?',
    options: [
      { text: '\\(60\\text{ km/h}\\) and \\(40\\text{ km/h}\\)', isCorrect: true },
      { text: '\\(70\\text{ km/h}\\) and \\(30\\text{ km/h}\\)', isCorrect: false },
      { text: '\\(50\\text{ km/h}\\) and \\(50\\text{ km/h}\\)', isCorrect: false },
      { text: '\\(65\\text{ km/h}\\) and \\(35\\text{ km/h}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let the speeds be \\(x\\) and \\(y\\) km/h (with \\(x > y\\)).\n2. In same direction, relative speed is \\(x - y\\): \\(5(x - y) = 100 \\implies x - y = 20\\).\n3. Towards each other, relative speed is \\(x + y\\): \\(1(x + y) = 100 \\implies x + y = 100\\).\n4. Adding equations: \\(2x = 120 \\implies x = 60\\text{ km/h}\\), and \\(y = 40\\text{ km/h}\\).'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Chapter 5 Linear Equations ===`);
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
  console.log('All Chapter 5 questions passed strict validation perfectly!');

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch5_linear_equations');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore across Chapter 5 Linear Equations!`);
}

main().catch(console.error);
