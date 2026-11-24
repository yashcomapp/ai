const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const fs = require('fs');
const path = require('path');

async function comprehensiveMh9ScitAudit() {
  console.log('Starting Comprehensive Audit of MH-9-SCIT (Class 9 Science)...');

  const snap = await adminDb.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', '==', '9')
    .where('boardCode', '==', 'MH')
    .select(
      'questionCode',
      'text',
      'options',
      'correctAnswer',
      'solution',
      'explanation',
      'type',
      'numericalValue',
      'topicCode'
    )
    .get();

  console.log(`Fetched ${snap.size} total questions in MH-9-SCIT.`);

  const anomalies = [];
  const getOptText = (opt) => {
    if (!opt) return '';
    if (typeof opt === 'object') return (opt.text || opt.value || opt.label || '').trim();
    return String(opt).trim();
  };

  snap.forEach(doc => {
    const q = doc.data();
    const docId = doc.id;
    const qCode = q.questionCode || docId;
    const type = q.type || 'OSC';
    const cAns = String(q.correctAnswer || '').trim().toUpperCase();
    const sol = (q.solution || q.explanation || '').trim();
    const options = Array.isArray(q.options) ? q.options : [];

    if (!sol || sol.length < 5) return;

    // Check 1: Explicit letter in solution
    // Looking for unambiguous patterns like:
    // "Correct Choice is (X)"
    // "Correct Choice is X."
    // "Correct Choice: (X)"
    // "Correct Option is (X)"
    // "Option (X) is correct"
    // "Correct Answer is (X)"
    const letterPatterns = [
      /Correct\s+Choice\s+is\s+\(?([A-D])\)?/i,
      /Correct\s+Choice:\s*\(?([A-D])\)?/i,
      /Correct\s+Option\s+is\s+\(?([A-D])\)?/i,
      /Option\s+\(?([A-D])\)?\s+is\s+correct/i,
      /Correct\s+Answer\s+is\s+\(([A-D])\)/i
    ];

    let statedLetter = null;
    let matchedPattern = null;

    for (const pat of letterPatterns) {
      const m = sol.match(pat);
      if (m && m[1]) {
        statedLetter = m[1].toUpperCase();
        matchedPattern = m[0];
        break;
      }
    }

    if (statedLetter && statedLetter !== cAns && ['A', 'B', 'C', 'D'].includes(statedLetter) && ['A', 'B', 'C', 'D'].includes(cAns)) {
      anomalies.push({
        docId,
        qCode,
        type,
        topicCode: q.topicCode || '',
        issue: 'EXPLANATION_LETTER_MISMATCH',
        statedLetter,
        currentCorrectAnswer: cAns,
        matchedPattern,
        text: (q.text || '').slice(0, 100),
        options: options.map((o, idx) => `${String.fromCharCode(65 + idx)}: ${getOptText(o)}`),
        solutionSnippet: sol.slice(0, 200)
      });
    }

    // Check 2: Options isCorrect contradiction
    if (options.length > 0 && typeof options[0] === 'object' && options[0] !== null) {
      const correctIdxs = [];
      options.forEach((opt, idx) => {
        if (opt && (opt.isCorrect === true || opt.correct === true)) {
          correctIdxs.push(idx);
        }
      });

      if (correctIdxs.length === 1) {
        const flagLetter = String.fromCharCode(65 + correctIdxs[0]);
        if (flagLetter !== cAns && ['A', 'B', 'C', 'D'].includes(cAns)) {
          anomalies.push({
            docId,
            qCode,
            type,
            topicCode: q.topicCode || '',
            issue: 'OPTION_IS_CORRECT_CONTRADICTION',
            flagLetter,
            currentCorrectAnswer: cAns,
            text: (q.text || '').slice(0, 100),
            options: options.map((o, idx) => `${String.fromCharCode(65 + idx)}: ${getOptText(o)}`),
            solutionSnippet: sol.slice(0, 200)
          });
        }
      }
    }
  });

  console.log(`\n======================================================`);
  console.log(`COMPREHENSIVE AUDIT RESULT FOR MH-9-SCIT`);
  console.log(`Total questions checked: ${snap.size}`);
  console.log(`Total anomalies found:   ${anomalies.length}`);
  console.log(`======================================================\n`);

  anomalies.forEach((a, i) => {
    console.log(`[${i + 1}] ID: ${a.docId} (${a.qCode}) - Type: ${a.type} - Issue: ${a.issue}`);
    console.log(`Text: ${a.text}`);
    console.log(`Current Answer: ${a.currentCorrectAnswer} | Detected: ${a.statedLetter || a.flagLetter}`);
    console.log(`Options:`, a.options);
    console.log(`Solution snippet: ${a.solutionSnippet}\n`);
  });

  return anomalies;
}

comprehensiveMh9ScitAudit().catch(console.error);
