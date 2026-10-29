# scripts/build_part2_full.py
import json
import re

with open('backups/staging/mh9_scit_8_raw.json', 'r', encoding='utf-8') as f:
    raw_all = json.load(f)

raw_part2 = raw_all[52:102]

# Read starter 10 questions from ch8_part2_starter.js
with open('scripts/ch8_part2_starter.js', 'r', encoding='utf-8') as f:
    starter_content = f.read()

# Extract JSON from starter
m = re.search(r'const part2_starter = (\[[\s\S]*?\]);\s*module\.exports', starter_content)
if not m:
    raise ValueError("Could not extract starter array")
starter_10 = json.loads(m.group(1))

print(f"Loaded {len(starter_10)} starter items (Q53 to Q62)")

# Now define rich pedagogical solutions for Q63 to Q102
# Q63: OSC-001 - Host plants of Rhizobium
q63_sol = """### 1. Scientific Principle & Host Specificity:
Biological nitrogen fixation requires a specialized symbiotic habitat capable of sustaining microaerophilic conditions. Members of the legume family (**Fabaceae** or **Leguminosae**) possess unique genetic mechanisms to establish symbiotic partnerships with diazotrophic soil bacteria.

### 2. Biological Process & Host Recognition:
- Plants such as peas (*Pisum sativum*), beans (*Phaseolus*), lentils, soybeans, and clover secrete specific flavonoid signaling molecules from their root hairs into the rhizosphere.
- In response, compatible **Rhizobium** bacteria synthesize lipochitooligosaccharide signaling molecules called **Nod factors**.
- This molecular dialogue initiates root hair curling, cortical cell proliferation, and the formation of specialized root nodules that encapsulate the bacteria.
- In contrast, non-legume monocots (like cereals) and gymnosperms lack the signaling machinery and receptors required for rhizobial infection and nodule organogenesis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Leguminous plants like beans, peas, gram, and clover are the canonical host organisms that develop root nodules harboring *Rhizobium*.
- **Option B is incorrect.** Cereal crops (wheat, rice, maize) are monocots that do not form root nodules with *Rhizobium* (though free-living or associative diazotrophs like *Azotobacter* and *Azospirillum* can colonize their rhizosphere).
- **Option C is incorrect.** Aquatic plants like *Hydrilla* are submerged angiosperms that lack rhizobial nodulation pathways.
- **Option D is incorrect.** Gymnosperms (pines, firs) utilize fungal mycorrhizae for mineral absorption rather than bacterial rhizobial nodules."""

# Q64: OSC-002 - Primary function of Rhizobium
q64_sol = """### 1. Scientific Principle & Biological Nitrogen Fixation:
Molecular nitrogen (\\(\\text{N}_2\\)) constitutes approximately \\(78\\%\\) of Earth's atmosphere, yet eukaryotic plant cells are completely incapable of direct metabolic assimilation because the diatomic triple bond (\\(\\text{N}\\equiv\\text{N}\\)) possesses an immense dissociation enthalpy of \\(945\\text{ kJ/mol}\\).

### 2. Biological Process & Enzymatic Reduction:
- *Rhizobium* bacteria residing inside legume root nodules differentiate into specialized bacteroids expressing the oxygen-labile enzyme **nitrogenase**.
- The enzyme catalyzes the biological reduction of inert atmospheric dinitrogen into bioavailable ammonia (\\(\\text{NH}_3\\)):
  \\[\\text{N}_2 + 8\\text{H}^+ + 8e^- + 16\\text{ATP} \\xrightarrow{\\text{Nitrogenase}} 2\\text{NH}_3 + \\text{H}_2 + 16\\text{ADP} + 16\\text{P}_i\\]
- The resulting ammonia is subsequently assimilated by the host plant into amino acids (glutamine, asparagine), nucleotides, and structural proteins.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Starch storage in plants occurs primarily inside amyloplasts within parenchymatous storage tissues (e.g., tubers, seeds), not through rhizobial activity.
- **Option B is incorrect.** Water absorption is carried out by the plant's root hair epidermis and vascular xylem system.
- **Option C is incorrect.** Photosynthesis takes place in chloroplast-containing green tissues (leaves and green stems) through chlorophyll pigments, whereas *Rhizobium* is a subterranean, non-photosynthetic heterotroph.
- **Option D is correct.** The fundamental evolutionary role of *Rhizobium* in legume root nodules is biological nitrogen fixation."""

# Q65: OSC-003 - Host exchange: what legumes provide
q65_sol = """### 1. Scientific Principle & Mutualistic Symbiosis:
Symbiosis is a bidirectional cooperative interaction between distinct biological species. In the *Rhizobium*-legume association, the energetic cost of breaking the dinitrogen triple bond is substantial, requiring extensive reducing equivalents and metabolic fuel.

### 2. Biological Process & Energetic Exchange:
- The host plant synthesizes carbohydrates (sucrose, glucose) in its leaves via oxygenic photosynthesis.
- These photosynthates are translocated through the phloem down to the root nodules, where host plant enzymes convert sugars into dicarboxylic acids (such as malate and succinate).
- *Rhizobium* bacteroids oxidize these dicarboxylates via their tricarboxylic acid (TCA) cycle and oxidative phosphorylation to produce the copious amounts of ATP (at least \\(16\\text{ ATP}\\) per molecule of \\(\\text{N}_2\\) fixed) and electrons required by nitrogenase.
- In return, the bacteroids export fixed ammonia and amino compounds back to the plant vascular bundle.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Underground root systems have zero access to solar radiation.
- **Option B is incorrect.** While trace minerals are absorbed from soil, the primary metabolic currency supplied by the host to nourish the bacteria is organic carbon.
- **Option C is correct.** Leguminous plants supply energy-yielding food materials (carbohydrates and organic acids) synthesized during photosynthesis to feed the symbiotic bacteria.
- **Option D is incorrect.** Subterranean nodules do not receive gaseous carbon dioxide directly from leaves; carbon arrives as dissolved organic sugars translocated via phloem sap."""

# Q66: OSC-004 - Shape and cellular nature
q66_sol = """### 1. Scientific Principle & Bacterial Taxonomy:
Bacteria are morphologically and structurally categorized according to cell shape, Gram-staining reaction, and cell wall architecture. The genus *Rhizobium* belongs to the class Alphaproteobacteria.

### 2. Biological Process & Cellular Structure:
- When subjected to Christian Gram's differential staining technique, *Rhizobium* cells retain the counterstain safranin (appearing pinkish-red) because their cell envelope possesses a thin peptidoglycan layer enclosed by an outer lipopolysaccharide membrane, defining them as **Gram-negative**.
- Morphologically, free-living *Rhizobium* cells in the soil are motile, non-sporing, cylindrical **rod-shaped** (bacilli) structures.
- Once inside host plant nodule cells, they swell and transform into pleomorphic, irregularly branched bacteroids dedicated to nitrogenase synthesis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** *Rhizobium* bacteria are Gram-negative, rod-shaped prokaryotic microorganisms.
- **Option B is incorrect.** Algae are eukaryotic, photosynthetic organisms containing chloroplasts, whereas *Rhizobium* is a heterotrophic bacterium.
- **Option C is incorrect.** Filamentous fungi are multicellular eukaryotic saprophytes or parasites composed of hyphae (e.g., *Rhizopus*, *Penicillium*).
- **Option D is incorrect.** Protozoa are single-celled eukaryotic heterotrophs (e.g., *Amoeba*, *Plasmodium*), completely distinct from prokaryotic eubacteria."""

