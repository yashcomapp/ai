const path = require('path');
const fs = require('fs');

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

const admin = require('firebase-admin');
const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
admin.initializeApp({
  credential: admin.credential.cert(JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8')))
});
const db = admin.firestore();

// 5 Diagram-Based Questions with High-Precision Inline SVGs
const questionsData = [
  {
    questionCode: 'MH-10-MTH2-1-1.4-OSC-501',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapter: 'Similarity',
    chapterNumber: '1',
    topic: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicName: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicCode: 'MH-10-MTH2-1-1.4',
    topicNumber: '1.4',
    type: 'OSC',
    vault: 'exam',
    difficulty: 'easy',
    bloomLevel: 'Understand',
    marks: 4,
    positiveMarks: 4,
    negativeMarks: 0,
    conceptTag: 'AA Similarity Test',
    requiresFigure: true,
    text: `In the figures given below, \\(\\triangle ABC\\) and \\(\\triangle PQR\\) are given with marked angle measures:

<svg viewBox="0 0 440 180" width="100%" height="180" style="max-width:440px; display:block; margin:12px auto; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Grid / subtle styling -->
  <defs>
    <marker id="dot" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4">
      <circle cx="5" cy="5" r="4" fill="#2563eb"/>
    </marker>
  </defs>
  
  <!-- Triangle ABC -->
  <polygon points="70,30 20,150 150,150" fill="rgba(37,99,235,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices ABC -->
  <text x="68" y="22" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>
  <text x="10" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="156" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  
  <!-- Angles in ABC -->
  <!-- Angle A = 60 deg -->
  <path d="M 60,50 A 22 22 0 0 0 80,50" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="70" y="66" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#2563eb" text-anchor="middle">60°</text>
  <!-- Angle B = 75 deg -->
  <path d="M 40,150 A 24 24 0 0 1 30,132" fill="none" stroke="#16a34a" stroke-width="2"/>
  <text x="44" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#16a34a">75°</text>
  
  <!-- Triangle PQR (Similar) -->
  <polygon points="310,45 250,150 390,150" fill="rgba(22,163,74,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices PQR -->
  <text x="310" y="37" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">P</text>
  <text x="238" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Q</text>
  <text x="396" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">R</text>
  
  <!-- Angles in PQR -->
  <!-- Angle Q = 75 deg -->
  <path d="M 270,150 A 24 24 0 0 1 260,132" fill="none" stroke="#16a34a" stroke-width="2"/>
  <text x="274" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#16a34a">75°</text>
  <!-- Angle R = 45 deg -->
  <path d="M 370,150 A 24 24 0 0 0 376,134" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="352" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#dc2626">45°</text>
</svg>

By which test of similarity are \\(\\triangle ABC\\) and \\(\\triangle PQR\\) similar, under the correspondence \\(ABC \\leftrightarrow PQR\\)?`,
    options: [
      'AA Test of Similarity',
      'SAS Test of Similarity',
      'SSS Test of Similarity',
      'The triangles are NOT similar'
    ],
    correctAnswer: 'AA Test of Similarity',
    solution: `**Step-by-step Solution:**
1. In \\(\\triangle ABC\\), the sum of all interior angles is \\(180^\\circ\\):
   \\[
   \\angle C = 180^\\circ - (\\angle A + \\angle B) = 180^\\circ - (60^\\circ + 75^\\circ) = 180^\\circ - 135^\\circ = 45^\\circ
   \\]
2. Comparing corresponding angles in \\(\\triangle ABC\\) and \\(\\triangle PQR\\):
   - \\(\\angle B \\cong \\angle Q = 75^\\circ\\)
   - \\(\\angle C \\cong \\angle R = 45^\\circ\\)
3. Since two pairs of corresponding angles are congruent, by the **AA Test of Similarity**, \\(\\triangle ABC \\sim \\triangle PQR\\).`
  },

  {
    questionCode: 'MH-10-MTH2-1-1.4-OSC-502',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapter: 'Similarity',
    chapterNumber: '1',
    topic: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicName: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicCode: 'MH-10-MTH2-1-1.4',
    topicNumber: '1.4',
    type: 'OSC',
    vault: 'exam',
    difficulty: 'medium',
    bloomLevel: 'Apply',
    marks: 4,
    positiveMarks: 4,
    negativeMarks: 0,
    conceptTag: 'SAS Similarity Test',
    requiresFigure: true,
    text: `Observe \\(\\triangle KLM\\) and \\(\\triangle XYZ\\) with the side lengths and included angles indicated:

<svg viewBox="0 0 440 180" width="100%" height="180" style="max-width:440px; display:block; margin:12px auto; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Triangle KLM (Larger) -->
  <polygon points="40,150 160,150 70,60" fill="rgba(14,165,233,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices -->
  <text x="30" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">K</text>
  <text x="166" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">M</text>
  <text x="68" y="50" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">L</text>
  
  <!-- Dimension Labels -->
  <text x="40" y="100" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">6</text>
  <text x="125" y="100" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">10</text>
  <!-- Angle L = 50 deg -->
  <path d="M 64,74 A 20 20 0 0 0 85,74" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="74" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#d97706" text-anchor="middle">50°</text>

  <!-- Triangle XYZ (Smaller, scaled 1:2) -->
  <polygon points="260,150 320,150 275,105" fill="rgba(245,158,11,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices -->
  <text x="250" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">X</text>
  <text x="326" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Z</text>
  <text x="275" y="96" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Y</text>
  
  <!-- Dimension Labels -->
  <text x="256" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">3</text>
  <text x="306" y="125" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">5</text>
  <!-- Angle Y = 50 deg -->
  <path d="M 271,114 A 14 14 0 0 0 284,114" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="278" y="128" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#d97706" text-anchor="middle">50°</text>
</svg>

Which statement correctly identifies the relationship between \\(\\triangle KLM\\) and \\(\\triangle XYZ\\)?`,
    options: [
      '\\(\\triangle KLM \\sim \\triangle XYZ\\) by SAS Test of similarity',
      '\\(\\triangle KLM \\cong \\triangle XYZ\\) by SAS Congruence test',
      '\\(\\triangle KLM \\sim \\triangle XYZ\\) by SSS Test of similarity',
      'The triangles are not similar because their sides are not equal'
    ],
    correctAnswer: '\\(\\triangle KLM \\sim \\triangle XYZ\\) by SAS Test of similarity',
    solution: `**Step-by-step Solution:**
1. Check the ratio of corresponding sides containing the angle:
   \\[
   \\frac{KL}{XY} = \\frac{6}{3} = 2
   \\]
   \\[
   \\frac{LM}{YZ} = \\frac{10}{5} = 2
   \\]
   Therefore, \\(\\frac{KL}{XY} = \\frac{LM}{YZ} = 2\\).
2. The included angles between these sides are congruent:
   \\[
   \\angle KLM \\cong \\angle XYZ = 50^\\circ
   \\]
3. Since two pairs of sides are in the same proportion and the included angles are congruent, the triangles are similar by the **SAS Test of Similarity** (\\(\\triangle KLM \\sim \\triangle XYZ\\)). Note that they are NOT congruent because the ratio of sides is \\(2:1 \\neq 1\\).`
  },

  {
    questionCode: 'MH-10-MTH2-1-1.4-OSC-503',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapter: 'Similarity',
    chapterNumber: '1',
    topic: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicName: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicCode: 'MH-10-MTH2-1-1.4',
    topicNumber: '1.4',
    type: 'OSC',
    vault: 'exam',
    difficulty: 'medium',
    bloomLevel: 'Apply',
    marks: 4,
    positiveMarks: 4,
    negativeMarks: 0,
    conceptTag: 'Vertically Opposite Angles Similarity',
    requiresFigure: true,
    text: `In the given figure, line segments \\(AD\\) and \\(BC\\) intersect each other at point \\(P\\).

<svg viewBox="0 0 440 200" width="100%" height="200" style="max-width:440px; display:block; margin:12px auto; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Intersecting lines AD and BC -->
  <!-- A=(40,40), D=(400,160), P=(220,100) -->
  <!-- B=(40,160), C=(400,40) -->
  <line x1="40" y1="40" x2="400" y2="160" stroke="#64748b" stroke-width="2"/>
  <line x1="40" y1="160" x2="400" y2="40" stroke="#64748b" stroke-width="2"/>
  
  <!-- Left triangle boundary AB -->
  <line x1="40" y1="40" x2="40" y2="160" stroke="#2563eb" stroke-width="2.5"/>
  <!-- Right triangle boundary CD -->
  <line x1="400" y1="40" x2="400" y2="160" stroke="#16a34a" stroke-width="2.5"/>
  
  <!-- Fill triangles -->
  <polygon points="40,40 220,100 40,160" fill="rgba(37,99,235,0.06)"/>
  <polygon points="400,40 220,100 400,160" fill="rgba(22,163,74,0.06)"/>

  <!-- Intersection P -->
  <circle cx="220" cy="100" r="4" fill="#0f172a"/>
  <text x="220" y="88" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">P</text>

  <!-- Vertices -->
  <text x="24" y="44" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="24" y="166" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="408" y="44" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="408" y="166" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">D</text>

  <!-- Segment lengths -->
  <!-- AP = 8 -->
  <text x="120" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">AP = 8</text>
  <!-- PD = 4 -->
  <text x="310" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#16a34a">PD = 4</text>
  <!-- BP = 6 -->
  <text x="120" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#2563eb">BP = 6</text>
  <!-- PC = 3 -->
  <text x="310" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#16a34a">PC = 3</text>
  <!-- CD = 5 -->
  <text x="414" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">CD = 5</text>
</svg>

Given \\(AP = 8\\text{ cm}\\), \\(PD = 4\\text{ cm}\\), \\(BP = 6\\text{ cm}\\), \\(PC = 3\\text{ cm}\\), and \\(CD = 5\\text{ cm}\\). Find the length of side \\(AB\\):`,
    options: [
      '10 cm',
      '12 cm',
      '8 cm',
      '15 cm'
    ],
    correctAnswer: '10 cm',
    solution: `**Step-by-step Solution:**
1. In \\(\\triangle APB\\) and \\(\\triangle DPC\\):
   - Vertically opposite angles are equal: \\(\\angle APB \\cong \\angle DPC\\).
   - Check the ratios of sides containing these angles:
     \\[
     \\frac{AP}{DP} = \\frac{8}{4} = 2
     \\]
     \\[
     \\frac{BP}{CP} = \\frac{6}{3} = 2
     \\]
   - Therefore, \\(\\frac{AP}{DP} = \\frac{BP}{CP} = 2\\).
2. By the **SAS Test of Similarity**, \\(\\triangle APB \\sim \\triangle DPC\\).
3. Since corresponding sides of similar triangles are in proportion:
   \\[
   \\frac{AB}{CD} = \\frac{AP}{DP} = 2
   \\]
   \\[
   \\frac{AB}{5} = 2 \\implies AB = 5 \\times 2 = 10\\text{ cm}.
   \\]`
  },

  {
    questionCode: 'MH-10-MTH2-1-1.4-OSC-504',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapter: 'Similarity',
    chapterNumber: '1',
    topic: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicName: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicCode: 'MH-10-MTH2-1-1.4',
    topicNumber: '1.4',
    type: 'OSC',
    vault: 'exam',
    difficulty: 'medium',
    bloomLevel: 'Analyze',
    marks: 4,
    positiveMarks: 4,
    negativeMarks: 0,
    conceptTag: 'Right Triangle Nested Similarity',
    requiresFigure: true,
    text: `In the given figure, \\(\\triangle ABC\\) has \\(\\angle ABC = 90^\\circ\\). Segment \\(DE \\perp AC\\) at point \\(D\\), where \\(E\\) lies on side \\(AB\\):

<svg viewBox="0 0 440 210" width="100%" height="210" style="max-width:440px; display:block; margin:12px auto; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Right triangle ABC with right angle at B=(60,170), A=(60,30), C=(380,170) -->
  <polygon points="60,30 60,170 380,170" fill="rgba(37,99,235,0.04)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  
  <!-- Right angle at B -->
  <rect x="60" y="152" width="18" height="18" fill="none" stroke="#2563eb" stroke-width="2"/>
  
  <!-- D on AC: AC goes from (60,30) to (380,170). Pick D=(180, 82.5) -->
  <!-- E on AB: AB is vertical x=60. Slope of AC is 140/320 = 7/16. Perpendicular slope is -16/7 -->
  <!-- Line from D=(180,82.5) with slope -16/7 goes to AB at y = 82.5 + (18/7)*16 ... Let's make E at (60, 135) and D perpendicular -->
  <line x1="60" y1="130" x2="190" y2="87" stroke="#dc2626" stroke-width="2.5"/>
  <polygon points="60,30 60,130 190,87" fill="rgba(220,38,38,0.08)"/>
  
  <!-- Right angle at D on line AC -->
  <path d="M 182,84 L 178,96 L 186,99" fill="none" stroke="#dc2626" stroke-width="2"/>
  
  <!-- Points -->
  <circle cx="60" cy="30" r="4" fill="#0f172a"/>
  <circle cx="60" cy="170" r="4" fill="#0f172a"/>
  <circle cx="380" cy="170" r="4" fill="#0f172a"/>
  <circle cx="60" cy="130" r="4" fill="#dc2626"/>
  <circle cx="190" cy="87" r="4" fill="#dc2626"/>

  <!-- Labels -->
  <text x="56" y="22" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="end">A</text>
  <text x="44" y="180" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="390" y="180" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="44" y="134" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#dc2626">E</text>
  <text x="200" y="82" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#dc2626">D</text>
</svg>

Which similarity test proves that \\(\\triangle ADE \\sim \\triangle ABC\\)?`,
    options: [
      'AA Test of Similarity (common \\(\\angle A\\), and \\(\\angle ADE = \\angle ABC = 90^\\circ\\))',
      'Hypotenuse-Side Congruence Test',
      'SAS Test of Similarity',
      'SSS Test of Similarity'
    ],
    correctAnswer: 'AA Test of Similarity (common \\(\\angle A\\), and \\(\\angle ADE = \\angle ABC = 90^\\circ\\))',
    solution: `**Step-by-step Solution:**
1. Consider \\(\\triangle ADE\\) and \\(\\triangle ABC\\):
   - \\(\\angle DAE = \\angle BAC\\) (Common angle at vertex \\(A\\)).
   - \\(\\angle ADE = \\angle ABC = 90^\\circ\\) (Both are right angles as \\(DE \\perp AC\\) and \\(\\angle B = 90^\\circ\\)).
2. Since two pairs of corresponding angles are congruent:
   \\[
   \\triangle ADE \\sim \\triangle ABC \\quad \\text{by AA Test of Similarity.}
   \\]`
  },

  {
    questionCode: 'MH-10-MTH2-1-1.4-OSC-505',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapter: 'Similarity',
    chapterNumber: '1',
    topic: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicName: 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)',
    topicCode: 'MH-10-MTH2-1-1.4',
    topicNumber: '1.4',
    type: 'OSC',
    vault: 'exam',
    difficulty: 'easy',
    bloomLevel: 'Understand',
    marks: 4,
    positiveMarks: 4,
    negativeMarks: 0,
    conceptTag: 'Congruence as a Special Case of Similarity',
    requiresFigure: true,
    text: `Study the two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\) shown in the figure with marked identical side lengths:

<svg viewBox="0 0 440 180" width="100%" height="180" style="max-width:440px; display:block; margin:12px auto; background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Triangle ABC -->
  <polygon points="40,150 160,150 100,50" fill="rgba(16,185,129,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices -->
  <text x="30" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="166" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="100" y="40" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">C</text>
  <!-- Side tick marks & lengths -->
  <text x="60" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669">5 cm</text>
  <text x="135" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669">7 cm</text>
  <text x="100" y="166" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">6 cm</text>

  <!-- Triangle DEF (Identical dimensions) -->
  <polygon points="270,150 390,150 330,50" fill="rgba(16,185,129,0.06)" stroke="#1e293b" stroke-width="2.5" stroke-linejoin="round"/>
  <!-- Vertices -->
  <text x="260" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">D</text>
  <text x="396" y="162" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">E</text>
  <text x="330" y="40" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">F</text>
  <!-- Side tick marks & lengths -->
  <text x="290" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669">5 cm</text>
  <text x="365" y="95" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669">7 cm</text>
  <text x="330" y="166" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#059669" text-anchor="middle">6 cm</text>
</svg>

Which statement is mathematically **TRUE** regarding \\(\\triangle ABC\\) and \\(\\triangle DEF\\)?`,
    options: [
      'They are both congruent (\\(\\triangle ABC \\cong \\triangle DEF\\)) and similar (\\(\\triangle ABC \\sim \\triangle DEF\\)) with similarity ratio \\(1:1\\)',
      'They are congruent but NOT similar',
      'They are similar with ratio \\(1:2\\)',
      'They cannot be proven similar without knowing angle measures'
    ],
    correctAnswer: 'They are both congruent (\\(\\triangle ABC \\cong \\triangle DEF\\)) and similar (\\(\\triangle ABC \\sim \\triangle DEF\\)) with similarity ratio \\(1:1\\)',
    solution: `**Step-by-step Solution:**
1. **Congruence:**
   Since all three corresponding sides are equal in length:
   \\[
   AC = DF = 5\\text{ cm}, \\quad AB = DE = 6\\text{ cm}, \\quad BC = EF = 7\\text{ cm}
   \\]
   By the **SSS Congruence Criterion**, \\(\\triangle ABC \\cong \\triangle DEF\\).
2. **Similarity:**
   The ratios of corresponding sides are:
   \\[
   \\frac{AC}{DF} = \\frac{AB}{DE} = \\frac{BC}{EF} = \\frac{1}{1} = 1
   \\]
   Since all corresponding sides are in constant proportion (scale factor \\(k = 1\\)), by the **SSS Test of Similarity**, \\(\\triangle ABC \\sim \\triangle DEF\\).
3. **Fundamental Principle:**
   *All congruent figures are similar with a scale factor of 1*, whereas similar figures are congruent only if their scale factor is 1.`
  }
];

