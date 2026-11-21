const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const QUESTIONS = [
  // =========================================================================
  // CHAPTER 4: Ratio and Proportion (Remaining Subtopics in 4.4)
  // Subtopics: 4.4.1, 4.4.3, 4.4.4
  // =========================================================================

  // --- Subtopic 4.4.1: Theorem: a/b = c/d = (a+c)/(b+d) [MH-9-MTH1-4-4.4.1] ---
  {
    questionCode: 'MH-9-MTH1-4-4.4.1-OSC-001',
    topicCode: 'MH-9-MTH1-4-4.4.1',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.1',
    topic: 'Theorem: a/b = c/d = (a+c)/(b+d)',
    topicName: 'Theorem on Equal Ratios: a/b = c/d = (a+c)/(b+d)',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Theorem on Equal Ratios Statement',
    text: 'If \\(\\frac{a}{b} = \\frac{c}{d}\\), then according to the theorem on equal ratios, each ratio is equal to:',
    options: [
      { text: '\\(\\frac{a + c}{b + d}\\)', isCorrect: true },
      { text: '\\(\\frac{a - c}{b + d}\\)', isCorrect: false },
      { text: '\\(\\frac{ac}{bd}\\)', isCorrect: false },
      { text: '\\(\\frac{a + d}{b + c}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The theorem on equal ratios states that if \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then \\(a = bk\\) and \\(c = dk\\).\n2. Adding numerators and denominators: \\(\\frac{a + c}{b + d} = \\frac{bk + dk}{b + d} = \\frac{k(b + d)}{b + d} = k\\).\n3. Hence each ratio equals \\(\\frac{a + c}{b + d}\\).'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.1-OSC-002',
    topicCode: 'MH-9-MTH1-4-4.4.1',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.1',
    topic: 'Theorem: a/b = c/d = (a+c)/(b+d)',
    topicName: 'Theorem on Equal Ratios: a/b = c/d = (a+c)/(b+d)',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'General Theorem on Equal Ratios',
    text: 'If \\(\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}\\), then what is the value of the ratio \\(\\frac{2x - 3y + 4z}{2(2) - 3(3) + 4(5)}\\)?',
    options: [
      { text: 'Each of the given ratios \\(\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}\\)', isCorrect: true },
      { text: '\\(0\\)', isCorrect: false },
      { text: '\\(1\\)', isCorrect: false },
      { text: '\\(\\frac{15}{23}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By the generalized theorem on equal ratios: if \\(\\frac{a}{p} = \\frac{b}{q} = \\frac{c}{r} = k\\), then for any non-zero multipliers \\(l, m, n\\), \\(\\frac{la + mb + nc}{lp + mq + nr} = k\\).\n2. Here multipliers are \\(l = 2, m = -3, n = 4\\).\n3. Therefore, \\(\\frac{2x - 3y + 4z}{2(2) - 3(3) + 4(5)} = k\\), which equals each of the original ratios.'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.1-OSC-003',
    topicCode: 'MH-9-MTH1-4-4.4.1',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.1',
    topic: 'Theorem: a/b = c/d = (a+c)/(b+d)',
    topicName: 'Theorem on Equal Ratios: a/b = c/d = (a+c)/(b+d)',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Solving Using Equal Ratios',
    text: 'If \\(\\frac{a}{x + y} = \\frac{b}{y + z} = \\frac{c}{z + x}\\), then \\(\\frac{a + b - c}{2y}\\) is equal to:',
    options: [
      { text: 'Each given ratio', isCorrect: true },
      { text: '\\(2\\)', isCorrect: false },
      { text: '\\(\\frac{1}{2}\\)', isCorrect: false },
      { text: '\\(a + b + c\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By theorem on equal ratios, each ratio equals \\(\\frac{\\text{Numerator 1} + \\text{Numerator 2} - \\text{Numerator 3}}{\\text{Denominator 1} + \\text{Denominator 2} - \\text{Denominator 3}}\\).\n2. Sum of denominators: \\((x + y) + (y + z) - (z + x) = x + y + y + z - z - x = 2y\\).\n3. Hence, \\(\\frac{a + b - c}{2y}\\) is equal to each given ratio.'
  },

  // --- Subtopic 4.4.3: Geometric mean formula b² = ac [MH-9-MTH1-4-4.4.3] ---
  {
    questionCode: 'MH-9-MTH1-4-4.4.3-OSC-001',
    topicCode: 'MH-9-MTH1-4-4.4.3',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.3',
    topic: 'Geometric mean formula b² = ac',
    topicName: 'Geometric mean formula b² = ac',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Geometric Mean Definition',
    text: 'If \\(a, b, c\\) are in continued proportion, then \\(b\\) is called the geometric mean of \\(a\\) and \\(c\\), and the relation between them is:',
    options: [
      { text: '\\(b^2 = ac\\)', isCorrect: true },
      { text: '\\(b = a + c\\)', isCorrect: false },
      { text: '\\(b = \\frac{a + c}{2}\\)', isCorrect: false },
      { text: '\\(b^2 = a + c\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. When \\(a, b, c\\) are in continued proportion, \\(\\frac{a}{b} = \\frac{b}{c}\\).\n2. Cross-multiplying gives \\(b \\times b = a \\times c \\implies b^2 = ac\\).\n3. Thus \\(b = \\sqrt{ac}\\) is the geometric mean (or mean proportional) of \\(a\\) and \\(c\\).'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.3-OSC-002',
    topicCode: 'MH-9-MTH1-4-4.4.3',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.3',
    topic: 'Geometric mean formula b² = ac',
    topicName: 'Geometric mean formula b² = ac',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Calculate Geometric Mean',
    text: 'Find the geometric mean of \\(4\\) and \\(25\\):',
    options: [
      { text: '\\(10\\)', isCorrect: true },
      { text: '\\(14.5\\)', isCorrect: false },
      { text: '\\(20\\)', isCorrect: false },
      { text: '\\(100\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Let \\(b\\) be the geometric mean of 4 and 25.\n2. By the formula: \\(b^2 = ac = 4 \\times 25 = 100\\).\n3. Taking square root: \\(b = \\sqrt{100} = 10\\).'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.3-OSC-003',
    topicCode: 'MH-9-MTH1-4-4.4.3',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.3',
    topic: 'Geometric mean formula b² = ac',
    topicName: 'Geometric mean formula b² = ac',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Find Third Proportional',
    text: 'If \\(12\\) is the mean proportional between \\(x\\) and \\(16\\), find the value of \\(x\\):',
    options: [
      { text: '\\(9\\)', isCorrect: true },
      { text: '\\(8\\)', isCorrect: false },
      { text: '\\(14\\)', isCorrect: false },
      { text: '\\(18\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. By geometric mean property, \\(b^2 = ac\\).\n2. Here \\(b = 12, c = 16\\), so \\(12^2 = x \\times 16\\).\n3. \\(144 = 16x \\implies x = \\frac{144}{16} = 9\\).'
  },

  // --- Subtopic 4.4.4: k-method of proof [MH-9-MTH1-4-4.4.4] ---
  {
    questionCode: 'MH-9-MTH1-4-4.4.4-OSC-001',
    topicCode: 'MH-9-MTH1-4-4.4.4',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.4',
    topic: 'k-method of proof',
    topicName: 'k-method of proof',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'k-method Substitution in Proportion',
    text: 'In the \\(k\\)-method, if \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then the substitutions for \\(a\\) and \\(c\\) are:',
    options: [
      { text: '\\(a = bk\\) and \\(c = dk\\)', isCorrect: true },
      { text: '\\(a = \\frac{k}{b}\\) and \\(c = \\frac{k}{d}\\)', isCorrect: false },
      { text: '\\(a = b + k\\) and \\(c = d + k\\)', isCorrect: false },
      { text: '\\(a = k\\) and \\(c = k\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In the \\(k\\)-method, we assume the common ratio is a constant \\(k\\): \\(\\frac{a}{b} = k \\implies a = bk\\).\n2. Similarly, \\(\\frac{c}{d} = k \\implies c = dk\\).\n3. Substituting these expressions into LHS and RHS simplifies both sides to verify identity.'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.4-OSC-002',
    topicCode: 'MH-9-MTH1-4-4.4.4',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.4',
    topic: 'k-method of proof',
    topicName: 'k-method of proof',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'k-method Continued Proportion',
    text: 'If \\(a, b, c\\) are in continued proportion and \\(\\frac{a}{b} = \\frac{b}{c} = k\\), then \\(a\\) and \\(b\\) expressed in terms of \\(c\\) and \\(k\\) are:',
    options: [
      { text: '\\(b = ck\\) and \\(a = ck^2\\)', isCorrect: true },
      { text: '\\(b = c\\) and \\(a = c\\)', isCorrect: false },
      { text: '\\(b = ck^2\\) and \\(a = ck\\)', isCorrect: false },
      { text: '\\(b = \\frac{c}{k}\\) and \\(a = \\frac{c}{k^2}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. From \\(\\frac{b}{c} = k\\), we get \\(b = ck\\).\n2. From \\(\\frac{a}{b} = k\\), we get \\(a = bk = (ck)k = ck^2\\).\n3. Therefore, \\(a = ck^2\\) and \\(b = ck\\).'
  },
  {
    questionCode: 'MH-9-MTH1-4-4.4.4-OSC-003',
    topicCode: 'MH-9-MTH1-4-4.4.4',
    parentTopicCode: 'MH-9-MTH1-4-4.4',
    topicNumber: '4.4.4',
    topic: 'k-method of proof',
    topicName: 'k-method of proof',
    parentTopicName: 'Theorem on Equal Ratios & Continued Proportion',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 4,
    chapter: 'Ratio and Proportion',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    conceptTag: 'k-method Algebraic Identity',
    text: 'If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then the value of \\(\\frac{5a + 3c}{5b + 3d}\\) simplifies to:',
    options: [
      { text: '\\(k\\)', isCorrect: true },
      { text: '\\(k^2\\)', isCorrect: false },
      { text: '\\(5k\\)', isCorrect: false },
      { text: '\\(\\frac{8k}{5b + 3d}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Substitute \\(a = bk\\) and \\(c = dk\\) into the expression:\n   \\(\\frac{5a + 3c}{5b + 3d} = \\frac{5(bk) + 3(dk)}{5b + 3d}\\)\n2. Factor out \\(k\\) from the numerator:\n   \\(\\frac{k(5b + 3d)}{5b + 3d} = k\\).\n3. Hence the expression equals \\(k\\).'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Chapter 4 Remaining Subtopics ===`);
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
  console.log('All Chapter 4 questions passed strict validation perfectly!');

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch4_remaining');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore across Chapter 4 Remaining Subtopics!`);
}

main().catch(console.error);
