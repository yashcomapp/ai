const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const admin = require('firebase-admin');

// Load environment variables
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

const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom';
if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({ credential: admin.credential.cert(credential) });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();

function getRequiredConfidence(topicClassification, targetQuestions) {
  if (targetQuestions && typeof targetQuestions === 'number' && targetQuestions > 0) {
    return targetQuestions;
  }
  const cls = (topicClassification || '').toLowerCase().trim();
  if (cls.includes('minor') || cls.includes('micro') || cls.includes('fact')) return 6;
  if (cls.includes('medium') || cls.includes('concept') || cls.includes('core')) return 10;
  if (cls.includes('major') || cls.includes('hots') || cls.includes('depth') || cls.includes('advanced')) return 15;
  return 10;
}

function formatReportStudentName(fullName) {
  if (!fullName) return '';
  const parts = fullName.trim().split(/\s+/).filter(Boolean);
  if (parts.length <= 2) return fullName.trim();
  return `${parts[0]} ${parts[parts.length - 1]}`;
}

function formatLastLoginIST(val) {
  if (!val) return 'Never';
  let dateObj = null;
  if (val?.toDate && typeof val.toDate === 'function') {
    dateObj = val.toDate();
  } else if (val instanceof Date) {
    dateObj = val;
  } else if (typeof val === 'string' || typeof val === 'number') {
    const d = new Date(val);
    if (!isNaN(d.getTime())) dateObj = d;
  }
  if (!dateObj) return 'Never';

  return new Intl.DateTimeFormat('en-IN', {
    timeZone: 'Asia/Kolkata',
    day: '2-digit',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  }).format(dateObj);
}

function getScoreChip(val, isHero = false) {
  if (val === null || val === undefined) {
    return `<span style="display:inline-block; min-width: 44px; padding: 3px 8px; border-radius: 6px; font-weight: 700; font-size: 13px; text-align: center; background: #f1f5f9; color: #64748b; border: 1px solid #cbd5e1;">-</span>`;
  }
  const num = Math.round(val);
  let bg = '#f8fafc';
  let color = '#0f172a';
  let border = '#cbd5e1';

  if (num >= 80) {
    bg = '#dcfce7';
    color = '#14532d';
    border = '#86efac';
  } else if (num >= 60) {
    bg = '#e0f2fe';
    color = '#0369a1';
    border = '#7dd3fc';
  } else if (num >= 40) {
    bg = '#fef3c7';
    color = '#92400e';
    border = '#fde68a';
  } else {
    bg = '#fee2e2';
    color = '#991b1b';
    border = '#fca5a5';
  }

  const fontSize = isHero ? '14px' : '12.5px';
  const fontWeight = isHero ? '900' : '800';
  const minWidth = isHero ? '52px' : '44px';

  return `<span style="display:inline-block; min-width: ${minWidth}; padding: 3px 8px; border-radius: 6px; font-weight: ${fontWeight}; font-size: ${fontSize}; text-align: center; background: ${bg}; color: ${color}; border: 1.5px solid ${border};">${num}%</span>`;
}

function getDeepScoreColor(score) {
  if (score >= 80) return '#14532d';
  if (score >= 60) return '#0369a1';
  if (score >= 40) return '#92400e';
  return '#991b1b';
}