# Q67: OSC-005 - Agricultural importance
q67_sol = """### 1. Scientific Principle & Sustainable Agro-Ecosystems:
Modern intensive agriculture often relies heavily on synthetic chemical fertilizers (such as urea and ammonium nitrate) synthesized via the energy-intensive industrial Haber-Bosch process. Excessive chemical fertilization causes soil acidification, soil microbiome degradation, groundwater nitrate contamination, and aquatic eutrophication.

### 2. Biological Process & Ecological Impact:
- Diazotrophic bacteria like *Rhizobium* act as natural, living biofertilizers that convert atmospheric dinitrogen into bioavailable organic and inorganic nitrogen forms directly within the rhizosphere.
- This continuous in-situ nutrient replenishment substantially diminishes the requirement for industrially synthesized synthetic nitrogen fertilizers.
- Furthermore, organic nitrogen released from decaying nodules improves soil aggregate stability, humic matter content, and long-term biological fertility.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Microorganisms do not substitute for irrigation; plants still require water for transpiration, turgor, and metabolic reactions.
- **Option B is correct.** *Rhizobium* diminishes dependency on synthetic nitrogen fertilizers by enriching soil fertility biologically and sustainably.
- **Option C is incorrect.** Biological nitrogen fixation does not impart broad-spectrum immunity against plant viruses.
- **Option D is incorrect.** Fruit ripening is governed primarily by plant phytohormones (ethylene) rather than rhizobial nitrogen fixation."""

# Q68: OSC-006 - Root response to infection
q68_sol = """### 1. Scientific Principle & Organogenesis:
Unlike pathogenic bacterial infections that cause necrotic decay, rhizobial infection triggers a tightly orchestrated developmental reprogramming in host legume root tissues.

### 2. Biological Process & Nodule Morphogenesis:
- Following rhizobial entry via curled root hairs through an intracellular tubular **infection thread**, bacterial Nod factors trigger localized mitotic reactivation in the root inner cortex and pericycle.
- These newly dividing cortical cells undergo continuous division and differentiation, forming a vascularized, specialized organ called a **root nodule**.
- The bacteria are released from the infection thread into the host cortical cytoplasm enclosed in host-derived peribacteroid membranes, transforming into active bacteroids.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Subterranean root nodules remain non-photosynthetic and do not develop chlorophyll pigments.
- **Option B is incorrect.** Root tissues do not turn woody or arrest development; rather, they form localized, metabolically hyperactive parenchymatous nodules.
- **Option C is incorrect.** Roots do not dissolve or undergo tissue liquefaction; host architecture is preserved and modified.
- **Option D is correct.** Host root cortical cells undergo localized hyperplastic cell divisions, resulting in characteristic macroscopic swellings known as root nodules."""

# Q69: OSC-007 - Nitrogenase enzyme
q69_sol = """### 1. Scientific Principle & Dinitrogen Reduction:
The diatomic nitrogen molecule (\\(\\text{N}_2\\)) contains a formidable covalent triple bond consisting of one \\(\\sigma\\) bond and two \\(\\pi\\) bonds. Catalytic cleaving of this bond at ambient temperature and pressure requires a specialized metalloenzyme.

### 2. Biological Process & Nitrogenase Complex:
- The **nitrogenase** enzyme complex comprises two essential catalytic protein components:
  1. **Fe-protein (Dinitrogenase reductase):** An iron-sulfur protein that binds ATP and transfers electrons with high reducing power.
  2. **MoFe-protein (Dinitrogenase):** A molybdenum-iron protein containing the FeMo-cofactor that binds dinitrogen and catalyzes its step-by-step reduction into ammonia:
     \\[\\text{N}_2 \\xrightarrow{+2\\text{H}^+, +2e^-} \\text{HN}=\\text{NH} \\xrightarrow{+2\\text{H}^+, +2e^-} \\text{H}_2\\text{N}-\\text{NH}_2 \\xrightarrow{+2\\text{H}^+, +2e^-} 2\\text{NH}_3\\]
- This multi-electron transfer cascade requires immense metabolic energy (\\(16\\text{ ATP}\\) per dinitrogen reduced).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Amylase is a hydrolytic carbohydrate enzyme that breaks down starch into maltose.
- **Option B is correct.** The nitrogenase enzyme complex is the unique catalytic machinery responsible for reducing atmospheric \\(\\text{N}_2\\) to ammonia.
- **Option C is incorrect.** Lipase hydrolyzes ester bonds in neutral triglycerides to yield glycerol and fatty acids.
- **Option D is incorrect.** Cellulase hydrolyzes \\(\\beta\\)-1,4-glycosidic linkages in cellulose plant cell walls."""

# Q70: OSC-008 - Role of leghemoglobin
q70_sol = """### 1. Scientific Principle & The Oxygen Paradox:
Nitrogenase requires a vast supply of ATP generated by aerobic cellular respiration in bacteroids; however, the Fe and MoFe subunits of the nitrogenase enzyme are irreversibly inactivated by free molecular oxygen (\\(\\text{O}_2\\)).

### 2. Biological Process & Oxygen Scavenging:
- To resolve this evolutionary conflict, host legume cells and *Rhizobium* bacteroids collaboratively synthesize **leghemoglobin**: the plant gene encodes the apoprotein globin, while the bacterium synthesizes the iron-porphyrin heme group.
- Leghemoglobin possesses an extraordinarily high affinity for oxygen (an association rate roughly \\(10\\) times higher than human myoglobin).
- It acts as an oxygen buffer and scavenger: maintaining the concentration of free, uncomplexed \\(\\text{O}_2\\) at nanomolar levels (preventing nitrogenase denaturation) while delivering a steady flux of bound oxygen directly to the bacteroid respiratory chain for oxidative phosphorylation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Subterranean roots do not conduct photosynthesis; leghemoglobin has no light-harvesting function.
- **Option B is incorrect.** Structural wall rigidity is conferred by cellulose microfibrils and pectin, not soluble globular hemoproteins.
- **Option C is correct.** Leghemoglobin regulates and buffers oxygen tension, safeguarding the oxygen-sensitive nitrogenase enzyme while sustaining bacteroid respiration.
- **Option D is incorrect.** Starch storage in root tissues is mediated by plastids (amyloplasts), not heme proteins."""

# Q71: OSC-009 - Seed inoculation
q71_sol = """### 1. Scientific Principle & Microbial Inoculants:
Agricultural soils, particularly those where a specific legume crop has never been cultivated or where environmental stresses (drought, extreme soil pH, excessive pesticide use) have depleted the native microbiota, frequently lack compatible, effective rhizobial strains.

### 2. Biological Process & Inoculation Mechanism:
- **Seed inoculation** (bacterization) involves coating legume seeds prior to sowing with a slurry containing a high-titer carrier-based culture (often peat or lignite formulation) of live, compatible *Rhizobium* strains alongside an adhesive (such as jaggery solution or gum arabic).
- Upon seed germination, the inoculated bacteria multiply rapidly in the emerging rhizosphere, ensuring immediate colonization of nascent root hairs and prompt establishment of effective nitrogen-fixing nodules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Rhizobial inoculation does not alter the intrinsic sugar profile or sweetness of dry legume seeds.
- **Option B is correct.** Seed inoculation guarantees an abundant population of compatible, high-efficiency nitrogen-fixing bacteria to initiate early nodulation.
- **Option C is incorrect.** Seed inoculation is a biological fertilization method, not an aesthetic coloring process.
- **Option D is incorrect.** Rhizobium does not inhibit water imbibition; seed hydration and germination proceed normally."""

