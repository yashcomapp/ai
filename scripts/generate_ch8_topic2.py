# scripts/generate_ch8_topic2.py
# Topic: MH-9-SCIT-8-8.2 (Antibiotics: Penicillin, Alexander Fleming, Broad vs Narrow Spectrum)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-8-8.2"
CHAPTER_NUM = 8

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Discovery of Penicillin & Alexander Fleming
    ("In which year did Scottish physician and microbiologist Sir Alexander Fleming discover penicillin?",
     ["1905", "1928", "1953", "1885"],
     "B", "OSC", "easy",
     "- Alexander Fleming made the accidental discovery of penicillin in September 1928 at St. Mary's Hospital in London.\nCorrect Choice is (B)."),

    ("Which bacterial culture plate did Alexander Fleming notice had become contaminated by an airborne green mold?",
     ["Escherichia coli", "Staphylococcus aureus", "Lactobacillus acidophilus", "Rhizobium leguminosarum"],
     "B", "OSC", "easy",
     "- Fleming was researching Staphylococcus aureus (a pathogen causing wound abscesses and boils).\nCorrect Choice is (B)."),

    ("What remarkable observation around the contaminating mold colony led to the discovery of penicillin?",
     ["The bacteria grew faster", "A clear, circular zone where all surrounding staphylococcal bacteria had been lysed and destroyed", "The bacteria turned bright green", "The petri dish melted"],
     "B", "OSC", "easy",
     "- Fleming observed a clear halo (zone of inhibition) where bacteria had disintegrated around the mold.\nCorrect Choice is (B)."),

    ("From which fungal genus was this first life-saving antibiotic chemical isolated?",
     ["Aspergillus", "Penicillium (specifically Penicillium notatum)", "Rhizopus", "Agaricus"],
     "B", "OSC", "easy",
     "- Penicillin was isolated from the green mold Penicillium notatum (now Penicillium chrysogenum).\nCorrect Choice is (B)."),

    ("What are 'Antibiotics' in medical pharmacology?",
     ["Toxic industrial chemical disinfectants", "Carbon compounds obtained from microorganisms (fungi and bacteria) capable of killing or inhibiting the growth of pathogenic bacteria", "Vitamins that give energy", "Synthetic sugar pills"],
     "B", "OSC", "easy",
     "- Antibiotics are secondary metabolites produced by micro-organisms that kill or inhibit other microscopic pathogens.\nCorrect Choice is (B)."),

    ("Which two scientists shared the 1945 Nobel Prize in Medicine alongside Alexander Fleming for successfully purifying and mass-producing penicillin?",
     ["James Watson and Francis Crick", "Howard Florey and Ernst Chain", "Robert Koch and Louis Pasteur", "Gregor Mendel and Charles Darwin"],
     "B", "OSC", "medium",
     "- Howard Florey and Ernst Chain purified stable penicillin, enabling its mass production to save soldiers during World War II.\nCorrect Choice is (B)."),

    ("What fundamental biochemical structure does penicillin destroy or prevent bacteria from building?",
     ["The DNA double helix", "The rigid peptidoglycan cell wall", "The cell's mitochondria", "The flagella motor"],
     "B", "OSC", "medium",
     "- Penicillin inhibits transpeptidase enzymes that cross-link peptidoglycan chains, causing the bacterial cell wall to rupture by osmotic pressure.\nCorrect Choice is (B)."),

    ("Why does penicillin destroy bacterial cells without harming human human host cells?",
     ["Because human cells are too small", "Because human animal cells completely lack a peptidoglycan cell wall, possessing only a flexible plasma membrane", "Because human blood is acidic", "Because penicillin loves humans"],
     "B", "OSC", "medium",
     "- Penicillin exhibits selective toxicity: It targets peptidoglycan synthesis, a structure unique to bacteria and absent in mammalian cells.\nCorrect Choice is (B)."),

    ("Can antibiotics like penicillin kill or cure viral infections such as the common cold, influenza (flu), or dengue?",
     ["Yes, they cure all viral diseases within 24 hours", "No, antibiotics are completely ineffective against viruses because viruses have no cell wall or independent cellular metabolic machinery", "Only if taken with hot tea", "Yes, in very large doses"],
     "B", "OSC", "easy",
     "- Viruses lack peptidoglycan cell walls, ribosomes, and independent metabolic pathways; antibiotics have zero effect on them.\nCorrect Choice is (B)."),

    ("What is an antibiotic that specifically kills bacteria termed in medical terminology?",
     ["Bacteriostatic", "Bactericidal", "Antiseptic", "Analgesic"],
     "B", "OSC", "medium",
     "- Bactericidal agents actively kill bacteria; bacteriostatic agents inhibit bacterial growth and multiplication.\nCorrect Choice is (B)."),

    # 11-20: Broad vs Narrow Spectrum Antibiotics
    ("What is a 'Broad-Spectrum Antibiotic'?",
     ["An antibiotic that kills only one specific bacterial strain", "An antibiotic that is effective against a wide variety of both Gram-positive and Gram-negative bacteria", "An antibiotic that works only in bright sunlight", "A vaccine for infants"],
     "B", "OSC", "easy",
     "- Broad-spectrum antibiotics act against a wide range of diverse bacterial pathogens.\nCorrect Choice is (B)."),

    ("When is a broad-spectrum antibiotic typically prescribed by a medical doctor?",
     ["When the exact causative pathogen is unknown, but symptoms of severe infection are evident (empiric therapy)", "Only when the patient has a mild headache", "When someone wants to gain weight", "Only after the infection is completely healed"],
     "A", "OSC", "easy",
     "- Broad-spectrum agents are deployed when immediate treatment is required before laboratory blood/culture identification results are available.\nCorrect Choice is (A)."),

    ("Which of the following is an example of a widely used Broad-Spectrum Antibiotic?",
     ["Penicillin-G", "Ampicillin / Amoxicillin / Tetracycline", "Erythromycin only", "Insulin"],
     "B", "OSC", "easy",
     "- Ampicillin, amoxicillin, tetracycline, and chloramphenicol are classic broad-spectrum antibiotics.\nCorrect Choice is (B)."),

    ("What is a 'Narrow-Spectrum Antibiotic'?",
     ["An antibiotic that cures every disease", "An antibiotic that targets and kills only a very specific group or limited species of bacteria", "An antibiotic sold in narrow bottles", "A topical cream for cuts"],
     "B", "OSC", "easy",
     "- Narrow-spectrum antibiotics act selectively against specific bacterial families (e.g., only against Gram-positive staphylococci).\nCorrect Choice is (B)."),

    ("Which of the following is a classic example of a Narrow-Spectrum Antibiotic?",
     ["Tetracycline", "Penicillin-G / Gentamicin / Erythromycin", "Amoxicillin", "Ciprofloxacin"],
     "B", "OSC", "medium",
     "- Natural penicillin-G acts almost exclusively against Gram-positive cocci, making it a narrow-spectrum agent.\nCorrect Choice is (B)."),

    ("What major medical risk arises if a patient stops taking their prescribed antibiotic course halfway through because they feel better?",
     ["The medicine expires", "Surviving, partially resistant bacteria multiply rapidly, leading to a relapse of a more severe, drug-resistant infection", "The body becomes allergic to water", "The liver turns into bone"],
     "B", "OSC", "easy",
     "- Incomplete courses eliminate only the most susceptible bacteria, selecting for resistant strains that rebound fiercely.\nCorrect Choice is (B)."),

    ("What are bacterial pathogens that develop genetic resistance to multiple standard antibiotics commonly called?",
     ["Super-bacteria / Superbugs (e.g. MRSA)", "Viruses", "Protozoa", "Yeasts"],
     "A", "OSC", "easy",
     "- Superbugs (like Methicillin-Resistant Staphylococcus aureus / MRSA) carry multiple resistance plasmids against conventional antibiotics.\nCorrect Choice is (A)."),

    ("Which enzyme is produced by resistant staphylococcal bacteria to destroy the penicillin molecule by hydrolyzing its active ring?",
     ["Amylase", "Beta-lactamase (Penicillinase)", "Lipase", "Pepsin"],
     "B", "OSC", "hard",
     "- Beta-lactamase cleaves the essential beta-lactam ring of penicillin, neutralizing its bactericidal ability.\nCorrect Choice is (B)."),

    ("State whether True or False: Antibiotics should be purchased over-the-counter without a registered doctor's prescription whenever one gets a throat ache.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Self-medication drives antibiotic resistance and is ineffective against viral sore throats; antibiotics must only be taken on doctor prescription.\nCorrect Choice is (B)."),

    ("Which of the following is an antibiotic derived from soil actinomycetes (Streptomyces)?",
     ["Penicillin", "Streptomycin", "Aspirin", "Paracetamol"],
     "B", "OSC", "medium",
     "- Selman Waksman discovered streptomycin from the soil bacterium Streptomyces griseus, effective against tuberculosis.\nCorrect Choice is (B)."),

    # 21-30: Clinical Safety & Antimicrobial Mechanisms
    ("Why is taking antibiotics unnecessarily for a simple viral flu harmful to a person's general health?",
     ["It gives too much energy", "It indiscriminately wipes out beneficial probiotic bacteria living in the intestines, causing digestive upset, diarrhea, and promoting resistant superbugs", "It causes tooth decay", "It turns blood blue"],
     "B", "OSC", "easy",
     "- Antibiotics destroy friendly commensal gut flora (like Lactobacilli), allowing opportunistic pathogens to cause colitis.\nCorrect Choice is (B)."),

    ("Which laboratory diagnostic test determines the susceptibility of a clinical bacterial isolate to different antibiotic disks?",
     ["Gram stain", "Kirby-Bauer Disk Diffusion (Antibiotic Sensitivity Test)", "Blood group test", "Biuret test"],
     "B", "OSC", "medium",
     "- The Kirby-Bauer test places paper disks infused with antibiotics on an agar lawn; the diameter of the clear zone measures sensitivity.\nCorrect Choice is (B)."),

    ("What does a larger 'Zone of Inhibition' around an antibiotic disk on an agar plate signify?",
     ["The bacterium is highly resistant to the drug", "The antibiotic is highly effective at inhibiting or killing that bacterial strain", "The antibiotic is expired", "The agar is spoiled"],
     "B", "OSC", "easy",
     "- A wide clear halo indicates high antimicrobial potency and bacterial susceptibility.\nCorrect Choice is (B)."),

    ("Which of the following classes of antibiotics acts by inhibiting bacterial protein synthesis on 70S ribosomes?",
     ["Penicillins", "Tetracyclines and Aminoglycosides", "Beta-lactams", "Cephalosporins"],
     "B", "OSC", "hard",
     "- Tetracyclines and aminoglycosides bind specifically to bacterial 30S ribosomal subunits, halting protein translation.\nCorrect Choice is (B)."),

    ("What is an 'antiseptic' as distinct from an 'antibiotic'?",
     ["Antiseptics are pills swallowed with food", "Antiseptics are topical chemical agents applied externally on living skin to prevent sepsis, whereas antibiotics are administered internally", "Antiseptics are made of sugar", "Antiseptics are only for cleaning floors"],
     "B", "OSC", "medium",
     "- Antiseptics (e.g. iodine, Dettol) are applied externally to living tissues; disinfectants to inanimate surfaces; antibiotics are taken systemically.\nCorrect Choice is (B)."),

    ("What is a 'disinfectant'?",
     ["A medicine injected into veins", "A strong chemical agent (like phenol or bleach) applied strictly to non-living surfaces and surgical instruments to eradicate pathogens", "A sweet syrup", "An edible ointment"],
     "B", "OSC", "easy",
     "- Disinfectants are harsh chemicals used on inanimate objects (floors, instruments) because they are too toxic for living tissue.\nCorrect Choice is (B)."),

    ("Assertion (A): Antibiotic treatment must be continued for the full duration prescribed by the doctor, even if all clinical symptoms disappear within two days.\nReason (R): Premature discontinuation leaves behind the most tolerant bacterial sub-populations, which develop resistance and cause a severe recurring infection.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Completing the entire course ensures that 100% of bacterial cells are cleared, preventing the selection of resistant mutants.\nCorrect Choice is (A)."),

    ("Assertion (A): Penicillin is the first-line treatment for curing viral influenza and dengue fever.\nReason (R): Penicillin destroys the protein coats of viral capsids.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "easy",
     "- Both statements are false. Penicillin has zero action against viruses because viruses have no peptidoglycan cell walls.\nCorrect Choice is (D)."),

    ("Why should one never share or consume leftover antibiotic tablets prescribed for another family member?",
     ["Because the medicine has bad luck", "Different bacterial infections require different specific antibiotics and dosages; incorrect usage promotes resistant strains and causes adverse drug toxicity", "Because tablets become sour", "Because tablets turn into sugar"],
     "B", "OSC", "easy",
     "- Drug specificity, therapeutic dosage, and patient kidney/liver tolerances differ; inappropriate antibiotic use fuels resistance.\nCorrect Choice is (B)."),

    ("Which organ in the human body is primarily responsible for metabolizing and eliminating antibiotics from the bloodstream?",
     ["Heart", "Liver and Kidneys", "Lungs", "Brain"],
     "B", "OSC", "medium",
     "- The liver metabolizes pharmaceuticals and the kidneys excrete drug residues in urine.\nCorrect Choice is (B)."),

    # 31-40: Historical Context & Advanced Concepts
    ("In which country was Sir Alexander Fleming working when he made the historic discovery of penicillin?",
     ["United States", "United Kingdom (Scotland / England)", "Germany", "France"],
     "B", "OSC", "easy",
     "- Fleming was a Scottish biologist working at St. Mary's Hospital Medical School in London, UK.\nCorrect Choice is (B)."),

    ("Which infectious disease of the lungs, caused by Mycobacterium tuberculosis, was treated with breakthrough efficacy by the antibiotic Streptomycin?",
     ["Asthma", "Tuberculosis (TB)", "Bronchitis", "Pneumonia"],
     "B", "OSC", "easy",
     "- Streptomycin was the first effective antibiotic weapon against tuberculosis.\nCorrect Choice is (B)."),

    ("What occurs when agricultural farm animals (poultry, cattle) are routinely fed sub-therapeutic doses of antibiotics as growth promoters?",
     ["Animals grow feathers", "Vast populations of antibiotic-resistant bacteria emerge in farm animals, which transfer to humans through food and water", "Animals become plants", "Animals stop needing food"],
     "B", "OSC", "medium",
     "- Widespread sub-lethal agricultural antibiotic use is a leading global driver of multi-drug resistant superbug strains.\nCorrect Choice is (B)."),

    ("Which of the following is a semi-synthetic derivative of penicillin developed to overcome stomach acid degradation?",
     ["Penicillin-G", "Amoxicillin", "Morphine", "Quinine"],
     "B", "OSC", "medium",
     "- Amoxicillin is an acid-stable, orally active, broad-spectrum aminopenicillin.\nCorrect Choice is (B)."),

    ("State whether True or False: Some patients are severely allergic to penicillin, and an injection can trigger life-threatening anaphylactic shock.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Hypersensitive individuals can suffer fatal anaphylaxis; doctors always test for penicillin allergy before systemic administration.\nCorrect Choice is (A)."),

    ("Identify the odd one out with respect to pharmacological class: Penicillin, Ampicillin, Tetracycline, Paracetamol.",
     ["Penicillin", "Ampicillin", "Tetracycline", "Paracetamol"],
     "D", "OSC", "easy",
     "- Paracetamol is an analgesic and antipyretic (pain/fever reliever); the others are antimicrobial antibiotics.\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to antibiotic spectrum: Amoxicillin, Tetracycline, Ampicillin, Penicillin-G.",
     ["Amoxicillin", "Tetracycline", "Ampicillin", "Penicillin-G"],
     "D", "OSC", "medium",
     "- Penicillin-G is a narrow-spectrum antibiotic; Amoxicillin, Tetracycline, and Ampicillin are broad-spectrum antibiotics.\nCorrect Choice is (D)."),

    ("What is the primary cellular structure that enables bacteria to transfer antibiotic-resistance genes horizontally to other neighboring bacteria?",
     ["Mitochondria", "Conjugation Pilus and Plasmids (R-plasmids)", "Chloroplasts", "Vacuoles"],
     "B", "OSC", "hard",
     "- Resistance plasmids (R-plasmids) are transferred rapidly between bacterial species through bacterial conjugation via sex pili.\nCorrect Choice is (B)."),

    ("Why are fungal and protozoan infections generally much harder to treat with antibiotics than bacterial infections without harming the human patient?",
     ["Because fungi are animals", "Because fungi and protozoa are eukaryotes like humans, sharing similar cellular biochemistry, ribosomes, and membranes", "Because fungi have no cells", "Because protozoa are made of metal"],
     "B", "OSC", "hard",
     "- Finding targets with selective toxicity is difficult in eukaryotic pathogens because their cellular machinery closely mirrors human host cells.\nCorrect Choice is (B)."),

    ("What global health organization coordinates surveillance and action plans against the crisis of Antimicrobial Resistance (AMR)?",
     ["UNESCO", "World Health Organization (WHO)", "Interpol", "NASA"],
     "B", "OSC", "easy",
     "- The World Health Organization (WHO) leads global surveillance and stewardship programs against antimicrobial resistance.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Principles & Discovery
    ("In Alexander Fleming's 1928 experiment, what was the natural biological role of the penicillin chemical produced by the mold in wild environments?",
     ["To provide food for ants", "To eliminate competing soil bacteria in its immediate surroundings and secure nutrients for the fungus", "To make soil salty", "To attract bees"],
     "B", "OSC", "easy",
     "- Microorganisms secrete antibiotics in nature to suppress competing microbes in their ecological micro-niche.\nCorrect Choice is (B)."),

    ("Which of the following bacterial structures is present in Gram-positive bacteria as a thick, protective outer layer targeted by penicillin?",
     ["Cellulose wall", "Peptidoglycan (Murein) meshwork", "Keratin coat", "Chitin wall"],
     "B", "OSC", "medium",
     "- Gram-positive bacteria feature a thick cross-linked peptidoglycan polymer layer that penicillin destabilizes.\nCorrect Choice is (B)."),

    ("What happens to a bacterial cell whose peptidoglycan wall has been weakened by penicillin when it resides in a hypotonic medium like bodily fluids?",
     ["It shrinks into a seed", "Water enters the cell by osmosis; the weakened wall cannot withstand internal turgor pressure, causing the cell to burst (osmotic lysis)", "It turns into a crystal", "It divides ten times faster"],
     "B", "OSC", "hard",
     "- Turgor pressure inside bacteria reaches 10-20 atmospheres; without a cross-linked wall, osmotic influx causes rapid cell lysis.\nCorrect Choice is (B)."),

    ("State whether True or False: Human red blood cells and nerve cells possess peptidoglycan cell walls.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Animal cells never have cell walls; they possess only a flexible phospholipid bilayer membrane.\nCorrect Choice is (B)."),

    ("Which antibiotic was famously mass-produced in giant 10,000-gallon aerated fermentation tanks to treat infected Allied wounded soldiers during World War II?",
     ["Aspirin", "Penicillin", "Insulin", "Cough syrup"],
     "B", "OSC", "easy",
     "- Submerged fermentation of Penicillium chrysogenum in deep tanks saved hundreds of thousands of wounded soldiers from fatal wound gangrene.\nCorrect Choice is (B)."),

    ("A patient visits a clinic with high fever, sore throat, running nose, and sneezing. A swab test confirms viral Influenza. Should the doctor inject penicillin?",
     ["Yes, immediately", "No, because penicillin has zero biological activity against viral infections and its misuse fosters drug-resistant bacteria", "Yes, to make the virus sleep", "Yes, in five doses"],
     "B", "OSC", "easy",
     "- Viral respiratory infections cannot be treated with antibacterial antibiotics; supportive therapy and antivirals are indicated.\nCorrect Choice is (B)."),

    ("What is an 'antibiogram'?",
     ["A drawing of bacteria", "The laboratory profile of a bacterial pathogen's sensitivity or resistance to a battery of antimicrobial drugs", "A medical thermometer", "A blood pressure monitor"],
     "B", "OSC", "medium",
     "- An antibiogram guides physicians to prescribe the most potent, narrowest-spectrum antibiotic tailored to the patient's specific culture.\nCorrect Choice is (B)."),

    ("Which mechanism enables certain resistant bacteria to pump antibiotics out of their cytoplasm before the drug can reach its cellular target?",
     ["Photosynthesis", "Multidrug Efflux Pumps", "Endocytosis", "Phagocytosis"],
     "B", "OSC", "hard",
     "- Active efflux pumps located in the bacterial membrane actively transport antibiotics out of the cell, neutralizing toxicity.\nCorrect Choice is (B)."),

    ("State whether True or False: Broad-spectrum antibiotics kill both harmful bacterial pathogens AND beneficial intestinal bacteria.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Broad-spectrum antibiotics lack specificity, decimating beneficial commensal gut microbes along with the target pathogen.\nCorrect Choice is (A)."),

    ("Why are doctors encouraged to switch from a broad-spectrum antibiotic to a narrow-spectrum antibiotic as soon as culture reports identify the exact bacterium?",
     ["To make the bill cheaper", "To target the specific pathogen directly while sparing the patient's beneficial gut microflora and minimizing resistance selection pressure", "Because narrow antibiotics taste sweet", "Because broad antibiotics expire faster"],
     "B", "OSC", "medium",
     "- Targeted narrow-spectrum therapy preserves commensal microbiomes and curbs the emergence of multi-drug resistance.\nCorrect Choice is (B)."),

    # 51-60: Clinical Practice & Microbial Genetics
    ("What is MRSA, an infamous hospital-acquired pathogen of great clinical concern?",
     ["Methicillin-Resistant Staphylococcus aureus", "A harmless skin virus", "A green marine alga", "A beneficial probiotic in yogurt"],
     "A", "OSC", "easy",
     "- MRSA is a virulent hospital strain resistant to methicillin, penicillin, and related beta-lactam antibiotics.\nCorrect Choice is (A)."),

    ("How do bacteria acquire new antibiotic-resistance genes through horizontal gene transfer?",
     ["By drinking water", "Through conjugation (plasmid transfer), transformation (uptake of free DNA), and transduction (bacteriophage viruses)", "By staying warm", "By breathing clean air"],
     "B", "OSC", "hard",
     "- Horizontal gene transfer allows rapid sharing of resistance genes across distinct bacterial lineages.\nCorrect Choice is (B)."),

    ("Which antibiotic was isolated from the soil fungus Cephalosporium acremonium, functioning similarly to penicillin?",
     ["Cephalosporin", "Aspirin", "Morphine", "Quinine"],
     "A", "OSC", "medium",
     "- Cephalosporins are beta-lactam antibiotics structurally related to penicillins, effective against broad bacterial spectra.\nCorrect Choice is (A)."),

    ("When a person experiences severe watery diarrhea following a prolonged 2-week course of strong broad-spectrum antibiotics, what has most likely occurred?",
     ["The body has run out of water", "The antibiotic destroyed the protective normal intestinal flora, permitting the opportunistic pathogen Clostridium difficile to overgrow and cause colitis", "The liver has dissolved", "The stomach became too acidic"],
     "B", "OSC", "hard",
     "- Decimation of commensal gut microbiota allows antibiotic-resistant Clostridium difficile to proliferate, releasing colitis-inducing toxins.\nCorrect Choice is (B)."),

    ("Why is taking a probiotic supplement (containing Lactobacilli) frequently recommended during or after a heavy course of antibiotics?",
     ["To make the medicine work faster", "To help recolonize and restore the beneficial bacterial population in the digestive tract", "To absorb the antibiotic pills", "To change the patient's blood type"],
     "B", "OSC", "easy",
     "- Probiotics replenish the depleted gut microbiome, re-establishing digestive balance and competitive barrier defense.\nCorrect Choice is (B)."),

    ("Which antibiotic, commonly prescribed in pediatrics for ear, nose, and throat infections, is often combined with clavulanic acid to block bacterial beta-lactamase?",
     ["Augmentin (Amoxicillin + Clavulanic acid)", "Insulin", "Paracetamol", "Chloroquine"],
     "A", "OSC", "hard",
     "- Clavulanic acid is a suicide beta-lactamase inhibitor that protects amoxicillin from enzymatic degradation by resistant bacteria.\nCorrect Choice is (A)."),

    ("State whether True or False: Taking antibiotics with cold tap water makes them permanently poisonous.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Antibiotics should be taken with normal potable water according to prescription schedules.\nCorrect Choice is (B)."),

    ("What is the term for a natural chemical substance that prevents the multiplication of bacteria without directly killing them outright?",
     ["Bactericidal", "Bacteriostatic", "Carcinogenic", "Mutagenic"],
     "B", "OSC", "medium",
     "- Bacteriostatic drugs halt bacterial population growth, giving the host immune system time to clear the infection.\nCorrect Choice is (B)."),

    ("Why are pregnant women advised to exercise extreme caution with certain antibiotics like Tetracycline?",
     ["Tetracycline is made of gold", "Tetracycline chelates with calcium and permanently discolors the developing teeth and bones of the fetus", "It turns hair pink", "It causes colds"],
     "B", "OSC", "hard",
     "- Tetracycline binds to calcium during fetal odontogenesis, causing permanent brown/gray tooth staining and enamel hypoplasia.\nCorrect Choice is (B)."),

    ("Fill in the blank: The specialized laboratory disc used in Kirby-Bauer sensitivity testing is made of sterile _______ paper.",
     ["Filter (Cellulose)", "Wax", "Sand", "Plastic"],
     "A", "OFB", "easy",
     "- Standardized absorbent cellulose filter paper discs impregnated with known drug microgram quantities are used.\nCorrect Choice is (A)."),

    # 61-70: Synthesis & Global Perspectives
    ("If an antibiotic sensitivity test shows zero clear zone (zone of inhibition = 0 mm) around an ampicillin disc on a bacterial lawn, how is that bacterium classified?",
     ["Highly sensitive", "Completely resistant", "Dead", "Beneficial"],
     "B", "OSC", "easy",
     "- Bacteria growing right up to the disc edge are completely resistant to that drug concentration.\nCorrect Choice is (B)."),

    ("Assertion (A): Antibiotics are among the greatest medical breakthroughs in human history, drastically extending average human life expectancy in the 20th century.\nReason (R): Prior to antibiotics, common bacterial infections (such as pneumonia, tuberculosis, and minor infected scratches) were frequently fatal.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- The advent of antibiotics transformed previously lethal bacterial infections into easily curable clinical conditions.\nCorrect Choice is (A)."),

    ("Assertion (A): If you feel 100% healthy on day 3 of a 7-day antibiotic course, it is safe and recommended to discard the remaining tablets.\nReason (R): Consuming unnecessary medicine damages the blood.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "easy",
     "- Stopping midway leaves the hardiest sub-lethal bacteria alive to acquire full drug resistance; courses must always be completed.\nCorrect Choice is (D)."),

    ("What is 'empirical antibiotic therapy'?",
     ["Treating with herbal leaves", "Initiating treatment with a broad-spectrum antibiotic based on clinical presentation before microbiological culture results return", "Taking no medicine", "Surgery"],
     "B", "OSC", "medium",
     "- Empirical therapy covers probable pathogens immediately in acute infections while awaiting laboratory confirmation.\nCorrect Choice is (B)."),

    ("Which of the following is NOT an antibiotic?",
     ["Erythromycin", "Penicillin", "Insulin (a peptide hormone regulating glucose)", "Tetracycline"],
     "C", "OSC", "easy",
     "- Insulin is an endocrine peptide hormone produced by the pancreas, not an antimicrobial antibiotic.\nCorrect Choice is (C)."),

    ("Which antibiotic was historically used as an ointment on the eyes of newborn babies to prevent neonatal gonococcal conjunctivitis?",
     ["Erythromycin / Silver nitrate", "Penicillin injection", "Aspirin", "Paracetamol"],
     "A", "OSC", "medium",
     "- Prophylactic ophthalmic erythromycin ointment prevents blindness from birth-canal bacterial exposure.\nCorrect Choice is (A)."),

    ("What does 'antibiotic stewardship' mean in hospital management?",
     ["Selling as many antibiotics as possible", "Systematic hospital policies and physician guidance to optimize antibiotic selection, dosing, and duration to curb drug resistance", "Throwing all antibiotics away", "Giving antibiotics without tests"],
     "B", "OSC", "medium",
     "- Antimicrobial stewardship optimizes clinical outcomes while minimizing unintended consequences like toxicity and resistance.\nCorrect Choice is (B)."),

    ("State whether True or False: Microorganisms like Penicillium produce antibiotics in order to help humans recover from fever.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Fungi produce antibiotics as natural chemical defenses to inhibit competing microbes in their soil environment; human use is an adaptation of nature.\nCorrect Choice is (B)."),

    ("What was the primary obstacle that prevented Alexander Fleming from using penicillin to treat patients immediately in 1928?",
     ["He lost his laboratory", "Penicillin was extremely unstable in liquid broth and chemically difficult to isolate and purify in concentrated quantities with 1920s chemistry techniques", "Nobody believed him", "Bacteria died out"],
     "B", "OSC", "hard",
     "- Fleming could not chemically stabilize or mass-extract the delicate molecule; Florey and Chain solved this decade-long purification hurdle in Oxford.\nCorrect Choice is (B)."),

    ("Which term describes an infection acquired by a patient inside a hospital environment, which often involves multi-drug resistant bacterial strains?",
     ["Nosocomial infection (Hospital-acquired infection)", "Genetic disease", "Congenital defect", "Nutritional deficiency"],
     "A", "OSC", "medium",
     "- Nosocomial infections occur in clinical settings where heavy antibiotic pressure selects for resistant superbug strains.\nCorrect Choice is (A).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Fleming's Historic Petri Dish (Inhibition Halo)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Alexander Fleming's Petri Dish (1928)</text>
  <!-- Petri Dish Outer Glass -->
  <circle cx="110" cy="115" r="75" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- Agar Base -->
  <circle cx="110" cy="115" r="70" fill="#334155"/>
  <!-- Penicillium Mold Colony at top center -->
  <circle cx="110" cy="80" r="16" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <text x="85" y="60" fill="#4ade80" font-size="8.5" font-weight="bold">Penicillium Mold</text>
  <!-- Clear Zone of Inhibition (No bacteria!) -->
  <circle cx="110" cy="80" r="38" fill="none" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="75" y="108" fill="#fde047" font-size="7.5" font-weight="bold">Clear Inhibition Halo</text>
  <!-- Staph Colonies far away (Yellow dots) -->
  <circle cx="75" cy="145" r="4" fill="#facc15"/>
  <circle cx="95" cy="155" r="4" fill="#facc15"/>
  <circle cx="120" cy="150" r="4" fill="#facc15"/>
  <circle cx="145" cy="140" r="4" fill="#facc15"/>
  <circle cx="155" cy="115" r="4" fill="#facc15"/>
  <text x="85" y="175" fill="#facc15" font-size="8">Staphylococcus aureus</text>
  <!-- Observation Box on Right -->
  <rect x="200" y="45" width="145" height="135" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="210" y="65" fill="#38bdf8" font-size="9.5" font-weight="bold">Fleming's Insight:</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="8">- Penicillium mold secreted</text>
  <text x="210" y="98" fill="#cbd5e1" font-size="8">  a soluble bactericidal</text>
  <text x="210" y="110" fill="#fde047" font-size="8">  chemical: PENICILLIN</text>
  <text x="210" y="128" fill="#34d399" font-size="8">- Lysed & killed adjacent</text>
  <text x="210" y="140" fill="#34d399" font-size="8">  Staph colonies</text>
  <text x="210" y="160" fill="#fb7185" font-size="8.5">Dawn of modern antibiotics</text>
  <text x="45" y="205" fill="#38bdf8" font-size="9.5">The clear zone confirmed that the mold produced an active antibacterial substance</text>
</svg>
</div>
In the historic petri dish observation illustrated above, what proved to Alexander Fleming that the green mold was producing a potent antibacterial substance?""",
     ["The bacteria changed color into bright blue",
      "A clear circular zone of inhibition formed around the mold where all adjacent staphylococcal colonies were lysed and dissolved",
      "The mold grew roots into the glass",
      "The agar gel turned into water"],
     "B", "OSC", "easy",
     "- The clear halo (zone of inhibition) free of bacterial growth proved that the mold secreted a diffusible bactericidal agent.\nCorrect Choice is (B)."),

    # 72: Penicillin Cell Wall Mechanism & Osmotic Lysis
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="60" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Penicillin Mechanism: Osmotic Lysis</text>
  <!-- Normal Intact Bacterium -->
  <rect x="25" y="55" width="130" height="85" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="75" fill="#34d399" font-size="9" font-weight="bold">Normal Cell Wall</text>
  <rect x="35" y="85" width="110" height="40" rx="10" fill="#166534" stroke="#22c55e" stroke-width="3"/>
  <text x="45" y="108" fill="#ffffff" font-size="8">Rigid Peptidoglycan</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8">Withstands 20 atm pressure</text>
  <!-- Penicillin Treated Bacterium (Rupturing) -->
  <rect x="180" y="55" width="135" height="85" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="75" fill="#f87171" font-size="9" font-weight="bold">+ Penicillin Treatment</text>
  <!-- Broken wall with herniating cytoplasm -->
  <path d="M 195,95 C 195,85 240,85 260,90 C 270,80 290,95 285,115 C 280,130 250,125 230,125 C 200,125 195,115 195,95 Z" fill="#991b1b" stroke="#ef4444" stroke-dasharray="3,2"/>
  <text x="210" y="105" fill="#fca5a5" font-size="8">Wall cross-links blocked</text>
  <text x="190" y="150" fill="#f87171" font-size="8">Osmotic Influx ➔ Cell Bursts!</text>
  <text x="45" y="185" fill="#fde047" font-size="9">Penicillin inhibits transpeptidase enzymes synthesizing the cell wall</text>
  <text x="45" y="198" fill="#cbd5e1" font-size="8">Human cells lack peptidoglycan walls and are completely unharmed</text>
</svg>
</div>
Why does penicillin cause multiplying bacteria to burst (undergo osmotic lysis) without harming human body cells?""",
     ["Because penicillin freezes the cell",
      "Because penicillin inhibits peptidoglycan cell wall cross-linking; human cells lack cell walls and are unaffected",
      "Because human cells have no water",
      "Because bacteria have no DNA"],
     "B", "OSC", "medium",
     "- Selective toxicity: Peptidoglycan is unique to bacterial cell walls. Weakened walls rupture under internal osmotic turgor pressure.\nCorrect Choice is (B)."),

    # 73: Broad vs Narrow Spectrum Activity Matrix
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Broad-Spectrum vs Narrow-Spectrum</text>
  <!-- Broad Spectrum Column -->
  <rect x="25" y="50" width="145" height="135" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="70" fill="#38bdf8" font-size="10.5" font-weight="bold">BROAD-SPECTRUM</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- Gram(+) AND Gram(-)</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8.5">- Wide range of pathogens</text>
  <text x="35" y="120" fill="#fde047" font-size="8.5">- Used when cause unknown</text>
  <text x="35" y="138" fill="#f87171" font-size="8">- May disturb gut flora</text>
  <text x="35" y="158" fill="#38bdf8" font-size="8.5" font-weight="bold">e.g. Amoxicillin, Tetracycline</text>
  <!-- Narrow Spectrum Column -->
  <rect x="190" y="50" width="145" height="135" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="200" y="70" fill="#34d399" font-size="10.5" font-weight="bold">NARROW-SPECTRUM</text>
  <text x="200" y="90" fill="#cbd5e1" font-size="8.5">- Highly selective target</text>
  <text x="200" y="105" fill="#cbd5e1" font-size="8.5">- Only Gram(+) OR Gram(-)</text>
  <text x="200" y="120" fill="#fde047" font-size="8.5">- Used after culture test</text>
  <text x="200" y="138" fill="#34d399" font-size="8">- Preserves gut microbiome</text>
  <text x="200" y="158" fill="#34d399" font-size="8.5" font-weight="bold">e.g. Penicillin-G, Gentamicin</text>
  <text x="45" y="202" fill="#fde047" font-size="9.5">Spectrum choice balances rapid empirical coverage vs preserving gut health</text>
</svg>
</div>
When a patient has a severe, acute bacterial infection but laboratory culture results identifying the exact bacterium will take 48 hours, which type of antibiotic does the doctor prescribe initially?""",
     ["A narrow-spectrum antibiotic", "A broad-spectrum antibiotic (like Amoxicillin)", "A sugar tablet", "A virus vaccine"],
     "B", "OSC", "easy",
     "- Broad-spectrum antibiotics provide immediate empiric coverage against diverse Gram-positive and Gram-negative pathogens.\nCorrect Choice is (B)."),

    # 74: Kirby-Bauer Sensitivity Disk Test
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Kirby-Bauer Disk Diffusion Test</text>
  <!-- Agar Plate Circle -->
  <circle cx="110" cy="110" r="70" fill="#334155" stroke="#64748b" stroke-width="2"/>
  <!-- Bacterial Lawn (Beige background) -->
  <circle cx="110" cy="110" r="65" fill="#ca8a04" opacity="0.6"/>
  <!-- Disk 1: Highly Sensitive (Large clear halo) -->
  <circle cx="85" cy="85" r="24" fill="#0f172a"/>
  <circle cx="85" cy="85" r="6" fill="#ffffff" stroke="#0f172a"/>
  <text x="82" y="88" fill="#0f172a" font-size="7" font-weight="bold">A</text>
  <text x="50" y="65" fill="#34d399" font-size="7.5" font-weight="bold">Sensitive (Large Halo)</text>
  <!-- Disk 2: Resistant (Zero halo! Bacteria touch disk) -->
  <circle cx="140" cy="135" r="6" fill="#ffffff" stroke="#0f172a"/>
  <text x="137" y="138" fill="#0f172a" font-size="7" font-weight="bold">B</text>
  <text x="125" y="160" fill="#f87171" font-size="7.5" font-weight="bold">Resistant (Zero Halo)</text>
  <!-- Explanation Box -->
  <rect x="200" y="45" width="125" height="130" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="208" y="65" fill="#fde047" font-size="9" font-weight="bold">Diagnostic Key:</text>
  <text x="208" y="85" fill="#34d399" font-size="8">- Disk A: Potent!</text>
  <text x="208" y="98" fill="#cbd5e1" font-size="7.5">  Wide inhibition zone</text>
  <text x="208" y="120" fill="#f87171" font-size="8">- Disk B: Ineffective!</text>
  <text x="208" y="133" fill="#cbd5e1" font-size="7.5">  Bacteria grow over it</text>
  <text x="208" y="155" fill="#38bdf8" font-size="7.5">Guides exact RX drug</text>
  <text x="45" y="198" fill="#fde047" font-size="9">Halo diameter directly indicates microbial susceptibility to that antibiotic</text>
</svg>
</div>
In the antibiotic susceptibility test shown above, why is Antibiotic [A] chosen to treat the patient rather than Antibiotic [B]?""",
     ["Because Disk B is smaller",
      "Because Disk A produces a wide clear zone of inhibition, proving the bacterium is highly susceptible to it, while Disk B shows complete resistance",
      "Because Disk A is cheaper",
      "Because Disk B contains poison"],
     "B", "OSC", "easy",
     "- A wide clear halo indicates effective bacterial inhibition; zero halo proves the bacterial strain is completely resistant.\nCorrect Choice is (B)."),

    # 75: Danger of Incomplete Antibiotic Course
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="55" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Why You Must Finish the Full 7-Day Course</text>
  <!-- Day 1-3 -->
  <rect x="20" y="48" width="85" height="110" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="28" y="66" fill="#38bdf8" font-size="8.5" font-weight="bold">Day 1 - 3</text>
  <text x="25" y="85" fill="#cbd5e1" font-size="7.5">- Susceptible bugs die</text>
  <text x="25" y="100" fill="#cbd5e1" font-size="7.5">- Symptoms fade</text>
  <text x="25" y="120" fill="#fde047" font-size="7.5" font-weight="bold">Patient feels fine!</text>
  <!-- Stopped Early Error -->
  <rect x="115" y="48" width="105" height="110" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="122" y="66" fill="#f87171" font-size="8.5" font-weight="bold">Stopped at Day 3 ✗</text>
  <text x="120" y="85" fill="#fca5a5" font-size="7.5">- Tougher bugs survive</text>
  <text x="120" y="100" fill="#fca5a5" font-size="7.5">- Gain resistance</text>
  <text x="120" y="120" fill="#ef4444" font-size="7.5" font-weight="bold">RELAPSE OF</text>
  <text x="120" y="132" fill="#ef4444" font-size="7.5" font-weight="bold">SUPERBUGS!</text>
  <!-- Completed Course -->
  <rect x="230" y="48" width="95" height="110" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="238" y="66" fill="#34d399" font-size="8.5" font-weight="bold">Day 7 Finished ✓</text>
  <text x="235" y="85" fill="#cbd5e1" font-size="7.5">- 100% bugs killed</text>
  <text x="235" y="100" fill="#cbd5e1" font-size="7.5">- Zero survivors</text>
  <text x="235" y="120" fill="#34d399" font-size="7.5" font-weight="bold">Full Cure,</text>
  <text x="235" y="132" fill="#34d399" font-size="7.5" font-weight="bold">Zero Resistance</text>
  <text x="35" y="180" fill="#fde047" font-size="9">Incomplete treatment breeds drug-resistant superbugs</text>
  <text x="35" y="195" fill="#cbd5e1" font-size="8">Always finish the exact number of days prescribed by the doctor</text>
