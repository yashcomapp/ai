const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const { createPreMutationSnapshot } = require('./pre-mutation-snapshot.js');
const { validateQuestion } = require('./question_validator.js');

const QUESTIONS = [
  // =========================================================================
  // CHAPTER 6: Financial Planning (Topics 6.2 and 6.3)
  // Subtopics: 6.2.1, 6.2.2, 6.2.3, 6.3.1, 6.3.2, 6.3.3
  // =========================================================================

  // --- Subtopic 6.2.1: Direct tax vs Indirect tax [MH-9-MTH1-6-6.2.1] ---
  {
    questionCode: 'MH-9-MTH1-6-6.2.1-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.2.1',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.1',
    topic: 'Direct tax vs Indirect tax',
    topicName: 'Direct tax vs Indirect tax',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Direct vs Indirect Tax Definition',
    text: 'A tax which is paid directly by an individual on their earned income to the government is called a:',
    options: [
      { text: 'Direct tax (e.g., Income Tax)', isCorrect: true },
      { text: 'Indirect tax (e.g., Goods and Services Tax - GST)', isCorrect: false },
      { text: 'Customs duty only', isCorrect: false },
      { text: 'Excise duty only', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Direct tax is paid directly by the taxpayer to the government on their income or wealth (such as Income Tax, Corporate Tax).\n2. Indirect tax (like GST) is collected by intermediaries from the consumer on goods and services.\n3. Hence income tax is a prime example of direct tax.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.1-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.2.1',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.1',
    topic: 'Direct tax vs Indirect tax',
    topicName: 'Direct tax vs Indirect tax',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Classify Tax Types',
    text: 'Which of the following is classified as an indirect tax in India?',
    options: [
      { text: 'Goods and Services Tax (GST)', isCorrect: true },
      { text: 'Income Tax', isCorrect: false },
      { text: 'Wealth Tax', isCorrect: false },
      { text: 'Corporation Tax', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Income tax and corporation tax are directly levied on personal and corporate incomes.\n2. Goods and Services Tax (GST) is levied on the manufacture, sale, and consumption of goods and services, making it an indirect tax.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.1-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.2.1',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.1',
    topic: 'Direct tax vs Indirect tax',
    topicName: 'Direct tax vs Indirect tax',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Tax Revenue Purpose',
    text: 'Government utilizes the revenue collected from income tax primarily for:',
    options: [
      { text: 'Public infrastructure, defence, healthcare, and welfare development', isCorrect: true },
      { text: 'Private corporate profit distributions', isCorrect: false },
      { text: 'Stock market speculation', isCorrect: false },
      { text: 'Foreign real estate purchases', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Taxes are the primary revenue of the government.\n2. This revenue is used for public welfare schemes, education, healthcare, roads, railways, and national defence.'
  },

  // --- Subtopic 6.2.2: Permanent Account Number (PAN) [MH-9-MTH1-6-6.2.2] ---
  {
    questionCode: 'MH-9-MTH1-6-6.2.2-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.2.2',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.2',
    topic: 'Permanent Account Number (PAN)',
    topicName: 'Permanent Account Number (PAN)',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'PAN Format',
    text: 'A Permanent Account Number (PAN) card issued by the Income Tax Department contains an alphanumeric code consisting of exactly how many characters?',
    options: [
      { text: '10 alphanumeric characters', isCorrect: true },
      { text: '12 numeric digits', isCorrect: false },
      { text: '8 alphanumeric characters', isCorrect: false },
      { text: '16 numeric digits', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. PAN is a unique 10-character alphanumeric identifier issued by the Income Tax Department of India.\n2. The structure typically contains 5 letters, 4 numerals, and 1 letter (e.g. ABCDE1234F).'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.2-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.2.2',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.2',
    topic: 'Permanent Account Number (PAN)',
    topicName: 'Permanent Account Number (PAN)',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Mandatory PAN Usage',
    text: 'In which of the following financial transactions is quoting the PAN card mandatory?',
    options: [
      { text: 'Opening a bank account, filing income tax returns, and high-value cash deposits', isCorrect: true },
      { text: 'Purchasing a bus ticket for city travel', isCorrect: false },
      { text: 'Buying vegetables in a local retail market', isCorrect: false },
      { text: 'Visiting a public garden or library', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Under Indian tax laws, PAN is legally required for financial identity verification.\n2. This includes filing income tax returns, opening bank accounts, buying or selling immovable property, and high-value transactions.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.2-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.2.2',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.2',
    topic: 'Permanent Account Number (PAN)',
    topicName: 'Permanent Account Number (PAN)',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Issuing Authority for PAN',
    text: 'Which government authority issues the Permanent Account Number (PAN)?',
    options: [
      { text: 'Income Tax Department, Central Board of Direct Taxes (CBDT)', isCorrect: true },
      { text: 'Reserve Bank of India (RBI)', isCorrect: false },
      { text: 'State Bank of India (SBI)', isCorrect: false },
      { text: 'Election Commission of India', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. PAN is issued by the Income Tax Department under the supervision of the Central Board of Direct Taxes (CBDT), Ministry of Finance.'
  },

  // --- Subtopic 6.2.3: Financial Year vs Assessment Year [MH-9-MTH1-6-6.2.3] ---
  {
    questionCode: 'MH-9-MTH1-6-6.2.3-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.2.3',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.3',
    topic: 'Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)',
    topicName: 'Financial Year vs Assessment Year',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Financial Year Duration',
    text: 'In India, a Financial Year (FY) begins on and ends on:',
    options: [
      { text: '1st April of the current year to 31st March of the following year', isCorrect: true },
      { text: '1st January to 31st December of the same calendar year', isCorrect: false },
      { text: '1st July to 30th June of the following year', isCorrect: false },
      { text: '1st October to 30th September of the following year', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. In Indian taxation, the 12-month period for earning income runs from 1st April to 31st March.\n2. This period is called the Financial Year (FY).'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.3-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.2.3',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.3',
    topic: 'Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)',
    topicName: 'Financial Year vs Assessment Year',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Identify Assessment Year',
    text: 'If an individual earns income during the Financial Year 2024-25 (1st April 2024 to 31st March 2025), what is the corresponding Assessment Year (AY)?',
    options: [
      { text: '2025-26', isCorrect: true },
      { text: '2024-25', isCorrect: false },
      { text: '2023-24', isCorrect: false },
      { text: '2026-27', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Assessment Year (AY) is the financial year immediately following the financial year in which the income was earned.\n2. For Financial Year 2024-25, the income is assessed and taxed in AY 2025-26.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.2.3-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.2.3',
    parentTopicCode: 'MH-9-MTH1-6-6.2',
    topicNumber: '6.2.3',
    topic: 'Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)',
    topicName: 'Financial Year vs Assessment Year',
    parentTopicName: 'Income Tax Basics: PAN Card, Financial Year & Assessment Year',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Understand',
    conceptTag: 'Income Earned vs Income Taxed',
    text: 'The period during which income is actually earned is known as the \\(\\text{__________}\\), while the period during which tax is computed and paid on that income is the \\(\\text{__________}\\).',
    options: [
      { text: 'Financial Year; Assessment Year', isCorrect: true },
      { text: 'Assessment Year; Financial Year', isCorrect: false },
      { text: 'Calendar Year; Financial Year', isCorrect: false },
      { text: 'Accounting Year; Leap Year', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. The year in which income is earned is the Financial Year (Previous Year).\n2. The immediate succeeding year in which tax return is filed is the Assessment Year.'
  },

  // --- Subtopic 6.3.1: Taxable income calculation [MH-9-MTH1-6-6.3.1] ---
  {
    questionCode: 'MH-9-MTH1-6-6.3.1-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.3.1',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.1',
    topic: 'Taxable income calculation',
    topicName: 'Taxable income calculation',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Taxable Income Formula',
    text: 'How is Taxable Income calculated from Gross Total Income?',
    options: [
      { text: '\\(\\text{Taxable Income} = \\text{Gross Total Income} - \\text{Total Eligible Deductions}\\)', isCorrect: true },
      { text: '\\(\\text{Taxable Income} = \\text{Gross Total Income} + \\text{Total Eligible Deductions}\\)', isCorrect: false },
      { text: '\\(\\text{Taxable Income} = \\text{Gross Total Income} \\times \\text{Tax Rate}\\)', isCorrect: false },
      { text: '\\(\\text{Taxable Income} = \\text{Total Savings} - \\text{Expenditure}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Gross Total Income is the total earnings from salary, business, interest, etc.\n2. Taxable Income is obtained by subtracting allowable deductions (under Section 80C, 80D, etc.) from Gross Total Income.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.1-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.3.1',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.1',
    topic: 'Taxable income calculation',
    topicName: 'Taxable income calculation',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Compute Taxable Income Sample',
    text: 'Mr. Sharma has a gross annual income of \\(₹8,50,000\\). He invests \\(₹1,50,000\\) under Section 80C and pays \\(₹25,000\\) for health insurance under Section 80D. What is his taxable income?',
    options: [
      { text: '\\(₹6,75,000\\)', isCorrect: true },
      { text: '\\(₹7,00,000\\)', isCorrect: false },
      { text: '\\(₹6,50,000\\)', isCorrect: false },
      { text: '\\(₹8,25,000\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Total deductions = \\(₹1,50,000\\) (under 80C) + \\(₹25,000\\) (under 80D) = \\(₹1,75,000\\).\n2. Taxable Income = Gross Income \\(- \\text{Deductions}\\)\n   \\(= ₹8,50,000 - ₹1,75,000 = ₹6,75,000\\).'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.1-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.3.1',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.1',
    topic: 'Taxable income calculation',
    topicName: 'Taxable income calculation',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Zero Tax Liability Threshold',
    text: 'If an individual taxpayer aged 45 years has a taxable income of \\(₹2,40,000\\), what is their basic income tax liability (excluding cess)?',
    options: [
      { text: '\\(₹0\\) (Nil)', isCorrect: true },
      { text: '\\(₹2,400\\)', isCorrect: false },
      { text: '\\(₹12,000\\)', isCorrect: false },
      { text: '\\(₹5,000\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Under standard tax slab Table 1 (individuals up to 60 years), income up to \\(₹2,50,000\\) is completely exempt from income tax (Tax rate = Nil).\n2. Since \\(₹2,40,000 \\le ₹2,50,000\\), tax liability is \\(₹0\\).'
  },

  // --- Subtopic 6.3.2: Deductions under section 80C up to 1.5 Lakh [MH-9-MTH1-6-6.3.2] ---
  {
    questionCode: 'MH-9-MTH1-6-6.3.2-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.3.2',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.2',
    topic: 'Deductions under section 80C up to 1.5 Lakh',
    topicName: 'Deductions under Section 80C up to 1.5 Lakh',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Section 80C Maximum Limit',
    text: 'What is the maximum permissible investment deduction limit allowed under Section 80C of the Income Tax Act?',
    options: [
      { text: '\\(₹1,50,000\\) (1.5 Lakh)', isCorrect: true },
      { text: '\\(₹1,00,000\\) (1 Lakh)', isCorrect: false },
      { text: '\\(₹2,00,000\\) (2 Lakh)', isCorrect: false },
      { text: '\\(₹2,50,000\\) (2.5 Lakh)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Section 80C of the Income Tax Act allows a maximum deduction of \\(₹1,50,000\\) per financial year for specified savings and investments.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.2-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.3.2',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.2',
    topic: 'Deductions under section 80C up to 1.5 Lakh',
    topicName: 'Deductions under Section 80C up to 1.5 Lakh',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Deduction Cap Application',
    text: 'Smt. Anjali invests \\(₹1,20,000\\) in PPF, \\(₹50,000\\) in Life Insurance Premium (LIC), and \\(₹20,000\\) in National Savings Certificates (NSC). What is the total deduction she can claim under Section 80C?',
    options: [
      { text: '\\(₹1,50,000\\)', isCorrect: true },
      { text: '\\(₹1,90,000\\)', isCorrect: false },
      { text: '\\(₹1,20,000\\)', isCorrect: false },
      { text: '\\(₹1,70,000\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Total investments made = \\(₹1,20,000 + ₹50,000 + ₹20,000 = ₹1,90,000\\).\n2. However, the maximum allowable ceiling under Section 80C is \\(₹1,50,000\\).\n3. Therefore, she can claim only \\(₹1,50,000\\).'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.2-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.3.2',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.2',
    topic: 'Deductions under section 80C up to 1.5 Lakh',
    topicName: 'Deductions under Section 80C up to 1.5 Lakh',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Understand',
    conceptTag: 'Eligible 80C Investments',
    text: 'Which of the following expenditures/investments is eligible for deduction under Section 80C?',
    options: [
      { text: 'Children\'s school tuition fees, PPF, and EPF', isCorrect: true },
      { text: 'Dining in restaurants and hotel stays', isCorrect: false },
      { text: 'Purchase of gold jewellery for weddings', isCorrect: false },
      { text: 'Monthly mobile recharge bills', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Eligible instruments under Section 80C include Provident Fund (PF/PPF), tuition fees of up to two children, ELSS mutual funds, and life insurance premiums.\n2. Personal consumer expenses are non-deductible.'
  },

  // --- Subtopic 6.3.3: Tax slabs for general, senior, and super senior citizens [MH-9-MTH1-6-6.3.3] ---
  {
    questionCode: 'MH-9-MTH1-6-6.3.3-OSC-001',
    topicCode: 'MH-9-MTH1-6-6.3.3',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.3',
    topic: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    topicName: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'easy',
    bloomLevel: 'Remember',
    conceptTag: 'Senior Citizen Age Definition',
    text: 'In Indian income tax regulations, a "Senior Citizen" is defined as an individual resident whose age during the financial year is:',
    options: [
      { text: '60 years or more, but less than 80 years', isCorrect: true },
      { text: '50 years or more', isCorrect: false },
      { text: '65 years or more', isCorrect: false },
      { text: 'Above 80 years only', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. A Senior Citizen is a person aged 60 years up to 80 years.\n2. A Super Senior Citizen is a person aged 80 years or above.'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.3-OSC-002',
    topicCode: 'MH-9-MTH1-6-6.3.3',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.3',
    topic: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    topicName: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'exam',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'medium',
    bloomLevel: 'Apply',
    conceptTag: 'Super Senior Exemption Limit',
    text: 'What is the basic income tax exemption limit for a Super Senior Citizen (age 80 years and above) under Table 3?',
    options: [
      { text: '\\(₹5,00,000\\)', isCorrect: true },
      { text: '\\(₹3,00,000\\)', isCorrect: false },
      { text: '\\(₹2,50,000\\)', isCorrect: false },
      { text: '\\(₹10,00,000\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Exemption limits under standard tax tables:\n   - General citizens (<60 yrs): \\(₹2,50,000\\)\n   - Senior citizens (60–80 yrs): \\(₹3,00,000\\)\n   - Super senior citizens ($\\ge 80$ yrs): \\(₹5,00,000\\).\n2. Hence for a super senior citizen, income up to \\(₹5,00,000\\) is completely exempt (Nil tax).'
  },
  {
    questionCode: 'MH-9-MTH1-6-6.3.3-OSC-003',
    topicCode: 'MH-9-MTH1-6-6.3.3',
    parentTopicCode: 'MH-9-MTH1-6-6.3',
    topicNumber: '6.3.3',
    topic: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    topicName: 'Tax slabs for general citizens, senior citizens, and super senior citizens',
    parentTopicName: 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)',
    boardCode: 'MH',
    board: 'Maharashtra Board',
    class: '9',
    subjectCode: 'MTH1',
    subject: 'Mathematics Part - 1 (Algebra)',
    chapterNumber: 6,
    chapter: 'Financial Planning',
    vault: 'practice',
    examCategory: 'standard',
    type: 'OSC',
    marks: 4,
    difficulty: 'hard',
    bloomLevel: 'Apply',
    conceptTag: 'Calculate Income Tax Slab',
    text: 'A 50-year-old resident individual has a taxable income of \\(₹4,50,000\\). If the tax slab for \\(₹2,50,001\\) to \\(₹5,00,000\\) is \\(5\\%\\), what is the basic income tax payable (before cess)?',
    options: [
      { text: '\\(₹10,000\\)', isCorrect: true },
      { text: '\\(₹22,500\\)', isCorrect: false },
      { text: '\\(₹12,500\\)', isCorrect: false },
      { text: '\\(₹5,000\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: '1. Up to \\(₹2,50,000\\): Nil tax.\n2. Taxable amount in the 5% bracket: \\(₹4,50,000 - ₹2,50,000 = ₹2,00,000\\).\n3. Tax at 5%: \\(₹2,00,000 \\times \\frac{5}{100} = ₹10,000\\).'
  }
];

async function main() {
  console.log(`=== Step 1: Validating ${QUESTIONS.length} Questions for Chapter 6 Financial Planning ===`);
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
  console.log('All Chapter 6 questions passed strict validation perfectly!');

  console.log('=== Step 2: Atomic Pre-Mutation Snapshot (Rule 2Q) ===');
  await createPreMutationSnapshot(['questions'], 'populate_mh9_mth1_ch6_financial_planning');
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
  console.log(`Successfully committed ${QUESTIONS.length} validated questions to Firestore across Chapter 6 Financial Planning!`);
}

main().catch(console.error);