# Q72: OSC-010 - Nitrogen forms absorbed by plants
q72_sol = """### 1. Scientific Principle & Plant Mineral Nutrition:
Vascular plants cannot incorporate elemental dinitrogen directly into their biochemical pathways. They rely on root transport proteins that recognize specific inorganic nitrogenous ions.

### 2. Biological Process & Nitrogen Assimilation:
- Within the root nodule, *Rhizobium* nitrogenase produces ammonia (\\(\\text{NH}_3\\)), which at biological pH rapidly protonates into ammonium ions (\\(\\text{NH}_4^+\\)).
- The ammonium is assimilated by host enzymes (such as glutamine synthetase and glutamate synthase, the GS-GOGAT pathway) into amino acids (glutamine, glutamate, and ureides like allantoin).
- When nodules decay or soil bacteria nitrify excreted compounds, soil nitrogen persists as **ammonium (\\(\\text{NH}_4^+\\))** and **nitrate (\\(\\text{NO}_3^-\\))** ions, which are absorbed by root ion-transporters and incorporated into plant biomass.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Plants do not absorb toxic atmospheric nitrogen dioxide gas directly from soil for nutrition.
- **Option B is correct.** Plants absorb and assimilate nitrogen primarily in the form of ammonium and nitrate ions (and amino acids formed from fixed ammonia).
- **Option C is incorrect.** Elemental dinitrogen gas is biologically inert to plant root uptake mechanisms.
- **Option D is incorrect.** Nitrous oxide (\\(\\text{N}_2\\text{O}\\)) is a volatile greenhouse gas produced during denitrification, not an absorbable plant nutrient."""

# Q73: OSC-011 - Appearance of active nodule
q73_sol = """### 1. Scientific Principle & Leghemoglobin Chromophore:
The functional viability of a root nodule can be assessed macroscopically by inspecting the color of its internal bacteroid zone.

### 2. Biological Process & Chromogenic State:
- A healthy, actively fixing legume root nodule contains high concentrations of the oxygen-binding hemoprotein **leghemoglobin**.
- Because leghemoglobin contains an iron-protoporphyrin IX prosthetic group structurally homologous to animal hemoglobin, it imparts an unmistakable **pink to deep reddish** coloration to the internal nodular tissue when sliced transversely.
- In contrast, ineffective, senescent, or uninfected nodules appear white (lacking leghemoglobin) or pale green/brown (where the heme group has degraded into biliverdin-like breakdown products).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Deep jet black coloration typically indicates necrotic fungal rot or advanced tissue decay.
- **Option B is correct.** Actively fixing nodules exhibit a distinct pink or reddish interior due to the abundance of leghemoglobin.
- **Option C is incorrect.** Bright translucent blue is not a biological coloration found in legume nodular tissues.
- **Option D is incorrect.** Pure chalky white internal tissue characterizes uninfected, young, or ineffective nodules devoid of leghemoglobin."""

# Q74: OSC-012 - Direct initial product of N2 fixation
q74_sol = """### 1. Scientific Principle & Biochemical Stoichiometry:
Biological nitrogen fixation is an electron-reduction process that sequentially hydrogenates the dinitrogen molecule.

### 2. Biological Process & The Reaction Product:
- The nitrogenase enzyme binds atmospheric dinitrogen (\\(\\text{N}_2\\)) and couples the hydrolysis of \\(16\\text{ ATP}\\) to the transfer of \\(8\\) electrons and \\(8\\) protons:
  \\[\\text{N}_2 + 8\\text{H}^+ + 8e^- + 16\\text{ATP} \\xrightarrow{\\text{Nitrogenase}} 2\\text{NH}_3 + \\text{H}_2 + 16\\text{ADP} + 16\\text{P}_i\\]
- The direct chemical product synthesized at the enzyme's catalytic metal center is **ammonia (\\(\\text{NH}_3\\))**, accompanied by an obligate molecule of hydrogen gas (\\(\\text{H}_2\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Carbon dioxide (\\(\\text{CO}_2\\)) is a respiratory byproduct released during decarboxylation reactions, not a product of nitrogen fixation.
- **Option B is incorrect.** Sodium chloride (\\(\\text{NaCl}\\)) is an inorganic mineral salt unrelated to dinitrogen reduction.
- **Option C is correct.** Ammonia (\\(\\text{NH}_3\\)) is the direct initial chemical product of biological dinitrogen reduction by nitrogenase.
- **Option D is incorrect.** Sulfur trioxide (\\(\\text{SO}_3\\)) is an industrial sulfur oxide compound and a strong acid anhydride, not produced in biological nitrogen fixation."""

# Q75: OSC-013 - Inhibitory environmental factors
q75_sol = """### 1. Scientific Principle & Energetic Cost & Feedback Regulation:
Biological nitrogen fixation is one of the most energy-demanding metabolic processes in biology, requiring upwards of \\(16\\text{--}24\\text{ ATP}\\) per molecule of dinitrogen reduced. Consequently, host legumes possess negative feedback loops to regulate nodulation according to soil nutrient availability.

### 2. Biological Process & Nitrate Inhibition:
- When agricultural soil contains high concentrations of pre-formed mineral nitrogen (such as synthetic nitrates or ammonium fertilizers), the plant absorbs these ions directly with minimal metabolic expenditure.
- High systemic nitrate triggers an autoregulation of nodulation (AON) signaling cascade via leaf-derived peptide hormones, which actively suppresses root hair curling, cortical cell divisions, and nodule initiation.
- Existing nodules may senesce prematurely because the plant redirects photosynthetic carbon away from the bacteroids toward shoot vegetative growth.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Adequate moisture is essential for rhizobial survival, motility, root hair infection, and plant transpiration.
- **Option B is incorrect.** Legume root exudates (rich in flavonoids) stimulate nodulation by inducing rhizobial nod genes.
- **Option C is correct.** High concentrations of available mineral nitrogen (nitrates/ammonium) actively suppress and inhibit root nodule formation and nitrogen fixation efficiency.
- **Option D is incorrect.** A neutral to slightly alkaline soil pH (\\(6.5\\text{--}7.5\\)) is optimal for rhizobial viability and nodulation."""

# Q76: OSC-014 - Type of interaction
q76_sol = """### 1. Scientific Principle & Ecological Interactions:
Ecological relationships between different species in an ecosystem are classified by their net fitness outcomes: mutualism \\((+/+)\\), commensalism \\((+/0)\\), parasitism \\((+/-)\\), or competition \\((-/-)\\).

### 2. Biological Process & The Legume-Rhizobium Partnership:
- The interaction between *Rhizobium* and leguminous plants is a classic paradigm of **mutualism (symbiosis)**:
  - **Benefit to the plant \\((+)\\):** Receives a continuous supply of bioavailable reduced nitrogen (ammonia/amino acids) for protein synthesis and vigorous growth.
  - **Benefit to the bacterium \\((+)\\):** Obtains a protected microenvironment inside root nodule cells and a dependable supply of organic carbon (malate, succinate) derived from plant photosynthesis.
- Both partners derive substantial reciprocal fitness benefits, confirming a \\((+/+)\\) mutualistic relationship.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Commensalism \\((+/0)\\) benefits one species while leaving the host unaffected, which does not match this mutually beneficial system.
- **Option B is incorrect.** Competition \\((-/-)\\) involves rival species contesting limited resources, causing mutual detriment.
- **Option C is correct.** The *Rhizobium*-legume partnership is a mutualistic symbiotic interaction where both organisms derive vital physiological advantages.
- **Option D is incorrect.** Predation \\((+/-)\\) involves one organism killing and consuming another."""

