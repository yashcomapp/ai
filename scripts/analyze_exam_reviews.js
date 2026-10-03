const admin = require('firebase-admin');
const fs = require('fs');

// Read .env.local
const envContent = fs.readFileSync('.env.local', 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
        v = v.slice(1, -1);
      }
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY || process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (sa) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
}
const db = admin.firestore();

function formatDuration(ms) {
  if (ms == null || isNaN(ms)) return 'N/A';
  if (ms < 0) return '0s (instant)';
  const totalSecs = Math.floor(ms / 1000);
  const days = Math.floor(totalSecs / 86400);
  const hours = Math.floor((totalSecs % 86400) / 3600);
  const mins = Math.floor((totalSecs % 3600) / 60);
  const secs = totalSecs % 60;
  const parts = [];
  if (days > 0) parts.push(`${days}d`);
  if (hours > 0) parts.push(`${hours}h`);
  if (mins > 0) parts.push(`${mins}m`);
  if (secs > 0 || parts.length === 0) parts.push(`${secs}s`);
  return parts.join(' ');
}

function parseDate(val) {
  if (!val) return null;
  if (val.toDate && typeof val.toDate === 'function') return val.toDate();
  if (val._seconds) return new Date(val._seconds * 1000);
  const d = new Date(val);
  return isNaN(d.getTime()) ? null : d;
}

