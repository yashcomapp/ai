// scripts/build-ch8-part1-full.js
// Generates scripts/ch8_part1.js containing all 52 questions of MH-9-SCIT-8-8.1
// with genuine 3-part gold standard pedagogical solutions.

const fs = require('fs');
const path = require('path');

const raw = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_8_raw.json', 'utf8')).slice(0, 52);

// Load the first 10 questions from make-ch8-part1.js
const { ch8_part1: first10 } = require('./ch8_part1.js');

// Now let's define questions 23 to 52 (from OSC-011 to OTF-010, exactly 30 items)
const remaining = [
  // Q23 (OSC-011)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-011",
    type: "OSC",
    text: "In the context of dairy fermentation, what is a 'starter'?",
    options: [
      "A small quantity of pre-existing yogurt containing active Lactobacilli",
      "A chemical preservative added to prevent spoilage",
      "A dye used to color milk",
      "An electric device used to stir milk"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Industrial Inoculum Terminology:
In food biotechnology, a **starter** (or starter culture) is a microbiological preparation containing large populations of specifically selected living microorganisms inoculated into a raw food substrate to drive desired, predictable fermentation.

### 2. Biological Process & The Starter Mechanism:
- In household and industrial dairy processing, adding a starter culture (such as a spoonful of fresh curd or a freeze-dried commercial culture of *Lactobacillus delbrueckii* and *Streptococcus thermophilus*) provides an initial bacterial concentration of approximately $10^6\\text{--}10^7\\text{ CFU/mL}$.
- This high initial population rapidly ferments lactose, drops the $\\text{pH}$, and outcompetes any residual post-pasteurization spoilage microorganisms, guaranteeing uniform texture, flavor, and curd firmness.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (A small quantity of pre-existing yogurt containing active Lactobacilli):** Correct. A starter is an active inoculum containing live fermenting bacteria.
- **Option B (A chemical preservative):** Incorrect. Starter cultures are living microbes, not synthetic chemical additives.
- **Option C (A dye used to color milk):** Incorrect. Starters do not act as colorants.
- **Option D (An electric device):** Incorrect. A starter is a biological culture, not mechanical hardware.`
  },
  // Q24 (OSC-012)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-012",
    type: "OSC",
    text: "How do Lactobacilli contribute to safeguarding the digestive tract from pathogenic microbes?",
    options: [
      "By producing organic acids and hydrogen peroxide that inhibit harmful bacteria",
      "By transforming the stomach into a muscular wall",
      "By secreting strong digestive enzymes that dissolve pathogens",
      "By absorbing all water in the gut"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Antimicrobial Biocontrol by Lactic Acid Bacteria:
*Lactobacilli* exhibit potent antimicrobial mechanisms that safeguard the gastrointestinal and urogenital tracts of mammals against invasion by pathogenic bacteria, yeasts, and parasites.

### 2. Biological Process & Biochemical Weapons:
1. **Lactic Acid Accumulation:** Rapidly lowers the microenvironmental $\\text{pH}$ below $4.5$. The undissociated organic acid diffuses across the outer membrane of Gram-negative pathogens (*Salmonella, Shigella, E. coli*), dissociates intracellularly, and acidifies the cytoplasm, collapsing the proton-motive force.
2. **Hydrogen Peroxide ($\\text{H}_2\\text{O}_2$) Synthesis:** Many *Lactobacillus* species synthesize $\\text{H}_2\\text{O}_2$ via flavoprotein oxidases in microaerophilic conditions, which oxidizes essential sulfhydryl groups in pathogen enzymes.
3. **Bacteriocins:** They synthesize ribosomally produced antimicrobial peptides (e.g., nisin, lactacin, acidolin) that form lethal ion-permeable pores in target pathogen membranes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (By producing organic acids and hydrogen peroxide that inhibit harmful bacteria):** Correct. Lactic acid, $\\text{H}_2\\text{O}_2$, and bacteriocins directly suppress and destroy pathogenic microbes.
- **Option B (Transforming stomach into muscular wall):** Incorrect. Stomach muscle architecture is genetically determined.
- **Option C (Secreting enzymes that dissolve pathogens):** Incorrect. Their primary mechanism is acidification and bacteriocins, not pathogen-dissolving digestive enzymes.
- **Option D (Absorbing all water in the gut):** Incorrect. Complete dehydration of the gut would be lethal.`
  },
  // Q25 (OSC-013)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-013",
    type: "OSC",
    text: "Which commercial product is manufactured by fermenting milk solids using specific bacterial cultures including Lactobacilli for extended shelf life and texture?",
    options: [
      "Vegetable oil",
      "Pure sugar syrup",
      "Cheese",
      "Refined wheat flour"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Industrial Cheese Manufacturing:
Cheese is a solid or semi-solid fermented dairy product produced through the controlled microbial coagulation of milk proteins and separation of aqueous whey.

### 2. Biological Process & Cheesemaking Steps:
1. **Acidification:** Pasteurized milk is inoculated with lactic acid starter bacteria (*Lactococcus lactis, Lactobacillus helveticus, L. bulgaricus*), which ferment lactose to lactic acid.
2. **Coagulation:** Acidification works synergistically with the proteolytic enzyme chymosin (**rennet**) to cleave $\\kappa$-casein, precipitating the protein into firm curds.
3. **Separation & Pressing:** Liquid whey is drained off, and the curd is salted and mechanically pressed into blocks.
4. **Ripening (Aging):** During storage, bacterial and fungal enzymes break down proteins and fats into complex peptides, esters, and volatile aromatics, imparting distinctive flavors and extending shelf life for months or years.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Vegetable oil):** Incorrect. Extracted from oilseeds (sunflower, mustard, soybean).
- **Option B (Pure sugar syrup):** Incorrect. Refined sucrose from sugarcane or sugar beet.
- **Option C (Cheese):** Correct. Cheese is the quintessential commercial dairy food manufactured via lactic acid bacterial fermentation.
- **Option D (Refined wheat flour):** Incorrect. Milled endosperm of cereal wheat grains.`
  },
  // Q26 (OSC-014)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-014",
    type: "OSC",
    text: "Which biochemical component of milk serves as the primary energy and carbon source for Lactobacilli during yogurt formation?",
    options: [
      "Glucose",
      "Lactose",
      "Fructose",
      "Sucrose"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Carbohydrate Biochemistry of Milk:
Milk is uniquely distinguished from all other mammalian body fluids by the presence of a specific disaccharide sugar synthesized in the mammary gland: **lactose**.

### 2. Biological Process & Lactose Fermentation:
- Lactose ($\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$) is a reducing disaccharide composed of one molecule of **D-galactose** and one molecule of **D-glucose** joined by a $\\beta$-(1,4)-glycosidic bond.
- It comprises approximately $4.5\\text{--}5.0\\%$ of whole bovine milk.
- *Lactobacilli* possess specialized lactose transport permeases and the intracellular enzyme **$\\beta$-galactosidase (lactase)**, which hydrolyzes lactose:
  $$\\text{Lactose} + \\text{H}_2\\text{O} \\xrightarrow{\\beta\\text{-galactosidase}} \\text{D-Glucose} + \\text{D-Galactose}$$
- Both hexose sugars are subsequently funneled through glycolysis to generate ATP and lactic acid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Glucose):** Incorrect. Free glucose exists only in trace quantities in raw milk; lactose is the dominant substrate.
- **Option B (Lactose):** Correct. The milk disaccharide lactose is the primary energy and carbon substrate for *Lactobacilli*.
- **Option C (Fructose):** Incorrect. Fructose is a plant fruit sugar not naturally present in milk.
- **Option D (Sucrose):** Incorrect. Sucrose is common table sugar derived from sugarcane.`
  },
  // Q27 (OSC-015)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-015",
    type: "OSC",
    text: "What is the main characteristic change observed in milk proteins when lactic acid is produced during fermentation?",
    options: [
      "Proteins dissolve completely into clear water",
      "Proteins undergo coagulation and gel formation",
      "Proteins turn into gaseous bubbles",
      "Proteins convert into lipids"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Colloid Chemistry of Casein:
In liquid milk, the soluble calcium-caseinate complex remains stably dispersed as colloidal particles due to negative surface zeta potential (electrostatic repulsion) at neutral $\\text{pH} = 6.6$.

### 2. Biological Process & Acid Coagulation:
- As *Lactobacilli* multiply and secrete lactic acid, the concentration of free hydronium ions ($[\\text{H}^+]$) rises.
- When the $\\text{pH}$ reaches the **isoelectric point (pI)** of casein ($\\text{pH} = 4.6$), the net electrical charge on the proteins becomes zero:
  $$\\text{Net Charge} = 0 \\implies \\text{Electrostatic Repulsion Collapses}$$
- Casein sub-micelles aggregate into clumps, forming a continuous three-dimensional fibrous network (**coagulum** or curd gel) that entraps liquid serum, transforming liquid milk into a semi-solid texture.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Proteins dissolve into clear water):** Incorrect. Proteins precipitate and coagulate, rather than dissolving.
- **Option B (Proteins undergo coagulation and gel formation):** Correct. Acidification drives casein micelles to their isoelectric point, triggering coagulation into a firm gel.
- **Option C (Proteins turn into gas):** Incorrect. Proteins do not vaporize into gas during dairy fermentation.
- **Option D (Proteins convert into lipids):** Incorrect. Amino acids are not biochemically converted into fats during curd setting.`
  },
  // Q28 (OSC-016)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-016",
    type: "OSC",
    text: "Why do people with lactose intolerance sometimes find fermented dairy products like yogurt easier to digest?",
    options: [
      "Lactobacilli pre-digest and break down a significant portion of the lactose",
      "Lactobacilli remove all fats from the milk",
      "Yogurt contains no organic molecules",
      "Yogurt is completely devoid of proteins"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Pathophysiology of Lactose Intolerance:
Lactose intolerance is caused by a physiological deficiency of the brush-border enzyme **lactase** in the human small intestinal mucosa, preventing the hydrolysis of milk lactose into absorbable glucose and galactose. Unabsorbed lactose passes into the colon, drawing water osmotically and fermenting into gas, causing cramps, bloating, and diarrhea.

### 2. Biological Process & Microbial Pre-Digestion:
- During fermentation into yogurt or curd, *Lactobacilli* actively consume and hydrolyze **$30\\text{--}50\\%$ of the lactose** into lactic acid.
- Furthermore, live *Lactobacillus* cells in unpasteurized yogurt contain endogenous bacterial **$\\beta$-galactosidase (lactase)**.
- When ingested, the bacterial cell walls are disrupted by bile salts in the duodenum, releasing active lactase directly into the intestinal lumen, which hydrolyzes remaining dietary lactose and prevents digestive distress.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Lactobacilli pre-digest and break down a significant portion of the lactose):** Correct. Fermentation depletes lactose and supplies bacterial lactase enzymes, making yogurt well-tolerated.
- **Option B (Remove all fats):** Incorrect. Yogurt retains milk fat unless made from skimmed milk.
- **Option C (Contains no organic molecules):** Incorrect. Yogurt is packed with proteins, lactic acid, and vitamins.
- **Option D (Devoid of proteins):** Incorrect. Yogurt is a rich source of coagulated protein.`
  },
  // Q29 (OSC-017)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-017",
    type: "OSC",
    text: "Which of the following best describes a probiotic dietary supplement?",
    options: [
      "A type of antibiotic drug",
      "A pill containing synthetic vitamins and minerals",
      "A preparation containing live beneficial microorganisms that support health",
      "An artificial chemical sweetener"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Probiotic Definition:
The scientific and clinical consensus (FAO/WHO, 2001) defines **probiotics** strictly as:
> *"Live microorganisms that, when administered in adequate amounts, confer a health benefit on the host."*

### 2. Biological Process & Probiotic Composition:
- Probiotic dietary supplements are prepared as lyophilized (freeze-dried) powders, capsules, chewable tablets, or micro-encapsulated suspensions.
- They contain authenticated, viable bacterial or fungal strains in standardized doses (typically $10^9\\text{--}10^{11}$ Colony Forming Units [CFU] per dose), such as:
  - *Lactobacillus acidophilus*, *Lactobacillus rhamnosus GG*
  - *Bifidobacterium lactis*, *Bifidobacterium longum*
  - *Saccharomyces boulardii* (a beneficial probiotic yeast)
- Unlike antibiotics (which kill microbes), probiotics introduce living symbiotic mutualists to reinforce the host's natural gut flora.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (A type of antibiotic drug):** Incorrect. Antibiotics kill bacteria; probiotics provide beneficial live bacteria.
- **Option B (Synthetic vitamins and minerals):** Incorrect. That describes a multivitamin, not a probiotic.
- **Option C (A preparation containing live beneficial microorganisms that support health):** Correct. Matches the universal scientific definition of a probiotic.
- **Option D (An artificial chemical sweetener):** Incorrect. Describes aspartame or sucralose.`
  },
  // Q30 (OSC-018)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-018",
    type: "OSC",
    text: "What happens if milk is inoculated with a starter culture when it is boiling hot?",
    options: [
      "The Lactobacilli bacteria get killed by heat and yogurt fails to set",
      "Yogurt sets much faster and tastes better",
      "The milk turns into solid cheese instantly",
      "No change occurs"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Thermal Denaturation of Microbial Cells:
Living vegetative bacterial cells consist of hydrated proteins, nucleic acids, and phospholipid bilayers held together by delicate non-covalent bonds (hydrogen bonds, ionic interactions, hydrophobic forces).

### 2. Biological Process & Heat Inactivation:
- *Lactobacilli* are non-spore-forming mesophiles/thermophiles with a maximum thermal tolerance of approximately **$45^\\circ\\text{C}\\text{--}50^\\circ\\text{C}$**.
- Boiling milk reaches temperatures of **$100^\\circ\\text{C}$**.
- When live starter culture is stirred into boiling milk:
  1. The intense thermal energy instantly denatures essential metabolic enzymes (such as lactate dehydrogenase and ATP synthase).
  2. The cytoplasmic membrane loses its selective permeability and ruptures.
  3. 100% of the inoculated *Lactobacilli* are destroyed within seconds.
- With zero living bacteria left to produce lactic acid, lactose fermentation cannot occur, and the milk remains a sweet, uncoagulated liquid that eventually spoils.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (The Lactobacilli bacteria get killed by heat and yogurt fails to set):** Correct. Boiling temperatures thermal-shock and kill the starter culture, preventing curd formation.
- **Option B (Yogurt sets much faster):** Incorrect. Dead bacteria cannot ferment milk.
- **Option C (Turns into solid cheese instantly):** Incorrect. Acid or rennet is required to make cheese, which dead bacteria cannot produce.
- **Option D (No change occurs):** Incorrect. The bacteria are completely destroyed.`
  },
  // Q31 (OSC-019)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-019",
    type: "OSC",
    text: "Which cellular structure is absent in Lactobacilli since they are bacterial cells?",
    options: [
      "Ribosome",
      "Defined nuclear membrane",
      "Cell wall",
      "Cell membrane"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Prokaryotic Cytology:
All living organisms are classified as either prokaryotes or eukaryotes based on fundamental cellular organization. *Lactobacilli* belong to Domain Bacteria, Kingdom Monera, and are true **prokaryotes**.

### 2. Biological Context & Structural Diagnostics:
- **Structures Present in Lactobacilli:**
  - A rigid, thick peptidoglycan **cell wall** (Gram-positive).
  - A phospholipid **cell membrane** (plasma membrane) regulating molecular transport.
  - Non-membrane-bound **70S ribosomes** for synthesizing proteins.
  - Naked, circular, double-stranded chromosomal DNA localized in the **nucleoid**.
- **Structures Absent in Lactobacilli:**
  - A true, double-membrane-bound **nuclear envelope (defined nuclear membrane)** enclosing the genetic material is completely absent in all bacteria.
  - Membrane-bound organelles (mitochondria, chloroplasts, endoplasmic reticulum, Golgi bodies) are likewise absent.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Ribosome):** Incorrect. *Lactobacilli* possess abundant 70S ribosomes.