# Q77: OSC-015 - Nutrient element received
q77_sol = """### 1. Scientific Principle & Essential Macro-Nutrients:
Plants require critical macronutrients for survival, traditionally abbreviated as NPK (Nitrogen, Phosphorus, Potassium). Among these, nitrogen is required in the largest quantity for synthesizing amino acids, structural and enzymatic proteins, nucleic acids (DNA and RNA), and chlorophyll molecules.

### 2. Biological Process & Rhizobial Contribution:
- *Rhizobium* bacteria possess the unique enzymatic capability to fix atmospheric dinitrogen (\\(\\text{N}_2\\)).
- The bacteria convert dinitrogen into ammonia (\\(\\text{NH}_3\\)) and transfer it directly to the host plant vascular tissues.
- Thus, the primary direct nutritional element supplied by *Rhizobium* to the host legume is **nitrogen**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Potassium is absorbed directly from soil water as \\(\\text{K}^+\\) ions through root cation transport channels.
- **Option B is incorrect.** Phosphorus is absorbed as phosphate ions (\\(\\text{H}_2\\text{PO}_4^-\\)), frequently assisted by mycorrhizal fungi rather than *Rhizobium*.
- **Option C is correct.** Nitrogen is the specific essential nutrient element fixed and delivered by *Rhizobium* bacteroids to the host plant.
- **Option D is incorrect.** Calcium is absorbed as divalent \\(\\text{Ca}^{2+}\\) ions from soil solutions via passive apoplastic flow."""

# Q78: OSC-016 - Soil fertility maintenance
q78_sol = """### 1. Scientific Principle & Biological Soil Enrichment:
Leguminous crops play a central role in organic and low-input sustainable farming systems because they enrich soil nitrogen reservoirs without consuming synthetic petrochemical inputs.

### 2. Biological Process & Nitrogen Sloughing and Turnover:
- As leguminous crops grow, a portion of the fixed nitrogen is continually released into the surrounding rhizosphere via root exudates and decaying nodule tissues.
- Following harvest, substantial quantities of fixed nitrogen remain sequestered within root crowns, nodules, and agricultural stubble.
- When soil saprophytic microbes decompose these organic residues (mineralization and ammonification), bioavailable ammonium and nitrate compounds are released into the topsoil, leaving the field enriched for subsequent crops.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Leguminous crops replenish soil fertility naturally by fixing atmospheric nitrogen through symbiotic bacteria housed in root nodules.
- **Option B is incorrect.** Plants cannot synthesize synthetic urea (carbamide) in their stems; urea is manufactured industrially or excreted by mammals.
- **Option C is incorrect.** Extracting heavy metals describes phytoremediation, not agricultural soil nutrient replenishment.
- **Option D is incorrect.** Legumes do not secrete toxic herbicidal acids that kill weeds as a mechanism of soil enrichment."""

# Q79: OSC-017 - Physical housing structure
q79_sol = """### 1. Scientific Principle & Specialized Symbiotic Organs:
Unlike free-living nitrogen fixers that operate dispersed in bulk soil, symbiotic rhizobia reside inside dedicated host morphological structures designed to maintain high bacterial density and controlled oxygen levels.

### 2. Biological Process & Root Nodule Anatomy:
- The specialized structures housing *Rhizobium* bacteria are **root nodules**.
- A root nodule consists of an outer protective cortex, a peripheral vascular system connected to the plant stele, an internal oxygen-diffusion barrier, and an infected central zone packed with host plant cells containing thousands of bacteroids enclosed in symbiosomes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Root hairs are unicellular epidermal extensions that serve as initial points of infection and curling, but do not house the mature bacteroid colonies.
- **Option B is correct.** Root nodules are the macroscopic, specialized anatomical structures that house and support symbiotic *Rhizobium* colonies.
- **Option C is incorrect.** Xylem vessels are hollow, dead, lignified tubes specialized for unidirectional conduction of water and dissolved minerals.
- **Option D is incorrect.** Lateral root caps are protective tissues that shield root apical meristems from mechanical abrasion during soil penetration."""

# Q80: OSC-018 - Non-legume identification
q80_sol = """### 1. Scientific Principle & Phylogenetic Constraints of Nodulation:
The genetic capacity to establish symbiotic root nodules with *Rhizobium* is almost exclusively restricted to flowering plants within the nitrogen-fixing clade of angiosperms, predominantly the family **Fabaceae** (Leguminosae).

### 2. Biological Process & Host Range:
- **Legumes:** Peas (*Pisum sativum*), beans (*Phaseolus*), lentils (*Lens culinaris*), soybeans (*Glycine max*), chickpeas (*Cicer arietinum*), and groundnuts (*Arachis hypogaea*) readily form root nodules with compatible *Rhizobium* species.
- **Non-legumes:** **Maize** (*Zea mays*) is a member of the grass family (**Poaceae**), a monocotyledonous cereal crop. Maize lacks the genetic and physiological apparatus to perceive Nod factors and develop root nodules with *Rhizobium*.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Pea is a canonical legume that forms typical indeterminate root nodules with *Rhizobium leguminosarum*.
- **Option B is incorrect.** Bean is a leguminous crop that nodulates actively with *Rhizobium phaseoli*.
- **Option C is incorrect.** Groundnut (peanut) is an oilseed legume that develops determinate root nodules harboring *Bradyrhizobium*.
- **Option D is correct.** Maize is a cereal grass (Poaceae), not a legume, and therefore does not form symbiotic root nodules with *Rhizobium*."""

# Q81: OSC-019 - Root exudates signaling
q81_sol = """### 1. Scientific Principle & Rhizosphere Chemotaxis:
The establishment of symbiosis is initiated by molecular communication between the plant root and compatible free-living soil microbes before physical contact occurs.

### 2. Biological Process & Molecular Signaling:
- Emerging legume roots continually release specialized **root exudates** into the surrounding soil.
- These exudates contain aromatic secondary metabolites, specifically **flavonoids**, isoflavones, and betaines (e.g., luteolin, daidzein).
- Compatible *Rhizobium* bacteria detect these chemical gradients via positive chemotaxis, swimming toward the root hair surface.
- Concurrently, flavonoids diffuse into the bacterial cytoplasm and bind to the constitutively expressed bacterial regulatory protein **NodD**, activating the transcription of the bacterial *nod* operons required for infection thread formation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Healthy root exudates foster beneficial microbial diversity rather than acting as non-specific biocides.
- **Option B is correct.** Root exudates chemically signal, attract, and activate compatible *Rhizobium* bacteria toward the root surface.
- **Option C is incorrect.** Gaseous atmospheric nitrogen is fixed enzymatically by nitrogenase inside bacteroids, not crystallized by exudates.
- **Option D is incorrect.** Root exudates do not dissolve soil to create physical cavities; root growth occurs via mechanical expansion and cell elongation."""

# Q82: OSC-020 - Introducing Rhizobium to new fields
q82_sol = """### 1. Scientific Principle & Soil Inoculation Agronomy:
When cultivating a leguminous crop in a virgin field or land previously restricted to non-leguminous monocultures, indigenous soils typically lack sufficient populations of the host-specific *Rhizobium* strain.

### 2. Biological Process & Biofertilizer Application:
- To ensure robust nodulation and early nitrogen fixation, agriculturalists apply **commercial Rhizobium biofertilizer inoculants**.
- These preparations consist of pure, laboratory-cultured, highly competitive bacterial strains formulated in sterile carrier media (such as peat, lignite, or liquid suspensions).
- Inoculants are applied directly as a seed dressing (seed coating with an organic binder) or introduced as in-furrow soil granulates during sowing, guaranteeing immediate root contact during germination.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Flooding fields with seawater causes severe salinization, osmotic shock, and rapid death of glycophytic crops and beneficial microbes.
- **Option B is incorrect.** Spraying sulfuric acid acidifies the soil to lethal levels, destroying soil microbiota and releasing toxic aluminum ions.
- **Option C is correct.** Applying commercial *Rhizobium* biofertilizer inoculants to seeds or soil is the standard, scientifically proven method to establish compatible diazotrophs.
- **Option D is incorrect.** Burning crop stubble incinerates organic matter, sterilizes topsoil microbiomes, and causes severe atmospheric air pollution."""

