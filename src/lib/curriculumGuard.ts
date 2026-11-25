/**
 * Curriculum Guard & Pedagogical Ceiling Engine (Classes 8–10)
 *
 * Enforces strict adherence to middle/secondary school curricula (NCERT & Balbharti).
 * Prevents:
 * 1. Invention of artificial numerical questions on purely qualitative/theoretical topics.
 * 2. Infiltration of university, engineering, GATE, or medical school concepts.
 */

// Chapters and topics that are strictly qualitative/theoretical with ZERO textbook calculations
const QUALITATIVE_TOPIC_PATTERNS = [
  /environment/i,
  /ecology/i,
  /ecosystem/i,
  /microbe/i,
  /bacteria/i,
  /fungi/i,
  /classification\s+of\s+plants/i,
  /living\s+world/i,
  /cell\s+and\s+cell\s+organelles/i,
  /disaster\s+management/i,
  /solid\s+waste/i,
  /weather\s+and\s+climate/i,
  /meteorology/i,
  /first\s+aid/i,
  /health\s+and\s+disease/i,
  /pollution/i,
  /biotechnology/i,
  /tissue\s+culture/i,
  /man-made\s+material/i,
  /useful\s+and\s+harmful/i
];

// Specific known qualitative chapter codes (no numerical objective questions)
const QUALITATIVE_CHAPTER_CODES = new Set([
  // CBSE Class 8 Curiosity
  'CBSE-8-CURI-1',  // Exploring the Investigative World of Science
  'CBSE-8-CURI-2',  // The Invisible Living World: Beyond Our Naked Eye
  'CBSE-8-CURI-3',  // Health: The Ultimate Treasure
  'CBSE-8-CURI-7',  // Particulate Nature of Matter
  'CBSE-8-CURI-8',  // Nature of Matter: Elements, Compounds, and Mixtures
  'CBSE-8-CURI-12', // How Nature Works in Harmony
  'CBSE-8-CURI-13', // Our Home: Earth, a Unique Life Sustaining Planet
  // CBSE Class 9 Science
  'CBSE-9-SCIE-1',  // Exploration: Entering the World of Secondary Science
  'CBSE-9-SCIE-2',  // Cell: The Building Block of Life
  'CBSE-9-SCIE-3',  // Tissues in Action
  'CBSE-9-SCIE-5',  // Exploring Mixtures and their Separation
  'CBSE-9-SCIE-11', // Reproduction: How Life Continues
  'CBSE-9-SCIE-12', // Patterns in Life: Diversity and Classification
  'CBSE-9-SCIE-13', // Earth as a System: Energy, Matter, and Life
  // CBSE Class 10 Science
  'CBSE-10-SCI-1',  // Chemical Reactions and Equations
  'CBSE-10-SCI-2',  // Acids, Bases and Salts
  'CBSE-10-SCI-3',  // Metals and Non-metals
  'CBSE-10-SCI-4',  // Carbon and its Compounds
  'CBSE-10-SCI-5',  // Life Processes
  'CBSE-10-SCI-6',  // Control and Coordination
  'CBSE-10-SCI-7',  // How do Organisms Reproduce?
  'CBSE-10-SCI-8',  // Heredity and Evolution
  'CBSE-10-SCI-13', // Our Environment
  // MH Class 8 General Science
  'MH-8-SCI-1',     // Living World and Classification of Microbes
  'MH-8-SCI-2',     // Health and Diseases
  'MH-8-SCI-7',     // Metals and Non-metals
  'MH-8-SCI-8',     // Pollution
  'MH-8-SCI-9',     // Disaster Management
  'MH-8-SCI-10',    // Cell and Cell Organelles
  'MH-8-SCI-11',    // Human Body and Organ System
  'MH-8-SCI-12',    // Introduction to Acid and Base
  'MH-8-SCI-17',    // Man-made Materials
  'MH-8-SCI-18',    // Ecosystems
  'MH-8-SCI-19',    // Life Cycle of Stars
  // MH Class 9 Science & Technology
  'MH-9-SCIT-5',    // Acids, Bases and Salts
  'MH-9-SCIT-6',    // Classification of Plants
  'MH-9-SCIT-7',    // Energy Flow in an Ecosystem
  'MH-9-SCIT-8',    // Useful and Harmful Microbes
  'MH-9-SCIT-9',    // Environmental Management
  'MH-9-SCIT-10',   // Information Communication Technology (ICT)
  'MH-9-SCIT-13',   // Carbon: An Important Element
  'MH-9-SCIT-14',   // Substances in Common Use
  'MH-9-SCIT-15',   // Life Processes in Living Organisms
  'MH-9-SCIT-16',   // Heredity and Variation
  'MH-9-SCIT-17',   // Introduction to Biotechnology
  // MH Class 10 Science & Technology Part - 1
  'MH-10-SCIT1-2',  // Periodic Classification of Elements
  'MH-10-SCIT1-3',  // Chemical Reactions and Equations
  'MH-10-SCIT1-8',  // Metallurgy
  'MH-10-SCIT1-9',  // Carbon Compounds
  // MH Class 10 Science & Technology Part - 2
  'MH-10-SCIT2-1',  // Heredity and Evolution
  'MH-10-SCIT2-2',  // Life Processes in Living Organisms Part - 1
  'MH-10-SCIT2-3',  // Life Processes in Living Organisms Part - 2
  'MH-10-SCIT2-4',  // Environmental Management
  'MH-10-SCIT2-5',  // Towards Green Energy
  'MH-10-SCIT2-6',  // Animal Classification
  'MH-10-SCIT2-7',  // Introduction to Microbiology
  'MH-10-SCIT2-8',  // Cell Biology and Biotechnology
  'MH-10-SCIT2-9',  // Social Health
  'MH-10-SCIT2-10'  // Disaster Management
]);

