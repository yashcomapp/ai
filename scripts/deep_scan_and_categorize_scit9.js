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

// Detailed out-of-syllabus criteria by chapter for Maharashtra Board Class 9 Science
const chapterOutCriteria = {
  // Ch 9: Environmental Management (Balbharti covers Weather vs Climate, IMD, Monsoon basics, Waste types & 7Rs, Composting/Landfill, Basic first aid ABC/CPR/Burns/Sprains)
  9: [
    /differential\s+equation/i, /non-linear/i, /numerical\s+weather\s+prediction/i, /supercomput/i,
    /lapse\s+rate/i, /vapor\s+pressure/i, /anemometer.*rotat/i, /hpa\b/i, /hectopascal/i,
    /fluidized\s+bed/i, /baghouse/i, /activated\s+carbon.*dioxin/i, /dioxin/i, /landfill\s+gas.*well/i,
    /phytoremediation/i, /hyperaccumulat/i, /anaerobic\s+digestion.*hydrolytic/i, /hydrolytic\s+fermentative/i,
    /methanogen.*archaea/i, /high-pressure\s+reverse\s+osmosis/i, /reverse\s+osmosis.*leachate/i,
    /refractory\s+organics/i, /eisenia\s+fetida/i, /hdpe\s+geomembrane/i, /geomembrane/i,
    /leachate\s+collection\s+pipes/i, /gizzards.*enzymatic/i, /semi-permeable\s+membrane.*leachate/i,
    /cpcb\s+standards/i, /iswm\s+mass\s+flow/i, /flue\s+gas/i, /pyrolysis.*monomers/i, /biochar/i,
    /vasoconstriction/i, /tourniquet.*every\s+5\s+min/i, /sternum.*lower\s+half/i, /capillary\s+bleeding/i,
    /diurnal\s+temperature/i, /synoptic/i, /troposphere.*meandering/i, /jet\s+stream/i
  ],
  // Ch 10: Information Communication Technology (Balbharti covers computer devices, MS Word/Excel/PowerPoint basics, utility of ICT)
  10: [
    /gigaflops/i, /teraflops/i, /petaflops/i, /top500\s+ai/i, /national\s+supercomputing\s+mission/i,
    /in-silico\s+screening/i, /molecular\s+mechanics/i, /quantum\s+simulations/i, /param\s+siddhi/i,
    /parallel\s+algorithm/i, /indigenous\s+server/i
  ],
  // Ch 15: Life Processes in Living Organisms (Balbharti covers Transportation in plants (xylem/phloem), Excretion in plants/animals, Human kidney/nephron basics, Control & Coordination nervous system & endocrine glands basics)
  15: [
    /potometer/i, /hydrostatic\s+tension.*eucalyptus/i, /urea\s+excreted\s+daily/i,
    /glomerular\s+filtration\s+rate/i, /gfr\b/i, /filtration\s+fraction/i, /active\s+symport/i,
    /podocyte\s+filtration\s+slits/i, /fenestrated\s+endothelium/i, /efferent\s+arteriole.*bottleneck/i,
    /proteinuria/i, /hematuria/i, /myelinated\s+axon.*speed/i, /nerve\s+impulse.*milliseconds/i,
    /31\s+pairs\s+of\s+spinal\s+nerves/i, /62\s+individual\s+spinal\s+nerves/i,
    /auxin\s+concentration.*ratio/i, /ethylene.*ripening.*days/i, /parathyroid\s+glands.*posterior/i
  ],
  // Ch 16: Heredity and Variation (Balbharti covers Inheritance, Chromosomes (structure, types), DNA/RNA basics, Mendel's laws (monohybrid/dihybrid ratios), Genetic disorders (Down, Turner, Klinefelter, Sickle cell))
  16: [
    /domestic\s+dog\s*\(2n\s*=\s*78\)/i, /mitotic\s+metaphase.*chromatids/i,
    /adenine.*cytosine.*percentage/i, /helical\s+turns.*base\s+pairs/i,
    /chargaff/i, /b-dna/i, /okazaki/i, /topoisomerase/i, /dna\s+gyrase/i,
    /palindromic\s+restriction/i
  ],
  // Ch 17: Introduction to Biotechnology (Balbharti covers Plant tissue culture, Agricultural biotechnology, Animal husbandry, Sericulture basics)
  17: [
    /phytoremediation/i, /somatostatin/i, /elisa\s+test.*antibody/i, /western\s+blot/i,
    /electrophoresis\s+agarose/i, /southern\s+blot/i, /pcr\s+primer\s+annealing/i,
    /taq\s+polymerase.*thermus\s+aquaticus/i
  ],
  // Ch 18: Observing Space: Telescopes (Balbharti covers Optical telescopes, Radio telescopes, ISRO/GMRT, Hubble, Chandra)
  18: [
    /relativistic\s+beaming/i, /synchrotron\s+emission/i, /schwarzschild\s+radius/i,
    /lorentz\s+factor/i, /bragg's\s+law/i
  ]
};

