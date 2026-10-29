# scripts/build_part3_full.py
import json
import re

with open('backups/staging/mh9_scit_8_raw.json', 'r', encoding='utf-8') as f:
    raw_all = json.load(f)

raw_part3 = raw_all[102:150] # Q103 to Q150 (48 questions)

# Q103 to Q108: OAR
q103_sol = """### 1. Scientific Principle & Dough Leavening:
Bread dough leavening relies on gas generation inside a viscoelastic food matrix. When *Saccharomyces cerevisiae* metabolizes fermentable carbohydrates under anaerobic conditions, it produces carbon dioxide gas (\\(\\text{CO}_2\\)) and ethanol.

### 2. Biological Process & Gluten-Gas Dynamics:
- The gluten protein network formed by glutenin and gliadin during flour hydration and kneading creates an elastic, extensible dough structure.
- As yeast cells respire anaerobically, the evolving \\(\\text{CO}_2\\) gas cannot escape immediately; instead, it expands and nucleates thousands of microscopic bubbles within the gluten matrix.
- During baking, the high oven temperatures cause the gas bubbles to expand further (Charles's law) while the starch gelatinizes and gluten proteins denature, permanently setting a porous, soft, and spongy crumb structure.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Yeast leavening makes bread light, airy, porous, and spongy.
- **Reason (R) Evaluation:** True. The enzymatic release of \\(\\text{CO}_2\\) gas by yeast trapped within the elastic gluten network creates these characteristic porous cavities.
- **Causal Connection:** Reason (R) provides the direct biochemical and structural explanation for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

q104_sol = """### 1. Scientific Principle & Anhydrobiosis & Yeast Reactivation:
Commercial active dry yeast is manufactured by dehydrating yeast cultures until cells enter a dormant, metabolically arrested state of anhydrobiosis to preserve shelf life.

### 2. Biological Process & Cellular Rehydration:
- Immersing dormant dry yeast granules in lukewarm water (approximately \\(35^\\circ\\text{C}\\text{--}40^\\circ\\text{C}\\)) rapidly rehydrates cell walls and plasma membranes without thermal shock.
- Adding a small amount of sucrose or glucose provides an immediate carbohydrate substrate for cellular glycolysis.
- The activated enzymes break down sugar, generating carbon dioxide foam (blooming), confirming the viability of the yeast culture before incorporation into dense flour dough.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Activating dry yeast in lukewarm sugar water ensures rapid, uniform fermentation and proves yeast viability.
- **Reason (R) Evaluation:** True. Mild warmth and accessible simple sugars provide the physical and metabolic stimuli required to terminate cellular dormancy.
- **Causal Connection:** Reason (R) correctly explains why the preliminary activation procedure is necessary.
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

q105_sol = """### 1. Scientific Principle & Renewable Biofuels:
Bio-ethanol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\)) produced from biological fermentation represents a renewable liquid transportation fuel capable of substituting or blending with petroleum gasoline.

### 2. Biological Process & The Short-Term Carbon Cycle:
- Plants (such as sugarcane and corn) absorb atmospheric carbon dioxide via photosynthesis:
  \\[6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\xrightarrow{\\text{Light}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2\\]
- Microbial fermentation converts these sugars into ethanol:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Yeast}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2\\]
- When bio-ethanol combusts in internal combustion engines, it releases \\(\\text{CO}_2\\) that was captured from the atmosphere during the current plant growing season, resulting in a closed, short-term carbon loop compared to ancient fossil hydrocarbons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Bio-ethanol is widely deployed worldwide as a clean biofuel additive (e.g., E10, E20 blends).
- **Reason (R) Evaluation:** True. Bio-ethanol recycles contemporary biogenic carbon rather than mobilizing subterranean fossil carbon deposits.
- **Causal Connection:** Reason (R) provides the fundamental thermodynamic and ecological rationale for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

q106_sol = """### 1. Scientific Principle & Microbial Population Kinetics:
Unicellular fungal microorganisms follow defined demographic growth phases (lag, exponential/log, stationary, and decline) governed by substrate availability.

### 2. Biological Process & Substrate Utilization:
- *Saccharomyces cerevisiae* is an organotrophic eukaryote that requires exogenous organic carbon for energy metabolism and biomass synthesis.
- In sugar-rich aqueous solutions, simple hexose sugars (glucose, fructose) diffuse into yeast cells via hexose transporters, driving rapid catabolism to synthesize ATP, nucleic acids, and cell wall mannoproteins.
- This energetic abundance fuels accelerated asexual reproduction via **budding**, causing exponential population expansion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Yeast populations proliferate exponentially in warm, nutrient-rich sugar solutions.
- **Reason (R) Evaluation:** True. Sugars furnish the carbon backbones and ATP necessary for cellular biosynthesis and cell division.
- **Causal Connection:** Reason (R) explains the metabolic driver behind the rapid population growth stated in Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

q107_sol = """### 1. Scientific Principle & Circular Bio-Economy:
The circular economy paradigm focuses on valorizing industrial byproducts and organic waste streams into value-added commodities, thereby eliminating waste and decreasing reliance on finite fossil fuels.

### 2. Biological Process & Molasses Valorization:
- **Molasses** is a viscous, dark industrial byproduct generated during the crystallization of sucrose in sugar mills, containing \\(40\\%\\text{--}50\\%\\) fermentable residual sugars.
- Fermenting this non-potable agricultural waste with *Saccharomyces cerevisiae* converts waste sugars into anhydrous bio-ethanol, useful as a high-octane automotive fuel additive, and spent yeast biomass for animal feed.
- This bioconversion turns a high-BOD environmental disposal problem into a renewable fuel resource.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Producing bio-ethanol from sugar refinery molasses exemplifies circular bio-economy principles.
- **Reason (R) Evaluation:** True. It upcycles industrial agricultural residue into renewable fuel, decreasing petroleum consumption.
- **Causal Connection:** Reason (R) directly explains the circular economic justification in Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

q108_sol = """### 1. Scientific Principle & Cellular Osmoregulation:
Living microbial cells maintain selective semi-permeable plasma membranes and are vulnerable to osmotic pressure gradients across their cellular boundaries.

### 2. Biological Process & Hypertonic Plasmolysis:
- Sodium chloride (\\(\\text{NaCl}\\)) dissociates into \\(\\text{Na}^+\\) and \\(\\text{Cl}^-\\) ions in solution, substantially lowering the external water potential.
- When concentrated salt is placed in direct contact with dry or rehydrating yeast cells, water rapidly diffuses out of the cytoplasm down its chemical potential gradient via **exosmosis**.
- This severe loss of turgor causes cellular plasmolysis, denatures membrane transport proteins, and halts glycolysis, severely inhibiting gas production and preventing the dough from rising.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Direct contact with concentrated salt dehydrates and damages yeast, suppressing fermentation.
- **Reason (R) Evaluation:** True. High osmotic pressure draws intracellular water out via exosmosis, causing cellular dehydration.
- **Causal Connection:** Reason (R) describes the exact biophysical mechanism responsible for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."""

# Q109 to Q112: OMC
q109_sol = """### 1. Scientific Principle & Fermentation Thermodynamics & Kinetics:
Microbial enzymatic fermentation is a biochemical process that requires specific physical and nutritional parameters to sustain catalytic efficiency.

### 2. Biological Process & Essential Environmental Parameters:
- **Substrate Availability:** Yeast cells require accessible hexose carbohydrates (glucose, fructose, maltose) to fuel glycolysis.
- **Aqueous Moisture:** Water provides the polar solvent medium necessary for enzyme diffusion, nutrient translocation, and membrane integrity.
- **Optimal Temperature Range:** *Saccharomyces cerevisiae* exhibits optimal metabolic activity in a warm temperature range of \\(28^\\circ\\text{C}\\text{--}35^\\circ\\text{C}\\). Freezing temperatures (below \\(0^\\circ\\text{C}\\)) arrest molecular motion and halt enzymatic catalysis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Fermentable sugars are mandatory biochemical substrates for glycolysis.
- **Option B is correct.** Liquid water/moisture is an indispensable physiological medium for metabolic transport and enzymatic function.
- **Option C is incorrect.** Freezing temperatures below zero reversibly arrest enzyme activity and cause ice-crystal damage rather than supporting active fermentation.
- **Option D is correct.** A warm temperature range (\\(28^\\circ\\text{C}\\text{--}35^\\circ\\text{C}\\)) ensures maximum kinetic rate without denaturing yeast enzymes."""

q110_sol = """### 1. Scientific Principle & Industrial Distillery Co-Products:
Anaerobic fermentation of sugar-rich molasses by *Saccharomyces cerevisiae* in commercial bioreactors yields specific biochemical and biological co-products.

