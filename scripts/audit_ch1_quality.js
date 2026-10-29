// scripts/audit_ch1_quality.js
const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Load environment
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}

const db = admin.firestore();

async function auditChapter1() {
  console.log('Querying all questions for Chapter 1 (topicCode: MH-9-SCIT-1-1.1)...');
  const snap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-1-1.1')
    .get();

  console.log(`Retrieved ${snap.size} questions from Firestore.`);
  
  const questions = [];
  snap.forEach(doc => {
    questions.push({ id: doc.id, ...doc.data() });
  });

  // Sort by id naturally
  questions.sort((a, b) => {
    const numA = parseInt(a.id.split('-').pop(), 10) || 0;
    const numB = parseInt(b.id.split('-').pop(), 10) || 0;
    return numA - numB;
  });

  const auditReport = {
    total: questions.length,
    missingThreePartSolution: [],
    containsPlaceholderDashes: [],
    containsNoneOfAbove: [],
    containsLeakedTeacherNotes: [],
    containsMissingDiagramReferences: [],
    genericPlaceholderOptions: [],
    emptySolution: [],
    cleanCount: 0
  };

  questions.forEach((q, idx) => {
    let hasIssue = false;

    // Check solution
    if (!q.solution || q.solution.trim().length === 0) {
      auditReport.emptySolution.push({ idx: idx + 1, id: q.id, text: q.text.substring(0, 60) });
      hasIssue = true;
    } else if (!q.solution.includes('### 1.') || !q.solution.includes('### 2.') || !q.solution.includes('### 3.')) {
      auditReport.missingThreePartSolution.push({
        idx: idx + 1,
        id: q.id,
        text: q.text.substring(0, 60),
        solutionPreview: q.solution.substring(0, 80)
      });
      hasIssue = true;
    }

    // Check placeholder dashes
    if (q.text && q.text.includes('---')) {
      auditReport.containsPlaceholderDashes.push({ idx: idx + 1, id: q.id, text: q.text });
      hasIssue = true;
    }

    // Check options
    if (Array.isArray(q.options)) {
      q.options.forEach((opt, optIdx) => {
        if (opt.toLowerCase().includes('none of above') || opt.toLowerCase().includes('none of the above')) {
          auditReport.containsNoneOfAbove.push({ idx: idx + 1, id: q.id, optIdx, opt });
          hasIssue = true;
        }
        if (opt.includes('Wrong:') || opt.includes('Right:')) {
          auditReport.containsLeakedTeacherNotes.push({ idx: idx + 1, id: q.id, optIdx, opt });
          hasIssue = true;
        }
        if (/^Option\s+\d+$/i.test(opt.trim())) {
          auditReport.genericPlaceholderOptions.push({ idx: idx + 1, id: q.id, optIdx, opt });
          hasIssue = true;
        }
      });
    }

    // Check missing diagram references
    if (q.text && (q.text.toLowerCase().includes('adjacent figure') || q.text.toLowerCase().includes('below figure') || q.text.toLowerCase().includes('given figure') || q.text.toLowerCase().includes('in the figure'))) {
      auditReport.containsMissingDiagramReferences.push({ idx: idx + 1, id: q.id, text: q.text });
      hasIssue = true;
    }

    if (!hasIssue) {
      auditReport.cleanCount++;
    }
  });

  console.log('\n=== CHAPTER 1 AUDIT RESULTS ===');
  console.log(`Total Questions: ${auditReport.total}`);
  console.log(`Clean 100% Gold-Standard: ${auditReport.cleanCount}`);
  console.log(`Missing 3-Part Solution: ${auditReport.missingThreePartSolution.length}`);
  console.log(`Empty Solution: ${auditReport.emptySolution.length}`);
  console.log(`Contains Placeholder Dashes ('---'): ${auditReport.containsPlaceholderDashes.length}`);
  console.log(`Contains 'None of above': ${auditReport.containsNoneOfAbove.length}`);
  console.log(`Contains Leaked Teacher Notes: ${auditReport.containsLeakedTeacherNotes.length}`);
  console.log(`Missing Diagram References: ${auditReport.containsMissingDiagramReferences.length}`);
  console.log(`Generic Placeholder Options ('Option 1'): ${auditReport.genericPlaceholderOptions.length}`);

  fs.writeFileSync('backups/staging/mh9_scit_1_audit_report.json', JSON.stringify(auditReport, null, 2), 'utf8');
  fs.writeFileSync('backups/staging/mh9_scit_1_current_firestore.json', JSON.stringify(questions, null, 2), 'utf8');
  console.log('\nFull audit report saved to backups/staging/mh9_scit_1_audit_report.json');
}

auditChapter1()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Audit failed:', err);
    process.exit(1);
  });