- **Option B (Defined nuclear membrane):** Correct. As prokaryotes, *Lactobacilli* lack a membrane-bound nucleus and nuclear envelope.
- **Option C (Cell wall):** Incorrect. *Lactobacilli* possess a thick Gram-positive peptidoglycan wall.
- **Option D (Cell membrane):** Incorrect. Present in all living bacterial cells.`
  },
  // Q32 (OSC-020)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-020",
    type: "OSC",
    text: "Which of the following sectors heavily utilizes Lactobacilli cultures for large-scale food preservation and processing?",
    options: [
      "Petroleum refining",
      "Textile industry",
      "Dairy industry",
      "Metallurgy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Industrial Biotechnology:
Industrial biotechnology utilizes microbial biocatalysts across specialized manufacturing sectors.

### 2. Biological Process & The Dairy Sector:
- The **dairy industry** is the largest commercial consumer of *Lactobacillus* cultures globally.
- Thousands of metric tons of raw animal milk are processed daily into:
  - **Yogurt & Curd:** Using *Lactobacillus delbrueckii* subsp. *bulgaricus*.
  - **Cheese Varieties (Cheddar, Swiss, Gouda, Mozzarella):** Using *Lactobacillus helveticus, L. casei*, and *L. lactis*.
  - **Probiotic Beverages & Kefir:** Using *Lactobacillus acidophilus*.
  - **Cultured Butter & Sour Cream:** Using lactic acid starter bacteria.
- In contrast, petroleum refining uses chemical cracking, textiles use amylases/cellulases, and metallurgy uses inorganic smelting or bioleaching by sulfur-oxidizing bacteria.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Petroleum refining):** Incorrect. Petroleum refining does not utilize dairy lactic bacteria.
- **Option B (Textile industry):** Incorrect. Uses fungal enzymes for sizing and de-sizing fabrics.
- **Option C (Dairy industry):** Correct. The dairy sector heavily depends on *Lactobacilli* for fermented milk products.
- **Option D (Metallurgy):** Incorrect. Metallurgy deals with metals and ores.`
  },
  // Q33 (OSC-021)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-021",
    type: "OSC",
    text: "What type of respiration or metabolic pathway is primarily utilized by Lactobacilli to convert sugars into energy and lactic acid?",
    options: [
      "Oxidative phosphorylation via mitochondria",
      "Aerobic photosynthesis",
      "Anaerobic fermentation / Glycolysis-based lactic acid pathway",
      "Chemosynthesis using sulfur"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Fermentative Metabolism:
Lactic acid bacteria (LAB) are chemoorganotrophic, aerotolerant anaerobes or facultative anaerobes that lack a functional cytochrome-linked respiratory electron transport chain.

### 2. Biological Process & The Homolactic Pathway:
- Because they lack mitochondria and electron transport complexes, *Lactobacilli* cannot perform oxidative phosphorylation.
- Instead, they generate all their cellular metabolic energy (ATP) strictly via **substrate-level phosphorylation** during anaerobic glycolysis (the Embden-Meyerhof-Parnas pathway):
  $$\\text{Glucose} + 2\\text{ADP} + 2\\text{P}_i + 2\\text{NAD}^+ \\longrightarrow 2\\text{Pyruvate} + 2\\text{ATP} + 2\\text{NADH} + 2\\text{H}^+$$
- To regenerate oxidized $\\text{NAD}^+$ in the absence of oxygen, pyruvate is directly reduced to **lactic acid** by lactate dehydrogenase:
  $$2\\text{Pyruvate} + 2\\text{NADH} + 2\\text{H}^+ \\longrightarrow 2\\text{Lactic Acid} + 2\\text{NAD}^+$$
- Net energy yield is exactly **$2\\text{ ATP}$** per mole of glucose metabolized.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Oxidative phosphorylation via mitochondria):** Incorrect. Bacteria lack mitochondria and respiratory cytochromes.
- **Option B (Aerobic photosynthesis):** Incorrect. *Lactobacilli* lack photosynthetic pigments.
- **Option C (Anaerobic fermentation / Glycolysis-based lactic acid pathway):** Correct. They generate ATP through anaerobic fermentation yielding lactic acid.
- **Option D (Chemosynthesis using sulfur):** Incorrect. Characteristic of deep-sea sulfur bacteria (*Thiobacillus*).`
  },
  // Q34 (OSC-022)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-022",
    type: "OSC",
    text: "How does regular consumption of probiotic yogurt benefit livestock or domestic animals, similar to humans?",
    options: [
      "Improves their hair color permanently",
      "Increases their body temperature drastically",
      "Stops their growth completely",
      "Enhances gut digestion and protects against intestinal infections"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Veterinary Probiotics:
In veterinary science and animal husbandry (poultry, cattle, swine, sheep), live microbial feed supplements (DFMs - Direct-Fed Microbials) are widely incorporated into animal feed to promote gut health and replace prophylactic sub-therapeutic antibiotic growth promoters.

### 2. Biological Process & Animal Physiology:
- Administering probiotic yogurt or cultured lactic feed introduces viable *Lactobacillus* strains into the animal's digestive tract:
  1. **Feed Conversion Efficiency:** Enhances the digestion and absorption of dietary nutrients, promoting healthy weight gain.
  2. **Pathogen Reduction:** Acidifies the intestinal lumen, significantly suppressing colonization by veterinary pathogens such as *Salmonella enterica, Escherichia coli*, and *Clostridium perfringens*.
  3. **Reduced Morbidity:** Dramatically lowers the incidence of infectious diarrhea (scours in calves), reducing mortality in young livestock.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Improves hair color permanently):** Incorrect. Coat color is determined by genetics, not gut bacteria.
- **Option B (Increases body temperature drastically):** Incorrect. That would cause dangerous fever.
- **Option C (Stops their growth completely):** Incorrect. Probiotics promote healthy growth.
- **Option D (Enhances gut digestion and protects against intestinal infections):** Correct. Probiotics optimize digestive efficiency and guard against enteric infections in livestock.`
  },
  // Q35 (OSC-023)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-023",
    type: "OSC",
    text: "What role do beneficial bacteria in the human gut play regarding immunity?",
    options: [
      "They destroy white blood cells",
      "They compete with pathogens and stimulate immune responses",
      "They act as physical armor plating over the skin",
      "They suppress the immune system entirely"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Gut-Associated Lymphoid Tissue (GALT):
Approximately $70\\%$ of the human body's immune cells reside within the gastrointestinal tract in the form of **Gut-Associated Lymphoid Tissue (GALT)**, including Peyer's patches, mesenteric lymph nodes, and lamina propria lymphocytes.

### 2. Biological Process & Immunological Modulation:
- Commensal bacteria like *Lactobacillus* continuously interact with host mucosal immune receptors (such as Toll-like receptors, TLRs):
  1. **Competitive Exclusion:** They form a dense physical biofilm over the intestinal epithelial surface, denying pathogenic microbes physical binding sites and starving them of micronutrients.
  2. **Immune Priming:** They stimulate plasma B cells to secrete **secretory Immunoglobulin A (sIgA)**, which neutralizes toxins and viruses in the gut lumen.
  3. **Cytokine Homeostasis:** They promote the differentiation of regulatory T cells ($\text{T}_{\\text{reg}}$), suppressing destructive autoimmune inflammation while maintaining vigilant defenses against invasive pathogens.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Destroy white blood cells):** Incorrect. Pathogens destroy leukocytes; beneficial bacteria cooperate with them.