### 2. Biological Process & The Reaction Mass Balance:
- As yeast converts sucrose, glucose, and fructose anaerobically:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Zymase complex}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 + 2\\text{ATP}\\]
- The direct chemical outputs are **bio-ethanol** (distilled into fuel) and **carbon dioxide gas** (scrubbed, compressed, and sold for carbonated beverages and dry ice).
- Concurrently, reproducing yeast cells accumulate as protein- and vitamin-rich **spent yeast biomass**, harvested as single-cell protein (SCP) for livestock feed.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Bio-ethanol is the primary liquid biofuel harvested from fermented molasses mash.
- **Option B is correct.** Spent yeast biomass (SCP) is a direct, valuable co-product harvested from fermentation vats.
- **Option C is incorrect.** Synthetic plastic polymers (e.g., polyethylene, polystyrene) are synthetic petrochemicals, not direct biological fermentation products.
- **Option D is correct.** Carbon dioxide gas is an obligate stoichiometric byproduct released during the decarboxylation of pyruvate to acetaldehyde."""

q111_sol = """### 1. Scientific Principle & Industrial Biotechnology Applications:
*Saccharomyces cerevisiae* (commonly known as baker's or brewer's yeast) is one of the most versatile model organisms in industrial biotechnology.

### 2. Biological Process & Commercial Applications:
- **Baking:** Evolution of \\(\\text{CO}_2\\) leavens dough, giving bread, buns, and pastries their porous, airy crumb structure.
- **Biofuel Refining:** Industrial-scale anaerobic fermentation converts agricultural molasses, corn starch, or cellulosic sugars into bio-ethanol.
- **Brewing:** Anaerobic fermentation of malted barley and fruit musts yields alcoholic beverages (beer, wine) containing ethanol and aromatic flavor esters.
- In contrast, inorganic nitrogen fertilizers (like urea) are manufactured chemically via high-temperature Haber-Bosch synthesis, not by yeast.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Leavened bread baking relies directly on \\(\\text{CO}_2\\) production by *S. cerevisiae*.
- **Option B is correct.** Large-scale bio-ethanol fuel manufacturing from molasses is driven by *S. cerevisiae*.
- **Option C is correct.** Commercial brewing of beer and wine utilizes *S. cerevisiae* for ethanol production.
- **Option D is incorrect.** Chemical nitrogen fertilizers are produced industrially from fossil methane and atmospheric nitrogen, not yeast metabolism."""

q112_sol = """### 1. Scientific Principle & Stuck Fermentation & Stress Physiology:
"Stuck fermentation" occurs in industrial bioreactors or bakeries when yeast cells arrest fermentation prematurely before available carbohydrates are fully metabolized.

### 2. Biological Process & Inhibitory Stress Factors:
- **Thermal Inactivation:** Temperatures exceeding \\(50^\\circ\\text{C}\\) denature essential metabolic enzymes and disrupt lipid bilayers, killing yeast cells; severe freezing arrests metabolic kinetics.
- **Substrate Exhaustion:** Depletion of fermentable sugars starves yeast cells of metabolic fuel, terminating glycolysis.
- **Ethanol Toxicity:** Ethanol is an amphiphilic solvent that intercalates into bacterial and fungal plasma membranes. When ethanol concentrations exceed yeast tolerance limits (typically \\(12\\%\\text{--}16\\%\\text{ v/v}\\)), membrane fluidity collapses, dissipating the proton motive force and arresting fermentation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Substrate exhaustion removes the metabolic precursor required for ethanol and gas synthesis.
- **Option B is correct.** Extreme thermal shock (temperatures above \\(50^\\circ\\text{C}\\)) kills yeast cells, causing abrupt cessation of fermentation.
- **Option C is correct.** Toxic ethanol accumulation destabilizes the yeast cell membrane, inhibiting enzymatic pathways.
- **Option D is incorrect.** Abundant moisture and controlled oxygen support healthy yeast growth and reproduction; they do not cause fermentation failure."""

# Q113 to Q141: OSC
q113_sol = """### 1. Scientific Principle & Industrial Mycology:
The biological production of baked goods and commercial biofuels relies on specific domesticated fungal species optimized for high glycolytic throughput.

### 2. Biological Process & Organism Profile:
- **Saccharomyces cerevisiae** is a unicellular, eukaryotic budding yeast belonging to the kingdom Fungi (phylum Ascomycota).
- It possesses exceptional biochemical capacity for rapid anaerobic glycolysis, fermenting simple hexose sugars into ethanol and carbon dioxide with high metabolic efficiency.
- Because of its safety, non-pathogenic nature, and robustness, *S. cerevisiae* is the universal organism of choice in baking and biofuel industries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** *Lactobacillus acidophilus* is a lactic acid bacterium that converts lactose to lactic acid, used in yogurt, not bread leavening.
- **Option B is correct.** *Saccharomyces cerevisiae* is the microscopic yeast used in bread baking and bio-ethanol production.
- **Option C is incorrect.** *Rhizobium leguminosarum* is a root-nodulating bacterium that fixes atmospheric nitrogen in legumes.
- **Option D is incorrect.** *Penicillium notatum* is a filamentous mold famous for producing the antibiotic penicillin."""

q114_sol = """### 1. Scientific Principle & Gaseous Metabolites of Fermentation:
During the anaerobic degradation of glucose, the metabolic intermediate pyruvate undergoes enzymatic decarboxylation, releasing an inorganic gaseous byproduct.

### 2. Biological Process & Reaction Dynamics:
- In yeast glycolysis, one glucose molecule yields two pyruvate molecules:
  \\[\\text{Glucose} \\xrightarrow{\\text{Glycolysis}} 2\\text{ Pyruvate} + 2\\text{NADH} + 2\\text{ATP}\\]
- Under anaerobic conditions, the enzyme pyruvate decarboxylase cleaves a carboxyl group from each pyruvate, generating acetaldehyde and releasing **carbon dioxide gas (\\(\\text{CO}_2\\))**:
  \\[\\text{Pyruvate} \\xrightarrow{\\text{Pyruvate decarboxylase}} \\text{Acetaldehyde} + \\text{CO}_2\\uparrow\\]
- This evolving \\(\\text{CO}_2\\) forms expanding gas pockets that leaven dough, causing it to swell and become porous.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Oxygen (\\(\\text{O}_2\\)) is consumed in aerobic respiration, never released during anaerobic fermentation.
- **Option B is correct.** Carbon dioxide (\\(\\text{CO}_2\\)) is the gas produced by yeast that causes dough leavening and porous crumb formation.
- **Option C is incorrect.** Nitrogen gas (\\(\\text{N}_2\\)) is not synthesized during fungal glycolysis.
- **Option D is incorrect.** Sulfur dioxide is an inorganic preservative sometimes added to wine, not a gas synthesized by yeast during dough fermentation."""

q115_sol = """### 1. Scientific Principle & Modes of Cellular Respiration:
Cellular respiration can proceed through aerobic pathways (requiring molecular oxygen as the terminal electron acceptor) or anaerobic pathways (fermentation) where organic molecules serve as electron donors and acceptors.

