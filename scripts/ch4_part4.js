// scripts/ch4_part4.js - Chapter 4 (Measurement of Matter / Topic 4.2) Questions 1-40 Gold Standard Enhancements
const ch4_part4 = [
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-001",
    text: "Among the following Period 2 elements, which one has the smallest atomic radius? (Lithium, Boron, Nitrogen, Oxygen)",
    options: [
      "Lithium (Li, atomic number 3)",
      "Oxygen (O, atomic number 8)",
      "Boron (B, atomic number 5)",
      "Nitrogen (N, atomic number 7)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Across a period from left to right in the periodic table:
1. Electrons are sequentially added to the **same principal quantum shell** (for Period 2, the \\(n=2\\) shell).
2. Concurrently, the nuclear charge (number of protons, \\(Z\\)) increases steadily:
\\[
Z_{\\text{eff}} = Z - \\sigma
\\]
where \\(\\sigma\\) is the screening/shielding constant. Because electrons in the same shell shield one another poorly, the effective nuclear charge (\\(Z_{\\text{eff}}\\)) increases monotonically across the period.
3. The stronger electrostatic attraction pulls the electron cloud closer to the nucleus, causing atomic radius to **decrease from left to right**:
\\[
r_{\\text{Li}} (152\\text{ pm}) > r_{\\text{B}} (88\\text{ pm}) > r_{\\text{N}} (70\\text{ pm}) > r_{\\text{O}} (66\\text{ pm})
\\]
Therefore, **Oxygen** has the smallest atomic radius among these elements.

### 2. Physical Context & Practical Illustration:
Even though an oxygen atom has more total subatomic particles than a lithium atom, its 8 protons exert a much stronger radial pull on the \\(n=2\\) electrons than lithium's 3 protons, compacting the oxygen atom to less than half the diameter of lithium.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Lithium is at the extreme left of Period 2 and has the largest radius (152 pm).
- **Option B is correct**: Oxygen is furthest to the right among the given choices, possessing the highest \\(Z_{\\text{eff}}\\) and smallest radius (66 pm).
- **Option C is incorrect**: Boron (88 pm) is larger than nitrogen and oxygen.
- **Option D is incorrect**: Nitrogen (70 pm) is larger than oxygen.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-002",
    text: "Which halogen exists as a dark purple-black, lustrous solid at room temperature and sublimates into a violet-colored vapor upon mild heating?",
    options: [
      "Chlorine (\\(\\text{Cl}_2\\))",
      "Bromine (\\(\\text{Br}_2\\))",
      "Iodine (\\(\\text{I}_2\\))",
      "Fluorine (\\(\\text{F}_2\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Group 17 (the Halogens), the physical state at room temperature changes progressively down the group due to increasing atomic size and polarizability:
\\[
\\text{London Dispersion Forces} \\propto \\text{Polarizability} \\propto \\text{Total Electrons}
\\]
- **Fluorine (\\(\\text{F}_2\\))**: Pale yellow gas (few electrons, very weak dispersion forces).
- **Chlorine (\\(\\text{Cl}_2\\))**: Greenish-yellow gas.
- **Bromine (\\(\\text{Br}_2\\))**: Dark reddish-brown volatile liquid.
- **Iodine (\\(\\text{I}_2\\))**: **Dark purple/violet-black crystalline solid** with metallic luster that readily sublimates into a dense violet vapor upon heating.

### 2. Physical Context & Practical Illustration:
Iodine crystals are used in tincture of iodine (an antiseptic) and iodine starch tests in biology. Heating solid iodine crystals in a dry test tube produces striking purple fumes that re-crystallize directly onto cooler glass walls without melting into liquid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Chlorine is a greenish-yellow gas.
- **Option B is incorrect**: Bromine is a reddish-brown liquid.
- **Option C is correct**: Iodine is a purple-black crystalline solid that forms violet vapors.
- **Option D is incorrect**: Fluorine is a pale yellow, highly corrosive gas.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-003",
    text: "In the periodic table, the elements possessing the LARGEST atomic radii within any given period are found in which group?",
    options: [
      "Halogens (Group 17)",
      "Noble gases (Group 18)",
      "Chalcogens (Group 16)",
      "Alkali metals (Group 1)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The periodic trend in atomic radius is governed by two competing mechanisms:
1. **Across a Period (left to right)**: The effective nuclear charge increases (\\(Z_{\\text{eff}} \\uparrow\\)) while the principal quantum number \\(n\\) remains unchanged. This contracts the electron shell, causing atomic radius to **decrease** from left to right.
2. **At Group 1 (extreme left)**: The single valence electron experiences the minimum effective nuclear charge (\\(Z_{\\text{eff}} = Z - \\sigma \\approx 1\\text{ to } 2.2\\)), leaving the outermost s-orbital maximally expanded.
Consequently, within each period, the **Alkali metals (Group 1)** have the largest atomic radii.

### 2. Physical Context & Practical Illustration:
Cesium (Cs) and Francium (Fr) at the bottom left of the periodic table have the largest atomic radii of all known elements (Cesium radius \\(\\approx 265\\text{ pm}\\)), which explains their extremely low ionization energies and intense chemical reactivity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Halogens (Group 17) have near-maximum \\(Z_{\\text{eff}}\\) and possess the smallest covalent radii in their periods.
- **Option B is incorrect**: Noble gases have small bonded radii (their non-bonded van der Waals radii are measured differently, but they do not have the largest chemically bonded radii).
- **Option C is incorrect**: Chalcogens are on the right side and have small radii.
- **Option D is correct**: Group 1 alkali metals have the lowest effective nuclear charge and the largest atomic radii.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-004",
    text: "Which family of chemical elements in the periodic table exhibits the LOWEST electronegativity (highest electropositivity)?",
    options: [
      "Halogens",
      "Alkaline earth metals",
      "Alkali metals",
      "Noble gases"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electronegativity is the measure of an atom's relative tendency to attract a shared pair of electrons in a chemical bond:
- **Periodic Trend**: Electronegativity increases across a period (left to right) and decreases down a group (top to bottom).
- **Alkali Metals (Group 1)**: Possess the largest atomic radii and the lowest effective nuclear charges in their respective periods:
\\[
\\text{Electronegativity} \\propto \\frac{Z_{\\text{eff}}}{r^2}
\\]
With Pauling electronegativity values ranging from \\(1.0\\) (Lithium) down to \\(0.7\\) (Cesium and Francium), alkali metals have the weakest electron-attracting power and are the most electropositive elements known.

### 2. Physical Context & Practical Illustration:
Because alkali metals hold their single valence electron so loosely, they react violently with water and non-metals to shed that electron and form stable cations (\\(\\text{M}^+\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Halogens are the *most* electronegative elements (Fluorine = 4.0).
- **Option B is incorrect**: Alkaline earth metals (Group 2) have higher electronegativities than alkali metals (Be = 1.5, Mg = 1.2).
- **Option C is correct**: Alkali metals have the lowest electronegativity values.
- **Option D is incorrect**: Noble gases do not typically form covalent bonds and have undefined Pauling electronegativities.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-005",
    text: "Which pioneering chemist successfully predicted the existence and detailed chemical properties of several undiscovered elements (such as Eka-boron, Eka-aluminum, and Eka-silicon) using his periodic table?",
    options: [
      "Johann Wolfgang Döbereiner",
      "John Newlands",
      "Dmitri Ivanovich Mendeleev",
      "Niels Bohr"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1869, Russian chemist **Dmitri Mendeleev** formulated Mendeleev's Periodic Law:
> *"The physical and chemical properties of the elements are a periodic function of their atomic masses."*

Mendeleev recognized gaps in his table and boldly predicted that elements yet undiscovered would fill them. He named them using the Sanskrit prefix *Eka-* ('one step beyond'):
- **Eka-boron** \\(\\longrightarrow\\) discovered in 1879 as **Scandium (Sc)**
- **Eka-aluminum** \\(\\longrightarrow\\) discovered in 1875 as **Gallium (Ga)**
- **Eka-silicon** \\(\\longrightarrow\\) discovered in 1886 as **Germanium (Ge)**
The discovered elements matched Mendeleev's predicted atomic masses, densities, melting points, and oxide formulas with astonishing precision.

### 2. Physical Context & Practical Illustration:
For example, Mendeleev predicted Eka-aluminum would have atomic mass 68, density \\(5.9\\text{ g/cm}^3\\), and formula \\(\\text{Ea}_2\\text{O}_3\\). When Gallium was isolated by Paul-Émile Lecoq de Boisbaudran, its measured atomic mass was \\(69.7\\), density \\(5.94\\text{ g/cm}^3\\), and formula \\(\\text{Ga}_2\\text{O}_3\\), cementing the periodic table's worldwide acceptance.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Döbereiner identified Law of Triads (1829).
- **Option B is incorrect**: Newlands proposed the Law of Octaves (1864).
- **Option C is correct**: Mendeleev predicted undiscovered elements with remarkable accuracy.
- **Option D is incorrect**: Bohr formulated the quantum mechanical atomic model.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-006",
    text: "In 1913, English physicist Henry Moseley established that the fundamental basis of elemental classification is:",
    options: [
      "Atomic number (nuclear proton charge, Z)",
      "Atomic mass (total mass number, A)",
      "Density of the elemental solid",
      "Number of neutrons in the nucleus"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, Henry Moseley studied the characteristic X-ray emission spectra of various elements bombarded with high-energy cathode rays. He discovered **Moseley's Law**:
\\[
\\sqrt{\\nu} = a(Z - b)
\\]
where:
- \\(\\nu\\) = frequency of characteristic \\(K_\\alpha\\) X-ray spectral lines
- \\(Z\\) = positive nuclear charge (atomic number)
- \\(a, b\\) = constants
Plotting \\(\\sqrt{\\nu}\\) against atomic number \\(Z\\) yielded a perfect straight line, proving that **atomic number** (the number of positive protons in the nucleus), rather than atomic mass, is the fundamental property governing elemental identity and periodicity.

### 2. Physical Context & Practical Illustration:
Moseley's discovery resolved several longstanding anomalies in Mendeleev's table, such as why Tellurium (\\(Z=52\\), mass 127.6) must precede Iodine (\\(Z=53\\), mass 126.9), and why Argon (\\(Z=18\\), mass 39.9) precedes Potassium (\\(Z=19\\), mass 39.1).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Moseley demonstrated that atomic number (\\(Z\\)) is the true basis of periodic classification.
- **Option B is incorrect**: Atomic mass was used by Mendeleev and Newlands, leading to isotopic anomalies.
- **Option C is incorrect**: Density varies irregularly.
- **Option D is incorrect**: Neutron count varies across isotopes of the same element.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-007",
    text: "Which of the following statements is TRUE regarding the transition elements (d-block elements) of the periodic table?",
    options: [
      "They have completely filled outermost shells and zero chemical valency",
      "They are all non-metals located exclusively in Group 17",
      "They have only one incomplete outermost shell while all inner shells are filled",
      "They have their two outermost shells incomplete and occupy Groups 3 to 12"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Transition elements** occupy the central d-block of the periodic table spanning **Groups 3 to 12**:
1. **Electronic Configuration**: Their general valence electronic configuration is:
\\[
(n-1)d^{1-10} ns^{1-2}
\\]
2. **Incomplete Shells**: Both the outermost shell (\\(n\\)) and the penultimate inner d-subshell (\\(n-1\\)) are partially filled during electron building (Aufbau principle).
3. **Properties**: They are all heavy metals exhibiting variable oxidation states, colored ionic complexes, high melting points, and catalytic properties.

### 2. Physical Context & Practical Illustration:
Familiar engineering metals such as Iron (Fe), Copper (Cu), Chromium (Cr), Nickel (Ni), Gold (Au), and Platinum (Pt) are transition metals. Because electrons from both the \\(4s\\) and \\(3d\\) levels can participate in bonding, iron can form both \\(\\text{Fe}^{2+}\\) (green) and \\(\\text{Fe}^{3+}\\) (yellow-brown) compounds.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Characteristic of noble gases (Group 18).
- **Option B is incorrect**: Characteristic of halogens; transition elements are all metals.
- **Option C is incorrect**: Representative/normal elements (s and p blocks) have only their outermost shell incomplete.
- **Option D is correct**: Transition elements possess two incomplete outermost shells and occupy Groups 3 to 12.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-008",
    text: "Which of the following statements correctly describes how atomic radius changes when moving down a group in the periodic table?",
    options: [
      "Atomic radius decreases because nuclear charge increases down the group",
      "Atomic radius remains completely constant down the group",
      "Atomic radius increases because a new principal electronic shell is added at each successive period",
      "Atomic radius first increases and then abruptly drops to zero"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Moving down any group (column) in the periodic table:
1. At each successive period, a **new principal energy shell** is added (e.g., Li: \\(n=2\\), Na: \\(n=3\\), K: \\(n=4\\), Rb: \\(n=5\\)).
2. The distance between the positively charged nucleus and the outermost valence electrons increases significantly:
\\[
r_n \\propto \\frac{n^2}{Z_{\\text{eff}}}
\\]
3. The increased shielding effect of the inner electron shells counterbalances the increase in nuclear charge, resulting in an effective nuclear charge (\\(Z_{\\text{eff}}\\)) that remains roughly constant down the group.
Consequently, the effect of adding new principal shells dominates, causing atomic radius to **increase down the group**.

### 2. Physical Context & Practical Illustration:
In Group 1 alkali metals:
- Lithium (Li, 2 shells): \\(152\\text{ pm}\\)
- Sodium (Na, 3 shells): \\(186\\text{ pm}\\)
- Potassium (K, 4 shells): \\(227\\text{ pm}\\)
- Cesium (Cs, 6 shells): \\(265\\text{ pm}\\)
Each added concentric electron shell visibly swells the atom's size.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Radius increases down a group; nuclear charge increase is offset by inner-shell shielding.
- **Option B is incorrect**: Atomic size changes systematically, not constantly.
- **Option C is correct**: Atomic radius increases down a group due to the addition of successive principal electron shells.
- **Option D is incorrect**: The trend is smooth and monotonically increasing.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-009",
    text: "Arrange the elements Boron (B), Carbon (C), Nitrogen (N), Fluorine (F), and Silicon (Si) in DECREASING order of their atomic radii:",
    options: [
      "\\(\\text{F} > \\text{N} > \\text{C} > \\text{B} > \\text{Si}\\)",
      "\\(\\text{Si} > \\text{F} > \\text{N} > \\text{C} > \\text{B}\\)",
      "\\(\\text{Si} > \\text{B} > \\text{C} > \\text{N} > \\text{F}\\)",
      "\\(\\text{B} > \\text{C} > \\text{N} > \\text{F} > \\text{Si}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing the positions in the periodic table:
- **Period 2 elements**: B (\\(Z=5\\)), C (\\(Z=6\\)), N (\\(Z=7\\)), F (\\(Z=9\\)).
  - Across Period 2, atomic radius decreases left-to-right due to increasing \\(Z_{\\text{eff}}\\):
\\[
r_{\\text{B}} (88\\text{ pm}) > r_{\\text{C}} (77\\text{ pm}) > r_{\\text{N}} (70\\text{ pm}) > r_{\\text{F}} (64\\text{ pm})
\\]
- **Period 3 element**: Silicon (Si, \\(Z=14\\)).
  - Silicon has 3 electronic shells (\\(2, 8, 4\\)), while Period 2 elements have only 2 shells (\\(n=2\\)).
  - Because of the additional third shell, Silicon is significantly larger than all Period 2 elements listed:
\\[
r_{\\text{Si}} \\approx 117\\text{ pm}
\\]
Combining both trends:
\\[
\\mathbf{\\text{Si} (117\\text{ pm}) > \\text{B} (88\\text{ pm}) > \\text{C} (77\\text{ pm}) > \\text{N} (70\\text{ pm}) > \\text{F} (64\\text{ pm})}
\\]

### 2. Physical Context & Practical Illustration:
Number of electron shells is always the primary factor in atomic size: 3-shell atoms are almost always larger than 2-shell atoms. Within the same shell count, increasing nuclear charge pulls electrons tighter.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Inverts the period trend (lists smallest first).
- **Option B is incorrect**: Places Fluorine before Boron.
- **Option C is correct**: \\(\\text{Si} > \\text{B} > \\text{C} > \\text{N} > \\text{F}\\) correctly accounts for shell count and periodic contraction.
- **Option D is incorrect**: Places 3-shell Silicon as smallest.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-010",
    text: "In the Modern Periodic Table, how many horizontal periods and vertical groups are present?",
    options: [
      "7 periods and 16 groups",
      "7 periods and 18 groups",
      "8 periods and 18 groups",
      "8 periods and 16 groups"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The IUPAC Modern Long Form of the Periodic Table is organized as:
- **7 Horizontal Rows**, termed **Periods**:
  - Period 1: 2 elements (H, He)
  - Period 2 & 3: 8 elements each (short periods)
  - Period 4 & 5: 18 elements each (long periods)
  - Period 6: 32 elements (very long period, includes Lanthanoids)
  - Period 7: 32 elements (includes Actinoids)
- **18 Vertical Columns**, termed **Groups** (numbered 1 to 18 according to modern IUPAC convention).

### 2. Physical Context & Practical Illustration:
The period number (1 to 7) corresponds to the highest principal quantum shell (\\(n\\)) occupied by electrons, while the group number (1 to 18) reflects valence electron configurations and chemical family similarities.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Mentions 16 groups (older Roman numeral notation VIII was counted differently).
- **Option B is correct**: Exactly 7 periods and 18 groups.
- **Option C is incorrect**: There are 7 periods, not 8.
- **Option D is incorrect**: Incorrect periods and groups.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-011",
    text: "In the Modern Periodic Table, chemical elements are systematically arranged in the increasing order of their:",
    options: [
      "Atomic masses (mass numbers)",
      "Atomic numbers (nuclear proton charge)",
      "Relative atomic densities",
      "Number of valence neutrons"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Modern Periodic Law** (established by Henry Moseley in 1913) states:
> *"The physical and chemical properties of the elements are periodic functions of their atomic numbers."*

Elements are arranged strictly in ascending order of their **atomic number (\\(Z\\))**, which equals the number of protons in the atomic nucleus:
\\[
Z = 1 (\\text{H}), \\; 2 (\\text{He}), \\; 3 (\\text{Li}), \\dots, \\; 118 (\\text{Og})
\\]
Because atomic number is an integer that increases by exactly \\(1\\) from element to element, it provides a flawless, continuous classification sequence without gaps or anomalies.

### 2. Physical Context & Practical Illustration:
Arranging by atomic number automatically resolves the placement of isotopes (all isotopes of carbon have \\(Z = 6\\), occupying the exact same position) and anomalous mass pairs like Argon (\\(Z = 18\\), mass 39.9) and Potassium (\\(Z = 19\\), mass 39.1).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Atomic mass was used in historical tables (Mendeleev, Newlands) and produced anomalies.
- **Option B is correct**: The modern periodic table arranges elements by increasing atomic number (\\(Z\\)).
- **Option C is incorrect**: Density does not exhibit regular monotonic progression.
- **Option D is incorrect**: Neutron count does not govern chemical periodicity.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-012",
    text: "Two elements X and Y belong to the exact same vertical group in the modern periodic table. Which of the following features do they definitely share in common?",
    options: [
      "They have the exact same total number of electron shells",
      "They have the exact same number of valence electrons in their outermost shells",
      "They have identical atomic numbers and masses",
      "They have identical atomic radii"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the periodic table, a **Group** consists of elements that have identical outermost valence electron configurations:
\\[
\\text{Valence configuration of Group } g = \\text{invariant}
\\]
For example:
- All Group 1 alkali metals (Li, Na, K, Rb, Cs) have \\(ns^1\\) (exactly **1 valence electron**).
- All Group 2 alkaline earths (Be, Mg, Ca, Sr, Ba) have \\(ns^2\\) (exactly **2 valence electrons**).
- All Group 17 halogens (F, Cl, Br, I) have \\(ns^2 np^5\\) (exactly **7 valence electrons**).
Because chemical bonding and reactions depend primarily on valence electrons, elements in the same group exhibit very similar chemical properties.

### 2. Physical Context & Practical Illustration:
Sodium (2,8,1) and Potassium (2,8,8,1) both have 1 valence electron. Consequently, both form \\(+1\\) ions, react vigorously with water to produce hydrogen gas and hydroxides (NaOH, KOH), and form white crystalline chloride salts (NaCl, KCl).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The number of electron shells increases down the group with period number.
- **Option B is correct**: Elements in the same group possess the same number of valence electrons.
- **Option C is incorrect**: Atomic numbers and masses increase down the group.
- **Option D is incorrect**: Atomic radii increase down the group.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-013",
    text: "How many total chemical elements are present in the second period (Period 2) of the modern periodic table?",
    options: [
      "\\(2\\text{ elements}\\)",
      "\\(8\\text{ elements}\\)",
      "\\(18\\text{ elements}\\)",
      "\\(32\\text{ elements}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The number of elements in a period corresponds to the maximum electron capacity of the orbitals being filled in that period:
- In Period 2, electrons fill the \\(2s\\) and \\(2p\\) subshells (principal shell \\(n = 2\\)):
  - \\(2s\\) orbital holds \\(2\\) electrons.
  - Three \\(2p\\) orbitals hold \\(3 \\times 2 = 6\\) electrons.
  - Total capacity = \\(2 + 6 = 8\\text{ electrons}\\).
Thus, Period 2 comprises exactly **\\(8\\text{ elements}\\)**:
\\[
\\text{Lithium (Li, 3)} \\longrightarrow \\text{Neon (Ne, 10)}
\\]
Namely: Li, Be, B, C, N, O, F, Ne.

### 2. Physical Context & Practical Illustration:
Period 2 is termed a 'short period'. It begins with the soft, highly reactive alkali metal Lithium and terminates with the chemically inert noble gas Neon.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Period 1 contains 2 elements (H and He).
- **Option B is correct**: Period 2 contains exactly 8 elements.
- **Option C is incorrect**: Period 4 and Period 5 each contain 18 elements.
- **Option D is incorrect**: Period 6 contains 32 elements.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-014",
    text: "On moving from left to right across a period in the modern periodic table, what systematic change occurs in the chemical nature (acidity/basicity) of the oxides of elements?",
    options: [
      "The acidic nature of the oxides increases (basic \\(\\to\\) amphoteric \\(\\to\\) acidic)",
      "The basic nature of the oxides increases significantly",
      "The oxides remain neutral throughout the entire period",
      "The oxides transition from strongly acidic to strongly basic"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Across a period from left to right:
1. Metallic character decreases, while non-metallic character and electronegativity increase:
\\[
\\text{Metal} \\longrightarrow \\text{Metalloid} \\longrightarrow \\text{Non-metal}
\\]
2. Metallic oxides are typically basic (releasing \\(\\text{OH}^-\\) in water or reacting with acids), whereas non-metallic oxides are covalent and acidic (forming oxoacids in water):
- **Period 3 Oxides Demonstration**:
  - \\(\\text{Na}_2\\text{O}\\): Strongly basic
  - \\(\\text{MgO}\\): Moderately basic
  - \\(\\text{Al}_2\\text{O}_3\\): **Amphoteric** (reacts with both acids and bases)
  - \\(\\text{SiO}_2\\): Weakly acidic
  - \\(\\text{P}_4\\text{O}_{10}\\): Acidic
  - \\(\\text{SO}_3\\): Strongly acidic
  - \\(\\text{Cl}_2\\text{O}_7\\): Extremely acidic
Therefore, across any period, the **acidity of the oxides steadily increases**.

### 2. Physical Context & Practical Illustration:
Dissolving \\(\\text{Na}_2\\text{O}\\) in water produces strong caustic base \\(\\text{NaOH}\\) (pH > 13). Moving across to sulfur, dissolving \\(\\text{SO}_3\\) produces battery-grade sulfuric acid \\(\\text{H}_2\\text{SO}_4\\) (pH < 1).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Oxide nature transitions progressively from strongly basic to amphoteric to strongly acidic across a period.
- **Option B is incorrect**: Basicity decreases, not increases.
- **Option C is incorrect**: Oxides exhibit dramatic chemical pH variation across a period.
- **Option D is incorrect**: Inverts the true direction of the periodic property.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-015",
    text: "Which two fundamental periodic properties of elements systematically DECREASE when moving from left to right across a period?",
    options: [
      "Electronegativity and Non-metallic character",
      "Ionization enthalpy and Electron affinity",
      "Nuclear charge and Valency",
      "Atomic radius and Metallic character"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Across a period from left to right:
1. **Atomic Radius**: The effective nuclear charge (\\(Z_{\\text{eff}}\\)) increases while electrons enter the same shell, pulling the electron cloud inward:
\\[
r_{\\text{atomic}} \\text{ decreases}
\\]
2. **Metallic Character (Electropositivity)**: As atoms become smaller and \\(Z_{\\text{eff}}\\) increases, valence electrons are held more tightly, reducing the tendency to lose electrons (forming cations):
\\[
\\text{Tendency to lose electrons } \\downarrow \\implies \\text{Metallic character decreases}
\\]
Conversely, electronegativity, ionization energy, and non-metallic character all *increase* across a period.

### 2. Physical Context & Practical Illustration:
In Period 3, Sodium on the far left is a soft, shiny metal with a large radius (186 pm) that easily loses electrons. Chlorine on the far right is a non-metallic gas with a small radius (99 pm) that vigorously gains electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Both electronegativity and non-metallic character *increase* across a period.
- **Option B is incorrect**: Ionization energy and electron affinity generally *increase* across a period.
- **Option C is incorrect**: Nuclear charge (\\(Z\\)) increases continuously.
- **Option D is correct**: Both atomic radius and metallic character systematically decrease across a period.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-016",
    text: "In the layout of the Modern Periodic Table, where are the vast majority of metallic elements situated?",
    options: [
      "Exclusively in the upper right-hand corner",
      "Only along the zig-zag metalloid border line",
      "On the left-hand side, in the central d-block, and in the bottom f-block",
      "Exclusively in Group 18"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Over \\(78\\%\\) of all known chemical elements are metals. In the periodic table:
1. **Left-hand Side (s-block)**: Alkali metals (Group 1) and Alkaline earth metals (Group 2) are highly electropositive reactive metals.
2. **Center (d-block)**: Groups 3 to 12 comprise the heavy transition metals.
3. **Bottom (f-block)**: Lanthanoids and Actinoids (inner transition metals) placed in two separate rows at the bottom.
4. **Lower p-block**: Post-transition metals like Al, Ga, In, Sn, Tl, Pb, Bi.
Non-metals are confined exclusively to the top right-hand corner of the p-block, separated from metals by a zig-zag line of metalloids (B, Si, Ge, As, Sb, Te, Po).

### 2. Physical Context & Practical Illustration:
Metals dominate the physical world: from structural steel (Fe) and wiring (Cu) to lightweight aerospace alloys (Al, Ti). Their broad placement on the left and center reflects their characteristic low ionization energy and electropositive nature.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The upper right-hand corner contains non-metals and noble gases.
- **Option B is incorrect**: The zig-zag line contains metalloids (semi-metals).
- **Option C is correct**: Metals occupy the entire left side, center (d-block), and bottom (f-block).
- **Option D is incorrect**: Group 18 consists strictly of non-metallic noble gases.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-017",
    text: "Who made the first historically successful and comprehensive attempt to classify all known chemical elements in a tabular periodic layout?",
    options: [
      "John Dalton",
      "Antoine Lavoisier",
      "Dmitri Ivanovich Mendeleev",
      "Henry Moseley"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
While Lavoisier classified elements into metals and non-metals (1789), Döbereiner grouped them into triads (1829), and Newlands proposed octaves (1864), the **first comprehensive and universally successful classification** was achieved by **Dmitri Mendeleev** in 1869:
- Mendeleev organized all 63 elements known at the time into a 2D grid based on atomic mass and recurring chemical formulas of hydrides and oxides (\\(R_2\\text{O}, RO, R_2\\text{O}_3\\), etc.).
- His table left intentional gaps for undiscovered elements, predicting their properties accurately and establishing the fundamental framework of modern chemistry.

### 2. Physical Context & Practical Illustration:
Mendeleev's periodic table organized scattered chemical knowledge into a unified, predictive scientific discipline, earning him the title of the 'Father of the Periodic Table'.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Dalton developed atomic theory, but not a periodic table classification.
- **Option B is incorrect**: Lavoisier compiled an early list of 33 elements divided simply as metals/non-metals.
- **Option C is correct**: Mendeleev created the first comprehensive and successful periodic table.
- **Option D is incorrect**: Moseley later modernized the table using atomic numbers in 1913.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-018",
    text: "In Mendeleev's periodic table, which newly discovered chemical element was found to correspond precisely to the predicted element 'Eka-aluminum'?",
    options: [
      "Scandium (Sc)",
      "Gallium (Ga)",
      "Germanium (Ge)",
      "Indium (In)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Mendeleev predicted three landmark elements that had not yet been discovered:
1. **Eka-boron** \\(\\longrightarrow\\) discovered by Lars Fredrik Nilson (1879) as **Scandium (Sc)**
2. **Eka-aluminum** \\(\\longrightarrow\\) discovered by Paul-Émile Lecoq de Boisbaudran (1875) as **Gallium (Ga)**
3. **Eka-silicon** \\(\\longrightarrow\\) discovered by Clemens Winkler (1886) as **Germanium (Ge)**

For Eka-aluminum vs Gallium:
- Predicted atomic mass: \\(68\\text{ u}\\) \\(\\to\\) Discovered mass: \\(69.7\\text{ u}\\)
- Predicted density: \\(5.9\\text{ g/cm}^3\\) \\(\\to\\) Discovered density: \\(5.94\\text{ g/cm}^3\\)
- Predicted oxide: \\(\\text{Ea}_2\\text{O}_3\\) \\(\\to\\) Discovered oxide: \\(\\text{Ga}_2\\text{O}_3\\)
Therefore, Eka-aluminum is **Gallium**.

### 2. Physical Context & Practical Illustration:
Gallium is a remarkable metal with a melting point of just \\(29.76^\circ\\text{C}\\) (it literally melts in the palm of your hand). It is now widely used in semiconductor optoelectronics and LEDs (gallium arsenide, GaAs).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Scandium corresponds to Eka-boron.
- **Option B is correct**: Gallium corresponds to Eka-aluminum.
- **Option C is incorrect**: Germanium corresponds to Eka-silicon.
- **Option D is incorrect**: Indium was already known prior to Mendeleev's prediction.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-019",
    text: "According to Mendeleev's original Periodic Law, the physical and chemical properties of elements are periodic functions of their:",
    options: [
      "Atomic numbers",
      "Atomic masses",
      "Atomic radii",
      "Electronegativity values"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Mendeleev's Periodic Law** (1869) was formulated based on the premise that atomic mass was the most fundamental characteristic of an atom:
> *"The physical and chemical properties of the elements are periodic functions of their atomic masses."*

When elements were arranged in increasing order of their atomic weights, elements with similar chemical properties (e.g., similar formulas for hydrides and oxides) recurred at regular periodic intervals.
(It was only in 1913 that Moseley updated this to *atomic numbers*).

### 2. Physical Context & Practical Illustration:
Relying on atomic mass was the greatest triumph of 19th-century chemistry, although it created minor inversions (like Te-I and Co-Ni) that could only be explained after the discovery of the nuclear proton and atomic number.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Atomic number is the basis of the *Modern* Periodic Law, not Mendeleev's.
- **Option B is correct**: Mendeleev's original periodic law was strictly based on atomic masses.
- **Option C is incorrect**: Atomic radius is a secondary periodic property.
- **Option D is incorrect**: Electronegativity was defined decades later by Linus Pauling.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-020",
    text: "Which of the following statements regarding the structure of the Modern Periodic Table is CORRECT?",
    options: [
      "Elements in the same period possess the same number of occupied electron shells",
      "Elements in the same period possess the exact same number of valence electrons",
      "Elements in the same group possess the same number of occupied electron shells",
      "The Modern Periodic Table contains 18 horizontal periods and 7 vertical groups"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the Modern Periodic Table:
1. **Period Principle**: The period number (\\(n = 1, 2, \\dots, 7\\)) denotes the highest principal quantum energy shell occupied by electrons in the ground state:
\\[
\\text{Period Number } n = \\text{Total occupied electron shells}
\\]
For example, all Period 3 elements (Na, Mg, Al, Si, P, S, Cl, Ar) have electrons occupying exactly **3 shells** (K, L, and M shells).
2. **Group Principle**: Elements in the same vertical column (group) share the same number of *valence electrons*.

### 2. Physical Context & Practical Illustration:
As you move across Period 3 from Sodium (2,8,1) to Argon (2,8,8), electrons fill the third (M) shell. The shell count remains invariant at 3 throughout the entire period.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Elements in the same period have the exact same number of occupied electronic shells.
- **Option B is incorrect**: Valence electrons increase from 1 to 8 across a period.
- **Option C is incorrect**: Shell count increases by 1 for each successive element down a group.
- **Option D is incorrect**: Inverts the structure (there are 7 periods and 18 groups).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-021",
    text: "Which family of chemical elements comprises Group 1 of the modern periodic table (excluding Hydrogen)?",
    options: [
      "Alkali metals",
      "Alkaline earth metals",
      "Halogens",
      "Noble gases"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Group 1 elements (Lithium, Sodium, Potassium, Rubidium, Cesium, Francium) are universally known as **Alkali Metals**:
- **Electronic Configuration**: Each has a single valence electron in an s-orbital (\\(ns^1\\)).
- **Origin of Name**: They react vigorously with water to produce soluble, strongly alkaline hydroxides and hydrogen gas:
\\[
2\\text{M}_{(s)} + 2\\text{H}_2\\text{O}_{(l)} \\longrightarrow 2\\text{MOH}_{(aq)} + \\text{H}_{2(g)}
\\]
- The resulting metal hydroxides (e.g. \\(\\text{NaOH}\\), \\(\\text{KOH}\\)) are strong bases (alkalis) that turn red litmus paper blue.

### 2. Physical Context & Practical Illustration:
Alkali metals are so soft they can easily be cut with a butter knife and have such low densities that Lithium, Sodium, and Potassium float on water before reacting. Because they oxidize rapidly in air, they are stored submerged under kerosene.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Group 1 elements are the alkali metals.
- **Option B is incorrect**: Group 2 elements are the alkaline earth metals.
- **Option C is incorrect**: Group 17 elements are the halogens.
- **Option D is incorrect**: Group 18 elements are the noble gases.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-022",
    text: "The fundamental statement: \"The physical and chemical properties of the elements are periodic functions of their atomic numbers\" is the formal definition of:",
    options: [
      "Mendeleev's Periodic Law",
      "The Modern Periodic Law",
      "Newlands' Law of Octaves",
      "Döbereiner's Law of Triads"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
This statement is the exact text of the **Modern Periodic Law**, formulated by Henry Moseley in 1913:
\\[
\\text{Properties of Element } X = f(\\text{Atomic Number } Z)
\\]
where \\(Z\\) is the nuclear charge (number of protons).
Because electron configuration and chemical bonding are governed directly by atomic number \\(Z\\), periodic repetition of similar outer electronic configurations occurs at regular intervals (atomic number intervals of 2, 8, 8, 18, 18, 32—the 'magic numbers').

### 2. Physical Context & Practical Illustration:
Unlike Mendeleev's law which was based on atomic mass (and suffered from isotopic and ordering anomalies), the Modern Periodic Law based on atomic number provides an unambiguous, mathematically consistent framework for all 118 known elements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Mendeleev's law is based on atomic *mass*.
- **Option B is correct**: Modern Periodic Law is based on atomic *number*.
- **Option C is incorrect**: Newlands' law states every eighth element has similar properties by atomic mass.
- **Option D is incorrect**: Döbereiner's triads involved arithmetic averages of three atomic masses.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-023",
    text: "Which of the following statements is TRUE regarding 'normal' (representative) elements of the s and p blocks?",
    options: [
      "All their inner and outermost electron shells are completely filled",
      "They have three incomplete outermost electronic shells",
      "They are all non-conductive gases at room temperature",
      "Only their outermost valence shell is incomplete while all inner shells are completely filled"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Normal (Representative) Elements** encompass the elements of the s-block and p-block (Groups 1, 2, and 13 to 17):
1. **Electronic Structure**: In these elements, all internal electronic core shells are completely filled to their maximum capacities:
\\[
\\text{Configuration} = [\\text{Noble Gas Core}] \\; ns^{1-2} np^{0-5}
\\]
2. **Incomplete Shell**: Only the single outermost principal shell (the valence shell, \\(n\\)) is incomplete.
3. During chemical reactions, these atoms gain, lose, or share electrons from this outermost incomplete shell to attain noble gas configuration.

### 2. Physical Context & Practical Illustration:
For example, Sodium (Na: 2, 8, 1) and Chlorine (Cl: 2, 8, 7) have their first two shells completely filled (K=2, L=8); only their outermost M-shell is incomplete. In contrast, transition metals (d-block) have *two* incomplete shells.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Completely filled shells characterize inert noble gases (Group 18).
- **Option B is incorrect**: Three incomplete shells characterize inner transition f-block elements.
- **Option C is incorrect**: Normal elements include solid metals (Na, Mg, Al), liquid (Br), and gases.
- **Option D is correct**: Representative elements have only their single outermost shell incomplete.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-024",
    text: "What are the vertical columns in the periodic table termed?",
    options: [
      "Groups",
      "Periods",
      "Series",
      "Octaves"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In periodic table terminology:
- **Groups**: The **vertical columns** (numbered 1 to 18). Elements in the same group share the same valence shell electron configuration and exhibit similar chemical families.
- **Periods**: The **horizontal rows** (numbered 1 to 7). Elements in the same period have the same number of occupied principal electronic shells.

### 2. Physical Context & Practical Illustration:
For example, Group 1 is the alkali metal family, Group 2 is the alkaline earth family, Group 17 is the halogen family, and Group 18 is the noble gas family.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The vertical columns are called Groups.
- **Option B is incorrect**: Horizontal rows are called Periods.
- **Option C is incorrect**: Series refers to horizontal sub-blocks like the lanthanide series.
- **Option D is incorrect**: Octaves refers to Newlands' historical groupings of 8.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-025",
    text: "In the modern periodic table, how many valence electrons are present in the outermost shell of elements belonging to Group 16 (the Chalcogen family)?",
    options: [
      "\\(2\\text{ electrons}\\)",
      "\\(4\\text{ electrons}\\)",
      "\\(6\\text{ electrons}\\)",
      "\\(8\\text{ electrons}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For main group p-block elements (Groups 13 to 18):
\\[
\\text{Number of valence electrons} = \\text{Group Number} - 10
\\]
For **Group 16** (Oxygen family / Chalcogens: O, S, Se, Te, Po):
\\[
\\text{Valence electrons} = 16 - 10 = \\mathbf{6\\text{ electrons}}
\\]
Their general outermost configuration is \\(ns^2 np^4\\).
To achieve a stable octet (8 electrons), these elements need 2 additional electrons, exhibiting a typical valency of \\(8 - 6 = 2\\) (divalent, forming \\(\\text{O}^{2-}\\), \\(\\text{S}^{2-}\\)).

### 2. Physical Context & Practical Illustration:
Oxygen (\\(2, 6\\)) and Sulfur (\\(2, 8, 6\\)) both have 6 valence electrons, both require 2 electrons for octet completion, and both form similar hydrides (\\(\\text{H}_2\\text{O}\\), \\(\\text{H}_2\\text{S}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: 2 is the valency of the element, not the number of valence electrons.
- **Option B is incorrect**: 4 valence electrons is Group 14 (Carbon family).
- **Option C is correct**: Group 16 elements contain 6 valence electrons.
- **Option D is incorrect**: 8 valence electrons is Group 18 (Noble gases).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-026",
    text: "What is the chemical valency of Chlorine (atomic number Z = 17)?",
    options: [
      "\\(1\\)",
      "\\(7\\)",
      "\\(2\\)",
      "\\(8\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A chlorine atom (\\(Z = 17\\)) has the electronic configuration:
\\[
\\text{Cl}: 2, 8, 7
\\]
- Number of valence electrons = \\(7\\).
- To achieve a stable octet (noble gas configuration of Argon: \\(2, 8, 8\\)), chlorine needs to gain or share \\(1\\) electron:
\\[
\\text{Valency} = 8 - \\text{Valence electrons} = 8 - 7 = 1
\\]
Therefore, the valency of chlorine is **\\(1\\)** (monovalent).

### 2. Physical Context & Practical Illustration:
Chlorine combines with monovalent hydrogen to form hydrogen chloride (HCl) and with monovalent sodium to form sodium chloride (NaCl). In both compounds, chlorine forms exactly one chemical bond.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The valency of chlorine is 1.
- **Option B is incorrect**: 7 is the number of valence electrons, not valency.
- **Option C is incorrect**: Valency of oxygen family.
- **Option D is incorrect**: Octet number.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-027",
    text: "Which chemical element is the FIRST member of the alkali metal family (Group 1)?",
    options: [
      "Hydrogen (H)",
      "Lithium (Li)",
      "Sodium (Na)",
      "Potassium (K)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Although Hydrogen (\\(Z=1\\)) has a \\(1s^1\\) configuration and is placed at the top of Group 1 for structural symmetry, hydrogen is a non-metallic diatomic gas that does not exhibit metallic properties.
The **first true alkali metal** is **Lithium (Li, atomic number 3)**:
- Electronic configuration: \\(2, 1\\)
- Group: 1, Period: 2
- Properties: A soft, silvery, highly electropositive metal with low density (\\(0.534\\text{ g/cm}^3\\)) that reacts with water to form lithium hydroxide (\\(\\text{LiOH}\\)).

### 2. Physical Context & Practical Illustration:
Lithium is the lightest of all solid metals. It floats on hydrocarbon oil and is the key active material in high-energy-density rechargeable batteries for electric vehicles and smartphones.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Hydrogen is a non-metal gas, not an alkali metal.
- **Option B is correct**: Lithium is the first alkali metal.
- **Option C is incorrect**: Sodium is the second alkali metal (Period 3).
- **Option D is incorrect**: Potassium is the third alkali metal (Period 4).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-028",
    text: "The two separate 14-element series displayed at the bottom of the modern periodic table (the Lanthanoids and Actinoids) are collectively known as:",
    options: [
      "Representative normal elements",
      "Alkaline earth metals",
      "Main transition elements",
      "Inner transition elements (f-block)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The Lanthanoids (elements 57/58 to 71) and Actinoids (elements 89/90 to 103) belong to the **f-block**:
1. **Electronic Filling**: In these elements, incoming electrons progressively fill deep inner \\(4f\\) and \\(5f\\) subshells:
\\[
(n-2)f^{1-14} (n-1)d^{0-1} ns^2
\\]
2. **Inner Transition Nomenclature**: Because the f-subshell being filled lies inside the penultimate d-shell (two steps beneath the outermost valence shell), they are termed **inner transition elements**.
3. They are placed at the bottom to maintain a compact, readable rectangular table geometry.

### 2. Physical Context & Practical Illustration:
Lanthanoids (rare earth elements like Neodymium and Europium) are vital for high-strength permanent magnets and smartphone display phosphors. Actinoids include radioactive elements like Uranium and Plutonium used in nuclear energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Representative elements are the s and p block elements.
- **Option B is incorrect**: Alkaline earths are Group 2.
- **Option C is incorrect**: Main transition elements are the d-block elements.
- **Option D is correct**: Lanthanoids and Actinoids are the inner transition elements (f-block).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-029",
    text: "In Mendeleev's Periodic Table, gaps were intentionally left for undiscovered elements. Which of the following elements, discovered later, accurately filled one of these predicted gaps as 'Eka-silicon'?",
    options: [
      "Germanium (Ge)",
      "Chlorine (Cl)",
      "Oxygen (O)",
      "Silicon (Si)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1869, Mendeleev left an empty space below Silicon in Group IV, predicting a new element named **Eka-silicon (Es)**:
- Predicted properties of Eka-silicon:
  - Atomic mass: \\(\\approx 72\\text{ u}\\)
  - Density: \\(5.5\\text{ g/cm}^3\\)
  - Oxide formula: \\(\\text{EsO}_2\\) (density \\(4.7\\text{ g/cm}^3\\))
  - Chloride formula: \\(\\text{EsCl}_4\\) (boiling point \\(< 100^\circ\\text{C}\\))
In 1886, German chemist Clemens Winkler isolated the element **Germanium (Ge, atomic number 32)**:
- Discovered properties of Germanium:
  - Atomic mass: \\(72.6\\text{ u}\\)
  - Density: \\(5.35\\text{ g/cm}^3\\)
  - Oxide formula: \\(\\text{GeO}_2\\) (density \\(4.7\\text{ g/cm}^3\\))
  - Chloride formula: \\(\\text{GeCl}_4\\) (boiling point \\(84^\circ\\text{C}\\))
The near-perfect agreement vindicated Mendeleev's periodic system.

### 2. Physical Context & Practical Illustration:
Germanium is a lustrous, hard-brittle metalloid that played a historic role as the semiconductor material in the world's first solid-state transistors invented at Bell Labs in 1947.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Germanium corresponds to Mendeleev's predicted Eka-silicon.
- **Option B is incorrect**: Chlorine was discovered in 1774 by Scheele, long before Mendeleev.
- **Option C is incorrect**: Oxygen was discovered in the 1770s.
- **Option D is incorrect**: Silicon was isolated in 1824 by Berzelius.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-030",
    text: "Which chemical family in the modern periodic table possesses exactly SEVEN electrons in its outermost valence shell?",
    options: [
      "Alkali metals",
      "Alkaline earth metals",
      "Halogens (Group 17)",
      "Noble gases (Group 18)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Halogen family** comprises Group 17 of the periodic table (Fluorine, Chlorine, Bromine, Iodine, Astatine):
- Outermost electronic configuration: \\(ns^2 np^5\\)
- Total valence electrons = \\(2 + 5 = \\mathbf{7\\text{ electrons}}\\)
Because they need only 1 additional electron to achieve a noble gas octet (\\(ns^2 np^6\\)), halogens have very high electron affinities and form stable monovalent anions (halides: \\(\\text{F}^-, \\text{Cl}^-, \\text{Br}^-, \\text{I}^-\\)).

### 2. Physical Context & Practical Illustration:
The name 'halogen' comes from Greek roots meaning 'salt-producer', because these elements react with metals to produce common ionic salts like sodium chloride (table salt, NaCl) and potassium bromide (KBr).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Alkali metals have 1 valence electron.
- **Option B is incorrect**: Alkaline earth metals have 2 valence electrons.
- **Option C is correct**: Halogens have 7 valence electrons.
- **Option D is incorrect**: Noble gases have 8 valence electrons (except He with 2).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-031",
    text: "An element has the ground-state electronic configuration 2, 8, 1. To which Period and Group of the modern periodic table does it belong?",
    options: [
      "Period 3, Group 1 (Sodium)",
      "Period 1, Group 3",
      "Period 2, Group 1",
      "Period 3, Group 2"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Given the electronic configuration \\(2, 8, 1\\):
1. **Determining Period**:
   - The electrons occupy 3 concentric shells: K (2), L (8), M (1).
   - Total number of occupied shells = \\(3\\).
   - Therefore, the element belongs to **Period 3**.
2. **Determining Group**:
   - The outermost (M) shell contains \\(1\\) valence electron.
   - For s-block elements, Group number = Number of valence electrons = \\(1\\).
   - Therefore, the element belongs to **Group 1** (Alkali metals).
3. **Identity**: Total electrons = \\(2 + 8 + 1 = 11\\), corresponding to **Sodium (Na)**.

### 2. Physical Context & Practical Illustration:
Sodium sits in Period 3 (third row) and Group 1 (first column) of the periodic table, right below Lithium and above Potassium.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Configuration \\(2, 8, 1\\) belongs to Period 3, Group 1.
- **Option B is incorrect**: Transposes period and group numbers.
- **Option C is incorrect**: Period 2 has only 2 shells (Lithium: 2, 1).
- **Option D is incorrect**: Group 2 has 2 valence electrons (Magnesium: 2, 8, 2).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-032",
    text: "Which principal electronic shell serves as the outermost valence shell for elements belonging to Period 2 of the periodic table?",
    options: [
      "K shell (n = 1)",
      "L shell (n = 2)",
      "M shell (n = 3)",
      "N shell (n = 4)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In atomic structure, principal electronic shells are designated by quantum numbers:
- \\(n = 1 \\implies \\text{K shell}\\) (filled in Period 1: H to He)
- \\(n = 2 \\implies \\text{L shell}\\) (filled in Period 2: Li to Ne)
- \\(n = 3 \\implies \\text{M shell}\\) (filled in Period 3: Na to Ar)
- \\(n = 4 \\implies \\text{N shell}\\) (filled in Period 4)
For all elements in Period 2, electrons are added to the \\(2s\\) and \\(2p\\) orbitals of the **L shell (\\(n = 2\\))**, which is their outermost valence shell.

### 2. Physical Context & Practical Illustration:
From Lithium (configuration 2, 1) to Neon (configuration 2, 8), the inner K shell remains filled with 2 core electrons, while the outer L shell fills progressively with 1 to 8 electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: K shell is outermost for Period 1 elements (H and He).
- **Option B is correct**: L shell (\\(n = 2\\)) is the outermost shell for Period 2 elements.
- **Option C is incorrect**: M shell is outermost for Period 3 elements.
- **Option D is incorrect**: N shell is outermost for Period 4 elements.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-033",
    text: "Five elements A, B, C, D, and E have atomic numbers 9, 11, 17, 19, and 20, respectively. Which two elements belong to the SAME chemical group?",
    options: [
      "Elements A (9) and B (11)",
      "Elements B (11) and C (17)",
      "Elements A (9) and C (17)",
      "Elements D (19) and E (20)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Elements belong to the same group if they possess the identical number of valence electrons:
- **Element A (\\(Z = 9\\), Fluorine)**: \\(2, 7 \\implies \\mathbf{7\\text{ valence electrons}}\\).
- **Element B (\\(Z = 11\\), Sodium)**: \\(2, 8, 1 \\implies 1\\text{ valence electron}\\).
- **Element C (\\(Z = 17\\), Chlorine)**: \\(2, 8, 7 \\implies \\mathbf{7\\text{ valence electrons}}\\).
- **Element D (\\(Z = 19\\), Potassium)**: \\(2, 8, 8, 1 \\implies 1\\text{ valence electron}\\).
- **Element E (\\(Z = 20\\), Calcium)**: \\(2, 8, 8, 2 \\implies 2\\text{ valence electrons}\\).

Comparing valence electrons:
- **Element A (9)** and **Element C (17)** both have **7 valence electrons**; they both belong to **Group 17 (the Halogens)**.
(Note: B and D also belong to Group 1, but A and C are the matching pair in the options).

### 2. Physical Context & Practical Illustration:
Fluorine (A) and Chlorine (C) are classic halogen non-metals that form diatomic gases (\\(\\text{F}_2, \\text{Cl}_2\\)) and salt anions (\\(\\text{F}^-, \\text{Cl}^-\\)) with nearly identical chemical behavior.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A has 7 valence electrons, while B has 1.
- **Option B is incorrect**: B has 1 valence electron, while C has 7.
- **Option C is correct**: Both A (Fluorine) and C (Chlorine) possess 7 valence electrons and belong to Group 17.
- **Option D is incorrect**: D belongs to Group 1, while E belongs to Group 2.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-034",
    text: "An element has the ground-state electronic configuration 2, 8, 7. What is the fundamental chemical nature of this element?",
    options: [
      "Metalloid",
      "Highly reactive metal",
      "Non-metal (Halogen)",
      "Inert semiconductor"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The electronic configuration is \\(2, 8, 7\\) (total electrons = \\(17\\), Chlorine, Cl):
- It has \\(7\\) valence electrons in its outermost shell.
- Elements with 5, 6, or 7 valence electrons have high electronegativities and high effective nuclear charges; they tend to gain electrons rather than donate them:
\\[
\\text{Cl} + e^- \\longrightarrow \\text{Cl}^- \\quad (\\Delta H_{\\text{eg}} = -349\\text{ kJ/mol})
\\]
An element that readily gains electrons to form negative anions is fundamentally a **non-metal**.

### 2. Physical Context & Practical Illustration:
Chlorine is a yellowish-green, pungent, choking gas at room temperature that does not conduct electricity and forms acidic oxides, exemplifying non-metallic character.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Metalloids typically have 3 to 5 valence electrons and intermediate electronegativities (e.g. Si: 2, 8, 4).
- **Option B is incorrect**: Metals have 1, 2, or 3 valence electrons and lose electrons easily.
- **Option C is correct**: With 7 valence electrons, it is an electronegative non-metal.
- **Option D is incorrect**: Chlorine is a non-conductive halogen gas, not a semiconductor.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-035",
    text: "Which of the following electronic configurations represents an element that is chemically MOST metallic and electropositive in character?",
    options: [
      "\\(2, 8, 7\\)",
      "\\(2, 8, 8, 1\\)",
      "\\(2, 8, 4\\)",
      "\\(2, 8, 2\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Metallic character (electropositivity) measures the ease with which an atom donates its outermost valence electrons to form positive cations:
- **Trend**: Metallic character increases with larger atomic radius (more shells) and fewer valence electrons (lower ionization energy):
1. **\\(2, 8, 7\\) (Chlorine)**: Non-metal with 7 valence electrons (gains electrons).
2. **\\(2, 8, 4\\) (Silicon)**: Metalloid with intermediate bonding.
3. **\\(2, 8, 2\\) (Magnesium)**: Metal with 3 shells and 2 valence electrons.
4. **\\(2, 8, 8, 1\\) (Potassium)**: Alkali metal with **4 electron shells** and only **1 valence electron**:
\\[
r_{\\text{K}} \\approx 227\\text{ pm}, \\quad \\text{IE}_1 = 419\\text{ kJ/mol (extremely low)}
\\]
Its single valence electron is far from the nucleus and shielded by three inner shells, making Potassium the most easily ionized and most metallic element among the options.

### 2. Physical Context & Practical Illustration:
Potassium reacts explosively with cold water, instantly igniting the evolved hydrogen with a characteristic lilac flame, demonstrating superior electropositive metallic reactivity compared to magnesium.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Chlorine is a non-metal.
- **Option B is correct**: Configuration \\(2, 8, 8, 1\\) (Potassium) has the largest radius and lowest ionization energy, making it the most metallic.
- **Option C is incorrect**: Silicon is a metalloid.
- **Option D is incorrect**: Magnesium has higher ionization energy than potassium.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-036",
    text: "In Mendeleev's Periodic Table, chemical elements were primarily arranged in the increasing order of their:",
    options: [
      "Atomic numbers",
      "Number of electrons in the valence shell",
      "Atomic masses",
      "Densities in the solid state"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Dmitri Mendeleev published his foundational periodic table in 1869 based on **atomic masses**:
\\[
\\text{Element Sequence: } H (1) \\longrightarrow Li (7) \\longrightarrow Be (9.4) \\longrightarrow B (11) \\dots
\\]
He noted that chemical similarities in valence hydrides and oxides recurred cyclically when elements were ordered by atomic mass.
(Arrangement by atomic number was only introduced 44 years later by Henry Moseley in 1913).

### 2. Physical Context & Practical Illustration:
Mendeleev's genius lay in prioritizing chemical properties over rigid atomic mass ordering: when the measured mass of Tellurium seemed heavier than Iodine, he correctly placed Tellurium before Iodine based on their chemical families, anticipating that atomic mass measurements would eventually be refined.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Atomic number was used later in the Modern Periodic Table.
- **Option B is incorrect**: Electron configurations were unknown in 1869 (the electron was discovered in 1897).
- **Option C is correct**: Mendeleev arranged elements in order of increasing atomic masses.
- **Option D is incorrect**: Density varies non-periodically.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-037",
    text: "Which of the following statements regarding the Modern Periodic Table is INCORRECT?",
    options: [
      "Elements in the same vertical group possess identical numbers of valence electrons",
      "Elements in the same horizontal period possess the same number of occupied electron shells",
      "The Modern Periodic Table is based strictly on the increasing order of elemental atomic masses",
      "Metals are located on the left and center, while non-metals reside in the upper right"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing each statement:
- **Statement A is true**: Groups are defined by shared valence electronic configurations.
- **Statement B is true**: Periods are defined by the principal quantum shell count (\\(n\\)).
- **Statement C is FALSE (the correct answer)**: The Modern Periodic Table is based strictly on increasing **atomic numbers (\\(Z\\))**, NOT atomic masses!
- **Statement D is true**: Metals occupy the s, d, and f blocks on the left, center, and bottom, while non-metals reside in the p-block on the upper right.

### 2. Physical Context & Practical Illustration:
The shift from atomic mass to atomic number by Moseley in 1913 is the defining milestone that separates the classical periodic table from the Modern Periodic Table.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a true statement**.
- **Option B is a true statement**.
- **Option C is incorrect (the correct answer to the question)**: Asserting the modern table is based on atomic mass is factually false; it is based on atomic number.
- **Option D is a true statement**.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-038",
    text: "The physical discovery that atomic number (Z), rather than atomic mass, is the true fundamental property determining chemical periodicity was established by:",
    options: [
      "Dmitri Mendeleev",
      "John Newlands",
      "Johann Döbereiner",
      "Henry Moseley"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, English physicist **Henry Moseley** used X-ray spectroscopy to establish:
\\[
\\sqrt{\\nu} = a(Z - b)
\\]
where \\(\\nu\\) is the frequency of characteristic X-rays emitted by an elemental anode and \\(Z\\) is its atomic number (positive nuclear charge).
This proved experimentally that the chemical properties of an element depend directly on its atomic number (number of nuclear protons / orbiting electrons), establishing the foundation of the Modern Periodic Table.

### 2. Physical Context & Practical Illustration:
Moseley's work provided an empirical physical measurement of atomic number for the first time, resolving anomalous element pairs and correctly predicting the exact number of undiscovered elements between aluminum and gold.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Mendeleev used atomic mass in 1869.
- **Option B is incorrect**: Newlands used atomic mass in his law of octaves.
- **Option C is incorrect**: Döbereiner used atomic mass in his triads.
- **Option D is correct**: Henry Moseley discovered the atomic number basis of the periodic table in 1913.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-039",
    text: "Which of the following statements does NOT explain why chemical elements belonging to the same vertical group exhibit similar chemical properties?",
    options: [
      "They have the exact same number of valence electrons in their outermost shell",
      "They have the exact same total number of core electronic shells",
      "They form chemical bonds by gaining, losing, or sharing the same number of electrons",
      "They exhibit identical valency in forming hydrides and oxides"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Elements in the same vertical group share similar chemical behavior because:
1. They possess identical numbers of **valence electrons** in their outermost shell (e.g. Group 1 has \\(ns^1\\), Group 17 has \\(ns^2 np^5\\)).
2. They undergo identical types of chemical bonding (same valency) to achieve octet stability.
However, **they do NOT have the same total number of electron shells**:
- In Group 1, Lithium has 2 shells, Sodium has 3 shells, Potassium has 4 shells, and Cesium has 6 shells.
The total number of shells increases down the group and is identical across a *period*, not a group!

### 2. Physical Context & Practical Illustration:
Chemical reactions occur at the atomic perimeter where valence electrons interact. The inner filled shells are chemically inert cores that do not dictate basic bonding stoichiometry.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a valid explanation**: Equal valence electrons cause similar bonding.
- **Option B is false (the correct answer to the question)**: Elements in a group have *different* numbers of electronic shells, increasing down the group.
- **Option C is a valid explanation**: Equal electron exchange rates produce identical valencies.
- **Option D is a valid explanation**: Identical valencies yield identical chemical formulas.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-040",
    text: "\"The physical and chemical properties of elements are periodic functions of their atomic numbers.\" This principle is the exact statement of:",
    options: [
      "Döbereiner's Law of Triads",
      "Mendeleev's Periodic Law",
      "The Modern Periodic Law",
      "Newlands' Law of Octaves"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
This is the formal definition of the **Modern Periodic Law**, enunciated by Henry Moseley in 1913.
- When elements are arranged in order of increasing **atomic number (\\(Z\\))**, elements with identical valence electron configurations recur at regular intervals (periods of 2, 8, 8, 18, 18, 32 elements).
- Because atomic number determines electron configuration, and electron configuration determines chemical behavior, periodicity is an intrinsic consequence of atomic number.

### 2. Physical Context & Practical Illustration:
This law replaced Mendeleev's earlier 1869 law (which erroneously used atomic mass), eliminating all historical anomalies in the periodic table.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Döbereiner's Law of Triads (1829).
- **Option B is incorrect**: Mendeleev's Periodic Law (1869) was based on atomic mass.
- **Option C is correct**: The Modern Periodic Law is based on atomic number.
- **Option D is incorrect**: Newlands' Law of Octaves (1864).`
  }
];

module.exports = { ch4_part4 };
