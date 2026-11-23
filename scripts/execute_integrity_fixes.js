const path = require('path');
const fs = require('fs');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

async function remediateIntegrityIssues() {
  console.log('=== REMEDIATING INTEGRITY ISSUES IDENTIFIED IN SWEEP ===');

  const updates = [
    // 1. Relative references -> self-contained
    {
      qCode: 'CBSE-9-MGM-10-10.1.3-OSC-210',
      text: 'In a histogram with unequal class intervals where frequency is represented by the area of the rectangles, if two bars each represent an equal frequency of 20 but have different class widths, which of the two rectangles has a larger area?'
    },
    {
      qCode: 'CBSE-9-MGM-11-11.1.1-OSC-308',
      text: 'In an iterative loop algorithm initialized with x = 0 and condition "while x != 5" with step x = x + 2, the loop runs infinitely. How can this condition be corrected to terminate properly?'
    },
    {
      qCode: 'CBSE-9-MGM-7-7.2.1-OSC-217',
      text: 'If a fair coin is tossed 10 times and results in 10 consecutive Heads, does an empirical probability of 1 guarantee that the 11th toss will also result in a Head?'
    },

    // 2. Placeholder conversational phrasing in MH-10-SCIT2
    {
      qCode: 'MH-10-SCIT2-1-1.3.2-OSC-012',
      text: 'Which organism serves as an important connecting link illustrating the evolutionary transition between Annelida and Arthropoda?'
    },
    {
      qCode: 'MH-10-SCIT2-1-1.3.5-OSC-012',
      text: 'Which animal serves as a living connecting link between fishes and amphibians?'
    },
    {
      qCode: 'MH-10-SCIT2-1-1.5.2-OSC-030',
      text: 'Which hominid ancestor with an erect posture emerged approximately 50,000 years ago, representing Neanderthal man?'
    },

    // 3. LaTeX Delimiter Fixes
    {
      qCode: 'CBSE-9-MGM-13-13.1.2-OSC-116',
      text: 'Which linear equation models the statement: "The combined weight of two objects \\(x\\) and \\(y\\) is \\(120\\text{ kg}\\)"?'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-014',
      text: 'A bucket of sand (radius \\(15\\text{ cm}\\), height \\(20\\text{ cm}\\)) is dumped to make a conical pile of height \\(15\\text{ cm}\\). Find the radius of the pile:'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-019',
      text: 'A full cylindrical pail (radius \\(8\\text{ cm}\\), height \\(18\\text{ cm}\\)) is emptied into a cone of height \\(12\\text{ cm}\\). The radius of the heap is:'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-028',
      text: 'When \\(1000\\) spherical balls of radius \\(0.7\\text{ cm}\\), are put into a cylinder of radius \\(7\\text{ cm}\\), the water level rises by:'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-035',
      text: 'Determine the time (in minutes) required to fill a cylindrical reservoir (radius \\(5\\text{ m}\\), height \\(2\\text{ m}\\)) from a pipe of diameter \\(20\\text{ cm}\\) at velocity \\(5\\text{ km/h}\\):'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-052',
      text: 'Calculate the storage capacity in tonnes of a silo (cylinder of radius \\(7\\text{ m}\\), height \\(14\\text{ m}\\) and cone of height \\(6\\text{ m}\\)) filled with grain of density \\(750\\text{ kg/m}^3\\):'
    },
    {
      qCode: 'CBSE-9-MGM-14-14.3.2-OSC-056',
      text: 'Determine the weight in tonnes of bulk material (\\(800\\text{ kg/m}^3\\)) filling a silo of cylindrical radius \\(1.4\\text{ m}\\), height \\(5\\text{ m}\\) and conical height \\(1.5\\text{ m}\\):'
    },
    {
      qCode: 'MH-10-MTH1-1-1.3.1-OSC-006',
      text: 'Evaluate the determinant \\(\\begin{vmatrix} \\frac{7}{3} & \\frac{5}{3} \\\\ \\frac{3}{2} & \\frac{1}{2} \\end{vmatrix}\\).'
    },
    {
      qCode: 'MH-10-MTH1-1-1.3.1-OSC-007',
      text: 'Evaluate the determinant \\(\\begin{vmatrix} \\frac{7}{3} & \\frac{5}{3} \\\\ \\frac{3}{2} & \\frac{1}{2} \\end{vmatrix}\\).'
    },
    {
      qCode: 'MH-9-MTH1-2-2.5.2-OSC-219',
      text: 'If \\(x = \\sqrt{2} + 1\\), what is the value of \\(x + \\frac{1}{x}\\)?'
    },
    {
      qCode: 'MH-9-MTH1-2-2.5.2-OSC-220',
      text: 'If \\(x = 3 + 2\\sqrt{2}\\), what is the value of \\(x - \\frac{1}{x}\\)?'
    },
    {
      qCode: 'MH-9-MTH2-3-3.5.2-OSC-138',
      text: 'Compute the perimeter of \\(\\Delta PQR\\) given \\(\\frac{\\text{Perimeter}_1}{\\text{Perimeter}_2} = \\frac{3}{7}\\) and \\(\\text{Perimeter}_1 = 21\\text{ cm}\\).'
    },
    {
      qCode: 'MH-9-MTH2-6-6.1.1-OSC-314',
      text: 'In a circle with centre \\(O\\), find the measure of perpendicular segment \\(OM\\) from centre \\(O\\) to chord \\(AB = 60\\text{ cm}\\) when the circle radius is \\(34\\text{ cm}\\).'
    },
    {
      qCode: 'MH-9-MTH2-8-8.1.1-OSC-301',
      text: 'For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\sin^2 C\\) when \\(\\sin C = \\frac{11}{61}\\).'
    }
  ];

  // 4. Duplicate options in MH-10-MTH1
  const dupCodes = [
    { qCode: 'MH-10-MTH1-2-2.5.4-OSC-101', newD: '\\(k = -4\\)' },
    { qCode: 'MH-10-MTH1-2-2.6.3-OSC-101', newD: '\\(11\\)' },
    { qCode: 'MH-10-MTH1-2-2.6.3-OSC-104', newD: '\\(38\\)' },
    { qCode: 'MH-10-MTH1-2-2.6.3-OSC-107', newD: '\\(18\\)' },
    { qCode: 'MH-10-MTH1-2-2.6.3-OSC-110', newD: '\\(51\\)' }
  ];

  const targetCodes = [
    ...updates.map(u => u.qCode),
    ...dupCodes.map(d => d.qCode)
  ];

  console.log(`[Targeted Pre-Mutation Snapshot] Backing up ${targetCodes.length} targeted questions before edit...`);
  const backupDocs = [];
  for (const code of targetCodes) {
    const snap = await adminDb.collection('questions').where('questionCode', '==', code).get();
    if (snap.size > 0) {
      backupDocs.push({ id: snap.docs[0].id, data: snap.docs[0].data() });
    }
  }

  const snapshotDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(snapshotDir)) fs.mkdirSync(snapshotDir, { recursive: true });
  const snapshotPath = path.join(snapshotDir, `snapshot_targeted_integrity_remediation_${Date.now()}.json`);
  fs.writeFileSync(snapshotPath, JSON.stringify(backupDocs, null, 2));
  console.log(`✓ Targeted backup (${backupDocs.length} docs) saved to: ${snapshotPath}`);

  // Apply updates
  for (const item of updates) {
    const snap = await adminDb.collection('questions').where('questionCode', '==', item.qCode).get();
    if (snap.size > 0) {
      await snap.docs[0].ref.update({ text: item.text });
      console.log('✓ Updated stem for:', item.qCode);
    } else {
      console.log('✗ Not found:', item.qCode);
    }
  }

  // Apply dup option fixes
  for (const item of dupCodes) {
    const snap = await adminDb.collection('questions').where('questionCode', '==', item.qCode).get();
    if (snap.size > 0) {
      const d = snap.docs[0].data();
      let opts = d.options || [];
      if (opts.length === 4) {
        if (typeof opts[3] === 'object' && opts[3] !== null) {
          opts[3].text = item.newD;
        } else {
          opts[3] = item.newD;
        }
        await snap.docs[0].ref.update({ options: opts });
        console.log('✓ Fixed duplicate options for:', item.qCode);
      }
    }
  }

  console.log('\n=== REMEDIATION COMPLETED SUCCESSFULLY ===');
  process.exit(0);
}

remediateIntegrityIssues().catch(err => {
  console.error(err);
  process.exit(1);
});
