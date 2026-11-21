// scripts/mh9_mth1_ch1_topic3_data.js
// 68 Questions for Topic 1.3: Equal Sets, Subsets & Universal Set
// Subtopics: 1.3.1 (22 Qs), 1.3.2 (24 Qs), 1.3.3 (22 Qs)

function makeQ(data) {
  const letters = ['A', 'B', 'C', 'D'];
  const correctIdx = data.options.findIndex(o => o.isCorrect === true);
  if (correctIdx === -1) throw new Error(`Question ${data.questionCode} has no correct option`);
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
    parentTopicCode: 'MH-9-MTH1-1-1.3',
    parentTopicName: 'Equal Sets, Subsets & Universal Set',
    type: 'OSC',
    marks: 4,
    timesUsed: 0,
    usedInClassroomTest: false,
    requiresFigure: false,
    createdAt: new Date(),
    updatedAt: new Date()
  };
}

const topic3Questions = [];

// =========================================================================
// Subtopic 1.3.1: Equal sets condition (22 questions: 11 Exam, 5 Practice, 6 Foundation)
// =========================================================================
const s131 = [
  // Exam (11)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Equal Sets Definition',
    text: 'Two sets \\(A\\) and \\(B\\) are said to be equal (written \\(A = B\\)) if and only if:',
    opts: [
      { text: 'Every element of \\(A\\) is in \\(B\\) and every element of \\(B\\) is in \\(A\\)', isCorrect: true },
      { text: 'They have the same number of elements only', isCorrect: false },
      { text: 'They are both infinite sets', isCorrect: false },
      { text: 'Their union is an empty set', isCorrect: false }
    ],
    sol: '1. By definition, two sets are equal if they contain exactly the same elements.\n2. In symbolic logic, \\(A = B\\) if \\(A \\subseteq B\\) and \\(B \\subseteq A\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Order in Equal Sets',
    text: 'Are the sets \\(A = \\{1, 3, 5\\}\\) and \\(B = \\{5, 1, 3\\}\\) equal?',
    opts: [
      { text: 'Yes, because the order of elements in a set does not matter', isCorrect: true },
      { text: 'No, because the order of elements is different', isCorrect: false },
      { text: 'They are disjoint sets', isCorrect: false },
      { text: 'Cannot be determined without a universal set', isCorrect: false }
    ],
    sol: '1. Both sets contain the exact same elements: 1, 3, and 5.\n2. In set theory, the sequence of listing elements does not change the set.\n3. Hence \\(A = B\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Repetition in Equal Sets',
    text: 'If \\(P = \\{2, 4, 6\\}\\) and \\(Q = \\{2, 2, 4, 6, 6\\}\\), then:',
    opts: [
      { text: '\\(P = Q\\), because repetition of elements does not alter a set', isCorrect: true },
      { text: '\\(P \\neq Q\\), because \\(n(Q) = 5\\) while \\(n(P) = 3\\)', isCorrect: false },
      { text: '\\(P \\subset Q\\)', isCorrect: false },
      { text: '\\(Q\\) is an invalid set', isCorrect: false }
    ],
    sol: '1. Repeating an element does not create a new element.\n2. Set \\(Q\\) has elements \\{2, 4, 6\\}, which are identical to \\(P\\).\n3. Therefore \\(P = Q\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Letters of LISTEN and SILENT',
    text: 'Let \\(X\\) be the set of letters in "LISTEN" and \\(Y\\) be the set of letters in "SILENT". Which relation holds?',
    opts: [
      { text: '\\(X = Y\\)', isCorrect: true },
      { text: '\\(X \\neq Y\\)', isCorrect: false },
      { text: '\\(X \\cap Y = \\emptyset\\)', isCorrect: false },
      { text: '\\(n(X) \\neq n(Y)\\)', isCorrect: false }
    ],
    sol: '1. \\(X = \\{L, I, S, T, E, N\\}\\).\n2. \\(Y = \\{S, I, L, E, N, T\\}\\).\n3. All letters are identical, so \\(X = Y\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Equation Root Sets Equal',
    text: 'Let \\(A = \\{x \\mid x \\in \\mathbb{I}, x^2 = 9\\}\\) and \\(B = \\{-3, 3\\}\\). Are \\(A\\) and \\(B\\) equal?',
    opts: [
      { text: 'Yes, because the integer solutions of \\(x^2 = 9\\) are strictly \\(-3\\) and \\(3\\)', isCorrect: true },
      { text: 'No, because \\(A\\) contains only positive roots', isCorrect: false },
      { text: 'No, because \\(A\\) is in rule form and \\(B\\) is in roster form', isCorrect: false },
      { text: '\\(A\\) is an empty set', isCorrect: false }
    ],
    sol: '1. \\(x^2 = 9 \\implies x = 3\\) or \\(x = -3\\).\n2. Both are integers, so \\(A = \\{-3, 3\\}\\).\n3. Since \\(B = \\{-3, 3\\}\\), \\(A = B\\).' },
  { v: 'exam', d: 'medium', b: 'Analyze', tag: 'Natural vs Whole Distinction',
    text: 'Let \\(A = \\{x \\mid x \\in \\mathbb{N}, x < 3\\}\\) and \\(B = \\{x \\mid x \\in \\mathbb{W}, x < 3\\}\\). Are \\(A\\) and \\(B\\) equal sets?',
    opts: [
      { text: 'No, because \\(B = \\{0, 1, 2\\}\\) contains \\(0\\) while \\(A = \\{1, 2\\}\\) does not', isCorrect: true },
      { text: 'Yes, because both represent numbers less than 3', isCorrect: false },
      { text: 'Yes, because \\(\\mathbb{N} = \\mathbb{W}\\)', isCorrect: false },
      { text: 'Both are empty sets', isCorrect: false }
    ],
    sol: '1. Natural numbers less than 3 are \\(A = \\{1, 2\\}\\).\n2. Whole numbers less than 3 are \\(B = \\{0, 1, 2\\}\\).\n3. Since \\(0 \\in B\\) but \\(0 \\notin A\\), \\(A \\neq B\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Even Prime vs Linear Root',
    text: 'If \\(A = \\{x \\mid x \\text{ is an even prime number}\\}\\) and \\(B = \\{x \\mid 7x - 1 = 13\\}\\), then:',
    opts: [
      { text: '\\(A = B = \\{2\\}\\)', isCorrect: true },
      { text: '\\(A \\neq B\\)', isCorrect: false },
      { text: '\\(B\\) is empty', isCorrect: false },
      { text: '\\(A\\) has 2 elements', isCorrect: false }
    ],
    sol: '1. The only even prime is 2, so \\(A = \\{2\\}\\).\n2. \\(7x - 1 = 13 \\implies 7x = 14 \\implies x = 2\\), so \\(B = \\{2\\}\\).\n3. Both sets have identical element \\(\\{2\\}\\), so \\(A = B\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Cubic Equation vs Integer Set',
    text: 'Let \\(S = \\{x \\mid x \\in \\mathbb{R}, x^3 - x = 0\\}\\) and \\(T = \\{-1, 0, 1\\}\\). Which statement is true?',
    opts: [
      { text: '\\(S = T\\)', isCorrect: true },
      { text: '\\(S \\subset T\\)', isCorrect: false },
      { text: '\\(S \\neq T\\) because \\(0\\) is excluded', isCorrect: false },
      { text: '\\(S\\) has only positive roots', isCorrect: false }
    ],
    sol: '1. \\(x^3 - x = x(x^2 - 1) = x(x - 1)(x + 1) = 0\\).\n2. The roots are \\(x = 0, 1, -1\\).\n3. In roster form, \\(S = \\{-1, 0, 1\\}\\), identical to \\(T\\). Thus \\(S = T\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Equal Sets with Unknown Parameter',
    text: 'If \\(A = \\{2, a, 7\\}\\) and \\(B = \\{7, 5, 2\\}\\) are equal sets, what is the value of \\(a\\)?',
    opts: [
      { text: '\\(a = 5\\)', isCorrect: true },
      { text: '\\(a = 2\\)', isCorrect: false },
      { text: '\\(a = 7\\)', isCorrect: false },
      { text: '\\(a = 0\\)', isCorrect: false }
    ],
    sol: '1. For \\(A = B\\), every element of \\(B\\) must be present in \\(A\\).\n2. Elements 2 and 7 match. The remaining element in \\(B\\) is 5.\n3. Therefore \\(a = 5\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Equivalent vs Equal Sets',
    text: 'If two sets \\(A\\) and \\(B\\) have \\(n(A) = n(B)\\), are they necessarily equal sets?',
    opts: [
      { text: 'Not necessarily; they are equivalent sets, but equal only if elements are identical', isCorrect: true },
      { text: 'Yes, equal cardinality always implies equal sets', isCorrect: false },
      { text: 'No, they can never be equal', isCorrect: false },
      { text: 'Yes, if both are finite', isCorrect: false }
    ],
    sol: '1. Equal cardinality \\(n(A) = n(B)\\) defines equivalent sets (e.g. \\(\\{1, 2\\}\\) and \\(\\{a, b\\}\\)).\n2. Equal sets strictly require the actual elements to be identical.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Letters of TEETH and SET',
    text: 'Let \\(A = \\{x \\mid x \\text{ is a letter in \"TEETH\"}\\}\\) and \\(B = \\{T, E, H\\}\\). Then:',
    opts: [
      { text: '\\(A = B\\)', isCorrect: true },
      { text: '\\(A \\neq B\\)', isCorrect: false },
      { text: '\\(n(A) = 5\\)', isCorrect: false },
      { text: '\\(B \\subset A\\)', isCorrect: false }
    ],
    sol: '1. Distinct letters of "TEETH" are T, E, H.\n2. In roster form, \\(A = \\{T, E, H\\}\\).\n3. Since \\(B = \\{T, E, H\\}\\), \\(A = B\\).' },

  // Practice (5)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Symbol for Equal Sets',
    text: 'Which mathematical symbol is used to denote that set \\(A\\) and set \\(B\\) are equal?',
    opts: [{ text: '\\(A = B\\)', isCorrect: true }, { text: '\\(A \\equiv B\\)', isCorrect: false }, { text: '\\(A \\approx B\\)', isCorrect: false }, { text: '\\(A \\subseteq B\\)', isCorrect: false }],
    sol: '1. The standard equality sign \\(=\\) is used to denote equal sets: \\(A = B\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Odd Prime Less than 6',
    text: 'Let \\(A = \\{x \\mid x \\text{ is an odd prime}, x < 6\\}\\) and \\(B = \\{3, 5\\}\\). Are \\(A\\) and \\(B\\) equal?',
    opts: [{ text: 'Yes, \\(A = B\\)', isCorrect: true }, { text: 'No, because \\(A\\) also includes 1', isCorrect: false }, { text: 'No, because \\(A\\) also includes 2', isCorrect: false }, { text: 'Cannot be determined', isCorrect: false }],
    sol: '1. Prime numbers less than 6 are 2, 3, 5.\n2. The odd primes among them are 3 and 5 (2 is even, 1 is not prime).\n3. Hence \\(A = \\{3, 5\\} = B\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Two Parameters Equal Sets',
    text: 'If \\(\\{x, 4\\} = \\{4, 9\\}\\), what is the value of \\(x\\)?',
    opts: [{ text: '\\(9\\)', isCorrect: true }, { text: '\\(4\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(13\\)', isCorrect: false }],
    sol: '1. Both sets must contain the exact same elements.\n2. Element 4 is common; the remaining element must match: \\(x = 9\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Absolute Value Equal Sets',
    text: 'Let \\(P = \\{x \\mid x \\in \\mathbb{I}, |x| \\le 1\\}\\) and \\(Q = \\{-1, 0, 1\\}\\). Then:',
    opts: [{ text: '\\(P = Q\\)', isCorrect: true }, { text: '\\(P \\neq Q\\)', isCorrect: false }, { text: '\\(P = \\{1\\}\\)', isCorrect: false }, { text: '\\(Q \\subset P\\)', isCorrect: false }],
    sol: '1. \\(|x| \\le 1\\) for integers means \\(-1 \\le x \\le 1\\).\n2. The integers are \\(-1, 0, 1\\).\n3. Thus \\(P = \\{-1, 0, 1\\} = Q\\).' },
  { v: 'practice', d: 'easy', b: 'Understand', tag: 'Empty Sets are Equal',
    text: 'Are two empty sets \\(\\emptyset_1\\) and \\(\\emptyset_2\\) always equal?',
    opts: [{ text: 'Yes, because every empty set contains no elements, so all empty sets are identical', isCorrect: true }, { text: 'No, because their names differ', isCorrect: false }, { text: 'Only if they are defined on the same universe', isCorrect: false }, { text: 'Never equal', isCorrect: false }],
    sol: '1. An empty set has no elements.\n2. By the axiom of extensionality, there is only one unique empty set in set theory. Hence \\(\\emptyset_1 = \\emptyset_2\\).' },

  // Foundation (6)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Equal Sets Concept',
    text: 'When every element of set \\(A\\) is an element of set \\(B\\) and vice-versa, then:',
    opts: [{ text: '\\(A = B\\)', isCorrect: true }, { text: '\\(A \\neq B\\)', isCorrect: false }, { text: '\\(A \\cap B = \\emptyset\\)', isCorrect: false }, { text: '\\(n(A) = 0\\)', isCorrect: false }],
    sol: '1. This is the fundamental definition of equal sets.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Elements Order Invariance',
    text: 'Does changing the order of elements inside set brackets change the set?',
    opts: [{ text: 'No, order of elements does not matter in sets', isCorrect: true }, { text: 'Yes, it forms an ordered pair', isCorrect: false }, { text: 'Yes, it changes cardinality', isCorrect: false }, { text: 'Only for numbers', isCorrect: false }],
    sol: '1. A set is an unordered collection. Order of elements has no mathematical significance.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Duplicate Elements Rule',
    text: 'In writing a set, is it customary to repeat identical elements?',
    opts: [{ text: 'No, elements are generally written only once', isCorrect: true }, { text: 'Yes, every element must be written twice', isCorrect: false }, { text: 'Yes, to increase cardinality', isCorrect: false }, { text: 'Mandatory in rule form', isCorrect: false }],
    sol: '1. By mathematical convention, repeated elements are redundant and written only once.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Check Simple Equal Sets',
    text: 'Are \\(\\{a, b, c\\}\\) and \\(\\{c, a, b\\}\\) equal?',
    opts: [{ text: 'Yes, they are equal sets', isCorrect: true }, { text: 'No, they are different', isCorrect: false }, { text: 'They are disjoint', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
    sol: '1. Both sets contain elements \\(a, b, c\\). Order does not matter, so they are equal.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Whole Numbers vs Digits',
    text: 'If \\(A = \\{0, 1, 2\\}\\) and \\(B = \\{1, 2\\}\\), then:',
    opts: [{ text: '\\(A \\neq B\\) because \\(0 \\in A\\) but \\(0 \\notin B\\)', isCorrect: true }, { text: '\\(A = B\\)', isCorrect: false }, { text: '\\(B \\supset A\\)', isCorrect: false }, { text: '\\(A\\) is an empty set', isCorrect: false }],
    sol: '1. \\(A\\) contains 0 while \\(B\\) does not. Since they do not have identical elements, \\(A \\neq B\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Not Equal Symbol',
    text: 'If two sets \\(A\\) and \\(B\\) do not contain identical elements, we write:',
    opts: [{ text: '\\(A \\neq B\\)', isCorrect: true }, { text: '\\(A = B\\)', isCorrect: false }, { text: '\\(A \\le B\\)', isCorrect: false }, { text: '\\(A < B\\)', isCorrect: false }],
    sol: '1. Inequality of sets is denoted by \\(A \\neq B\\).' }
];

