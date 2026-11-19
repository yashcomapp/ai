// scripts/mh8_ch5_topic2_part2.js
// Set B: Topic 5.2 Rutherford Gold Foil Experiment & Nuclear Model of Atom (Questions 006-010)

const topic2Part2Questions = [
  // 5.2.1 Set B
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-006",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.1",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.1",
    subtopicName: "Alpha particle scattering experiment",
    topicNumber: "5.2.1",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which two research associates physically executed the thousands of microscopic scintillation measurements under Rutherford's guidance in the gold foil experiment?",
    options: [
      "Hans Geiger and Ernest Marsden",
      "John Dalton and J.J. Thomson",
      "James Chadwick and Niels Bohr",
      "Marie Curie and Pierre Curie"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1909–1911 at the University of Manchester, the physical counting of \\(\\alpha\\)-particle scintillations on zinc sulfide screens was carried out by **Hans Geiger** (senior colleague) and **Ernest Marsden** (undergraduate student) under the direct supervision of Ernest Rutherford. The experiment is often historically termed the **Geiger-Marsden experiment**.

### 2. Physical Context & Practical Illustration:
Geiger and Marsden sat in absolute darkness for hours, allowing their eyes to adapt to detect microscopic flashes of light through a low-power viewing microscope.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Hans Geiger and Ernest Marsden performed the experimental measurements.
- **Option B is incorrect**: Dalton proposed indivisible atoms; Thomson discovered electrons.
- **Option C is incorrect**: Chadwick discovered neutrons; Bohr proposed the quantum orbit model.
- **Option D is incorrect**: Marie and Pierre Curie discovered Polonium and Radium in Paris.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-007",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.1",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.1",
    subtopicName: "Alpha particle scattering experiment",
    topicNumber: "5.2.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What led Rutherford to conclude that the positive charge of an atom must be concentrated in an exceedingly small volume rather than spread throughout the atom?",
    options: [
      "Only a very tiny fraction of \\(\\alpha\\)-particles suffered large-angle deflections, meaning the positive repelling core occupies only a minuscule fraction of atomic volume",
      "All \\(\\alpha\\)-particles bounced back uniformly in all directions",
      "Electrons stopped moving and fell directly into the radioactive source",
      "The gold foil dissolved completely into helium gas during bombardment"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
If the positive charge was spread over the entire atomic volume (radius \\(R \\approx 10^{-10}\\text{ m}\\)), the maximum electric field would be far too weak to deflect heavy, fast \\(\\alpha\\)-particles by large angles:
\\[
E_{\\text{diffuse}} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze}{R^2} \\approx \\text{weak}
\\]
Only by compressing the total positive charge \\(+Ze\\) into an ultra-dense nucleus of radius \\(r_0 \\approx 10^{-15}\\text{ m}\\) does the local repulsive field become colossal:
\\[
E_{\\text{nuclear}} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze}{r_0^2} \\propto 10^{10} \\times E_{\\text{diffuse}}
\\]
Because this intense field is confined to a tiny target, only particles passing exceptionally close (a tiny fraction) experience large deflections.

### 2. Physical Context & Practical Illustration:
A needle in a haystack: you will almost never hit the needle unless you pass directly through its infinitesimal cross-section.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The rarity of large-angle deflections proves the extreme compactness of the positive core.
- **Option B is incorrect**: Over 99% passed straight undeflected.
- **Option C is incorrect**: Extranuclear electrons do not fall into the source.
- **Option D is incorrect**: Gold foil remains intact; no chemical dissolution occurs.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-008",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.1",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.1",
    subtopicName: "Alpha particle scattering experiment",
    topicNumber: "5.2.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "According to Rutherford's scattering formula, how does the number of scattered \\(\\alpha\\)-particles \\(N(\\theta)\\) detected per unit area vary with the scattering angle \\(\\theta\\)?",
    options: [
      "\\(N(\\theta) \\propto \\frac{1}{\\sin^4(\\theta / 2)}\\)",
      "\\(N(\\theta) \\propto \\sin^2(\\theta)\\)",
      "\\(N(\\theta) \\propto \\cos(\\theta / 2)\\)",
      "\\(N(\\theta) \\propto \\frac{1}{\\theta^2}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rutherford derived the differential scattering cross-section by applying Coulomb's inverse-square law to classical hyperbolic orbits:
\\[
N(\\theta) = \\frac{n_i n_t Z^2 e^4}{(8\\pi\\varepsilon_0)^2 r^2 K^2} \\cdot \\frac{1}{\\sin^4(\\theta / 2)}
\\]
This means the number of detected particles decreases dramatically as the scattering angle increases:
\\[
N(\\theta) \\propto \\frac{1}{\\sin^4(\\theta / 2)}
\\]
For example, the number of particles scattered at \\(\\theta = 90^\\circ\\) is \\(16\\) times greater than those scattered at \\(\\theta = 180^\\circ\\).

### 2. Physical Context & Practical Illustration:
Geiger and Marsden's experimental scintillation counts across angles from \\(5^\\circ\\) to \\(150^\\circ\\) matched this \\(\\frac{1}{\\sin^4(\\theta/2)}\\) curve with spectacular precision.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(N(\\theta) \\propto \\frac{1}{\\sin^4(\\theta / 2)}\\) is Rutherford's famous scattering law.
- **Option B is incorrect**: Direct sine dependence would predict zero particles at small angles, contradicting observations.
- **Option C is incorrect**: Cosine dependence fails to capture the steep Coulomb drop.
- **Option D is incorrect**: Simple inverse square in angle fails at large angles.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-009",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.1",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.1",
    subtopicName: "Alpha particle scattering experiment",
    topicNumber: "5.2.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What protective enclosure was used to contain the radioactive source in the gold foil experiment so that a sharp, collimated beam of \\(\\alpha\\)-particles was directed toward the foil?",
    options: [
      "A thick lead (\\(\\text{Pb}\\)) block with a narrow slit aperture",
      "An iron magnet with magnetic focusing coils",
      "A sealed wooden box filled with water",
      "A glass cylinder coated with aluminum foil"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Alpha particles are absorbed by dense matter. To create a narrow, straight pencil-beam of \\(\\alpha\\)-particles:
1. The radioactive source (Radium/Bismuth) was placed inside a thick **lead cavity**. Lead has high density (\\(11.34\\text{ g/cm}^3\\)) and high atomic number (\\(Z = 82\\)), absorbing all stray radiation emitted in unwanted directions.
2. A narrow aperture or slit in the lead block collimated the particles into a fine, parallel beam directed straight at the gold target.

### 2. Physical Context & Practical Illustration:
Lead collimators remain the universal standard in radiation shielding, radiology, and nuclear physics experiments.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: A thick lead block with a narrow slit collimated the beam.
- **Option B is incorrect**: Magnetic focusing was not used in the original 1911 setup.
- **Option C is incorrect**: Wood and water do not provide precision directional collimation for radioactive sources.
- **Option D is incorrect**: Glass cannot absorb multi-MeV alpha radiation effectively.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-010",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.1",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.1",
    subtopicName: "Alpha particle scattering experiment",
    topicNumber: "5.2.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "In the scattering of \\(\\alpha\\)-particles by a heavy nucleus, the perpendicular distance from the center of the nucleus to the initial velocity vector of the projectile at infinity is defined as the:",
    options: [
      "Impact parameter (\\(b\\))",
      "Distance of closest approach (\\(r_0\\))",
      "Scattering angle (\\(\\theta\\))",
      "Nuclear radius (\\(R_N\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **impact parameter (\\(b\\))** is defined as the perpendicular distance between the initial trajectory line of the \\(\\alpha\\)-particle (before deflection) and the center of the target nucleus.
It is mathematically related to the scattering angle \\(\\theta\\) by:
\\[
b = \\frac{1}{4\\pi\\varepsilon_0} \\frac{Z e^2}{K} \\cot\\left(\\frac{\\theta}{2}\\right)
\\]
- For head-on collisions (\\(b = 0\\)): \\(\\cot(\\theta / 2) = 0 \\implies \\theta = 180^\\circ\\) (direct rebound).
- For large impact parameters (\\(b \\gg r_0\\)): \\(\\theta \\approx 0^\\circ\\) (virtually undeflected).

### 2. Physical Context & Practical Illustration:
The impact parameter acts as an aim offset. A smaller impact parameter means a closer encounter with the positive core, producing a violent deflection.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The perpendicular distance is the impact parameter (\\(b\\)).
- **Option B is incorrect**: Distance of closest approach is the minimum physical separation during head-on collision.
- **Option C is incorrect**: Scattering angle is the angular deviation, not a spatial distance.
- **Option D is incorrect**: Nuclear radius is the boundary dimension of the nucleus itself.`
  },

  // 5.2.2 Set B
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-006",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.2",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.2",
    subtopicName: "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
    topicNumber: "5.2.2",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What astronomical analogy did Rutherford explicitly use to describe the arrangement of electrons in his atomic model?",
    options: [
      "Planets revolving in orbits around the massive central Sun (Solar System)",
      "Saturn's rings composed of static ice crystals",
      "Galactic spiral arms rotating around a supermassive black hole",
      "Moons colliding with an asteroid belt"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rutherford modeled the atom directly after the **Solar System**:
- The heavy, positively charged nucleus corresponds to the massive central **Sun**.
- The light, negatively charged electrons correspond to the revolving **planets**.
- The attractive electrostatic Coulomb force \\(F_e = \\frac{k q_1 q_2}{r^2}\\) plays the role of the gravitational attraction \\(F_g = \\frac{G M m}{r^2}\\).

### 2. Physical Context & Practical Illustration:
Just as the solar system is mostly empty space with planets orbiting at immense distances from the Sun, an atom is overwhelmingly empty space with electrons orbiting at immense distances from the nucleus.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The planetary solar system is Rutherford's famous analogy.
- **Option B is incorrect**: Saturn's rings was Nagaoka's earlier Saturnian model (1904).
- **Option C is incorrect**: Galaxies were not understood in their modern form in 1911.
- **Option D is incorrect**: Electrons do not collide randomly like asteroid belts in stable atoms.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-007",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.2",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.2",
    subtopicName: "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
    topicNumber: "5.2.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What prevents the negatively charged planetary electrons in Rutherford's model from being pulled straight into the positively charged nucleus by electrostatic attraction?",
    options: [
      "The rapid circular orbital motion of the electrons provides the required dynamic inertia and centripetal acceleration balance",
      "Nuclear neutrons actively push the electrons away with positive magnetic force",
      "Electrons carry an internal antigravity field that repels the nucleus",
      "The vacuum between the nucleus and electrons blocks electric field lines"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
If electrons were static and at rest, the attractive electrostatic Coulomb force:
\\[
F_e = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze^2}{r^2}
\\]
would pull them directly into the positive nucleus, causing instant collapse.
Rutherford proposed that electrons are in **continuous, rapid orbital motion**. The inward electrostatic force acts as the necessary **centripetal force** that continuously curves their velocity vector into a stable circular orbit:
\\[
\\frac{m_e v^2}{r} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze^2}{r^2}
\\]

### 2. Physical Context & Practical Illustration:
Just as the Moon does not fall onto Earth because of its orbital tangential velocity, electrons do not fall into the nucleus because of their orbital velocity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Orbital tangential motion provides the dynamic centripetal balance.
- **Option B is incorrect**: Neutrons have zero electric charge and do not repel electrons.
- **Option C is incorrect**: Antigravity does not exist in subatomic physics.
- **Option D is incorrect**: Coulomb fields propagate uninhibited through vacuum.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-008",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.2",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.2",
    subtopicName: "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
    topicNumber: "5.2.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Given that the density of matter inside the atomic nucleus is approximately \\(10^{17}\\text{ kg/m}^3\\), what does this colossal density reveal about the physical nature of atoms?",
    options: [
      "Ordinary bulk matter appears solid only because of electrostatic electron repulsive envelopes, while actual nuclear mass is compressed into an ultra-dense point-like core",
      "Atoms are solid lead-like marbles throughout their entire volume",
      "Electrons have higher density than the atomic nucleus",
      "Nuclear density fluctuates with changes in atmospheric pressure"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Nuclear density (\\(\\rho_{\\text{nucleus}}\\)) is calculated from nuclear mass and radius:
\\[
\\rho = \\frac{M}{V} = \\frac{A \\cdot 1.66 \\times 10^{-27}\\text{ kg}}{\\frac{4}{3}\\pi (R_0 A^{1/3})^3} = \\frac{3 \\times 1.66 \\times 10^{-27}}{4\\pi (1.2 \\times 10^{-15})^3} \\approx 2.3 \\times 10^{17}\\text{ kg/m}^3
\\]
This density is constant for all nuclei and is over \\(10^{14}\\) times denser than water!
This means that nearly 100% of the mass of any solid object (tables, rocks, human bodies) is concentrated into microscopic nuclear packets separated by enormous voids. What prevents objects from passing through each other is not solid mass, but the electrostatic repulsion between their outer electron clouds.

### 2. Physical Context & Practical Illustration:
One cubic centimeter of pure nuclear matter would weigh approximately 230 million metric tons (the mass of a mountain).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Nuclear matter is ultra-dense, and bulk solidity is mediated by electron cloud fields.
- **Option B is incorrect**: Bulk matter is not uniformly dense; 99.999% of atomic volume is vacuum.
- **Option C is incorrect**: Electron mass is negligible compared to nuclear nucleons.
- **Option D is incorrect**: Nuclear density is governed by strong nuclear forces and is completely independent of pressure.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-009",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.2",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.2",
    subtopicName: "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
    topicNumber: "5.2.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What term is officially used in physics to describe the central core discovered by Rutherford that contains all the positive charge and nucleons of an atom?",
    options: [
      "Nucleus",
      "Positron",
      "Nucleoid",
      "Centrosome"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In his May 1911 paper published in the *Philosophical Magazine*, Ernest Rutherford introduced the term **atomic nucleus** to describe the central charge-bearing core of the atom.
Characteristics of the nucleus:
1. Carries positive charge equal to \\(+Ze\\).
2. Contains protons and neutrons (jointly termed **nucleons**).
3. Has a radius on the order of \\(10^{-15}\\text{ m}\\) (femtometres).

### 2. Physical Context & Practical Illustration:
The word *nucleus* comes from Latin meaning 'little nut' or 'kernel', highlighting its position as the tiny, hard kernel inside the soft atomic shell.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The nucleus is the official scientific term.
- **Option B is incorrect**: A positron is an antimatter positive electron, discovered in 1932 by Anderson.
- **Option C is incorrect**: A nucleoid is the unorganized genetic region in bacterial cells.
- **Option D is incorrect**: A centrosome is a cellular organelle involved in cell division.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-010",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.2",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.2",
    subtopicName: "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
    topicNumber: "5.2.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "If an \\(\\alpha\\)-particle of kinetic energy \\(5\\text{ MeV}\\) approaches a gold nucleus (\\(Z = 79\\)) head-on, what is the calculated order of magnitude of the distance of closest approach \\(r_0\\)?",
    options: [
      "\\(\\approx 4.5 \\times 10^{-14}\\text{ m} = 45\\text{ fm}\\)",
      "\\(\\approx 10^{-10}\\text{ m} = 1\\text{ Å}\\)",
      "\\(\\approx 10^{-6}\\text{ m} = 1\\,\\mu\\text{m}\\)",
      "\\(\\approx 10^{-20}\\text{ m}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
At closest approach, \\(K = U\\):
\\[
K = \\frac{1}{4\\pi\\varepsilon_0} \\frac{(2e)(Ze)}{r_0} \\implies r_0 = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 K}
\\]
Given:
- \\(Z = 79\\) (Gold)
- \\(K = 5\\text{ MeV} = 5 \\times 10^6 \\times 1.602 \\times 10^{-19}\\text{ J} = 8.01 \\times 10^{-13}\\text{ J}\\)
- \\(\\frac{1}{4\\pi\\varepsilon_0} = 8.99 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2\\)
Substituting:
\\[
r_0 = \\frac{(8.99 \\times 10^9) \\times 2 \\times 79 \\times (1.602 \\times 10^{-19})^2}{8.01 \\times 10^{-13}}
\\]
\\[
r_0 = \\frac{(8.99 \\times 10^9) \\times 158 \\times (2.566 \\times 10^{-38})}{8.01 \\times 10^{-13}} = \\frac{3.64 \\times 10^{-26}}{8.01 \\times 10^{-13}} \\approx 4.55 \\times 10^{-14}\\text{ m} = 45.5\\text{ fm}
\\]
This proved to Rutherford that the radius of the gold nucleus must be strictly less than \\(4.55 \\times 10^{-14}\\text{ m}\\).

### 2. Physical Context & Practical Illustration:
The \\(\\alpha\\)-particle turns around at 45.5 femtometres away, well outside the gold nucleus (whose true physical radius is \\(R \\approx 7\\text{ fm}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(r_0 \\approx 4.5 \\times 10^{-14}\\text{ m}\\).
- **Option B is incorrect**: \\(10^{-10}\\text{ m}\\) is the size of the whole atom, not the nuclear closest approach.
- **Option C is incorrect**: \\(10^{-6}\\text{ m}\\) is a microscopic cellular scale.
- **Option D is incorrect**: \\(10^{-20}\\text{ m}\\) is sub-quark scale, far beyond Rutherford probe energies.`
  },

  // 5.2.3 Set B
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-006",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.3",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.3",
    subtopicName: "Drawbacks of Rutherford model (stability of orbital electrons)",
    topicNumber: "5.2.3",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why is a revolving electron considered to be an accelerated particle even if its orbital speed remains constant?",
    options: [
      "Because its direction of motion is continuously changing along the curved circular path, producing a centripetal acceleration \\(a = \\frac{v^2}{r}\\)",
      "Because its mass increases continuously as it orbits the nucleus",
      "Because gravity constantly speeds up the electron toward the Earth",
      "Because electric charge changes magnitude during rotation"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is defined as the time rate of change of **velocity** (a vector quantity):
\\[
\\vec{a} = \\frac{d\\vec{v}}{dt}
\\]
Even if the scalar speed \\(|\\vec{v}| = v\\) is constant, an electron moving in a circular path must constantly change the direction of its velocity vector. This directional change generates an inward **centripetal acceleration**:
\\[
a_c = \\frac{v^2}{r}
\\]
directed toward the central nucleus. By Maxwell's electrodynamics, any accelerating electric charge must radiate electromagnetic energy.

### 2. Physical Context & Practical Illustration:
Just as a car rounding a curve at a steady 50 km/h pushes passengers sideways due to centripetal acceleration, a revolving electron is always accelerated.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Continuous change in velocity direction creates centripetal acceleration \\(a = v^2/r\\).
- **Option B is incorrect**: In circular orbits of constant speed, relativistic mass does not increase.
- **Option C is incorrect**: Subatomic acceleration is overwhelmingly electrostatic, not terrestrial gravity.
- **Option D is incorrect**: Electric charge is an invariant scalar.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-007",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.3",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.3",
    subtopicName: "Drawbacks of Rutherford model (stability of orbital electrons)",
    topicNumber: "5.2.3",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What geometric trajectory would a revolving electron follow if it continuously radiated energy as predicted by classical physics?",
    options: [
      "A contracting inward spiral ending in a collision with the nucleus",
      "An expanding outward spiral flying into outer space",
      "A perfect unchanging ellipse with fixed major and minor axes",
      "A figure-eight lemniscate alternating between two nuclei"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The total mechanical energy of an electron in a circular orbit of radius \\(r\\) is:
\\[
E = K + U = \\frac{1}{2}m_e v^2 - \\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze^2}{r} = -\\frac{1}{8\\pi\\varepsilon_0}\\frac{Ze^2}{r}
\\]
As the electron radiates electromagnetic waves, its total energy \\(E\\) must become increasingly negative:
\\[
\\frac{dE}{dt} = -P_{\\text{rad}} < 0 \\implies \\frac{d}{dt}\\left(-\\frac{1}{r}\\right) < 0 \\implies \\frac{dr}{dt} < 0
\\]
The orbital radius \\(r\\) must continuously shrink, forcing the electron into an **inward spiral path** until it impacts the nucleus.

### 2. Physical Context & Practical Illustration:
Like an artificial satellite experiencing atmospheric drag that slowly loses altitude and spirals into the Earth, an electron radiating energy spirals inward.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Energy loss forces an inward contracting spiral toward the nucleus.
- **Option B is incorrect**: Expanding outward would require continuous energy *input*, not radiation loss.
- **Option C is incorrect**: Fixed elliptical orbits occur only when energy is perfectly conserved (no radiation).
- **Option D is incorrect**: Figure-eight orbits describe molecular orbitals in diatomic molecules, not single atoms.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-008",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.3",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.3",
    subtopicName: "Drawbacks of Rutherford model (stability of orbital electrons)",
    topicNumber: "5.2.3",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which fundamental branch of physics, founded by Max Planck and Albert Einstein, was required to replace classical mechanics to explain the true behavior of atomic electrons?",
    options: [
      "Quantum Mechanics",
      "Classical Thermodynamics",
      "Newtonian Kinematics",
      "Geometrical Optics"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Classical mechanics (Newton's laws) and classical electrodynamics (Maxwell's equations) assume physical quantities (energy, momentum, orbit radius) can vary continuously.
At subatomic dimensions (\\(\\approx 10^{-10}\\text{ m}\\)), classical physics fails completely.
**Quantum Mechanics**, initiated by Planck's energy quantization (\\(E = h\\nu\\)), Einstein's photoelectric effect, and Bohr's quantized orbits, demonstrated that:
1. Energy states are discrete (quantized).
2. Electrons exhibit wave-particle duality (de Broglie: \\(\\lambda = h/p\\)).
3. Radiation occurs only during quantum leaps between stationary states, resolving the Rutherford collapse.

### 2. Physical Context & Practical Illustration:
Quantum mechanics is the bedrock of all modern technology, including semiconductors, lasers, magnetic resonance imaging (MRI), and digital microchips.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Quantum mechanics was the new physics that solved atomic stability.
- **Option B is incorrect**: Thermodynamics governs macroscopic heat and entropy, not subatomic orbital mechanics.
- **Option C is incorrect**: Newtonian kinematics is the very classical framework that failed.
- **Option D is incorrect**: Geometrical optics treats light as classical straight rays, ignoring quantum effects.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-009",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.3",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.3",
    subtopicName: "Drawbacks of Rutherford model (stability of orbital electrons)",
    topicNumber: "5.2.3",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why could Rutherford's model not explain the discrete characteristic colors produced by different metal salts in a flame test (e.g. golden yellow for Sodium, red for Strontium)?",
    options: [
      "Because the model lacked quantized electron energy levels and could not predict discrete emission wavelengths",
      "Because Rutherford believed all elements contain identical atomic nuclei",
      "Because the flame test was not invented until modern laser spectroscopy was developed",
      "Because the model claimed that heat energy turns electrons into protons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When metallic salts are heated in a flame:
1. Thermal energy excites valence electrons to higher energy states.
2. When these electrons fall back to lower shells, they emit photons of exact, discrete wavelengths:
\\[
\\lambda = \\frac{hc}{\\Delta E}
\\]
- Sodium emits two sharp yellow lines at \\(589.0\\text{ nm}\\) and \\(589.6\\text{ nm}\\) (D-lines).
- Strontium emits bright crimson red lines at \\(640\\text{ to } 690\\text{ nm}\\).
Because Rutherford's model allowed arbitrary continuous orbits, it predicted that heated atoms should emit an unbroken rainbow smear of light, failing to explain the distinctive flame colors.

### 2. Physical Context & Practical Illustration:
Flame test colors are used in fireworks chemistry and forensic mineralogy as reliable visual signatures of specific metal cations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Continuous classical orbits cannot account for discrete wavelength emissions.
- **Option B is incorrect**: Rutherford explicitly proved that different elements have different nuclear charges (\\(Z\\)).
- **Option C is incorrect**: Flame tests were developed in the mid-19th century by Bunsen and Kirchhoff, well before Rutherford.
- **Option D is incorrect**: Heat does not convert electrons into protons.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-010",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.2.3",
    parentTopicCode: "MH-8-SCI-5-5.2",
    parentTopicName: "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
    subtopicCode: "MH-8-SCI-5-5.2.3",
    subtopicName: "Drawbacks of Rutherford model (stability of orbital electrons)",
    topicNumber: "5.2.3",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Louis de Broglie later (1924) explained Bohr's stable stationary orbits by introducing the wave nature of electrons. What wave condition guarantees that an electron orbit is completely stable without destructive interference?",
    options: [
      "The circumference of the circular orbit must be an integral multiple of the electron's de Broglie wavelength: \\(2\\pi r = n\\lambda\\)",
      "The orbital radius must be exactly equal to the wavelength of red light",
      "The frequency of the electron wave must match the cosmic microwave background",
      "The electron wave must undergo destructive interference at all points along the orbit"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1924, Louis de Broglie proposed that moving particles possess an associated matter wavelength:
\\[
\\lambda = \\frac{h}{p} = \\frac{h}{m_e v}
\\]
For an electron wave to be stable and avoid destroying itself through destructive interference around a closed circular path of radius \\(r\\), the path length (circumference) must accommodate an integer number of complete wavelengths, forming a **standing wave**:
\\[
2\\pi r = n\\lambda, \\quad n = 1, 2, 3, \\dots
\\]
Substituting \\(\\lambda = \\frac{h}{m_e v}\\):
\\[
2\\pi r = n \\left(\\frac{h}{m_e v}\\right) \\implies m_e v r = n \\frac{h}{2\\pi}
\\]
This elegantly derived Bohr's arbitrary angular momentum quantization postulate from fundamental standing wave mechanics!

### 2. Physical Context & Practical Illustration:
Just as a guitar string only vibrates stably at fundamental harmonics where nodes fit the string length, an electron wave can only exist stably in orbits that fit an integer number of matter wavelengths.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The standing wave condition \\(2\\pi r = n\\lambda\\) ensures non-destructive stability.
- **Option B is incorrect**: Electron de Broglie wavelengths are \\(\\approx 0.1\\text{ nm}\\), thousands of times smaller than red light (\\(700\\text{ nm}\\)).
- **Option C is incorrect**: Cosmic microwave radiation is irrelevant to atomic standing waves.
- **Option D is incorrect**: Destructive interference would annihilate the electron wave.`
  }
];

module.exports = { topic2Part2Questions };
