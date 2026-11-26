// scripts/clean_bad_worded_questions.js
// Cleans badly worded, templated, and unnecessary board/study-prefix questions in Firestore.
// Usage: node scripts/clean_bad_worded_questions.js [--dry-run]
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();

const { adminDb } = require('../src/lib/firebase/admin.ts');

const DRY_RUN = process.argv.includes('--dry-run');
const SCAN_PATH = 'C:/Users/Admin/.gemini/antigravity/brain/eef894ba-e298-45ca-bd0e-3186ef25eb6f/scratch/bad_questions_scan.json';

const CONCEPT_QUESTIONS = {
  "Laws of Reflection of light": "Which statement accurately describes the laws of reflection of light?",
  "Plane mirror image characteristics": "What are the characteristics of an image formed by a plane mirror?",
  "Concave spherical mirror (Converging mirror)": "Which of the following is a characteristic property of a concave spherical mirror (converging mirror)?",
  "Convex spherical mirror (Diverging mirror)": "Which of the following is a characteristic property of a convex spherical mirror (diverging mirror)?",
  "relationship between radius of curvature R and focal length f of a spherical mirror": "What is the relationship between the radius of curvature \\(R\\) and focal length \\(f\\) of a spherical mirror?",
  "Mirror Formula relating object distance u, image distance v, and focal length f": "Which equation represents the mirror formula relating object distance \\(u\\), image distance \\(v\\), and focal length \\(f\\)?",
  "why convex mirrors are used as rear-view mirrors in vehicles": "Why are convex mirrors used as rear-view mirrors in vehicles?",
  "mechanical nature of sound waves": "Why are sound waves classified as mechanical waves?",
  "speed of sound across different states of matter": "How does the speed of sound compare across solids, liquids, and gases?",
  "relationship between wave velocity v, frequency f, and wavelength λ": "What is the relationship between wave velocity \\(v\\), frequency \\(f\\), and wavelength \\(\\lambda\\)?",
  "audible range of sound frequencies for human hearing": "What is the audible range of sound frequencies for human hearing?",
  "condition required to hear a distinct echo of sound in air at 22 °C (speed ~344 m/s)": "What is the minimum distance required to hear a distinct echo in air at \\(22\\,^\\circ\\text{C}\\) (speed of sound \\(\\approx 344\\text{ m/s}\\))?",
  "reveration in large auditoriums and concert halls": "What causes reverberation in large auditoriums and concert halls?",
  "reverberation in large auditoriums and concert halls": "What causes reverberation in large auditoriums and concert halls?",
  "Ultrasonic sound (Ultrasound)": "What is ultrasonic sound (ultrasound), and what are its common applications?",
  "tetravalency and catenation capacity of carbon": "What is meant by the tetravalency and catenation capacity of carbon?",
  "crystalline allotropes of carbon": "Which of the following are the crystalline allotropes of carbon?",
  "structure and properties of Diamond": "Which statement accurately describes the structure and properties of diamond?",
  "structure and electrical conductivity of Graphite": "Why is graphite a good conductor of electricity?",
  "Washing soda (Sodium carbonate decahydrate)": "What is the chemical formula and common use of washing soda?",
  "Baking soda (Sodium hydrogen carbonate / Sodium bicarbonate)": "What is the chemical formula and common use of baking soda?",
  "Bleaching powder (Calcium oxychloride)": "What is the chemical formula and method of preparation of bleaching powder?",
  "Plaster of Paris (Calcium sulphate hemihydrate)": "What is the chemical formula and method of preparation of Plaster of Paris?",
  "Natural and artificial radioactivity discovery (Henri Becquerel, Marie Curie)": "What is radioactivity, as discovered by Henri Becquerel and Marie Curie?",
  "Food adulteration dyes and risks": "Which health risks are associated with synthetic food adulteration dyes such as metanil yellow and rhodamine B?",
  "Transpiration pull mechanism in tall trees": "How does the transpiration pull mechanism help transport water in tall trees?",
  "translocation of organic food nutrients in phloem tissue": "How does translocation of organic food nutrients occur in phloem tissue?",
  "excretion in human beings (Nephron functional unit of kidney)": "What are the main steps of urine formation in a nephron?",
  "Artificial kidney (Hemodialysis)": "What is the function of an artificial kidney (hemodialysis)?",
  "Plant growth inhibitor Abscisic Acid (ABA)": "What is the role of the plant growth inhibitor abscisic acid (ABA)?",
  "Human brain: Cerebellum function": "What is the primary function of the cerebellum in the human brain?",
  "chromosome morphology and centromere classification": "How are chromosomes classified based on the position of the centromere?",
  "DNA molecular architecture (Watson and Crick model 1953)": "Which statement accurately describes the Watson and Crick model of DNA structure (1953)?",
  "functional definition of a Gene": "What is a gene?",
  "three major types of cellular RNA": "What are the three major types of cellular RNA and their functions?",
  "Mendel's Dihybrid Cross phenotypic ratio in F2 generation": "What is the phenotypic ratio in the \\(F_2\\) generation of Mendel's dihybrid cross?",
  "Down syndrome (Trisomy 21)": "What causes Down syndrome (Trisomy 21)?",
  "Mendel's Law of Segregation (Purity of Gametes)": "What does Mendel's Law of Segregation (Purity of Gametes) state?",
  "Gregor Johann Mendel's Monohybrid Cross on garden pea (Pisum sativum)": "What are the \\(F_1\\) and \\(F_2\\) outcomes of Mendel's monohybrid cross between tall (\\(TT\\)) and dwarf (\\(tt\\)) pea plants?",
  "cellular totipotency in plant tissue culture (Gottlieb Haberlandt concept)": "What is cellular totipotency in plant tissue culture?",
  "micropropagation stages in plant tissue culture": "What is the correct sequence of stages in micropropagation?",
  "Genetically Modified Bt Cotton": "How is genetically modified Bt cotton protected against bollworm pests?",
  "Golden Rice bio-fortification": "Why was Golden Rice developed through genetic engineering?",
  "Bio-fertilizers: Azotobacter, Rhizobium, Anabaena, and Mycorrhizae": "How do bio-fertilizers such as Azotobacter, Rhizobium, Anabaena, and Mycorrhizae benefit crops?",
  "Pisciculture (Fish farming: Composite Fish Culture)": "What is the principle behind composite fish culture?",
  "different bands of the Electromagnetic (EM) spectrum": "Which statement correctly describes the bands of the electromagnetic spectrum?",
  "Refracting telescope (invented by Hans Lippershey, used by Galileo Galilei 1609)": "How does a refracting telescope form an image?",
  "Reflecting telescope (invented by Sir Isaac Newton)": "How does a Newtonian reflecting telescope collect and focus light?",
  "Cassegrain reflecting telescope optical design": "What is the optical design of a Cassegrain reflecting telescope?",
  "Chandra X-ray Observatory (launched 1999 by NASA)": "What type of radiation is the Chandra X-ray Observatory designed to detect?",
  "why major astronomical observatories are placed in high mountains or in outer space": "Why are major astronomical observatories placed on high mountains or in outer space?",
  "James Webb Space Telescope (JWST, launched 2021)": "What are the key features of the James Webb Space Telescope (JWST)?",
  "Hubble Space Telescope (HST, launched 1990 by NASA/ESA)": "What are the key features of the Hubble Space Telescope (HST)?",
  "Giant Metrewave Radio Telescope (GMRT) at Narayangaon near Pune, India": "What is the Giant Metrewave Radio Telescope (GMRT) near Pune?",
  "the angle between applied force and displacement is 0 degrees (same direction)": "What is the work done when the angle between the applied force and displacement is \\(0^\\circ\\)?",
  "the angle between applied force and displacement is 90 degrees (perpendicular)": "What is the work done when the angle between the applied force and displacement is \\(90^\\circ\\)?",
  "the angle between applied force and displacement is 180 degrees (opposite, e.g. friction)": "What is the work done when the angle between the applied force and displacement is \\(180^\\circ\\)?",
  "converting 1 Joule into Ergs": "What is the value of \\(1\\text{ Joule}\\) in ergs?",
  "total mechanical energy of a freely falling body at any point in its trajectory": "What happens to the total mechanical energy of a freely falling body at any point in its trajectory?",
  "commercial unit of electrical energy (1 kilowatt-hour / 1 unit)": "What is \\(1\\text{ kilowatt-hour (kWh)}\\) equal to in Joules?",
  "kinetic energy of an object of mass m moving with velocity v": "What is the formula for the kinetic energy of an object of mass \\(m\\) moving with velocity \\(v\\)?",
  "potential energy of an object of mass m raised to height h": "What is the formula for the gravitational potential energy of an object of mass \\(m\\) raised to height \\(h\\)?",
  "rate of doing work (Power P = W / t)": "What is the SI unit of power (rate of doing work)?",
  "1 Horsepower (hp) in electrical units": "How many Watts are equal to \\(1\\text{ Horsepower (hp)}\\)?",
  "electric current I passing through a cross-section carrying charge Q in time t": "Which formula relates electric current \\(I\\), charge \\(Q\\), and time \\(t\\)?",
  "electric potential difference V between two points when work W is done moving charge Q": "Which formula defines electric potential difference \\(V\\) in terms of work \\(W\\) and charge \\(Q\\)?",
  "Ohm's Law for a metallic conductor at constant temperature": "What does Ohm's Law state for a metallic conductor at constant temperature?",
  "equivalent resistance Rs of resistors R1, R2, R3 connected in series": "What is the equivalent resistance \\(R_s\\) of resistors \\(R_1, R_2, R_3\\) connected in series?",
  "equivalent resistance Rp of resistors connected in parallel": "What is the equivalent resistance \\(R_p\\) of resistors \\(R_1, R_2, R_3\\) connected in parallel?",
  "resistivity (specific resistance ρ) of a conductor": "What is the formula and SI unit for the resistivity (\\(\\rho\\)) of a conductor?",
  "standard color coding of domestic electric cables in India": "What is the standard color coding for live, neutral, and earth wires in domestic electric cables in India?",
  "function of an electric fuse wire or Miniature Circuit Breaker (MCB)": "What is the function of an electric fuse wire or Miniature Circuit Breaker (MCB)?",
  "substance having very high resistance and used as heating elements in toasters and irons": "Which alloy has high resistance and is used for heating elements in electric toasters and irons?",
  "I-V characteristic of an ohmic conductor": "What is the shape of the \\(I\\text{-}V\\) graph for an ohmic conductor?",
  "Law of Conservation of Mass (formulated by Antoine Lavoisier in 1789)": "What does the Law of Conservation of Mass (formulated by Antoine Lavoisier in 1789) state?",
  "modern unified atomic mass unit (Dalton / u)": "How is the modern unified atomic mass unit (Dalton / u) defined?",
  "Avogadro's number (NA)": "What is the value of Avogadro's number (\\(N_A\\))?",
  "definition of an acidic radical (anion)": "Which of the following correctly defines an acidic radical (anion)?",
  "molecular mass of water (H2O)": "What is the molecular mass of water (\\(\\text{H}_2\\text{O}\\))?",
  "Law of Constant Proportion (formulated by Joseph Proust in 1799)": "What does the Law of Constant Proportion (formulated by Joseph Proust in 1799) state?",
  "number of moles n of a substance of mass m (in grams) and molar mass M": "Which formula gives the number of moles \\(n\\) of a substance of mass \\(m\\) (in grams) and molar mass \\(M\\)?",
  "definition of a basic radical (cation)": "Which of the following correctly defines a basic radical (cation)?",
  "writing chemical formula using the criss-cross valency method for Aluminium oxide": "How is the chemical formula of aluminium oxide determined using the criss-cross valency method?",
  "measuring atomic radius in nanometres": "What is \\(1\\text{ nanometre (nm)}\\) equal to in metres?",
  "the pH scale (devised by Soren Sorensen in 1909)": "How are acidic, neutral, and basic solutions classified on the pH scale?",
  "reaction of an acid with a base (Neutralisation reaction)": "What are the products of a neutralisation reaction between an acid and a base?",
  "color of blue litmus paper when exposed to an acidic solution": "What color change occurs when blue litmus paper is dipped into an acidic solution?",
  "color of phenolphthalein indicator in basic solution": "What color does phenolphthalein indicator turn in a basic solution?",
  "reaction of active metals (Zn, Mg, Fe) with dilute acids": "What is produced when active metals such as Zn, Mg, or Fe react with dilute acids?",
  "water of crystallisation in Blue vitriol (Copper sulphate)": "What is the chemical formula of blue vitriol (hydrated copper sulphate), and how many molecules of water of crystallisation does it contain?",
  "reaction of acids with metal carbonates and bicarbonates": "Which gas is released when an acid reacts with a metal carbonate or bicarbonate?",
  "Arrhenius definition of an acid": "According to the Arrhenius theory, what is an acid?",
  "Arrhenius definition of a base": "According to the Arrhenius theory, what is a base?",
  "water of crystallisation in Washing soda": "How many molecules of water of crystallisation are present in washing soda?",
  "Thallophyta (Algae like Spirogyra, Ulva, Chara)": "Which characteristics define plants belonging to division Thallophyta?",
  "Bryophyta (Amphibians of the plant kingdom like Moss / Funaria, Riccia, Marchantia)": "Why are Bryophytes called the amphibians of the plant kingdom, and what are their key features?",
  "Pteridophyta (Ferns like Nephrolepis, Marsilea, Pteris)": "Which characteristics define plants belonging to division Pteridophyta?",
  "Gymnosperms (e.g. Cycas, Pinus / Deodar)": "Which characteristics define Gymnosperms?",
  "Dicotyledonous plants (Dicots e.g. Pea, Mustard, Sunflower, Mango)": "Which characteristics define dicotyledonous plants (dicots)?",
  "Cryptogams (Eichler's sub-kingdom of non-seed plants)": "What are Cryptogams?",
  "Monocotyledonous plants (Monocots e.g. Maize, Wheat, Grass, Bamboo)": "Which characteristics define monocotyledonous plants (monocots)?",
  "Rhizoids in Bryophytes": "What is the function of rhizoids in Bryophytes?",
  "unidirectional flow of energy in an ecosystem": "Why is the flow of energy in an ecosystem unidirectional?",
  "Lindeman's 10% law of energy transfer across trophic levels": "What does Lindeman's 10% law state about energy transfer across trophic levels?",
  "producers (Autotrophs) in an ecosystem": "What is the role of producers (autotrophs) in an ecosystem?",
  "primary consumers (Herbivores)": "Which organisms are classified as primary consumers in an ecosystem?",
  "biogeochemical cycling of nutrients (gaseous vs sedimentary cycles)": "How do biogeochemical cycles maintain nutrient balance in an ecosystem?",
  "Lactobacillus bacteria in milk": "How do Lactobacillus bacteria convert milk into yoghurt?",
  "Rhizobium symbiotic bacteria": "What is the role of symbiotic Rhizobium bacteria in leguminous plants?",
  "Yeast (Saccharomyces cerevisiae) fermentation": "What are the products of sugar fermentation by yeast (Saccharomyces cerevisiae)?",
  "Penicillin antibiotic discovery (Alexander Fleming in 1928)": "From which organism was the antibiotic penicillin discovered by Alexander Fleming in 1928?",
  "narrow-spectrum antibiotics (e.g. penicillin G, erythromycin)": "What are narrow-spectrum antibiotics?",
  "Vaccines (invented by Edward Jenner using cowpox against smallpox)": "How do vaccines protect the body against infectious diseases?",
  "bio-fungicides and bio-pesticides using Trichoderma and Bacillus thuringiensis": "How are Trichoderma and Bacillus thuringiensis used in agriculture?",
  "Clostridium bacteria (e.g. Clostridium botulinum, Clostridium tetani)": "Which diseases or toxins are associated with anaerobic Clostridium bacteria?"
};