- **Option B (They compete with pathogens and stimulate immune responses):** Correct. Beneficial gut bacteria outcompete pathogens and actively train host immune defenses.
- **Option C (Physical armor plating on skin):** Incorrect. They reside in the gut mucosal lining, not as skin armor.
- **Option D (Suppress immune system entirely):** Incorrect. Total immune suppression would lead to fatal systemic infection.`
  },
  // Q36 (OSC-024)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-024",
    type: "OSC",
    text: "Which of the following organisms is a bacterium used in dairy fermentation, distinguishing it from yeast used in baking?",
    options: [
      "Lactobacillus acidophilus",
      "Mucor",
      "Aspergillus niger",
      "Saccharomyces cerevisiae"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Microorganism Categorization:
Microorganisms harnessed in food biotechnology span different biological kingdoms:
- **Kingdom Monera (Bacteria):** Prokaryotic organisms.
- **Kingdom Fungi (Yeasts and Molds):** Eukaryotic organisms.

### 2. Biological Context & Microbial Profiles:
- **Lactobacillus acidophilus:** A prokaryotic, gram-positive, rod-shaped bacterium that ferments lactose to lactic acid, serving as the premier commercial dairy culture for yogurt and probiotics.
- **Saccharomyces cerevisiae (Baker's Yeast):** A unicellular eukaryotic fungus that performs alcoholic fermentation, converting glucose into ethanol and $\\text{CO}_2$ gas used to leaven bread dough.
- **Mucor:** A filamentous saprophytic pin mold (fungus).
- **Aspergillus niger:** A filamentous black mold (fungus) used industrially to synthesize citric acid.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Lactobacillus acidophilus):** Correct. *Lactobacillus acidophilus* is a true bacterium utilized in dairy fermentation.
- **Option B (Mucor):** Incorrect. *Mucor* is a eukaryotic mold fungus.
- **Option C (Aspergillus niger):** Incorrect. *Aspergillus* is a mold fungus used for citric acid.
- **Option D (Saccharomyces cerevisiae):** Incorrect. *Saccharomyces* is a baking and brewing yeast (fungus), not a dairy bacterium.`
  },
  // Q37 (OSC-025)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-025",
    type: "OSC",
    text: "Why is milk checked for proper lukewarm warmth before adding the yogurt starter?",
    options: [
      "To make the milk evaporate completely",
      "To freeze the fat contents",
      "To ensure the container does not crack from thermal shock",
      "To provide the optimum thermal range for Lactobacilli multiplication without denaturing them"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Temperature Sensitivity of Biological Inocula:
Enzymatic reaction rates in bacteria are bounded by two thermal thresholds: metabolic freezing at low temperatures and irreversible denaturation at high temperatures.

### 2. Biological Process & The Lukewarm Window:
- **Lukewarm Milk ($37^\\circ\\text{C}\\text{--}42^\\circ\\text{C}$):** Matches the body temperature of mammals, providing the ideal thermal kinetic environment for *Lactobacillus delbrueckii* and *Streptococcus thermophilus*.
- **Consequences of Deviations:**
  - If milk is **too hot ($> 55^\\circ\\text{C}$):** The high temperature breaks secondary and tertiary bonds in bacterial enzymes, denaturing them and killing the starter culture instantly.
  - If milk is **too cold ($< 20^\\circ\\text{C}$):** Bacterial metabolism slows dramatically, enzyme turnover is near zero, and the milk fails to set into curd within a practical timeframe.
- Checking that milk is pleasantly lukewarm to touch ensures that the inoculated *Lactobacilli* remain viable and enter exponential division immediately.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (To make milk evaporate):** Incorrect. Evaporation is not the goal of setting curd.
- **Option B (To freeze fat):** Incorrect. Lukewarm milk keeps fats liquid, not frozen.
- **Option C (Ensure container does not crack):** Incorrect. While thermal shock affects glass, the biological reason relates to bacterial survival.
- **Option D (To provide the optimum thermal range for Lactobacilli multiplication without denaturing them):** Correct. The lukewarm temperature provides the perfect thermal range for bacterial survival and rapid fermentation.`
  },
  // Q38 (OSC-026)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-026",
    type: "OSC",
    text: "What physical change occurs to milk when it transforms into yogurt other than taste and acidity?",
    options: [
      "It turns into a transparent gas",
      "It becomes a hard crystal",
      "It separates into pure solid gold",
      "It changes from a liquid to a semi-solid gel state"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Rheological Phase Transition in Dairy:
The conversion of milk into yogurt involves a fundamental rheological transformation from a low-viscosity Newtonian fluid to a high-viscosity, viscoelastic semi-solid gel.

### 2. Biological Process & Microscopic Mechanics:
- Liquid milk is an emulsion of butterfat droplets and a colloidal suspension of casein protein micelles in an aqueous lactose-mineral serum.
- When *Lactobacilli* produce lactic acid, the drop in $\\text{pH}$ to $4.6$ neutralizes the negative surface charge on the casein micelles.
- Destabilized micelles fuse into branching chains that aggregate into a continuous three-dimensional microscopic network.
- This protein matrix physically traps water and fat droplets within its pores via capillary action, converting free-flowing liquid milk into a cohesive, custard-like **semi-solid gel (curd)**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Turns into transparent gas):** Incorrect. Curd remains a semi-solid liquid-protein gel.
- **Option B (Becomes a hard crystal):** Incorrect. Curd is a soft viscoelastic gel, not a mineral crystal.
- **Option C (Separates into gold):** Incorrect. Pure mythological fantasy.
- **Option D (It changes from a liquid to a semi-solid gel state):** Correct. The primary physical change is the phase transition from liquid milk to a semi-solid coagulated protein gel.`
  },
  // Q39 (OSC-027)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-027",
    type: "OSC",
    text: "Which property of lactic acid bacteria makes them effective in preserving certain foods naturally?",
    options: [
      "Production of high levels of acid that lower pH and inhibit spoilage microbes",
      "Creation of a dry vacuum",
      "Production of toxic heavy metals",
      "Release of high-intensity radiation"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Biological Food Preservation:
Natural food preservation relies on establishing hurdles (the "Hurdle Technology" concept) that prevent spoilage microorganisms from proliferating.

### 2. Biological Process & Acid Inhibition:
- Lactic acid bacteria (LAB) metabolize hexose sugars to produce copious quantities of **lactic acid**, rapidly driving the $\\text{pH}$ down from near-neutral ($6.5$) to acidic ($3.8\\text{--}4.5$).
- **Inhibitory Action on Spoilage Organisms:**
  1. Most putrefying decay bacteria (*Pseudomonas, Proteus, Bacillus*) and deadly enteric pathogens (*Salmonella, Clostridium botulinum*) cannot grow below $\\text{pH} = 4.6$.
  2. The high proton concentration alters bacterial transmembrane electrochemical gradients, denatures outer membrane enzymes, and prevents spore germination.
  3. Consequently, fermented foods (yogurt, sauerkraut, kimchi, fermented sausages, and pickles) remain safely preserved without refrigeration for prolonged periods.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Production of high levels of acid that lower pH and inhibit spoilage microbes):** Correct. Acid production and low pH are the definitive preserving mechanisms of lactic acid bacteria.
