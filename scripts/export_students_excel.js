const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');
const XLSX = require('xlsx');

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
if (!admin.apps.length) {
  if (sa) {
    const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
    admin.initializeApp({ credential: admin.credential.cert(cred) });
  } else {
    admin.initializeApp({ projectId: envVars.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom' });
  }
}
const db = admin.firestore();

async function generateReport() {
  console.log('Fetching batches and students from Firestore...');
  const batchesSnap = await db.collection('batches').get();
  const batchMap = {};
  batchesSnap.forEach(doc => {
    const d = doc.data();
    batchMap[doc.id] = d.name || d.batchName || doc.id;
  });

  const studentsSnap = await db.collection('users').where('role', '==', 'student').get();
  const students = [];

  studentsSnap.forEach(doc => {
    const d = doc.data();
    // Rule 2C: Inactive students MUST be completely excluded from all active loops, rosters, and reports
    if (d.status === 'inactive') {
      return;
    }
    const batchName = batchMap[d.batchId] || d.batch || d.batchName || d.className || 'Unassigned';
    students.push({
      studentCode: d.studentCode || doc.id,
      name: d.name || d.displayName || d.studentName || 'Unknown',
      batchName: batchName,
      isAutonomous: d.autonomous === true,
      category: d.autonomous === true ? 'Autonomous' : 'Regular',
      status: (d.status || 'active').toUpperCase(),
      email: d.email || '',
      phone: d.phone || d.mobile || '',
      parentName: d.parentName || '',
      parentPhone: d.parentPhone || d.parentMobile || '',
      rollNo: d.rollNo || d.rollNumber || ''
    });
  });

  // Sort master list: Batch ASC, Category (Autonomous first), Name ASC
  students.sort((a, b) => {
    if (a.batchName !== b.batchName) return a.batchName.localeCompare(b.batchName);
    if (a.category !== b.category) return a.category === 'Autonomous' ? -1 : 1;
    return a.name.localeCompare(b.name);
  });

  // Calculate Summary Stats
  const batches = Array.from(new Set(students.map(s => s.batchName))).sort();
  const summaryRows = [];
  let grandTotal = 0;
  let grandAutonomous = 0;
  let grandRegular = 0;

  batches.forEach(bName => {
    const batchStudents = students.filter(s => s.batchName === bName);
    const autoCount = batchStudents.filter(s => s.isAutonomous).length;
    const regCount = batchStudents.filter(s => !s.isAutonomous).length;
    const totalCount = batchStudents.length;
    const autoPct = totalCount > 0 ? ((autoCount / totalCount) * 100).toFixed(1) + '%' : '0%';

    grandTotal += totalCount;
    grandAutonomous += autoCount;
    grandRegular += regCount;

    summaryRows.push({
      'Batch / Class': bName,
      'Total Students': totalCount,
      'Autonomous (A)': autoCount,
      'Regular (R)': regCount,
      'Autonomous Ratio': autoPct
    });
  });

  summaryRows.push({
    'Batch / Class': 'GRAND TOTAL',
    'Total Students': grandTotal,
    'Autonomous (A)': grandAutonomous,
    'Regular (R)': grandRegular,
    'Autonomous Ratio': grandTotal > 0 ? ((grandAutonomous / grandTotal) * 100).toFixed(1) + '%' : '0%'
  });

  const wb = XLSX.utils.book_new();

  // Helper to format student array for worksheet (Rule 2B: Zero raw student codes in UI/exports)
  const formatStudentRows = (list) => {
    return list.map((s, idx) => ({
      'Sr No': idx + 1,
      'Student Name': s.name,
      'Category': s.category,
      'Batch / Class': s.batchName,
      'Status': s.status,
      'Email': s.email,
      'Mobile / Phone': s.phone,
      'Parent Name': s.parentName,
      'Parent Phone': s.parentPhone
    }));
  };

  // Helper to set column widths
  const setCols = (ws) => {
    ws['!cols'] = [
      { wch: 8 },   // Sr No
      { wch: 30 },  // Student Name
      { wch: 16 },  // Category
      { wch: 24 },  // Batch / Class
      { wch: 12 },  // Status
      { wch: 32 },  // Email
      { wch: 16 },  // Mobile
      { wch: 26 },  // Parent Name
      { wch: 16 }   // Parent Phone
    ];
  };

  // 1. Summary Sheet
  const wsSummary = XLSX.utils.json_to_sheet(summaryRows);
  wsSummary['!cols'] = [
    { wch: 26 },
    { wch: 16 },
    { wch: 18 },
    { wch: 16 },
    { wch: 18 }
  ];
  XLSX.utils.book_append_sheet(wb, wsSummary, 'Summary');

  // 2. Master List (All Students)
  const wsMaster = XLSX.utils.json_to_sheet(formatStudentRows(students));
  setCols(wsMaster);
  XLSX.utils.book_append_sheet(wb, wsMaster, 'All Students');

  // 3. Per Batch Sheets
  batches.forEach(bName => {
    const batchStudents = students.filter(s => s.batchName === bName);
    const safeSheetName = bName.replace(/[\\/*?:[\]]/g, '').slice(0, 31);
    const wsBatch = XLSX.utils.json_to_sheet(formatStudentRows(batchStudents));
    setCols(wsBatch);
    XLSX.utils.book_append_sheet(wb, wsBatch, safeSheetName);
  });

  // 4. Autonomous Only Sheet
  const autonomousStudents = students.filter(s => s.isAutonomous);
  const wsAuto = XLSX.utils.json_to_sheet(formatStudentRows(autonomousStudents));
  setCols(wsAuto);
  XLSX.utils.book_append_sheet(wb, wsAuto, 'Autonomous (Only)');

  // 5. Regular Only Sheet
  const regularStudents = students.filter(s => !s.isAutonomous);
  const wsReg = XLSX.utils.json_to_sheet(formatStudentRows(regularStudents));
  setCols(wsReg);
  XLSX.utils.book_append_sheet(wb, wsReg, 'Regular (Only)');

  console.log('\n--- ACTIVE STUDENTS SUMMARY ---');
  console.log(JSON.stringify(summaryRows, null, 2));
  console.log(`Total Active Students: ${students.length}`);

  // Output paths - do NOT output to public/ to prevent unauthenticated PII exposure
  const outputDir = path.resolve(__dirname, '..', 'reports');

  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

  const safeWrite = (fn, desc) => {
    try {
      fn();
    } catch (e) {
      console.warn(`Could not write ${desc}: ${e.message}`);
    }
  };

  const fixedXlsx = path.join(outputDir, 'Autonomous_and_Regular_Active_Students_Batchwise.xlsx');
  const fixedXls = path.join(outputDir, 'Autonomous_and_Regular_Active_Students_Batchwise.xls');
  const fixedCsv = path.join(outputDir, 'Autonomous_and_Regular_Active_Students_Batchwise.csv');

  const defaultXlsx = path.join(outputDir, 'Autonomous_and_Regular_Students_Batchwise.xlsx');
  const defaultXls = path.join(outputDir, 'Autonomous_and_Regular_Students_Batchwise.xls');
  const defaultCsv = path.join(outputDir, 'Autonomous_and_Regular_Students_Batchwise.csv');

  safeWrite(() => XLSX.writeFile(wb, fixedXlsx), 'fixedXlsx');
  safeWrite(() => XLSX.writeFile(wb, fixedXls, { bookType: 'biff8' }), 'fixedXls');
  const csvContent = XLSX.utils.sheet_to_csv(wsMaster);
  safeWrite(() => fs.writeFileSync(fixedCsv, csvContent, 'utf-8'), 'fixedCsv');

  safeWrite(() => XLSX.writeFile(wb, defaultXlsx), 'defaultXlsx');
  safeWrite(() => XLSX.writeFile(wb, defaultXls, { bookType: 'biff8' }), 'defaultXls');
  safeWrite(() => fs.writeFileSync(defaultCsv, csvContent, 'utf-8'), 'defaultCsv');

  console.log('\nActive Student Reports Generated Successfully.');
}

generateReport().catch(console.error);