async function run() {
  console.log('1. Upserting 5 Diagram-Based Questions into "questions" collection...');
  for (const q of questionsData) {
    const qDocRef = db.collection('questions').doc(q.questionCode);
    await qDocRef.set({
      ...q,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      createdBy: 'admin@yashcom.com'
    }, { merge: true });
    console.log(`   ✓ Saved question: ${q.questionCode}`);
  }

  const examId = '001-MH-10-Geometry-Similarity-Tests-061026';
  const examName = '001-MH-10-Geometry-Similarity-Tests-061026';
  const examTitle = 'Class 10 Geometry: Similarity & Congruency Tests (Diagram Suite)';
  const questionCodes = questionsData.map(q => q.questionCode);

  console.log('\n2. Creating Exam document in "exams" collection...');
  const examPayload = {
    id: examId,
    examId: examId,
    sequence: 1,
    sequence3digit: '001',
    name: examName,
    title: examTitle,
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subjectCode: 'MTH2',
    subjects: ['Mathematics Part - 2 (Geometry)'],
    chapter: 'Similarity',
    chapterNumber: '1',
    topicCodes: ['MH-10-MTH2-1-1.4'],
    topicNames: ['Tests of Similarity of Triangles (AAA, AA, SAS, SSS)'],
    isMixed: false,
    examType: 'obj',
    totalMarks: 20, // 5 questions * 4 marks
    questionCount: 5,
    duration: 20, // 20 minutes
    positiveMarks: 4,
    negativeMarks: 0,
    status: 'active',
    createdBy: 'admin@yashcom.com',
    source: 'exam_generator',
    templateId: 'daily_topic_5',
    templateDetails: {
      id: 'daily_topic_5',
      name: 'Similarity Diagram Objective Test (5 Questions • 20 Mins • 20 Marks)',
      totalQuestions: 5,
      duration: 20,
      positiveMarks: 4,
      negativeMarks: 0,
      examCategory: 'standard'
    },
    questionCodes: questionCodes,
    questions: questionsData.map(q => ({
      id: q.questionCode,
      questionCode: q.questionCode,
      text: q.text,
      type: q.type,
      options: q.options,
      correctAnswer: q.correctAnswer,
      solution: q.solution,
      marks: q.marks,
      difficulty: q.difficulty,
      bloomLevel: q.bloomLevel,
      requiresFigure: true
    })),
    createdAt: admin.firestore.FieldValue.serverTimestamp(),
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  };

  await db.collection('exams').doc(examId).set(examPayload, { merge: true });
  console.log(`   ✓ Exam created: ${examId}`);

  console.log('\n3. Finding Class 10 Students in batch "2X6IKivAqbush6AQb92n"...');
  const targetBatchId = '2X6IKivAqbush6AQb92n';
  const studentsSnap = await db.collection('users')
    .where('role', '==', 'student')
    .get();

  const assignedStudentCodes = [];
  studentsSnap.forEach(doc => {
    const s = doc.data();
    if (s.status !== 'inactive') {
      const isClass10 = String(s.className || s.class).includes('10');
      const inBatch = s.batchId === targetBatchId || (Array.isArray(s.batchIds) && s.batchIds.includes(targetBatchId));
      if (isClass10 || inBatch) {
        assignedStudentCodes.push(s.studentCode);
      }
    }
  });

  console.log(`   Found ${assignedStudentCodes.length} active Class 10 students.`);

  console.log('\n4. Assigning Exam to Batch & Students in "batchAssignments"...');
  const now = new Date();
  const twoWeeksLater = new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000);

  const assignmentPayload = {
    examId: examId,
    targetType: 'batch',
    targetBatches: [targetBatchId],
    targetStudents: assignedStudentCodes,
    openMode: 'immediate',
    startAt: admin.firestore.Timestamp.fromDate(now),
    endAt: admin.firestore.Timestamp.fromDate(twoWeeksLater),
    attemptLimit: 3,
    lateEntryRestriction: false,
    status: 'active',
    createdBy: 'admin@yashcom.com',
    createdAt: admin.firestore.FieldValue.serverTimestamp(),
    updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    title: examTitle,
    assignmentType: 'exam',
    examDuration: 20
  };

  // Check if assignment exists
  const existingAssignSnap = await db.collection('batchAssignments')
    .where('examId', '==', examId)
    .get();

  let assignmentDocId;
  if (!existingAssignSnap.empty) {
    assignmentDocId = existingAssignSnap.docs[0].id;
    await existingAssignSnap.docs[0].ref.set(assignmentPayload, { merge: true });
    console.log(`   ✓ Updated existing assignment: ${assignmentDocId}`);
  } else {
    const docRef = await db.collection('batchAssignments').add(assignmentPayload);
    assignmentDocId = docRef.id;
    console.log(`   ✓ Created new assignment: ${assignmentDocId}`);
  }

  console.log('\n========================================');
  console.log('SUCCESSFULLY CREATED AND ASSIGNED EXAM!');
  console.log('Exam ID:', examId);
  console.log('Assignment ID:', assignmentDocId);
  console.log('Target Batch:', targetBatchId, '(Class 10 State Board)');
  console.log('Students Assigned Count:', assignedStudentCodes.length);
  console.log('Question Codes:', questionCodes.join(', '));
  console.log('========================================');
}

run().then(() => process.exit(0)).catch(err => {
  console.error('FAILED:', err);
  process.exit(1);
});
