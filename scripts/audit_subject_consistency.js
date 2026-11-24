const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const fs = require('fs');
const path = require('path');

// Core audit logic for a single question
function checkQuestionConsistency(q, docId) {
  const issues = [];
  const qCode = q.questionCode || docId;
  const type = q.type || 'OSC';
  const cAns = String(q.correctAnswer || '').trim().toUpperCase();
  const sol = (q.solution || q.explanation || '').trim();
  const options = Array.isArray(q.options) ? q.options : [];

  if (!sol || sol.length < 5) {
    // Missing solution
    return null;
  }

  // Helper to extract option text
  const getOptText = (idx) => {
    if (idx < 0 || idx >= options.length) return '';
    const opt = options[idx];
    if (typeof opt === 'object' && opt !== null) {
      return (opt.text || opt.value || opt.label || '').trim();
    }
    return String(opt).trim();
  };

  // 1. Check: Explanation explicitly states "Correct Choice is (X)" or "Correct Answer is (X)"
  const choiceMatches = [
    ...sol.matchAll(/Correct\s+(?:Choice|Option)\s+(?:is\s+)?\(?([A-D])\)?/gi),
    ...sol.matchAll(/Correct\s+Answer\s+is\s+\(?([A-D])\)?/gi),
    ...sol.matchAll(/Option\s+\(?([A-D])\)?\s+is\s+correct/gi)
  ];

  if (choiceMatches.length > 0) {
    const lastMatch = choiceMatches[choiceMatches.length - 1];
    const statedLetter = lastMatch[1].toUpperCase();
    if (statedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(statedLetter)) {
      issues.push({
        type: 'STATED_CHOICE_MISMATCH',
        statedInExplanation: statedLetter,
        currentCorrectAnswer: cAns,
        matchedPhrase: lastMatch[0],
        confidence: 'HIGH'
      });
    }
  }

  // 2. Check: Object-based options with isCorrect flag
  if (options.length > 0 && typeof options[0] === 'object' && options[0] !== null) {
    const correctIndices = [];
    options.forEach((opt, idx) => {
      if (opt && (opt.isCorrect === true || opt.correct === true)) {
        correctIndices.push(idx);
      }
    });

    if (correctIndices.length === 1) {
      const expectedLetter = String.fromCharCode(65 + correctIndices[0]);
      if (expectedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(cAns)) {
        issues.push({
          type: 'OPTION_IS_CORRECT_MISMATCH',
          flaggedInOptions: expectedLetter,
          currentCorrectAnswer: cAns,
          confidence: 'HIGH'
        });
      }
    }
  }

  // 3. Check: Numerical Objective (ONE) where explanation calculates a number
  // e.g. "Correct Answer is 3000" or "= 3000 W"
  if (type === 'ONE' || qCode.includes('-ONE-')) {
    const numMatch = sol.match(/Correct\s+Answer\s+is\s+([0-9.]+)/i);
    if (numMatch) {
      const calcNum = parseFloat(numMatch[1]);

      // Check against numericalValue
      if (q.numericalValue !== undefined && Math.abs(parseFloat(q.numericalValue) - calcNum) > 0.05) {
        issues.push({
          type: 'NUMERICAL_VALUE_MISMATCH',
          calculatedInExplanation: calcNum,
          currentNumericalValue: q.numericalValue,
          confidence: 'HIGH'
        });
      }

      // Check if options exist: which option matches calcNum?
      if (options.length > 0) {
        let matchingIdx = -1;
        options.forEach((opt, idx) => {
          const txt = getOptText(idx).replace(/\\text\{[^}]+\}/g, '').replace(/[^0-9.]/g, '');
          const val = parseFloat(txt);
          if (!isNaN(val) && Math.abs(val - calcNum) < 0.05) {
            matchingIdx = idx;
          }
        });

        if (matchingIdx !== -1) {
          const matchingLetter = String.fromCharCode(65 + matchingIdx);
          if (matchingLetter !== cAns) {
            issues.push({
              type: 'NUMERICAL_OPTION_KEY_MISMATCH',
              calculatedNumber: calcNum,
              matchingOptionLetter: matchingLetter,
              currentCorrectAnswer: cAns,
              confidence: 'HIGH'
            });
          }
        }
      }
    }
  }

  // 4. Check: Assertion-Reason (OAR)
  if (type === 'OAR' || qCode.includes('-OAR-')) {
    const solLower = sol.toLowerCase();
    let deducedLetter = null;
    if (solLower.includes('assertion is false') || solLower.includes('assertion (a) is false')) {
      deducedLetter = 'D';
    } else if (solLower.includes('reason is false') || solLower.includes('reason (r) is false')) {
      deducedLetter = 'C';
    } else if (solLower.includes('not the correct explanation') || solLower.includes('is not the correct explanation')) {
      deducedLetter = 'B';
    } else if (solLower.includes('correct explanation of a') || solLower.includes('correct explanation of assertion')) {
      deducedLetter = 'A';
    }

    if (deducedLetter && deducedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(cAns)) {
      issues.push({
        type: 'ASSERTION_REASON_MISMATCH',
        deducedFromExplanation: deducedLetter,
        currentCorrectAnswer: cAns,
        confidence: 'MEDIUM'
      });
    }
  }

  // 5. Check: True/False (OTF)
  if (type === 'OTF' || qCode.includes('-OTF-')) {
    const solLower = sol.toLowerCase();
    let deducedAns = null;
    if (solLower.includes('statement is true') || solLower.includes('evaluates to true') || solLower.includes('correct answer: true')) {
      deducedAns = 'True';
    } else if (solLower.includes('statement is false') || solLower.includes('evaluates to false') || solLower.includes('correct answer: false')) {
      deducedAns = 'False';
    }

    if (deducedAns) {
      const isActuallyTrue = cAns === 'TRUE' || cAns === 'A';
      const isActuallyFalse = cAns === 'FALSE' || cAns === 'B';
      if ((deducedAns === 'True' && isActuallyFalse) || (deducedAns === 'False' && isActuallyTrue)) {
        issues.push({
          type: 'TRUE_FALSE_MISMATCH',
          deducedFromExplanation: deducedAns,
          currentCorrectAnswer: cAns,
          confidence: 'HIGH'
        });
      }
    }
  }

  if (issues.length > 0) {
    return {
      docId,
      qCode,
      topicCode: q.topicCode || '',
      type,
      text: (q.text || '').slice(0, 100),
      currentCorrectAnswer: cAns,
      solutionSnippet: sol.slice(0, 150),
      options: options.map((o, idx) => `${String.fromCharCode(65 + idx)}: ${getOptText(idx)}`),
      issues
    };
  }

  return null;
}

