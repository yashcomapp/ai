# scripts/generate_ch17_topic2.py
# MH-9-SCIT-17-17.2: Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-17-17.2"

exam_data = [
    # 1-10: GM Crops Basics & Bt Cotton
    ("What are crops whose genome has been modified by introducing foreign genes from other species using recombinant DNA technology called?",
     ["Genetically Modified (GM) Crops (Transgenic crops)", "Hybrid crops", "Organic crops", "Wild varieties"],
     "A", "OSC", "easy",
     "Genetically Modified (GM) crops carry stably integrated foreign genes (transgenes) introduced via molecular biotechnology to confer specific agronomic traits."),

    ("Which soil bacterium is the natural source of the insecticidal 'cry' genes incorporated into pest-resistant transgenic crops such as Bt cotton?",
     ["Bacillus thuringiensis", "Escherichia coli", "Rhizobium leguminosarum", "Agrobacterium tumefaciens"],
     "A", "OSC", "easy",
     "Bacillus thuringiensis (Bt) is a Gram-positive spore-forming soil bacterium that synthesizes parasporal crystalline delta-endotoxin proteins toxic to insect pests."),

    ("Which devastating insect pest of cotton crops is specifically targeted and controlled by Bt cotton expressing cry1Ac and cry2Ab proteins?",
     ["Cotton Bollworm (Helicoverpa armigera / Pectinophora gossypiella)", "Aphids", "Termites", "Locusts"],
     "A", "OSC", "easy",
     "Bt cotton produces Cry endotoxins that target lepidopteran cotton bollworms, which chew into developing cotton bolls and ruin lint quality."),

    ("Why is the crystalline Bt endotoxin completely NON-TOXIC to the bacterium itself and to human beings who consume plant products?",
     ["It is produced as an inactive protoxin that requires the specific ALKALINE pH (pH > 9) of insect midguts to become activated, whereas human stomachs are acidic (pH 1.5-2)",
      "Humans possess an immune shield against all bacteria",
      "The toxin evaporates when touched by humans",
      "Bt protein turns into sugar in human blood"],
     "A", "OSC", "medium",
     "Bt crystal proteins exist as inert protoxins; only the high alkaline pH of lepidopteran insect midguts solubilizes and proteolytically cleaves them into active lethal toxins."),

    ("What molecular cellular mechanism causes the death of a cotton bollworm larva after it ingests Bt cotton leaf tissue?",
     ["Activated Cry toxin binds to cadherin receptors on midgut epithelial cells, creating perforating pores that cause cell swelling, lysis, and fatal gut paralysis",
      "The toxin freezes the insect's heart instantly",
      "The insect's wings fall off immediately",
      "The insect turns into a butterfly prematurely"],
     "A", "OSC", "hard",
     "Activated Cry toxins oligomerize and insert into the brush border membrane of midgut epithelial cells, forming lytic pores that disrupt osmotic equilibrium, causing starvation and septic death."),

    ("What is the primary agricultural and environmental benefit of widespread cultivation of Bt cotton for farmers?",
     ["Drastic reduction in the need for hazardous chemical pesticide spraying and significantly higher harvest yields of unblemished cotton",
      "Cotton plants produce colored silk instead of cotton",
      "Plants grow without needing any water",
      "Cotton bolls pick themselves automatically"],
     "A", "OSC", "easy",
     "Bt cotton provides endogenous pest resistance, slashing toxic synthetic insecticide applications by 70-80% and preventing catastrophic bollworm crop losses."),

    ("What is 'Golden Rice', a groundbreaking genetically biofortified transgenic crop developed by Ingo Potrykus and Peter Beyer?",
     ["Genetically engineered rice enriched with beta-carotene (provitamin A) to combat childhood blindness and Vitamin A deficiency (VAD)",
      "Rice coated with pure metallic gold powder",
      "Rice that grows in salt water",
      "Rice with double the amount of caffeine"],
     "A", "OSC", "easy",
     "Golden Rice was engineered by introducing phytoene synthase (psy) and carotene desaturase (crtI) genes to synthesize beta-carotene in the edible endosperm."),

    ("In which organ in the human body is beta-carotene synthesized by Golden Rice biochemically converted into active Vitamin A (retinol)?",
     ["Small intestinal mucosa and Liver", "Lungs", "Kidneys", "Pancreas"],
     "A", "OSC", "medium",
     "Dietary beta-carotene is enzymatically cleaved by beta-carotene 15,15'-monooxygenase in the enterocytes of the small intestine and stored as retinol in the liver."),

    ("Which plant pathogen bacterium is celebrated as 'Nature's Genetic Engineer' because its Ti-plasmid naturally transfers T-DNA into plant host genomes?",
     ["Agrobacterium tumefaciens", "Bacillus thuringiensis", "Pseudomonas putida", "Rhizobium leguminosarum"],
     "A", "OSC", "easy",
     "Agrobacterium tumefaciens harbors a Tumor-inducing (Ti) plasmid; molecular biologists disarm its oncogenes to use its T-DNA as a primary vehicle for introducing transgenes into dicot plants."),

    ("What was the commercial innovation behind the famous 'Flavr Savr' transgenic tomato developed in 1994?",
     ["Antisense RNA technology blocked polygalacturonase enzyme synthesis, delaying cell-wall pectin breakdown and prolonging shelf-life without rotting",
      "It tasted like chocolate",
      "It grew without seeds",
      "It had blue skin to resist insects"],
     "A", "OSC", "medium",
     "Flavr Savr tomatoes utilized antisense RNA to suppress the polygalacturonase gene, preventing softening of the fruit pericarp and allowing extended vine ripening and shipping."),

    # 11-20: Biofertilisers & Nitrogen Fixation
    ("What are biofertilisers in modern sustainable agricultural biotechnology?",
     ["Living microbial inoculants containing bacteria, fungi, or algae that enrich soil nutrient availability by fixing nitrogen or solubilizing phosphorus",
      "Chemical synthetic urea pellets",
      "Powdered dry leaves",
      "Insecticide sprays"],
     "A", "OSC", "easy",
     "Biofertilisers are biologically active preparations containing beneficial microorganisms that enhance nutrient uptake via natural nitrogen fixation, phosphate solubilization, or mycorrhizal symbiosis."),

    ("Which symbiotic nitrogen-fixing bacterium infects the root hairs of leguminous plants (such as gram, peas, and groundnut) to form specialized root nodules?",
     ["Rhizobium leguminosarum", "Azotobacter chroococcum", "Clostridium pasteurianum", "Bacillus subtilis"],
     "A", "OSC", "easy",
     "Rhizobium enters root hairs via infection threads, transforming into bacteroids within root cortical nodules to reduce atmospheric N2 into ammonia ($NH_3$)."),

    ("What is the unique oxygen-scavenging pink pigment found inside active, nitrogen-fixing Rhizobium legume root nodules?",
     ["Leghemoglobin", "Hemoglobin", "Myoglobin", "Chlorophyll"],
     "A", "OSC", "easy",
     "Leghemoglobin is an iron-heme protein produced cooperatively by plant and bacteroid; it binds free oxygen to protect oxygen-sensitive nitrogenase enzyme while supplying respiration."),

    ("Why must the enzyme nitrogenase in nitrogen-fixing bacteria be strictly protected by leghemoglobin from free molecular oxygen (O2)?",
     ["Nitrogenase is irreversibly poisoned and inactivated by free molecular oxygen",
      "Oxygen turns nitrogenase into toxic gas",
      "Nitrogenase requires pure carbon dioxide to function",
      "Oxygen melts the bacterial cell wall"],
     "A", "OSC", "medium",
     "The dinitrogenase molybdenum-iron catalytic core is irreversibly denatured by O2; leghemoglobin maintains an microaerobic environment delivering oxygen to respiratory chains at low partial pressures."),

    ("Which free-living, non-symbiotic aerobic bacterium fixes atmospheric nitrogen in neutral to alkaline soils without needing a plant host?",
     ["Azotobacter", "Rhizobium", "Agrobacterium", "Pseudomonas"],
     "A", "OSC", "easy",
     "Azotobacter is a free-living aerobic diazotroph that fixes significant atmospheric nitrogen non-symbiotically, simultaneously secreting plant growth-promoting hormones (auxins, gibberellins)."),

    ("Which free-living, non-symbiotic ANAEROBIC bacterium fixes atmospheric nitrogen in oxygen-depleted waterlogged soils?",
     ["Clostridium", "Azotobacter", "Rhizobium", "Nitrosomonas"],
     "A", "OSC", "medium",
     "Clostridium pasteurianum is an obligate anaerobic free-living diazotroph capable of fixing nitrogen in sub-surface or waterlogged soils lacking oxygen."),

    ("Which associative symbiotic bacterium colonizes the rhizosphere and root cortex of cereals and grasses (such as maize, wheat, and sorghum) to fix nitrogen?",
     ["Azospirillum", "Rhizobium", "Agrobacterium", "Streptomyces"],
     "A", "OSC", "medium",
     "Azospirillum forms associative relationships with grass roots without forming nodules, proliferating in intercellular spaces and supplying fixed nitrogen."),

    ("The tiny aquatic water fern Azolla is widely cultivated in paddy rice fields because its leaf dorsal cavities harbor which symbiotic nitrogen-fixing cyanobacterium?",
     ["Anabaena azollae", "Nostoc commune", "Spirulina platensis", "Chlorella vulgaris"],
     "A", "OSC", "easy",
     "The symbiotic association between the water fern Azolla and the blue-green alga Anabaena azollae can fix 40-60 kg of nitrogen per hectare, serving as a green biofertiliser in rice paddies."),

    ("What are the specialized thick-walled, pale cells in filamentous cyanobacteria (such as Nostoc and Anabaena) that provide an anaerobic site for nitrogen fixation called?",
     ["Heterocysts", "Akinetes", "Hormogonia", "Trichomes"],
     "A", "OSC", "medium",
     "Heterocysts lack oxygen-generating Photosystem II and possess thick multi-layered glycolipid walls that impede oxygen diffusion, creating ideal conditions for nitrogenase."),

    ("Which group of beneficial soil microorganisms (e.g., Pseudomonas striata and Bacillus megaterium) converts insoluble rock phosphate into soluble bioavailable forms?",
     ["Phosphate Solubilizing Biofertilisers (PSB)", "Nitrogen fixers", "Cellulolytic fungi", "Methanogens"],
     "A", "OSC", "easy",
     "PSBs secrete organic acids (gluconic, citric, malic acids) that chelate calcium and iron cations, converting insoluble tricalcium phosphate into bioavailable soluble monocalcium phosphate."),

    # 21-30: Mycorrhizae, Biopesticides & Sustainable Agriculture
    ("What is Mycorrhiza, an essential component of biofertiliser technology?",
     ["A mutualistic symbiotic association between a beneficial soil fungus (e.g. Glomus) and the roots of higher vascular plants",
      "A parasitic bacterium that kills trees",
      "A disease of tomato leaves",
      "A type of chemical weed killer"],
     "A", "OSC", "easy",
     "Mycorrhizae represent a classic mutualistic symbiosis: the fungal mycelium dramatically expands root surface area for phosphorus and water uptake in exchange for plant carbohydrates."),

    ("What does the acronym 'VAM' stand for in soil microbiology and biofertiliser science?",
     ["Vesicular-Arbuscular Mycorrhiza", "Viral-Algal Mutualism", "Vegetative-Asexual Microbe", "Vascular-Auxin Medium"],
     "A", "OSC", "medium",
     "VAM (endomycorrhizae) forms branched arbuscules for nutrient exchange and lipid-storing vesicles within root cortical cells, greatly enhancing phosphorus mobilization."),

    ("Which free-living soil fungus is widely used in organic farming as a potent biocontrol agent (biopesticide) against soil-borne fungal root-rot pathogens (e.g. Fusarium and Pythium)?",
     ["Trichoderma (e.g. Trichoderma harzianum)", "Penicillium", "Aspergillus", "Puccinia"],
     "A", "OSC", "easy",
     "Trichoderma secretes chitinases and glucanases that mycoparasitize and lyse pathogenic fungi, while competing aggressively for root rhizosphere colonization."),

    ("Which group of narrow-spectrum, species-specific insect viruses (Baculoviruses) are utilized as biological control agents against caterpillar and sawfly pests without harming non-target organisms?",
     ["Nucleopolyhedrovirus (NPV)", "Retrovirus", "Bacteriophage", "Tobacco mosaic virus"],
     "A", "OSC", "medium",
     "NPVs belong to the genus Baculovirus; their narrow-spectrum host range infects specific arthropods without having any pathogenic impact on fish, birds, mammals, or beneficial pollinators."),

    ("What is the major active biochemical limonoid extracted from the seeds and leaves of the Neem tree (Azadirachta indica) that acts as an eco-friendly biopesticide and antifeedant?",
     ["Azadirachtin", "Rotenone", "Nicotine", "Pyrethrin"],
     "A", "OSC", "easy",
     "Azadirachtin disrupts insect ecdysone titers, preventing larval molting, repelling adult oviposition, and acting as a potent antifeedant without leaving chemical residues."),

    ("Why are biofertilisers and biopesticides considered vastly superior to synthetic chemical fertilizers and chemical insecticides for long-term agriculture?",
     ["They restore natural soil microbiome health, do not cause groundwater pollution or eutrophication, and pests do not develop rapid resistance",
      "They cost a million dollars per gram",
      "They destroy all soil earthworms",
      "They eliminate rainfall from the atmosphere"],
     "A", "OSC", "easy",
     "Biological inputs are biodegradable, renewable, and eco-friendly; unlike synthetic NPK chemicals, they improve soil structure and prevent toxic chemical biomagnification."),

    ("What severe environmental crisis results when excessive synthetic nitrogen and phosphorus chemical fertilizers wash off farm fields into lakes and rivers?",
     ["Eutrophication (algal blooms leading to oxygen depletion and massive fish kills)",
      "Global cooling",
      "Acidification of the upper stratosphere",
      "Volcanic eruptions"],
     "A", "OSC", "easy",
     "Runoff of synthetic nitrates and phosphates causes explosive cyanobacterial and algal blooms; decomposing algae exhaust dissolved oxygen, suffocating aquatic aquatic fauna (eutrophication)."),

    ("In recombinant DNA technology used to engineer GM crops, which enzyme acts as 'molecular scissors' to cleave DNA molecules at specific palindromic recognition sequences?",
     ["Restriction Endonuclease", "DNA Ligase", "DNA Polymerase", "RNA Primase"],
     "A", "OSC", "medium",
     "Restriction endonucleases identify specific palindromic 4-8 bp sequences and cleave phosphodiester bonds, generating sticky or blunt ends for recombinant gene cloning."),

    ("Which enzyme acts as 'molecular glue' by catalyzing the covalent rejoining of sticky or blunt ends to construct a recombinant plasmid vector?",
     ["DNA Ligase", "Restriction Endonuclease", "Helicase", "Amylase"],
     "A", "OSC", "medium",
     "DNA ligase forms covalent 3'-5' phosphodiester bonds between adjacent nucleotides, physically sealing the passenger transgene into the vector plasmid."),

    ("What is a 'gene gun' (biolistics / microprojectile bombardment) in plant biotechnology?",
     ["A physical gene delivery apparatus that fires gold or tungsten microparticles coated with recombinant DNA into plant cells at supersonic velocity",
      "A weapon used to hunt agricultural insect pests",
      "A laser that burns weeds in the field",
      "An electronic machine that counts seeds"],
     "A", "OSC", "medium",
     "Biolistic particle delivery accelerates DNA-coated microscopic gold beads using high-pressure helium, penetrating intact plant cell walls to transform monocots (e.g. maize, rice).")
]