</svg>
</div>
What dangerous consequence occurs if a patient discontinues their antibiotic course on Day 3 simply because their fever has subsided?""",
     ["The tablets turn into poison in the box",
      "Only the most sensitive bacteria were killed; the hardier partially resistant bacteria survive, multiply into an incurable resistant infection, and relapse",
      "The body becomes immune to all food",
      "The fever never returns"],
     "B", "OSC", "easy",
     "- Premature cessation kills only weak microbes, selecting for resistant strains that rebound in a more virulent, drug-refractory form.\nCorrect Choice is (B)."),

    # 76: Bacterial Beta-Lactamase Resistance
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Enzymatic Resistance: Beta-Lactamase</text>
  <!-- Penicillin Molecule with Beta-lactam ring -->
  <rect x="25" y="55" width="130" height="80" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="75" fill="#38bdf8" font-size="9" font-weight="bold">Active Penicillin</text>
  <rect x="50" y="85" width="35" height="30" fill="#0369a1" stroke="#38bdf8"/>
  <text x="55" y="103" fill="#ffffff" font-size="7">β-Lactam</text>
  <text x="35" y="125" fill="#34d399" font-size="8">Intact: Kills bacteria</text>
  <!-- Attack by Beta-Lactamase scissors -->
  <text x="160" y="95" fill="#f87171" font-size="16">✂</text>
  <text x="145" y="75" fill="#f87171" font-size="7.5">β-Lactamase</text>
  <!-- Broken Inactive Penicillin -->
  <rect x="185" y="55" width="130" height="80" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="195" y="75" fill="#f87171" font-size="9" font-weight="bold">Broken Penicilloic Acid</text>
  <path d="M 210,85 L 230,85 L 240,115 L 210,115" stroke="#ef4444" stroke-width="2" fill="none"/>
  <text x="195" y="125" fill="#fca5a5" font-size="8">Ring cleaved: INACTIVE!</text>
  <text x="45" y="165" fill="#fde047" font-size="9">Resistant bacteria secrete enzymes that destroy the antibiotic</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="8">Overcome by adding inhibitors like Clavulanic Acid (Augmentin)</text>
</svg>
</div>
How do penicillin-resistant bacteria biochemically disarm the penicillin antibiotic before it can damage their cell wall?""",
     ["By freezing the drug",
      "By producing the enzyme Beta-lactamase (penicillinase), which breaks the essential beta-lactam chemical ring of penicillin",
      "By eating the doctor's prescription",
      "By escaping into the air"],
     "B", "OSC", "medium",
     "- Resistant bacteria secrete beta-lactamase enzymes that hydrolyze the critical four-membered beta-lactam ring, destroying antimicrobial action.\nCorrect Choice is (B)."),

    # 77: Antibiotics Ineffective Against Viruses
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Why Antibiotics Cannot Cure Viruses</text>
  <!-- Bacterium (Target of Antibiotic) -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="10" font-weight="bold">BACTERIUM (Cellular)</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8">- Peptidoglycan cell wall</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8">- 70S Ribosomes</text>
  <text x="35" y="120" fill="#cbd5e1" font-size="8">- Independent metabolism</text>
  <text x="35" y="145" fill="#34d399" font-size="9" font-weight="bold">✓ ANTIBIOTIC TARGET</text>
  <!-- Virus (Non-cellular, No Target!) -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="70" fill="#f87171" font-size="10" font-weight="bold">VIRUS (Acellular)</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8">- NO cell wall</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="8">- NO ribosomes</text>
  <text x="190" y="120" fill="#cbd5e1" font-size="8">- Hijacks human cells</text>
  <text x="190" y="145" fill="#ef4444" font-size="9" font-weight="bold">✗ ZERO EFFECT!</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Never take antibiotics for common cold, viral flu, or dengue fever</text>
