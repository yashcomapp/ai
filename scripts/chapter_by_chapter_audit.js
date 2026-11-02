const path = require('path');
const fs = require('fs');

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

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

// Higher/Advanced university or college-level keywords that should never appear in Class 8-10 school syllabi
const universityPatterns = [
  /\bdifferential\s+equations?\b/i,
  /\bhamiltonian\b/i,
  /\bschrod?inger\b/i,
  /\bbragg's\s+law\b/i,
  /\blorentz\b/i,
  /\brelativistic\b/i,
  /\bsynchrotron\b/i,
  /\bcrystal\s+field\b/i,
  /\bgibbs\s+free\s+energy\b/i,
  /\btopoisomerase\b/i,
  /\bdna\s+gyrase\b/i,
  /\bpalindromic\s+restriction\b/i,
  /\bfluidized\s+bed\b/i,
  /\bphytoremediation\b/i,
  /\bhyperaccumulat/i,
  /\banaerobic\s+digestion.*hydrolytic\b/i,
  /\bglomerular\s+filtrat.*fraction\b/i,
  /\bpotometer\s+transpires\b/i,
  /\bgigaflops\s+are\s+in\b/i,
  /\bteraflops\s+are\b/i
];

async function runChapterByChapterAudit() {
  console.log('Fetching all questions from Firestore for complete chapter-by-chapter audit...');
  const snap = await db.collection('questions').get();
  console.log(`Total questions in database: ${snap.size}`);

  const chaptersMap = {};

  snap.forEach(doc => {
    const q = doc.data();
    const board = q.boardCode || (q.board && q.board.toLowerCase().includes('cbse') ? 'CBSE' : 'MH');
    const cl = String(q.class || '');
    const sub = q.subjectCode || 'UNKNOWN';
    const ch = String(q.chapterNumber ?? '0');
    const chKey = `${board}_Class${cl}_${sub}_Ch${ch}`;

    if (!chaptersMap[chKey]) {
      chaptersMap[chKey] = {
        board,
        class: cl,
        subject: sub,
        chapter: ch,
        total: 0,
        usedCount: 0,
        typeCounts: {},
        issues: {
          missingOptions: [],
          insufficientOptions: [],
          duplicateOptions: [],
          placeholderOptions: [],
          invalidAnswerKey: [],
          missingSolution: [],
          brokenMath: [],
          advancedContent: []
        }
      };
    }

    const c = chaptersMap[chKey];
    c.total++;
    if (q.used || q.usageCount > 0 || q.timesUsed > 0) c.usedCount++;

    const type = q.type || 'UNKNOWN';
    c.typeCounts[type] = (c.typeCounts[type] || 0) + 1;

    // 1. Options check
    const opts = q.options;
    if (!opts || !Array.isArray(opts)) {
      if (type !== 'ONE') { // ONE questions may not have options in some formats, but in QB they usually do
        c.issues.missingOptions.push(doc.id);
      }
    } else {
      if (opts.length < 2 && type !== 'ONE') {
        c.issues.insufficientOptions.push(doc.id);
      }

      // Check duplicates and placeholder strings
      const optTexts = opts.map(o => (typeof o === 'object' && o !== null ? (o.text || o.label || o.value || '') : String(o || '')).trim());
      const lowerTexts = optTexts.map(t => t.toLowerCase());

      const duplicates = lowerTexts.filter((item, index) => lowerTexts.indexOf(item) !== index && item !== '');
      if (duplicates.length > 0) {
        c.issues.duplicateOptions.push({ id: doc.id, duplicates });
      }

      const placeholders = optTexts.filter(t => {
        const l = t.toLowerCase();
        return l === 'correct option' || l === 'wrong option' || l.startsWith('right:') || l.startsWith('wrong:') || l.startsWith('alternative comparative parameter');
      });
      if (placeholders.length > 0) {
        c.issues.placeholderOptions.push({ id: doc.id, placeholders });
      }
    }

    // 2. Answer key check
    const ans = q.correctAnswer;
    const ansArr = q.correctAnswers;
    const hasSingleAns = ans !== undefined && ans !== null && String(ans).trim() !== '';
    const hasMultiAns = Array.isArray(ansArr) && ansArr.length > 0;
    if (!hasSingleAns && !hasMultiAns) {
      c.issues.invalidAnswerKey.push(doc.id);
    }

    // 3. Solution check
    const sol = (q.solution || q.explanation || '').trim();
    if (!sol) {
      c.issues.missingSolution.push(doc.id);
    }

    // 4. Math / KaTeX formatting check
    const fullText = `${q.text || ''} ${sol} ${(q.options || []).map(o => typeof o === 'object' ? (o.text || '') : String(o)).join(' ')}`;
    if (fullText.includes('\\(\\)')) {
      c.issues.brokenMath.push(doc.id);
    }

    // 5. University / College level check
    for (const pat of universityPatterns) {
      if (pat.test(fullText)) {
        c.issues.advancedContent.push({ id: doc.id, pattern: pat.toString() });
        break;
      }
    }
  });

  const sortedKeys = Object.keys(chaptersMap).sort();
  console.log(`\n======================================================`);
  console.log(`FOUND ${sortedKeys.length} DISTINCT CHAPTERS IN QUESTION BANK`);
  console.log(`======================================================\n`);

  const report = [];

  sortedKeys.forEach(k => {
    const c = chaptersMap[k];
    const totalIssues = 
      c.issues.missingOptions.length +
      c.issues.insufficientOptions.length +
      c.issues.duplicateOptions.length +
      c.issues.placeholderOptions.length +
      c.issues.invalidAnswerKey.length +
      c.issues.missingSolution.length +
      c.issues.brokenMath.length +
      c.issues.advancedContent.length;

    const status = totalIssues === 0 ? '🟢 PRISTINE' : `⚠️ ${totalIssues} ISSUES DETECTED`;

    report.push({
      chapterKey: k,
      board: c.board,
      class: c.class,
      subject: c.subject,
      chapter: c.chapter,
      totalQuestions: c.total,
      usedQuestions: c.usedCount,
      typeDistribution: c.typeCounts,
      status,
      issueDetails: c.issues
    });

    console.log(`[${status}] ${k}: ${c.total} Qs (Types: ${JSON.stringify(c.typeCounts)})`);
    if (totalIssues > 0) {
      if (c.issues.missingOptions.length) console.log(`   - Missing options: ${c.issues.missingOptions.length}`);
      if (c.issues.insufficientOptions.length) console.log(`   - Insufficient options: ${c.issues.insufficientOptions.length}`);
      if (c.issues.duplicateOptions.length) console.log(`   - Duplicate options: ${c.issues.duplicateOptions.length}`);
      if (c.issues.placeholderOptions.length) console.log(`   - Placeholder options: ${c.issues.placeholderOptions.length}`);
      if (c.issues.invalidAnswerKey.length) console.log(`   - Invalid answer key: ${c.issues.invalidAnswerKey.length}`);
      if (c.issues.missingSolution.length) console.log(`   - Missing solution: ${c.issues.missingSolution.length}`);
      if (c.issues.brokenMath.length) console.log(`   - Broken KaTeX math: ${c.issues.brokenMath.length}`);
      if (c.issues.advancedContent.length) console.log(`   - Advanced content: ${c.issues.advancedContent.length}`);
    }
  });

  fs.writeFileSync('scripts/chapter_by_chapter_audit_report.json', JSON.stringify(report, null, 2));
  console.log(`\nSaved detailed audit report to scripts/chapter_by_chapter_audit_report.json`);
}

runChapterByChapterAudit().then(() => process.exit(0)).catch(console.error);