### 2. Biological Process & Alcoholic Fermentation:
- In bread dough or submerged sugar vats, oxygen rapidly becomes depleted.
- Yeast operates as a facultative anaerobe, switching to **anaerobic respiration (alcoholic fermentation)**:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Yeast enzymes}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 + 2\\text{ATP}\\]
- Acetaldehyde acts as the terminal electron acceptor, regenerating \\(\\text{NAD}^+\\) from \\(\\text{NADH}\\) so glycolysis can continue generating ATP in the absence of oxygen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Aerobic respiration requires abundant oxygen and completely oxidizes glucose into \\(\\text{CO}_2\\) and \\(\\text{H}_2\\text{O}\\), producing no ethanol.
- **Option B is correct.** Yeast performs anaerobic respiration (alcoholic fermentation) to convert sugars into ethanol and carbon dioxide.
- **Option C is incorrect.** Photophosphorylation is a light-dependent ATP generation process occurring in photosynthetic chloroplasts, which fungi lack.
- **Option D is incorrect.** Chemoautotrophic oxidation is practiced by specialized lithotrophic bacteria, not heterotrophic yeast."""

q116_sol = """### 1. Scientific Principle & Biofuel Chemistry:
Anaerobic fermentation of hexose carbohydrates by yeasts yields a low-molecular-weight monohydric alcohol that serves as a clean liquid fuel.

### 2. Biological Process & Ethanol Synthesis:
- In the second terminal step of alcoholic fermentation, the enzyme alcohol dehydrogenase reduces acetaldehyde using electrons donated by \\(\\text{NADH}\\):
  \\[\\text{CH}_3\\text{CHO} + \\text{NADH} + \\text{H}^+ \\xrightarrow{\\text{Alcohol dehydrogenase}} \\text{CH}_3\\text{CH}_2\\text{OH} + \\text{NAD}^+\\]
- The resulting liquid organic molecule is **ethanol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\))**, commonly termed bio-ethanol when harvested from agricultural biomass for blending with gasoline.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Ethanol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\)) is the liquid organic compound synthesized during yeast fermentation that serves as an eco-friendly biofuel.
- **Option B is incorrect.** Methanol (\\(\\text{CH}_3\\text{OH}\\)) is a highly toxic alcohol produced by destructive distillation of wood or pectin breakdown, not the primary product of yeast glycolysis.
- **Option C is incorrect.** Acetic acid is produced by *Acetobacter* bacteria during oxidative vinegar fermentation.
- **Option D is incorrect.** Lactic acid is produced by lactic acid bacteria (*Lactobacillus*) and mammalian muscle during anaerobic exertion."""

q117_sol = """### 1. Scientific Principle & Industrial Fermentation Feedstocks:
Large-scale commercial production of industrial commodities requires abundant, high-sugar, and economically inexpensive agricultural feedstocks.

### 2. Biological Process & Molasses as Fermentation Medium:
- In sugar refineries, extracting crystallized sucrose from crushed sugarcane or sugar beet juice leaves behind a thick, viscous, non-crystallizable syrup called **molasses**.
- Molasses contains \\(45\\%\\text{--}55\\%\\) total fermentable sugars (sucrose, glucose, fructose) alongside essential trace minerals (calcium, potassium) and vitamins that nourish yeast cultures.
- In countries like India and Brazil, molasses is the primary economical raw material utilized in commercial distilleries to manufacture industrial alcohol and bio-ethanol.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Coal tar is a dense liquid obtained as a byproduct of coke production from coal, containing polycyclic aromatic hydrocarbons toxic to living cells.
- **Option B is incorrect.** Crushed limestone consists of calcium carbonate (\\(\\text{CaCO}_3\\)), an inorganic mineral containing zero fermentable sugars.
- **Option C is correct.** Molasses is the sugar-rich agricultural byproduct from sugar mills used as the cheap starting substrate for bio-ethanol fermentation.
- **Option D is incorrect.** Crude petroleum is a non-renewable fossil hydrocarbon mixture that cannot be biologically fermented by baker's yeast."""

q118_sol = """### 1. Scientific Principle & Carbon Neutrality & Renewable Energy:
Petroleum fuels extract ancient carbon buried millions of years ago and emit it into the atmosphere, causing a net increase in greenhouse gas concentrations.

### 2. Biological Process & The Biogenic Carbon Cycle:
- Bio-ethanol is produced from biomass (sugarcane molasses, corn, agricultural residues) that captures atmospheric carbon dioxide via photosynthesis during crop cultivation.
- When combusted as an automotive fuel additive, bio-ethanol releases oxygenated emissions with fewer unburned hydrocarbons, lower carbon monoxide levels, and zero net addition of ancient fossil carbon to the biosphere.
- It thus constitutes a renewable, carbon-recycling energy carrier.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Bio-ethanol is not a non-flammable liquid; it burns readily with a clean, blue flame.
- **Option B is correct.** Bio-ethanol is renewable and derived from plant biomass, cycling contemporary carbon and diminishing net greenhouse gas emissions.
- **Option C is incorrect.** Bio-ethanol contains carbon and releases carbon dioxide upon combustion (\\(\\text{C}_2\\text{H}_5\\text{OH} + 3\\text{O}_2 \\rightarrow 2\\text{CO}_2 + 3\\text{H}_2\\text{O}\\)).
- **Option D is incorrect.** Bio-ethanol does not generate toxic sulfur oxides; its advantage is precisely its lack of sulfur."""

q119_sol = """### 1. Scientific Principle & Five-Kingdom Taxonomy:
In Robert Whittaker's Five-Kingdom classification system, organisms are classified according to cellular organization, presence of a nuclear membrane, body complexity, and mode of nutrition.

### 2. Biological Process & Fungal Characteristics:
- *Saccharomyces cerevisiae* is categorized in the kingdom **Fungi** (phylum Ascomycota).
- It possesses eukaryotic cellular architecture, a rigid cell wall containing chitin and glucan, and heterotrophic (absorptive/saprophytic) nutrition, lacking photosynthetic chlorophyll pigments completely.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Kingdom Plantae comprises multicellular, autotrophic photosynthetic organisms with cellulose cell walls.
- **Option B is incorrect.** Kingdom Monera contains unicellular prokaryotic organisms devoid of nuclear membranes (e.g., bacteria).
- **Option C is correct.** *Saccharomyces cerevisiae* belongs to the kingdom Fungi.
- **Option D is incorrect.** Kingdom Animalia consists of multicellular, eukaryotic heterotrophs lacking cell walls."""

q120_sol = """### 1. Scientific Principle & Enzymatic Glycolysis & Hydrolysis:
Yeasts produce specialized hydrolytic and glycolytic enzymes to convert complex disaccharides into absorbable monosaccharides and subsequently into fermentation products.

### 2. Biological Process & Invertase and Zymase Roles:
- **Invertase (\\(\\beta\\)-fructofuranosidase):** Secreted into the periplasmic space or medium to hydrolyze disaccharide sucrose into glucose and fructose:
  \\[\\text{C}_{12}\\text{H}_{22}\\text{O}_{11} + \\text{H}_2\\text{O} \\xrightarrow{\\text{Invertase}} \\text{C}_6\\text{H}_{12}\\text{O}_6 \\text{ (glucose)} + \\text{C}_6\\text{H}_{12}\\text{O}_6 \\text{ (fructose)}\\]
- **Zymase Complex:** An intracellular multienzyme system that catalyzes the anaerobic breakdown of hexose sugars into ethanol and carbon dioxide:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Zymase}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Pepsin and trypsin are proteolytic digestive enzymes produced in animal stomach and pancreas, not fungal glycolytic enzymes.
- **Option B is correct.** Zymase and invertase are the primary enzymes responsible for sucrose hydrolysis and alcoholic fermentation in yeast.
- **Option C is incorrect.** DNA ligase and helicase are nucleic acid replication enzymes.
- **Option D is incorrect.** Amylase hydrolyzes starch, while cellulase degrades plant cellulose walls."""