# Additional 10 questions to make exam_data 40
exam_data.extend([
    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("Bt Cotton carries insecticidal genes called ________ genes isolated from Bacillus thuringiensis.",
     ["cry", "lac", "lux", "amp"],
     "A", "OFB", "easy",
     "Cry genes (crystal protein genes) encode delta-endotoxins that confer resistance against chewing lepidopteran bollworms."),

    ("Golden Rice is biofortified to synthesize high concentrations of ________, the metabolic precursor of Vitamin A.",
     ["beta-carotene (provitamin A)", "vitamin C", "iron", "calcium"],
     "A", "OFB", "easy",
     "Carotenoid biosynthesis genes give the polished endosperm its golden color due to beta-carotene accumulation."),

    ("The active form of Bt crystal protein is solubilized strictly in the ________ pH environment of the insect larval midgut.",
     ["alkaline (pH > 9)", "acidic (pH < 3)", "neutral (pH 7)", "freezing"],
     "A", "OFB", "easy",
     "Alkaline gut pH is the essential biochemical trigger that dissolves the crystal protoxin, sparing non-target organisms with acidic guts."),

    ("State whether True or False: Leghemoglobin imparts a bright pink or red color to the interior of active, nitrogen-fixing legume root nodules.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Active Rhizobium nodules are pinkish-red inside due to high leghemoglobin concentrations; inactive nodules appear white or pale green."),

    ("Which of the following organisms are widely utilized as commercial BIOFERTILISERS in agriculture? (Select all that apply)",
     ["Rhizobium, Azotobacter, Anabaena azollae, and Mycorrhiza (Glomus)",
      "Only synthetic ammonium nitrate",
      "Only DDT and endosulfan",
      "Motor oil and kerosene"],
     "A", "OMC", "easy",
     "Rhizobium, Azotobacter, blue-green algae, and mycorrhizae represent the primary categories of commercial living biofertilisers."),

    ("Assertion (A): Cultivating the water fern Azolla in rice paddies enhances grain yield while reducing urea fertilizer requirements.\nReason (R): Azolla lives in obligate mutualistic symbiosis with the nitrogen-fixing cyanobacterium Anabaena azollae.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Anabaena inside Azolla cavities fixes atmospheric nitrogen, which is released into the paddy mud when the fern dies and decomposes as green manure."),

    ("What is the primary role of the Ti plasmid in Agrobacterium tumefaciens when modified for plant genetic transformation?",
     ["It serves as a disarmed vector that transfers foreign genes of interest (transgenes) directly into plant chromosomal DNA",
      "It produces deadly poison that kills all plants",
      "It dissolves soil rocks into sand",
      "It turns plant roots into edible fruits"],
     "A", "OSC", "medium",
     "Molecular biologists replace the tumor-causing auxin/cytokinin oncogenes within the T-DNA with beneficial transgenes, utilizing the natural transfer machinery of the Ti plasmid."),

    ("Which fungal biofertiliser forms an extensive underground network of hyphae that enhances plant absorption of phosphorus, zinc, and water from dry soil?",
     ["Vesicular-Arbuscular Mycorrhiza (VAM / Glomus)", "Yeast (Saccharomyces)", "Agaricus bisporus", "Rhizopus"],
     "A", "OSC", "easy",
     "VAM hyphae explore soil volumes 100 times greater than root hairs alone, translocating insoluble orthophosphate ions directly to the host cortex."),

    ("Why is biological control using Trichoderma or Baculoviruses safer than chemical pesticide spraying?",
     ["They target specific plant pests without leaving toxic chemical residues, killing beneficial pollinators, or causing biomagnification in food chains",
      "They make crops taste like sugar",
      "They stop all weeds from germinating",
      "They eliminate the need for sunlight"],
     "A", "OSC", "easy",
     "Biopesticides offer targeted, biodegradable pest suppression without bioaccumulating in human tissues or contaminating drinking aquifers."),

    ("State whether True or False: Glyphosate-tolerant 'Roundup Ready' crops carry an altered EPSPS enzyme that allows farmers to spray herbicide over the field to kill weeds without harming the crop.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Roundup Ready transgenic crops express bacterial CP4-EPSPS, conferring immunity to glyphosate herbicide and permitting selective chemical weed eradication.")
])

