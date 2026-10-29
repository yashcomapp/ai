# -*- coding: utf-8 -*-
"""
Chapter 17 - Topic 2: Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers
40 Gold Standard Questions (26 OSC, 6 OTF, 4 OAR, 4 OMC)
Canonical topicCode: MH-9-SCIT-17-17.2
"""

topic2_questions = [
    # --- 26 OSC Questions ---
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-001",
        "type": "OSC",
        "bloomLevel": "Analyze",
        "difficulty": "medium",
        "conceptTag": "Bt Cotton mechanism of action",
        "text": "In genetically modified Bt cotton, what specific physiological mechanism causes the mortality of the bollworm caterpillar upon ingesting the plant tissues?",
        "options": [
            "The plant produces acidic secretions that corrode the insect's outer cuticle.",
            "Inactive crystal protoxins dissolve in the insect's alkaline midgut, get cleaved by proteases into active endotoxins, and perforate epithelial cells causing lysis.",
            "The plant synthesizes volatile neurotoxins that instantly paralyze the insect's respiratory spiracles.",
            "The plant induces hyper-osmotic dehydration by extracting water from the insect's hemolymph."
        ],
        "correctAnswer": "B",
        "solution": """**Key Concept:**
The bacterium *Bacillus thuringiensis* produces inactive crystalline protoxins (Cry proteins) that dissolve specifically in the alkaline environment of the insect midgut (\(\\text{pH} > 9.0\)), where gut proteases cleave them into toxic active forms that bind to epithelial cells, creating lethal pores.

**Option Analysis:**
- **(A) Acidic secretions corroding the outer cuticle** — Incorrect; Cry toxins are ingested proteins that act internally on the gut epithelium, not external topical acids.
- **(B) Inactive crystal protoxins dissolve in the insect's alkaline midgut, get cleaved by proteases into active endotoxins, and perforate epithelial cells causing lysis (Correct)** — Accurately describes the precise biochemical activation and pore-forming lysis mechanism in bollworm caterpillars.
- **(C) Volatile neurotoxins paralyzing respiratory spiracles** — Incorrect; Cry proteins are pore-forming pore toxins targeting digestive tract cells, not aerosol neurotransmitter blockers.
- **(D) Hyper-osmotic dehydration of hemolymph** — Incorrect; mortality results from midgut cell rupture, gut leakage, and starvation/septicemia, not osmotic water extraction."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-002",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Bacterial origin of Bt gene",
        "text": "Which soil bacterium serves as the natural genetic source for the insecticidal Cry genes incorporated into Bt crops?",
        "options": [
            "Azotobacter chroococcum",
            "Rhizobium leguminosarum",
            "Bacillus thuringiensis",
            "Agrobacterium tumefaciens"
        ],
        "correctAnswer": "C",
        "solution": """**Key Concept:**
The acronym 'Bt' stands for *Bacillus thuringiensis*, a common Gram-positive, spore-forming soil bacterium that naturally synthesizes crystalline protein inclusions lethal to specific insect orders.

**Option Analysis:**
- **(A) Azotobacter chroococcum** — Incorrect; a free-living aerobic nitrogen-fixing bacterium used as a biofertiliser.
- **(B) Rhizobium leguminosarum** — Incorrect; a symbiotic nitrogen-fixing bacterium inhabiting legume root nodules.
- **(C) Bacillus thuringiensis (Correct)** — The specific soil bacterium from which the crystal protein (Cry) genes are isolated for genetic modification.
- **(D) Agrobacterium tumefaciens** — Incorrect; a natural plant genetic engineer often used as a cloning vector, but not the donor of the Cry endotoxin gene."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-003",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Golden Rice nutritional enhancement",
        "text": "Golden Rice was genetically engineered primarily to synthesize which nutrient precursor in its edible endosperm to combat childhood deficiency diseases?",
        "options": [
            "Ascorbic acid (precursor of Vitamin C)",
            "Beta-carotene (provitamin precursor of Vitamin A)",
            "Cobalamin (Vitamin B12)",
            "Calciferol (Vitamin D3)"
        ],
        "correctAnswer": "B",
        "solution": """**Key Concept:**
Golden Rice (*Oryza sativa*) is genetically engineered to express the biosynthetic pathway for \(\\beta\)-carotene (provitamin A) in the edible grain endosperm, providing a dietary solution to childhood night blindness and xerophthalmia in rice-dependent populations.

**Option Analysis:**
- **(A) Ascorbic acid** — Incorrect; Vitamin C is abundant in citrus fruits and synthesized independently of the carotenoid pathway.
- **(B) Beta-carotene (provitamin precursor of Vitamin A) (Correct)** — Two introduced genes (phytoene synthase and carotene desaturase) enable the rice endosperm to produce \(\\beta\)-carotene, giving the grains their golden-yellow hue.
- **(C) Cobalamin** — Incorrect; Vitamin B12 is synthesized exclusively by certain bacteria and archaea, not engineered plants.
- **(D) Calciferol** — Incorrect; Vitamin D3 is synthesized photochemically in animal skin or found in animal fats."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-004",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Symbiotic nitrogen fixation",
        "text": "Which bacterium forms a symbiotic association with the root nodules of leguminous plants to fix atmospheric nitrogen into usable ammonium compounds?",
        "options": [
            "Rhizobium",
            "Lactobacillus acidophilus",
            "Clostridium botulinum",
            "Streptomyces griseus"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Rhizobium* species infect legume root hairs to form specialized root nodules where bacterial nitrogenase enzymes convert inert atmospheric dinitrogen (\(\\ce{N2}\)) into plant-absorbable ammonium (\(\\ce{NH4+}\)).

**Option Analysis:**
- **(A) Rhizobium (Correct)** — The canonical symbiotic bacterium that establishes nitrogen-fixing nodules with pulses, beans, and peas.
- **(B) Lactobacillus acidophilus** — Incorrect; a lactic acid-producing bacterium used in dairy fermentation (curd and yogurt).
- **(C) Clostridium botulinum** — Incorrect; an anaerobic spore-former that produces the potent neurotoxin responsible for botulism food poisoning.
- **(D) Streptomyces griseus** — Incorrect; an actinobacterium cultivated in industrial biotechnology to produce the antibiotic streptomycin."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-005",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Free-living nitrogen fixers",
        "text": "Which of the following organisms is an example of an aerobic, free-living nitrogen-fixing bacterium commonly formulated into agricultural biofertilisers?",
        "options": [
            "Azotobacter",
            "Penicillium notatum",
            "Saccharomyces cerevisiae",
            "Escherichia coli"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Azotobacter* is an aerobic, free-living soil bacterium capable of fixing atmospheric nitrogen non-symbiotically, widely applied as a microbial inoculant for non-leguminous crops like wheat, rice, and vegetables.

**Option Analysis:**
- **(A) Azotobacter (Correct)** — Independent, free-living aerobic nitrogen-fixing bacterium used commercially as a sustainable biofertiliser.
- **(B) Penicillium notatum** — Incorrect; a saprophytic fungus renowned for producing the antibiotic penicillin, incapable of nitrogen fixation.
- **(C) Saccharomyces cerevisiae** — Incorrect; baker's and brewer's yeast utilized for alcoholic fermentation and leavening.
- **(D) Escherichia coli** — Incorrect; a common enteric gut bacterium widely used as a genetic lab model, but lacking nitrogenase activity."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-006",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Cyanobacteria in paddy fields",
        "text": "Which pair of photosynthetic cyanobacteria (blue-green algae) are routinely inoculated into wet paddy (rice) fields as economical biofertilisers?",
        "options": [
            "Nostoc and Anabaena",
            "Yeast and Mucor",
            "Amoeba and Paramecium",
            "Spirogyra and Ulothrix"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Anabaena* and *Nostoc* are photosynthetic cyanobacteria with specialized thick-walled cells called heterocysts containing oxygen-sensitive nitrogenase, enabling them to fix nitrogen efficiently in waterlogged paddy fields.

**Option Analysis:**
- **(A) Nostoc and Anabaena (Correct)** — Filamentous cyanobacteria that enrich waterlogged paddy soils with fixed nitrogen and organic matter.
- **(B) Yeast and Mucor** — Incorrect; heterotrophic fungi that decompose organic matter rather than fixing nitrogen.
- **(C) Amoeba and Paramecium** — Incorrect; heterotrophic protozoans that consume bacteria and micro-algae.
- **(D) Spirogyra and Ulothrix** — Incorrect; green algae (chlorophytes) that carry out photosynthesis but cannot fix atmospheric nitrogen."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-007",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Mycorrhiza biofertiliser function",
        "text": "What is the primary agricultural benefit provided to host plants by symbiotic mycorrhizal fungi (VAM - Vesicular Arbuscular Mycorrhiza)?",
        "options": [
            "Enhanced absorption of poorly mobile soil phosphorus and minerals through extensive hyphal networks.",
            "Direct fixation of gaseous nitrogen inside the fungal spores.",
            "Synthesis of animal proteins to repel herbivorous mammals.",
            "Production of chlorophyll pigments for underground photosynthesis."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Mycorrhiza represents a mutualistic association between plant roots and fungal hyphae; the fungus dramatically expands the root surface area to absorb poorly mobile ions—principally phosphorus—while receiving carbohydrates from the plant.

**Option Analysis:**
- **(A) Enhanced absorption of poorly mobile soil phosphorus and minerals through extensive hyphal networks (Correct)** — Fungal hyphae explore soil micropores beyond root depletion zones to solubilize and uptake phosphorus and micronutrients.
- **(B) Direct fixation of gaseous nitrogen inside fungal spores** — Incorrect; fungi are eukaryotic organisms that lack the bacterial nitrogenase enzyme complex.
- **(C) Synthesis of animal proteins to repel herbivorous mammals** — Incorrect; mycorrhizae are subterranean root symbionts, not producers of foliar mammalian repellents.
- **(D) Production of chlorophyll pigments for underground photosynthesis** — Incorrect; fungi are completely achlorophyllous and depend heterotrophically on plant photosynthates."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-008",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Target pest of Bt Cotton",
        "text": "Which devastating agricultural pest is primarily controlled through the widespread adoption of Bt cotton cultivars?",
        "options": [
            "Cotton bollworm (Pectinophora gossypiella)",
            "Aphids and whiteflies",
            "Locust swarms",
            "Termites"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Bt cotton expressing Cry1Ac and Cry2Ab endotoxins was engineered specifically to control lepidopteran insect pests, predominantly the pink bollworm (*Pectinophora gossypiella*) and spotted bollworm, which bore into developing cotton bolls.

**Option Analysis:**
- **(A) Cotton bollworm (Pectinophora gossypiella) (Correct)** — The primary target caterpillar pest whose larvae feed on flower buds and bolls, causing catastrophic yield loss.
- **(B) Aphids and whiteflies** — Incorrect; sap-sucking hemipteran pests that are not susceptible to standard Cry1/Cry2 endotoxins.
- **(C) Locust swarms** — Incorrect; orthopteran defoliators that migrate in swarms, controlled by contact insecticides or biopesticides like *Metarhizium*.
- **(D) Termites** — Incorrect; subterranean wood-eating isopteran insects with distinct digestive physiology."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-009",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Leghemoglobin function in nodules",
        "text": "What is the crucial biochemical function of the pink-red pigment leghemoglobin present inside active legume root nodules?",
        "options": [
            "It acts as an oxygen scavenger to protect the oxygen-sensitive bacterial nitrogenase enzyme.",
            "It transports carbon dioxide into the plant chloroplasts.",
            "It converts glucose into lactic acid during anaerobic respiration.",
            "It gives roots a bright floral color to attract pollinating bees."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
The bacterial nitrogenase enzyme that catalyzes nitrogen fixation is irreversibly inactivated by molecular oxygen; leghemoglobin binds oxygen with high affinity, maintaining an ultra-low free \(\\ce{O2}\) concentration while supplying sufficient oxygen for bacterial respiration.

**Option Analysis:**
- **(A) It acts as an oxygen scavenger to protect the oxygen-sensitive bacterial nitrogenase enzyme (Correct)** — Essential biological scavenger preserving an anaerobic micro-environment for nitrogenase while facilitating oxygen delivery to bacteroids.
- **(B) Transports carbon dioxide into chloroplasts** — Incorrect; root nodules are underground non-photosynthetic organs; \(\\ce{CO2}\) enters leaves via stomata.
- **(C) Converts glucose into lactic acid** — Incorrect; anaerobic glycolysis produces lactate via lactate dehydrogenase, not hemoglobin.
- **(D) Gives roots bright floral color to attract bees** — Incorrect; bees pollinate aerial flowers, not subterranean root systems."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-010",
        "type": "OSC",
        "bloomLevel": "Analyze",
        "difficulty": "hard",
        "conceptTag": "Safety of Bt toxins to humans",
        "text": "Why do Bt endotoxins pose virtually zero toxic threat to humans, livestock, and other mammalian consumers?",
        "options": [
            "Mammals possess acidic gastric juice (pH ~ 1.5–2.0) that rapidly denatures and digests the protein, and lack the specific midgut epithelial receptors.",
            "Human skin absorbs Bt toxins before they can enter the oral cavity.",
            "Mammals produce anti-Bt antibodies naturally from birth.",
            "Bt toxins convert into pure glucose when swallowed by mammals."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Bt Cry toxins require two specific biological criteria to exert toxicity: an alkaline gut environment (\(\\text{pH} > 9.0\)) to solubilize the crystal and specific cadherin/aminopeptidase receptors on gut cells. Mammalian stomachs are highly acidic (\(\\text{pH} < 2.0\)), which rapidly digests the protein into harmless amino acids, and mammals lack the specific receptor targets.

**Option Analysis:**
- **(A) Mammals possess acidic gastric juice that rapidly denatures and digests the protein, and lack the specific midgut epithelial receptors (Correct)** — Cry proteins behave as ordinary harmless dietary proteins in acidic mammalian stomachs.
- **(B) Human skin absorbing Bt toxins** — Incorrect; ingested food passes through the gastrointestinal tract, not skin absorption.
- **(C) Natural anti-Bt antibodies from birth** — Incorrect; humans do not possess innate preformed antibodies against specific bacterial Cry proteins.
- **(D) Conversion into pure glucose** — Incorrect; Cry toxins are polypeptides made of amino acids, not polysaccharides."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-011",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Biofertiliser definition",
        "text": "How are biofertilisers fundamentally distinguished from conventional chemical fertilizers like urea and diammonium phosphate (DAP)?",
        "options": [
            "Biofertilisers consist of living microbial cultures that naturally enrich soil nutrient availability through biological processes.",
            "Biofertilisers are synthetic petrochemical salts manufactured in chemical industrial factories.",
            "Biofertilisers contain radioactive isotopes that mutate crop DNA for rapid growth.",
            "Biofertilisers are acidic chemical solutions sprayed to strip away weeds."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Biofertilisers are formulations of living microorganisms (bacteria, fungi, cyanobacteria) that improve soil fertility and plant growth by fixing atmospheric nitrogen, solubilizing insoluble minerals, or stimulating root development without causing chemical pollution.

**Option Analysis:**
- **(A) Biofertilisers consist of living microbial cultures that naturally enrich soil nutrient availability through biological processes (Correct)** — The foundational definition of biofertilisers as eco-friendly biological inoculants.
- **(B) Synthetic petrochemical salts manufactured in factories** — Incorrect; describes chemical fertilizers synthesized by Haber-Bosch or rock acidulation processes.
- **(C) Radioactive isotopes mutating crop DNA** — Incorrect; completely fictitious and contrary to biological safety.
- **(D) Acidic chemical solutions to strip weeds** — Incorrect; describes chemical herbicides, not biological nutrient enhancers."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-012",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Biocontrol agent Trichoderma",
        "text": "Which free-living soil fungus is widely utilized in organic farming and biotechnology as a natural biological control agent against soil-borne plant pathogenic fungi?",
        "options": [
            "Trichoderma",
            "Rhizopus stolonifer",
            "Agaricus bisporus",
            "Puccinia graminis"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Trichoderma* species (e.g. *T. harzianum*, *T. viride*) are beneficial soil-dwelling filamentous fungi that protect crops by parasiting pathogenic fungi, secreting antifungal enzymes (chitinases and glucanases), and competing for rhizosphere niches.

**Option Analysis:**
- **(A) Trichoderma (Correct)** — The primary fungal biocontrol agent used globally for seed treatment and soil application against pathogens like *Fusarium* and *Rhizoctonia*.
- **(B) Rhizopus stolonifer** — Incorrect; black bread mold, a common spoilage saprophyte with no biocontrol utility.
- **(C) Agaricus bisporus** — Incorrect; the common edible white button mushroom cultivated for human food.
- **(D) Puccinia graminis** — Incorrect; a destructive plant parasite responsible for black stem rust of wheat."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-013",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Flavr Savr Tomato trait",
        "text": "The genetically modified 'Flavr Savr' tomato was engineered to possess which commercially advantageous agricultural trait?",
        "options": [
            "Delayed fruit softening and prolonged shelf-life due to suppression of polygalacturonase enzyme.",
            "Synthesis of heavy metal crystals in the fruit rind.",
            "Permanent blue coloration of tomato seeds.",
            "Ability to grow completely submerged underwater."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
The Flavr Savr tomato was engineered using antisense RNA technology to downregulate the enzyme polygalacturonase, which degrades pectin in cell walls during ripening, thereby significantly delaying softening and rotting during transit.

**Option Analysis:**
- **(A) Delayed fruit softening and prolonged shelf-life due to suppression of polygalacturonase enzyme (Correct)** — Slows pectin breakdown, allowing tomatoes to stay firm and vine-ripen longer without rapid post-harvest spoiling.
- **(B) Synthesis of heavy metal crystals** — Incorrect; would render the tomato toxic and inedible.
- **(C) Permanent blue coloration of seeds** — Incorrect; seed color was untouched by polygalacturonase antisense manipulation.
- **(D) Ability to grow completely submerged underwater** — Incorrect; tomato is an upland terrestrial crop that suffocates in waterlogged conditions."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-014",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Phosphate solubilizing bacteria",
        "text": "How do Phosphate Solubilizing Biofertilisers (PSB, e.g. Pseudomonas putida, Bacillus megaterium) convert insoluble soil phosphates into plant-absorbable forms?",
        "options": [
            "By secreting low molecular weight organic acids that chelate mineral cations and dissolve rock phosphates.",
            "By heating the soil to boiling temperatures via exothermic reactions.",
            "By capturing atmospheric nitrogen and converting it into phosphorus.",
            "By absorbing light energy and transforming it into phosphorus atoms."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Most soil phosphorus is locked up in insoluble complexes (tricalcium phosphate, aluminum/iron phosphates); phosphate-solubilizing bacteria secrete organic acids (citric, gluconic, oxalic acids) that lower soil pH and chelate bound cations, liberating soluble orthophosphate ions (\(\\ce{H2PO4^-}\)).

**Option Analysis:**
- **(A) By secreting low molecular weight organic acids that chelate mineral cations and dissolve rock phosphates (Correct)** — The established biochemical pathway of bacterial phosphate solubilization in agricultural soils.
- **(B) Heating the soil to boiling temperatures** — Incorrect; bacterial metabolism generates minuscule heat, incapable of boiling soil.
- **(C) Capturing nitrogen and converting it to phosphorus** — Incorrect; violates nuclear conservation of elements; biological enzymes cannot perform atomic transmutation.
- **(D) Transforming light energy into phosphorus atoms** — Incorrect; light energy cannot create matter out of radiation in biological systems."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-015",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Environmental impact of biofertilisers",
        "text": "What major environmental hazard associated with excessive synthetic chemical fertilizer use is effectively mitigated by adopting biofertilisers?",
        "options": [
            "Eutrophication and nitrate contamination of groundwater reservoirs.",
            "Depletion of ozone in the polar stratosphere by methane.",
            "Accelerated tectonic plate movement.",
            "Production of acid rain by bacterial nitrogenase."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Over-application of chemical nitrogen and phosphorus fertilizers leads to agricultural runoff, causing algal blooms and oxygen depletion (eutrophication) in aquatic ecosystems and dangerous nitrate leaching into drinking groundwater; biofertilisers release nutrients slowly and sustainably without runoff pollution.

**Option Analysis:**
- **(A) Eutrophication and nitrate contamination of groundwater reservoirs (Correct)** — Slow biological nutrient release prevents mineral surplus runoff, preserving aquatic and drinking water quality.
- **(B) Depletion of ozone in the polar stratosphere by methane** — Incorrect; ozone depletion is driven primarily by halogenated CFCs and halons, not nitrogen fertilizer runoff.
- **(C) Accelerated tectonic plate movement** — Incorrect; plate tectonics are driven by mantle convection currents, completely unrelated to soil inputs.
- **(D) Production of acid rain by bacterial nitrogenase** — Incorrect; acid rain is caused by industrial sulfur dioxide (\(\\ce{SO2}\)) and nitrogen oxides (\(\\ce{NO_x}\)), not biofertiliser enzymes."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-016",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Azospirillum association",
        "text": "Which associative symbiotic nitrogen-fixing bacterium colonizes the root surfaces of cereal crops such as maize, sorghum, and sugarcane?",
        "options": [
            "Azospirillum",
            "Mycobacterium tuberculosis",
            "Vibrio cholerae",
            "Salmonella typhi"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Azospirillum* forms an associative symbiotic relationship with the rhizosphere and root surfaces of non-leguminous grasses and cereals, fixing nitrogen and secreting plant-growth-promoting hormones like auxins and gibberellins.

**Option Analysis:**
- **(A) Azospirillum (Correct)** — The primary associative biofertiliser used for cereal crops, millets, and sugarcane.
- **(B) Mycobacterium tuberculosis** — Incorrect; a human pathogenic bacterium that causes tuberculosis in lungs and other tissues.
- **(C) Vibrio cholerae** — Incorrect; a water-borne enteric pathogen causing acute watery diarrhea (cholera).
- **(D) Salmonella typhi** — Incorrect; a dangerous food- and water-borne pathogen causing enteric typhoid fever."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-017",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Herbicide tolerant GM crops",
        "text": "What is the primary agricultural purpose of engineering herbicide-tolerant (HT) crops (e.g. glyphosate-tolerant soybeans and cotton)?",
        "options": [
            "To allow farmers to spray broad-spectrum herbicides to eliminate competing weeds without damaging the crop plants.",
            "To make the crop produce its own chemical weedkiller that sterilizes all surrounding soil permanently.",
            "To turn weeds into edible fruit-bearing branches.",
            "To stop crops from requiring any sunlight for vegetative growth."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Herbicide-tolerant crops express an insensitive bacterial version of the target enzyme (e.g. 5-enolpyruvylshikimate-3-phosphate synthase, EPSPS), allowing fields to be sprayed with non-selective herbicides to kill weeds cleanly while leaving the crop unharmed.

**Option Analysis:**
- **(A) To allow farmers to spray broad-spectrum herbicides to eliminate competing weeds without damaging the crop plants (Correct)** — Enables post-emergence weed management with reduced manual labor and minimal crop injury.
- **(B) Making crop produce weedkiller sterilizing surrounding soil permanently** — Incorrect; HT crops tolerate external herbicides rather than permanently poisoning the soil.
- **(C) Turning weeds into edible fruit branches** — Incorrect; genetic modification of the crop does not transform the genome or morphology of surrounding weeds.
- **(D) Stopping crops from requiring sunlight** — Incorrect; all crop plants remain obligate photosynthetic organisms dependent on solar radiation."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-018",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Bio-pesticide Baculovirus",
        "text": "Baculoviruses (such as Nuclear Polyhedrosis Virus - NPV) are preferred as biological pesticides in integrated pest management because they:",
        "options": [
            "Exhibit narrow-spectrum species-specific action, having zero pathogenic impact on non-target beneficial insects, birds, or mammals.",
            "Eradicate every single insect, worm, and microbe living within a 10-mile radius.",
            "Permanently acidify soil water to dissolve insect exoskeletons on contact.",
            "Convert harmful caterpillar larvae into photosynthetic honeybees."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Baculoviruses belonging to the genus *Nucleopolyhedrovirus* are narrow-spectrum pathogen agents that selectively infect specific insect pests (mainly caterpillars of *Helicoverpa* and *Spodoptera*) without collateral toxicity to pollinating bees, predatory ladybird beetles, or vertebrate wildlife.

**Option Analysis:**
- **(A) Exhibit narrow-spectrum species-specific action, having zero pathogenic impact on non-target beneficial insects, birds, or mammals (Correct)** — The ideal characteristic of biocontrol viruses in conserving ecological biodiversity.
- **(B) Eradicate every single organism within 10-mile radius** — Incorrect; broad-spectrum total annihilation is characteristic of dangerous chemical weapons, not specific viral biocontrols.
- **(C) Permanently acidify soil water** — Incorrect; viral occlusion bodies do not alter soil chemistry or water pH.
- **(D) Convert caterpillars into honeybees** — Incorrect; biological metamorphosis cannot transform an insect from one order (Lepidoptera) to another (Hymenoptera)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-019",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Transgenic plant definition",
        "text": "A plant whose genome has been stably modified through the artificial introduction of one or more foreign genes from another species is termed a:",
        "options": [
            "Transgenic (Genetically Modified) plant",
            "Hydroponic plant",
            "Saprophytic plant",
            "Cryptogamic plant"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
A transgenic or Genetically Modified (GM) organism possesses one or more foreign genes (transgenes) introduced across taxonomic boundaries using recombinant DNA technology.

**Option Analysis:**
- **(A) Transgenic (Genetically Modified) plant (Correct)** — The precise botanical and scientific term for an organism carrying stable heterologous transgenes.
- **(B) Hydroponic plant** — Incorrect; refers to plants cultivated in soilless nutrient-enriched water solutions.
- **(C) Saprophytic plant** — Incorrect; non-photosynthetic organisms that derive nutrients directly from decaying organic matter.
- **(D) Cryptogamic plant** — Incorrect; classical taxonomic group of non-seed-bearing plants (thallophytes, bryophytes, pteridophytes)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-020",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Vector in plant genetic engineering",
        "text": "Which bacterium is commonly known as 'nature's genetic engineer' because its Ti-plasmid naturally transfers a segment of DNA (T-DNA) into the plant host genome?",
        "options": [
            "Agrobacterium tumefaciens",
            "Lactobacillus bulgaricus",
            "Staphylococcus aureus",
            "Streptococcus pneumoniae"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Agrobacterium tumefaciens* is a soil-dwelling phytopathogen harboring the tumor-inducing (Ti) plasmid; molecular biologists disarm this plasmid by removing disease-causing genes and replacing them with genes of interest to transform plant cells efficiently.

**Option Analysis:**
- **(A) Agrobacterium tumefaciens (Correct)** — The universal natural biological vector utilized for introducing foreign transgenes into dicotyledonous plant genomes.
- **(B) Lactobacillus bulgaricus** — Incorrect; a probiotic bacterium used in fermented yogurt production.
- **(C) Staphylococcus aureus** — Incorrect; a Gram-positive pathogenic bacterium causing skin, wound, and bloodstream infections in animals.
- **(D) Streptococcus pneumoniae** — Incorrect; an encapsulated human pathogen responsible for bacterial pneumonia."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-021",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Azolla-Anabaena association",
        "text": "The aquatic water fern Azolla is widely grown as a green manure in wetland rice paddies because its leaf cavities house which nitrogen-fixing endosymbiont?",
        "options": [
            "Anabaena azollae",
            "Spirulina maxima",
            "Chlorella vulgaris",
            "Euglena viridis"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
The floating freshwater fern *Azolla* maintains an obligate mutualistic association with the filamentous cyanobacterium *Anabaena azollae* inside dorsal leaf cavities, fixing up to 50–100 kg of atmospheric nitrogen per hectare per year.

**Option Analysis:**
- **(A) Anabaena azollae (Correct)** — The symbiotic nitrogen-fixing cyanobacterium living inside *Azolla* leaf pores, providing abundant biological nitrogen to paddy fields.
- **(B) Spirulina maxima** — Incorrect; a free-living, spiral-shaped cyanobacterium cultivated commercially as a single-cell protein nutritional supplement.
- **(C) Chlorella vulgaris** — Incorrect; a unicellular green alga used in oxygen generation and food supplements, unable to fix nitrogen.
- **(D) Euglena viridis** — Incorrect; a flagellated, mixotrophic eukaryotic protist found in stagnant freshwater."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-022",
        "type": "OSC",
        "bloomLevel": "Analyze",
        "difficulty": "hard",
        "conceptTag": "Insect resistance management in Bt crops",
        "text": "Why do agricultural guidelines mandate that farmers plant a mandatory 'refuge' border of non-Bt cotton around fields of Bt cotton?",
        "options": [
            "To delay the evolution of genetic resistance in bollworm populations by maintaining a pool of susceptible homozygous wild-type moths.",
            "To provide shade to keep the Bt cotton roots cool during hot afternoons.",
            "To confuse bollworms into flying toward neighboring towns.",
            "Because non-Bt cotton seeds absorb all excessive rainfall."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
The refuge strategy requires planting a border of susceptible non-Bt plants to sustain a population of bollworms that do not experience selection pressure; when rare resistant moths emerging from Bt fields mate with these susceptible wild-type moths, their heterozygous offspring remain susceptible to Bt toxins, preventing pest resistance.

**Option Analysis:**
- **(A) To delay the evolution of genetic resistance in bollworm populations by maintaining a pool of susceptible homozygous wild-type moths (Correct)** — Essential resistance management protocol slowing the selection of recessive resistance alleles in target pest populations.
- **(B) Providing shade to keep roots cool** — Incorrect; refuge crops are identical height plants spaced at the field periphery, offering no significant shade to central crops.
- **(C) Confusing bollworms into flying away** — Incorrect; insects disperse according to wind and pheromone plumes, not visual confusion.
- **(D) Absorbing excessive rainfall** — Incorrect; non-Bt and Bt cotton have identical transpiration and root absorption physiology."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-023",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Bio-herbicide examples",
        "text": "What term describes a formulation composed of specific fungal spores or bacterial agents used selectively to suppress or destroy target weed species without harming cash crops?",
        "options": [
            "Bio-herbicide (Myco-herbicide)",
            "Synthetic defoliant",
            "Petrochemical fumigant",
            "Inorganic fungicide"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
A bio-herbicide (often a myco-herbicide based on fungal pathogens like *Colletotrichum* or *Phytophthora*) utilizes living biological pathogens to induce selective disease and mortality in target weed populations without contaminating soil with synthetic chemical residues.

**Option Analysis:**
- **(A) Bio-herbicide (Myco-herbicide) (Correct)** — The specific biological pest control category that suppresses unwanted weeds via living micro-pathogens.
- **(B) Synthetic defoliant** — Incorrect; chemically synthesized chemical compounds that cause premature leaf drop (e.g. Agent Orange components).
- **(C) Petrochemical fumigant** — Incorrect; volatile synthetic gases (e.g. methyl bromide) used to sterilize soil of all biological life.
- **(D) Inorganic fungicide** — Incorrect; mineral salts (e.g. copper sulfate / Bordeaux mixture) formulated to kill fungi, not weeds."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-024",
        "type": "OSC",
        "bloomLevel": "Remember",
        "difficulty": "easy",
        "conceptTag": "Genes introduced into Golden Rice",
        "text": "Which two donor organisms provided the key enzymatic genes (phytoene synthase and carotene desaturase) integrated into Golden Rice to reconstitute the beta-carotene pathway?",
        "options": [
            "Daffodil (Narcissus pseudonarcissus) and the soil bacterium Erwinia uredovora",
            "Sugarcane and Baker's yeast",
            "Pine tree and Escherichia coli",
            "Mushroom and Silkworm"
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Ingo Potrykus and Peter Beyer engineered Golden Rice by introducing the *psy* gene (phytoene synthase) from daffodil (*Narcissus pseudonarcissus*) and the *crtI* gene (carotene desaturase) from the soil bacterium *Erwinia uredovora* under the control of an endosperm-specific promoter.

**Option Analysis:**
- **(A) Daffodil (Narcissus pseudonarcissus) and the soil bacterium Erwinia uredovora (Correct)** — The landmark historic donor organisms whose cDNA reconstructed the active provitamin A pathway in rice grain endosperm.
- **(B) Sugarcane and Baker's yeast** — Incorrect; sugarcane produces sucrose and yeast lacks the complete plant carotenoid pathway.
- **(C) Pine tree and Escherichia coli** — Incorrect; non-relevant organisms not employed in the pioneer construction of Golden Rice.
- **(D) Mushroom and Silkworm** — Incorrect; silkworms are sericultural insects and mushrooms are non-photosynthetic fungi."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-025",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Biofertiliser carrier material",
        "text": "What is the primary role of sterile carrier materials like peat, lignite, or charcoal powder in the commercial manufacturing of biofertiliser packets?",
        "options": [
            "To provide a moist, protective, non-toxic physical matrix that keeps the inoculated microorganisms viable until field application.",
            "To act as a high-temperature fuel that burns weeds when sprinkled onto soil.",
            "To permanently color the soil black so it absorbs maximum lunar radiation.",
            "To crystallize the bacteria into non-living mineral stones."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Carrier materials provide physical support, moisture retention, buffering capacity, and trace carbon to sustain high counts of viable living cells (minimum \(10^7\) to \(10^8\) CFU/gram) during transport and shelf storage.

**Option Analysis:**
- **(A) To provide a moist, protective, non-toxic physical matrix that keeps the inoculated microorganisms viable until field application (Correct)** — The standard industrial purpose of neutral, finely pulverized organic carriers in biofertiliser production.
- **(B) Acting as a high-temperature fuel to burn weeds** — Incorrect; biofertilisers are applied at ambient temperatures and do not combust.
- **(C) Coloring soil to absorb lunar radiation** — Incorrect; lunar light plays negligible role in soil warmth, and carriers are mixed locally into root zones.
- **(D) Crystallizing bacteria into non-living stones** — Incorrect; dead or crystallized bacteria cannot fix nitrogen or colonize plant roots."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OSC-026",
        "type": "OSC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Biopesticide advantages",
        "text": "Which of the following is a major ecological advantage of employing biopesticides over persistent synthetic organochlorine pesticides (e.g. DDT)?",
        "options": [
            "Biopesticides are biodegradable, leave no toxic residue in the food chain, and do not cause biomagnification in top predators.",
            "Biopesticides permanently poison all soil water for 500 years.",
            "Biopesticides kill all aquatic fish in nearby rivers instantly.",
            "Biopesticides prevent plants from absorbing any water from soil."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Unlike persistent chemical pesticides that bioaccumulate across trophic levels, biopesticides are composed of natural living pathogens or biodegradable compounds that break down rapidly in sunlight and soil without biomagnifying in wildlife or humans.

**Option Analysis:**
- **(A) Biopesticides are biodegradable, leave no toxic residue in the food chain, and do not cause biomagnification in top predators (Correct)** — Major environmental and food-safety rationale for adopting biological pest control.
- **(B) Permanently poisoning soil water for 500 years** — Incorrect; describes persistent chemical pollution, the exact problem biopesticides avoid.
- **(C) Killing all aquatic fish instantly** — Incorrect; biopesticides are selected for their safety toward aquatic vertebrates.
- **(D) Preventing plants from absorbing water** — Incorrect; biopesticides protect crops from pathogens without impeding plant vascular transport."""
    },

    # --- 6 OTF Questions ---
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-001",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Cry protoxin harmlessness in plant",
        "text": "Cry proteins produced inside the cells of Bt cotton plants are harmless to the plant itself because they exist as inactive, insoluble protoxins that require an insect's alkaline digestive environment to activate.",
        "options": ["False", "True"],
        "correctAnswer": "True",
        "solution": """**Key Concept:**
The Cry endotoxin is synthesized by plants in an inert, crystalline protoxin conformation; it remains completely non-toxic to plant cells and is activated only upon enzymatic solubilization at the alkaline \(\\text{pH}\) (\(> 9.0\)) typical of lepidopteran insect midguts.

**Statement Evaluation:**
- **Statement: \"True\" (Correct)** — Inactive protoxin crystals cannot harm plant tissues; their destructive pore-forming conformation is triggered exclusively by insect alkaline gut proteases.
- **Statement: \"False\"** — Incorrect; botanical physiology confirms that Bt plants grow vigorously without any self-toxicity from endogenous Cry protein synthesis."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-002",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Golden Rice provitamin identity",
        "text": "Golden Rice contains fully formed animal Vitamin A (retinol) directly synthesized by the transgenic rice plants.",
        "options": ["False", "True"],
        "correctAnswer": "False",
        "solution": """**Key Concept:**
