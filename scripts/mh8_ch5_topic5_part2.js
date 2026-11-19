// scripts/mh8_ch5_topic5_part2.js
// Set B: Topic 5.5 Atomic Number (Z), Mass Number (A) & Electronic Configuration (Questions 006-010)

const topic5Part2Questions = [
  // 5.5.1 Set B
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-006",
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
    text: "What German word is the universal scientific symbol \\(Z\\) for atomic number derived from?",
    options: [
      "Zahl (meaning 'number')",
      "Zelle (meaning 'cell')",
      "Zeit (meaning 'time')",
      "Zink (meaning 'zinc')"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The conventional symbol \\(Z\\) for atomic number comes from the German word **Atomzahl** (meaning 'atomic number') or simply **Zahl** (meaning 'number').
Before Moseley's work, \\(Z\\) simply represented the ordinal rank or position number of an element in Mendeleev's periodic table. Moseley proved that \\(Z\\) is the physical count of positive nuclear elementary charges.

### 2. Physical Context & Practical Illustration:
The notation \\(^A_Z\\text{X}\\) was standardized by the IUPAC where \\(Z\\) is the atomic number and \\(A\\) is the mass number (from *Atomgewicht* or *Massenzahl*).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: *Zahl* means number in German.
- **Option B is incorrect**: *Zelle* means biological cell or electrochemical cell.
- **Option C is incorrect**: *Zeit* means time in German (as in *Zeitgeist*).
- **Option D is incorrect**: *Zink* is the metallic element Zinc.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-007",
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
    text: "An oxide ion \\(\\text{O}^{2-}\\) has an atomic number of \\(Z = 8\\). What is the total electric charge of the electron cloud surrounding this nucleus?",
    options: [
      "\\(-1.602 \\times 10^{-18}\\text{ C}\\) (corresponding to 10 electrons)",
      "\\(-1.282 \\times 10^{-18}\\text{ C}\\) (corresponding to 8 electrons)",
      "\\(-3.204 \\times 10^{-19}\\text{ C}\\) (corresponding to 2 electrons)",
      "\\(0\\text{ C}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. For Oxygen (\\(Z = 8\\)), a neutral atom has 8 electrons.
2. In forming the oxide anion \\(\\text{O}^{2-}\\), it gains 2 extra electrons:
\\[
n_e = Z + 2 = 8 + 2 = 10\\text{ electrons}
\\]
3. The total charge of these 10 electrons is:
\\[
Q_{\\text{electrons}} = 10 \\times (-1.60218 \\times 10^{-19}\\text{ C}) = -1.60218 \\times 10^{-18}\\text{ C}
\\]
(The positive charge of the 8 nuclear protons is \\(+1.282 \\times 10^{-18}\\text{ C}\\), yielding a net ionic charge of \\(-3.204 \\times 10^{-19}\\text{ C} = -2e\\)).

### 2. Physical Context & Practical Illustration:
The 10 electrons arrange into the stable neon noble-gas octet (2, 8).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: 10 electrons carry a total negative charge of \\(-1.602 \\times 10^{-18}\\text{ C}\\).
- **Option B is incorrect**: \\(-1.282 \\times 10^{-18}\\text{ C}\\) is the charge of 8 electrons (neutral oxygen).
- **Option C is incorrect**: \\(-3.204 \\times 10^{-19}\\text{ C}\\) is the *net* charge of the ion, not the total charge of the whole electron cloud.
- **Option D is incorrect**: The electron cloud carries negative charge.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-008",
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
    text: "Can two different chemical elements ever possess the exact same atomic number \\(Z\\)?",
    options: [
      "No, because the atomic number \\(Z\\) uniquely defines the chemical identity and elemental nature of an atom",
      "Yes, if they belong to the same group in the periodic table",
      "Yes, if they have identical mass numbers (isobars)",
      "Yes, when they form an alloy at high temperature"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **atomic number (\\(Z\\))** is the unique, 1-to-1 bijective identifier of an element:
\\[
\\text{Element Identity} \\iff Z
\\]
No two different elements can have the same \\(Z\\). If two atoms have the same \\(Z\\), they are by definition the exact same chemical element (they may only be different isotopes of that same element).
- If \\(Z = 6\\), it is always Carbon.
- If \\(Z = 7\\), it is always Nitrogen.
Isobars share the same mass number \\(A\\), but must have different atomic numbers \\(Z\\).

### 2. Physical Context & Practical Illustration:
The atomic number \\(Z\\) determines the number of electrons, which determines the valence orbitals, which strictly dictates all chemical properties.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(Z\\) is uniquely element-specific; two different elements can never have the same \\(Z\\).
- **Option B is incorrect**: Elements in the same group have identical valence electrons, but different \\(Z\\) (e.g. F has 9, Cl has 17).
- **Option C is incorrect**: Isobars have the same \\(A\\), but different \\(Z\\).
- **Option D is incorrect**: Alloys are physical mixtures; their constituent atoms retain their native \\(Z\\).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-009",
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
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What is the atomic number of the element that has 8 electrons in its L shell and 2 electrons in its K shell in its ground state?",
    options: [
      "\\(Z = 10\\) (Neon)",
      "\\(Z = 8\\) (Oxygen)",
      "\\(Z = 18\\) (Argon)",
      "\\(Z = 12\\) (Magnesium)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a neutral ground-state atom:
\\[
\\text{Total electrons} = \\text{Electrons in K} + \\text{Electrons in L} = 2 + 8 = 10
\\]
Since the atom is neutral:
\\[
Z = \\text{Number of protons} = \\text{Total electrons} = 10
\\]
Element with \\(Z = 10\\) is **Neon (\\(\\text{Ne}\\))**.

### 2. Physical Context & Practical Illustration:
Neon is an inert noble gas with a complete octet in its outer shell, widely used in luminous orange-red gas discharge signboards.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(2 + 8 = 10\\), which corresponds to Neon (\\(Z = 10\\)).
- **Option B is incorrect**: Oxygen (\\(Z = 8\\)) has 2 in K and 6 in L.
- **Option C is incorrect**: Argon (\\(Z = 18\\)) has 2 in K, 8 in L, and 8 in M.
- **Option D is incorrect**: Magnesium (\\(Z = 12\\)) has 2 in K, 8 in L, and 2 in M.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.1-OSC-010",
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
    text: "An atom has 15 protons, 16 neutrons, and 18 electrons. What is the correct IUPAC chemical formula, symbol, and net electric charge of this species?",
    options: [
      "Phosphide ion, \\(^{31}_{15}\\text{P}^{3-}\\)",
      "Phosphorus neutral atom, \\(^{31}_{15}\\text{P}\\)",
      "Sulfur cation, \\(^{31}_{16}\\text{S}^{2+}\\)",
      "Argon isotope, \\(^{31}_{18}\\text{Ar}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Identify the element**:
   - Number of protons \\(Z = 15 \\implies\\) Element is **Phosphorus (\\(\\text{P}\\))**.
2. **Calculate mass number \\(A\\)**:
   - \\(A = \\text{protons} + \\text{neutrons} = 15 + 16 = 31\\).
3. **Calculate net charge \\(q\\)**:
   - \\(q = \\text{protons} - \\text{electrons} = 15 - 18 = -3\\).
4. **Complete symbol**:
   - \\(^{31}_{15}\\text{P}^{3-}\\) (Phosphide anion).

### 2. Physical Context & Practical Illustration:
Phosphide ions occur in binary ionic compounds like calcium phosphide (\\(\\text{Ca}_3\\text{P}_2\\)) used in signal flares.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(^{31}_{15}\\text{P}^{3-}\\) with \\(Z=15, A=31, q=-3\\).
- **Option B is incorrect**: A neutral atom would require 15 electrons, not 18.
- **Option C is incorrect**: \\(Z = 15\\) is Phosphorus, not Sulfur (\\(Z = 16\\)).
- **Option D is incorrect**: 18 is the electron count, not the atomic number.`
  },

  // 5.5.2 Set B
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-006",
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
    text: "What collective scientific term is used to refer to both protons and neutrons located inside the atomic nucleus?",
    options: [
      "Nucleons",
      "Positrons",
      "Photons",
      "Leptons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Protons and neutrons reside together in the atomic nucleus and share nearly identical mass (\\(\\approx 1\\text{ u}\\)) and strong nuclear interaction properties.
They are collectively termed **nucleons**:
\\[
\\text{Total number of nucleons} = A = Z + N
\\]

### 2. Physical Context & Practical Illustration:
Nuclear physics frequently deals with 'binding energy per nucleon', measuring the stability of the nuclear core irrespective of whether a particle is a proton or neutron.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Nucleons is the collective term for protons and neutrons.
- **Option B is incorrect**: Positrons are antimatter positive electrons.
- **Option C is incorrect**: Photons are quantum packets of electromagnetic light.
- **Option D is incorrect**: Leptons are extranuclear fundamental particles like electrons.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-007",
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
    text: "An isotope of Carbon has a mass number of \\(A = 14\\) and an atomic number of \\(Z = 6\\). What is the ratio of neutrons to protons in this nucleus?",
    options: [
      "\\(4 : 3\\)",
      "\\(1 : 1\\)",
      "\\(7 : 3\\)",
      "\\(3 : 4\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. For Carbon-14 (\\(^{14}_6\\text{C}\\)):
   - Number of protons \\(Z = 6\\)
   - Mass number \\(A = 14\\)
2. Number of neutrons:
\\[
N = A - Z = 14 - 6 = 8
\\]
3. Ratio of neutrons to protons:
\\[
\\frac{N}{Z} = \\frac{8}{6} = \\frac{4}{3}
\\]

### 2. Physical Context & Practical Illustration:
In stable Carbon-12, \\(N/Z = 6/6 = 1.0\\). The excess neutron ratio \\(8/6 = 1.33\\) in Carbon-14 causes nuclear instability, resulting in spontaneous beta-minus decay with a 5730-year half-life.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(8/6 = 4/3\\).
- **Option B is incorrect**: \\(1:1\\) corresponds to Carbon-12 (6 neutrons, 6 protons).
- **Option C is incorrect**: \\(14/6 = 7/3\\) is the ratio of *mass number* to protons, not neutrons to protons.
- **Option D is incorrect**: Inverts the ratio (protons to neutrons).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-008",
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
    text: "Two atomic nuclides are given: \\(^{14}_6\\text{C}\\) and \\(^{16}_8\\text{O}\\). What nuclear relationship exists between these two atoms?",
    options: [
      "They are isotones (both contain exactly 8 neutrons)",
      "They are isotopes (same atomic number)",
      "They are isobars (same mass number)",
      "They are isoelectronic (same electron count)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Compute the neutron count \\(N = A - Z\\) for both nuclides:
1. For \\(^{14}_6\\text{C}\\):
\\[
N_1 = 14 - 6 = 8\\text{ neutrons}
\\]
2. For \\(^{16}_8\\text{O}\\):
\\[
N_2 = 16 - 8 = 8\\text{ neutrons}
\\]
Since \\(N_1 = N_2 = 8\\), but their atomic numbers differ (\\(Z_1 = 6 \\ne Z_2 = 8\\)), they are **isotones** (nuclides having the same number of neutrons).

### 2. Physical Context & Practical Illustration:
Isotones help nuclear physicists study how nuclear shell closures depend on neutron number independently of proton charge.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Both have \\(N = 8\\), making them isotones.
- **Option B is incorrect**: \\(Z\\) values are 6 and 8; they are different elements, not isotopes.
- **Option C is incorrect**: Mass numbers are 14 and 16; they are not isobars.
- **Option D is incorrect**: Neutral Carbon has 6 electrons; neutral Oxygen has 8 electrons; they are not isoelectronic.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-009",
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
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Can the mass number (\\(A\\)) of any atomic nucleus ever be strictly less than its atomic number (\\(Z\\))?",
    options: [
      "No, because \\(A = Z + N\\) and neutron count \\(N \\ge 0\\), so \\(A \\ge Z\\) always",
      "Yes, for elements with more than 100 protons",
      "Yes, for gaseous elements like helium and neon",
      "Yes, when atoms are cooled to absolute zero"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition:
\\[
A = Z + N
\\]
Since the number of neutrons \\(N\\) is an integer count of physical particles, it cannot be negative:
\\[
N \\ge 0
\\]
Therefore:
\\[
A \\ge Z
\\]
The minimum possible value occurs for Protium (\\(^1_1\\text{H}\\)), where \\(N = 0\\) and \\(A = Z = 1\\). For all other nuclides, \\(N > 0\\), so \\(A > Z\\). Under no circumstances can \\(A < Z\\).

### 2. Physical Context & Practical Illustration:
Mass number is the whole building (protons + neutrons); it can never have fewer rooms than the number of protons inside it.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(A \\ge Z\\) is a mathematical necessity since \\(N \\ge 0\\).
- **Option B is incorrect**: Transuranic elements have \\(N \\gg Z\\) (e.g. \\(Z=100, A=257\\)).
- **Option C is incorrect**: Helium has \\(Z=2, A=4\\); Neon has \\(Z=10, A=20\\); both have \\(A > Z\\).
- **Option D is incorrect**: Temperature has no effect on nuclear particle counts.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.2-OSC-010",
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
    text: "During radioactive alpha decay, a parent nucleus \\(^A_Z\\text{X}\\) emits an alpha particle (\\(^4_2\\text{He}\\)). What are the mass number and atomic number of the resulting daughter nucleus \\(\\text{Y}\\)?",
    options: [
      "Mass number \\(A - 4\\) and atomic number \\(Z - 2\\)",
      "Mass number \\(A - 2\\) and atomic number \\(Z - 4\\)",
      "Mass number \\(A\\) and atomic number \\(Z + 1\\)",
      "Mass number \\(A - 1\\) and atomic number \\(Z - 1\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In nuclear decay, both total nucleon number (mass number \\(A\\)) and total electric charge (atomic number \\(Z\\)) are strictly conserved:
\\[
^A_Z\\text{X} \\rightarrow ^{A-4}_{Z-2}\\text{Y} + ^4_2\\text{He}
\\]
1. **Conservation of Mass Number**:
\\[
A_{\\text{parent}} = A_{\\text{daughter}} + 4 \\implies A_{\\text{daughter}} = A - 4
\\]
2. **Conservation of Atomic Number**:
\\[
Z_{\\text{parent}} = Z_{\\text{daughter}} + 2 \\implies Z_{\\text{daughter}} = Z - 2
\\]
This is Soddy-Fajans' displacement law for alpha decay: the element shifts two places to the left in the periodic table.

### 2. Physical Context & Practical Illustration:
For example, Uranium-238 decays into Thorium-234:
\\[
^{238}_{92}\\text{U} \\rightarrow ^{234}_{90}\\text{Th} + ^4_2\\text{He}
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(A - 4\\) and \\(Z - 2\\) conserve nucleons and charge.
- **Option B is incorrect**: Inverts the changes in \\(A\\) and \\(Z\\).
- **Option C is incorrect**: \\(A\\) and \\(Z + 1\\) describes beta-minus (\\(\\beta^-\\)) decay.
- **Option D is incorrect**: Describes proton emission.`
  },

  // 5.5.3 Set B
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-006",
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
    text: "Who jointly formulated the rules governing the distribution of electrons in different shells of an atom (the \\(2n^2\\) rule and octet rule) in 1921?",
    options: [
      "Niels Bohr and Charles Bury",
      "Ernest Rutherford and Hans Geiger",
      "John Dalton and Amedeo Avogadro",
      "Dmitri Mendeleev and Henry Moseley"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1921, Danish physicist **Niels Bohr** and English chemist **Charles R. Bury** independently proposed the systematic scheme for electron arrangements in atomic shells, universally known as the **Bohr-Bury Scheme**:
1. Maximum shell capacity is \\(2n^2\\).
2. Outermost shell cannot hold more than 8 electrons (octet).
3. The penultimate shell cannot hold more than 18 electrons.
4. A new outer shell begins filling as soon as the current valence shell acquires 8 electrons.

### 2. Physical Context & Practical Illustration:
The Bohr-Bury scheme provided the first structural explanation for why periods in the periodic table have 2, 8, 8, 18, 18, and 32 elements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Niels Bohr and Charles Bury formulated the scheme in 1921.
- **Option B is incorrect**: Rutherford and Geiger investigated alpha particle scattering.
- **Option C is incorrect**: Dalton and Avogadro founded early atomic and molecular theory.
- **Option D is incorrect**: Mendeleev and Moseley structured the periodic table.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-007",
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
    text: "Why does Potassium (\\(Z = 19\\)) have the electronic configuration 2, 8, 8, 1 instead of 2, 8, 9, even though the M shell has a maximum theoretical capacity of 18 electrons?",
    options: [
      "Because the outermost shell of an atom cannot hold more than 8 electrons, so once M reaches 8, the next electron must enter the N shell",
      "Because the M shell physically collapses after receiving 8 electrons",
      "Because the 19th electron carries a positive charge that repels the M shell",
      "Because Potassium is an artificial man-made isotope"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By the **Bohr-Bury Rule**:
- *The outermost shell cannot hold more than 8 electrons.*
For Potassium (\\(Z = 19\\)):
- K shell: 2
- L shell: 8
If the remaining 9 electrons were put into M, M would become the outermost shell with 9 electrons, violating the octet limit.
Therefore, M holds 8 electrons, and the 19th electron starts the N shell:
\\[
\\text{Configuration} = (2, 8, 8, 1)
\\]
In modern orbital terms, the \\(4s\\) orbital has lower energy than the \\(3d\\) orbital (\\(n + l\\) rule: for \\(4s\\), \\(4 + 0 = 4\\); for \\(3d\\), \\(3 + 2 = 5\\)), so \\(4s\\) fills before \\(3d\\).

### 2. Physical Context & Practical Illustration:
This is why Potassium is an alkali metal in Group 1 with 1 valence electron, closely resembling Sodium (2, 8, 1).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The outermost octet limit forces the 19th electron into the N shell.
- **Option B is incorrect**: The M shell does not collapse; it later expands to hold 18 in Scandium through Zinc.
- **Option C is incorrect**: All electrons carry identical negative charge \\(-e\\).
- **Option D is incorrect**: Potassium is a naturally abundant alkali metal.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-008",
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
    text: "At which chemical element does the M shell (\\(n = 3\\)) finally achieve its full capacity of 18 electrons in the periodic table?",
    options: [
      "Zinc (\\(Z = 30\\), configuration 2, 8, 18, 2)",
      "Argon (\\(Z = 18\\), configuration 2, 8, 8)",
      "Calcium (\\(Z = 20\\), configuration 2, 8, 8, 2)",
      "Krypton (\\(Z = 36\\), configuration 2, 8, 18, 8)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us trace the filling of the M shell:
- Argon (\\(Z = 18\\)): \\(2, 8, 8\\) (M has 8)
- Potassium (\\(Z = 19\\)): \\(2, 8, 8, 1\\) (N starts)
- Calcium (\\(Z = 20\\)): \\(2, 8, 8, 2\\) (N has 2)
Now with N acting as the outermost shell, the inner M shell is free to fill its remaining capacity up to 18 via the \\(3d\\) subshell (transition elements from Scandium \\(Z=21\\) to Zinc \\(Z=30\\)):
- Scandium (\\(Z = 21\\)): \\(2, 8, 9, 2\\)
- Iron (\\(Z = 26\\)): \\(2, 8, 14, 2\\)
- **Zinc (\\(Z = 30\\))**: \\(2, 8, 18, 2\\)
At Zinc (\\(Z = 30\\)), the M shell is completely saturated with its maximum theoretical capacity of \\(2(3)^2 = 18\\) electrons.

### 2. Physical Context & Practical Illustration:
Zinc completes the 3d transition series; in the next element Gallium (\\(Z=31\\)), electrons begin populating the N shell again (2, 8, 18, 3).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Zinc (\\(Z = 30\\)) has a completely full M shell with 18 electrons.
- **Option B is incorrect**: Argon has only 8 electrons in M.
- **Option C is incorrect**: Calcium has only 8 electrons in M.
- **Option D is incorrect**: Krypton has full M (18) and full N octet (8), but Zinc was the first to complete M.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-009",
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
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What is the maximum number of electrons that can be accommodated in the penultimate (second from outside) shell of any atom according to the Bohr-Bury scheme?",
    options: [
      "18 electrons",
      "8 electrons",
      "32 electrons",
      "2 electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The third rule of the **Bohr-Bury scheme** governs internal boundary capacities:
1. Outermost shell: Maximum **8 electrons**.
2. Penultimate shell (shell immediately preceding the outermost shell, \\(n - 1\\)): Maximum **18 electrons**.
3. Antepenultimate shell (two shells inside, \\(n - 2\\)): Maximum **32 electrons**.

### 2. Physical Context & Practical Illustration:
This rule prevents transition elements from overloading inner shells with more than 18 electrons while their valence shell contains 1 or 2 electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The penultimate shell capacity limit is 18 electrons.
- **Option B is incorrect**: 8 is the limit for the *outermost* shell.
- **Option C is incorrect**: 32 is the limit for the *antepenultimate* shell.
- **Option D is incorrect**: 2 is the capacity of the K shell only.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.3-OSC-010",
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
    text: "Why does the 4th period of the periodic table contain exactly 18 elements rather than 32 elements, despite the N shell (\\(n = 4\\)) having a maximum theoretical capacity of \\(2(4)^2 = 32\\)?",
    options: [
      "Because the 4th period fills only the \\(4s\\) (2 electrons), \\(3d\\) (10 electrons), and \\(4p\\) (6 electrons) orbitals: \\(2 + 10 + 6 = 18\\), while \\(4f\\) fills later in period 6",
      "Because 14 elements in period 4 decay radioactively and are excluded from the table",
      "Because the speed of electrons in period 4 exceeds the speed of light",
      "Because the N shell cannot hold more than 18 electrons under any circumstances"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to the Aufbau principle (energy ordering given by the \\(n + l\\) rule):
The orbitals filling in the 4th period are:
1. \\(4s\\) subshell (\\(n=4, l=0, n+l=4\\)): holds 2 electrons (K and Ca).
2. \\(3d\\) subshell (\\(n=3, l=2, n+l=5\\)): holds 10 electrons (Sc to Zn).
3. \\(4p\\) subshell (\\(n=4, l=1, n+l=5\\)): holds 6 electrons (Ga to Kr).
Total elements in Period 4:
\\[
2 + 10 + 6 = 18\\text{ elements}
\\]
The \\(4f\\) subshell (\\(n=4, l=3, n+l=7\\)) has higher energy than \\(5s, 4d, 5p, 6s\\); its filling is delayed until **Period 6** (Lanthanoids), where the N shell finally achieves its full capacity of 32.

### 2. Physical Context & Practical Illustration:
Subshell energy splitting explains why the lengths of periods in the periodic table are 2, 8, 8, 18, 18, 32, 32.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The 4th period fills \\(4s + 3d + 4p = 18\\) electrons; \\(4f\\) fills in period 6.
- **Option B is incorrect**: Period 4 elements (Potassium through Krypton) are stable and well known.
- **Option C is incorrect**: Electron velocity is well below light speed.
- **Option D is incorrect**: The N shell can and does hold 32 electrons in elements with \\(Z \\ge 71\\).`
  },

  // 5.5.4 Set B
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-006",
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
    text: "What is the valency of Carbon (\\(Z = 6\\)), and what specific term is used to describe an element with this valency?",
    options: [
      "Valency = 4 (Tetravalent)",
      "Valency = 2 (Divalent)",
      "Valency = 1 (Monovalent)",
      "Valency = 3 (Trivalent)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. Electronic configuration of Carbon (\\(Z = 6\\)):
\\[
\\text{K} = 2, \\quad \\text{L} = 4 \\implies (2, 4)
\\]
2. Carbon has 4 valence electrons in its outer shell.
3. To attain the stable octet of Neon (8), Carbon shares 4 electrons with other atoms, forming 4 covalent bonds:
\\[
\\text{Valency} = 4
\\]
An element with valency 4 is termed **tetravalent** (from Greek *tetra* meaning four).

### 2. Physical Context & Practical Illustration:
Carbon's tetravalency combined with its unique ability for catenation (forming stable chains and rings) is the structural foundation of all organic chemistry and biological life.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Valency is 4; Carbon is tetravalent.
- **Option B is incorrect**: Valency 2 is divalent (like Oxygen, Magnesium).
- **Option C is incorrect**: Valency 1 is monovalent (like Hydrogen, Sodium).
- **Option D is incorrect**: Valency 3 is trivalent (like Aluminium, Nitrogen).`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-007",
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
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "An element \\(\\text{M}\\) has an electronic configuration of 2, 8, 2. Another element \\(\\text{X}\\) has an electronic configuration of 2, 7. What is the chemical formula and bonding type of the compound formed between \\(\\text{M}\\) and \\(\\text{X}\\)?",
    options: [
      "\\(\\text{MX}_2\\) (Ionic compound)",
      "\\(\\text{MX}\\) (Covalent compound)",
      "\\(\\text{M}_2\\text{X}\\) (Metallic compound)",
      "\\(\\text{M}_2\\text{X}_3\\) (Coordinate compound)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Element \\(\\text{M}\\) (2, 8, 2, Magnesium, \\(Z=12\\))**:
   - Metal with 2 valence electrons.
   - Readily loses 2 electrons: \\(\\text{M} \\rightarrow \\text{M}^{2+} + 2e^-\\).
   - Valency = 2.
2. **Element \\(\\text{X}\\) (2, 7, Chlorine/Fluorine, \\(Z=9\\text{ or }17\\))**:
   - Non-metal with 7 valence electrons.
   - Readily gains 1 electron: \\(\\text{X} + e^- \\rightarrow \\text{X}^-\\).
   - Valency = \\(8 - 7 = 1\\).
3. **Formula formation**:
   - Valency of \\(\\text{M} = 2\\), Valency of \\(\\text{X} = 1\\).
   - Criss-crossing valencies:
\\[
\\text{Formula} = \\text{MX}_2 \\quad (\\text{representing } \\text{MgCl}_2 \\text{ or } \\text{MgF}_2)
\\]
Because electrons are completely transferred from metal to non-metal, the bond is **ionic (electrovalent)**.

### 2. Physical Context & Practical Illustration:
One Magnesium cation (\\(\\text{Mg}^{2+}\\)) electrostatically binds two halide anions (\\(2\\text{X}^-\\)) into a high-melting ionic crystalline solid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\text{MX}_2\\) with ionic bonding.
- **Option B is incorrect**: \\(\\text{MX}\\) would require valency 1 on both atoms.
- **Option C is incorrect**: \\(\\text{M}_2\\text{X}\\) corresponds to monovalent metal oxide (e.g. \\(\\text{Na}_2\\text{O}\\)).
- **Option D is incorrect**: \\(\\text{M}_2\\text{X}_3\\) requires valency 3 on metal.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-008",
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
    text: "Which of the following pairs of elements have identical numbers of valence electrons and therefore exhibit very similar chemical properties?",
    options: [
      "Lithium (\\(Z = 3\\)) and Sodium (\\(Z = 11\\))",
      "Carbon (\\(Z = 6\\)) and Nitrogen (\\(Z = 7\\))",
      "Magnesium (\\(Z = 12\\)) and Aluminium (\\(Z = 13\\))",
      "Helium (\\(Z = 2\\)) and Beryllium (\\(Z = 4\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Elements in the same periodic group have identical outer valence electron counts:
- **Lithium (\\(Z = 3\\))**: Electronic configuration \\(2, 1\\) \\(\\implies 1\\) valence electron.
- **Sodium (\\(Z = 11\\))**: Electronic configuration \\(2, 8, 1\\) \\(\\implies 1\\) valence electron.
Both belong to Group 1 (Alkali Metals). Both have valency 1, readily lose their single valence electron to form \\(+1\\) cations (\\(\\text{Li}^+, \\text{Na}^+\\)), react vigorously with water releasing hydrogen gas, and form basic hydroxides (\\(\\text{LiOH}, \\text{NaOH}\\)).

### 2. Physical Context & Practical Illustration:
The periodic recurrence of similar chemical properties down vertical columns occurs precisely because valence shell structures repeat cyclically.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Both Lithium and Sodium have 1 valence electron and belong to Group 1.
- **Option B is incorrect**: Carbon has 4 valence electrons; Nitrogen has 5.
- **Option C is incorrect**: Magnesium has 2 valence electrons; Aluminium has 3.
- **Option D is incorrect**: Although both end in 2, Helium (2) is an inert noble gas with a complete duplet, while Beryllium (2, 2) is a reactive alkaline earth metal.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-009",
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
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What is the valency of the Noble Gas Helium (\\(Z = 2\\)), and why is it chemically inert even though it has only 2 electrons in its valence shell?",
    options: [
      "Valency = 0, because its outermost K shell has a maximum capacity of only 2 electrons (\\(2n^2 = 2\\)), making its duplet completely saturated and stable",
      "Valency = 2, because it forms two ionic bonds with oxygen",
      "Valency = 8, because it contains 8 invisible virtual electrons",
      "Valency = 1, because it behaves like hydrogen gas"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For Helium (\\(Z = 2\\)):
- The single occupied shell is the K shell (\\(n = 1\\)).
- The maximum holding capacity of the K shell by the \\(2n^2\\) rule is:
\\[
2(1)^2 = 2\\text{ electrons}
\\]
Because its outermost shell is completely filled to maximum capacity, it possesses a stable closed **duplet**.
It has zero tendency to lose, gain, or share electrons:
\\[
\\text{Valency} = 0
\\]

### 2. Physical Context & Practical Illustration:
Helium has the highest first ionization energy of any element in the periodic table (\\(24.6\\text{ eV}\\)), making it the most unreactive chemical element known.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The K shell duplet is completely filled and stable, giving a valency of 0.
- **Option B is incorrect**: Helium forms zero stable chemical bonds with oxygen under normal conditions.
- **Option C is incorrect**: Helium has strictly 2 electrons total, not 8.
- **Option D is incorrect**: Hydrogen is reactive and monovalent, while Helium is inert with valency 0.`
  },
  {
    questionCode: "MH-8-SCI-5-5.5.4-OSC-010",
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
    text: "Phosphorus (\\(Z = 15\\)) forms two stable chlorides: Phosphorus trichloride (\\(\\text{PCl}_3\\)) and Phosphorus pentachloride (\\(\\text{PCl}_5\\)). What quantum phenomenon explains this expanded octet and variable valency of 3 and 5?",
    options: [
      "In the excited state, one \\(3s\\) electron unpairs and promotes into an available vacant \\(3d\\) orbital, providing 5 unpaired electrons for bonding",
      "Phosphorus atoms split into two fragments when reacting with chlorine",
      "Chlorine atoms inject extra protons into the phosphorus nucleus",
      "Phosphorus gains 5 electrons from outer space"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Ground state of Phosphorus (\\(Z = 15\\))**:
   - Configuration: \\(1s^2 2s^2 2p^6 3s^2 3p^3\\) (or 2, 8, 5)
   - The three \\(3p\\) electrons are unpaired (\\(3p_x^1 3p_y^1 3p_z^1\\)).
   - Sharing with 3 chlorine atoms yields **\\(\\text{PCl}_3\\)** (valency = 3).
2. **Excited state (promotion to \\(3d\\))**:
   - Because Phosphorus is in the 3rd period (\\(n = 3\\)), it possesses vacant energetically accessible **\\(3d\\) orbitals** that are absent in 2nd-period elements like Nitrogen.
   - Upon excitation, one \\(3s\\) electron unpairs and is promoted into a vacant \\(3d\\) orbital:
\\[
3s^1 3p_x^1 3p_y^1 3p_z^1 3d^1
\\]
   - This creates **5 unpaired electrons**, allowing Phosphorus to form 5 covalent bonds with chlorine in **\\(\\text{PCl}_5\\)** (expanded octet with 10 shared valence electrons, valency = 5).

### 2. Physical Context & Practical Illustration:
Nitrogen (\\(Z=7\\), 2nd period) has no \\(2d\\) orbitals, so \\(\\text{NCl}_5\\) cannot form; Phosphorus (3rd period) has vacant \\(3d\\) orbitals, so \\(\\text{PCl}_5\\) easily forms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Unpairing and promotion of a \\(3s\\) electron into an accessible vacant \\(3d\\) orbital enables valency 5.
- **Option B is incorrect**: Molecules form via covalent sharing, not nuclear fission.
- **Option C is incorrect**: Protons are in the nucleus and do not transfer during chemical bonding.
- **Option D is incorrect**: Electrons are supplied by the reacting chlorine atoms.`
  }
];

module.exports = { topic5Part2Questions };
