const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (sa) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
}
const db = admin.firestore();

const CANONICAL_TYPES = new Set([
  'OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE',
  'SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'
]);
const CANONICAL_BLOOMS = new Set([
  'remember', 'understand', 'apply', 'analyze', 'evaluate', 'create'
]);
const CANONICAL_DIFFS = new Set(['easy', 'medium', 'hard']);

async function auditWholeQuestionBank() {
  console.log('--- Fetching all questions from Firestore for forensic deep audit ---');
  const snap = await db.collection('questions').get();
  console.log(`Fetched ${snap.size} total questions.`);

  const issues = {
    badDifficulty: [],
    badBloomLevel: [],
    badType: [],
    missingOptions: [],
    placeholderOptions: [],
    duplicateOptions: [],
    oscKeyMismatch: [],
    otfKeyMismatch: [],
    oneMissingNumerical: [],
    emptySolution: [],
    badMarks: [],
    invalidTopicCode: []
  };

  snap.forEach(doc => {
    const q = doc.data();
    const id = doc.id;
    const type = (q.type || q.typeCode || '').toUpperCase();

    // 1. Difficulty
    const rawDiff = String(q.difficulty || '').trim().toLowerCase();
    if (!CANONICAL_DIFFS.has(rawDiff)) {
      issues.badDifficulty.push({ id, topicCode: q.topicCode, difficulty: q.difficulty });
    }

    // 2. Bloom Level
    const rawBloom = String(q.bloomLevel || '').trim().toLowerCase();
    if (!CANONICAL_BLOOMS.has(rawBloom)) {
      issues.badBloomLevel.push({ id, topicCode: q.topicCode, bloomLevel: q.bloomLevel });
    }

    // 3. Question Type
    if (!CANONICAL_TYPES.has(type)) {
      issues.badType.push({ id, topicCode: q.topicCode, type: q.type, typeCode: q.typeCode });
    }

    // 4. Options checks
    const isObjective = ['OSC', 'OMC', 'OTF', 'OAR'].includes(type);
    if (isObjective) {
      const opts = Array.isArray(q.options) ? q.options : [];
      if (opts.length === 0) {
        issues.missingOptions.push({ id, type, reason: 'Empty options array' });
      } else if (type === 'OTF' && opts.length !== 2) {
        issues.missingOptions.push({ id, type, reason: `OTF has ${opts.length} options instead of 2` });
      } else if (['OSC', 'OMC', 'OAR'].includes(type) && opts.length < 2) {
        issues.missingOptions.push({ id, type, reason: `${type} has only ${opts.length} option` });
      }

      // Check placeholder options & duplicates
      const optTexts = opts.map(o => typeof o === 'object' ? (o.text || o.value || '') : String(o));
      for (const t of optTexts) {
        const cleanT = t.trim();
        if (/^Option\s+[A-D]$/i.test(cleanT) || /^Option\s+[A-D]\s*\(/i.test(cleanT) || /placeholder/i.test(cleanT)) {
          issues.placeholderOptions.push({ id, type, optText: cleanT });
          break;
        }
      }
      const uniqueTexts = new Set(optTexts.map(t => t.trim().toLowerCase()));
      if (uniqueTexts.size < optTexts.length && optTexts.length > 0) {
        issues.duplicateOptions.push({ id, type, optTexts });
      }

      // 5. Answer Key Mismatch for OSC
      if (type === 'OSC') {
        const cAns = String(q.correctAnswer || '').trim().toUpperCase();
        if (!['A', 'B', 'C', 'D'].includes(cAns)) {
          issues.oscKeyMismatch.push({ id, reason: `Invalid correctAnswer letter: "${q.correctAnswer}"` });
        } else {
          const letterIdx = cAns.charCodeAt(0) - 65;
          if (letterIdx >= opts.length) {
            issues.oscKeyMismatch.push({ id, reason: `correctAnswer ${cAns} out of bounds for ${opts.length} options` });
          }
        }
        // If options are objects with isCorrect
        const objOpts = opts.filter(o => typeof o === 'object' && o !== null && o.isCorrect !== undefined);
        if (objOpts.length > 0) {
          const trueIndices = opts.map((o, idx) => (o && typeof o === 'object' && o.isCorrect === true) ? idx : -1).filter(i => i !== -1);
          if (trueIndices.length === 1) {
            const expectedLetter = String.fromCharCode(65 + trueIndices[0]);
            if (cAns && cAns !== expectedLetter && ['A', 'B', 'C', 'D'].includes(cAns)) {
              issues.oscKeyMismatch.push({ id, reason: `Option object isCorrect=true at index ${trueIndices[0]} (${expectedLetter}) but correctAnswer is ${cAns}` });
            }
          }
        }
      }

      // 6. Answer Key Mismatch for OTF
      if (type === 'OTF' && opts.length === 2) {
        const cAns = String(q.correctAnswer || '').trim();
        const cAnsList = Array.isArray(q.correctAnswers) ? q.correctAnswers : [];
        if (cAnsList.length > 0) {
          const opt0 = optTexts[0].toLowerCase();
          const opt1 = optTexts[1].toLowerCase();
          const truth = String(cAnsList[0]).toLowerCase();
          let expectedLetter = '';
          if (opt0 === truth) expectedLetter = 'A';
          else if (opt1 === truth) expectedLetter = 'B';
          if (expectedLetter && cAns.toUpperCase() !== expectedLetter && ['A', 'B'].includes(cAns.toUpperCase())) {
            issues.otfKeyMismatch.push({ id, opt0, opt1, truth, cAns, expectedLetter });
          }
        }
      }
    }

    // 7. Numerical Objective checks
    if (type === 'ONE') {
      if (q.numericalValue === undefined || q.numericalValue === null || isNaN(Number(q.numericalValue))) {
        // check if correctAnswer is numeric
        const numVal = parseFloat(String(q.correctAnswer || ''));
        if (isNaN(numVal)) {
          issues.oneMissingNumerical.push({ id, numericalValue: q.numericalValue, correctAnswer: q.correctAnswer });
        }
      }
    }

    // 8. Empty solution
    if (!q.solution || String(q.solution).trim() === '') {
      issues.emptySolution.push({ id, type });
    }

    // 9. Marks
    if (typeof q.marks !== 'number' || q.marks <= 0) {
      issues.badMarks.push({ id, marks: q.marks });
    }
  });

  console.log('\n=== AUDIT RESULTS SUMMARY ===');
  console.log(`1. Bad Difficulty: ${issues.badDifficulty.length}`);
  console.log(`2. Bad Bloom Level: ${issues.badBloomLevel.length}`);
  console.log(`3. Bad Question Type: ${issues.badType.length}`);
  console.log(`4. Missing / Irregular Options: ${issues.missingOptions.length}`);
  console.log(`5. Placeholder Options: ${issues.placeholderOptions.length}`);
  console.log(`6. Duplicate Options: ${issues.duplicateOptions.length}`);
  console.log(`7. OSC Answer Key Mismatches: ${issues.oscKeyMismatch.length}`);
  console.log(`8. OTF Answer Key Mismatches: ${issues.otfKeyMismatch.length}`);
  console.log(`9. ONE Missing Numerical Values: ${issues.oneMissingNumerical.length}`);
  console.log(`10. Empty Solutions: ${issues.emptySolution.length}`);
  console.log(`11. Bad / Invalid Marks: ${issues.badMarks.length}`);

  fs.writeFileSync('qb_audit_full_report.json', JSON.stringify(issues, null, 2), 'utf-8');
  console.log('\nWrote full audit report to qb_audit_full_report.json');
}

auditWholeQuestionBank().catch(console.error);