practice_data = [
    # 41-50: Advanced Genetic Engineering & Microbial Interactions
    ("How does the antisense RNA technology utilized in Flavr Savr tomatoes inhibit the expression of the polygalacturonase enzyme?",
     ["The introduced antisense RNA strand base-pairs with the sense mRNA strand, forming a double-stranded RNA duplex that cannot be translated by ribosomes",
      "Antisense RNA physically cuts the DNA into pieces",
      "It destroys the cell wall directly",
      "It freezes the tomatoes to -20 degrees C"],
     "A", "OSC", "hard",
     "Antisense RNA binds complementarily to endogenous mRNA; the resulting RNA duplex prevents ribosomal access and is targeted by cellular nucleases for degradation."),

    ("Which selectable marker gene is commonly incorporated into plant transformation vectors along with the gene of interest to identify successfully transformed cells?",
     ["Antibiotic resistance gene (e.g. nptII conferring kanamycin resistance)",
      "Hemoglobin gene",
      "Insulin gene",
      "Melanin gene"],
     "A", "OSC", "medium",
     "Selectable markers (such as neomycin phosphotransferase II / nptII) allow only successfully transformed plant cells to survive and proliferate on media containing toxic kanamycin."),

    ("What is 'Reporter Gene' (e.g., Green Fluorescent Protein / GFP or GUS) used for in plant genetic transformation?",
     ["Visually verifying and tracking where and when a transgene is actively expressed inside transformed plant tissues",
      "Killing all bacterial competitors",
      "Accelerating soil drying",
      "Sweetening fruit juices"],
     "A", "OSC", "medium",
     "Reporter genes (like jellyfish GFP or bacterial GUS) produce easily detectable fluorescence or blue color, confirming successful transcriptional activity in target tissues."),

    ("Why is biological nitrogen fixation through the nitrogenase enzyme an extremely energy-expensive biochemical reaction for bacteria?",
     ["Fixing a single molecule of atmospheric nitrogen (N2) into two molecules of ammonia (NH3) requires a minimum of 16 molecules of ATP: N2 + 8H+ + 8e- + 16 ATP -> 2NH3 + H2 + 16 ADP + 16 Pi",
      "It requires electrical currents from thunderstorms",
      "It burns pure coal inside the root",
      "It consumes all glucose in the human body"],
     "A", "OSC", "hard",
     "Breaking the extremely strong covalent triple bond of dinitrogen ($N \\equiv N$) demands 16 ATP molecules per N2 reduced, supplied by plant photosynthetic sucrose."),

    ("Which essential trace transition metal ions constitute the catalytic prosthetic core of the active nitrogenase enzyme complex?",
     ["Molybdenum and Iron (Mo-Fe protein complex)", "Copper and Zinc", "Calcium and Magnesium", "Sodium and Potassium"],
     "A", "OSC", "medium",
     "The catalytic MoFe protein contains a unique iron-molybdenum cofactor (FeMo-co) that binds dinitrogen and mediates multi-electron transfer for reduction to ammonia."),

    ("How do chemical signaling flavonoids released by legume roots initiate the nodulation process with Rhizobium bacteria?",
     ["Flavonoids diffuse into the rhizosphere and activate bacterial NodD regulatory proteins, which induce the transcription of nodulation (nod) genes",
      "Flavonoids poison the bacteria to keep them small",
      "Flavonoids turn the soil acidic",
      "Flavonoids kill all surrounding fungi"],
     "A", "OSC", "hard",
     "Root flavonoids act as molecular chemoattractants and ligands for bacterial NodD, triggering the synthesis and secretion of lipochitooligosaccharide Nod factors."),

    ("What morphological change in the host legume root hair is triggered by Rhizobium Nod factors during the initial infection step?",
     ["Root hair curling (Shepherd's crook formation)", "Root hair elongation into bark", "Root hair falling off completely", "Root hair freezing into ice"],
     "A", "OSC", "medium",
     "Nod factors induce asymmetric cell wall deposition and calcium spiking in the root hair tip, curling it into a tight 'shepherd's crook' that traps dividing rhizobia."),

    ("State whether True or False: Inoculating seeds with Rhizobium culture before sowing is an established agronomic practice to maximize pulse and soybean production without heavy urea fertilizer use.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Seed bacterization with carrier-based Rhizobium peat or lignite formulations ensures rapid early nodulation and reduces synthetic nitrogen requirements by 25-50%."),

    ("What is an 'endophytic' microorganism in agricultural biotechnology?",
     ["A bacterium or fungus that lives asymptomatically inside the internal tissues of a plant without causing disease symptoms, often enhancing growth and stress tolerance",
      "A microbe that lives only in deep ocean trenches",
      "A parasite that destroys the plant within 24 hours",
      "A bacterium found exclusively in milk"],
     "A", "OSC", "medium",
     "Endophytes colonize intercellular apoplastic spaces and vascular vessels mutualistically, producing phytohormones, fixing nitrogen, and priming systemic induced resistance against pests."),

    ("What are the environmental hazards associated with synthetic chemical insecticides like DDT, which prompted their global ban in agriculture?",
     ["Extreme chemical persistence, bioaccumulation, biomagnification through food chains, and thinning of bird eggshells",
      "They turn all insects into birds",
      "They make rain water taste sweet",
      "They cause clouds to disappear"],
     "A", "OSC", "easy",
     "Organochlorines like DDT are lipophilic and resist degradation, concentrating exponentially up trophic levels (biomagnification) and causing raptor reproductive failure.")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further GM & Biofertiliser Concepts
    ("Which gene from the bacterium Erwinia uredovora was introduced into rice to construct the beta-carotene biosynthetic pathway in Golden Rice?",
     ["crtI (Phytoene desaturase)", "cry1Ac", "nptII", "bar"],
     "A", "OSC", "hard",
     "The crtI gene encodes a multifunctional bacterial desaturase that converts phytoene directly into lycopene in endosperm plastids, completing the provitamin A cascade."),

    ("In agricultural biocontrol, what does the term 'Mycoparasitism' describe in the action of Trichoderma against pathogenic fungi?",
     ["Trichoderma physically coils around the pathogenic fungal hypha, secretes cell-wall degrading enzymes (chitinases), and digests the pathogen from within",
      "Trichoderma feeds on plant roots",
      "Trichoderma produces chemical fertilizers",
      "Trichoderma acts as food for insects"],
     "A", "OSC", "medium",
     "Trichoderma recognizes host surface lectins, tightly wraps around pathogenic hyphae (e.g. Rhizoctonia, Sclerotium), and hydrolyzes the fungal cell wall via chitinases and glucanases."),

    ("How do Phosphate Solubilizing Bacteria (PSBs) lower the rhizosphere pH to dissolve insoluble calcium phosphate minerals?",
     ["They secrete low-molecular-weight organic acids such as gluconic acid, lactic acid, and 2-ketogluconic acid",
      "They pump boiling water into the soil",
      "They absorb all sunlight from the soil",
      "They release pure sulfuric acid"],
     "A", "OSC", "medium",
     "Microbial oxidative pathways oxidize glucose to gluconic and 2-ketogluconic acids; proton release acidifies the microenvironment, solubilizing mineral phosphates."),

    ("State whether True or False: Mycorrhizal fungi cannot be grown axenically in pure artificial culture media without living host plant roots.",
     ["True", "False"],
     "A", "OTF", "hard",
     "Arbuscular mycorrhizal fungi (AMF / Glomus) are obligate biotrophs, strictly requiring fatty acids and carbon from living host root cells to complete their life cycle."),

    ("What is 'Bioremediation' in environmental biotechnology?",
     ["The use of microorganisms or plants to detoxify, degrade, or remove hazardous pollutants and heavy metals from contaminated soil and groundwater",
      "Using computers to predict the weather",
      "Building greenhouses from plastic",
      "Applying chemical fertilizers to crops"],
     "A", "OSC", "easy",
     "Bioremediation employs microbial enzymatic degradation (e.g. Pseudomonas putida breaking down crude oil hydrocarbons) to clean up ecological contaminants."),

    ("Which genetically engineered bacterium, patented by Ananda Mohan Chakrabarty, was designed to digest multiple hydrocarbon components of marine oil spills?",
     ["Pseudomonas putida ('Superbug')", "Bacillus thuringiensis", "Escherichia coli", "Agrobacterium tumefaciens"],
     "A", "OSC", "medium",
     "Chakrabarty's multi-plasmid Pseudomonas putida was engineered by cross-mating plasmids carrying genes for degrading octane, hexane, xylene, and camphor in oil slicks."),

    ("What is 'Phytoremediation'?",
     ["The utilization of green plants to extract, sequester, or detoxify toxic heavy metals (like lead, arsenic, cadmium) from contaminated soils",
      "Curing plant diseases with antibiotics",
      "Making paper from wood pulp",
      "Watering plants with chemical fertilizers"],
     "A", "OSC", "easy",
     "Phytoremediation leverages hyperaccumulating plants (e.g. Brassica juncea, sunflower) to translocate heavy metal contaminants from soil into harvestable biomass."),

    ("State whether True or False: Azotobacter biofertiliser simultaneously enhances plant growth by synthesizing phytohormones such as indole-3-acetic acid (IAA) and gibberellins.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Beyond nitrogen fixation, Azotobacter excretes substantial quantities of auxins, gibberellic acid, and B-vitamins that stimulate root elongation and crop vigor."),

    ("Which enzyme in blue-green algae (Cyanobacteria) catalyzes the conversion of atmospheric dinitrogen into ammonium ions?",
     ["Nitrogenase", "DNA polymerase", "Cellulase", "Ribulose bisphosphate carboxylase"],
     "A", "OSC", "easy",
     "Nitrogenase is the universal metalloenzyme complex responsible for biological nitrogen reduction across all diazotrophic cyanobacteria and eubacteria."),

    ("What role does the 'T-DNA' border sequence play in Agrobacterium Ti-plasmid vectors?",
     ["Two 25-base-pair direct repeat sequences (Left and Right borders) demarcate the specific DNA segment that is excised and transferred into the plant nucleus",
      "They make the bacterium glow green",
      "They freeze the plant roots",
      "They kill all neighboring plants"],
     "A", "OSC", "hard",
     "The 25 bp imperfect direct repeat flanking borders (LB and RB) are recognized by VirD1/D2 endonucleases, which nick the borders to release the single-stranded T-strand for nuclear transfer.")
])

