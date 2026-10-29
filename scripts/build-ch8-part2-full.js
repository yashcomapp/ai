// scripts/build-ch8-part2-full.js
const fs = require('fs');

const part2 = [
  // Q53 (OAR-001)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-001",
    type: "OAR",
    text: "Assertion (A): Cultivation of leguminous crops helps enrich the soil with nitrogenous compounds.\nReason (R): Rhizobium bacteria fix atmospheric nitrogen into compounds that become available in the soil.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Biological Nitrogen Fixation:
Molecular atmospheric dinitrogen ($\\text{N}_2$) comprises approximately $78\\%$ of the Earth's atmosphere, but plants cannot absorb or metabolize it directly due to the exceptionally high dissociation energy of its chemical triple bond ($\\text{N}\\equiv\\text{N}$, $945\\text{ kJ/mol}$).

### 2. Biological Process & The Rhizobial Mechanism:
- Leguminous plants (Family Fabaceae, e.g., peas, beans, clover, soybeans, groundnuts) form a mutualistic symbiotic association with diazotrophic soil bacteria of the genus **Rhizobium**.
- Inside specialized root nodules, *Rhizobium* expresses the enzyme **nitrogenase**, which catalytically reduces inert atmospheric $\\text{N}_2$ into bioavailable ammonia ($\\text{NH}_3$):
  $$\\text{N}_2 + 8\\text{H}^+ + 8e^- + 16\\text{ATP} \\xrightarrow{\\text{Nitrogenase}} 2\\text{NH}_3 + \\text{H}_2 + 16\\text{ADP} + 16\\text{P}_i$$
- While much of this ammonia is assimilated into plant proteins, significant quantities of amino acids, nitrates, and nitrites are sloughed off into the rhizosphere and returned to the topsoil when root nodules decompose post-harvest, substantially enriching soil fertility.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Cultivating legumes naturally boosts soil nitrogen levels without requiring synthetic chemical fertilizers.
- **Reason (R) Evaluation:** True. Symbiotic *Rhizobium* bacteria convert atmospheric $\\text{N}_2$ into bioavailable nitrogenous compounds.
- **Causal Connection:** Reason (R) provides the direct biological explanation for Assertion (A).
- **Option A is correct.** Both statements are true, and Reason is the correct explanation of Assertion.`
  },
  // Q54 (OAR-002)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-002",
    type: "OAR",
    text: "Assertion (A): Crop rotation involving leguminous and non-leguminous crops replenishes soil nitrogen naturally.\nReason (R): Legumes harbor Rhizobium in their root nodules which add usable nitrogen compounds to the soil.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Agronomic Crop Rotation:
Cereal crops (such as wheat, rice, maize, and sugarcane) are heavy nitrogen feeders that rapidly deplete soil nitrate and ammonium reserves, leading to soil exhaustion if grown in continuous monoculture.

### 2. Biological Process & Nutrient Cycling:
- In classical **crop rotation**, a cereal crop is alternated with a leguminous pulse or forage crop (e.g., chickpea, pigeon pea, alfalfa).
- The root nodules of the legumes harbor active **Rhizobium** colonies.
- The bacteria fix up to $100\\text{--}300\\text{ kg}$ of atmospheric nitrogen per hectare per growing season.
- After harvesting the legume seeds, the decomposing root residues, nodules, and foliage (green manure) release bound nitrogen into the soil, replenishing mineral fertility for the subsequent cereal crop without heavy reliance on synthetic urea.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Crop rotation with legumes prevents soil exhaustion and restores organic nitrogen.
- **Reason (R) Evaluation:** True. *Rhizobium* in legume root nodules converts atmospheric $\\text{N}_2$ into soil-available nitrogen.
- **Causal Connection:** Reason (R) correctly explains why crop rotation replenishes soil nitrogen.
- **Option A is correct.** Both statements are true, and Reason is the correct explanation of Assertion.`
  },
  // Q55 (OAR-003)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-003",
    type: "OAR",
    text: "Assertion (A): Rhizobium bacteria cannot fix nitrogen independently in laboratory culture without plant signals.\nReason (R): The establishment of symbiosis and activation of nitrogen fixation genes require specific molecular communication between the host legume and the bacterium.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Symbiotic Gene Regulation:
Free-living soil diazotrophs like *Azotobacter* can fix nitrogen independently, but *Rhizobium* is an obligate symbiotic diazotroph whose nitrogenase expression is strictly locked under free-living soil conditions.