# Q83: OSC-021 - Crop rotation agronomic value
q83_sol = """### 1. Scientific Principle & Agro-Ecological Nutrient Cycling:
Cereal grains (such as wheat, rice, and maize) are exhaustive nitrogen feeders that systematically deplete available soil nitrate and ammonium reserves, degrading soil health if maintained in continuous monoculture.

### 2. Biological Process & The Rotation Advantage:
- Incorporating legumes into a **crop rotation** cycle restores soil biochemical balance.
- Symbiotic *Rhizobium* bacteria in legume root nodules convert atmospheric \\(\\text{N}_2\\) into organic nitrogen compounds.
- Significant quantities of this fixed nitrogen remain in the soil as decomposing root nodules, root biomass, and crop residue after harvest.
- This natural enrichment provides readily available mineral nitrogen for the succeeding cereal crop, breaking pest and pathogen life cycles while significantly lowering fertilizer expenditure.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Crop rotation enhances soil organic crumb structure and cation exchange capacity; it does not turn clay into sand.
- **Option B is incorrect.** Crop rotation promotes soil biodiversity and earthworm populations rather than eradicating them.
- **Option C is incorrect.** Sunlight remains an absolute, non-negotiable requirement for plant photosynthesis regardless of rotation schemes.
- **Option D is correct.** Crop rotation with legumes naturally replenishes soil nitrogen reserves depleted by previous heavy-feeding cereal crops."""

# Q84: OSC-022 - Post-harvest fate of nodules & green manuring
q84_sol = """### 1. Scientific Principle & Decomposition & Mineralization:
Organic matter incorporated into soil undergoes microbial decomposition, transforming complex biological macromolecules into simpler inorganic nutrients accessible to root systems.

### 2. Biological Process & Green Manure Decomposition:
- In agricultural **green manuring**, leguminous crops (such as sunn hemp, *Sesbania*, or clover) or post-harvest legume root residue are plowed directly into the topsoil.
- Soil heterotrophic bacteria and fungi decompose the protein-rich root nodules and vegetative tissues through **ammonification**:
  \\[\\text{Organic Nitrogen (Proteins/Amino acids)} \\xrightarrow{\\text{Ammonifiers}} \\text{NH}_4^+\\]
- Subsequent aerobic nitrifying bacteria (*Nitrosomonas* and *Nitrobacter*) convert ammonium into nitrate (\\(\\text{NO}_3^-\\)), significantly elevating plant-available mineral fertility for the next crop.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Decomposing organic matter does not evaporate into elemental oxygen; carbon is released as \\(\\text{CO}_2\\) while nitrogen is converted into inorganic ions.
- **Option B is correct.** Post-harvest decomposition of root nodules mineralizes organically bound nitrogen into bioavailable ammonium and nitrate, enriching the soil.
- **Option C is incorrect.** Organic decomposition is a non-radioactive biological recycling process.
- **Option D is incorrect.** Organic matter breaks down into soil humus and mineral ions; it does not petrify into permanent rock structures."""

# Q85: OSC-023 - Gas captured in fixation
q85_sol = """### 1. Scientific Principle & The Biogeochemical Nitrogen Cycle:
Earth's atmosphere acts as an immense chemical reservoir of elemental nitrogen gas, existing predominantly as inert diatomic molecules.

### 2. Biological Process & Gaseous Reduction:
- Biological nitrogen fixation specifically captures and transforms gaseous **nitrogen (\\(\\text{N}_2\\))** present in the interstitial air spaces of porous soil.
- The nitrogenase enzyme binds \\(\\text{N}_2\\) and catalyzes its reduction to ammonia (\\(\\text{NH}_3\\)), transforming a previously inaccessible atmospheric gas into a biologically reactive chemical species that enters the global food web.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Oxygen (\\(\\text{O}_2\\)) is utilized in aerobic respiration, but its presence at the nitrogenase active site irreversibly inactivates the enzyme.
- **Option B is incorrect.** Carbon dioxide (\\(\\text{CO}_2\\)) is captured during photosynthetic carbon fixation via the Calvin cycle (Rubisco enzyme), not nitrogen fixation.
- **Option C is correct.** Atmospheric nitrogen gas (\\(\\text{N}_2\\)) is the specific chemical substrate captured and reduced during biological nitrogen fixation.
- **Option D is incorrect.** Hydrogen gas (\\(\\text{H}_2\\)) is an obligate byproduct generated during nitrogenase catalysis, not the initial captured reactant."""

# Q86: OSC-024 - Bacterial entry pathway
q86_sol = """### 1. Scientific Principle & Plant Infection Pathways:
Rhizobial infection represents a non-destructive, host-regulated invasion process that relies on specialized host structural modifications rather than mechanical wounding.

### 2. Biological Process & Infection Thread Dynamics:
- *Rhizobium* bacteria adhere to the tip of an emerging legume root hair, secreting Nod factors that induce dramatic tip curling into a "shepherd's crook" structure.
- The bacteria become entrapped in the fold; localized hydrolytic softening of the plant cell wall occurs, and the plant invaginates its plasma membrane to form an inward-growing tubular structure called an **infection thread**.
- The bacteria divide and migrate internally along this plant-synthesized infection thread through the epidermal and outer cortical cell layers toward the newly dividing inner cortex.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** *Rhizobium* enters host roots via root hair curling and inward migration through an infection thread.
- **Option B is incorrect.** Rhizobial infection is a natural soil microbiological process independent of insect vectoring.
- **Option C is incorrect.** Root-nodulating bacteria do not enter through floral organs or aerial petals.
- **Option D is incorrect.** Nodulation occurs in tender, primary root zones of herbaceous legumes, not through dead outer tree bark pores (lenticels)."""

# Q87: OSC-025 - Macroscopic indicator of symbiosis
q87_sol = """### 1. Scientific Principle & Agronomic Field Diagnostics:
Farmers and agronomists evaluate the success of rhizobial colonization by directly examining the morphological characteristics of washed root systems.

### 2. Biological Process & Visual Hallmark:
- Successful, active colonization manifests macroscopically as discrete, spherical, or elongated **pinkish-red root nodules** clustered prominently around the primary taproot and proximal lateral roots.
- The presence of plump, pink nodules confirms that infection thread progression, cortical organogenesis, bacteroid differentiation, and leghemoglobin synthesis have proceeded successfully.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** The macroscopic presence of plump, pinkish root nodules confirms successful establishment of effective *Rhizobium* symbiosis.
- **Option B is incorrect.** Plant leaf venation color is determined by chlorophyll and anthocyanins; Rhizobium infection does not produce blue veins.
- **Option C is incorrect.** Roots remain flexible and cylindrical; they do not metamorphose into sclerified thorns.
- **Option D is incorrect.** Root hairs remain abundant and functional across expanding root zones."""

