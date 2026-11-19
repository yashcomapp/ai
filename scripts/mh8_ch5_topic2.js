// scripts/mh8_ch5_topic2.js
// Topic 5.2: Rutherford Gold Foil Experiment & Nuclear Model of Atom
// Subtopics: 5.2.1, 5.2.2, 5.2.3
// Vaults: exam, practice, foundation

const topic2Questions = [
  // ==========================================
  // SUBTOPIC 5.2.1: Alpha particle scattering experiment
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-001",
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
    text: "In Rutherford's famous scattering experiment, which radioactive emission was used to bombard the thin gold foil?",
    options: [
      "Positively charged \\(\\alpha\\) (alpha) particles (Helium nuclei, \\(^4_2\\text{He}^{2+}\\))",
      "Negatively charged \\(\\beta\\) (beta) particles (high-speed electrons)",
      "Neutral \\(\\gamma\\) (gamma) radiation photons",
      "High-energy cathode ray beams"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1911, Ernest Rutherford bombarded an extremely thin sheet of gold foil with fast-moving \\(\\alpha\\)-particles (alpha particles) emitted by a radioactive source (such as Radium or Bismuth). An \\(\\alpha\\)-particle is a doubly ionized Helium nucleus:
\\[
\\alpha = ^4_2\\text{He}^{2+}
\\]
It has a mass of \\(4\\text{ u}\\) and carries a net positive charge of \\(+2e = +3.2 \\times 10^{-19}\\text{ C}\\).

### 2. Physical Context & Practical Illustration:
Because \\(\\alpha\\)-particles have significant mass (approx. 7300 times the mass of an electron) and considerable kinetic energy, Rutherford expected them to pass straight through if Thomson's plum pudding model (diffuse positive charge) were correct.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Doubly charged helium ions (\\(^4_2\\text{He}^{2+}\\)) were the exact projectile particles used.
- **Option B is incorrect**: Beta particles are high-speed electrons, which were discovered earlier by Thomson and Becquerel but not used as projectiles here.
- **Option C is incorrect**: Gamma rays are uncharged electromagnetic photons; they do not experience electrostatic repulsion.
- **Option D is incorrect**: Cathode rays are streams of electrons in discharge tubes, not alpha projectiles.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-002",
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
    text: "Why did Ernest Rutherford select a foil made specifically of gold (\\(\\text{Au}\\)) rather than any other metal for his scattering experiment?",
    options: [
      "Gold has exceptionally high malleability, allowing it to be hammered into sheets only about \\(10^{-7}\\text{ m}\\) (approx. 1000 atoms) thick",
      "Gold is a chemical insulator that prevents electrostatic charge buildup",
      "Gold atoms contain zero neutrons, preventing unwanted nuclear absorption",
      "Gold exhibits natural spontaneous radioactivity that boosts beam intensity"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
To observe the scattering caused by individual atomic interactions without multiple overlapping collisions, the metallic target needed to be as thin as physically possible:
\\[
\\text{Thickness of gold foil} \\approx 10^{-7}\\text{ m} = 100\\text{ nm} \\approx 1000\\text{ atomic layers}
\\]
Gold is the most malleable of all known metals, enabling the fabrication of foils of near-monoatomic thinness.

### 2. Physical Context & Practical Illustration:
If a thicker foil of less malleable metal (like copper or iron) were used, the alpha particles would undergo multiple consecutive scatterings, blurring the sharp trajectory data needed to deduce nuclear structure.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The supreme malleability of gold allowed hammered foils of thickness \\(\\approx 10^{-7}\\text{ m}\\).
- **Option B is incorrect**: Gold is an excellent electrical conductor, not an insulator.
- **Option C is incorrect**: Natural gold (\\(^{197}_{79}\\text{Au}\\)) has 118 neutrons; it is definitely not neutron-free.
- **Option D is incorrect**: Standard gold-197 is stable and non-radioactive.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-003",
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
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "During the gold foil experiment, what material was coated on the surrounding circular fluorescent screen to detect scattered \\(\\alpha\\)-particles by producing tiny flashes of light (scintillations)?",
    options: [
      "Zinc sulfide (\\(\\text{ZnS}\\))",
      "Lead oxide (\\(\\text{PbO}\\))",
      "Sodium chloride (\\(\\text{NaCl}\\))",
      "Barium sulfate (\\(\\text{BaSO}_4\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an energetic charged particle strikes a phosphorescent/scintillating screen coated with **Zinc Sulfide (\\(\\text{ZnS}\\))**, it excites the orbital electrons of the phosphor atoms. Upon de-excitation, visible photons of light (scintillations) are emitted:
\\[
\\alpha + \\text{ZnS} \\rightarrow \\text{ZnS}^* \\rightarrow \\text{ZnS} + h\\nu\\text{ (visible flash)}
\\]
These tiny flashes were observed and manually counted using a mobile microscope in a darkened room by Geiger and Marsden.

### 2. Physical Context & Practical Illustration:
Zinc sulfide acts as a sensitive microscopic detector screen. The circular arrangement allowed detection of particles scattered in any direction, from \\(0^\\circ\\) to \\(180^\\circ\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Zinc sulfide (\\(\\text{ZnS}\\)) is the canonical scintillating phosphor used in the experiment.
- **Option B is incorrect**: Lead oxide was used in protective shields to absorb radiation, not as a scintillator.
- **Option C is incorrect**: Sodium chloride does not produce visible scintillations upon alpha particle impact.
- **Option D is incorrect**: Barium sulfate is radiopaque (used in X-ray imaging), not a fluorescent scintillation screen.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-004",
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
    text: "Which primary experimental observation from the \\(\\alpha\\)-particle scattering experiment directly proved that most of the space inside an atom is completely empty?",
    options: [
      "An overwhelming majority of \\(\\alpha\\)-particles passed straight through the foil with zero or negligible deflection",
      "A small fraction of \\(\\alpha\\)-particles were deflected at angles greater than \\(90^\\circ\\)",
      "All \\(\\alpha\\)-particles were completely absorbed inside the gold lattice",
      "Electrons were knocked out of the gold atoms and collected as an electric current"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Rutherford's quantitative findings:
- Over \\(99.9\\%\\) of the incident \\(\\alpha\\)-particles passed directly through the gold foil without any deviation (deflection angle \\(\\theta \\approx 0^\\circ\\)).
If mass and positive charge were uniformly distributed throughout the atom (as proposed by J.J. Thomson), every particle would encounter uniform electric fields and suffer small, continuous deflections. The straight unhindered passage of the vast majority proved that there are no massive charged obstacles in most of the atomic volume:
\\[
\\text{Fraction undeflected} \\approx 1 \\implies \\text{Atomic interior is predominantly empty space}
\\]

### 2. Physical Context & Practical Illustration:
Imagine firing bullets into a dense forest. If 99.9% of bullets pass through without hitting anything, the trees must be tiny and spaced extremely far apart relative to the size of the forest.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The undeflected passage of almost all alpha particles proves empty internal atomic volume.
- **Option B is incorrect**: Large-angle deflection proved the existence of a concentrated positive nucleus, not empty space.
- **Option C is incorrect**: Particles were scattered, not completely absorbed.
- **Option D is incorrect**: Electron emission was not the measured phenomenon proving atomic void space.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.1-OSC-005",
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
    text: "Approximately what proportion of incident \\(\\alpha\\)-particles experienced rebound deflections of nearly \\(180^\\circ\\) (bouncing straight back toward the source), leading Rutherford to compare it to 'firing a 15-inch shell at tissue paper and having it bounce back'?",
    options: [
      "Approximately 1 in \\(20{,}000\\) particles (about \\(0.005\\%\\))",
      "Approximately 1 in 10 particles (about \\(10\\%\\))",
      "Approximately 1 in \\(200\\) particles (about \\(0.5\\%\\))",
      "Approximately 1 in \\(2{,}000{,}000\\) particles"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rutherford's quantitative scattering measurements revealed that large-angle rebound (\\(\\theta \\approx 180^\\circ\\)) is an exceptionally rare event:
\\[
\\frac{N(180^\\circ)}{N_{\\text{total}}} \\approx \\frac{1}{20{,}000} \\quad (\\text{or } 1 \\text{ in } 8{,}000 \\text{ to } 20{,}000)
\\]
For a heavy projectile like an \\(\\alpha\\)-particle (mass \\(4\\text{ u}\\), kinetic energy \\(\\approx 5\\text{ MeV}\\)) to be stopped and repelled backward along its path of incidence, it must experience a colossal repulsive Coulomb force from an extremely dense, concentrated positive core:
\\[
F_e = \\frac{1}{4\\pi \\varepsilon_0} \\frac{(2e)(Ze)}{r^2}
\\]

### 2. Physical Context & Practical Illustration:
Rutherford famously recorded: *"It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you."*

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The experimental ratio of direct back-scattering was approximately 1 in 20,000 (0.005%).
- **Option B is incorrect**: 1 in 10 would mean atoms are densely packed impenetrable solid spheres, which contradicts the 99.9% straight passage.
- **Option C is incorrect**: 1 in 200 is two orders of magnitude too frequent.
- **Option D is incorrect**: 1 in 2,000,000 is far too rare; it would have made Geiger and Marsden's visual scintillation counts statistically undetectable.`
  },

  // ==========================================
  // SUBTOPIC 5.2.2: Positively charged dense central nucleus, empty space around nucleus, planetary electrons
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-001",
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
    text: "According to Rutherford's nuclear model of the atom, where is almost the entire mass and positive charge of the atom concentrated?",
    options: [
      "In a tiny, extremely dense central region called the nucleus",
      "Uniformly spread across the outer spherical boundary of the atom",
      "Evenly distributed throughout the planetary electron orbits",
      "Divided equally between revolving electrons and outer boundary space"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rutherford formulated the **Nuclear Model of the Atom** (1911) with the following core postulate:
- There is a positively charged, extremely dense center in an atom called the **nucleus**.
- Nearly all the mass of the atom resides inside this nucleus:
\\[
M_{\\text{atom}} \\approx M_{\\text{nucleus}} \\quad (\\because m_e \\approx \\frac{1}{1837} m_p)
\\]

### 2. Physical Context & Practical Illustration:
The nucleus is so dense that if an atom were enlarged to the size of a full sports stadium, the nucleus at the center would be no larger than a tiny marble or cricket ball.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The nucleus is the dense central core carrying almost 100% of the mass and all positive charge.
- **Option B is incorrect**: This was J.J. Thomson's disproved model of diffuse charge.
- **Option C is incorrect**: Electrons have negligible mass (approx. 0.054% of an atom's mass).
- **Option D is incorrect**: The mass distribution is overwhelmingly concentrated in the center, not divided equally.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-002",
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
    text: "How does the physical radius of the atomic nucleus compare to the overall radius of the atom?",
    options: [
      "The radius of the nucleus (\\(\\approx 10^{-15}\\text{ m}\\)) is approximately \\(10^5\\) (100,000) times smaller than the radius of the atom (\\(\\approx 10^{-10}\\text{ m}\\))",
      "The radius of the nucleus is roughly half (\\(50\\%\\)) of the atomic radius",
      "The radius of the nucleus is equal to the radius of the atom",
      "The radius of the nucleus is \\(10^5\\) times larger than the atomic radius"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Experimental measurements establish:
- Typical radius of an atom: \\(R_{\\text{atom}} \\approx 10^{-10}\\text{ m} = 0.1\\text{ nm} = 1\\text{ Å}\\)
- Typical radius of a nucleus: \\(R_{\\text{nucleus}} \\approx 10^{-15}\\text{ m} = 1\\text{ fm}\\) (1 femtometre)
The dimensional ratio is:
\\[
\\frac{R_{\\text{atom}}}{R_{\\text{nucleus}}} = \\frac{10^{-10}\\text{ m}}{10^{-15}\\text{ m}} = 10^5 = 100{,}000
\\]
Consequently, the volume fraction occupied by the nucleus is:
\\[
\\frac{V_{\\text{nucleus}}}{V_{\\text{atom}}} = \\left(\\frac{R_{\\text{nucleus}}}{R_{\\text{atom}}}\\right)^3 = (10^{-5})^3 = 10^{-15}
\\]

### 2. Physical Context & Practical Illustration:
The volume occupied by the nucleus is only one-quadrillionth (\\(10^{-15}\\)) of the atom's total volume. The remaining \\(99.9999999999999\\%\\) of the atom is entirely unoccupied empty space.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The nuclear radius (\\(10^{-15}\\text{ m}\\)) is \\(10^5\\) times smaller than the atomic radius (\\(10^{-10}\\text{ m}\\)).
- **Option B is incorrect**: A 50% ratio would imply a massive core filling half the atom, which would have deflected half the alpha particles.
- **Option C is incorrect**: If equal, the atom would be a solid dense block of nuclear matter.
- **Option D is incorrect**: The nucleus is inside the atom; it cannot be larger than the atom.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-003",
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
    text: "In Rutherford's atomic model, what provides the necessary centripetal force to keep the negatively charged planetary electrons revolving around the positive nucleus?",
    options: [
      "The electrostatic Coulomb attraction between the positively charged nucleus and negative electrons",
      "Gravitational attraction between the masses of electrons and the nucleus",
      "Magnetic repulsion generated by nuclear spin",
      "Nuclear strong forces extending outside the nuclear boundary"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Rutherford's planetary model, an electron of mass \\(m_e\\) moving at tangential speed \\(v\\) in a circular orbit of radius \\(r\\) requires a centripetal force:
\\[
F_c = \\frac{m_e v^2}{r}
\\]
This mechanical centripetal force is provided solely by the electrostatic Coulomb attraction between the positively charged nucleus (\\(+Ze\\)) and the negatively charged electron (\\(-e\\)):
\\[
\\frac{m_e v^2}{r} = \\frac{1}{4\\pi\\varepsilon_0} \\frac{Z e^2}{r^2}
\\]

### 2. Physical Context & Practical Illustration:
This dynamical balance is analogous to the solar system, where gravitational pull between the massive Sun and revolving planets provides the centripetal force maintaining planetary orbits.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Electrostatic Coulomb force provides the required centripetal acceleration.
- **Option B is incorrect**: Gravitational force between subatomic particles is approximately \\(10^{39}\\) times weaker than electrostatic force and is completely negligible.
- **Option C is incorrect**: Magnetic spin forces do not provide orbital centripetal force.
- **Option D is incorrect**: Strong nuclear forces operate only within short ranges (\\(\\le 10^{-15}\\text{ m}\\)) inside the nucleus.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-004",
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
    text: "Why is an electrically neutral atom stable as a whole under Rutherford's model in terms of net charge?",
    options: [
      "The total positive charge of the central nucleus exactly equals the sum of the negative charges of all revolving electrons",
      "Neutrons in the nucleus neutralize the positive charge of protons inside the core",
      "Electrons lose their electrical charge when placed into high-speed orbital motion",
      "The empty space around the nucleus acts as an electrical insulator preventing charge leakage"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An atom is electrically neutral in its ground state because:
\\[
Q_{\\text{total}} = Q_{\\text{nucleus}} + Q_{\\text{electrons}} = (+Z e) + (-Z e) = 0
\\]
where \\(Z\\) is the atomic number (number of nuclear protons) and each electron carries an elementary charge \\(e = 1.602 \\times 10^{-19}\\text{ C}\\).

### 2. Physical Context & Practical Illustration:
Even though massive positive charge is packed inside the nucleus and negative charge resides in distant revolving electrons, the magnitudes are perfectly balanced, making the net atom neutral to outside detectors.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Net charge neutrality requires \\(Q_{\\text{nucleus}} = -Q_{\\text{electrons}}\\).
- **Option B is incorrect**: Neutrons have zero charge; they do not neutralize or cancel proton charge.
- **Option C is incorrect**: Electron charge is an intrinsic invariant property that never vanishes during motion.
- **Option D is incorrect**: Empty space has no charge-insulating property; fields propagate directly through vacuum.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.2-OSC-005",
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
    text: "At the distance of closest approach (\\(r_0\\)) for a head-on collision of an \\(\\alpha\\)-particle of kinetic energy \\(K\\) with a target nucleus of atomic number \\(Z\\), what fundamental conservation principle dictates the value of \\(r_0\\)?",
    options: [
      "Initial kinetic energy of the \\(\\alpha\\)-particle is completely converted into electrostatic potential energy: \\(K = \\frac{1}{4\\pi\\varepsilon_0}\\frac{2Ze^2}{r_0}\\)",
      "Nuclear binding energy is completely converted into electromagnetic gamma rays",
      "Total linear momentum is annihilated to zero with zero potential energy storage",
      "The \\(\\alpha\\)-particle transfers its mass directly into kinetic energy of revolving electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a direct head-on collision (scattering angle \\(\\theta = 180^\\circ\\)), the incoming \\(\\alpha\\)-particle (charge \\(q_1 = +2e\\)) approaches the gold nucleus (charge \\(q_2 = +Ze\\)). As it moves against the repulsive Coulomb field, its kinetic energy decreases until it momentarily comes to rest at the distance of closest approach \\(r_0\\):
\\[
K_i + U_i = K_f + U_f
\\]
At infinity, \\(U_i = 0\\). At closest approach, \\(K_f = 0\\) and:
\\[
K = \\frac{1}{4\\pi\\varepsilon_0} \\frac{(2e)(Ze)}{r_0} \\implies r_0 = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 K}
\\]
This calculation allowed Rutherford to place an upper experimental bound on the size of the atomic nucleus (\\(r_0 \\approx 10^{-14}\\text{ m}\\)).

### 2. Physical Context & Practical Illustration:
The \\(\\alpha\\)-particle does not physically touch the gold nucleus; it is turned around purely by the immense electrostatic repulsion before contact.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Complete conversion of initial \\(K\\) into electrostatic potential energy \\(U = \\frac{2Ze^2}{4\\pi\\varepsilon_0 r_0}\\) governs closest approach.
- **Option B is incorrect**: No nuclear binding reactions or gamma emissions occur at these Rutherford energy levels.
- **Option C is incorrect**: Linear momentum reverses; it is conserved by the motion of the recoil nucleus.
- **Option D is incorrect**: Mass is conserved; no mass-energy annihilation takes place.`
  },

  // ==========================================
  // SUBTOPIC 5.2.3: Drawbacks of Rutherford model (stability of orbital electrons)
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-001",
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
    text: "What is the most critical scientific drawback of Rutherford's nuclear model of the atom?",
    options: [
      "It could not explain the mechanical stability of the atom according to classical electromagnetic theory",
      "It predicted that the nucleus must have a net negative charge",
      "It failed to predict that electrons are much lighter than alpha particles",
      "It claimed that atoms cannot form chemical bonds with other atoms"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to James Clerk Maxwell's well-established classical electrodynamics, any accelerated charged particle must continuously radiate energy in the form of electromagnetic waves:
\\[
P = \\frac{e^2 a^2}{6\\pi\\varepsilon_0 c^3} > 0
\\]
An electron revolving in a circular orbit constantly experiences centripetal acceleration \\(a = \\frac{v^2}{r}\\). Thus, it should continuously radiate energy, lose orbital kinetic energy, spiral inward, and crash into the nucleus in less than \\(10^{-8}\\text{ s}\\). Since real atoms are stable and do not collapse, Rutherford's model had a fundamental defect.

### 2. Physical Context & Practical Illustration:
If classical physics applied to planetary electrons without restriction, matter itself could not exist for more than a few nanoseconds; every atom in the universe would collapse into its nucleus.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The inability to explain atomic stability against radiative electromagnetic collapse was the fatal limitation.
- **Option B is incorrect**: Rutherford correctly proved the nucleus is positively charged.
- **Option C is incorrect**: Rutherford knew electrons are thousands of times lighter than alpha particles.
- **Option D is incorrect**: Rutherford did not postulate rules on chemical bonding.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-002",
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
    text: "Under classical electrodynamics, an accelerating electron revolving around the nucleus would radiate energy continuously. What type of emission spectrum did Rutherford's model incorrectly imply for atoms?",
    options: [
      "A continuous spectrum of all emitted frequencies rather than the observed sharp, discrete line spectrum",
      "A dark absorption band spectrum only in the infrared region",
      "Zero emission of radiation under any thermal conditions",
      "Only a single monochromatic spectral line at one fixed wavelength"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
As a revolving electron continuously radiates energy, its orbital radius \\(r\\) steadily contracts, and its orbital frequency:
\\[
f_{\\text{orb}} = \\frac{v}{2\\pi r}
\\]
must change continuously. Consequently, the emitted electromagnetic waves should span a continuous spectrum across all frequencies.
However, real experimental spectroscopy reveals that isolated gaseous atoms (like Hydrogen) emit **sharp, discrete line spectra** with exact characteristic wavelengths. Rutherford's model could not explain this discrete quantization.

### 2. Physical Context & Practical Illustration:
Atomic line spectra act like unique barcodes or fingerprints for chemical elements. Rutherford's classical model could only predict a continuous rainbow smear, failing to explain these distinct spectral barcodes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Rutherford's model implied a continuous spectrum, contradicting the observed discrete line spectra.
- **Option B is incorrect**: Gaseous discharge tubes emit bright emission lines, not purely infrared absorption bands.
- **Option C is incorrect**: Classical theory predicted intense continuous radiation, not zero radiation.
- **Option D is incorrect**: A single monochromatic line would require a fixed unchanging orbit, which classical accelerating charges cannot maintain.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-003",
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
    text: "According to classical calculations, what is the approximate theoretical collapse time for an electron in a hydrogen atom to spiral into the nucleus under Rutherford's model?",
    options: [
      "Approximately \\(10^{-8}\\text{ s}\\) to \\(10^{-11}\\text{ s}\\)",
      "Approximately 1 hour",
      "Approximately 24 hours",
      "Approximately \\(10^{10}\\text{ years}\\) (age of universe)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By integrating Larmor's radiation formula for an electron of mass \\(m_e\\) spiraling from Bohr radius \\(r_0 \\approx 0.53 \\times 10^{-10}\\text{ m}\\) to \\(r = 0\\):
\\[
\\tau = \\int_0^{r_0} \\frac{dr}{|dr/dt|} = \\frac{m_e^2 c^3 r_0^3}{4 e^4 \\left(\\frac{1}{4\\pi\\varepsilon_0}\\right)^3} \\approx 10^{-11}\\text{ s} \\text{ to } 10^{-8}\\text{ s}
\\]
This means the atom should collapse almost instantaneously. Since atoms have been stable for billions of years, classical mechanics completely fails at the subatomic scale.

### 2. Physical Context & Practical Illustration:
This glaring paradox between theoretical instant collapse (\\(\\approx 10^{-11}\\text{ s}\\)) and observed eternal stability proved that new physical principles (quantum mechanics) were urgently required.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The calculated spiral collapse time is extremely rapid, between \\(10^{-11}\\text{ s}\\) and \\(10^{-8}\\text{ s}\\).
- **Option B is incorrect**: 1 hour is trillions of times longer than the classical electrodynamic spiral time.
- **Option C is incorrect**: 24 hours represents a macroscopic terrestrial timescale with no subatomic validity.
- **Option D is incorrect**: \\(10^{10}\\text{ years}\\) is the actual stability timescale of real atoms, which Rutherford's classical model utterly failed to explain.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-004",
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
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Besides the problem of atomic stability, what other major structural detail did Rutherford's model leave completely undefined?",
    options: [
      "The specific electronic configuration, shell arrangements, and distribution of energies of electrons around the nucleus",
      "The location and positive sign of the atomic nucleus",
      "The fact that matter is composed of elements and compounds",
      "The approximate mass difference between atoms of different elements"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rutherford stated that electrons revolve around the nucleus like planets around the Sun, but he provided no rules or principles regarding:
1. Which orbital radii or energy levels electrons can occupy.
2. How many electrons can occupy a particular region.
3. How electrons are distributed among different energy levels or shells.
This complete absence of an **electronic configuration** framework made it impossible to explain chemical periodicity and valence behavior.

### 2. Physical Context & Practical Illustration:
Rutherford gave us the nuclear 'planetary' architecture, but he could not provide the 'orbital flight paths' or rules governing where electrons actually live.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The model said nothing about electron distribution, orbital quantization, or electronic configuration.
- **Option B is incorrect**: Rutherford explicitly discovered and located the positive nucleus.
- **Option C is incorrect**: Dalton and Lavoisier had already established elements and compounds a century earlier.
- **Option D is incorrect**: Atomic weights were already well cataloged by Mendeleev and others.`
  },
  {
    questionCode: "MH-8-SCI-5-5.2.3-OSC-005",
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
    text: "Which historical scientific breakthrough successfully resolved the primary drawback of Rutherford's model regarding electron radiation and atomic collapse?",
    options: [
      "Niels Bohr's quantum postulate (1913) of discrete non-radiating stationary orbits where orbital angular momentum is quantized: \\(L = mvr = \\frac{nh}{2\\pi}\\)",
      "Isaac Newton's formulation of universal gravitation applied to subatomic particles",
      "J.J. Thomson's discovery of isotopes using positive ray parabolas",
      "Avogadro's molecular hypothesis stating equal volumes of gases contain equal molecules"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, Danish physicist Niels Bohr rescued Rutherford's model by combining it with Max Planck's quantum theory:
1. Electrons revolve only in certain allowed, non-radiating circular orbits called **stationary states**. While in these stationary orbits, electrons do not radiate electromagnetic energy despite centripetal acceleration.
2. The allowed orbits are those where the orbital angular momentum \\(L\\) is an integral multiple of \\(\\frac{h}{2\\pi}\\):
\\[
L = m_e v r = n \\frac{h}{2\\pi}, \\quad n = 1, 2, 3, \\dots
\\]
where \\(h\\) is Planck's constant (\\(6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\)).

### 2. Physical Context & Practical Illustration:
Bohr postulated that nature forbids electrons from spiraling into the nucleus: the ground state (\\(n=1\\)) represents the lowest possible stable energy floor.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Bohr's quantized stationary orbits resolved the radiation collapse paradox.
- **Option B is incorrect**: Classical Newtonian gravity cannot explain quantum stability or electromagnetic radiation.
- **Option C is incorrect**: Thomson's isotope discovery dealt with atomic mass variations, not orbital dynamics.
- **Option D is incorrect**: Avogadro's hypothesis relates gas volumes and mole numbers, not electron orbital mechanics.`
  }
];

module.exports = { topic2Questions };
