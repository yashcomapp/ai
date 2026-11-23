import json
import random
import os
from build_mh8_sci_batch import make_question, get_vaults_and_diffs

random.seed(8911)

def run():
    with open("scripts/mh8_sci_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 10 DATA
    # -------------------------------------------------------------------------
    ch10_cases = {
        "MH-8-SCI-10-10.1.1": [
            ("What is the primary structural carbohydrate component of the plant cell wall that provides rigidity?", "Cellulose and pectin", ["Chitin and glycogen", "Phospholipids and cholesterol", "Peptidoglycan"]),
            ("Which statement accurately describes the permeability and nature of the plant cell wall?", "It is freely permeable, non-living, and situated outside the plasma membrane", ["It is semi-permeable and living", "It is impermeable to water", "It contains hemoglobin"]),
            ("Why do animal cells lack a cell wall unlike plant and fungal cells?", "Animals have flexible structural systems like skeletons and do not face extreme osmotic turgor pressure changes", ["Animal cells have no plasma membrane", "Animal cells cannot synthesize proteins", "Animal cells do not contain cytoplasm"]),
            ("Which carbohydrate constitutes the rigid cell wall in fungi such as Aspergillus and Yeast?", "Chitin", ["Cellulose", "Starch", "Peptidoglycan"])
        ],
        "MH-8-SCI-10-10.1.2": [
            ("The plasma membrane is described as a 'selectively permeable membrane' because it:", "Permits only specific solutes and solvents to enter and leave while restricting others", ["Allows all molecules to pass without restriction", "Blocks all substances completely", "Dissolves in water immediately"]),
            ("According to the Fluid Mosaic Model (Singer & Nicolson), the plasma membrane is primarily composed of:", "A phospholipid bilayer with embedded protein molecules", ["A triple layer of carbohydrates", "Rigid cellulose strands", "Pure ribonucleic acid"]),
            ("When a plant cell is placed in a hypertonic solution, water moves out causing the protoplasm to shrink away from the cell wall. This phenomenon is called:", "Plasmolysis", ["Endosmosis", "De-plasmolysis", "Cytokinesis"]),
            ("The movement of water molecules across a selectively permeable membrane from higher water concentration to lower water concentration is called:", "Osmosis", ["Active diffusion", "Phagocytosis", "Transpiration"])
        ],
        "MH-8-SCI-10-10.1.3": [
            ("What is the clear, jelly-like ground substance of the cytoplasm excluding cell organelles known as?", "Cytosol", ["Nucleoplasm", "Tonoplast", "Chromatin"]),
            ("Which vital cellular metabolic pathway takes place within the cytosol (cytoplasm) of both prokaryotes and eukaryotes?", "Glycolysis (initial breakdown of glucose)", ["Krebs cycle in matrix", "Electron transport chain", "Transcription in nucleus"]),
            ("Which of the following organic molecules are stored dissolved in the cellular cytoplasm?", "Amino acids, glucose, fatty acids, and mineral ions", ["Solid calcium carbonate crystals", "Pure gaseous nitrogen", "Only DNA molecules"]),
            ("The constant streaming movement of cytoplasm inside living eukaryotic cells is known as:", "Cyclosis (cytoplasmic streaming)", ["Pinocytosis", "Dialysis", "Osmosis"])
        ],
        "MH-8-SCI-10-10.2.1": [
            ("Which organelle acts as the chief control center of cellular activities and contains genetic information?", "Nucleus", ["Golgi apparatus", "Ribosome", "Centrosome"]),
            ("The double-layered boundary enclosing the nucleus with distinct pores for macromolecular exchange is the:", "Nuclear membrane", ["Plasma membrane", "Tonoplast", "Pericardium"]),
            ("Chromatin fibers in a non-dividing cell condense and coil during cell division to form visible structures called:", "Chromosomes", ["Lysosomes", "Cristae", "Chloroplasts"]),
            ("The dense spherical structure located inside the nucleus responsible for ribosome subunit synthesis is the:", "Nucleolus", ["Centriole", "Mitochondrion", "Vacuole"])
        ],
        "MH-8-SCI-10-10.2.2": [
            ("What gives Rough Endoplasmic Reticulum (RER) its characteristic rough granular appearance under an electron microscope?", "Attachment of ribosomes on its outer surface", ["Presence of cristae", "Lipid droplets", "Cellulose fibers"]),
            ("What is the primary function of Smooth Endoplasmic Reticulum (SER) in eukaryotic cells?", "Synthesis of lipids, steroids, and detoxification of drugs and poisons", ["Protein translation", "Photosynthesis", "Digestion of foreign antigens"]),
            ("Endoplasmic reticulum forms an interconnected network of branching tubules and cisternae serving primarily as:", "An internal transport system and structural framework for the cell", ["An optical reflecting layer", "A rigid skeleton like bone", "A water storage reservoir"]),
            ("Proteins synthesized on the ribosomes of RER are packaged and primarily transferred next to which organelle for modification?", "Golgi complex", ["Chloroplast", "Nucleolus", "Centrosome"])
        ],
        "MH-8-SCI-10-10.3.1": [
            ("Which scientist first observed and described the organelle composed of flat membrane-bound parallel sacs (cisternae) in 1898?", "Camillo Golgi", ["Robert Hooke", "Antonie van Leeuwenhoek", "Robert Brown"]),
            ("What is the chief physiological role of the Golgi apparatus in a secretory eukaryotic cell?", "Modifying, packaging, and sorting glycoproteins and enzymes into secretory vesicles", ["Generating cellular ATP", "Synthesizing ribosomal RNA", "Digesting cellular waste"]),
            ("The flat, parallel, curved membrane-bound cisternae of Golgi complex have two distinct functional faces called:", "Cis face (forming) and Trans face (maturing)", ["Anode and Cathode", "Prophase and Metaphase", "Active and Passive"]),
            ("Which organelle is formed by the cooperative packaging of hydrolytic enzymes by the Golgi complex and ER?", "Lysosome", ["Mitochondrion", "Ribosome", "Chloroplast"])
        ],
        "MH-8-SCI-10-10.3.2": [
            ("Why are lysosomes commonly referred to as 'suicide bags' (demolition squads) of the cell?", "During cellular damage or starvation, they burst and their hydrolytic enzymes digest the cell itself (autolysis)", ["They absorb sunlight to generate heat", "They release poison into the bloodstream", "They eject the nucleus out of the cell"]),
            ("Lysosomes contain approximately 40 to 50 types of powerful digestive enzymes that operate optimally at:", "Acidic pH (around 4.5 to 5.0)", ["Alkaline pH (around 9.0)", "Neutral pH (7.0)", "Boiling temperature"]),
            ("Which cellular function is executed by lysosomes when defending the cell against invading bacteria and viruses?", "Phagocytic breakdown and destruction of pathogens", ["Replication of viral RNA", "Photosynthetic fixation", "Neutralization with ammonia"]),
            ("In which human cell type are lysosomes exceptionally abundant to digest debris and engulf pathogens?", "White Blood Cells (phagocytic leukocytes / macrophages)", ["Mature RBCs", "Bone osteocytes", "Hair cuticle cells"])
        ],
        "MH-8-SCI-10-10.4.1": [
            ("Why are mitochondria called the 'powerhouses of the cell'?", "They synthesize ATP (adenosine triphosphate) through oxidative phosphorylation during aerobic respiration", ["They store electrical charges like batteries", "They pump blood across tissues", "They absorb solar energy directly"]),
            ("The inner membrane of a mitochondrion is deeply folded into numerous finger-like projections called:", "Cristae", ["Cisternae", "Thylakoids", "Grana"]),
            ("Mitochondria are considered semi-autonomous organelles because they possess their own:", "Circular DNA and 70S ribosomes to synthesize some of their own proteins", ["Cell wall and nucleus", "Chlorophyll pigments", "Cellular vacuoles"]),
            ("How many membranes surround a mitochondrion, and how do they differ?", "Two: outer smooth permeable membrane and inner folded selectively permeable membrane", ["Single porous membrane", "Three rigid chitin membranes", "No membrane at all"])
        ],
        "MH-8-SCI-10-10.4.2": [
            ("Which type of plastids contain chlorophyll and carotenoids, making them the site of photosynthesis in plants?", "Chloroplasts", ["Leucoplasts", "Chromoplasts", "Amyloplasts"]),
            ("Plastids that give vivid red, orange, and yellow colors to flowers and ripening fruits due to carotene and xanthophyll are:", "Chromoplasts", ["Chloroplasts", "Leucoplasts", "Lysosomes"]),
            ("Colorless plastids called leucoplasts function primarily in plant cells to store:", "Starch (carbohydrates), oils, and proteins", ["Carbon dioxide gas", "Digestive hydrolytic enzymes", "Chlorophyll pigments"]),
            ("Inside a chloroplast, stacks of disc-shaped thylakoids containing chlorophyll are called:", "Grana (singular: granum)", ["Cristae", "Cisternae", "Centrioles"])
        ],
        "MH-8-SCI-10-10.5.1": [
            ("In plant cells, the large central vacuole is bounded by a single semi-permeable membrane called the:", "Tonoplast", ["Crista", "Pericardium", "Capsule"]),
            ("How does the central vacuole of a mature plant cell differ in size and proportion compared to animal cells?", "Plant cells have a single giant central vacuole occupying 50% to 90% of cell volume, while animal cells have small temporary vacuoles", ["Plant cells lack vacuoles entirely", "Animal vacuoles are 10 times larger", "Both plant and animal cells have identical vacuoles"]),
            ("The liquid contents present within the plant cell vacuole consisting of water, sugars, salts, and pigments is termed:", "Cell sap", ["Cytosol", "Blood plasma", "Matrix"]),
            ("Which organelle provides mechanical turgidity and rigidity to plant leaves and stems through internal fluid pressure?", "Large central vacuole", ["Ribosome", "Centrosome", "Smooth ER"])
        ],
        "MH-8-SCI-10-10.5.2": [
            ("What primary role does the central vacuole perform in plant cells regarding waste metabolites?", "Stores toxic metabolic by-products and excretory crystals to isolate them from cytoplasm", ["Transcribes messenger RNA", "Oxidizes glucose to CO2", "Duplicates chromosomes"]),
            ("In single-celled freshwater organisms like Amoeba, which specialized vacuole regulates osmoregulation by expelling excess water?", "Contractile vacuole", ["Food vacuole", "Gas vacuole", "Sap vacuole"]),
            ("When a plant wilts due to prolonged lack of water, which vacuolar property has diminished?", "Turgor pressure of cell sap", ["Nuclear DNA concentration", "Chloroplast number", "Enzyme concentration"]),
            ("In Amoeba and Paramecium, nutrient digestion takes place inside temporary digestive vesicles called:", "Food vacuoles", ["Contractile vacuoles", "Tonoplasts", "Centrioles"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 11 DATA
    # -------------------------------------------------------------------------
    ch11_cases = {
        "MH-8-SCI-11-11.1.1": [
            ("Air entering the nasal cavity is warmed, humidified, and cleaned of dust particles primarily by:", "Mucus layer and fine ciliated epithelial hairs", ["Vocal cords", "Cartilaginous rings", "Alveolar capillaries"]),
            ("Which cartilage structure covers the glottis during swallowing to prevent food from entering the trachea?", "Epiglottis", ["Thyroid cartilage", "Pericardium", "Pleura"]),
            ("The voice box containing the vocal cords which vibrate to produce vocal sound is anatomically called the:", "Larynx", ["Pharynx", "Trachea", "Bronchus"]),
            ("Why is the human trachea (windpipe) supported by C-shaped rings of hyaline cartilage?", "To prevent the windpipe from collapsing when air pressure drops during inhalation", ["To produce digestive juices", "To generate blood cells", "To filter red blood cells"])
        ],
        "MH-8-SCI-11-11.1.2": [
            ("During inhalation (inspiration), what happens to the diaphragm and rib cage?", "Diaphragm contracts and flattens, ribs move upward and outward, increasing thoracic volume", ["Diaphragm relaxes and arches upward, ribs move down", "Both diaphragm and ribs remain immobile", "Thoracic cavity volume decreases drastically"]),
            ("During normal exhalation (expiration), what change occurs in intra-thoracic air pressure?", "Pressure inside lungs rises above atmospheric pressure, pushing air out passively", ["Pressure inside lungs becomes a vacuum", "Diaphragm contracts violently", "Alveoli expand to double their size"]),
            ("Which muscle group contracts simultaneously with the diaphragm to pull ribs upward during deep breathing?", "External intercostal muscles", ["Cardiac muscles", "Smooth visceral muscles", "Deltoid muscles"]),
            ("The normal resting breathing rate of a healthy adult human is approximately:", "12 to 18 breaths per minute", ["40 to 60 breaths per minute", "2 to 4 breaths per minute", "80 to 100 breaths per minute"])
        ],
        "MH-8-SCI-11-11.2.1": [
            ("Gas exchange in human lungs occurs across the microscopic, balloon-like air sacs known as:", "Alveoli", ["Bronchioles", "Tracheal rings", "Pleura"]),
            ("By which physical process do oxygen and carbon dioxide move between alveolar air and capillary blood?", "Simple diffusion driven by concentration (partial pressure) gradients", ["Active pumping requiring ATP", "Endocytosis", "Facilitated filtration"]),
            ("What structural feature of alveolar walls makes them exceptionally suited for rapid diffusion of gases?", "Extremely thin walls (single squamous epithelial layer) surrounded by a dense network of capillaries", ["Thick muscular cartilage", "Waxy impermeable cuticle", "Dry epithelial surface"]),
            ("Roughly how many millions of alveoli are estimated to be present in both adult human lungs combined?", "Approximately 300 to 500 million alveoli", ["Only about 500", "About 10,000", "Over 50 billion"])
        ],
        "MH-8-SCI-11-11.2.2": [
            ("What is cellular respiration fundamentally defined as in human physiology?", "The biochemical oxidation of glucose inside mitochondria using oxygen to produce ATP, CO2, and water", ["The mechanical inhalation of ambient air", "The pumping of blood by the heart", "The transport of bile to the intestine"]),
            ("Which chemical equation correctly summarizes complete aerobic cellular respiration?", "\\(\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{ATP (energy)}\\)", ["\\(6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\rightarrow \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2\\)", "\\(\\text{C}_6\\text{H}_{12}\\text{O}_6 \\rightarrow 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2\\)", "\\(\\text{CO}_2 + \\text{O}_2 \\rightarrow \\text{Energy}\\)"]),
            ("Approximately how many net ATP molecules are produced from complete oxidation of one mole of glucose in aerobic respiration?", "36 to 38 ATP molecules", ["2 ATP molecules", "1000 ATP molecules", "Zero ATP"]),
            ("When skeletal muscle cells undergo intense exercise with insufficient oxygen supply, glucose is partially converted to:", "Lactic acid, causing muscle fatigue and cramps", ["Carbon monoxide", "Pure urea", "Ethanol and sulfur"])
        ],
        "MH-8-SCI-11-11.3.1": [
            ("How many internal muscular chambers does the human heart have?", "Four chambers (two superior atria and two inferior ventricles)", ["Two chambers", "Three chambers", "Six chambers"]),
            ("Which chamber of the heart receives deoxygenated blood returning from the upper and lower vena cava?", "Right atrium", ["Left atrium", "Left ventricle", "Right ventricle"]),
            ("Which heart chamber has the thickest, strongest muscular wall to pump oxygenated blood into the systemic aorta?", "Left ventricle", ["Right atrium", "Right ventricle", "Left atrium"]),
            ("The muscular dividing wall that separates the right and left sides of the heart to prevent mixing of blood is the:", "Septum", ["Pericardium", "Valve", "Aorta"])
        ],
        "MH-8-SCI-11-11.3.2": [
            ("The human heart is protected externally by a tough, double-walled sac known as the:", "Pericardium", ["Pleura", "Peritoneum", "Meninges"]),
            ("What is the function of the pericardial fluid present between the pericardial membranes?", "Reduces friction between the beating heart and surrounding organs and cushions against mechanical shock", ["Supplies glucose to the lungs", "Filters deoxygenated blood", "Generates the electrical heartbeat"]),
            ("The valve located between the right atrium and the right ventricle possessing three fibrous flaps is the:", "Tricuspid valve", ["Bicuspid (mitral) valve", "Aortic semilunar valve", "Pulmonary valve"]),
            ("The bicuspid (mitral) valve regulates unidirectional blood flow between which two heart chambers?", "Left atrium and left ventricle", ["Right atrium and right ventricle", "Left ventricle and aorta", "Right ventricle and pulmonary artery"])
        ],
        "MH-8-SCI-11-11.3.3": [
            ("The rhythmic contraction phase of the heart chambers when blood is pumped out is called:", "Systole", ["Diastole", "Peristalsis", "Osmosis"]),
            ("The rhythmic relaxation and filling phase of the heart chambers between contractions is called:", "Diastole", ["Systole", "Fibrillation", "Tetanus"]),
            ("The two characteristic audible heart sounds ('lub' and 'dub') heard through a stethoscope are produced by:", "The closure of atrioventricular valves ('lub') followed by the closure of semilunar valves ('dub')", ["Blood rushing through the aorta", "The expansion of the pericardium", "The rubbing of lungs against ribs"]),
            ("In a normal adult at rest, the average heartbeat rate is approximately:", "70 to 72 beats per minute", ["120 to 140 beats per minute", "30 to 40 beats per minute", "15 to 20 beats per minute"])
        ],
        "MH-8-SCI-11-11.4.1": [
            ("Why do systemic arteries have thick, elastic, muscular walls compared to veins?", "To withstand high hydrostatic pressure exerted by blood pumped directly from the ventricles", ["To allow gases to diffuse through them directly", "To store waste metabolites", "Because they have internal valves"]),
            ("Which major artery is the only artery in the adult human body that carries deoxygenated blood?", "Pulmonary artery (carrying blood from right ventricle to lungs)", ["Aorta", "Carotid artery", "Renal artery"]),
            ("Why are internal valves ABSENT in normal human systemic arteries?", "Blood flows forward continuously under high pressure created by heart ventricular contractions", ["Arteries are too narrow for valves", "Valves only exist in lymphatic ducts", "Gravity pulls arterial blood up"]),
            ("The largest systemic artery emerging directly from the left ventricle to distribute oxygenated blood to the body is the:", "Aorta", ["Vena cava", "Pulmonary vein", "Femoral vein"])
        ],
        "MH-8-SCI-11-11.4.2": [
            ("What structural feature inside veins prevents the backward flow of slow-moving, low-pressure blood?", "Semilunar flap valves", ["Thick muscular sphincters", "Cilia", "Chitinous ridges"]),
            ("Which veins are the only veins in the human body that carry oxygenated blood?", "Pulmonary veins (carrying oxygenated blood from lungs to left atrium)", ["Superior vena cava", "Inferior vena cava", "Hepatic portal vein"]),
            ("Why are veins located more superficially (closer to the skin surface) than arteries?", "Arteries carry blood under high pressure and are buried deep to prevent catastrophic hemorrhage", ["Veins need sunlight to absorb vitamin D", "Veins absorb oxygen directly through skin", "Arteries have thinner walls"]),
            ("Deoxygenated blood from the upper head, neck, and chest regions drains into the right atrium via the:", "Superior vena cava", ["Inferior vena cava", "Pulmonary trunk", "Coronary sinus"])
        ],
        "MH-8-SCI-11-11.4.3": [
            ("Capillaries have microscopic walls composed of only a single layer of cells termed:", "Endothelium (squamous epithelial cells)", ["Stratified keratin", "Cardiac muscle", "Hyaline cartilage"]),
            ("What is the primary physiological function of capillary networks in body tissues?", "Facilitating diffusion and exchange of nutrients, oxygen, hormones, and metabolic wastes with cells", ["Storing reserves of whole blood", "Generating arterial blood pressure", "Neutralizing bacterial endotoxins"]),
            ("The diameter of a typical blood capillary is approximately \\(7\\text{ to }8\\ \\mu\\text{m}\\), which means:", "RBCs must squeeze through single file in narrow capillaries", ["White blood cells cannot enter tissues", "Capillaries can store large volumes of blood", "Blood flow velocity is highest in capillaries"]),
            ("Fluid that filters out of capillary walls into surrounding intercellular spaces to bathe cells is called:", "Tissue fluid (interstitial fluid / lymph)", ["Blood plasma", "Cytosol", "Synovial fluid"])
        ],
        "MH-8-SCI-11-11.5.1": [
            ("Whole blood is composed of what percentage of fluid plasma and formed cellular elements?", "55% plasma and 45% formed elements (blood cells)", ["90% plasma and 10% cells", "50% plasma and 50% cells", "30% plasma and 70% cells"]),
            ("Which iron-containing conjugated protein inside Red Blood Cells (erythrocytes) binds reversibly to oxygen?", "Hemoglobin", ["Myoglobin", "Albumin", "Fibrinogen"]),
            ("Why do mature mammalian Red Blood Cells (RBCs) lack a nucleus and mitochondria?", "To maximize internal cytoplasmic volume for packing maximum hemoglobin molecules", ["Because they are dead cells", "To divide faster in circulation", "Because they have no cell membrane"]),
            ("Which cellular fragments derived from megakaryocytes are essential for blood coagulation (clotting) at wound sites?", "Blood platelets (thrombocytes)", ["Leukocytes", "Erythrocytes", "Lymphocytes"])
        ],
        "MH-8-SCI-11-11.5.2": [
            ("Who discovered the human ABO blood group system in 1900 and received the Nobel Prize in 1930?", "Karl Landsteiner", ["Louis Pasteur", "Alexander Fleming", "Edward Jenner"]),
            ("Which blood group is designated as the 'Universal Blood Donor' because its red blood cells lack both A and B antigens?", "Group O negative (\\(\\text{O}^-\\))", ["Group AB positive (\\(\\text{AB}^+\\))", "Group A positive", "Group B negative"]),
            ("Why is an individual with blood group AB positive (\\(\\text{AB}^+\\)) considered the 'Universal Recipient'?", "Their plasma lacks anti-A, anti-B, and anti-Rh antibodies, so transfused RBCs are not agglutinated", ["Their blood contains no red blood cells", "They cannot catch infectious diseases", "They have double the normal volume of blood"]),
            ("What dangerous immunological reaction occurs when incompatible blood is transfused into a recipient?", "Agglutination (clumping of donor RBCs by recipient antibodies) leading to hemolysis and kidney failure", ["Instant transformation of blood into plasma", "Hyper-speed oxygen delivery", "Benign dilution of plasma"])
        ],
        "MH-8-SCI-11-11.5.3": [
            ("The medical instrument used to measure human arterial blood pressure is called a:", "Sphygmomanometer", ["Stethoscope", "Spirometer", "Electrocardiograph (ECG)"]),
            ("In a normal, healthy resting adult human, standard blood pressure reading is approximately:", "\\(120/80\\ \\text{mm Hg}\\) (Systolic 120, Diastolic 80)", ["\\(180/120\\ \\text{mm Hg}\\)", "\\(80/120\\ \\text{mm Hg}\\)", "\\(200/50\\ \\text{mm Hg}\\)"]),
            ("Persistently elevated blood pressure above \\(140/90\\ \\text{mm Hg}\\) is clinically diagnosed as:", "Hypertension (high blood pressure)", ["Hypotension", "Anemia", "Arteriosclerosis"]),
            ("The listening instrument used by doctors to hear heartbeat valves opening and closing is called a:", "Stethoscope", ["Sphygmomanometer", "Thermometer", "Otoscope"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 12 DATA
    # -------------------------------------------------------------------------
    ch12_cases = {
        "MH-8-SCI-12-12.1.1": [
            ("According to Arrhenius theory, an acid is a chemical substance that produces which ion when dissolved in water?", "Hydrogen ions (\\(\\text{H}^+\\) or hydronium \\(\\text{H}_3\\text{O}^+\\))", ["Hydroxide ions (\\(\\text{OH}^-\\))", "Sodium ions (\\(\\text{Na}^+\\))", "Chloride ions (\\(\\text{Cl}^-\\))"]),
            ("What is the characteristic taste shared by acidic substances like lemons, vinegar, and tamarind?", "Sour taste", ["Bitter taste", "Sweet taste", "Salty taste"]),
            ("When an acid reacts with active metals like zinc or magnesium, which gas is evolved with effervescence?", "Hydrogen gas (\\(\\text{H}_2\\))", ["Oxygen gas", "Carbon dioxide gas", "Nitrogen gas"]),
            ("What effect does an aqueous acid solution have on blue litmus paper?", "Turns blue litmus red", ["Turns red litmus blue", "Turns litmus green", "No color change"])
        ],
        "MH-8-SCI-12-12.1.2": [
            ("Which organic acid is naturally present in lemons, oranges, and other citrus fruits?", "Citric acid", ["Acetic acid", "Lactic acid", "Tartaric acid"]),
            ("Vinegar commonly used in cooking and food preservation is a 5% to 8% aqueous solution of:", "Acetic acid (ethanoic acid, \\(\\text{CH}_3\\text{COOH}\\))", ["Sulfuric acid", "Hydrochloric acid", "Nitric acid"]),
            ("Which acid is formed naturally when milk turns sour and ferments into yogurt or curd?", "Lactic acid", ["Citric acid", "Oxalic acid", "Formic acid"]),
            ("Which organic acid is abundantly found in tamarind, unripe mangoes, and grapes?", "Tartaric acid", ["Ascorbic acid", "Acetic acid", "Formic acid"])
        ],
        "MH-8-SCI-12-12.1.3": [
            ("Which mineral acid is known commercially as the 'King of Chemicals' due to its vast industrial applications?", "Sulfuric acid (\\(\\text{H}_2\\text{SO}_4\\))", ["Hydrochloric acid (\\(\\text{HCl}\\))", "Nitric acid (\\(\\text{HNO}_3\\))", "Carbonic acid"]),
            ("What is the strictly prescribed safety rule when diluting a concentrated mineral acid with water in a laboratory?", "Always add concentrated acid slowly to water with continuous stirring, NEVER water to acid", ["Pour water rapidly into the acid container", "Heat the acid to boiling before adding water", "Mix equal volumes instantly in an open beaker"]),
            ("Why is pouring water into concentrated sulfuric acid extremely hazardous?", "The hydration reaction is violently exothermic, causing sudden localized boiling that splatters acid dangerously", ["The acid turns into non-reactive gas", "It freezes the glass beaker", "It neutralizes without warning"]),
            ("Which mineral acid is present naturally in the human gastric stomach juice to digest proteins and kill bacteria?", "Hydrochloric acid (\\(\\text{HCl}\\))", ["Sulfuric acid", "Phosphoric acid", "Boric acid"])
        ],
        "MH-8-SCI-12-12.2.1": [
            ("According to Arrhenius theory, a base is a chemical compound that dissociates in aqueous solution to yield:", "Hydroxide ions (\\(\\text{OH}^-\\))", ["Hydrogen ions (\\(\\text{H}^+\\))", "Hydronium ions (\\(\\text{H}_3\\text{O}^+\\))", "Oxide ions (\\(\\text{O}^{2-}\\))"]),
            ("What are the two tactile and gustatory properties characteristic of basic (alkaline) substances?", "Bitter taste and slippery (soapy) touch", ["Sour taste and rough touch", "Sweet taste and gritty touch", "Tasteless and oily touch"]),
            ("A water-soluble base is specifically termed an:", "Alkali", ["Acid", "Indicator", "Ester"]),
            ("What color change occurs when red litmus paper is dipped into an alkaline (basic) solution?", "Red litmus turns blue", ["Blue litmus turns red", "Red litmus turns yellow", "No change"])
        ],
        "MH-8-SCI-12-12.2.2": [
            ("What is the common chemical name and formula of caustic soda used in manufacturing hard soaps and paper?", "Sodium hydroxide (\\(\\text{NaOH}\\))", ["Calcium hydroxide", "Ammonium hydroxide", "Sodium chloride"]),
            ("Slaked lime used for whitewashing walls and neutralizing acidic soil has the chemical formula:", "Calcium hydroxide, \\(\\text{Ca(OH)}_2\\)", ["Calcium carbonate, \\(\\text{CaCO}_3\\)", "Calcium oxide, \\(\\text{CaO}\\)", "Calcium sulfate, \\(\\text{CaSO}_4\\)"]),
            ("Which mild base is commonly marketed as 'Milk of Magnesia' and used as an antacid medicine?", "Magnesium hydroxide, \\(\\text{Mg(OH)}_2\\)", ["Sodium hydroxide", "Potassium hydroxide", "Sulfuric acid"]),
            ("Potassium hydroxide (\\(\\text{KOH}\\)), also known as caustic potash, is primarily used in the preparation of:", "Soft soaps, shampoos, and alkaline storage batteries", ["Whitewash paint", "Cement mortar", "Glass etching acids"])
        ],
        "MH-8-SCI-12-12.3.1": [
            ("Litmus indicator is a natural plant dye chemically extracted from which symbiotic organism?", "Lichens (symbiosis of algae and fungi)", ["Mosses", "Ferns", "Hibiscus petals"]),
            ("When a yellow turmeric stain on a white shirt is washed with laundry detergent (basic soap), what color does it turn?", "Reddish-brown (or red)", ["Bright blue", "Colorless", "Deep green"]),
            ("Turmeric paper stays yellow in acidic or neutral solutions, but in an alkaline solution it turns:", "Reddish-brown", ["White", "Black", "Pink"]),
            ("Extract of red cabbage leaves acts as a natural indicator; what color does it exhibit in strongly basic solutions?", "Green or yellow", ["Bright red", "Purple", "Colorless"])
        ],
        "MH-8-SCI-12-12.3.2": [
            ("What is the color of synthetic indicator phenolphthalein in an acidic medium and in a basic medium, respectively?", "Colorless in acid, deep pink (magenta) in base", ["Yellow in acid, blue in base", "Pink in acid, colorless in base", "Red in acid, green in base"]),
            ("What color changes are exhibited by synthetic indicator methyl orange in acidic and basic solutions, respectively?", "Red (or pink) in acid, yellow in base", ["Blue in acid, red in base", "Colorless in acid, orange in base", "Green in acid, blue in base"]),
            ("An unknown liquid turns phenolphthalein deep pink. What is the chemical nature of this liquid?", "Basic (alkaline)", ["Acidic", "Neutral water", "Mineral acid"]),
            ("A universal indicator is preferred over simple litmus because it:", "Provides a continuous spectrum of colors indicating the precise pH value (0 to 14) of a solution", ["Only reacts with strong acids", "Is completely edible", "Cannot measure neutral solutions"])
        ],
        "MH-8-SCI-12-12.4.1": [
            ("What is the general chemical equation representing a neutralization reaction?", "\\(\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water}\\)", ["\\(\\text{Acid} + \\text{Metal} \\rightarrow \\text{Salt} + \\text{Hydrogen}\\)", "\\(\\text{Base} + \\text{Non-metal} \\rightarrow \\text{Oxide}\\)", "\\(\\text{Salt} + \\text{Water} \\rightarrow \\text{Acid}\\)"]),
            ("When hydrochloric acid (\\(\\text{HCl}\\)) reacts with sodium hydroxide (\\(\\text{NaOH}\\)), what products are formed?", "Sodium chloride (\\(\\text{NaCl}\\)) and water (\\(\\text{H}_2\\text{O}\\))", ["Sodium hydride and chlorine gas", "Sodium carbonate and hydrogen", "Sodium sulfate and water"]),
            ("Why is neutralization considered an exothermic process?", "Heat energy is released when \\(\\text{H}^+\\) and \\(\\text{OH}^-\\) ions combine to form stable covalent water molecules \\(\\text{H}_2\\text{O}\\)", ["It absorbs light from the room", "Temperature drops below zero", "It requires external boiling"]),
            ("What is the net ionic equation for any strong acid-strong base neutralization reaction in aqueous solution?", "\\(\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}\\)", ["\\(\\text{Na}^+ + \\text{Cl}^- \\rightarrow \\text{NaCl}\\)", "\\(2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}\\)", "\\(\\text{Ca}^{2+} + 2\\text{OH}^- \\rightarrow \\text{Ca(OH)}_2\\)"])
        ],
        "MH-8-SCI-12-12.4.2": [
            ("A person suffering from acidity in the stomach is treated with an antacid tablet containing:", "Mild bases like magnesium hydroxide or aluminium hydroxide", ["Dilute hydrochloric acid", "Strong caustic soda (NaOH)", "Concentrated vinegar"]),
            ("When agricultural soil becomes excessively acidic due to acid rain or chemical fertilizers, farmers neutralize it by adding:", "Quicklime (\\(\\text{CaO}\\)) or slaked lime (\\(\\text{Ca(OH)}_2\\))", ["Sulfuric acid", "Urea crystals", "Sodium chloride"]),
            ("The painful burning sting of an ant or bee contains formic acid (methanoic acid). It is best soothed by applying:", "Mild baking soda (sodium hydrogen carbonate) paste or calamine lotion (zinc carbonate)", ["Lemon juice", "Concentrated nitric acid", "Vinegar"]),
            ("Industrial factory wastes containing acidic chemicals must be neutralized with slaked lime before discharge into rivers to:", "Prevent acidification of aquatic habitats and protect aquatic life", ["Increase fish salinity", "Evaporate the river water", "Make river water fizzy"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 13 DATA
    # -------------------------------------------------------------------------
    ch13_cases = {
        "MH-8-SCI-13-13.1.1": [
            ("How does a chemical change fundamentally differ from a physical change?", "A chemical change forms entirely new substances with different chemical properties and is usually irreversible", ["A chemical change only alters shape and size temporarily", "A chemical change is always easily reversible by physical cooling", "A chemical change does not involve energy changes"]),
            ("Which of the following common phenomena represents a physical change rather than a chemical change?", "Melting of ice into liquid water", ["Rusting of iron nails", "Ripening of a banana", "Burning of LPG cooking gas"]),
            ("Why is the boiling of water to form steam considered a reversible physical change?", "No new chemical substance is formed; steam can be condensed back into liquid water with identical chemical composition", ["The chemical bonds in H2O break into hydrogen and oxygen gas", "Water molecules disappear completely", "New elements are generated"]),
            ("Which of the following processes is an irreversible chemical change?", "Baking a cake from flour, sugar, and eggs", ["Dissolving sugar in water", "Freezing juice into an ice lolly", "Tearing a sheet of paper into small pieces"])
        ],
        "MH-8-SCI-13-13.1.2": [
            ("When clear limewater turns milky upon bubbling a colorless gas through it, what chemical reaction is demonstrated?", "Carbon dioxide reacts with calcium hydroxide to form insoluble white calcium carbonate precipitate", ["Oxygen burns calcium into ash", "Nitrogen dissolves calcium into ions", "Hydrogen gas evaporates the water"]),
            ("Which observation provides definitive proof that a chemical change has taken place?", "Permanent change in color, evolution of gas with effervescence, temperature change, or formation of an insoluble precipitate", ["Temporary change in state upon heating", "Change in position of the object", "Reflection of light from surface"]),
            ("When a copper sulphate solution reacts with an iron nail, what observable color change takes place?", "Blue copper sulphate solution turns green (ferrous sulphate) and reddish copper deposits on nail", ["Blue solution turns bright purple", "No color change occurs", "Solution evaporates instantly"]),
            ("When barium chloride solution is mixed with sodium sulphate solution, what immediate visual evidence of chemical change occurs?", "Formation of a dense white insoluble precipitate of barium sulphate (\\(\\text{BaSO}_4\\))", ["Rapid boiling and red flames", "The liquid turns into pure gas", "No visible reaction"])
        ],
        "MH-8-SCI-13-13.2.1": [
            ("Which natural biochemical reaction in green leaves converts light energy into chemical energy stored in glucose?", "Photosynthesis", ["Transpiration", "Fermentation", "Decomposition"]),
            ("What are the primary reactants required by green plants to carry out photosynthesis?", "Carbon dioxide (\\(\\text{CO}_2\\)), water (\\(\\text{H}_2\\text{O}\\)), sunlight, and chlorophyll", ["Oxygen, glucose, and soil minerals", "Nitrogen, carbon monoxide, and ozone", "Methane and hydrogen peroxide"]),
            ("The balanced chemical equation representing natural photosynthesis in green plants is:", "\\(6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\xrightarrow{\\text{Light, Chlorophyll}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2\\)", ["\\(\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O}\\)", "\\(2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}\\)", "\\(\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{CO}_3\\)"]),
            ("Which life-sustaining gas is released into the Earth's atmosphere as a by-product of photosynthesis?", "Oxygen gas (\\(\\text{O}_2\\))", ["Carbon dioxide", "Carbon monoxide", "Sulfur dioxide"])
        ],
        "MH-8-SCI-13-13.2.2": [
            ("What is the primary biological purpose of cellular respiration in living organisms?", "Releasing metabolic energy in the form of ATP by breaking down glucose", ["Absorbing sunlight to build cellulose", "Filtering toxins from blood", "Synthesizing inorganic mineral salts"]),
            ("Which two chemical substances are the vital reactants consumed during aerobic cellular respiration?", "Glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)) and Oxygen (\\(\\text{O}_2\\))", ["Carbon dioxide and water", "Nitrogen and methane", "Starch and carbon monoxide"]),
            ("The chemical reaction of cellular respiration is classified as:", "An exothermic chemical change", ["An endothermic physical change", "A reversible physical change", "A photochemical displacement"]),
            ("How does the chemical equation of aerobic respiration relate to the equation of photosynthesis?", "It is exactly the reverse chemical reaction of photosynthesis", ["It is completely identical to photosynthesis", "It produces solid carbon without energy", "It does not involve oxygen or glucose"])
        ],
        "MH-8-SCI-13-13.2.3": [
            ("What are the two essential environmental factors required for the rusting of iron?", "Presence of both moisture (water) and oxygen (air)", ["Only pure dry oxygen", "Only boiling water free of oxygen", "Sub-zero temperatures"]),
            ("What is the chemical composition and formula of rust formed on iron surfaces?", "Hydrated ferric oxide, \\(\\text{Fe}_2\\text{O}_3 \\cdot x\\text{H}_2\\text{O}\\)", ["Ferrous chloride, \\(\\text{FeCl}_2\\)", "Pure iron sulfide, \\(\\text{FeS}\\)", "Iron carbonate, \\(\\text{FeCO}_3\\)"]),
            ("The rusting of iron is chemically classified as which type of reaction?", "Slow oxidation and corrosion reaction", ["Fast displacement reaction", "Neutralization reaction", "Thermal decomposition"]),
            ("Which industrial method prevents the rusting of iron by coating it with a thin layer of molten zinc metal?", "Galvanization", ["Vulcanization", "Polymerization", "Electrolysis"])
        ],
        "MH-8-SCI-13-13.3.1": [
            ("What is combustion chemically defined as in science?", "A rapid exothermic chemical reaction between a fuel and oxygen that releases heat and light energy", ["A slow endothermic change absorbing heat", "A reversible physical melting of solids", "A radioactive decay process"]),
            ("What are the primary chemical products formed during complete combustion of hydrocarbon fuels like methane (\\(\\text{CH}_4\\))?", "Carbon dioxide (\\(\\text{CO}_2\\)) and water vapor (\\(\\text{H}_2\\text{O}\\))", ["Carbon monoxide and soot", "Hydrogen gas and carbon", "Sulfur dioxide and oxygen"]),
            ("Incomplete combustion of cooking fuels in limited air supply is hazardous because it produces which toxic, colorless gas?", "Carbon monoxide (\\(\\text{CO}\\))", ["Carbon dioxide (\\(\\text{CO}_2\\))", "Ozone (\\(\\text{O}_3\\))", "Nitrogen gas (\\(\\text{N}_2\\))"]),
            ("Which chemical reaction represents the complete combustion of methane (natural gas)?", "\\(\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O} + \\text{Heat}\\)", ["\\(\\text{CH}_4 + \\text{O}_2 \\rightarrow \\text{C} + 2\\text{H}_2\\text{O}\\)", "\\(2\\text{CH}_4 + 3\\text{O}_2 \\rightarrow 2\\text{CO} + 4\\text{H}_2\\text{O}\\)", "\\(\\text{CH}_4 \\rightarrow \\text{C} + 2\\text{H}_2\\)"])
        ],
        "MH-8-SCI-13-13.3.2": [
            ("Why does effervescence (bubbling) occur when dilute hydrochloric acid is used to clean ceramic bathroom tiles coated with hard water scale?", "Hydrochloric acid reacts with insoluble calcium carbonate scales to evolve carbon dioxide gas (\\(\\text{CO}_2\\))", ["Acid melts the porcelain tile instantly", "Water boils due to nuclear heat", "Hydrogen gas explodes continuously"]),
            ("What is the chemical equation for cleaning calcium carbonate tile stains with hydrochloric acid?", "\\(\\text{CaCO}_3 + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\)", ["\\(\\text{CaCO}_3 + \\text{HCl} \\rightarrow \\text{CaCl} + \\text{CO}_3\\)", "\\(\\text{Ca} + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\)", "\\(\\text{CaO} + \\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O}\\)"]),
            ("Why should one avoid using strong concentrated hydrochloric acid frequently on marble flooring?", "Marble is composed of calcium carbonate, which chemically dissolves and corrodes upon reaction with acid", ["Marble catches fire instantly", "Marble becomes softer than rubber", "Marble changes into pure diamond"]),
            ("Which gas produced during tile cleaning with acid extinguishes a burning splint and turns limewater milky?", "Carbon dioxide (\\(\\text{CO}_2\\))", ["Hydrogen gas", "Oxygen gas", "Sulfur dioxide"])
        ],
        "MH-8-SCI-13-13.3.3": [
            ("Hardness in ground water is primarily caused by dissolved salts of which two divalent metal cations?", "Calcium (\\(\\text{Ca}^{2+}\\)) and Magnesium (\\(\\text{Mg}^{2+}\\))", ["Sodium and Potassium", "Iron and Lead", "Zinc and Copper"]),
            ("Which commercial chemical compound is added to hard water to soften it by precipitating calcium and magnesium ions?", "Washing soda (Sodium carbonate, \\(\\text{Na}_2\\text{CO}_3\\))", ["Baking soda (Sodium bicarbonate)", "Common salt (Sodium chloride)", "Caustic soda (Sodium hydroxide)"]),
            ("What chemical precipitate is formed when washing soda reacts with calcium chloride in hard water?", "Insoluble calcium carbonate (\\(\\text{CaCO}_3\\)) precipitate", ["Soluble sodium chloride", "Calcium hydroxide solution", "Magnesium metal"]),
            ("Why does ordinary laundry soap fail to form rich lather in hard water until water is softened?", "Soap reacts with calcium and magnesium ions forming an insoluble sticky curdy precipitate (scum)", ["Hard water dissolves the soap bar completely", "Soap evaporates in hard water", "Hard water neutralizes the perfume"])
        ],
        "MH-8-SCI-13-13.4.1": [
            ("An ionic (electrovalent) chemical bond is formed between two atoms by the:", "Complete transfer of one or more valence electrons from a metal atom to a non-metal atom", ["Mutual sharing of electron pairs", "Attraction between two positively charged ions", "Gravitational force between nuclei"]),
            ("When a neutral metal atom loses valence electrons to achieve stable octet configuration, it becomes a:", "Positively charged cation", ["Negatively charged anion", "Neutral isotope", "Positron"]),
            ("What strong fundamental force holds oppositely charged ions tightly together in an ionic crystal lattice?", "Electrostatic force of attraction", ["Weak Van der Waals force", "Nuclear strong force", "Magnetic repulsion"]),
            ("Which group of elements on the periodic table typically donate electrons to form ionic bonds with non-metals?", "Metals (Group 1 alkali metals and Group 2 alkaline earth metals)", ["Noble gases (Group 18)", "Halogens (Group 17)", "Chalcogens (Group 16)"])
        ],
        "MH-8-SCI-13-13.4.2": [
            ("During the formation of sodium chloride (\\(\\text{NaCl}\\)), which electron transfer event takes place?", "Sodium (2,8,1) donates 1 valence electron to chlorine (2,8,7), forming \\(\\text{Na}^+\\) and \\(\\text{Cl}^-\\)", ["Chlorine donates 1 electron to sodium", "Each atom shares 2 electrons equally", "Sodium receives 7 electrons from chlorine"]),
            ("In magnesium chloride (\\(\\text{MgCl}_2\\)), how many electrons are transferred from the magnesium atom to how many chlorine atoms?", "Magnesium donates 2 valence electrons (one to each of two chlorine atoms)", ["Magnesium donates 1 electron to one chlorine", "Magnesium receives 2 electrons from chlorine", "No electrons are transferred"]),
            ("Why do solid ionic compounds like \\(\\text{NaCl}\\) conduct electricity when molten or dissolved in water, but NOT in solid state?", "In solid state ions are locked tightly in lattice; when melted or in solution, ions become free to migrate", ["Solid ionic compounds have no electrons", "Water creates new electrons", "Solid ionic compounds contain only protons"]),
            ("Which of the following compounds is formed entirely through ionic bonding?", "Calcium oxide (\\(\\text{CaO}\\))", ["Methane (\\(\\text{CH}_4\\))", "Water (\\(\\text{H}_2\\text{O}\\))", "Carbon dioxide (\\(\\text{CO}_2\\))"])
        ],
        "MH-8-SCI-13-13.5.1": [
            ("A covalent bond is defined as a chemical bond formed by the:", "Mutual sharing of one or more pairs of electrons between two non-metallic atoms", ["Complete transfer of electrons from metal to non-metal", "Attraction between opposite magnetic poles", "Transfer of protons from one nucleus to another"]),
            ("How many shared pairs of electrons constitute a single covalent bond, double covalent bond, and triple covalent bond, respectively?", "1 pair (2 electrons), 2 pairs (4 electrons), and 3 pairs (6 electrons)", ["1, 2, and 3 electrons", "2, 4, and 8 pairs", "4, 6, and 8 electrons"]),
            ("Why do non-metallic atoms share electrons instead of transferring them when forming covalent bonds?", "Both non-metals have high electronegativity and high ionization enthalpy, making complete electron loss unfavorable", ["Non-metals have no valence electrons", "Non-metals have zero nuclear charge", "They want to form radioactive isotopes"]),
            ("General physical characteristics of covalent compounds include:", "Relatively low melting and boiling points, and poor electrical conductivity", ["Extremely high melting points and metallic luster", "High electrical conductivity in solid state", "Always solid at room temperature"])
        ],
        "MH-8-SCI-13-13.5.2": [
            ("How many electron pairs are shared between the two nitrogen atoms in a nitrogen molecule (\\(\\text{N}_2\\)) to achieve stable octet configuration?", "Three pairs of electrons (triple covalent bond, \\(\\text{N}\\equiv\\text{N}\\))", ["One pair of electrons", "Two pairs of electrons", "Four pairs of electrons"]),
            ("How many single covalent bonds are present in one molecule of methane (\\(\\text{CH}_4\\))?", "Four single covalent bonds (C-H)", ["One quadruple bond", "Two double bonds", "Three single bonds"]),
            ("In an oxygen molecule (\\(\\text{O}_2\\)), the two oxygen atoms achieve neon electron configuration (2,8) by forming a:", "Double covalent bond (\\(\\text{O}=\\text{O}\\))", ["Single covalent bond", "Triple covalent bond", "Ionic bond"]),
            ("In a molecule of water (\\(\\text{H}_2\\text{O}\\)), the central oxygen atom forms how many single covalent bonds with hydrogen atoms?", "Two single covalent bonds (O-H)", ["One double bond", "Three single bonds", "An ionic bond"])
        ]
    }

    # Generate each chapter
    for ch_num, cases_dict in [(10, ch10_cases), (11, ch11_cases), (12, ch12_cases), (13, ch13_cases)]:
        item = next(x for x in manifest if str(x["chapterNumber"]) == str(ch_num))
        ch_questions = []
        start_seq = 300
        for lf in item["leafs"]:
            tc = lf["topicCode"]
            needed = lf["needed"]
            sub_name = lf["name"]
            cases = cases_dict[tc]
            vaults, diffs = get_vaults_and_diffs(needed)

            for i in range(needed):
                ctx, ans, wrongs = cases[i % len(cases)]
                step1 = f"Identify the biological / chemical principle concerning {sub_name}."
                step2 = f"Apply standard scientific definitions: {ctx}"
                step3 = f"Therefore, the correct answer is {ans}."
                q = make_question(tc, sub_name, ctx, ans, wrongs, step1, step2, step3, diffs[i], vaults[i], start_seq)
                start_seq += 1
                ch_questions.append(q)

        out_path = f"scripts/mh8_sci_ch{ch_num}_topup.json"
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(ch_questions, out_f, indent=2)
        print(f"Generated {len(ch_questions)} questions for Chapter {ch_num} -> {out_path}")

if __name__ == "__main__":
    run()