const MH9_KINEMATICS_MAP = [
  {
    match: /a body is in uniform circular motion\?/i,
    text: "Which statement correctly describes the motion of a body in uniform circular motion?"
  },
  {
    match: /the area under a velocity-time graph is calculated for a given time interval\?/i,
    text: "What physical quantity is represented by the area under a velocity-time graph for a given time interval?"
  },
  {
    match: /a car travels the first half of a journey with speed v1 and second half with speed v2\?/i,
    text: "A car travels the first half of a journey with speed \\(v_1\\) and the second half with speed \\(v_2\\). What is its average speed?"
  }
];

function capitalizeFirst(str) {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function cleanGeneralQuestionText(text) {
  let t = String(text || '').trim();

  // Fix corrupted LaTeX in CBSE-9-MGM-9-9.3.2-OSC-120
  t = t.replace(/\\sqrtProven theorem standard/g, '\\(\\sqrt{2}\\)');

  // Check MH9 kinematics 3-variant template
  if (/^In the study of .+, what is the correct physical relationship when /i.test(t)) {
    for (const item of MH9_KINEMATICS_MAP) {
      if (item.match.test(t)) return item.text;
    }
  }

  // Remove unnecessary board / textbook / study prefixes
  const prefixPatterns = [
    /^In Balbharti Class 10 Science Part [12],\s*/i,
    /^In Balbharti Class 10,\s*/i,
    /^In the Balbharti textbook(?:\s+activity(?:\s+for)?)?,\s*/i,
    /^In the Balbharti textbook experiment,\s*/i,
    /^According to the Balbharti Class 10(?:th)?(?: textbook)?,\s*/i,
    /^According to the Maharashtra State Board(?: curriculum| textbook)?,\s*/i,
    /^In Maharashtra State Board geometry,\s*/i,
    /^In CBSE Class 9 Ganita Manjari Chapter \d+:\s*/i,
    /^In CBSE Class 9 grading criteria:\s*/i,
    /^In CBSE Class 9 comparative statistics:\s*/i,
    /^In CBSE Class \d+ (?:mathematics )?examinations,\s*/i,
    /^Determine the accurate examination protocol:\s*/i,
    /^Follow the standard flowchart guidelines:\s*/i,
    /^Synthesize the principles of converses:\s*/i,
    /^Select the accurate mathematical fact:\s*/i,
    /^Choose the mathematically correct answer:\s*/i,
    /^Why does the Balbharti Class 10\s+/i,
    /^Why did the Balbharti Class 10\s+/i,
    /^In the study of [^,.:]+,\s*/i,
  ];

  // Handle "Why does the Balbharti Class 10 ..." -> "Why does ..."
  if (/^Why (does|did) the Balbharti Class 10\s+/i.test(t)) {
    t = t.replace(/^Why (does|did) the Balbharti Class 10\s+/i, 'Why $1 the ');
  } else {
    for (const p of prefixPatterns) {
      if (p.test(t)) {
        t = t.replace(p, '');
        break;
      }
    }
  }

  // Handle "In the Balbharti diagram of ..." -> "In the diagram of ..."
  t = t.replace(/\bIn the Balbharti diagram of\b/gi, 'In the diagram of');
  t = t.replace(/\bIn the standard Balbharti DC motor diagram\b/gi, 'In a standard DC motor diagram');
  t = t.replace(/\bIn the Balbharti textbook activity for\b/gi, 'In the activity for');
  t = t.replace(/\bIn Balbharti Class 10\b/gi, '');
  t = t.replace(/\bBalbharti Class 10\b/gi, '');
  t = t.replace(/\bBalbharti\b\s*/gi, '');

  // Strip trailing / inline board & fluff phrases
  t = t.replace(/\bIn CBSE Class \d+ (?:mathematics )?examinations,\s*/gi, '');
  t = t.replace(/\s+in CBSE Class \d+ Science\?/gi, '?');
  t = t.replace(/\s+in CBSE Class \d+ mathematics\?/gi, '?');
  t = t.replace(/\s+in CBSE Class \d+ mathematics examinations,\s*/gi, ' ');
  t = t.replace(/\s+In CBSE Class \d+ examinations,\s*/gi, ' ');
  t = t.replace(/\s+for full marks in CBSE exams\?/gi, '?');
  t = t.replace(/\s+in Balbharti mathematics\?/gi, '?');
  t = t.replace(/\s+in Maharashtra State Board geometry\?/gi, '?');
  t = t.replace(/\s+considered scientifically accurate in the Maharashtra Board curriculum/gi, ' correct');
  t = t.replace(/\s+scientifically accurate according to the Maharashtra Board curriculum/gi, ' correct');
  t = t.replace(/\s+as given in Balbharti Class 10\?/gi, '?');
  t = t.replace(/\s+in the study of spherical mirrors\?/gi, ' in spherical mirrors?');
  t = t.replace(/\s+in the study of cell discovery\?:/gi, ' in the discovery of the cell?');
  t = t.replace(/what is the most scientifically accurate response\?/gi, 'what is the correct explanation?');
  t = t.replace(/\bare scientifically accurate\b/gi, 'are correct');
  t = t.replace(/\bWhich demonstration is scientifically accurate\?/gi, 'Which demonstration is correct?');
  t = t.replace(/\bThe scientifically accurate classification is:/gi, 'The correct classification is:');
  t = t.replace(/\bwhich of the following is scientifically accurate\?:/gi, 'which of the following is correct?');
  t = t.replace(/\bscientifically accurate definition of\b/gi, 'correct definition of');
  t = t.replace(/\bIn the study of unicellular living microorganisms:\s*'([^']+)'\.\s*Identify the correct biological fact:/i, "Which statement about the unicellular microorganism '$1' is correct?");
  t = t.replace(/\bRegarding the tissue system:\s*'([^']+)',\s*which of the following is correct\?/i, "Which statement about '$1' is correct?");

  // Clean up double spaces, leading punctuation
  t = t.replace(/\s{2,}/g, ' ').replace(/^\s*[,;:\-]\s*/, '').trim();
  return capitalizeFirst(t);
}

