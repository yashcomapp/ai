// Chapter 5 (Acids, Bases and Salts) - Part 4: MH-9-SCIT-5-5.1 (Q91 to Q122, 32 Questions)
// Gold Standard 3-Part Solutions, Valid KaTeX, Zero Distractor Defects

const ch5_part4 = [
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-091",
    text: "Which specific chemical mixture of concentrated mineral acids in definite volumetric proportions is known as aqua regia?",
    options: [
      "Concentrated \\(HCl\\) and concentrated \\(H_2SO_4\\) in a 3:1 ratio",
      "Concentrated \\(HCl\\) and concentrated \\(HNO_3\\) in a 3:1 ratio by volume",
      "Concentrated \\(HNO_3\\) and concentrated \\(H_2SO_4\\) in a 1:1 ratio",
      "Dilute \\(HCl\\) and dilute \\(CH_3COOH\\) in a 2:1 ratio"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Aqua regia** (Latin for 'royal water') is an intensely corrosive, fuming yellow-orange liquid prepared by mixing:
\\[
\\mathbf{3 \\text{ volumes of concentrated } HCl (37\\%) : 1 \\text{ volume of concentrated } HNO_3 (68\\%)}
\\]
Neither acid alone can dissolve noble metals such as gold (\\(Au\\)) or platinum (\\(Pt\\)), but their mixture produces active reagents through a redox reaction:
\\[
HNO_3(aq) + 3HCl(aq) \\longrightarrow NOCl(g) + Cl_2(g) + 2H_2O(l)
\\]
Nitrosyl chloride (\\(NOCl\\)) and nascent chlorine attack noble metals, while high chloride ion concentration coordinates with oxidized metal ions to form exceptionally stable soluble complexes (such as chlorauric acid, \\(HAuCl_4\\)):
\\[
Au(s) + 3HNO_3(aq) + 4HCl(aq) \\longrightarrow HAuCl_4(aq) + 3NO_2(g) + 3H_2O(l)
\\]

### 2. Physical Context & Practical Illustration:
Aqua regia must be prepared fresh immediately prior to use because volatile nitrosyl chloride and chlorine gas gradually evolve, causing the mixture to lose its dissolution potency. It is widely used in precious metal refining and etching microelectronics circuits.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Hydrochloric acid and sulphuric acid do not produce nascent oxidising chlorine species.
- **Option B:** Correct. Aqua regia is a 3:1 volumetric mixture of concentrated \\(HCl\\) and concentrated \\(HNO_3\\).
- **Option C:** Incorrect. A 1:1 mixture of \\(HNO_3\\) and \\(H_2SO_4\\) is nitrating mixture, used in organic synthesis.
- **Option D:** Incorrect. Acetic acid is too weak to dissolve noble metals.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-092",
    text: "Which of the following room-temperature liquids has the highest physical density?",
    options: [
      "Glycerin (glycerol)",
      "Kerosene oil",
      "Turpentine oil",
      "Mercury"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Physical density (\\(\\rho\\)) is the mass of a substance per unit volume (\\(\\rho = \\frac{m}{V}\\)).
Let us compare the densities of the listed liquids at \\(20^\\circ\\text{C}\\):
1. **Kerosene oil:** \\(\\rho \\approx 0.80\\text{ g/cm}^3\\) (\\(800\\text{ kg/m}^3\\))
2. **Turpentine oil:** \\(\\rho \\approx 0.87\\text{ g/cm}^3\\) (\\(870\\text{ kg/m}^3\\))
3. **Glycerin:** \\(\\rho \\approx 1.26\\text{ g/cm}^3\\) (\\(1260\\text{ kg/m}^3\\))
4. **Mercury (\\(Hg\\)):** \\(\\rho \\approx 13.55\\text{ g/cm}^3\\) (\\(13,550\\text{ kg/m}^3\\))
Mercury is a dense transition metal whose heavy atomic nucleus (atomic mass \\(200.59\\text{ u}\\)) and relativistic electron contraction result in exceptionally tight atomic packing, conferring a density more than 10 times greater than glycerin and 13.6 times greater than water.

### 2. Physical Context & Practical Illustration:
Because of its extreme density, a heavy solid iron cannonball (density \\(7.87\\text{ g/cm}^3\\)) floats effortlessly on the surface of liquid mercury, submerging only slightly past its midpoint.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Glycerin):** Incorrect. Glycerin is viscous but has a density of only \\(1.26\\text{ g/cm}^3\\).
- **Option B (Kerosene):** Incorrect. Kerosene is lighter than water (\\(0.80\\text{ g/cm}^3\\)).
- **Option C (Turpentine):** Incorrect. Turpentine has a density of \\(0.87\\text{ g/cm}^3\\).
- **Option D (Mercury):** Correct. Mercury has the highest density (\\(13.55\\text{ g/cm}^3\\)) among all room-temperature liquids.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-093",
    text: "Which atmospheric pollutant gas reacts with polished silver ornaments, causing them to turn black over time?",
    options: [
      "Carbon dioxide (\\(CO_2\\))",
      "Hydrogen sulphide (\\(H_2S\\))",
      "Ammonia gas (\\(NH_3\\))",
      "Pure nitrogen gas (\\(N_2\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Silver (\\(Ag\\)) is a noble metal with a high positive standard reduction potential (\\(E^\\circ = +0.80\\text{ V}\\)). It does not react with atmospheric oxygen or moisture under normal conditions.
However, traces of **hydrogen sulphide gas** (\\(H_2S\\)) present in air (from sewage decomposition, vehicular exhaust, and burning fossil fuels) react with metallic silver in the presence of atmospheric oxygen via corrosion:
\\[
4Ag(s) + 2H_2S(g) + O_2(g) \\longrightarrow 2\\mathbf{Ag_2S(s)} + 2H_2O(l)
\\]
The product formed is **silver sulphide** (\\(Ag_2S\\)), an insoluble black crystalline compound. The formation of this thin surface layer of \\(Ag_2S\\) is termed the **tarnishing of silver**.

### 2. Physical Context & Practical Illustration:
Tarnished silver ornaments can be restored without losing silver mass by electrochemical reduction: placing the tarnished article in a warm sodium bicarbonate solution inside an aluminium pan causes aluminium (more electropositive) to reduce silver sulphide back to metallic silver:
\\[
3Ag_2S(s) + 2Al(s) + 6OH^-(aq) \\longrightarrow 6Ag(s) + Al_2S_3(s) + 6OH^-
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(CO_2\\)):** Incorrect. Carbon dioxide does not react with silver.
- **Option B (\\(H_2S\\)):** Correct. Hydrogen sulphide gas reacts with silver to produce black silver sulphide tarnish.
- **Option C (\\(NH_3\\)):** Incorrect. Ammonia forms soluble complexes with silver ions but does not tarnish elemental silver black.
- **Option D (\\(N_2\\)):** Incorrect. Molecular nitrogen is chemically inert.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-094",
    text: "Which of the following chemical elements is the ODD ONE OUT based on metallic versus non-metallic character?",
    options: [
      "Copper (\\(Cu\\))",
      "Sodium (\\(Na\\))",
      "Gold (\\(Au\\))",
      "Bromine (\\(Br\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Elements are fundamentally classified based on electronic configuration, electronegativity, and physical-chemical properties into metals and non-metals:
1. **Copper (\\(Cu\\)):** A transition metal (Group 11); lustrous, malleable, ductile, excellent conductor of heat and electricity.
2. **Sodium (\\(Na\\)):** An alkali metal (Group 1); electropositive, metallic luster, forms basic oxides and ionic cations (\\(Na^+\\)).
3. **Gold (\\(Au\\)):** A noble transition metal (Group 11); highly malleable and metallic.
4. **Bromine (\\(Br\\)):** A halogen (Group 17, non-metal). It has a high electronegativity (\\(\\chi = 2.96\\)), exists as diatomic covalent molecules (\\(Br_2\\)), forms acidic oxides, and is the only non-metallic element that is a liquid at room temperature.
Because copper, sodium, and gold are true metals while bromine is a non-metal, bromine is the distinct odd element.

### 2. Physical Context & Practical Illustration:
Bromine forms a reddish-brown, volatile, corrosive liquid that conducts no electric current in its pure state, contrasting starkly with the electrical conductivity and metallic bonding of \\(Cu\\), \\(Na\\), and \\(Au\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Cu):** Incorrect choice (copper is a metal).
- **Option B (Na):** Incorrect choice (sodium is a metal).
- **Option C (Au):** Incorrect choice (gold is a metal).
- **Option D (Br):** Correct. Bromine is a non-metal halogen, whereas the other three are metals.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-095",
    text: "Which noble gas is filled in low-pressure electrical discharge lamps to produce a characteristic brilliant reddish-orange glow for advertising signs?",
    options: [
      "Argon",
      "Neon",
      "Helium",
      "Radon"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In an electrical discharge tube containing low-pressure gas, an applied high potential difference accelerates electrons. Inelastic collisions between free electrons and neutral gas atoms excite bound electrons to higher quantum energy states.
Upon spontaneous de-excitation back to lower orbitals, photons are emitted with discrete energies matching atomic spectral transitions (\\(\\Delta E = h\\nu = \\frac{hc}{\\lambda}\\)):
- **Neon (\\(Ne\\)):** Possesses intense atomic emission lines densely clustered in the red and orange regions of the visible spectrum (predominantly between \\(585\\text{ nm}\\) and \\(650\\text{ nm}\\)), producing an intense, vivid **reddish-orange glow**.
- **Argon (\\(Ar\\)):** Emits pale violet-blue light (used with mercury vapour in fluorescent tubes).
- **Helium (\\(He\\)):** Emits pale yellow-white light.
- **Radon (\\(Rn\\)):** Intensely radioactive noble gas, never used in lighting.

### 2. Physical Context & Practical Illustration:
Neon lighting (invented by Georges Claude in 1910) revolutionized nighttime commercial advertising worldwide. Because neon light penetrates fog effectively, neon beacons are also utilized in maritime and aviation lighthouses.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Argon):** Incorrect. Argon produces a pale blue-violet glow.
- **Option B (Neon):** Correct. Neon gas emits the iconic reddish-orange glow used in neon advertising signs.
- **Option C (Helium):** Incorrect. Helium produces a soft yellow-white discharge.
- **Option D (Radon):** Incorrect. Radon is hazardous, radioactive, and not used in commercial lamps.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-096",
    text: "Which electropositive metal is applied as a protective sacrificial barrier coating in the process of galvanizing iron or steel?",
    options: [
      "Copper (\\(Cu\\))",
      "Magnesium (\\(Mg\\))",
      "Aluminium (\\(Al\\))",
      "Zinc (\\(Zn\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Galvanization** is the metallurgical process of coating iron or steel with a thin protective layer of **zinc** (\\(Zn\\)), typically by hot-dip immersion in molten zinc at \\(\\approx 450^\\circ\\text{C}\\).
Zinc protects iron through two distinct mechanisms:
1. **Barrier Protection:** Zinc reacts with atmospheric oxygen and carbon dioxide to form an insoluble, adhering patina of basic zinc carbonate (\\(ZnCO_3 \\cdot 3Zn(OH)_2\\)), sealing the iron surface from moisture.
2. **Sacrificial (Cathodic) Protection:** Zinc is more electropositive than iron in the electrochemical reactivity series:
   \\[
   E^\\circ_{Zn^{2+}/Zn} = -0.76\\text{ V} \\quad \\text{vs.} \\quad E^\\circ_{Fe^{2+}/Fe} = -0.44\\text{ V}
   \\]
   Even if the coating is deeply scratched or cracked, zinc acts as the sacrificial anode and corrodes preferentially:
   \\[
   Zn(s) \\longrightarrow Zn^{2+}(aq) + 2e^-
   \\]
   The released electrons flow to the exposed iron, forcing it to act as the cathode where iron oxidation is prevented.

### 2. Physical Context & Practical Illustration:
Galvanized iron (GI) sheets are universally employed for roofing, outdoor water pipes, barbed wire, and automobile undercarriages. If tin were used instead (tin-plating), scratching the coating would accelerate iron rusting because iron is more active than tin.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Copper):** Incorrect. Copper is less active than iron (\\(E^\\circ = +0.34\\text{ V}\\)); scratching copper-coated iron would accelerate iron corrosion.
- **Option B (Magnesium):** Incorrect. Magnesium is too reactive and depletes rapidly.
- **Option C (Aluminium):** Incorrect. Aluminium coatings are applied in aluminizing, but galvanizing specifically refers to zinc.
- **Option D (Zinc):** Correct. Zinc is the definitive metal used in galvanizing iron.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-097",
    text: "When red-hot metals such as iron or magnesium react with steam (water vapour at elevated temperatures), which products are formed?",
    options: [
      "Metal oxide and hydrogen gas (\\(H_2\\))",
      "Metal oxide and oxygen gas (\\(O_2\\))",
      "Metal hydroxide and oxygen gas (\\(O_2\\))",
      "Metal hydride and ozone gas"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The reaction between metals and water depends critically on the metal's reactivity and the temperature of the water:
1. **Cold Water:** Highly reactive alkali metals (\\(Na, K\\)) and alkaline earth metals (\\(Ca\\)) react vigorously with cold water to form **metal hydroxides** and hydrogen gas:
   \\[
   2Na(s) + 2H_2O(l) \\longrightarrow 2NaOH(aq) + H_2(g)\\uparrow
   \\]
2. **Steam (High Temperature):** Moderately active metals such as magnesium, zinc, and red-hot iron do not react with cold water, but react vigorously with **steam**:
   - Magnesium burns in steam to form white magnesium oxide:
     \\[
     Mg(s) + H_2O(g) \\longrightarrow MgO(s) + H_2(g)\\uparrow
     \\]
   - Red-hot iron reacts reversibly with steam to form magnetic iron oxide (triferric tetroxide) and hydrogen gas:
     \\[
     3Fe(s) + 4H_2O(g) \\rightleftharpoons Fe_3O_4(s) + 4H_2(g)\\uparrow
     \\]
At these elevated temperatures, metal hydroxides thermally decompose into **metal oxides** and water; thus, the reaction with steam yields the **metal oxide and hydrogen gas**.

### 2. Physical Context & Practical Illustration:
Passing steam over red-hot iron filings in a combustion tube is the historical Lane process utilized industrially to manufacture pure hydrogen gas.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Correct. Reaction of heated metals with steam yields the metal oxide and hydrogen gas.
- **Option B:** Incorrect. Oxygen gas is never liberated; hydrogen is displaced from water.
- **Option C:** Incorrect. Hydroxides decompose at high steam temperatures into oxides.
- **Option D:** Incorrect. Metal hydrides are unstable at steam temperatures and ozone is not formed.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-098",
    text: "From which of the following natural phosphate minerals is elemental phosphorus commercially extracted?",
    options: [
      "Phosphorite rock (calcium phosphate)",
      "Cryolite mineral",
      "Cinnabar mineral",
      "Bauxite mineral"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Elemental phosphorus (\\(P_4\\)) is extracted commercially from **phosphorite rock** (also called rock phosphate), whose primary constituent is **calcium phosphate**, \\(Ca_3(PO_4)_2\\) (often occurring as apatite minerals, \\(Ca_5(PO_4)_3(F,Cl,OH)\\)).
In the industrial electrothermal process, crushed phosphorite rock is blended with silica sand (\\(SiO_2\\)) and coke (\\(C\\)) and heated in an electric arc furnace to approximately **\\(1400^\\circ\\text{C} - 1500^\\circ\\text{C}\\)**:
1. Silica displaces volatile phosphorus pentoxide from calcium phosphate, forming fusible calcium silicate slag:
   \\[
   2Ca_3(PO_4)_2(s) + 6SiO_2(s) \\longrightarrow 6CaSiO_3(l) + P_4O_{10}(g)
   \\]
2. Coke reduces the phosphorus pentoxide to elemental white phosphorus vapour:
   \\[
   P_4O_{10}(g) + 10C(s) \\longrightarrow P_4(g)\\uparrow + 10CO(g)
   \\]
Overall reaction:
\\[
2Ca_3(PO_4)_2 + 6SiO_2 + 10C \\longrightarrow 6CaSiO_3 + 10CO + P_4
\\]
The escaping phosphorus vapour is condensed under cold water as white/yellow phosphorus.

### 2. Physical Context & Practical Illustration:
Phosphorus extracted from phosphorite is the cornerstone of the modern agricultural fertilizer industry (superphosphates), safety match manufacture, and synthetic detergent builders.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Phosphorite):** Correct. Phosphorite rock (\\(Ca_3(PO_4)_2\\)) is the commercial mineral source of phosphorus.
- **Option B (Cryolite):** Incorrect. Cryolite (\\(Na_3AlF_6\\)) is an ore of aluminium.
- **Option C (Cinnabar):** Incorrect. Cinnabar (\\(HgS\\)) is the ore of mercury.
- **Option D (Bauxite):** Incorrect. Bauxite is the principal ore of aluminium.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-099",
    text: "Which of the following metals is strongly ferromagnetic and strongly attracted by an external magnetic field?",
    options: [
      "Aluminium",
      "Iron",
      "Copper",
      "Bismuth"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Materials are classified magnetically according to their response to an external magnetic field (\\(B\\)):
1. **Diamagnetic Materials (Copper, Bismuth):** Possess paired electrons with zero net permanent atomic dipole moment. When placed in a magnetic field, an opposing magnetic dipole is induced (Lenz's law), causing them to be **weakly repelled** by magnets (magnetic susceptibility \\(\\chi_m < 0\\)). Bismuth is one of the strongest diamagnetic elements.
2. **Paramagnetic Materials (Aluminium):** Possess unpaired electrons; weakly attracted by magnetic fields (\\(\\chi_m > 0\\), small).
3. **Ferromagnetic Materials (Iron, Cobalt, Nickel):** Possess permanent atomic magnetic dipole moments that spontaneously align parallel within microscopic macroscopic regions called **magnetic domains** through quantum exchange coupling. When exposed to an external field, domain walls shift and align, causing the metal to be **powerfully attracted** to the magnet (\\(\\chi_m \\gg 1\\), typically thousands of units).
Thus, iron is strongly attracted, rather than repelled, by a magnetic field.

### 2. Physical Context & Practical Illustration:
A permanent bar magnet readily picks up iron paper clips, nails, and steel keys with strong tactile force. Conversely, a diamagnetic metal like copper or bismuth experiences a very minute repulsive force detectable only with sensitive laboratory torsion balances.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Aluminium):** Incorrect. Aluminium is weakly paramagnetic.
- **Option B (Iron):** Correct. Iron is strongly ferromagnetic and vigorously attracted by magnetic fields.
- **Option C (Copper):** Incorrect. Copper is diamagnetic and weakly repelled by magnetic fields.
- **Option D (Bismuth):** Incorrect. Bismuth is famously diamagnetic and distinctly repelled by strong magnetic fields.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-100",
    text: "Which non-metallic element occurs as bright yellow rhombic crystals near volcanic vents and is widely used in manufacturing drugs, gunpowder, and vulcanised rubber?",
    options: [
      "Sulphur (\\(S_8\\))",
      "Yellow phosphorus (\\(P_4\\))",
      "Silicon (\\(Si\\))",
      "Graphite (\\(C\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Sulphur** (symbol \\(S\\), atomic number 16) is a non-metallic element in Group 16 (chalcogens).
It occurs in nature in both the free native state and combined states:
- Near volcanic fumaroles, hot springs, and volcanic craters, hot subterranean hydrogen sulphide and sulphur dioxide gases interact to deposit pure elemental sulphur as bright yellow crystals:
\\[
2H_2S(g) + SO_2(g) \\longrightarrow 3S(s) + 2H_2O(g)
\\]
Under ambient conditions, the stable allotrope is **rhombic sulphur** (\\(\\alpha\\)-sulphur), which forms large, transparent yellow bipyramidal crystals consisting of puckered crown-shaped octatomic rings (\\(S_8\\)).

### 2. Physical Context & Practical Illustration:
Major industrial and commercial applications of sulphur include:
1. **Vulcanisation of Rubber:** Heating natural rubber with \\(1\\%\\) to \\(3\\%\\) sulphur creates cross-linking disulphide bridges (\\(-S-S-\\)) between polyisoprene chains, transforming soft, sticky rubber into tough, elastic tyre rubber.
2. **Black Gunpowder:** A classic pyrotechnic mixture of potassium nitrate (\\(75\\%\\)), charcoal (\\(15\\%\\)), and sulphur (\\(10\\%\\)).
3. **Medicines:** Sulpha drugs, antiseptic ointments for skin disorders (dermatology).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Sulphur):** Correct. Sulphur forms yellow volcanic crystals and is used in vulcanisation, gunpowder, and pharmaceuticals.
- **Option B (Yellow phosphorus):** Incorrect. Yellow phosphorus is waxy, translucent, ignites spontaneously in air, and does not form volcanic crystals.
- **Option C (Silicon):** Incorrect. Silicon is a lustrous grey metalloid.
- **Option D (Graphite):** Incorrect. Graphite is an opaque black allotrope of carbon.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-101",
    text: "Among the trivalent oxides of Group 15 elements, which of the following compounds exhibits the HIGHEST acidic character?",
    options: [
      "Antimony trioxide (\\(Sb_2O_3\\))",
      "Arsenic trioxide (\\(As_2O_3\\))",
      "Phosphorus trioxide (\\(P_2O_3\\))",
      "Bismuth trioxide (\\(Bi_2O_3\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the periodic table, the acid-base character of element oxides depends on the **electronegativity** of the central element and the ionic versus covalent nature of the element-oxygen bond:
- Moving down Group 15 (\\(N, P, As, Sb, Bi\\)), atomic radius increases, electronegativity decreases systematically:
\\[
P (2.19) > As (2.18) > Sb (2.05) > Bi (2.02)
\\]
As electropositive metallic character increases down the group, oxide behaviour shifts progressively from acidic to amphoteric to basic:
1. \\(N_2O_3\\) and **\\(P_2O_3\\) (\\(P_4O_6\\)):** Purely **strongly acidic oxides**. When dissolved in water, \\(P_2O_3\\) readily forms phosphorous acid:
   \\[
   P_4O_6(s) + 6H_2O(l) \\longrightarrow 4H_3PO_3(aq) \\quad (\\text{Acidic, turns blue litmus red})
   \\]
2. \\(As_2O_3\\) and \\(Sb_2O_3\\): **Amphoteric oxides** (react with both acids and alkalis).
3. \\(Bi_2O_3\\): Predominantly **basic oxide**.
Therefore, **\\(P_2O_3\\)** is the most acidic oxide among the choices.

### 2. Physical Context & Practical Illustration:
Phosphorus trioxide reacts vigorously with alkalis to form phosphite salts, whereas bismuth trioxide reacts with strong acids to yield bismuth cations, directly reflecting the non-metal to metal transition down the group.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(Sb_2O_3\\)):** Incorrect. Antimony trioxide is amphoteric.
- **Option B (\\(As_2O_3\\)):** Incorrect. Arsenic trioxide is weakly acidic/amphoteric, less acidic than \\(P_2O_3\\).
- **Option C (\\(P_2O_3\\)):** Correct. Phosphorus trioxide is a purely non-metallic, strongly acidic oxide.
- **Option D (\\(Bi_2O_3\\)):** Incorrect. Bismuth trioxide is basic.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-102",
    text: "Which of the following mineral ores does NOT fit into the group of sulphide ores?",
    options: [
      "Galena (\\(PbS\\))",
      "Cinnabar (\\(HgS\\))",
      "Bauxite (\\(Al_2O_3 \\cdot 2H_2O\\))",
      "Zinc blende (\\(ZnS\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Mineral ores are classified according to the principal chemical anion radical combining with the metal:
1. **Sulphide Ores:** Contain sulphide anions (\\(S^{2-}\\)):
   - **Galena:** Lead(II) sulphide (\\(PbS\\))
   - **Cinnabar:** Mercury(II) sulphide (\\(HgS\\))
   - **Zinc blende / Sphalerite:** Zinc sulphide (\\(ZnS\\))
   - Iron pyrites (\\(FeS_2\\)), Copper pyrites (\\(CuFeS_2\\))
   All sulphide ores are concentrated by the froth flotation process and roasted in air to convert them into oxides before reduction.
2. **Oxide Ores:** Contain oxide or hydroxide anions:
   - **Bauxite:** Hydrated aluminium oxide (\\(Al_2O_3 \\cdot 2H_2O\\))
Because Bauxite is an **oxide ore** while Galena, Cinnabar, and Zinc blende are all **sulphide ores**, Bauxite does not fit into the group.

### 2. Physical Context & Practical Illustration:
Sulphide ores release polluting sulphur dioxide gas (\\(SO_2\\)) during metallurgical roasting in smelters, whereas oxide ores like bauxite are purified by chemical leaching (Bayer process) without generating sulphur emissions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Galena):** Incorrect choice (galena is a sulphide ore, \\(PbS\\)).
- **Option B (Cinnabar):** Incorrect choice (cinnabar is a sulphide ore, \\(HgS\\)).
- **Option C (Bauxite):** Correct. Bauxite is an oxide ore (\\(Al_2O_3 \\cdot 2H_2O\\)) and does not belong to the sulphide group.
- **Option D (Zinc blende):** Incorrect choice (zinc blende is a sulphide ore, \\(ZnS\\)).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-103",
    text: "In chemical nomenclature, chemical compounds containing the prefix 'Thio-' must contain which element replacing an oxygen atom?",
    options: [
      "Carbon (\\(C\\))",
      "Nitrogen (\\(N\\))",
      "Aluminium (\\(Al\\))",
      "Sulphur (\\(S\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In chemical terminology, the prefix **Thio-** is derived from the ancient Greek word *theion* (\\(\\theta\\epsilon\\tilde{\\iota}ov\\)), meaning **sulphur**.
In IUPAC and classical nomenclature, 'thio-' signifies that an **oxygen atom** in a chemical compound, functional group, or radical has been replaced by a **sulphur atom**:
1. **Thiosulphate ion (\\(S_2O_3^{2-}\\)):** Derived from the sulphate ion (\\(SO_4^{2-}\\)) by substituting one oxygen atom with a sulphur atom:
   \\[
   [SO_4]^{2-} \\xrightarrow{\\text{replace one } O \\text{ with } S} [S_2O_3]^{2-}
   \\]
2. **Thiocyanate ion (\\(SCN^-\\)):** Derived from cyanate (\\(OCN^-\\)).
3. **Thiol (Mercaptan, \\(R-SH\\)):** The sulphur analogue of an alcohol (\\(R-OH\\)).
4. **Thiourea (\\(SC(NH_2)_2\\)):** The sulphur analogue of urea (\\(OC(NH_2)_2\\)).
Therefore, any chemical entity bearing the prefix 'thio-' must contain **sulphur**.

### 2. Physical Context & Practical Illustration:
Sodium thiosulphate (\\(Na_2S_2O_3 \\cdot 5H_2O\\), photographic hypo) is universally used in film photography to dissolve unexposed silver halide crystals.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Carbon):** Incorrect. Carbon compounds do not take the 'thio-' prefix.
- **Option B (Nitrogen):** Incorrect. Nitrogen analogues are termed 'aza-' or 'amino-'.
- **Option C (Aluminium):** Incorrect. Aluminium has no relation to the thio- prefix.
- **Option D (Sulphur):** Correct. The prefix 'Thio-' specifically denotes the presence of sulphur replacing oxygen.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-104",
    text: "What is the primary technological role of adding 2% to 3% gypsum (\\(CaSO_4 \\cdot 2H_2O\\)) to clinker during cement manufacturing?",
    options: [
      "To increase the overall compressive strength of the cured concrete",
      "To accelerate the initial hydration rate so that concrete sets within 5 minutes",
      "To impart a dark grey colour to the Portland cement powder",
      "To retard the initial rate of setting, preventing premature flash setting"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Portland cement is manufactured by calcining limestone and clay into clinker, which is then pulverized. The clinker contains four major mineral phases:
- Tricalcium silicate (\\(C_3S\\))
- Dicalcium silicate (\\(C_2S\\))
- Tricalcium aluminate (\\(C_3A\\), \\(3CaO \\cdot Al_2O_3\\))
- Tetracalcium aluminoferrite (\\(C_4AF\\))
Tricalcium aluminate (\\(C_3A\\)) is exceptionally reactive with water. In the absence of gypsum, when water is added to cement, \\(C_3A\\) hydrates violently and exothermically, causing the paste to solidify uncontrollably within 2 to 5 minutes—a disastrous defect known as **flash setting**.
When **gypsum** (\\(CaSO_4 \\cdot 2H_2O\\), \\(2\\%\\text{ to } 3\\%\\)) is interground with clinker:
\\[
C_3A + 3(CaSO_4 \\cdot 2H_2O) + 26H_2O \\longrightarrow \\mathbf{C_3A \\cdot 3CaSO_4 \\cdot 32H_2O} \\quad (\\text{Ettringite crystals})
\\]
Gypsum rapidly dissolves to form a protective colloidal coating of ettringite needle crystals over the surface of \\(C_3A\\) grains, acting as a diffusion barrier. This dramatically **retards the initial setting time** to 30–45 minutes.

### 2. Physical Context & Practical Illustration:
This delayed setting provides construction masons with the vital working window needed to mix, transport, pour, vibrate, and screed fresh concrete into building formwork before it stiffens.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Ultimate compressive strength is provided by silicates (\\(C_3S\\) and \\(C_2S\\)), not gypsum.
- **Option B:** Incorrect. Accelerating setting would cause flash setting; gypsum does the exact opposite.
- **Option C:** Incorrect. Colour is determined by iron compounds, not white gypsum.
- **Option D:** Correct. Gypsum retards the hydration rate of tricalcium aluminate, preventing flash setting.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-105",
    text: "Which of the following chemical elements is classified as a true metalloid (semimetal)?",
    options: [
      "Bromine (\\(Br\\))",
      "Zinc (\\(Zn\\))",
      "Silicon (\\(Si\\))",
      "Potassium (\\(K\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Metalloids** (or semimetals) are chemical elements situated along the diagonal dividing line ('staircase') between metals and non-metals in the p-block of the Modern Periodic Table.
They exhibit intermediate physical and chemical properties:
- **Metals:** Electropositive, lustrous, high electrical conductivity that decreases with temperature.
- **Non-metals:** Electronegative, insulators, form acidic covalent oxides.
- **Metalloids:** Possess intermediate electronegativities (\\(\\approx 1.8 - 2.2\\)), form amphoteric or weakly acidic oxides, and act as intrinsic semiconductors:
\\[
\\text{Recognized Metalloids: } \\mathbf{B, \\, Si, \\, Ge, \\, As, \\, Sb, \\, Te}
\\]
**Silicon (\\(Si\\), atomic number 14):** Possesses a metallic grey sheen like a metal, but is brittle and acts as a covalent diamond-cubic semiconductor whose electrical conductivity increases with temperature (band gap \\(E_g = 1.12\\text{ eV}\\)).
In contrast, Bromine is a non-metal halogen, Zinc is a transition-related metal, and Potassium is an alkali metal.

### 2. Physical Context & Practical Illustration:
Because of its metalloid semiconductor bandgap, silicon is the foundational material of modern microelectronics, used to fabricate billions of transistors on microprocessors, computer memory chips, and solar photovoltaic cells.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Bromine):** Incorrect. Bromine is a non-metal halogen.
- **Option B (Zinc):** Incorrect. Zinc is a metallic transition element.
- **Option C (Silicon):** Correct. Silicon is the archetypal metalloid semimetal.
- **Option D (Potassium):** Incorrect. Potassium is a highly reactive alkali metal.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-106",
    text: "Which of the following naturally occurring minerals does NOT contain aluminium in its chemical composition?",
    options: [
      "Cinnabar",
      "Cryolite",
      "Potassium feldspar",
      "Bauxite"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us inspect the chemical formulas of each mineral:
1. **Cryolite:** Sodium hexafluoroaluminate, **\\(Na_3AlF_6\\)**. Contains aluminium (\\(Al\\)), sodium, and fluorine; used in aluminium smelting.
2. **Potassium Feldspar (Orthoclase):** An aluminosilicate rock mineral, **\\(KAlSi_3O_8\\)**. Contains aluminium.
3. **Bauxite:** Hydrated aluminium oxide, **\\(Al_2O_3 \\cdot 2H_2O\\)**. The principal commercial ore of aluminium.
4. **Cinnabar:** Mercury(II) sulphide, **\\(HgS\\)**. A dense, brilliant red mineral ore consisting solely of mercury (\\(Hg\\)) and sulphur (\\(S\\)).
Therefore, **Cinnabar contains zero aluminium**.

### 2. Physical Context & Practical Illustration:
Cinnabar is the historic mineral from which elemental mercury is extracted by roasting in air:
\\[
HgS(s) + O_2(g) \\xrightarrow{\\Delta} Hg(g) + SO_2(g)
\\]
Historically, crushed cinnabar was used as the red pigment vermilion in painting and cosmetic powders.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Cinnabar):** Correct. Cinnabar is mercury sulphide (\\(HgS\\)) and contains no aluminium.
- **Option B (Cryolite):** Incorrect. Cryolite is \\(Na_3AlF_6\\) and contains aluminium.
- **Option C (Feldspar):** Incorrect. Feldspar is \\(KAlSi_3O_8\\) and contains aluminium.
- **Option D (Bauxite):** Incorrect. Bauxite is \\(Al_2O_3 \\cdot 2H_2O\\) and contains aluminium.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-107",
    text: "What is the physical mechanical state of plastic sulphur at room temperature?",
    options: [
      "A free-flowing colloidal liquid",
      "A transparent Newtonian liquid",
      "An amorphous, rubbery solid that gradually hardens into rhombic crystals",
      "A permanent non-viscous gas"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Plastic sulphur** is an amorphous allotrope of sulphur.
It is prepared by heating crystalline rhombic sulphur until it boils (\\(\\approx 444^\\circ\\text{C}\\)) and pouring the viscous molten liquid in a thin stream into cold water:
1. At boiling temperature, the crown-shaped \\(S_8\\) rings rupture into open, diradical polymeric chains containing thousands of sulphur atoms (\\(-S-S_n-S-\\)).
2. Rapid quenching in cold water freezes these long polymeric chains before they have time to re-assemble into \\(S_8\\) rings.
The resulting material is **plastic sulphur**: a soft, dark amber, elastic, rubber-like **amorphous solid** that can be stretched like rubber.
Because it is thermodynamically metastable, upon standing at room temperature over several days, the long chains slowly break down and recrystallise into the stable yellow crystalline **rhombic sulphur** (\\(\\alpha\\)-sulphur).

### 2. Physical Context & Practical Illustration:
Plastic sulphur demonstrates how thermal quench rates alter polymeric entanglement: like quickly cooling heated vulcanized polymers, the frozen entangled sulfur chains allow macroscopic elastic deformation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. It is not a liquid suspension or sol.
- **Option B:** Incorrect. It does not flow as a liquid; it can be held and stretched by hand.
- **Option C:** Correct. Plastic sulphur is an amorphous, rubbery solid that slowly reverts to crystalline rhombic sulphur.
- **Option D:** Incorrect. Plastic sulphur is a condensed solid, not a gas.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-108",
    text: "Which poisonous chemical gas is instantly recognizable by its characteristic foul odour of rotten eggs?",
    options: [
      "Carbon monoxide (\\(CO\\))",
      "Sulphur dioxide (\\(SO_2\\))",
      "Hydrogen sulphide (\\(H_2S\\))",
      "Nitrogen dioxide (\\(NO_2\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Hydrogen sulphide** (chemical formula \\(H_2S\\)) is a colourless, flammable, extremely toxic hydride gas.
It possesses an unmistakable, pungent, offensive odour resembling **rotten eggs**.
This odour arises in nature because the anaerobic decomposition of sulfur-containing proteins (such as cysteine and methionine found in egg whites) by sulphate-reducing bacteria produces trace amounts of volatile hydrogen sulphide:
\\[
\\text{Organic sulfur proteins} \\xrightarrow{\\text{anaerobic bacteria}} H_2S(g)
\\]
In the laboratory, hydrogen sulphide is generated by the reaction between ferrous sulphide and dilute sulphuric acid in Kipp's apparatus:
\\[
FeS(s) + H_2SO_4(aq) \\longrightarrow FeSO_4(aq) + H_2S(g)\\uparrow
\\]

### 2. Physical Context & Practical Illustration:
Although the human nose can detect \\(H_2S\\) at concentrations as low as \\(0.0005\\text{ ppm}\\), at higher concentrations (> \\(100\\text{ ppm}\\)) it rapidly paralyses the olfactory nerve, eliminating the warning smell before causing fatal asphyxiation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(CO\\)):** Incorrect. Carbon monoxide is completely odourless and colourless.
- **Option B (\\(SO_2\\)):** Incorrect. Sulphur dioxide has a suffocating, choking odour of burning sulphur (matches).
- **Option C (\\(H_2S\\)):** Correct. Hydrogen sulphide gas is universally known for its foul rotten-egg odour.
- **Option D (\\(NO_2\\)):** Incorrect. Nitrogen dioxide has a biting, pungent, irritating odour and reddish-brown colour.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-109",
    text: "During the electrolysis of acidified water in a Hofmann voltameter, which gas is collected at the negative cathode in a 2:1 volume ratio compared to the anode?",
    options: [
      "Hydrogen gas (\\(H_2\\))",
      "Carbon dioxide gas (\\(CO_2\\))",
      "Oxygen gas (\\(O_2\\))",
      "Chlorine gas (\\(Cl_2\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Pure water is a poor conductor, so a small quantity of dilute sulphuric acid (\\(H_2SO_4\\)) is added to supply mobile ions.
When a direct electric current is passed through the Hofmann voltameter using platinum electrodes:
1. **At the Cathode (Negative Electrode):** Reduction of hydronium ions occurs, liberating **Hydrogen gas**:
   \\[
   4H^+(aq) + 4e^- \\longrightarrow 2\\mathbf{H_2(g)}\\uparrow
   \\]
2. **At the Anode (Positive Electrode):** Oxidation of water molecules occurs, liberating **Oxygen gas**:
   \\[
   2H_2O(l) \\longrightarrow \\mathbf{O_2(g)}\\uparrow + 4H^+(aq) + 4e^-
   \\]
Overall stoichiometric decomposition:
\\[
2H_2O(l) \\xrightarrow{\\text{electrical energy}} 2H_2(g) + O_2(g)
\\]
According to Avogadro's law, equal volumes of gases at identical temperature and pressure contain equal numbers of moles:
\\[
\\frac{\\text{Volume of } H_2}{\\text{Volume of } O_2} = \\frac{2\\text{ moles}}{1\\text{ mole}} = 2 : 1
\\]
Therefore, the gas collected above the negative cathode is **Hydrogen (\\(H_2\\))**, occupying exactly twice the volume of oxygen.

### 2. Physical Context & Practical Illustration:
Testing the gases confirms their identities:
- Bringing a burning splint to the cathode gas produces a flame that burns with a soft 'pop' sound (hydrogen).
- Bringing a glowing wooden ember to the anode gas causes it to reignite vigorously (oxygen supports combustion).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Hydrogen):** Correct. Hydrogen gas is liberated at the negative cathode in a 2:1 volumetric ratio.
- **Option B (Carbon dioxide):** Incorrect. No carbon is present in pure acidified water.
- **Option C (Oxygen):** Incorrect. Oxygen gas is evolved at the positive anode in half the volume.
- **Option D (Chlorine):** Incorrect. Acidified water contains sulphate, not chloride.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-110",
    text: "Which chemical element is the most abundant by mass in the Earth's crust?",
    options: [
      "Oxygen (\\(\\approx 46.6\\%\\))",
      "Silicon (\\(\\approx 27.7\\%\\))",
      "Aluminium (\\(\\approx 8.1\\%\\))",
      "Iron (\\(\\approx 5.0\\%\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The continental and oceanic Earth's crust is composed predominantly of silicate, aluminosilicate, and carbonate minerals.
The quantitative elemental abundance by mass in the Earth's crust is:
1. **Oxygen (\\(O\\)):** **\\(46.6\\%\\)** (most abundant overall)
2. **Silicon (\\(Si\\)):** **\\(27.7\\%\\)** (most abundant metalloid / second overall)
3. **Aluminium (\\(Al\\)):** **\\(8.1\\%\\)** (most abundant metallic element)
4. **Iron (\\(Fe\\)):** **\\(5.0\\%\\)** (second most abundant metal)
5. **Calcium (\\(Ca\\)):** \\(3.6\\%\\)
6. **Sodium (\\(Na\\)):** \\(2.8\\%\\)
7. **Potassium (\\(K\\)):** \\(2.6\\%\\)
8. **Magnesium (\\(Mg\\)):** \\(2.1\\%\\)
Together, Oxygen and Silicon account for almost three-quarters (\\(74.3\\%\\)) of the entire mass of the Earth's crust.
(Note: While Hydrogen is the most abundant element in the *universe*, Oxygen is the most abundant in the *Earth's crust*).

### 2. Physical Context & Practical Illustration:
Although elemental oxygen exists in the atmosphere as a gas (\\(21\\%\\) by volume), in the lithosphere it is chemically bound as oxide anions (\\(O^{2-}\\)) bonded to silicon, aluminium, and iron in rocks, clays, and sands.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Oxygen):** Correct. Oxygen is the most abundant element in the Earth's crust (46.6% by mass).
- **Option B (Silicon):** Incorrect. Silicon is second (27.7%).
- **Option C (Aluminium):** Incorrect. Aluminium is third overall (8.1%), though it is the most abundant metal.
- **Option D (Iron):** Incorrect. Iron is fourth (5.0%).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-110", // wait, let's check code for 111
    questionCode: "MH-9-SCIT-5-5.1-OSC-111",
    text: "Which constituent of Earth's atmospheric air demonstrates the greatest geographical and meteorological variation in percentage concentration?",
    options: [
      "Carbon dioxide gas (\\(CO_2\\))",
      "Nitrogen gas (\\(N_2\\))",
      "Water vapour (humidity)",
      "Argon gas"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The gases in dry air maintain remarkably constant volumetric proportions up to the stratopause:
- Nitrogen (\\(N_2\\)): \\(78.08\\%\\) (virtually constant)
- Oxygen (\\(O_2\\)): \\(20.95\\%\\) (virtually constant)
- Argon (\\(Ar\\)): \\(0.93\\%\\) (virtually constant)
- Carbon dioxide (\\(CO_2\\)): \\(\\approx 0.042\\%\\) (\\(420\\text{ ppm}\\), varies slightly by a few ppm).
In stark contrast, **water vapour (humidity)** is non-homogeneously distributed and varies dramatically:
- In extremely cold polar regions or high-altitude deserts: **less than \\(0.01\\%\\) (\\(< 100\\text{ ppm}\\))**.
- In hot, humid equatorial tropical rainforests: **up to \\(4.0\\% - 5.0\\%\\) by volume**.
This represents a variation spanning multiple orders of magnitude (a factor of over 400), governed dynamically by temperature and the Clausius-Clapeyron equation:
\\[
\\frac{d P_{\\text{sat}}}{d T} = \\frac{\\Delta H_{\\text{vap}}}{T \\Delta V}
\\]

### 2. Physical Context & Practical Illustration:
This dynamic variation in water vapour concentration drives all meteorological phenomena on Earth: cloud formation, monsoons, precipitation, fog, and the atmospheric greenhouse hydrological cycle.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(CO_2\\)):** Incorrect. Carbon dioxide varies only slightly across locations (around 0.04%).
- **Option B (\\(N_2\\)):** Incorrect. Nitrogen is constant at 78% globally.
- **Option C (Water vapour):** Correct. Water vapour varies massively from nearly 0% to over 4% of air volume.
- **Option D (Argon):** Incorrect. Argon is an inert noble gas with a constant atmospheric fraction (0.93%).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-112",
    text: "Which of the following chemical compounds does NOT decompose to yield oxygen gas upon simple thermal heating in a laboratory tube?",
    options: [
      "Potassium chlorate (\\(KClO_3\\))",
      "Potassium permanganate (\\(KMnO_4\\))",
      "Calcium carbonate (\\(CaCO_3\\))",
      "Mercury(II) oxide (\\(HgO\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the thermal decomposition reactions of each compound:
1. **Potassium chlorate (\\(KClO_3\\)):** Decomposes upon heating (especially with \\(MnO_2\\) catalyst) to liberate oxygen gas:
   \\[
   2KClO_3(s) \\xrightarrow{\\Delta} 2KCl(s) + 3\\mathbf{O_2(g)}\\uparrow
   \\]
2. **Potassium permanganate (\\(KMnO_4\\)):** Decomposes at \\(200^\\circ\\text{C}\\) to release oxygen:
   \\[
   2KMnO_4(s) \\xrightarrow{\\Delta} K_2MnO_4(s) + MnO_2(s) + \\mathbf{O_2(g)}\\uparrow
   \\]
3. **Mercury(II) oxide (\\(HgO\\)):** Undergoes thermal decomposition (Priestley's classic experiment):
   \\[
   2HgO(s) \\xrightarrow{\\Delta} 2Hg(l) + \\mathbf{O_2(g)}\\uparrow
   \\]
4. **Calcium carbonate (\\(CaCO_3\\)):** Calcines at \\(\\approx 900^\\circ\\text{C}\\) to release **carbon dioxide gas**, NOT oxygen:
   \\[
   CaCO_3(s) \\xrightarrow{\\Delta} CaO(s) + \\mathbf{CO_2(g)}\\uparrow
   \\]
Thus, calcium carbonate cannot yield oxygen gas upon simple heating.

### 2. Physical Context & Practical Illustration:
Heating a pinch of \\(KMnO_4\\) in a test tube rapidly reignites a glowing wooden splint held at the mouth due to evolved \\(O_2\\). In contrast, heating \\(CaCO_3\\) produces \\(CO_2\\), which immediately extinguishes any burning flame.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(KClO_3\\)):** Incorrect choice (yields \\(O_2\\) upon heating).
- **Option B (\\(KMnO_4\\)):** Incorrect choice (yields \\(O_2\\) upon heating).
- **Option C (\\(CaCO_3\\)):** Correct. Calcium carbonate decomposes to liberate carbon dioxide (\\(CO_2\\)), not oxygen gas.
- **Option D (\\(HgO\\)):** Incorrect choice (yields \\(O_2\\) upon heating).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-113",
    text: "Bright yellow octahedral (bipyramidal) crystals formed by the slow evaporation of a solution in carbon disulphide (\\(CS_2\\)) are characteristic of:",
    options: [
      "Rhombic sulphur (\\(\\alpha\\)-sulphur)",
      "Diamond allotrope of carbon",
      "Red phosphorus",
      "Metallic crystalline sodium"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Sulphur exhibits polymorphism, existing in two principal crystalline allotropic forms:
1. **Rhombic Sulphur (\\(\\alpha\\)-sulphur):** The thermodynamically stable allotrope of sulphur at temperatures below \\(95.6^\\circ\\text{C}\\) (\\(368.6\\text{ K}\\)).
   - It forms translucent, bright yellow **octahedral (bipyramidal)** crystals.
   - It is insoluble in polar water, but dissolves readily in non-polar **carbon disulphide** (\\(CS_2\\)).
   - When a saturated solution of roll sulphur in \\(CS_2\\) is allowed to evaporate slowly in a fume hood, perfect rhombic octahedral crystals are deposited:
   \\[
   S_8(\\text{solvated in } CS_2) \\xrightarrow{\\text{slow evaporation}} S_8(\\text{Rhombic octahedral crystals})
   \\]
2. **Monoclinic Sulphur (\\(\\beta\\)-sulphur):** Stable between \\(95.6^\\circ\\text{C}\\) and \\(119^\\circ\\text{C}\\); forms needle-shaped (acicular) crystals.

### 2. Physical Context & Practical Illustration:
The temperature \\(95.6^\\circ\\text{C}\\) is the **transition temperature** of sulphur. Below this temperature, monoclinic needles slowly transform into rhombic octahedra.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Rhombic sulphur):** Correct. Rhombic sulphur crystallises as bright yellow octahedra from carbon disulphide.
- **Option B (Diamond):** Incorrect. Diamond is colourless and insoluble in \\(CS_2\\).
- **Option C (Red phosphorus):** Incorrect. Red phosphorus is an amorphous or polymeric dark red powder.
- **Option D (Sodium):** Incorrect. Sodium is a soft metallic solid that reacts violently with moisture.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-114",
    text: "Which of the following natural mineral ores is the primary source for the extraction of Aluminium?",
    options: [
      "Galena (\\(PbS\\))",
      "Bauxite (\\(Al_2O_3 \\cdot 2H_2O\\))",
      "Chalcopyrite (\\(CuFeS_2\\))",
      "Haematite (\\(Fe_2O_3\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Bauxite** (hydrated aluminium oxide, \\(Al_2O_3 \\cdot 2H_2O\\)) is the principal commercial ore used worldwide for the metallurgical extraction of metallic aluminium.
The extraction process consists of two primary steps:
1. **Bayer's Process:** Bauxite ore is digested with concentrated sodium hydroxide at \\(150^\\circ\\text{C} - 200^\\circ\\text{C}\\) under pressure to extract soluble sodium aluminate while separating insoluble iron oxide impurities ('red mud'):
   \\[
   Al_2O_3 \\cdot 2H_2O(s) + 2NaOH(aq) \\longrightarrow 2NaAlO_2(aq) + 3H_2O(l)
   \\]
   The aluminate is hydrolysed and calcined to produce pure, dry alumina (\\(Al_2O_3\\)).
2. **Hall-Heroult Electrolytic Reduction:** Pure alumina is dissolved in molten cryolite (\\(Na_3AlF_6\\)) and fluorspar (\\(CaF_2\\)) to lower the melting point to \\(\\approx 950^\\circ\\text{C}\\), and electrolysed using carbon anodes:
   \\[
   2Al_2O_3(l) + 3C(s) \\longrightarrow 4Al(l) + 3CO_2(g)
   \\]

### 2. Physical Context & Practical Illustration:
Bauxite deposits are abundant in tropical regions (e.g., Odisha, Maharashtra, and Jharkhand in India). Extracting aluminium from bauxite powers modern aerospace and transportation engineering.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Galena):** Incorrect. Galena (\\(PbS\\)) is the principal ore of lead.
- **Option B (Bauxite):** Correct. Bauxite (\\(Al_2O_3 \\cdot 2H_2O\\)) is the principal ore of aluminium.
- **Option C (Chalcopyrite):** Incorrect. Chalcopyrite (\\(CuFeS_2\\)) is an ore of copper.
- **Option D (Haematite):** Incorrect. Haematite (\\(Fe_2O_3\\)) is the principal ore of iron.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-115",
    text: "Solder, the fusible low-melting alloy used to join electronic components and electrical wiring, is composed of which two metals?",
    options: [
      "Tin and lead (\\(Sn\\) and \\(Pb\\))",
      "Copper and zinc (\\(Cu\\) and \\(Zn\\))",
      "Lead and iron (\\(Pb\\) and \\(Fe\\))",
      "Aluminium and magnesium (\\(Al\\) and \\(Mg\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Soft solder** is an alloy composed of **tin (\\(Sn\\))** and **lead (\\(Pb\\))** (typically in a \\(60\\%\\, Sn : 40\\%\\, Pb\\) or eutectic \\(63\\%\\, Sn : 37\\%\\, Pb\\) ratio).
- Melting point of pure lead: \\(327.5^\\circ\\text{C}\\)
- Melting point of pure tin: \\(231.9^\\circ\\text{C}\\)
- Melting point of eutectic solder (\\(63\\%\\, Sn, 37\\%\\, Pb\\)): **\\(183^\\circ\\text{C}\\)**.
By forming a solid solution, the alloy displays a significantly lower melting point than either of its pure constituent metals:
\\[
T_{\\text{solder}} (183^\\circ\\text{C}) \\ll T_{Sn} (232^\\circ\\text{C}) < T_{Pb} (328^\\circ\\text{C})
\\]
This low melting point allows electrical wires to be soldered without thermally damaging adjacent delicate semiconductor electronic components.

### 2. Physical Context & Practical Illustration:
When molten solder is applied with a heated soldering iron tip, it wets copper circuit board traces through capillary action and solidifies rapidly, forming a mechanically sturdy, low-resistance electrical joint.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Tin and lead):** Correct. Solder is an alloy of tin (\\(Sn\\)) and lead (\\(Pb\\)).
- **Option B (Copper and zinc):** Incorrect. Copper and zinc form brass.
- **Option C (Lead and iron):** Incorrect. Lead and iron do not form solder alloys.
- **Option D (Aluminium and magnesium):** Incorrect. Aluminium and magnesium form magnalium.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-116",
    text: "Which of the following metals is applied as a coating to galvanise iron sheets and prevent them from rusting?",
    options: [
      "Copper (\\(Cu\\))",
      "Lead (\\(Pb\\))",
      "Zinc (\\(Zn\\))",
      "Nickel (\\(Ni\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Galvanisation** is the application of a protective sacrificial coating of **zinc** (\\(Zn\\)) onto iron or steel.
Zinc is electrochemically more reactive than iron:
\\[
E^\\circ_{Zn^{2+}/Zn} = -0.76\\text{ V} \\quad \\text{vs.} \\quad E^\\circ_{Fe^{2+}/Fe} = -0.44\\text{ V}
\\]
Because zinc has a more negative reduction potential, it oxidises preferentially in the presence of moisture and air:
\\[
Zn(s) \\longrightarrow Zn^{2+}(aq) + 2e^-
\\]
The iron structure is cathodically protected: even when the zinc layer is cracked or chipped, electrons continue to flow from zinc to iron, preventing iron from oxidising to rust (\\(Fe_2O_3 \\cdot xH_2O\\)).

### 2. Physical Context & Practical Illustration:
Galvanized iron (GI) corrugated sheets are the universal standard for roofing, water supply pipes, and farm fencing due to their prolonged multi-decade resistance to atmospheric weathering.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Copper):** Incorrect. Copper is less active than iron; a scratch would cause rapid pitting of iron.
- **Option B (Lead):** Incorrect. Lead is toxic and not used for galvanising iron.
- **Option C (Zinc):** Correct. Zinc is the metal universally used to galvanise iron.
- **Option D (Nickel):** Incorrect. Nickel is used for decorative electroplating (nickel-plating), not galvanisation.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-117",
    text: "Which hydrocarbon fuel gas is mixed with oxygen to produce the intensely hot flame used in industrial gas welding and cutting?",
    options: [
      "Methane gas (\\(CH_4\\))",
      "Hydrogen gas (\\(H_2\\))",
      "Chlorine gas (\\(Cl_2\\))",
      "Acetylene gas (ethyne, \\(C_2H_2\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In industrial gas welding, **acetylene gas** (systematic IUPAC name: **ethyne**, chemical formula **\\(C_2H_2\\)**) is burned in pure oxygen in an oxyacetylene torch:
\\[
2C_2H_2(g) + 5O_2(g) \\longrightarrow 4CO_2(g) + 2H_2O(g) \\quad (\\Delta H = -2600\\text{ kJ})
\\]
The carbon-carbon triple bond (\\(H-C \\equiv C-H\\)) stores high endothermic bond energy. Upon combustion in pure oxygen, it releases intense heat, achieving flame temperatures of approximately **\\(3100^\\circ\\text{C} - 3300^\\circ\\text{C}\\)**.
Because structural steel melts at \\(\\approx 1500^\\circ\\text{C}\\), the oxyacetylene flame easily melts edges of heavy steel plates, fusing them into a continuous metallic weld upon cooling.

### 2. Physical Context & Practical Illustration:
Acetylene is manufactured by the reaction of calcium carbide with water:
\\[
CaC_2(s) + 2H_2O(l) \\longrightarrow Ca(OH)_2(aq) + C_2H_2(g)\\uparrow
\\]
Because compressed free acetylene is prone to explosive detonation, it is safely stored in steel cylinders dissolved in acetone under pressure within a porous monolithic mass.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Methane):** Incorrect. Methane burns at lower temperatures (\\(\\approx 1900^\\circ\\text{C}\\)), insufficient for welding steel.
- **Option B (Hydrogen):** Incorrect. Oxyhydrogen flames are used for specialized platinum melting, but acetylene is the primary welding fuel gas.
- **Option C (Chlorine):** Incorrect. Chlorine is an oxidising toxic halogen, not a fuel gas.
- **Option D (Acetylene):** Correct. Acetylene gas is the standard fuel gas for oxy-fuel welding and metal cutting.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-118",
    text: "Given the industrial chemical processes and their designated catalysts, which of the following pairs is INCORRECT?",
    options: [
      "Contact Process (\\(SO_3\\) manufacture) — Vanadium pentoxide (\\(V_2O_5\\))",
      "Haber Process (\\(NH_3\\) manufacture) — Phosphorus pentoxide (\\(P_2O_5\\))",
      "Hydrogenation of vegetable oils — Finely divided Nickel (\\(Ni\\))",
      "Ostwald Process (\\(HNO_3\\) manufacture) — Platinum-Rhodium gauze"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us examine the established catalysts for each industrial chemical synthesis:
1. **Contact Process (\\(H_2SO_4\\)):** Oxidation of \\(SO_2\\) to \\(SO_3\\) uses **Vanadium pentoxide (\\(V_2O_5\\))** at \\(450^\\circ\\text{C}\\):
   \\[
   2SO_2 + O_2 \\xrightarrow{V_2O_5} 2SO_3 \\quad (\\text{Correct})
   \\]
2. **Hydrogenation of Vegetable Oils:** Addition of \\(H_2\\) to alkenes uses **finely divided Nickel (\\(Ni\\))** at \\(180^\\circ\\text{C}\\):
   \\[
   -CH=CH- + H_2 \\xrightarrow{Ni} -CH_2-CH_2- \\quad (\\text{Correct})
   \\]
3. **Ostwald Process (\\(HNO_3\\)):** Catalytic oxidation of ammonia to \\(NO\\) uses **Platinum-Rhodium gauze** at \\(800^\\circ\\text{C}\\) (\\(\\text{Correct}\\)).
4. **Haber Process (\\(NH_3\\)):** Synthesis of ammonia from nitrogen and hydrogen:
   \\[
   N_2(g) + 3H_2(g) \\rightleftharpoons 2NH_3(g)
   \\]
   The industrial catalyst is **finely divided Iron (\\(Fe\\))** with molybdenum or potassium/aluminium oxide promoters.
   **Phosphorus pentoxide (\\(P_2O_5\\))** is a dehydrating agent, never a catalyst for the Haber process.
Thus, Pair B is completely **INCORRECT**.

### 2. Physical Context & Practical Illustration:
In the Haber process, the iron catalyst lowers the high activation energy of breaking the \\(N \\equiv N\\) triple bond (bond energy \\(945\\text{ kJ/mol}\\)), enabling commercial production of ammonia fertilizers that sustain global food crops.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Correct pair (not the incorrect choice). \\(V_2O_5\\) is the Contact process catalyst.
- **Option B:** **INCORRECT pair** (hence the correct answer). The Haber process utilizes an iron catalyst, not \\(P_2O_5\\).
- **Option C:** Correct pair. Nickel is the hydrogenation catalyst.
- **Option D:** Correct pair. Platinum gauze is the Ostwald ammonia oxidation catalyst.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-119",
    text: "What is the chemical acid-base nature of an aqueous solution of copper sulphate (\\(CuSO_4\\))?",
    options: [
      "Acidic (\\(\\text{pH} < 7.0\\))",
      "Basic (\\(\\text{pH} > 7.0\\))",
      "Strictly neutral (\\(\\text{pH} = 7.0\\))",
      "Strongly alkaline (\\(\\text{pH} \\approx 12\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Copper sulphate (\\(CuSO_4\\)) is an ionic salt formed from a **weak base** (copper(II) hydroxide, \\(Cu(OH)_2\\)) and a **strong mineral acid** (sulphuric acid, \\(H_2SO_4\\)):
\\[
Cu(OH)_2(s) + H_2SO_4(aq) \\longrightarrow CuSO_4(aq) + 2H_2O(l)
\\]
In aqueous solution, \\(CuSO_4\\) dissociates completely into \\(Cu^{2+}\\) and \\(SO_4^{2-}\\) ions:
- \\(SO_4^{2-}\\) is the conjugate base of strong \\(H_2SO_4\\) and does not hydrolyse.
- \\(Cu^{2+}\\) has high charge density (small radius) and undergoes **cationic hydrolysis** with coordinating water molecules:
\\[
[Cu(H_2O)_6]^{2+}(aq) + H_2O(l) \\rightleftharpoons [Cu(H_2O)_5(OH)]^+(aq) + H_3O^+(aq)
\\]
The release of excess hydronium ions into solution causes \\([H_3O^+] > 10^{-7}\\text{ M}\\), rendering the solution **acidic** (typical pH \\(\\approx 4.0 - 4.5\\)).

### 2. Physical Context & Practical Illustration:
When blue litmus paper is dipped into an aqueous solution of blue copper sulphate crystals, the blue litmus turns distinctly red, proving its acidic nature.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Acidic):** Correct. Cationic hydrolysis of \\(Cu^{2+}\\) releases hydronium ions, making the solution acidic (\\(\\text{pH} < 7.0\\)).
- **Option B (Basic):** Incorrect. Basic salts originate from strong bases and weak acids.
- **Option C (Neutral):** Incorrect. Only salts of strong acid + strong base (like \\(NaCl\\)) are strictly neutral.
- **Option D (Strongly alkaline):** Incorrect. Copper sulphate solution is never alkaline.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-120",
    text: "Calcium carbonate (\\(CaCO_3\\)) is widely known in nature and everyday life in which common physical forms?",
    options: [
      "Plaster of Paris and gypsum",
      "Quicklime and burnt lime",
      "Chalk, limestone, and marble",
      "Slaked lime and limewater"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Calcium carbonate** (chemical formula \\(CaCO_3\\), molar mass \\(100.09\\text{ g/mol}\\)) is an insoluble ionic mineral compound that exists in three major natural and commercial allotropic varieties:
1. **Limestone:** A sedimentary rock formed from accumulated marine shells and micro-fossils over geological eras.
2. **Chalk:** A soft, white, porous, fine-textured sedimentary form composed of microscopic calcite shells of coccolithophores.
3. **Marble:** A hard, crystalline, metamorphic rock formed when limestone is subjected to intense subterranean heat and pressure (recrystallising into compact calcite grains).
All three forms share the identical chemical identity **\\(CaCO_3\\)** and react identically with dilute acids to evolve carbon dioxide gas:
\\[
CaCO_3(s) + 2HCl(aq) \\longrightarrow CaCl_2(aq) + H_2O(l) + CO_2(g)\\uparrow
\\]

### 2. Physical Context & Practical Illustration:
While blackboard chalk was historically pure \\(CaCO_3\\) (and is still used as calcium carbonate powder), quicklime is \\(CaO\\), slaked lime is \\(Ca(OH)_2\\), and Plaster of Paris is \\(CaSO_4 \\cdot \\frac{1}{2}H_2O\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Plaster of Paris and gypsum are calcium sulphate salts, not carbonates.
- **Option B:** Incorrect. Quicklime is calcium oxide (\\(CaO\\)).
- **Option C:** Correct. Chalk, limestone, and marble are all physical forms of calcium carbonate (\\(CaCO_3\\)).
- **Option D:** Incorrect. Slaked lime is calcium hydroxide (\\(Ca(OH)_2\\)).`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-121",
    text: "Which logarithmic quantitative parameter is universally utilized in chemistry as the standard measure of the acidity or alkalinity of an aqueous solution?",
    options: [
      "Total ion count alone",
      "Boiling point elevation",
      "pH value (potential of hydrogen)",
      "Freezing point depression"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1909, Danish biochemist S. P. L. Sorensen devised the **pH scale** (from German *Potenz*, power of hydrogen) to provide a compact, convenient quantitative scale for specifying the concentration of hydronium ions across many orders of magnitude:
\\[
\\text{pH} = -\\log_{10}[H_3O^+] = \\log_{10}\\left(\\frac{1}{[H_3O^+]}\\right)
\\]
At \\(25^\\circ\\text{C}\\):
- **Neutral Solution:** \\([H_3O^+] = 1.0 \\times 10^{-7}\\text{ M} \\implies \\mathbf{\\text{pH} = 7.0}\\)
- **Acidic Solution:** \\([H_3O^+] > 1.0 \\times 10^{-7}\\text{ M} \\implies \\mathbf{\\text{pH} < 7.0}\\) (e.g., \\([H_3O^+] = 10^{-2}\\text{ M} \\implies \\text{pH} = 2.0\\))
- **Alkaline Solution:** \\([H_3O^+] < 1.0 \\times 10^{-7}\\text{ M} \\implies \\mathbf{\\text{pH} > 7.0}\\) (e.g., \\([H_3O^+] = 10^{-12}\\text{ M} \\implies \\text{pH} = 12.0\\))
Because the scale is logarithmic, each unit decrease in pH corresponds to a tenfold (10x) increase in hydrogen ion concentration.

### 2. Physical Context & Practical Illustration:
pH measurements are vital across science and industry: maintaining blood pH within tight homeostatic limits (\\(7.35 - 7.45\\)), testing soil suitability for crops, swimming pool sanitation, and water treatment quality control.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** Incorrect. Total ion count measures electrical conductivity, not specific hydrogen ion activity.
- **Option B:** Incorrect. Boiling point elevation is a colligative property proportional to total solute particles.
- **Option C:** Correct. pH is the universal mathematical measure of the acidity of an aqueous solution.
- **Option D:** Incorrect. Freezing point depression depends on total dissolved particles, not acidity.`
  },
  {
    questionCode: "MH-9-SCIT-5-5.1-OSC-122",
    text: "Which of the following statements is NOT TRUE regarding the chemical and physical properties of elemental iron (\\(Fe\\))?",
    options: [
      "Iron dissolves readily and completely in concentrated nitric acid without forming any protective oxide film",
      "Pure metallic iron is strongly ferromagnetic at room temperature",
      "Iron alloys with carbon and other metals to form versatile steels",
      "Cast iron contains 2% to 4% carbon and is mechanically hard and brittle"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze each statement regarding the chemistry of iron:
- **Statement A:** **NOT TRUE**. Concentrated nitric acid (\\(HNO_3\\), \\(\\approx 68\\%\\)) is an exceptionally powerful oxidising agent. When iron is dipped into concentrated \\(HNO_3\\), an impervious, microscopic, passive surface layer of magnetic iron oxide (triferric tetroxide, \\(Fe_3O_4\\)) is instantaneously formed on the metal surface:
  \\[
  3Fe + 8HNO_3 \\longrightarrow Fe_3O_4(s) + 8NO_2 + 4H_2O
  \\]
  This dense, adherent oxide film completely passivates the metal, blocking contact between acid and inner iron atoms. Consequently, **iron does NOT dissolve** in concentrated nitric acid; it becomes chemically **passive**. (Passive iron can be reactivated only by scratching its surface or heating with strong reducing agents).
- **Statement B:** True. Iron is ferromagnetic with high magnetic permeability.
- **Statement C:** True. Iron alloyed with \\(0.1\\% - 1.5\\%\\) carbon forms carbon steels; with \\(Cr\\) and \\(Ni\\) it forms stainless steel.
- **Statement D:** True. Cast iron (pig iron) contains 2% to 4% carbon, rendering it hard and brittle under shock.

### 2. Physical Context & Practical Illustration:
Because iron becomes passive in concentrated nitric acid, concentrated nitric acid can be safely stored and transported in iron or steel railway tanker cars without corrosive dissolution.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A:** **NOT TRUE statement** (hence the correct answer). Iron becomes passive in concentrated nitric acid and does not dissolve readily.
- **Option B:** True statement. Iron is a classic ferromagnetic element.
- **Option C:** True statement. Steel is an alloy of iron and carbon.
- **Option D:** True statement. Cast iron is brittle due to high carbon content.`
  }
];

module.exports = { ch5_part4 };