async function main() {
  console.log('Fetching users, batches, topic mastery, and practice reviews...');
  const [usersSnap, batchesSnap, masterySnap, parentReviewsSnap] = await Promise.all([
    db.collection('users').where('role', '==', 'student').get(),
    db.collection('batches').get(),
    db.collection('studentTopicMastery').get(),
    db.collection('parentReviews').get()
  ]);

  const batchesMap = new Map();
  batchesSnap.docs.forEach(doc => {
    batchesMap.set(doc.id, { id: doc.id, ...doc.data() });
  });

  const activeStudents = usersSnap.docs
    .map(doc => ({ id: doc.id, ...doc.data() }))
    .filter(u => u.status !== 'inactive' && !u.isDemo);

  const studentTopicMasteryMap = {};
  masterySnap.docs.forEach(doc => {
    const data = doc.data();
    const code = data.studentCode;
    if (!code) return;
    const val = Number(data.mastery || 0);
    const conf = Number(data.confidence || 0);
    const tCode = data.topicCode;
    const reqConf = getRequiredConfidence(data.topicClassification, data.targetQuestions);

    if (tCode) {
      if (!studentTopicMasteryMap[code]) {
        studentTopicMasteryMap[code] = new Map();
      }
      studentTopicMasteryMap[code].set(tCode, {
        mastery: val,
        confidence: conf,
        reqConf,
        isRecoveryMastered: Boolean(data.isRecoveryMastered)
      });
    }
  });

  // October 2026 IST Date Range:
  // Starts: 2026-10-01T00:00:00+05:30 -> UTC 2026-09-30T18:30:00.000Z
  // EXCLUDES TODAY (16-Oct): Strictly before 2026-10-16T00:00:00+05:30 -> UTC 2026-10-15T18:30:00.000Z
  const octStart = new Date('2026-09-30T18:30:00.000Z');
  const octEndExclToday = new Date('2026-10-15T18:30:00.000Z');

  console.log(`October Window (Excl Today): ${octStart.toISOString()} to ${octEndExclToday.toISOString()}`);

  const studentPracticeMap = {};
  parentReviewsSnap.docs.forEach(doc => {
    const data = doc.data();
    const code = data.studentCode;
    if (!code) return;

    if (!studentPracticeMap[code]) {
      studentPracticeMap[code] = {
        allTimeSessions: 0,
        allTimeQuestions: 0,
        octSessions: 0,
        octQuestions: 0,
        octTopicsAttempted: new Set()
      };
    }

    const qCount = Number(data.totalQuestions || (data.questions ? data.questions.length : 0)) || 0;
    studentPracticeMap[code].allTimeSessions += 1;
    studentPracticeMap[code].allTimeQuestions += qCount;

    let msgDate = null;
    const rawTime = data.createdAt || data.timestamp || data.startedAt || data.submittedAt;
    if (rawTime?.toDate && typeof rawTime.toDate === 'function') {
      msgDate = rawTime.toDate();
    } else if (rawTime) {
      const d = new Date(rawTime);
      if (!isNaN(d.getTime())) msgDate = d;
    }

    // Strictly between 1 Oct 00:00 IST and 15 Oct 23:59:59 IST (Excluding today 16-Oct)
    if (msgDate && msgDate >= octStart && msgDate < octEndExclToday) {
      studentPracticeMap[code].octSessions += 1;
      studentPracticeMap[code].octQuestions += qCount;
      if (data.topicCode) studentPracticeMap[code].octTopicsAttempted.add(data.topicCode);
    }
  });

  // Calculate batch conducted topics (SSOT)
  const batchConductedTopicsMap = new Map();
  activeStudents.forEach(s => {
    const code = s.studentCode;
    const bIds = s.batchIds && s.batchIds.length > 0 ? s.batchIds : (s.batchId ? [s.batchId] : ['unassigned']);
    const studentTopics = new Set();
    if (studentTopicMasteryMap[code]) {
      studentTopicMasteryMap[code].forEach((_, t) => studentTopics.add(t));
    }
    bIds.forEach(bId => {
      if (!batchConductedTopicsMap.has(bId)) {
        batchConductedTopicsMap.set(bId, new Set());
      }
      const bSet = batchConductedTopicsMap.get(bId);
      studentTopics.forEach(t => bSet.add(t));
    });
  });

  const classes = {
    'Class 8th': [],
    'Class 9th': [],
    'Class 10th': []
  };

  activeStudents.forEach(s => {
    const code = s.studentCode;
    const bIds = s.batchIds && s.batchIds.length > 0 ? s.batchIds : (s.batchId ? [s.batchId] : ['unassigned']);
    
    let className = s.class || s.className || '';
    let batchName = '';
    bIds.forEach(bId => {
      const b = batchesMap.get(bId);
      if (b) {
        if (!className && b.classNum) className = `Class ${b.classNum}`;
        if (b.name) batchName = b.name;
      }
    });

    let targetClassKey = null;
    if (className.includes('8') || batchName.includes('8')) targetClassKey = 'Class 8th';
    else if (className.includes('9') || batchName.includes('9')) targetClassKey = 'Class 9th';
    else if (className.includes('10') || batchName.includes('10')) targetClassKey = 'Class 10th';

    if (!targetClassKey) return;

    const combinedBatchSet = new Set();
    bIds.forEach(bId => {
      const bSet = batchConductedTopicsMap.get(bId);
      if (bSet) bSet.forEach(t => combinedBatchSet.add(t));
    });
    const conductedTopics = Array.from(combinedBatchSet);
    const totalBatchTopics = conductedTopics.length;

    const masteryMap = studentTopicMasteryMap[code] || new Map();
    let mCount = 0;
    let pCount = 0;
    let naCount = 0;
    let totalMasterySum = 0;

    conductedTopics.forEach(tCode => {
      const record = masteryMap.get(tCode);
      if (record) {
        const val = record.mastery;
        const conf = record.confidence;
        const reqConf = record.reqConf || 10;
        totalMasterySum += val;
        if ((val >= 90 && conf >= reqConf) || record.isRecoveryMastered) {
          mCount++;
        } else if (val >= 50) {
          pCount++;
        } else {
          naCount++;
        }
      } else {
        naCount++;
      }
    });

    const pData = studentPracticeMap[code] || {
      allTimeSessions: 0,
      allTimeQuestions: 0,
      octSessions: 0,
      octQuestions: 0,
      octTopicsAttempted: new Set()
    };

    const avgMastery = totalBatchTopics > 0 ? Math.round(totalMasterySum / totalBatchTopics) : 0;
    const octEffortPercent = totalBatchTopics > 0 
      ? Math.min(100, Math.round((pData.octSessions / totalBatchTopics) * 100))
      : 0;

    const allTimeEffortPercent = totalBatchTopics > 0
      ? Math.min(100, Math.round((pData.allTimeSessions / totalBatchTopics) * 100))
      : 0;

    const lastLoginFormatted = formatLastLoginIST(s.lastLogin || s.lastLoginAt || s.updatedAt);

    classes[targetClassKey].push({
      studentCode: code,
      rawName: s.name || '',
      displayName: formatReportStudentName(s.name),
      batchName: batchName || 'Standard Batch',
      totalBatchTopics,
      avgMastery,
      mastered: mCount,
      practicing: pCount,
      needsAttention: naCount,
      octSessions: pData.octSessions,
      octQuestions: pData.octQuestions,
      octEffortPercent,
      allTimeSessions: pData.allTimeSessions,
      allTimeQuestions: pData.allTimeQuestions,
      allTimeEffortPercent,
      lastLogin: lastLoginFormatted
    });
  });

  // Sort each class: Oct Efforts desc, Oct Sessions desc, Avg Mastery desc, Name asc
  for (const cKey of Object.keys(classes)) {
    classes[cKey].sort((a, b) => {
      if (b.octEffortPercent !== a.octEffortPercent) return b.octEffortPercent - a.octEffortPercent;
      if (b.octSessions !== a.octSessions) return b.octSessions - a.octSessions;
      if (b.avgMastery !== a.avgMastery) return b.avgMastery - a.avgMastery;
      return a.displayName.localeCompare(b.displayName);
    });
  }

  // Ensure export directory
  const exportsDir = path.join(__dirname, '..', 'exports');
  const artifactsDir = path.join('C:\\Users\\Admin\\.gemini\\antigravity\\brain\\4cafec98-aaf9-4115-bc73-f64a2294768f');
  if (!fs.existsSync(exportsDir)) fs.mkdirSync(exportsDir, { recursive: true });

  const browserPath = fs.existsSync('C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe')
    ? 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    : 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

  console.log(`Using browser engine: ${browserPath}`);

  const generatedCards = [];

  for (const [classKey, students] of Object.entries(classes)) {
    console.log(`Generating card for ${classKey} (${students.length} students)...`);

    const totalStudents = students.length;
    const totalOctSessions = students.reduce((sum, s) => sum + s.octSessions, 0);
    const totalOctQuestions = students.reduce((sum, s) => sum + s.octQuestions, 0);
    const totalAllSessions = students.reduce((sum, s) => sum + s.allTimeSessions, 0);
    const totalAllQuestions = students.reduce((sum, s) => sum + s.allTimeQuestions, 0);
    const batchAvgMastery = Math.round(students.reduce((sum, s) => sum + s.avgMastery, 0) / (totalStudents || 1));
    const batchAvgOctEfforts = Math.round(students.reduce((sum, s) => sum + s.octEffortPercent, 0) / (totalStudents || 1));
    const uniformTopics = students[0]?.totalBatchTopics || 0;

    const rowsHtml = students.map((s, idx) => {
      const rank = idx + 1;
      const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
      const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';

      return `
        <tr style="border-bottom: 1px solid #e2e8f0; height: 42px; background-color: ${rowBg};">
          <td style="padding: 7px 8px; text-align: center; font-weight: 900; font-size: 13px; color: #0f172a;">${rankBadge}</td>
          <td style="padding: 7px 12px; font-weight: 800; font-size: 14px; color: #0f172a; white-space: nowrap;">
            ${s.displayName}
          </td>
          <td style="padding: 7px 8px; text-align: center; white-space: nowrap;">
            ${getScoreChip(s.octEffortPercent, true)}
          </td>
          <td style="padding: 7px 8px; text-align: center; font-weight: 800; font-size: 13.5px; color: #0284c7;">
            ${s.octSessions}
          </td>
          <td style="padding: 7px 8px; text-align: center; font-weight: 800; font-size: 13.5px; color: #0f172a;">
            ${s.octQuestions}
          </td>
          <td style="padding: 7px 8px; text-align: center; white-space: nowrap;">
            ${getScoreChip(s.avgMastery)}
          </td>
          <td style="padding: 7px 10px; text-align: center; white-space: nowrap;">
            <div style="display: inline-flex; align-items: center; gap: 4px;">
              <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #dcfce7; color: #14532d; border: 1px solid #86efac;" title="Mastered (>=90%)">
                🟢 ${s.mastered}
              </span>
              <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #fef3c7; color: #92400e; border: 1px solid #fcd34d;" title="In Progress (50-89%)">
                🟡 ${s.practicing}
              </span>
              <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5;" title="Needs Attention / Unattempted">
                🔴 ${s.needsAttention}
              </span>
            </div>
          </td>
          <td style="padding: 7px 8px; text-align: center; font-weight: 700; font-size: 12.5px; color: #475569;">
            ${s.allTimeSessions}
          </td>
          <td style="padding: 7px 8px; text-align: center; font-weight: 700; font-size: 12.5px; color: #475569;">
            ${s.allTimeQuestions}
          </td>
          <td style="padding: 7px 10px; text-align: center; font-size: 12px; font-weight: 700; color: #334155; white-space: nowrap;">
            ${s.lastLogin}
          </td>
        </tr>
      `;
    }).join('');

    const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${classKey} October Practice Card</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Noto Sans Devanagari', 'Mangal', sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      padding: 24px;
      display: flex;
      justify-content: center;
    }
    .card-container {
      width: 1100px;
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 14px;
      padding: 26px 30px;
      box-shadow: 0 10px 35px rgba(0,0,0,0.06);
    }
  </style>
</head>
<body>
  <div class="card-container">
    
    <!-- Top Header -->
    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
      <div>
        <div style="color: #92400e; font-size: 14.5px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
          YASHCOM FOUNDATION, SHEGAON
        </div>
        <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
          🏋️ ${classKey} • October Practice & Mastery Report
        </div>
        <div style="color: #0369a1; font-size: 15px; font-weight: 800;">
          Practice Window: 1st Oct – 15th Oct 2026 (Excluding Today's Sessions)
        </div>
      </div>
      <div style="text-align: right;">
        <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 13px; font-weight: 800; padding: 6px 14px; border-radius: 6px; display: inline-block;">
          📅 As on 16 Oct 2026
        </div>
        <div style="color: #475569; font-size: 12.5px; font-weight: 700; margin-top: 5px;">
          Curriculum Scope: <strong style="color:#0f172a;">${uniformTopics} Assigned Topics</strong>
        </div>
      </div>
    </div>

    <!-- 6 KPI Summary Cards -->
    <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 20px;">
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: #0f172a; line-height: 1.1;">${totalStudents}</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Students</div>
      </div>
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: #0284c7; line-height: 1.1;">${totalOctSessions}</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Oct Sessions</div>
      </div>
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: #047857; line-height: 1.1;">${totalOctQuestions}</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Oct Questions</div>
      </div>
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: ${getDeepScoreColor(batchAvgOctEfforts)}; line-height: 1.1;">${batchAvgOctEfforts}%</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Oct Efforts %</div>
      </div>
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: ${getDeepScoreColor(batchAvgMastery)}; line-height: 1.1;">${batchAvgMastery}%</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Avg Mastery</div>
      </div>
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 10px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size: 24px; font-weight: 900; color: #6366f1; line-height: 1.1;">${totalAllQuestions}</div>
        <div style="font-size: 10.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">All-Time Qs</div>
      </div>
    </div>

    <!-- Main Table -->
    <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
      <thead>
        <tr style="background: #0f172a; color: #ffffff; font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; height: 40px;">
          <th style="padding: 8px 6px; text-align: center; width: 44px;">Rank</th>
          <th style="padding: 8px 12px; text-align: left;">Student Name</th>
          <th style="padding: 8px 6px; text-align: center; width: 85px;">Oct Efforts</th>
          <th style="padding: 8px 6px; text-align: center; width: 75px;">Oct Sess</th>
          <th style="padding: 8px 6px; text-align: center; width: 75px;">Oct Qs</th>
          <th style="padding: 8px 6px; text-align: center; width: 80px;">Mastery</th>
          <th style="padding: 8px 10px; text-align: center; width: 175px;">Topics (${uniformTopics} Assigned)</th>
          <th style="padding: 8px 6px; text-align: center; width: 75px;">Total Sess</th>
          <th style="padding: 8px 6px; text-align: center; width: 75px;">Total Qs</th>
          <th style="padding: 8px 10px; text-align: center; width: 130px;">Last Login</th>
        </tr>
      </thead>
      <tbody>
        ${rowsHtml}
      </tbody>
    </table>

    <!-- Pedagogical Explanation & Parent Guidance Banner (Marathi) -->
    <div style="margin-top: 20px; padding: 18px 22px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
      <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
        <span style="font-size: 20px; line-height: 1;">💡</span>
        <strong style="color: #0f172a; font-size: 14.5px; font-weight: 900;">
          पालकांसाठी महत्त्वाचे स्पष्टीकरण व मार्गदर्शन (Topic Status & Parent Guidance):
        </strong>
      </div>
      <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13px; line-height: 1.7; font-weight: 600;">
        <li style="margin-bottom: 6px;">
          <strong style="color: #0f172a;">📌 एकूण नेमून दिलेले अभ्यासक्रम घटक (${uniformTopics} घटक):</strong> या बॅचसाठी शिकवून पूर्ण झालेले व सरावासाठी उपलब्ध असलेले एकूण घटक = 🟢 पूर्ण प्रभुत्व + 🟡 सराव सुरू + 🔴 सराव बाकी.
        </li>
        <li style="margin-bottom: 6px;">
          <strong style="color: #0369a1;">📌 ऑक्टोबर सराव प्रयत्न (Oct Efforts %):</strong> ऑक्टोबर महिन्यात (१ ते १५ ऑक्टोबर) पूर्ण केलेल्या सराव सेट्सचे प्रमाण. बोर्ड परीक्षेत ९०%+ प्रभुत्व मिळवण्यासाठी दरमहा १००% सराव प्रयत्न अनिवार्य आहेत.
        </li>
        <li style="margin-bottom: 6px;">
          <strong style="color: #14532d;">🟢 Mastered (संकल्पना प्रभुत्व):</strong> ज्या घटकांमध्ये विद्यार्थ्याने <strong>≥ ९०% अचूकता</strong> आणि किमान आवश्यक प्रश्नांचा सराव यशस्वीरीत्या पूर्ण केला आहे.
        </li>
        <li style="margin-bottom: 6px;">
          <strong style="color: #92400e;">🟡 In Progress (सराव सुरू):</strong> अचूकता ५०% ते ८९% दरम्यान आहे. अजून २ ते ३ सराव सेट्स सोडवून ९०%+ संपादन करणे आवश्यक आहे.
        </li>
        <li style="margin-bottom: 6px;">
          <strong style="color: #991b1b;">🔴 Needs Attention / Unattempted (सराव बाकी):</strong> अचूकता ५०% पेक्षा कमी आहे किंवा अद्याप सराव सुरू केलेला नाही. हे घटक तत्काळ सोडवणे अनिवार्य आहे.
        </li>
        <li>
          <strong style="color: #0f172a;">📌 पालकांसाठी कृती कार्यक्रम:</strong> दररोज घरी न चुकता किमान २ ते ३ सराव सेट्स (१५-२० प्रश्न) सोडवून सर्व 🟡 व 🔴 घटकांना 🟢 (Mastered) मध्ये रूपांतरित करावे.
        </li>
      </ul>
    </div>

    <!-- Footer -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
      <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Practice Track Evaluation Portal</span>
      <span>Official Batch Practice & Topic Mastery Summary • Confidential</span>
    </div>

  </div>
</body>
</html>`;

    const htmlFileName = `class_${classKey.replace(/\s+/g, '_').toLowerCase()}_oct_practice.html`;
    const htmlFilePath = path.join(exportsDir, htmlFileName);
    fs.writeFileSync(htmlFilePath, htmlContent, 'utf8');

    // Dynamic height calculation: header (200px) + KPI (90px) + table header (40px) + (rows * 44px) + guidance (220px) + footer (50px) + padding (80px)
    const cardHeight = Math.max(900, 200 + 90 + 40 + (students.length * 44) + 240 + 80);
    const pngFileName = `${classKey.replace(/\s+/g, '_')}_October_Practice_Report.png`;
    const pngExportPath = path.join(exportsDir, pngFileName);
    const pngArtifactPath = path.join(artifactsDir, pngFileName);

    console.log(`Rendering PNG via headless browser: ${pngFileName} (Height: ${cardHeight}px)...`);

    const command = `"${browserPath}" --headless=new --screenshot="${pngExportPath}" --window-size=1180,${cardHeight} --force-device-scale-factor=2 "file:///${htmlFilePath.replace(/\\/g, '/')}"`;
    execSync(command, { stdio: 'ignore' });

    // Copy to artifacts directory
    fs.copyFileSync(pngExportPath, pngArtifactPath);
    console.log(`Saved to ${pngExportPath} and artifacts.`);

    generatedCards.push({
      classKey,
      studentCount: totalStudents,
      uniformTopics,
      totalOctSessions,
      totalOctQuestions,
      batchAvgOctEfforts,
      batchAvgMastery,
      pngFileName,
      pngArtifactPath,
      pngExportPath
    });
  }

  console.log('\n--- ALL WHATSAPP CARDS GENERATED SUCCESSFULLY ---');
  console.log(JSON.stringify(generatedCards, null, 2));
}

main().catch(console.error);