### 2. Biological Process & Molecular Signaling:
1. **Flavonoid Exudation:** The roots of leguminous plants secrete specific chemical signal molecules called **flavonoids** or isoflavonoids into the rhizosphere.
2. **Nod Factor Induction:** These flavonoids bind to the bacterial regulatory protein NodD, activating the transcription of bacterial *nod* genes (*nodABC*), which synthesize lipochitooligosaccharide signaling molecules called **Nod factors**.
3. **Nodule Morphogenesis:** Nod factors trigger root hair curling, cortical cell division, and infection thread formation.
4. **Bacteroid Differentiation & nif Gene Activation:** Only inside the microaerophilic environment of the host root nodule are the bacterial **nif (nitrogen fixation) genes** derepressed to synthesize the oxygen-sensitive enzyme nitrogenase.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. *Rhizobium* grown in pure laboratory agar or liquid broth does not fix nitrogen under normal atmospheric conditions.
- **Reason (R) Evaluation:** True. Molecular cross-talk between host flavonoids and bacterial Nod factors is mandatory to activate symbiosis and *nif* gene expression.
- **Causal Connection:** Reason (R) provides the precise biochemical rationale for Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason correctly explains Assertion.`
  },
  // Q56 (OAR-004)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-004",
    type: "OAR",
    text: "Assertion (A): Rhizobium bacteria inside root nodules lose their free-living flagella and transform into swollen structures called bacteroids.\nReason (R): This morphological transformation is a structural adaptation necessary for carrying out efficient nitrogen fixation within host plant cells.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Bacteroid Cytology:
Inside the developing root nodule, *Rhizobium* undergoes terminal morphological and physiological differentiation.

### 2. Biological Process & Cellular Transformation:
- When free-swimming flagellated rod-shaped *Rhizobium* cells enter host plant cortical cells via the infection thread, they are endocytosed into the host cytoplasm, remaining surrounded by a host-derived membrane called the **peribacteroid membrane** (forming a functional symbiosome).
- In response to plant-secreted antimicrobial peptides (NCR peptides), the bacteria halt binary fission and undergo extensive DNA endoreduplication.
- They swell up to 5–10 times their original size, shed their flagella, and alter their cell envelope into irregular, branched, Y-shaped, or pleomorphic structures termed **bacteroids**.
- In this specialized bacteroid state, cellular energy is redirected almost entirely from cell division toward the synthesis of the nitrogenase enzyme complex and high-flux nitrogen fixation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Symbiotic *Rhizobia* shed flagella, swell dramatically, and differentiate into bacteroids.
- **Reason (R) Evaluation:** True. This terminal differentiation reorganizes metabolism to maximize nitrogen fixation.
- **Causal Connection:** Reason (R) directly explains the evolutionary purpose of bacteroid transformation.
- **Option A is correct.** Both statements are true, and Reason is the correct explanation of Assertion.`
  },
  // Q57 (OAR-005)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-005",
    type: "OAR",
    text: "Assertion (A): Leguminous seeds are often rich in proteins compared to many cereal grains.\nReason (R): The abundant supply of fixed nitrogen provided by symbiotic Rhizobium enables plants to synthesize large amounts of amino acids and proteins.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Nitrogen-to-Protein Biosynthesis:
Proteins are biological macromolecules composed of linear chains of $\\alpha$-amino acids. The fundamental chemical building blocks of all amino acids contain an amine group ($-\\text{NH}_2$), making **nitrogen** the primary limiting nutrient for protein synthesis.