async function deepScan() {
  const snap = await db.collection('questions')
    .where('subjectCode', '==', 'SCIT')
    .where('class', 'in', ['9', 9])
    .get();

  console.log(`Analyzing ${snap.size} questions in Class 9 Science across all 18 chapters...`);

  const flagged = [];
  const byChapter = {};

  snap.forEach(d => {
    const q = d.data();
    const ch = Number(q.chapterNumber);
    byChapter[ch] = byChapter[ch] || { total: 0, flagged: 0, byReason: {} };
    byChapter[ch].total++;

    const str = `${q.text || ''} ${q.solution || ''} ${q.explanation || ''}`;
    const patterns = chapterOutCriteria[ch] || [];

    let isOut = false;
    let reason = '';

    // Check specific out-of-syllabus criteria
    for (const pat of patterns) {
      if (pat.test(str)) {
        isOut = true;
        reason = pat.toString();
        break;
      }
    }

    // Check artificial ONE questions in pure theory chapters (Ch 6, 7, 8, 9, 10, 15, 16, 17)
    const pureTheoryChs = [6, 7, 8, 9, 10, 15, 16, 17];
    if (!isOut && pureTheoryChs.includes(ch) && q.type === 'ONE') {
      // Check if text is artificial calculation
      if (/transpires|hydrostatic|excreted|filtered|auxin|ethylene|impulse|spinal\s+nerves|chromatid|autosome|adenine|helical\s+turns|gigaflops|teraflops|anemometer|lapse\s+rate|vapor\s+pressure|methane\s+captured|earthworm.*converts/i.test(str)) {
        isOut = true;
        reason = 'Artificial numerical in pure theory chapter';
      }
    }

    if (isOut) {
      flagged.push({
        id: d.id,
        chapter: ch,
        topicCode: q.topicCode,
        type: q.type,
        text: q.text,
        sol: q.solution || q.explanation,
        reason
      });
      byChapter[ch].flagged++;
      byChapter[ch].byReason[reason] = (byChapter[ch].byReason[reason] || 0) + 1;
    }
  });

  console.log('\n======================================================');
  console.log(`TOTAL OUT-OF-SYLLABUS QUESTIONS IDENTIFIED IN SCIT 9: ${flagged.length}`);
  console.log('======================================================');

  Object.keys(byChapter).sort((a,b) => Number(a) - Number(b)).forEach(ch => {
    console.log(`Chapter ${ch}: ${byChapter[ch].flagged} out-of-syllabus / ${byChapter[ch].total} total`);
  });

  fs.writeFileSync('scripts/scit9_out_of_syllabus_remedy_list.json', JSON.stringify(flagged, null, 2));
  console.log('Saved remedy list to scripts/scit9_out_of_syllabus_remedy_list.json');
}

deepScan().then(() => process.exit(0)).catch(console.error);