q121_sol = """### 1. Scientific Principle & Thermal Denaturation of Proteins:
Enzymes and cellular membranes in mesophilic microorganisms operate within specific thermal boundaries. Exceeding the maximum critical temperature causes irreversible protein denaturation.

### 2. Biological Process & Thermal Death Point:
- *Saccharomyces cerevisiae* is a mesophilic fungus with an optimal growth range of \\(28^\\circ\\text{C}\\text{--}35^\\circ\\text{C}\\).
- When dough is exposed to boiling or scalding temperatures (exceeding \\(55^\\circ\\text{C}\\text{--}60^\\circ\\text{C}\\)), thermal agitation disrupts hydrogen bonds and hydrophobic interactions stabilizing enzyme secondary and tertiary structures.
- Intracellular enzymes (including the zymase complex) denature irreversibly, membrane integrity collapses, and yeast cells die, abruptly halting all metabolic gas production and preventing dough leavening.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** High boiling temperatures do not stimulate yeast; they destroy cell viability.
- **Option B is correct.** Boiling temperatures kill yeast cells and denature enzymes, stopping fermentation completely so dough cannot rise.
- **Option C is incorrect.** Yeast cells die rather than undergoing sudden asexual budding at boiling temperatures.
- **Option D is incorrect.** Yeast cells do not synthesize chlorophyll or perform photosynthesis under heat or any other conditions."""

q122_sol = """### 1. Scientific Principle & Industrial Biotechnology Sectors:
The metabolic versatility of microorganisms enables their deployment across distinct commercial manufacturing sectors.

### 2. Biological Process & The Fermentation Industry:
- The **brewing and fermentation industry** relies extensively on *Saccharomyces cerevisiae*.
- Strains of brewer's yeast convert grain starches (malted barley, wheat) and fruit musts into alcoholic beverages (beers, wines, spirits) and industrial bio-ethanol fuel.
- In addition, the baking sector uses identical metabolic pathways to generate carbon dioxide for leavening bread dough.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Heavy metal mining extracts mineral ores through geochemical or physical separation, not fungal fermentation.
- **Option B is correct.** The brewing, distilling, and fermentation industries rely on *Saccharomyces cerevisiae* for manufacturing beverages and bio-ethanol.
- **Option C is incorrect.** Petrochemical refining cracks fossil crude oil into gasoline and naphtha through fractional distillation.
- **Option D is incorrect.** Synthetic textile manufacturing synthesizes polymers from petrochemical monomers (nylon, polyester)."""

q123_sol = """### 1. Scientific Principle & Rheology of Dough & Viscoelasticity:
Leavened bread requires two indispensable components: a gas generator (yeast) and an extensible, impermeable physical matrix capable of capturing and expanding with the evolving gas.

### 2. Biological Process & The Gluten Network:
- When wheat flour is mixed with water and kneaded, two major storage proteins—**gliadin** (conferring viscosity and extensibility) and **glutenin** (conferring elasticity and tensile strength)—cross-link via disulfide bonds to form a continuous three-dimensional network known as **gluten**.
- As *Saccharomyces cerevisiae* ferments sugars, the evolving \\(\\text{CO}_2\\) gas collects in microscopic air cells.
- The elastic gluten sheets stretch under the internal gas pressure without rupturing, effectively entrapping the gas bubbles and causing the dough to double in volume (rise).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Gluten does not function to kill bacteria; it is a structural storage protein.
- **Option B is correct.** The primary function of the gluten network is to trap expanding carbon dioxide bubbles, allowing uniform leavening and dough rise.
- **Option C is incorrect.** Gluten does not prevent starch from absorbing water; hydration is essential for gluten formation itself.
- **Option D is incorrect.** Gluten does not evaporate during baking; it coagulates and sets the permanent bread structure."""

q124_sol = """### 1. Scientific Principle & Facultative Anaerobic Catabolism:
Facultative anaerobes possess alternate metabolic pathways that activate according to ambient dissolved oxygen levels.

### 2. Biological Process & Anaerobic Fermentation Pathway:
- In the complete absence of molecular oxygen (\\(\\text{O}_2\\)), mitochondrial oxidative phosphorylation cannot operate because there is no terminal electron acceptor.
- *Saccharomyces cerevisiae* survives by executing alcoholic fermentation:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Yeast enzymes}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 + 2\\text{ATP}\\]
- Pyruvate is decarboxylated to acetaldehyde and \\(\\text{CO}_2\\), and acetaldehyde is subsequently reduced to ethanol, regenerating \\(\\text{NAD}^+\\) to sustain substrate-level phosphorylation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Complete oxidation of glucose to \\(\\text{CO}_2\\) and \\(\\text{H}_2\\text{O}\\) requires aerobic cellular respiration with molecular oxygen.
- **Option B is correct.** Under anaerobic conditions, yeast carries out alcoholic fermentation yielding ethanol and carbon dioxide.
- **Option C is incorrect.** Direct synthesis of cellulose occurs in plant cell walls and certain bacteria, not as an anaerobic yeast catabolic route.
- **Option D is incorrect.** Lactic acid fermentation is carried out by lactic acid bacteria and vertebrate muscles, not *Saccharomyces cerevisiae*."""

q125_sol = """### 1. Scientific Principle & Food Technology & Quality Standardization:
Commercial bakery operations depend on precise biochemical kinetic control to guarantee consistent product texture, crumb elasticity, and flavor profile.

### 2. Biological Process & Proofing Control:
- Proofing is the period during which shaped dough rests in a humidity- and temperature-controlled environment (typically \\(28^\\circ\\text{C}\\text{--}38^\\circ\\text{C}\\)) to allow active yeast fermentation.
- **Under-proofing:** Insufficient fermentation yields dense, heavy, unexpanded bread with low volume.
- **Over-proofing:** Excessive fermentation over-stretches the gluten network, causing gas bubbles to coalesce and the dough to collapse, resulting in an overly sour, coarse crumb and yeasty off-flavors.
- Thus, precise control of temperature and proofing duration is essential for optimal gas retention and crumb structure.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Bakery monitoring is not designed to sterilize wheat flour; yeast must remain actively fermenting.
- **Option B is correct.** Monitoring proofing ensures optimal gas production, balanced gluten expansion, and ideal bread crumb texture.
- **Option C is incorrect.** Leavened bread requires yeast; bakeries aim to cultivate active yeast rather than eliminate it during proofing.
- **Option D is incorrect.** Proofing conditions develop crumb porosity, not rock-hard dry crackers."""

q126_sol = """### 1. Scientific Principle & Binomial Nomenclature:
In biological classification, every organism is designated by an international two-part Latinized scientific name consisting of its genus and specific epithet.

### 2. Biological Process & The Model Baker's Yeast:
- The common baker's and brewer's yeast belongs to the genus **Saccharomyces** (derived from Greek for "sugar fungus") and species **cerevisiae** (referring to beer).
- Therefore, its standardized taxonomic binomial name is **Saccharomyces cerevisiae**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** *Escherichia coli* is a Gram-negative bacterium inhabiting the lower intestine of warm-blooded organisms.
- **Option B is correct.** *Saccharomyces cerevisiae* is the official scientific name of common baker's and brewer's yeast.
- **Option C is incorrect.** *Bacillus anthracis* is a Gram-positive endospore-forming pathogenic bacterium responsible for anthrax.
- **Option D is incorrect.** *Streptococcus pneumoniae* is a bacterial pathogen causing lobar pneumonia."""

q127_sol = """### 1. Scientific Principle & Dough Structural Morphology:
The macroscopic appearance of fermenting dough directly reflects the microscopic accumulation of trapped gas pockets.

### 2. Biological Process & Structural Transformation:
- Prior to fermentation, kneaded dough is dense, heavy, and compact.
- As yeast cells ferment sugars, \\(\\text{CO}_2\\) gas accumulates inside hundreds of tiny gluten micro-alveoli.
- As the volume of gas expands, the dough visibly inflates to twice or thrice its original size, transforming into a light, **porous, swollen, and spongy** mass filled with internal aeration pockets.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Dense, stone-like dough indicates fermentation failure or absence of leavening agents.
- **Option B is correct.** Successful fermentation transforms dough into a porous, swollen, spongy matrix filled with \\(\\text{CO}_2\\) gas pockets.
- **Option C is incorrect.** Dough does not liquefy into a translucent runny liquid during normal leavening.
- **Option D is incorrect.** Dough remains hydrated and elastic; it does not turn into dry, crystalline powder."""

