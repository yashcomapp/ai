const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (serviceAccount) {
  const cred = JSON.parse(serviceAccount.startsWith('{') ? serviceAccount : Buffer.from(serviceAccount, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: 'ai-yashcom' });
}

const db = admin.firestore();

async function auditOar() {
  console.log('=== Step 1: Auditing Used Questions ===');
  const usedIds = new Set();
  const examsSnap = await db.collection('exams').get();
  examsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.questions || []).forEach(q => {
      if (typeof q === 'string') usedIds.add(q);
      else if (q && q.id) usedIds.add(q.id);
      else if (q && q.questionCode) usedIds.add(q.questionCode);
    });
    (d.questionIds || []).forEach(id => usedIds.add(id));
  });

  const subjSnap = await db.collection('subjectiveExams').get();
  subjSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.questions || []).forEach(q => {
      if (typeof q === 'string') usedIds.add(q);
      else if (q && q.id) usedIds.add(q.id);
      else if (q && q.questionCode) usedIds.add(q.questionCode);
    });
    (d.questionIds || []).forEach(id => usedIds.add(id));
  });

  const attemptsSnap = await db.collection('attempts').get();
  attemptsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  const parentReviewsSnap = await db.collection('parentReviews').get();
  parentReviewsSnap.docs.forEach(doc => {
    const d = doc.data();
    (d.answers || []).forEach(a => {
      if (a && a.questionId) usedIds.add(a.questionId);
      if (a && a.questionCode) usedIds.add(a.questionCode);
    });
  });

  console.log(`Total used identifiers: ${usedIds.size}`);

  console.log('=== Step 2: Fetching All OAR Questions ===');
  // Query both 'OAR' and 'assertion_reason'
  const oarSnap1 = await db.collection('questions').where('type', '==', 'OAR').get();
  const oarSnap2 = await db.collection('questions').where('type', '==', 'assertion_reason').get();

  const oarMap = new Map();
  oarSnap1.docs.forEach(d => oarMap.set(d.id, d));
  oarSnap2.docs.forEach(d => oarMap.set(d.id, d));

  console.log(`Found ${oarMap.size} total Assertion & Reason questions in database.`);

  const issues = [];
  const wellFormatted = [];

  for (const [id, doc] of oarMap.entries()) {
    const d = doc.data();
    const code = d.questionCode || id;
    const isUsed = usedIds.has(id) || usedIds.has(code);
    const text = String(d.text || '');
    const assertion = String(d.assertion || '');
    const reason = String(d.reason || '');
    const options = Array.isArray(d.options) ? d.options : [];

    const problemList = [];

    // Check for bad intro text
    if (/given\s+below|in\s+the\s+following|directions?\s*:/i.test(text)) {
      problemList.push('Has verbose intro text in question text');
    }

    // Check for empty options
    if (options.length === 0) {
      problemList.push('Options array is completely empty');
    } else if (options.length !== 4) {
      problemList.push(`Options array has ${options.length} options instead of 4`);
    }

    // Check for missing assertion / reason fields
    if (!assertion || !reason) {
      problemList.push('Missing explicit assertion or reason top-level fields');
    }

    // Check for raw \n string instead of actual linebreaks or broken split
    if (text.includes('\\n') && !text.includes('\n')) {
      problemList.push('Contains unescaped literal \\n in text');
    }

    if (problemList.length > 0) {
      issues.push({
        id,
        code,
        topicCode: d.topicCode,
        isUsed,
        text: text.slice(0, 100),
        assertion: assertion.slice(0, 60),
        reason: reason.slice(0, 60),
        optionsCount: options.length,
        correctAnswer: d.correctAnswer,
        problems: problemList
      });
    } else {
      wellFormatted.push(id);
    }
  }

  console.log(`\nAudit Results:`);
  console.log(`- Clean & well-formatted OARs: ${wellFormatted.length}`);
  console.log(`- OARs with formatting / options issues: ${issues.length}`);

  const issuesReportPath = path.join(__dirname, '..', 'backups', 'reports', 'oar_issues_report.json');
  fs.writeFileSync(issuesReportPath, JSON.stringify(issues, null, 2), 'utf8');
  console.log(`Saved detailed report to ${issuesReportPath}`);

  // Summary by problem type
  const countsByProblem = {};
  issues.forEach(item => {
    item.problems.forEach(p => {
      countsByProblem[p] = (countsByProblem[p] || 0) + 1;
    });
  });
  console.log('\nBreakdown of issues:');
  console.table(countsByProblem);

  // Used vs Unused breakdown
  const usedWithIssues = issues.filter(i => i.isUsed).length;
  const unusedWithIssues = issues.filter(i => !i.isUsed).length;
  console.log(`\nIssues in Used questions: ${usedWithIssues}`);
  console.log(`Issues in Unused questions: ${unusedWithIssues}`);
}

auditOar().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
