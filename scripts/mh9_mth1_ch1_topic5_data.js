// scripts/mh9_mth1_ch1_topic5_data.js
// 74 Questions for Topic 1.5: Number of Elements in Set Formula
// Subtopics: 1.5.1 (37 Qs), 1.5.2 (37 Qs)

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
    parentTopicCode: 'MH-9-MTH1-1-1.5',
    parentTopicName: 'Number of Elements in Set Formula: n(A ∪ B) = n(A) + n(B) - n(A ∩ B)',
    type: 'OSC',
    marks: 4,
    timesUsed: 0,
    usedInClassroomTest: false,
    requiresFigure: false,
    createdAt: new Date(),
    updatedAt: new Date()
  };
}

const topic5Questions = [];

// =========================================================================
// Subtopic 1.5.1: Cardinality formula calculations (37 questions: 18 Exam, 10 Practice, 9 Foundation)
// =========================================================================
const s151 = [
  // Exam (18)
  { v: 'exam', d: 'easy', b: 'Remember', tag: 'Cardinality Formula Statement',
    text: 'For any two finite sets \\(A\\) and \\(B\\), the relationship between the number of elements in their union and intersection is given by:',
    opts: [
      { text: '\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)', isCorrect: true },
      { text: '\\(n(A \\cup B) = n(A) + n(B) + n(A \\cap B)\\)', isCorrect: false },
      { text: '\\(n(A \\cup B) = n(A) \\times n(B) - n(A \\cap B)\\)', isCorrect: false },
      { text: '\\(n(A \\cup B) = n(A) - n(B)\\)', isCorrect: false }
    ],
    sol: '1. In adding \\(n(A)\\) and \\(n(B)\\), elements in \\(A \\cap B\\) are counted twice.\n2. Subtracting \\(n(A \\cap B)\\) once corrects the count: \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Calculate Union Direct',
    text: 'If \\(n(A) = 15\\), \\(n(B) = 24\\), and \\(n(A \\cap B) = 7\\), find \\(n(A \\cup B)\\):',
    opts: [
      { text: '\\(32\\)', isCorrect: true },
      { text: '\\(39\\)', isCorrect: false },
      { text: '\\(46\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)\n2. \\(n(A \\cup B) = 15 + 24 - 7 = 39 - 7 = 32\\).' },
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Calculate Intersection Direct',
    text: 'If \\(n(A) = 20\\), \\(n(B) = 28\\), and \\(n(A \\cup B) = 36\\), find \\(n(A \\cap B)\\):',
    opts: [
      { text: '\\(12\\)', isCorrect: true },
      { text: '\\(8\\)', isCorrect: false },
      { text: '\\(16\\)', isCorrect: false },
      { text: '\\(48\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B)\\)\n2. \\(n(A \\cap B) = 20 + 28 - 36 = 48 - 36 = 12\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Calculate n(A) from Others',
    text: 'If \\(n(A \\cup B) = 50\\), \\(n(A \\cap B) = 14\\), and \\(n(B) = 30\\), find \\(n(A)\\):',
    opts: [
      { text: '\\(34\\)', isCorrect: true },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(36\\)', isCorrect: false },
      { text: '\\(44\\)', isCorrect: false }
    ],
    sol: '1. \\(50 = n(A) + 30 - 14 \\implies 50 = n(A) + 16\\)\n2. \\(n(A) = 50 - 16 = 34\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Calculate n(B) from Others',
    text: 'If \\(n(A) = 45\\), \\(n(A \\cap B) = 18\\), and \\(n(A \\cup B) = 70\\), find \\(n(B)\\):',
    opts: [
      { text: '\\(43\\)', isCorrect: true },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(52\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false }
    ],
    sol: '1. \\(70 = 45 + n(B) - 18 \\implies 70 = 27 + n(B)\\)\n2. \\(n(B) = 70 - 27 = 43\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Disjoint Special Case',
    text: 'If \\(n(A) = 17\\), \\(n(B) = 23\\), and \\(A \\cap B = \\emptyset\\), what is \\(n(A \\cup B)\\)?',
    opts: [
      { text: '\\(40\\)', isCorrect: true },
      { text: '\\(6\\)', isCorrect: false },
      { text: '\\(391\\)', isCorrect: false },
      { text: '\\(0\\)', isCorrect: false }
    ],
    sol: '1. Since \\(A \\cap B = \\emptyset\\), \\(n(A \\cap B) = 0\\).\n2. \\(n(A \\cup B) = 17 + 23 - 0 = 40\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Only in A Formula',
    text: 'The number of elements that belong to set \\(A\\) ONLY (and not to set \\(B\\)) is calculated by:',
    opts: [
      { text: '\\(n(A) - n(A \\cap B)\\)', isCorrect: true },
      { text: '\\(n(A \\cup B) - n(A)\\)', isCorrect: false },
      { text: '\\(n(A) - n(B)\\)', isCorrect: false },
      { text: '\\(n(A \\cap B) - n(B)\\)', isCorrect: false }
    ],
    sol: '1. Elements belonging exclusively to \\(A\\) is \\(A - B\\).\n2. Since \\(A = (A - B) \\cup (A \\cap B)\\) and they are disjoint, \\(n(A - B) = n(A) - n(A \\cap B)\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Only in B Formula',
    text: 'If \\(n(B) = 35\\) and \\(n(A \\cap B) = 12\\), how many elements belong to \\(B\\) only?',
    opts: [
      { text: '\\(23\\)', isCorrect: true },
      { text: '\\(47\\)', isCorrect: false },
      { text: '\\(12\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false }
    ],
    sol: '1. Elements in \\(B\\) only \\(= n(B) - n(A \\cap B) = 35 - 12 = 23\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Max Value of Union',
    text: 'If \\(n(A) = 10\\) and \\(n(B) = 15\\), what is the MAXIMUM possible value of \\(n(A \\cup B)\\)?',
    opts: [
      { text: '\\(25\\) (when \\(A\\) and \\(B\\) are disjoint)', isCorrect: true },
      { text: '\\(15\\)', isCorrect: false },
      { text: '\\(10\\)', isCorrect: false },
      { text: '\\(150\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B)\\) is maximized when overlap \\(n(A \\cap B) = 0\\).\n2. Max value \\(= 10 + 15 - 0 = 25\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Min Value of Union',
    text: 'If \\(n(A) = 10\\) and \\(n(B) = 15\\), what is the MINIMUM possible value of \\(n(A \\cup B)\\)?',
    opts: [
      { text: '\\(15\\) (when \\(A \\subseteq B\\))', isCorrect: true },
      { text: '\\(10\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B)\\) is minimized when \\(A\\) is completely contained inside \\(B\\) (\\(A \\subseteq B\\)).\n2. Then \\(A \\cup B = B\\), so minimum cardinality is \\(n(B) = 15\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Max Value of Intersection',
    text: 'If \\(n(A) = 12\\) and \\(n(B) = 18\\), what is the MAXIMUM possible value of \\(n(A \\cap B)\\)?',
    opts: [
      { text: '\\(12\\) (when \\(A \\subseteq B\\))', isCorrect: true },
      { text: '\\(18\\)', isCorrect: false },
      { text: '\\(6\\)', isCorrect: false },
      { text: '\\(30\\)', isCorrect: false }
    ],
    sol: '1. Common elements cannot exceed the size of the smaller set.\n2. Since \\(n(A) = 12\\), at most 12 elements can be shared (when \\(A \\subseteq B\\)).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Min Value of Intersection',
    text: 'If \\(n(U) = 40\\), \\(n(A) = 25\\), and \\(n(B) = 30\\), what is the MINIMUM possible value of \\(n(A \\cap B)\\)?',
    opts: [
      { text: '\\(15\\)', isCorrect: true },
      { text: '\\(0\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false },
      { text: '\\(10\\)', isCorrect: false }
    ],
    sol: '1. Since \\(A \\cup B \\subseteq U\\), \\(n(A \\cup B) \\le 40\\).\n2. \\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B) \\ge 25 + 30 - 40 = 55 - 40 = 15\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Sum of Disjoint Partitions',
    text: 'If \\(n(A - B) = 14\\), \\(n(B - A) = 16\\), and \\(n(A \\cap B) = 8\\), what is \\(n(A \\cup B)\\)?',
    opts: [
      { text: '\\(38\\)', isCorrect: true },
      { text: '\\(30\\)', isCorrect: false },
      { text: '\\(46\\)', isCorrect: false },
      { text: '\\(22\\)', isCorrect: false }
    ],
    sol: '1. The three disjoint components of \\(A \\cup B\\) are \\((A - B)\\), \\((B - A)\\), and \\((A \\cap B)\\).\n2. \\(n(A \\cup B) = 14 + 16 + 8 = 38\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Find n(A) from Partitions',
    text: 'Using the data \\(n(A - B) = 14\\) and \\(n(A \\cap B) = 8\\), what is \\(n(A)\\)?',
    opts: [
      { text: '\\(22\\)', isCorrect: true },
      { text: '\\(6\\)', isCorrect: false },
      { text: '\\(14\\)', isCorrect: false },
      { text: '\\(28\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A) = n(A - B) + n(A \\cap B) = 14 + 8 = 22\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Symmetric Difference Formula',
    text: 'The symmetric difference \\(A \\Delta B = (A - B) \\cup (B - A)\\) represents elements in exactly one of the sets. Its cardinality is:',
    opts: [
      { text: '\\(n(A \\cup B) - n(A \\cap B)\\)', isCorrect: true },
      { text: '\\(n(A) + n(B)\\)', isCorrect: false },
      { text: '\\(n(A \\cap B)\\)', isCorrect: false },
      { text: '\\(n(A \\cup B) + n(A \\cap B)\\)', isCorrect: false }
    ],
    sol: '1. Total union minus overlap leaves elements in either \\(A\\) alone or \\(B\\) alone: \\(n(A \\cup B) - n(A \\cap B)\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Calculate Symmetric Difference Count',
    text: 'If \\(n(A) = 30\\), \\(n(B) = 40\\), and \\(n(A \\cap B) = 10\\), how many elements belong to EITHER \\(A\\) or \\(B\\) but NOT both?',
    opts: [
      { text: '\\(50\\)', isCorrect: true },
      { text: '\\(60\\)', isCorrect: false },
      { text: '\\(70\\)', isCorrect: false },
      { text: '\\(40\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B) = 30 + 40 - 10 = 60\\).\n2. Elements in exactly one set \\(= n(A \\cup B) - n(A \\cap B) = 60 - 10 = 50\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Check Consistency of Counts',
    text: 'Can two sets have \\(n(A) = 20\\), \\(n(B) = 15\\), and \\(n(A \\cap B) = 25\\)?',
    opts: [
      { text: 'No, because \\(n(A \\cap B)\\) cannot exceed \\(n(A)\\) or \\(n(B)\\)', isCorrect: true },
      { text: 'Yes, if the universal set is large', isCorrect: false },
      { text: 'Yes, if sets are infinite', isCorrect: false },
      { text: 'Yes, always', isCorrect: false }
    ],
    sol: '1. Since \\(A \\cap B \\subseteq A\\) and \\(A \\cap B \\subseteq B\\), \\(n(A \\cap B) \\le \\min(n(A), n(B)) = 15\\).\n2. 25 is mathematically impossible.' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Neither Set Elements Count',
    text: 'If \\(n(U) = 100\\), \\(n(A) = 40\\), \\(n(B) = 35\\), and \\(n(A \\cap B) = 15\\), how many elements belong to NEITHER \\(A\\) nor \\(B\\)?',
    opts: [
      { text: '\\(40\\)', isCorrect: true },
      { text: '\\(60\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(50\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B) = 40 + 35 - 15 = 60\\).\n2. Neither \\(A\\) nor \\(B = n((A \\cup B)\') = n(U) - n(A \\cup B) = 100 - 60 = 40\\).' },

  // Practice (10)
  { v: 'practice', d: 'easy', b: 'Apply', tag: 'Practice Union Calculation 1',
    text: 'If \\(n(A) = 8\\), \\(n(B) = 12\\), and \\(n(A \\cap B) = 3\\), find \\(n(A \\cup B)\\):',
    opts: [{ text: '\\(17\\)', isCorrect: true }, { text: '\\(20\\)', isCorrect: false }, { text: '\\(15\\)', isCorrect: false }, { text: '\\(23\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 8 + 12 - 3 = 17\\).' },
  { v: 'practice', d: 'easy', b: 'Apply', tag: 'Practice Intersection Calculation 2',
    text: 'If \\(n(A) = 25\\), \\(n(B) = 18\\), and \\(n(A \\cup B) = 35\\), find \\(n(A \\cap B)\\):',
    opts: [{ text: '\\(8\\)', isCorrect: true }, { text: '\\(10\\)', isCorrect: false }, { text: '\\(7\\)', isCorrect: false }, { text: '\\(43\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cap B) = 25 + 18 - 35 = 43 - 35 = 8\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Practice Missing n(A)',
    text: 'If \\(n(A \\cup B) = 42\\), \\(n(A \\cap B) = 10\\), and \\(n(B) = 22\\), find \\(n(A)\\):',
    opts: [{ text: '\\(30\\)', isCorrect: true }, { text: '\\(20\\)', isCorrect: false }, { text: '\\(32\\)', isCorrect: false }, { text: '\\(28\\)', isCorrect: false }],
    sol: '1. \\(n(A) = n(A \\cup B) + n(A \\cap B) - n(B) = 42 + 10 - 22 = 30\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Practice Missing n(B)',
    text: 'If \\(n(A \\cup B) = 60\\), \\(n(A) = 38\\), and \\(n(A \\cap B) = 15\\), find \\(n(B)\\):',
    opts: [{ text: '\\(37\\)', isCorrect: true }, { text: '\\(22\\)', isCorrect: false }, { text: '\\(45\\)', isCorrect: false }, { text: '\\(53\\)', isCorrect: false }],
    sol: '1. \\(n(B) = 60 + 15 - 38 = 37\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Practice Disjoint Sum',
    text: 'If \\(n(A) = 19\\), \\(n(B) = 21\\), and \\(n(A \\cap B) = 0\\), find \\(n(A \\cup B)\\):',
    opts: [{ text: '\\(40\\)', isCorrect: true }, { text: '\\(2\\)', isCorrect: false }, { text: '\\(399\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 19 + 21 - 0 = 40\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Practice Elements in A only',
    text: 'If \\(n(A) = 50\\) and \\(n(A \\cap B) = 18\\), how many elements are strictly in \\(A - B\\)?',
    opts: [{ text: '\\(32\\)', isCorrect: true }, { text: '\\(68\\)', isCorrect: false }, { text: '\\(18\\)', isCorrect: false }, { text: '\\(50\\)', isCorrect: false }],
    sol: '1. \\(n(A - B) = 50 - 18 = 32\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Practice Elements in B only',
    text: 'If \\(n(B) = 44\\) and \\(n(A \\cap B) = 14\\), how many elements are strictly in \\(B - A\\)?',
    opts: [{ text: '\\(30\\)', isCorrect: true }, { text: '\\(58\\)', isCorrect: false }, { text: '\\(14\\)', isCorrect: false }, { text: '\\(44\\)', isCorrect: false }],
    sol: '1. \\(n(B - A) = 44 - 14 = 30\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Practice Neither Count',
    text: 'In a universal set of 80 elements, \\(n(A) = 35\\), \\(n(B) = 45\\), and \\(n(A \\cap B) = 20\\). How many elements belong to neither set?',
    opts: [{ text: '\\(20\\)', isCorrect: true }, { text: '\\(60\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(10\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 35 + 45 - 20 = 60\\).\n2. \\(n((A \\cup B)\') = 80 - 60 = 20\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Practice Either But Not Both',
    text: 'If \\(n(A) = 22\\), \\(n(B) = 28\\), and \\(n(A \\cap B) = 10\\), what is \\(n(A \\Delta B)\\)?',
    opts: [{ text: '\\(30\\)', isCorrect: true }, { text: '\\(40\\)', isCorrect: false }, { text: '\\(50\\)', isCorrect: false }, { text: '\\(20\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 22 + 28 - 10 = 40\\).\n2. \\(n(A \\Delta B) = 40 - 10 = 30\\).' },
  { v: 'practice', d: 'easy', b: 'Remember', tag: 'Rearranged Intersection Formula',
    text: 'Rearranging the formula gives \\(n(A \\cap B) = \\text{__________}\\).',
    opts: [{ text: '\\(n(A) + n(B) - n(A \\cup B)\\)', isCorrect: true }, { text: '\\(n(A \\cup B) - n(A) - n(B)\\)', isCorrect: false }, { text: '\\(n(A) \\times n(B)\\)', isCorrect: false }, { text: '\\(n(A) - n(B)\\)', isCorrect: false }],
    sol: '1. Bringing \\(n(A \\cap B)\\) to LHS and \\(n(A \\cup B)\\) to RHS yields \\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B)\\).' },

  // Foundation (9)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'What is n(A)',
    text: 'The symbol \\(n(A)\\) represents:',
    opts: [{ text: 'The number of elements in set \\(A\\)', isCorrect: true }, { text: 'The variable \\(n\\) multiplied by \\(A\\)', isCorrect: false }, { text: 'The universal set', isCorrect: false }, { text: 'The subset of \\(A\\)', isCorrect: false }],
    sol: '1. \\(n(A)\\) is standard notation for the cardinality of set \\(A\\).' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Count Elements Simple Set',
    text: 'If \\(A = \\{3, 6, 9, 12, 15\\}\\), what is \\(n(A)\\)?',
    opts: [{ text: '\\(5\\)', isCorrect: true }, { text: '\\(15\\)', isCorrect: false }, { text: '\\(3\\)', isCorrect: false }, { text: '\\(4\\)', isCorrect: false }],
    sol: '1. There are 5 distinct numbers in the set, so \\(n(A) = 5\\).' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Count Empty Set',
    text: 'What is \\(n(\\emptyset)\\)?',
    opts: [{ text: '\\(0\\)', isCorrect: true }, { text: '\\(1\\)', isCorrect: false }, { text: '\\(-1\\)', isCorrect: false }, { text: 'Undefined', isCorrect: false }],
    sol: '1. The empty set has 0 elements.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Basic Formula Plug 1',
    text: 'If \\(n(A) = 5\\), \\(n(B) = 6\\), and \\(n(A \\cap B) = 2\\), what is \\(n(A \\cup B)\\)?',
    opts: [{ text: '\\(9\\)', isCorrect: true }, { text: '\\(11\\)', isCorrect: false }, { text: '\\(7\\)', isCorrect: false }, { text: '\\(13\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 5 + 6 - 2 = 9\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Basic Formula Plug 2',
    text: 'If \\(n(A) = 10\\), \\(n(B) = 10\\), and \\(n(A \\cap B) = 5\\), what is \\(n(A \\cup B)\\)?',
    opts: [{ text: '\\(15\\)', isCorrect: true }, { text: '\\(20\\)', isCorrect: false }, { text: '\\(25\\)', isCorrect: false }, { text: '\\(5\\)', isCorrect: false }],
    sol: '1. \\(n(A \\cup B) = 10 + 10 - 5 = 15\\).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Why Subtract Intersection',
    text: 'Why do we subtract \\(n(A \\cap B)\\) in the union formula?',
    opts: [{ text: 'Because common elements are counted twice when we add \\(n(A)\\) and \\(n(B)\\)', isCorrect: true }, { text: 'Because common elements do not belong to the union', isCorrect: false }, { text: 'To make the answer smaller', isCorrect: false }, { text: 'By random convention', isCorrect: false }],
    sol: '1. Common elements are included in both \\(n(A)\\) and \\(n(B)\\), so subtracting once avoids double-counting.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Disjoint Simple Union',
    text: 'If \\(A = \\{1, 2\\}\\) and \\(B = \\{3, 4\\}\\), what is \\(n(A \\cup B)\\)?',
    opts: [{ text: '\\(4\\)', isCorrect: true }, { text: '\\(2\\)', isCorrect: false }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(8\\)', isCorrect: false }],
    sol: '1. \\(A \\cup B = \\{1, 2, 3, 4\\}\\), so \\(n(A \\cup B) = 4\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Complement from Universe Count',
    text: 'If \\(n(U) = 20\\) and \\(n(A) = 13\\), what is \\(n(A\')\\)?',
    opts: [{ text: '\\(7\\)', isCorrect: true }, { text: '\\(33\\)', isCorrect: false }, { text: '\\(13\\)', isCorrect: false }, { text: '\\(20\\)', isCorrect: false }],
    sol: '1. \\(n(A\') = 20 - 13 = 7\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Can Cardinality be Negative',
    text: 'Can the cardinality \\(n(A)\\) of any set ever be a negative number?',
    opts: [{ text: 'No, cardinality is always a non-negative integer (\\(\\ge 0\\))', isCorrect: true }, { text: 'Yes, for negative numbers', isCorrect: false }, { text: 'Yes, for the empty set', isCorrect: false }, { text: 'Only in algebra', isCorrect: false }],
    sol: '1. Cardinality is a count of physical elements and is always \\(\\ge 0\\).' }
];

s151.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic5Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.5.1-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.5.1',
    topicNumber: '1.5.1',
    topic: 'Cardinality of sets',
    topicName: 'Cardinality of sets',
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
// Subtopic 1.5.2: Word problems on sets (37 questions: 18 Exam, 9 Practice, 10 Foundation)
// =========================================================================
const s152 = [
  // Exam (18)
  { v: 'exam', d: 'easy', b: 'Apply', tag: 'Languages English French',
    text: 'In a class of 50 students, 30 speak English, 25 speak French, and 10 speak both languages. How many students speak at least one of these two languages?',
    opts: [
      { text: '\\(45\\)', isCorrect: true },
      { text: '\\(55\\)', isCorrect: false },
      { text: '\\(40\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false }
    ],
    sol: '1. Let \\(E\\) be English speakers and \\(F\\) be French speakers.\n2. \\(n(E) = 30, n(F) = 25, n(E \\cap F) = 10\\).\n3. \\(n(E \\cup F) = 30 + 25 - 10 = 45\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Languages Neither Language',
    text: 'Using the previous class of 50 students (30 English, 25 French, 10 both), how many students speak NEITHER English nor French?',
    opts: [
      { text: '\\(5\\)', isCorrect: true },
      { text: '\\(10\\)', isCorrect: false },
      { text: '\\(15\\)', isCorrect: false },
      { text: '\\(0\\)', isCorrect: false }
    ],
    sol: '1. Students speaking at least one language \\(= 45\\).\n2. Total students in class \\(= 50\\).\n3. Neither \\(= 50 - 45 = 5\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Cricket and Football Both',
    text: 'In a school hostel of 125 students, 80 play cricket, 60 play football, and 20 play neither game. How many students play BOTH cricket and football?',
    opts: [
      { text: '\\(35\\)', isCorrect: true },
      { text: '\\(40\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(15\\)', isCorrect: false }
    ],
    sol: '1. Total students playing at least one game \\(= 125 - 20 = 105\\).\n2. \\(n(C) = 80, n(F) = 60\\).\n3. \\(n(C \\cap F) = 80 + 60 - 105 = 140 - 105 = 35\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Cricket Only',
    text: 'From the same hostel (80 play cricket, 60 play football, 35 play both), how many students play cricket ONLY?',
    opts: [
      { text: '\\(45\\)', isCorrect: true },
      { text: '\\(80\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false }
    ],
    sol: '1. Cricket only \\(= n(C) - n(C \\cap F) = 80 - 35 = 45\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Football Only',
    text: 'From the same hostel, how many students play football ONLY?',
    opts: [
      { text: '\\(25\\)', isCorrect: true },
      { text: '\\(60\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false },
      { text: '\\(20\\)', isCorrect: false }
    ],
    sol: '1. Football only \\(= n(F) - n(C \\cap F) = 60 - 35 = 25\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Newspaper Readers Overlap',
    text: 'In a society of 100 families, 65 families read Newspaper A and 45 families read Newspaper B. If every family reads at least one newspaper, how many read both?',
    opts: [
      { text: '\\(10\\)', isCorrect: true },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(15\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false }
    ],
    sol: '1. \\(n(A \\cup B) = 100\\).\n2. \\(n(A \\cap B) = 65 + 45 - 100 = 110 - 100 = 10\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Tea and Coffee Beverage Survey',
    text: 'Out of 200 people surveyed in an office, 120 drink tea, 90 drink coffee, and 30 drink neither. How many drink ONLY tea?',
    opts: [
      { text: '\\(80\\)', isCorrect: true },
      { text: '\\(40\\)', isCorrect: false },
      { text: '\\(50\\)', isCorrect: false },
      { text: '\\(120\\)', isCorrect: false }
    ],
    sol: '1. People drinking at least one \\(= 200 - 30 = 170\\).\n2. Both \\(= 120 + 90 - 170 = 40\\).\n3. Tea only \\(= 120 - 40 = 80\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Tea and Coffee Coffee Only',
    text: 'In the same beverage survey (120 tea, 90 coffee, 40 both), how many drink ONLY coffee?',
    opts: [
      { text: '\\(50\\)', isCorrect: true },
      { text: '\\(40\\)', isCorrect: false },
      { text: '\\(90\\)', isCorrect: false },
      { text: '\\(30\\)', isCorrect: false }
    ],
    sol: '1. Coffee only \\(= 90 - 40 = 50\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Tree Plantation Tree Types',
    text: 'In a tree plantation campaign, 110 students planted Neem trees, 90 planted Banyan trees, and 40 planted both types. What was the total number of students who planted trees?',
    opts: [
      { text: '\\(160\\)', isCorrect: true },
      { text: '\\(200\\)', isCorrect: false },
      { text: '\\(150\\)', isCorrect: false },
      { text: '\\(180\\)', isCorrect: false }
    ],
    sol: '1. \\(n(N \\cup B) = n(N) + n(B) - n(N \\cap B) = 110 + 90 - 40 = 160\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Science and Math Passed Students',
    text: 'In an exam, 70 students passed in English, 65 passed in Mathematics, and 45 passed in both subjects. If every student passed in at least one subject, how many total students appeared?',
    opts: [
      { text: '\\(90\\)', isCorrect: true },
      { text: '\\(135\\)', isCorrect: false },
      { text: '\\(110\\)', isCorrect: false },
      { text: '\\(100\\)', isCorrect: false }
    ],
    sol: '1. \\(n(E \\cup M) = 70 + 65 - 45 = 90\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Math Only Passed',
    text: 'Using the previous exam data (70 English, 65 Math, 45 both), how many passed in Mathematics ONLY?',
    opts: [
      { text: '\\(20\\)', isCorrect: true },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(45\\)', isCorrect: false },
      { text: '\\(65\\)', isCorrect: false }
    ],
    sol: '1. Math only \\(= 65 - 45 = 20\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'English Only Passed',
    text: 'From the same exam data, how many passed in English ONLY?',
    opts: [
      { text: '\\(25\\)', isCorrect: true },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(45\\)', isCorrect: false },
      { text: '\\(70\\)', isCorrect: false }
    ],
    sol: '1. English only \\(= 70 - 45 = 25\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Rock Climbing and Trekking',
    text: 'In a scout camp of 60 students, 42 opted for Rock Climbing, 38 opted for Trekking, and all 60 opted for at least one activity. How many opted for BOTH activities?',
    opts: [
      { text: '\\(20\\)', isCorrect: true },
      { text: '\\(24\\)', isCorrect: false },
      { text: '\\(16\\)', isCorrect: false },
      { text: '\\(18\\)', isCorrect: false }
    ],
    sol: '1. Both \\(= 42 + 38 - 60 = 80 - 60 = 20\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Rock Climbing Only',
    text: 'From the scout camp (42 Rock Climbing, 38 Trekking, 20 both), how many opted for Rock Climbing ONLY?',
    opts: [
      { text: '\\(22\\)', isCorrect: true },
      { text: '\\(18\\)', isCorrect: false },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(42\\)', isCorrect: false }
    ],
    sol: '1. Rock climbing only \\(= 42 - 20 = 22\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Trekking Only',
    text: 'From the scout camp, how many opted for Trekking ONLY?',
    opts: [
      { text: '\\(18\\)', isCorrect: true },
      { text: '\\(22\\)', isCorrect: false },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(38\\)', isCorrect: false }
    ],
    sol: '1. Trekking only \\(= 38 - 20 = 18\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Exactly One Activity',
    text: 'In the scout camp, how many students opted for EXACTLY ONE activity?',
    opts: [
      { text: '\\(40\\) (\\(22 + 18\\))', isCorrect: true },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(60\\)', isCorrect: false },
      { text: '\\(30\\)', isCorrect: false }
    ],
    sol: '1. Exactly one activity \\(= \\text{Only Climbing} + \\text{Only Trekking} = 22 + 18 = 40\\).' },
  { v: 'exam', d: 'medium', b: 'Apply', tag: 'Music and Dance Academy',
    text: 'In a cultural academy of 80 artists, 50 learn classical vocal music and 45 learn Kathak dance. If 25 artists learn both, how many learn NEITHER?',
    opts: [
      { text: '\\(10\\)', isCorrect: true },
      { text: '\\(15\\)', isCorrect: false },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(5\\)', isCorrect: false }
    ],
    sol: '1. Learning music or dance \\(= 50 + 45 - 25 = 70\\).\n2. Neither \\(= 80 - 70 = 10\\).' },
  { v: 'exam', d: 'hard', b: 'Analyze', tag: 'Cars and Bikes Commuters',
    text: 'In a corporate office of 150 employees, 85 travel by car, 75 travel by bike, and 20 use public bus (neither car nor bike). How many commute using BOTH car and bike?',
    opts: [
      { text: '\\(30\\)', isCorrect: true },
      { text: '\\(40\\)', isCorrect: false },
      { text: '\\(25\\)', isCorrect: false },
      { text: '\\(35\\)', isCorrect: false }
    ],
    sol: '1. Employees using car or bike \\(= 150 - 20 = 130\\).\n2. Both \\(= 85 + 75 - 130 = 160 - 130 = 30\\).' },

  // Practice (9)
  { v: 'practice', d: 'easy', b: 'Apply', tag: 'Cats and Dogs Pets',
    text: 'In a colony of 40 houses, 22 have a pet dog, 18 have a pet cat, and 6 houses have both. How many houses have at least one pet?',
    opts: [{ text: '\\(34\\)', isCorrect: true }, { text: '\\(40\\)', isCorrect: false }, { text: '\\(28\\)', isCorrect: false }, { text: '\\(30\\)', isCorrect: false }],
    sol: '1. \\(n(D \\cup C) = 22 + 18 - 6 = 34\\).' },
  { v: 'practice', d: 'easy', b: 'Apply', tag: 'No Pets Houses',
    text: 'In the same colony of 40 houses (34 have at least one pet), how many houses have NO pets?',
    opts: [{ text: '\\(6\\)', isCorrect: true }, { text: '\\(12\\)', isCorrect: false }, { text: '\\(4\\)', isCorrect: false }, { text: '\\(8\\)', isCorrect: false }],
    sol: '1. No pets \\(= 40 - 34 = 6\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Hindi and Marathi Speakers',
    text: 'In a group of 70 people, 52 speak Marathi, 38 speak Hindi, and all 70 speak at least one of these two languages. How many speak BOTH?',
    opts: [{ text: '\\(20\\)', isCorrect: true }, { text: '\\(18\\)', isCorrect: false }, { text: '\\(22\\)', isCorrect: false }, { text: '\\(16\\)', isCorrect: false }],
    sol: '1. Both \\(= 52 + 38 - 70 = 90 - 70 = 20\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Marathi Only Speakers',
    text: 'From the same group of 70 people (52 Marathi, 38 Hindi, 20 both), how many speak Marathi ONLY?',
    opts: [{ text: '\\(32\\)', isCorrect: true }, { text: '\\(52\\)', isCorrect: false }, { text: '\\(18\\)', isCorrect: false }, { text: '\\(20\\)', isCorrect: false }],
    sol: '1. Marathi only \\(= 52 - 20 = 32\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Hindi Only Speakers',
    text: 'From the same group, how many speak Hindi ONLY?',
    opts: [{ text: '\\(18\\)', isCorrect: true }, { text: '\\(38\\)', isCorrect: false }, { text: '\\(32\\)', isCorrect: false }, { text: '\\(20\\)', isCorrect: false }],
    sol: '1. Hindi only \\(= 38 - 20 = 18\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Library Books Fiction NonFiction',
    text: 'A library has 90 members. 55 borrow fiction books, 48 borrow non-fiction books, and 18 borrow both. How many members borrow NEITHER type of book?',
    opts: [{ text: '\\(5\\)', isCorrect: true }, { text: '\\(10\\)', isCorrect: false }, { text: '\\(12\\)', isCorrect: false }, { text: '\\(15\\)', isCorrect: false }],
    sol: '1. Members borrowing at least one \\(= 55 + 48 - 18 = 85\\).\n2. Neither \\(= 90 - 85 = 5\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Apples and Oranges Fruit Preference',
    text: 'In a picnic of 45 children, 28 like apples, 24 like oranges, and 12 like both. How many children like apples ONLY?',
    opts: [{ text: '\\(16\\)', isCorrect: true }, { text: '\\(12\\)', isCorrect: false }, { text: '\\(28\\)', isCorrect: false }, { text: '\\(14\\)', isCorrect: false }],
    sol: '1. Apples only \\(= 28 - 12 = 16\\).' },
  { v: 'practice', d: 'hard', b: 'Analyze', tag: 'Oranges Only Fruit Preference',
    text: 'In the same picnic, how many children like oranges ONLY?',
    opts: [{ text: '\\(12\\)', isCorrect: true }, { text: '\\(16\\)', isCorrect: false }, { text: '\\(24\\)', isCorrect: false }, { text: '\\(10\\)', isCorrect: false }],
    sol: '1. Oranges only \\(= 24 - 12 = 12\\).' },
  { v: 'practice', d: 'medium', b: 'Apply', tag: 'Swimming and Badminton',
    text: 'In a sports club of 100 members, 60 swim and 50 play badminton. If 30 do both, how many do at least one of these sports?',
    opts: [{ text: '\\(80\\)', isCorrect: true }, { text: '\\(110\\)', isCorrect: false }, { text: '\\(70\\)', isCorrect: false }, { text: '\\(90\\)', isCorrect: false }],
    sol: '1. \\(60 + 50 - 30 = 80\\).' },

  // Foundation (10)
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Word Problem Approach',
    text: 'To solve practical word problems involving two groups, the most effective visual mathematical tool is a:',
    opts: [{ text: 'Venn diagram', isCorrect: true }, { text: 'Compass', isCorrect: false }, { text: 'Protractor', isCorrect: false }, { text: 'Number line only', isCorrect: false }],
    sol: '1. Venn diagrams provide an intuitive visual representation for word problems involving set overlap.' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Simple Word Problem Tea Coffee',
    text: 'Out of 10 friends, 6 like tea and 4 like coffee. If 2 like both, how many like tea or coffee?',
    opts: [{ text: '\\(8\\)', isCorrect: true }, { text: '\\(10\\)', isCorrect: false }, { text: '\\(12\\)', isCorrect: false }, { text: '\\(6\\)', isCorrect: false }],
    sol: '1. \\(6 + 4 - 2 = 8\\).' },
  { v: 'foundation', d: 'easy', b: 'Apply', tag: 'Neither Simple Calculation',
    text: 'If 8 friends out of 10 like tea or coffee, how many like neither?',
    opts: [{ text: '\\(2\\)', isCorrect: true }, { text: '\\(0\\)', isCorrect: false }, { text: '\\(4\\)', isCorrect: false }, { text: '\\(1\\)', isCorrect: false }],
    sol: '1. \\(10 - 8 = 2\\).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'What does "Both" Mean',
    text: 'In a word problem, the word "both" corresponds to which set operation?',
    opts: [{ text: 'Intersection (\\(\\cap\\))', isCorrect: true }, { text: 'Union (\\(\\cup\\))', isCorrect: false }, { text: 'Complement (\\(\'\\))', isCorrect: false }, { text: 'Disjoint', isCorrect: false }],
    sol: '1. "Both" means satisfying both criteria, which is the intersection.' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'What does "Either or Both" Mean',
    text: 'In a word problem, the phrase "at least one" or "either or both" corresponds to which set operation?',
    opts: [{ text: 'Union (\\(\\cup\\))', isCorrect: true }, { text: 'Intersection (\\(\\cap\\))', isCorrect: false }, { text: 'Empty set', isCorrect: false }, { text: 'Subset', isCorrect: false }],
    sol: '1. "At least one" is the definition of union.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Pens and Pencils',
    text: 'In a stationery box with 20 items, 12 are pens and 8 are pencils. If there are no items that are both pen and pencil, the sets of pens and pencils are:',
    opts: [{ text: 'Disjoint sets', isCorrect: true }, { text: 'Equal sets', isCorrect: false }, { text: 'Overlapping sets', isCorrect: false }, { text: 'Infinite sets', isCorrect: false }],
    sol: '1. No item is both, so intersection is empty, making them disjoint.' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Simple Math Only',
    text: 'If 15 students like math and 5 like both math and science, how many like math only?',
    opts: [{ text: '\\(10\\)', isCorrect: true }, { text: '\\(20\\)', isCorrect: false }, { text: '\\(5\\)', isCorrect: false }, { text: '\\(15\\)', isCorrect: false }],
    sol: '1. Math only \\(= 15 - 5 = 10\\).' },
  { v: 'foundation', d: 'medium', b: 'Apply', tag: 'Simple Science Only',
    text: 'If 12 students like science and 5 like both math and science, how many like science only?',
    opts: [{ text: '\\(7\\)', isCorrect: true }, { text: '\\(17\\)', isCorrect: false }, { text: '\\(12\\)', isCorrect: false }, { text: '\\(5\\)', isCorrect: false }],
    sol: '1. Science only \\(= 12 - 5 = 7\\).' },
  { v: 'foundation', d: 'easy', b: 'Understand', tag: 'Sum of Disjoint Regions',
    text: 'In a two-set Venn diagram, the total number of students in the union is the sum of: (Only A) + (Only B) + \\(\\text{__________}\\).',
    opts: [{ text: 'Both A and B (Overlap)', isCorrect: true }, { text: 'Neither A nor B', isCorrect: false }, { text: 'The universal set', isCorrect: false }, { text: 'Total school students', isCorrect: false }],
    sol: '1. Union \\(= \\text{Only } A + \\text{Only } B + \\text{Both}\\).' },
  { v: 'foundation', d: 'easy', b: 'Remember', tag: 'Check Total Consistency',
    text: 'Can the number of students who like both sports exceed the total number of students who like the first sport?',
    opts: [{ text: 'No, never', isCorrect: true }, { text: 'Yes, always', isCorrect: false }, { text: 'Only if the school is large', isCorrect: false }, { text: 'Depends on the sports', isCorrect: false }],
    sol: '1. The intersection cannot be larger than any of its constituent sets.' }
];

s152.forEach((item, idx) => {
  const seq = String(idx + 1).padStart(3, '0');
  const vPre = item.v === 'exam' ? 'E' : (item.v === 'practice' ? 'P' : 'F');
  topic5Questions.push(makeQ({
    questionCode: `MH-9-MTH1-1-1.5.2-OSC-${vPre}${seq}`,
    topicCode: 'MH-9-MTH1-1-1.5.2',
    topicNumber: '1.5.2',
    topic: 'Word problems on sets',
    topicName: 'Word problems on sets',
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

module.exports = { topic5Questions };