q128_sol = """### 1. Scientific Principle & Asexual Reproduction in Ascomycetous Yeasts:
Unicellular yeasts possess distinctive vegetative reproduction mechanisms that allow rapid clonal multiplication under nutrient-replete conditions.

### 2. Biological Process & The Budding Mechanism:
- The primary mode of asexual reproduction in *Saccharomyces cerevisiae* is **budding** (torulation).
- Under favorable temperatures and nutrient availability, a localized softening occurs in the parent cell wall, forming a small cytoplasmic protrusion or **bud**.
- The parent nucleus undergoes mitotic division, and one daughter nucleus migrates into the expanding bud.
- A chitinous septum forms between the mother and daughter cell, and the bud constricts and detaches, leaving a permanent **bud scar** on the parent cell wall.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Multiple fission within a cyst is characteristic of protozoans like *Plasmodium*, not *S. cerevisiae*.
- **Option B is correct.** Yeast reproduces asexually by budding, where a small daughter bulge forms on the parent, receives a mitotic nucleus, and detaches.
- **Option C is incorrect.** Binary transverse fission with equal longitudinal splitting characterizes many bacteria and ciliates, not budding yeast.
- **Option D is incorrect.** Fragmentation of multicellular filaments characterizes filamentous molds and algae (e.g., *Spirogyra*), whereas yeast is unicellular."""

q129_sol = """### 1. Scientific Principle & The Purpose of Leavening:
Unleavened bread (e.g., flatbreads, crackers) consists of a solid, compressed flour matrix that lacks softness. Leavening introduces gaseous voids to yield a palatable, aerated crumb.

### 2. Biological Process & Leavening Mechanics:
- When baker's yeast is incorporated into hydrated wheat flour, it immediately begins fermenting dough sugars.
- The evolution of **carbon dioxide gas (\\(\\text{CO}_2\\))** inflates the dough structure, creating thousands of microscopic cellular cavities.
- During baking, this aeration produces the tender, light, and digestible texture characteristic of high-quality loaf bread.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Yeast is added to produce gas and aerate dough, not to turn bread yellow.
- **Option B is correct.** The primary purpose of adding yeast is to leaven the dough through the enzymatic release of expanding \\(\\text{CO}_2\\) gas bubbles.
- **Option C is incorrect.** Adding yeast does not convert carbohydrates into non-digestible sand; it improves digestibility.
- **Option D is incorrect.** Yeast does not sterilize dough against all bacteria; in fact, sourdough relies on symbiotic coexistence with lactic acid bacteria."""

q130_sol = """### 1. Scientific Principle & Gas Safety in Industrial Fermentation:
Industrial fermentation vessels contain immense volumes of liquid mash undergoing rapid anaerobic glycolysis. Stoichiometrically, each mole of glucose metabolized yields two moles of carbon dioxide gas.

### 2. Biological Process & Safety Management of CO2:
- In distillery fermenters, the rapid release of **carbon dioxide (\\(\\text{CO}_2\\))** displaces atmospheric air.
- Because \\(\\text{CO}_2\\) is denser than air, it pools in low-lying bioreactor pits, presenting a severe risk of lethal asphyxiation to workers if ventilation fails.
- Consequently, modern distilleries install gas scrubbing and recovery towers to safely capture, purify, and liquefy the \\(\\text{CO}_2\\) for commercial sale.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Pure chlorine gas (\\(\\text{Cl}_2\\)) is an industrial chemical element not produced by yeast metabolism.
- **Option B is correct.** Carbon dioxide (\\(\\text{CO}_2\\)) is the heavy gas generated in massive quantities during industrial molasses fermentation that must be safely ventilated or recovered.
- **Option C is incorrect.** Carbon monoxide (\\(\\text{CO}\\)) is generated by incomplete combustion of hydrocarbons, not yeast glycolysis.
- **Option D is incorrect.** Pure oxygen gas (\\(\\text{O}_2\\)) is consumed in aerobic metabolism, not generated during fermentation."""

q131_sol = """### 1. Scientific Principle & Thermal Volatilization of Organic Solvents:
Ethanol is a volatile organic liquid with a significantly lower boiling point than water.

### 2. Biological Process & Alcohol Evaporation during Baking:
- During fermentation, yeast produces equal molar quantities of ethanol and \\(\\text{CO}_2\\).
- Bread dough typically contains \\(0.5\\%\\text{--}1.5\\%\\) alcohol by weight prior to baking.
- Commercial baking ovens operate at temperatures of \\(180^\\circ\\text{C}\\text{--}220^\\circ\\text{C}\\), whereas ethanol has a normal boiling point of \\(78.37^\\circ\\text{C}\\).
- As internal loaf temperature exceeds \\(80^\\circ\\text{C}\\), the ethanol rapidly vaporizes and escapes into the oven atmosphere, leaving the finished bread practically alcohol-free.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Alcohol is not broken down by UV radiation inside dark commercial ovens.
- **Option B is correct.** High oven baking temperatures vaporize and evaporate the ethanol, driving it out of the bread.
- **Option C is incorrect.** Alcohol does not react with table salt to form solid rock crystals.
- **Option D is incorrect.** Alcohol does not turn into poisonous liquid mercury during heating."""

q132_sol = """### 1. Scientific Principle & Autotrophic vs Heterotrophic Classification:
Photosynthetic organisms contain chlorophyll pigments to transduce light into chemical energy, whereas non-photosynthetic organisms depend entirely on preformed organic matter.

### 2. Biological Process & Fungal Nutritional Mode:
- Unlike green algae and terrestrial plants, fungi such as *Saccharomyces cerevisiae* completely **lack chlorophyll** and photosynthetic plastids.
- Consequently, they are incapable of autotrophic photosynthesis and must live as chemoorganoheterotrophic saprophytes, absorbing dissolved sugars directly from their surroundings.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Fungi have well-defined, organized eukaryotic nuclei, not lacking nuclei.
- **Option B is correct.** Fungi are distinguished by their complete absence of chlorophyll and inability to perform photosynthesis.
- **Option C is incorrect.** Many fungi (mushrooms, molds) are multicellular; unicellularity is specific to yeasts, not all fungi.
- **Option D is incorrect.** Fungal cell walls contain chitin and glucan, but lack of photosynthesis is the definitive metabolic distinction."""

q133_sol = """### 1. Scientific Principle & Eukaryotic vs Prokaryotic Cell Organization:
Living organisms are fundamentally divided into prokaryotes (lacking membrane-bound internal organelles) and eukaryotes (possessing compartmentalized intracellular organelles).

### 2. Biological Process & The Yeast Cell Architecture:
- *Saccharomyces cerevisiae* is a unicellular **eukaryote**.
- Under transmission electron microscopy, yeast cells clearly display a double-membrane-bound **nucleus** housing linear chromosomes, along with mitochondria, an endoplasmic reticulum, Golgi apparatus, and vacuoles.
- This sharply distinguishes yeast from prokaryotic bacteria (such as *Lactobacillus* or *Rhizobium*), whose circular DNA resides naked in the cytoplasm.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Prokaryotes are defined by the absence of a nuclear envelope, whereas yeast is a eukaryote.
- **Option B is correct.** All yeast cells possess a well-defined membrane-bound nucleus containing their genetic material.
- **Option C is incorrect.** Yeast cells do not possess photosynthetic chloroplasts.
- **Option D is incorrect.** Flagella are locomotive appendages found in motile bacteria and certain algae; *S. cerevisiae* cells are non-motile and lack flagella."""

