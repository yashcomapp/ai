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

const { createPreMutationSnapshot } = require('../scripts/pre-mutation-snapshot.js');

const REPLACEMENTS = {
  // 1. MH-10-SCIT1-10-10.3.2-OSC-009 (Relativity -> GPS in MEO)
  'MH-10-SCIT1-10-10.3.2-OSC-009': {
    text: "Which famous satellite navigation constellation operates in Medium Earth Orbits (MEO) at an altitude of approximately \\(20,200\\text{ km}\\) to provide positioning data across the globe?",
    options: [
      "Global Positioning System (GPS)",
      "Hubble Space Telescope",
      "International Space Station (ISS)",
      "INSAT Weather Satellite"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Medium Earth Orbits (altitude 2,000 km to 35,786 km) are primarily used by navigation satellite constellations such as the GPS network operating at approximately 20,200 km."
  },

  // 2. MH-10-SCIT1-10-10.2.5-OSC-002 (Replace Lagrangian distractor)
  'MH-10-SCIT1-10-10.2.5-OSC-002': {
    options: [
      "Geostationary Earth Orbit (GEO)",
      "Highly Elliptical Orbit (HEO)",
      "Sun-synchronous Polar Orbit (SSO)",
      "Equatorial Low Earth Orbit"
    ],
    solution: "Sun-synchronous polar orbits allow remote sensing satellites to pass over any given point on Earth at roughly the same local solar time, ensuring uniform illumination for imaging."
  },

  // 3. MH-10-SCIT1-10-10.2.6-OSC-002 (Replace Lagrangian distractor)
  'MH-10-SCIT1-10-10.2.6-OSC-002': {
    options: [
      "Low Earth Orbit (LEO) / Sun-synchronous Polar Orbit",
      "High Earth Orbit (HEO)",
      "Equatorial Geosynchronous Orbit",
      "Geostationary Earth Orbit (GEO)"
    ],
    solution: "Surveillance satellites operate in low polar orbits to maintain close proximity to the Earth's surface, enabling high-resolution imaging."
  },

  // 4. MH-10-SCIT1-10-10.3.3-OSC-006 (Replace Lagrangian distractor)
  'MH-10-SCIT1-10-10.3.3-OSC-006': {
    options: [
      "High Elliptical Orbit",
      "Geostationary Equatorial Orbit",
      "Sun-synchronous Polar Orbit",
      "Low Inclination Equatorial Orbit"
    ],
    solution: "Polar and sun-synchronous orbits pass over the polar regions, allowing remote sensing satellites to image stripe-by-stripe as the Earth rotates beneath them."
  },

  // 5. MH-9-SCIT-13-13.2-OTF-037 (Gibbs Free Energy -> Diamond Non-Conductor)
  'MH-9-SCIT-13-13.2-OTF-037': {
    text: "State whether the following statement is True or False: Diamond is a good conductor of electricity due to the presence of free electrons.",
    options: ["True", "False"],
    correctAnswer: "B",
    correctAnswers: ["B"],
    solution: "False. In diamond, each carbon atom is bonded to four neighboring carbon atoms by covalent bonds, leaving no free electrons; hence diamond is a bad conductor of electricity."
  },

  // 6. MH-9-SCIT-14-14.1-OSC-072 (Ligand field splitting -> Blue vitriol formula)
  'MH-9-SCIT-14-14.1-OSC-072': {
    text: "What is the chemical formula of blue vitriol (copper sulphate crystals) containing water of crystallization?",
    options: [
      "\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)",
      "\\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)",
      "\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)",
      "\\(\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Blue vitriol is copper sulphate pentahydrate with formula \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\). When heated, it loses its water of crystallization and turns into white anhydrous powder."
  },

  // 7. MH-9-SCIT-14-14.3-OAR-030 (Lorentz force in solution -> Class 9 explanation)
  'MH-9-SCIT-14-14.3-OAR-030': {
    solution: "Assertion and Reason are both true, and Reason is the correct explanation. Gamma rays consist of neutral electromagnetic radiation without electric charge; hence they do not experience deflection in magnetic or electric fields."
  },

  // 8. MH-9-SCIT-14-14.3-OSC-009 (Lorentz force in solution -> Class 9 explanation)
  'MH-9-SCIT-14-14.3-OSC-009': {
    solution: "Gamma (\\(\\gamma\\)) radiation consists of electromagnetic radiation that carries zero electric charge; therefore, it travels straight without any deflection through electric or magnetic fields."
  },

  // 9. MH-9-SCIT-14-14.3-OSC-076 (Lorentz force in solution -> Class 9 explanation)
  'MH-9-SCIT-14-14.3-OSC-076': {
    solution: "Alpha particles (positive charge) deflect toward the negative plate, beta particles (negative charge) deflect toward the positive plate, and neutral gamma rays pass straight through without deflection."
  },

  // 10. MH-9-SCIT-18-18.1-OSC-028 (Swift/Fermi GRBs -> Chandra X-ray Observatory)
  'MH-9-SCIT-18-18.1-OSC-028': {
    text: "Which space observatory was launched into orbit by NASA in 1999 specifically to detect X-rays from celestial sources?",
    options: [
      "Chandra X-ray Observatory",
      "Hubble Space Telescope",
      "James Webb Space Telescope",
      "Galileo Spacecraft"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "According to Maharashtra Board Class 9 Science textbook, Chandra X-ray Observatory was launched by NASA in 1999 to detect cosmic X-rays, named after Indian astrophysicist Subrahmanyan Chandrasekhar."
  },

  // 11. MH-9-SCIT-18-18.1-OSC-038 (Bragg's law -> Atmospheric absorption of X-rays)
  'MH-9-SCIT-18-18.1-OSC-038': {
    text: "Why can X-ray telescopes not be placed and operated on the Earth's surface?",
    options: [
      "X-rays emitted by celestial bodies are absorbed by the Earth's atmosphere",
      "X-rays travel significantly slower in the Earth's atmosphere",
      "X-rays are totally reflected by ground dust particles",
      "X-rays interfere with commercial radio broadcasts on Earth"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "The Earth's atmosphere absorbs cosmic X-rays, preventing them from reaching ground-based observatories. Therefore, X-ray telescopes must be placed in orbit outside the atmosphere."
  },

  // 12. MH-9-SCIT-18-18.1-OSC-051 (Doppler redshift -> Visible light wavelength)
  'MH-9-SCIT-18-18.1-OSC-051': {
    text: "What is the approximate wavelength range of visible light that human eyes are sensitive to?",
    options: [
      "\\(400\\text{ nm to } 800\\text{ nm}\\)",
      "\\(10\\text{ nm to } 100\\text{ nm}\\)",
      "\\(1\\text{ mm to } 1\\text{ m}\\)",
      "\\(800\\text{ nm to } 10000\\text{ nm}\\)"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "According to the Class 9 textbook, visible light radiation has wavelengths between approximately \\(400\\text{ nm}\\) (violet) and \\(800\\text{ nm}\\) (red)."
  },

  // 13. MH-9-SCIT-18-18.1-OSC-059 (Relativistic cosmic rays -> Astrosat satellite)
  'MH-9-SCIT-18-18.1-OSC-059': {
    text: "Which dedicated multi-wavelength space observatory was launched into space by ISRO in the year 2015?",
    options: [
      "Astrosat",
      "Aditya-L1",
      "Mangalyaan",
      "Chandrayaan-1"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "In 2015, the Indian Space Research Organisation (ISRO) launched Astrosat, India's first dedicated multi-wavelength space observatory."
  },

  // 14. MH-9-SCIT-18-18.3-OSC-014 (Pulsars relativistic magnetosphere -> GMRT location)
  'MH-9-SCIT-18-18.3-OSC-014': {
    text: "Near which town in Maharashtra is the Giant Metrewave Radio Telescope (GMRT) located?",
    options: [
      "Narayangaon near Pune",
      "Mahabaleshwar",
      "Nagpur",
      "Aurangabad"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "The Giant Metrewave Radio Telescope (GMRT) is established at Narayangaon near Pune, Maharashtra, by the National Centre for Radio Astrophysics (NCRA)."
  },

  // 15. MH-9-SCIT-18-18.3-OSC-022 (Radio lobes relativistic jets -> GMRT dishes count)
  'MH-9-SCIT-18-18.3-OSC-022': {
    text: "How many parabolic dish antennas make up the Giant Metrewave Radio Telescope (GMRT) array?",
    options: [
      "30 dish antennas",
      "12 dish antennas",
      "50 dish antennas",
      "64 dish antennas"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "GMRT consists of an array of 30 parabolic dish antennas, each having a diameter of 45 metres, distributed over an area of about 25 km."
  },

  // 16. MH-9-SCIT-18-18.3-OSC-023 (Synchrotron radiation -> Radio telescope dish)
  'MH-9-SCIT-18-18.3-OSC-023': {
    text: "What type of reflector surface is used in a radio telescope to collect and focus cosmic radio waves to a receiver?",
    options: [
      "A large parabolic metal dish",
      "A flat glass mirror",
      "A convex glass lens",
      "A triangular quartz prism"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Radio telescopes use large parabolic dishes made of metal mesh to reflect and gather radio waves at a focal receiver, similar to how concave mirrors focus light."
  },

  // 17. MH-9-SCIT-18-18.3-OSC-059 (Solar radio bursts Type II/IV -> GMRT operating institute)
  'MH-9-SCIT-18-18.3-OSC-059': {
    text: "Which research institute operates and maintains the Giant Metrewave Radio Telescope (GMRT)?",
    options: [
      "National Centre for Radio Astrophysics (NCRA-TIFR)",
      "Bhabha Atomic Research Centre (BARC)",
      "Indian Space Research Organisation (ISRO)",
      "Council of Scientific and Industrial Research (CSIR)"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "GMRT is operated by the National Centre for Radio Astrophysics (NCRA), which is a premier research centre of the Tata Institute of Fundamental Research (TIFR)."
  },

  // 18. MH-9-SCIT-18-18.3-OSC-076 (Relativistic pulsar -> GMRT dish diameter)
  'MH-9-SCIT-18-18.3-OSC-076': {
    text: "What is the diameter of each parabolic dish antenna in the Giant Metrewave Radio Telescope (GMRT) array?",
    options: [
      "\\(45\\text{ metres}\\)",
      "\\(25\\text{ metres}\\)",
      "\\(100\\text{ metres}\\)",
      "\\(10\\text{ metres}\\)"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Each of the 30 parabolic dish antennas of GMRT has a diameter of 45 metres, providing a massive collective collecting area."
  },

  // 19. MH-9-SCIT-18-18.3-OSC-081 (Relativistic jets -> Cassegrain telescope secondary mirror)
  'MH-9-SCIT-18-18.3-OSC-081': {
    text: "In a Cassegrain reflecting telescope, what type of secondary mirror is used to direct light through a hole in the primary mirror?",
    options: [
      "Convex mirror",
      "Concave mirror",
      "Plane mirror",
      "Cylindrical mirror"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "In a Cassegrain telescope, light reflected from the primary concave mirror is intercepted by a small convex secondary mirror, which reflects it back through a central hole in the primary concave mirror to the eyepiece."
  },

  // 20. MH-9-SCIT-18-18.4-OSC-027 (Aditya-L1 Lagrange mechanics -> Hubble Space Telescope)
  'MH-9-SCIT-18-18.4-OSC-027': {
    text: "In which year was the optical Hubble Space Telescope launched into Earth orbit by NASA?",
    options: [
      "1990",
      "1980",
      "2000",
      "2015"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "NASA launched the optical Hubble Space Telescope into Low Earth Orbit in 1990 at an altitude of approximately 589 km."
  },

  // 21. MH-9-SCIT-18-18.4-OSC-028 (Aditya-L1 Lagrange mechanics -> Telescopes in space advantage)
  'MH-9-SCIT-18-18.4-OSC-028': {
    text: "What is the major scientific advantage of placing telescopes in space rather than on the ground?",
    options: [
      "Observations are free from atmospheric absorption, light pollution, and weather turbulence",
      "Space telescopes travel closer to the stars, making them appear significantly larger",
      "Lenses in space can focus light without needing any mirrors",
      "Gravitational forces are completely absent in space"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Space telescopes overcome the problems caused by Earth's atmosphere, which absorbs certain radiations (X-rays, gamma rays) and causes optical distortion due to changing temperature and atmospheric density."
  },

  // 22. MH-9-SCIT-4-4.2-OSC-512 (Lorentz force -> Water molecular mass)
  'MH-9-SCIT-4-4.2-OSC-512': {
    text: "What is the molecular mass of water (\\(\\text{H}_2\\text{O}\\)) in unified atomic mass units (\\(\\text{u}\\))?",
    options: [
      "\\(18\\text{ u}\\)",
      "\\(16\\text{ u}\\)",
      "\\(20\\text{ u}\\)",
      "\\(2\\text{ u}\\)"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "\\(\\text{Molecular mass of } \\text{H}_2\\text{O} = (2 \\times 1) + (1 \\times 16) = 18\\text{ u}\\)."
  },

  // 23. MH-9-SCIT-5-5.4-OSC-502 (Crystal field splitting -> Hydrated copper sulphate color)
  'MH-9-SCIT-5-5.4-OSC-502': {
    text: "What is the characteristic color of hydrated copper sulphate crystals (\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\))?",
    options: [
      "Blue",
      "White",
      "Green",
      "Yellow"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Hydrated copper sulphate is blue due to its water of crystallization. When heated strongly, the water is driven off and it turns into a white anhydrous powder."
  },

  // 24. MH-9-SCIT-13-13.4-OTF-027 (Electrophilic addition of alkynes -> Saturated hydrocarbons definition)
  'MH-9-SCIT-13-13.4-OTF-027': {
    text: "State whether the following statement is True or False: Saturated hydrocarbons contain only single covalent bonds between carbon atoms.",
    options: ["True", "False"],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "True. Hydrocarbons in which all carbon atoms are joined exclusively by single covalent bonds are called saturated hydrocarbons (alkanes)."
  },

  // 25. MH-9-SCIT-16-16.2-OSC-045 (Retrovirus cDNA reverse transcriptase -> mRNA function)
  'MH-9-SCIT-16-16.2-OSC-045': {
    text: "Which type of RNA carries the genetic message from the cell nucleus to the ribosomes for protein synthesis?",
    options: [
      "mRNA (Messenger RNA)",
      "rRNA (Ribosomal RNA)",
      "tRNA (Transfer RNA)",
      "snRNA"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "According to Maharashtra Board Class 9 textbook, mRNA carries genetic information from the DNA in the cell nucleus to ribosomes for protein synthesis."
  },

  // 26. MH-9-SCIT-16-16.2-OSC-064 (Topoisomerase supercoiling -> Centromere definition)
  'MH-9-SCIT-16-16.2-OSC-064': {
    text: "What is the primary constriction region on a chromosome where sister chromatids are held together called?",
    options: [
      "Centromere",
      "Telomere",
      "Centrosome",
      "Chromatid"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Every chromosome has a primary constriction called the centromere, which holds the sister chromatids together and divides the chromosome into two arms."
  },

  // 27. MH-9-SCIT-17-17.2-OSC-028 (Restriction endonuclease palindromic -> Plant tissue culture)
  'MH-9-SCIT-17-17.2-OSC-028': {
    text: "Which technique involves the cultivation of plant cells or tissues in a sterile, nutrient-rich artificial medium?",
    options: [
      "Tissue culture",
      "Hydroponics",
      "Grafting",
      "Hybridization"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "Tissue culture is the ex vivo growth of plant cells or tissues in an aseptic, nutrient medium to produce disease-free plantlets."
  },

  // 28. MH-9-SCIT-17-17.2-OSC-029 (Sticky/blunt end plasmid ligation -> Callus definition)
  'MH-9-SCIT-17-17.2-OSC-029': {
    text: "What is the unorganized, undifferentiated mass of multiplying cells formed during plant tissue culture called?",
    options: [
      "Callus",
      "Explant",
      "Embryoid",
      "Meristem"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "In plant tissue culture, multiplying cells initially form an unorganized, undifferentiated mass of cells known as a callus."
  },

  // 29. MH-9-SCIT-17-17.2-OSC-080 (Plasmid restriction enzyme diagram -> Explant definition)
  'MH-9-SCIT-17-17.2-OSC-080': {
    text: "What is the excised plant part (such as a shoot tip or leaf piece) used to initiate a tissue culture called?",
    options: [
      "Explant",
      "Callus",
      "Inoculum",
      "Seedling"
    ],
    correctAnswer: "A",
    correctAnswers: ["A"],
    solution: "An explant is any excised part of a plant (e.g., root tip, stem node, leaf tissue) taken and placed on nutrient medium to start a tissue culture."
  }
};

async function executeRemediation() {
  console.log('--- Step 1: Pre-Mutation Snapshot ---');
  await createPreMutationSnapshot(['questions'], 'remedy_29_out_of_syllabus_questions_and_boardcodes');
  console.log('Snapshot completed.');

  console.log('--- Step 2: Remediating 29 Out-Of-Syllabus Questions ---');
  for (const [id, patch] of Object.entries(REPLACEMENTS)) {
    const ref = db.collection('questions').doc(id);
    const snap = await ref.get();
    if (snap.exists) {
      console.log(`Updating ${id}...`);
      await ref.update({
        ...patch,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        isCurriculumAligned: true,
        alignedAt: admin.firestore.FieldValue.serverTimestamp()
      });
    } else {
      console.warn(`Warning: doc ${id} not found!`);
    }
  }

  console.log('--- Step 3: Fixing boardCode for 611 undefined-9-SCIT questions ---');
  const undefSnap = await db.collection('questions').get();
  const batchArray = [];
  let currentBatch = db.batch();
  let count = 0;
  let fixedCount = 0;

  undefSnap.forEach(doc => {
    const data = doc.data();
    if (!data.boardCode || data.boardCode === 'undefined') {
      let bCode = 'MH';
      if (data.board && data.board.toLowerCase().includes('cbse')) bCode = 'CBSE';
      else if (data.questionCode && data.questionCode.startsWith('CBSE')) bCode = 'CBSE';

      currentBatch.update(doc.ref, {
        boardCode: bCode,
        board: bCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      count++;
      fixedCount++;

      if (count === 400) {
        batchArray.push(currentBatch);
        currentBatch = db.batch();
        count = 0;
      }
    }
  });

  if (count > 0) batchArray.push(currentBatch);

  for (let i = 0; i < batchArray.length; i++) {
    await batchArray[i].commit();
    console.log(`Committed boardCode batch ${i + 1}/${batchArray.length}`);
  }

  console.log(`Successfully fixed boardCode for ${fixedCount} questions!`);
  console.log('--- Remediation Complete ---');
}

executeRemediation().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
