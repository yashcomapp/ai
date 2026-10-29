// Chapter 5 (Acids, Bases and Salts) - Part 2: MH-9-SCIT-5-5.1 (Q31 to Q60, 30 Questions)
// Gold Standard 3-Part Solutions, Valid KaTeX, Zero Distractor Defects

const ch5_part2 = [
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-031",
    text: "What type of chemical product is obtained when a basic metallic oxide dissolves in water?",
    options: [
      "A base (alkaline metal hydroxide)",
      "An inorganic mineral acid",
      "A neutral insoluble salt",
      "A gaseous non-metallic hydride"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Most metallic oxides are basic anhydrides. When an electropositive metal oxide reacts with or dissolves in water, oxide ions (\\(O^{2-}\\)) act as powerful Bronsted-Lowry bases, abstracting protons from water molecules to generate hydroxide ions (\\(OH^-\\)):
\\[
O^{2-}(s) + H_2O(l) \\longrightarrow 2OH^-(aq)
\\]
For example, dissolving sodium oxide or potassium oxide in water yields soluble alkaline hydroxides:
\\[
Na_2O(s) + H_2O(l) \\longrightarrow 2NaOH(aq)
\\]
\\[
CaO(s) + H_2O(l) \\longrightarrow Ca(OH)_2(aq)
\\]
The resulting aqueous solution contains mobile hydroxide ions, rendering it basic and alkaline (\\(\\text{pH} > 7.0\\)).

### 2. Physical Context & Practical Illustration:
When white quicklime (\\(CaO\\)) powder is added to a beaker of water, an energetic exothermic slaking reaction occurs, warming the container and forming slaked lime (\\(Ca(OH)_2\\)). Dipping red litmus paper into the resulting solution immediately turns it blue, demonstrating the basic nature of dissolved metal oxides.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Base / Hydroxide):** Correct. Metallic oxides react with water to produce basic metal hydroxides.
- **Option B (Acid):** Incorrect. Non-metallic oxides (such as \\(SO_2, CO_2\\)) form acids in water, not metallic oxides.
- **Option C (Salt):** Incorrect. A salt is formed by neutralisation between an acid and a base, not metal oxide + water alone.
- **Option D (Hydride):** Incorrect. Hydrides are binary compounds of hydrogen; metallic oxides produce hydroxides.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-032",
    text: "When solid sodium oxide (\\(Na_2O\\)) is dissolved in pure water at \\(25^\\circ\\text{C}\\), the pH of the resulting solution is:",
    options: [
      "Equal to 1.0",
      "Equal to 7.0",
      "Less than 7.0",
      "Greater than 7.0"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Sodium oxide is a strongly basic ionic alkali-metal oxide. Upon addition to water, it undergoes complete, quantitative hydration to form sodium hydroxide:
\\[
Na_2O(s) + H_2O(l) \\longrightarrow 2Na^+(aq) + 2OH^-(aq)
\\]
Sodium hydroxide is a strong base that dissociates \\(100\\%\\) in aqueous solution. Because of the liberation of high concentrations of mobile hydroxide ions:
\\[
[OH^-] \\gg 1.0 \\times 10^{-7}\\text{ mol/L}
\\]
Using the ionic product of water at \\(25^\\circ\\text{C}\\) (\\(K_w = [H^+][OH^-] = 10^{-14}\\)):
\\[
[H^+] = \\frac{K_w}{[OH^-]} \\ll 10^{-7}\\text{ mol/L} \\implies \\text{pH} = -\\log_{10}[H^+] > 7.0
\\]
Typical solutions of \\(Na_2O\\) exhibit strongly alkaline pH values ranging from 12 to 14.

### 2. Physical Context & Practical Illustration:
The solution feels slippery to the touch, turns colourless phenolphthalein indicator deep magenta pink, and turns red litmus paper blue, confirming a pH well above 7.0.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1.0):** Incorrect. A pH of 1 represents a strong acid (like \\(0.1\\text{ M } HCl\\)).
- **Option B (7.0):** Incorrect. A pH of 7 represents pure neutral water.
- **Option C (Less than 7.0):** Incorrect. \\(\\text{pH} < 7\\) denotes an acidic solution.
- **Option D (Greater than 7.0):** Correct. Dissolving \\(Na_2O\\) forms \\(NaOH\\), making the solution strongly basic with \\(\\text{pH} > 7.0\\).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-033",
    text: "When completely dry strips of blue and red litmus paper are held inside a gas jar containing dry sulphur dioxide gas (\\(SO_2\\)), what observable change occurs?",
    options: [
      "Blue litmus paper immediately turns red",
      "Red litmus paper turns blue",
      "No colour change occurs in either litmus paper",
      "Blue paper turns red and red paper turns blue"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acid-base indicators function via reversible proton transfer equilibria. For an acidic gas to exhibit its acidic properties and effect a colour change, it must first dissociate to generate hydronium ions (\\(H_3O^+\\)):
\\[
SO_2(g) + H_2O(l) \\rightleftharpoons H_2SO_3(aq) \\rightleftharpoons H^+(aq) + HSO_3^-(aq)
\\]
In the complete absence of moisture (both the \\(SO_2\\) gas and the litmus paper are dry), no liquid water is present to hydrate the gas or hydrolyse the indicator dye molecules. Consequently, no free \\(H^+\\) ions are formed:
\\[
[H^+] = 0 \\implies \\text{No protonation of indicator chromophores}
\\]
Therefore, dry \\(SO_2\\) cannot alter the colour of completely dry litmus paper.

### 2. Physical Context & Practical Illustration:
If the litmus paper is subsequently moistened with a single drop of distilled water and re-introduced into the same \\(SO_2\\) jar, the blue litmus instantly turns bright red due to the rapid formation of sulfurous acid (\\(H_2SO_3\\)), followed by slow bleaching to white.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Blue litmus turns red only when moisture is present to form sulfurous acid.
- **Option B:** Incorrect. \\(SO_2\\) is an acidic gas and never behaves as a base.
- **Option C:** Correct. In the absence of water, dry acidic gases do not ionise, producing zero colour change on dry litmus papers.
- **Option D:** Incorrect. Indicator colour changes require moisture and are unidirectional.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-034",
    text: "A dilute aqueous solution containing approximately 5% to 8% acetic acid is commonly known as:",
    options: [
      "Vinegar",
      "Soda water",
      "Denatured spirit",
      "Saline solution"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Vinegar** is an aqueous solution containing approximately **\\(5\\%\\) to \\(8\\%\\) acetic acid** (\\(CH_3COOH\\)) by volume.
It is manufactured by the microbiological oxidation of dilute ethanol (derived from fermented apple cider, wine, or sugarcane molasses) using *Acetobacter* bacteria in the presence of atmospheric oxygen:
\\[
C_2H_5OH(aq) + O_2(g) \\xrightarrow{\\text{Acetobacter}} CH_3COOH(aq) + H_2O(l)
\\]
Pure anhydrous acetic acid (melting point \\(16.6^\\circ\\text{C}\\) / \\(290\\text{ K}\\)) freezes into clear, ice-like crystals at cool temperatures and is known as **glacial acetic acid**.

### 2. Physical Context & Practical Illustration:
Vinegar is widely used in households as a culinary condiment, pickling preservative, and mild cleaning agent. Its acidic nature (\\(\\text{pH} \\approx 2.5\\text{ to } 3.0\\)) inhibits bacterial proliferation in preserved foods and dissolves alkaline mineral scale in kitchen kettles.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Vinegar):** Correct. Dilute acetic acid (5% to 8%) is universally known as vinegar.
- **Option B (Soda water):** Incorrect. Soda water is carbon dioxide dissolved under pressure in water.
- **Option C (Denatured spirit):** Incorrect. Denatured spirit is ethanol poisoned with methanol and pyridine to render it non-potable.
- **Option D (Saline solution):** Incorrect. Saline solution is dilute sodium chloride in water.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-035",
    text: "What is the chemical molecular formula of quicklime?",
    options: [
      "\\(CaO\\)",
      "\\(Ca(OH)_2\\)",
      "\\(CaCO_3\\)",
      "\\(Ca(HCO_3)_2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The calcium cycle involves three distinct chemical compounds:
1. **Limestone / Chalk / Marble (\\(CaCO_3\\)):** Calcium carbonate. When thermally decomposed (calcined) in a lime kiln at \\(\\approx 900^\\circ\\text{C}\\) to \\(1000^\\circ\\text{C}\\), it loses carbon dioxide:
   \\[
   CaCO_3(s) \\xrightarrow{\\Delta} \\mathbf{CaO(s)} + CO_2(g)\\uparrow
   \\]
   The solid product obtained is calcium oxide, universally designated as **quicklime** (or burnt lime).
2. **Slaked lime (\\(Ca(OH)_2\\)):** Formed when quicklime reacts with water:
   \\[
   CaO(s) + H_2O(l) \\longrightarrow Ca(OH)_2(s)
   \\]
Thus, the molecular formula of quicklime is **\\(CaO\\)**.

### 2. Physical Context & Practical Illustration:
Quicklime is an essential raw material in civil construction (cement manufacturing), steelmaking (as a basic flux to remove silicate impurities), and paper manufacturing. It is a powerful desiccant due to its intense affinity for moisture.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(CaO\\)):** Correct. Calcium oxide is quicklime.
- **Option B (\\(Ca(OH)_2\\)):** Incorrect. Calcium hydroxide is slaked lime.
- **Option C (\\(CaCO_3\\)):** Incorrect. Calcium carbonate is limestone or marble.
- **Option D (\\(Ca(HCO_3)_2\\)):** Incorrect. Calcium hydrogencarbonate causes temporary water hardness.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-036",
    text: "Which of the following organic carboxylic acids is naturally present in ripe tamarind and grapes?",
    options: [
      "Citric acid",
      "Gluconic acid",
      "Lactic acid",
      "Tartaric acid"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Tartaric acid** is a diprotic organic dicarboxylic acid having the chemical formula \\(C_4H_6O_6\\) and the structural formula:
\\[
HOOC-CH(OH)-CH(OH)-COOH
\\]
It contains two chiral carbon centres and two ionisable carboxylic acid groups (\\(pK_{a1} = 2.89\\), \\(pK_{a2} = 4.40\\)).
It occurs naturally in high concentrations in the pulp of tamarind (*Tamarindus indica*), grapes, and bananas, existing both as the free acid and as its potassium hydrogen salt (cream of tartar, \\(KHC_4H_4O_6\\)).

### 2. Physical Context & Practical Illustration:
Because tartaric acid is a solid, non-hygroscopic edible acid, it is a key constituent of commercial baking powder along with sodium bicarbonate (\\(NaHCO_3\\)). When mixed with water in dough, it reacts gently to liberate \\(CO_2\\) without leaving a bitter alkaline sodium carbonate residue.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Citric acid):** Incorrect. Citric acid is found predominantly in citrus fruits such as lemons and limes.
- **Option B (Gluconic acid):** Incorrect. Gluconic acid is produced by oxidation of glucose in honey.
- **Option C (Lactic acid):** Incorrect. Lactic acid is found in sour milk and yogurt.
- **Option D (Tartaric acid):** Correct. Tartaric acid is the characteristic organic acid present in tamarind and grapes.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-037",
    text: "Which chemical pair is charged into a soda-acid fire extinguisher to generate extinguishing carbon dioxide gas?",
    options: [
      "Calcium carbonate and hydrochloric acid",
      "Calcium carbonate and sulphuric acid",
      "Sodium bicarbonate and sulphuric acid",
      "Sodium carbonate and hydrochloric acid"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a soda-acid chemical fire extinguisher, the active chemical charge comprises:
1. An aqueous solution of **sodium bicarbonate** (baking soda, \\(NaHCO_3\\)) stored in the main metal cylinder.
2. Concentrated or dilute **sulphuric acid** (\\(H_2SO_4\\)) held in an internal, sealed glass ampoule or container.
When the plunger mechanism is struck, the acid vessel ruptures, mixing the reactants:
\\[
2NaHCO_3(aq) + H_2SO_4(aq) \\longrightarrow Na_2SO_4(aq) + 2H_2O(l) + 2CO_2(g)\\uparrow
\\]
The reaction generates high internal pressure of non-combustible carbon dioxide gas, expelling the aqueous mixture at high velocity.

### 2. Physical Context & Practical Illustration:
The water cools the burning fuel below its flash point, while the heavy \\(CO_2\\) gas blankets the combustion zone, displacing ambient atmospheric oxygen and extinguishing Class A (solid fuel) fires.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Calcium carbonate is an insoluble solid and hydrochloric acid is too volatile and corrosive.
- **Option B:** Incorrect. The reaction between \\(CaCO_3\\) and \\(H_2SO_4\\) forms an insoluble crust of calcium sulphate (\\(CaSO_4\\)) that quickly stops the reaction.
- **Option C:** Correct. Sodium bicarbonate (\\(NaHCO_3\\)) and sulphuric acid (\\(H_2SO_4\\)) produce rapid, reliable \\(CO_2\\) discharge.
- **Option D:** Incorrect. Volatile \\(HCl\\) produces choking acid fumes, making it unsuitable for portable extinguishers.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-038",
    text: "What is the official chemical name of the essential dietary nutrient Vitamin C?",
    options: [
      "Lactic acid",
      "Acetic acid",
      "Ascorbic acid",
      "Benzoic acid"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Vitamin C** is chemically defined as **L-ascorbic acid** (chemical formula \\(C_6H_8O_6\\), molar mass \\(176.12\\text{ g/mol}\\)).
Structurally, it is a lactone featuring an enediol grouping (\\(-\\text{C}(OH)=\\text{C}(OH)-\\)) adjacent to a carbonyl group:
\\[
C_6H_8O_6 \\rightleftharpoons C_6H_7O_6^- + H^+ \\quad (pK_a = 4.10)
\\]
The enediol hydrogen atoms are acidic because the resulting ascorbate monoanion is strongly stabilized by delocalisation of negative charge across the conjugated system.

### 2. Physical Context & Practical Illustration:
Ascorbic acid is a powerful physiological antioxidant and water-soluble vitamin. It easily oxidises to dehydroascorbic acid, thereby scavenging free radicals, maintaining iron in the absorbable ferrous (\\(Fe^{2+}\\)) state, and co-catalysing collagen hydroxylation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Lactic acid):** Incorrect. Lactic acid is found in dairy products, not Vitamin C.
- **Option B (Acetic acid):** Incorrect. Acetic acid is the active constituent of vinegar.
- **Option C (Ascorbic acid):** Correct. The chemical name of Vitamin C is ascorbic acid.
- **Option D (Benzoic acid):** Incorrect. Benzoic acid is an aromatic preservative used in packaged fruit juices.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-039",
    text: "When drops of phenolphthalein indicator are added to an acidic carbonated soft drink, what change in the indicator occurs?",
    options: [
      "The solution turns deep magenta pink",
      "The solution turns royal blue",
      "The indicator remains colourless (no pink colour appears)",
      "The solution turns dark opaque black"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Phenolphthalein (\\(C_{20}H_{14}O_4\\)) is a synthetic organic dye used as an acid-base indicator. In aqueous solution, it exists in an equilibrium between its un-ionised colourless lactone form and its ionised pink/magenta quinonoid dianion form:
\\[
H_2\\text{Ph} (\\text{Colourless}) + 2H_2O \\rightleftharpoons 2H_3O^+ + \\text{Ph}^{2-} (\\text{Pink})
\\]
- In acidic or neutral solutions with \\(\\text{pH} < 8.3\\), excess hydronium ions shift the equilibrium entirely to the left, maintaining the indicator in its **colourless** state.
- In alkaline solutions with \\(\\text{pH} > 8.3\\), hydroxide ions neutralise \\(H_3O^+\\), forming the resonance-stabilized quinonoid dianion (\\(\\text{Ph}^{2-}\\)), producing a vivid **pink/magenta** colour.
Carbonated beverages contain dissolved carbonic acid (\\(H_2CO_3\\)) and citric acid, giving them an acidic pH (typically \\(2.5\\text{ to } 3.5\\)). Consequently, phenolphthalein remains completely colourless.

### 2. Physical Context & Practical Illustration:
If dilute sodium hydroxide (\\(NaOH\\)) is subsequently added dropwise to the carbonated beverage, the acid is gradually neutralised. Once the pH crosses 8.3, the solution suddenly flashes pink.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Phenolphthalein turns pink only in alkaline conditions (\\(\\text{pH} > 8.3\\)).
- **Option B:** Incorrect. Phenolphthalein never turns blue (blue indicates base on litmus).
- **Option C:** Correct. In acidic media (\\(\\text{pH} < 8.3\\)), phenolphthalein indicator is completely colourless.
- **Option D:** Incorrect. No black precipitate is formed.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-040",
    text: "Which of the following statements regarding acids, bases, and salts is INCORRECT?",
    options: [
      "Metallic oxides generally exhibit basic chemical properties",
      "All bases are alkalis, but all alkalis are not bases",
      "Non-metallic oxides generally exhibit acidic chemical properties",
      "Salts formed from the reaction between a strong acid and a weak base yield acidic solutions"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze each statement based on chemical definitions:
- **Statement A:** Correct. Electropositive metal oxides (e.g., \\(Na_2O, CaO, MgO\\)) form basic hydroxides in water or react with acids to form salts.
- **Statement B:** **INCORRECT**. The true relationship is the exact reverse:
  \\[
  \\text{\"All alkalis are bases, but all bases are not alkalis.\"}
  \\]
  An alkali is specifically defined as a base that is soluble in water (such as \\(NaOH, KOH, Ca(OH)_2\\)). Insoluble bases (such as \\(Cu(OH)_2, Fe(OH)_3, Al(OH)_3\\)) are bases because they neutralise acids, but they are *not* alkalis because they do not dissolve in water.
- **Statement C:** Correct. Non-metallic oxides (such as \\(CO_2, SO_2, NO_2\\)) are acid anhydrides that form acidic solutions in water.
- **Statement D:** Correct. A salt formed from a strong acid and a weak base (such as \\(NH_4Cl\\)) undergoes cation hydrolysis, producing \\(\\text{pH} < 7.0\\).

### 2. Physical Context & Practical Illustration:
Think of 'alkalis' as a subset contained inside the broader set of 'bases'. Just as all squares are rectangles, but not all rectangles are squares, all alkalis are bases, but insoluble bases are not alkalis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Correct statement (hence not the incorrect choice). Metal oxides are basic.
- **Option B:** **INCORRECT statement** (hence the correct answer). It falsely claims all bases are alkalis.
- **Option C:** Correct statement. Non-metal oxides are acidic.
- **Option D:** Correct statement. Strong acid + weak base salts hydrolyse to form acidic solutions.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-041",
    text: "Which of the following common domestic substances is acidic in nature (\\(\\text{pH} < 7.0\\))?",
    options: [
      "Natural apple juice",
      "Soap solution",
      "Slaked lime solution",
      "Baking soda solution"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us assess the pH and chemical nature of each substance:
1. **Apple juice:** Contains natural organic acids, predominantly **malic acid** (\\(C_4H_6O_5\\)), giving it a distinctly acidic pH typically between **\\(3.3\\) and \\(4.0\\)** (strictly \\(< 7.0\\)).
2. **Soap solution:** Formed by alkaline hydrolysis of fatty acids; aqueous soaps undergo partial hydrolysis to generate free \\(OH^-\\) ions, resulting in a basic pH of **\\(9.0\\text{ to } 10.0\\)**.
3. **Slaked lime (\\(Ca(OH)_2\\)):** A strong chemical base that dissociates to yield hydroxide ions, producing a strongly basic pH of **\\(12.0\\text{ to } 12.5\\)**.
4. **Baking soda (\\(NaHCO_3\\)):** The salt of a strong base (\\(NaOH\\)) and a weak acid (\\(H_2CO_3\\)); undergoes anion hydrolysis to produce a mildly alkaline pH of **\\(\\approx 8.3\\)**.

### 2. Physical Context & Practical Illustration:
Dipping blue litmus paper into fresh apple juice causes it to turn red immediately, whereas soap solution, slaked lime, and baking soda solution all turn red litmus paper blue.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Apple juice):** Correct. Apple juice is rich in malic acid and is naturally acidic.
- **Option B (Soap solution):** Incorrect. Soap solution is alkaline (\\(\\text{pH} \\approx 9-10\\)).
- **Option C (Slaked lime):** Incorrect. Slaked lime is strongly basic (\\(\\text{pH} \\approx 12.4\\)).
- **Option D (Baking soda):** Incorrect. Sodium bicarbonate is mildly basic (\\(\\text{pH} \\approx 8.3\\)).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-042",
    text: "When tested with both red and blue litmus papers, an aqueous solution of pure sodium chloride (\\(NaCl\\)) will produce:",
    options: [
      "A colour change from red to blue only",
      "A colour change from blue to red only",
      "No colour change in either red or blue litmus paper",
      "A complete bleaching of both litmus papers to white"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Sodium chloride (\\(NaCl\\)) is a normal salt formed by the complete neutralisation of a strong acid (\\(HCl\\)) with an equivalent amount of a strong base (\\(NaOH\\)):
\\[
HCl(aq) + NaOH(aq) \\longrightarrow NaCl(aq) + H_2O(l)
\\]
In aqueous solution, sodium chloride dissociates completely:
\\[
NaCl(s) \\xrightarrow{H_2O} Na^+(aq) + Cl^-(aq)
\\]
- \\(Na^+\\) is the conjugate cation of the strong base \\(NaOH\\) and does not react with water.
- \\(Cl^-\\) is the conjugate anion of the strong acid \\(HCl\\) and does not react with water.
Because neither ion undergoes salt hydrolysis, the auto-ionisation equilibrium of water remains undisturbed:
\\[
[H_3O^+] = [OH^-] = 1.0 \\times 10^{-7}\\text{ mol/L} \\implies \\text{pH} = 7.0 \\quad (\\text{Neutral})
\\]

### 2. Physical Context & Practical Illustration:
Because the solution is strictly neutral at pH 7.0, red litmus paper remains red and blue litmus paper remains blue. Furthermore, testing with universal indicator yields a green colour.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Turning red litmus blue is a characteristic of alkaline solutions (\\(\\text{pH} > 7\\)).
- **Option B:** Incorrect. Turning blue litmus red is a characteristic of acidic solutions (\\(\\text{pH} < 7\\)).
- **Option C:** Correct. As a neutral salt with \\(\\text{pH} = 7.0\\), sodium chloride produces no colour change on either litmus paper.
- **Option D:** Incorrect. Bleaching is caused by strong oxidising agents like chlorine or hypochlorite, not neutral \\(NaCl\\).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-043",
    text: "Hardness of natural water is caused primarily by the presence of dissolved bicarbonates, chlorides, and sulphates of which metallic cations?",
    options: [
      "Sodium and Potassium (\\(Na^+\\) and \\(K^+\\))",
      "Zinc and Aluminium (\\(Zn^{2+}\\) and \\(Al^{3+}\\))",
      "Copper and Silver (\\(Cu^{2+}\\) and \\(Ag^+\\))",
      "Calcium and Magnesium (\\(Ca^{2+}\\) and \\(Mg^{2+}\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Water hardness is defined by its capacity to precipitate soap and form boiler scale. It is caused by the presence of soluble salts of **divalent alkaline earth metal cations**, predominantly **calcium (\\(Ca^{2+}\\))** and **magnesium (\\(Mg^{2+}\\))**:
1. **Temporary Hardness:** Caused by dissolved hydrogen carbonates (bicarbonates):
   \\[
   Ca(HCO_3)_2 \\quad \\text{and} \\quad Mg(HCO_3)_2
   \\]
   Can be removed simply by boiling, which precipitates insoluble carbonates:
   \\[
   Ca(HCO_3)_2(aq) \\xrightarrow{\\Delta} CaCO_3(s)\\downarrow + H_2O(l) + CO_2(g)\\uparrow
   \\]
2. **Permanent Hardness:** Caused by dissolved chlorides and sulphates:
   \\[
   CaCl_2, \\, MgCl_2, \\, CaSO_4, \\, MgSO_4
   \\]
   Cannot be removed by boiling; requires chemical precipitation with washing soda (\\(Na_2CO_3\\)) or ion-exchange resins.

### 2. Physical Context & Practical Illustration:
When soap (sodium stearate) is added to hard water, \\(Ca^{2+}\\) and \\(Mg^{2+}\\) ions precipitate insoluble calcium and magnesium stearates (scum), preventing lather formation until all divalent ions are removed.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Sodium and potassium salts form soluble stearates and do not cause water hardness.
- **Option B:** Incorrect. Zinc and aluminium occur in negligible amounts in natural freshwater.
- **Option C:** Incorrect. Copper and silver are trace heavy metals.
- **Option D:** Correct. Dissolved calcium and magnesium salts are the primary causes of temporary and permanent water hardness.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-044",
    text: "Which chemical acid is universally designated as the 'King of Chemicals' owing to its central role across modern industry?",
    options: [
      "Acetic acid (\\(CH_3COOH\\))",
      "Phosphoric acid (\\(H_3PO_4\\))",
      "Oxalic acid (\\(H_2C_2O_4\\))",
      "Sulphuric acid (\\(H_2SO_4\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Sulphuric acid** (\\(H_2SO_4\\)) is known as the **King of Chemicals** (and 'King of Acids').
Its premier industrial status arises from its unique combination of chemical attributes:
1. **Strong Dibasic Mineral Acid:** Undergoes two-step dissociation:
   \\[
   H_2SO_4 \\longrightarrow H^+ + HSO_4^- \\quad (K_{a1} \\gg 1)
   \\]
   \\[
   HSO_4^- \\rightleftharpoons H^+ + SO_4^{2-} \\quad (K_{a2} = 1.2 \\times 10^{-2})
   \\]
2. **Powerful Dehydrating Agent:** Avidly removes chemically combined water from carbohydrates (charring sugar into pure carbon):
   \\[
   C_{12}H_{22}O_{11}(s) \\xrightarrow{\\text{conc. } H_2SO_4} 12C(s) + 11H_2O(g)
   \\]
3. **Low Volatility and High Boiling Point (\\(337^\\circ\\text{C}\\)):** Used to displace more volatile acids (like \\(HCl\\) and \\(HNO_3\\)) from their respective salts.

### 2. Physical Context & Practical Illustration:
Sulphuric acid is consumed in immense quantities in manufacturing fertilizers (ammonium sulphate, superphosphate), refining petroleum, manufacturing paints, synthetic fibres (rayon), explosives, and vehicle batteries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Acetic acid):** Incorrect. Acetic acid is a weak organic acid.
- **Option B (Phosphoric acid):** Incorrect. Phosphoric acid has specialized uses in soft drinks and fertilizers.
- **Option C (Oxalic acid):** Incorrect. Oxalic acid is a weak organic dicarboxylic acid.
- **Option D (Sulphuric acid):** Correct. Sulphuric acid is universally known as the 'King of Chemicals'.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-045",
    text: "When an acidic aqueous solution is tested with blue litmus paper, the colour of the paper changes to:",
    options: [
      "Bright green",
      "Bright red",
      "Bright yellow",
      "Deep orange"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Litmus is a natural water-soluble mixture of dyes extracted from lichens. Its principal chromophore is **7-hydroxyphenoxazone**. In aqueous solution, it acts as a weak organic acid:
\\[
H\\text{In}(aq) \\rightleftharpoons H^+(aq) + \\text{In}^-(aq)
\\]
- The conjugate base form (\\(\\text{In}^-\\)) is **blue**.
- The un-ionised protonated acid form (\\(H\\text{In}\\)) is **red**.
When blue litmus paper is brought into contact with an acidic solution possessing a high concentration of hydronium ions (\\([H_3O^+] > 10^{-7}\\text{ M}\\)), Le Chatelier's principle shifts the equilibrium toward the protonated form:
\\[
\\text{In}^- (\\text{blue}) + H_3O^+ \\longrightarrow H\\text{In} (\\text{red}) + H_2O
\\]
Consequently, the blue paper changes to a distinct **red colour**.

### 2. Physical Context & Practical Illustration:
This colour change is the universal test for acids taught throughout chemistry. It applies equally to laboratory mineral acids (\\(HCl\\), \\(HNO_3\\), \\(H_2SO_4\\)) and domestic acidic fluids (lemon juice, tomato juice, vinegar).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Green):** Incorrect. Green indicates neutrality on universal indicator, not litmus.
- **Option B (Red):** Correct. Acids turn blue litmus paper red.
- **Option C (Yellow):** Incorrect. Yellow is the colour of methyl orange in base or universal indicator in weak acid.
- **Option D (Orange):** Incorrect. Litmus has only two distinct colour forms: red and blue.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-046",
    text: "What is the basicity of acetic acid (\\(CH_3COOH\\))?",
    options: [
      "1 (Monobasic)",
      "2 (Dibasic)",
      "3 (Tribasic)",
      "4 (Tetrabasic)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **basicity of an acid** is defined as the number of ionisable, replaceable hydrogen ions (\\(H^+\\)) furnished by one molecule of the acid upon dissociation in water:
\\[
\\text{Basicity} = \\frac{\\text{Number of ionisable } H^+ \\text{ ions}}{\\text{One molecule of acid}}
\\]
The structural formula of acetic acid is:
\\[
CH_3-COOH
\\]
- The 3 hydrogen atoms bonded directly to the carbon atom in the methyl group (\\(-\\text{CH}_3\\)) share non-polar covalent bonds (low electronegativity difference, \\(\\Delta\\chi = 2.5 - 2.1 = 0.4\\)) and are not ionisable.
- Only the single hydrogen atom bonded to the highly electronegative oxygen atom in the carboxyl group (\\(-\\text{O}-\\text{H}\\)) can undergo heterolytic cleavage in polar water:
\\[
CH_3COOH(aq) + H_2O(l) \\rightleftharpoons CH_3COO^-(aq) + H_3O^+(aq)
\\]
Because each molecule produces exactly **one** hydronium ion, acetic acid is strictly **monobasic (basicity = 1)**.

### 2. Physical Context & Practical Illustration:
A common misconception is that because acetic acid contains four hydrogen atoms in its formula (\\(C_2H_4O_2\\)), its basicity must be 4. Stoichiometric titrations clearly disprove this: exactly 1 mole of \\(NaOH\\) neutralises 1 mole of acetic acid to reach the equivalence point:
\\[
CH_3COOH + NaOH \\longrightarrow CH_3COONa + H_2O
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1 - Monobasic):** Correct. Only the single carboxylic proton is ionisable in aqueous solution.
- **Option B (2 - Dibasic):** Incorrect. Dibasic acids have 2 ionisable protons (e.g., \\(H_2SO_4\\)).
- **Option C (3 - Tribasic):** Incorrect. Tribasic acids have 3 ionisable protons (e.g., \\(H_3PO_4\\)).
- **Option D (4 - Tetrabasic):** Incorrect. The 3 methyl hydrogens are firmly bound to carbon and do not ionise.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-047",
    text: "Which chemical mineral acid was historically known in alchemy as 'oil of vitriol'?",
    options: [
      "Aqua regia",
      "Sulphuric acid (\\(H_2SO_4\\))",
      "Nitric acid (\\(HNO_3\\))",
      "Hydrochloric acid (\\(HCl\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In medieval alchemy, hydrated sulphate salts of transition metals were called **vitriols** because their glassy crystals resembled glass (Latin *vitrum*):
- Green vitriol: Ferrous sulphate heptahydrate (\\(FeSO_4 \\cdot 7H_2O\\))
- Blue vitriol: Copper(II) sulphate pentahydrate (\\(CuSO_4 \\cdot 5H_2O\\))
When green vitriol crystals were thermally decomposed in an alembic retort, sulfur trioxide and water distilled off to condense as a heavy, dense, oily, corrosive liquid:
\\[
2FeSO_4 \\cdot 7H_2O(s) \\xrightarrow{\\Delta} Fe_2O_3(s) + SO_2(g) + SO_3(g) + 14H_2O(g)
\\]
\\[
SO_3(g) + H_2O(l) \\longrightarrow H_2SO_4(l)
\\]
Because of its viscous, oily consistency and its origin from green vitriol, Jabir ibn Hayyan and European alchemists called this liquid **oil of vitriol** (now universally named **sulphuric acid**, \\(H_2SO_4\\)).

### 2. Physical Context & Practical Illustration:
Concentrated sulphuric acid (98%) retains this characteristic oily physical appearance, with a high viscosity (\\(26.7\\text{ mPa}\\cdot\\text{s}\\) at \\(20^\\circ\\text{C}\\)) and a high density of \\(1.84\\text{ g/cm}^3\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Aqua regia):** Incorrect. Aqua regia is a mixture of nitric acid and hydrochloric acid (royal water).
- **Option B (\\(H_2SO_4\\)):** Correct. Sulphuric acid is the historic 'oil of vitriol'.
- **Option C (\\(HNO_3\\)):** Incorrect. Nitric acid was historically called *aqua fortis* (strong water).
- **Option D (\\(HCl\\)):** Incorrect. Hydrochloric acid was historically called *muriatic acid* or *spirit of salt*.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-048",
    text: "Which of the following acid-base indicators displays two distinctly different colours in acidic versus alkaline media?",
    options: [
      "Red litmus paper",
      "Phenolphthalein",
      "Turmeric extract",
      "Methyl orange"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the colour behaviour of each indicator in acidic and alkaline conditions:
1. **Red litmus:** Stays red in acidic/neutral media; turns blue only in alkaline media.
2. **Phenolphthalein:** Colourless in acidic media (\\(\\text{pH} < 8.3\\)) and neutral water; turns pink only in alkaline media.
3. **Turmeric extract:** Remains yellow in acidic and neutral media; turns reddish-brown only in basic media (such as soap).
4. **Methyl orange:** Contains a pH-sensitive azo dye that undergoes distinct colour transitions across its operational range (\\(\\text{pH } 3.1 - 4.4\\)):
   - In acidic solution (\\(\\text{pH} < 3.1\\)): Exhibits a distinct **red/pink** colour.
   - In alkaline solution (\\(\\text{pH} > 4.4\\)): Exhibits a distinct **yellow** colour.
Thus, **methyl orange** provides clear, distinct, active colour changes in both acidic (red) and alkaline (yellow) media.

### 2. Physical Context & Practical Illustration:
Because methyl orange produces a bright yellow in basic solutions and switches sharply to red in acidic media, it is widely utilized in industrial and educational laboratories for titrating strong acids against both strong and weak bases.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Red litmus):** Incorrect. Remains red in acid; only changes colour in alkali.
- **Option B (Phenolphthalein):** Incorrect. Remains colourless in acid; only shows color in base.
- **Option C (Turmeric):** Incorrect. Remains yellow in acid; turns reddish-brown only in base.
- **Option D (Methyl orange):** Correct. Changes colour actively in both regimes: red in acid and yellow in alkali.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-049",
    text: "When moist blue litmus paper is introduced into a gas jar containing carbon dioxide gas (\\(CO_2\\)), what observable colour change occurs?",
    options: [
      "Blue litmus paper turns bright yellow",
      "Blue litmus paper remains completely blue",
      "Blue litmus paper turns faint red",
      "Blue litmus paper is bleached to pure white"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Carbon dioxide (\\(CO_2\\)) is a non-metallic acidic oxide (an acid anhydride). When it encounters the moisture on wet blue litmus paper, it dissolves and chemically hydrates to form unstable diprotic **carbonic acid** (\\(H_2CO_3\\)):
\\[
CO_2(g) + H_2O(l) \\rightleftharpoons H_2CO_3(aq)
\\]
Carbonic acid partially ionises in water to release hydronium ions:
\\[
H_2CO_3(aq) + H_2O(l) \\rightleftharpoons H_3O^+(aq) + HCO_3^-(aq)
\\]
The presence of hydronium ions lowers the pH (typically to \\(\\approx 4.0 - 5.5\\)), causing the blue litmus dye to be protonated into its red acid form:
\\[
\\text{In}^- (\\text{blue}) + H^+ \\longrightarrow H\\text{In} (\\text{red})
\\]
Because carbonic acid is a weak acid, the blue paper turns **faint red (or pinkish-red)**.

### 2. Physical Context & Practical Illustration:
This test confirms the acidic nature of non-metallic combustion gases. When one blows breath through a straw into water coloured with blue litmus, the solution gradually turns pale red as dissolved respiratory \\(CO_2\\) forms carbonic acid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Litmus does not turn yellow (yellow is typical of methyl orange).
- **Option B:** Incorrect. Blue litmus changes to red in the presence of acidic carbonic acid.
- **Option C:** Correct. Dissolved \\(CO_2\\) forms carbonic acid, turning moist blue litmus paper faint red.
- **Option D:** Incorrect. Bleaching to white is caused by chlorine (\\(Cl_2\\)) or sulfur dioxide (\\(SO_2\\)), not carbon dioxide.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-050",
    text: "Why is common salt (sodium chloride, \\(NaCl\\)) added during the final stage of soap manufacturing?",
    options: [
      "To chemically disinfect and sterilise the soap mixture",
      "To increase the lathering and foaming capacity of the soap",
      "To precipitate and separate the insoluble soap from the aqueous reaction mixture (salting out)",
      "To dehydrate the soap by evaporating all residual water"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
During saponification, fats or oils (glyceryl esters) are hydrolysed by boiling with sodium hydroxide solution, yielding soap (sodium fatty acid salts, e.g., sodium stearate, \\(C_{17}H_{35}COONa\\)) and glycerol dissolved together in water:
\\[
\\text{Triglyceride} + 3NaOH \\longrightarrow \\text{Glycerol} + 3C_{17}H_{35}COONa(aq)
\\]
Because sodium stearate remains partially colloidal and soluble in hot water, common salt (\\(NaCl\\)) is added.
Dissolving \\(NaCl\\) introduces a very high concentration of sodium ions (\\(Na^+\\)):
\\[
NaCl(s) \\longrightarrow Na^+(aq) + Cl^-(aq)
\\]
By the **common ion effect**, the elevated \\([Na^+]\\) concentration dramatically exceeds the solubility product (\\(K_{sp}\\)) of sodium stearate:
\\[
[C_{17}H_{35}COO^-][Na^+] > K_{sp}
\\]
This shifts the ionic equilibrium to the left, causing the soap to precipitate out as an insoluble solid curd that floats to the surface. This industrial technique is known as **salting out of soap**.

### 2. Physical Context & Practical Illustration:
The solid precipitated soap curd is easily skimmed off, washed, and pressed into moulds, while the underlying aqueous layer ('spent lye') containing valuable glycerol is drained away and purified for pharmaceutical uses.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Common salt is not added as a disinfectant in soap boiling.
- **Option B:** Incorrect. Salt does not enhance foaming; excessive salt actually suppresses soap lathering.
- **Option C:** Correct. Common salt causes the precipitation of solid soap from the aqueous solution via the common ion effect (salting out).
- **Option D:** Incorrect. Salt does not evaporate water; it induces phase separation.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-051",
    text: "Nitric acid (\\(HNO_3\\)) is a strong mineral acid. The aqueous pH of any nitric acid solution will always be:",
    options: [
      "Exactly equal to 1.0 regardless of concentration",
      "Equal to 7.0",
      "Strictly less than 7.0 (\\(\\text{pH} < 7.0\\))",
      "Strictly greater than 7.0 (\\(\\text{pH} > 7.0\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Nitric acid (\\(HNO_3\\)) is a strong monoprotic mineral acid that ionises completely in aqueous solution:
\\[
HNO_3(aq) + H_2O(l) \\longrightarrow H_3O^+(aq) + NO_3^-(aq)
\\]
The total concentration of hydronium ions in solution is the sum of hydronium from nitric acid and that from water auto-ionisation:
\\[
[H_3O^+] = [H_3O^+]_{HNO_3} + [H_3O^+]_{H_2O} > 1.0 \\times 10^{-7}\\text{ mol/L}
\\]
Applying the mathematical definition of \\(\\text{pH}\\):
\\[
\\text{pH} = -\\log_{10}[H_3O^+]
\\]
Because \\([H_3O^+]\\) is strictly greater than \\(1.0 \\times 10^{-7}\\text{ M}\\) at \\(25^\\circ\\text{C}\\), the \\(\\text{pH}\\) of any aqueous nitric acid solution must always be **strictly less than 7.0**:
\\[
\\text{pH} < 7.0
\\]

### 2. Physical Context & Practical Illustration:
Even in an extremely dilute solution (e.g., \\(10^{-8}\\text{ M } HNO_3\\)), water's self-ionisation ensures that the pH is \\(\\approx 6.98\\), remaining strictly below 7.0. It will universally turn blue litmus red.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. pH varies with concentration (\\(0.1\\text{ M } HNO_3\\) has pH 1, but \\(0.01\\text{ M}\\) has pH 2, and \\(0.001\\text{ M}\\) has pH 3).
- **Option B:** Incorrect. A pH of 7 represents pure neutral water.
- **Option C:** Correct. As an acid, its pH is universally less than 7.0 at \\(25^\\circ\\text{C}\\).
- **Option D:** Incorrect. A pH greater than 7 indicates an alkaline solution.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-052",
    text: "The effervescent household antacid formulation 'Eno' rapidly neutralises gastric acidity through the active reaction between:",
    options: [
      "Calcium carbonate and dilute nitric acid",
      "Magnesium oxide and concentrated sulphuric acid",
      "Sodium bicarbonate (\\(NaHCO_3\\)) and citric acid",
      "Potassium hydroxide and acetic acid"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Commercial effervescent antacids such as **Eno** consist of an anhydrous dry mixture of:
1. **Sodium bicarbonate** (\\(NaHCO_3\\), \\(\\approx 46\\%\\))
2. **Citric acid** (\\(C_6H_8O_7\\), \\(\\approx 44\\%\\))
3. **Anhydrous sodium carbonate** (\\(Na_2CO_3\\), \\(\\approx 8\\%\\))
In the dry powdered state, the solid reactants do not react. However, when stirred into a glass of water, the ions dissolve and undergo a brisk acid-base effervescence reaction:
\\[
3NaHCO_3(aq) + C_6H_8O_7(aq) \\longrightarrow Na_3C_6H_5O_7(aq) + 3H_2O(l) + 3CO_2(g)\\uparrow
\\]
The reaction produces soluble **sodium citrate** (a mild basic buffer) and copiously liberates carbon dioxide gas bubbles (brisk effervescence).

### 2. Physical Context & Practical Illustration:
When ingested, the alkaline sodium citrate and residual bicarbonate neutralise excess stomach hydrochloric acid:
\\[
NaHCO_3 + HCl \\longrightarrow NaCl + H_2O + CO_2\\uparrow
\\]
This rapidly elevates stomach pH back into the comfortable range of 3 to 4, relieving acid reflux and heartburn within seconds.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Nitric acid is toxic and corrosive; it is never used in antacids.
- **Option B:** Incorrect. Sulphuric acid is dangerous and caustic.
- **Option C:** Correct. Sodium bicarbonate and edible citric acid constitute the classic effervescent Eno antacid formula.
- **Option D:** Incorrect. Potassium hydroxide is caustic and not present in antacid drinks.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-053",
    text: "When dry pieces of blue and red litmus paper are dipped into an aqueous solution of acetic acid (\\(CH_3COOH\\)), what is observed?",
    options: [
      "Blue litmus turns red, and red litmus remains red",
      "Red litmus turns blue, and blue litmus remains blue",
      "Red litmus turns blue, and blue litmus turns red",
      "Only the blue litmus changes colour, turning green"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acetic acid (\\(CH_3COOH\\)) is a weak organic acid that dissociates in aqueous solution:
\\[
CH_3COOH(aq) + H_2O(l) \\rightleftharpoons CH_3COO^-(aq) + H_3O^+(aq)
\\]
For a typical \\(0.1\\text{ M}\\) acetic acid solution:
\\[
[H_3O^+] = \\sqrt{K_a \\cdot C} = \\sqrt{(1.8 \\times 10^{-5})(0.1)} \\approx 1.34 \\times 10^{-3}\\text{ mol/L}
\\]
\\[
\\text{pH} = -\\log_{10}(1.34 \\times 10^{-3}) \\approx 2.87
\\]
Because \\(\\text{pH} < 7.0\\):
1. **Blue litmus paper:** The blue conjugate base form of the indicator dye is protonated by hydronium ions into its red acid form; hence, **blue litmus turns red**.
2. **Red litmus paper:** The dye is already in its protonated red form; hence, **red litmus remains red**.

### 2. Physical Context & Practical Illustration:
This dual observation is characteristic of all acidic solutions: blue litmus changes to red, while red litmus demonstrates no colour change, serving as clear confirmation of an acidic medium.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Correct. Blue litmus turns red, and red litmus remains red in an acidic medium.
- **Option B:** Incorrect. Red litmus turns blue only in alkaline solutions.
- **Option C:** Incorrect. Red litmus does not turn blue in an acid.
- **Option D:** Incorrect. Blue litmus turns red, not green.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-054",
    text: "Which of the following chemical salts produces a strictly neutral solution (\\(\\text{pH} = 7.0\\)) when dissolved in pure water?",
    options: [
      "Sodium sulphate (\\(Na_2SO_4\\))",
      "Ammonium sulphate (\\((NH_4)_2SO_4\\))",
      "Aluminium chloride (\\(AlCl_3\\))",
      "Sodium carbonate (\\(Na_2CO_3\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The pH of a salt solution depends on whether its constituent ions undergo hydrolysis:
1. **Sodium sulphate (\\(Na_2SO_4\\)):** Formed by neutralisation of a strong base (\\(NaOH\\)) and a strong acid (\\(H_2SO_4\\)):
   \\[
   2NaOH + H_2SO_4 \\longrightarrow Na_2SO_4 + 2H_2O
   \\]
   Neither \\(Na^+\\) nor \\(SO_4^{2-}\\) hydrolyses in water. The solution remains neutral with **\\(\\text{pH} = 7.0\\)**.
2. **Ammonium sulphate (\\((NH_4)_2SO_4\\)):** Salt of a weak base (\\(NH_4OH\\)) and a strong acid (\\(H_2SO_4\\)); cation hydrolysis yields an **acidic** solution (\\(\\text{pH} < 7\\)):
   \\[
   NH_4^+ + H_2O \\rightleftharpoons NH_3 + H_3O^+
   \\]
3. **Aluminium chloride (\\(AlCl_3\\)):** Salt of a weak base and a strong acid; hydrolyses to yield an **acidic** solution (\\(\\text{pH} < 7\\)).
4. **Sodium carbonate (\\(Na_2CO_3\\)):** Salt of a strong base and a weak acid; anion hydrolysis yields a **basic** solution (\\(\\text{pH} > 7\\)).

### 2. Physical Context & Practical Illustration:
When dissolved in neutral water containing universal indicator, sodium sulphate retains a pure emerald green colour (pH 7), whereas ammonium sulphate turns yellow/orange and sodium carbonate turns blue/violet.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Sodium sulphate):** Correct. Salt of a strong acid and strong base; does not hydrolyse and remains neutral at pH 7.0.
- **Option B (Ammonium sulphate):** Incorrect. Hydrolyses to form an acidic solution.
- **Option C (Aluminium chloride):** Incorrect. Undergoes cationic hydrolysis to form an acidic solution.
- **Option D (Sodium carbonate):** Incorrect. Undergoes anionic hydrolysis to form an alkaline solution.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-055",
    text: "Why is natural tamarind pulp or lemon juice traditionally used to clean and polish tarnished brass and copper vessels?",
    options: [
      "The organic acid present dissolves the basic copper carbonate tarnish layer",
      "It acts as an alkaline soap to saponify atmospheric grease deposits",
      "It deposits a protective metallic electroplated layer on the vessel surface",
      "It functions as a mechanical abrasive powder without chemical reaction"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When brass (an alloy of copper and zinc) or copper utensils are exposed to moist atmospheric air, they undergo slow atmospheric corrosion. Copper reacts with atmospheric oxygen, moisture, and carbon dioxide to develop a dull greenish tarnish layer consisting of **basic copper carbonate** (verdigris):
\\[
2Cu(s) + H_2O(l) + CO_2(g) + O_2(g) \\longrightarrow \\mathbf{CuCO_3 \\cdot Cu(OH)_2(s)} \\quad (\\text{Green basic tarnish})
\\]
Being chemically basic, this tarnish layer is insoluble in plain water but reacts readily with dilute acids.
Tamarind pulp contains **tartaric acid** (\\(C_4H_6O_6\\)) and lemon juice contains **citric acid** (\\(C_6H_8O_7\\)). These organic acids neutralise and dissolve the basic copper carbonate and oxide layer, converting them into soluble copper citrate or tartrate complexes:
\\[
CuCO_3 \\cdot Cu(OH)_2(s) + 4H^+(aq) \\longrightarrow 2Cu^{2+}(aq) + 3H_2O(l) + CO_2(g)\\uparrow
\\]
Rinsing with water washes away the soluble salts, restoring the bright, shining metallic lustre of copper and brass.

### 2. Physical Context & Practical Illustration:
Rubbing half a lemon with a sprinkle of salt on an oxidized, dark brown brass lamp instantly clears the tarnish in seconds, revealing radiant golden metal beneath.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Correct. Tartaric and citric acids react with and dissolve the basic copper carbonate tarnish layer.
- **Option B:** Incorrect. Tamarind and lemon are acidic, not alkaline soaps.
- **Option C:** Incorrect. No new metallic layer is plated; existing surface tarnish is chemically stripped.
- **Option D:** Incorrect. The cleaning is driven by an acid-base neutralisation reaction, not merely mechanical abrasion.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-056",
    text: "Why can ordinary edible vegetable oil alone NOT be used as a practical agent for washing dirty clothes?",
    options: [
      "It reacts explosively with cold water",
      "It is too volatile and evaporates before cleaning can occur",
      "It bleaches coloured fabric dyes destructively",
      "It is non-polar, water-insoluble, and lacks the ionic hydrophilic heads needed to form cleansing micelles"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Cleansing of fabric requires an **amphiphilic surfactant** possessing two contrasting structural domains:
1. A **hydrophobic non-polar tail** that dissolves into grease, dirt, and oils.
2. A **hydrophilic ionic head** (such as \\(-\\text{COO}^- Na^+\\) in soap or \\(-\\text{SO}_3^- Na^+\\) in synthetic detergents) that forms strong ion-dipole interactions with polar water molecules.
In water, soap molecules orient into spherical **micelles** that encapsulate oily dirt droplets at their hydrophobic core while presenting their charged heads to the water, allowing the emulsion to be rinsed away.
In contrast, edible vegetable oils are non-polar triglycerides. They are completely insoluble in water and possess no ionic hydrophilic heads:
\\[
\\text{Vegetable Oil} + \\text{Water} \\longrightarrow \\text{Two separate immiscible phases}
\\]
Pouring oil onto soiled fabric would simply deposit more oily greasy stain without creating any emulsifying micellar action.

### 2. Physical Context & Practical Illustration:
To transform edible oil into a cleansing agent, it must undergo **saponification** by boiling with a strong alkali (\\(NaOH\\)), breaking the ester linkages to generate free sodium fatty acid salts (soap).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Vegetable oils are chemically unreactive with cold water.
- **Option B:** Incorrect. Vegetable oils are non-volatile and do not evaporate at room temperature.
- **Option C:** Incorrect. Edible oils do not bleach fabric dyes.
- **Option D:** Correct. Oils lack ionic hydrophilic groups and cannot form micelles to suspend and carry away dirt in water.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-057",
    text: "Which of the following metallic combinations does NOT form a true liquid or solid amalgam under standard conditions?",
    options: [
      "Mercury and Potassium",
      "Mercury and Platinum",
      "Mercury and Gold",
      "Mercury and Silver"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An **amalgam** is a specialized alloy formed by **mercury** (\\(Hg\\)) with one or more other metals:
- Mercury readily dissolves alkali metals (forming sodium amalgam \\(Na-Hg\\), a powerful reducing agent), gold (\\(Au-Hg\\), used in gold extraction), and silver (\\(Ag-Hg\\), dental amalgam).
However, a few transition metals resist amalgamation due to exceptionally high metallic cohesive bonding energy, refractory melting points, and unfavourable electronic structures:
- **Iron (\\(Fe\\))** and **Platinum (\\(Pt\\))** do not form amalgams with mercury under standard laboratory conditions.
Because iron does not amalgamate with mercury, liquid mercury is safely stored and transported commercially in heavy iron containers or flasks.

### 2. Physical Context & Practical Illustration:
In electrochemistry and organic syntheses, platinum electrodes can be immersed into mercury pools without dissolving or degrading, providing durable, inert electrical contacts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Mercury + Potassium):** Incorrect. Potassium dissolves exothermically in mercury to form potassium amalgam.
- **Option B (Mercury + Platinum):** Correct. Platinum does not readily form an amalgam with mercury under standard conditions.
- **Option C (Mercury + Gold):** Incorrect. Gold amalgamates with mercury very readily.
- **Option D (Mercury + Silver):** Incorrect. Silver forms dental amalgam alloys with mercury.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-058",
    text: "A building lightning conductor consists of sharp pointed metallic rods connected to a thick earthing strip. Which metal is predominantly used for this conductor?",
    options: [
      "Silver",
      "Copper",
      "Aluminium alloy",
      "Cast iron"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **lightning conductor** (invented by Benjamin Franklin) protects buildings from destructive atmospheric lightning strikes.
When a charged thundercloud passes overhead, it induces an opposite electrical charge on the earth. The pointed spikes on the roof concentrate the electric field (corona discharge), ionizing the air and safely routing the massive surge current directly to the earth.
The connecting down-conductor requires:
1. **High Electrical Conductivity:** To minimize Joule heating (\\(P = I^2 R\\)) caused by discharge currents exceeding \\(20,000\\text{ to } 100,000\\text{ amperes}\\).
2. **High Thermal Melting Point and Heat Capacity:** To prevent the conductor from vaporizing.
3. **Corrosion Resistance:** To withstand outdoor weathering over decades.
**Copper** possesses the second highest electrical conductivity of all metals (\\(\\sigma \\approx 5.96 \\times 10^7\\text{ S/m}\\), just behind silver), while being vastly more economical than silver and far more ductile and corrosion-resistant than iron.

### 2. Physical Context & Practical Illustration:
A heavy copper strip runs unbroken down the exterior wall of tall buildings to a buried copper earthing plate surrounded by charcoal and salt, ensuring an ultra-low ground impedance path (\\(< 10\\ \\Omega\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Silver):** Incorrect. Silver is too costly for large-scale architectural grounding strips.
- **Option B (Copper):** Correct. Copper is the standard engineering metal for lightning conductors and ground strips.
- **Option C (Aluminium):** Incorrect. Aluminium has lower conductivity and corrodes rapidly in contact with mortar and soil.
- **Option D (Cast iron):** Incorrect. Cast iron has much higher electrical resistance and would shatter or melt during intense strikes.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-059",
    text: "Which of the following chemical element-name pairs correctly reflects the historical Latin name from which its chemical symbol is derived?",
    options: [
      "Silver — Aurum",
      "Tin — Wolfram",
      "Tungsten — Stannum",
      "Lead — Plumbum"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In chemical nomenclature standardized by J. J. Berzelius, several elemental symbols are derived from classical Latin names:
- **Lead (\\(Pb\\)):** Derived from Latin **Plumbum** (meaning liquid metal/pipe metal; hence 'plumbing').
- **Silver (\\(Ag\\)):** Derived from Latin **Argentum** (not Aurum).
- **Gold (\\(Au\\)):** Derived from Latin **Aurum** (meaning shining dawn).
- **Tin (\\(Sn\\)):** Derived from Latin **Stannum** (not Wolfram).
- **Tungsten (\\(W\\)):** Derived from German **Wolfram** (from the mineral wolframite; not Stannum).
- **Iron (\\(Fe\\)):** Derived from Latin **Ferrum**.
- **Copper (\\(Cu\\)):** Derived from Latin **Cuprum**.
- **Sodium (\\(Na\\)):** Derived from Neo-Latin **Natrium**.
- **Potassium (\\(K\\)):** Derived from Neo-Latin **Kalium**.

### 2. Physical Context & Practical Illustration:
The symbol \\(Pb\\) for lead is found universally on chemical reagent bottles, storage battery labels, and the periodic table, tracing directly back to ancient Roman lead piping (plumbum).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Aurum is the Latin root for Gold (\\(Au\\)), whereas Silver is Argentum (\\(Ag\\)).
- **Option B:** Incorrect. Wolfram is the source of Tungsten (\\(W\\)), whereas Tin is Stannum (\\(Sn\\)).
- **Option C:** Incorrect. Stannum is the Latin root for Tin (\\(Sn\\)), not Tungsten.
- **Option D:** Correct. Lead derives its symbol \\(Pb\\) from the Latin name Plumbum.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-060",
    text: "Which of the following statements is scientifically accurate regarding 22-carat jewelry gold?",
    options: [
      "It is an amalgam formed by dissolving gold in liquid mercury",
      "It is a coarse heterogeneous suspension of solid copper flakes in gold",
      "It is a stoichiometric chemical compound with formula \\(Au_{22}Cu_2\\)",
      "It is a solid homogeneous solution (alloy) composed of approximately 91.6% gold with copper or silver"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The purity of gold is quantified on the **carat scale**, where pure gold is defined as **24 carats** (\\(100\\%\\) gold by mass).
For 22-carat gold:
\\[
\\text{Purity} = \\frac{22}{24} \\times 100\\% = 91.67\\% \\approx 91.6\\% \\text{ pure gold by mass}
\\]
The remaining \\(8.33\\%\\) consists of alloying metals, typically **copper (\\(Cu\\))** or **silver (\\(Ag\\))** or a blend of both.
Pure 24-carat gold is exceptionally soft, malleable, and ductile; jewelry crafted from pure gold easily deforms, scratches, and wears away.
Alloying gold with copper or silver forms a **substitutional solid solution (homogeneous alloy)**: copper atoms fit into the face-centred cubic lattice of gold, distorting the planes and impeding dislocation glide. This confers substantial mechanical hardness and tensile strength while preserving lustrous beauty.

### 2. Physical Context & Practical Illustration:
Hallmarked 22-carat gold jewelry is stamped with the international fineness mark **916** (signifying 916 parts per thousand pure gold).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Amalgams are alloys of mercury; 22-carat gold contains zero mercury.
- **Option B:** Incorrect. It is not a heterogeneous suspension; the metals are melted together and freeze into a uniform solid solution.
- **Option C:** Incorrect. Alloys are non-stoichiometric homogeneous mixtures, not fixed chemical compounds.
- **Option D:** Correct. 22-carat gold is a homogeneous solid solution (alloy) containing 91.6% gold combined with copper or silver.`
  }
];

module.exports = { ch5_part2 };
