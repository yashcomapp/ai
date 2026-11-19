// scripts/mh8_ch5_topic6_part2.js
// Set B: Topic 5.6 Isotopes & Uses of Radioactive Isotopes (Questions 006-010)

const topic6Part2Questions = [
  // 5.6.1 Set B
  {
    questionCode: "MH-8-SCI-5-5.6.1-OSC-006",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.1",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.1",
    subtopicName: "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
    topicNumber: "5.6.1",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Who coined the scientific term 'isotope' in 1913 on the suggestion of Margaret Todd to describe chemically identical elements occupying the same position in the periodic table?",
    options: [
      "Frederick Soddy",
      "Ernest Rutherford",
      "J.J. Thomson",
      "Niels Bohr"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, British radiochemist **Frederick Soddy** recognized that radioactive decay chains produced elements with distinct atomic weights and radioactive decay properties, but indistinguishable chemical behavior.
At a dinner party, physician Margaret Todd suggested the Greek word **isotope** (*iso* = 'equal', *topos* = 'place'), signifying that these nuclides occupy the exact same place in the periodic table.
Soddy was awarded the Nobel Prize in Chemistry in 1921 for his pioneering investigations into the origin and nature of isotopes.

### 2. Physical Context & Practical Illustration:
Before Soddy's work, elements were assumed to have a single monolithic atomic weight; isotopes revealed that elements are naturally mixtures of atoms with different neutron numbers.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Frederick Soddy introduced the term isotope in 1913.
- **Option B is incorrect**: Rutherford discovered the atomic nucleus and proton.
- **Option C is incorrect**: Thomson built early positive-ray mass spectrographs confirming neon isotopes.
- **Option D is incorrect**: Bohr created the quantum orbital shell model.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.1-OSC-007",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.1",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.1",
    subtopicName: "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
    topicNumber: "5.6.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which instrument is used in modern chemistry and physics to physically separate, identify, and measure the precise percentage abundances of different isotopes of an element?",
    options: [
      "Mass Spectrometer",
      "Geiger Counter",
      "Electrochemical Voltameter",
      "Optical Microscope"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **Mass Spectrometer** (first developed by F.W. Aston in 1919) operates on the principle of electromagnetic deflection:
1. Atoms are vaporized and ionized into positive ions of charge \\(q = +e\\).
2. The ions are accelerated through a potential difference \\(V\\), acquiring kinetic energy:
\\[
\\frac{1}{2}m v^2 = q V \\implies v = \\sqrt{\\frac{2qV}{m}}
\\]
3. The beam enters a perpendicular magnetic field \\(B\\), where magnetic Lorentz force bends the ions into circular trajectories of radius \\(R\\):
\\[
q v B = \\frac{m v^2}{R} \\implies R = \\frac{m v}{q B} = \\frac{1}{B}\\sqrt{\\frac{2 m V}{q}} \\propto \\sqrt{m}
\\]
Because ions of different isotopes have different masses \\(m\\), they follow arcs of different radii and strike the detector at different positions, allowing precise measurement of isotopic masses and relative abundances.

### 2. Physical Context & Practical Illustration:
Aston received the 1922 Nobel Prize in Chemistry after using his mass spectrograph to discover 212 of the 287 naturally occurring isotopes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: A mass spectrometer separates and measures isotopes by their mass-to-charge ratio.
- **Option B is incorrect**: A Geiger counter detects radiation counts, but cannot distinguish isotopic masses.
- **Option C is incorrect**: Voltameters measure electrical charge passed in electrolysis.
- **Option D is incorrect**: Optical microscopes use visible light and cannot resolve subatomic particles.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.1-OSC-008",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.1",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.1",
    subtopicName: "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
    topicNumber: "5.6.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why can chemical reactions NOT be used to separate different isotopes of the same element (such as separating Uranium-235 from Uranium-238)?",
    options: [
      "Because all isotopes of an element have identical numbers of valence electrons and identical electronic configurations, making their chemical reactivity indistinguishable",
      "Because chemical reagents destroy isotopes on contact",
      "Because isotopes only exist in outer space",
      "Because all isotopes turn into lead during chemical mixing"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Chemical reactions depend exclusively on the interaction of **valence electrons**.
Both \\(^{235}_{92}\\text{U}\\) and \\(^{238}_{92}\\text{U}\\) have:
- Exactly 92 protons and 92 electrons.
- Identical electronic configurations: \\([\\text{Rn}] 5f^3 6d^1 7s^2\\).
- Identical chemical valencies and bonding tendencies.
When reacted with fluorine, both form Uranium hexafluoride (\\(\\text{UF}_6\\)) with identical chemical properties.
Therefore, isotopes cannot be separated by chemical precipitation, distillation, or titration. They can ONLY be separated using **physical mass-dependent methods** (such as gas centrifugation, gaseous diffusion through porous membranes, or laser isotope separation), exploiting the \\(0.85\\%\\) mass difference between \\(^{235}\\text{UF}_6\\) and \\(^{238}\\text{UF}_6\\).

### 2. Physical Context & Practical Illustration:
This is why enriching Uranium-235 for nuclear fuel requires massive industrial centrifuge cascades rather than simple chemical refinery reactions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Identical valence configurations cause identical chemical reactions, preventing chemical separation.
- **Option B is incorrect**: Chemical reagents form stable isotopic compounds without destruction.
- **Option C is incorrect**: Isotopes make up ordinary terrestrial matter everywhere.
- **Option D is incorrect**: Only radioactive decay chains over billions of years lead to lead.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.1-OSC-009",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.1",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.1",
    subtopicName: "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
    topicNumber: "5.6.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which internationally agreed reference isotope serves as the universal anchor standard for defining the unified atomic mass unit (\\(1\\text{ u}\\))?",
    options: [
      "Carbon-12 (\\(^{12}_6\\text{C}\\)) assigned a mass of exactly \\(12\\text{ u}\\)",
      "Hydrogen-1 (\\(^1_1\\text{H}\\)) assigned a mass of exactly \\(1\\text{ u}\\)",
      "Oxygen-16 (\\(^{16}_8\\text{O}\\)) assigned a mass of exactly \\(16\\text{ u}\\)",
      "Uranium-238 (\\(^{238}_{92}\\text{U}\\)) assigned a mass of \\(238\\text{ u}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1961, the International Union of Pure and Applied Chemistry (IUPAC) and the International Union of Pure and Applied Physics (IUPAP) agreed to define the unified atomic mass unit (symbol \\(\\text{u}\\) or \\(\\text{Da}\\), Dalton) relative to the **Carbon-12 isotope**:
\\[
1\\text{ u} = \\frac{1}{12} \\times \\text{Mass of one unbound neutral } ^{12}_6\\text{C}\\text{ atom in its ground state}
\\]
Numerically:
\\[
1\\text{ u} = \\frac{1.992646547 \\times 10^{-26}\\text{ kg}}{12} = 1.66053906660 \\times 10^{-27}\\text{ kg} \\approx 931.494\\text{ MeV}/c^2
\\]

### 2. Physical Context & Practical Illustration:
Before 1961, chemists used natural oxygen (16.000) and physicists used the Oxygen-16 isotope, causing slight discrepancies; Carbon-12 unified both branches of science.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Carbon-12 is the universal international mass anchor standard.
- **Option B is incorrect**: Hydrogen was Dalton's original 1803 standard, abandoned due to compound formation errors.
- **Option C is incorrect**: Oxygen was used between 1900 and 1961, then replaced by Carbon-12.
- **Option D is incorrect**: Uranium-238 has never been used as the base reference.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.1-OSC-010",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.1",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.1",
    subtopicName: "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
    topicNumber: "5.6.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Magnesium exists as three natural stable isotopes: \\(^{24}\\text{Mg}\\) (78.99%, mass 23.985 u), \\(^{25}\\text{Mg}\\) (10.00%, mass 24.986 u), and \\(^{26}\\text{Mg}\\) (11.01%, mass 25.983 u). What is the average atomic mass of natural magnesium?",
    options: [
      "\\(24.31\\text{ u}\\)",
      "\\(25.00\\text{ u}\\)",
      "\\(23.99\\text{ u}\\)",
      "\\(26.00\\text{ u}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Compute the weighted sum across all three stable isotopes:
\\[
A_{\\text{avg}} = \\sum_{i=1}^3 (f_i \\times m_i)
\\]
1. For \\(^{24}\\text{Mg}\\): \\(0.7899 \\times 23.985\\text{ u} = 18.9458\\text{ u}\\)
2. For \\(^{25}\\text{Mg}\\): \\(0.1000 \\times 24.986\\text{ u} = 2.4986\\text{ u}\\)
3. For \\(^{26}\\text{Mg}\\): \\(0.1101 \\times 25.983\\text{ u} = 2.8607\\text{ u}\\)
Adding the components:
\\[
A_{\\text{avg}} = 18.9458 + 2.4986 + 2.8607 = 24.3051\\text{ u} \\approx 24.31\\text{ u}
\\]

### 2. Physical Context & Practical Illustration:
This calculated \\(24.31\\text{ u}\\) matches the official standard atomic weight of Magnesium printed on all periodic tables worldwide.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The weighted average is \\(24.31\\text{ u}\\).
- **Option B is incorrect**: \\(25.00\\text{ u}\\) is the unweighted average \\(\\frac{24+25+26}{3}\\), ignoring the 79% dominance of Mg-24.
- **Option C is incorrect**: \\(23.99\\text{ u}\\) ignores the heavier isotopes entirely.
- **Option D is incorrect**: \\(26.00\\text{ u}\\) reflects only Mg-26.`
  },

  // 5.6.2 Set B
  {
    questionCode: "MH-8-SCI-5-5.6.2-OSC-006",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.2",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.2",
    subtopicName: "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating",
    topicNumber: "5.6.2",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which radioisotope is injected into underground oil and water pipelines as a radioactive tracer to pinpoint the exact location of subterranean leaks without digging?",
    options: [
      "Sodium-24 (\\(^{24}_{11}\\text{Na}\\))",
      "Uranium-238 (\\(^{238}_{92}\\text{U}\\))",
      "Carbon-14 (\\(^{14}_6\\text{C}\\))",
      "Plutonium-239 (\\(^{239}_{94}\\text{Pu}\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Sodium-24 (\\(^{24}_{11}\\text{Na}\\))** is an ideal industrial tracer:
1. It dissolves readily in fluids as \\(^{24}\\text{NaCl}\\).
2. It decays with a short half-life of \\(T_{1/2} = 15.0\\text{ hours}\\), ensuring that no long-term hazardous radioactivity lingers in the environment.
3. It emits penetrating gamma rays (\\(1.37\\text{ MeV}\\) and \\(2.75\\text{ MeV}\\)) that easily penetrate soil and pipe walls.
When fluid leaks out, radioactive liquid accumulates in the surrounding soil. A technician walking above ground with a portable Geiger-Müller counter detects a sharp peak in radiation at the exact leak position.

### 2. Physical Context & Practical Illustration:
Using tracers saves millions of rupees and hours of labor by avoiding destructive excavation of hundreds of meters of intact underground piping.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Sodium-24 is the standard short-lived tracer for pipeline leaks and circulatory medical diagnostics.
- **Option B is incorrect**: Uranium-238 has a 4.5-billion-year half-life and alpha emission, unsuited for leak tracking.
- **Option C is incorrect**: Carbon-14 emits weak beta particles that cannot penetrate pipe steel or soil.
- **Option D is incorrect**: Plutonium is a heavy toxic weapons-grade fissile material.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.2-OSC-007",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.2",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.2",
    subtopicName: "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating",
    topicNumber: "5.6.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which radioisotope is widely used in agricultural research as a radioactive tracer to study the rate and pathways of fertilizer uptake by plant roots?",
    options: [
      "Phosphorus-32 (\\(^{32}_{15}\\text{P}\\))",
      "Iodine-131 (\\(^{131}_{53}\\text{I}\\))",
      "Cobalt-60 (\\(^{60}_{27}\\text{Co}\\))",
      "Lead-206 (\\(^{206}_{82}\\text{Pb}\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Phosphorus is an essential plant macronutrient required for ATP synthesis, DNA, and root development.
By adding trace amounts of **Phosphorus-32 (\\(^{32}_{15}\\text{P}\\))** (a beta emitter with a half-life of \\(14.3\\text{ days}\\)) to phosphate fertilizers:
\\[
^{32}_{15}\\text{P} \\rightarrow ^{32}_{16}\\text{S} + e^- + \\bar{\\nu}_e
\\]
scientists can map the movement of phosphorus from soil into roots, stems, and leaves using autoradiography or radiation counters. This determines the exact optimum timing, placement, and quantity of fertilizer required for crop yield maximization.

### 2. Physical Context & Practical Illustration:
Phosphorus-32 tracing enabled the Green Revolution to optimize fertilizer usage, reducing chemical waste and groundwater contamination.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Phosphorus-32 is the agricultural tracer for phosphate uptake.
- **Option B is incorrect**: Iodine-131 is used for thyroid medicine, not agricultural plant uptake.
- **Option C is incorrect**: Cobalt-60 is an industrial/medical sterilizer, not a metabolic fertilizer tracer.
- **Option D is incorrect**: Lead-206 is a stable, non-radioactive end-product of uranium decay.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.2-OSC-008",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.2",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.2",
    subtopicName: "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating",
    topicNumber: "5.6.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "In industrial radiography, how are high-energy gamma-emitting radioisotopes (like Cobalt-60 and Iridium-192) utilized for non-destructive testing (NDT)?",
    options: [
      "To inspect the internal structural integrity of metal castings, aircraft wings, and heavy welds for hidden micro-cracks without cutting or damaging the components",
      "To weld thick metal plates together using nuclear heat",
      "To clean rust and paint off metallic surfaces",
      "To magnetize titanium submarine hulls"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Industrial radiography utilizes the high penetration power of gamma rays:
\\[
I = I_0 e^{-\\mu x}
\\]
where \\(\\mu\\) is the linear attenuation coefficient of the metal and \\(x\\) is thickness.
A radioactive pellet of **Iridium-192** or **Cobalt-60** is placed on one side of a metal weld or casting, and a photographic film (or digital detector) is placed on the opposite side:
- Dense, defect-free metal absorbs gamma rays uniformly.
- Any internal void, air pocket, slag inclusion, or hairline crack absorbs fewer gamma rays, producing a darker shadow on the radiographic film.
This non-destructive evaluation ensures structural safety before equipment enters service.

### 2. Physical Context & Practical Illustration:
Every high-pressure gas pipeline, aircraft engine turbine blade, and nuclear pressure vessel weld is verified using industrial gamma radiography.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Industrial radiography detects hidden internal cracks and voids non-destructively.
- **Option B is incorrect**: Gamma rays do not produce thermal fusion for welding.
- **Option C is incorrect**: Sandblasting or acids remove rust, not radioisotope pellets.
- **Option D is incorrect**: Titanium is non-magnetic, and gamma rays do not impart magnetization.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.2-OSC-009",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.2",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.2",
    subtopicName: "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating",
    topicNumber: "5.6.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "How is gamma radiation from Cobalt-60 commercially employed in food preservation and medical manufacturing?",
    options: [
      "To sterilize packaged surgical instruments (syringes, gloves) and eradicate bacteria, insects, and sprouting in stored food without using heat or chemical preservatives",
      "To cook food thoroughly from the inside like a microwave oven",
      "To add nutritional vitamins and minerals directly into grains",
      "To dye medical gloves a bright blue surgical color"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Food irradiation and cold sterilization**:
High-energy gamma rays from Cobalt-60 pass directly through pre-packaged, sealed items. The ionizing radiation disrupts the DNA of microorganisms (bacteria like *Salmonella* and *E. coli*, molds, fungi) and insects, killing them instantly without raising the product's temperature ('cold sterilization'):
\\[
\\text{Gamma dose} \\implies \\text{Microbial DNA double-strand breaks} \\implies \\text{Sterility}
\\]
Crucially:
- The treated product **never becomes radioactive** because gamma photon energies (\\(\\approx 1.25\\text{ MeV}\\)) are far below the threshold needed to induce nuclear reactions.
- Packaged surgical tools remain sterile indefinitely until the hermetic seal is broken.

### 2. Physical Context & Practical Illustration:
BARC operates industrial irradiators in India (like KRUSHAK in Lasalgaon for onions and spices) to prevent post-harvest spoilage and extend shelf life for export.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Cold sterilization destroys pathogens in surgical equipment and preserves food without heat.
- **Option B is incorrect**: Gamma irradiation produces negligible thermal heating.
- **Option C is incorrect**: Radiation does not synthesize vitamins.
- **Option D is incorrect**: Dyes are chemical colorants, not radiation effects.`
  },
  {
    questionCode: "MH-8-SCI-5-5.6.2-OSC-010",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.6.2",
    parentTopicCode: "MH-8-SCI-5-5.6",
    parentTopicName: "Isotopes & Uses of Radioactive Isotopes",
    subtopicCode: "MH-8-SCI-5-5.6.2",
    subtopicName: "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating",
    topicNumber: "5.6.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Why is the technique of Carbon-14 radiocarbon dating ineffective for determining the geological age of dinosaur fossils or ancient granite rocks (\\(> 65\\text{ million years old}\\))?",
    options: [
      "Because the half-life of Carbon-14 is only \\(5730\\text{ years}\\), so after \\(\\approx 50{,}000\\text{ years}\\) (approx. 10 half-lives), the remaining \\(^{14}\\text{C}\\) has decayed to virtually undetectable levels, requiring long-lived radioisotopes like Uranium-238 or Potassium-40 instead",
      "Because dinosaurs contained zero carbon atoms in their skeletons",
      "Because granite rocks dissolve Carbon-14 into helium gas",
      "Because cosmic rays only began producing Carbon-14 in the 20th century"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Radioactive decay equation:
\\[
\\frac{N(t)}{N_0} = \\left(\\frac{1}{2}\\right)^{t / T_{1/2}}
\\]
With \\(T_{1/2} = 5730\\text{ years}\\):
- After 10 half-lives (\\(57{,}300\\text{ years}\\)):
\\[
\\frac{N}{N_0} = \\left(\\frac{1}{2}\\right)^{10} = \\frac{1}{1024} \\approx 0.1\\%
\\]
- After 65 million years (\\(t \\approx 65 \\times 10^6\\text{ years}\\)):
\\[
n = \\frac{65 \\times 10^6}{5730} \\approx 11{,}344\\text{ half-lives} \\implies \\frac{N}{N_0} = (0.5)^{11344} \\approx 0
\\]
Not a single atom of the original \\(^{14}\\text{C}\\) survives.
To date rocks and dinosaur-bearing geological strata from millions to billions of years ago, geologists use **geochronological radioisotopes with multi-billion-year half-lives**:
1. **Potassium-40 to Argon-40** (\\(T_{1/2} = 1.25 \\times 10^9\\text{ years}\\))
2. **Uranium-238 to Lead-206** (\\(T_{1/2} = 4.47 \\times 10^9\\text{ years}\\))
3. **Rubidium-87 to Strontium-87** (\\(T_{1/2} = 4.9 \\times 10^{10}\\text{ years}\\))

### 2. Physical Context & Practical Illustration:
Using Carbon-14 to date dinosaurs is like trying to measure the distance across an ocean using a 15-centimeter plastic school ruler.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The 5730-year half-life limits \\(^{14}\\text{C}\\) dating to \\(\\approx 50{,}000\\text{ years}\\); deep geological dating requires \\(^{238}\\text{U}\\) or \\(^{40}\\text{K}\\).
- **Option B is incorrect**: Dinosaurs were organic carbon-based living organisms.
- **Option C is incorrect**: Granite is silicate rock; it does not turn carbon into helium.
- **Option D is incorrect**: Cosmic rays have bombarded Earth's atmosphere continuously for billions of years.`
  }
];

module.exports = { topic6Part2Questions };
