const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function runAudit() {
  console.log('=== FULL COMPREHENSIVE QUESTION BANK AUDIT ===');
  console.log('Fetching all questions from Firestore...');

  const snap = await db.collection('questions').get();
  console.log(`Total questions in DB: ${snap.size}`);

  const topicStats = {};
  const issues = {
    missingText: [],
    shortText: [],
    missingOptions: [],
    lessThanTwoOptions: [],
    placeholderOptions: [],
    duplicateOptions: [],
    missingExplanation: [],
    trivialExplanation: [],
    allOptionATopics: [],
    dominantOptionATopics: []
  };

  const overallAnswerDist = { A: 0, B: 0, C: 0, D: 0, other: 0, subjective: 0 };

  snap.docs.forEach(doc => {
    const d = doc.data();
    const id = doc.id;
    const qCode = d.questionCode || id;
    const qType = (d.type || 'OSC').toUpperCase();
    const topicCode = d.topicCode || (qCode.split('-').slice(0, 5).join('-'));
    const subject = d.subject || (qCode.split('-')[2] || 'UNKNOWN');
    const text = (d.text || d.questionText || '').trim();
    const explanation = (d.explanation || d.solution || '').trim();
    const options = d.options || [];

    if (!topicStats[topicCode]) {
      topicStats[topicCode] = {
        total: 0,
        objective: 0,
        subjective: 0,
        dist: { A: 0, B: 0, C: 0, D: 0, other: 0 },
        subject,
        docIds: []
      };
    }
    const tStat = topicStats[topicCode];
    tStat.total++;
    tStat.docIds.push(id);

    // Check Question Text
    if (!text) {
      issues.missingText.push({ id, qCode, topicCode });
    } else if (text.length < 10) {
      issues.shortText.push({ id, qCode, text, topicCode });
    }

    const isObjective = ['OSC', 'OMC', 'OTF', 'OAR'].includes(qType);
    if (!isObjective) {
      tStat.subjective++;
      overallAnswerDist.subjective++;
      return;
    }

    tStat.objective++;

    // Check Answer
    let ans = String(d.correctAnswer || '').trim().toUpperCase();
    if (ans.startsWith('OPTION ')) ans = ans.replace('OPTION ', '').trim();
    if (['A', 'B', 'C', 'D'].includes(ans)) {
      overallAnswerDist[ans]++;
      tStat.dist[ans]++;
    } else {
      overallAnswerDist.other++;
      tStat.dist.other++;
    }

    // Check Options
    if (!Array.isArray(options) || options.length === 0) {
      issues.missingOptions.push({ id, qCode, topicCode });
    } else if (options.length < 2) {
      issues.lessThanTwoOptions.push({ id, qCode, optionsLength: options.length, topicCode });
    } else {
      const optTexts = options.map(o => (typeof o === 'object' ? (o.text || '') : String(o || '')).trim());
      
      // Check for placeholder options like "Option A", "Option B", empty, null
      const hasPlaceholder = optTexts.some(o => 
        !o || 
        /^option\s*[a-d]$/i.test(o) || 
        /^(dummy|placeholder|text|sample)$/i.test(o)
      );
      if (hasPlaceholder) {
        issues.placeholderOptions.push({ id, qCode, optTexts, topicCode });
      }

      // Check duplicate options
      const nonEmpties = optTexts.filter(Boolean);
      const uniqueOpts = new Set(nonEmpties.map(o => o.toLowerCase()));
      if (uniqueOpts.size < nonEmpties.length) {
        issues.duplicateOptions.push({ id, qCode, optTexts, topicCode });
      }
    }

    // Check Explanation
    if (!explanation) {
      issues.missingExplanation.push({ id, qCode, topicCode });
    } else if (explanation.length < 5 || /^(solution|ans|answer|none|refer textbook|see above)$/i.test(explanation)) {
      issues.trivialExplanation.push({ id, qCode, explanation, topicCode });
    }
  });

  // Check Topics where Option A is > 40% or 100%
  for (const [tCode, stat] of Object.entries(topicStats)) {
    if (stat.objective >= 5) {
      const aCount = stat.dist.A;
      const totalObj = stat.objective;
      const aPct = (aCount / totalObj) * 100;
      if (aPct === 100) {
        issues.allOptionATopics.push({ topicCode: tCode, total: totalObj, aCount, aPct, subject: stat.subject });
      } else if (aPct > 40) {
        issues.dominantOptionATopics.push({ topicCode: tCode, total: totalObj, aCount, aPct: Math.round(aPct), subject: stat.subject });
      }
    }
  }

  console.log('\n=== AUDIT SUMMARY RESULTS ===');
  console.log('Overall Answer Distribution:', overallAnswerDist);
  console.log('Topics with 100% Option A:', issues.allOptionATopics.length);
  console.log('Topics with > 40% Option A:', issues.dominantOptionATopics.length);
  console.log('Missing Question Text:', issues.missingText.length);
  console.log('Very Short Question Text (<10 chars):', issues.shortText.length);
  console.log('Missing Options array:', issues.missingOptions.length);
  console.log('Less than 2 options:', issues.lessThanTwoOptions.length);
  console.log('Placeholder options ("Option A", empty, "dummy"):', issues.placeholderOptions.length);
  console.log('Duplicate options in same question:', issues.duplicateOptions.length);
  console.log('Missing Explanations:', issues.missingExplanation.length);
  console.log('Trivial Explanations:', issues.trivialExplanation.length);

  fs.writeFileSync('audit_results.json', JSON.stringify({ overallAnswerDist, issues, topicStatsCount: Object.keys(topicStats).length }, null, 2));
  console.log('Saved detailed audit to audit_results.json');
}

runAudit().catch(console.error);