# 10 more questions to complete practice_data to 30
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("Why is Bt Brinjal (eggplant) an important agricultural biotechnology development in South Asia?",
     ["It provides endogenous resistance against the destructive Brinjal Fruit and Shoot Borer (FSB), reducing pesticide applications by over 80%",
      "It grows brinjal fruits made of pure gold",
      "It grows on dry rocks without any soil",
      "It tastes like sweet honey"],
     "A", "OSC", "easy",
     "Bt Brinjal expresses Cry1Ac, controlling the fruit and shoot borer (Leucinodes orbonalis) and eliminating hazardous organophosphate and pyrethroid pesticide sprays."),

    ("Which Indian regulatory statutory body under the Ministry of Environment evaluates and approves the environmental release of GM crops in India?",
     ["Genetic Engineering Appraisal Committee (GEAC)", "ICAR", "UGC", "CSIR"],
     "A", "OSC", "medium",
     "GEAC (Genetic Engineering Appraisal Committee) evaluates biosafety, food safety, and environmental impact before permitting commercial cultivation of GM crops."),

    ("What is 'Refugia' planting in Bt cotton management strategy?",
     ["Planting a border of non-Bt cotton around a Bt cotton field to sustain a population of susceptible bollworms and prevent the emergence of Bt-resistant pests",
      "Building a fence around the farm",
      "Covering the crops with plastic sheets",
      "Digging a water canal around the farm"],
     "A", "OSC", "hard",
     "Refugia rows preserve non-Bt-exposed susceptible insects to mate with rare resistant individuals, maintaining recessive susceptibility alleles and delaying pest resistance evolution."),

    ("Which biofertiliser is uniquely adapted for dryland agriculture because its spores survive severe soil desiccation for years?",
     ["Mycorrhizal fungal spores (Glomus / VAM)", "Free-living Rhizobium", "Anabaena", "Azolla"],
     "A", "OSC", "medium",
     "Thick-walled chlamydospores of VAM fungi survive severe drought and extreme temperatures, germinating upon sensing root exudates during the next rainfall."),

    ("State whether True or False: Synthetic chemical nitrogen fertilizers (like urea) can be completely replaced in leguminous crops by inoculating seeds with effective Rhizobium strains.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Well-nodulated pulses and legumes obtain 80-90% of their nitrogen requirements through symbiotic Rhizobium fixation, requiring zero basal chemical nitrogen."),

    ("Which vitamin-producing gene from daffodils (Narcissus pseudonarcissus) provided the phytoene synthase (psy) enzyme for Golden Rice engineering?",
     ["psy gene (Phytoene synthase)", "cry1Ac", "bar gene", "GFP gene"],
     "A", "OSC", "hard",
     "The daffodil psy gene directs the condensation of two geranylgeranyl diphosphate molecules into phytoene, initiating the carotenoid pathway in rice endosperm."),

    ("What is an 'antifeedant' biopesticide effect (such as that caused by neem azadirachtin)?",
     ["Insects cease feeding on the treated foliage and starve to death even when food is abundant",
      "Insects explode instantly upon touching the leaf",
      "Insects reproduce 100 times faster",
      "Insects fall asleep immediately"],
     "A", "OSC", "easy",
     "Antifeedants stimulate insect deterrent chemoreceptors while paralyzing swallowing and feeding reflexes, causing larvae to starve without environmental chemical toxicity."),

    ("Which agricultural waste product is commonly inoculated with beneficial microbes and earthworms to manufacture organic vermicompost?",
     ["Cattle dung, crop straw, and vegetable residue", "Plastic bottles", "Glass shards", "Electronic computer parts"],
     "A", "OSC", "easy",
     "Vermicomposting combines epigeic earthworms (Eisenia foetida) with microbial consortia to rapidly decompose farm biomass into nutrient-rich humus casting biofertiliser."),

    ("How do biofertilisers enhance soil carbon sequestration compared to chemical fertilizer application?",
     ["Microbial biomass and fungal glomalin synthesize stable soil aggregates and humus that store atmospheric carbon in the soil profile for decades",
      "Biofertilisers burn the carbon away",
      "They turn soil into diamond crystals",
      "They release all carbon as gas into the sky"],
     "A", "OSC", "medium",
     "Mycorrhizae produce glomalin, a recalcitrant hydrophobic glycoprotein that glues soil particles into stable aggregates, sequestering carbon and resisting erosion."),

    ("State whether True or False: Bt crops do not harm beneficial non-target insects such as honeybees, ladybird beetles, and butterflies that do not chew on the transgenic crop tissues.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Bt toxins are tissue-specific and act solely via ingestion by susceptible chewing pests; pollinators feeding strictly on nectar and predatory beetles remain completely unharmed.")
])