function cleanGeneralSolution(sol) {
  if (!sol) return sol;
  let s = String(sol);
  s = s.replace(/\*\*Step 1: Understand the concepts of [^.]+\.\*\*\s*Recall the established principles of the Maharashtra State Board curriculum for this topic\.\s*/gi, '');
  s = s.replace(/\*\*Step 2: Evaluate the situation\.\*\*\s*For [^,]+,\s*the correct scientific outcome is:\s*/gi, '');
  s = s.replace(/\n?\*\*Step 3: Conclusion\.\*\*\s*Therefore,\s*.+?\s*is the correct option\.?/gi, '');
  s = s.replace(/In Maharashtra State Board geometry,\s*/gi, '');
  s = s.replace(/Is AAA listed as a valid congruence criterion in Maharashtra State Board geometry\?\s*/gi, '');
  s = s.replace(/in Balbharti mathematics/gi, '');
  s = s.replace(/according to the Maharashtra (?:State )?Board curriculum/gi, '');
  return s.trim();
}

async function run() {
  const docs = JSON.parse(fs.readFileSync(SCAN_PATH, 'utf8'));
  console.log(`Loaded ${docs.length} matched questions from scan (${DRY_RUN ? 'DRY RUN' : 'LIVE'})`);

  const updates = [];
  let caseACount = 0;
  let caseBCount = 0;
  let caseCCount = 0;
  const unmappedConcepts = new Set();

  for (const q of docs) {
    const origText = String(q.text || '');
    const origSol = String(q.solution || q.explanation || '');

    const step2Match = origSol.match(/For\s+(.+?),\s+the correct scientific outcome is:\s*(.+?)(?:\n|\*\*Step 3|$)/i);
    let newText = origText;
    let newSol = origSol;

    if (step2Match) {
      const concept = step2Match[1].trim();
      const outcome = step2Match[2].trim().replace(/\.$/, '');
      if (CONCEPT_QUESTIONS[concept]) {
        newText = CONCEPT_QUESTIONS[concept];
        newSol = `**Concept:** ${capitalizeFirst(concept)}\n\n${capitalizeFirst(outcome)}.`;
        caseACount++;
      } else {
        unmappedConcepts.add(concept);
        newText = cleanGeneralQuestionText(origText);
        newSol = cleanGeneralSolution(origSol);
      }
    } else if (/^In the study of .+, what is the correct physical relationship when /i.test(origText)) {
      newText = cleanGeneralQuestionText(origText);
      newSol = cleanGeneralSolution(origSol);
      caseBCount++;
    } else {
      newText = cleanGeneralQuestionText(origText);
      newSol = cleanGeneralSolution(origSol);
      caseCCount++;
    }

    if (newText !== origText || newSol !== origSol) {
      const patch = {
        text: newText,
        updatedAt: new Date()
      };
      if (q.solution !== undefined) patch.solution = newSol;
      if (q.explanation !== undefined) patch.explanation = newSol;
      if (q.solution === undefined && q.explanation === undefined && newSol) patch.solution = newSol;
      updates.push({ id: q.id, origText, newText, origSol: origSol.slice(0, 80), newSol: newSol.slice(0, 80), patch });
    }
  }

  console.log(`Breakdown: Case A (Step2 concepts)=${caseACount}, Case B (MH9 kinematics)=${caseBCount}, Case C (general)=${caseCCount}`);
  console.log(`Unmapped concepts: ${unmappedConcepts.size}`, Array.from(unmappedConcepts));
  console.log(`Total documents to update: ${updates.length}`);

  if (DRY_RUN) {
    console.log('\nSample 10 updates:');
    for (const u of updates.slice(0, 10)) {
      console.log(`- [${u.id}]`);
      console.log(`  OLD: ${u.origText}`);
      console.log(`  NEW: ${u.newText}`);
      console.log(`  SOL: ${u.newSol}`);
    }
    console.log('\nSample Case C updates:');
    const caseCSamples = updates.filter(u => !u.origSol.includes('Recall the established principles')).slice(0, 10);
    for (const u of caseCSamples) {
      console.log(`- [${u.id}]`);
      console.log(`  OLD: ${u.origText}`);
      console.log(`  NEW: ${u.newText}`);
    }
    process.exit(0);
  }

  // Commit in batches of 400
  let committed = 0;
  for (let i = 0; i < updates.length; i += 400) {
    const chunk = updates.slice(i, i + 400);
    const batch = adminDb.batch();
    for (const u of chunk) {
      batch.update(adminDb.collection('questions').doc(u.id), u.patch);
    }
    await batch.commit();
    committed += chunk.length;
    console.log(`Committed ${committed}/${updates.length}...`);
  }

  console.log('Done! All badly worded questions updated.');
  process.exit(0);
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