async function auditSubject(subjectCode = 'SCIT', classVal = '9', board = 'MH') {
  console.log(`Auditing Subject: ${board} Class ${classVal} ${subjectCode}...`);

  // Query only questions for this subject to minimize reads
  let q = adminDb.collection('questions')
    .where('subjectCode', '==', subjectCode)
    .where('class', '==', String(classVal));

  if (board) {
    q = q.where('boardCode', '==', board);
  }

  const query = q.select(
    'questionCode',
    'text',
    'options',
    'correctAnswer',
    'solution',
    'explanation',
    'type',
    'numericalValue',
    'topicCode',
    'class',
    'subjectCode',
    'boardCode'
  );

  const snap = await query.get();
  console.log(`Fetched ${snap.size} questions for ${board} Class ${classVal} ${subjectCode}`);

  const anomalies = [];
  snap.forEach(doc => {
    const result = checkQuestionConsistency(doc.data(), doc.id);
    if (result) {
      anomalies.push(result);
    }
  });

  console.log(`Total anomalies detected: ${anomalies.length}`);

  const outDir = path.join(__dirname, 'audit_data');
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  const outFile = path.join(outDir, `audit_${board}_${classVal}_${subjectCode}.json`);
  fs.writeFileSync(outFile, JSON.stringify(anomalies, null, 2), 'utf8');
  console.log(`Saved report to ${outFile}`);

  // Display top 10 anomalies
  anomalies.slice(0, 10).forEach((a, i) => {
    console.log(`\n[${i + 1}] ID: ${a.docId} (${a.qCode}) - Topic: ${a.topicCode}`);
    console.log(`Text: ${a.text}`);
    console.log(`Current Answer: ${a.currentCorrectAnswer}`);
    console.log(`Issues:`, a.issues);
  });

  return anomalies;
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const subject = args[0] || 'SCIT';
  const cls = args[1] || '9';
  const board = args[2] || 'MH';
  auditSubject(subject, cls, board).catch(console.error);
}

module.exports = { checkQuestionConsistency, auditSubject };