# Q88: OSC-026 - Maximizing benefits in fields
q88_sol = """### 1. Scientific Principle & Agronomic Sustainability:
To optimize biological nitrogen fixation on a farm scale, crop cultivation cycles must strategically leverage the legacy nitrogen left behind by legumes.

### 2. Biological Process & Strategic Rotation:
- The optimal agricultural strategy is **crop rotation alternating leguminous crops with non-leguminous cereals or cash crops**.
- The legume phase replenishes soil nitrogen, improves organic matter, and breaks persistent weed and insect cycles.
- The subsequent cereal phase exploits this biological nitrogen, maximizing yield while minimizing expensive synthetic chemical inputs.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Alternating legumes with non-legumes in systematic crop rotation maximizes biological nitrogen input and sustains soil fertility.
- **Option B is incorrect.** Depriving fields of water induces severe drought stress, collapsing plant turgor and killing beneficial soil bacteria.
- **Option C is incorrect.** Chemical soil sterilization annihilates all beneficial microbial communities, severely degrading agricultural productivity.
- **Option D is incorrect.** Continuous cereal monoculture with heavy synthetic urea causes nutrient exhaustion, soil acidification, and pest outbreaks."""

# Q89: OSC-027 - Bacteroid differentiation fate
q89_sol = """### 1. Scientific Principle & Terminal Cellular Differentiation:
Inside host nodule cells, *Rhizobium* bacteria undergo extensive developmental and morphological remodeling that adapts them specifically for hyperactive catalytic function.

### 2. Biological Process & The Bacteroid State:
- Upon release from the infection thread into the host cell cytoplasm, each bacterium becomes surrounded by a host-derived membrane (peribacteroid membrane) to form a **symbiosome**.
- In many legumes (especially galegoid legumes like peas and alfalfa), the bacteria undergo endoreduplication (genome amplification without cytokinesis), swell up to several times their original volume, and transform into irregularly shaped **bacteroids**.
- These bacteroids dedicate their metabolic machinery almost entirely to synthesizing nitrogenase and fixing nitrogen; in doing so, they undergo terminal differentiation, largely losing the capacity for independent vegetative reproduction.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** *Rhizobium* is a prokaryotic eubacterium that cannot transform into eukaryotic fungal spores.
- **Option B is incorrect.** Bacteroids remain strictly confined inside subterranean root nodule symbiosomes.
- **Option C is incorrect.** Bacteroids remain heterotrophic in underground dark root cells and do not synthesize chlorophyll.
- **Option D is correct.** Differentiated bacteroids specialize in nitrogen fixation and lose their capacity for independent cell division and free-living reproduction."""

# Q90: OSC-028 - Impact of excessive synthetic fertilizer
q90_sol = """### 1. Scientific Principle & Autoregulation of Nodulation (AON):
Biological nitrogen fixation requires heavy photosynthetic investment from the host plant (upwards of \\(20\\%\\) of total photosynthate is partitioned to root nodules). Plants possess regulatory systems to avoid wasting carbon when inorganic nitrogen is already saturating the soil.

### 2. Biological Process & Repression Mechanism:
- In soils saturated with synthetic ammonium nitrate or urea, host plants absorb inorganic nitrate (\\(\\text{NO}_3^-\\)) and ammonium (\\(\\text{NH}_4^+\\)) directly via low-energy root transporter proteins.
- High intracellular nitrate triggers the synthesis of CLE-family signaling peptides in roots, which travel through xylem to the shoots, binding to leucine-rich repeat receptor kinases (such as NARK/SUNN).
- This triggers a shoot-to-root descending signal that downregulates nodule initiation, suppresses infection thread development, and halts nitrogenase expression, severely inhibiting nodulation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect.** Synthetic fertilizers do not stimulate symbiotic nodulation; high mineral nitrogen actively suppresses it.
- **Option B is correct.** Nodulation and biological nitrogen fixation are severely inhibited because the host plant conserves energy by assimilating pre-formed mineral nitrogen.
- **Option C is incorrect.** Nodules do not swell abnormally or turn into storage tubers under excess mineral nitrogen; their development is arrested.
- **Option D is incorrect.** Plant roots do not self-destruct or undergo complete necrosis solely from standard chemical nitrogen application."""

# Q91: OSC-029 - Co-evolutionary significance
q91_sol = """### 1. Scientific Principle & Co-Evolutionary Ecology:
Throughout evolutionary history, nitrogen availability has served as a primary limiting factor constraining terrestrial primary productivity.

### 2. Biological Process & The Evolutionary Breakthrough:
- The co-evolution of legumes and diazotrophic *Rhizobium* represents an evolutionary adaptation to nitrogen-deficient soils.
- By outsourcing the energetically expensive reduction of atmospheric \\(\\text{N}_2\\) to specialized bacterial symbionts in exchange for photosynthetic surplus, legumes effectively bypassed the primary ecological barrier to colonization of marginal, nutrient-poor landscapes.
- This dedicated microbial bio-factory provided ancestral legumes with a distinctive competitive edge over non-nodulating competitors.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** The legume-*Rhizobium* symbiosis represents an evolutionary breakthrough allowing plants to bypass nitrogen deficiency via a dedicated microbial bio-factory.
- **Option B is incorrect.** Microbes do not render plants independent of water; transpiration and hydration requirements remain unaltered.
- **Option C is incorrect.** Nodules are localized root structures and do not alter the fundamental morphology of aerial leaves into photosynthetic needles.
- **Option D is incorrect.** Symbiosis does not convert eukaryotic plants into prokaryotes."""

# Q92: OSC-030 - Inactive nitrogenase mutation
q92_sol = """### 1. Scientific Principle & Evolutionary Stability of Mutualism:
Mutualistic partnerships remain stable only as long as both partners provide reciprocal metabolic services. When one partner ceases to contribute, the mutualistic balance collapses.

### 2. Biological Process & Sanctions Against Cheaters:
- If a mutant *Rhizobium* strain infects root hairs and forms nodules but harbors a permanently inactive nitrogenase enzyme, the bacteroids continue to consume host plant photosynthate (malate and succinate) without exporting reduced ammonia.
- Functionally, the bacterium transitions from a mutualistic symbiont into an energetic sink or metabolic parasite.
- Under natural conditions, host legumes invoke "host sanctions," restricting oxygen and sucrose delivery to non-fixing nodules to starve out unproductive bacterial strains.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct.** Without nitrogenase activity, the plant gains no fixed nitrogen while losing photosynthates, rendering the relationship functionally parasitic or non-beneficial to the plant.
- **Option B is incorrect.** Non-fixing nodules are starved of host resources and remain stunted rather than growing excessively large.
- **Option C is incorrect.** Metabolic failure in nodules does not induce golden fruit mutations in the shoot canopy.
- **Option D is incorrect.** Bacterial bacteroids cannot spontaneously transform into photosynthetic plant chloroplasts."""

# Q93: OTF-001 - Parasitism vs Mutualism
q93_sol = """### 1. Scientific Principle & Symbiotic Mutualism:
Parasitism is defined as an ecological relationship in which one organism (the parasite) benefits at the direct metabolic expense and physiological detriment of the host \\((+/-)\\).

### 2. Biological Process & Mutualistic Reciprocity:
- In the *Rhizobium*-legume partnership, both organisms gain essential physiological advantages: the plant acquires bioavailable nitrogen for protein synthesis, while the bacterium receives protective shelter and energy-rich carbohydrates.
- Because the interaction enhances the biological fitness of both partners, it is classified as **mutualism** or **symbiotic mutualism** \\((+/+)\\), not parasitism.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that the relationship is an example of parasitism. This is scientifically **False**.
- The relationship is a textbook example of mutualistic symbiosis."""