- **Option B (Creation of a dry vacuum):** Incorrect. Fermentation occurs in aqueous media without vacuums.
- **Option C (Production of toxic heavy metals):** Incorrect. Bacteria do not synthesize elemental heavy metals.
- **Option D (Release of radiation):** Incorrect. Biological bacteria do not emit nuclear radiation.`
  },
  // Q40 (OSC-028)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-028",
    type: "OSC",
    text: "How do symbiotic and mutualistic relationships between humans and beneficial bacteria like Lactobacilli best exemplify biological adaptation?",
    options: [
      "Bacteria convert human tissue directly into plant matter.",
      "Bacteria parasitize human cells completely without providing any benefits.",
      "Bacteria secure a nutrient-rich habitat in the gut while conferring metabolic advantages such as pathogen exclusion and vitamin synthesis to the host.",
      "Bacteria live independently in soil and never interact with human bodies."
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mutualistic Symbiosis:
**Mutualism** is an interspecific ecological interaction ($+/+$) where both participating species derive substantial evolutionary fitness advantages, reciprocal nutritional benefits, and survival enhancements.

### 2. Biological Context & The Human-Microbe Axis:
- **What the Bacteria Gain:**
  - A homeostatically regulated, warm, aqueous environment ($37^\\circ\\text{C}$) protected from extreme fluctuations.
  - A continuous, abundant influx of dietary carbohydrates, proteins, and fluid substrates for energy.
- **What the Human Host Gains:**
  - **Competitive Barrier:** Probiotic *Lactobacilli* occupy mucosal niches, preventing deadly enteric pathogens from establishing.
  - **Nutritional Synthesis:** Bacteria synthesize essential coenzymes (Vitamin K, $\\text{B}_{12}$, folic acid) and ferment non-digestible fiber into beneficial short-chain fatty acids (butyrate, acetate) that nourish colonic colonocytes.
  - **Immune Priming:** Continuous interaction strengthens the mucosal barrier and trains immune tolerance.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Convert human tissue to plant matter):** Incorrect. Biologically impossible.
- **Option B (Parasitize without providing benefits):** Incorrect. This describes harmful parasitism, not mutualism.
- **Option C (Bacteria secure a nutrient-rich habitat while conferring metabolic advantages to host):** Correct. Perfectly summarizes reciprocal mutualistic symbiosis between gut bacteria and humans.
- **Option D (Live only in soil without interacting):** Incorrect. *Lactobacilli* form dense colonizing populations in mammalian digestive tracts.`
  },
  // Q41 (OSC-029)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-029",
    type: "OSC",
    text: "Why might a person undergoing broad-spectrum antibiotic treatment develop mild digestive disturbances, and how do probiotics counteract this?",
    options: [
      "Antibiotics cause the stomach to shrink; probiotics expand it.",
      "Antibiotics kill both harmful and beneficial gut bacteria, disrupting digestion; probiotics replenish the beneficial bacterial pool.",
      "Antibiotics freeze gut fluids; probiotics heat them up.",
      "Antibiotics turn milk into poison; probiotics remove poison."
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Antibiotic-Induced Dysbiosis:
Broad-spectrum antibiotics are designed to kill or inhibit a wide range of bacterial pathogens by targeting universal bacterial structures (such as bacterial ribosomes or peptidoglycan cell walls).

### 2. Biological Process & The Probiotic Remedy:
- **Mechanism of Disturbance (Dysbiosis):**
  - Because broad-spectrum antibiotics cannot distinguish between pathogenic invaders and beneficial commensal bacteria, they eradicate massive populations of native gut *Lactobacilli* and *Bifidobacteria*.
  - This collateral destruction impairs colonic fermentation, reduces short-chain fatty acid production, and allows opportunistic pathogens (such as *Clostridium difficile*) to bloom, resulting in diarrhea, abdominal cramps, and indigestion.
- **Role of Probiotics:**
  - Ingesting probiotic supplements or active curd supplies live, resilient strains that safely transit to the colon, repopulate the mucosal niches, restore acidic $\\text{pH}$, and re-establish a healthy, stable microbial ecosystem.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Stomach shrinks):** Incorrect. Antibiotics do not alter stomach dimensions.