s131.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic3Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.3.1-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.3.1',
    topicNumber: '1.3.1',
    topic: 'Equal sets condition',
    topicName: 'Equal sets condition',
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

// =========================================================================
// Subtopic 1.3.2: Subset definition (A ⊆ B) (24 questions: 12 Exam, 6 Practice, 6 Foundation)
// =========================================================================
const s132 = [
  // Exam (12)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Subset Definition',
    text: 'If every element of set \\(A\\) is also an element of set \\(B\\), then \\(A\\) is called a:',
    opts: [
      { text: 'Subset of \\(B\\), written \\(A \\subseteq B\\)', isCorrect: true },
      { text: 'Superset of \\(A\\)', isCorrect: false },
      { text: 'Universal set', isCorrect: false },
      { text: 'Disjoint set', isCorrect: false }
    ],
    sol: '1. By mathematical definition, \\(A \\subseteq B\\) means for every \\(x \\in A\\), \\(x \\in B\\).\n2. \\(A\\) is called a subset of \\(B\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Empty Set Subset Property',
    text: 'Which fundamental theorem regarding subsets is ALWAYS true for any set \\(A\\)?',
    opts: [
      { text: '\\(\\emptyset \\subseteq A\\) (The empty set is a subset of every set)', isCorrect: true },
      { text: '\\(A \\subseteq \\emptyset\\)', isCorrect: false },
      { text: '\\(A \\cap \\emptyset = A\\)', isCorrect: false },
      { text: '\\(\\emptyset \\in A\\) always', isCorrect: false }
    ],
    sol: '1. Since the empty set contains no elements, it trivially satisfies the condition that all its elements belong to \\(A\\).\n2. Thus \\(\\emptyset \\subseteq A\\) for every set \\(A\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Self Subset Property',
    text: 'For any set \\(A\\), which of the following relations is universally true?',
    opts: [
      { text: '\\(A \\subseteq A\\) (Every set is a subset of itself)', isCorrect: true },
      { text: '\\(A \\subset A\\)', isCorrect: false },
      { text: '\\(A \\cap A = \\emptyset\\)', isCorrect: false },
      { text: '\\(A \\cup A = \\emptyset\\)', isCorrect: false }
    ],
    sol: '1. Every element of \\(A\\) belongs to \\(A\\).\n2. Hence every set is an improper subset of itself: \\(A \\subseteq A\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Number of Subsets Formula',
    text: 'If a finite set \\(A\\) has \\(n\\) elements, the total number of subsets of \\(A\\) is given by the formula:',
    opts: [
      { text: '\\(2^n\\)', isCorrect: true },
      { text: '\\(n^2\\)', isCorrect: false },
      { text: '\\(2n\\)', isCorrect: false },
      { text: '\\(n!\\)', isCorrect: false }
    ],
    sol: '1. For each of the \\(n\\) elements, there are 2 choices: either include it in a subset or exclude it.\n2. By multiplication principle: \\(2 \\times 2 \\times \\dots \\times 2 = 2^n\\) total subsets.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Calculate Number of Subsets 3 Elements',
    text: 'How many subsets does the set \\(S = \\{1, 2, 3\\}\\) have in total?',
    opts: [
      { text: '\\(8\\)', isCorrect: true },
      { text: '\\(6\\)', isCorrect: false },
      { text: '\\(7\\)', isCorrect: false },
      { text: '\\(9\\)', isCorrect: false }
    ],
    sol: '1. Here \\(n(S) = 3\\).\n2. Total number of subsets \\(= 2^n = 2^3 = 8\\).\n3. The subsets are: \\(\\emptyset, \\{1\\}, \\{2\\}, \\{3\\}, \\{1, 2\\}, \\{1, 3\\}, \\{2, 3\\}, \\{1, 2, 3\\}\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Proper Subsets Formula',
    text: 'The number of proper subsets of a set having \\(4\\) elements is:',
    opts: [
      { text: '\\(15\\)', isCorrect: true },
      { text: '\\(16\\)', isCorrect: false },
      { text: '\\(14\\)', isCorrect: false },
      { text: '\\(8\\)', isCorrect: false }
    ],
    sol: '1. Total subsets \\(= 2^4 = 16\\).\n2. A proper subset is any subset strictly smaller than the set itself (excluding the set itself).\n3. Number of proper subsets \\(= 2^n - 1 = 16 - 1 = 15\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Number Systems Subset Hierarchy',
    text: 'Which of the following subset chains correctly depicts the hierarchy of number sets?',
    opts: [
      { text: '\\(\\mathbb{N} \\subset \\mathbb{W} \\subset \\mathbb{I} \\subset \\mathbb{Q} \\subset \\mathbb{R}\\)', isCorrect: true },
      { text: '\\(\\mathbb{R} \\subset \\mathbb{Q} \\subset \\mathbb{I} \\subset \\mathbb{W} \\subset \\mathbb{N}\\)', isCorrect: false },
      { text: '\\(\\mathbb{W} \\subset \\mathbb{N} \\subset \\mathbb{I} \\subset \\mathbb{Q} \\subset \\mathbb{R}\\)', isCorrect: false },
      { text: '\\(\\mathbb{N} \\subset \\mathbb{I} \\subset \\mathbb{W} \\subset \\mathbb{R} \\subset \\mathbb{Q}\\)', isCorrect: false }
    ],
    sol: '1. Every natural number is a whole number (\\(\\mathbb{N} \\subset \\mathbb{W}\\)).\n2. Every whole number is an integer (\\(\\mathbb{W} \\subset \\mathbb{I}\\)).\n3. Every integer is a rational number (\\(\\mathbb{I} \\subset \\mathbb{Q}\\)).\n4. Every rational number is a real number (\\(\\mathbb{Q} \\subset \\mathbb{R}\\)).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Verify Subset True Statement',
    text: 'If \\(A = \\{2, 4, 6\\}\\) and \\(B = \\{1, 2, 3, 4, 5, 6, 7\\}\\), which statement is correct?',
    opts: [
      { text: '\\(A \\subseteq B\\)', isCorrect: true },
      { text: '\\(B \\subseteq A\\)', isCorrect: false },
      { text: '\\(A = B\\)', isCorrect: false },
      { text: '\\(A \\cap B = \\emptyset\\)', isCorrect: false }
    ],
    sol: '1. The elements of \\(A\\) are 2, 4, 6.\n2. All three elements 2, 4, 6 belong to set \\(B\\).\n3. Hence \\(A \\subseteq B\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Element Belonging vs Subset Notation',
    text: 'If \\(A = \\{1, 2, \\{3, 4\\}, 5\\}\\), which of the following statements is INCORRECT?',
    opts: [
      { text: '\\(\\{3, 4\\} \\subseteq A\\)', isCorrect: true },
      { text: '\\(\\{3, 4\\} \\in A\\)', isCorrect: false },
      { text: '\\(\\{\\{3, 4\\}\\} \\subseteq A\\)', isCorrect: false },
      { text: '\\(\\{1, 2\\} \\subseteq A\\)', isCorrect: false }
    ],
    sol: '1. The set \\(\\{3, 4\\}\\) is an ELEMENT of \\(A\\), so \\(\\{3, 4\\} \\in A\\) is correct.\n2. To be a subset, it must be enclosed in another set bracket: \\(\\{\\{3, 4\\}\\} \\subseteq A\\).\n3. Therefore, \\(\\{3, 4\\} \\subseteq A\\) is mathematically incorrect.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Subsets of Singleton',
    text: 'How many subsets does a singleton set \\(\\{x\\}\\) possess?',
    opts: [
      { text: '\\(2\\) (namely \\(\\emptyset\\) and \\(\\{x\\}\\))', isCorrect: true },
      { text: '\\(1\\)', isCorrect: false },
      { text: '\\(0\\)', isCorrect: false },
      { text: '\\(4\\)', isCorrect: false }
    ],
    sol: '1. \\(n = 1\\), so total subsets \\(= 2^1 = 2\\).\n2. They are \\(\\emptyset\\) and \\(\\{x\\}\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Transitivity of Subsets',
    text: 'If \\(A \\subseteq B\\) and \\(B \\subseteq C\\), then which of the following MUST be true?',
    opts: [
      { text: '\\(A \\subseteq C\\) (Transitive property of subsets)', isCorrect: true },
      { text: '\\(C \\subseteq A\\)', isCorrect: false },
      { text: '\\(A = C\\)', isCorrect: false },
      { text: '\\(A \\cap C = \\emptyset\\)', isCorrect: false }
    ],
    sol: '1. If every element of \\(A\\) is in \\(B\\), and every element of \\(B\\) is in \\(C\\), then every element of \\(A\\) is in \\(C\\).\n2. Hence \\(A \\subseteq C\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Subsets of Empty Set',
    text: 'How many subsets does the empty set \\(\\emptyset\\) have?',
    opts: [
      { text: '\\(1\\) (only \\(\\emptyset\\) itself, since \\(2^0 = 1\\))', isCorrect: true },
      { text: '\\(0\\)', isCorrect: false },
      { text: '\\(2\\)', isCorrect: false },
      { text: 'Infinite', isCorrect: false }
    ],
    sol: '1. For the empty set, cardinality \\(n = 0\\).\n2. Total subsets \\(= 2^0 = 1\\).\n3. The sole subset is \\(\\emptyset\\) itself.' },

  // Practice (6)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Subset Symbol',
    text: 'The mathematical symbol \\(\\subseteq\\) stands for:',
    opts: [{ text: 'Is a subset of', isCorrect: true }, { text: 'Belongs to', isCorrect: false }, { text: 'Union of', isCorrect: false }, { text: 'Intersection of', isCorrect: false }],
    sol: '1. \\(\\subseteq\\) denotes the subset relation between two sets.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'List Subsets of Two Elements',
    text: 'Which of the following is the complete list of subsets of \\(A = \\{a, b\\}\\)?',
    opts: [{ text: '\\(\\emptyset, \\{a\\}, \\{b\\}, \\{a, b\\}\\)', isCorrect: true }, { text: '\\(\\{a\\}, \\{b\\}\\)', isCorrect: false }, { text: '\\(\\{a\\}, \\{b\\}, \\{a, b\\}\\)', isCorrect: false }, { text: '\\(\\{a, b\\}\\)', isCorrect: false }],
    sol: '1. \\(n = 2\\), so \\(2^2 = 4\\) subsets.\n2. Subsets are: \\(\\emptyset, \\{a\\}, \\{b\\}, \\{a, b\\}\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Calculate Subsets for 5 Elements',
    text: 'A set has 5 elements. What is the total number of its subsets?',
    opts: [{ text: '\\(32\\)', isCorrect: true }, { text: '\\(25\\)', isCorrect: false }, { text: '\\(10\\)', isCorrect: false }, { text: '\\(64\\)', isCorrect: false }],
    sol: '1. Number of subsets \\(= 2^5 = 32\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Antisymmetry of Subsets',
    text: 'If \\(A \\subseteq B\\) and \\(B \\subseteq A\\), what can be concluded?',
    opts: [{ text: '\\(A = B\\)', isCorrect: true }, { text: '\\(A \\neq B\\)', isCorrect: false }, { text: '\\(A \\cap B = \\emptyset\\)', isCorrect: false }, { text: '\\(A = \\emptyset\\)', isCorrect: false }],
    sol: '1. If every element of \\(A\\) is in \\(B\\) and vice-versa, both sets are identical: \\(A = B\\).' },
  { v: 'practice', d: 'easy', b: 'Understand', tag: 'Superset Concept',
    text: 'If \\(A \\subseteq B\\), then \\(B\\) is called the \\(\\text{__________}\\) of \\(A\\).',
    opts: [{ text: 'Superset', isCorrect: true }, { text: 'Subset', isCorrect: false }, { text: 'Power set', isCorrect: false }, { text: 'Sub-interval', isCorrect: false }],
    sol: '1. If \\(A\\) is a subset of \\(B\\), then \\(B\\) is a superset of \\(A\\), denoted \\(B \\supseteq A\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Find Not a Subset',
    text: 'If \\(P = \\{1, 2, 3\\}\\) and \\(Q = \\{2, 3, 4\\}\\), is \\(P \\subseteq Q\\)?',
    opts: [{ text: 'No, because \\(1 \\in P\\) but \\(1 \\notin Q\\)', isCorrect: true }, { text: 'Yes, because they share 2 and 3', isCorrect: false }, { text: 'Yes, because \\(n(P) = n(Q)\\)', isCorrect: false }, { text: 'Yes, because both are finite', isCorrect: false }],
    sol: '1. For \\(P \\subseteq Q\\), every element of \\(P\\) must be in \\(Q\\).\n2. Since \\(1 \\in P\\) but \\(1 \\notin Q\\), \\(P \\not\\subseteq Q\\).' },

  // Foundation (6)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Subset Meaning',
    text: 'When we say \\(A\\) is a subset of \\(B\\), it means:',
    opts: [{ text: 'All members of \\(A\\) are contained in \\(B\\)', isCorrect: true }, { text: 'Some members of \\(A\\) are in \\(B\\)', isCorrect: false }, { text: '\\(A\\) has more members than \\(B\\)', isCorrect: false }, { text: '\\(A\\) and \\(B\\) have no common members', isCorrect: false }],
    sol: '1. A subset contains only elements that also belong to the larger (or equal) set.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Empty Set is Subset of All',
    text: 'Is the empty set \\(\\emptyset\\) a subset of \\(\\{5, 10, 15\\}\\)?',
    opts: [{ text: 'Yes, \\(\\emptyset\\) is a subset of every set', isCorrect: true }, { text: 'No, because 0 is not in the set', isCorrect: false }, { text: 'Only if the set is infinite', isCorrect: false }, { text: 'No, \\(\\emptyset\\) has no relation to sets', isCorrect: false }],
    sol: '1. By mathematical theorem, the empty set is a subset of every set without exception.' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Every Set is Subset of Itself',
    text: 'Is it true that \\(\\{1, 2\\} \\subseteq \\{1, 2\\}\\)?',
    opts: [{ text: 'Yes, every set is a subset of itself', isCorrect: true }, { text: 'No, a set cannot be its own subset', isCorrect: false }, { text: 'Only in infinite sets', isCorrect: false }, { text: 'False', isCorrect: false }],
    sol: '1. Every set \\(A\\) satisfies \\(A \\subseteq A\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Count Subsets for 1 Element',
    text: 'A set has 1 element. How many subsets does it have?',
    opts: [{ text: '\\(2\\) (the empty set and the set itself)', isCorrect: true }, { text: '\\(1\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(3\\)', isCorrect: false }],
    sol: '1. \\(2^1 = 2\\) subsets.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Is 3 in Set or Subset',
    text: 'For the set \\(A = \\{3, 6, 9\\}\\), which expression correctly uses the subset symbol?',
    opts: [{ text: '\\(\\{3\\} \\subseteq A\\)', isCorrect: true }, { text: '\\(3 \\subseteq A\\)', isCorrect: false }, { text: '\\(\\{3\\} \\in A\\)', isCorrect: false }, { text: '\\(A \\subseteq \\{3\\}\\)', isCorrect: false }],
    sol: '1. 3 is an element (\\(3 \\in A\\)), while \\(\\{3\\}\\) is a set containing 3, so \\(\\{3\\} \\subseteq A\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Belongs to vs Subset',
    text: 'The symbol \\(\\in\\) is used between an \\(\\text{__________}\\) and a set, while \\(\\subseteq\\) is used between two \\(\\text{__________}\\).',
    opts: [{ text: 'element; sets', isCorrect: true }, { text: 'set; elements', isCorrect: false }, { text: 'number; variables', isCorrect: false }, { text: 'equation; expressions', isCorrect: false }],
    sol: '1. \\(\\in\\) indicates membership of an element in a set.\n2. \\(\\subseteq\\) indicates inclusion relation between two sets.' }
];