# Q94: OTF-002 - Free-living vs symbiotic fixation
q94_sol = """### 1. Scientific Principle & Physiological Conditions for Nitrogenase Activity:
The nitrogenase enzyme complex is exceptionally sensitive to oxygen denaturation and demands an immense quantity of ATP to break the \\(\\text{N}\\equiv\\text{N}\\) triple bond.

### 2. Biological Process & Free-Living Constraints:
- While free-living diazotrophs (like *Azotobacter* and *Clostridium*) possess specialized adaptations to fix nitrogen independently, *Rhizobium* species living freely in bulk soil cannot fix nitrogen effectively.
- In free soil, *Rhizobium* lacks the oxygen-buffering protection of host **leghemoglobin** and the concentrated supply of plant-derived dicarboxylic acids necessary to fuel the process.
- Consequently, expression of the *nif* (nitrogen fixation) gene cluster and functional nitrogenase activity in *Rhizobium* are strictly triggered inside root nodules under microaerophilic conditions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that *Rhizobium* can independently fix nitrogen when living freely in soil without a host plant. This is **False**.
- *Rhizobium* requires the specialized microaerophilic and nutritional conditions of legume root nodules to achieve biological nitrogen fixation."""

# Q95: OTF-003 - Nitrogenase oxygen sensitivity
q95_sol = """### 1. Scientific Principle & Metalloenzyme Biochemistry:
The catalytic core of the nitrogenase enzyme consists of Fe-protein (dinitrogenase reductase) and MoFe-protein (dinitrogenase), containing delicate iron-sulfur and molybdenum-iron-sulfur clusters.

### 2. Biological Process & Oxygen Inactivation:
- Molecular oxygen (\\(\\text{O}_2\\)) acts as a potent irreversible inhibitor of the Fe-protein component.
- Exposure to free oxygen rapidly oxidizes and destroys the [4Fe-4S] cluster of the reductase subunit, permanently abolishing electron transfer.
- Legume root nodules prevent this denaturation via host-produced **leghemoglobin**, which binds free oxygen tightly and maintains free \\(\\text{O}_2\\) tension at safe nanomolar concentrations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that the nitrogenase enzyme complex inside root nodules is highly sensitive to excess oxygen and requires protection. This is **True**.
- Oxygen irrevocably inactivates the enzyme, necessitating physiological mechanisms like leghemoglobin and diffusion barriers to preserve catalytic integrity."""

# Q96: OTF-004 - Indiscriminate infection myth
q96_sol = """### 1. Scientific Principle & Host-Symbiont Specificity:
Symbiotic partnerships in nature rely on rigorous molecular recognition mechanisms to prevent opportunistic invasion by incompatible or pathogenic microbes.

### 2. Biological Process & Cross-Inoculation Groups:
- *Rhizobium* does not infect plants indiscriminately; rather, it exhibits strict **host specificity**.
- Particular species or biovars of *Rhizobium* infect only designated legume hosts:
  - *Rhizobium leguminosarum* bv. *viciae* nodulates peas and lentils.
  - *Rhizobium meliloti* (*Sinorhizobium meliloti*) nodulates alfalfa.
  - *Bradyrhizobium japonicum* nodulates soybeans.
- Recognition depends entirely on matching the specific structure of plant-secreted flavonoids with corresponding bacterial Nod factor decorations (sulfation, fucosylation, fatty acyl chain structure). Non-legumes and non-matching legumes fail to nodulate.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that *Rhizobium* can infect any plant species indiscriminately. This is **False**.
- *Rhizobium* exhibits stringent host specificity mediated by precise chemical signaling dialogue."""

# Q97: OTF-005 - Biogeochemical nitrogen cycle contribution
q97_sol = """### 1. Scientific Principle & Global Biogeochemical Cycling:
The global nitrogen cycle describes the movement of nitrogen between the atmosphere, biosphere, hydrosphere, and lithosphere.

### 2. Biological Process & Terrestrial Nitrogen Flux:
- Elemental dinitrogen (\\(\\text{N}_2\\)) in the atmosphere is inaccessible to the vast majority of living organisms.
- Biological nitrogen fixation by diazotrophs—with symbiotic *Rhizobium* accounting for a massive fraction of terrestrial fixation (roughly \\(40\\text{--}60\\text{ million metric tons}\\) of nitrogen per year globally)—serves as the primary biological pathway channeling atmospheric dinitrogen into terrestrial trophic pyramids.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that symbiotic nitrogen fixation by *Rhizobium* contributes significantly to the global biogeochemical nitrogen cycle. This is **True**.
- *Rhizobium* symbiosis is one of the most quantitatively significant biological drivers of terrestrial nitrogen availability on Earth."""

# Q98: OTF-006 - Nitrogen absorption in leaves myth
q98_sol = """### 1. Scientific Principle & Anatomical Localization of Fixation:
Biological nitrogen fixation is an enzymatic process that occurs within specific microbial cells located in specialized root organs.

### 2. Biological Process & Transport Pathway:
- *Rhizobium* bacteria reside strictly within subterranean **root nodules**, not in aerial plant leaves.
- Nitrogen gas present in soil macropores diffuses into the root nodules where nitrogenase reduces it to ammonia.
- The host root cells convert this ammonia into organic nitrogen compounds (amino acids or ureides), which are subsequently translocated upward through the vascular **xylem** vessels to the leaves.
- Leaves do not absorb nitrogen gas directly from soil water, nor do *Rhizobium* bacteria reside inside foliar tissues.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that *Rhizobium* bacteria absorb nitrogen gas directly from soil water and store it in plant leaves. This is **False**.
- Fixation takes place exclusively inside root nodules, from where assimilated organic nitrogen is translocated via vascular xylem sap."""

# Q99: OTF-007 - Heterotrophic bacterial dependency
q99_sol = """### 1. Scientific Principle & Heterotrophic Microbial Metabolism:
Unlike autotrophic cyanobacteria that perform both oxygenic photosynthesis and nitrogen fixation, *Rhizobium* is a chemoorganoheterotroph that cannot synthesize its own organic carbon from carbon dioxide.

### 2. Biological Process & Host Carbon Feeding:
- Inside the microaerophilic environment of root nodules, *Rhizobium* bacteroids cannot carry out photosynthesis.
- They depend entirely on the host legume to supply organic dicarboxylic acids (such as malate, succinate, and fumarate) derived from phloem-transported photosynthetic sucrose.
- These carbon compounds fuel bacteroid cellular respiration, generating the ATP and reducing equivalents essential for powering nitrogenase.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement asserts that *Rhizobium* bacteria depend on the host plant for shelter and organic nutrients. This is **True**.
- As heterotrophic endosymbionts, bacteroids rely completely on host photosynthates for carbon skeletons and metabolic energy."""

# Q100: OTF-008 - Energetic requirement of fixation
q100_sol = """### 1. Scientific Principle & Thermodynamics of Dinitrogen Cleavage:
The covalent triple bond of diatomic nitrogen (\\(\\text{N}\\equiv\\text{N}\\)) has a very high bond dissociation energy (\\(945\\text{ kJ/mol}\\)), rendering it one of the least reactive chemical bonds in nature.

### 2. Biological Process & High ATP Consumption:
- To lower the activation barrier and transfer electrons across negative redox potentials, the nitrogenase Fe-protein couples electron transfer to ATP hydrolysis:
  \\[\\text{N}_2 + 8\\text{H}^+ + 8e^- + 16\\text{ATP} \\xrightarrow{\\text{Nitrogenase}} 2\\text{NH}_3 + \\text{H}_2 + 16\\text{ADP} + 16\\text{P}_i\\]
- A minimum of \\(16\\text{ ATP}\\) molecules (and often \\(20\\text{--}30\\text{ ATP}\\) in vivo due to hydrogen-evolution inefficiencies) are consumed per molecule of \\(\\text{N}_2\\) reduced.
- This enormous metabolic demand is satisfied by host plant respiration oxidizing photosynthetic sugars.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement states that nitrogen fixation by *Rhizobium* is an energy-intensive biological process requiring ATP supplied by the plant. This is **True**.
- Biological reduction of the dinitrogen triple bond requires immense thermodynamic input supplied via host-derived ATP."""