- **Option B (Antibiotics kill both harmful and beneficial gut bacteria; probiotics replenish the pool):** Correct. Accurately explains antibiotic dysbiosis and the therapeutic restoration provided by probiotics.
- **Option C (Freeze gut fluids):** Incorrect. Antibiotics have no cryogenic freezing effects.
- **Option D (Turn milk into poison):** Incorrect. A folk myth; antibiotics do not turn milk into poison.`
  },
  // Q42 (OSC-030)
  {
    questionCode: "MH-9-SCIT-8-8.1-OSC-030",
    type: "OSC",
    text: "Which critical biochemical transformation distinguishes lactic acid fermentation performed by Lactobacilli from alcoholic fermentation performed by yeast?",
    options: [
      "Lactobacilli produce lactic acid as the primary end-product without ethanol/carbon dioxide gas release, whereas yeast produces ethanol and carbon dioxide.",
      "Yeast produces solid iron deposits.",
      "Lactobacilli produce high levels of methane gas.",
      "Lactobacilli produce gold nanoparticles."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Divergent Fermentation Pathways:
Both lactic acid bacteria and brewer's yeast utilize anaerobic glycolysis to generate ATP by breaking down hexose sugars into pyruvate, but they employ distinct terminal enzymes to regenerate oxidized $\\text{NAD}^+$.

### 2. Biological Process & Reaction Comparison:
- **Lactic Acid Fermentation (*Lactobacilli*):**
  - Pyruvate is directly reduced by **lactate dehydrogenase**:
    $$\\text{C}_6\\text{H}_{12}\\text{O}_6 \\longrightarrow 2\\text{CH}_3\\text{CH(OH)COOH (Lactic Acid)} + 2\\text{ATP}$$
  - There is **no decarboxylation**: no carbon dioxide ($\\text{CO}_2$) gas is released, and no ethanol is formed. The chemical energy remains in the 3-carbon lactic acid molecule.
- **Alcoholic Fermentation (*Yeast - Saccharomyces*):**
  - Pyruvate undergoes decarboxylation by *pyruvate decarboxylase* followed by reduction by *alcohol dehydrogenase*:
    $$\\text{C}_6\\text{H}_{12}\\text{O}_6 \\longrightarrow 2\\text{C}_2\\text{H}_5\\text{OH (Ethanol)} + 2\\text{CO}_2 \\uparrow + 2\\text{ATP}$$
  - Generates volatile **ethanol** and gaseous **carbon dioxide** (which causes dough to rise and beer to froth).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Lactobacilli produce lactic acid without ethanol/$\\text{CO}_2$, whereas yeast produces ethanol and $\\text{CO}_2$):** Correct. Accurately contrasts the distinct end-products of the two fermentation pathways.
- **Option B (Yeast produces iron):** Incorrect. Biological fermentation does not synthesize iron.
- **Option C (Lactobacilli produce methane):** Incorrect. Methane is produced by methanogenic archaea, not *Lactobacilli*.
- **Option D (Produce gold):** Incorrect. Pure fantasy.`
  },
  // Q43 (OTF-001)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-001",
    type: "OTF",
    text: "Lactobacilli are rod-shaped, aerobic or facultatively anaerobic bacteria.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "True",
    solution: `### 1. Scientific Principle & Physiological Classification of Lactobacilli:
Bacteria of the genus *Lactobacillus* are gram-positive, non-spore-forming, cylindrical rod-shaped prokaryotes belonging to the order Lactobacillales.

### 2. Biological Process & Oxygen Relationships:
- Most *Lactobacillus* species are aerotolerant anaerobes or **facultative anaerobes**.
- While they do not utilize oxygen for cellular respiration (they lack functional cytochromes and catalase), they possess protective manganese complexes or peroxidase systems that allow them to survive in the presence of atmospheric oxygen, while flourishing vigorously under the microaerophilic or anaerobic conditions found in deep milk containers and the mammalian gastrointestinal lumen.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement asserts that *Lactobacilli* are rod-shaped (which is anatomically true, bacillus morphology) and facultatively anaerobic/aerotolerant (which is physiologically true).
- **Conclusion:** The statement is completely accurate.
- **Option True is correct.**`
  },
  // Q44 (OTF-002)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-002",
    type: "OTF",
    text: "Probiotics contain active bacteria that are harmful to human health.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Definition of Probiotics:
By scientific and medical definition (FAO/WHO), **probiotics** are:
> *"Live microorganisms that, when administered in adequate amounts, confer a health benefit on the host."*

### 2. Biological Process & Health Benefits:
- Probiotics contain thoroughly tested, non-pathogenic, beneficial mutualistic strains such as *Lactobacillus acidophilus*, *Bifidobacterium bifidum*, and *Lactobacillus rhamnosus*.
- Far from being harmful, they:
  1. Compete against and eliminate virulent food-borne pathogens (*Salmonella, Clostridium*).
  2. Aid in the digestion of dietary fiber and lactose.
  3. Synthesize essential Vitamin B-complex vitamins and Vitamin K.
  4. Reinforce gut mucosal immunity and reduce systemic inflammation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement claims that probiotic bacteria are harmful to human health.
- **Factual Verification:** This statement is completely false; probiotics are therapeutic and beneficial, having full Generally Recognized as Safe (GRAS) status.
- **Option False is correct.**`
  },
  // Q45 (OTF-003)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-003",
    type: "OTF",
    text: "Lactobacilli convert milk proteins directly into alcohol.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Fermentation Specificity:
Microbial fermentation pathways are biochemically substrate-specific and enzyme-limited.

### 2. Biological Process & The Reaction Pathway:
- *Lactobacilli* ferment the **disaccharide sugar lactose**, NOT milk proteins.
- Furthermore, their homofermentative metabolic pathway converts lactose into **lactic acid**, NOT alcohol:
  $$\\text{Lactose} \\longrightarrow \\text{Lactic Acid}$$
- Alcoholic fermentation (converting sugars into ethanol and carbon dioxide) is carried out by **yeast (*Saccharomyces cerevisiae*)**, not by *Lactobacilli*.
- Milk proteins (casein) are simply coagulated by the acid produced; they are not turned into alcohol.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement claims that *Lactobacilli* convert milk proteins into alcohol.
- **Factual Verification:** Both parts of the statement are incorrect (they ferment lactose, not protein; and they produce lactic acid, not alcohol).
- **Option False is correct.**`
  },
  // Q46 (OTF-004)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-004",
    type: "OTF",
    text: "All bacteria present in dairy products are harmful to human health.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Helpful vs. Harmful Microbes:
Microorganisms in food science are divided into three distinct categories:
1. **Beneficial / Fermentative Microbes:** Improve texture, flavor, and preservation (*e.g., Lactobacilli*).
2. **Spoilage Microbes:** Cause souring or foul odors (*e.g., Pseudomonas*).
3. **Pathogenic Microbes:** Cause disease (*e.g., Mycobacterium bovis, Salmonella*).

### 2. Biological Process & Dairy Probiotics:
- Millions of metric tons of yogurt, curd, cheese, and buttermilk consumed daily across the world owe their existence, health benefits, and nutritional enhancement to live bacteria.
- Beneficial lactic acid bacteria like *Lactobacillus acidophilus* and *Streptococcus thermophilus* promote digestion, boost immunity, and prevent bowel infections.
- Asserting that *all* bacteria in dairy are harmful represents a fundamental microbiological misconception.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement makes an absolute claim that every bacterium in dairy products is harmful.
- **Factual Verification:** Many dairy bacteria are essential mutualists and probiotics vital for human health.
- **Option False is correct.**`
  },
  // Q47 (OTF-005)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-005",
    type: "OTF",
    text: "Lactobacilli bacteria can survive and multiply in acidic environments created by their own metabolic byproduct.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "True",
    solution: `### 1. Scientific Principle & Acidotolerance (Aciduric Nature):
Most bacteria are neutrophilic, perishing when environmental $\\text{pH}$ drops below $5.5$. In contrast, lactic acid bacteria are **acidophilic / acidotolerant (aciduric)**.

### 2. Biological Process & Physiological Adaptations:
- As *Lactobacilli* ferment milk sugars, they accumulate lactic acid, driving the medium $\\text{pH}$ down to $4.5\\text{--}3.8$.
- While this acidity halts the growth of competing putrefactive bacteria, *Lactobacilli* continue to survive and multiply.
- **Survival Mechanisms:**
  1. Membrane-bound $\\text{F}_1\\text{F}_0\\text{-ATPase}$ proton pumps actively pump excess intracellular $\\text{H}^+$ ions out of the cytoplasm into the medium, maintaining a stable neutral internal $\\text{pH}$.
  2. Alterations in membrane fatty acid composition (increasing cyclopropane fatty acids) reduce membrane proton permeability.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement asserts that *Lactobacilli* can survive and grow in the acidic environment created by their own lactic acid byproduct.