async function analyze() {
  console.log('Fetching students, exams, reviews, and evaluations...');
  
  // 1. Fetch Students
  const usersSnap = await db.collection('users').where('role', '==', 'student').get();
  const studentMap = new Map();
  usersSnap.docs.forEach(doc => {
    const d = doc.data();
    studentMap.set(d.studentCode || doc.id, {
      name: d.name,
      studentCode: d.studentCode,
      autonomous: !!d.autonomous,
      status: d.status || 'active',
      parentEmail: d.parentEmail
    });
  });

  // 2. Fetch Exams
  const examsSnap = await db.collection('exams').get();
  const examMap = new Map();
  examsSnap.docs.forEach(doc => {
    const d = doc.data();
    examMap.set(doc.id, {
      id: doc.id,
      title: d.title || d.name || d.examCode || doc.id,
      examCode: d.examCode,
      createdAt: parseDate(d.createdAt)
    });
  });

  // 3. Fetch Reviews
  const reviewsSnap = await db.collection('reviews').get();
  console.log(`Loaded ${reviewsSnap.size} total reviews.`);

  // 4. Fetch Evaluations (for parent approval timestamp fallback)
  const evalsSnap = await db.collection('evaluations').where('evaluatorType', '==', 'parent').get();
  const parentEvalMap = new Map(); // key: `${examId}_${studentCode}` or attemptId or legacyId
  evalsSnap.docs.forEach(doc => {
    const d = doc.data();
    const created = parseDate(d.createdAt);
    if (d.legacyId) parentEvalMap.set(d.legacyId, created);
    if (d.attemptId) parentEvalMap.set(d.attemptId, created);
    if (d.examId && d.studentCode) parentEvalMap.set(`${d.examId}_${d.studentCode}`, created);
  });

  // Filter reviews for regular (non-autonomous) students
  const records = [];

  reviewsSnap.docs.forEach(doc => {
    const data = doc.data();
    const studentCode = data.studentCode;
    const student = studentMap.get(studentCode);

    // Filter for regular students (not autonomous)
    if (student && student.autonomous) {
      return; // skip autonomous students
    }

    const examId = data.examId || data.examCode || (doc.id.includes('_') ? doc.id.split('_')[0] : doc.id);
    const exam = examMap.get(examId) || {};
    const examTitle = exam.title || data.examName || data.examTitle || examId;

    // Resolve Timestamps:
    // 1. Student Submission / Completion
    const completedAt = parseDate(data.completedAt) || parseDate(data.startedAt) || parseDate(data.submittedAt);
    
    // 2. Student Self-Review (if applicable)
    const studentReviewedAt = parseDate(data.studentReviewedAt);

    // 3. Parent Review / Approval
    let parentReviewedAt = parseDate(data.reviewedAt) || parseDate(data.parentReviewedAt);
    if (!parentReviewedAt) {
      parentReviewedAt = parentEvalMap.get(doc.id) || 
                         (examId && studentCode ? parentEvalMap.get(`${examId}_${studentCode}`) : null);
    }

    // Time elapsed from when exam became ready for parent review (student completion or student self-review)
    const readyForParentAt = studentReviewedAt || completedAt;

    let timeToParentReviewMs = null;
    let studentReviewDurationMs = null;
    let totalTurnaroundMs = null;

    if (completedAt && studentReviewedAt) {
      studentReviewDurationMs = studentReviewedAt.getTime() - completedAt.getTime();
    }

    if (readyForParentAt && parentReviewedAt) {
      timeToParentReviewMs = parentReviewedAt.getTime() - readyForParentAt.getTime();
    }

    if (completedAt && parentReviewedAt) {
      totalTurnaroundMs = parentReviewedAt.getTime() - completedAt.getTime();
    }

    records.push({
      docId: doc.id,
      examId,
      examTitle,
      studentCode,
      studentName: student?.name || data.studentName || 'Student',
      status: data.status,
      completedAt,
      studentReviewedAt,
      parentReviewedAt,
      timeToParentReviewMs,
      studentReviewDurationMs,
      totalTurnaroundMs
    });
  });

  console.log(`Analyzed ${records.length} reviews for regular students.`);

  // Group by Exam
  const examGroups = new Map();
  records.forEach(r => {
    // Normalise exam key
    const key = r.examTitle || r.examId;
    if (!examGroups.has(key)) {
      examGroups.set(key, {
        examTitle: key,
        examId: r.examId,
        totalAttempts: 0,
        approvedCount: 0,
        pendingCount: 0,
        studentReviewCount: 0,
        reviewedByParentCount: 0,
        durationsMs: [],
        records: []
      });
    }
    const group = examGroups.get(key);
    group.totalAttempts++;
    if (r.status === 'approved') group.approvedCount++;
    if (r.status === 'pending') group.pendingCount++;
    if (r.status === 'student_review') group.studentReviewCount++;
    
    if (r.timeToParentReviewMs != null && r.timeToParentReviewMs >= 0) {
      group.reviewedByParentCount++;
      group.durationsMs.push(r.timeToParentReviewMs);
    }
    group.records.push(r);
  });

  // Sort groups and display summary
  const summaryList = Array.from(examGroups.values());
  summaryList.sort((a, b) => a.examTitle.localeCompare(b.examTitle, undefined, { numeric: true }));

  console.log('\n========================================================================================');
  console.log('EXAM-BY-EXAM PARENT REVIEW ANALYSIS (REGULAR STUDENTS)');
  console.log('========================================================================================\n');

  summaryList.forEach((g, idx) => {
    const validDurations = g.durationsMs.slice().sort((a, b) => a - b);
    const count = validDurations.length;
    let avgMs = null;
    let medianMs = null;
    let minMs = null;
    let maxMs = null;

    if (count > 0) {
      avgMs = validDurations.reduce((a, b) => a + b, 0) / count;
      medianMs = count % 2 === 0 
        ? (validDurations[count / 2 - 1] + validDurations[count / 2]) / 2 
        : validDurations[Math.floor(count / 2)];
      minMs = validDurations[0];
      maxMs = validDurations[count - 1];
    }

    console.log(`[Exam #${idx + 1}] ${g.examTitle} (ID: ${g.examId})`);
    console.log(`  Total Attempts: ${g.totalAttempts}`);
    console.log(`  Status Breakdown: Approved: ${g.approvedCount} | Pending: ${g.pendingCount} | Student Review: ${g.studentReviewCount}`);
    console.log(`  Parent Reviewed Count: ${count} of ${g.totalAttempts} (${Math.round((count / (g.totalAttempts || 1)) * 100)}%)`);
    if (count > 0) {
      console.log(`  Average Time to Parent Review: ${formatDuration(avgMs)}`);
      console.log(`  Median Time: ${formatDuration(medianMs)}`);
      console.log(`  Fastest: ${formatDuration(minMs)} | Slowest: ${formatDuration(maxMs)}`);
    } else {
      console.log(`  Average Time to Parent Review: No parent reviews recorded or all pending.`);
    }

    // Print sample of attempts
    if (g.records.length > 0) {
      console.log('  Student Breakdown:');
      g.records.slice(0, 5).forEach(rec => {
        console.log(`    • ${rec.studentName} (${rec.studentCode}): Status=${rec.status} | Time Taken=${formatDuration(rec.timeToParentReviewMs)} | Submitted=${rec.completedAt ? rec.completedAt.toISOString().replace('T', ' ').slice(0, 16) : 'N/A'} | Approved=${rec.parentReviewedAt ? rec.parentReviewedAt.toISOString().replace('T', ' ').slice(0, 16) : 'Pending/None'}`);
      });
      if (g.records.length > 5) {
        console.log(`    ... and ${g.records.length - 5} more students`);
      }
    }
    console.log('----------------------------------------------------------------------------------------');
  });

  // Overall Statistics across all exams
  const allDurations = records.map(r => r.timeToParentReviewMs).filter(d => d != null && d >= 0).sort((a, b) => a - b);
  const totalCompletedReviews = allDurations.length;
  const overallAvg = totalCompletedReviews > 0 ? allDurations.reduce((a, b) => a + b, 0) / totalCompletedReviews : 0;
  const overallMedian = totalCompletedReviews > 0 
    ? (totalCompletedReviews % 2 === 0 ? (allDurations[totalCompletedReviews / 2 - 1] + allDurations[totalCompletedReviews / 2]) / 2 : allDurations[Math.floor(totalCompletedReviews / 2)])
    : 0;

  console.log('\n========================================================================================');
  console.log('OVERALL SUMMARY ACROSS ALL EXAMS');
  console.log('========================================================================================');
  console.log(`Total Student Exam Attempts Analyzed: ${records.length}`);
  console.log(`Total Parent Approvals Recorded: ${totalCompletedReviews} (${Math.round((totalCompletedReviews / (records.length || 1)) * 100)}%)`);
  console.log(`Overall Average Time Taken by Parents: ${formatDuration(overallAvg)}`);
  console.log(`Overall Median Time Taken by Parents: ${formatDuration(overallMedian)}`);
  console.log(`Still Pending / Abandoned by Parents: ${records.filter(r => r.status === 'pending').length}`);
  console.log('========================================================================================\n');
}

analyze().then(() => process.exit(0)).catch(err => { console.error(err); process.exit(1); });
