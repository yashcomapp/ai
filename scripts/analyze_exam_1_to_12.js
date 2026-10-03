const fs = require('fs');
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

function parseDate(val) {
  if (!val) return null;
  if (val.toDate && typeof val.toDate === 'function') return val.toDate();
  if (val._seconds) return new Date(val._seconds * 1000);
  const d = new Date(val);
  return isNaN(d.getTime()) ? null : d;
}

function formatDuration(ms) {
  if (ms == null || isNaN(ms)) return 'N/A';
  if (ms < 0) return '0s (instant)';
  const totalSecs = Math.floor(ms / 1000);
  const days = Math.floor(totalSecs / 86400);
  const hours = Math.floor((totalSecs % 86400) / 3600);
  const mins = Math.floor((totalSecs % 3600) / 60);
  const parts = [];
  if (days > 0) parts.push(days + 'd');
  if (hours > 0) parts.push(hours + 'h');
  if (mins > 0 || parts.length === 0) parts.push(mins + 'm');
  return parts.join(' ');
}

async function run() {
  const [usersSnap, reviewsSnap, evalsSnap] = await Promise.all([
    db.collection('users').where('role', '==', 'student').get(),
    db.collection('reviews').get(),
    db.collection('evaluations').where('evaluatorType', '==', 'parent').get()
  ]);

  const studentMap = new Map();
  usersSnap.docs.forEach(doc => {
    const d = doc.data();
    studentMap.set(d.studentCode || doc.id, { name: d.name, autonomous: !!d.autonomous });
  });

  const parentEvalMap = new Map();
  evalsSnap.docs.forEach(doc => {
    const d = doc.data();
    const dt = parseDate(d.createdAt);
    if (d.legacyId) parentEvalMap.set(d.legacyId, dt);
    if (d.attemptId) parentEvalMap.set(d.attemptId, dt);
    if (d.examId && d.studentCode) parentEvalMap.set(d.examId + '_' + d.studentCode, dt);
  });

  // Group by Exam Number prefix (001 to 012)
  const examSeries = {};
  for (let i = 1; i <= 12; i++) {
    const numStr = String(i).padStart(3, '0');
    examSeries[numStr] = { 
      num: i, 
      numStr, 
      attempts: 0, 
      approved: 0, 
      pending: 0, 
      durations: [], 
      examTitles: new Set(),
      parentReviews: []
    };
  }

  reviewsSnap.docs.forEach(doc => {
    const data = doc.data();
    const student = studentMap.get(data.studentCode);
    if (student && student.autonomous) return; // skip autonomous

    const examId = data.examId || data.examCode || (doc.id.includes('_') ? doc.id.split('_')[0] : doc.id);
    const prefix = examId.slice(0, 3);
    if (!examSeries[prefix]) return;

    const group = examSeries[prefix];
    group.attempts++;
    group.examTitles.add(data.examName || examId);

    if (data.status === 'approved') group.approved++;
    if (data.status === 'pending') group.pending++;

    const completedAt = parseDate(data.completedAt) || parseDate(data.startedAt) || parseDate(data.submittedAt);
    const studentReviewedAt = parseDate(data.studentReviewedAt);
    let parentReviewedAt = parseDate(data.reviewedAt) || parseDate(data.parentReviewedAt) || parentEvalMap.get(doc.id) || (examId && data.studentCode ? parentEvalMap.get(examId + '_' + data.studentCode) : null);

    const readyAt = studentReviewedAt || completedAt;
    let diff = null;
    if (readyAt && parentReviewedAt) {
      diff = parentReviewedAt.getTime() - readyAt.getTime();
      if (diff >= 0) {
        group.durations.push(diff);
      }
    }

    group.parentReviews.push({
      studentName: student?.name || data.studentName || 'Student',
      studentCode: data.studentCode,
      status: data.status,
      diff,
      submitted: readyAt ? readyAt.toISOString().replace('T', ' ').slice(0, 16) : null,
      approved: parentReviewedAt ? parentReviewedAt.toISOString().replace('T', ' ').slice(0, 16) : null
    });
  });

  console.log('\n=========================================================================================================');
  console.log('DETAILED TURNAROUND ANALYSIS: EXAM 1 TO 12 (REGULAR / NON-AUTONOMOUS STUDENTS)');
  console.log('=========================================================================================================\n');

  const rows = [];
  for (let i = 1; i <= 12; i++) {
    const numStr = String(i).padStart(3, '0');
    const g = examSeries[numStr];
    const validDurs = g.durations.slice().sort((a, b) => a - b);
    const count = validDurs.length;
    let avgMs = null;
    let medianMs = null;
    let minMs = null;
    let maxMs = null;
    let under1h = 0;
    let between1hAnd12h = 0;
    let between12hAnd24h = 0;
    let over24h = 0;

    if (count > 0) {
      avgMs = validDurs.reduce((a, b) => a + b, 0) / count;
      medianMs = count % 2 === 0 ? (validDurs[count / 2 - 1] + validDurs[count / 2]) / 2 : validDurs[Math.floor(count / 2)];
      minMs = validDurs[0];
      maxMs = validDurs[count - 1];

      validDurs.forEach(d => {
        const hrs = d / (1000 * 3600);
        if (hrs < 1) under1h++;
        else if (hrs <= 12) between1hAnd12h++;
        else if (hrs <= 24) between12hAnd24h++;
        else over24h++;
      });
    }

    rows.push({
      examNo: `Exam #${i} (${numStr})`,
      titles: Array.from(g.examTitles).slice(0, 2).join(', '),
      attempts: g.attempts,
      reviewed: count,
      compliance: `${Math.round((count / (g.attempts || 1)) * 100)}%`,
      avgTime: formatDuration(avgMs),
      medianTime: formatDuration(medianMs),
      fastest: formatDuration(minMs),
      slowest: formatDuration(maxMs),
      under1h,
      between1hAnd12h,
      between12hAnd24h,
      over24h,
      sampleRecords: g.parentReviews
    });
  }

  console.table(rows.map(r => ({
    'Exam': r.examNo,
    'Attempts': r.attempts,
    'Reviewed': r.reviewed,
    'Compliance': r.compliance,
    'Average Time': r.avgTime,
    'Median Time': r.medianTime,
    'Fastest': r.fastest,
    'Slowest': r.slowest,
    '< 1 hr': r.under1h,
    '1-12 hrs': r.between1hAnd12h,
    '12-24 hrs': r.between12hAnd24h,
    '> 24 hrs': r.over24h
  })));

  console.log('\n--- EXAM DETAILS & PARENT BEHAVIOR PATTERNS ---');
  rows.forEach(r => {
    console.log(`\n📌 ${r.examNo} (${r.titles}):`);
    console.log(`   • Total Attempts: ${r.attempts} | Parent Reviewed: ${r.reviewed} (${r.compliance})`);
    console.log(`   • Average Turnaround: ${r.avgTime} | Median: ${r.medianTime}`);
    console.log(`   • Range: Fastest = ${r.fastest} ↔ Slowest = ${r.slowest}`);
    console.log(`   • Distribution: <1 hr: ${r.under1h} | 1-12 hrs: ${r.between1hAnd12h} | 12-24 hrs: ${r.between12hAnd24h} | >24 hrs: ${r.over24h}`);
    if (r.sampleRecords.length > 0) {
      console.log('   • Sample Reviews:');
      r.sampleRecords.slice(0, 3).forEach(sr => {
        console.log(`     - ${sr.studentName}: ${formatDuration(sr.diff)} (Submitted: ${sr.submitted || 'N/A'} → Approved: ${sr.approved || 'Pending'})`);
      });
    }
  });

  console.log('\n=========================================================================================================\n');
}

run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