mock_data = [
    # 71: Bt Endotoxin Activation Mechanism in Bollworm Alkaline Gut
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Step 1: Crystal Protoxin Ingested -->
  <rect x="20" y="30" width="100" height="60" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="50,45 70,35 90,45 80,65 60,65" fill="#38bdf8"/>
  <text x="70" y="80" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">1. Inactive Cry Crystal</text>
  <line x1="120" y1="60" x2="155" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Step 2: Alkaline Gut Dissolution -->
  <rect x="155" y="30" width="110" height="60" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <circle cx="210" cy="50" r="12" fill="#eab308"/>
  <text x="210" y="75" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">2. Alkaline Midgut (pH > 9)</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Solubilizes into active toxin</text>
  <line x1="265" y1="60" x2="300" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Step 3: Membrane Lysis -->
  <rect x="300" y="30" width="85" height="60" rx="5" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <circle cx="342" cy="50" r="14" fill="#ef4444"/>
  <circle cx="342" cy="50" r="5" fill="#090d16"/>
  <text x="342" y="75" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">3. Pores in Midgut</text>
  <text x="342" y="85" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Epithelial Cell Lysis!</text>
  <!-- Summary Box -->
  <rect x="30" y="110" width="340" height="80" rx="6" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="130" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Why Bt Endotoxin is Safe for Humans but Lethal to Bollworms:</text>
  <text x="200" y="150" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Human stomach is highly ACIDIC (pH 1.5-2) -> Protoxin remains inert & digested</text>
  <text x="200" y="170" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle">Bollworm midgut is ALKALINE (pH > 9) -> Toxin solubilizes, creates pores & kills pest!</text>
</svg>
</div>
Based on the molecular activation pathway shown above, why does the Bt crystal endotoxin selectively kill chewing caterpillar pests while posing zero toxicity to humans?""",
     ["The protoxin requires the high alkaline pH (>9) of insect midguts to dissolve and bind specific cadherin receptors, whereas human stomachs are highly acidic (pH 1.5-2)",
      "Humans never eat cotton plants",
      "Bollworms have no cell membranes",
      "The toxin evaporates before humans can touch it"],
     "A", "OSC", "medium",
     "Solubilization and proteolytic activation of Bt protoxin into active 60 kDa delta-endotoxin strictly requires alkaline midgut conditions and specific invertebrate cadherin receptors lacking in mammals."),

    # 72: Golden Rice Beta-Carotene Biosynthetic Pathway
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Precursor -->
  <rect x="30" y="30" width="95" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="77" y="48" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">GGPP</text>
  <text x="77" y="60" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">(Natural in rice)</text>
  <!-- Enzyme 1 (psy) -->
  <line x1="125" y1="50" x2="165" y2="50" stroke="#facc15" stroke-width="2"/>
  <text x="145" y="40" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">psy gene</text>
  <!-- Intermediate -->
  <rect x="165" y="30" width="85" height="40" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="207" y="48" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Phytoene</text>
  <!-- Enzyme 2 (crtI) -->
  <line x1="250" y1="50" x2="290" y2="50" stroke="#facc15" stroke-width="2"/>
  <text x="270" y="40" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">crtI gene</text>
  <!-- End Product -->
  <rect x="290" y="25" width="85" height="50" rx="5" fill="#854d0e" stroke="#eab308" stroke-width="2"/>
  <text x="332" y="48" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">BETA-</text>
  <text x="332" y="62" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">CAROTENE</text>
  <!-- Human Health Benefit Box -->
  <rect x="40" y="100" width="320" height="75" rx="6" fill="#090d16" stroke="#4ade80" stroke-width="1"/>
  <text x="200" y="120" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Golden Rice (Ingo Potrykus & Peter Beyer)</text>
  <text x="200" y="140" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Beta-carotene in rice endosperm -> Converted to active VITAMIN A in human liver</text>
  <text x="200" y="160" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Combats childhood blindness & Vitamin A Deficiency (VAD) in developing nations!</text>
</svg>
</div>
Which two exogenous genes were transferred into rice endosperm plastids to reconstruct the complete beta-carotene biosynthesis pathway in Golden Rice?""",
     ["Phytoene synthase (psy from daffodil/maize) and Phytoene desaturase (crtI from Erwinia uredovora)",
      "Insulin gene and Hemoglobin gene",
      "Amylase gene and Pepsin gene",
      "Cry1Ac gene and Cry2Ab gene"],
     "A", "OSC", "hard",
     "Potrykus and Beyer solved Golden Rice engineering by supplying daffodil/maize phytoene synthase (psy) and bacterial carotene desaturase (crtI) to produce beta-carotene in endosperm tissue."),

    # 73: Legume Root Nodule Rhizobium & Pink Leghemoglobin
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Root with nodule -->
  <line x1="30" y1="100" x2="370" y2="100" stroke="#78350f" stroke-width="8"/>
  <!-- Nodule cross section -->
  <circle cx="150" cy="100" r="38" fill="#831843" stroke="#f43f5e" stroke-width="3"/>
  <text x="150" y="95" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pink Nodule</text>
  <text x="150" y="108" fill="#fbcfe8" font-size="8" font-family="sans-serif" text-anchor="middle">Interior</text>
  <!-- Bacteroids inside -->
  <circle cx="138" cy="85" r="4" fill="#facc15"/>
  <circle cx="155" cy="88" r="4" fill="#facc15"/>
  <circle cx="145" cy="115" r="4" fill="#facc15"/>
  <circle cx="162" cy="110" r="4" fill="#facc15"/>
  <!-- Labels -->
  <line x1="188" y1="85" x2="230" y2="50" stroke="#f43f5e" stroke-width="2"/>
  <text x="240" y="45" fill="#f43f5e" font-size="10" font-family="sans-serif" font-weight="bold">Pink Leghemoglobin Pigment</text>
  <text x="240" y="60" fill="#cbd5e1" font-size="8" font-family="sans-serif">Oxygen scavenger: Maintains low O2</text>
  <line x1="188" y1="115" x2="230" y2="135" stroke="#facc15" stroke-width="2"/>
  <text x="240" y="130" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Rhizobium Bacteroids</text>
  <text x="240" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif">Nitrogenase reduces N2 -> NH3</text>
  <text x="240" y="160" fill="#4ade80" font-size="8" font-family="sans-serif">Nitrogenase is poisoned by O2!</text>
