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

// Specific known qualitative chapter codes (e.g. MH-9-SCIT Chapter 6, 7, 8, 9, 10, 17)
const QUALITATIVE_CHAPTER_CODES = new Set([
  'MH-9-SCIT-6',   // Classification of Plants
  'MH-9-SCIT-7',   // Energy Flow in an Ecosystem
  'MH-9-SCIT-8',   // Useful and Harmful Microbes
  'MH-9-SCIT-9',   // Environmental Management
  'MH-9-SCIT-10',  // ICT: The New Direction of Progress
  'MH-9-SCIT-17',  // Introduction to Biotechnology
  'MH-8-SCI-1',    // Living World and Classification of Microbes
  'MH-8-SCI-2',    // Health and Diseases
  'MH-8-SCI-7',    // Metals and Nonmetals (descriptive)
  'MH-8-SCI-8',    // Pollution
  'MH-8-SCI-9',    // Disaster Management
  'MH-8-SCI-10',   // Cell and Cell Organelles
  'MH-8-SCI-17',   // Man-made Materials
  'MH-8-SCI-18',   // Ecosystems
  'CBSE-8-CURI-5', // Curiosity: Reproduction in Animals / Microorganisms
  'MH-10-SCIT2-7', // Introduction to Microbiology
  'MH-10-SCIT2-8'  // Cell Biology and Biotechnology
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
