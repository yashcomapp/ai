// scripts/ch4_part2.js - Chapter 4 (Measurement of Matter) Questions 36-70 Gold Standard Enhancements
const ch4_part2 = [
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-036",
    text: "Which of the following \\(5\\text{ g}\\) samples contains the LARGEST number of constituent atoms? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{N} = 14\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(5\\text{ g of elemental Oxygen atoms (O)}\\)",
      "\\(5\\text{ g of Water (\\(\\text{H}_2\\text{O}\\))}\\)",
      "\\(5\\text{ g of elemental Nitrogen atoms (N)}\\)",
      "\\(5\\text{ g of Carbon dioxide (\\(\\text{CO}_2\\))}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We calculate the total number of constituent atoms in each \\(5\\text{ g}\\) sample:
1. **\\(5\\text{ g of O (atomic)}\\)**:
\\[
N_{\\text{atoms}} = \\frac{5}{16} \\times N_A \\approx 0.3125 N_A
\\]
2. **\\(5\\text{ g of N (atomic)}\\)**:
\\[
N_{\\text{atoms}} = \\frac{5}{14} \\times N_A \\approx 0.357 N_A
\\]
3. **\\(5\\text{ g of } \\text{H}_2\\text{O}\\)**:
- Molar mass \\(M = 18\\text{ g/mol}\\). Moles of \\(\\text{H}_2\\text{O} = \\frac{5}{18} \\approx 0.278\\text{ mol}\\).
- Each \\(\\text{H}_2\\text{O}\\) molecule contains 3 atoms (2 H + 1 O):
\\[
N_{\\text{atoms}} = 3 \\times \\left(\\frac{5}{18}\\right) \\times N_A = \\frac{15}{18} N_A = \\frac{5}{6} N_A \\approx \\mathbf{0.833 N_A}
\\]
4. **\\(5\\text{ g of } \\text{CO}_2\\)**:
- Molar mass \\(M = 44\\text{ g/mol}\\). Each molecule contains 3 atoms:
\\[
N_{\\text{atoms}} = 3 \\times \\left(\\frac{5}{44}\\right) \\times N_A \\approx 0.341 N_A
\\]

Comparing atom counts:
\\[
0.833 N_A (\\text{H}_2\\text{O}) > 0.357 N_A (\\text{N}) > 0.341 N_A (\\text{CO}_2) > 0.3125 N_A (\\text{O})
\\]
Therefore, \\(5\\text{ g}\\) of water contains the largest total number of atoms.

### 2. Physical Context & Practical Illustration:
Water has a high proportion of extremely light hydrogen atoms (\\(1\\text{ u}\\) each). Because hydrogen atoms contribute minimal mass per particle, a given weight of water packs significantly more total individual atoms than heavier elemental samples.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Contains \\(0.3125 N_A\\) atoms.
- **Option B is correct**: Contains \\(0.833 N_A\\) atoms, the highest atomic count.
- **Option C is incorrect**: Contains \\(0.357 N_A\\) atoms.
- **Option D is incorrect**: Contains \\(0.341 N_A\\) atoms.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-037",
    text: "Which of the following molar quantities possesses the GREATEST mass in grams? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{N} = 14\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(1\\text{ mole of atomic Nitrogen (N)}\\)",
      "\\(1\\text{ mole of atomic Oxygen (O)}\\)",
      "\\(1\\text{ mole of molecular Hydrogen (\\(\\text{H}_2\\))}\\)",
      "\\(1\\text{ mole of Water (\\(\\text{H}_2\\text{O}\\))}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The mass in grams of one mole of any pure substance is numerically equal to its molar mass:
1. **\\(1\\text{ mole of atomic N}\\)**: \\(m = 1 \\times 14\\text{ g/mol} = 14\\text{ g}\\)
2. **\\(1\\text{ mole of atomic O}\\)**: \\(m = 1 \\times 16\\text{ g/mol} = 16\\text{ g}\\)
3. **\\(1\\text{ mole of molecular } \\text{H}_2\\)**: \\(m = 1 \\times 2\\text{ g/mol} = 2\\text{ g}\\)
4. **\\(1\\text{ mole of } \\text{H}_2\\text{O}\\)**: \\(m = 1 \\times (2 + 16)\\text{ g/mol} = 18\\text{ g}\\)

Comparing the masses:
\\[
18\\text{ g (\\(\\text{H}_2\\text{O}\\))} > 16\\text{ g (O)} > 14\\text{ g (N)} > 2\\text{ g (\\(\\text{H}_2\\))}
\\]
Therefore, \\(1\\text{ mole of water}\\) has the greatest mass.

### 2. Physical Context & Practical Illustration:
Each mole of these substances contains identical counts of formula units (\\(6.022 \\times 10^{23}\\)). However, because a water molecule (composed of two hydrogens and one oxygen) has the largest collective molecular mass (\\(18\\text{ u}\\)), its aggregate molar mass is the heaviest.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Weighs \\(14\\text{ g}\\).
- **Option B is incorrect**: Weighs \\(16\\text{ g}\\).
- **Option C is incorrect**: Weighs \\(2\\text{ g}\\).
- **Option D is correct**: Weighs \\(18\\text{ g}\\), the heaviest among all options.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-038",
    text: "Which specific nuclide isotope was internationally chosen by IUPAC in 1961 as the universal standard reference for determining relative atomic masses?",
    options: [
      "Hydrogen-1 (\\(^1\\text{H}\\))",
      "Carbon-12 (\\(^{12}\\text{C}\\))",
      "Oxygen-16 (\\(^{16}\\text{O}\\))",
      "Nitrogen-14 (\\(^{14}\\text{N}\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1961, the International Union of Pure and Applied Chemistry (IUPAC) established the unified atomic mass unit scale based on the **Carbon-12 (\\(^{12}\\text{C}\\)) nuclide**:
\\[
1\\text{ u} = \\frac{1}{12} \\times \\text{mass of one atom of } ^{12}\\text{C} \\approx 1.660539 \\times 10^{-27}\\text{ kg}
\\]
The Carbon-12 atom was assigned an exact relative atomic mass of \\(12.0000\\dots\\text{ u}\\).

### 2. Physical Context & Practical Illustration:
Prior to 1961, physicists used \\(^{16}\\text{O}\\) while chemists used natural atmospheric oxygen (an isotopic mixture of \\(^{16}\\text{O}\\), \\(^{17}\\text{O}\\), and \\(^{18}\\text{O}\\)), creating slight systematic discrepancies. Adopting pure \\(^{12}\\text{C}\\) unified both scientific scales perfectly.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Hydrogen was Dalton's original 19th-century reference, later replaced due to measurement limitations.
- **Option B is correct**: Carbon-12 is the official international reference standard.
- **Option C is incorrect**: Oxygen was used prior to 1961 but superseded by Carbon-12.
- **Option D is incorrect**: Nitrogen was never adopted as the atomic mass benchmark.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-039",
    text: "The atomic mass of sodium is \\(23\\text{ u}\\). How many moles of sodium atoms are present in a \\(46\\text{ g}\\) sample of pure sodium metal?",
    options: [
      "\\(2\\text{ moles}\\)",
      "\\(1\\text{ mole}\\)",
      "\\(0.5\\text{ moles}\\)",
      "\\(4\\text{ moles}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of moles (\\(n\\)) of an elemental substance is calculated from its mass in grams (\\(m\\)) and molar mass (\\(M\\)):
\\[
n = \\frac{m}{M}
\\]
Given:
- Mass \\(m = 46\\text{ g}\\)
- Molar mass of Sodium (Na) \\(M = 23\\text{ g/mol}\\)

Calculate \\(n\\):
\\[
n = \\frac{46\\text{ g}}{23\\text{ g/mol}} = 2\\text{ moles}
\\]

### 2. Physical Context & Practical Illustration:
Two moles of sodium metal contain \\(2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\) sodium atoms. If reacted with water, these two moles will react vigorously to generate exactly one mole (\\(22.4\\text{ L}\\) at STP) of hydrogen gas.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(n = 46 / 23 = 2\\text{ moles}\\).
- **Option B is incorrect**: \\(1\\text{ mole}\\) is \\(23\\text{ g}\\).
- **Option C is incorrect**: \\(0.5\\text{ moles}\\) is \\(11.5\\text{ g}\\).
- **Option D is incorrect**: \\(4\\text{ moles}\\) is \\(92\\text{ g}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-040",
    text: "One atom of oxygen has an atomic mass of \\(16\\text{ u}\\). What is the total mass of one mole of isolated oxygen atoms (O) in grams?",
    options: [
      "\\(1.6\\text{ g}\\)",
      "\\(32\\text{ g}\\)",
      "\\(16\\text{ g}\\)",
      "\\(8\\text{ g}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The gram atomic mass (or molar mass) of an element is the mass of one mole (\\(N_A = 6.022 \\times 10^{23}\\)) of its atoms expressed in grams:
\\[
\\text{Mass of 1 atom} = 16\\text{ u} = 16 \\times (1.6605 \\times 10^{-24}\\text{ g})
\\]
\\[
\\text{Mass of } 1\\text{ mole of atoms} = 16 \\times (1.6605 \\times 10^{-24}\\text{ g}) \\times (6.0221 \\times 10^{23}) = 16.0\\text{ g}
\\]
By definition of the mole, the numerical value of atomic mass in unified units (\\(\\text{u}\\)) is identically equal to its mass in grams per mole (\\(\\text{g/mol}\\)).
Therefore, one mole of oxygen atoms has a mass of **\\(16\\text{ g}\\)**.

### 2. Physical Context & Practical Illustration:
A common source of confusion is the distinction between atomic oxygen (\\(\\text{O}\\), \\(16\\text{ g/mol}\\)) and molecular oxygen gas (\\(\\text{O}_2\\), \\(32\\text{ g/mol}\\)). The question explicitly specifies isolated oxygen atoms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Involves an arbitrary division by 10.
- **Option B is incorrect**: \\(32\\text{ g}\\) is the mass of one mole of diatomic oxygen *molecules* (\\(\\text{O}_2\\)), not oxygen atoms.
- **Option C is correct**: One mole of oxygen atoms (O) has a mass of exactly \\(16\\text{ g}\\).
- **Option D is incorrect**: \\(8\\text{ g}\\) is half a mole.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-041",
    text: "An atom of element A contains 12 protons and 20 neutrons in its nucleus. What is its mass number (A) and chemical identity?",
    options: [
      "Mass number = 32 (Magnesium isotope)",
      "Mass number = 12 (Carbon)",
      "Mass number = 20 (Neon)",
      "Mass number = 8 (Oxygen)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Atomic Number (\\(Z\\))**: The number of protons identifies the chemical element:
\\[
Z = 12 \\implies \\text{Magnesium (Mg)}
\\]
2. **Mass Number (\\(A\\))**: The total number of nucleons (protons + neutrons) in the nucleus:
\\[
A = Z + N = 12\\text{ protons} + 20\\text{ neutrons} = 32
\\]
Therefore, the atom has a mass number of \\(32\\) (a heavy synthetic isotope of Magnesium, \\(^{32}\\text{Mg}\\)).

### 2. Physical Context & Practical Illustration:
The chemical identity of an atom is dictated exclusively by its proton count (\\(Z\\)). All atoms with 12 protons are magnesium atoms, regardless of how many neutrons are present in the nucleus.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Mass number \\(A = 12 + 20 = 32\\), and \\(Z = 12\\) corresponds to magnesium.
- **Option B is incorrect**: Confuses mass number with atomic number.
- **Option C is incorrect**: Confuses mass number with neutron count.
- **Option D is incorrect**: Subtracts protons from neutrons (\\(20 - 12 = 8\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-042",
    text: "When exactly one mole of a solute is dissolved in sufficient solvent to form one liter of final solution, the concentration of the resulting solution is termed a:",
    options: [
      "Normal solution (1 N)",
      "Molar solution (1 M)",
      "Molal solution (1 m)",
      "Saturated solution"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Molarity (M)** is defined as the number of moles of solute dissolved per liter of solution:
\\[
\\text{Molarity } (M) = \\frac{\\text{Moles of solute } (n)}{\\text{Volume of solution in liters } (V_L)} = \\frac{1\\text{ mol}}{1\\text{ L}} = 1\\text{ mol/L} = 1\\text{ M}
\\]
A solution containing \\(1\\text{ mole}\\) of solute per liter of solution is universally designated as a **1 Molar (1 M) solution**.

### 2. Physical Context & Practical Illustration:
To prepare a \\(1\\text{ M}\\) aqueous sodium hydroxide (\\(\\text{NaOH}\\)) solution, an analytical chemist weighs out \\(40.0\\text{ g}\\) (1 mole) of pure NaOH, dissolves it in a beaker with distilled water, and transfers it to a volumetric flask, adding water until the total solution volume reaches exactly the \\(1.0\\text{ liter}\\) graduation mark.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A Normal solution (1 N) contains 1 gram-equivalent of solute per liter of solution.
- **Option B is correct**: 1 mole of solute in 1 liter of solution is the precise definition of a 1 Molar (1 M) solution.
- **Option C is incorrect**: A Molal solution (1 m) contains 1 mole of solute per 1 kilogram of *solvent*, not per liter of solution.
- **Option D is incorrect**: Saturated refers to maximum solubility equilibrium, not specific 1 mol/L concentration.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-043",
    text: "Nitrogen has an atomic number of 7. What is its chemical valency in forming simple binary hydride compounds like ammonia (\\(\\text{NH}_3\\))?",
    options: [
      "\\(5\\)",
      "\\(3\\)",
      "\\(1\\)",
      "\\(2\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Nitrogen (\\(Z = 7\\)) has the ground-state electronic configuration:
\\[
\\text{N}: 2, 5
\\]
It has 5 electrons in its outermost valence shell. To attain an octet configuration (8 electrons):
\\[
\\text{Valency} = 8 - \\text{Valence electrons} = 8 - 5 = 3
\\]
Nitrogen requires 3 additional electrons to complete its valence shell, which it achieves by sharing three pairs of electrons (such as with 3 hydrogen atoms in \\(\\text{NH}_3\\)).
Therefore, the valency of nitrogen is **\\(3\\)** (trivalent).

### 2. Physical Context & Practical Illustration:
In ammonia (\\(\\text{NH}_3\\)), the nitrogen atom forms three single covalent bonds with three hydrogen atoms and retains one unshared lone pair of electrons, satisfying its valency of 3 and giving ammonia its characteristic pyramidal geometry.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(5\\) is the number of *valence electrons*, not the combining valency.
- **Option B is correct**: Valency of nitrogen is \\(8 - 5 = 3\\).
- **Option C is incorrect**: Valency of 1 is typical of alkali metals and halogens.
- **Option D is incorrect**: Valency of 2 is typical of alkaline earth metals and oxygen.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-044",
    text: "An atom contains 3 protons, 4 neutrons, and 3 electrons. What is its chemical valency?",
    options: [
      "\\(3\\)",
      "\\(4\\)",
      "\\(1\\)",
      "\\(0\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Atomic Number (\\(Z\\))**:
\\[
Z = 3 \\implies \\text{Lithium (Li)}
\\]
2. **Electronic Configuration**:
\\[
\\text{Li}: 2, 1
\\]
The outermost shell contains \\(1\\) valence electron.
3. **Valency**: To achieve a stable duplet shell resembling noble gas Helium (\\(2\\)), lithium readily donates its single valence electron:
\\[
\\text{Valency} = 1
\\]

### 2. Physical Context & Practical Illustration:
Lithium (found in lithium-ion rechargeable batteries) is an alkali metal in Group 1 of the periodic table. It forms monovalent cations (\\(\\text{Li}^+\\)) in salts such as lithium fluoride (LiF) and lithium chloride (LiCl).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(3\\) is the proton number (atomic number), not the valency.
- **Option B is incorrect**: \\(4\\) is the neutron number.
- **Option C is correct**: With electronic configuration \\(2, 1\\), the valency is \\(1\\).
- **Option D is incorrect**: Valency of 0 is characteristic of inert noble gases.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-045",
    text: "An element has an electronic configuration of 2, 8, 7. What is its chemical valency?",
    options: [
      "\\(1\\)",
      "\\(7\\)",
      "\\(2\\)",
      "\\(8\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The electronic configuration is \\(2, 8, 7\\) (total electrons = \\(17\\), corresponding to Chlorine, Cl).
- Number of valence electrons = \\(7\\).
- To attain a stable octet (8 electrons in the valence shell), the atom needs to gain or share \\(1\\) electron:
\\[
\\text{Valency} = 8 - \\text{Valence electrons} = 8 - 7 = 1
\\]
Therefore, its valency is **\\(1\\)** (monovalent).

### 2. Physical Context & Practical Illustration:
Chlorine atoms eagerly accept one electron from electropositive metals (such as sodium) to form stable chloride anions (\\(\\text{Cl}^-\\)), forming common salt (NaCl).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The valency is \\(8 - 7 = 1\\).
- **Option B is incorrect**: \\(7\\) is the number of valence electrons, not the valency.
- **Option C is incorrect**: \\(2\\) would imply gaining two electrons.
- **Option D is incorrect**: \\(8\\) is the target octet number.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-046",
    text: "What is the correct molecular chemical formula of Sulfur hexafluoride?",
    options: [
      "\\(\\text{SF}_6\\)",
      "\\(\\text{S}_6\\text{F}\\)",
      "\\(\\text{SF}_4\\)",
      "\\(\\text{S}_2\\text{F}_6\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In chemical nomenclature for binary covalent compounds:
- 'Sulfur' indicates one central sulfur atom (\\(\\text{S}\\)).
- Prefix 'hexa-' represents the Greek numerical prefix for \\(6\\).
- 'fluoride' indicates fluorine atoms (\\(\\text{F}\\)).
Combining these yields one sulfur atom covalently bonded to six fluorine atoms:
\\[
\\mathbf{\\text{SF}_6}
\\]
In \\(\\text{SF}_6\\), sulfur exhibits an expanded octet with a valency of 6 (sp³d² hybridization, octahedral molecular geometry).

### 2. Physical Context & Practical Illustration:
Sulfur hexafluoride (\\(\\text{SF}_6\\)) is an extremely dense, non-toxic, chemically inert gas with exceptional electrical insulating properties. It is universally used as a gaseous dielectric insulator in high-voltage electrical circuit breakers and switchgear.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\text{SF}_6\\) is sulfur hexafluoride.
- **Option B is incorrect**: Inverts the elemental subscripts (hexasulfur monofluoride).
- **Option C is incorrect**: \\(\\text{SF}_4\\) is sulfur tetrafluoride.
- **Option D is incorrect**: Disulfur hexafluoride.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-047",
    text: "Given that the relative atomic mass of Hydrogen is \\(1\\text{ u}\\), one gram-atomic mass of Hydrogen (\\(1\\text{ g}\\)) contains:",
    options: [
      "Exactly 1 single atom of Hydrogen",
      "Exactly 2 atoms of Hydrogen",
      "Exactly 1 mole (\\(6.022 \\times 10^{23}\\)) of Hydrogen atoms",
      "\\(6.022 \\times 10^{28}\\) atoms of Hydrogen"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition:
- **Gram-atomic mass** is the relative atomic mass of an element expressed in grams.
- For Hydrogen, atomic mass = \\(1\\text{ u}\\) \\(\\implies\\) Gram-atomic mass = \\(1\\text{ g}\\).
- One gram-atomic mass of any element contains exactly **1 mole** of atoms, which corresponds to Avogadro's number:
\\[
N = 1\\text{ mole} = 6.022 \\times 10^{23}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
A single hydrogen atom weighs only \\(1.66 \\times 10^{-24}\\text{ g}\\). To accumulate an entire gram of hydrogen on a laboratory balance, one must collect \\(602,200,000,000,000,000,000,000\\) individual hydrogen atoms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Confuses 1 unified mass unit (the mass of 1 atom) with 1 gram.
- **Option B is incorrect**: \\(1\\text{ g}\\) contains an astronomical count of atoms, not just 2.
- **Option C is correct**: 1 gram-atomic mass equals 1 mole (\\(6.022 \\times 10^{23}\\)) of atoms.
- **Option D is incorrect**: Has an incorrect exponent (\\(10^{28}\\) instead of \\(10^{23}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-048",
    text: "A trivalent cation of an element has 3 positive charges (\\(X^{3+}\\)). If its mass number is 27 and the ion contains 10 electrons, how many neutrons are present in its nucleus?",
    options: [
      "\\(10\\text{ neutrons}\\)",
      "\\(14\\text{ neutrons}\\)",
      "\\(13\\text{ neutrons}\\)",
      "\\(17\\text{ neutrons}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Determining Number of Protons (Atomic Number, \\(Z\\))**:
The ion carries a \\(+3\\) charge, meaning the neutral atom lost 3 electrons to form \\(X^{3+}\\):
\\[
\\text{Electrons in neutral atom} = \\text{Electrons in ion} + 3 = 10 + 3 = 13
\\]
Since a neutral atom has equal numbers of protons and electrons:
\\[
Z = \\text{Number of protons} = 13 \\quad (\\text{Aluminum, Al})
\\]
2. **Determining Number of Neutrons (\\(N\\))**:
Mass number \\(A = Z + N = 27\\):
\\[
N = A - Z = 27 - 13 = 14\\text{ neutrons}
\\]

### 2. Physical Context & Practical Illustration:
This ion is the aluminum cation (\\(\\text{Al}^{3+}\\)). In the aluminum nucleus, 13 positive protons and 14 neutral neutrons are bound together by the strong nuclear force, while 10 electrons orbit in the stable neon core configuration (\\(2, 8\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(10\\) is the number of remaining electrons, not neutrons.
- **Option B is correct**: \\(N = 27 - 13 = 14\\text{ neutrons}\\).
- **Option C is incorrect**: \\(13\\) is the number of protons.
- **Option D is incorrect**: Subtracts the 10 electrons directly from mass number 27 (\\(27 - 10 = 17\\)), forgetting to add back the 3 positive charges.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-049",
    text: "Which of the following represents the correct chemical symbol and charge of the Chloride radical (anion)?",
    options: [
      "\\(\\text{Cl}^-\\)",
      "\\(\\text{Cl}_2^-\\)",
      "\\(\\text{ClO}_3^-\\)",
      "\\(\\text{Cl}^{2-}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A chlorine atom (\\(Z = 17\\)) has the electron configuration \\(2, 8, 7\\).
To achieve an argon-like octet (\\(2, 8, 8\\)), it gains one electron:
\\[
\\text{Cl} + e^- \\longrightarrow \\mathbf{\\text{Cl}^-}
\\]
The resulting chloride anion carries a single negative charge (valency = 1).
- \\(\\text{ClO}_3^-\\) is the *chlorate* radical.
- \\(\\text{Cl}_2\\) is neutral molecular chlorine gas.

### 2. Physical Context & Practical Illustration:
Chloride ions (\\(\\text{Cl}^-\\)) are the most abundant extracellular anions in human blood plasma and tissue fluid, crucial for maintaining osmotic pressure, fluid balance, and producing gastric hydrochloric acid in the stomach.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\text{Cl}^-\\) is the chloride radical with a single negative charge.
- **Option B is incorrect**: \\(\\text{Cl}_2^-\\) is chemically invalid.
- **Option C is incorrect**: \\(\\text{ClO}_3^-\\) is the chlorate oxyanion.
- **Option D is incorrect**: Chlorine forms a monovalent anion (\\(-1\\)), not divalent (\\(-2\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-050",
    text: "Which of the following represents the correct chemical formula and charge of the Hydride radical (anion)?",
    options: [
      "\\(\\text{H}^+\\)",
      "\\(\\text{H}^-\\)",
      "\\(\\text{OH}^-\\)",
      "\\(\\text{H}_2^-\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A hydrogen atom (\\(1s^1\\)) can achieve a stable noble-gas duplet configuration (resembling Helium, \\(1s^2\\)) by gaining one electron from an electropositive metal:
\\[
\\text{H} + e^- \\longrightarrow \\mathbf{\\text{H}^-}
\\]
The resulting anion carrying a single negative charge is called the **hydride ion** (\\(\\text{H}^-\\)).
- In contrast, \\(\\text{H}^+\\) is the hydrogen cation (proton).
- \\(\\text{OH}^-\\) is the hydroxide ion.

### 2. Physical Context & Practical Illustration:
Hydride ions form ionic salts with highly reactive electropositive metals (e.g. sodium hydride, \\(\\text{NaH}\\); calcium hydride, \\(\\text{CaH}_2\\)). When added to water, hydride ions react vigorously to evolve hydrogen gas: \\(\\text{H}^- + \\text{H}_2\\text{O} \\to \\text{H}_2 + \\text{OH}^-\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{H}^+\\) is the hydrogen cation (proton).
- **Option B is correct**: \\(\\text{H}^-\\) is the hydride anion.
- **Option C is incorrect**: \\(\\text{OH}^-\\) is the hydroxide ion.
- **Option D is incorrect**: Non-existent molecular anion.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-051",
    text: "In chemical nomenclature and ionic representation, what does a negative sign placed before or on the valency of a radical indicate?",
    options: [
      "The atom tends to lose electrons and form a cation",
      "The atom or radical has gained electrons and exists as an acidic radical (anion)",
      "The atom has zero reactivity and behaves as a noble gas",
      "The atom has more protons than electrons"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In electrochemical terminology:
- An atom or group of atoms that **gains electrons** acquires a net excess of negative electrical charge, forming an **anion** (or acidic radical):
\\[
A + n e^- \\longrightarrow A^{n-}
\\]
- A negative valence indicates the capacity to accept electrons, characteristic of non-metallic elements (e.g., \\(\\text{Cl}^-\\), \\(\\text{O}^{2-}\\), \\(\\text{SO}_4^{2-}\\)).
Conversely, electropositive elements that donate electrons acquire positive valencies (cations / basic radicals).

### 2. Physical Context & Practical Illustration:
During electrolysis of molten salts or aqueous solutions, negatively charged anions migrate toward the positive anode (hence the name *anion*).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Losing electrons produces a positive cation (basic radical).
- **Option B is correct**: A negative valency signifies electron gain, forming an anion (acidic radical).
- **Option C is incorrect**: Noble gases have a valency of zero.
- **Option D is incorrect**: Having more protons than electrons creates a positive charge.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-052",
    text: "What does the chemical symbol notation \\(\\text{Mg}^{2+}\\) specifically signify?",
    options: [
      "A neutral magnesium atom with two extra neutrons in its nucleus",
      "A magnesium atom that has gained two electrons into its outer shell",
      "A magnesium molecule consisting of two bonded atoms",
      "A magnesium cation formed when a neutral magnesium atom loses two valence electrons"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A neutral magnesium atom (\\(Z = 12\\)) has the electron configuration:
\\[
\\text{Mg}: 2, 8, 2 \\quad (12\\text{ protons, } 12\\text{ electrons})
\\]
To attain a stable noble gas configuration (Neon: \\(2, 8\\)), magnesium readily donates its two valence electrons from the M shell:
\\[
\\text{Mg} \\longrightarrow \\mathbf{\\text{Mg}^{2+}} + 2e^-
\\]
The resulting species \\(\\text{Mg}^{2+}\\) contains 12 protons and 10 electrons, possessing a net positive charge of \\(+2\\). It is a divalent magnesium cation.

### 2. Physical Context & Practical Illustration:
Magnesium cations (\\(\\text{Mg}^{2+}\\)) are abundant in seawater and hard tap water, and play an indispensable biochemical role as the central coordinating metallic ion in the chlorophyll molecule responsible for plant photosynthesis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Charge relates to electrons, not nuclear neutrons.
- **Option B is incorrect**: Gaining electrons would produce a negative charge (\\(\\text{Mg}^{2-}\\)).
- **Option C is incorrect**: Diatomic molecules are written with subscripts (\\(\\text{Mg}_2\\)).
- **Option D is correct**: \\(\\text{Mg}^{2+}\\) represents a magnesium ion formed by losing two valence electrons.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-053",
    text: "A sample of \\(17\\text{ g}\\) of pure hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)) contains how many moles of \\(\\text{H}_2\\text{O}_2\\)? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(0.5\\text{ moles}\\)",
      "\\(1.0\\text{ mole}\\)",
      "\\(2.0\\text{ moles}\\)",
      "\\(0.25\\text{ moles}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Hydrogen Peroxide (\\(\\text{H}_2\\text{O}_2\\))**:
\\[
M = (2 \\times A_r(\\text{H})) + (2 \\times A_r(\\text{O}))
\\]
\\[
M = (2 \\times 1) + (2 \\times 16) = 2 + 32 = 34\\text{ g/mol}
\\]
2. **Number of Moles (\\(n\\))**:
\\[
n = \\frac{m}{M} = \\frac{17\\text{ g}}{34\\text{ g/mol}} = 0.5\\text{ moles}
\\]

### 2. Physical Context & Practical Illustration:
Hydrogen peroxide is an unstable liquid commonly used in diluted aqueous form (\\(3\\%\\)) as an antiseptic and bleaching agent. Because its molar mass is \\(34\\text{ g/mol}\\), measuring out \\(17\\text{ g}\\) represents exactly half a mole (\\(0.5\\text{ mol}\\)), containing \\(3.011 \\times 10^{23}\\) peroxide molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(n = 17 / 34 = 0.5\\text{ moles}\\).
- **Option B is incorrect**: \\(1.0\\text{ mole}\\) would require \\(34\\text{ g}\\).
- **Option C is incorrect**: \\(2.0\\text{ moles}\\) would require \\(68\\text{ g}\\).
- **Option D is incorrect**: \\(0.25\\text{ moles}\\) would require \\(8.5\\text{ g}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-054",
    text: "Given that the atomic mass of Nitrogen is \\(14\\text{ u}\\), how many molecules of nitrogen gas (\\(\\text{N}_2\\)) are present in \\(28\\text{ g}\\) of pure nitrogen gas? (Given: \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(6.022 \\times 10^{23}\\text{ molecules}\\)",
      "\\(1.2044 \\times 10^{24}\\text{ molecules}\\)",
      "\\(3.011 \\times 10^{23}\\text{ molecules}\\)",
      "\\(2.8 \\times 10^{23}\\text{ molecules}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Nitrogen Gas (\\(\\text{N}_2\\))**:
\\[
M = 2 \\times 14\\text{ g/mol} = 28\\text{ g/mol}
\\]
2. **Number of Moles**:
\\[
n = \\frac{m}{M} = \\frac{28\\text{ g}}{28\\text{ g/mol}} = 1.0\\text{ mole}
\\]
3. **Number of Molecules**:
\\[
N = n \\times N_A = 1.0 \\times 6.022 \\times 10^{23} = 6.022 \\times 10^{23}\\text{ molecules}
\\]

### 2. Physical Context & Practical Illustration:
Nitrogen gas constitutes \\(78\\%\\) of Earth's atmosphere by volume. Weighing out \\(28\\text{ g}\\) of pure \\(\\text{N}_2\\) yields exactly one mole, containing \\(6.022 \\times 10^{23}\\) diatomic molecules (and \\(1.2044 \\times 10^{24}\\) constituent nitrogen atoms).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(28\\text{ g}\\) is exactly 1 mole of \\(\\text{N}_2\\), containing \\(6.022 \\times 10^{23}\\) molecules.
- **Option B is incorrect**: \\(1.2044 \\times 10^{24}\\) is the number of individual nitrogen *atoms*, not molecules.
- **Option C is incorrect**: Corresponds to half a mole (\\(14\\text{ g}\\)).
- **Option D is incorrect**: Arbitrary value.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-055",
    text: "What is the mass in grams of \\(0.5\\text{ moles}\\) of nitrogen gas (\\(\\text{N}_2\\))? (Given: atomic mass of \\(\\text{N} = 14\\text{ u}\\))",
    options: [
      "\\(7.0\\text{ g}\\)",
      "\\(28.0\\text{ g}\\)",
      "\\(14.0\\text{ g}\\)",
      "\\(3.5\\text{ g}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Nitrogen Gas (\\(\\text{N}_2\\))**:
\\[
M = 2 \\times A_r(\\text{N}) = 2 \\times 14 = 28\\text{ g/mol}
\\]
2. **Mass Calculation**:
\\[
m = n \\times M = 0.5\\text{ mol} \\times 28\\text{ g/mol} = 14.0\\text{ g}
\\]

### 2. Physical Context & Practical Illustration:
Half a mole of diatomic nitrogen gas has a mass of \\(14\\text{ g}\\). Note that \\(14\\text{ g}\\) is also the mass of \\(1.0\\text{ mole}\\) of atomic nitrogen (N). Distinguishing between molecular gas (\\(\\text{N}_2\\)) and atomic nitrogen (N) is crucial.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(7.0\\text{ g}\\) is the mass of \\(0.5\\text{ moles}\\) of isolated nitrogen *atoms* (\\(0.5 \\times 14 = 7\\)).
- **Option B is incorrect**: \\(28.0\\text{ g}\\) is the mass of 1 full mole of \\(\\text{N}_2\\).
- **Option C is correct**: \\(m = 0.5 \\times 28 = 14.0\\text{ g}\\).
- **Option D is incorrect**: \\(3.5\\text{ g}\\) corresponds to \\(0.25\\) moles of atomic nitrogen.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-056",
    text: "Which of the following expressions correctly represents the molar quantity and molecular count in a \\(360\\text{ g}\\) sample of pure water (\\(\\text{H}_2\\text{O}\\))? (Given: \\(M = 18\\text{ g/mol}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(2\\text{ moles of water and } 1.2044 \\times 10^{24}\\text{ molecules}\\)",
      "\\(10\\text{ moles of water and } 6.022 \\times 10^{24}\\text{ molecules}\\)",
      "\\(18\\text{ moles of water and } 1.084 \\times 10^{25}\\text{ molecules}\\)",
      "\\(20\\text{ moles of water and } 1.2044 \\times 10^{25}\\text{ molecules}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Water (\\(\\text{H}_2\\text{O}\\))**:
\\[
M = (2 \\times 1) + 16 = 18\\text{ g/mol}
\\]
2. **Number of Moles (\\(n\\))**:
\\[
n = \\frac{m}{M} = \\frac{360\\text{ g}}{18\\text{ g/mol}} = 20\\text{ moles}
\\]
3. **Total Number of Water Molecules (\\(N\\))**:
\\[
N = n \\times N_A = 20 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{25}\\text{ molecules}
\\]

### 2. Physical Context & Practical Illustration:
A standard glass of water contains about \\(200\\text{ to } 250\\text{ mL}\\). A volume of \\(360\\text{ g}\\) (or \\(360\\text{ mL}\\)) represents a large mug of water, containing twenty full moles of water and over twelve septillion individual \\(\\text{H}_2\\text{O}\\) molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Confuses 20 moles with 2 moles (off by a factor of 10).
- **Option B is incorrect**: Corresponds to \\(180\\text{ g}\\) of water.
- **Option C is incorrect**: Conflates molar mass (18) with mole count.
- **Option D is correct**: \\(n = 360 / 18 = 20\\text{ moles}\\), and \\(N = 20 \\times N_A = 1.2044 \\times 10^{25}\\text{ molecules}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-057",
    text: "Which of the following represents the total number of constituent oxygen atoms present in exactly \\(1\\text{ mole}\\) of molecular oxygen gas (\\(\\text{O}_2\\))?",
    options: [
      "\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(3.011 \\times 10^{23}\\text{ atoms}\\)",
      "\\(18.066 \\times 10^{23}\\text{ atoms}\\)",
      "\\(1.2044 \\times 10^{24}\\text{ atoms}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Molecular oxygen gas exists as homonuclear diatomic molecules (\\(\\text{O}_2\\)). By Avogadro's law, \\(1\\text{ mole}\\) of any molecular substance contains exactly Avogadro's number (\\(N_A\\)) of discrete molecules:
\\[
N_A = 6.022 \\times 10^{23}\\text{ molecules/mol}
\\]
Because each \\(\\text{O}_2\\) molecule contains exactly \\(2\\) chemically bonded oxygen atoms (atomicity = 2), the total number of constituent oxygen atoms in \\(1\\text{ mole}\\) is given by:
\\[
N_{\\text{atoms}} = \\text{Moles} \\times \\text{Atomicity} \\times N_A = 1 \\times 2 \\times (6.022 \\times 10^{23}) = 1.2044 \\times 10^{24}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
Students often confuse the number of *molecules* of a diatomic gas with the number of constituent *atoms*. While \\(1\\text{ mole}\\) of \\(\\text{O}_2\\) (mass \\(32\\text{ g}\\)) contains \\(6.022 \\times 10^{23}\\) diatomic molecules, breaking all covalent double bonds (\\(O=O\\)) yields \\(2\\text{ moles}\\) of isolated, free oxygen atoms (\\(1.2044 \\times 10^{24}\\) atoms).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(6.022 \\times 10^{23}\\)):** Incorrect. This is the number of \\(\\text{O}_2\\) *molecules*, not constituent oxygen *atoms*.
- **Option B (\\(3.011 \\times 10^{23}\\)):** Incorrect. This corresponds to half a mole of atoms (\\(0.25\\text{ mol } O_2\\)).
- **Option C (\\(18.066 \\times 10^{23}\\)):** Incorrect. This would correspond to 3 moles of atoms (as in ozone, \\(O_3\\)).
- **Option D (\\(1.2044 \\times 10^{24}\\)):** Correct. \\(1\\text{ mole}\\) of diatomic \\(\\text{O}_2\\) contains \\(2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\) constituent oxygen atoms.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-058",
    text: "Given that the molecular mass of water (\\(\\text{H}_2\\text{O}\\)) is \\(18\\text{ u}\\), what is the total mass of \\(1\\text{ mole}\\) of pure liquid water?",
    options: [
      "\\(1.8\\text{ g}\\)",
      "\\(9.0\\text{ g}\\)",
      "\\(36.0\\text{ g}\\)",
      "\\(18.0\\text{ g}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The molecular mass of water (\\(\\text{H}_2\\text{O}\\)) is calculated from the constituent atomic masses (\\(H = 1\\text{ u}\\), \\(O = 16\\text{ u}\\)):
\\[
M = (2 \\times 1) + 16 = 18\\text{ u}
\\]
By definition of the mole concept, the mass of \\(1\\text{ mole}\\) of any chemical substance expressed in grams is numerically equal to its molecular mass in atomic mass units (unified mass units, \\(\\text{u}\\)). This quantity is called the **gram-molecular mass** or **molar mass**:
\\[
\\text{Molar mass of } \\text{H}_2\\text{O} = 18\\text{ g/mol}
\\]
Therefore, the mass (\\(m\\)) of \\(n = 1\\text{ mole}\\) of water is:
\\[
m = n \\times M = 1\\text{ mol} \\times 18\\text{ g/mol} = 18.0\\text{ g}
\\]

### 2. Physical Context & Practical Illustration:
Since the density of liquid water at room temperature is approximately \\(1.0\\text{ g/cm}^3\\) (\\(1.0\\text{ g/mL}\\)), \\(18\\text{ g}\\) of water corresponds to a volume of approximately \\(18\\text{ mL}\\) (roughly one standard tablespoon). Drinking one tablespoon of water delivers exactly \\(1\\text{ mole}\\) or \\(6.022 \\times 10^{23}\\) water molecules to the body.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(1.8\\text{ g}\\)):** Incorrect. This represents only \\(0.1\\text{ mole}\\) of water.
- **Option B (\\(9.0\\text{ g}\\)):** Incorrect. This corresponds to \\(0.5\\text{ mole}\\) of water.
- **Option C (\\(36.0\\text{ g}\\)):** Incorrect. This corresponds to \\(2\\text{ moles}\\) of water.
- **Option D (\\(18.0\\text{ g}\\)):** Correct. The gram-molecular mass of water is \\(18\\text{ g}\\), so \\(1\\text{ mole}\\) has a mass of exactly \\(18.0\\text{ g}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-059",
    text: "Which of the following chemical samples possesses the GREATEST mass in grams? (Molar masses: Sucrose \\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11} = 342\\text{ g/mol}\\), \\(\\text{CO}_2 = 44\\text{ g/mol}\\), \\(\\text{CaCO}_3 = 100\\text{ g/mol}\\), \\(\\text{H}_2\\text{O} = 18\\text{ g/mol}\\))",
    options: [
      "\\(0.2\\text{ moles of Sucrose (\\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}\\))}\\)",
      "\\(2\\text{ moles of Carbon dioxide (\\(\\text{CO}_2\\))}\\)",
      "\\(2\\text{ moles of Calcium carbonate (\\(\\text{CaCO}_3\\))}\\)",
      "\\(10\\text{ moles of Water (\\(\\text{H}_2\\text{O}\\))}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We calculate the actual mass (\\(m = n \\times M\\)) for each sample:
1. **\\(0.2\\text{ moles of Sucrose}\\)**:
\\[
m = 0.2\\text{ mol} \\times 342\\text{ g/mol} = 68.4\\text{ g}
\\]
2. **\\(2\\text{ moles of } \\text{CO}_2\\)**:
\\[
m = 2\\text{ mol} \\times 44\\text{ g/mol} = 88.0\\text{ g}
\\]
3. **\\(2\\text{ moles of } \\text{CaCO}_3\\)**:
\\[
m = 2\\text{ mol} \\times 100\\text{ g/mol} = \\mathbf{200.0\\text{ g}}
\\]
4. **\\(10\\text{ moles of } \\text{H}_2\\text{O}\\)**:
\\[
m = 10\\text{ mol} \\times 18\\text{ g/mol} = 180.0\\text{ g}
\\]

Comparing calculated masses:
\\[
200.0\\text{ g (\\(\\text{CaCO}_3\\))} > 180.0\\text{ g (\\(\\text{H}_2\\text{O}\\))} > 88.0\\text{ g (\\(\\text{CO}_2\\))} > 68.4\\text{ g (Sucrose)}
\\]
Therefore, \\(2\\text{ moles of Calcium carbonate}\\) (\\(200\\text{ g}\\)) has the highest mass.

### 2. Physical Context & Practical Illustration:
Even though \\(10\\text{ moles of water}\\) represents five times the number of moles as \\(2\\text{ moles of calcium carbonate}\\), the heavy molar mass of limestone (\\(100\\text{ g/mol}\\)) outweighs the ten moles of water (\\(180\\text{ g}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Weighs \\(68.4\\text{ g}\\).
- **Option B is incorrect**: Weighs \\(88.0\\text{ g}\\).
- **Option C is correct**: Weighs \\(200.0\\text{ g}\\), the highest mass.
- **Option D is incorrect**: Weighs \\(180.0\\text{ g}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-060",
    text: "What is the mass in grams of \\(0.5\\text{ moles}\\) of isolated Nitrogen ATOMS (N)? (Given: atomic mass of \\(\\text{N} = 14\\text{ u}\\))",
    options: [
      "\\(14.0\\text{ g}\\)",
      "\\(7.0\\text{ g}\\)",
      "\\(28.0\\text{ g}\\)",
      "\\(0.7\\text{ g}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The mass in grams (\\(m\\)) is the product of the number of moles (\\(n\\)) and the molar mass of the specified chemical entity (\\(M\\)):
\\[
m = n \\times M
\\]
Given:
- Number of moles \\(n = 0.5\\text{ mol}\\)
- Molar mass of atomic Nitrogen (N) \\(M = 14\\text{ g/mol}\\)

Calculate mass:
\\[
m = 0.5\\text{ mol} \\times 14\\text{ g/mol} = 7.0\\text{ g}
\\]

### 2. Physical Context & Practical Illustration:
This problem highlights the critical distinction in chemical stoichiometry: \\(0.5\\text{ moles}\\) of atomic nitrogen (N) weighs \\(7\\text{ g}\\), whereas \\(0.5\\text{ moles}\\) of diatomic molecular nitrogen gas (\\(\\text{N}_2\\)) weighs \\(14\\text{ g}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(14.0\\text{ g}\\) is the mass of 1 full mole of atomic nitrogen (or \\(0.5\\) moles of \\(\\text{N}_2\\)).
- **Option B is correct**: \\(m = 0.5 \\times 14 = 7.0\\text{ g}\\).
- **Option C is incorrect**: \\(28.0\\text{ g}\\) is 1 mole of \\(\\text{N}_2\\).
- **Option D is incorrect**: Decimal error.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-061",
    text: "How many moles of carbon dioxide (\\(\\text{CO}_2\\)) are present in a \\(220\\text{ mg}\\) sample of carbon dioxide gas? (Atomic masses: \\(\\text{C} = 12\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(0.05\\text{ mol}\\)",
      "\\(0.005\\text{ mol } (5.0 \\times 10^{-3}\\text{ mol})\\)",
      "\\(0.5\\text{ mol}\\)",
      "\\(5.0 \\times 10^{-4}\\text{ mol}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Molar Mass of Carbon Dioxide (\\(\\text{CO}_2\\))**:
\\[
M = 12 + (2 \\times 16) = 12 + 32 = 44\\text{ g/mol}
\\]
2. **Convert Mass to Grams**:
\\[
m = 220\\text{ mg} = 220 \\times 10^{-3}\\text{ g} = 0.22\\text{ g}
\\]
3. **Calculate Number of Moles (\\(n\\))**:
\\[
n = \\frac{m}{M} = \\frac{0.22\\text{ g}}{44\\text{ g/mol}} = \\frac{22 \\times 10^{-2}}{44} = 0.5 \\times 10^{-2} = 5.0 \\times 10^{-3}\\text{ mol} = 0.005\\text{ mol}
\\]

### 2. Physical Context & Practical Illustration:
Laboratory microbalances measure reagents in milligrams. In \\(220\\text{ mg}\\) of carbon dioxide, there are \\(0.005\\text{ moles}\\), corresponding to \\(0.005 \\times 6.022 \\times 10^{23} = 3.011 \\times 10^{21}\\) molecules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(0.05\\text{ mol}\\) corresponds to \\(2.2\\text{ g}\\).
- **Option B is correct**: \\(n = 0.22 / 44 = 0.005\\text{ mol} = 5.0 \\times 10^{-3}\\text{ mol}\\).
- **Option C is incorrect**: \\(0.5\\text{ mol}\\) corresponds to \\(22\\text{ g}\\).
- **Option D is incorrect**: \\(5.0 \\times 10^{-4}\\text{ mol}\\) corresponds to \\(22\\text{ mg}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-062",
    text: "A sample of nitrogen gas contains \\(5.6 \\times 10^{19}\\) nitrogen atoms. What is the total mass of this nitrogen sample in milligrams? (Atomic mass of \\(\\text{N} = 14\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(0.13\\text{ mg}\\)",
      "\\(1.30\\text{ mg}\\)",
      "\\(13.0\\text{ mg}\\)",
      "\\(0.013\\text{ mg}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Number of Moles of Nitrogen Atoms**:
\\[
n = \\frac{N}{N_A} = \\frac{5.6 \\times 10^{19}}{6.022 \\times 10^{23}} \\approx 0.930 \\times 10^{-4}\\text{ mol} = 9.30 \\times 10^{-5}\\text{ mol}
\\]
2. **Mass in Grams**:
\\[
m = n \\times M = (9.30 \\times 10^{-5}\\text{ mol}) \\times 14\\text{ g/mol} \\approx 1.302 \\times 10^{-3}\\text{ g}
\\]
3. **Convert to Milligrams**:
\\[
m_{\\text{mg}} = (1.302 \\times 10^{-3}\\text{ g}) \\times 10^3\\text{ mg/g} \\approx \\mathbf{1.30\\text{ mg}}
\\]

### 2. Physical Context & Practical Illustration:
Even though \\(56\\text{ quintillion}\\) atoms sounds like an enormous count, atoms are so unimaginably lightweight that their combined mass is barely more than a single milligram—about the weight of a tiny grain of sand.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Off by a factor of 10.
- **Option B is correct**: \\(m = \\frac{5.6 \\times 10^{19} \\times 14}{6.022 \\times 10^{23}} \\times 10^3 \\approx 1.30\\text{ mg}\\).
- **Option C is incorrect**: Off by a factor of 10 too large.
- **Option D is incorrect**: Off by a factor of 100 too small.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-063",
    text: "Which of the following given samples contains the LARGEST number of molecules?",
    options: [
      "\\(1\\text{ mole of water (\\(\\text{H}_2\\text{O}\\))}\\)",
      "\\(1\\text{ g of water (\\(\\text{H}_2\\text{O}\\))}\\)",
      "\\(1\\text{ g of methane (\\(\\text{CH}_4\\))}\\)",
      "\\(0.5\\text{ moles of carbon dioxide (\\(\\text{CO}_2\\))}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of molecules is directly proportional to the number of moles (\\(N = n \\times N_A\\)):
- **Option A (\\(1\\text{ mole of } \\text{H}_2\\text{O}\\))**:
\\[
n = 1.0\\text{ mol} \\implies N = 6.022 \\times 10^{23}\\text{ molecules}
\\]
- **Option B (\\(1\\text{ g of } \\text{H}_2\\text{O}\\))**:
\\[
n = \\frac{1}{18} \\approx 0.0556\\text{ mol} \\implies N = 3.35 \\times 10^{22}\\text{ molecules}
\\]
- **Option C (\\(1\\text{ g of } \\text{CH}_4\\))**:
\\[
n = \\frac{1}{16} = 0.0625\\text{ mol} \\implies N = 3.76 \\times 10^{22}\\text{ molecules}
\\]
- **Option D (\\(0.5\\text{ moles of } \\text{CO}_2\\))**:
\\[
n = 0.5\\text{ mol} \\implies N = 3.011 \\times 10^{23}\\text{ molecules}
\\]

Comparing molecular counts:
\\[
1.0\\text{ mol (Option A)} > 0.5\\text{ mol (Option D)} > 0.0625\\text{ mol (Option C)} > 0.0556\\text{ mol (Option B)}
\\]
Therefore, \\(1\\text{ mole of water}\\) contains the maximum number of molecules.

### 2. Physical Context & Practical Illustration:
One full mole of any compound always contains \\(6.022 \\times 10^{23}\\) molecules, which easily surpasses small single-gram fractions or half-moles.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Contains \\(1.0 N_A = 6.022 \\times 10^{23}\\) molecules, the largest among all choices.
- **Option B is incorrect**: Contains only \\(0.0556 N_A\\) molecules.
- **Option C is incorrect**: Contains only \\(0.0625 N_A\\) molecules.
- **Option D is incorrect**: Contains \\(0.5 N_A\\) molecules.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-064",
    text: "What is the relative molecular mass of a water molecule (\\(\\text{H}_2\\text{O}\\)) in unified atomic mass units (u)? (Atomic masses: \\(\\text{H} = 1\\text{ u}\\), \\(\\text{O} = 16\\text{ u}\\))",
    options: [
      "\\(16\\text{ u}\\)",
      "\\(32\\text{ u}\\)",
      "\\(34\\text{ u}\\)",
      "\\(18\\text{ u}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Molecular mass is the sum of the atomic masses of all atoms present in the chemical formula:
\\[
M(\\text{H}_2\\text{O}) = (2 \\times A_r(\\text{H})) + (1 \\times A_r(\\text{O}))
\\]
\\[
M(\\text{H}_2\\text{O}) = (2 \\times 1\\text{ u}) + (1 \\times 16\\text{ u}) = 2 + 16 = 18\\text{ u}
\\]

### 2. Physical Context & Practical Illustration:
One water molecule consists of one central oxygen atom covalently bonded to two hydrogen atoms at a bond angle of \\(104.5^\\circ\\), yielding a total mass of \\(18\\text{ unified atomic mass units}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(16\\text{ u}\\) is only the oxygen atom mass.
- **Option B is incorrect**: \\(32\\text{ u}\\) is oxygen gas (\\(\\text{O}_2\\)).
- **Option C is incorrect**: \\(34\\text{ u}\\) is hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)).
- **Option D is correct**: Molecular mass of water is \\(18\\text{ u}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-065",
    text: "An element X has the ground-state electronic configuration 2, 8, 7. When element X combines with Calcium (Ca, atomic number 20), what is the correct chemical formula of the resulting compound?",
    options: [
      "\\(\\text{CaX}\\)",
      "\\(\\text{CaX}_2\\)",
      "\\(\\text{Ca}_2\\text{X}\\)",
      "\\(\\text{CaX}_3\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Valency of Element X**:
   - Electronic configuration: \\(2, 8, 7\\) (Chlorine, Cl)
   - Valency = \\(8 - 7 = 1\\) (forms anion \\(X^-\\))
2. **Valency of Calcium (Ca)**:
   - Atomic number \\(Z = 20\\), electronic configuration: \\(2, 8, 8, 2\\)
   - Valency = \\(2\\) (forms cation \\(\\text{Ca}^{2+}\\))
3. **Criss-Cross Formula Method**:
   - Symbols: \\(\\text{Ca}\\) and \\(X\\)
   - Valencies: \\(2\\) and \\(1\\)
   - Cross-combining: \\(\\text{Ca}_1 X_2 \\implies \\mathbf{\\text{CaX}_2}\\).

### 2. Physical Context & Practical Illustration:
Element X is Chlorine, and the resulting ionic salt is Calcium Chloride (\\(\\text{CaCl}_2\\)). Calcium donates two electrons, one to each of two chlorine atoms, achieving stable octets for all three ions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{CaX}\\) would only be neutral if both were divalent.
- **Option B is correct**: \\(\\text{CaX}_2\\) balances the \\(+2\\) charge of calcium with two \\(-1\\) charges of X.
- **Option C is incorrect**: \\(\\text{Ca}_2 X\\) has mismatched valencies.
- **Option D is incorrect**: Mismatched valency.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-066",
    text: "In the chemical formula unit of aluminum chloride (\\(\\text{AlCl}_3\\)), what is the chemical valency of the Aluminum atom?",
    options: [
      "\\(1\\)",
      "\\(2\\)",
      "\\(3\\)",
      "\\(6\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In binary ionic compounds formed between a metal and a non-metal:
- Chlorine is monovalent: each chloride ion (\\(\\text{Cl}^-\\)) carries a valency of \\(1\\).
- Three chloride ions combine with one aluminum ion:
\\[
\\text{Valency of Al} = 3 \\times \\text{Valency of Cl} = 3 \\times 1 = 3
\\]
Aluminum (\\(Z = 13\\), configuration \\(2, 8, 3\\)) loses its three valence electrons to form the trivalent cation \\(\\text{Al}^{3+}\\).
Hence, the valency of Aluminum is **\\(3\\)**.

### 2. Physical Context & Practical Illustration:
The stoichiometric coefficient in front of a formula (e.g. \\(2\\text{AlCl}_3\\)) denotes the number of formula units, but the intrinsic valency of Aluminum within the compound remains strictly 3.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: 1 is the valency of chlorine.
- **Option B is incorrect**: Divalent state is not typical of aluminum.
- **Option C is correct**: Aluminum has a valency of 3.
- **Option D is incorrect**: Multiplying the prefix 2 by subscript 3 (\\(2 \\times 3 = 6\\)) confuses total chlorine atom count with the valency of aluminum.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-067",
    text: "What is the mass in grams of a sample containing \\(3.011 \\times 10^{23}\\) nitrogen atoms (N)? (Given: atomic mass of \\(\\text{N} = 14\\text{ u}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(14.0\\text{ g}\\)",
      "\\(7.0\\text{ g}\\)",
      "\\(28.0\\text{ g}\\)",
      "\\(3.5\\text{ g}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Calculate Number of Moles of Nitrogen Atoms**:
\\[
n = \\frac{N}{N_A} = \\frac{3.011 \\times 10^{23}}{6.022 \\times 10^{23}} = 0.5\\text{ mol}
\\]
2. **Calculate Mass in Grams**:
\\[
m = n \\times M = 0.5\\text{ mol} \\times 14\\text{ g/mol} = 7.0\\text{ g}
\\]

### 2. Physical Context & Practical Illustration:
Since one full mole (\\(6.022 \\times 10^{23}\\) atoms) of nitrogen has a mass of \\(14\\text{ g}\\), exactly half a mole (\\(3.011 \\times 10^{23}\\) atoms) weighs half as much: \\(7.0\\text{ g}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(14.0\\text{ g}\\) corresponds to a full mole of N atoms.
- **Option B is correct**: \\(m = 0.5 \\times 14 = 7.0\\text{ g}\\).
- **Option C is incorrect**: \\(28.0\\text{ g}\\) is 1 mole of \\(\\text{N}_2\\) gas.
- **Option D is incorrect**: \\(3.5\\text{ g}\\) is a quarter mole.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-068",
    text: "How many total atoms are present in \\(0.27\\text{ g}\\) of pure water (\\(\\text{H}_2\\text{O}\\))? (Given: \\(M = 18\\text{ g/mol}\\), \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\))",
    options: [
      "\\(9.033 \\times 10^{21}\\text{ atoms}\\)",
      "\\(1.8066 \\times 10^{22}\\text{ atoms}\\)",
      "\\(5.4198 \\times 10^{22}\\text{ atoms}\\)",
      "\\(2.710 \\times 10^{22}\\text{ atoms}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Number of Moles of Water**:
\\[
n = \\frac{m}{M} = \\frac{0.27\\text{ g}}{18\\text{ g/mol}} = 0.015\\text{ mol}
\\]
2. **Number of Water Molecules**:
\\[
N_{\\text{molecules}} = n \\times N_A = 0.015 \\times 6.022 \\times 10^{23} = 9.033 \\times 10^{21}\\text{ molecules}
\\]
3. **Total Atoms**: Each molecule of \\(\\text{H}_2\\text{O}\\) has 3 atoms (2 H + 1 O):
\\[
N_{\\text{atoms}} = 3 \\times N_{\\text{molecules}} = 3 \\times (9.033 \\times 10^{21}) = 2.7099 \\times 10^{22} \\approx 2.710 \\times 10^{22}\\text{ atoms}
\\]

### 2. Physical Context & Practical Illustration:
A drop of water has a mass of about \\(0.05\\text{ g}\\); therefore, \\(0.27\\text{ g}\\) represents roughly 5 to 6 small drops, containing 27 sextillion individual atoms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(9.033 \\times 10^{21}\\) is the number of *molecules*, forgetting to multiply by 3 atoms per molecule.
- **Option B is incorrect**: \\(1.8066 \\times 10^{22}\\) counts only the hydrogen atoms (\\(2 \\times 9.033 \\times 10^{21}\\)).
- **Option C is incorrect**: Arithmetic error.
- **Option D is correct**: \\(N_{\\text{atoms}} = 3 \\times 0.015 \\times 6.022 \\times 10^{23} = 2.710 \\times 10^{22}\\text{ atoms}\\).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-069",
    text: "During the rainy season, exposed copper vessels develop a greenish coating over time due to corrosion. What chemical compound constitutes this green patina?",
    options: [
      "Basic Copper Carbonate [\\(\\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2\\)]",
      "Copper Sulfate pentahydrate [\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)]",
      "Copper(II) Sulfide [\\(\\text{CuS}\\)]",
      "Copper(I) Oxide [\\(\\text{Cu}_2\\text{O}\\)]"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When metallic copper is exposed to moist air over long durations, it undergoes atmospheric corrosion:
- Copper reacts slowly with atmospheric carbon dioxide (\\(\\text{CO}_2\\)), oxygen (\\(\\text{O}_2\\)), and moisture (\\(\\text{H}_2\\text{O}\\)):
\\[
2\\text{Cu}_{(s)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)} + \\text{O}_{2(g)} \\longrightarrow \\mathbf{\\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2}_{(s)}
\\]
The product is **basic copper carbonate** (a mixture of copper carbonate and copper hydroxide), which forms an insoluble protective green surface patina.

### 2. Physical Context & Practical Illustration:
The Statue of Liberty is clad in copper sheets and owes its iconic green appearance entirely to this natural patina of basic copper carbonate. Cleaning copper cookware with acidic lemon juice or tamarind (citric/tartaric acid) dissolves the basic carbonate, restoring shiny reddish-brown copper.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Basic copper carbonate [\\(\\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2\\)] is the chemical compound responsible for the green coating.
- **Option B is incorrect**: Copper sulfate is blue vitriol, not formed by atmospheric corrosion.
- **Option C is incorrect**: Copper sulfide is black, formed by reaction with hydrogen sulfide gas.
- **Option D is incorrect**: Copper(I) oxide is reddish-brown.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.1-OSC-070",
    text: "What is the actual mass in grams of a single Nitrogen atom (\\(^{14}\\text{N}\\))? (Given: \\(N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}\\), \\(1\\text{ u} = 1.6605 \\times 10^{-24}\\text{ g}\\))",
    options: [
      "\\(14.0\\text{ g}\\)",
      "\\(1.66 \\times 10^{-24}\\text{ g}\\)",
      "\\(4.65 \\times 10^{-23}\\text{ g}\\)",
      "\\(2.325 \\times 10^{-23}\\text{ g}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The mass of one mole of nitrogen atoms (\\(6.022 \\times 10^{23}\\) atoms) is \\(14.0\\text{ g}\\).
To find the mass of a single nitrogen atom:
\\[
m_{\\text{single atom}} = \\frac{\\text{Molar mass } M}{N_A} = \\frac{14.0\\text{ g/mol}}{6.02214 \\times 10^{23}\\text{ mol}^{-1}}
\\]
\\[
m_{\\text{single atom}} = 14.0 \\times (1.66054 \\times 10^{-24}\\text{ g}) = 2.3248 \\times 10^{-23}\\text{ g} \\approx 2.325 \\times 10^{-23}\\text{ g}
\\]

### 2. Physical Context & Practical Illustration:
This calculation underscores the microscopic scale of subatomic matter: it takes over 43 sextillion nitrogen atoms to weigh just one single gram.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(14.0\\text{ g}\\) is the mass of one full mole (\\(6.022 \\times 10^{23}\\)) of nitrogen atoms, not a single atom.
- **Option B is incorrect**: \\(1.66 \\times 10^{-24}\\text{ g}\\) is the mass of \\(1\\text{ u}\\) (approximately one hydrogen atom).
- **Option C is incorrect**: \\(4.65 \\times 10^{-23}\\text{ g}\\) is the mass of a diatomic \\(\\text{N}_2\\) molecule.
- **Option D is correct**: \\(m = 14 / (6.022 \\times 10^{23}) = 2.325 \\times 10^{-23}\\text{ g}\\).`
  }
];

module.exports = { ch4_part2 };