Plants cannot synthesize preformed Vitamin A (retinol), which is exclusive to animal tissues; instead, Golden Rice synthesizes \(\\beta\)-carotene, a provitamin carotenoid that the human body cleaves enzymatically in the intestinal mucosa into two molecules of active retinol.

**Statement Evaluation:**
- **Statement: \"False\" (Correct)** — Golden Rice produces \(\\beta\)-carotene (provitamin A), not retinol (pure Vitamin A); human intestinal enzymes convert \(\\beta\)-carotene into Vitamin A after ingestion.
- **Statement: \"True\"** — Incorrect; plants never synthesize animal retinol directly."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-003",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Biofertiliser renewable nature",
        "text": "Biofertilisers are renewable, environmentally sustainable biological agents that help replenish soil organic carbon and microflora while reducing chemical reliance.",
        "options": ["False", "True"],
        "correctAnswer": "True",
        "solution": """**Key Concept:**
Because biofertilisers utilize living microbial cultures capable of self-multiplication and organic nutrient cycling, they represent a renewable, carbon-neutral, and ecologically restorative alternative to energy-intensive synthetic fertilizers.

**Statement Evaluation:**
- **Statement: \"True\" (Correct)** — Microorganisms in biofertilisers proliferate in the rhizosphere, improving soil structure, water retention, and microbial biodiversity over successive seasons.
- **Statement: \"False\"** — Incorrect; agricultural ecology establishes biofertilisers as a core component of sustainable, non-polluting farming."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-004",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "easy",
        "conceptTag": "Rhizobium host specificity",
        "text": "Any species of Rhizobium can naturally form root nodules and fix nitrogen equally well on all crops, including wheat, maize, and sugarcane.",
        "options": ["True", "False"],
        "correctAnswer": "False",
        "solution": """**Key Concept:**
