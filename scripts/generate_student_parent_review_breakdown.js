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

function formatDateIST(d) {
  if (!d) return '—';
  const ist = new Date(d.getTime() + (5.5 * 60 * 60 * 1000));
  const day = String(ist.getUTCDate()).padStart(2, '0');
  const month = String(ist.getUTCMonth() + 1).padStart(2, '0');
  const year = ist.getUTCFullYear();
  let hours = ist.getUTCHours();
  const minutes = String(ist.getUTCMinutes()).padStart(2, '0');
  const ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12 || 12;
  return `${day}/${month}/${year}, ${hours}:${minutes} ${ampm}`;
}

function formatDuration(ms) {
  if (ms == null || isNaN(ms)) return 'Pending / None';
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

async function run() {
  const [usersSnap, reviewsSnap, evalsSnap] = await Promise.all([
    db.collection('users').where('role', '==', 'student').get(),
    db.collection('reviews').get(),
    db.collection('evaluations').where('evaluatorType', '==', 'parent').get()
  ]);

  const studentMap = new Map();
  usersSnap.docs.forEach(doc => {
    const d = doc.data();
    studentMap.set(d.studentCode || doc.id, {
      name: d.name || 'Student',
      studentCode: d.studentCode,
      autonomous: !!d.autonomous,
      parentEmail: d.parentEmail || ''
    });
  });

  const parentEvalMap = new Map();
  evalsSnap.docs.forEach(doc => {
    const d = doc.data();
    const dt = parseDate(d.createdAt);
    const timeSpentSecs = d.timeSpentSeconds || d.durationSeconds || null;
    const entry = { dt, timeSpentSecs, evaluatorName: d.evaluatorName };
    if (d.legacyId) parentEvalMap.set(d.legacyId, entry);
    if (d.attemptId) parentEvalMap.set(d.attemptId, entry);
    if (d.examId && d.studentCode) parentEvalMap.set(`${d.examId}_${d.studentCode}`, entry);
  });

  const allRecords = [];

  reviewsSnap.docs.forEach(doc => {
    const data = doc.data();
    const studentCode = data.studentCode;
    const student = studentMap.get(studentCode);
    if (student && student.autonomous) return; // skip autonomous

    const examId = data.examId || data.examCode || (doc.id.includes('_') ? doc.id.split('_')[0] : doc.id);
    const prefix = examId.slice(0, 3);
    const examNum = parseInt(prefix, 10);
    if (isNaN(examNum) || examNum < 1 || examNum > 12) return; // focus on Exam 1 to 12

    const completedAt = parseDate(data.completedAt) || parseDate(data.startedAt) || parseDate(data.submittedAt);
    const studentReviewedAt = parseDate(data.studentReviewedAt);

    let parentReviewedAt = parseDate(data.reviewedAt) || parseDate(data.parentReviewedAt);
    let activeTimeSpent = data.timeSpentSeconds || data.parentReviewTimeSeconds || null;

    const evalEntry = parentEvalMap.get(doc.id) || (examId && studentCode ? parentEvalMap.get(`${examId}_${studentCode}`) : null);
    if (!parentReviewedAt && evalEntry) {
      parentReviewedAt = evalEntry.dt;
      if (!activeTimeSpent && evalEntry.timeSpentSecs) activeTimeSpent = evalEntry.timeSpentSecs;
    }

    const readyAt = studentReviewedAt || completedAt;
    let elapsedMs = null;
    if (readyAt && parentReviewedAt) {
      elapsedMs = parentReviewedAt.getTime() - readyAt.getTime();
      if (elapsedMs < 0) elapsedMs = 0;
    }

    allRecords.push({
      examNum,
      examNumStr: `Exam #${examNum} (${prefix})`,
      examId,
      examName: data.examName || examId,
      studentCode,
      studentName: student?.name || data.studentName || 'Student',
      status: data.status,
      score: data.score != null ? `${data.score}/${data.totalMarks || data.totalQuestions || 20}` : '—',
      percentage: data.percentage != null ? `${data.percentage}%` : (data.scorePercent != null ? `${data.scorePercent}%` : '—'),
      completedAt,
      studentReviewedAt,
      parentReviewedAt,
      elapsedMs,
      elapsedFormatted: formatDuration(elapsedMs),
      completedFormatted: formatDateIST(completedAt),
      parentReviewedFormatted: formatDateIST(parentReviewedAt),
      activeTimeSpentFormatted: activeTimeSpent ? `${activeTimeSpent}s` : 'Instant / Not Timed (< 30s)'
    });
  });

  // Group records by student
  const studentGroups = new Map();
  allRecords.forEach(rec => {
    if (!studentGroups.has(rec.studentCode)) {
      studentGroups.set(rec.studentCode, {
        studentCode: rec.studentCode,
        studentName: rec.studentName,
        exams: []
      });
    }
    studentGroups.get(rec.studentCode).exams.push(rec);
  });

  // Sort students alphabetically
  const studentList = Array.from(studentGroups.values());
  studentList.sort((a, b) => a.studentName.localeCompare(b.studentName));

  studentList.forEach(s => {
    s.exams.sort((a, b) => a.examNum - b.examNum);
  });

  // Write output JSON for easy reading
  fs.writeFileSync('scripts/student_exam_breakdown.json', JSON.stringify(studentList, null, 2));
  console.log(`Generated breakdown for ${studentList.length} regular students across Exams 1 to 12.`);
}

run().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