</svg>
</div>
Based on the structural contrast illustrated above, why do antibiotics have zero curative effect on the common cold, flu, or dengue virus?""",
     ["Because viruses are too fast to catch",
      "Because viruses have no peptidoglycan cell walls, ribosomes, or independent metabolic enzymes for antibiotics to target",
      "Because viruses eat antibiotics",
      "Because viruses live only in winter"],
     "B", "OSC", "easy",
     "- Antibiotics target specific bacterial cellular structures (cell walls, bacterial ribosomes). Viruses lack these and are unaffected.\nCorrect Choice is (B)."),

    # 78: Bactericidal vs Bacteriostatic Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Bactericidal vs Bacteriostatic Action</text>
  <!-- Bactericidal -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="70" fill="#f87171" font-size="10" font-weight="bold">BACTERICIDAL</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- Actively KILLS bacteria</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8.5">- Irreversible destruction</text>
  <text x="35" y="120" fill="#cbd5e1" font-size="8.5">- e.g. Penicillin, Vancomycin</text>
  <text x="35" y="145" fill="#f87171" font-size="9" font-weight="bold">Kills even weak patients</text>
  <!-- Bacteriostatic -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="190" y="70" fill="#facc15" font-size="10" font-weight="bold">BACTERIOSTATIC</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8.5">- INHIBITS multiplication</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="8.5">- Halts protein synthesis</text>
  <text x="190" y="120" fill="#cbd5e1" font-size="8.5">- e.g. Tetracycline, Sulfa</text>
  <text x="190" y="145" fill="#fde047" font-size="9" font-weight="bold">Relies on host immunity</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Bactericidal directly destroys; Bacteriostatic pauses growth for immune clearance</text>
</svg>
</div>
What is the functional difference between a 'Bactericidal' antibiotic and a 'Bacteriostatic' antibiotic?""",
     ["Bactericidal drugs freeze cells; bacteriostatic drugs heat them",
      "Bactericidal antibiotics actively kill bacteria directly; bacteriostatic antibiotics inhibit bacterial multiplication, allowing the immune system to eliminate them",
      "Both are identical in action",
      "Bacteriostatic antibiotics kill viruses"],
     "B", "OSC", "easy",
     "- Bactericidal agents cause irreversible bacterial cell death; bacteriostatic agents halt cell replication without killing existing cells directly.\nCorrect Choice is (B)."),

    # 79: Gram-Positive vs Gram-Negative Wall Target
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Gram(+) vs Gram(-) Cell Envelope Barrier</text>
  <!-- Gram Positive (Thick naked Peptidoglycan) -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#c084fc" rx="4"/>
  <text x="35" y="70" fill="#c084fc" font-size="9.5" font-weight="bold">GRAM-POSITIVE</text>
  <rect x="35" y="80" width="115" height="25" fill="#a855f7"/>
  <text x="40" y="96" fill="#fff" font-size="8">Thick Peptidoglycan (exposed)</text>
  <rect x="35" y="110" width="115" height="15" fill="#0284c7"/>
  <text x="45" y="122" fill="#fff" font-size="7.5">Plasma Membrane</text>
  <text x="35" y="145" fill="#fde047" font-size="8">Highly vulnerable to Penicillin</text>
  <!-- Gram Negative (Outer Protective Membrane) -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="190" y="70" fill="#fb7185" font-size="9.5" font-weight="bold">GRAM-NEGATIVE</text>
  <rect x="190" y="80" width="115" height="12" fill="#ef4444"/>
  <text x="195" y="90" fill="#fff" font-size="7.5">Outer LPS Membrane (Shield)</text>
  <rect x="190" y="95" width="115" height="10" fill="#a855f7"/>
  <text x="195" y="103" fill="#fff" font-size="7">Thin Peptidoglycan</text>
  <rect x="190" y="108" width="115" height="12" fill="#0284c7"/>
  <text x="195" y="118" fill="#fff" font-size="7.5">Plasma Membrane</text>
  <text x="190" y="145" fill="#f87171" font-size="8">Blocks natural Penicillin-G</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Outer lipopolysaccharide membrane shields Gram(-) bacteria from standard penicillin</text>