*Rhizobium* displays strict host-symbiont specificity mediated by reciprocal molecular recognition (flavonoids secreted by the legume root binding to bacterial NodD proteins to trigger Nod factor production); non-leguminous cereals like wheat and maize lack this symbiotic machinery.

**Statement Evaluation:**
- **Statement: \"False\" (Correct)** — *Rhizobium* nodulates exclusively leguminous host plants (family Fabaceae); it cannot form symbiotic nodules or fix nitrogen in monocotyledonous cereals like wheat or maize.
- **Statement: \"True\"** — Incorrect; cereals do not form root nodules with *Rhizobium* (they benefit from free-living or associative fixers like *Azotobacter* and *Azospirillum*)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-005",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Azolla dual benefit",
        "text": "When incorporated into flooded rice paddy soils, the water fern Azolla acts both as a rapid biological nitrogen supplier and as a green manure that suppresses weed emergence.",
        "options": ["False", "True"],
        "correctAnswer": "True",
        "solution": """**Key Concept:**
Floating mats of *Azolla* form a dense surface canopy over flooded paddy water, physically blocking sunlight to prevent weed seeds from germinating while fixing up to 1 kg of nitrogen per hectare daily through its cyanobacterial symbiont *Anabaena azollae*.

**Statement Evaluation:**
- **Statement: \"True\" (Correct)** — *Azolla* provides dual ecological benefits: intense nitrogen enrichment upon incorporation and vegetative weed suppression during early rice growth.
- **Statement: \"False\"** — Incorrect; agronomic trials confirm *Azolla*'s dual action as a potent green manure and weed-suppressing cover in wetland paddies."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OTF-006",
        "type": "OTF",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Bio-control pathogen persistence",
        "text": "Biopesticides leave toxic non-biodegradable synthetic chemical residues on fresh market vegetables that must be detoxified by industrial washing.",
        "options": ["True", "False"],
        "correctAnswer": "False",
        "solution": """**Key Concept:**
