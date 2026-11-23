const fs = require('fs');

function validateBatch(filePath) {
  console.log(`=== VALIDATING BATCH: ${filePath} ===`);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  console.log(`Loaded ${data.length} questions.`);

  let errors = [];

  data.forEach((q, idx) => {
    const prefix = `[Q #${idx + 1} - ${q.questionCode || 'NO_CODE'}]`;

    // 1. Question Code
    if (!q.questionCode || !q.questionCode.includes('-OSC-')) {
      errors.push(`${prefix} Invalid questionCode`);
    }

    // 2. Text
    if (!q.text || q.text.trim().length < 10) {
      errors.push(`${prefix} Question text too short or missing`);
    }

    // 3. Options
    if (!Array.isArray(q.options) || q.options.length !== 4) {
      errors.push(`${prefix} Must have exactly 4 options, found: ${q.options ? q.options.length : 0}`);
    } else {
      const optTexts = new Set();
      let correctCount = 0;
      let matchedCorrect = false;

      q.options.forEach((opt, oIdx) => {
        if (!opt.text || opt.text.trim().length === 0) {
          errors.push(`${prefix} Option ${opt.id || oIdx} is empty`);
        }
        const lower = opt.text.trim().toLowerCase();
        if (optTexts.has(lower)) {
          errors.push(`${prefix} Duplicate option text detected: "${opt.text}"`);
        }
        optTexts.add(lower);

        if (opt.isCorrect) {
          correctCount++;
          if (opt.id === q.correctAnswer) {
            matchedCorrect = true;
          }
        }
      });

      if (correctCount !== 1) {
        errors.push(`${prefix} Expected exactly 1 isCorrect: true, found ${correctCount}`);
      }
      if (!matchedCorrect) {
        errors.push(`${prefix} correctAnswer "${q.correctAnswer}" does not match isCorrect: true option`);
      }
    }

    // 4. Solution
    if (!q.solution) {
      errors.push(`${prefix} Missing solution`);
    } else {
      if (!q.solution.includes('**Step 1:**') || !q.solution.includes('**Step 2:**') || !q.solution.includes('**Step 3:**')) {
        errors.push(`${prefix} Solution missing 3-step structured format (**Step 1:**, **Step 2:**, **Step 3:**)`);
      }
    }

    // 5. Vault
    if (!['exam', 'practice', 'foundation'].includes(q.vault)) {
      errors.push(`${prefix} Invalid vault: "${q.vault}"`);
    }

    // 6. TopicCode
    if (!q.topicCode || q.topicCode.length < 5) {
      errors.push(`${prefix} Missing topicCode`);
    }
  });

  if (errors.length > 0) {
    console.error(`❌ VALIDATION FAILED with ${errors.length} errors:`);
    errors.slice(0, 15).forEach(e => console.error('  ' + e));
    process.exit(1);
  } else {
    console.log(`✅ ALL ${data.length} QUESTIONS PASSED 100% VALIDATION WITH 0 ERRORS!\n`);
  }
}

const fileToValidate = process.argv[2] || 'scripts/cbse8_mgp1_ch1_topup.json';
validateBatch(fileToValidate);