</svg>
</div>
What vital biochemical duty is fulfilled by the pink leghemoglobin pigment inside active Rhizobium root nodules?""",
     ["It acts as an oxygen buffer/scavenger, sequestering free O2 to protect oxygen-sensitive nitrogenase enzyme while supplying respiration to bacteroids",
      "It colors the root pink to scare underground insects",
      "It absorbs table salt from the groundwater",
      "It produces red flower petals on the leaves"],
     "A", "OSC", "medium",
     "Free oxygen irreversibly denatures the iron-molybdenum core of nitrogenase; leghemoglobin binds free oxygen with high affinity, delivering it to bacterial respiratory cytochromes at safe low tensions."),

    # 74: Agrobacterium Ti-Plasmid T-DNA Transformation Vector
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Circular Ti Plasmid -->
  <circle cx="120" cy="100" r="55" fill="none" stroke="#38bdf8" stroke-width="8"/>
  <!-- T-DNA Segment (Golden) -->
  <path d="M 120 45 A 55 55 0 0 1 175 100" stroke="#facc15" stroke-width="12" fill="none"/>
  <text x="160" y="65" fill="#facc15" font-size="9" font-family="sans-serif" font-weight="bold">T-DNA</text>
  <!-- Vir genes region -->
  <path d="M 65 100 A 55 55 0 0 1 120 45" stroke="#ec4899" stroke-width="8" fill="none"/>
  <text x="75" y="65" fill="#ec4899" font-size="8" font-family="sans-serif">Vir Genes</text>
  <text x="120" y="105" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Disarmed Ti</text>
  <text x="120" y="118" fill="#bfdbfe" font-size="8" font-family="sans-serif" text-anchor="middle">Plasmid</text>
  <!-- Transfer Arrow -->
  <line x1="185" y1="100" x2="230" y2="100" stroke="#facc15" stroke-width="3"/>
  <!-- Plant Cell Nucleus -->
  <rect x="230" y="45" width="140" height="110" rx="8" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <circle cx="300" cy="95" r="28" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
  <text x="300" y="92" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Plant</text>
  <text x="300" y="104" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Genome</text>
  <text x="300" y="138" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Transgene Integrated!</text>
  <text x="200" y="180" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Agrobacterium tumefaciens: "Nature's Genetic Engineer"</text>
</svg>
</div>
Why is Agrobacterium tumefaciens widely known as 'Nature's Genetic Engineer' in plant biotechnology?""",
     ["Its Ti-plasmid naturally transfers a discrete segment of DNA (T-DNA) across kingdom boundaries into plant nuclear chromosomes",
      "It builds greenhouses for farmers",
      "It fixes nitrogen directly inside seeds",
      "It kills all weeds in crop fields"],
     "A", "OSC", "easy",
     "Agrobacterium evolved the biological machinery (vir genes and T-DNA borders) to transfer DNA into plant nuclear genomes; disarming its tumor genes allows scientists to shuttle transgenes into crops."),

    # 75: Azolla-Anabaena Paddy Biofertiliser Cycle
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Water surface -->
  <rect x="30" y="90" width="340" height="75" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="2"/>
  <text x="50" y="110" fill="#38bdf8" font-size="9" font-family="sans-serif">Flooded Paddy Field Water</text>
  <!-- Floating Azolla fern -->
  <path d="M 80 88 Q 110 75 140 88 Q 120 95 80 88 Z" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="110" y="70" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Azolla Water Fern</text>
  <!-- Anabaena inside cavity -->
  <circle cx="110" cy="85" r="4" fill="#38bdf8"/>
  <line x1="110" y1="60" x2="160" y2="35" stroke="#38bdf8" stroke-width="2"/>
  <text x="170" y="35" fill="#38bdf8" font-size="9" font-family="sans-serif" font-weight="bold">Anabaena azollae (Cyanobacteria)</text>
  <text x="170" y="48" fill="#cbd5e1" font-size="8" font-family="sans-serif">Lives in leaf cavities & fixes 40-60 kg N/ha</text>
  <!-- Nitrogen released to rice -->
  <line x1="110" y1="95" x2="110" y2="135" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <text x="120" y="145" fill="#facc15" font-size="9" font-family="sans-serif">Decomposes -> Releases Ammonium (NH4+) to Rice Roots</text>
  <!-- Rice plant stalk -->
  <line x1="280" y1="150" x2="280" y2="40" stroke="#22c55e" stroke-width="4"/>
  <text x="280" y="30" fill="#22c55e" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rice Plant</text>
  <text x="280" y="175" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Heavy Nitrogen Uptake</text>