s132.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic3Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.3.2-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.3.2',
    topicNumber: '1.3.2',
    topic: 'Subset definition (A ⊆ B)',
    topicName: 'Subset definition (A ⊆ B)',
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

// =========================================================================
// Subtopic 1.3.3: Universal set & Complement (22 questions: 11 Exam, 5 Practice, 6 Foundation)
// =========================================================================
const s133 = [
  // Exam (11)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Universal Set Definition',
    text: 'A set which accommodates all the given sets under consideration as its subsets is known as the:',
    opts: [
      { text: 'Universal set (usually denoted by \\(U\\))', isCorrect: true },
      { text: 'Power set', isCorrect: false },
      { text: 'Null set', isCorrect: false },
      { text: 'Disjoint set', isCorrect: false }
    ],
    sol: '1. A universal set \\(U\\) contains all possible objects under consideration in a given discussion.\n2. All other sets in that context are subsets of \\(U\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Complement of Set Definition',
    text: 'Let \\(U\\) be the universal set. The complement of set \\(A\\) (denoted \\(A\'\\) or \\(A^c\\)) is defined as:',
    opts: [
      { text: 'The set of all elements in \\(U\\) that are NOT in \\(A\\)', isCorrect: true },
      { text: 'The set of all elements in \\(A\\) that are in \\(U\\)', isCorrect: false },
      { text: 'The set of elements common to \\(A\\) and \\(U\\)', isCorrect: false },
      { text: 'The empty set always', isCorrect: false }
    ],
    sol: '1. By definition, \\(A\' = \\{x \\mid x \\in U \\text{ and } x \\notin A\\}\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Compute Complement Simple',
    text: 'If \\(U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}\\) and \\(A = \\{2, 4, 6, 8, 10\\}\\), then the complement \\(A\'\\) is:',
    opts: [
      { text: '\\(\\{1, 3, 5, 7, 9\\}\\)', isCorrect: true },
      { text: '\\(\\{2, 4, 6, 8, 10\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(\\{1, 2, 3, 4, 5\\}\\)', isCorrect: false }
    ],
    sol: '1. \\(A\'\\) contains all elements of \\(U\\) that are not in \\(A\\).\n2. Removing even numbers \\(\\{2, 4, 6, 8, 10\\}\\) from \\(U\\) leaves odd numbers \\(\\{1, 3, 5, 7, 9\\}\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Double Complement Property',
    text: 'For any set \\(A\\) within a universal set \\(U\\), what is \\((A\')\'\\)?',
    opts: [
      { text: '\\(A\\) (The complement of the complement of a set is the set itself)', isCorrect: true },
      { text: '\\(A\'\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    sol: '1. \\(A\'\\) contains elements not in \\(A\\).\n2. The complement of \\(A\'\\) contains elements not in \\(A\'\\), which brings us back to \\(A\\).\n3. Hence \\((A\')\' = A\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Complement of Universal Set',
    text: 'What is the complement of the universal set \\(U\'\\)?',
    opts: [
      { text: '\\(\\emptyset\\) (The empty set)', isCorrect: true },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\{0\\}\\)', isCorrect: false },
      { text: 'Undefined', isCorrect: false }
    ],
    sol: '1. \\(U\' = \\{x \\mid x \\in U \\text{ and } x \\notin U\\}\\).\n2. No element can belong to \\(U\\) and simultaneously not belong to \\(U\\).\n3. Thus \\(U\' = \\emptyset\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Complement of Empty Set',
    text: 'What is the complement of the empty set \\(\\emptyset\'\\)?',
    opts: [
      { text: '\\(U\\) (The universal set)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(\\{0\\}\\)', isCorrect: false },
      { text: 'A singleton set', isCorrect: false }
    ],
    sol: '1. \\(\\emptyset\' = \\{x \\mid x \\in U \\text{ and } x \\notin \\emptyset\\}\\).\n2. Since no element is in \\(\\emptyset\\), all elements of \\(U\\) satisfy this condition.\n3. Therefore \\(\\emptyset\' = U\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Intersection of Set and Complement',
    text: 'For any set \\(A\\), what is the value of \\(A \\cap A\'\\)?',
    opts: [
      { text: '\\(\\emptyset\\) (They are disjoint)', isCorrect: true },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    sol: '1. By definition, no element can simultaneously be in \\(A\\) and in \\(A\'\\).\n2. Therefore their intersection has 0 common elements: \\(A \\cap A\' = \\emptyset\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Union of Set and Complement',
    text: 'For any set \\(A\\), what is \\(A \\cup A\'\\)?',
    opts: [
      { text: '\\(U\\) (The universal set)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    sol: '1. Every element in \\(U\\) is either in \\(A\\) or in \\(A\'\\).\n2. Combining both sets covers the entire universe: \\(A \\cup A\' = U\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Complement of Subset Inversion',
    text: 'If \\(A \\subseteq B\\), then what is the relationship between their complements \\(A\'\\) and \\(B\'\\)?',
    opts: [
      { text: '\\(B\' \\subseteq A\'\\)', isCorrect: true },
      { text: '\\(A\' \\subseteq B\'\\)', isCorrect: false },
      { text: '\\(A\' = B\'\\)', isCorrect: false },
      { text: '\\(A\' \\cap B\' = U\\)', isCorrect: false }
    ],
    sol: '1. Let \\(x \\in B\' \\implies x \\notin B\\).\n2. Since \\(A \\subseteq B\\), if \\(x \\notin B\\), then \\(x\\) cannot be in \\(A\\).\n3. Thus \\(x \\in A\'\\).\n4. This proves \\(B\' \\subseteq A\'\\) (complementation reverses the inclusion).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Letters Complement Problem',
    text: 'Let \\(U = \\{a, b, c, d, e, f, g\\}\\) and \\(A = \\{b, d, f\\}\\). What is \\(n(A\')\\)?',
    opts: [
      { text: '\\(4\\) (elements are \\{a, c, e, g\\})', isCorrect: true },
      { text: '\\(3\\)', isCorrect: false },
      { text: '\\(7\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false }
    ],
    sol: '1. \\(A\' = \\{a, c, e, g\\}\\).\n2. The number of elements is 4, so \\(n(A\') = 4\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Cardinality Formula for Complement',
    text: 'If \\(U\\) is a finite universal set and \\(A \\subseteq U\\), then \\(n(A\')\\) is given by:',
    opts: [
      { text: '\\(n(U) - n(A)\\)', isCorrect: true },
      { text: '\\(n(A) - n(U)\\)', isCorrect: false },
      { text: '\\(n(U) + n(A)\\)', isCorrect: false },
      { text: '\\(n(U) / n(A)\\)', isCorrect: false }
    ],
    sol: '1. Since \\(A\\) and \\(A\'\\) are disjoint and \\(A \\cup A\' = U\\), \\(n(A) + n(A\') = n(U)\\).\n2. Rearranging gives \\(n(A\') = n(U) - n(A)\\).' },

  // Practice (5)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Venn Diagram Universal Symbol',
    text: 'In a Venn diagram, the universal set \\(U\\) is conventionally represented by a:',
    opts: [{ text: 'Rectangle', isCorrect: true }, { text: 'Circle', isCorrect: false }, { text: 'Triangle', isCorrect: false }, { text: 'Parallelogram', isCorrect: false }],
    sol: '1. In standard Venn diagrams, the universal set is drawn as a rectangle, and its subsets are drawn as circles inside it.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Complement of Factors of 12',
    text: 'Let \\(U = \\{1, 2, 3, 4, 5, 6\\}\\) and \\(B = \\{1, 2, 3, 6\\}\\). Find \\(B\'\\):',
    opts: [{ text: '\\(\\{4, 5\\}\\)', isCorrect: true }, { text: '\\(\\{1, 2, 3, 6\\}\\)', isCorrect: false }, { text: '\\(\\{4\\}\\)', isCorrect: false }, { text: '\\(\\emptyset\\)', isCorrect: false }],
    sol: '1. Elements in \\(U\\) but not in \\(B\\) are 4 and 5.\n2. Thus \\(B\' = \\{4, 5\\}\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Cardinality Complement Calculation',
    text: 'If \\(n(U) = 50\\) and \\(n(A) = 32\\), find \\(n(A\')\\):',
    opts: [{ text: '\\(18\\)', isCorrect: true }, { text: '\\(82\\)', isCorrect: false }, { text: '\\(32\\)', isCorrect: false }, { text: '\\(50\\)', isCorrect: false }],
    sol: '1. \\(n(A\') = n(U) - n(A) = 50 - 32 = 18\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Self Complement Empty Condition',
    text: 'If a set \\(A\\) satisfies \\(A = A\'\\), what must be true about \\(A\\)?',
    opts: [{ text: 'No such set \\(A\\) can exist, because \\(A \\cap A\' = \\emptyset\\)', isCorrect: true }, { text: '\\(A = U\\)', isCorrect: false }, { text: '\\(A = \\emptyset\\)', isCorrect: false }, { text: '\\(A = \\{0\\}\\)', isCorrect: false }],
    sol: '1. Since \\(A \\cap A\' = \\emptyset\\), if \\(A = A\'\\), then \\(A \\cap A = A = \\emptyset\\).\n2. But if \\(A = \\emptyset\\), then \\(A\' = U\\), so \\(\\emptyset = U\\), which is impossible for non-empty universes.\n3. Hence a set cannot equal its complement.' },
  { v: 'practice', d: 'easy', b: 'Understand', tag: 'Notation of Complement',
    text: 'Which of the following notations denotes the complement of set \\(A\\)?',
    opts: [{ text: '\\(A\'\\) or \\(A^c\\)', isCorrect: true }, { text: '\\(A^{-1}\\)', isCorrect: false }, { text: '\\(|A|\\)', isCorrect: false }, { text: '\\(1/A\\)', isCorrect: false }],
    sol: '1. The complement of \\(A\\) is written as \\(A\'\\) or \\(A^c\\).' },

  // Foundation (6)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Universal Set Meaning',
    text: 'The large set containing all the elements under study in a problem is called the:',
    opts: [{ text: 'Universal set', isCorrect: true }, { text: 'Empty set', isCorrect: false }, { text: 'Singleton set', isCorrect: false }, { text: 'Natural set', isCorrect: false }],
    sol: '1. The universal set is the reference set for all elements considered in that context.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Complement Meaning',
    text: 'The complement of set \\(A\\) contains all elements that:',
    opts: [{ text: 'Do NOT belong to set \\(A\\)', isCorrect: true }, { text: 'Belong to set \\(A\\)', isCorrect: false }, { text: 'Are negative numbers', isCorrect: false }, { text: 'Are prime numbers', isCorrect: false }],
    sol: '1. \\(A\'\\) consists of everything in the universe outside of \\(A\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Empty Set Complement Concept',
    text: 'What is the complement of "nothing" (the empty set) with respect to the universe \\(U\\)?',
    opts: [{ text: 'The entire universe \\(U\\)', isCorrect: true }, { text: 'The empty set', isCorrect: false }, { text: 'A single point', isCorrect: false }, { text: 'Zero', isCorrect: false }],
    sol: '1. Everything outside the empty set is the entire universe: \\(\\emptyset\' = U\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Basic Complement 1 to 5',
    text: 'If \\(U = \\{1, 2, 3, 4, 5\\}\\) and \\(A = \\{1, 3, 5\\}\\), what is \\(A\'\\)?',
    opts: [{ text: '\\(\\{2, 4\\}\\)', isCorrect: true }, { text: '\\(\\{1, 3, 5\\}\\)', isCorrect: false }, { text: '\\(\\{0, 2, 4\\}\\)', isCorrect: false }, { text: '\\(\\emptyset\\)', isCorrect: false }],
    sol: '1. Removing 1, 3, 5 from \\(\\{1, 2, 3, 4, 5\\}\\) leaves \\(\\{2, 4\\}\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'If Set Equals Universe Complement',
    text: 'If set \\(A = U\\), what is its complement \\(A\'\\)?',
    opts: [{ text: '\\(\\emptyset\\)', isCorrect: true }, { text: '\\(U\\)', isCorrect: false }, { text: '\\(\\{1\\}\\)', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
    sol: '1. The complement of the whole universe is empty: \\(U\' = \\emptyset\\).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Does A and A prime overlap',
    text: 'Can any element belong to BOTH set \\(A\\) and set \\(A\'\\) at the same time?',
    opts: [{ text: 'No, they have no elements in common', isCorrect: true }, { text: 'Yes, always', isCorrect: false }, { text: 'Only if the element is 0', isCorrect: false }, { text: 'Only in infinite sets', isCorrect: false }],
    sol: '1. An element is either in \\(A\\) or in \\(A\'\\), never both. \\(A \\cap A\' = \\emptyset\\).' }
];

s133.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic3Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.3.3-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.3.3',
    topicNumber: '1.3.3',
    topic: 'Universal set (U) and Complement of a set (A\')',
    topicName: 'Universal set (U) and Complement of a set (A\')',
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

module.exports = { topic3Questions };