q134_sol = """### 1. Scientific Principle & Industrial Economics of Biofuels:
The commercial viability of renewable biofuels depends primarily on feedstock procurement costs, which typically account for \\(60\\%\\text{--}70\\%\\) of total production expenditure.

### 2. Biological Process & Waste Valorization:
- Refined table sugar (pure sucrose) is an expensive food commodity. Using food-grade refined sugar to manufacture automotive fuel would compete with human food supplies and result in prohibitive fuel prices.
- In contrast, **molasses** is an inexpensive, non-edible industrial byproduct generated during sugar refining that contains up to \\(50\\%\\) fermentable sugars.
- Utilizing molasses valorizes industrial agro-waste into valuable bio-ethanol economically without cannibalizing food supplies.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Pure sucrose is readily fermentable; yeast does not require molasses specifically to digest sugar.
- **Option B is correct.** Molasses is an inexpensive industrial agro-waste byproduct rich in sugars, making large-scale bio-ethanol production commercially and economically viable.
- **Option C is incorrect.** Table sugar does not kill yeast; hypertonic concentrations of any sugar cause osmotic stress, but moderate sucrose solutions support rapid fermentation.
- **Option D is incorrect.** Biofuels are combustible fuels; non-combustibility would defeat the purpose of fuel production."""

q135_sol = """### 1. Scientific Principle & Density & Buoyancy in Viscoelastic Foams:
Density is defined as mass per unit volume (\\(\\rho = m / V\\)). When a gas evolves within an expandable, closed fluid or viscoelastic matrix, volume expands while mass remains essentially constant.

### 2. Biological Process & Dough Inflation:
- As yeast produces \\(\\text{CO}_2\\) gas, the gas forms expanding micro-bubbles within the elastic gluten network.
- The total volume (\\(V\\)) of the dough increases substantially (often doubling or tripling).
- Because mass changes negligibly (minor gas escape), the overall bulk density of the dough **decreases** dramatically:
  \\[\\rho_{\\text{dough}} = \\frac{m_{\\text{dough}}}{V_{\\text{expanded}}} \\ll \\rho_{\\text{initial}}\\]
- This density reduction causes the dough to feel light, aerated, and rise buoyant in its proofing container.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Density does not increase; volume increases far more than any negligible mass change, lowering bulk density.
- **Option B is correct.** Dough density decreases as trapped gas bubbles expand the volume, making the dough lighter and causing it to rise.
- **Option C is incorrect.** Dough density does not remain constant; volumetric expansion is the hallmark of leavening.
- **Option D is incorrect.** Density does not drop to zero; dough maintains mass."""

q136_sol = """### 1. Scientific Principle & Industrial Safety & Hazard Identification:
Large-scale biochemical processes generate massive volumes of gases and volatile organic compounds that pose severe physical and chemical hazards if unmanaged.

### 2. Biological Process & Facility Safety:
- **Asphyxiation Hazard:** Anaerobic fermentation vats produce thousands of cubic meters of \\(\\text{CO}_2\\). Because \\(\\text{CO}_2\\) has a molar mass of \\(44\\text{ g/mol}\\) (heavier than air at \\(29\\text{ g/mol}\\)), it settles in basements and enclosed pits, displacing oxygen and causing rapid loss of consciousness and death.
- **Explosion Hazard:** Ethanol is a volatile, flammable liquid with a low flash point (\\(13^\\circ\\text{C}\\)). Vaporized ethanol in closed spaces can ignite or explode upon contact with electrical sparks.
- Therefore, rigorous **mechanical ventilation and air monitoring** are critical life-safety standards in distilleries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Proper ventilation is essential to prevent deadly carbon dioxide asphyxiation and the accumulation of explosive ethanol vapors.
- **Option B is incorrect.** Sealing all air vents completely would trap asphyxiating gases and create a catastrophic explosion risk.
- **Option C is incorrect.** Introducing open flames near ethanol vapors would trigger immediate fires and explosions.
- **Option D is incorrect.** Distilleries rely on liquid water throughout operations; excluding water is impossible and irrelevant to gas safety."""

q137_sol = """### 1. Scientific Principle & Nutritional Requirements of Fermentation:
Cellular glycolysis in *Saccharomyces cerevisiae* requires both a living biocatalyst (viable yeast cells) and an accessible organic carbohydrate substrate.

### 2. Biological Process & Experimental Analysis:
- Consider a standard laboratory setup:
  - **Tube A (Yeast + Distilled Water):** Contains yeast but no carbon source; yeast lacks substrate for glycolysis, producing negligible gas.
  - **Tube B (Yeast + Warm Sugar Solution):** Contains viable yeast cells, accessible carbohydrate substrate, and favorable temperature; glycolysis proceeds rapidly, generating copious \\(\\text{CO}_2\\) bubbles and ethanol.
  - **Tube C (Sugar Solution alone):** Contains substrate but zero yeast biocatalyst; no fermentation can occur.
- Therefore, active fermentation occurs exclusively in **Tube B**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Tube A lacks sugar substrate, preventing fermentation.
- **Option B is correct.** Only Tube B possesses both the active yeast biocatalyst and the fermentable sugar substrate required for fermentation.
- **Option C is incorrect.** Tube C lacks yeast cells, so no enzymatic breakdown occurs.
- **Option D is incorrect.** Tubes without either yeast or sugar cannot undergo fermentation."""

q138_sol = """### 1. Scientific Principle & Mechanical Development of Gluten Proteins:
Flour proteins (gliadin and glutenin) exist in raw unkneaded flour as disordered, randomly folded globular clusters with internal disulfide bonds.

### 2. Biological Process & Gluten Polymerization through Kneading:
- Thorough mechanical kneading applies shear stresses that uncoil and stretch folded glutenin and gliadin polypeptide chains.
- This mechanical alignment allows inter-molecular disulfide (\\(-\\text{S}-\\text{S}-\\)) cross-links and hydrogen bonds to form between adjacent chains, weaving an elastic, cohesive three-dimensional protein mesh.
- This well-developed gluten network possesses high tensile strength and elasticity, which are indispensable for capturing and holding expanding \\(\\text{CO}_2\\) gas bubbles generated by yeast during proofing.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Kneading does not destroy all vitamins; it is a mechanical dough development process.
- **Option B is correct.** Kneading develops and aligns the elastic gluten network, creating the viscoelastic matrix required to trap \\(\\text{CO}_2\\) gas bubbles.
- **Option C is incorrect.** Kneading does not convert wheat protein into insoluble limestone rock.
- **Option D is incorrect.** Kneading does not dry out dough; water must be present for gluten hydration."""

q139_sol = """### 1. Scientific Principle & Thermodynamic Yields: Aerobic vs Anaerobic Respiration:
The complete oxidation of glucose by oxygen yields far more free energy (\\(\\Delta G^\\circ = -2870\\text{ kJ/mol}\\)) than partial anaerobic fermentation (\\(\\Delta G^\\circ = -218\\text{ kJ/mol}\\)).

### 2. Biological Process & ATP Yield Comparison:
- **Aerobic Respiration (with O2):** Glucose is fully oxidized through glycolysis, the pyruvate dehydrogenase complex, the Krebs cycle, and electron transport-coupled oxidative phosphorylation:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\sim 30\\text{--}32\\text{ ATP}\\]
- **Anaerobic Fermentation (without O2):** Pyruvate is reduced to ethanol and \\(\\text{CO}_2\\) without mitochondrial oxidative phosphorylation, generating a net of only:
  \\[\\text{C}_6\\text{H}_{12}\\text{O}_6 \\rightarrow 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 + 2\\text{ ATP}\\]
- Aerobic respiration is roughly \\(15\\text{--}16\\) times more energetically efficient per mole of glucose consumed (Pasteur Effect).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Aerobic respiration yields substantially more metabolic energy (\\(\\sim 30\\text{--}32\\text{ ATP}\\)) per glucose molecule than anaerobic fermentation (\\(2\\text{ ATP}\\)).
- **Option B is incorrect.** Anaerobic fermentation yields far less ATP (only \\(2\\text{ ATP}\\)) because glucose is only partially catabolized.
- **Option C is incorrect.** The energy yields are radically different due to the operation of the electron transport chain in the presence of oxygen.
- **Option D is incorrect.** Yeast cells extract metabolic energy under both conditions, but aerobic respiration yields substantially more."""