</svg>
</div>
How does co-cultivating the tiny water fern Azolla in flooded paddy fields dramatically boost rice yields without synthetic urea?""",
     ["Symbiotic Anabaena cyanobacteria inside Azolla leaf cavities fix atmospheric nitrogen, which fertilizes rice roots when the fern biomass decomposes",
      "Azolla ferns eat all weeds in the paddy",
      "Azolla turns water into pure ethanol",
      "Azolla protects rice from thunderstorm lightning"],
     "A", "OSC", "easy",
     "Azolla harbors Anabaena azollae in dorsal leaf pouches, fixing 40-60 kg atmospheric N/ha; rapid vegetative biomass decomposition mineralizes nitrogen into bioavailable ammonium for rice crops."),

    # 76: VAM (Vesicular-Arbuscular Mycorrhiza) Hyphal Network
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Root Cylinder -->
  <rect x="30" y="50" width="100" height="90" rx="8" fill="#78350f" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="95" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Plant Root</text>
  <!-- Internal Arbuscules & Vesicles -->
  <circle cx="105" cy="75" r="8" fill="#facc15"/>
  <text x="105" y="78" fill="#000000" font-size="6" font-family="sans-serif" text-anchor="middle">V</text>
  <!-- Extensive Fungal Hyphae Network extending into soil -->
  <path d="M 130 95 Q 180 60 230 75 T 320 60 T 360 85" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 130 95 Q 190 120 250 110 T 340 135" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 230 75 L 260 40" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 250 110 L 290 155" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Soil Phosphate uptake -->
  <circle cx="340" cy="65" r="5" fill="#ec4899"/>
  <text x="350" y="68" fill="#ec4899" font-size="8" font-family="sans-serif">P</text>
  <circle cx="320" cy="140" r="5" fill="#ec4899"/>
  <text x="330" y="143" fill="#ec4899" font-size="8" font-family="sans-serif">P</text>
  <!-- Summary Box -->
  <text x="250" y="25" fill="#38bdf8" font-size="11" font-family="sans-serif" font-weight="bold">VAM Hyphal Network (Glomus)</text>
  <text x="250" y="175" fill="#facc15" font-size="9" font-family="sans-serif">100x Surface Area Expansion -> Mobilizes Insoluble Phosphorus & Micronutrients!</text>
</svg>
</div>
Why does inoculating crop roots with VAM (Vesicular-Arbuscular Mycorrhizal) fungi dramatically improve crop performance in phosphorus-deficient dry soils?""",
     ["Extensive microscopic fungal hyphae explore soil volumes 100 times beyond root hair reach, solubilizing and translocating immobile phosphate ions and water to the plant",
      "VAM fungi turn dry sand into wet clay",
      "VAM fungi produce synthetic pesticide chemicals",
      "VAM fungi make plants produce fruits overnight"],
     "A", "OSC", "easy",
     "Insoluble phosphate ions diffuse slowly in soil; VAM extra-radical hyphal networks bridge the depletion zone, secreting phosphatases and transporting phosphorus and water back to host cortical cells."),

    # 77: Free-Living vs Symbiotic Nitrogen Fixers Classification
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Symbiotic Column -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">SYMBIOTIC FIXERS</text>
  <text x="107" y="70" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Form mutualistic host links</text>
  <text x="107" y="95" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Rhizobium (Legume nodules)</text>
  <text x="107" y="115" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Anabaena azollae (Water fern)</text>
  <text x="107" y="135" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Frankia (Alnus non-legume)</text>
  <text x="107" y="152" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">High N Fixation (50-200 kg/ha)</text>
  <!-- Free-Living Column -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="48" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">FREE-LIVING DIAZOTROPHS</text>
  <text x="292" y="70" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Independent in bulk soil</text>
  <text x="292" y="95" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle">Azotobacter (Aerobic soil)</text>
  <text x="292" y="115" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle">Clostridium (Anaerobic mud)</text>
  <text x="292" y="135" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle">Azospirillum (Grass roots)</text>
  <text x="292" y="152" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">Secrete plant growth hormones</text>
</svg>
</div>
What functional distinction separates symbiotic nitrogen fixers (like Rhizobium) from free-living diazotrophs (like Azotobacter)?""",
     ["Symbiotic fixers require mutualistic root nodule formation with host plants to obtain energy, whereas free-living fixers fix nitrogen independently in open soil",
      "Free-living fixers kill all plant roots",
      "Symbiotic fixers are animals while free-living fixers are plants",
      "Free-living fixers operate only in pure salt water"],
     "A", "OSC", "easy",
     "Rhizobium depends obligately on host photosynthates within organized nodules; Azotobacter and Clostridium derive energy independently from soil organic matter decomposition."),

    # 78: Trichoderma Biocontrol Mycoparasitism Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Pathogenic Fungus Hypha (Red) -->
  <line x1="40" y1="95" x2="360" y2="95" stroke="#ef4444" stroke-width="12" stroke-linecap="round"/>
  <text x="50" y="75" fill="#f87171" font-size="10" font-family="sans-serif" font-weight="bold">Pathogen Hypha (Fusarium / Rhizoctonia Root Rot)</text>
  <!-- Trichoderma Coiling Around (Green) -->
  <path d="M 120 75 Q 140 120 160 75 T 200 75 T 240 75" stroke="#22c55e" stroke-width="6" fill="none"/>
  <circle cx="160" cy="95" r="6" fill="#facc15"/>
  <text x="160" y="60" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Chitinase Enzyme Attack</text>
  <!-- Description -->
  <rect x="40" y="120" width="320" height="55" rx="5" fill="#18181b" stroke="#22c55e" stroke-width="1"/>
  <text x="200" y="138" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Trichoderma Biopesticide Mechanism: Mycoparasitism</text>
  <text x="200" y="155" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Coils around fungal pathogens -> Secretes chitinase -> Lysates & kills root rot fungi!</text>
</svg>
</div>
How does the biological control fungus Trichoderma protect crop seedlings from damping-off and root-rot diseases?""",
     ["It directly recognizes and coils around pathogenic fungal hyphae, secreting chitinases and glucanases to dissolve the pathogen's cell wall",
      "It freezes the soil to kill bacteria",
      "It changes the color of plant leaves to red",
      "It absorbs all water from the soil"],
     "A", "OSC", "medium",
     "Trichoderma exhibits active mycoparasitism: it coils around phytopathogenic fungi (e.g. Fusarium, Sclerotium) and excretes lytic beta-1,3-glucanases and chitinases that perforate and destroy the pathogen."),

    # 79: Flavr Savr Tomato Antisense RNA Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Sense mRNA -->
  <line x1="50" y1="50" x2="200" y2="50" stroke="#38bdf8" stroke-width="4"/>
  <text x="125" y="40" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Sense Polygalacturonase mRNA (Softening)</text>
  <!-- Antisense RNA introduced -->
  <line x1="50" y1="70" x2="200" y2="70" stroke="#ec4899" stroke-width="4"/>
  <text x="125" y="90" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle">Introduced Antisense RNA (Complementary)</text>
  <!-- Duplex Block -->
  <line x1="220" y1="60" x2="270" y2="60" stroke="#facc15" stroke-width="2"/>
  <rect x="270" y="40" width="105" height="40" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <text x="322" y="58" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Double-Stranded</text>
  <text x="322" y="70" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">RNA Blocked!</text>
  <!-- Result Box -->
  <rect x="40" y="115" width="320" height="55" rx="5" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="135" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Result: Flavr Savr Extended Shelf-Life Tomato</text>
  <text x="200" y="152" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Pectin cell wall remains firm -> Fruit stays fresh & firm for weeks without rotting!</text>