</svg>
</div>
Why was natural Penicillin-G ineffective against most Gram-negative bacteria (like E. coli), necessitating the development of broad-spectrum amoxicillin?""",
     ["Because Gram-negative bacteria have no DNA",
      "Because Gram-negative bacteria have an extra outer lipopolysaccharide membrane that blocks standard penicillin from reaching the peptidoglycan wall",
      "Because Gram-negative bacteria eat penicillin",
      "Because Gram-negative bacteria are too cold"],
     "B", "OSC", "hard",
     "- The outer lipopolysaccharide membrane of Gram-negative bacteria acts as a permeability barrier, excluding hydrophobic Penicillin-G.\nCorrect Choice is (B)."),

    # 80: The Global Superbug Epidemic (AMR)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Drivers of Antimicrobial Resistance</text>
  <!-- Driver 1 -->
  <rect x="25" y="50" width="290" height="32" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="35" y="70" fill="#f87171" font-size="9" font-weight="bold">1. Over-prescription for viral colds & flu</text>
  <!-- Driver 2 -->
  <rect x="25" y="88" width="290" height="32" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="35" y="108" fill="#f87171" font-size="9" font-weight="bold">2. Stopping courses midway when symptoms fade</text>
  <!-- Driver 3 -->
  <rect x="25" y="126" width="290" height="32" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="35" y="146" fill="#f87171" font-size="9" font-weight="bold">3. Massive overuse in livestock and poultry feed</text>
  <text x="45" y="180" fill="#fde047" font-size="9.5" font-weight="bold">Result: Pan-resistant Superbugs with zero effective cure</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="8">Responsible antibiotic stewardship is a global public health imperative</text>
</svg>
</div>
Which human practice is a primary driver accelerating the emergence of antibiotic-resistant superbugs worldwide?""",
     ["Drinking clean boiled water",
      "Over-prescribing antibiotics for viral illnesses, stopping courses prematurely, and feeding antibiotics to healthy farm livestock",
      "Washing hands with soap",
      "Exercising outdoors"],
     "B", "OSC", "easy",
     "- Unnecessary clinical misuse and agricultural sub-therapeutic dosing create intense selective pressure for antibiotic resistance.\nCorrect Choice is (B)."),

    # 81: Historical Legacy: Howard Florey & Ernst Chain
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">From Lab Curiosity to Miracle Medicine</text>
  <!-- Step 1: Fleming 1928 -->
  <rect x="25" y="50" width="85" height="110" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="32" y="70" fill="#fde047" font-size="9" font-weight="bold">1. Fleming (1928)</text>
  <text x="30" y="90" fill="#cbd5e1" font-size="7.5">- Discovers mold</text>
  <text x="30" y="105" fill="#cbd5e1" font-size="7.5">- Observes zone</text>
  <text x="30" y="120" fill="#cbd5e1" font-size="7.5">- Cannot purify</text>
  <!-- Step 2: Florey & Chain 1940 -->
  <rect x="125" y="50" width="95" height="110" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="130" y="70" fill="#38bdf8" font-size="8.5" font-weight="bold">2. Florey/Chain (1940)</text>
  <text x="130" y="90" fill="#cbd5e1" font-size="7.5">- Freeze-drying</text>
  <text x="130" y="105" fill="#cbd5e1" font-size="7.5">- Chemical stability</text>
  <text x="130" y="120" fill="#cbd5e1" font-size="7.5">- First human cures</text>
  <!-- Step 3: Industrial Scale 1944 -->
  <rect x="235" y="50" width="85" height="110" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="240" y="70" fill="#34d399" font-size="9" font-weight="bold">3. Mass Scale (1944)</text>
  <text x="240" y="90" fill="#cbd5e1" font-size="7.5">- Deep vats</text>
  <text x="240" y="105" fill="#cbd5e1" font-size="7.5">- Corn steep liquor</text>
  <text x="240" y="120" fill="#34d399" font-size="7.5">- Saves WWII troops</text>
  <text x="50" y="195" fill="#fde047" font-size="9.5">Shared the 1945 Nobel Prize in Physiology or Medicine</text>
