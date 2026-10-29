// scripts/ch4_part6.js - Chapter 4 (Measurement of Matter / Topic 4.2) Questions 81-120 Gold Standard Enhancements
const ch4_part6 = [
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-081",
    text: "The modern long form of the periodic table arranges chemical elements strictly in the increasing order of their:",
    options: [
      "Isotopic mass numbers",
      "Atomic numbers (Z)",
      "Bulk physical densities",
      "Atomic radii"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The Modern Periodic Table is constructed on the foundation of the **Modern Periodic Law** (Moseley, 1913):
\\[
\\text{Properties of elements are a periodic function of their atomic numbers } (Z)
\\]
Atomic number represents the total number of positive protons in the atomic nucleus, which equals the total number of electrons in a neutral atom:
- As \\(Z\\) increases sequentially by \\(1\\) from Hydrogen (\\(Z=1\\)) to Oganesson (\\(Z=118\\)), electrons occupy quantized shells according to the Aufbau principle.
- Elements with identical outer valence shell electron arrangements recur at regular, predictable intervals (periods of 2, 8, 8, 18, 18, 32 elements).

### 2. Physical Context & Practical Illustration:
Arrangement by atomic number automatically resolves earlier contradictions in Mendeleev's mass-based table, such as why Tellurium (\\(Z=52\\)) must precede Iodine (\\(Z=53\\)), and why isotopes of the same element share one single periodic slot.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Mass numbers vary across isotopes of the same element.
- **Option B is correct**: Elements are ordered by increasing atomic number.
- **Option C is incorrect**: Density does not exhibit regular monotonic progression.
- **Option D is incorrect**: Atomic radius decreases across periods and increases down groups.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-082",
    text: "\"The physical and chemical properties of chemical elements are a periodic function of their atomic numbers.\" This landmark scientific statement is known as:",
    options: [
      "Mendeleev's Periodic Law",
      "Newlands' Law of Octaves",
      "Döbereiner's Law of Triads",
      "The Modern Periodic Law"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
This is the foundational definition of the **Modern Periodic Law**, enunciated by Henry Moseley in 1913:
- In contrast to Mendeleev's earlier 1869 law (which stated that properties are periodic functions of *atomic masses*), Moseley proved through characteristic X-ray spectroscopy (\\(\\sqrt{\\nu} = a(Z - b)\\)) that the nuclear charge (atomic number, \\(Z\\)) is the true fundamental property governing elemental identity and periodicity.

### 2. Physical Context & Practical Illustration:
Because chemical reactivity is dictated by valence electron interactions, and electron count in neutral atoms is strictly equal to the atomic number \\(Z\\), chemical periodicity is a direct mathematical consequence of atomic number.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Mendeleev's law is based on atomic mass.
- **Option B is incorrect**: Newlands' law of octaves was based on atomic mass.
- **Option C is incorrect**: Döbereiner's triads were based on atomic mass.
- **Option D is correct**: The Modern Periodic Law is based on atomic number.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-083",
    text: "How many concentric electronic shells are occupied by electrons in atoms of elements belonging to Period 3 of the periodic table?",
    options: [
      "\\(1\\text{ shell}\\)",
      "\\(2\\text{ shells}\\)",
      "\\(3\\text{ shells (K, L, and M shells)}\\)",
      "\\(4\\text{ shells}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the periodic table, the period number (\\(n\\)) is identically equal to the principal quantum number of the outermost valence shell, which corresponds to the **total number of occupied electron shells**:
- Period 1: 1 shell (K shell)
- Period 2: 2 shells (K, L shells)
- **Period 3**: **3 shells (K, L, and M shells)**
For all elements in Period 3 (from Sodium, \\(2, 8, 1\\), to Argon, \\(2, 8, 8\\)), electrons occupy the K, L, and M shells.

### 2. Physical Context & Practical Illustration:
Across Period 3, the inner K (2 electrons) and L (8 electrons) shells form a stable, complete core. Successive elements add electrons exclusively into the third (M) shell until it reaches an octet at Argon.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Period 1 elements have 1 shell.
- **Option B is incorrect**: Period 2 elements have 2 shells.
- **Option C is correct**: All Period 3 elements possess 3 occupied electron shells.
- **Option D is incorrect**: Period 4 elements have 4 shells.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-084",
    text: "Potassium (atomic number Z = 19) belongs to which family of chemical elements in the modern periodic table?",
    options: [
      "Alkali metals (Group 1)",
      "Alkaline earth metals (Group 2)",
      "Halogens (Group 17)",
      "Noble gases (Group 18)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Potassium (\\(Z = 19\\)) has the ground-state electronic configuration:
\\[
\\text{K}: 2, 8, 8, 1
\\]
- It has \\(1\\) valence electron in its outermost N-shell (\\(4s^1\\)).
- Elements with a single valence s-electron belong to **Group 1**, universally known as the **Alkali Metals** (Li, Na, K, Rb, Cs, Fr).
- Potassium readily loses this single electron to form a monovalent cation: \\(\\text{K} \\to \\text{K}^+ + e^-\\).

### 2. Physical Context & Practical Illustration:
Potassium is a soft, silvery-white metal that reacts violently and exothermically with water to form potassium hydroxide (KOH, a strong alkali) and hydrogen gas, which ignites with a characteristic lilac-colored flame.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Potassium belongs to Group 1, the alkali metals.
- **Option B is incorrect**: Alkaline earth metals belong to Group 2 (e.g. Calcium, \\(Z=20\\)).
- **Option C is incorrect**: Halogens belong to Group 17.
- **Option D is incorrect**: Noble gases belong to Group 18.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-085",
    text: "Among five elements A (Z = 3), B (Z = 11), C (Z = 12), D (Z = 19), and E (Z = 20), which three elements belong to the SAME chemical group?",
    options: [
      "Elements A (3), C (12), and E (20)",
      "Elements A (3), B (11), and D (19)",
      "Elements B (11), C (12), and D (19)",
      "Elements C (12), D (19), and E (20)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
We determine the electronic configurations and valence electrons:
- **Element A (\\(Z = 3\\), Lithium)**: \\(2, 1 \\implies \\mathbf{1\\text{ valence electron}}\\) (Group 1)
- **Element B (\\(Z = 11\\), Sodium)**: \\(2, 8, 1 \\implies \\mathbf{1\\text{ valence electron}}\\) (Group 1)
- **Element C (\\(Z = 12\\), Magnesium)**: \\(2, 8, 2 \\implies 2\\text{ valence electrons}\\) (Group 2)
- **Element D (\\(Z = 19\\), Potassium)**: \\(2, 8, 8, 1 \\implies \\mathbf{1\\text{ valence electron}}\\) (Group 1)
- **Element E (\\(Z = 20\\), Calcium)**: \\(2, 8, 8, 2 \\implies 2\\text{ valence electrons}\\) (Group 2)

Comparing valence electrons:
**Elements A (Lithium), B (Sodium), and D (Potassium)** all possess exactly **1 valence electron** in their outermost shell; hence, all three belong to **Group 1 (Alkali Metals)**.

### 2. Physical Context & Practical Illustration:
Lithium, Sodium, and Potassium form a classic homologous family of soft, highly reactive light metals that show a smooth gradation in physical properties down Group 1.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A has 1 valence electron, while C and E have 2.
- **Option B is correct**: Elements A (3), B (11), and D (19) all belong to Group 1.
- **Option C is incorrect**: C has 2 valence electrons, unlike B and D.
- **Option D is incorrect**: D belongs to Group 1, while C and E belong to Group 2.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-086",
    text: "In the modern periodic table, the main-group elements belonging to Groups 1, 2, and 13 to 17 are collectively designated as:",
    options: [
      "Noble gases",
      "Representative (Normal) elements",
      "Transition elements",
      "Inner transition elements"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The periodic table is classified into four blocks based on subshell filling:
1. **Representative (Normal) Elements**: Comprise the **s-block (Groups 1 and 2)** and **p-block (Groups 13 to 17)**. In these elements, all inner shells are completely filled, and only the single outermost valence shell (\\(n\\)) is incomplete.
2. **Noble Gases (Group 18)**: Outermost shell is completely filled (\\(ns^2 np^6\\)).
3. **Transition Elements (Groups 3 to 12)**: d-block elements with two incomplete outermost shells.
4. **Inner Transition Elements**: f-block elements with three incomplete outermost shells.

### 2. Physical Context & Practical Illustration:
Representative elements include the most familiar chemical elements of our daily life: alkali metals, alkaline earths, carbon, nitrogen, oxygen, and halogens.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Noble gases are strictly Group 18.
- **Option B is correct**: Groups 1, 2, and 13 to 17 are called representative or normal elements.
- **Option C is incorrect**: Transition elements are Groups 3 to 12.
- **Option D is incorrect**: Inner transition elements are the f-block series.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-087",
    text: "By which industrial metallurgical process is pure aluminum metal extracted from its purified oxide (alumina, \\(\\text{Al}_2\\text{O}_3\\))?",
    options: [
      "Carbon coke reduction in a blast furnace",
      "Thermite aluminothermic reduction",
      "Roasting with limestone flux",
      "Electrolytic reduction of molten alumina dissolved in cryolite (Hall-Héroult process)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Aluminum is a highly electropositive metal with strong affinity for oxygen. Its oxide (\\(\\text{Al}_2\\text{O}_3\\)) cannot be reduced by carbon coke:
- In the **Hall-Héroult process**, purified alumina is dissolved in molten cryolite (\\(\\text{Na}_3\\text{AlF}_6\\)) and fluorspar (\\(\\text{CaF}_2\\)) at \\(\\approx 950^\circ\\text{C}\\).
- Cryolite acts as a solvent that lowers the melting point from \\(2050^\circ\\text{C}\\) to \\(950^\circ\\text{C}\\) and imparts electrical conductivity.
- Electric current reduces \\(\\text{Al}^{3+}\\) at the carbon cathode:
\\[
\\text{Al}^{3+} + 3e^- \\longrightarrow \\mathbf{\\text{Al}_{(l)}}
\\]
Molten aluminum is collected at the bottom of the cell.

### 2. Physical Context & Practical Illustration:
Before Charles Martin Hall and Paul Héroult independently invented this electrolytic process in 1886, aluminum was rarer and more expensive than silver or gold.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Carbon reduction of alumina is thermodynamically infeasible at blast furnace temperatures.
- **Option B is incorrect**: Thermite reaction uses aluminum to reduce other metal oxides (like \\(\\text{Fe}_2\\text{O}_3\\)), not to extract aluminum!
- **Option C is incorrect**: Roasting applies to sulfide ores.
- **Option D is correct**: Aluminum is extracted via electrolytic reduction in molten cryolite.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-088",
    text: "Although Iron Pyrite (\\(\\text{FeS}_2\\), 'fool's gold') contains over 46% iron by mass, why is it NOT commercially used as an iron ore for smelting iron in a blast furnace?",
    options: [
      "Because it contains no iron atoms in its chemical formula",
      "Because it is an imaginary synthetic mineral not found in the Earth's crust",
      "Because it decomposes into toxic mercury vapor upon heating",
      "Because roasting its high sulfur content releases massive SO₂ pollution and residual sulfur makes the resulting iron brittle and unworkable"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An **ore** is a mineral from which a metal can be extracted **profitably, easily, and cleanly**:
- Iron Pyrite (\\(\\text{FeS}_2\\)) contains \\(46.6\\%\\) Iron and \\(53.4\\%\\) Sulfur.
- **Why it is rejected for iron smelting**:
  1. Smelting \\(\\text{FeS}_2\\) produces huge quantities of corrosive, toxic sulfur dioxide (\\(\\text{SO}_2\\)) gas:
\\[
4\\text{FeS}_2 + 11\\text{O}_2 \\longrightarrow 2\\text{Fe}_2\\text{O}_3 + 8\\text{SO}_2 \\uparrow
\\]
  2. Even tiny residual traces of sulfur (\\(> 0.05\\%\\)) in pig iron form low-melting ferrous sulfide (FeS) along grain boundaries, causing severe **'hot shortness'** (extreme brittleness at red heat that causes the steel to crack and shatter during forging).
Instead, oxide ores like **Hematite (\\(\\text{Fe}_2\\text{O}_3\\))** and **Magnetite (\\(\\text{Fe}_3\\text{O}_4\\))** are used because they contain no sulfur and yield high-purity iron directly with carbon.

### 2. Physical Context & Practical Illustration:
Pyrite was historically mined for manufacturing sulfuric acid (by burning the sulfur into \\(\\text{SO}_2\\)), but never for iron production. Hematite remains the premier commercial iron ore worldwide.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Pyrite contains \\(46.6\\%\\) iron by mass.
- **Option B is incorrect**: Pyrite is an abundant natural mineral.
- **Option C is incorrect**: Pyrite contains iron and sulfur, zero mercury.
- **Option D is correct**: High sulfur content causes severe pollution and renders the iron brittle and useless.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-089",
    text: "What is the general chemical acid-base nature of non-metallic oxides (such as \\(\\text{SO}_2\\), \\(\\text{CO}_2\\), and \\(\\text{P}_2\\text{O}_5\\))?",
    options: [
      "Basic in nature",
      "Acidic in nature (forming acids when dissolved in water)",
      "Strongly alkaline",
      "Metallic in nature"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Non-metals are electronegative elements. When they combine with oxygen, they form covalent oxides:
- When non-metallic oxides dissolve in water, they hydrolyze to form oxoacids that release hydrogen ions (\\(\\text{H}^+\\)):
\\[
\\text{SO}_{2(g)} + \\text{H}_2\\text{O}_{(l)} \\longrightarrow \\text{H}_2\\text{SO}_{3(aq)} \\text{ (Sulfurous acid)}
\\]
\\[
\\text{CO}_{2(g)} + \\text{H}_2\\text{O}_{(l)} \\longrightarrow \\text{H}_2\\text{CO}_{3(aq)} \\text{ (Carbonic acid)}
\\]
\\[
\\text{P}_4\\text{O}_{10(s)} + 6\\text{H}_2\\text{O}_{(l)} \\longrightarrow 4\\text{H}_3\\text{PO}_{4(aq)} \\text{ (Phosphoric acid)}
\\]
- Insoluble non-metallic oxides react with basic metal oxides or hydroxides to form salts and water.
Therefore, non-metallic oxides are **acidic in nature**, turning blue litmus paper red.

### 2. Physical Context & Practical Illustration:
Dissolving carbon dioxide gas in water under pressure creates fizzy soda water with a tangy, mildly acidic taste due to the formation of carbonic acid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Metallic oxides are basic.
- **Option B is correct**: Non-metallic oxides are acidic in nature.
- **Option C is incorrect**: Alkaline implies water-soluble basic hydroxides.
- **Option D is incorrect**: Non-metal oxides are covalent, not metallic.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-090",
    text: "Which of the following metals does NOT react with cold water or boiling hot water, but reacts only with superheated steam at red heat to produce metal oxide and hydrogen gas?",
    options: [
      "Potassium (K)",
      "Sodium (Na)",
      "Calcium (Ca)",
      "Iron (Fe)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the reactivity series:
- **Potassium & Sodium**: React vigorously and violently with **cold water** to form soluble hydroxides and hydrogen:
\\[
2\\text{K} + 2\\text{H}_2\\text{O} \\longrightarrow 2\\text{KOH} + \\text{H}_2
\\]
- **Calcium**: Reacts moderately with cold water to form \\(\\text{Ca(OH)}_2\\).
- **Magnesium**: Reacts very slowly with cold water, but rapidly with boiling hot water.
- **Iron (Fe)**: Displays **zero reaction** with cold water and zero reaction with boiling liquid water. It reacts exclusively when red-hot with **superheated steam** to form magnetic iron oxide (triferric tetroxide, \\(\\text{Fe}_3\\text{O}_4\\)) and hydrogen:
\\[
3\\text{Fe}_{(s)} + 4\\text{H}_2\\text{O}_{(g)} \\xrightarrow{\\Delta} \\mathbf{\\text{Fe}_3\\text{O}_{4(s)}} + 4\\text{H}_{2(g)}
\\]

### 2. Physical Context & Practical Illustration:
Iron pipes safely carry cold and hot household water for decades without chemically dissolving. However, passing high-pressure steam over red-hot iron in a furnace tube produces brisk streams of hydrogen gas.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Potassium reacts explosively with cold water.
- **Option B is incorrect**: Sodium reacts vigorously with cold water.
- **Option C is incorrect**: Calcium reacts steadily with cold water.
- **Option D is correct**: Iron does not react with cold or boiling water, reacting only with steam at high temperatures.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-091",
    text: "Which alloying element is primarily added to iron and carbon to impart corrosion resistance and a bright silvery-lustrous finish to stainless steel?",
    options: [
      "Copper",
      "Lead",
      "Chromium (with Nickel)",
      "Mercury"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Standard **Stainless Steel** is an iron alloy typically composed of:
- Iron (Fe): \\(\\approx 70\\% - 74\\%\\)
- **Chromium (Cr)**: **\\(\\approx 18\\%\\)**
- **Nickel (Ni)**: **\\(\\approx 8\\%\\)**
- Carbon (C): \\(< 0.1\\%\\)
(Commonly known as 18/8 stainless steel).
1. **Passivation Mechanism**: Chromium reacts spontaneously with atmospheric oxygen to form an invisible, self-healing, adherent nanoscale passive film of **Chromium(III) oxide (\\(\\text{Cr}_2\\text{O}_3\\))** across the entire surface.
2. This transparent oxide layer protects the underlying iron from water, acids, and rusting while reflecting light to give stainless steel its gleaming silvery-white appearance.

### 2. Physical Context & Practical Illustration:
Unlike ordinary iron which flakes away into brown rust (\\(\\text{Fe}_2\\text{O}_3 \\cdot x\\text{H}_2\\text{O}\\)), stainless steel cutlery, surgical scalpels, and kitchen sinks maintain their bright polished finish indefinitely because the chromium oxide layer instantly reforms if scratched.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Copper is added to brass/bronze, not stainless steel.
- **Option B is incorrect**: Lead is toxic and not used in stainless steel.
- **Option C is correct**: Chromium and Nickel provide stainless steel with its silvery luster and rust resistance.
- **Option D is incorrect**: Mercury forms liquid amalgams, not steel alloys.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-092",
    text: "Which of the following statements regarding the arrangement of the Modern Periodic Table is CORRECT?",
    options: [
      "It consists of 18 horizontal periods and 7 vertical groups",
      "It consists of 7 horizontal periods and 18 vertical groups",
      "Elements are arranged strictly by decreasing atomic number",
      "Non-metals are placed exclusively on the far left side"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The IUPAC Modern Long Form of the Periodic Table comprises:
- **7 Horizontal Rows**, termed **Periods** (numbered 1 to 7).
- **18 Vertical Columns**, termed **Groups** (numbered 1 to 18 from left to right).
Elements are systematically arranged in ascending order of their **atomic number (\\(Z\\))**, placing elements with similar valence electronic configurations into the same vertical group.

### 2. Physical Context & Practical Illustration:
The 7 periods reflect the sequential filling of the 7 principal electron shells (\\(n=1\\) to \\(n=7\\)). The 18 groups organize the s, d, and p blocks cleanly across the 2D plane.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Inverts the numbers (it is 7 periods and 18 groups).
- **Option B is correct**: The modern periodic table has 7 periods and 18 groups.
- **Option C is incorrect**: Arranged in *increasing* order of atomic number.
- **Option D is incorrect**: Non-metals are on the upper right side.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-093",
    text: "Which of the following atomic factors does NOT contribute to determining the metallic character (electropositivity) of an element?",
    options: [
      "The color of the laboratory balance used to weigh the element",
      "The magnitude of effective nuclear charge (Z_eff)",
      "The atomic radius (distance from nucleus to valence electrons)",
      "The total number of inner shielding electronic shells"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Metallic character is the chemical tendency of an atom to lose its valence electrons and form positive cations:
\\[
\\text{Metallic Character} \\propto \\frac{1}{\\text{Ionization Energy}}
\\]
Ionization energy is physically governed by three intrinsic atomic factors:
1. **Atomic Radius**: A larger radius means valence electrons are farther from the nucleus and more easily lost (increasing metallic character).
2. **Effective Nuclear Charge (\\(Z_{\\text{eff}}\\))**: Higher nuclear pull binds electrons tighter, reducing metallic character.
3. **Screening (Shielding) Effect**: Inner electron shells shield valence electrons from nuclear attraction, increasing metallic character.
The color of laboratory apparatus is an irrelevant external macroscopic human artifact that has zero connection to atomic physics!

### 2. Physical Context & Practical Illustration:
Cesium is the most metallic stable element because it combines the largest atomic radius with the greatest number of shielding inner shells, making its single valence electron exceptionally easy to detach.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct (the correct answer to the question)**: The color of weighing equipment has no influence on metallic character.
- **Option B is a valid factor**: Effective nuclear charge directly controls ionization energy.
- **Option C is a valid factor**: Atomic radius dictates electron proximity.
- **Option D is a valid factor**: Shielding shells directly weaken nuclear attraction.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-094",
    text: "For main-group representative elements belonging to Groups 1 and 2 of the modern periodic table, the number of valence electrons in the outermost shell is equal to:",
    options: [
      "The period number minus 1",
      "The group number (Group 1 has 1 electron, Group 2 has 2 electrons)",
      "The total atomic mass number",
      "The total number of neutrons in the nucleus"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the s-block of the modern periodic table:
- **Group 1 (Alkali Metals)**: All elements (Li, Na, K, Rb, Cs, Fr) possess the valence configuration \\(ns^1\\), containing **1 valence electron** in their outermost shell.
- **Group 2 (Alkaline Earth Metals)**: All elements (Be, Mg, Ca, Sr, Ba, Ra) possess the valence configuration \\(ns^2\\), containing **2 valence electrons** in their outermost shell.
Thus, for these elements, the number of valence electrons is **identically equal to their group number**.

### 2. Physical Context & Practical Illustration:
This 1:1 correspondence explains why all Group 1 metals form \\(+1\\) ions (\\(\\text{Li}^+, \\text{Na}^+, \\text{K}^+\\)) and why all Group 2 metals form \\(+2\\) ions (\\(\\text{Mg}^{2+}, \\text{Ca}^{2+}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Period number indicates total shell count, not valence electrons.
- **Option B is correct**: Number of valence electrons equals the group number for Groups 1 and 2.
- **Option C is incorrect**: Mass number represents nucleons (protons + neutrons).
- **Option D is incorrect**: Neutron count does not govern group placement.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-095",
    text: "Which of the following non-metallic elements exists in the liquid state under normal room temperature and pressure?",
    options: [
      "Chlorine",
      "Iodine",
      "Bromine",
      "Sulfur"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the entire periodic table, only two elements are liquids at \\(25^\circ\\text{C}\\) and \\(1\\text{ atm}\\):
- Liquid metal: Mercury (Hg)
- **Liquid non-metal**: **Bromine (\\(\\text{Br}_2\\))**
Bromine is a dark reddish-brown, volatile, heavy liquid (density \\(\\approx 3.1\\text{ g/cm}^3\\)) that evaporates readily into dense, suffocating reddish-brown fumes.

### 2. Physical Context & Practical Illustration:
Bromine molecules (\\(\\text{Br}_2\\)) have intermediate London dispersion forces: stronger than gaseous \\(\\text{F}_2\\) and \\(\\text{Cl}_2\\), but weaker than solid crystalline \\(\\text{I}_2\\), placing its melting point at \\(-7.2^\circ\\text{C}\\) and boiling point at \\(58.8^\circ\\text{C}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Chlorine is a gas.
- **Option B is incorrect**: Iodine is a solid.
- **Option C is correct**: Bromine is the only liquid non-metal at room temperature.
- **Option D is incorrect**: Sulfur is a yellow solid.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-096",
    text: "What is the electrochemical process of 'Anodizing' widely used in protecting aluminum articles?",
    options: [
      "Electroplating a protective layer of silver onto aluminum",
      "Coating molten zinc onto iron sheets (galvanizing)",
      "Electrolytically developing a thick, durable, corrosion-resistant protective oxide layer (Al₂O₃) on an aluminum article acting as the anode",
      "Coating a thin layer of tin onto steel cans"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Anodizing** is an electrolytic surface-finishing process used primarily for **Aluminum**:
1. **Electrolytic Setup**: The cleaned aluminum article is made the **anode** (positive electrode) in an electrolytic bath containing dilute sulfuric acid (\\(\\text{H}_2\\text{SO}_4\\)).
2. **Anodic Reaction**: Electric current liberates oxygen gas at the aluminum anode:
\\[
2\\text{Al}_{(s)} + 3\\text{O}^{2-} \\longrightarrow \\mathbf{\\text{Al}_2\\text{O}_{3(s)}} + 6e^-
\\]
3. The released nascent oxygen reacts instantly with the aluminum surface to form a dense, uniform, durable, non-porous layer of **aluminum oxide (\\(\\text{Al}_2\\text{O}_3\\))**.
4. This oxide layer seals the metal, conferring superior resistance to corrosion and wear, and its porous cellular surface can be dyed into vibrant permanent colors.

### 2. Physical Context & Practical Illustration:
Anodized aluminum is universally used for modern window and door frames, cookware (hard-anodized pressure cookers), smartphone metal casings, and aircraft skins.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Anodizing produces an oxide coating, not silver plating.
- **Option B is incorrect**: Coating zinc onto iron is galvanization.
- **Option C is correct**: Anodizing forms a thick, protective aluminum oxide layer electrolytically.
- **Option D is incorrect**: Coating tin onto steel is tinning.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-097",
    text: "Which of the following non-metallic oxides is completely NEUTRAL in nature, showing zero reaction with both acids and bases and having no effect on litmus paper?",
    options: [
      "Carbon dioxide (\\(\\text{CO}_2\\))",
      "Carbon monoxide (CO)",
      "Phosphorus pentoxide (\\(\\text{P}_2\\text{O}_5\\))",
      "Sulfur dioxide (\\(\\text{SO}_2\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
While most non-metallic oxides are acidic in nature (reacting with water to form oxoacids):
- A few non-metallic oxides in low oxidation states exhibit neither acidic nor basic properties and are classified as **Neutral Oxides**:
\\[
\\text{Neutral Oxides: } \\mathbf{\\text{CO}}, \\; \\text{NO}, \\; \\text{N}_2\\text{O}, \\; \\text{H}_2\\text{O}
\\]
- **Carbon Monoxide (CO)** does not react with water, does not react with acids, does not react with bases, and leaves both blue and red litmus paper completely unaffected.
In contrast, \\(\\text{CO}_2\\), \\(\\text{SO}_2\\), and \\(\\text{P}_2\\text{O}_5\\) are all strongly acidic oxides that form carbonic, sulfurous, and phosphoric acids, respectively.

### 2. Physical Context & Practical Illustration:
Carbon monoxide is a silent, toxic, odorless gas produced by incomplete combustion. Because it is neutral, it cannot be trapped or scrubbed by simple alkaline scrubbers like \\(\\text{CO}_2\\) or \\(\\text{SO}_2\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{CO}_2\\) forms carbonic acid (acidic).
- **Option B is correct**: Carbon monoxide (CO) is a neutral oxide.
- **Option C is incorrect**: \\(\\text{P}_2\\text{O}_5\\) forms phosphoric acid (strongly acidic).
- **Option D is incorrect**: \\(\\text{SO}_2\\) forms sulfurous acid (strongly acidic).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-098",
    text: "Which of the following statements regarding the physical and chemical properties of metals is CORRECT?",
    options: [
      "Metals have high densities, high melting points, and generally form basic oxides",
      "All metals are brittle solids that cannot conduct heat or electricity",
      "Metals have 5 to 7 valence electrons and readily accept electrons to form anions",
      "Metals form covalent acidic oxides that turn blue litmus paper red"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing the characteristic properties of metals:
1. **Physical Properties**: Metals possess metallic bonding, which gives them high tensile strength, high density, high melting points, malleability, ductility, and high thermal/electrical conductivity via free conduction electrons.
2. **Electronic Structure**: Metals typically possess 1, 2, or 3 valence electrons in their outermost shell, easily lost to form electropositive cations (\\(\\text{M}^{n+}\\)).
3. **Chemical Behavior**: Metals react with oxygen to form ionic **basic oxides** (e.g. \\(\\text{Na}_2\\text{O}, \\text{CaO}, \\text{MgO}\\)) that turn red litmus paper blue.
Thus, Statement A is completely accurate.

### 2. Physical Context & Practical Illustration:
From high-strength structural iron beams in skyscrapers to conductive copper electrical wiring, metallic bonding provides the unique combination of electrical conductivity, strength, and basic chemical reactivity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Metals have high densities, high melting points, and form basic oxides.
- **Option B is incorrect**: Metals are malleable and ductile, not brittle; and are excellent conductors.
- **Option C is incorrect**: Having 5 to 7 valence electrons characterizes non-metals.
- **Option D is incorrect**: Non-metals form covalent acidic oxides.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-099",
    text: "Chromium has an atomic number of 24 (Z = 24). To which block and group of the modern periodic table does it belong?",
    options: [
      "s-block, Group 2",
      "p-block, Group 14",
      "d-block, Group 6 (Transition metal)",
      "f-block, Group 3"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Chromium (\\(Z = 24\\)) has an anomalous ground-state electron configuration due to the extra stability of a half-filled d-subshell:
\\[
\\text{Cr}: [\\text{Ar}] \\; 3d^5 4s^1
\\]
1. **Determining Block**: The differentiating (last entered) electron enters a \\(d\\)-orbital (the \\(3d\\) subshell). Therefore, Chromium belongs to the **d-block** (transition elements).
2. **Determining Period**: The highest principal quantum shell is \\(n = 4\\) (the \\(4s\\) orbital); hence it resides in **Period 4**.
3. **Determining Group**: For d-block elements:
\\[
\\text{Group Number} = \\text{Number of } (n-1)d\\text{ electrons} + \\text{Number of } ns\\text{ electrons} = 5 + 1 = \\mathbf{6}
\\]
Therefore, Chromium belongs to **d-block, Group 6**.

### 2. Physical Context & Practical Illustration:
Chromium is a hard, lustrous transition metal famous for electroplating car bumpers and alloying stainless steel to prevent rust.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Group 2 is alkaline earths (Calcium, \\(Z=20\\)).
- **Option B is incorrect**: Group 14 is Carbon group.
- **Option C is correct**: Chromium is a d-block transition metal in Group 6.
- **Option D is incorrect**: f-block contains inner transition elements.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-100",
    text: "In the modern periodic table, under which specific block are virtually all the non-metallic elements grouped?",
    options: [
      "s-block",
      "p-block",
      "d-block",
      "f-block"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the Modern Periodic Table:
1. **s-block**: Composed entirely of reactive metals (Groups 1 and 2), with Hydrogen being the sole non-metal anomaly.
2. **d-block**: Composed entirely of transition metals (Groups 3 to 12).
3. **f-block**: Composed entirely of inner transition metals (Lanthanoids and Actinoids).
4. **p-block (Groups 13 to 18)**: The ONLY block in the entire periodic table that houses all three classes of elements: metals, metalloids, and **all of the non-metals** (such as Carbon, Nitrogen, Oxygen, Fluorine, Phosphorus, Sulfur, Chlorine, Bromine, Iodine, and all the noble gases).

### 2. Physical Context & Practical Illustration:
The p-block displays the greatest chemical diversity in chemistry: ranging from pure metals (aluminum, lead) and semi-conducting metalloids (silicon, germanium) to atmospheric gases and oxidizing halogens.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: s-block contains metals (except hydrogen).
- **Option B is correct**: All non-metals reside in the p-block.
- **Option C is incorrect**: d-block consists purely of transition metals.
- **Option D is incorrect**: f-block consists purely of metals.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-101",
    text: "Who made the earliest documented scientific attempt to classify chemical elements into groups of three elements based on atomic masses in 1829?",
    options: [
      "Johann Wolfgang Döbereiner",
      "John Newlands",
      "Dmitri Mendeleev",
      "Henry Moseley"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1829, German chemist **Johann Wolfgang Döbereiner** identified that certain chemically similar elements could be arranged in groups of three, which he termed **Triads**:
- **Döbereiner's Law of Triads**: In a triad of chemically similar elements arranged in ascending order of atomic mass, the atomic mass of the middle element was approximately equal to the arithmetic mean (average) of the atomic masses of the first and third elements:
\\[
A_{\\text{middle}} \\approx \\frac{A_1 + A_3}{2}
\\]
- Example: **Alkali Metal Triad (Li, Na, K)**:
  - Lithium (\\(A_1 = 7\\)), Potassium (\\(A_3 = 39\\))
\\[
A_{\\text{Na}} = \\frac{7 + 39}{2} = \\frac{46}{2} = 23\\text{ u (exact measured mass of Sodium!)}
\\]

### 2. Physical Context & Practical Illustration:
Other classic Döbereiner triads included the Halogen triad (Chlorine 35.5, Bromine 80, Iodine 127: \\((35.5 + 127)/2 = 81.25\\)) and the Alkaline Earth triad (Calcium, Strontium, Barium). This was the earliest historical clue that atomic mass is linked to chemical properties.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Döbereiner proposed the Law of Triads in 1829.
- **Option B is incorrect**: Newlands proposed Law of Octaves in 1864.
- **Option C is incorrect**: Mendeleev formulated the periodic table in 1869.
- **Option D is incorrect**: Moseley established atomic numbers in 1913.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-102",
    text: "In 1869, which German chemist independently developed a periodic classification by plotting the atomic volumes of elements against their atomic weights, demonstrating sharp periodic curves?",
    options: [
      "John Dalton",
      "Robert Boyle",
      "Antoine Lavoisier",
      "Julius Lothar Meyer"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1869, German chemist **Julius Lothar Meyer** calculated atomic volumes by dividing atomic weight by density:
\\[
V_{\\text{atomic}} = \\frac{\\text{Atomic Weight } M}{\\text{Density } \\rho}
\\]
When he plotted atomic volume against atomic weight:
1. The curve showed a striking series of repeating periodic peaks and troughs.
2. Strongly electropositive **alkali metals (Li, Na, K, Rb, Cs)** occupied the **peaks (maxima)** of the curve.
3. Alkaline earth metals (Be, Mg, Ca, Sr, Ba) occupied the descending slopes.
4. Halogens and noble non-metals occupied ascending slopes.
5. Transition metals occupied the broad troughs (minima).
This proved graphically that physical properties are periodic functions of atomic weights.

### 2. Physical Context & Practical Illustration:
Lothar Meyer's atomic volume curve provided graphic visual confirmation of periodicity alongside Mendeleev's chemical table published in the exact same year.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Dalton proposed atomic theory.
- **Option B is incorrect**: Boyle defined gas pressure-volume relationships.
- **Option C is incorrect**: Lavoisier formulated the conservation of mass.
- **Option D is correct**: Lothar Meyer plotted the atomic volume vs atomic weight periodic curve.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-103",
    text: "In 1862, French geologist Alexandre-Émile Béguyer de Chancourtois created an early three-dimensional geometric representation of element periodicity by arranging elements along a spiral cylinder known as the:",
    options: [
      "Atomic Spiral",
      "Cylindrical Prism",
      "Octave Wheel",
      "Telluric Helix (Vis Tellurique)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1862, French geologist **Alexandre-Émile Béguyer de Chancourtois** designed the **Telluric Helix (Vis Tellurique)**:
- He inscribed a spiral line around a vertical cylinder divided into 16 equal segments corresponding to the atomic weight of oxygen (16).
- He plotted the elements along the helical thread at heights proportional to their atomic weights.
- When unwound, chemically similar elements aligned along vertical lines parallel to the cylinder axis (e.g. Lithium, Sodium, Potassium).
This was the first historical geometric depiction of periodic recurrence.

### 2. Physical Context & Practical Illustration:
The term *telluric* was derived from *tellus* (the Latin name for Earth), honoring the element Tellurium which fell near the geometric center of his helix.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Non-standard descriptive term.
- **Option B is incorrect**: Non-standard term.
- **Option C is incorrect**: Conflates Newlands' octaves with geometric wheels.
- **Option D is correct**: De Chancourtois created the Telluric Helix.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-104",
    text: "In Period 6 of the modern periodic table, the series of 14 inner transition elements occupying the separate bottom row (from Cerium to Lutetium) is called the:",
    options: [
      "Alkali series",
      "Halogen series",
      "Actinoid series",
      "Lanthanoid (Lanthanide) series"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Period 6, following Lanthanum (\\(Z = 57\\)), electrons fill the inner \\(4f\\) subshell across 14 elements (from Cerium, \\(Z = 58\\), to Lutetium, \\(Z = 71\\)):
\\[
\\text{Electron filling: } 4f^1 \\longrightarrow 4f^{14}
\\]
This 14-element series is termed the **Lanthanoid (or Lanthanide) series**:
- They are located in Period 6, Group 3.
- To prevent the main body of the periodic table from becoming unmanageably wide, they are displayed as a separate horizontal row beneath the main table.

### 2. Physical Context & Practical Illustration:
Lanthanoids are also known as the rare earth elements. They possess very similar ionic radii due to 'lanthanoid contraction' and are essential for supermagnets, lasers, and petroleum cracking catalysts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Alkali metals are Group 1.
- **Option B is incorrect**: Halogens are Group 17.
- **Option C is incorrect**: Actinoids belong to Period 7 (Thorium to Lawrencium, filling \\(5f\\)).
- **Option D is correct**: Period 6 inner transition elements are the Lanthanoids.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-105",
    text: "Why is Hydrogen conventionally placed at the head of Group 1 (IA) in the modern periodic table?",
    options: [
      "Because it is a dense, shiny alkali metal that reacts with sulfur to form slag",
      "Because its ground-state electronic configuration is 1s¹, containing a single valence electron like alkali metals",
      "Because it is completely unreactive under all conditions like noble gases",
      "Because its atomic mass is 12 unified mass units"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Hydrogen (\\(Z = 1\\)) has the ground-state electronic configuration:
\\[
\\text{H}: 1s^1
\\]
- Like Group 1 alkali metals (Li: \\(2s^1\\), Na: \\(3s^1\\), K: \\(4s^1\\)), Hydrogen has **exactly one valence electron** in an s-orbital.
- It can lose its single electron to form a monovalent proton (cation \\(\\text{H}^+\\)), and forms binary compounds with oxygen (\\(\\text{H}_2\\text{O}\\)), halogens (\\(\\text{HCl}\\)), and sulfur (\\(\\text{H}_2\\text{S}\\)) with identical stoichiometry to alkali metals (\\(\\text{Na}_2\\text{O}, \\text{NaCl}, \\text{Na}_2\\text{S}\\)).
Therefore, based on valence electronic configuration, it is conventionally positioned atop Group 1.

### 2. Physical Context & Practical Illustration:
Hydrogen occupies a unique dual position: it resembles alkali metals by forming \\(\\text{H}^+\\), but also resembles halogens (Group 17) by needing 1 electron to complete its duplet shell and forming diatomic gas (\\(\\text{H}_2\\)) and hydride anions (\\(\\text{H}^-\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Hydrogen is a non-metallic gas, not a dense metal.
- **Option B is correct**: Hydrogen has a \\(1s^1\\) configuration with 1 valence electron, matching Group 1.
- **Option C is incorrect**: Hydrogen is combustible and chemically reactive.
- **Option D is incorrect**: Hydrogen's mass is \\(1\\text{ u}\\), not 12.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-106",
    text: "What is the correct sequence of chemical elements descending down Group 1 (Alkali Metals) of the modern periodic table?",
    options: [
      "\\(\\text{Na} \\to \\text{Li} \\to \\text{K} \\to \\text{Cs} \\to \\text{Rb}\\)",
      "\\(\\text{Li} \\to \\text{Na} \\to \\text{K} \\to \\text{Rb} \\to \\text{Cs} \\to \\text{Fr}\\)",
      "\\(\\text{K} \\to \\text{Na} \\to \\text{Li} \\to \\text{Rb} \\to \\text{Cs}\\)",
      "\\(\\text{Be} \\to \\text{Mg} \\to \\text{Ca} \\to \\text{Sr} \\to \\text{Ba}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Group 1, as the principal quantum number increases from \\(n=2\\) to \\(n=7\\), elements occur in the exact order of their atomic numbers:
1. **Lithium (Li)**: \\(Z = 3\\) (Period 2)
2. **Sodium (Na)**: \\(Z = 11\\) (Period 3)
3. **Potassium (K)**: \\(Z = 19\\) (Period 4)
4. **Rubidium (Rb)**: \\(Z = 37\\) (Period 5)
5. **Cesium (Cs)**: \\(Z = 55\\) (Period 6)
6. **Francium (Fr)**: \\(Z = 87\\) (Period 7)
The unambiguous sequence is **\\(\\text{Li} \\to \\text{Na} \\to \\text{K} \\to \\text{Rb} \\to \\text{Cs} \\to \\text{Fr}\\)**.

### 2. Physical Context & Practical Illustration:
Down this sequence, atomic radius increases, ionization energy drops, and reactivity with water increases dramatically—from Lithium's gentle fizzing to Cesium's violent shatter upon contact with water.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Transposes Lithium and Sodium, and Cesium and Rubidium.
- **Option B is correct**: The exact descending order of Group 1 is Li, Na, K, Rb, Cs, Fr.
- **Option C is incorrect**: Inverts the upper sequence.
- **Option D is incorrect**: Lists Group 2 (alkaline earth metals).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-107",
    text: "Which of the following statements regarding the physical and chemical properties of Alkali Metals (Group 1) is INCORRECT?",
    options: [
      "They are soft metals that can easily be cut with a common knife",
      "They have very low densities and low melting points compared to other metals",
      "They have completely filled outermost electronic shells and exhibit zero chemical valency",
      "They react vigorously with water to form strongly alkaline hydroxides and hydrogen gas"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing the verified properties of alkali metals (Li, Na, K, Rb, Cs):
- **Softness**: Weak metallic bonding with only 1 valence electron makes them extremely soft; sodium and potassium can easily be sliced with a butter knife. (Statement A is true)
- **Low Density**: Large atomic radii and body-centered cubic packing give them very low densities (Li, Na, K float on water) and low melting points (\\(\\text{Na} = 98^\circ\\text{C}\\)). (Statement B is true)
- **Reactivity with Water**: They react exothermically to form basic hydroxides (\\(2\\text{M} + 2\\text{H}_2\\text{O} \\to 2\\text{MOH} + \\text{H}_2\\)). (Statement D is true)
- **Valency**: They possess \\(1\\) valence electron (\\(ns^1\\)), NOT a completely filled shell! They have a valency of **\\(1\\)** and are among the most reactive elements in chemistry. Asserting they have completely filled shells with zero valency is **completely false** (that describes noble gases)!

### 2. Physical Context & Practical Illustration:
Alkali metals are stored under inert mineral oil or kerosene specifically because their incomplete valence shell makes them react instantly with atmospheric moisture and oxygen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is true**: Alkali metals are soft.
- **Option B is true**: Alkali metals have low density and low melting points.
- **Option C is false (the correct answer to the question)**: They have 1 valence electron and valency of 1, not zero.
- **Option D is true**: They react vigorously with water.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-108",
    text: "An element has an atomic number of 19 (Z = 19). Which of the following statements accurately characterizes this element?",
    options: [
      "A solid non-metal with a valency of 2",
      "A diatomic gas with a valency of 2",
      "A highly reactive alkali metal with a valency of 1 (Potassium)",
      "A tetravalent metalloid with semiconductor properties"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For an element with \\(Z = 19\\):
1. **Electronic Configuration**:
\\[
\\text{K}: 2, 8, 8, 1
\\]
2. **Classification**:
   - Outermost shell has \\(1\\) valence electron in the \\(4s\\) orbital.
   - It belongs to **Period 4, Group 1** (Alkali Metals).
   - Identity: **Potassium (K)**.
3. **Valency**: It readily loses its single valence electron to achieve argon-like stability (\\(2, 8, 8\\)):
\\[
\\text{K} \\longrightarrow \\text{K}^+ + e^- \\implies \\mathbf{\\text{Valency } = 1}
\\]
Potassium is a soft, highly reactive alkali metal with a valency of 1.

### 2. Physical Context & Practical Illustration:
Potassium ions (\\(\\text{K}^+\\)) are essential electrolytes in human biology, critical for generating nerve impulses, regulating heart rhythm, and maintaining cellular osmotic balance.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Potassium is a metal, not a non-metal; valency is 1, not 2.
- **Option B is incorrect**: It is a solid metal, not a gas.
- **Option C is correct**: It is Potassium (K), a highly reactive alkali metal with a valency of 1.
- **Option D is incorrect**: Tetravalent metalloids include Silicon and Germanium.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-109",
    text: "To attain a stable noble gas electronic octet in its outermost shell, an Aluminum atom (atomic number Z = 13) will:",
    options: [
      "Gain five electrons to form an Al⁵⁻ anion",
      "Share eight pairs of electrons covalently with neighboring atoms",
      "Lose its three outermost valence electrons to form an Al³⁺ cation",
      "Disintegrate its nucleus into carbon and helium"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A neutral Aluminum atom (\\(Z = 13\\)) has the ground-state electron configuration:
\\[
\\text{Al}: 2, 8, 3 \\quad (\\text{K}=2, \\text{L}=8, \\text{M}=3)
\\]
- The outermost M-shell contains \\(3\\) valence electrons.
- Thermodynamically, losing 3 valence electrons requires far less energy than attempting to gain 5 electrons against strong electrostatic repulsion:
\\[
\\text{Al} \\longrightarrow \\mathbf{\\text{Al}^{3+}} + 3e^-
\\]
The resulting aluminum cation (\\(\\text{Al}^{3+}\\)) achieves the completely filled, stable octet configuration of Neon (\\(2, 8\\)).

### 2. Physical Context & Practical Illustration:
This tendency to lose 3 electrons governs all of aluminum's chemical compounds: it forms \\(\\text{AlCl}_3\\) with chlorine and \\(\\text{Al}_2\\text{O}_3\\) with oxygen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Gaining 5 electrons is energetically impossible due to intense electron-electron repulsion.
- **Option B is incorrect**: Metals typically form ionic bonds by electron loss.
- **Option C is correct**: Aluminum loses its 3 valence electrons to form the stable octet \\(\\text{Al}^{3+}\\) cation.
- **Option D is incorrect**: Chemical bonding does not involve nuclear decay.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-110",
    text: "In which horizontal period of the modern periodic table do the transition elements (d-block elements) FIRST appear?",
    options: [
      "Period 1",
      "Period 2",
      "Period 3",
      "Period 4 (starting with Scandium, Z = 21)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Transition elements are defined by the progressive filling of inner \\((n-1)d\\) subshells:
- According to the Aufbau energy ordering principle:
\\[
1s < 2s < 2p < 3s < 3p < \\mathbf{4s < 3d} < 4p
\\]
- The \\(3d\\) subshell has higher energy than the \\(4s\\) subshell; therefore, after Potassium (\\(4s^1\\)) and Calcium (\\(4s^2\\)) in **Period 4**, electrons begin entering the \\(3d\\) subshell at **Scandium (\\(Z = 21\\))**.
- Periods 1, 2, and 3 contain only s and p block elements (no d-block elements).
Therefore, transition elements first appear in **Period 4**.

### 2. Physical Context & Practical Illustration:
Period 4 spans 18 elements: 2 s-block metals (K, Ca), 10 transition metals (Sc to Zn, filling the \\(3d\\) subshell), and 6 p-block elements (Ga to Kr).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Period 1 contains only 1s elements (H, He).
- **Option B is incorrect**: Period 2 contains 2s and 2p elements (Li to Ne).
- **Option C is incorrect**: Period 3 fills 3s and 3p; the 3d orbitals remain empty until Period 4.
- **Option D is correct**: Transition elements start in Period 4 with Scandium (\\(Z=21\\)).`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-111",
    text: "Which of the following elements readily LOSES three electrons to attain the stable electronic configuration of a noble gas?",
    options: [
      "Sodium (Na)",
      "Magnesium (Mg)",
      "Aluminum (Al)",
      "Silicon (Si)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Examining the valence electronic configurations:
- **Sodium (Na, \\(Z=11\\))**: \\(2, 8, 1 \\implies\\) loses **1 electron** to form \\(\\text{Na}^+\\).
- **Magnesium (Mg, \\(Z=12\\))**: \\(2, 8, 2 \\implies\\) loses **2 electrons** to form \\(\\text{Mg}^{2+}\\).
- **Aluminum (Al, \\(Z=13\\))**: \\(2, 8, 3 \\implies\\) loses **3 electrons** to attain the noble gas configuration of Neon (\\(2, 8\\)):
\\[
\\text{Al} \\longrightarrow \\mathbf{\\text{Al}^{3+}} + 3e^-
\\]
- **Silicon (Si, \\(Z=14\\))**: \\(2, 8, 4 \\implies\\) typically shares 4 electrons covalently.
Therefore, **Aluminum** loses 3 electrons.

### 2. Physical Context & Practical Illustration:
The loss of these 3 valence electrons gives aluminum its characteristic \\(+3\\) oxidation state in bauxite ore (\\(\\text{Al}_2\\text{O}_3\\)) and alum salts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Sodium loses only 1 electron.
- **Option B is incorrect**: Magnesium loses only 2 electrons.
- **Option C is correct**: Aluminum loses 3 electrons to form \\(\\text{Al}^{3+}\\).
- **Option D is incorrect**: Silicon shares 4 electrons.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-112",
    text: "Why does the noble gas Argon (atomic number Z = 18) NOT take part in chemical reactions under normal conditions?",
    options: [
      "Because its nucleus has too many protons that repel other atoms",
      "Because its outermost electronic valence shell is completely filled with a stable octet (2, 8, 8)",
      "Because it is a solid metal with very high melting point",
      "Because it has zero electrons in all its shells"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Argon (\\(Z = 18\\)) has the ground-state electron configuration:
\\[
\\text{Ar}: 2, 8, 8 \\quad (\\text{K}=2, \\text{L}=8, \\text{M}=8)
\\]
- Chemical reactivity is driven by the thermodynamic tendency of atoms to achieve a stable electronic octet.
- In Argon, the outermost M-shell already possesses **8 valence electrons (a complete octet)**:
\\[
\\text{Valence configuration} = 3s^2 3p^6
\\]
- It has an extremely high ionization enthalpy (difficult to remove electrons) and a positive electron gain enthalpy (cannot accept electrons).
Consequently, Argon is chemically inert and does not take part in chemical reactions.

### 2. Physical Context & Practical Illustration:
Because argon is completely non-reactive even at high temperatures, it is used as an inert shielding gas in tungsten arc welding (TIG welding) and to fill incandescent light bulbs to prevent the hot tungsten filament from oxidizing.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Protons are shielded inside the nucleus and do not repel neutral atoms.
- **Option B is correct**: Argon is chemically inert due to its completely filled stable octet (2, 8, 8).
- **Option C is incorrect**: Argon is a colorless, odorless gas.
- **Option D is incorrect**: Argon has 18 electrons.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-113",
    text: "How many chemical elements are contained in the 'short periods' (Periods 2 and 3) of the modern periodic table?",
    options: [
      "\\(8\\text{ elements each}\\)",
      "\\(2\\text{ elements each}\\)",
      "\\(18\\text{ elements each}\\)",
      "\\(32\\text{ elements each}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the Modern Periodic Table, periods are categorized by length based on orbital capacities:
- **Period 1**: Very Short Period = **2 elements** (H, He, filling \\(1s\\)).
- **Period 2**: Short Period = **8 elements** (Li to Ne, filling \\(2s, 2p\\)).
- **Period 3**: Short Period = **8 elements** (Na to Ar, filling \\(3s, 3p\\)).
- **Period 4 & 5**: Long Periods = **18 elements each** (filling \\(s, p,\\) and \\(d\\) orbitals).
- **Period 6 & 7**: Very Long Periods = **32 elements each** (filling \\(s, p, d,\\) and \\(f\\) orbitals).
Therefore, each short period contains exactly **\\(8\\text{ elements}\\)**.

### 2. Physical Context & Practical Illustration:
The 8-element length of Periods 2 and 3 corresponds to the 'rule of eight' (the octet rule) that underpins basic chemical bonding in main-group chemistry.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Short periods (Periods 2 and 3) contain 8 elements each.
- **Option B is incorrect**: 2 elements is the very short Period 1.
- **Option C is incorrect**: 18 elements is the long periods (Periods 4 and 5).
- **Option D is incorrect**: 32 elements is the very long periods.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-114",
    text: "At the termination (far right end) of every horizontal period in the modern periodic table, what type of chemical elements are situated?",
    options: [
      "Reactive alkali metals",
      "Amphoteric transition metals",
      "Corrosive halogens",
      "Chemically inert noble gases (Group 18)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Every period in the modern periodic table follows a consistent electronic progression:
1. It begins on the far left (Group 1) with an electropositive **alkali metal** having 1 valence electron (\\(ns^1\\)).
2. As one moves across the period, metallic character decreases and non-metallic character increases through halogens in Group 17 (\\(ns^2 np^5\\)).
3. Every period terminates at **Group 18** with a **noble gas (inert gas)** having a completely filled, saturated valence shell:
\\[
\\text{Period 1 terminates at Helium } (1s^2)
\\]
\\[
\\text{Periods 2 to 7 terminate at Ne, Ar, Kr, Xe, Rn, Og } (ns^2 np^6)
\\]
Therefore, **noble gases** are present at the end of every period.

### 2. Physical Context & Practical Illustration:
The noble gases represent points of maximum chemical stability and electronic closure, after which a brand-new quantum shell must open in the next period.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Alkali metals are at the *beginning* (far left) of periods.
- **Option B is incorrect**: Transition metals occupy the middle (Groups 3-12).
- **Option C is incorrect**: Halogens occupy Group 17, immediately preceding the end.
- **Option D is correct**: Noble gases (Group 18) terminate every period.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-115",
    text: "In the modern periodic table, the total number of occupied concentric electron shells in an atom is numerically equal to its:",
    options: [
      "Period number",
      "Group number",
      "Valency",
      "Number of valence electrons"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The electronic architecture of the periodic table links quantum numbers directly to table coordinates:
- The **Period Number (\\(n\\))** corresponds to the principal quantum number of the outermost shell, which equals the **total number of occupied electron shells**:
  - Period 1 elements have electrons in **1 shell** (K shell).
  - Period 2 elements have electrons in **2 shells** (K, L shells).
  - Period 3 elements have electrons in **3 shells** (K, L, M shells).
  - Period 4 elements have electrons in **4 shells** (K, L, M, N shells).
- In contrast, the *Group number* relates to the number of valence electrons.

### 2. Physical Context & Practical Illustration:
Potassium (\\(2, 8, 8, 1\\)) has electrons distributed across 4 shells (K, L, M, N); thus, it sits on the fourth horizontal row (Period 4).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The number of occupied shells equals the period number.
- **Option B is incorrect**: Group number reflects valence electrons.
- **Option C is incorrect**: Valency is combining capacity.
- **Option D is incorrect**: Valence electrons range from 1 to 8 across a period.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-116",
    text: "What common chemical family name is given to elements placed in Group 2 of the modern periodic table (Beryllium, Magnesium, Calcium, Strontium, Barium, Radium)?",
    options: [
      "Alkali metals",
      "Halogens",
      "Chalcogens",
      "Alkaline earth metals"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Group 2 elements (Be, Mg, Ca, Sr, Ba, Ra) are universally termed **Alkaline Earth Metals**:
1. **Electronic Configuration**: They have two valence electrons in their outermost s-subshell (\\(ns^2\\)).
2. **Origin of Name**:
   - Their oxides (e.g. \\(\\text{CaO}, \\text{MgO}\\)) react with water to form alkaline solutions (turn red litmus blue).
   - In alchemical terminology, mineral substances that resisted heat and were insoluble in water were called 'earths'. Because these basic metal oxides were found abundantly in the Earth's rocky crust, they were named **alkaline earths**.
3. They exhibit a uniform valency of **\\(2\\)** (divalent cations, \\(\\text{M}^{2+}\\)).

### 2. Physical Context & Practical Illustration:
Calcium and Magnesium are the two most abundant alkaline earth metals, forming major geological rock formations (limestone, \\(\\text{CaCO}_3\\); dolomite, \\(\\text{CaCO}_3 \\cdot \\text{MgCO}_3\\)) and playing essential biological roles in bones, teeth, and enzyme catalysis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Alkali metals are Group 1.
- **Option B is incorrect**: Halogens are Group 17.
- **Option C is incorrect**: Chalcogens are Group 16.
- **Option D is correct**: Group 2 elements are the alkaline earth metals.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-117",
    text: "How many total chemical elements are present in Period 2 of the modern periodic table?",
    options: [
      "\\(2\\text{ elements}\\)",
      "\\(8\\text{ elements}\\)",
      "\\(18\\text{ elements}\\)",
      "\\(32\\text{ elements}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Period 2, electrons fill the \\(2s\\) and \\(2p\\) subshells:
- The \\(2s\\) subshell holds \\(2\\) electrons.
- The \\(2p\\) subshell holds \\(6\\) electrons.
- Total electron capacity = \\(2 + 6 = 8\\text{ electrons}\\).
Corresponding to this capacity, Period 2 comprises exactly **\\(8\\text{ elements}\\)**:
\\[
\\text{Lithium (Li, 3)}, \\text{Be (4)}, \\text{B (5)}, \\text{C (6)}, \\text{N (7)}, \\text{O (8)}, \\text{F (9)}, \\text{Neon (Ne, 10)}
\\]

### 2. Physical Context & Practical Illustration:
Period 2 begins with the electropositive metal Lithium and transitions smoothly through metalloid Boron, non-metals Carbon, Nitrogen, Oxygen, and reactive halogen Fluorine, before concluding at noble gas Neon.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Period 1 contains 2 elements (H and He).
- **Option B is correct**: Period 2 contains exactly 8 elements.
- **Option C is incorrect**: Period 4 and 5 contain 18 elements.
- **Option D is incorrect**: Period 6 contains 32 elements.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-118",
    text: "What provisional name was assigned by Dmitri Mendeleev to the predicted undiscovered element having an atomic weight of approximately 72, which was later discovered in 1886 as Germanium?",
    options: [
      "Eka-boron (discovered as Scandium)",
      "Eka-aluminum (discovered as Gallium)",
      "Eka-silicon (discovered as Germanium)",
      "Eka-manganese (discovered as Technetium)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1869, Dmitri Mendeleev left three famous vacant spaces in his periodic table:
1. **Eka-boron**: Predicted atomic mass \\(\\approx 44\\text{ u}\\) \\(\\to\\) Discovered as **Scandium (Sc)** in 1879.
2. **Eka-aluminum**: Predicted atomic mass \\(\\approx 68\\text{ u}\\) \\(\\to\\) Discovered as **Gallium (Ga)** in 1875.
3. **Eka-silicon**: Predicted atomic mass **\\(\\approx 72\\text{ u}\\)** \\(\\to\\) Discovered as **Germanium (Ge)** in 1886 by Clemens Winkler.
Mendeleev predicted Eka-silicon would have:
- Atomic weight: \\(72\\text{ u}\\) (measured: \\(72.6\\text{ u}\\))
- Specific gravity: \\(5.5\\) (measured: \\(5.35\\))
- Oxide formula: \\(\\text{EsO}_2\\) (measured: \\(\\text{GeO}_2\\))
- Chloride formula: \\(\\text{EsCl}_4\\) (measured: \\(\\text{GeCl}_4\\))
Therefore, the element with predicted atomic weight 72 was **Eka-silicon**.

### 2. Physical Context & Practical Illustration:
The breathtaking accuracy with which Germanium matched every predicted parameter of Eka-silicon transformed the scientific world's view of Mendeleev's periodic law from an interesting hypothesis into an established natural law.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Eka-boron had predicted atomic weight 44 (Scandium).
- **Option B is incorrect**: Eka-aluminum had predicted atomic weight 68 (Gallium).
- **Option C is correct**: Eka-silicon had predicted atomic weight 72 (Germanium).
- **Option D is incorrect**: Eka-manganese had predicted atomic weight 100.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-119",
    text: "Which of the following chemical oxides is strongly BASIC in nature?",
    options: [
      "Sulfur dioxide (\\(\\text{SO}_2\\))",
      "Carbon dioxide (\\(\\text{CO}_2\\))",
      "Sodium oxide (\\(\\text{Na}_2\\text{O}\\))",
      "Dichlorine heptoxide (\\(\\text{Cl}_2\\text{O}_7\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Chemical nature of oxides:
- **Non-metallic Oxides**: Formed by electronegative non-metals (S, C, Cl); they are acidic oxides that hydrolyze in water to form acids:
  - \\(\\text{SO}_2 + \\text{H}_2\\text{O} \\to \\text{H}_2\\text{SO}_3\\) (Acidic)
  - \\(\\text{CO}_2 + \\text{H}_2\\text{O} \\to \\text{H}_2\\text{CO}_3\\) (Acidic)
  - \\(\\text{Cl}_2\\text{O}_7 + \\text{H}_2\\text{O} \\to 2\\text{HClO}_4\\) (Strongly acidic)
- **Metallic Oxides**: Formed by electropositive metals with low electronegativity:
  - **Sodium oxide (\\(\\text{Na}_2\\text{O}\\))** is an ionic oxide containing \\(\\text{O}^{2-}\\) ions. When dissolved in water, it reacts vigorously to yield strong caustic alkali sodium hydroxide:
\\[
\\text{Na}_2\\text{O}_{(s)} + \\text{H}_2\\text{O}_{(l)} \\longrightarrow 2\\text{NaOH}_{(aq)} \\quad (\\text{pH} \\approx 14, \\text{ Strongly Basic})
\\]
Therefore, **Sodium oxide** is strongly basic.

### 2. Physical Context & Practical Illustration:
Adding a pinch of \\(\\text{Na}_2\\text{O}\\) to water causes the solution to turn red litmus paper deep blue instantly, while bubbling \\(\\text{CO}_2\\) or \\(\\text{SO}_2\\) through water turns blue litmus red.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(\\text{SO}_2\\) is an acidic oxide.
- **Option B is incorrect**: \\(\\text{CO}_2\\) is an acidic oxide.
- **Option C is correct**: \\(\\text{Na}_2\\text{O}\\) is a strongly basic metallic oxide.
- **Option D is incorrect**: \\(\\text{Cl}_2\\text{O}_7\\) is an extremely acidic non-metal oxide.`
  },
  {
    questionCode: "MH-9-SCIT-4-4.2-OSC-120",
    text: "Which atmospheric gaseous pollutants are primarily responsible for the formation of Acid Rain?",
    options: [
      "Argon and Helium",
      "Methane and Hydrogen",
      "Sulfur dioxide (\\(\\text{SO}_2\\)) and Nitrogen dioxide (\\(\\text{NO}_2\\))",
      "Pure Oxygen and Nitrogen"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acid rain (rainwater with pH < 5.6) is caused primarily by atmospheric emissions of **Sulfur dioxide (\\(\\text{SO}_2\\))** and **Nitrogen oxides (\\(\\text{NO}_x\\), primarily \\(\\text{NO}_2\\))**:
1. **From Sulfur Dioxide**: Emitted from coal-fired power plants and oil refineries:
\\[
2\\text{SO}_{2(g)} + \\text{O}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)} \\longrightarrow 2\\mathbf{\\text{H}_2\\text{SO}_{4(aq)}} \\text{ (Sulfuric acid)}
\\]
2. **From Nitrogen Dioxide**: Emitted from high-temperature internal combustion automobile engines:
\\[
4\\text{NO}_{2(g)} + \\text{O}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)} \\longrightarrow 4\\mathbf{\\text{HNO}_{3(aq)}} \\text{ (Nitric acid)}
\\]
These strong acids dissolve in cloud droplets and precipitate as acid rain, causing severe ecological and structural damage.

### 2. Physical Context & Practical Illustration:
Acid rain corrodes marble and limestone monuments (such as the Taj Mahal) via chemical acid-carbonate decomposition: \\(\\text{CaCO}_3 + \\text{H}_2\\text{SO}_4 \\to \\text{CaSO}_4 + \\text{H}_2\\text{O} + \\text{CO}_2\\) (termed 'stone cancer').

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Argon and Helium are unreactive noble gases.
- **Option B is incorrect**: Methane and Hydrogen do not form strong acids.
- **Option C is correct**: Sulfur dioxide and Nitrogen dioxide are the primary causes of acid rain.
- **Option D is incorrect**: Pure oxygen and nitrogen are normal harmless atmospheric constituents.`
  }
];

module.exports = { ch4_part6 };