- **Factual Verification:** This statement is scientifically true and describes their definitive acidotolerant physiology.
- **Option True is correct.**`
  },
  // Q48 (OTF-006)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-006",
    type: "OTF",
    text: "Lactobacilli are eukaryotic microorganisms.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Biological Domain Classification:
All cellular life is divided into two structural categories: **Prokaryotes** (Domains Bacteria and Archaea) and **Eukaryotes** (Domain Eukarya: Protists, Fungi, Plants, Animals).

### 2. Biological Process & Prokaryotic Cytology of Lactobacilli:
- *Lactobacilli* are true eubacteria belonging to the phylum Bacillota (Firmicutes).
- **Prokaryotic Hallmarks:**
  - Complete absence of a membrane-bound nucleus (DNA is a naked circular nucleoid).
  - Complete absence of membrane-bound organelles (no mitochondria, endoplasmic reticulum, or Golgi apparatus).
  - Protein synthesis mediated by small **70S ribosomes** (eukaryotes possess 80S cytosolic ribosomes).
- Claiming that *Lactobacilli* are eukaryotes is biologically false.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement asserts that *Lactobacilli* are eukaryotic microorganisms.
- **Factual Verification:** *Lactobacilli* are true prokaryotic bacteria, NOT eukaryotes.
- **Option False is correct.**`
  },
  // Q49 (OTF-007)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-007",
    type: "OTF",
    text: "High cooking temperatures destroy Lactobacilli bacteria present in yogurt.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "True",
    solution: `### 1. Scientific Principle & Thermal Susceptibility of Vegetative Bacteria:
Vegetative bacterial cells lack protective endospores and are susceptible to thermal inactivation through the denaturation of structural proteins and enzymes.

### 2. Biological Process & Thermal Death:
- *Lactobacillus* species are non-spore-forming mesophiles and thermotolerant bacteria.
- When yogurt or curd is subjected to high cooking temperatures (such as boiling in curries, baking, or frying at temperatures exceeding $65^\\circ\\text{C}\\text{--}100^\\circ\\text{C}$):
  - Hydrogen bonds stabilizing bacterial enzymes are broken.
  - Active site conformations collapse, and bacterial cell membranes lyse.
  - 100% of the live probiotic *Lactobacilli* are destroyed (thermal death).
- While the nutritional proteins and lactic acid remain, the live probiotic benefits are completely lost upon high heat cooking.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement asserts that high cooking temperatures destroy the *Lactobacilli* bacteria in yogurt.
- **Factual Verification:** This statement is completely accurate.
- **Option True is correct.**`
  },
  // Q50 (OTF-008)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-008",
    type: "OTF",
    text: "Lactobacilli require organic nutrients to carry out fermentation.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "True",
    solution: `### 1. Scientific Principle & Chemoorganotrophic Nutrition:
Living organisms are classified by their nutritional modes:
- **Autotrophs:** Fix inorganic carbon dioxide into organic food using light or inorganic chemicals.
- **Chemoorganotrophs (Heterotrophs):** Must obtain pre-formed organic compounds from their environment as sources of both carbon and chemical energy.

### 2. Biological Process & Substrate Requirements:
- *Lactobacilli* are fastidious chemoorganotrophic heterotrophs.
- They completely lack photosynthetic pigments and cannot fix $\\text{CO}_2$.
- To survive, divide, and carry out lactic fermentation, they require:
  1. **Fermentable Carbohydrates:** Such as the disaccharide **lactose** or monosaccharides glucose and galactose.
  2. **Amino Acids and Peptides:** Derived from milk casein.
  3. **Vitamins and Purines/Pyrimidines:** To support DNA replication and cofactor synthesis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement states that *Lactobacilli* require organic nutrients to carry out fermentation.
- **Factual Verification:** This statement is scientifically true.
- **Option True is correct.**`
  },
  // Q51 (OTF-009)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-009",
    type: "OTF",
    text: "Adding excessive amounts of starter culture at a very low temperature will set yogurt instantly.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Kinetic Limitations of Low Temperature:
Enzyme-catalyzed biochemical reactions require molecular kinetic energy to overcome the activation energy barrier ($E_a$):
$$k = A e^{-E_a / (RT)}$$

### 2. Biological Process & Cold Inactivation:
- In refrigerated or cold conditions ($0^\\circ\\text{C}\\text{--}10^\\circ\\text{C}$):
  - Lipid bilayers in bacterial membranes solidify into a rigid, non-fluid gel state, halting transport permease activity.
  - Molecular collision rates between enzymes and substrate molecules drop toward zero.
- Even if a massive quantity of starter culture is dumped into cold milk:
  - The bacteria cannot metabolize lactose at near-zero temperatures.
  - No lactic acid is produced, no drop in $\\text{pH}$ occurs, and casein proteins will **never coagulate** into yogurt.
- Setting curd requires both bacterial inoculum **and** an appropriate warm incubation temperature ($37^\\circ\\text{C}\\text{--}42^\\circ\\text{C}$).

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement claims that adding excessive starter culture at very low temperature sets yogurt instantly.
- **Factual Verification:** This statement is completely false; cold halts fermentation regardless of culture volume.
- **Option False is correct.**`
  },
  // Q52 (OTF-010)
  {
    questionCode: "MH-9-SCIT-8-8.1-OTF-010",
    type: "OTF",
    text: "Lactobacilli play a crucial role in converting plant fibers into wood pulp.",
    options: [
      "False",
      "True"
    ],
    correctAnswer: "False",
    solution: `### 1. Scientific Principle & Lignocellulose Degradation vs. Lactic Fermentation:
Plant cell walls are composed of recalcitrant structural biopolymers: **cellulose, hemicellulose, and lignin**.

### 2. Biological Process & Substrate Specificity:
- Decomposing wood and plant fibers to produce paper pulp requires specialized **ligninolytic and cellulolytic enzymes** (such as lignin peroxidase, laccase, and cellulase complexes).
- These enzymes are produced by wood-rotting **white-rot and brown-rot fungi** (e.g., *Phanerochaete chrysosporium, Trichoderma*) and certain actinomycetes, or through industrial chemical processes (the Kraft pulping process).
- *Lactobacilli* completely lack cellulase and ligninase genes; they specialize in fermenting simple soluble mono- and disaccharides (lactose, glucose, sucrose) in dairy, vegetable pickling, and silage, having **zero role in industrial wood pulping**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Statement Analysis:** The statement claims that *Lactobacilli* convert plant fibers into wood pulp.
- **Factual Verification:** This statement is completely false; wood pulping is performed by cellulolytic fungi and chemical treatments, not dairy *Lactobacilli*.
- **Option False is correct.**`
  }
];

const fullPart1 = [
  ...first10,
  ...remaining
];

console.log(`Total questions in Part 1: ${fullPart1.length}`);
if (fullPart1.length !== 52) {
  console.error(`ERROR: Expected 52 questions, got ${fullPart1.length}`);
  process.exit(1);
}

fs.writeFileSync('scripts/ch8_part1.js', 'const ch8_part1 = ' + JSON.stringify(fullPart1, null, 2) + ';\n\nmodule.exports = { ch8_part1 };\n', 'utf8');
console.log('Successfully saved full 52 questions to scripts/ch8_part1.js');