</svg>
</div>
Who solved the difficult chemical purification and freeze-drying challenge that turned Alexander Fleming's mold broth into stable, injectable medicine?""",
     ["Howard Florey and Ernst Chain", "Louis Pasteur", "Gregor Mendel", "Charles Darwin"],
     "A", "OSC", "easy",
     "- Florey and Chain purified and stabilized penicillin at Oxford, proving its curative power in human clinical trials.\nCorrect Choice is (A)."),

    # 82: Golden Rules of Antibiotic Stewardship
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Golden Rules of Antibiotic Safety</text>
  <!-- Rule 1 -->
  <rect x="20" y="42" width="320" height="38" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="30" y="58" fill="#34d399" font-size="9.5" font-weight="bold">1. Doctor's Prescription Only:</text>
  <text x="30" y="72" fill="#cbd5e1" font-size="8.5">Never buy or consume antibiotics over the counter without medical diagnosis</text>
  <!-- Rule 2 -->
  <rect x="20" y="85" width="320" height="38" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="30" y="101" fill="#fde047" font-size="9.5" font-weight="bold">2. Complete the Full Course:</text>
  <text x="30" y="115" fill="#cbd5e1" font-size="8.5">Never stop early when symptoms fade; eradicate 100% of bacterial cells</text>
  <!-- Rule 3 -->
  <rect x="20" y="128" width="320" height="42" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="30" y="144" fill="#f87171" font-size="9.5" font-weight="bold">3. Never Take for Viral Infections:</text>
  <text x="30" y="158" fill="#cbd5e1" font-size="8.5">Ineffective against common cold, flu, and dengue; only damages healthy gut flora</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Safeguarding miracle drugs for future human generations</text>