</svg>
</div>
How did antisense RNA technology prevent fruit rotting and softening in the Flavr Savr tomato?""",
     ["Complementary antisense RNA hybridized with endogenous polygalacturonase mRNA, preventing ribosomal translation and pectin breakdown",
      "It injected plastic into the tomato skin",
      "It removed all water from the tomato",
      "It replaced tomato seeds with stones"],
     "A", "OSC", "medium",
     "Antisense mRNA pairing forms an untranslatable RNA duplex, silencing polygalacturonase enzyme production and preserving cell-wall structural pectin for delayed softening and prolonged shelf-life."),

    # 80: Recombinant DNA (rDNA) Technology Construction Steps
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Plasmid Vector -->
  <circle cx="80" cy="65" r="28" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="80" y="68" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Vector Plasmid</text>
  <text x="130" y="70" fill="#ffffff" font-size="16" font-family="sans-serif">+</text>
  <!-- Foreign Gene of Interest -->
  <rect x="155" y="55" width="40" height="20" rx="3" fill="#facc15"/>
  <text x="175" y="68" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gene</text>
  <line x1="215" y1="65" x2="265" y2="65" stroke="#facc15" stroke-width="2"/>
  <text x="240" y="55" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">DNA Ligase</text>
  <!-- Recombinant Plasmid -->
  <circle cx="320" cy="65" r="28" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <path d="M 320 37 A 28 28 0 0 1 348 65" stroke="#facc15" stroke-width="6" fill="none"/>
  <text x="320" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">rDNA</text>
  <!-- Step labels -->
  <rect x="30" y="115" width="340" height="60" rx="6" fill="#090d16" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="135" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Enzymatic Tools of Recombinant DNA Technology:</text>
  <text x="200" y="152" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">1. Restriction Endonuclease ("Molecular Scissors"): Cleaves at palindromes</text>
  <text x="200" y="167" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">2. DNA Ligase ("Molecular Glue"): Forms phosphodiester bonds to seal transgene</text>
</svg>
</div>
What paired roles are performed by Restriction Endonuclease and DNA Ligase in creating recombinant plasmids for transgenic crops?""",
     ["Restriction endonuclease acts as molecular scissors to cut DNA at specific palindromic sequences, while DNA ligase acts as molecular glue to join foreign genes into vectors",
      "Restriction endonuclease freezes DNA while ligase boils it",
      "Both enzymes destroy DNA completely",
      "DNA ligase cuts DNA while restriction enzyme repairs it"],
     "A", "OSC", "easy",
     "Restriction endonucleases generate complementary sticky ends at defined recognition palindromes; DNA ligase catalyzes phosphodiester bond formation between vector and passenger DNA to complete recombinant vectors."),

    # 81: Biofertiliser vs Chemical Fertilizer Environmental Impact
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Chemical Fertilizer Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="107" y="48" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">CHEMICAL FERTILIZERS</text>
  <text x="107" y="70" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">(Synthetic Urea, NPK)</text>
  <text x="107" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Destroys soil microbiome</text>
  <text x="107" y="112" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Runoff causes Eutrophication</text>
  <text x="107" y="129" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Contaminates groundwater</text>
  <text x="107" y="148" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Long-term soil degradation</text>
  <!-- Biofertiliser Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="292" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">BIOFERTILISERS</text>
  <text x="292" y="70" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">(Living Microbial Inoculants)</text>
  <text x="292" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Restores living soil health</text>
  <text x="292" y="112" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Renewable & zero pollution</text>
  <text x="292" y="129" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Secretes natural hormones</text>
  <text x="292" y="148" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sustainable & eco-friendly!</text>
</svg>
</div>
Why does agricultural biotechnology advocate shifting from chemical synthetic fertilizers to biological microbial biofertilisers?""",
     ["Biofertilisers enhance soil biology sustainably, prevent chemical runoff eutrophication into rivers, and provide continuous nutrient release without toxic residues",
      "Chemical fertilizers are too cheap to use",
      "Biofertilisers eliminate the need to harvest crops",
      "Chemical fertilizers make plants grow backwards"],
     "A", "OSC", "easy",
     "Synthetic nitrogen runoff triggers massive freshwater eutrophication and soil acidification; biofertilisers provide closed-loop natural nutrient cycling without ecological contamination."),

    # 82: Neem Azadirachtin Biopesticide Spectrum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Neem Leaf & Seed -->
  <circle cx="80" cy="80" r="35" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="80" y="75" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Neem Tree</text>
  <text x="80" y="90" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">(Azadirachta)</text>
  <!-- Arrow -->
  <line x1="125" y1="80" x2="175" y2="80" stroke="#facc15" stroke-width="3"/>
  <text x="150" y="70" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Extract</text>
  <!-- Azadirachtin Action Box -->
  <rect x="180" y="30" width="195" height="130" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="277" y="52" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Azadirachtin Limonoid Actions:</text>
  <text x="195" y="75" fill="#cbd5e1" font-size="9" font-family="sans-serif">1. Antifeedant: Pests refuse to eat</text>
  <text x="195" y="95" fill="#cbd5e1" font-size="9" font-family="sans-serif">2. Ecdysone Blocker: Halts larval molting</text>
  <text x="195" y="115" fill="#cbd5e1" font-size="9" font-family="sans-serif">3. Oviposition Deterrent: Prevents egg lay</text>
  <text x="195" y="135" fill="#4ade80" font-size="9" font-family="sans-serif">4. Non-toxic to bees & earthworms!</text>
</svg>
</div>
How does the natural botanical biopesticide azadirachtin extracted from neem trees control chewing insect pests without chemical toxicity?""",
     ["It acts as an antifeedant and disrupts ecdysone hormone regulation, preventing pest larvae from molting into adults while repelling egg laying",
      "It suffocates plants with smoke",
      "It burns the insect wings with fire",
      "It melts soil minerals into liquid glass"],
     "A", "OSC", "easy",
     "Azadirachtin binds sensory deterrent receptors to arrest feeding, and downregulates prothoracicotropic and ecdysteroid titers, arresting larval metamorphoses without synthetic neurotoxic harm to beneficial pollinators.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch17_topic2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