### 2. Biological Process & Legume Seed Enrichment:
- While non-leguminous cereals (rice, wheat) rely solely on limited mineral nitrate absorbed from soil water (resulting in high carbohydrate starch accumulation, but only $8\\text{--}12\\%$ protein), legumes receive an unlimited, direct supply of reduced nitrogen ($\\text{NH}_4^+$) from symbiotic *Rhizobium*.
- The fixed ammonium is assimilated into **glutamine** and **glutamate** via the GS-GOGAT (glutamine synthetase / glutamate synthase) pathway.
- These amino acids are translocated to developing seeds, where they are synthesized into dense storage globulins (**legumin** and **vicilin**).
- Consequently, pulse and legume seeds (soybeans, lentils, chickpeas, peas) contain exceptionally high protein concentrations, typically **$20\\text{--}40\\%$ by dry weight**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Pulses and legume seeds are renowned for high protein content compared to starch-heavy cereals.
- **Reason (R) Evaluation:** True. Symbiotic nitrogen fixation supplies abundant nitrogen precursors for amino acid synthesis.
- **Causal Connection:** Reason (R) provides the direct biochemical mechanism for the high protein content in Assertion (A).
- **Option A is correct.** Both Assertion and Reason are true, and Reason correctly explains Assertion.`
  },
  // Q58 (OAR-006)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OAR-006",
    type: "OAR",
    text: "Assertion (A): Ineffective strains of Rhizobium can form nodules on legume roots that fail to fix nitrogen (so-called 'cheater' or ineffective nodules).\nReason (R): Nodulation and nitrogen fixation are genetically separable traits, and some bacterial strains may trick the plant into providing food without providing fixed nitrogen in return.",
    options: [
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
      "Assertion (A) is true, but Reason (R) is false.",
      "Assertion (A) is false, but Reason (R) is true."
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Evolutionary Cheating in Mutualisms:
Mutualisms are vulnerable to evolutionary exploitation where one partner reaps benefits without contributing reciprocal services.

### 2. Biological Process & Ineffective Nodulation:
- In the *Rhizobium*-legume symbiosis:
  - **Nodulation genes (*nod* genes):** Control infection thread development, root hair curling, and nodule organogenesis.
  - **Nitrogen fixation genes (*nif* and *fix* genes):** Control the synthesis and operation of the nitrogenase enzyme complex.
- Because these gene sets are distinct and genetically separable (often located on mobile plasmids or symbiotic islands), certain wild strains of *Rhizobium* possess intact *nod* genes but defective or absent *nif* genes ($Nod^+ Fix^-$).
- These "ineffective" strains infect legume roots, inducing small white or pale nodules, and consume plant photosynthates without returning any fixed nitrogen.
- Plants respond through **host sanctions**: selectively restricting oxygen and nutrient allocation to non-fixing nodules to penalize cheating strains.

### 3. Step-by-Step Option & Misconception Analysis:
- **Assertion (A) Evaluation:** True. Ineffective nodules formed by $Fix^-$ strains fail to fix nitrogen.
- **Reason (R) Evaluation:** True. Nodulation and nitrogen fixation are controlled by separate gene systems (*nod* vs. *nif*).
- **Causal Connection:** Reason (R) correctly explains how ineffective nodules arise.
- **Option A is correct.** Both statements are true, and Reason is the correct explanation of Assertion.`
  },
  // Q59 (OMC-001)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OMC-001",
    type: "OMC",
    text: "Which of the following plants belong to the leguminous family (Fabaceae) that typically form symbiotic root nodules with Rhizobium?",
    options: [
      "Wheat (Triticum aestivum)",
      "Pea (Pisum sativum)",
      "Soybean (Glycine max)",
      "Groundnut (Arachis hypogaea)"
    ],
    correctAnswer: "B, C, D",
    solution: `### 1. Scientific Principle & Host Plant Families for Rhizobium:
Biological nitrogen fixation by *Rhizobium* is phylogenetically restricted almost exclusively to members of the angiosperm family **Fabaceae** (Leguminosae).

### 2. Biological Process & Plant Grouping:
- **Pea (*Pisum sativum*):** A quintessential legume with root nodules colonized by *Rhizobium leguminosarum* symbiovar *viciae*.
- **Soybean (*Glycine max*):** A major oilseed legume colonized by *Bradyrhizobium japonicum*.
- **Groundnut / Peanut (*Arachis hypogaea*):** A geocarpic legume colonized by cowpea-type *Bradyrhizobium*.
- **Wheat (*Triticum aestivum*):** Belongs to the monocotyledonous grass family **Poaceae (Gramineae)**. Cereal grasses do not form symbiotic root nodules with *Rhizobium*.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Wheat):** Incorrect. Cereal grass (Poaceae), not a legume.
- **Option B (Pea):** Correct. Legume belonging to Fabaceae.
- **Option C (Soybean):** Correct. Leguminous crop plant.
- **Option D (Groundnut):** Correct. Legume that forms abundant nitrogen-fixing root nodules.
- **Correct Options are B, C, and D.**`
  },
  // Q60 (OMC-002)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OMC-002",
    type: "OMC",
    text: "Which of the following cellular components or biochemical molecules are essential for effective symbiotic nitrogen fixation within root nodules?",
    options: [
      "Leghemoglobin",
      "Nitrogenase enzyme complex",
      "Differentiated bacteroids",
      "Photosynthetic Chloroplasts"
    ],
    correctAnswer: "A, B, C",
    solution: `### 1. Scientific Principle & Biochemistry of Nitrogen Fixation:
Symbiotic nitrogen fixation in root nodules requires a specialized biochemical and cellular micro-environment.

### 2. Biological Process & Key Molecular Components:
1. **Nitrogenase Enzyme Complex:** The Mo-Fe catalytic enzyme that reduces $\\text{N}_2$ to $\\text{NH}_3$.
2. **Leghemoglobin:** A pink oxygen-binding hemoprotein synthesized jointly by the host plant (globin) and bacterium (heme). It scavenges free dissolved oxygen down to nanomolar levels (preventing irreversible inactivation of nitrogenase) while delivering oxygen at high flux to bacteroid respirasomes for ATP production.
3. **Bacteroids:** Differentiated, enlarged, Y-shaped bacterial cells that house nitrogenase.
4. **Chloroplasts:** Root nodules grow underground in total darkness; they contain **zero chloroplasts** (photosynthesis occurs in leaves, and sucrose is transported down to the nodule via phloem).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Leghemoglobin):** Correct. Essential oxygen scavenger.
- **Option B (Nitrogenase enzyme):** Correct. The primary catalyst of $\\text{N}_2$ reduction.
- **Option C (Differentiated bacteroids):** Correct. The specialized bacterial state carrying out the reaction.
- **Option D (Chloroplasts):** Incorrect. Root nodules are non-photosynthetic subterranean organs.
- **Correct Options are A, B, and C.**`
  },
  // Q61 (OMC-003)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OMC-003",
    type: "OMC",
    text: "Which of the following benefits are gained by leguminous plants from their symbiotic association with Rhizobium?",
    options: [
      "Enhanced growth and vigor in nitrogen-deficient soils",
      "Substantially improved protein content in developing seeds",
      "Protection from soil pests through bacterial toxins",
      "Direct availability of usable nitrogenous compounds without requiring synthetic urea"
    ],
    correctAnswer: "A, B, D",
    solution: `### 1. Scientific Principle & Ecological Advantages of Symbiosis:
Symbiosis between legumes and *Rhizobium* confers substantial physiological, ecological, and agronomic benefits to the host plant.

### 2. Biological Process & Host Benefits:
- **Direct Nitrogen Nutrition:** Fixed ammonium is directly assimilated into amino acids, bypassing dependency on scarce soil nitrates or synthetic fertilizers.
- **Colonization of Poor Soils:** Legumes can thrive and establish in sandy, gravelly, or exhausted soils where non-legumes starve.
- **Protein Synthesis:** Abundant reduced nitrogen is translocated into seeds, yielding high protein concentrations ($20\\text{--}40\\%$).
- **Pest Defense Myth:** *Rhizobium* does NOT produce insecticidal toxins (like *Bacillus thuringiensis* / Bt toxin); its role is purely nutritional.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Enhanced growth in poor soils):** Correct. Bypasses nitrogen limitations.
- **Option B (Improved protein content):** Correct. Fuels amino acid and protein biosynthesis.
- **Option C (Protection via toxins):** Incorrect. *Rhizobia* are nutrient-fixing mutualists, not pesticide-producing bacteria.
- **Option D (Direct availability of nitrogen):** Correct. Eliminates dependency on chemical urea.
- **Correct Options are A, B, and D.**`
  },
  // Q62 (OMC-004)
  {
    questionCode: "MH-9-SCIT-8-8.1.2-OMC-004",
    type: "OMC",
    text: "Which of the following experimental observations confirm that a root nodule on a legume is actively fixing nitrogen rather than being inactive or senescent?",
    options: [
      "Internal tissue exhibits a distinct pink or reddish-brown coloration upon cross-sectioning",
      "The host plant exhibits dark green, healthy foliage rather than chlorotic yellow leaves",
      "Internal tissue is completely pale white or decaying green",
      "The nodule contains active leghemoglobin and intact bacteroids"
    ],
    correctAnswer: "A, B, D",
    solution: `### 1. Scientific Principle & Morphological Indicators of Nodule Activity:
Field botanists and agronomists evaluate nodule efficacy through cross-sectional dissection and foliage health.

### 2. Biological Process & Nodule Diagnostics:
- **Pink/Red Cross-Section:** An actively fixing nodule contains high concentrations of **leghemoglobin**, which imparts an unmistakable **vivid pink, red, or brownish-red color** to the central bacteroid tissue.
- **White or Green Nodules:**
  - *White nodules:* Immature nodules that have not yet expressed leghemoglobin, or ineffective nodules caused by non-fixing bacterial strains.
  - *Green nodules:* Senescent nodules where the heme iron of leghemoglobin has degraded into green choleglobin, signaling cessation of nitrogen fixation.
- **Plant Foliage:** Active nitrogen fixation prevents nitrogen deficiency (chlorosis), ensuring lush, dark green foliage packed with chlorophyll.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Pink/red cross-section):** Correct. Definitive hallmark of active leghemoglobin.
- **Option B (Dark green foliage):** Correct. Reflects abundant nitrogen nutrition.
- **Option C (Pale white or decaying green):** Incorrect. Indicates inactive or dying nodules.
- **Option D (Contains active leghemoglobin and bacteroids):** Correct. The biological machinery of active fixation.
- **Correct Options are A, B, and D.**`
  }
];

fs.writeFileSync('scripts/ch8_part2_starter.js', 'const part2_starter = ' + JSON.stringify(part2, null, 2) + ';\nmodule.exports = { part2_starter };\n', 'utf8');
console.log('Saved first 10 items of Part 2');