q140_sol = """### 1. Scientific Principle & Fractional Distillation & Vapor-Liquid Equilibrium:
Separating miscible liquid components from a homogeneous mixture relies on differences in their thermodynamic physical properties, specifically normal boiling points.

### 2. Biological Process & Ethanol Recovery:
- At the end of fermentation, the fermented wash (mash) contains roughly \\(8\\%\\text{--}12\\%\\) ethanol, with the remainder being water, dissolved solids, and spent yeast cells.
- Because ethanol has a lower normal boiling point (\\(78.37^\\circ\\text{C}\\)) than water (\\(100.0^\\circ\\text{C}\\)) at standard atmospheric pressure, heating the wash in a fractional distillation column vaporizes the ethanol selectively.
- The ethanol-rich vapor rises, enters a condenser, and condenses into concentrated distillate (rectified spirit, \\(\\sim 95\\%\\) alcohol), leaving water and spent solids behind.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Fractional distillation separates ethanol from water based on the significant difference in their normal boiling points.
- **Option B is incorrect.** Magnetic separation separates ferromagnetic minerals, but neither water nor ethanol is magnetic.
- **Option C is incorrect.** Sedimentation separates heavy insoluble particulates (spent yeast cells), but cannot separate miscible ethanol from water.
- **Option D is incorrect.** Ethanol and water are completely miscible in all proportions and cannot be separated with a mechanical kitchen sieve."""

q141_sol = """### 1. Scientific Principle & Metabolic Engineering of Industrial Yeasts:
Wild-type *Saccharomyces cerevisiae* can readily ferment simple hexoses (glucose, fructose), but lacks native pathways to metabolize pentose sugars (such as xylose and arabinose) abundant in lignocellulosic agricultural residues.

### 2. Biological Process & Genetic Optimization:
- Industrial geneticists engineer recombinant *S. cerevisiae* strains by inserting genes for xylose isomerase or xylose reductase/xylitol dehydrogenase from other organisms (e.g., *Pichia stipitis*).
- These engineered strains can simultaneously ferment both hexose and pentose sugars derived from agricultural waste (corn stover, bagasse, wheat straw) into bio-ethanol.
- Furthermore, strains are selected for enhanced ethanol tolerance and thermotolerance, dramatically improving overall biofuel yields and industrial economic viability.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Engineered strains enhance conversion efficiency of diverse agricultural sugars into bio-ethanol, boosting commercial yields.
- **Option B is incorrect.** Biofuel strains are engineered to maximize ethanol output, not to halt ethanol production entirely.
- **Option C is incorrect.** Genetic optimization does not convert fungal yeast into multicellular marine crustaceans.
- **Option D is incorrect.** Engineered yeasts are designed for mass fuel production, not to render fuels toxic or non-flammable."""

# Q142 to Q150: OTF
q142_sol = """### 1. Scientific Principle & Fungal Phylogeny & Vegetative Propagation:
Yeasts are unicellular microfungi that belong phylogenetically to the kingdom Fungi (predominantly Ascomycota).

### 2. Biological Process & The Budding Mechanism:
- Under favorable environmental conditions (moderate temperature, adequate moisture, abundant sugars), *Saccharomyces cerevisiae* reproduces predominantly via an asexual process called **budding**.
- A small daughter outgrowth emerges from the mother cell, receives a mitotic copy of the nucleus, synthesizes a separating septum, and eventually pinches off as an independent daughter yeast cell.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that yeast belongs to the kingdom Fungi and reproduces primarily by budding under favorable conditions. This is scientifically **True**.
- Yeast is an ascomycetous fungus that reproduces asexually by vegetative budding."""

q143_sol = """### 1. Scientific Principle & Heat Transfer & Phase Change in Baking:
Gases and volatile organic solvents expand and volatilize when exposed to elevated temperatures.

### 2. Biological Process & Thermal Escape of Fermentation Products:
- The baking oven operates at \\(180^\\circ\\text{C}\\text{--}220^\\circ\\text{C}\\).
- Ethanol boils at \\(78.37^\\circ\\text{C}\\), causing virtually all alcohol produced during proofing to vaporize and escape into the oven ventilation.
- Concurrently, expanding \\(\\text{CO}_2\\) gas ruptures microscopic cell walls as starch gelatinizes and proteins coagulate, escaping from the bread while leaving permanent open pore networks.
- Therefore, neither alcohol nor \\(\\text{CO}_2\\) remains trapped indefinitely inside baked bread.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that the alcohol and carbon dioxide produced remain trapped inside baked bread indefinitely. This is **False**.
- High oven temperatures vaporize the alcohol and drive out the gas, leaving only the porous solid crumb behind."""

q144_sol = """### 1. Scientific Principle & Microscopic Unicellular Organization:
Biological organisms range from microscopic single cells to massive macroscopic multicellular entities.

### 2. Biological Process & Morphology of Yeast:
- *Saccharomyces cerevisiae* is an obligate **unicellular** microorganism.
- Individual yeast cells measure only \\(3\\text{--}10\\,\\mu\\text{m}\\) in diameter and are completely invisible to the naked human eye.
- They can only be observed individually under compound optical microscopy or scanning electron microscopy.
- While commercial yeast cakes or granules are visible in bulk, they consist of billions of aggregated individual unicellular organisms.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that yeast cells are multicellular organisms visible easily with the naked eye. This is **False**.
- Individual yeast organisms are unicellular microscopic fungi invisible without magnification."""

q145_sol = """### 1. Scientific Principle & Fuel Blending & Oxygenated Additives:
Ethanol is fully miscible with petroleum gasoline and possesses a high research octane number (RON \\(\\sim 108\\)), acting as an effective anti-knock agent and oxygenate.

### 2. Biological Process & Commercial Fuel Blends:
- Anhydrous bio-ethanol produced from the fermentation of sugarcane molasses or grain starch is widely blended with gasoline worldwide:
  - **E10:** \\(10\\%\\) bio-ethanol and \\(90\\%\\) gasoline.
  - **E20:** \\(20\\%\\) bio-ethanol blend, mandated in India's national biofuel roadmap.
  - **E85:** Flex-fuel vehicle blend.
- These blends burn cleaner, reduce toxic carbon monoxide emissions, and decrease reliance on imported fossil crude oil.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that bio-ethanol can be blended with gasoline (petrol) to fuel motor vehicles. This is **True**.
- Bio-ethanol is universally deployed as an automotive fuel blending agent."""

q146_sol = """### 1. Scientific Principle & Chemoorganoheterotrophic Metabolism:
Heterotrophic organisms cannot synthesize organic nutrients from inorganic atmospheric carbon and must acquire carbon skeletons from preformed organic substrates.

### 2. Biological Process & Sugar Catabolism:
- *Saccharomyces cerevisiae* obtains its biological energy and metabolic carbon by breaking down hexose sugars (glucose, fructose) and disaccharides (sucrose, maltose) through glycolysis.
- The free energy liberated during carbon bond cleavage is captured as adenosine triphosphate (ATP) to drive cellular biosynthesis, reproduction, and maintenance.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that yeast cells obtain food and energy by breaking down organic sugars in their environment. This is **True**.
- Yeast is a chemoorganotroph that catabolizes environmental sugars to produce ATP."""

q147_sol = """### 1. Scientific Principle & Facultative Anaerobic Capability:
Organisms that can adjust their catabolic pathways based on molecular oxygen availability are termed facultative anaerobes.

### 2. Biological Process & Metabolic Plasticity:
- In the presence of dissolved oxygen, *Saccharomyces cerevisiae* carries out **aerobic respiration**, fully oxidizing sugars via the TCA cycle and mitochondrial oxidative phosphorylation to generate maximum ATP (\\(\\sim 30\\text{--}32\\text{ ATP}\\)).
- When oxygen is depleted or absent, it shifts to **anaerobic fermentation**, converting pyruvate into ethanol and \\(\\text{CO}_2\\) to regenerate \\(\\text{NAD}^+\\) and maintain ATP synthesis (\\(2\\text{ ATP}\\)).
- This dual capability confirms that yeast is a classic facultative anaerobe.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that yeast can respire both aerobically in the presence of oxygen and anaerobically in its absence. This is **True**.
- Yeast is a textbook example of a facultative anaerobic microorganism."""