Biopesticides are composed of naturally occurring microorganisms or organic biological metabolites that decompose rapidly under ambient solar UV radiation and atmospheric weathering, leaving zero synthetic residues on harvested food crops.

**Statement Evaluation:**
- **Statement: \"False\" (Correct)** — Unlike synthetic chemicals, biopesticides possess short environmental half-lives and leave zero harmful synthetic residues, requiring zero post-harvest chemical decontamination.
- **Statement: \"True\"** — Incorrect; the total absence of toxic synthetic chemical residues is the hallmark advantage of biopesticides."""
    },

    # --- 4 OAR Questions ---
    {
        "questionCode": "MH-9-SCIT-17-17.2-OAR-001",
        "type": "OAR",
        "bloomLevel": "Analyze",
        "difficulty": "hard",
        "conceptTag": "Bt Cotton selectivity mechanism",
        "text": "Assertion (A): Bt cotton crops are toxic to caterpillar pests like bollworms but completely harmless to human beings and grazing cattle.\\nReason (R): The Cry protoxin requires an alkaline pH above 9.0 to solubilize and specific epithelial receptor proteins to bind, both of which are present in bollworm midguts but absent in the mammalian gastrointestinal tract.",
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
The high selectivity of Cry toxins stems from the unique physiological conditions of the target insect midgut (high alkaline \(\\text{pH}\) and cadherin receptors), whereas mammalian stomachs are strongly acidic (\(\\text{pH} < 2.0\)) and lack compatible binding sites.

**Assertion & Reason Analysis:**
- **Assertion (A):** True — Ingesting Bt cotton foliage or seed oil produces no pathological symptoms in mammals or humans while exterminating bollworms.
- **Reason (R):** True — The biochemical prerequisites for Cry toxin activation (alkaline dissolution, specific protease processing, and midgut receptor binding) exist exclusively in target insect orders and are completely absent in mammalian digestive systems.
- **Conclusion (A) (Correct)** — Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OAR-002",
        "type": "OAR",
        "bloomLevel": "Analyze",
        "difficulty": "medium",
        "conceptTag": "Golden Rice night blindness prevention",
        "text": "Assertion (A): Cultivating and consuming Golden Rice can significantly alleviate childhood night blindness (xerophthalmia) in developing nations.\\nReason (R): Golden Rice grains synthesize high levels of beta-carotene, which is biochemically converted into Vitamin A by the human body after consumption.",
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
Vitamin A deficiency is the leading cause of preventable childhood blindness worldwide; Golden Rice biofortifies staple rice grains with provitamin A (\(\\beta\)-carotene), providing an accessible dietary source that directly treats hypovitaminosis A.

**Assertion & Reason Analysis:**
- **Assertion (A):** True — Clinical nutrition studies confirm that consuming modest daily portions of Golden Rice delivers adequate Vitamin A to prevent ocular pathology like night blindness.
- **Reason (R):** True — Endosperm-specific expression of carotenoid enzymes produces \(\\beta\)-carotene, which human intestinal enzymes convert directly into retinal and retinol (active Vitamin A).
- **Conclusion (A) (Correct)** — Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OAR-003",
        "type": "OAR",
        "bloomLevel": "Analyze",
        "difficulty": "hard",
        "conceptTag": "Chemical fertilizer vs biofertiliser sustainability",
        "text": "Assertion (A): Continuous and excessive reliance on chemical nitrogenous fertilizers eventually leads to the degradation of agricultural soil fertility and environmental pollution.\\nReason (R): Chemical fertilizers do not replenish soil organic carbon, alter soil pH, inhibit beneficial native microbial activity, and easily wash into water bodies causing eutrophication.",
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
While synthetic mineral fertilizers provide rapid nutrient pulses, their chronic long-term overuse destroys soil humic structure, acidifies the pedosphere, suppresses earthworms and beneficial bacteria, and leads to destructive water eutrophication.

**Assertion & Reason Analysis:**
- **Assertion (A):** True — Over-application of chemical salts exhausts natural soil regenerative capacity, causing compaction, salinization, and loss of native fertility.
- **Reason (R):** True — Inorganic fertilizers lack organic matter, destroy microbial micro-ecosystems, and leach rapidly into aquatic reservoirs where they trigger toxic algal blooms and hypoxia.
- **Conclusion (A) (Correct)** — Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OAR-004",
        "type": "OAR",
        "bloomLevel": "Analyze",
        "difficulty": "medium",
        "conceptTag": "Trichoderma biocontrol mechanism",
        "text": "Assertion (A): Farmers apply preparations of the fungus Trichoderma to seeds and seedling roots to safeguard crops against soil-borne wilt and root rot diseases.\\nReason (R): Trichoderma acts as an aggressive mycoparasite that wraps around pathogenic fungal hyphae, dissolves their cell walls with chitinase enzymes, and colonizes root surfaces.",
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": "A",
        "solution": """**Key Concept:**
*Trichoderma* functions as an effective biological fungicide through multiple coordinated modes of action: direct mycoparasitism, secretion of cell-wall lytic enzymes (chitinases, \(\\beta\)-1,3-glucanases), and competitive exclusion of plant pathogens in the rhizosphere.

**Assertion & Reason Analysis:**
- **Assertion (A):** True — Treating seeds with *Trichoderma* formulations drastically reduces seedling mortality caused by damping-off and root-rot pathogens.
- **Reason (R):** True — *Trichoderma* coils around the hyphae of harmful fungi like *Rhizoctonia* and *Pythium*, digesting their structural chitin walls and establishing a protective shield over plant root surfaces.
- **Conclusion (A) (Correct)** — Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."""
    },

    # --- 4 OMC Questions ---
    {
        "questionCode": "MH-9-SCIT-17-17.2-OMC-001",
        "type": "OMC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Microorganisms used as biofertilisers",
        "text": "Which of the following organisms are commercially formulated and utilized in agriculture as biofertilisers?",
        "options": [
            "Rhizobium",
            "Azotobacter",
            "Anabaena azollae",
            "Plasmodium vivax"
        ],
        "correctAnswer": "A, B, C",
        "correctAnswers": [
            "Rhizobium",
            "Azotobacter",
            "Anabaena azollae"
        ],
        "solution": """**Key Concept:**
Biofertilisers comprise beneficial microorganisms—including symbiotic bacteria (*Rhizobium*), free-living nitrogen fixers (*Azotobacter*), and cyanobacteria (*Anabaena*)—that enhance soil nutrient availability through biological fixation.

**Option Analysis:**
- **(A) Rhizobium (Correct)** — Symbiotic nitrogen fixer widely applied to pulse and legume seeds before planting.
- **(B) Azotobacter (Correct)** — Free-living aerobic nitrogen-fixing bacterium applied to cereals, vegetables, and cash crops.
- **(C) Anabaena azollae (Correct)** — Symbiotic cyanobacterium used in wetland rice cultivation for biological nitrogen enrichment.
- **(D) Plasmodium vivax** — Incorrect; a protozoan parasite that causes malaria in humans, completely devoid of agricultural utility."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OMC-002",
        "type": "OMC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Desirable traits in GM crops",
        "text": "Which of the following traits have been successfully engineered into commercial genetically modified (GM) crops using modern biotechnology?",
        "options": [
            "Pest resistance against boring insect caterpillars (e.g. Bt endotoxin)",
            "Nutritional enhancement with vitamin precursors (e.g. beta-carotene in Golden Rice)",
            "Tolerance to broad-spectrum chemical herbicides",
            "Ability of crop plants to spontaneously generate electricity to power farm tractors"
        ],
        "correctAnswer": "A, B, C",
        "correctAnswers": [
            "Pest resistance against boring insect caterpillars (e.g. Bt endotoxin)",
            "Nutritional enhancement with vitamin precursors (e.g. beta-carotene in Golden Rice)",
            "Tolerance to broad-spectrum chemical herbicides"
        ],
        "solution": """**Key Concept:**
Commercial transgenic crops are engineered for proven agronomic and nutritional enhancements: insect resistance (Bt crops), provitamin biofortification (Golden Rice), herbicide tolerance (HT soybeans/cotton), and extended post-harvest shelf-life.

**Option Analysis:**
- **(A) Pest resistance against boring insect caterpillars (Correct)** — Engineered via *Bacillus thuringiensis* Cry endotoxins in cotton, corn, and brinjal.
- **(B) Nutritional enhancement with vitamin precursors (Correct)** — Engineered in Golden Rice to deliver provitamin A (\(\\beta\)-carotene) to deficient populations.
- **(C) Tolerance to broad-spectrum chemical herbicides (Correct)** — Engineered in glyphosate- and glufosinate-tolerant crops to streamline weed management.
- **(D) Ability to spontaneously generate electricity to power farm tractors** — Incorrect; biologically impossible and pure science fiction."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OMC-003",
        "type": "OMC",
        "bloomLevel": "Analyze",
        "difficulty": "hard",
        "conceptTag": "Ecological advantages of biofertilisers over chemical fertilizers",
        "text": "Which of the following represent verified ecological and agricultural advantages of adopting biofertilisers over exclusive chemical fertilization?",
        "options": [
            "Biofertilisers improve soil biological activity and physical crumb structure over time.",
            "Biofertilisers do not cause groundwater nitrate leaching or aquatic eutrophication.",
            "Biofertilisers reduce greenhouse gas emissions associated with industrial chemical fertilizer manufacturing.",
            "Biofertilisers completely eradicate all native soil earthworms and fungi within 24 hours."
        ],
        "correctAnswer": "A, B, C",
        "correctAnswers": [
            "Biofertilisers improve soil biological activity and physical crumb structure over time.",
            "Biofertilisers do not cause groundwater nitrate leaching or aquatic eutrophication.",
            "Biofertilisers reduce greenhouse gas emissions associated with industrial chemical fertilizer manufacturing."
        ],
        "solution": """**Key Concept:**
Biofertilisers provide multiple long-term ecological benefits: rebuilding the soil food web, eliminating hazardous chemical runoff into waterways, and replacing fossil-fuel-intensive industrial fertilizer production with renewable biological processes.

**Option Analysis:**
- **(A) Biofertilisers improve soil biological activity and physical crumb structure over time (Correct)** — Secretion of microbial polysaccharides, mucilage, and organic acids enhances soil aggregation and water retention.
- **(B) Biofertilisers do not cause groundwater nitrate leaching or aquatic eutrophication (Correct)** — Nutrients are released slowly and absorbed directly by plant roots without surplus chemical runoff.
- **(C) Biofertilisers reduce greenhouse gas emissions associated with industrial manufacturing (Correct)** — Displacing energy-heavy Haber-Bosch chemical ammonia synthesis significantly cuts industrial carbon footprints.
- **(D) Eradicating all native soil earthworms and fungi** — Incorrect; biofertilisers actively support earthworms and beneficial mycorrhizae, never harming them."""
    },
    {
        "questionCode": "MH-9-SCIT-17-17.2-OMC-004",
        "type": "OMC",
        "bloomLevel": "Understand",
        "difficulty": "medium",
        "conceptTag": "Biopesticides and biocontrol organisms",
        "text": "Which of the following biological agents are deployed in organic and integrated pest management systems as biopesticides or biocontrol organisms?",
        "options": [
            "Bacillus thuringiensis (bacterial spray)",
            "Trichoderma viride (fungal antagonist)",
            "Nuclear Polyhedrosis Virus - NPV (viral pathogen of caterpillars)",
            "Sulfuric acid and copper arsenic dust"
        ],
        "correctAnswer": "A, B, C",
        "correctAnswers": [
            "Bacillus thuringiensis (bacterial spray)",
            "Trichoderma viride (fungal antagonist)",
            "Nuclear Polyhedrosis Virus - NPV (viral pathogen of caterpillars)"
        ],
        "solution": """**Key Concept:**
Biological pest control relies on living organisms or their natural derivatives—including bacterial formulations (*Bt*), fungal bio-fungicides (*Trichoderma*), and species-specific baculoviruses (*NPV*)—to suppress pest and pathogen populations naturally.

**Option Analysis:**
- **(A) Bacillus thuringiensis (Correct)** — Formulated as biological sprays containing bacterial spores and Cry endotoxin crystals against pest caterpillars.
- **(B) Trichoderma viride (Correct)** — Widely formulated bio-fungicide that combats root-rotting and damping-off plant fungi.
- **(C) Nuclear Polyhedrosis Virus - NPV (Correct)** — Baculovirus deployed for targeted control of specific lepidopteran pests like *Helicoverpa armigera*.
- **(D) Sulfuric acid and copper arsenic dust** — Incorrect; hazardous inorganic chemical poisons that devastate soils and poison ecosystems."""
    }
]

print(f"Authored {len(topic2_questions)} gold-standard questions for Topic 17.2.")
