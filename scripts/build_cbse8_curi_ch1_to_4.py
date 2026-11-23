import json
import random
import os
from build_cbse8_curi_batch import make_question, get_vaults_and_diffs

random.seed(8821)

def run():
    with open("scripts/cbse8_curi_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 1 DATA
    # -------------------------------------------------------------------------
    ch1_cases = {
        "CBSE-8-CURI-1-1.1.1": [
            ("Why does a rolled dough puri puff up when dropped into hot cooking oil?", "Water trapped in the dough rapidly turns into steam, expanding and pushing the dough layers apart", ["Air is injected into the oil by bubbles", "The dough chemically decomposes into helium gas", "Oil penetrates the inner layer instantly"]),
            ("Why does a freshly sliced apple turn brown when left exposed to ambient air?", "Enzymatic browning caused by polyphenol oxidase reacting with atmospheric oxygen", ["The apple absorbs dust particles from the room", "Microscopic mold grows within 10 seconds", "Water evaporates leaving solid carbon"]),
            ("Morning dew drops seen glistening on spiderwebs and grass blades are formed due to:", "Condensation of atmospheric water vapor on cool surfaces during the night", ["Water oozing out from plant veins", "Microscopic morning rain showers", "Melting of underground frost"]),
            ("What scientific attitude is sparked by observing everyday phenomena like curd formation or shadows changing length?", "Curiosity and the drive for scientific inquiry", ["Blind faith in myths", "Passive acceptance without thinking", "Disregard for observation"])
        ],
        "CBSE-8-CURI-1-1.1.2": [
            ("What is the foundational spirit of scientific inquiry in science education?", "Asking 'Why?' and 'How?' about natural occurrences and seeking evidence-based explanations", ["Memorizing textbook definitions without experiments", "Accepting traditional opinions unquestioningly", "Guessing answers randomly"]),
            ("Which historical scientist formulated the universal law of gravitation after questioning why an apple falls straight to the ground?", "Sir Isaac Newton", ["Galileo Galilei", "Albert Einstein", "Michael Faraday"]),
            ("A student wonders why iron rusts in moist air but not in dry air. What is the first step of inquiry they should undertake?", "Formulate a testable hypothesis and design a controlled experiment with dry and moist test tubes", ["Paint the nail immediately", "Assume all metals rust equally", "Ignore the question"]),
            ("In scientific inquiry, what distinguishes a scientific question from a subjective opinion?", "A scientific question can be tested and verified through systematic observation and experiment", ["A scientific question is always voted on by a majority", "A scientific question cannot be measured", "A scientific question has no mathematical basis"])
        ],
        "CBSE-8-CURI-1-1.1.3": [
            ("Why is careful observation considered the primary starting point of all scientific investigations?", "It reveals repeatable patterns, anomalies, and relationships in the physical world that require explanation", ["It replaces the need for any experiment", "It proves theories without testing", "It guarantees instant mathematical formulas"]),
            ("What is the critical difference between a casual glance and an active scientific observation?", "Scientific observation is systematic, purposeful, recorded with precision, and often assisted by measuring tools", ["Scientific observation only occurs under sunlight", "Casual glances are always recorded in notebooks", "There is no difference"]),
            ("When observing the burning of a candle, which observation is qualitative rather than quantitative?", "The flame has a yellow luminous zone and a blue non-luminous base", ["The candle height decreases by \\(1.5\\ \\text{cm}\\) per hour", "The flame temperature measures \\(800^\\circ\\text{C}\\)", "The candle weighs \\(25\\ \\text{g}\\)"]),
            ("Which scientific instrument allowed biologists to observe microscopic cells for the very first time in history?", "The compound optical microscope", ["The telescope", "The barometer", "The magnetic compass"])
        ],
        "CBSE-8-CURI-1-1.2.1": [
            ("Which of the following is formulated as a focused, scientifically testable question?", "Does increasing the amount of fertilizer increase the growth rate of pea plants?", ["Are red flowers more beautiful than white flowers?", "Why is science the best subject?", "Do plants have dreams?"]),
            ("A testable scientific question must possess which essential characteristic?", "It specifies clear variables that can be measured or observed experimentally", ["It must be answerable by a simple personal belief", "It cannot be disproven by any evidence", "It must involve expensive equipment"]),
            ("What is a testable tentative explanation proposed to answer a scientific question called?", "A hypothesis", ["A scientific law", "An absolute fact", "A conclusion"]),
            ("If a student asks: 'Does the salinity of water affect the boiling point of water?', what makes this a testable question?", "Water salinity can be varied systematically and boiling point measured with a thermometer", ["It has never been studied before", "It requires space technology", "It has no independent variable"])
        ],
        "CBSE-8-CURI-1-1.2.2": [
            ("In an experiment testing how temperature affects the rate of sugar dissolving in water, what is the INDEPENDENT variable?", "The temperature of the water", ["The time taken for sugar to dissolve", "The type of sugar crystals", "The volume of water used"]),
            ("In the same dissolving experiment, what is the DEPENDENT variable?", "The time taken for the sugar to dissolve completely", ["The temperature set by the burner", "The brand of thermometer", "The size of the beaker"]),
            ("Why must CONTROLLED variables (like water volume, stirring speed, and sugar mass) be kept strictly constant in an experiment?", "To ensure that any observed change in the dependent variable is caused solely by the independent variable", ["To make the experiment finish faster", "To save laboratory chemicals", "To prevent water from heating up"]),
            ("A fair scientific test is defined as an experimental design where:", "Only one independent variable is changed at a time while all other conditions are kept constant", ["All variables are changed simultaneously", "No measurements are recorded", "The expected result is decided before starting"])
        ],
        "CBSE-8-CURI-1-1.2.3": [
            ("Why do scientists conduct multiple repeated trials when collecting experimental data?", "To minimize random measurement errors and ensure reliability and reproducibility of results", ["To use up remaining reagents", "To pass the time in the laboratory", "Because single measurements are illegal"]),
            ("When experimental evidence contradicts the initial hypothesis, what is the scientifically honest course of action?", "Re-evaluate the hypothesis in light of the evidence and modify or reject it", ["Alter the recorded data to match the hypothesis", "Discard the experiment and hide results", "Ignore the contradictory data points"]),
            ("A line graph plotting plant growth over 30 days is primarily useful in scientific data evaluation because:", "It visualizes trends, rates of change, and correlations that are difficult to see in raw tables", ["It proves the experiment was expensive", "It eliminates the need for units", "It replaces the conclusion"]),
            ("Drawing a valid scientific conclusion requires that:", "The conclusion is directly supported by empirical data collected during the investigation", ["The conclusion agrees with popular public opinion", "The conclusion is dramatic and unexpected", "The conclusion changes every week"])
        ],
        "CBSE-8-CURI-1-1.2.4": [
            ("Which standard SI units should be used when recording mass, length, volume, and temperature in science investigations?", "Kilograms (kg), metres (m), cubic metres or litres (L), and Kelvin or Celsius", ["Pounds, feet, gallons, and Fahrenheit", "Ounces, inches, pints, and degrees", "Grams, cubits, cups, and shades"]),
            ("Why is honest and transparent documentation of all experimental procedures and anomalous results vital in science?", "It enables other researchers worldwide to peer-review, replicate, and verify the findings independently", ["It guarantees a patent immediately", "It ensures high sales of products", "It prevents anyone else from doing the experiment"]),
            ("Which laboratory measuring tool provides the most precise measurement of the volume of a liquid?", "A graduated measuring cylinder or volumetric pipette", ["A wide-mouth beaker", "A conical flask", "A flat petri dish"]),
            ("What type of error occurs when a student reads a graduated cylinder's meniscus from an angle above or below eye level?", "Parallax error", ["Zero calibration error", "Systemic digital error", "Mass balance error"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 2 DATA
    # -------------------------------------------------------------------------
    ch2_cases = {
        "CBSE-8-CURI-2-2.1.1": [
            ("Why is the cell universally considered the fundamental structural and functional unit of all living organisms?", "All living beings are built of cells, and all basic biochemical life processes take place inside cells", ["Cells are the largest structures in the universe", "Non-living rocks are made of cells", "Cells can only be made of iron"]),
            ("Which famous postulate of the Cell Theory was proposed by Rudolf Virchow in 1855 ('Omnis cellula-e cellula')?", "All new cells arise only from pre-existing cells through cell division", ["Cells generate spontaneously from mud", "Cells do not contain genetic material", "Plants are not composed of cells"]),
            ("Which two German scientists originally formulated the classical Cell Theory in 1838–1839?", "Matthias Schleiden (botanist) and Theodor Schwann (zoologist)", ["Robert Hooke and Antonie van Leeuwenhoek", "Louis Pasteur and Robert Koch", "Gregor Mendel and Charles Darwin"]),
            ("Which of the following biological entities is an exception to the classical Cell Theory because it lacks cellular organization?", "Viruses", ["Bacteria", "Fungi", "Amoeba"])
        ],
        "CBSE-8-CURI-2-2.1.2": [
            ("Who first observed and coined the word 'cell' in 1665 while examining thin slices of bottle cork under a primitive microscope?", "Robert Hooke", ["Robert Brown", "Antonie van Leeuwenhoek", "Alexander Fleming"]),
            ("What did Robert Hooke actually see in the cork slices that reminded him of monastery rooms (cellulae)?", "Empty dead cell walls of plant tissue forming a honeycomb lattice", ["Active swimming bacteria", "Living cell nuclei", "Flowing blood cells"]),
            ("In which historic scientific book did Robert Hooke publish his detailed microscopic drawings of cork, fleas, and feathers?", "Micrographia (1665)", ["Origin of Species", "Philosophiae Naturalis Principia", "Systema Naturae"]),
            ("Bottle cork examined by Robert Hooke is derived from which natural plant tissue?", "Bark of the cork oak tree (Quercus suber)", ["Soft bamboo stem", "Pine tree needles", "Coconut husk fiber"])
        ],
        "CBSE-8-CURI-2-2.1.3": [
            ("Who was the first Dutch scientist to observe and describe living moving microscopic organisms ('animalcules') in 1674?", "Antonie van Leeuwenhoek", ["Robert Hooke", "Louis Pasteur", "Edward Jenner"]),
            ("From which natural sources did Antonie van Leeuwenhoek first collect and discover living bacteria and protozoa?", "Pond water, rainwater, and dental scrapings from human teeth", ["Boiling volcanic lava", "Frozen arctic glaciers", "Sterile distilled water"]),
            ("What unique skill enabled Antonie van Leeuwenhoek to achieve magnifications up to \\(270\\times\\) with his simple single-lens microscopes?", "His exceptional mastery of grinding and polishing tiny, high-curvature spherical glass lenses", ["He used electric halogen lamps", "He used compound magnetic prisms", "He stained specimens with fluorescent dyes"]),
            ("What did Antonie van Leeuwenhoek call the tiny, motile microbes he saw darting in pond water under his lens?", "'Animalcules' (meaning little animals)", ["Chromosomes", "Ribosomes", "Plastids"])
        ],
        "CBSE-8-CURI-2-2.1.4": [
            ("In a student compound optical microscope, which two lens systems cooperate to magnify the specimen?", "The objective lens (near specimen) and the eyepiece/ocular lens (near eye)", ["Two concave mirrors", "A single magnifying hand glass", "Two polarizing filters"]),
            ("When preparing a temporary mount of an onion peel, what chemical stain is commonly added to highlight cell nuclei and walls?", "Safranin (or dilute iodine solution)", ["Methylene blue", "Hydrochloric acid", "Copper sulfate"]),
            ("Why is a glass coverslip lowered gently at a \\(45^\\circ\\) angle using a needle onto the mounted specimen drop?", "To prevent the entrapment of air bubbles under the coverslip", ["To flatten the glass slide into powder", "To warm up the specimen", "To seal the specimen with glue"]),
            ("If a microscope has a \\(10\\times\\) eyepiece and a \\(40\\times\\) objective lens, what is its total visual magnification?", "\\(400\\times\\) (\\(10 \\times 40 = 400\\))", ["\\(50\\times\\)", "\\(4000\\times\\)", "\\(4\\times\\)"])
        ],
        "CBSE-8-CURI-2-2.1.5": [
            ("Which three fundamental structural features are universally present in almost all eukaryotic cells?", "Cell (plasma) membrane, cytoplasm, and a distinct membrane-bound nucleus", ["Cell wall, chloroplast, and centrosome", "Hemoglobin, bone matrix, and neuron", "Chitin wall, capsule, and flagella"]),
            ("The thin, flexible outer boundary that encloses the living protoplasm of all cells is the:", "Plasma membrane (cell membrane)", ["Nuclear membrane", "Tonoplast", "Pectin layer"]),
            ("What is the semi-fluid jelly-like matrix located between the plasma membrane and the nucleus called?", "Cytoplasm", ["Cytosol only", "Nucleoplasm", "Extracellular matrix"]),
            ("The spherical central organelle that houses genetic chromatin fibers and coordinates cellular metabolism is the:", "Nucleus", ["Golgi apparatus", "Ribosome", "Endoplasmic reticulum"])
        ],
        "CBSE-8-CURI-2-2.2.1": [
            ("A unicellular organism is defined as a living being:", "Whose entire body consists of only a single independent cell capable of performing all life functions", ["Composed of trillions of interconnected cells", "Having neither nucleus nor cytoplasm", "That cannot reproduce or feed"]),
            ("Which of the following freshwater microscopic organisms is unicellular and moves using temporary projections called pseudopodia?", "Amoeba proteus", ["Hydra", "Earthworm", "Spirogyra"]),
            ("Which unicellular green alga possesses a cup-shaped chloroplast and two whip-like anterior flagella for swimming?", "Chlamydomonas", ["Paramecium", "Yeast", "Mucor"]),
            ("Paramecium caudatum is a slipper-shaped unicellular protozoan that propels itself through water using:", "Thousands of microscopic hair-like cilia covering its pellicle", ["A single long flagellum", "Muscular foot", "Pseudopodia"])
        ],
        "CBSE-8-CURI-2-2.2.2": [
            ("In multicellular organisms, what is 'division of labour' fundamentally defined as?", "Specialization of different groups of cells to execute specific physiological tasks efficiently", ["All cells doing identical jobs at the same time", "Cells dividing only once in a lifetime", "Cells competing to absorb food"]),
            ("How do human red blood cells exhibit functional specialization compared to nerve cells (neurons)?", "RBCs are biconcave and packed with hemoglobin to transport oxygen, while neurons have long axons to transmit electrical impulses", ["RBCs transmit thoughts", "Neurons carry blood through arteries", "Both have identical shapes and functions"]),
            ("Why cannot a single isolated muscle cell survive independently outside the body like a free-living Amoeba?", "Specialized cells in multicellular organisms depend on other tissues for nutrition, oxygenation, and waste removal", ["Muscle cells have no DNA", "Muscle cells have no cell membrane", "Muscle cells do not respire"]),
            ("Which specialized plant cells form long hollow tubes adapted for conducting water and dissolved minerals from roots to leaves?", "Xylem vessels and tracheids", ["Phloem sieve tubes", "Parenchyma storage cells", "Collenchyma fibers"])
        ],
        "CBSE-8-CURI-2-2.2.3": [
            ("What is the correct biological hierarchy of structural organization in a multicellular living organism from simplest to most complex?", "\\(\\text{Cell} \\rightarrow \\text{Tissue} \\rightarrow \\text{Organ} \\rightarrow \\text{Organ System} \\rightarrow \\text{Organism}\\)", ["\\(\\text{Organism} \\rightarrow \\text{Cell} \\rightarrow \\text{Tissue} \\rightarrow \\text{Organ}\\)", "\\(\\text{Tissue} \\rightarrow \\text{Cell} \\rightarrow \\text{Organ System} \\rightarrow \\text{Organ}\\)", "\\(\\text{Cell} \\rightarrow \\text{Organ} \\rightarrow \\text{Tissue} \\rightarrow \\text{Organism}\\)"]),
            ("A tissue is defined in biology as:", "A group of similar cells with common embryonic origin working together to perform a specific function", ["A single giant cell with multiple nuclei", "An entire organ like the stomach", "A collection of unrelated organs"]),
            ("The human stomach is classified at which level of the biological structural hierarchy?", "Organ (composed of epithelial, muscular, and connective tissues working together)", ["Tissue level", "Cellular level", "Organism level"]),
            ("The heart, blood, and blood vessels together constitute which level of organization?", "An organ system (the Circulatory System)", ["A tissue group", "A cellular colony", "A species"])
        ],
        "CBSE-8-CURI-2-2.3.1": [
            ("Microorganisms (microbes) are broadly defined as:", "Living microscopic organisms that are too small to be seen clearly by the unaided human eye", ["Extinct prehistoric fossil remains", "Inorganic crystals dissolved in water", "Small insects visible on leaves"]),
            ("What is the standard unit of length typically used to measure the microscopic dimensions of bacterial and animal cells?", "Micrometre (\\(\\mu\\text{m}\\)), where \\(1\\ \\mu\\text{m} = 10^{-6}\\ \\text{m}\\)", ["Millimetre (mm)", "Nanometre (nm)", "Kilometre (km)"]),
            ("Which scientific field is dedicated specifically to the study of microscopic organisms?", "Microbiology", ["Astronomy", "Geology", "Anthropology"]),
            ("Can microorganisms survive in extreme environments like boiling geothermal hot springs and sub-zero polar ice?", "Yes, many extremophilic bacteria and archaea possess specialized cellular adaptations allowing survival in harsh extremes", ["No, microbes die above 30 degrees Celsius", "No, microbes only live in drinking water", "Only inside human blood"])
        ],
        "CBSE-8-CURI-2-2.3.2": [
            ("What are the four major traditional groups into which microorganisms are classified?", "Bacteria, Fungi, Protozoa, and Algae", ["Insects, Worms, Birds, and Reptiles", "Viruses, Prions, Minerals, and Rocks", "Ferns, Mosses, Conifers, and Palms"]),
            ("Which major microbial group consists of unicellular prokaryotes lacking a membrane-bound nucleus?", "Bacteria", ["Fungi", "Protozoa", "Algae"]),
            ("Yeast (Saccharomyces cerevisiae) and bread mold (Rhizopus) belong to which major group of microorganisms?", "Fungi (saprophytic eukaryotes)", ["Bacteria", "Algae", "Protozoa"]),
            ("Which group of microorganisms possesses chlorophyll and performs plant-like photosynthesis in aquatic habitats?", "Microscopic Algae (such as Chlorella and Spirogyra)", ["Protozoa", "Fungi", "Bacteria lacking pigments"])
        ],
        "CBSE-8-CURI-2-2.3.3": [
            ("When a drop of stagnant green pond water is examined under a compound microscope, which organisms are commonly observed?", "Spirogyra strands, Chlamydomonas, Paramecium, and Amoeba", ["Goldfish embryos", "Marine coral polyps", "Terrestrial earthworms"]),
            ("Why is fertile garden soil rich in diverse microbial populations?", "Soil provides abundant moisture, decaying organic humus, mineral salts, and protective pores for bacterial and fungal growth", ["Soil contains pure alcohol", "Soil is completely sterile", "Microbes cannot live in air"]),
            ("What specialized dormant structure do many bacteria form to survive prolonged desiccation, extreme heat, or starvation?", "Endospores (tough, resistant protective coats)", ["Cysts in algae", "Seeds like plants", "Buds like yeast"]),
            ("How do microorganisms spread between distant natural habitats across the biosphere?", "Carried passively by air currents, flowing water streams, soil transport, and on bodies of insects and animals", ["By burrowing through the Earth's core", "By generating laser beams", "They never leave their birthplace"])
        ],
        "CBSE-8-CURI-2-2.3.4": [
            ("Why are viruses uniquely classified on the borderline between living organisms and non-living matter?", "They are inert non-cellular crystalline particles outside a host, but replicate and exhibit genetic heredity inside living host cells", ["They eat bacteria like food", "They grow into giant mushrooms", "They can photosynthesize in sunlight"]),
            ("What are the two essential biochemical components of a basic viral particle (virion)?", "A nucleic acid core (DNA or RNA) enclosed within a protective protein coat (capsid)", ["Cell wall and cytoplasm", "Cell membrane and mitochondria", "Cellulose and starch"]),
            ("A virus that specifically attacks and infects bacterial cells is scientifically named a:", "Bacteriophage", ["Protozoan", "Viroid", "Plasmid"]),
            ("Which of the following human diseases is caused by a viral infection rather than a bacterial infection?", "Influenza (Flu), Common Cold, Polio, and Chickenpox", ["Tuberculosis and Cholera", "Typhoid and Tetanus", "Ringworm and Athlete's foot"])
        ],
        "CBSE-8-CURI-2-2.4.1": [
            ("Which beneficial bacterium converts the lactose sugar in milk into lactic acid to produce curd (yogurt)?", "Lactobacillus acidophilus (lactic acid bacteria)", ["Streptococcus pneumoniae", "Escherichia coli", "Vibrio cholerae"]),
            ("Why does bread dough rise and become soft, spongy, and porous when Baker's yeast is added?", "Yeast ferments sugars anaerobically, releasing carbon dioxide gas bubbles that get trapped and expand in the dough matrix", ["Yeast generates steam through heat", "Yeast digests the flour into liquid", "Yeast absorbs all atmospheric nitrogen"]),
            ("The biochemical process of converting sugars into alcohol and carbon dioxide by microorganisms like yeast is termed:", "Fermentation", ["Pasteurization", "Nitrogen fixation", "Sublimation"]),
            ("Which French microbiologist discovered the biological nature of fermentation in 1857 and developed pasteurization?", "Louis Pasteur", ["Edward Jenner", "Alexander Fleming", "Robert Koch"])
        ],
        "CBSE-8-CURI-2-2.4.2": [
            ("Antibiotics are chemical substances produced by microorganisms (such as fungi and bacteria) that:", "Kill or inhibit the growth of pathogenic bacteria inside the body", ["Kill all human cells", "Neutralize stomach acid", "Provide vitamins to the skin"]),
            ("Who discovered the first antibiotic, Penicillin, in 1928 from the green mold Penicillium notatum?", "Alexander Fleming", ["Louis Pasteur", "Edward Jenner", "Robert Hooke"]),
            ("A vaccine protects the human body against future infectious disease outbreaks by:", "Introducing weakened or killed pathogens to stimulate the immune system to produce antibodies and memory cells", ["Supplying ready-made sugar to muscles", "Killing viruses with high electricity", "Coating the skin with wax"]),
            ("Who developed the world's very first successful vaccine in 1796 to eradicate smallpox using cowpox pus?", "Edward Jenner", ["Louis Pasteur", "Robert Koch", "Alexander Fleming"])
        ],
        "CBSE-8-CURI-2-2.4.3": [
            ("How do saprophytic microorganisms in soil contribute to environmental cleanliness and agricultural soil fertility?", "They decompose fallen dead leaves, animal carcasses, and farm waste into dark organic humus, recycling essential plant nutrients", ["They turn soil into hard solid granite", "They evaporate all soil water", "They consume minerals permanently"]),
            ("Which symbiotic bacterium residing in the root nodules of leguminous plants (pulses, peas) fixes atmospheric nitrogen into nitrates?", "Rhizobium", ["Lactobacillus", "Clostridium", "Penicillium"]),
            ("Why is biological nitrogen fixation indispensable for agricultural crop production?", "Plants cannot absorb gaseous nitrogen directly from air; they require fixed soil nitrates to synthesize essential proteins and amino acids", ["Nitrogen makes fruits sweet", "Nitrogen prevents plant transpiration", "Plants need nitrogen to reflect sunlight"]),
            ("If all decomposing bacteria and fungi were suddenly eliminated from Earth, what ecological crisis would occur?", "Dead organic plant and animal debris would accumulate endlessly, choking ecosystems as nutrient recycling grinds to a halt", ["Soil would become infinitely fertile", "Air would become 100% oxygen", "All plant growth would double"])
        ],
        "CBSE-8-CURI-2-2.4.4": [
            ("Microorganisms that enter living hosts and cause infectious diseases are termed:", "Pathogens (disease-causing agents)", ["Saprophytes", "Symbionts", "Probiotics"]),
            ("Which deadly waterborne bacterial disease is characterized by severe watery diarrhea, rapid dehydration, and vomiting?", "Cholera (caused by Vibrio cholerae)", ["Malaria", "Ringworm", "Tuberculosis"]),
            ("Tuberculosis (TB) is a chronic pulmonary disease caused by which pathogenic bacterium spread through airborne cough droplets?", "Mycobacterium tuberculosis", ["Salmonella typhi", "Plasmodium vivax", "Influenza virus"]),
            ("Which female mosquito serves as the biological vector transmitting the protozoan parasite Plasmodium that causes malaria?", "Female Anopheles mosquito", ["Female Aedes aegypti", "Culex mosquito", "Housefly"])
        ],
        "CBSE-8-CURI-2-2.4.5": [
            ("Food preservation techniques prevent microbial spoilage primarily by:", "Creating conditions (low moisture, high osmotic pressure, extreme temperature, lack of air) that inhibit microbial growth and enzymatic activity", ["Adding sugar to make food sweet", "Killing microbes with chemical bleach", "Washing food with hot milk"]),
            ("Adding high concentrations of common salt (curing) or sugar (in jams and jellies) preserves food because:", "High solute concentration causes hypertonic plasmolysis, drawing water out of microbial cells and inhibiting their growth", ["Salt and sugar are toxic to all life", "Microbes prefer salty water", "Salt produces antibiotic chemicals"]),
            ("Pasteurization of commercial dairy milk involves heating milk to approximately:", "\\(70^\\circ\\text{C}\\) for 15 to 30 seconds, followed by rapid chilling to below \\(10^\\circ\\text{C}\\) to kill harmful bacteria without altering flavor", ["\\(100^\\circ\\text{C}\\) for two hours continuously", "\\(40^\\circ\\text{C}\\) for 5 minutes", "\\(0^\\circ\\text{C}\\) overnight"]),
            ("Which chemical food preservative is commonly added to packaged fruit squashes, ketchups, and juices to retard microbial fermentation?", "Sodium benzoate (or potassium metabisulfite)", ["Hydrochloric acid", "Sodium chloride crystals only", "Copper sulfate"])
        ],
        "CBSE-8-CURI-2-2.5.1": [
            ("A single free-living cell like Amoeba exhibits independent existence because it carries out all essential life processes including:", "Nutrition, cellular respiration, excretion, osmoregulation, and reproduction within its single boundary", ["Building brick houses", "Photosynthesizing in darkness", "Filtering arterial blood"]),
            ("In Amoeba, how is respiratory gas exchange (taking in \\(\\text{O}_2\\) and expelling \\(\\text{CO}_2\\)) carried out?", "By simple diffusion across the selectively permeable plasma membrane into the surrounding water", ["Through internal lungs", "Via tracheal tubes", "Through gills"]),
            ("How does Amoeba ingest food particles like microscopic algae through phagocytosis?", "By extending finger-like pseudopodia around the food particle to engulf it into a temporary food vacuole", ["By biting with teeth", "By sucking with an oral proboscis", "By filtering through feathers"]),
            ("Undigested food residues in Amoeba are eliminated from the cell by:", "Migrating the food vacuole to the cell membrane surface and rupturing it outward (exocytosis)", ["Expelling through a permanent rectum", "Dissolving the entire cell", "Filtering through cilia"])
        ],
        "CBSE-8-CURI-2-2.5.2": [
            ("Why is cell division essential for living organisms?", "For growth of tissues, replacement of worn-out or damaged cells, and reproduction of the species", ["To make cells heavier", "To change cell color", "To stop cellular respiration"]),
            ("In unicellular organisms like Amoeba and Bacteria, cell division by binary fission directly represents:", "Asexual reproduction resulting in two genetically identical offspring daughter cells", ["Physical damage to the cell", "Tissue specialization", "Cellular death"]),
            ("When a skin scratch heals over several days, which cellular process is actively generating new epithelial cells?", "Mitotic cell division", ["Meiotic gamete formation", "Cellular decomposition", "Osmotic swelling"]),
            ("Prior to cell division, what crucial genetic event must take place inside the nucleus to ensure each daughter cell receives complete genetic instructions?", "Accurate replication and duplication of nuclear DNA / chromosomes", ["Dissolution of all cell organelles", "Expulsion of the cytoplasm", "Absorption of soil nutrients"])
        ],
        "CBSE-8-CURI-2-2.5.3": [
            ("Where is the universal cellular energy currency ATP (Adenosine Triphosphate) primarily synthesized inside eukaryotic cells?", "Mitochondria (through cellular respiration)", ["Ribosomes", "Lysosomes", "Centrioles"]),
            ("Which cellular macromolecular machines are responsible for translating genetic mRNA messages into polypeptide protein chains?", "Ribosomes", ["Golgi cisternae", "Smooth ER tubules", "Vacuoles"]),
            ("Which organelle modifies, sorts, and packages synthesized proteins and lipids into vesicles for transport to target destinations?", "Golgi complex (apparatus)", ["Nucleolus", "Mitochondrion", "Chloroplast"]),
            ("In green plant cells, light energy is trapped and converted into chemical energy stored in glucose molecules inside:", "Chloroplasts (via photosynthesis)", ["Chromoplasts", "Leucoplasts", "Centrosomes"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 3 DATA
    # -------------------------------------------------------------------------
    ch3_cases = {
        "CBSE-8-CURI-3-3.1.1": [
            ("According to the World Health Organization (WHO), health is officially defined as:", "A state of complete physical, mental, and social well-being, and not merely the absence of disease or infirmity", ["The absence of physical fever only", "Possessing large muscular body weight", "Never visiting a medical clinic"]),
            ("Why is health not simply defined as 'not being sick'?", "A person free from clinical disease may still suffer from severe psychological stress, anxiety, or social isolation", ["Because diseases do not exist", "Because all humans are always healthy", "Because medicine cannot treat diseases"]),
            ("Which dimension of health encompasses the proper functioning of biological organ systems, muscular vigor, and physical stamina?", "Physical health", ["Social health", "Mental health", "Spiritual health"]),
            ("Which dimension of health reflects an individual's ability to form harmonious relationships, communicate constructively, and adapt within society?", "Social health", ["Physical health", "Physiological health", "Genetic health"])
        ],
        "CBSE-8-CURI-3-3.1.2": [
            ("What is the crucial distinction between being 'healthy' and being 'disease-free'?", "Being disease-free means having no identified physiological disorder, while being healthy implies optimal physical, mental, and social wellness", ["There is no difference between the terms", "Healthy applies only to animals", "Disease-free implies immortal life"]),
            ("A flute player who has no cough or physical illness but lacks lung capacity to sustain musical notes may be described as:", "Disease-free, but not achieving optimal physical fitness/health for their specific craft", ["Clinically diseased", "Suffering from chronic asthma", "Socially isolated"]),
            ("Can a person experiencing severe chronic workplace depression and insomnia be classified as truly healthy under WHO standards?", "No, because their mental and psychological well-being is substantially impaired", ["Yes, as long as they have no bacterial infection", "Yes, because mental state has no role in health", "Yes, if they have normal body temperature"]),
            ("The health of an individual depends intrinsically on both personal biological factors and which external factor?", "The surrounding physical, social, and economic community environment", ["The phase of the moon", "The color of house walls", "The type of car owned"])
        ],
        "CBSE-8-CURI-3-3.1.3": [
            ("What does emotional wellness encompass in holistic human health?", "The ability to recognize, understand, express, and constructively manage one's feelings and stress effectively", ["Suppressing all emotions permanently", "Reacting with anger to all challenges", "Never feeling sad under any circumstances"]),
            ("Which practice is recognized in modern medicine for promoting emotional balance, reducing cortisol stress hormones, and calming the mind?", "Mindfulness meditation, yoga, and regular reflective quiet time", ["Excessive binge eating of fast food", "Spending entire nights playing video games", "Complete social withdrawal"]),
            ("Why is social well-being vital for long-term psychological resilience in teenagers?", "Supportive social connections with family and friends provide emotional security, belonging, and constructive coping avenues", ["It allows bullying others online", "It eliminates the need for healthy eating", "It replaces the need for sleep"]),
            ("Chronic unmanaged emotional stress can manifest as physical health problems, such as:", "Elevated blood pressure, tension headaches, peptic ulcers, and weakened immune defense", ["Increased physical strength", "Improved vision in darkness", "Zero metabolic waste"])
        ],
        "CBSE-8-CURI-3-3.2.1": [
            ("What constitutes a scientifically balanced diet for growing adolescents?", "A diet providing carbohydrates, proteins, fats, vitamins, minerals, dietary roughage, and water in proper proportions", ["A diet composed entirely of deep-fried potato chips", "Eating only sugary sweets and carbonated drinks", "Consuming only protein powders without vegetables"]),
            ("Which macronutrient serves as the primary building block for muscular tissue growth, enzymatic synthesis, and cellular repair?", "Proteins (composed of essential amino acids)", ["Carbohydrates", "Fats", "Dietary fiber"]),
            ("Why is dietary roughage (dietary fiber found in whole grains, fruits, and green vegetables) indispensable in our daily meals?", "It adds bulk to the food, facilitating smooth intestinal peristalsis and preventing chronic constipation", ["It provides hundreds of ATP calories", "It dissolves into pure glucose", "It turns into blood plasma"]),
            ("Deficiency of vitamin C (ascorbic acid) in the daily diet leads to which bleeding gum disorder?", "Scurvy", ["Rickets", "Beriberi", "Night blindness"])
        ],
        "CBSE-8-CURI-3-3.2.2": [
            ("Why is regular, thorough handwashing with soap and clean water the most effective basic hygiene practice?", "Soap breaks down lipid membranes of pathogenic bacteria and enveloped viruses, rinsing them mechanically off skin", ["Soap permanently sterilizes skin cells", "Water creates an impermeable acid shield", "Soap colors the hands"]),
            ("Dental caries (tooth decay and cavities) are caused primarily by:", "Bacterial plaque fermenting residual food sugars in the mouth into acids that demineralize tooth enamel", ["Chewing tough fibrous raw vegetables", "Brushing teeth twice daily", "Drinking plain water"]),
            ("How does maintaining personal bodily hygiene (daily bathing, wearing clean washed clothes) prevent dermatological infections?", "Removes accumulated sweat, dead epidermal cells, and inhibits fungal skin infections like ringworm and acne", ["Increases body height rapidly", "Changes skin color", "Stops normal sweating"]),
            ("Proper oral hygiene guidelines recommend brushing teeth thoroughly:", "At least twice a day—in the morning and at night before bed", ["Once every few weeks", "Only when visiting a dentist", "Ten times after every meal"])
        ],
        "CBSE-8-CURI-3-3.2.3": [
            ("How does regular physical exercise and outdoor sports benefit the human cardiovascular system?", "Strengthens cardiac muscle, improves lung vital capacity, enhances blood circulation, and lowers resting blood pressure", ["Makes heart valves stop beating", "Increases arterial cholesterol clogging", "Shrinks the size of the lungs"]),
            ("Practicing Yogasanas and Pranayama breathing exercises regularly helps in:", "Enhancing musculoskeletal flexibility, correcting posture, calming nervous anxiety, and optimizing pulmonary ventilation", ["Curing bacterial pneumonia overnight", "Eliminating the need for a balanced diet", "Halting normal cellular growth"]),
            ("Sedentary lifestyle habits (excessive screen time on smartphones/TV, lack of physical movement) are directly linked to:", "Childhood obesity, insulin resistance, muscular atrophy, and poor cardiovascular stamina", ["Superior athletic performance", "Immunity to all infectious pathogens", "High muscular strength"]),
            ("Why does participating in team sports promote both physical health and social development in students?", "Combines rigorous physical conditioning with teamwork, communication, leadership, and emotional camaraderie", ["Encourages solitary isolation", "Eliminates need for hydration", "Replaces school studies"])
        ],
        "CBSE-8-CURI-3-3.2.4": [
            ("Why is adequate, uninterrupted sleep (8 to 9 hours nightly) crucial for growing adolescents?", "Growth hormone is secreted during deep sleep, and the brain consolidates learning memories while repairing cellular tissues", ["Sleep stops the heart from beating", "Sleep eliminates the need for calories", "Sleep turns blood into spinal fluid"]),
            ("Chronic sleep deprivation in teenagers leads to which observable cognitive and physiological consequences?", "Impaired attention, memory lapses, irritability, weakened immune defenses, and diminished academic performance", ["Superhuman memory recall", "Complete physical immunity to flu", "Permanent energy bursts"]),
            ("What healthy sleep hygiene habit helps in establishing a restorative circadian sleep rhythm?", "Maintaining a consistent sleep-wake schedule and avoiding electronic blue-light screens right before bedtime", ["Drinking high-caffeine beverages at midnight", "Sleeping with loud bright lights on", "Sleeping only 2 hours on weekdays and 16 hours on Sunday"]),
            ("Relaxation activities like listening to soothing music, nature walks, or reading before sleep serve to:", "Activate the parasympathetic nervous system, lowering heart rate and preparing the body for restful sleep", ["Induce extreme adrenaline release", "Shock the cardiac muscle", "Stop brain respiration"])
        ],
        "CBSE-8-CURI-3-3.2.5": [
            ("Why is access to safe, potable drinking water fundamental to public community health?", "Prevents catastrophic outbreaks of life-threatening waterborne gastrointestinal diseases like cholera, typhoid, and dysentery", ["Water has zero nutritional value", "Water replaces all dietary protein", "Water causes immediate fever"]),
            ("What simple, reliable household method makes biologically contaminated water safe from pathogens during flood emergencies?", "Boiling water vigorously for at least 10 to 15 minutes", ["Straining water through a coarse wire mesh", "Adding table salt", "Leaving water in the dark"]),
            ("How does improper, unmanaged disposal of municipal garbage and sewage in neighborhoods affect human health?", "Serves as breeding grounds for disease vectors like flies, mosquitoes, and rodents that transmit pathogens to food and water", ["Cleans ambient city air", "Enriches drinking water wells", "Prevents insect breeding"]),
            ("Stagnant water puddles in discarded tires, open plastic containers, and uncleaned desert air coolers provide breeding sites for:", "Aedes mosquitoes (transmitting dengue and chikungunya) and Anopheles (malaria)", ["Beneficial honeybees", "Earthworms", "House sparrows"])
        ],
        "CBSE-8-CURI-3-3.3.1": [
            ("What is the physiological significance of an elevated body temperature (fever) during an infection?", "It is an active defense reaction where the body raises temperature to inhibit pathogen replication and stimulate leukocyte activity", ["It indicates the body is freezing", "It means blood has turned into steam", "It indicates permanent brain death"]),
            ("Which of the following is a physical signal or clinical sign that a physician can observe and measure objectively?", "Body temperature of \\(39^\\circ\\text{C}\\) on a thermometer, inflamed throat redness, or rash", ["A patient's feeling of sadness", "A patient's headache intensity", "A patient's bad dream"]),
            ("Persistent cough lasting more than two weeks, blood in sputum, chest pain, and night sweats are warning signs of:", "Pulmonary tuberculosis", ["Common cold", "Mild indigestion", "Vitamin D deficiency"]),
            ("Sudden, acute pain in the chest radiating to the left arm accompanied by profuse sweating and shortness of breath is a critical signal of:", "A myocardial infarction (heart attack) requiring immediate emergency medical intervention", ["Mild stomach gas", "Muscle fatigue from running", "Lack of sleep"])
        ],
        "CBSE-8-CURI-3-3.3.2": [
            ("In clinical diagnosis, what is the fundamental difference between a 'symptom' and a 'sign'?", "A symptom is a subjective feeling experienced by the patient (e.g., headache, nausea), whereas a sign is an objective finding observed or measured by a doctor (e.g., fever, rash, high BP)", ["Symptoms are measured with instruments, signs are not", "Signs only occur in plant diseases", "There is no scientific difference"]),
            ("Which of the following is correctly classified as a subjective symptom?", "Nausea, dizziness, and fatigue felt by the patient", ["Blood pressure reading of \\(150/100\\ \\text{mm Hg}\\)", "\\(102^\\circ\\text{F}\\) on thermometer", "Swollen red tonsils observed with a torch"]),
            ("Why does a doctor record both the patient's reported symptoms and observable clinical signs?", "To synthesize an accurate differential diagnosis and prescribe appropriate confirmatory diagnostic tests", ["To fill out hospital paperwork only", "Because symptoms are always false", "Because signs cannot be treated with medicine"]),
            ("Jaundice is characterized by yellowing of skin and sclera of eyes. This yellow pigmentation is:", "A clinical sign caused by high bilirubin levels in blood due to liver dysfunction", ["A subjective symptom felt only in dreams", "A harmless skin tan", "A temporary fungal dye"])
        ],
        "CBSE-8-CURI-3-3.3.3": [
            ("When should an individual promptly seek professional medical consultation rather than relying on home remedies?", "When symptoms persist, worsen rapidly, or involve high fever, breathing distress, severe pain, or bleeding", ["Only when they are completely unconscious", "Never; all illnesses resolve without doctors", "Only once every 10 years"]),
            ("What is the clinical role of diagnostic laboratory tests like complete blood counts (CBC), urine tests, and throat swabs?", "They provide objective microbiological and biochemical evidence to identify the exact cause of illness", ["They replace the need for prescription drugs", "They cure infections instantly during the test", "They are performed only for curiosity"]),
            ("Why is diagnostic testing essential before initiating targeted antibiotic therapy?", "Antibiotics are effective solely against specific bacterial infections and are useless against viral illnesses like common cold or flu", ["Antibiotics can treat broken bones", "Antibiotics work equally on all viruses and fungi", "Testing makes antibiotics taste better"]),
            ("Which medical imaging technique uses high-frequency sound waves to visualize internal soft organs like liver and kidneys safely without radiation?", "Ultrasonography (ultrasound scan)", ["X-ray radiography", "CT scan", "PET scan"])
        ],
        "CBSE-8-CURI-3-3.4.1": [
            ("How are human diseases broadly classified based on whether they can be transmitted between individuals?", "Communicable (infectious) diseases and Non-communicable (non-infectious) diseases", ["Curable and non-curable only", "Bacterial and mineral only", "Childhood and elder diseases only"]),
            ("Which of the following diseases is classified as a communicable (infectious) disease?", "Tuberculosis, cholera, measles, and influenza", ["Diabetes mellitus", "Hypertension", "Coronary heart disease"]),
            ("Which of the following is classified as a non-communicable lifestyle disease that cannot spread from person to person?", "Type 2 diabetes, cardiovascular diseases, and cancer", ["Chickenpox", "Amoebic dysentery", "Common cold"]),
            ("What causes communicable diseases to spread across a community?", "Transmission of infectious biological pathogens (viruses, bacteria, protozoa, fungi) through air, water, food, or vectors", ["Breathing pure mountain air", "Eating home-cooked balanced food", "Drinking boiled water"])
        ],
        "CBSE-8-CURI-3-3.4.2": [
            ("Which pathogen causes the tropical mosquito-borne disease malaria in humans?", "Plasmodium (a microscopic protozoan parasite)", ["Escherichia coli bacterium", "Varicella zoster virus", "Candida fungus"]),
            ("Typhoid fever is caused by infection with which pathogenic bacterium ingested through contaminated food or water?", "Salmonella typhi", ["Streptococcus pneumoniae", "Clostridium tetani", "Rhinovirus"]),
            ("Athlete's foot and ringworm (tinea) are common contagious skin infections caused by:", "Dermatophytic fungi", ["Viruses", "Bacteria", "Flatworms"]),
            ("Acquired Immunodeficiency Syndrome (AIDS) is caused by which retrovirus that attacks human immune helper T-cells?", "Human Immunodeficiency Virus (HIV)", ["Hepatitis B virus", "Herpes simplex virus", "Rabies virus"])
        ],
        "CBSE-8-CURI-3-3.4.3": [
            ("How do respiratory infections like influenza, common cold, and COVID-19 transmit between people?", "Through microscopic aerosol droplets expelled when an infected person coughs, sneezes, or talks", ["Through insect bites like ticks", "Only by swimming in chlorinated pools", "By walking on dry grass"]),
            ("Food-and-water-borne diseases (such as cholera, typhoid, and hepatitis A) spread through the:", "Fecal-oral transmission route via contaminated drinking water or unhygienically handled food", ["Direct transmission through undamaged skin", "Inhalation of pure oxygen", "Hearing loud music"]),
            ("Biological vectors in disease transmission are defined as:", "Living carrier organisms (like mosquitoes, fleas, or flies) that transmit pathogens from an infected host to a susceptible individual", ["Contaminated surgical instruments", "Bottled medicines", "Sterile bandage rolls"]),
            ("Why is covering the mouth and nose with a handkerchief or elbow when sneezing a vital public health measure?", "Prevents the projection of infectious aerosol droplets into ambient air and onto shared surfaces", ["Warms the nose in winter", "Muffles the sound of sneezing", "Stops the heart from skipping a beat"])
        ],
        "CBSE-8-CURI-3-3.4.4": [
            ("Lifestyle diseases (such as Type 2 diabetes, atherosclerosis, and hypertension) develop primarily due to:", "Sedentary physical inactivity, chronic stress, poor diet high in processed sugars/fats, and tobacco/alcohol use", ["Infection by airborne viruses", "Drinking clean boiled water", "Exercising daily outdoors"]),
            ("Nutritional deficiency disease Kwashiorkor in young children is caused by severe lack of which nutrient in meals?", "Proteins", ["Vitamin A", "Carbohydrates", "Iron"]),
            ("Goitre, characterized by an abnormal enlargement of the thyroid gland in the neck, is caused by nutritional deficiency of:", "Iodine (essential for synthesizing thyroxine hormone)", ["Calcium", "Iron", "Vitamin D"]),
            ("Anemia, resulting in pale skin, extreme fatigue, and dizziness, is most commonly caused by deficiency of:", "Iron (required for hemoglobin synthesis in red blood cells)", ["Vitamin C", "Sodium", "Phosphorus"])
        ],
        "CBSE-8-CURI-3-3.5.1": [
            ("What is the human immune system fundamentally designed to do?", "Defend the body against invading pathogens, foreign antigens, and abnormal cancerous cells", ["Filter waste blood like kidneys", "Pump arterial blood like heart", "Digest food inside the stomach"]),
            ("What serves as the human body's first line of innate physical and chemical defense against invading microbes?", "Undamaged skin barrier, mucosal secretions, stomach hydrochloric acid, and lysozyme enzymes in tears/saliva", ["Red blood cells in veins", "Skeletal bones and teeth", "Subcutaneous adipose fat"]),
            ("Which specialized white blood cells engulf, ingest, and destroy invading bacteria through phagocytosis?", "Neutrophils and Macrophages", ["Erythrocytes", "Platelets", "Osteocytes"]),
            ("What protective proteins are synthesized by plasma B-lymphocytes to specifically bind, neutralize, and tag foreign antigens?", "Antibodies (immunoglobulins)", ["Enzymes like amylase", "Structural keratins", "Hormones like insulin"])
        ],
        "CBSE-8-CURI-3-3.5.2": [
            ("What is the underlying biological principle of vaccination (immunization)?", "Introducing harmless antigenic proteins or weakened pathogens to trigger primary immune response and generate long-lasting memory cells", ["Injecting concentrated bacterial toxins into blood", "Coating veins with plastic", "Paralyzing white blood cells"]),
            ("When an immunized individual is subsequently exposed to the real virulent pathogen, how does the body respond?", "Immunological memory cells recognize the antigen immediately and launch a rapid, massive antibody response that destroys the pathogen before disease develops", ["The body fails to notice the pathogen", "White blood cells commit suicide", "The pathogen multiples completely unhindered"]),
            ("What is 'Herd Immunity' in public health vaccination campaigns?", "When a high percentage of the population is vaccinated, the spread of the pathogen is contained, protecting vulnerable unvaccinated individuals", ["Vaccinating farm animals only", "Immunity that lasts only 24 hours", "A disease that infects herds of deer"]),
            ("Which global vaccination campaign conducted by WHO achieved the historic eradication of which deadly viral human disease in 1980?", "Smallpox", ["Common cold", "Malaria", "Cholera"])
        ],
        "CBSE-8-CURI-3-3.5.3": [
            ("Why should antibiotic medications NEVER be taken for viral infections like the common cold, viral cough, or influenza?", "Antibiotics target bacterial cellular structures (like cell walls and bacterial ribosomes) and have zero therapeutic effect against viruses", ["Antibiotics make viruses grow 100 times larger", "Viruses are allergic to antibiotics", "Antibiotics only work in freezing cold"]),
            ("What dangerous global health threat arises from indiscriminate overuse and incomplete courses of prescription antibiotics?", "Development of Antibiotic Resistance (emergence of drug-resistant 'Superbugs')", ["Antibiotics turning into vitamins", "Human blood turning completely sterile", "Bacterial pathogens becoming completely extinct"]),
            ("What is the strict medical guideline regarding the duration of an antibiotic course prescribed by a doctor?", "Complete the entire prescribed dosage course even if symptoms subside early, to ensure all pathogenic bacteria are eliminated", ["Stop taking the medication as soon as you feel slightly better", "Double the dosage whenever you feel tired", "Share leftover antibiotics with family members"]),
            ("Self-medication without a physician's prescription is dangerous because it can lead to:", "Incorrect diagnosis, severe adverse drug reactions, drug resistance, and organ toxicity", ["Guaranteed instant recovery", "Immunity to all known diseases", "Enhanced physical stamina"])
        ],
        "CBSE-8-CURI-3-3.5.4": [
            ("How does eliminating stagnant water collections in overhead tanks, flowerpots, and discarded containers prevent dengue outbreaks?", "It destroys the essential aquatic breeding habitats where female Aedes mosquitoes lay eggs and larvae develop", ["It starves adult mosquitoes", "It drives mosquitoes into forests", "It freezes mosquito wings"]),
            ("What biological vector control measure involves introducing Gambusia (mosquito fish) into ponds and lakes?", "Gambusia fish actively feed on mosquito larvae and pupae, drastically suppressing the mosquito population naturally", ["Fish poison the lake water", "Fish emit sound waves that repel insects", "Fish consume water weed only"]),
            ("Why are bed nets treated with insecticide and window wire-mesh screens highly recommended in malaria-endemic regions?", "They provide a physical and chemical barrier preventing night-biting female Anopheles mosquitoes from reaching sleeping individuals", ["They keep the bedroom warm in winter", "They filter atmospheric carbon dioxide", "They attract beneficial butterflies"]),
            ("Spraying safe chemical larvicides or mineral oil on the surface of open stagnant drains controls mosquitoes by:", "Forming a thin surface film that blocks breathing siphons of mosquito larvae, causing them to suffocate", ["Turning water into solid ice", "Attracting flies to eat larvae", "Altering water pH to neutral"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 4 DATA
    # -------------------------------------------------------------------------
    ch4_cases = {
        "CBSE-8-CURI-4-4.1.1": [
            ("Which Danish physicist first discovered in 1820 that an electric current flowing through a wire deflects a nearby magnetic compass needle?", "Hans Christian Oersted", ["Michael Faraday", "Andre-Marie Ampere", "James Prescott Joule"]),
            ("What fundamental scientific law of electromagnetism was established by Oersted's historic compass experiment?", "An electric current flowing through a conductor produces a magnetic field in the surrounding space", ["Magnets generate electricity without movement", "Current creates static friction in air", "Electricity destroys magnetic poles"]),
            ("What happens to the magnetic compass needle when the direction of electric current flowing in the adjacent wire is reversed?", "The compass needle deflects in the exactly opposite direction", ["The needle stops moving permanently", "The needle spins continuously at light speed", "The needle loses all magnetism"]),
            ("What happens to the deflection of the compass needle when the magnitude of the electric current through the wire is increased?", "The angle of deflection increases, indicating a stronger magnetic field", ["The deflection decreases to zero", "The needle remains completely stationary", "The needle points only South"])
        ],
        "CBSE-8-CURI-4-4.1.2": [
            ("The magnetic field lines produced around a long straight current-carrying wire form which geometric pattern?", "Concentric circles centered on the wire lying in planes perpendicular to the wire", ["Straight lines parallel to the wire", "Radial lines pointing away from the wire", "Random zigzag waves"]),
            ("Which rule determines the direction of the magnetic field lines around a straight current-carrying conductor?", "Right-Hand Thumb Rule (Maxwell's Corkscrew Rule)", ["Fleming's Left-Hand Rule", "Ohm's Law", "Newton's Third Law"]),
            ("According to the Right-Hand Thumb Rule, if the right thumb points in the direction of conventional electric current, the curled fingers indicate:", "The direction of the magnetic field lines encircling the conductor", ["The direction of mechanical force", "The direction of electrostatic voltage", "The direction of heat dissipation"]),
            ("As one moves further away from a current-carrying wire, what happens to the strength of its magnetic field?", "The magnetic field strength decreases inversely with distance", ["The magnetic field strength increases infinitely", "The magnetic field strength remains constant", "The magnetic field vanishes instantly at 1 cm"])
        ],
        "CBSE-8-CURI-4-4.1.3": [
            ("An electromagnet is constructed by:", "Winding insulated copper wire tightly around a soft iron core and passing an electric current through the coil", ["Placing a copper rod in boiling water", "Rubbing an iron nail with silk cloth", "Connecting two magnets with plastic wire"]),
            ("Why is soft iron strictly preferred over hard steel as the magnetic core of a temporary electromagnet?", "Soft iron gains strong magnetism quickly when current is on, and loses almost all magnetism immediately when current is switched off", ["Soft iron stays permanently magnetized forever", "Soft iron is lighter than plastic", "Soft iron does not conduct heat"]),
            ("Which of the following actions will INCREASE the magnetic strength of an electromagnet?", "Increasing the electric current in the coil and increasing the number of coil turns", ["Decreasing the number of coil turns", "Replacing the iron core with wood", "Decreasing the battery voltage"]),
            ("What makes an electromagnet fundamentally superior to a natural permanent magnet in industrial cranes?", "Its magnetic power can be controlled, increased, and turned completely on or off at will by a switch", ["It never requires any electrical power source", "It is made of pure natural diamonds", "It only attracts non-metallic plastics"])
        ],
        "CBSE-8-CURI-4-4.1.4": [
            ("In an electric bell mechanism, what happens the instant the push button switch is pressed?", "Current energizes the electromagnet, which attracts the soft iron armature, causing the hammer to strike the gong", ["The gong melts from heat", "The battery explodes safely", "The bell rings only after an hour"]),
            ("What breaks the electrical circuit immediately after the hammer strikes the gong in a traditional electric bell?", "The armature pulls away from the contact screw, opening the circuit (interrupter mechanism)", ["The battery discharges completely", "The gong detaches from the wall", "The electromagnet permanently burns out"]),
            ("What causes the rhythmic continuous ringing of an electric bell as long as the switch is kept pressed?", "Rapid alternating cycle: circuit closes -> hammer strikes gong -> contact breaks -> spring returns armature -> circuit closes again", ["A small motor rotating the hammer", "The ringing is caused by acoustic resonance of air", "The wire vibrates like a guitar string"]),
            ("Besides electric bells, electromagnets are vital components in which modern technologies?", "Scrap yard cranes for lifting steel, Maglev bullet trains, MRI hospital scanners, and electric relays", ["Non-stick cooking pans", "Simple glass mercury thermometers", "Ordinary wooden pencils"])
        ],
        "CBSE-8-CURI-4-4.2.1": [
            ("What is the fundamental physical cause of the Heating Effect of electric current (Joule heating) in a conductor?", "Collisions between moving conduction electrons and the vibrating atomic lattice ions of the conductor dissipate kinetic energy as heat", ["Electrons melt into thermal liquid", "Protons flow out through the wire surface", "Friction with atmospheric air around the wire"]),
            ("Which mathematical law formulated by James Prescott Joule calculates the heat energy (\\(H\\)) generated in a conductor of resistance \\(R\\) carrying current \\(I\\) for time \\(t\\)?", "\\(H = I^2 \\times R \\times t\\)", ["\\(H = I \\times R \\times t\\)", "\\(H = I^2 / (R \\times t)\\)", "\\(H = R^2 / (I \\times t)\\)"]),
            ("If the electric current flowing through a fixed heating resistor is DOUBLED, by what factor does the heat generated per second increase?", "Increases by a factor of 4 (\\(2^2 = 4\\))", ["Doubles (factor of 2)", "Increases by a factor of 8", "Remains unchanged"]),
            ("Electrical resistance in a conductor is a physical property that measures:", "The opposition offered by the material to the free flow of electric charge (current)", ["The speed of light in vacuum", "The magnetic polarity of atoms", "The weight of copper atoms"])
        ],
        "CBSE-8-CURI-4-4.2.2": [
            ("Why is nichrome wire (an alloy of nickel, chromium, and iron) chosen as the heating element in electric irons and toasters?", "It has very high electrical resistance and high melting point, and does not oxidize (burn) even when glowing red-hot", ["It is the best conductor of electricity like silver", "It melts at low temperatures like ice", "It is cheaper than iron wire"]),
            ("How does the electrical resistance of a metallic wire change when its length is increased and its cross-sectional thickness is reduced?", "Resistance increases directly with length and inversely with cross-sectional area (\\(R \\propto L/A\\))", ["Resistance decreases to zero", "Resistance remains strictly constant", "Resistance doubles then halves"]),
            ("Why does the connecting copper cord of an electric heater remain cool while the heating element inside glows red-hot?", "Copper cord has extremely low electrical resistance (dissipating negligible heat), whereas the heating element has very high resistance", ["Current does not flow through the copper cord", "The copper cord is insulated with refrigeration ice", "Heat travels in only one direction"]),
            ("When a current-carrying nichrome wire glows red hot in air, its temperature reaches approximately:", "Around \\(800^\\circ\\text{C}\\ \\text{to}\\ 1000^\\circ\\text{C}\\)", ["Around \\(50^\\circ\\text{C}\\)", "\\(0^\\circ\\text{C}\\)", "\\(10{,}000^\\circ\\text{C}\\)"])
        ],
        "CBSE-8-CURI-4-4.2.3": [
            ("Which common household appliances utilize the Heating Effect of electric current for their primary operation?", "Electric room heaters, electric water geysers, toasters, and electric clothing irons", ["Electric ceiling fans and refrigerators", "Washing machines and air conditioners", "Computers and mobile screens"]),
            ("In a traditional incandescent light bulb, the glowing filament is made of which refractory metal having an extraordinarily high melting point (\\(3422^\\circ\\text{C}\\))?", "Tungsten", ["Copper", "Aluminium", "Silver"]),
            ("Why is the glass envelope of an incandescent electric bulb filled with chemically inert gases like argon or nitrogen instead of air?", "To prevent the white-hot tungsten filament from rapidly oxidizing and burning out in air", ["To make the bulb lighter than air", "To generate electrical current inside the glass", "To keep the glass freezing cold"]),
            ("Why have modern compact fluorescent lamps (CFLs) and Light Emitting Diodes (LEDs) largely replaced incandescent tungsten bulbs in homes?", "They convert electrical energy directly into light with high luminous efficiency, wasting very little energy as unwanted heat", ["They produce heat instead of light", "They only work on battery power", "They consume ten times more electricity"])
        ],
        "CBSE-8-CURI-4-4.2.4": [
            ("An electric fuse is a critical safety device installed in household circuits to protect against:", "Excessive current surges caused by short circuits or overloading that could cause electrical fires", ["Voltage dropping below zero", "Magnets attracting the appliances", "Lightning striking radio antennas"]),
            ("A fuse wire is manufactured from an alloy (like tin-lead alloy) possessing which specific physical properties?", "Relatively high resistance and an appropriately LOW melting point", ["Low resistance and infinitely high melting point", "Zero resistance and made of pure tungsten", "Made of combustible paper"]),
            ("What physical event occurs inside an electric fuse when a severe short circuit causes a massive current surge?", "Excessive Joule heating (\\(I^2Rt\\)) melts the fuse wire rapidly, breaking the circuit and stopping current flow safely", ["The fuse wire becomes five times thicker", "The fuse stores the excess current in a capacitor", "The fuse wire turns into copper"]),
            ("Modern domestic electrical distribution boards replace traditional replaceable wire fuses with automatic safety switches called:", "Miniature Circuit Breakers (MCBs) which trip open automatically when current exceeds safe limits", ["Rheostats", "Step-down transformers", "Galvanometers"])
        ],
        "CBSE-8-CURI-4-4.3.1": [
            ("What is the primary energy conversion that takes place inside an electrochemical cell (battery)?", "Chemical energy stored in reactants is converted into electrical energy", ["Thermal energy is converted into nuclear energy", "Electrical energy is destroyed into mass", "Sound energy is converted into kinetic energy"]),
            ("An electrochemical cell produces a steady electric potential difference between its two terminals by:", "Driving spontaneous oxidation-reduction (redox) chemical reactions between electrodes and electrolyte", ["Attracting static charge from air", "Generating friction through mechanical wheels", "Absorbing thermal heat from sunlight"]),
            ("The two conductive metal terminals of an electrochemical cell through which current enters and leaves the electrolyte are called:", "Electrodes (Anode and Cathode)", ["Insulators", "Resistors", "Dielectrics"]),
            ("The ionic liquid or gel medium inside a chemical cell that conducts electric current via the migration of ions is termed the:", "Electrolyte", ["Electromagnet", "Dielectric oil", "Capacitor"])
        ],
        "CBSE-8-CURI-4-4.3.2": [
            ("Who invented the world's first true chemical electric battery (the Voltaic Pile) in 1800?", "Alessandro Volta", ["Luigi Galvani", "Michael Faraday", "Thomas Edison"]),
            ("What historic observation by Italian physician Luigi Galvani in 1780 led to the concept of 'animal electricity' and inspired Volta's battery?", "Dissected frog leg muscles twitched convulsively when touched simultaneously by two dissimilar metals (brass and iron)", ["Frogs glowing in darkness", "Electric eels producing fire", "Frogs swimming in saltwater"]),
            ("What were the alternating metal discs and moist electrolyte layers used by Alessandro Volta to construct his historic Voltaic Pile?", "Discs of copper and zinc separated by cardboard discs soaked in brine (saltwater or dilute acid)", ["Discs of gold and silver in pure oil", "Sheets of lead and tin in honey", "Plates of plastic and glass in alcohol"]),
            ("The standard unit of electric potential difference (electromotive force), the Volt (V), was named in honor of:", "Alessandro Volta", ["Luigi Galvani", "Andre-Marie Ampere", "James Watt"])
        ],
        "CBSE-8-CURI-4-4.3.3": [
            ("In an ordinary commercial dry cell (Leclanché dry cell used in flashlights and clocks), what material forms the outer cylindrical container that acts as the ANODE (negative terminal)?", "Zinc metal can", ["Copper cylinder", "Carbon rod", "Aluminium foil"]),
            ("What is the central cylindrical rod in a dry cell that serves as the CATHODE (positive terminal) and is surrounded by black manganese dioxide powder?", "Carbon (graphite) rod with a brass cap", ["Zinc rod", "Lead rod", "Iron needle"]),
            ("Why is it called a 'DRY cell' even though its interior is not completely dry?", "The electrolyte is not a free-flowing liquid, but a moist, non-spillable paste of ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) and zinc chloride", ["It is completely made of dry sand", "It operates only in dry desert heat", "It contains no chemicals at all"]),
            ("What is the standard nominal voltage produced by a fresh single zinc-carbon or alkaline dry cell?", "\\(1.5\\ \\text{V}\\)", ["\\(12\\ \\text{V}\\)", "\\(220\\ \\text{V}\\)", "\\(0.1\\ \\text{V}\\)"])
        ],
        "CBSE-8-CURI-4-4.3.4": [
            ("How does a secondary (rechargeable) battery fundamentally differ from a primary non-rechargeable dry cell?", "Its chemical reactions are electrically reversible; passing an external electric current backwards regenerates the original chemical reactants", ["It never runs out of power", "It contains no chemical electrolyte", "It generates nuclear fusion power"]),
            ("Which heavy-duty rechargeable battery composed of lead plates and dilute sulfuric acid electrolyte has powered automobile vehicle starters for over a century?", "Lead-acid storage battery (typically 12 V)", ["Zinc-carbon dry cell", "Alkaline button cell", "Mercury cell"]),
            ("Which lightweight, high-energy-density rechargeable battery powers modern smartphones, laptops, and electric vehicles (EVs)?", "Lithium-ion (Li-ion) battery", ["Leclanché dry cell", "Nickel-iron battery", "Voltaic pile"]),
            ("Why is proper recycling of spent lead-acid and lithium-ion batteries essential for environmental safety?", "Prevents toxic heavy metal contamination (lead, cobalt, lithium) and corrosive acid pollution in soils and municipal groundwater", ["Old batteries turn into diamonds if buried", "Discarded batteries consume oxygen from air", "Batteries attract lightning strikes"])
        ]
    }

    # Generate Chapters 1, 2, 3, 4
    for ch_num, cases_dict in [(1, ch1_cases), (2, ch2_cases), (3, ch3_cases), (4, ch4_cases)]:
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
                step1 = f"Identify the scientific concept relating to {sub_name}."
                step2 = f"Evaluate key principles: {ctx}"
                step3 = f"Therefore, the correct answer is {ans}."
                q = make_question(tc, sub_name, ctx, ans, wrongs, step1, step2, step3, diffs[i], vaults[i], start_seq)
                start_seq += 1
                ch_questions.append(q)

        out_path = f"scripts/cbse8_curi_ch{ch_num}_topup.json"
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(ch_questions, out_f, indent=2)
        print(f"Generated {len(ch_questions)} questions for Chapter {ch_num} -> {out_path}")

if __name__ == "__main__":
    run()
