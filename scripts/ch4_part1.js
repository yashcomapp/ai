// scripts/ch4_part1.js - Chapter 4 (Measurement of Matter) Questions 1-35 Gold Standard Enhancements
const ch4_part1 = [
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-001",
    text: "How many total atoms are present in \\(0.9\\text{ g}\\) of pure water (\\(\\text{H}_2\\text{O}\\))? (Given: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(3.011 \\times 10^{22}\\text{ atoms}\\)",
      "\\(6.022 \\times 10^{22}\\text{ atoms}\\)",
      "\\(9.033 \\times 10^{22}\\text{ atoms}\\)",
      "\\(1.806 \\times 10^{23}\\text{ atoms}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Water (\\(\\text{H}_2\\text{O}\\))**:
\\[
M = (2 \\times 1) + 16 = 18\\text{ g/mol}
\\]
2. **Number of Moles of \\(\\text{H}_2\\text{O}\\)**:
\\[
n = \\frac{m}{M} = \\frac{0.9\\text{ g}}{18\\text{ g/mol}} = 0.05\\text{ mol}
\\]
3. **Number of Water Molecules**:
\\[
N_{\\text{molecules}} = n \\times N_A = 0.05 \\times 6.022 \\times 10^{23} = 3.011 \\times 10^{22}\\text{ molecules}
\\]
4. **Total Atoms**: Each molecule of \\(\\text{H}_2\\text{O}\\) contains 3 atoms (2 Hydrogen atoms + 1 Oxygen atom):
\\[
N_{\\text{atoms}} = 3 \\times N_{\\text{molecules}} = 3 \\times (3.011 \\times 10^{22}) = 9.033 \\times 10^{22}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
Even a tiny fraction of a drop of water (\\(0.9\\text{ g}\\) is less than a millilitre) contains over 90 sextillion individual atoms bonded into stable triatomic molecular geometries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(3.011 \\times 10^{22}\\) is the number of water *molecules*, forgetting to multiply by the 3 constituent atoms per molecule.
- **Option B is incorrect**: \\(6.022 \\times 10^{22}\\) counts only the hydrogen atoms (\\(2 \\times 3.011 \\times 10^{22}\\)), ignoring oxygen.
- **Option C is correct**: \\(N_{\\text{atoms}} = 3 \\times 0.05 \\times 6.022 \\times 10^{23} = 9.033 \\times 10^{22}\\text{ atoms}\\).
- **Option D is incorrect**: \\(1.806 \\times 10^{23}\\) corresponds to calculating for a full mole or arithmetic miscalculation.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-002",
    text: "The capacity of an atom of an element to combine chemically with atoms of other elements to attain a stable electronic configuration is called its:",
    options: [
      "Radioactivity",
      "Electronegativity",
      "Valency",
      "Isotropy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Valency** is defined as the combining capacity of an element. It is determined by the number of valence electrons an atom gains, loses, or shares to achieve a stable octet (or duplet for lighter elements like H and He) in its outermost shell:
\\[
\\text{Valency} = 
\\begin{cases} 
V_e & \\text{if } V_e \\le 4 \\\\ 
8 - V_e & \\text{if } V_e > 4 
\\end{cases}
\\]
where \\(V_e\\) is the number of valence electrons.

### 2. Physical Context & Practical Illustration:
For example, Sodium (Na, 2,8,1) donates 1 electron, having a valency of 1. Chlorine (Cl, 2,8,7) accepts 1 electron, having a valency of 1. They combine in a 1:1 ratio to form table salt (NaCl). Carbon (C, 2,4) shares 4 electrons, having a tetravalency of 4 in methane (CH₄).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Radioactivity is the spontaneous nuclear decay of unstable atomic nuclei emitting radiation.
- **Option B is incorrect**: Electronegativity is the relative tendency of an atom to attract a shared pair of electrons toward itself.
- **Option C is correct**: Valency represents the fundamental combining capacity of an element.
- **Option D is incorrect**: Isotropy refers to physical properties being identical in all directions.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-003",
    text: "According to the international unified atomic mass standard, what is the standard relative atomic mass of the Carbon-12 isotope?",
    options: [
      "\\(12\\text{ u}\\)",
      "\\(6\\text{ u}\\)",
      "\\(1\\text{ u}\\)",
      "\\(14\\text{ u}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1961, the International Union of Pure and Applied Chemistry (IUPAC) adopted the **Carbon-12 (\\(^{12}\\text{C}\\)) isotope** as the universal standard reference for atomic mass:
\\[
1\\text{ unified atomic mass unit (u)} = \\frac{1}{12} \\times \\text{Mass of one } ^{12}\\text{C atom}
\\]
By definition, the relative atomic mass of an unbonded neutral Carbon-12 atom in its nuclear and electronic ground state is assigned an exact value of:
\\[
A_r(^{12}\\text{C}) = 12\\text{ u} \\quad (1\\text{ u} \\approx 1.6605 \\times 10^{-27}\\text{ kg})
\\]

### 2. Physical Context & Practical Illustration:
Prior to 1961, Hydrogen and Oxygen were used as standards, causing discrepancies between physical and chemical scales. The Carbon-12 scale resolved this because carbon is abundant, solid, and easily prepared in high isotopic purity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The atomic mass of the reference Carbon-12 isotope is defined as exactly \\(12\\text{ u}\\).
- **Option B is incorrect**: \\(6\\) is the atomic number (\\(Z\\), number of protons) of carbon, not its atomic mass.
- **Option C is incorrect**: \\(1\\text{ u}\\) is approximately the mass of a single proton or hydrogen atom.
- **Option D is incorrect**: \\(14\\text{ u}\\) is the atomic mass of Nitrogen-14 or Carbon-14.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-004",
    text: "What electronic change occurs when a neutral sodium atom (Na) transforms into a sodium cation (\\(\\text{Na}^+\\))?",
    options: [
      "Its relative atomic mass changes significantly by one unified mass unit",
      "It loses one valence electron to achieve a stable octet configuration",
      "It gains one electron into its outermost electronic shell",
      "Its nuclear atomic number changes by one unit"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A neutral sodium atom (\\(Z = 11\\)) has the ground-state electron configuration:
\\[
\\text{Na}: 2, 8, 1 \\quad (11\\text{ protons, } 11\\text{ electrons})
\\]
To attain a stable noble gas configuration (Neon: \\(2, 8\\)), sodium readily loses its single loosely bound valence electron:
\\[
\\text{Na} \\longrightarrow \\text{Na}^+ + e^-
\\]
The resulting sodium cation (\\(\\text{Na}^+\\)) has 11 protons and 10 electrons, possessing a net positive charge of \\(+1\\) while retaining its original nuclear identity (atomic number \\(Z = 11\\)).

### 2. Physical Context & Practical Illustration:
Because the mass of an electron is negligible (\\(\\approx 1/1836\\) of a proton's mass), ionization does not alter the mass number. The atomic nucleus remains untouched; only the outer electron cloud contracts, giving \\(\\text{Na}^+\\) a smaller ionic radius than the neutral atom.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The mass of one electron is negligible; relative atomic mass remains effectively unchanged.
- **Option B is correct**: Sodium loses its single outermost valence electron to form a stable octet \\(\\text{Na}^+\\) ion.
- **Option C is incorrect**: Gaining an electron would form an unstable anion \\(\\text{Na}^-\\).
- **Option D is incorrect**: Nuclear proton count is unchanged (\\(Z = 11\\)); only electrons participate in chemical ionization.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-005",
    text: "Given that the relative atomic mass of oxygen is \\(16\\text{ u}\\), what is the molecular mass of an oxygen gas molecule (\\(\\text{O}_2\\))?",
    options: [
      "\\(16\\text{ u}\\)",
      "\\(8\\text{ u}\\)",
      "\\(48\\text{ u}\\)",
      "\\(32\\text{ u}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The molecular mass of a substance is the sum of the atomic masses of all the constituent atoms present in one molecule of that substance:
\\[
M(\\text{O}_2) = 2 \\times A_r(\\text{O})
\\]
Oxygen gas naturally exists as a **diatomic molecule** (atomicity = 2):
\\[
M(\\text{O}_2) = 2 \\times 16\\text{ u} = 32\\text{ u}
\\]
Its molar mass is correspondingly \\(32\\text{ g/mol}\\).

### 2. Physical Context & Practical Illustration:
One mole of elemental oxygen atoms (\\(\\text{O}\\)) has a mass of \\(16\\text{ g}\\), but one mole of breathable atmospheric oxygen gas (\\(\\text{O}_2\\)) has a mass of \\(32\\text{ g}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(16\\text{ u}\\) is the atomic mass of an isolated oxygen atom (\\(\\text{O}\\)).
- **Option B is incorrect**: \\(8\\) is the atomic number of oxygen (number of protons).
- **Option C is incorrect**: \\(48\\text{ u}\\) is the molecular mass of ozone (\\(\\text{O}_3\\)).
- **Option D is correct**: Oxygen gas is diatomic; \\(M = 2 \\times 16 = 32\\text{ u}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-006",
    text: "What is the standard relative atomic mass of the lightest element, Hydrogen (¹H)?",
    options: [
      "\\(1\\text{ Avogadro number}\\)",
      "\\(1\\text{ Mole}\\)",
      "\\(1\\text{ u}\\)",
      "\\(2\\text{ u}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The protium isotope of hydrogen (\\(^1\\text{H}\\)) consists of a single proton in its nucleus and a single orbiting electron:
\\[
A_r(\\text{H}) \\approx 1.008\\text{ u} \\approx 1\\text{ u}
\\]
In unified atomic mass units (\\(\\text{u}\\)), where \\(1\\text{ u} = \\frac{1}{12} m(^{12}\\text{C})\\), hydrogen has a relative atomic mass taken as \\(1\\text{ u}\\).

### 2. Physical Context & Practical Illustration:
Hydrogen was the original benchmark used by John Dalton in his relative atomic mass scale because it is the lightest known element in the universe.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Avogadro's number is a dimensionless count (\\(6.022 \\times 10^{23}\\)), not an atomic mass.
- **Option B is incorrect**: A mole is an amount of substance containing \\(N_A\\) particles.
- **Option C is correct**: The relative atomic mass of hydrogen is \\(1\\text{ u}\\) (unified atomic mass unit).
- **Option D is incorrect**: \\(2\\text{ u}\\) is the molecular mass of hydrogen gas (\\(\\text{H}_2\\)) or the atomic mass of deuterium (\\(^2\\text{H}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-007",
    text: "Which of the following elemental substances exists naturally as a triatomic molecule (atomicity = 3)?",
    options: [
      "Ozone (\\(\\text{O}_3\\))",
      "Nitrogen (\\(\\text{N}_2\\))",
      "Carbon monoxide (\\(\\text{CO}\\))",
      "Hydrogen (\\(\\text{H}_2\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Atomicity** refers to the total number of atoms constituting a single molecule of an element or compound:
- Monoatomic: Noble gases (He, Ne, Ar) - atomicity = 1
- Diatomic: \\(\\text{H}_2\\), \\(\\text{N}_2\\), \\(\\text{O}_2\\), \\(\\text{Cl}_2\\) - atomicity = 2
- **Triatomic**: **Ozone (\\(\\text{O}_3\\))** - atomicity = 3 (composed of three oxygen atoms bonded in a bent geometry)
- Tetra-atomic: Phosphorus (\\(\\text{P}_4\\)) - atomicity = 4
- Polyatomic: Sulfur (\\(\\text{S}_8\\)) - atomicity = 8

### 2. Physical Context & Practical Illustration:
Ozone forms the protective stratospheric ozone layer, absorbing harmful solar ultraviolet radiation. In the upper atmosphere, UV light breaks \\(\\text{O}_2\\) into nascent oxygen atoms, which combine with molecular \\(\\text{O}_2\\) to form triatomic ozone: \\(\\text{O} + \\text{O}_2 \\to \\text{O}_3\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Ozone (\\(\\text{O}_3\\)) is a triatomic molecule consisting of 3 oxygen atoms.
- **Option B is incorrect**: Nitrogen (\\(\\text{N}_2\\)) is diatomic (atomicity = 2).
- **Option C is incorrect**: Carbon monoxide (\\(\\text{CO}\\)) is a hetero-diatomic compound, not an elemental triatomic molecule.
- **Option D is incorrect**: Hydrogen (\\(\\text{H}_2\\)) is diatomic.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-008",
    text: "For Carbon, with atomic mass 12 and atomic number 6, which statement correctly defines the relationship with the atomic mass of Hydrogen on the unified atomic scale?",
    options: [
      "The atomic mass of a Hydrogen atom is \\(1/6\\)th of the atomic mass of a Carbon-12 atom",
      "The atomic mass of a Hydrogen atom is equal to 6 times the Carbon atomic mass",
      "The atomic mass of a Hydrogen atom is equal to 12 times the Carbon atomic mass",
      "The atomic mass of a Hydrogen atom is approximately \\(1/12\\)th of the atomic mass of a Carbon-12 atom"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By international IUPAC definition, the unified atomic mass unit (\\(1\\text{ u}\\)) is defined as exactly one-twelfth (\\(1/12\\)) of the mass of a single atom of Carbon-12:
\\[
1\\text{ u} = \\frac{1}{12} \\times m(^{12}\\text{C})
\\]
Since a Hydrogen atom (\\(^1\\text{H}\\)) has an atomic mass of approximately \\(1\\text{ u}\\):
\\[
m(\\text{H}) \\approx 1\\text{ u} = \\frac{1}{12} \\times m(^{12}\\text{C})
\\]
Hence, the mass of one Hydrogen atom is approximately \\(1/12\\)th of the mass of a Carbon-12 atom.

### 2. Physical Context & Practical Illustration:
A carbon atom's nucleus contains 6 protons and 6 neutrons (total 12 nucleons), whereas a protium hydrogen atom contains only 1 nucleon (a single proton). Consequently, a carbon atom is roughly 12 times heavier than a hydrogen atom.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Uses atomic number 6 instead of atomic mass 12.
- **Option B is incorrect**: Inverts the relationship and confuses mass with atomic number.
- **Option C is incorrect**: Inverts the ratio; hydrogen is lighter, not heavier than carbon.
- **Option D is correct**: Hydrogen's atomic mass is approximately \\(1/12\\) of the Carbon-12 mass.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-009",
    text: "What is the standard numerical value of Avogadro's constant (\\(N_A\\))?",
    options: [
      "\\(6.022 \\times 10^{24}\\text{ mol}^{-1}\\)",
      "\\(6.022 \\times 10^{22}\\text{ mol}^{-1}\\)",
      "\\(60.22 \\times 10^{23}\\text{ mol}^{-1}\\)",
      "\\(6.022 \\times 10^{23}\\text{ mol}^{-1}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Avogadro's constant** (\\(N_A\\) or \\(L\\)) is the proportionality factor that relates the molar amount of a substance to the number of constituent elementary entities (atoms, molecules, ions, or electrons):
\\[
N_A = 6.02214076 \\times 10^{23}\\text{ mol}^{-1} \\approx 6.022 \\times 10^{23}\\text{ mol}^{-1}
\\]
Under the 2019 SI redefinition, \\(N_A\\) is an exact defining constant of the International System of Units. Exactly one mole of any pure substance contains \\(6.022 \\times 10^{23}\\) elementary entities.

### 2. Physical Context & Practical Illustration:
Named in honor of Italian scientist Amedeo Avogadro, this constant bridges the atomic scale and the macroscopic laboratory scale. If you weigh out \\(12\\text{ g}\\) of pure Carbon-12 or \\(18\\text{ g}\\) of pure water, you are holding precisely \\(6.022 \\times 10^{23}\\) particles.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The exponent is \\(10^{24}\\), an order of magnitude too large.
- **Option B is incorrect**: The exponent is \\(10^{22}\\), an order of magnitude too small.
- **Option C is incorrect**: Shifts the decimal point incorrectly (\\(60.22 \\times 10^{23} = 6.022 \\times 10^{24}\\)).
- **Option D is correct**: Standard Avogadro constant value is \\(6.022 \\times 10^{23}\\text{ mol}^{-1}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-010",
    text: "All samples of carbon dioxide (\\(\\text{CO}_2\\)), whether prepared in a laboratory or obtained from natural sources, contain carbon and oxygen combined in a fixed mass ratio of 3:8. This experimental fact validates which fundamental chemical law?",
    options: [
      "Law of Conservation of Mass",
      "Law of Constant (Definite) Proportions",
      "Law of Multiple Proportions",
      "Law of Reciprocal Proportions"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Law of Constant Proportions** (formulated by Joseph Proust in 1799) states:
> *"In a pure chemical compound, the constituent elements are always combined together in a fixed, definite proportion by mass, irrespective of the method of preparation or the source from which it was obtained."*

For carbon dioxide (\\(\\text{CO}_2\\)):
\\[
\\text{Mass of Carbon} = 12\\text{ u}, \\quad \\text{Mass of Oxygen} = 2 \\times 16 = 32\\text{ u}
\\]
\\[
\\text{Mass Ratio } \\text{C} : \\text{O} = \\frac{12}{32} = \\frac{3}{8}
\\]
Every sample of pure \\(\\text{CO}_2\\) contains carbon and oxygen in the fixed mass ratio of \\(3 : 8\\).

### 2. Physical Context & Practical Illustration:
Whether carbon dioxide is collected from human respiration, burning fossil fuels, decomposing limestone, or the reaction of vinegar and baking soda, decomposing \\(11\\text{ g}\\) of \\(\\text{CO}_2\\) will always yield exactly \\(3\\text{ g}\\) of carbon and \\(8\\text{ g}\\) of oxygen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Law of Conservation of Mass states total mass remains unchanged during chemical reactions.
- **Option B is correct**: Constant mass ratio in a compound is the defining principle of the Law of Constant Proportions.
- **Option C is incorrect**: The Law of Multiple Proportions applies when two elements form more than one compound (e.g. CO and CO₂).
- **Option D is incorrect**: The Law of Reciprocal Proportions involves ratios between three different elements.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-011",
    text: "Which of the following given samples contains the LARGEST total number of molecules? (Molar masses: \\(\\text{H}_2 = 2\\text{ g/mol}\\), \\(\\text{H}_2\\text{O} = 18\\text{ g/mol}\\), \\(\\text{CO}_2 = 44\\text{ g/mol}\\))",
    options: [
      "\\(0.2\\text{ moles of } \\text{H}_2\\)",
      "\\(0.8\\text{ g of } \\text{H}_2\\)",
      "\\(17\\text{ g of } \\text{H}_2\\text{O}\\)",
      "\\(6.0\\text{ g of } \\text{CO}_2\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of molecules is directly proportional to the number of moles (\\(N = n \\times N_A\\)). We calculate moles (\\(n = m / M\\)) for each option:
- **Option A**: \\(n = 0.2\\text{ mol}\\)
- **Option B**: \\(n = \\frac{0.8\\text{ g}}{2\\text{ g/mol}} = 0.4\\text{ mol}\\)
- **Option C**: \\(n = \\frac{17\\text{ g}}{18\\text{ g/mol}} \\approx 0.944\\text{ mol}\\)
- **Option D**: \\(n = \\frac{6.0\\text{ g}}{44\\text{ g/mol}} \\approx 0.136\\text{ mol}\\)

Comparing the moles:
\\[
0.944\\text{ mol (\\(\\text{H}_2\\text{O}\\))} > 0.4\\text{ mol (\\(\\text{H}_2\\))} > 0.2\\text{ mol (\\(\\text{H}_2\\))} > 0.136\\text{ mol (\\(\\text{CO}_2\\))}
\\]
Therefore, \\(17\\text{ g}\\) of \\(\\text{H}_2\\text{O}\\) contains the largest number of molecules (\\(\\approx 0.944 N_A \\approx 5.68 \\times 10^{23}\\) molecules).

### 2. Physical Context & Practical Illustration:
Because water has a relatively low molar mass (\\(18\\text{ g/mol}\\)), \\(17\\text{ g}\\) represents nearly a full mole (\\(0.944\\) mole) of substance, far surpassing the mole counts of the smaller gram quantities given.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Contains \\(0.2 N_A = 1.204 \\times 10^{23}\\) molecules.
- **Option B is incorrect**: Contains \\(0.4 N_A = 2.409 \\times 10^{23}\\) molecules.
- **Option C is correct**: Contains \\(0.944 N_A = 5.68 \\times 10^{23}\\) molecules, the largest among all options.
- **Option D is incorrect**: Contains \\(0.136 N_A = 8.21 \\times 10^{22}\\) molecules.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-012",
    text: "What is the total number of Helium atoms present in \\(8\\text{ g}\\) of pure Helium gas? (Given: atomic mass of \\(\\text{He} = 4\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(3.011 \\times 10^{23}\\text{ atoms}\\)",
      "\\(1.2044 \\times 10^{24}\\text{ atoms}\\)",
      "\\(2.4088 \\times 10^{24}\\text{ atoms}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Helium (He) is a noble gas that exists naturally as a monoatomic gas (atomicity = 1).
1. **Molar Mass of Helium**: \\(M = 4\\text{ g/mol}\\).
2. **Number of Moles (or gram-atoms)**:
\\[
n = \\frac{m}{M} = \\frac{8\\text{ g}}{4\\text{ g/mol}} = 2\\text{ moles (2 gram-atoms)}
\\]
3. **Number of Helium Atoms**:
\\[
N = n \\times N_A = 2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
Since one mole of helium atoms has a mass of \\(4\\text{ g}\\) and contains \\(6.022 \\times 10^{23}\\) atoms, doubling the mass to \\(8\\text{ g}\\) exactly doubles the atomic count to \\(1.2044 \\times 10^{24}\\) atoms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Corresponds to only 1 mole (\\(4\\text{ g}\\)) of Helium.
- **Option B is incorrect**: Corresponds to \\(0.5\\) moles (\\(2\\text{ g}\\)) of Helium.
- **Option C is correct**: \\(N = 2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\text{ atoms}\\).
- **Option D is incorrect**: Corresponds to 4 moles (\\(16\\text{ g}\\)) of Helium.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-013",
    text: "How many oxygen molecules (\\(\\text{O}_2\\)) are present in a \\(6.4\\text{ g}\\) sample of oxygen gas? (Given: atomic mass of \\(\\text{O} = 16\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(6.022 \\times 10^{23}\\text{ molecules}\\)",
      "\\(6.022 \\times 10^{22}\\text{ molecules}\\)",
      "\\(1.2044 \\times 10^{23}\\text{ molecules}\\)",
      "\\(1.2044 \\times 10^{22}\\text{ molecules}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Oxygen Gas (\\(\\text{O}_2\\))**:
\\[
M = 2 \\times 16 = 32\\text{ g/mol}
\\]
2. **Number of Moles of \\(\\text{O}_2\\)**:
\\[
n = \\frac{m}{M} = \\frac{6.4\\text{ g}}{32\\text{ g/mol}} = 0.2\\text{ mol}
\\]
3. **Number of \\(\\text{O}_2\\) Molecules**:
\\[
N = n \\times N_A = 0.2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{23}\\text{ molecules}
\\]

### 2. Physical Context & Practical Illustration:
Oxygen gas molecules are diatomic. In \\(6.4\\text{ g}\\) of oxygen gas, there are \\(1.2044 \\times 10^{23}\\) diatomic molecules, which correspond to \\(2 \\times (1.2044 \\times 10^{23}) = 2.4088 \\times 10^{23}\\) individual oxygen atoms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Corresponds to 1 mole (\\(32\\text{ g}\\)) of oxygen gas.
- **Option B is incorrect**: Corresponds to \\(0.1\\) mole (\\(3.2\\text{ g}\\)) of oxygen gas.
- **Option C is correct**: \\(N = 0.2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{23}\\text{ molecules}\\).
- **Option D is incorrect**: Involves an exponent error (\\(10^{22}\\) instead of \\(10^{23}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-014",
    text: "When two chemical elements combine to form more than one distinct compound, the masses of one element that combine with a fixed mass of the other element are in the ratio of small whole numbers. This fundamental law is known as the:",
    options: [
      "Law of Constant Proportions",
      "Law of Multiple Proportions",
      "Law of Reciprocal Proportions",
      "Law of Conservation of Mass"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Law of Multiple Proportions** was formulated by John Dalton in 1803:
> *"When two elements combine to form two or more different chemical compounds, the different masses of one element that combine with a fixed mass of the other element are in a ratio of simple whole numbers."*

Example with Carbon and Oxygen:
1. In Carbon Monoxide (CO): \\(12\\text{ g}\\) of Carbon combines with \\(16\\text{ g}\\) of Oxygen.
2. In Carbon Dioxide (\\(\\text{CO}_2\\)): \\(12\\text{ g}\\) of Carbon combines with \\(32\\text{ g}\\) of Oxygen.
Comparing the masses of Oxygen combining with a fixed mass (\\(12\\text{ g}\\)) of Carbon:
\\[
\\text{Ratio of Oxygen masses} = \\frac{16\\text{ g}}{32\\text{ g}} = \\frac{1}{2} = 1 : 2
\\]
This simple integer ratio (1:2) directly proves the atomic nature of matter.

### 2. Physical Context & Practical Illustration:
Similarly, Nitrogen and Oxygen combine to form five distinct oxides (\\(\\text{N}_2\\text{O}\\), \\(\\text{NO}\\), \\(\\text{N}_2\\text{O}_3\\), \\(\\text{NO}_2\\), \\(\\text{N}_2\\text{O}_5\\)), where oxygen masses combining with a fixed mass of nitrogen follow the exact integer ratio 1:2:3:4:5.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Law of Constant Proportions applies to the fixed composition of a single compound.
- **Option B is correct**: The Law of Multiple Proportions governs different compounds formed by the same pair of elements.
- **Option C is incorrect**: The Law of Reciprocal Proportions involves three distinct elements.
- **Option D is incorrect**: The Law of Conservation of Mass states mass cannot be created or destroyed.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-015",
    text: "What is the molecular mass of Acetic Acid (\\(\\text{CH}_3\\text{COOH}\\))? (Atomic masses: \\(\\text{C} = 12\\text{ u}\\), \\(\\text{H} = 1\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(46\\text{ u}\\)",
      "\\(48\\text{ u}\\)",
      "\\(60\\text{ u}\\)",
      "\\(68\\text{ u}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The molecular formula of acetic acid is \\(\\text{CH}_3\\text{COOH}\\), containing:
- Carbon atoms: \\(2\\)
- Hydrogen atoms: \\(4\\)
- Oxygen atoms: \\(2\\)

Summing the atomic masses:
\\[
M = (2 \\times A_r(\\text{C})) + (4 \\times A_r(\\text{H})) + (2 \\times A_r(\\text{O}))
\\]
\\[
M = (2 \\times 12) + (4 \\times 1) + (2 \\times 16)
\\]
\\[
M = 24 + 4 + 32 = 60\\text{ u}
\\]
Its molar mass is correspondingly \\(60\\text{ g/mol}\\).

### 2. Physical Context & Practical Illustration:
Acetic acid is the active acidic component of household vinegar (a \\(4\\% - 8\\%\\) aqueous solution). In laboratory stoichiometric calculations, \\(60\\text{ g}\\) represents exactly one mole of pure glacial acetic acid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(46\\text{ u}\\) is the molecular mass of ethanol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\)) or formic acid (\\(\\text{HCOOH}\\)).
- **Option B is incorrect**: \\(48\\text{ u}\\) is an arithmetic miscalculation omitting hydrogen.
- **Option C is correct**: \\(M = 24 + 4 + 32 = 60\\text{ u}\\).
- **Option D is incorrect**: \\(68\\text{ u}\\) incorrectly adds an extra oxygen atom.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-016",
    text: "Which of the following given samples possesses the GREATEST total mass? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{N} = 14\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(10^{23}\\text{ molecules of } \\text{H}_2\\)",
      "\\(1\\text{ mole of } \\text{H}_2\\text{O}\\)",
      "\\(1\\text{ mole of } \\text{N}_2\\)",
      "\\(10^{22}\\text{ atoms of oxygen}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We calculate the actual mass in grams for each option:
- **Option A (\\(10^{23}\\) molecules of \\(\\text{H}_2\\))**:
\\[
m = \\frac{10^{23}}{6.022 \\times 10^{23}} \\times 2\\text{ g/mol} \\approx 0.166 \\times 2 = 0.332\\text{ g}
\\]
- **Option B (\\(1\\text{ mole of } \\text{H}_2\\text{O}\\))**:
\\[
m = 1 \\times 18\\text{ g/mol} = 18\\text{ g}
\\]
- **Option C (\\(1\\text{ mole of } \\text{N}_2\\))**:
\\[
m = 1 \\times (2 \\times 14)\\text{ g/mol} = 28\\text{ g}
\\]
- **Option D (\\(10^{22}\\) atoms of oxygen)**:
\\[
m = \\frac{10^{22}}{6.022 \\times 10^{23}} \\times 16\\text{ g/mol} \\approx 0.0166 \\times 16 = 0.266\\text{ g}
\\]

Comparing masses:
\\[
28\\text{ g (\\(\\text{N}_2\\))} > 18\\text{ g (\\(\\text{H}_2\\text{O}\\))} > 0.332\\text{ g (\\(\\text{H}_2\\))} > 0.266\\text{ g (O)}
\\]
Therefore, \\(1\\text{ mole of } \\text{N}_2\\) (\\(28\\text{ g}\\)) weighs the most.

### 2. Physical Context & Practical Illustration:
Molar mass plays a decisive role: even though \\(1\\text{ mole of } \\text{H}_2\\text{O}\\) and \\(1\\text{ mole of } \\text{N}_2\\) contain the exact same number of molecules (\\(6.022 \\times 10^{23}\\)), each nitrogen molecule has a mass of \\(28\\text{ u}\\) compared to water's \\(18\\text{ u}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Weighs only \\(\\approx 0.33\\text{ g}\\).
- **Option B is incorrect**: Weighs \\(18\\text{ g}\\), which is less than \\(28\\text{ g}\\).
- **Option C is correct**: Weighs \\(28\\text{ g}\\), the greatest mass among all choices.
- **Option D is incorrect**: Weighs only \\(\\approx 0.27\\text{ g}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-017",
    text: "Which of the following is the correct chemical formula for the compound Ammonium Hydroxide?",
    options: [
      "\\(\\text{NH}_3\\text{OH}\\)",
      "\\(\\text{NH}_4\\text{OH}\\)",
      "\\(\\text{NH}(\\text{OH})_2\\)",
      "\\(\\text{N}_2\\text{H}_4\\text{OH}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Ammonium hydroxide is formed by the combination of two polyatomic composite radicals:
1. **Ammonium basic radical (cation)**: \\(\\text{NH}_4^+\\) with valency \\(+1\\).
2. **Hydroxide acidic radical (anion)**: \\(\\text{OH}^-\\) with valency \\(-1\\).

Using the criss-cross method for formula writing:
- Symbols: \\(\\text{NH}_4\\) and \\(\\text{OH}\\)
- Valencies: \\(1\\) and \\(1\\)
- Cross-multiplying: \\((\\text{NH}_4)_1(\\text{OH})_1 \\implies \\mathbf{\\text{NH}_4\\text{OH}}\\).

### 2. Physical Context & Practical Illustration:
Ammonium hydroxide (commonly known as ammonia water or household ammonia) forms when ammonia gas (\\(\\text{NH}_3\\)) dissolves in water: \\(\\text{NH}_3 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4^+ + \\text{OH}^-\\). It is a weak base widely used in window cleaning solutions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{NH}_3\\text{OH}\\) is chemically invalid; \\(\\text{NH}_3\\) is neutral ammonia, not the ammonium radical.
- **Option B is correct**: \\(\\text{NH}_4\\text{OH}\\) correctly combines the ammonium ion (\\(\\text{NH}_4^+\\)) and hydroxide ion (\\(\\text{OH}^-\\)).
- **Option C is incorrect**: Implies an imaginary divalent \\(\\text{NH}^{2+}\\) radical.
- **Option D is incorrect**: Incorporates hydrazine (\\(\\text{N}_2\\text{H}_4\\)) formula incorrectly.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-018",
    text: "Which of the following represents the correct chemical formula and charge of the Nitrate radical?",
    options: [
      "\\(\\text{NO}_3^-\\)",
      "\\(\\text{N}^{2-}\\)",
      "\\(\\text{NO}_2^-\\)",
      "\\(\\text{N}^{3-}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A radical is an atom or a group of atoms carrying an electric charge that acts as a single unit in chemical reactions:
- **Nitrate radical**: A composite polyatomic oxyanion consisting of one nitrogen atom covalently bonded to three oxygen atoms, carrying an overall net charge of \\(-1\\):
\\[
\\mathbf{\\text{NO}_3^-} \\quad (\\text{Valency } = 1)
\\]
- In contrast, \\(\\text{NO}_2^-\\) is the *nitrite* radical.
- \\(\\text{N}^{3-}\\) is the simple monoatomic *nitride* ion.

### 2. Physical Context & Practical Illustration:
The nitrate radical forms vital soluble salts such as potassium nitrate (\\(\\text{KNO}_3\\), saltpetre) and sodium nitrate (\\(\\text{NaNO}_3\\)), which are indispensable agricultural nitrogenous fertilizers.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\text{NO}_3^-\\) is the nitrate radical with a valency of 1.
- **Option B is incorrect**: Non-existent simple nitrogen ion.
- **Option C is incorrect**: \\(\\text{NO}_2^-\\) is the nitrite ion, not nitrate.
- **Option D is incorrect**: \\(\\text{N}^{3-}\\) is the nitride ion.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-019",
    text: "Which of the following represents the correct chemical formula and ionic charge of the Phosphate radical?",
    options: [
      "\\(\\text{PO}_3^{3-}\\)",
      "\\(\\text{PO}_4^{3-}\\)",
      "\\(\\text{P}_2\\text{O}_5^{2-}\\)",
      "\\(\\text{PO}_4^{2-}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **phosphate radical** is a trivalent polyatomic oxyanion derived from phosphoric acid (\\(\\text{H}_3\\text{PO}_4\\)):
\\[
\\text{H}_3\\text{PO}_4 \\longrightarrow 3\\text{H}^+ + \\mathbf{\\text{PO}_4^{3-}}
\\]
It consists of one central phosphorus atom coordinated tetrahedrally to four oxygen atoms, possessing a net electric charge of \\(-3\\) and a valency of \\(3\\).

### 2. Physical Context & Practical Illustration:
Phosphate groups form the structural mineral component of human bones and teeth (calcium phosphate, \\(\\text{Ca}_3(\\text{PO}_4)_2\\)) and constitute the energy-transfer backbone of life (adenosine triphosphate, ATP) and DNA/RNA molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{PO}_3^{3-}\\) is the phosphite radical.
- **Option B is correct**: \\(\\text{PO}_4^{3-}\\) is the phosphate radical with a valency of 3.
- **Option C is incorrect**: \\(\\text{P}_2\\text{O}_5\\) is phosphorus pentoxide, a neutral molecular compound.
- **Option D is incorrect**: \\(\\text{PO}_4^{2-}\\) has an incorrect ionic charge (it is trivalent, \\(-3\\), not \\(-2\\); \\(\\text{HPO}_4^{2-}\\) is hydrogen phosphate).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-020",
    text: "\"In a pure chemical compound, the constituent elements are always present in a definite proportion by mass.\" This statement is the formal definition of the:",
    options: [
      "Law of Conservation of Energy",
      "Law of Conservation of Mass",
      "Law of Constant (Definite) Proportions",
      "Law of Combining Volumes"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The statement defines the **Law of Constant Proportions** (also called the Law of Definite Proportions or Proust's Law), enunciated by French chemist Joseph Louis Proust in 1799:
\\[
\\frac{m_A}{m_B} = \\text{constant for a given pure compound}
\\]
For example, pure water (\\(\\text{H}_2\\text{O}\\)) always contains hydrogen and oxygen in the fixed mass ratio:
\\[
\\frac{m_{\\text{H}}}{m_{\\text{O}}} = \\frac{2 \\times 1}{16} = \\frac{1}{8}
\\]
Regardless of whether water is collected from rain, rivers, meltwater, or chemical synthesis, \\(9\\text{ g}\\) of water decomposes into exactly \\(1\\text{ g}\\) of hydrogen and \\(8\\text{ g}\\) of oxygen.

### 2. Physical Context & Practical Illustration:
This law established chemistry as a quantitative exact science, proving that compounds have fixed chemical formulas rather than variable, arbitrary mixtures of elements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Law of Conservation of Energy states energy cannot be created or destroyed.
- **Option B is incorrect**: The Law of Conservation of Mass states total mass before and after a chemical reaction is identical.
- **Option C is correct**: This is the exact textbook statement of the Law of Constant Proportions.
- **Option D is incorrect**: Gay-Lussac's Law of Combining Volumes deals with reacting gas volumes.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-021",
    text: "How many molecules are present in \\(0.25\\text{ moles}\\) of methane gas (\\(\\text{CH}_4\\))? (Given: \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(1.5055 \\times 10^{22}\\text{ molecules}\\)",
      "\\(3.011 \\times 10^{23}\\text{ molecules}\\)",
      "\\(1.5055 \\times 10^{23}\\text{ molecules}\\)",
      "\\(2.4088 \\times 10^{23}\\text{ molecules}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition, one mole of any molecular substance contains Avogadro's number (\\(N_A\\)) of molecules:
\\[
N = n \\times N_A
\\]
Given:
- Number of moles \\(n = 0.25\\text{ mol} = \\frac{1}{4}\\text{ mol}\\)
- \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\)

Calculate the number of molecules:
\\[
N = 0.25 \\times 6.022 \\times 10^{23} = \\frac{6.022 \\times 10^{23}}{4} = 1.5055 \\times 10^{23}\\text{ molecules}
\\]

### 2. Physical Context & Practical Illustration:
Methane (\\(\\text{CH}_4\\)) is the principal component of natural gas and biogas. A quantity of \\(0.25\\text{ moles}\\) corresponds to \\(0.25 \\times 16\\text{ g/mol} = 4\\text{ g}\\) of methane gas, which contains approximately \\(150\\text{ sextillion}\\) methane molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Involves a decimal order-of-magnitude error (\\(10^{22}\\) instead of \\(10^{23}\\)).
- **Option B is incorrect**: \\(3.011 \\times 10^{23}\\) corresponds to \\(0.5\\text{ moles}\\) (half a mole).
- **Option C is correct**: \\(N = 0.25 \\times 6.022 \\times 10^{23} = 1.5055 \\times 10^{23}\\text{ molecules}\\).
- **Option D is incorrect**: \\(2.4088 \\times 10^{23}\\) corresponds to \\(0.4\\text{ moles}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-022",
    text: "Sodium chloride has a mass of \\(58.5\\text{ u}\\) calculated from \\(\\text{Na} (23\\text{ u}) + \\text{Cl} (35.5\\text{ u})\\). Because sodium chloride does not consist of discrete molecules but a continuous ionic crystal lattice, this mass value is most accurately termed its:",
    options: [
      "Atomic mass",
      "Formula unit mass",
      "Isotopic mass",
      "Equivalent mass"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In ionic compounds (such as \\(\\text{NaCl}\\)), discrete single molecules do not exist. Instead, positive cations (\\(\\text{Na}^+\\)) and negative anions (\\(\\text{Cl}^-\\)) are arranged in a continuous, three-dimensional cubic crystal lattice where each \\(\\text{Na}^+\\) ion is octahedrally surrounded by six \\(\\text{Cl}^-\\) ions, and vice-versa.
Because there is no discrete single molecule of NaCl:
\\[
\\text{Formula Unit Mass} = \\sum \\text{Atomic masses of all atoms in the simplest empirical formula}
\\]
\\[
\\text{Formula Unit Mass of NaCl} = 23 + 35.5 = 58.5\\text{ u}
\\]
Chemists term this the **formula unit mass** rather than molecular mass.

### 2. Physical Context & Practical Illustration:
While 'molecular mass' is technically used for covalent substances with discrete molecules (like \\(\\text{H}_2\\text{O}\\), \\(\\text{CH}_4\\), \\(\\text{CO}_2\\)), 'formula mass' is the scientifically precise nomenclature for giant ionic networks like \\(\\text{NaCl}\\), \\(\\text{CaCO}_3\\), and \\(\\text{MgO}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Atomic mass applies to an individual element's atom, not a multi-element compound.
- **Option B is correct**: Formula unit mass is the exact scientific term for the sum of atomic masses in an ionic compound formula.
- **Option C is incorrect**: Isotopic mass refers to a specific individual isotope of an element.
- **Option D is incorrect**: Equivalent mass is molecular mass divided by valency/n-factor.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-023",
    text: "How many magnesium atoms are present in a \\(36\\text{ g}\\) ribbon of pure Magnesium metal? (Given: atomic mass of \\(\\text{Mg} = 24\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(9.033 \\times 10^{22}\\text{ atoms}\\)",
      "\\(9.033 \\times 10^{23}\\text{ atoms}\\)",
      "\\(1.2044 \\times 10^{24}\\text{ atoms}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Magnesium**: \\(M = 24\\text{ g/mol}\\).
2. **Number of Moles of Magnesium**:
\\[
n = \\frac{m}{M} = \\frac{36\\text{ g}}{24\\text{ g/mol}} = 1.5\\text{ mol}
\\]
3. **Number of Atoms**:
\\[
N = n \\times N_A = 1.5 \\times 6.022 \\times 10^{23} = 9.033 \\times 10^{23}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
A \\(36\\text{ g}\\) strip of magnesium ribbon contains one and a half moles of magnesium. When burned in air, these \\(9.033 \\times 10^{23}\\) magnesium atoms react with oxygen to form a brilliant white powder of magnesium oxide (\\(\\text{MgO}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Corresponds to exactly 1 mole (\\(24\\text{ g}\\)) of magnesium.
- **Option B is incorrect**: Has an incorrect exponent (\\(10^{22}\\) instead of \\(10^{23}\\)).
- **Option C is correct**: \\(N = 1.5 \\times 6.022 \\times 10^{23} = 9.033 \\times 10^{23}\\text{ atoms}\\).
- **Option D is incorrect**: Corresponds to 2 moles (\\(48\\text{ g}\\)) of magnesium.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-024",
    text: "When \\(10\\text{ g}\\) of calcium carbonate (\\(\\text{CaCO}_3\\)) is heated strongly, it decomposes completely to yield \\(5.6\\text{ g}\\) of solid calcium oxide (\\(\\text{CaO}\\)) and \\(4.4\\text{ g}\\) of carbon dioxide gas (\\(\\text{CO}_2\\)). This experimental observation verified which fundamental law?",
    options: [
      "Law of Constant Proportions",
      "Law of Multiple Proportions",
      "Law of Reciprocal Proportions",
      "Law of Conservation of Mass"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Law of Conservation of Mass** (formulated by Antoine Lavoisier in 1774) states:
> *"Matter can neither be created nor destroyed in a chemical reaction. The total mass of the products formed is always exactly equal to the total mass of the reactants consumed."*

In the thermal decomposition of calcium carbonate:
\\[
\\text{CaCO}_{3(s)} \\xrightarrow{\\Delta} \\text{CaO}_{(s)} + \\text{CO}_{2(g)}
\\]
- **Total mass of reactant**:
\\[
m_{\\text{reactant}} = m(\\text{CaCO}_3) = 10.0\\text{ g}
\\]
- **Total mass of products**:
\\[
m_{\\text{products}} = m(\\text{CaO}) + m(\\text{CO}_2) = 5.6\\text{ g} + 4.4\\text{ g} = 10.0\\text{ g}
\\]
Since \\(m_{\\text{reactant}} = m_{\\text{products}} = 10.0\\text{ g}\\), mass is perfectly conserved.

### 2. Physical Context & Practical Illustration:
Before Lavoisier conducted closed-system experiments, scientists thought mass was lost when gases evolved because the gas escaped unnoticed into the room. Trapping and weighing the evolved \\(\\text{CO}_2\\) proves that mass balance is strictly preserved.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Law of Constant Proportions concerns the mass ratios of elements within each compound.
- **Option B is incorrect**: The Law of Multiple Proportions applies to multiple compounds formed by the same elements.
- **Option C is incorrect**: The Law of Reciprocal Proportions involves three distinct elements.
- **Option D is correct**: Total mass of reactants equals total mass of products (\\(10.0\\text{ g} = 5.6\\text{ g} + 4.4\\text{ g}\\)), proving Conservation of Mass.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-025",
    text: "Given that the relative atomic mass of Argon is \\(40\\text{ u}\\), what is the molecular mass of Argon gas (Ar)?",
    options: [
      "\\(40\\text{ u}\\)",
      "\\(80\\text{ u}\\)",
      "\\(60\\text{ u}\\)",
      "\\(20\\text{ u}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Argon (Ar) is an inert noble gas with a stable electronic octet configuration (\\(2, 8, 8\\)).
Because its valence shell is completely filled, argon atoms have zero chemical combining capacity and do not bond with each other:
- Argon exists as an independent, single-atom molecule: it is strictly **monoatomic** (atomicity = 1).
- Therefore, its molecular mass is identical to its atomic mass:
\\[
M(\\text{Ar}) = 1 \\times A_r(\\text{Ar}) = 1 \\times 40\\text{ u} = 40\\text{ u}
\\]

### 2. Physical Context & Practical Illustration:
All noble gases (Helium, Neon, Argon, Krypton, Xenon, Radon) exist as monoatomic gases under standard conditions. Unlike reactive gases (\\(\\text{O}_2\\), \\(\\text{N}_2\\), \\(\\text{H}_2\\)), argon does not form diatomic molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Argon is monoatomic (atomicity = 1); its molecular mass equals its atomic mass (\\(40\\text{ u}\\)).
- **Option B is incorrect**: \\(80\\text{ u}\\) erroneously assumes argon is diatomic like oxygen (\\(\\text{Ar}_2\\)).
- **Option C is incorrect**: Arbitrary value.
- **Option D is incorrect**: \\(20\\text{ u}\\) is the atomic mass of Neon.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-026",
    text: "Which of the following represents the correct chemical formula and charge of the Sulfate radical?",
    options: [
      "\\(\\text{SO}_3^{2-}\\)",
      "\\(\\text{SO}_4^{2-}\\)",
      "\\(\\text{S}^{2-}\\)",
      "\\(\\text{HSO}_4^-\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **sulfate radical** is a divalent polyatomic oxyanion derived from sulfuric acid (\\(\\text{H}_2\\text{SO}_4\\)):
\\[
\\text{H}_2\\text{SO}_4 \\longrightarrow 2\\text{H}^+ + \\mathbf{\\text{SO}_4^{2-}}
\\]
- It comprises one sulfur atom bonded to four oxygen atoms with an overall electric charge of \\(-2\\) (valency = 2).
- Distinctions among sulfur-bearing radicals:
  - Sulfate: \\(\\text{SO}_4^{2-}\\)
  - Sulfite: \\(\\text{SO}_3^{2-}\\)
  - Sulfide: \\(\\text{S}^{2-}\\) (simple monoatomic ion)
  - Bisulfate / Hydrogen sulfate: \\(\\text{HSO}_4^-\\)\\

### 2. Physical Context & Practical Illustration:
The sulfate radical forms many stable mineral salts essential to industry and everyday life, such as copper sulfate pentahydrate (\\(CuSO_4 \\cdot 5H_2O\\), blue vitriol), calcium sulfate dihydrate (\\(CaSO_4 \\cdot 2H_2O\\), gypsum), and magnesium sulfate heptahydrate (\\(MgSO_4 \\cdot 7H_2O\\), Epsom salt). In aqueous testing, the sulfate radical produces a characteristic white precipitate of barium sulfate (\\(BaSO_4\\)) upon addition of barium chloride solution, insoluble in dilute acids.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(\\text{SO}_3^{2-}\\)):** Incorrect. This is the sulfite radical derived from sulfurous acid (\\(H_2SO_3\\)).
- **Option B (\\(\\text{SO}_4^{2-}\\)):** Correct. The sulfate radical consists of one sulfur atom and four oxygen atoms bearing a net charge of \\(-2\\).
- **Option C (\\(\\text{S}^{2-}\\)):** Incorrect. This is the simple monoatomic sulfide ion formed when a sulfur atom gains two electrons.
- **Option D (\\(\\text{HSO}_4^-\\)):** Incorrect. This is the monovalent bisulfate (hydrogen sulfate) radical.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-027",
    text: "Which of the following chemical formulas represents a chemically correct and electrically neutral compound?",
    options: [
      "\\(\\text{CaCl}\\)",
      "\\(\\text{BiPO}_4\\)",
      "\\(\\text{NaSO}_4\\)",
      "\\(\\text{NaS}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A valid chemical formula must satisfy electrical neutrality: total positive charges from cations must equal total negative charges from anions:
- **Option A (\\(\\text{CaCl}\\))**: \\(\\text{Ca}^{2+}\\) has valency 2, \\(\\text{Cl}^-\\) has valency 1. Correct formula is \\(\\text{CaCl}_2\\).
- **Option B (\\(\\text{BiPO}_4\\))**: Bismuth forms bismuth(III) cation \\(\\text{Bi}^{3+}\\) (valency 3), and phosphate is \\(\\text{PO}_4^{3-}\\) (valency 3). Equal valencies cancel (3:3 = 1:1), yielding \\(\\mathbf{\\text{BiPO}_4}\\) (Bismuth Phosphate), which is electrically neutral and chemically correct!
- **Option C (\\(\\text{NaSO}_4\\))**: \\(\\text{Na}^+\\) has valency 1, \\(\\text{SO}_4^{2-}\\) has valency 2. Correct formula is \\(\\text{Na}_2\\text{SO}_4\\).
- **Option D (\\(\\text{NaS}\\))**: \\(\\text{Na}^+\\) has valency 1, \\(\\text{S}^{2-}\\) has valency 2. Correct formula is \\(\\text{Na}_2\\text{S}\\).

### 2. Physical Context & Practical Illustration:
Bismuth phosphate (\\(\\text{BiPO}_4\\)) is an extremely insoluble crystalline compound historically used in radiochemistry and the Manhattan Project (Bismuth Phosphate process) to precipitate and separate plutonium from uranium.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Calcium chloride is \\(\\text{CaCl}_2\\).
- **Option B is correct**: \\(\\text{Bi}^{3+}\\) and \\(\\text{PO}_4^{3-}\\) balance in a 1:1 stoichiometric ratio to form \\(\\text{BiPO}_4\\).
- **Option C is incorrect**: Sodium sulfate is \\(\\text{Na}_2\\text{SO}_4\\).
- **Option D is incorrect**: Sodium sulfide is \\(\\text{Na}_2\\text{S}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-028",
    text: "Which scientific law states that a given chemical compound always contains its constituent elements in an identical, fixed proportion by mass regardless of where or how it was prepared?",
    options: [
      "Dalton's Atomic Theory",
      "Law of Conservation of Mass",
      "Avogadro's Hypothesis",
      "Law of Definite (Constant) Proportions"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Law of Definite Proportions** (or Constant Proportions), discovered experimentally by Joseph Louis Proust in 1799, establishes:
\\[
\\text{Mass Ratio of Elements in Compound } AB = \\frac{m_A}{m_B} = \\text{invariant constant}
\\]
For example, pure sodium chloride (table salt) always consists of \\(39.34\\%\\) sodium and \\(60.66\\%\\) chlorine by mass, whether mined from ancient underground rock formations or synthesized directly by reacting sodium metal with chlorine gas.

### 2. Physical Context & Practical Illustration:
If you react \\(1.0\\text{ g}\\) of hydrogen with \\(10.0\\text{ g}\\) of oxygen, only \\(8.0\\text{ g}\\) of oxygen will combine (forming \\(9.0\\text{ g}\\) of water), leaving \\(2.0\\text{ g}\\) of unreacted oxygen gas behind, because the chemical stoichiometry strictly demands a fixed 1:8 mass ratio.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Dalton's atomic theory provides the theoretical model explaining why these laws occur, but the empirical statement itself is Proust's law.
- **Option B is incorrect**: Conservation of mass relates total reactant mass to total product mass.
- **Option C is incorrect**: Avogadro's hypothesis relates gas volume to number of molecules at equal temperature and pressure.
- **Option D is correct**: This is the formal scientific statement of the Law of Definite (Constant) Proportions.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-029",
    text: "The respective atomic numbers of four elements P, Q, R, and S are 6, 9, 12, and 17. Which two elements have the exact same number of valence electrons in their outermost shells?",
    options: [
      "Elements P and R",
      "Elements P and Q",
      "Elements R and S",
      "Elements Q and S"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We determine the electronic configurations of elements P, Q, R, and S from their atomic numbers (\\(Z\\)):
1. **Element P (\\(Z = 6\\), Carbon)**:
   - Electronic configuration: \\(2, 4\\)
   - Number of valence electrons = \\(\\mathbf{4}\\)
2. **Element Q (\\(Z = 9\\), Fluorine)**:
   - Electronic configuration: \\(2, 7\\)
   - Number of valence electrons = \\(\\mathbf{7}\\)
3. **Element R (\\(Z = 12\\), Magnesium)**:
   - Electronic configuration: \\(2, 8, 2\\)
   - Number of valence electrons = \\(\\mathbf{2}\\)
4. **Element S (\\(Z = 17\\), Chlorine)**:
   - Electronic configuration: \\(2, 8, 7\\)
   - Number of valence electrons = \\(\\mathbf{7}\\)

Comparing the outermost valence shells:
Both **Element Q** and **Element S** have exactly **7 valence electrons**. They belong to Group 17 (the halogens) of the periodic table.

### 2. Physical Context & Practical Illustration:
Having the same number of valence electrons endows Fluorine (Q) and Chlorine (S) with remarkably similar chemical reactivity: both need exactly 1 electron to achieve octet stability, both form monovalent halide salts (like NaF and NaCl), and both exist as diatomic non-metal gases.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: P has 4 valence electrons, while R has 2.
- **Option B is incorrect**: P has 4 valence electrons, while Q has 7.
- **Option C is incorrect**: R has 2 valence electrons, while S has 7.
- **Option D is correct**: Both Q (Fluorine) and S (Chlorine) possess 7 valence electrons.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-030",
    text: "A sample of \\(32\\text{ g}\\) of oxygen gas (\\(\\text{O}_2\\)) represents exactly how many moles of molecular oxygen? (Given: atomic mass of \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(2\\text{ moles of } \\text{O}_2\\)",
      "\\(1\\text{ mole of } \\text{O}_2\\)",
      "\\(0.5\\text{ moles of } \\text{O}_2\\)",
      "\\(4\\text{ moles of } \\text{O}_2\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Oxygen Gas (\\(\\text{O}_2\\))**:
\\[
M = 2 \\times A_r(\\text{O}) = 2 \\times 16\\text{ g/mol} = 32\\text{ g/mol}
\\]
2. **Number of Moles (\\(n\\))**:
\\[
n = \\frac{\\text{Mass in grams}}{\\text{Molar mass}} = \\frac{32\\text{ g}}{32\\text{ g/mol}} = 1\\text{ mole}
\\]
Therefore, \\(32\\text{ g}\\) of oxygen gas is precisely equal to **\\(1\\text{ mole}\\)** of \\(\\text{O}_2\\) molecules (or \\(2\\text{ moles}\\) of individual oxygen atoms).

### 2. Physical Context & Practical Illustration:
At Standard Temperature and Pressure (STP), this \\(32\\text{ g}\\) (1 mole) of oxygen gas occupies a molar volume of approximately \\(22.4\\text{ liters}\\) and contains exactly \\(6.022 \\times 10^{23}\\) diatomic molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(32\\text{ g}\\) is 2 moles of isolated oxygen *atoms* (\\(\\text{O}\\)), but only 1 mole of oxygen *molecules* (\\(\\text{O}_2\\)).
- **Option B is correct**: \\(n = 32 / 32 = 1\\text{ mole of } \\text{O}_2\\).
- **Option C is incorrect**: \\(0.5\\) moles corresponds to \\(16\\text{ g}\\) of \\(\\text{O}_2\\).
- **Option D is incorrect**: \\(4\\) moles corresponds to \\(128\\text{ g}\\) of \\(\\text{O}_2\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-031",
    text: "What is the number of moles present in a sample containing \\(3.011 \\times 10^{23}\\) molecules of oxygen gas? (Given: \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(1.0\\text{ mol}\\)",
      "\\(0.5\\text{ mol}\\)",
      "\\(2.0\\text{ mol}\\)",
      "\\(0.2\\text{ mol}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of moles (\\(n\\)) is calculated by dividing the given number of particles (\\(N\\)) by Avogadro's constant (\\(N_A\\)):
\\[
n = \\frac{N}{N_A}
\\]
Given:
- \\(N = 3.011 \\times 10^{23}\\text{ molecules}\\)
- \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\)

Substitute the values:
\\[
n = \\frac{3.011 \\times 10^{23}}{6.022 \\times 10^{23}} = \\frac{1}{2} = 0.5\\text{ mol}
\\]

### 2. Physical Context & Practical Illustration:
Half a mole of oxygen molecules (\\(0.5\\text{ mol of } \\text{O}_2\\)) has a mass of \\(0.5 \\times 32\\text{ g/mol} = 16\\text{ g}\\) and occupies \\(11.2\\text{ liters}\\) at STP.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: 1 mole corresponds to \\(6.022 \\times 10^{23}\\) molecules.
- **Option B is correct**: \\(n = 3.011 \\times 10^{23} / 6.022 \\times 10^{23} = 0.5\\text{ mol}\\).
- **Option C is incorrect**: 2 moles corresponds to \\(1.2044 \\times 10^{24}\\) molecules.
- **Option D is incorrect**: \\(0.2\\) moles corresponds to \\(1.2044 \\times 10^{23}\\) molecules.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-032",
    text: "How many moles of glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)) correspond to \\(1.5055 \\times 10^{23}\\) molecules of glucose? (Given: \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(0.025\\text{ mol}\\)",
      "\\(0.25\\text{ mol}\\)",
      "\\(2.5\\text{ mol}\\)",
      "\\(0.50\\text{ mol}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of moles (\\(n\\)) is related to the number of molecules (\\(N\\)) by:
\\[
n = \\frac{N}{N_A}
\\]
Given:
- \\(N = 1.5055 \\times 10^{23}\\)
- \\(N_A = 6.022 \\times 10^{23}\\)

Calculate \\(n\\):
\\[
n = \\frac{1.5055 \\times 10^{23}}{6.022 \\times 10^{23}} = \\frac{1.5055}{6.022} = 0.25\\text{ mol}
\\]

### 2. Physical Context & Practical Illustration:
Molar mass of glucose is \\(180\\text{ g/mol}\\). A quarter of a mole (\\(0.25\\text{ mol}\\)) represents \\(0.25 \\times 180 = 45\\text{ g}\\) of pure glucose powder, containing exactly \\(1.5055 \\times 10^{23}\\) glucose molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Involves a decimal place error by a factor of 10 (\\(0.025\\)).
- **Option B is correct**: \\(n = 1.5055 / 6.022 = 0.25\\text{ mol}\\).
- **Option C is incorrect**: Involves a misplaced decimal point (\\(2.5\\)).
- **Option D is incorrect**: \\(0.50\\) mol corresponds to \\(3.011 \\times 10^{23}\\) molecules.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-033",
    text: "Comparing \\(10\\text{ moles}\\) of atomic oxygen (O), \\(10\\text{ moles}\\) of oxygen gas (\\(\\text{O}_2\\)), and \\(10\\text{ moles}\\) of ozone gas (\\(\\text{O}_3\\)), which sample contains the largest total number of oxygen ATOMS?",
    options: [
      "\\(10\\text{ moles of } \\text{O}\\)",
      "\\(10\\text{ moles of } \\text{O}_2\\)",
      "\\(10\\text{ moles of } \\text{O}_3\\)",
      "All three samples contain the exact same number of oxygen atoms"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We calculate the total number of oxygen atoms in each sample:
1. **\\(10\\text{ moles of } \\text{O}\\)**:
   - Each entity contains 1 atom.
   - Total atoms = \\(10 \\times 1 \\times N_A = 10 N_A\\text{ atoms}\\).
2. **\\(10\\text{ moles of } \\text{O}_2\\)**:
   - Each molecule contains 2 atoms.
   - Total atoms = \\(10 \\times 2 \\times N_A = 20 N_A\\text{ atoms}\\).
3. **\\(10\\text{ moles of } \\text{O}_3\\)**:
   - Each molecule contains 3 atoms.
   - Total atoms = \\(10 \\times 3 \\times N_A = 30 N_A\\text{ atoms}\\).

Comparing total atom counts:
\\[
30 N_A (\\text{O}_3) > 20 N_A (\\text{O}_2) > 10 N_A (\\text{O})
\\]
Therefore, \\(10\\text{ moles of Ozone (\\(\\text{O}_3\\))}\\) contains the largest number of atoms (\\(30 N_A \\approx 1.8066 \\times 10^{25}\\) atoms).

### 2. Physical Context & Practical Illustration:
While all three samples contain the exact same number of *moles of molecules/particles* (\\(10 N_A\\) particles), the atomicity of ozone (3 atoms/molecule) packs 3 times as many oxygen atoms into the same molar quantity compared to atomic oxygen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Contains only \\(10 N_A\\) atoms.
- **Option B is incorrect**: Contains \\(20 N_A\\) atoms.
- **Option C is correct**: Contains \\(30 N_A\\) atoms, the highest count.
- **Option D is incorrect**: Conflates number of moles of molecules with total number of constituent atoms.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-034",
    text: "What is the molecular mass of a water molecule (\\(\\text{H}_2\\text{O}\\))? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(16\\text{ u}\\)",
      "\\(32\\text{ u}\\)",
      "\\(18\\text{ u}\\)",
      "\\(34\\text{ u}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The molecular mass of water is calculated by adding the relative atomic masses of all constituent atoms in its chemical formula \\(\\text{H}_2\\text{O}\\):
\\[
M(\\text{H}_2\\text{O}) = (2 \\times A_r(\\text{H})) + (1 \\times A_r(\\text{O}))
\\]
\\[
M(\\text{H}_2\\text{O}) = (2 \\times 1\\text{ u}) + (16\\text{ u}) = 2\\text{ u} + 16\\text{ u} = 18\\text{ u}
\\]
Its molar mass is correspondingly \\(18\\text{ g/mol}\\).

### 2. Physical Context & Practical Illustration:
A single water molecule weighs \\(18\\text{ u}\\) (\\(\\approx 2.99 \\times 10^{-26}\\text{ kg}\\)). When measuring out \\(18\\text{ grams}\\) (approximately \\(18\\text{ mL}\\)) of liquid water at room temperature, one possesses exactly one mole of water containing \\(6.022 \\times 10^{23}\\) molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(16\\text{ u}\\) is the mass of only the oxygen atom, neglecting the two hydrogen atoms.
- **Option B is incorrect**: \\(32\\text{ u}\\) is the molecular mass of oxygen gas (\\(\\text{O}_2\\)).
- **Option C is correct**: \\(M = (2 \\times 1) + 16 = 18\\text{ u}\\).
- **Option D is incorrect**: \\(34\\text{ u}\\) is the molecular mass of hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-035",
    text: "Which of the following statements regarding the fundamental concept of a 'Mole' is INCORRECT?",
    options: [
      "A mole is the SI base unit used to measure the amount of substance",
      "One mole of any chemical substance contains exactly Avogadro's number (\\(6.022 \\times 10^{23}\\)) of elementary particles",
      "The mass of one mole of a substance in grams is numerically equal to its atomic or molecular mass in unified atomic mass units (u)",
      "One mole of water (\\(\\text{H}_2\\text{O}\\)) contains the exact same total number of atoms as one mole of helium gas (He)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing the definitions of the mole:
- A mole contains exactly \\(N_A = 6.022 \\times 10^{23}\\) constituent formula units.
- **Helium (He)** is monoatomic; \\(1\\text{ mole of He}\\) contains \\(1 \\times N_A = \\mathbf{1 N_A\\text{ atoms}}\\).
- **Water (\\(\\text{H}_2\\text{O}\\))** is triatomic (2 H + 1 O); \\(1\\text{ mole of } \\text{H}_2\\text{O}\\) contains \\(N_A\\) water molecules, but:
\\[
\\text{Total Atoms in } 1\\text{ mole of } \\text{H}_2\\text{O} = 3 \\times N_A = \\mathbf{3 N_A\\text{ atoms}}
\\]
Since \\(3 N_A \\neq 1 N_A\\), asserting that they contain the same total number of atoms is fundamentally false!

### 2. Physical Context & Practical Illustration:
One mole of any substance contains the same number of *molecules* or *formula units*, but the number of *atoms* depends directly on the atomicity of the molecule. One dozen cars have the same count of vehicles as one dozen bicycles, but cars have 4 wheels each while bicycles have only 2 wheels each.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a true statement**: Mole is the official SI base unit for amount of substance.
- **Option B is a true statement**: By definition, 1 mole contains \\(6.022 \\times 10^{23}\\) entities.
- **Option C is a true statement**: Molar mass in g/mol is numerically identical to molecular mass in unified mass units (u).
- **Option D is incorrect (the correct answer to the question)**: Water contains \\(3 N_A\\) atoms per mole while helium contains only \\(1 N_A\\) atoms per mole.`
  }
];

module.exports = { ch4_part1 };
