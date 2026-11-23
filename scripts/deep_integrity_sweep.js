const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');
const fs = require('fs');

async function runDeepIntegritySweep() {
  console.log('================================================================================');
  console.log('=== LOS-NEXT COMPREHENSIVE QUESTION BANK INTEGRITY & QUALITY AUDIT SWEEP ===');
  console.log('================================================================================');
  console.log('Scanning all questions in Firestore using select() stream for cost & memory efficiency...\n');

  const stats = {
    totalScanned: 0,
    byClass: { '8': 0, '9': 0, '10': 0, other: 0 },
    issues: {
      placeholders: [],
      jokeQuestions: [],
      relativeReferences: [], // "in previous question", "above question"
      brokenLatex: [],
      missingOptions: [],
      duplicateOptionsWithinQuestion: [],
      emptyOptionText: [],
      invalidCorrectAnswer: [],
      missingSolution: [],
      identicalStemsInSameTopic: []
    }
  };

  // Regular expressions for anomalies
  const placeholderRegex = /\b(lorem\s+ipsum|placeholder|sample\s+question|test\s+question|dummy\s+text|temp\s+question|asdf|foo\s+bar|\btodo\b|\btbd\b|to\s+be\s+added|temp\s+data)\b/i;
  const jokeRegex = /\b(chicken\s+cross|batman|superman|sponge\s*bob|mickey\s*mouse|funny\s+question|joke|hahaha|rofl)\b/i;
  const relativeRefRegex = /\b(in\s+the\s+previous\s+question|as\s+mentioned\s+above|refer\s+to\s+(the\s+)?above|from\s+the\s+above\s+question|in\s+part\s+[a-d]\s+above|in\s+the\s+earlier\s+question|referring\s+to\s+question|from\s+the\s+preceding\s+question|in\s+the\s+next\s+question)\b/i;

  // Stream all questions
  const query = adminDb.collection('questions')
    .select(
      'questionCode',
      'text',
      'options',
      'correctAnswer',
      'solution',
      'explanation',
      'type',
      'topicCode',
      'class',
      'subjectCode'
    );

  const stream = query.stream();

  // For checking exact identical stems within same topic
  const topicStemMap = new Map(); // topicCode -> Map(stem -> [questionCode])

  let count = 0;
  for await (const doc of stream) {
    count++;
    stats.totalScanned++;
    const data = doc.data();
    const qCode = data.questionCode || doc.id;
    const cls = String(data.class || 'other');
    if (stats.byClass[cls] !== undefined) {
      stats.byClass[cls]++;
    } else {
      stats.byClass.other++;
    }

    const text = (data.text || '').trim();
    const sol = (data.solution || data.explanation || '').trim();
    const type = data.type || 'OSC';
    const tc = data.topicCode || 'UNKNOWN';

    // 1. Placeholder check in stem and solution
    if (placeholderRegex.test(text) || placeholderRegex.test(sol)) {
      stats.issues.placeholders.push({ qCode, text: text.slice(0, 80), tc });
    }

    // 2. Joke / Absurd content check
    if (jokeRegex.test(text) || jokeRegex.test(sol)) {
      stats.issues.jokeQuestions.push({ qCode, text: text.slice(0, 80), tc });
    }

    // 3. Relative reference check ("as above", "in previous question")
    if (relativeRefRegex.test(text)) {
      stats.issues.relativeReferences.push({ qCode, text: text.slice(0, 80), tc });
    }

    // 4. Broken LaTeX delimiter checks
    const openParenCount = (text.match(/\\\(/g) || []).length;
    const closeParenCount = (text.match(/\\\)/g) || []).length;
    const openBracketCount = (text.match(/\\\[/g) || []).length;
    const closeBracketCount = (text.match(/\\\]/g) || []).length;

    if (openParenCount !== closeParenCount || openBracketCount !== closeBracketCount) {
      stats.issues.brokenLatex.push({
        qCode,
        openParen: openParenCount,
        closeParen: closeParenCount,
        openBracket: openBracketCount,
        closeBracket: closeBracketCount,
        text: text.slice(0, 80)
      });
    }

    // 5. Options Integrity (for OSC / OMC)
    if (type === 'OSC' || type === 'OMC' || type === 'OTF') {
      const opts = data.options || [];
      const expectedCount = type === 'OTF' ? 2 : 4;
      
      if (opts.length !== expectedCount) {
        // Some legacy questions might have different length, record it
        stats.issues.missingOptions.push({ qCode, count: opts.length, expected: expectedCount, type });
      }

      // Check duplicate options within same question
      const optTexts = [];
      let hasEmptyOpt = false;
      for (const opt of opts) {
        const oText = (typeof opt === 'object' && opt !== null) ? (opt.text || '') : String(opt);
        const norm = oText.trim().toLowerCase();
        if (!norm) {
          hasEmptyOpt = true;
        } else {
          optTexts.push(norm);
        }
      }

      if (hasEmptyOpt) {
        stats.issues.emptyOptionText.push({ qCode, tc });
      }

      const uniqueSet = new Set(optTexts);
      if (uniqueSet.size < optTexts.length) {
        stats.issues.duplicateOptionsWithinQuestion.push({
          qCode,
          tc,
          options: optTexts
        });
      }

      // Check correctAnswer validity
      const corr = data.correctAnswer;
      if (!corr || !['A', 'B', 'C', 'D'].includes(String(corr).toUpperCase())) {
        if (type !== 'ONE') {
          stats.issues.invalidCorrectAnswer.push({ qCode, corr, type });
        }
      }
    }

    // 6. Solution Integrity
    if (!sol || sol.length < 15) {
      stats.issues.missingSolution.push({ qCode, solLength: sol ? sol.length : 0, tc });
    }

    // 7. Duplicate Stem in Same Topic Check
    if (text.length > 20) {
      if (!topicStemMap.has(tc)) {
        topicStemMap.set(tc, new Map());
      }
      const stemMap = topicStemMap.get(tc);
      const cleanStem = text.replace(/\\\([^)]+\\\)/g, 'MATH').replace(/\s+/g, ' ').toLowerCase();
      if (stemMap.has(cleanStem)) {
        stemMap.get(cleanStem).push(qCode);
      } else {
        stemMap.set(cleanStem, [qCode]);
      }
    }

    if (count % 10000 === 0) {
      console.log(`... processed ${count} questions`);
    }
  }

  // Extract identical stems within same topic
  for (const [tc, stemMap] of topicStemMap.entries()) {
    for (const [stem, qCodes] of stemMap.entries()) {
      if (qCodes.length > 1) {
        stats.issues.identicalStemsInSameTopic.push({
          tc,
          count: qCodes.length,
          stem: stem.slice(0, 80),
          qCodes: qCodes.slice(0, 5)
        });
      }
    }
  }

  console.log('\n================================================================================');
  console.log('=== AUDIT RESULTS SUMMARY ===');
  console.log('================================================================================');
  console.log(`Total Questions Scanned:   ${stats.totalScanned}`);
  console.log(`  Class 8:                 ${stats.byClass['8']}`);
  console.log(`  Class 9:                 ${stats.byClass['9']}`);
  console.log(`  Class 10:                ${stats.byClass['10']}`);
  console.log(`  Other / Unassigned:      ${stats.byClass.other}`);
  console.log('--------------------------------------------------------------------------------');
  console.log(`1. Placeholders (TODO, lorem, test...):       ${stats.issues.placeholders.length}`);
  console.log(`2. Joke / Absurd Questions:                   ${stats.issues.jokeQuestions.length}`);
  console.log(`3. Relative References ("as above", etc.):    ${stats.issues.relativeReferences.length}`);
  console.log(`4. Broken LaTeX Delimiters:                   ${stats.issues.brokenLatex.length}`);
  console.log(`5. Missing / Abnormal Option Counts:          ${stats.issues.missingOptions.length}`);
  console.log(`6. Duplicate Options Within Same Question:    ${stats.issues.duplicateOptionsWithinQuestion.length}`);
  console.log(`7. Empty Option Strings:                      ${stats.issues.emptyOptionText.length}`);
  console.log(`8. Invalid / Missing Correct Answer:          ${stats.issues.invalidCorrectAnswer.length}`);
  console.log(`9. Missing / Short (<15 chars) Solutions:     ${stats.issues.missingSolution.length}`);
  console.log(`10. Identical Stems within Same Topic:        ${stats.issues.identicalStemsInSameTopic.length}`);
  console.log('================================================================================');

  fs.mkdirSync('./scripts/audit_data', { recursive: true });
  fs.writeFileSync('./scripts/audit_data/integrity_sweep_report.json', JSON.stringify(stats, null, 2));
  console.log('Detailed JSON report saved to scripts/audit_data/integrity_sweep_report.json');

  // Print sample details if any issues found
  if (stats.issues.placeholders.length > 0) {
    console.log('\n[!] Sample Placeholders:');
    console.log(JSON.stringify(stats.issues.placeholders.slice(0, 3), null, 2));
  }
  if (stats.issues.jokeQuestions.length > 0) {
    console.log('\n[!] Sample Joke Questions:');
    console.log(JSON.stringify(stats.issues.jokeQuestions.slice(0, 3), null, 2));
  }
  if (stats.issues.relativeReferences.length > 0) {
    console.log('\n[!] Sample Relative References:');
    console.log(JSON.stringify(stats.issues.relativeReferences.slice(0, 3), null, 2));
  }
  if (stats.issues.duplicateOptionsWithinQuestion.length > 0) {
    console.log('\n[!] Sample Duplicate Options:');
    console.log(JSON.stringify(stats.issues.duplicateOptionsWithinQuestion.slice(0, 3), null, 2));
  }
  if (stats.issues.brokenLatex.length > 0) {
    console.log('\n[!] Sample Broken LaTeX:');
    console.log(JSON.stringify(stats.issues.brokenLatex.slice(0, 3), null, 2));
  }
  if (stats.issues.missingSolution.length > 0) {
    console.log('\n[!] Sample Missing Solutions:');
    console.log(JSON.stringify(stats.issues.missingSolution.slice(0, 3), null, 2));
  }

  process.exit(0);
}

runDeepIntegritySweep().catch(err => {
  console.error('Fatal error during sweep:', err);
  process.exit(1);
});