# Q101: OTF-009 - Obligate parasite misconception
q101_sol = """### 1. Scientific Principle & Symbiosis vs Parasitism:
An obligate parasite is an organism that cannot survive without a host and typically harms, debilitates, or eventually kills the host during its life cycle.

### 2. Biological Process & Beneficial Mutualism:
- *Rhizobium* is neither an obligate parasite nor does it kill its host legume.
- *Rhizobium* can survive as a free-living, saprophytic bacterium in soil (though it fixes nitrogen only in symbiosis).
- Furthermore, the association provides essential reduced nitrogen that enhances host growth, foliage vigor, seed protein content, and reproductive yield rather than causing morbidity or mortality.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that *Rhizobium* bacteria are obligate parasites that eventually kill their host leguminous plant. This is **False**.
- *Rhizobium* is a facultative, mutualistic symbiont that enhances host growth rather than killing it."""

# Q102: OTF-010 - Direct atmospheric nitrogen access myth
q102_sol = """### 1. Scientific Principle & Chemical Inertness of Atmospheric Nitrogen:
Although nitrogen constitutes roughly \\(78\\%\\) of Earth's atmosphere, it exists as non-polar diatomic molecules with an extremely strong triple covalent bond.

### 2. Biological Process & The Biological Need for Fixers:
- Terrestrial plants completely lack genes encoding the nitrogenase enzyme or any alternative biochemical pathways to break the \\(\\text{N}\\equiv\\text{N}\\) triple bond.
- Without diazotrophic microorganisms (such as *Rhizobium*, *Azotobacter*, and cyanobacteria) or physical fixation via lightning discharges, plants would experience total nitrogen starvation in terrestrial ecosystems.
- Atmospheric dinitrogen is completely inaccessible to vascular plant metabolism without preliminary biological or chemical fixation into ammonium or nitrates.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Evaluation:** The statement claims that without *Rhizobium* or similar symbionts, terrestrial plants would have unlimited access to all forms of atmospheric nitrogen directly. This is **False**.
- Plants cannot absorb or metabolize gaseous elemental nitrogen directly due to the lack of dinitrogen-reducing enzymes."""

# Map solutions for Q63 to Q102
sol_map = {
    63: q63_sol, 64: q64_sol, 65: q65_sol, 66: q66_sol, 67: q67_sol,
    68: q68_sol, 69: q69_sol, 70: q70_sol, 71: q71_sol, 72: q72_sol,
    73: q73_sol, 74: q74_sol, 75: q75_sol, 76: q76_sol, 77: q77_sol,
    78: q78_sol, 79: q79_sol, 80: q80_sol, 81: q81_sol, 82: q82_sol,
    83: q83_sol, 84: q84_sol, 85: q85_sol, 86: q86_sol, 87: q87_sol,
    88: q88_sol, 89: q89_sol, 90: q90_sol, 91: q91_sol, 92: q92_sol,
    93: q93_sol, 94: q94_sol, 95: q95_sol, 96: q96_sol, 97: q97_sol,
    98: q98_sol, 99: q99_sol, 100: q100_sol, 101: q101_sol, 102: q102_sol
}

# Correct answers for OSC (Q63 to Q92) and OTF (Q93 to Q102)
# Let's verify letters for OSC Q63 to Q92 from raw options
ans_map = {}
for idx in range(63, 93):
    raw_item = raw_part2[idx - 53] # raw_part2 is 0-indexed for Q53 to Q102
    opts = raw_item['options']
    raw_ans = raw_item['correctAnswer']
    
    # Clean options from raw (remove \ce{...} etc)
    clean_opts = []
    for opt in opts:
        cleaned_opt = opt.replace(r'\ce{N2}', r'\(\text{N}_2\)').replace(r'\ce{NH3}', r'\(\text{NH}_3\)').replace(r'\ce{CO2}', r'\(\text{CO}_2\)').replace(r'\ce{O2}', r'\(\text{O2}\)').replace(r'\ce{NaCl}', r'\(\text{NaCl}\)').replace(r'\ce{SO3}', r'\(\text{SO}_3\)').replace(r'\ce{H2}', r'\(\text{H}_2\)')
        clean_opts.append(cleaned_opt)
    
    # Find matching option index
    found_letter = None
    letters = ['A', 'B', 'C', 'D']
    for opt_idx, opt in enumerate(opts):
        if raw_ans.strip().lower() in opt.strip().lower() or opt.strip().lower() in raw_ans.strip().lower():
            found_letter = letters[opt_idx]
            break
    if not found_letter:
        print(f"Warning: match not found for Q{idx}, raw_ans: {raw_ans}")
        found_letter = "A"
    ans_map[idx] = (found_letter, clean_opts)

# For OTF Q93 to Q102
otf_ans = {
    93: "False",
    94: "False",
    95: "True",
    96: "False",
    97: "True",
    98: "False",
    99: "True",
    100: "True",
    101: "False",
    102: "False"
}

# Construct full part2 array
part2_full = []
# Add starter 10 (Q53 to Q62)
part2_full.extend(starter_10)

# Add Q63 to Q92 (OSC)
for idx in range(63, 93):
    raw_item = raw_part2[idx - 53]
    letter, clean_opts = ans_map[idx]
    
    # Clean text of question
    clean_text = raw_item['text'].replace(r'\ce{N2}', r'\(\text{N}_2\)').replace(r'\ce{NH3}', r'\(\text{NH}_3\)').replace(r'\ce{CO2}', r'\(\text{CO}_2\)').replace(r'\ce{O2}', r'\(\text{O2}\)')
    
    item = {
        "questionCode": raw_item['questionCode'],
        "type": raw_item['type'],
        "text": clean_text,
        "options": clean_opts,
        "correctAnswer": letter,
        "solution": sol_map[idx]
    }
    part2_full.append(item)

# Add Q93 to Q102 (OTF)
for idx in range(93, 103):
    raw_item = raw_part2[idx - 53]
    clean_text = raw_item['text'].replace(r'\ce{N2}', r'\(\text{N}_2\)').replace(r'\ce{NH3}', r'\(\text{NH}_3\)')
    
    item = {
        "questionCode": raw_item['questionCode'],
        "type": raw_item['type'],
        "text": clean_text,
        "options": ["True", "False"],
        "correctAnswer": otf_ans[idx],
        "solution": sol_map[idx]
    }
    part2_full.append(item)

print(f"Total Part 2 questions generated: {len(part2_full)}")

# Write to scripts/ch8_part2.js
output_js = "// scripts/ch8_part2.js\n"
output_js += "// MH-9-SCIT-8-8.1.2 Useful Microbes: Rhizobium & Nitrogen Fixation (50 questions, Q53 to Q102)\n"
output_js += "const ch8_part2 = " + json.dumps(part2_full, indent=2, ensure_ascii=False) + ";\n\n"
output_js += "module.exports = { ch8_part2 };\n"

with open('scripts/ch8_part2.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("Saved scripts/ch8_part2.js successfully!")