</svg>
</div>
According to the golden rules of antibiotic safety, what must a patient always do when prescribed an antibiotic course?""",
     ["Stop taking the tablets as soon as fever drops on day 2",
      "Complete the entire prescribed dosage and duration, even after feeling completely better",
      "Share leftover pills with neighbors",
      "Take double the dose to heal in 1 hour"],
     "B", "OSC", "easy",
     "- Completing the full prescribed regimen ensures total eradication of pathogens, preventing the selection of drug-resistant mutants.\nCorrect Choice is (B).")
]

# Generate questions list
all_questions = []

# 1-40 Exam
for i, item in enumerate(exam_data, start=1):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}" if item[3] == "OSC" else (
            f"{TOPIC_CODE}-OMC-{i:03d}" if item[3] == "OMC" else (
            f"{TOPIC_CODE}-OTF-{i:03d}" if item[3] == "OTF" else (
            f"{TOPIC_CODE}-OAR-{i:03d}" if item[3] == "OAR" else (
            f"{TOPIC_CODE}-OFB-{i:03d}" if item[3] == "OFB" else f"{TOPIC_CODE}-ONE-{i:03d}"))))
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
        {"text": "True", "isCorrect": (item[2] == "A")},
        {"text": "False", "isCorrect": (item[2] == "B")}
    ]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

# 41-70 Practice
for i, item in enumerate(practice_data, start=41):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}" if item[3] == "OSC" else (
            f"{TOPIC_CODE}-OMC-{i:03d}" if item[3] == "OMC" else (
            f"{TOPIC_CODE}-OTF-{i:03d}" if item[3] == "OTF" else (
            f"{TOPIC_CODE}-OAR-{i:03d}" if item[3] == "OAR" else (
            f"{TOPIC_CODE}-OFB-{i:03d}" if item[3] == "OFB" else f"{TOPIC_CODE}-ONE-{i:03d}"))))
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
        {"text": "True", "isCorrect": (item[2] == "A")},
        {"text": "False", "isCorrect": (item[2] == "B")}
    ]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

# 71-82 Mock / Foundation (with Diagrams)
for i, item in enumerate(mock_data, start=71):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "mock", "foundation", item[5]))

out_file = "scripts/ch8_topic2.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
