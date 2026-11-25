const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

function fixDoubleBraces(str) {
  if (typeof str !== 'string') return str;
  return str.replace(/\\text\{\{([^}]*)\}\}/g, '\\text{$1}');
}

async function run() {
  console.log('=== Step 1: Fetch all MH Class 10 questions & create targeted pre-mutation backup ===');
  const snap = await db.collection('questions').where('boardCode', '==', 'MH').where('class', '==', '10').get();
  console.log(`Fetched ${snap.size} MH Class 10 questions.`);

  const updates = [];
  const backupDocs = [];

  for (const doc of snap.docs) {
    const q = doc.data();
    const id = doc.id;
    let txt = q.text || '';
    let sol = q.solution || '';
    let opts = Array.isArray(q.options) ? q.options.map(o => (typeof o === 'object' ? { ...o } : o)) : [];
    let correctAnswer = q.correctAnswer;
    let changed = false;

    // 1. Fix MH-10-MTH2-2-2.1.2 (Geometric Mean: CD^2 = AD * DB)
    if (q.topicCode === 'MH-10-MTH2-2-2.1.2') {
      const m = txt.match(/AD = (\d+)\\text\{ cm\}.*?DB = (\d+)\\text\{ cm\}/);
      if (m) {
        const ad = Number(m[1]), dbVal = Number(m[2]);
        const cd = Math.sqrt(ad * dbVal);
        if (!Number.isInteger(cd)) {
          const pairs = [[9, 16, 12], [2, 8, 4], [3, 12, 6], [4, 16, 8]];
          const idx = (ad + dbVal) % pairs.length;
          const [nAd, nDb, nCd] = pairs[idx];
          txt = txt
            .replace(`AD = ${ad}\\text{ cm}`, `AD = ${nAd}\\text{ cm}`)
            .replace(`DB = ${dbVal}\\text{ cm}`, `DB = ${nDb}\\text{ cm}`)
            .replace(new RegExp(`>${ad}<`, 'g'), `>${nAd}<`)
            .replace(new RegExp(`>${dbVal}<`, 'g'), `>${nDb}<`);
          const newCorrect = `\\(CD = ${nCd}\\text{ cm}\\)`;
          const newDistractors = [`\\(CD = ${nCd + 2}\\text{ cm}\\)`, `\\(CD = ${nAd + nDb}\\text{ cm}\\)`, `\\(CD = ${nCd * 2}\\text{ cm}\\)`];
          let dIdx = 0;
          opts = opts.map(o => ({
            ...o,
            text: o.isCorrect ? newCorrect : newDistractors[dIdx++]
          }));
          sol = `**Step 1: Conceptual Principle:** Theorem of Geometric Mean: In a right triangle, the altitude to the hypotenuse is the geometric mean of the segments of the hypotenuse: \\(CD^2 = AD \\times DB\\).\n\n**Step 2: Detailed Calculation:** \\(CD^2 = ${nAd} \\times ${nDb} = ${nAd * nDb} \\implies CD = \\sqrt{${nAd * nDb}} = ${nCd}\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Length of altitude \\(CD = ${nCd}\\text{ cm}\\).`;
          changed = true;
        }
      }
    }

    // 2. Fix MH-10-MTH2-2-2.2.1 (Pythagoras: BC=b, AB=h, AC=hyp)
    if (q.topicCode === 'MH-10-MTH2-2-2.2.1') {
      const m = txt.match(/BC = (\d+)\\text\{ cm\}.*?AB = (\d+)\\text\{ cm\}/);
      if (m) {
        const b = Number(m[1]), h = Number(m[2]);
        if (!Number.isInteger(Math.sqrt(b * b + h * h))) {
          const map = {
            '5,6': [6, 8, 10],
            '7,8': [8, 15, 17],
            '9,10': [5, 12, 13]
          };
          const [nb, nh, nhyp] = map[`${b},${h}`] || [6, 8, 10];
          txt = txt
            .replace(`BC = ${b}\\text{ cm}`, `BC = ${nb}\\text{ cm}`)
            .replace(`AB = ${h}\\text{ cm}`, `AB = ${nh}\\text{ cm}`)
            .replace(`>${b} cm<`, `>${nb} cm<`)
            .replace(`>${h} cm<`, `>${nh} cm<`);
          const newCorrect = `\\(AC = ${nhyp}\\text{ cm}\\)`;
          const newDistractors = [`\\(AC = ${nhyp + 2}\\text{ cm}\\)`, `\\(AC = ${nb + nh}\\text{ cm}\\)`, `\\(AC = ${nhyp - 1}\\text{ cm}\\)`];
          let dIdx = 0;
          opts = opts.map(o => ({
            ...o,
            text: o.isCorrect ? newCorrect : newDistractors[dIdx++]
          }));
          sol = `**Step 1: Conceptual Principle:** Pythagoras Theorem: In a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the other two sides: \\(AC^2 = AB^2 + BC^2\\).\n\n**Step 2: Detailed Calculation:** \\(AC^2 = (${nh})^2 + (${nb})^2 = ${nh * nh} + ${nb * nb} = ${nhyp * nhyp} \\implies AC = ${nhyp}\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** The hypotenuse length is \\(${nhyp}\\text{ cm}\\).`;
          changed = true;
        }
      }
    }

    // 3. Fix MH-10-MTH2-3-3.3.1 (Tangent Segment Length: sqrt(d^2 - r^2))
    if (q.topicCode === 'MH-10-MTH2-3-3.3.1') {
      const m = txt.match(/radius \\\((\d+)\\text\{ cm\}\\\).*?OP = (\d+)\\text\{ cm\}/);
      if (m) {
        const r = Number(m[1]), d = Number(m[2]);
        if (!Number.isInteger(Math.sqrt(d * d - r * r))) {
          const map = {
            '5,14': [6, 10, 8],
            '5,15': [8, 17, 15],
            '5,16': [9, 15, 12]
          };
          const [nr, nd, ntan] = map[`${r},${d}`] || [6, 10, 8];
          txt = txt
            .replace(`radius \\(${r}\\text{ cm}\\)`, `radius \\(${nr}\\text{ cm}\\)`)
            .replace(`OP = ${d}\\text{ cm}`, `OP = ${nd}\\text{ cm}`);
          const newCorrect = `\\(PA = PB = ${ntan}\\text{ cm}\\)`;
          const newDistractors = [
            `\\(PA = ${ntan}\\text{ cm}, PB = ${ntan + 2}\\text{ cm}\\)`,
            `\\(PA = ${nd}\\text{ cm}, PB = ${nr}\\text{ cm}\\)`,
            `\\(PA = PB = ${nd + nr}\\text{ cm}\\)`
          ];
          let dIdx = 0;
          opts = opts.map(o => ({
            ...o,
            text: o.isCorrect ? newCorrect : newDistractors[dIdx++]
          }));
          sol = `**Step 1: Conceptual Principle:** Tangent Segment Theorem: The lengths of tangent segments drawn from an external point to a circle are equal (\\(PA = PB\\)).\n\n**Step 2: Detailed Calculation:** In right \\(\\triangle OAP\\): \\(PA = \\sqrt{OP^2 - OA^2} = \\sqrt{${nd}^2 - ${nr}^2} = ${ntan}\\text{ cm}\\). Hence \\(PA = PB = ${ntan}\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Both tangent segments measure \\(${ntan}\\text{ cm}\\).`;
          changed = true;
        }
      }
    }

    // 4. Fix MH-10-MTH2-3-3.8.2 (Tangent-Secant: PT^2 = PA * PB)
    if (q.topicCode === 'MH-10-MTH2-3-3.8.2') {
      const m = txt.match(/PA = (\d+)\\text\{ cm\}.*?PB = (\d+)\\text\{ cm\}/);
      if (m) {
        const pa = Number(m[1]), pb = Number(m[2]);
        if (!Number.isInteger(Math.sqrt(pa * pb))) {
          const pairs = [[4, 9, 6], [4, 16, 8], [9, 16, 12], [2, 8, 4]];
          const [npa, npb, npt] = pairs[(pa + pb) % pairs.length];
          txt = txt
            .replace(`PA = ${pa}\\text{ cm}`, `PA = ${npa}\\text{ cm}`)
            .replace(`PB = ${pb}\\text{ cm}`, `PB = ${npb}\\text{ cm}`)
            .replace(' (nearest integer)', '');
          const newCorrect = `\\(PT = ${npt}\\text{ cm}\\)`;
          const newDistractors = [
            `\\(PT = ${npa + npb}\\text{ cm}\\)`,
            `\\(PT = ${npt + 2}\\text{ cm}\\)`,
            `\\(PT = ${npt * 2}\\text{ cm}\\)`
          ];
          let dIdx = 0;
          opts = opts.map(o => ({
            ...o,
            text: o.isCorrect ? newCorrect : newDistractors[dIdx++]
          }));
          sol = `**Step 1: Conceptual Principle:** Tangent Secant Segment Theorem: \\(PT^2 = PA \\times PB\\).\n\n**Step 2: Detailed Calculation:** \\(PT^2 = ${npa} \\times ${npb} = ${npa * npb} \\implies PT = \\sqrt{${npa * npb}} = ${npt}\\text{ cm}\\).\n\n**Step 3: Verification & Distractor Analysis:** Length \\(PT = ${npt}\\text{ cm}\\).`;
          changed = true;
        }
      }
    }

    // 5. Fix MH-10-MTH2-5-5.1.1 (Distance from origin: sqrt(x^2 + y^2))
    if (q.topicCode === 'MH-10-MTH2-5-5.1.1') {
      const m = txt.match(/P\((\d+), (\d+)\)/);
      if (m) {
        const x = Number(m[1]), y = Number(m[2]);
        if (!Number.isInteger(Math.sqrt(x * x + y * y))) {
          const map = {
            '5,6': [6, 8, 10],
            '7,8': [8, 15, 17],
            '9,10': [5, 12, 13]
          };
          const [nx, ny, nd] = map[`${x},${y}`] || [6, 8, 10];
          txt = txt.replace(`P(${x}, ${y})`, `P(${nx}, ${ny})`);
          const newCorrect = `\\(${nd}\\text{ units}\\)`;
          const newDistractors = [`\\(${nd + 2}\\text{ units}\\)`, `\\(${nx + ny}\\text{ units}\\)`, `\\(${nd * 2}\\text{ units}\\)`];
          let dIdx = 0;
          opts = opts.map(o => ({
            ...o,
            text: o.isCorrect ? newCorrect : newDistractors[dIdx++]
          }));
          sol = `**Step 1: Conceptual Principle:** Distance from origin: \\(d = \\sqrt{x^2 + y^2}\\).\n\n**Step 2: Detailed Calculation:** \\(d = \\sqrt{${nx}^2 + ${ny}^2} = \\sqrt{${nx * nx} + ${ny * ny}} = \\sqrt{${nd * nd}} = ${nd}\\text{ units}\\).\n\n**Step 3: Verification & Distractor Analysis:** Distance is \\(${nd}\\text{ units}\\).`;
          changed = true;
        }
      }
    }

    // 6. Strip mismatched Frustum SVG from Sphere questions in 7.2.1
    if (txt.includes('Frustum of a Cone') && txt.toLowerCase().includes('sphere')) {
      txt = txt.replace(/<div[^>]*>[\s\S]*?<\/svg>\s*<\/div>\s*/i, '');
      changed = true;
    }

    // 7. Fix 18 duplicate options in MH-10-MTH1
    if (opts.length >= 2 && typeof opts[0] === 'object') {
      const seen = new Set();
      let dupFound = false;
      for (let i = 0; i < opts.length; i++) {
        const t = (opts[i].text || '').trim();
        if (seen.has(t)) {
          dupFound = true;
          if (!opts[i].isCorrect) {
            if (t === '\\(\\frac{1}{6}\\)') opts[i].text = '\\(\\frac{4}{6}\\)';
            else if (t === '\\(25\\)') opts[i].text = '\\(27\\)';
            else if (t === '\\(9\\)') opts[i].text = '\\(11\\)';
            else if (t === '\\(36\\)') opts[i].text = '\\(38\\)';
          }
        }
        seen.add(opts[i].text.trim());
      }
      if (dupFound) changed = true;
    }

    // 8. Fix double-brace KaTeX \text{{...}} -> \text{...}
    const fixedTxt = fixDoubleBraces(txt);
    const fixedSol = fixDoubleBraces(sol);
    let optsBraceChanged = false;
    opts = opts.map(o => {
      if (o && typeof o === 'object' && typeof o.text === 'string') {
        const ft = fixDoubleBraces(o.text);
        if (ft !== o.text) optsBraceChanged = true;
        return { ...o, text: ft };
      }
      return o;
    });
    if (fixedTxt !== txt || fixedSol !== sol || optsBraceChanged) {
      txt = fixedTxt;
      sol = fixedSol;
      changed = true;
    }

    if (changed) {
      backupDocs.push({ id, data: q });
      updates.push({
        ref: doc.ref,
        payload: {
          text: txt,
          options: opts,
          solution: sol,
          ...(correctAnswer !== undefined ? { correctAnswer } : {}),
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        }
      });
    }
  }

  console.log(`Found ${updates.length} MH Class 10 questions to update.`);
  if (updates.length === 0) return;

  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });
  const backupFile = path.join(backupDir, `snapshot_mh10_all_defects_${Date.now()}.json`);
  fs.writeFileSync(backupFile, JSON.stringify({ count: backupDocs.length, docs: backupDocs }, null, 2), 'utf-8');
  console.log(`✓ Saved pre-mutation backup of ${backupDocs.length} docs to ${path.basename(backupFile)}`);

  let batch = db.batch();
  let count = 0;
  for (const u of updates) {
    batch.update(u.ref, u.payload);
    count++;
    if (count >= 400) {
      await batch.commit();
      batch = db.batch();
      count = 0;
    }
  }
  if (count > 0) await batch.commit();
  console.log(`✓ Successfully updated ${updates.length} MH Class 10 questions in Firestore.`);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
