// scripts/mh8_ch5_topic5.js
// Topic 5.5: Atomic Number (Z), Mass Number (A) & Electronic Configuration
// Subtopics: 5.5.1, 5.5.2, 5.5.3, 5.5.4
// Vaults: exam, practice, foundation

const topic5Questions = [
  // ==========================================
  // SUBTOPIC 5.5.1: Atomic number Z = number of protons = number of electrons
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.1",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.1",
    subtopicName: "Atomic number Z = number of protons = number of electrons",
    topicNumber: "5.5.1",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "The atomic number (\\(Z\\)) of a neutral chemical element is defined as the total number of:",
    options: [
      "Protons present in the atomic nucleus (which equals the number of extranuclear electrons in a neutral atom)",
      "Neutrons present inside the nucleus",
      "Protons plus neutrons combined in the nucleus",
      "Electrons located exclusively in the outermost valence shell"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Atomic Number (\\(Z\\))** is the fundamental defining identity of a chemical element:
\\[
Z = \\text{Number of protons in the nucleus}
\\]
For any electrically neutral atom:
\\[
\\text{Number of electrons} = \\text{Number of protons} = Z
\\]
If an atom gains or loses electrons, it becomes an ion, but its atomic number \\(Z\\) remains strictly constant because the number of protons does not change.

### 2. Physical Context & Practical Illustration:
Moseley's X-ray law (1913) proved that the periodic table is ordered by atomic number \\(Z\\), not atomic mass. Carbon is Carbon because \\(Z = 6\\); change \\(Z\\) to 7, and it is Nitrogen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(Z\\) is the number of nuclear protons, which equals extranuclear electrons in a neutral atom.
- **Option B is incorrect**: Neutron count is \\(N = A - Z\\), not \\(Z\\).
- **Option C is incorrect**: Protons plus neutrons is the mass number \\(A\\).
- **Option D is incorrect**: Outermost electrons are valence electrons, not the atomic number.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.1",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.1",
    subtopicName: "Atomic number Z = number of protons = number of electrons",
    topicNumber: "5.5.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "A divalent cation \\(\\text{Mg}^{2+}\\) has an atomic number of \\(Z = 12\\). How many protons and electrons does this ion contain?",
    options: [
      "12 protons and 10 electrons",
      "12 protons and 12 electrons",
      "10 protons and 12 electrons",
      "14 protons and 12 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Protons**: The atomic number \\(Z = 12\\) dictates the number of protons:
\\[
\\text{Number of protons} = Z = 12
\\]
Proton count never changes during chemical ionization.
2. **Electrons**: A neutral Magnesium atom has 12 electrons. Forming the divalent cation \\(\\text{Mg}^{2+}\\) requires the loss of 2 valence electrons:
\\[
\\text{Number of electrons} = Z - (\\text{positive charge}) = 12 - 2 = 10
\\]
Net charge:
\\[
(+12) + (-10) = +2
\\]

### 2. Physical Context & Practical Illustration:
By losing 2 electrons, \\(\\text{Mg}^{2+}\\) achieves the stable, inert electronic configuration of Neon (2, 8).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: 12 protons in the nucleus and 10 electrons in shells.
- **Option B is incorrect**: 12 electrons would be a neutral atom, not a \\(\\text{Mg}^{2+}\\) cation.
- **Option C is incorrect**: Protons are in the nucleus; forming a positive ion does NOT remove nuclear protons.
- **Option D is incorrect**: Protons cannot be added to form a cation.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.1",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.1",
    subtopicName: "Atomic number Z = number of protons = number of electrons",
    topicNumber: "5.5.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "A nitride ion \\(\\text{N}^{3-}\\) is formed from a nitrogen atom (\\(Z = 7\\)). How many total electrons are present in this ion?",
    options: [
      "10 electrons",
      "7 electrons",
      "4 electrons",
      "14 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For any anion with charge \\(-n\\):
\\[
\\text{Number of electrons} = Z + n
\\]
For Nitrogen (\\(Z = 7\\)) gaining 3 electrons to form nitride \\(\\text{N}^{3-}\\):
\\[
\\text{Number of electrons} = 7 + 3 = 10
\\]
Total protons = \\(7\\), Total electrons = \\(10\\).
Net charge = \\(+7 + (-10) = -3\\).

### 2. Physical Context & Practical Illustration:
Nitride \\(\\text{N}^{3-}\\), Oxide \\(\\text{O}^{2-}\\), Fluoride \\(\\text{F}^-\\), and Neon (Ne) all possess 10 electrons; they form an **isoelectronic series**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(7 + 3 = 10\\) electrons.
- **Option B is incorrect**: 7 electrons is neutral atomic nitrogen.
- **Option C is incorrect**: \\(7 - 3 = 4\\) mistakenly subtracts electrons instead of adding them for a negative ion.
- **Option D is incorrect**: 14 is the mass number of nitrogen, not the electron count.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.1",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.1",
    subtopicName: "Atomic number Z = number of protons = number of electrons",
    topicNumber: "5.5.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Henry Moseley's historic X-ray emission experiments (1913) proved that the frequency (\\(\\nu\\)) of characteristic X-rays emitted by metallic targets follows which mathematical relationship with atomic number \\(Z\\)?",
    options: [
      "\\(\\sqrt{\\nu} = a(Z - b)\\), showing frequency is directly related to nuclear charge \\(Z\\)",
      "\\(\\nu = a Z^3\\), showing frequency depends on nuclear volume",
      "\\(\\nu^2 = a (A - Z)\\), showing frequency depends on neutron excess",
      "\\(\\frac{1}{\\nu} = a Z\\), showing frequency decreases with atomic number"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, British physicist **Henry Moseley** bombarded different element targets with high-speed electrons and measured the frequencies of the resulting \\(K_\\alpha\\) characteristic X-rays.
He discovered **Moseley's Law**:
\\[
\\sqrt{\\nu} = a(Z - b)
\\]
where \\(a\\) and \\(b\\) are screening constants.
Plotting \\(\\sqrt{\\nu}\\) against atomic number \\(Z\\) yielded a flawless straight line, whereas plotting against atomic mass \\(A\\) gave irregular zig-zag lines.

### 2. Physical Context & Practical Illustration:
Moseley's law settled the fundamental basis of chemistry: the atomic number \\(Z\\) (number of nuclear protons), not atomic weight \\(A\\), governs chemical periodicity and element properties.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Moseley's law is \\(\\sqrt{\\nu} = a(Z - b)\\).
- **Option B is incorrect**: Frequency does not scale with \\(Z^3\\).
- **Option C is incorrect**: X-ray frequencies are independent of neutron count \\(A - Z\\).
- **Option D is incorrect**: Frequency increases monotonically with \\(Z\\), it does not decrease.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.1",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.1",
    subtopicName: "Atomic number Z = number of protons = number of electrons",
    topicNumber: "5.5.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Which of the following sets of chemical species constitutes a true isoelectronic series (identical total electron count)?",
    options: [
      "\\(\\text{N}^{3-}, \\text{O}^{2-}, \\text{F}^-, \\text{Ne}, \\text{Na}^+, \\text{Mg}^{2+}, \\text{Al}^{3+}\\) (all having 10 electrons)",
      "\\(\\text{H}^+, \\text{He}, \\text{Li}^+, \\text{Be}^{2+}, \\text{B}^{3+}\\) (all having 3 electrons)",
      "\\(\\text{Cl}^-, \\text{Ar}, \\text{K}^+, \\text{Ca}^{2+}, \\text{Sc}^{3+}\\) (all having 10 electrons)",
      "\\(\\text{Fe}^{2+}, \\text{Fe}^{3+}, \\text{Mn}^{2+}, \\text{Cr}^{3+}\\) (all having 26 electrons)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Isoelectronic species** are atoms, molecules, or ions that contain exactly the same number of electrons.
Let us evaluate each member of set A:
- \\(\\text{N}^{3-}\\): \\(Z = 7 \\implies 7 + 3 = 10\\text{ electrons}\\)
- \\(\\text{O}^{2-}\\): \\(Z = 8 \\implies 8 + 2 = 10\\text{ electrons}\\)
- \\(\\text{F}^-\\): \\(Z = 9 \\implies 9 + 1 = 10\\text{ electrons}\\)
- \\(\\text{Ne}\\): \\(Z = 10 \\implies 10\\text{ electrons}\\)
- \\(\\text{Na}^+\\): \\(Z = 11 \\implies 11 - 1 = 10\\text{ electrons}\\)
- \\(\\text{Mg}^{2+}\\): \\(Z = 12 \\implies 12 - 2 = 10\\text{ electrons}\\)
- \\(\\text{Al}^{3+}\\): \\(Z = 13 \\implies 13 - 3 = 10\\text{ electrons}\\)
All species possess exactly 10 electrons and share the same electronic configuration \\(1s^2 2s^2 2p^6\\) (or 2, 8).

### 2. Physical Context & Practical Illustration:
As nuclear charge \\(Z\\) increases across an isoelectronic series from \\(N^{3-} (Z=7)\\) to \\(Al^{3+} (Z=13)\\), ionic radius decreases dramatically because 13 protons pull the same 10 electrons much closer than 7 protons can.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: All 7 species possess exactly 10 electrons.
- **Option B is incorrect**: \\(\\text{H}^+\\) has 0 electrons, \\(\\text{He}\\) has 2 electrons; they do not have 3 electrons.
- **Option C is incorrect**: \\(\\text{Cl}^-, \\text{Ar}, \\text{K}^+\\) have 18 electrons (Argon core), not 10.
- **Option D is incorrect**: \\(\\text{Fe}^{2+}\\) has 24 electrons, \\(\\text{Fe}^{3+}\\) has 23 electrons; they are not isoelectronic.`
  },

  // ==========================================
  // SUBTOPIC 5.5.2: Mass number A = protons + neutrons
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.2",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.2",
    subtopicName: "Mass number A = protons + neutrons",
    topicNumber: "5.5.2",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What does the mass number (\\(A\\)) of an atom represent?",
    options: [
      "The total sum of protons and neutrons (nucleons) present inside the nucleus",
      "The total number of electrons revolving around the nucleus",
      "The total mass of the atom measured in grams",
      "The difference between the number of neutrons and protons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Mass Number (\\(A\\))** is defined as the total integer count of nucleons (protons + neutrons) inside the atomic nucleus:
\\[
A = Z + N
\\]
where:
- \\(Z\\) = Number of protons (atomic number)
- \\(N\\) = Number of neutrons
Since electrons have negligible mass (\\(\\approx 1/1837\\text{ u}\\)), practically \\(99.95\\%\\) of atomic mass resides in these \\(A\\) nucleons.

### 2. Physical Context & Practical Illustration:
Mass number is always an integer (e.g. 12, 14, 23, 235), whereas atomic weight is a real fractional number due to isotope abundance averaging.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(A = \\text{protons} + \\text{neutrons}\\).
- **Option B is incorrect**: Electron count equals \\(Z\\) in neutral atoms, not \\(A\\).
- **Option C is incorrect**: \\(A\\) is a dimensionless count of nucleons, not a mass in grams.
- **Option D is incorrect**: Difference is the neutron excess \\(N - Z\\), not mass number.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.2",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.2",
    subtopicName: "Mass number A = protons + neutrons",
    topicNumber: "5.5.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "An atom of Sodium is represented symbolically as \\(^{23}_{11}\\text{Na}\\). How many protons, neutrons, and electrons does a neutral atom of this isotope possess?",
    options: [
      "11 protons, 12 neutrons, and 11 electrons",
      "11 protons, 23 neutrons, and 11 electrons",
      "12 protons, 11 neutrons, and 12 electrons",
      "23 protons, 11 neutrons, and 23 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In canonical nuclear notation \\(^A_Z\\text{X}\\):
- Subscript \\(Z = 11\\) (Atomic Number = number of protons)
- Superscript \\(A = 23\\) (Mass Number = protons + neutrons)
Calculations:
1. \\(\\text{Number of protons} = Z = 11\\)
2. \\(\\text{Number of electrons} = Z = 11\\) (neutral atom)
3. \\(\\text{Number of neutrons} = A - Z = 23 - 11 = 12\\)

### 2. Physical Context & Practical Illustration:
The sodium nucleus contains 11 positive protons and 12 neutral neutrons bound by strong nuclear forces, with 11 electrons distributed as 2, 8, 1 in the outer shells.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: 11 protons, \\(23 - 11 = 12\\) neutrons, 11 electrons.
- **Option B is incorrect**: 23 is the mass number \\(A\\), not the neutron count \\(N\\).
- **Option C is incorrect**: Inverts the proton and neutron counts.
- **Option D is incorrect**: Confuses mass number with atomic number.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.2",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.2",
    subtopicName: "Mass number A = protons + neutrons",
    topicNumber: "5.5.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "A nucleus of Uranium-238 (\\(^{238}_{92}\\text{U}\\)) undergoes nuclear decay. How many neutrons are packed inside this nucleus?",
    options: [
      "146 neutrons",
      "92 neutrons",
      "238 neutrons",
      "330 neutrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Using the standard formula:
\\[
N = A - Z
\\]
For \\(^{238}_{92}\\text{U}\\):
- Mass number \\(A = 238\\)
- Atomic number \\(Z = 92\\)
\\[
N = 238 - 92 = 146
\\]
There are 146 neutrons and 92 protons.

### 2. Physical Context & Practical Illustration:
In heavy nuclei like Uranium, the ratio of neutrons to protons is \\(N/Z = 146/92 \\approx 1.59\\). The extra neutrons are necessary to dilute proton-proton electrostatic repulsion and maintain nuclear cohesion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(238 - 92 = 146\\) neutrons.
- **Option B is incorrect**: 92 is the number of protons (atomic number \\(Z\\)).
- **Option C is incorrect**: 238 is the total nucleon mass number \\(A\\).
- **Option D is incorrect**: \\(238 + 92 = 330\\) mistakenly adds \\(A\\) and \\(Z\\).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.2",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.2",
    subtopicName: "Mass number A = protons + neutrons",
    topicNumber: "5.5.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Atoms of different chemical elements having the same mass number (\\(A\\)) but different atomic numbers (\\(Z\\)) are known as:",
    options: [
      "Isobars (e.g. \\(^{40}_{18}\\text{Ar}\\) and \\(^{40}_{20}\\text{Ca}\\))",
      "Isotopes (e.g. \\(^{12}_6\\text{C}\\) and \\(^{14}_6\\text{C}\\))",
      "Isotones (e.g. \\(^{14}_6\\text{C}\\) and \\(^{16}_8\\text{O}\\))",
      "Isomers (e.g. butane and isobutane)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Definitions of atomic relations:
1. **Isobars**: Same mass number \\(A\\), different atomic number \\(Z\\).
   - Example: \\(^{40}_{18}\\text{Ar}\\) (18 protons, 22 neutrons, \\(A=40\\)) and \\(^{40}_{20}\\text{Ca}\\) (20 protons, 20 neutrons, \\(A=40\\)).
   - Isobars belong to completely different chemical elements and have distinct chemical properties.
2. **Isotopes**: Same \\(Z\\), different \\(A\\).
3. **Isotones**: Same number of neutrons \\(N = A - Z\\).
4. **Isomers**: Same molecular formula, different structural connectivity.

### 2. Physical Context & Practical Illustration:
Argon is an inert noble gas, while Calcium is a reactive alkaline earth metal. Despite having identical nuclear masses (\\(A = 40\\)), their different proton counts give them completely unrelated chemistries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Isobars share the same \\(A\\) across different elements.
- **Option B is incorrect**: Isotopes share the same \\(Z\\) (same element).
- **Option C is incorrect**: Isotones share the same neutron count \\(N\\).
- **Option D is incorrect**: Isomers are organic chemical structural variants.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.2",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.2",
    subtopicName: "Mass number A = protons + neutrons",
    topicNumber: "5.5.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "An unknown neutral atom has 17 electrons. If its nucleus contains 18 neutrons, what is the canonical nuclear notation and mass number of this atom?",
    options: [
      "\\(^{35}_{17}\\text{Cl}\\) with a mass number of \\(A = 35\\)",
      "\\(^{18}_{17}\\text{Cl}\\) with a mass number of \\(A = 18\\)",
      "\\(^{35}_{18}\\text{Ar}\\) with a mass number of \\(A = 35\\)",
      "\\(^{17}_{35}\\text{Cl}\\) with a mass number of \\(A = 17\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. In a neutral atom:
\\[
\\text{Number of protons } Z = \\text{Number of electrons} = 17
\\]
Element with \\(Z = 17\\) is Chlorine (\\(\\text{Cl}\\)).
2. Given number of neutrons:
\\[
N = 18
\\]
3. Mass number \\(A\\):
\\[
A = Z + N = 17 + 18 = 35
\\]
4. Standard nuclear symbol representation:
\\[
^A_Z\\text{X} = ^{35}_{17}\\text{Cl}
\\]

### 2. Physical Context & Practical Illustration:
Chlorine-35 makes up about \\(76\\%\\) of all natural chlorine on Earth, with the remaining \\(24\\%\\) being Chlorine-37 (17 protons, 20 neutrons).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(^{35}_{17}\\text{Cl}\\) with \\(A = 17 + 18 = 35\\).
- **Option B is incorrect**: 18 is the neutron count, not the mass number.
- **Option C is incorrect**: \\(Z = 17\\) is Chlorine, not Argon (\\(Z = 18\\)).
- **Option D is incorrect**: Inverts the position of superscript \\(A\\) and subscript \\(Z\\).`
  },

  // ==========================================
  // SUBTOPIC 5.5.3: Shell capacity formula 2n² (K=2, L=8, M=18, N=32)
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.3",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.3",
    subtopicName: "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
    topicNumber: "5.5.3",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What mathematical formula dictates the maximum electron-holding capacity of an electron shell having principal quantum number \\(n\\)?",
    options: [
      "\\(2n^2\\)",
      "\\(n^2\\)",
      "\\(2n\\)",
      "\\(2(2l + 1)\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to the **Bohr-Bury scheme** (1921), the maximum number of electrons that can be accommodated in any principal shell with quantum number \\(n\\) is given by:
\\[
\\text{Max Capacity} = 2n^2
\\]
Derivation from quantum mechanics:
- Each shell \\(n\\) contains \\(n^2\\) spatial atomic orbitals.
- By Pauli's Exclusion Principle, each orbital can hold a maximum of 2 electrons with opposite spins (\\(+\\frac{1}{2}, -\\frac{1}{2}\\)).
\\[
\\text{Total electrons} = 2 \\times n^2 = 2n^2
\\]

### 2. Physical Context & Practical Illustration:
This fundamental rule determines the maximum population of all atomic shells: K holds 2, L holds 8, M holds 18, and N holds 32.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(2n^2\\) is the canonical shell capacity formula.
- **Option B is incorrect**: \\(n^2\\) gives the number of orbitals, not the number of electrons.
- **Option C is incorrect**: \\(2n\\) fails for \\(n \\ge 2\\) (gives 4 for L shell instead of 8).
- **Option D is incorrect**: \\(2(2l + 1)\\) is the subshell capacity formula for orbital quantum number \\(l\\).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.3",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.3",
    subtopicName: "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
    topicNumber: "5.5.3",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What are the maximum electron capacities for the first four principal shells K (\\(n=1\\)), L (\\(n=2\\)), M (\\(n=3\\)), and N (\\(n=4\\))?",
    options: [
      "K = 2, L = 8, M = 18, N = 32",
      "K = 2, L = 4, M = 6, N = 8",
      "K = 2, L = 8, M = 8, N = 18",
      "K = 1, L = 4, M = 9, N = 16"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Applying the \\(2n^2\\) formula:
- **K shell** (\\(n = 1\\)): \\(2(1)^2 = 2 \\times 1 = 2\\)
- **L shell** (\\(n = 2\\)): \\(2(2)^2 = 2 \\times 4 = 8\\)
- **M shell** (\\(n = 3\\)): \\(2(3)^2 = 2 \\times 9 = 18\\)
- **N shell** (\\(n = 4\\)): \\(2(4)^2 = 2 \\times 16 = 32\\)

### 2. Physical Context & Practical Illustration:
Even though the M shell has a theoretical capacity of 18, the octet rule dictates that when M is the outermost valence shell, it cannot hold more than 8 electrons before the N shell begins filling.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: 2, 8, 18, 32 strictly follow \\(2n^2\\).
- **Option B is incorrect**: Linear sequence with step size 2 is erroneous.
- **Option C is incorrect**: 2, 8, 8, 18 reflects the valence filling sequence (Aufbau), not theoretical maximum capacities.
- **Option D is incorrect**: 1, 4, 9, 16 gives \\(n^2\\) (orbital counts), forgetting the factor of 2 for spin pairs.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.3",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.3",
    subtopicName: "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
    topicNumber: "5.5.3",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "According to the Bohr-Bury rules, what is the maximum number of electrons that can be accommodated in the outermost (valence) shell of any atom, regardless of the shell's theoretical \\(2n^2\\) capacity?",
    options: [
      "8 electrons (Octet Rule)",
      "18 electrons",
      "32 electrons",
      "2 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The second rule of the **Bohr-Bury scheme** states:
*The outermost shell of an atom cannot accommodate more than **8 electrons**, even if it has the capacity to hold more electrons according to the \\(2n^2\\) rule.*
(The only exception is the K shell, where the maximum capacity is 2 electrons, known as a duplet).

### 2. Physical Context & Practical Illustration:
For example, for Potassium (\\(Z = 19\\)):
- K shell holds 2
- L shell holds 8
- M shell receives 8 (making 18 electrons total)
Even though M can hold 18, the 19th electron goes into the N shell: \\(2, 8, 8, 1\\) (NOT \\(2, 8, 9\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The outermost valence shell can hold at most 8 electrons (octet rule).
- **Option B is incorrect**: 18 is the maximum capacity of an *inner* M shell, not an outermost valence shell.
- **Option C is incorrect**: 32 applies only to an inner N shell.
- **Option D is incorrect**: 2 is the limit only for the K shell (duplet rule for H and He).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.3",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.3",
    subtopicName: "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
    topicNumber: "5.5.3",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What is the correct step-wise electronic configuration of Calcium (\\(Z = 20\\)) across the K, L, M, and N shells?",
    options: [
      "2, 8, 8, 2",
      "2, 8, 10, 0",
      "2, 10, 8, 0",
      "2, 8, 9, 1"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For Calcium (\\(Z = 20\\)):
1. K shell (\\(n=1\\)): Fills with \\(2\\) electrons. (Remaining: 18)
2. L shell (\\(n=2\\)): Fills with \\(8\\) electrons. (Remaining: 10)
3. M shell (\\(n=3\\)): Although its total capacity is 18, it cannot hold more than 8 if it is outermost. Therefore, it takes \\(8\\) electrons. (Remaining: 2)
4. N shell (\\(n=4\\)): Takes the remaining \\(2\\) electrons.
Configuration:
\\[
\\text{K} = 2, \\quad \\text{L} = 8, \\quad \\text{M} = 8, \\quad \\text{N} = 2 \\implies (2, 8, 8, 2)
\\]

### 2. Physical Context & Practical Illustration:
In orbital notation, this corresponds to \\(1s^2 2s^2 2p^6 3s^2 3p^6 4s^2\\). The \\(4s\\) subshell has lower energy than the \\(3d\\) subshell, so it fills first.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(2, 8, 8, 2\\) satisfies both Bohr-Bury and Aufbau principles.
- **Option B is incorrect**: \\(2, 8, 10\\) violates the rule that an outermost shell cannot hold more than 8 electrons.
- **Option C is incorrect**: L shell can strictly hold a maximum of \\(2(2)^2 = 8\\) electrons, never 10.
- **Option D is incorrect**: \\(2, 8, 9, 1\\) violates the octet threshold before starting the next shell.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.3",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.3",
    subtopicName: "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
    topicNumber: "5.5.3",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Theoretically, what would be the maximum electron capacity of the hypothetical 5th principal shell (O shell, \\(n = 5\\)) if it were completely filled?",
    options: [
      "50 electrons",
      "32 electrons",
      "25 electrons",
      "72 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Applying the general capacity formula:
\\[
N_{\\text{max}} = 2n^2
\\]
For the 5th shell (O shell, \\(n = 5\\)):
\\[
N_{\\text{max}} = 2 \\times (5)^2 = 2 \\times 25 = 50\\text{ electrons}
\\]
Orbital breakdown:
- \\(s\\) subshell (\\(l = 0\\)): 1 orbital = 2 electrons
- \\(p\\) subshell (\\(l = 1\\)): 3 orbitals = 6 electrons
- \\(d\\) subshell (\\(l = 2\\)): 5 orbitals = 10 electrons
- \\(f\\) subshell (\\(l = 3\\)): 7 orbitals = 14 electrons
- \\(g\\) subshell (\\(l = 4\\)): 9 orbitals = 18 electrons
Total = \\(2 + 6 + 10 + 14 + 18 = 50\\) electrons.

### 2. Physical Context & Practical Illustration:
Although no known element in the ground state currently populates all 50 slots of the 5th shell, the quantum mechanical upper bound remains strictly 50.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(2 \\times 5^2 = 50\\) electrons.
- **Option B is incorrect**: 32 is the capacity of the \\(n=4\\) (N shell).
- **Option C is incorrect**: 25 is \\(n^2\\) (orbital count), forgetting electron spin pairing.
- **Option D is incorrect**: 72 corresponds to \\(n = 6\\) (\\(2 \\times 6^2 = 72\\)).`
  },

  // ==========================================
  // SUBTOPIC 5.5.4: Valence electrons and valency determination
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.4",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.4",
    subtopicName: "Valence electrons and valency determination",
    topicNumber: "5.5.4",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What are valence electrons?",
    options: [
      "Electrons present in the outermost shell of an atom",
      "Electrons located tightly inside the innermost K shell",
      "Electrons that have been permanently knocked out of an atom",
      "Neutrons that have acquired a negative charge"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Valence electrons** are the electrons occupying the outermost energy level (valence shell) of an atom.
These electrons determine the chemical reactivity, bonding capability, oxidation states, and valency of the element.
Inner shell electrons are shielded core electrons that do not participate in ordinary chemical reactions.

### 2. Physical Context & Practical Illustration:
For example, Carbon has 6 electrons arranged as (2, 4). The 4 electrons in the L shell are its valence electrons, allowing it to form 4 covalent bonds in organic molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Valence electrons are by definition the outermost shell electrons.
- **Option B is incorrect**: Innermost K shell electrons are core electrons.
- **Option C is incorrect**: Ejected electrons are free electrons or photoelectrons.
- **Option D is incorrect**: Neutrons never turn into valence electrons.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.4",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.4",
    subtopicName: "Valence electrons and valency determination",
    topicNumber: "5.5.4",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "An element has an atomic number of \\(Z = 16\\) (Sulfur). How many valence electrons does it possess, and what is its combining capacity (valency) in forming hydrogen sulfide (\\(\\text{H}_2\\text{S}\\))?",
    options: [
      "6 valence electrons and a valency of 2",
      "6 valence electrons and a valency of 6",
      "4 valence electrons and a valency of 4",
      "2 valence electrons and a valency of 6"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Electronic configuration of Sulfur (\\(Z = 16\\))**:
\\[
\\text{K} = 2, \\quad \\text{L} = 8, \\quad \\text{M} = 6 \\implies (2, 8, 6)
\\]
Number of valence electrons \\(V_e = 6\\).
2. **Valency determination**:
When the number of valence electrons is greater than 4:
\\[
\\text{Valency} = 8 - V_e = 8 - 6 = 2
\\]
Sulfur requires 2 additional electrons to complete its stable octet (8), so its primary valency is 2.

### 2. Physical Context & Practical Illustration:
Sulfur shares 1 electron with each of two Hydrogen atoms to form \\(\\text{H}_2\\text{S}\\), satisfying its valency of 2.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: 6 valence electrons, valency \\(= 8 - 6 = 2\\).
- **Option B is incorrect**: Confuses valence electron count (6) with valency (combining capacity = 2).
- **Option C is incorrect**: Sulfur has 6 valence electrons, not 4.
- **Option D is incorrect**: Reverses the values.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.4",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.4",
    subtopicName: "Valence electrons and valency determination",
    topicNumber: "5.5.4",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why do noble gases (such as Helium, Neon, and Argon) have a chemical valency of zero?",
    options: [
      "Their outermost shells are completely filled (duplet for He, octet for Ne and Ar), giving them maximum electronic stability with zero tendency to lose, gain, or share electrons",
      "Their atomic nuclei contain zero protons to attract chemical bonds",
      "They have negative atomic mass numbers that repel other elements",
      "Their electrons move too rapidly to allow chemical collisions"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The electronic configurations of noble gases:
- **Helium (\\(Z = 2\\))**: \\(2\\) (completely filled K shell duplet)
- **Neon (\\(Z = 10\\))**: \\(2, 8\\) (completely filled L shell octet)
- **Argon (\\(Z = 18\\))**: \\(2, 8, 8\\) (stable octet in M shell)
Because their outermost shells are completely filled with stable closed-shell configurations:
\\[
\\text{Valency} = 8 - 8 = 0
\\]
They have neither the tendency to gain nor lose electrons under standard conditions, resulting in a valency of zero.

### 2. Physical Context & Practical Illustration:
Noble gases exist naturally as monoatomic gases (He, Ne, Ar, Kr, Xe) and do not readily react with other elements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Complete duplet/octet stability results in zero chemical combining capacity.
- **Option B is incorrect**: Noble gases have standard positive nuclear charges (\\(Z = 2, 10, 18\\dots\\)).
- **Option C is incorrect**: Mass numbers are positive integers.
- **Option D is incorrect**: Kinetic speed is governed by temperature, not zero valency.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.4",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.4",
    subtopicName: "Valence electrons and valency determination",
    topicNumber: "5.5.4",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Element \\(\\text{X}\\) has atomic number 13 (Aluminium) and element \\(\\text{Y}\\) has atomic number 8 (Oxygen). Based on their valencies, what is the chemical formula of the compound formed between \\(\\text{X}\\) and \\(\\text{Y}\\)?",
    options: [
      "\\(\\text{X}_2\\text{Y}_3\\)",
      "\\(\\text{XY}\\)",
      "\\(\\text{X}_3\\text{Y}_2\\)",
      "\\(\\text{XY}_2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Element \\(\\text{X}\\) (\\(Z = 13\\))**:
   - Configuration: \\(2, 8, 3\\)
   - Valence electrons = \\(3\\) (\\(\\le 4\\))
   - \\(\\text{Valency of X} = 3\\)
2. **Element \\(\\text{Y}\\) (\\(Z = 8\\))**:
   - Configuration: \\(2, 6\\)
   - Valence electrons = \\(6\\) (\\(> 4\\))
   - \\(\\text{Valency of Y} = 8 - 6 = 2\\)
3. **Criss-Cross Formula Method**:
   - Symbol: \\(\\text{X} \\quad \\text{Y}\\)
   - Valency: \\(3 \\quad 2\\)
   - Criss-crossing the valencies yields the empirical formula:
\\[
\\text{Formula} = \\text{X}_2\\text{Y}_3 \\quad (\\text{representing } \\text{Al}_2\\text{O}_3)
\\]

### 2. Physical Context & Practical Illustration:
Two Aluminium atoms donate a total of \\(2 \\times 3 = 6\\) electrons, which are accepted by three Oxygen atoms (\\(3 \\times 2 = 6\\) electrons), forming stable ionic Aluminium Oxide (\\(\\text{Al}_2\\text{O}_3\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\text{X}_2\\text{Y}_3\\) is obtained by criss-crossing valencies 3 and 2.
- **Option B is incorrect**: \\(\\text{XY}\\) would require identical 1:1 valencies.
- **Option C is incorrect**: Inverts the subscripts.
- **Option D is incorrect**: \\(\\text{XY}_2\\) would correspond to a tetravalent metal.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.5.4",
    parentTopicCode: "MH-8-SCI-5-5.5",
    parentTopicName: "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
    subtopicCode: "MH-8-SCI-5-5.5.4",
    subtopicName: "Valence electrons and valency determination",
    topicNumber: "5.5.4",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Certain elements (such as Iron, Copper, and Lead) exhibit 'variable valency'. What fundamental subatomic phenomenon explains why transition elements can exhibit more than one valency?",
    options: [
      "Electrons from both the outermost shell and the penultimate (inner \\(d\\) or \\(s\\)) shell have comparable energy levels and can participate in bond formation under different conditions",
      "The atomic nucleus spontaneously changes its number of protons during chemical reactions",
      "Neutrons in the nucleus transform intermittently into valence electrons",
      "Valence electrons continuously split into fractional sub-electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In main group elements, only outermost \\(s\\) and \\(p\\) electrons participate in bonding.
However, in transition and heavy elements:
- The energy difference between the outermost shell \\(ns\\) and the penultimate inner shell \\((n-1)d\\) is extremely small:
\\[
\\Delta E_{(ns - (n-1)d)} \\approx 0
\\]
Under different chemical environments (e.g. oxidizing conditions, temperature, nature of combining atom):
- Iron (Fe, \\(Z=26\\)) can lose 2 electrons from \\(4s\\) to exhibit valency 2 (Ferrous, \\(\\text{Fe}^{2+}\\)).
- Under stronger oxidizing conditions, it can additionally lose 1 electron from the \\(3d\\) subshell to attain a stable half-filled \\(3d^5\\) state, exhibiting valency 3 (Ferric, \\(\\text{Fe}^{3+}\\)).
Similarly, Copper exhibits valencies of 1 (Cuprous, \\(\\text{Cu}^+\\)) and 2 (Cupric, \\(\\text{Cu}^{2+}\\)).

### 2. Physical Context & Practical Illustration:
Variable valency allows transition metals to act as versatile industrial catalysts and form diverse colorful coordination complexes (like hemoglobin in blood).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Penultimate shell electron participation due to small energy gaps causes variable valency.
- **Option B is incorrect**: Chemical bonding involves electron rearrangements; nuclear proton count is invariant.
- **Option C is incorrect**: Neutrons do not convert to valence electrons in chemical reactions.
- **Option D is incorrect**: Electron charge is indivisible in chemistry.`
  }
];

module.exports = { topic5Questions };
