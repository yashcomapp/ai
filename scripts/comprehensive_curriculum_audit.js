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

async function runGlobalCurriculumAudit() {
  console.log('--- Scanning all questions in Question Bank for out-of-syllabus college/engineering content ---');
  const snap = await db.collection('questions').get();
  console.log(`Total questions loaded: ${snap.size}`);

  // Patterns that define clearly out-of-syllabus college/engineering/advanced content for Classes 8-10
  const outOfSyllabusPatterns = [
    // Higher engineering / Atmospheric physics
    /\bdifferential\s+equations?\b/i,
    /\bnon-linear\s+equations?\b/i,
    /\blapse\s+rate\b/i,
    /\bactual\s+vapor\s+pressure\b/i,
    /\bsaturation\s+vapor\s+pressure\b/i,
    /\banemometer\s+rotates\b/i,
    /\bfluidized\s+bed\b/i,
    /\bbaghouse\s+filters?\b/i,
    /\bactivated\s+carbon\s+injection\b/i,
    /\bdioxins?\s+and\s+mercury\b/i,
    /\blandfill\s+gas\s+collection\s+well\b/i,
    /\bphytoremediation\b/i,
    /\bhyperaccumulat/i,
    /\bhydrolytic\s+fermentative\b/i,
    /\bmethanogenic\s+archaea\b/i,
    /\bhigh-pressure\s+reverse\s+osmosis\b/i,
    /\brefractory\s+organics\b/i,
    /\beisenia\s+fetida\b/i,
    /\bhdpe\s+geomembrane\b/i,

    // Advanced biology/medical school
    /\bglomerular\s+filtrat/i,
    /\bpotometer\s+transpires\b/i,
    /\bhydrostatic\s+tension.*eucalyptus\b/i,
    /\burea\s+excreted\s+daily\b/i,
    /\b31\s+pairs\s+of\s+spinal\s+nerves\b/i,
    /\bdomestic\s+dog\s*\(2n\s*=\s*78\)/i,
    /\bchromatids\s+are\s+present.*mitotic\s+metaphase\b/i,
    /\bdouble-stranded\s+dna\s+contains\s+30%\s+adenine\b/i,
    /\b100\s+complete\s+helical\s+turns\b/i,
    /\bvasoconstriction,\s+curbing\s+internal\s+capillary\b/i,
    /\bparathyroid\s+glands\s+embedded\b/i,
    /\bmyelinated\s+axon\b/i,

    // Supercomputing / Advanced ICT
    /\bgigaflops\s+are\s+in\s+exactly\b/i,
    /\bteraflops\s+are\s+contained\b/i,
    /\btop500\s+ai\s+systems\b/i,
    /\bnational\s+supercomputing\s+mission\b/i,
    /\bbenchmark\s+unit.*measure\s+computational\s+performance\s+of\s+supercomputers\b/i
  ];

  const flagged = [];
  const bySubject = {};

  snap.forEach(d => {
    const q = d.data();
    const str = `${q.text || ''} ${q.solution || ''} ${q.explanation || ''}`;
    const sub = q.subjectCode || 'UNKNOWN';
    const cl = q.class || 'UNKNOWN';
    const key = `${sub}-Cl${cl}`;
    bySubject[key] = bySubject[key] || { total: 0, flagged: 0 };
    bySubject[key].total++;

    const isMatch = outOfSyllabusPatterns.some(p => p.test(str));
    if (isMatch) {
      flagged.push({
        id: d.id,
        subject: sub,
        class: cl,
        topicCode: q.topicCode,
        chapter: q.chapterNumber,
        type: q.type,
        text: q.text,
        sol: q.solution || q.explanation,
        used: q.used || q.usageCount > 0 || q.timesUsed > 0
      });
      bySubject[key].flagged++;
    }
  });

  console.log(`\n======================================================`);
  console.log(`GLOBAL AUDIT RESULTS: ${flagged.length} OUT-OF-SYLLABUS QUESTIONS FLAGGED`);
  console.log(`======================================================`);

  for (const [k, v] of Object.entries(bySubject)) {
    console.log(`${k}: ${v.flagged} flagged out of ${v.total} questions`);
  }

  const usedFlagged = flagged.filter(f => f.used);
  console.log(`\nTotal flagged used questions: ${usedFlagged.length}`);
  if (usedFlagged.length > 0) {
    usedFlagged.forEach(f => {
      console.log(`  USED: ${f.id} (${f.topicCode}): ${f.text.slice(0, 80)}`);
    });
  }

  // Save the complete list of flagged questions to a file for transparent processing
  fs.writeFileSync('scripts/flagged_out_of_syllabus_questions.json', JSON.stringify(flagged, null, 2));
  console.log(`Saved detailed list to scripts/flagged_out_of_syllabus_questions.json`);
}

runGlobalCurriculumAudit().then(() => process.exit(0)).catch(console.error);
