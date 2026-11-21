// scripts/mh9_mth1_ch1_topic4_data.js
// 70 Questions for Topic 1.4: Venn Diagrams & Operations on Sets (Union & Intersection)
// Subtopics: 1.4.1 (17 Qs), 1.4.2 (18 Qs), 1.4.3 (17 Qs), 1.4.4 (18 Qs)

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
    parentTopicCode: 'MH-9-MTH1-1-1.4',
    parentTopicName: 'Venn Diagrams & Operations on Sets (Union & Intersection)',
    type: 'OSC',
    marks: 4,
    timesUsed: 0,
    usedInClassroomTest: false,
    requiresFigure: false,
    createdAt: new Date(),
    updatedAt: new Date()
  };
}

const topic4Questions = [];

// =========================================================================
// Subtopic 1.4.1: John Venn diagram representations (17 questions: 8 Exam, 4 Practice, 5 Foundation)
// =========================================================================
const s141 = [
  // Exam (8)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Venn Diagram Pioneer',
    text: 'Diagrammatic representations of sets using closed geometric figures were first introduced by the English logician:',
    opts: [
      { text: 'John Venn', isCorrect: true },
      { text: 'Isaac Newton', isCorrect: false },
      { text: 'René Descartes', isCorrect: false },
      { text: 'Euclid', isCorrect: false }
    ],
    sol: '1. John Venn (1834–1923) introduced the use of overlapping geometric shapes to illustrate relationships between sets.' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Venn Diagram Shapes',
    text: 'In standard Venn diagrams, which geometric shape is traditionally used to represent the universal set \\(U\\)?',
    opts: [
      { text: 'A rectangle', isCorrect: true },
      { text: 'A circle', isCorrect: false },
      { text: 'A triangle', isCorrect: false },
      { text: 'A regular hexagon', isCorrect: false }
    ],
    sol: '1. In a Venn diagram, the universal set \\(U\\) is shown as a rectangle, and subsets are shown as circles (or closed curves) inside it.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Subset in Venn Diagram',
    text: 'If set \\(A\\) is a proper subset of set \\(B\\) (\\(A \\subset B\\)), how are they drawn in a Venn diagram?',
    opts: [
      { text: 'Circle \\(A\\) lies completely inside circle \\(B\\)', isCorrect: true },
      { text: 'Circle \\(B\\) lies completely inside circle \\(A\\)', isCorrect: false },
      { text: 'Two completely separated non-overlapping circles', isCorrect: false },
      { text: 'Two intersecting circles with equal areas', isCorrect: false }
    ],
    sol: '1. Since every element of \\(A\\) belongs to \\(B\\), the region representing \\(A\\) must be enclosed entirely within the region representing \\(B\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Venn Diagram Reading',
    text: 'In a Venn diagram, the region common to both circles \\(A\\) and \\(B\\) represents:',
    opts: [
      { text: 'Intersection \\(A \\cap B\\)', isCorrect: true },
      { text: 'Union \\(A \\cup B\\)', isCorrect: false },
      { text: 'Complement \\(A\'\\)', isCorrect: false },
      { text: 'Difference \\(B - A\\)', isCorrect: false }
    ],
    sol: '1. The overlapping portion shared by both circles contains elements that belong to both \\(A\\) and \\(B\\), which is \\(A \\cap B\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Venn Diagram Outside Region',
    text: 'In a universal set \\(U\\) containing circles \\(A\\) and \\(B\\), the region outside both circles represents:',
    opts: [
      { text: '\\((A \\cup B)\'\\) (or \\(A\' \\cap B\'\\))', isCorrect: true },
      { text: '\\(A \\cap B\\)', isCorrect: false },
      { text: '\\(A \\cup B\\)', isCorrect: false },
      { text: '\\(A\' \\cup B\'\\)', isCorrect: false }
    ],
    sol: '1. The region outside both circles consists of elements of \\(U\\) not in \\(A\\) and not in \\(B\\).\n2. This is \\((A \\cup B)\'\\), which equals \\(A\' \\cap B\'\\) by De Morgan\'s Law.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Disjoint Venn Representation',
    text: 'How are two disjoint sets \\(P\\) and \\(Q\\) represented in a Venn diagram?',
    opts: [
      { text: 'Two separate circles that do not touch or overlap', isCorrect: true },
      { text: 'Two overlapping circles', isCorrect: false },
      { text: 'One circle completely inside another', isCorrect: false },
      { text: 'A single shared circle', isCorrect: false }
    ],
    sol: '1. Disjoint sets have no common elements (\\(P \\cap Q = \\emptyset\\)).\n2. Hence their circles have zero overlap.' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Three Circle Venn Overlap',
    text: 'In a Venn diagram with three sets \\(A, B, C\\), the central region where all three circles overlap represents:',
    opts: [
      { text: '\\(A \\cap B \\cap C\\)', isCorrect: true },
      { text: '\\(A \\cup B \\cup C\\)', isCorrect: false },
      { text: '\\((A \\cup B) \\cap C\'\\)', isCorrect: false },
      { text: '\\(A\' \\cap B\' \\cap C\'\\)', isCorrect: false }
    ],
    sol: '1. The central overlapping region belongs to \\(A\\), \\(B\\), and \\(C\\) simultaneously: \\(A \\cap B \\cap C\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Only A Region in Venn',
    text: 'The region of circle \\(A\\) that excludes the overlap with circle \\(B\\) represents:',
    opts: [
      { text: '\\(A - B\\) (Elements in \\(A\\) only, not in \\(B\\))', isCorrect: true },
      { text: '\\(B - A\\)', isCorrect: false },
      { text: '\\(A \\cap B\\)', isCorrect: false },
      { text: '\\(A \\cup B\\)', isCorrect: false }
    ],
    sol: '1. The non-overlapping part of circle \\(A\\) represents elements belonging exclusively to \\(A\\): \\(A - B = A \\cap B\'\\).' },

  // Practice (4)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Venn Diagram Benefit',
    text: 'What is the primary advantage of using Venn diagrams in set theory?',
    opts: [
      { text: 'They provide a clear visual representation of relationships and operations between sets', isCorrect: true },
      { text: 'They eliminate the need for numbers', isCorrect: false },
      { text: 'They make infinite sets finite', isCorrect: false },
      { text: 'They replace algebraic equations', isCorrect: false }
    ],
    sol: '1. Venn diagrams visually demonstrate subset relations, intersections, unions, and disjoint sets.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Complement in Venn Diagram',
    text: 'In a Venn diagram of universal set \\(U\\) with subset \\(A\\), the region shaded outside circle \\(A\\) but inside the rectangle is:',
    opts: [{ text: 'The complement \\(A\'\\)', isCorrect: true }, { text: 'The set \\(A\\)', isCorrect: false }, { text: 'The empty set', isCorrect: false }, { text: 'The universal set \\(U\\)', isCorrect: false }],
    sol: '1. Shading outside \\(A\\) within rectangle \\(U\\) represents \\(A\'\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Venn Diagram Cardinality Check',
    text: 'In a Venn diagram, circle \\(A\\) has 8 elements exclusive to \\(A\\), the overlap has 5 elements, and circle \\(B\\) has 12 elements exclusive to \\(B\\). What is \\(n(A)\\)?',
    opts: [{ text: '\\(13\\) (\\(8 + 5\\))', isCorrect: true }, { text: '\\(8\\)', isCorrect: false }, { text: '\\(25\\)', isCorrect: false }, { text: '\\(17\\)', isCorrect: false }],
    sol: '1. Total elements in circle \\(A = \\text{Only } A + \\text{Overlap} = 8 + 5 = 13\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Venn Diagram Total Union Count',
    text: 'Using the previous Venn diagram (8 in only \\(A\\), 5 in overlap, 12 in only \\(B\\)), what is \\(n(A \\cup B)\\)?',
    opts: [{ text: '\\(25\\) (\\(8 + 5 + 12\\))', isCorrect: true }, { text: '\\(20\\)', isCorrect: false }, { text: '\\(30\\)', isCorrect: false }, { text: '\\(17\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 8 + 5 + 12 = 25\\).' },

  // Foundation (5)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Venn Diagram Definition',
    text: 'Pictures or drawings used to represent sets are called:',
    opts: [{ text: 'Venn diagrams', isCorrect: true }, { text: 'Bar graphs', isCorrect: false }, { text: 'Pie charts', isCorrect: false }, { text: 'Histograms', isCorrect: false }],
    sol: '1. Diagrams representing sets with closed figures are Venn diagrams.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Circle Inside Circle Meaning',
    text: 'If circle \\(P\\) is drawn inside circle \\(Q\\), which set is larger (or superset)?',
    opts: [{ text: 'Set \\(Q\\) is the superset of \\(P\\)', isCorrect: true }, { text: 'Set \\(P\\) is larger than \\(Q\\)', isCorrect: false }, { text: 'Both sets are empty', isCorrect: false }, { text: 'They are disjoint', isCorrect: false }],
    sol: '1. Circle \\(P\\) inside \\(Q\\) means \\(P \\subseteq Q\\), so \\(Q\\) contains \\(P\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Dots Inside Circles in Venn',
    text: 'In a Venn diagram, how are individual elements usually written?',
    opts: [{ text: 'As points (or labels) inside the closed figure', isCorrect: true }, { text: 'Outside the rectangle only', isCorrect: false }, { text: 'On the boundary lines only', isCorrect: false }, { text: 'Below the title only', isCorrect: false }],
    sol: '1. Elements of a set are listed as distinct points inside the set\'s closed boundary.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Two Circles Without Overlap Meaning',
    text: 'If two circles \\(A\\) and \\(B\\) have NO overlapping area, do they share any elements?',
    opts: [{ text: 'No, they share zero elements', isCorrect: true }, { text: 'Yes, all elements', isCorrect: false }, { text: 'Yes, exactly one element', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
    sol: '1. Zero overlap means \\(A \\cap B = \\emptyset\\).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Full Shading of Both Circles',
    text: 'If you shade the entire area of BOTH circles \\(A\\) and \\(B\\) including their overlap, you have shaded:',
    opts: [{ text: '\\(A \\cup B\\) (Union)', isCorrect: true }, { text: '\\(A \\cap B\\) (Intersection)', isCorrect: false }, { text: '\\(A\'\\) (Complement)', isCorrect: false }, { text: '\\(U\\)', isCorrect: false }],
    sol: '1. The combined region of both circles is the union \\(A \\cup B\\).' }
];

s141.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic4Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.4.1-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.4.1',
    topicNumber: '1.4.1',
    topic: 'John Venn diagram representations',
    topicName: 'John Venn diagram representations',
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
// Subtopic 1.4.2: Intersection of sets (A ∩ B) (18 questions: 8 Exam, 5 Practice, 5 Foundation)
// =========================================================================
const s142 = [
  // Exam (8)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Intersection Definition',
    text: 'The intersection of two sets \\(A\\) and \\(B\\) (denoted \\(A \\cap B\\)) is the set of all elements that:',
    opts: [
      { text: 'Belong to BOTH \\(A\\) and \\(B\\)', isCorrect: true },
      { text: 'Belong to either \\(A\\) or \\(B\\)', isCorrect: false },
      { text: 'Belong to \\(A\\) but not \\(B\\)', isCorrect: false },
      { text: 'Belong to \\(U\\) but neither \\(A\\) nor \\(B\\)', isCorrect: false }
    ],
    sol: '1. \\(A \\cap B = \\{x \\mid x \\in A \\text{ and } x \\in B\\}\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Compute Intersection Simple',
    text: 'If \\(A = \\{1, 3, 5, 7\\}\\) and \\(B = \\{2, 3, 6, 7\\}\\), then \\(A \\cap B\\) is:',
    opts: [
      { text: '\\(\\{3, 7\\}\\)', isCorrect: true },
      { text: '\\(\\{1, 2, 3, 5, 6, 7\\}\\)', isCorrect: false },
      { text: '\\(\\{1, 5\\}\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    sol: '1. Common elements in both sets are 3 and 7.\n2. Hence \\(A \\cap B = \\{3, 7\\}\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Commutative Property of Intersection',
    text: 'For any two sets \\(A\\) and \\(B\\), the commutative property of intersection states:',
    opts: [
      { text: '\\(A \\cap B = B \\cap A\\)', isCorrect: true },
      { text: '\\(A \\cap B = A \\cup B\\)', isCorrect: false },
      { text: '\\(A \\cap B = (A \\cap B)\'\\)', isCorrect: false },
      { text: '\\(A \\cap B = \\emptyset\\)', isCorrect: false }
    ],
    sol: '1. The elements common to \\(A\\) and \\(B\\) are the same as common to \\(B\\) and \\(A\\).\n2. Therefore \\(A \\cap B = B \\cap A\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Idempotent Law Intersection',
    text: 'What is the intersection of set \\(A\\) with itself (\\(A \\cap A\\))?',
    opts: [
      { text: '\\(A\\) (Idempotent Law)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(2A\\)', isCorrect: false }
    ],
    sol: '1. Common elements between \\(A\\) and \\(A\\) are simply all elements of \\(A\\).\n2. Thus \\(A \\cap A = A\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Intersection with Empty Set',
    text: 'For any set \\(A\\), what is \\(A \\cap \\emptyset\\)?',
    opts: [
      { text: '\\(\\emptyset\\)', isCorrect: true },
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\{0\\}\\)', isCorrect: false }
    ],
    sol: '1. Since \\(\\emptyset\\) has no elements, there can be no elements common to \\(A\\) and \\(\\emptyset\\).\n2. Therefore \\(A \\cap \\emptyset = \\emptyset\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Intersection with Universal Set',
    text: 'For any subset \\(A \\subseteq U\\), what is \\(A \\cap U\\)?',
    opts: [
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    sol: '1. Every element of \\(A\\) is in \\(U\\).\n2. The elements common to \\(A\\) and \\(U\\) are precisely the elements of \\(A\\).\n3. Hence \\(A \\cap U = A\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Subset Intersection Property',
    text: 'If \\(A \\subseteq B\\), then what is \\(A \\cap B\\)?',
    opts: [
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(B\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false }
    ],
    sol: '1. Since \\(A \\subseteq B\\), every element of \\(A\\) is already in \\(B\\).\n2. The shared elements between \\(A\\) and \\(B\\) is the entire set \\(A\\).\n3. Hence \\(A \\cap B = A\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Intersection of Primes and Evens',
    text: 'Let \\(P\\) be the set of all prime numbers and \\(E\\) be the set of all even natural numbers. Find \\(P \\cap E\\):',
    opts: [
      { text: '\\(\\{2\\}\\)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(\\{2, 4\\}\\)', isCorrect: false },
      { text: 'An infinite set', isCorrect: false }
    ],
    sol: '1. The only even prime number is 2.\n2. Therefore the intersection of primes and even numbers is the singleton set \\(\\{2\\}\\).' },

  // Practice (5)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Intersection Symbol',
    text: 'The mathematical symbol \\(\\cap\\) denotes:',
    opts: [{ text: 'Intersection of sets', isCorrect: true }, { text: 'Union of sets', isCorrect: false }, { text: 'Subset of', isCorrect: false }, { text: 'Element of', isCorrect: false }],
    sol: '1. The inverted U-shaped symbol \\(\\cap\\) denotes intersection.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Intersection Numerical Problem',
    text: 'Let \\(X = \\{2, 4, 6, 8, 10\\}\\) and \\(Y = \\{4, 8, 12, 16\\}\\). Find \\(X \\cap Y\\):',
    opts: [{ text: '\\(\\{4, 8\\}\\)', isCorrect: true }, { text: '\\(\\{2, 6, 10\\}\\)', isCorrect: false }, { text: '\\(\\{4, 8, 12\\}\\)', isCorrect: false }, { text: '\\(\\emptyset\\)', isCorrect: false }],
    sol: '1. Common elements are 4 and 8: \\(X \\cap Y = \\{4, 8\\}\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Cardinality of Intersection',
    text: 'If \\(A = \\{a, b, c, d\\}\\) and \\(B = \\{c, d, e, f, g\\}\\), what is \\(n(A \\cap B)\\)?',
    opts: [{ text: '\\(2\\) (common elements are \\(c, d\\))', isCorrect: true }, { text: '\\(4\\)', isCorrect: false }, { text: '\\(7\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }],
    sol: '1. Common elements: \\(c, d\\).\n2. Count \\(n(A \\cap B) = 2\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Associative Property Intersection',
    text: 'For any three sets \\(A, B, C\\), the associative property of intersection is written as:',
    opts: [{ text: '\\((A \\cap B) \\cap C = A \\cap (B \\cap C)\\)', isCorrect: true }, { text: '\\(A \\cap (B \\cup C) = (A \\cap B) \\cup C\\)', isCorrect: false }, { text: '\\((A \\cap B) \\cap C = A \\cup B \\cup C\\)', isCorrect: false }, { text: '\\(A \\cap B = B \\cap C\\)', isCorrect: false }],
    sol: '1. The associative law states that grouping does not change the result: \\((A \\cap B) \\cap C = A \\cap (B \\cap C)\\).' },
  { v: 'practice', d: 'easy', b: 'Understand', tag: 'Empty Intersection Implication',
    text: 'If \\(A \\cap B = \\emptyset\\), what can be said about the elements of \\(A\\) and \\(B\\)?',
    opts: [{ text: 'They share no common elements', isCorrect: true }, { text: 'Both sets are empty', isCorrect: false }, { text: '\\(A = B\\)', isCorrect: false }, { text: '\\(A \\subseteq B\\)', isCorrect: false }],
    sol: '1. An empty intersection means not a single element is common to both sets.' },

  // Foundation (5)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Intersection Meaning',
    text: 'The word "intersection" in set theory refers to:',
    opts: [{ text: 'Common elements shared by both sets', isCorrect: true }, { text: 'All elements combined together', isCorrect: false }, { text: 'Elements in the first set only', isCorrect: false }, { text: 'Elements in neither set', isCorrect: false }],
    sol: '1. Intersection strictly means common elements.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Simple Intersection Example',
    text: 'If \\(A = \\{1, 2\\}\\) and \\(B = \\{2, 3\\}\\), what is \\(A \\cap B\\)?',
    opts: [{ text: '\\(\\{2\\}\\)', isCorrect: true }, { text: '\\(\\{1, 2, 3\\}\\)', isCorrect: false }, { text: '\\(\\{1, 3\\}\\)', isCorrect: false }, { text: '\\(\\emptyset\\)', isCorrect: false }],
    sol: '1. The only common element is 2. \\(A \\cap B = \\{2\\}\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'No Common Element Intersection',
    text: 'Find \\(\\{1, 3\\} \\cap \\{2, 4\\}\\):',
    opts: [{ text: '\\(\\emptyset\\) (No common element)', isCorrect: true }, { text: '\\(\\{1, 2, 3, 4\\}\\)', isCorrect: false }, { text: '\\(\\{0\\}\\)', isCorrect: false }, { text: '\\(\\{1, 4\\}\\)', isCorrect: false }],
    sol: '1. The two sets share no elements. Hence intersection is empty (\\(\\emptyset\\)).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Intersection is Smaller than Both',
    text: 'Is \\(n(A \\cap B)\\) always less than or equal to \\(n(A)\\)?',
    opts: [{ text: 'Yes, because common elements cannot exceed the elements in \\(A\\)', isCorrect: true }, { text: 'No, it can be larger', isCorrect: false }, { text: 'Only if \\(A = B\\)', isCorrect: false }, { text: 'Never', isCorrect: false }],
    sol: '1. Since \\(A \\cap B \\subseteq A\\), \\(n(A \\cap B) \\le n(A)\\) is always true.' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Cap Symbol Look',
    text: 'The intersection symbol \\(\\cap\\) resembles which letter written upside down?',
    opts: [{ text: 'Letter U', isCorrect: true }, { text: 'Letter A', isCorrect: false }, { text: 'Letter O', isCorrect: false }, { text: 'Letter C', isCorrect: false }],
    sol: '1. \\(\\cup\\) is Union; upside down \\(\\cap\\) is Intersection.' }
];

s142.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic4Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.4.2-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.4.2',
    topicNumber: '1.4.2',
    topic: 'Intersection of sets (A ∩ B)',
    topicName: 'Intersection of sets (A ∩ B)',
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
// Subtopic 1.4.3: Disjoint sets (17 questions: 8 Exam, 4 Practice, 5 Foundation)
// =========================================================================
const s143 = [
  // Exam (8)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Disjoint Sets Definition',
    text: 'Two sets \\(A\\) and \\(B\\) are said to be disjoint sets if and only if:',
    opts: [
      { text: '\\(A \\cap B = \\emptyset\\) (They have no common elements)', isCorrect: true },
      { text: '\\(A \\cup B = U\\)', isCorrect: false },
      { text: '\\(A = B\\)', isCorrect: false },
      { text: '\\(A \\subseteq B\\)', isCorrect: false }
    ],
    sol: '1. By definition, sets with completely non-overlapping elements (intersection is empty) are disjoint sets.' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Identify Disjoint Pair',
    text: 'Which of the following pairs of sets are disjoint sets?',
    opts: [
      { text: '\\(A = \\{1, 3, 5\\}\\) and \\(B = \\{2, 4, 6\\}\\)', isCorrect: true },
      { text: '\\(A = \\{1, 2, 3\\}\\) and \\(B = \\{3, 4, 5\\}\\)', isCorrect: false },
      { text: '\\(A = \\{x, y\\}\\) and \\(B = \\{y, z\\}\\)', isCorrect: false },
      { text: '\\(A = \\{2\\}\\) and \\(B = \\{2, 4\\}\\)', isCorrect: false }
    ],
    sol: '1. Odd numbers \\(\\{1, 3, 5\\}\\) and even numbers \\(\\{2, 4, 6\\}\\) have 0 common elements.\n2. \\(A \\cap B = \\emptyset\\), hence they are disjoint.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Set and Complement are Disjoint',
    text: 'For any set \\(A\\) within universal set \\(U\\), the sets \\(A\\) and \\(A\'\\) are always:',
    opts: [
      { text: 'Disjoint sets, because \\(A \\cap A\' = \\emptyset\\)', isCorrect: true },
      { text: 'Equal sets', isCorrect: false },
      { text: 'Singleton sets', isCorrect: false },
      { text: 'Empty sets', isCorrect: false }
    ],
    sol: '1. \\(A\'\\) contains elements not in \\(A\\).\n2. Thus \\(A\\) and \\(A\'\\) never share elements, making them disjoint.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Disjoint Cardinality Property',
    text: 'If \\(A\\) and \\(B\\) are disjoint finite sets, then the cardinality \\(n(A \\cup B)\\) is equal to:',
    opts: [
      { text: '\\(n(A) + n(B)\\)', isCorrect: true },
      { text: '\\(n(A) + n(B) - 1\\)', isCorrect: false },
      { text: '\\(n(A) \\times n(B)\\)', isCorrect: false },
      { text: '\\(0\\)', isCorrect: false }
    ],
    sol: '1. General formula: \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n2. For disjoint sets, \\(n(A \\cap B) = 0\\).\n3. Hence \\(n(A \\cup B) = n(A) + n(B)\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Prime and Composite Numbers Disjoint',
    text: 'Let \\(P\\) be the set of all prime numbers and \\(C\\) be the set of all composite numbers. Are \\(P\\) and \\(C\\) disjoint sets?',
    opts: [
      { text: 'Yes, because no number can be both prime and composite', isCorrect: true },
      { text: 'No, because 1 is in both', isCorrect: false },
      { text: 'No, because 2 is in both', isCorrect: false },
      { text: 'They are equal sets', isCorrect: false }
    ],
    sol: '1. A prime number has exactly two factors, while a composite number has more than two.\n2. No number satisfies both definitions. (1 is neither prime nor composite).\n3. Thus \\(P \\cap C = \\emptyset\\), making them disjoint.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Venn Diagram Disjoint Circles',
    text: 'In a Venn diagram, two disjoint sets appear as:',
    opts: [
      { text: 'Two separate circles with no common region', isCorrect: true },
      { text: 'Two intersecting circles', isCorrect: false },
      { text: 'Concentric circles', isCorrect: false },
      { text: 'A single overlapping circle', isCorrect: false }
    ],
    sol: '1. Disjoint sets share 0 elements, so their Venn diagram representations never overlap.' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Multiple Sets Disjoint',
    text: 'Three sets \\(A, B, C\\) are pairwise disjoint if:',
    opts: [
      { text: '\\(A \\cap B = \\emptyset, B \\cap C = \\emptyset\\), and \\(A \\cap C = \\emptyset\\)', isCorrect: true },
      { text: '\\(A \\cap B \\cap C = \\emptyset\\) only', isCorrect: false },
      { text: '\\(A \\cup B \\cup C = \\emptyset\\)', isCorrect: false },
      { text: '\\(n(A) = n(B) = n(C)\\)', isCorrect: false }
    ],
    sol: '1. Pairwise disjoint means every possible pair among the sets has an empty intersection.' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Multiples of 2 and 3 Disjoint?',
    text: 'Let \\(A\\) be multiples of 2 and \\(B\\) be multiples of 3. Are \\(A\\) and \\(B\\) disjoint sets?',
    opts: [
      { text: 'No, because they share common multiples like \\(6, 12, 18, \\dots\\)', isCorrect: true },
      { text: 'Yes, because 2 and 3 are prime to each other', isCorrect: false },
      { text: 'Yes, because 2 is even and 3 is odd', isCorrect: false },
      { text: 'Cannot be determined', isCorrect: false }
    ],
    sol: '1. Multiples of 6 belong to both \\(A\\) and \\(B\\).\n2. \\(A \\cap B = \\{6, 12, 18, \\dots\\} \\neq \\emptyset\\).\n3. Hence they are NOT disjoint.' },

  // Practice (4)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Intersection Value of Disjoint',
    text: 'What is the value of \\(n(A \\cap B)\\) if \\(A\\) and \\(B\\) are disjoint sets?',
    opts: [{ text: '\\(0\\)', isCorrect: true }, { text: '\\(1\\)', isCorrect: false }, { text: '\\(-1\\)', isCorrect: false }, { text: '\\(n(A)\\)', isCorrect: false }],
    sol: '1. Disjoint sets have no common elements, so \\(n(A \\cap B) = 0\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Disjoint Check Vowels and Consonants',
    text: 'The set of vowels \\(V = \\{a, e, i, o, u\\}\\) and the set of consonants \\(C\\) in the English alphabet are:',
    opts: [{ text: 'Disjoint sets', isCorrect: true }, { text: 'Equal sets', isCorrect: false }, { text: 'Overlapping sets', isCorrect: false }, { text: 'Empty sets', isCorrect: false }],
    sol: '1. A letter cannot be both a vowel and a consonant.\n2. \\(V \\cap C = \\emptyset\\), so they are disjoint sets.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Disjoint Union Cardinality Calculation',
    text: 'If \\(A\\) and \\(B\\) are disjoint sets with \\(n(A) = 15\\) and \\(n(B) = 25\\), find \\(n(A \\cup B)\\):',
    opts: [{ text: '\\(40\\)', isCorrect: true }, { text: '\\(10\\)', isCorrect: false }, { text: '\\(375\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = n(A) + n(B) = 15 + 25 = 40\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Negative and Positive Integers Disjoint',
    text: 'Are the set of positive integers \\(\\mathbb{I}^+\\) and negative integers \\(\\mathbb{I}^-\\) disjoint?',
    opts: [{ text: 'Yes, no integer can be both positive and negative', isCorrect: true }, { text: 'No, they share 0', isCorrect: false }, { text: 'No, they share -1 and 1', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
    sol: '1. Positive integers \\(= \\{1, 2, \\dots\\}\\), negative integers \\(= \\{-1, -2, \\dots\\}\\).\n2. 0 is neither positive nor negative.\n3. The two sets share no elements and are disjoint.' },

  // Foundation (5)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Disjoint Meaning',
    text: 'The word "disjoint" literally means:',
    opts: [{ text: 'Not joined (having nothing in common)', isCorrect: true }, { text: 'Joined together', isCorrect: false }, { text: 'Equal in size', isCorrect: false }, { text: 'Empty', isCorrect: false }],
    sol: '1. Disjoint sets are separate sets with no common members.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Simple Disjoint Check',
    text: 'Are \\(\\{1, 2\\}\\) and \\(\\{3, 4\\}\\) disjoint sets?',
    opts: [{ text: 'Yes, they have no common elements', isCorrect: true }, { text: 'No, they both contain numbers', isCorrect: false }, { text: 'They are equal', isCorrect: false }, { text: 'False', isCorrect: false }],
    sol: '1. Common elements = none. Therefore disjoint.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Non-disjoint Simple Check',
    text: 'Are \\(\\{1, 2\\}\\) and \\(\\{2, 3\\}\\) disjoint sets?',
    opts: [{ text: 'No, they share the common element 2', isCorrect: true }, { text: 'Yes, they are disjoint', isCorrect: false }, { text: 'They are equal', isCorrect: false }, { text: 'Empty', isCorrect: false }],
    sol: '1. Since 2 is in both sets, they overlap and are NOT disjoint.' },
  { v: 'foundation', d: 'medium', b: 'Understand', tag: 'Is Empty Set Disjoint with Any Set',
    text: 'Is the empty set \\(\\emptyset\\) disjoint with any set \\(A\\)?',
    opts: [{ text: 'Yes, because \\(A \\cap \\emptyset = \\emptyset\\)', isCorrect: true }, { text: 'No, they share 0', isCorrect: false }, { text: 'Only if \\(A\\) is also empty', isCorrect: false }, { text: 'Never', isCorrect: false }],
    sol: '1. By definition, their intersection is empty, so \\(\\emptyset\\) is disjoint with every set.' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Overlap in Disjoint',
    text: 'How much do disjoint sets overlap?',
    opts: [{ text: 'Zero overlap', isCorrect: true }, { text: '50% overlap', isCorrect: false }, { text: '100% overlap', isCorrect: false }, { text: 'Depends on universal set', isCorrect: false }],
    sol: '1. Disjoint sets have zero overlap.' }
];

s143.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic4Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.4.3-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.4.3',
    topicNumber: '1.4.3',
    topic: 'Disjoint sets',
    topicName: 'Disjoint sets',
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
// Subtopic 1.4.4: Union of sets (A ∪ B) (18 questions: 8 Exam, 5 Practice, 5 Foundation)
// =========================================================================
const s144 = [
  // Exam (8)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Union Definition',
    text: 'The union of two sets \\(A\\) and \\(B\\) (written \\(A \\cup B\\)) is the set of all elements that:',
    opts: [
      { text: 'Belong to \\(A\\), or belong to \\(B\\), or belong to both', isCorrect: true },
      { text: 'Belong strictly to both \\(A\\) and \\(B\\) only', isCorrect: false },
      { text: 'Belong to \\(A\\) but not \\(B\\)', isCorrect: false },
      { text: 'Belong to \\(U\\) outside \\(A\\) and \\(B\\)', isCorrect: false }
    ],
    sol: '1. \\(A \\cup B = \\{x \\mid x \\in A \\text{ or } x \\in B\\}\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Compute Union Simple',
    text: 'If \\(A = \\{1, 2, 3\\}\\) and \\(B = \\{2, 3, 4, 5\\}\\), then \\(A \\cup B\\) is:',
    opts: [
      { text: '\\(\\{1, 2, 3, 4, 5\\}\\)', isCorrect: true },
      { text: '\\(\\{2, 3\\}\\)', isCorrect: false },
      { text: '\\(\\{1, 4, 5\\}\\)', isCorrect: false },
      { text: '\\(\\{1, 2, 2, 3, 3, 4, 5\\}\\)', isCorrect: false }
    ],
    sol: '1. Combining elements of \\(A\\) and \\(B\\) without duplicate repetition gives \\(\\{1, 2, 3, 4, 5\\}\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Commutative Property of Union',
    text: 'For any two sets \\(A\\) and \\(B\\), the commutative property of union states:',
    opts: [
      { text: '\\(A \\cup B = B \\cup A\\)', isCorrect: true },
      { text: '\\(A \\cup B = A \\cap B\\)', isCorrect: false },
      { text: '\\(A \\cup B = U\\)', isCorrect: false },
      { text: '\\(A \\cup B = \\emptyset\\)', isCorrect: false }
    ],
    sol: '1. Combining \\(A\\) with \\(B\\) gives the exact same result as combining \\(B\\) with \\(A\\): \\(A \\cup B = B \\cup A\\).' },
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Idempotent Law Union',
    text: 'What is the union of set \\(A\\) with itself (\\(A \\cup A\\))?',
    opts: [
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(2A\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    sol: '1. Combining set \\(A\\) with \\(A\\) does not introduce any new elements. \\(A \\cup A = A\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Union with Empty Set',
    text: 'For any set \\(A\\), what is \\(A \\cup \\emptyset\\)?',
    opts: [
      { text: '\\(A\\)', isCorrect: true },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\{0\\}\\)', isCorrect: false }
    ],
    sol: '1. Since \\(\\emptyset\\) has zero elements, uniting it with \\(A\\) leaves \\(A\\) unchanged: \\(A \\cup \\emptyset = A\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Union with Universal Set',
    text: 'For any subset \\(A \\subseteq U\\), what is \\(A \\cup U\\)?',
    opts: [
      { text: '\\(U\\)', isCorrect: true },
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false },
      { text: '\\(A\'\\)', isCorrect: false }
    ],
    sol: '1. Universal set \\(U\\) contains all elements. Uniting \\(A\\) with \\(U\\) gives \\(U\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Subset Union Property',
    text: 'If \\(A \\subseteq B\\), then what is \\(A \\cup B\\)?',
    opts: [
      { text: '\\(B\\)', isCorrect: true },
      { text: '\\(A\\)', isCorrect: false },
      { text: '\\(U\\)', isCorrect: false },
      { text: '\\(\\emptyset\\)', isCorrect: false }
    ],
    sol: '1. If every element of \\(A\\) is already inside \\(B\\), uniting \\(A\\) with \\(B\\) produces \\(B\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Union of Multiples 2 and 4',
    text: 'Let \\(A\\) be the set of multiples of 4 and \\(B\\) be the set of multiples of 2. Then \\(A \\cup B\\) is equal to:',
    opts: [
      { text: '\\(B\\) (The set of all multiples of 2)', isCorrect: true },
      { text: '\\(A\\) (The set of all multiples of 4)', isCorrect: false },
      { text: 'Multiples of 8', isCorrect: false },
      { text: 'All natural numbers', isCorrect: false }
    ],
    sol: '1. Every multiple of 4 is an even number, so \\(A \\subseteq B\\).\n2. Since \\(A \\subseteq B\\), \\(A \\cup B = B\\).' },

  // Practice (5)
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Union Symbol',
    text: 'The mathematical symbol \\(\\cup\\) denotes:',
    opts: [{ text: 'Union of sets', isCorrect: true }, { text: 'Intersection of sets', isCorrect: false }, { text: 'Subset of', isCorrect: false }, { text: 'Universal set only', isCorrect: false }],
    sol: '1. The cup-shaped symbol \\(\\cup\\) represents union.' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Union Numerical Problem',
    text: 'Let \\(P = \\{a, b, c\\}\\) and \\(Q = \\{c, d, e\\}\\). Find \\(P \\cup Q\\):',
    opts: [{ text: '\\(\\{a, b, c, d, e\\}\\)', isCorrect: true }, { text: '\\(\\{c\\}\\)', isCorrect: false }, { text: '\\(\\{a, b, d, e\\}\\)', isCorrect: false }, { text: '\\(\\{a, b, c, c, d, e\\}\\)', isCorrect: false }],
    sol: '1. Combining elements without repetition: \\(\\{a, b, c, d, e\\}\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Cardinality of Disjoint Union',
    text: 'If \\(A \\cap B = \\emptyset\\), \\(n(A) = 12\\), and \\(n(B) = 18\\), find \\(n(A \\cup B)\\):',
    opts: [{ text: '\\(30\\)', isCorrect: true }, { text: '\\(6\\)', isCorrect: false }, { text: '\\(216\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }],
    sol: '1. For disjoint sets, \\(n(A \\cup B) = n(A) + n(B) = 12 + 18 = 30\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Associative Property Union',
    text: 'For any three sets \\(A, B, C\\), the associative property of union is:',
    opts: [{ text: '\\((A \\cup B) \\cup C = A \\cup (B \\cup C)\\)', isCorrect: true }, { text: '\\(A \\cup (B \\cap C) = (A \\cup B) \\cap C\\)', isCorrect: false }, { text: '\\(A \\cup B = B \\cup C\\)', isCorrect: false }, { text: '\\(A \\cup B = \\emptyset\\)', isCorrect: false }],
    sol: '1. Associative law states that groupings can be shifted freely: \\((A \\cup B) \\cup C = A \\cup (B \\cup C)\\).' },
  { v: 'practice', d: 'easy', b: 'Understand', tag: 'Set Subset of Union',
    text: 'For any two sets \\(A\\) and \\(B\\), is \\(A \\subseteq (A \\cup B)\\)?',
    opts: [{ text: 'Yes, \\(A\\) is always a subset of \\(A \\cup B\\)', isCorrect: true }, { text: 'No, only if \\(B = \\emptyset\\)', isCorrect: false }, { text: 'No, \\(A \\cup B \\subseteq A\\)', isCorrect: false }, { text: 'False', isCorrect: false }],
    sol: '1. Every element of \\(A\\) is naturally included in \\(A \\cup B\\).' },

  // Foundation (5)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Union Meaning',
    text: 'The union of sets means:',
    opts: [{ text: 'Putting all members of both sets together into one set', isCorrect: true }, { text: 'Taking only the common members', isCorrect: false }, { text: 'Subtracting one set from another', isCorrect: false }, { text: 'Multiplying the members', isCorrect: false }],
    sol: '1. Union unites all elements of the given sets.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Simple Union 1 to 4',
    text: 'Find \\(\\{1, 2\\} \\cup \\{3, 4\\}\\):',
    opts: [{ text: '\\(\\{1, 2, 3, 4\\}\\)', isCorrect: true }, { text: '\\(\\emptyset\\)', isCorrect: false }, { text: '\\(\\{2, 3\\}\\)', isCorrect: false }, { text: '\\(\\{1, 4\\}\\)', isCorrect: false }],
    sol: '1. Combining both sets gives \\(\\{1, 2, 3, 4\\}\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Union with Shared Elements',
    text: 'Find \\(\\{a, b\\} \\cup \\{b, c\\}\\):',
    opts: [{ text: '\\(\\{a, b, c\\}\\)', isCorrect: true }, { text: '\\(\\{b\\}\\)', isCorrect: false }, { text: '\\(\\{a, c\\}\\)', isCorrect: false }, { text: '\\(\\{a, b, b, c\\}\\)', isCorrect: false }],
    sol: '1. Elements are a, b, c. The duplicate b is listed once.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Union is Larger than Both',
    text: 'Is \\(n(A \\cup B)\\) always greater than or equal to \\(n(A)\\)?',
    opts: [{ text: 'Yes, because \\(A \\subseteq A \\cup B\\)', isCorrect: true }, { text: 'No, it can be smaller', isCorrect: false }, { text: 'Only if both are empty', isCorrect: false }, { text: 'Never', isCorrect: false }],
    sol: '1. Adding more elements to a set cannot decrease its cardinality.' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Cup Symbol Look',
    text: 'The union symbol \\(\\cup\\) looks like the letter:',
    opts: [{ text: 'U', isCorrect: true }, { text: 'V', isCorrect: false }, { text: 'C', isCorrect: false }, { text: 'N', isCorrect: false }],
    sol: '1. \\(\\cup\\) looks like U for Union.' }
];

s144.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic4Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.4.4-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.4.4',
    topicNumber: '1.4.4',
    topic: 'Union of sets (A ∪ B)',
    topicName: 'Union of sets (A ∪ B)',
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

module.exports = { topic4Questions };