q148_sol = """### 1. Scientific Principle & Industrial Media Preparation & Osmotic Regulation:
Industrial raw materials must be chemically and physically standardized to provide an optimal physiological environment for microbial biocatalysts.

### 2. Biological Process & Conditioning of Raw Molasses:
- Raw molasses from sugar mills is an extremely viscous, hypertonic slurry containing \\(70\\%\\text{--}80\\%\\) total solids, with a high osmotic pressure that would rapidly dehydrate and plasmolyze yeast cells.
- Before fermentation, distilleries must:
  1. **Dilute** the molasses with water to an optimal fermentable sugar concentration of \\(15\\%\\text{--}20\\%\\).
  2. **Adjust pH** to \\(4.5\\text{--}5.0\\) using dilute sulfuric acid (inhibiting contaminating bacteria while favoring yeast).
  3. **Supplement nutrients** such as ammonium sulfate (nitrogen source) and urea.
- Therefore, molasses cannot be fermented raw without preparatory dilution and conditioning.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that molasses is directly fermented by yeast without requiring any preparatory dilution or pH adjustment. This is **False**.
- Raw molasses must undergo mandatory dilution, pH adjustment, and nutrient supplementation before fermentation."""

q149_sol = """### 1. Scientific Principle & Fossil Resource Depletion & Energy Security:
Petroleum crude oil is a finite, non-renewable fossil resource formed over millions of years whose combustion depletes terrestrial hydrocarbon reserves.

### 2. Biological Process & Renewable Substitution:
- Bio-ethanol is produced continuously through annual agricultural crop cycles and microbial fermentation of renewable biomass.
- Substituting or blending bio-ethanol into transportation gasoline directly displaces an equivalent volume of refined petroleum, thereby conserving finite petroleum reserves and enhancing domestic energy security.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that bio-ethanol production helps conserve petroleum reserves by providing a renewable alternative liquid fuel. This is **True**.
- Utilizing renewable agricultural bio-ethanol diminishes dependence on and consumption of depleting fossil petroleum reserves."""

q150_sol = """### 1. Scientific Principle & Anaerobic vs Oxidative Metabolism:
Oxidative processes utilize molecular oxygen (\\(\\text{O}_2\\)) as an electron acceptor. In contrast, fermentation is defined biochemically as an anaerobic redox process.

### 2. Biological Process & Anaerobic Glycolysis:
- Fermentation of sugars by yeast is an **anaerobic** process that occurs in the absence of molecular oxygen.
- It does not consume \\(\\text{O}_2\\); instead, an internal organic metabolic intermediate (acetaldehyde) acts as the terminal electron acceptor to regenerate \\(\\text{NAD}^+\\).
- Indeed, bubbling excess oxygen through the medium suppresses alcoholic fermentation in favor of aerobic biomass growth (the Pasteur Effect).

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that fermentation of sugar by yeast is an oxidative process that consumes molecular oxygen from air. This is **False**.
- Fermentation is strictly an anaerobic process that proceeds without consuming molecular oxygen."""

# Solution dictionary for Q103 to Q150
sol_p3 = {
    103: q103_sol, 104: q104_sol, 105: q105_sol, 106: q106_sol, 107: q107_sol, 108: q108_sol,
    109: q109_sol, 110: q110_sol, 111: q111_sol, 112: q112_sol,
    113: q113_sol, 114: q114_sol, 115: q115_sol, 116: q116_sol, 117: q117_sol,
    118: q118_sol, 119: q119_sol, 120: q120_sol, 121: q121_sol, 122: q122_sol,
    123: q123_sol, 124: q124_sol, 125: q125_sol, 126: q126_sol, 127: q127_sol,
    128: q128_sol, 129: q129_sol, 130: q130_sol, 131: q131_sol, 132: q132_sol,
    133: q133_sol, 134: q134_sol, 135: q135_sol, 136: q136_sol, 137: q137_sol,
    138: q138_sol, 139: q139_sol, 140: q140_sol, 141: q141_sol,
    142: q142_sol, 143: q143_sol, 144: q144_sol, 145: q145_sol, 146: q146_sol,
    147: q147_sol, 148: q148_sol, 149: q149_sol, 150: q150_sol
}

# Standardize OAR Q103 to Q108
oar_options = [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
]

part3_full = []

# Q103 to Q108 (OAR)
for idx in range(103, 109):
    raw_item = raw_part3[idx - 103]
    item = {
        "questionCode": raw_item['questionCode'],
        "type": "OAR",
        "text": raw_item['text'],
        "options": oar_options,
        "correctAnswer": "A",
        "solution": sol_p3[idx]
    }
    part3_full.append(item)

# Q109 to Q112 (OMC)
omc_answers = {
    109: ["Availability of fermentable sugars", "Presence of moisture", "Suitable warm temperature range"],
    110: ["Bio-ethanol", "Yeast biomass (single-cell protein)", "Carbon dioxide gas"],
    111: ["Baking leavened bread", "Producing bio-ethanol fuel from molasses", "Brewing alcoholic beverages"],
    112: ["Complete depletion of available sugar substrates", "Extreme thermal shock (boiling or freezing)", "High accumulation of toxic ethanol concentrations that inhibit yeast viability"]
}

for idx in range(109, 113):
    raw_item = raw_part3[idx - 103]
    item = {
        "questionCode": raw_item['questionCode'],
        "type": "OMC",
        "text": raw_item['text'],
        "options": raw_item['options'],
        "correctAnswer": omc_answers[idx],
        "solution": sol_p3[idx]
    }
    part3_full.append(item)

# Q113 to Q141 (OSC)
for idx in range(113, 142):
    raw_item = raw_part3[idx - 103]
    opts = raw_item['options']
    raw_ans = raw_item['correctAnswer']
    
    clean_opts = []
    for opt in opts:
        cleaned_opt = opt.replace(r'\ce{CO2}', r'\(\text{CO}_2\)').replace(r'\ce{O2}', r'\(\text{O}_2\)').replace(r'\ce{H2O}', r'\(\text{H}_2\text{O}\)')
        clean_opts.append(cleaned_opt)
        
    found_letter = None
    letters = ['A', 'B', 'C', 'D']
    for opt_idx, opt in enumerate(opts):
        if raw_ans.strip().lower() in opt.strip().lower() or opt.strip().lower() in raw_ans.strip().lower():
            found_letter = letters[opt_idx]
            break
    if not found_letter:
        print(f"Warning: match not found for Q{idx}, raw_ans: {raw_ans}")
        found_letter = "A"
        
    clean_text = raw_item['text'].replace(r'\ce{CO2}', r'\(\text{CO}_2\)').replace(r'\ce{O2}', r'\(\text{O}_2\)')
    
    item = {
        "questionCode": raw_item['questionCode'],
        "type": "OSC",
        "text": clean_text,
        "options": clean_opts,
        "correctAnswer": found_letter,
        "solution": sol_p3[idx]
    }
    part3_full.append(item)

# Q142 to Q150 (OTF)
otf_ans_p3 = {
    142: "True",
    143: "False",
    144: "False",
    145: "True",
    146: "True",
    147: "True",
    148: "False",
    149: "True",
    150: "False"
}

for idx in range(142, 151):
    raw_item = raw_part3[idx - 103]
    item = {
        "questionCode": raw_item['questionCode'],
        "type": "OTF",
        "text": raw_item['text'],
        "options": ["True", "False"],
        "correctAnswer": otf_ans_p3[idx],
        "solution": sol_p3[idx]
    }
    part3_full.append(item)

print(f"Total Part 3 questions generated: {len(part3_full)}")

# Write scripts/ch8_part3.js
output_js = "// scripts/ch8_part3.js\n"
output_js += "// MH-9-SCIT-8-8.1.3 Useful Microbes: Yeast, Fermentation, Bio-ethanol & Bread (48 questions, Q103 to Q150)\n"
output_js += "const ch8_part3 = " + json.dumps(part3_full, indent=2, ensure_ascii=False) + ";\n\n"
output_js += "module.exports = { ch8_part3 };\n"

with open('scripts/ch8_part3.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Saved scripts/ch8_part3.js successfully!")