// Prohibited university, engineering, or medical degree level keywords
export const PROHIBITED_ADVANCED_KEYWORDS: { pattern: RegExp; label: string }[] = [
  // Higher Mathematics / Physics / Atmospheric Dynamics
  { pattern: /\bdifferential\s+equations?\b/i, label: 'Differential Equations' },
  { pattern: /\bnavier[- ]stokes\b/i, label: 'Navier-Stokes Equations' },
  { pattern: /\bhamiltonian\b/i, label: 'Hamiltonian Mechanics' },
  { pattern: /schr(?:o|ö|oe)dinger/i, label: 'Schrodinger Equation' },
  { pattern: /\blorentz\s+(?:force|factor|transformation)\b/i, label: 'Lorentz Transformations' },
  { pattern: /\brelativistic\s+(?:time\s+dilation|beaming|mass)\b/i, label: 'Relativistic Physics' },
  { pattern: /\bsynchrotron\b/i, label: 'Synchrotron Radiation' },
  { pattern: /\bschwarzschild\s+radius\b/i, label: 'Schwarzschild Metric' },
  { pattern: /\bbragg's\s+law\b/i, label: "Bragg's Law Crystallography" },
  { pattern: /\bcrystal\s+field\s+splitting\b/i, label: 'Crystal Field Theory' },
  { pattern: /\bgibbs\s+free\s+energy\b/i, label: 'Gibbs Free Energy Thermodynamics' },
  { pattern: /\blapse\s+rate\b/i, label: 'Atmospheric Lapse Rate Calculation' },
  { pattern: /\bpsychrometric\b/i, label: 'Psychrometric Thermodynamics' },
  { pattern: /\bactual\s+vapor\s+pressure.*saturation\b/i, label: 'Vapor Pressure Numericals' },

  // Engineering & Advanced Industrial Processes
  { pattern: /\bphytoremediation\b/i, label: 'Phytoremediation / Hyperaccumulation' },
  { pattern: /\bhyperaccumulat/i, label: 'Hyperaccumulating Plants' },
  { pattern: /\bfluidized\s+bed\s+incinerator\b/i, label: 'Fluidized Bed Combustion' },
  { pattern: /\bactivated\s+carbon\s+injection.*dioxin\b/i, label: 'Dioxin Flue Gas Scrubbing' },
  { pattern: /\bbaghouse\s+filters?\b/i, label: 'Baghouse Fabric Filters' },
  { pattern: /\bhigh-pressure\s+reverse\s+osmosis.*leachate\b/i, label: 'Industrial Leachate RO' },
  { pattern: /\blandfill\s+gas.*collection\s+well\b/i, label: 'Landfill Gas Extraction Math' },
  { pattern: /\banaerobic\s+digestion.*hydrolytic\b/i, label: 'Hydrolytic Acidogenesis Biochemistry' },
  { pattern: /\bmethanogenic\s+archaea\b/i, label: 'Methanogenic Archaea Kinetics' },
  { pattern: /\bhdpe\s+geomembrane\b/i, label: 'HDPE Geomembrane Engineering' },

  // Supercomputing / HPC Benchmarking
  { pattern: /\bgigaflops\s+are\s+in\b/i, label: 'GigaFLOPS Conversion Math' },
  { pattern: /\bteraflops\s+are\b/i, label: 'TeraFLOPS Conversion Math' },
  { pattern: /\btop500\s+ai\b/i, label: 'Top500 AI Supercomputing' },
  { pattern: /\bnational\s+supercomputing\s+mission\b/i, label: 'National Supercomputing Mission' },

  // Advanced Physiology & Molecular Biology
  { pattern: /\bglomerular\s+filtration\s+rate\b/i, label: 'GFR Ultrafiltration Math' },
  { pattern: /\bfiltration\s+fraction\b/i, label: 'Renal Filtration Fraction' },
  { pattern: /\bpodocyte\s+filtration\s+slits\b/i, label: 'Podocyte Slit Diaphragms' },
  { pattern: /\bactive\s+symport\b/i, label: 'Active Symport Carrier Transport' },
  { pattern: /\bpotometer\s+transpires\b/i, label: 'Potometer Transpiration Rate Math' },
  { pattern: /\bhydrostatic\s+tension.*eucalyptus\b/i, label: 'Xylem Tension Physics Math' },
  { pattern: /\bmyelinated\s+axon.*speed\b/i, label: 'Nerve Conduction Velocity Math' },
  { pattern: /\bdomestic\s+dog\s*\(2n\s*=\s*78\)/i, label: 'Canine Cytogenetics' },
  { pattern: /\btopoisomerase\b/i, label: 'Topoisomerase / DNA Gyrase' },
  { pattern: /\bdna\s+gyrase\b/i, label: 'DNA Gyrase' },
  { pattern: /\bpalindromic\s+restriction\b/i, label: 'Palindromic Restriction Endonucleases' },
  { pattern: /\bsomatostatin\b/i, label: 'Recombinant Somatostatin' },
  { pattern: /\bwestern\s+blot\b/i, label: 'Western Blotting' },
  { pattern: /\bsouthern\s+blot\b/i, label: 'Southern Blotting' },
  { pattern: /\bagarose\s+gel\s+electrophoresis\b/i, label: 'Gel Electrophoresis' },
  { pattern: /\btaq\s+polymerase\b/i, label: 'Taq Polymerase PCR' }
];

/**
 * Checks if a given topic is purely qualitative and should never contain numerical (ONE) questions.
 */
export function isTopicPurelyQualitative(topicCode?: string, chapterName?: string, subjectName?: string): boolean {
  if (!topicCode && !chapterName) return false;

  const tCode = String(topicCode || '').trim();

  // Check prefix match against known qualitative chapter codes
  for (const prefix of QUALITATIVE_CHAPTER_CODES) {
    if (tCode === prefix || tCode.startsWith(`${prefix}-`) || tCode.startsWith(`${prefix}.`)) {
      return true;
    }
  }

  // Check topic text or chapter name
  const combined = `${tCode} ${chapterName || ''} ${subjectName || ''}`.toLowerCase();
  for (const pat of QUALITATIVE_TOPIC_PATTERNS) {
    if (pat.test(combined)) {
      return true;
    }
  }

  return false;
}

/**
 * Validates a single question against curriculum and pedagogical ceiling invariants.
 * Returns an array of error messages (empty if question is 100% compliant).
 */
export function validateQuestionCurriculum(q: any): { valid: boolean; errors: string[] } {
  const errors: string[] = [];
  if (!q) return { valid: true, errors };

  const type = String(q.type || '').toUpperCase();
  const topicCode = String(q.topicCode || '');
  const chapterName = String(q.chapterName || q.chapterTitle || '');
  const subjectName = String(q.subject || q.subjectName || '');

  // 1. Numerical Disqualification Guard
  if (type === 'ONE') {
    if (isTopicPurelyQualitative(topicCode, chapterName, subjectName)) {
      errors.push(
        `[CURRICULUM GUARD] Numerical question (ONE) rejected: Topic '${topicCode}' is purely qualitative/theoretical. ` +
        `Artificial calculations, fake flow rates, or synthetic arithmetic are strictly forbidden on this topic.`
      );
    }
  }

  // 2. School-Level Ceiling Barrier (Classes 8–10)
  const fullText = `${q.text || ''} ${q.solution || ''} ${q.explanation || ''} ${Array.isArray(q.options) ? q.options.map((o: any) => typeof o === 'object' ? (o.text || '') : String(o)).join(' ') : ''}`;

  for (const { pattern, label } of PROHIBITED_ADVANCED_KEYWORDS) {
    if (pattern.test(fullText)) {
      errors.push(
        `[CURRICULUM GUARD] Out-of-syllabus concept rejected: Contains prohibited advanced/university term '${label}'. ` +
        `Questions must remain strictly within the prescribed Class 8–10 school textbook curriculum.`
      );
      break; // Report the primary violation
    }
  }

  return {
    valid: errors.length === 0,
    errors
  };
}
