# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-8-8.3: Harmful Microbes: Clostridium & Other Pathogens
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json
import os
import re

TOPIC_CODE = "MH-9-SCIT-8-8.3"
OUTPUT_FILE = "scripts/ch8_topic3.json"

exam_data = [
    {
        "q": "Which genus of bacteria is characterized by rod-shaped, strictly anaerobic bacilli that produce heat-resistant endospores?",
        "options": ["Lactobacillus", "Clostridium", "Rhizobium", "Saccharomyces"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Clostridium is a genus of anaerobic, rod-shaped bacteria capable of forming durable, heat-resistant endospores that survive adverse environmental conditions."
    },
    {
        "q": "Clostridium botulinum thrives and produces lethal toxins primarily in which kind of environment?",
        "options": ["Highly aerated boiling broth", "Strictly anaerobic sealed foods or canned goods", "Direct sunlight and dry open air", "Acidic citrus fruits with pH below 3"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Clostridium botulinum is an obligate anaerobe; it cannot grow in the presence of oxygen and produces botulinum neurotoxin in improperly canned or airtight packaged food."
    },
    {
        "q": "Which of the following diseases is caused by Clostridium tetani entering through deep puncture wounds or lacerations?",
        "options": ["Tetanus (lockjaw)", "Typhoid", "Tuberculosis", "Amoebic dysentery"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Clostridium tetani spores enter through deep wounds contaminated with soil or rust. In anaerobic conditions within damaged tissue, they germinate and produce tetanospasmin, causing tetanus (lockjaw)."
    },
    {
        "q": "Which disease is transmitted by the female Anopheles mosquito vector?",
        "options": ["Dengue", "Malaria", "Swine Flu", "Chikungunya"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Malaria is transmitted from person to person through the bite of an infected female Anopheles mosquito carrying Plasmodium parasites."
    },
    {
        "q": "The dengue virus is transmitted to humans by which specific mosquito species?",
        "options": ["Culex pipiens", "Aedes aegypti", "Anopheles stephensi", "Mansonia annulifera"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Dengue is an acute viral disease transmitted by the bite of daytime-active female Aedes aegypti mosquitoes."
    },
    {
        "q": "Which pathogen is responsible for causing typhoid fever in humans?",
        "options": ["Vibrio cholerae", "Salmonella typhi", "Mycobacterium tuberculosis", "Plasmodium vivax"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Typhoid fever is an enteric bacterial infection caused by Salmonella typhi, transmitted via contaminated food and water."
    },
    {
        "q": "What diagnostic clinical test is widely used to confirm typhoid fever by detecting antibodies against Salmonella antigens?",
        "options": ["ELISA test", "Widal test", "Mantoux test", "Western blot test"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Widal agglutination test is the classic serological examination used to diagnose typhoid by detecting antibodies against O and H antigens of Salmonella typhi."
    },
    {
        "q": "Which virus is the causative agent of Swine Flu?",
        "options": ["H5N1", "H1N1 influenza virus", "Rhinovirus", "Human Papillomavirus"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Swine flu is an acute respiratory infection caused by the Influenza A subtype H1N1 virus."
    },
    {
        "q": "What is the primary mode of transmission of Hepatitis A virus?",
        "options": ["Bite of infected sandflies", "Contaminated food and drinking water", "Direct contact with infected plant sap", "Inhalation of fungal basidiospores"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Hepatitis A is transmitted primarily through the fecal-oral route via food and water contaminated with the feces of an infected person."
    },
    {
        "q": "Which fungal pathogen causes ringworm (dermatophytosis), characterized by circular itchy skin lesions?",
        "options": ["Saccharomyces cerevisiae", "Trichophyton and Microsporum", "Penicillium notatum", "Rhizobium leguminosarum"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Ringworm is not caused by a worm; it is a fungal infection of keratinized tissue caused by dermatophytes such as Trichophyton and Microsporum."
    },
    {
        "q": "Which organ in the human body is primarily attacked and inflamed by Hepatitis viruses?",
        "options": ["Kidneys", "Liver", "Lungs", "Spleen"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Hepatitis literally means inflammation of the liver, resulting in jaundice, dark urine, and liver dysfunction."
    },
    {
        "q": "Which of the following symptoms is a hallmark diagnostic feature of acute Dengue fever?",
        "options": ["Rapid drop in blood platelet count (thrombocytopenia)", "Sudden increase in erythrocyte count", "Severe paralysis of the vocal cords", "Excessive insulin secretion"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Dengue fever frequently leads to thrombocytopenia (a rapid and severe decline in blood platelet count), increasing the risk of hemorrhages."
    },
    {
        "q": "Why are Clostridium species able to survive prolonged boiling and exposure to harsh chemicals?",
        "options": ["They produce thick cellulose outer jackets", "They form highly resilient, dehydrated endospores", "They possess eukaryotic nuclear membranes", "They secrete digestive enzymes that neutralize heat"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Clostridium forms endospores protected by a thick proteinaceous spore coat, dipicolinic acid, and a dehydrated core, granting extraordinary resistance to heat, radiation, and disinfectants."
    },
    {
        "q": "What kind of paralysis is caused by botulinum toxin produced by Clostridium botulinum?",
        "options": ["Flaccid paralysis (inability of muscles to contract)", "Spastic paralysis (uncontrolled muscle spasm)", "Hyperactive reflex tremors", "Permanent skeletal ossification"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Botulinum toxin cleaves SNARE proteins at presynaptic motor terminals, preventing acetylcholine release and leading to symmetric, descending flaccid paralysis."
    },
    {
        "q": "How does tetanospasmin (tetanus toxin) cause continuous muscle contraction (lockjaw)?",
        "options": ["It blocks the release of inhibitory neurotransmitters (GABA and glycine)", "It accelerates acetylcholine breakdown at the synaptic cleft", "It prevents ATP synthesis in motor neurons", "It destroys postsynaptic acetylcholine receptors"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Tetanospasmin travels retrograde to spinal inhibitory interneurons and blocks the release of glycine and GABA, removing inhibitory control and causing sustained, painful spastic contractions."
    },
    {
        "q": "Which of the following bacteria causes cholera, leading to profuse watery diarrhea and rapid dehydration?",
        "options": ["Salmonella typhi", "Vibrio cholerae", "Clostridium perfringens", "Shigella dysenteriae"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Vibrio cholerae is a comma-shaped bacterium that colonizes the small intestine and secretes cholera enterotoxin, causing rice-water diarrhea and life-threatening dehydration."
    },
    {
        "q": "What is the primary intervention required to treat severe dehydration caused by cholera?",
        "options": ["Immediate high-protein diet", "Oral Rehydration Solution (ORS) containing electrolytes and glucose", "Antiviral corticosteroid tablets", "Fasting and restriction of all fluid intake"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Oral Rehydration Salts (ORS) provide glucose and electrolytes (sodium, potassium, chloride, citrate) that harness the sodium-glucose cotransporter in the gut to rapidly restore body fluids."
    },
    {
        "q": "Which bacterium is the causative agent of tuberculosis (TB)?",
        "options": ["Corynebacterium diphtheriae", "Mycobacterium tuberculosis", "Streptococcus pneumoniae", "Bordetella pertussis"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Tuberculosis is an infectious granulomatous disease caused by the acid-fast bacterium Mycobacterium tuberculosis, predominantly affecting the lungs."
    },
    {
        "q": "What is the global public health treatment strategy for tuberculosis that ensures supervised medication compliance?",
        "options": ["DOTS (Directly Observed Treatment, Short-course)", "BCG lifelong injection therapy", "ORS rehydration regimen", "Widal monitoring protocol"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "DOTS (Directly Observed Treatment, Short-course) is the WHO-recommended strategy where health workers observe patients swallowing each dose of anti-TB drugs."
    },
    {
        "q": "Which of the following organisms causes amoebiasis (amoebic dysentery)?",
        "options": ["Plasmodium vivax", "Entamoeba histolytica", "Trypanosoma gambiense", "Giardia lamblia"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Entamoeba histolytica is an enteric protozoan parasite that invades the mucosal lining of the large intestine, causing amoebic dysentery with bloody mucus-laden stools."
    },
    {
        "q": "Which stage of the Plasmodium parasite is injected into the human bloodstream during the bite of a female Anopheles mosquito?",
        "options": ["Merozoite", "Sporozoite", "Trophozoite", "Gametocyte"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Infective sporozoites residing in the salivary glands of the female Anopheles mosquito are injected into the host's bloodstream and rapidly travel to the liver."
    },
    {
        "q": "The periodic chills and shivering accompanied by high fever in malaria occur due to the release of which substance when erythrocytes rupture?",
        "options": ["Bilirubin", "Hemozoin toxin", "Hemoglobin A", "Tetanospasmin"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "When infected red blood cells rupture, mature merozoites and the toxic malarial pigment hemozoin are released into circulation, triggering release of endogenous pyrogens and periodic chills/fever."
    },
    {
        "q": "Select ALL characteristics that correctly describe the genus Clostridium:",
        "options": [
            "Obligate or aerotolerant anaerobes",
            "Produce resilient endospores",
            "Synthesize chlorophyll a and conduct photosynthesis",
            "Capable of producing potent protein exotoxins"
        ],
        "ans": [0, 1, 3],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Clostridium species are strictly or aerotolerant anaerobic, endospore-forming rod-shaped bacteria that synthesize powerful exotoxins. They are heterotrophic and do not contain chlorophyll."
    },
    {
        "q": "Select ALL diseases caused by pathogenic viruses:",
        "options": [
            "Dengue",
            "Swine Flu (H1N1)",
            "Typhoid",
            "Hepatitis B"
        ],
        "ans": [0, 1, 3],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Dengue, Swine Flu, and Hepatitis B are all viral diseases. Typhoid is caused by the bacterium Salmonella typhi."
    },
    {
        "q": "Select ALL diseases that are transmitted by insect or arthropod vectors:",
        "options": [
            "Malaria",
            "Dengue",
            "Tuberculosis",
            "Amoebiasis"
        ],
        "ans": [0, 1],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Malaria (Anopheles mosquito) and Dengue (Aedes mosquito) are vector-borne diseases. Tuberculosis is transmitted by airborne aerosols, and amoebiasis through contaminated food and water."
    },
    {
        "q": "True or False: Clostridium botulinum can only multiply and release toxins when abundant free oxygen is available.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Clostridium botulinum is an obligate anaerobe; atmospheric oxygen inhibits its growth. It thrives strictly in oxygen-depleted (anaerobic) environments."
    },
    {
        "q": "True or False: Ringworm is caused by an intestinal parasitic roundworm.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Ringworm (tinea) is caused by fungal dermatophytes, not by helminth worms."
    },
    {
        "q": "True or False: The female Anopheles mosquito requires blood meals to obtain proteins needed for developing her eggs.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Male mosquitoes feed exclusively on plant nectar; only female mosquitoes bite and feed on vertebrate blood to nurture their developing eggs."
    },
    {
        "q": "True or False: Proper commercial canning relies on autoclaving food under steam pressure at 121 deg C to kill heat-resistant bacterial endospores.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Simple boiling at 100 deg C fails to destroy Clostridium endospores; moist heat autoclaving at 121 deg C for 15-20 minutes under 15 psi pressure kills endospores reliably."
    },
    {
        "q": "True or False: Antibiotics are the frontline cure for viral infections like Dengue and Swine Flu.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Antibiotics specifically target bacterial cell structures (cell walls, bacterial ribosomes) and have zero efficacy against viruses."
    },
    {
        "q": "Assertion (A): Canned food containers showing swollen or bulging lids must never be consumed and should be discarded immediately.\\nReason (R): Anaerobic fermentation by Clostridium species produces gas along with hazardous botulinum neurotoxins.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Both statements are true. Gas accumulation from anaerobic microbial growth deforms the can, indicating viable contamination and presence of lethal botulinum toxin."
    },
    {
        "q": "Assertion (A): Standing water in open containers, discarded tires, and coolers should be drained weekly.\\nReason (R): Aedes aegypti mosquitoes breed in clean, stagnant water collections around residential premises.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Eliminating stagnant domestic water breaks the reproductive life cycle of Aedes mosquitoes, preventing outbreaks of dengue and chikungunya."
    },
    {
        "q": "Assertion (A): Tetanus toxoid vaccination provides active artificial immunity against tetanus.\\nReason (R): Inactivated tetanus toxin (toxoid) stimulates the host immune system to generate specific protective antibodies and memory cells.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "The toxoid vaccine uses chemically detoxified tetanospasmin that retains antigenicity, inducing long-term neutralising antibodies without causing pathology."
    },
    {
        "q": "Fill in the blank: The comma-shaped bacterium responsible for Asiatic cholera is ________ cholerae.",
        "options": ["Vibrio", "Bacillus", "Spirillum", "Lactobacillus"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Vibrio cholerae is the scientific name of the causative agent of cholera, exhibiting characteristic curved or comma morphology."
    },
    {
        "q": "Fill in the blank: The primary vector transmitting the malarial parasite Plasmodium is the female ________ mosquito.",
        "options": ["Anopheles", "Aedes", "Culex", "Mansonia"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The female Anopheles mosquito is the definitive host and biological vector for Plasmodium species."
    },
    {
        "q": "Fill in the blank: Food poisoning caused specifically by the ingestion of neurotoxin produced by Clostridium is called ________.",
        "options": ["botulism", "tetanus", "typhoid", "cholera"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Botulism is the precise medical term for intoxication caused by Clostridium botulinum neurotoxin."
    },
    {
        "q": "Fill in the blank: The vaccine administered to newborn infants to provide immunity against tuberculosis is the ________ vaccine.",
        "options": ["BCG", "DPT", "MMR", "OPV"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "BCG (Bacillus Calmette-Guérin) is an attenuated live vaccine derived from Mycobacterium bovis that confers protection against severe childhood tuberculosis."
    },
    {
        "q": "Fill in the blank: The microscopic stage of Plasmodium that infects and multiplies inside human liver cells (hepatocytes) is called a ________.",
        "options": ["sporozoite", "gametocyte", "oocyst", "trophozoite"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "Sporozoites travel directly to the liver parenchyma upon inoculation and invade hepatocytes to begin exo-erythrocytic schizogony."
    },
    {
        "q": "If the temperature danger zone for microbial growth in perishable food is 5 deg C to 60 deg C, what is the temperature range span (in deg C) over which harmful bacteria multiply most rapidly?",
        "options": ["55", "50", "65", "60"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The span is 60 - 5 = 55 deg C. Keeping food outside this zone (below 5 deg C or above 60 deg C) suppresses microbial proliferation."
    },
    {
        "q": "Standard autoclaving for destroying bacterial endospores requires heating at 121 deg C under 15 psi pressure for approximately how many minutes?",
        "options": ["15", "5", "45", "60"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Standard medical and laboratory autoclaving guidelines specify 121 deg C for 15 to 20 minutes under 15 psi of saturated steam."
    }
]

practice_data = [
    {
        "q": "Which shape best describes bacteria belonging to the genus Clostridium under light microscopy?",
        "options": ["Spherical cocci in clusters", "Rod-shaped bacilli, often with swollen ends", "Spiral-shaped spirochetes", "Star-shaped aggregates"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Clostridium are elongated rod-shaped bacilli. When forming endospores, the terminal or subterminal spore causes the cell to swell into a drumstick or bottle shape."
    },
    {
        "q": "Which species of Clostridium is notorious for causing gas gangrene and tissue necrosis?",
        "options": ["Clostridium perfringens", "Clostridium butyricum", "Clostridium acetobutylicum", "Lactobacillus acidophilus"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Clostridium perfringens produces alpha toxin and gas within ischemic wound tissue, causing gas gangrene (myonecrosis)."
    },
    {
        "q": "Why is honey unsafe to feed to infants under 12 months of age?",
        "options": ["It contains high acidity that erodes tooth enamel", "It may contain Clostridium botulinum endospores that colonize infant intestines", "It lacks sufficient dietary fiber", "It contains active yeast that ferments milk"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Infant botulism occurs when infants ingest honey containing Clostridium botulinum spores; their undeveloped gut flora cannot prevent spore germination."
    },
    {
        "q": "Which virus causes Bird Flu?",
        "options": ["H5N1 avian influenza virus", "H1N1 virus", "Hepatitis C virus", "Varicella zoster"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Avian influenza is primarily caused by influenza A virus subtype H5N1, which circulates naturally among wild aquatic birds and infects domestic poultry."
    },
    {
        "q": "What is the primary target immune cell destroyed by the Human Immunodeficiency Virus (HIV)?",
        "options": ["Erythrocytes", "CD4+ helper T-lymphocytes", "Platelets", "Osteoclasts"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "HIV selectively infects and depletes CD4+ helper T cells, crippling cell-mediated immunity and leading to AIDS."
    },
    {
        "q": "Which disease is transmitted via respiratory droplets released during coughing or sneezing by an infected individual?",
        "options": ["Tuberculosis", "Amoebic dysentery", "Tetanus", "Malaria"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Tuberculosis and influenza are spread via aerosolized respiratory droplet nuclei when an infected patient coughs, sneezes, or speaks."
    },
    {
        "q": "What is the main transmission vector for the Zika virus and Chikungunya virus, alongside Dengue?",
        "options": ["Aedes mosquito", "Housefly (Musca domestica)", "Head louse", "Tick (Ixodes)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Aedes aegypti and Aedes albopictus serve as the primary urban vectors transmitting Dengue, Chikungunya, and Zika viruses."
    },
    {
        "q": "Which disease is characterized by stiffness of jaw muscles followed by painful involuntary spasms of the neck and facial muscles (risus sardonicus)?",
        "options": ["Tetanus", "Typhoid", "Cholera", "Polio"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Trismus (lockjaw) and risus sardonicus (grimacing facial spasm) are classical early diagnostic symptoms of tetanus."
    },
    {
        "q": "Which protozoan parasite causes sleeping sickness (African trypanosomiasis)?",
        "options": ["Trypanosoma brucei", "Plasmodium falciparum", "Entamoeba histolytica", "Leishmania donovani"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Trypanosoma brucei, transmitted by the bite of the tsetse fly (Glossina), causes African sleeping sickness."
    },
    {
        "q": "Which microbial disease is effectively eradicated or prevented by the OPV and IPV vaccines?",
        "options": ["Poliomyelitis", "Typhoid", "Dengue", "Malaria"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Oral Poliovirus Vaccine (Sabin/OPV) and Inactivated Poliovirus Vaccine (Salk/IPV) have been instrumental in eradicating poliomyelitis globally."
    },
    {
        "q": "Which of the following is an effective vector control method against mosquito breeding in stagnant ponds?",
        "options": ["Introducing Gambusia (larvivorous fish) into water bodies", "Adding sucrose syrup to open drains", "Covering water bodies with dark soil", "Aerating water with pure nitrogen gas"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Biological control using Gambusia affinis (mosquitofish) is an environmentally safe method because they voraciously consume mosquito larvae."
    },
    {
        "q": "What type of organism is responsible for producing athlete's foot (tinea pedis)?",
        "options": ["Dermatophyte fungus", "Protozoan cyst", "Gram-negative bacillus", "Retrovirus"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Athlete's foot is a common cutaneous fungal infection caused by dermatophytes that feed on keratin in moist epidermal layers."
    },
    {
        "q": "Which hepatitis virus is transmitted through infected blood transfusions and contaminated hypodermic needles rather than food/water?",
        "options": ["Hepatitis B and C", "Hepatitis A", "Hepatitis E", "Rotavirus"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Hepatitis B and C are parenteral and blood-borne pathogens, whereas Hepatitis A and E are enteric viruses spread through contaminated food and water."
    },
    {
        "q": "In the malaria parasite lifecycle, where does sexual reproduction (syngamy and sporogony) take place?",
        "options": ["Inside the stomach/gut of the female Anopheles mosquito", "Inside human liver hepatocytes", "Inside human circulating red blood cells", "Inside human lymph nodes"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "The sexual cycle (gamete fusion forming ookinetes and oocysts) occurs in the midgut of the female Anopheles mosquito, making the mosquito the definitive host."
    },
    {
        "q": "What is the primary symptom of Kala-azar (visceral leishmaniasis)?",
        "options": ["Enlargement of spleen and liver (hepatosplenomegaly) and persistent fever", "Acute paralysis of thumb flexors", "Rapid shedding of hair", "Excessive calcium deposition in lungs"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Kala-azar, caused by Leishmania donovani and spread by sandflies, causes irregular bouts of fever, substantial weight loss, anemia, and massive enlargement of the spleen and liver."
    },
    {
        "q": "Select ALL measures that prevent the spread of water-borne pathogens like Vibrio cholerae and Salmonella typhi:",
        "options": [
            "Boiling drinking water or using chlorine disinfection",
            "Consuming hygienically prepared, freshly cooked food",
            "Leaving uncovered food in open street stalls",
            "Washing hands thoroughly with soap before meals"
        ],
        "ans": [0, 1, 3],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Boiling water, eating clean hot food, and washing hands interrupt the fecal-oral route of enteric transmission."
    },
    {
        "q": "Select ALL statements that correctly compare Clostridium tetani and Clostridium botulinum:",
        "options": [
            "Both are spore-forming Gram-positive anaerobic bacilli",
            "C. botulinum toxin causes flaccid paralysis",
            "C. tetani toxin causes spastic paralysis and sustained spasms",
            "Both bacteria are harmless commensals in human saliva"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Both are spore-forming anaerobic rods producing neurotoxins with opposite physiological manifestations: botulinum prevents muscle contraction (flaccid), while tetanospasmin prevents relaxation (spastic)."
    },
    {
        "q": "Select ALL pathogenic protozoans:",
        "options": [
            "Plasmodium",
            "Entamoeba",
            "Lactobacillus",
            "Leishmania"
        ],
        "ans": [0, 1, 3],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Plasmodium, Entamoeba, and Leishmania are pathogenic protozoans. Lactobacillus is a beneficial probiotic bacterium."
    },
    {
        "q": "True or False: Botulinum toxin is considered one of the most lethal biological neurotoxins known to science.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. With a lethal dose measured in nanograms per kilogram, botulinum toxin is among the most potent biological poisons known."
    },
    {
        "q": "True or False: Hepatitis B can be effectively prevented through active vaccination.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The recombinant Hepatitis B vaccine produces high protective antibody titers and is a routine childhood immunization."
    },
    {
        "q": "True or False: Dengue fever is also colloquialized as 'breakbone fever' due to intense muscle, bone, and joint aches.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Severe myalgia, arthralgia, and retro-orbital headache earned dengue the descriptive name 'breakbone fever'."
    },
    {
        "q": "True or False: Anopheles mosquitoes bite almost exclusively in broad daylight during midday.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "False. Anopheles mosquitoes are nocturnal or crepuscular biters (dusk to dawn). Aedes mosquitoes are daytime biters."
    },
    {
        "q": "Assertion (A): Patients infected with cholera require urgent oral rehydration therapy (ORT).\\nReason (R): Cholera toxin causes massive secretion of water and electrolytes into the intestinal lumen, causing life-threatening hypovolemic shock if untreated.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Cholera toxin stimulates adenylate cyclase, leading to hypersecretion of chloride ions and massive osmotic water loss into the gut. ORT replaces lost fluids and electrolytes."
    },
    {
        "q": "Assertion (A): Pasteurization of milk destroys vegetative pathogens like Mycobacterium and Salmonella.\\nReason (R): Pasteurization sterilizes liquids completely by eradicating every bacterial endospore.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 2,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Pasteurization kills vegetative pathogenic bacteria without altering nutritional quality, but it does NOT kill all endospores or achieve complete commercial sterility."
    },
    {
        "q": "Fill in the blank: The characteristic posture of an Anopheles mosquito when resting on a wall is at an angle of roughly ________ degrees to the surface.",
        "options": ["45", "90", "0", "180"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Anopheles mosquitoes rest with their abdomen tilted upward at roughly a 45-degree angle to the surface, unlike Culex which rests parallel."
    },
    {
        "q": "Fill in the blank: The Mantoux skin test is used as a screening tool for detecting exposure to ________.",
        "options": ["tuberculosis", "typhoid", "malaria", "dengue"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "The Mantoux tuberculin skin test evaluates delayed-type hypersensitivity to tuberculin purified protein derivative (PPD) to screen for tuberculosis."
    },
    {
        "q": "Fill in the blank: The toxic metabolic byproduct released during the rupture of malarial schizonts in red blood cells that triggers cyclical chills is ________.",
        "options": ["hemozoin", "bilirubin", "toxoid", "histamine"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "Hemozoin, the crystalline insoluble disposal form of heme produced by Plasmodium, induces fever and chills upon erythrocyte lysis."
    },
    {
        "q": "Fill in the blank: Ringworm lesions commonly present as circular, erythematous, itchy patches known clinically as ________.",
        "options": ["tinea", "edema", "carbuncle", "abscess"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Tinea is the clinical terminology for superficial fungal dermatophyte infections (such as tinea corporis or tinea pedis)."
    },
    {
        "q": "If a healthy adult's normal platelet count is approximately 250,000 per microliter and a severe dengue infection drops it to 50,000 per microliter, by what percentage has the platelet count declined?",
        "options": ["80", "50", "20", "75"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The drop is 250,000 - 50,000 = 200,000. Percentage drop = (200,000 / 250,000) * 100 = 80%."
    },
    {
        "q": "In high-temperature short-time (HTST) pasteurization, milk is heated to 72 deg C for how many seconds before rapid chilling?",
        "options": ["15", "60", "120", "5"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "HTST pasteurization heats milk to 71.7 deg C to 72 deg C for exactly 15 seconds, followed by swift refrigeration below 4 deg C."
    }
]

svg_diagrams = [
    # SVG 1: Clostridium endospore rod
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="28" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Clostridium Morphology &amp; Terminal Endospore</text>
  <!-- Rod with terminal spore -->
  <g transform="translate(40, 60)">
    <!-- Vegetative cell body -->
    <rect x="50" y="45" width="220" height="50" rx="25" fill="#3b82f6" stroke="#93c5fd" stroke-width="2"/>
    <text x="140" y="75" fill="#ffffff" font-size="12" font-family="sans-serif" font-weight="bold">Vegetative Bacillus</text>
    <!-- Swollen terminal endospore -->
    <circle cx="270" cy="70" r="38" fill="#e11d48" stroke="#fecdd3" stroke-width="3"/>
    <circle cx="270" cy="70" r="26" fill="#fbbf24" stroke="#fef08a" stroke-width="2"/>
    <text x="270" y="74" fill="#0f172a" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">Endospore</text>
    <!-- Labels -->
    <path d="M 270 32 L 270 12 L 320 12" fill="none" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="325" y="15" fill="#f8fafc" font-size="11" font-family="sans-serif">Dehydrated core (Heat Resistant)</text>
    <path d="M 120 95 L 120 120 L 60 120" fill="none" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="55" y="135" fill="#93c5fd" font-size="11" font-family="sans-serif">Anaerobic rod (Clostridium tetani / botulinum)</text>
  </g>
</svg>''',

    # SVG 2: Bacteria vs Virus Structure
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Bacterial Cell vs Viral Particle Architecture</text>
  <!-- Bacterium -->
  <g transform="translate(30, 45)">
    <rect x="10" y="20" width="160" height="90" rx="40" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Nucleoid -->
    <path d="M 40 65 Q 60 45 80 65 T 120 65 T 140 65" fill="none" stroke="#34d399" stroke-width="3"/>
    <!-- Flagellum -->
    <path d="M 10 65 Q -15 40 -30 70 T -50 65" fill="none" stroke="#10b981" stroke-width="2"/>
    <text x="90" y="130" fill="#10b981" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Bacterium (Cellular)</text>
    <text x="90" y="146" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Cell wall, Ribosomes, DNA loop</text>
  </g>
  <!-- Divider -->
  <line x1="250" y1="40" x2="250" y2="210" stroke="#334155" stroke-dasharray="4"/>
  <!-- Virus -->
  <g transform="translate(280, 45)">
    <!-- Capsid icosahedron / envelope -->
    <circle cx="100" cy="65" r="45" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <!-- Genetic core -->
    <path d="M 85 65 Q 100 50 115 65 T 100 80" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <!-- Spikes -->
    <line x1="100" y1="20" x2="100" y2="8" stroke="#f43f5e" stroke-width="2"/>
    <circle cx="100" cy="6" r="3" fill="#f43f5e"/>
    <line x1="145" y1="65" x2="157" y2="65" stroke="#f43f5e" stroke-width="2"/>
    <circle cx="159" cy="65" r="3" fill="#f43f5e"/>
    <line x1="55" y1="65" x2="43" y2="65" stroke="#f43f5e" stroke-width="2"/>
    <circle cx="41" cy="65" r="3" fill="#f43f5e"/>
    <text x="100" y="130" fill="#f43f5e" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Virus (Acellular)</text>
    <text x="100" y="146" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Protein capsid + RNA/DNA only</text>
  </g>
</svg>''',

    # SVG 3: Mosquito vectors (Aedes vs Anopheles)
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="26" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Vector Comparison: Aedes vs Anopheles Mosquito</text>
  <!-- Aedes -->
  <g transform="translate(50, 55)">
    <rect x="0" y="0" width="170" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="85" y="24" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Aedes aegypti</text>
    <text x="15" y="55" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; White striped body / legs</text>
    <text x="15" y="75" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; Day biter (early morning)</text>
    <text x="15" y="95" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; Breeds in clean stagnant water</text>
    <text x="15" y="125" fill="#fbbf24" font-size="11" font-family="sans-serif" font-weight="bold">Transmits: Dengue, Chikungunya</text>
  </g>
  <!-- Anopheles -->
  <g transform="translate(280, 55)">
    <rect x="0" y="0" width="170" height="150" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="85" y="24" fill="#c084fc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Anopheles mosquito</text>
    <text x="15" y="55" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; Rests tilted at 45 deg angle</text>
    <text x="15" y="75" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; Night / dusk-to-dawn biter</text>
    <text x="15" y="95" fill="#f8fafc" font-size="11" font-family="sans-serif">&#8226; Spotted wings</text>
    <text x="15" y="125" fill="#f43f5e" font-size="11" font-family="sans-serif" font-weight="bold">Transmits: Malaria (Plasmodium)</text>
  </g>
</svg>''',

    # SVG 4: Plasmodium Lifecycle
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Human Stages of Plasmodium (Malarial Parasite) Lifecycle</text>
  <!-- Step 1: Mosquito bite -->
  <rect x="20" y="50" width="90" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="65" y="75" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1. Sporozoite</text>
  <text x="65" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Injected via saliva</text>
  <!-- Arrow -->
  <path d="M 115 85 L 140 85" stroke="#f8fafc" stroke-width="2" marker-end="url(#arr)"/>
  <!-- Step 2: Liver -->
  <rect x="145" y="50" width="95" height="70" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="192" y="75" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">2. Liver Stage</text>
  <text x="192" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Asexual Schizogony</text>
  <!-- Arrow -->
  <path d="M 245 85 L 270 85" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 3: RBC ring stage -->
  <rect x="275" y="50" width="100" height="70" rx="6" fill="#1e293b" stroke="#f59e0b"/>
  <text x="325" y="75" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">3. RBC Stage</text>
  <text x="325" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Trophozoite / Ring</text>
  <!-- Arrow -->
  <path d="M 380 85 L 405 85" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 4: Rupture & Hemozoin -->
  <rect x="410" y="50" width="80" height="70" rx="6" fill="#1e293b" stroke="#f43f5e"/>
  <text x="450" y="75" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">4. Lysis</text>
  <text x="450" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Hemozoin &#8594; Chills</text>
  <!-- Bottom summary banner -->
  <rect x="30" y="145" width="440" height="70" rx="8" fill="#334155"/>
  <text x="250" y="172" fill="#fef08a" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Clinical Hallmark: Periodic Chills &amp; High Fever</text>
  <text x="250" y="195" fill="#f8fafc" font-size="11" font-family="sans-serif" text-anchor="middle">Occurs every 48-72 hours when RBCs burst simultaneously releasing hemozoin</text>
</svg>''',

    # SVG 5: Dengue thrombocytopenia graph
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Clinical Course of Dengue: Platelet Count vs Disease Day</text>
  <!-- Axes -->
  <line x1="60" y1="190" x2="450" y2="190" stroke="#64748b" stroke-width="2"/>
  <line x1="60" y1="40" x2="60" y2="190" stroke="#64748b" stroke-width="2"/>
  <text x="250" y="215" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Days from Onset of Fever (Days 1 to 10)</text>
  <text x="20" y="120" fill="#94a3b8" font-size="10" font-family="sans-serif" transform="rotate(-90 20,120)" text-anchor="middle">Platelet Count</text>
  <!-- Normal reference line -->
  <line x1="60" y1="70" x2="450" y2="70" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="350" y="65" fill="#10b981" font-size="10" font-family="sans-serif">Normal Range (&gt;150,000 / &#956;L)</text>
  <!-- Platelet drop curve -->
  <path d="M 60 75 Q 160 80 220 160 T 310 165 T 440 85" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <!-- Critical Phase highlight -->
  <rect x="200" y="45" width="120" height="140" fill="#f43f5e" fill-opacity="0.15"/>
  <text x="260" y="110" fill="#fca5a5" font-size="11" font-family="sans-serif" font-weight="bold" text-anchor="middle">Critical Phase</text>
  <text x="260" y="126" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">(Day 4-6: Platelets &lt; 50k)</text>
</svg>''',

    # SVG 6: Modes of Infection
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="25" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Major Transmission Routes of Infectious Pathogens</text>
  <!-- 4 Quadrants -->
  <g transform="translate(25, 45)">
    <!-- Airborne -->
    <rect x="0" y="0" width="215" height="75" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="12" y="24" fill="#38bdf8" font-size="12" font-weight="bold">Airborne Droplets</text>
    <text x="12" y="45" fill="#f8fafc" font-size="10">Coughing, sneezing aerosols</text>
    <text x="12" y="62" fill="#94a3b8" font-size="10">Ex: Tuberculosis, Swine Flu, Common Cold</text>
    <!-- Water / Food -->
    <rect x="235" y="0" width="215" height="75" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="247" y="24" fill="#10b981" font-size="12" font-weight="bold">Contaminated Water &amp; Food</text>
    <text x="247" y="45" fill="#f8fafc" font-size="10">Fecal-oral ingestion</text>
    <text x="247" y="62" fill="#94a3b8" font-size="10">Ex: Typhoid, Cholera, Hepatitis A</text>
    <!-- Vector Borne -->
    <rect x="0" y="90" width="215" height="75" rx="8" fill="#1e293b" stroke="#fbbf24"/>
    <text x="12" y="114" fill="#fbbf24" font-size="12" font-weight="bold">Biological Vectors</text>
    <text x="12" y="135" fill="#f8fafc" font-size="10">Mosquitoes, sandflies, fleas</text>
    <text x="12" y="152" fill="#94a3b8" font-size="10">Ex: Malaria (Anopheles), Dengue (Aedes)</text>
    <!-- Direct / Wounds -->
    <rect x="235" y="90" width="215" height="75" rx="8" fill="#1e293b" stroke="#f43f5e"/>
    <text x="247" y="114" fill="#f43f5e" font-size="12" font-weight="bold">Puncture Wounds &amp; Soil</text>
    <text x="247" y="135" fill="#f8fafc" font-size="10">Spores entering tissue breaks</text>
    <text x="247" y="152" fill="#94a3b8" font-size="10">Ex: Tetanus (Clostridium tetani)</text>
  </g>
</svg>''',

    # SVG 7: Anaerobic broth tube test
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Thioglycolate Broth: Oxygen Requirements of Bacteria</text>
  <!-- Tube 1: Obligate Aerobe -->
  <g transform="translate(60, 45)">
    <rect x="10" y="10" width="50" height="130" rx="12" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <!-- Broth fill -->
    <rect x="12" y="30" width="46" height="108" rx="10" fill="#334155"/>
    <!-- Growth at top -->
    <circle cx="25" cy="40" r="3" fill="#38bdf8"/>
    <circle cx="35" cy="38" r="4" fill="#38bdf8"/>
    <circle cx="45" cy="42" r="3" fill="#38bdf8"/>
    <text x="35" y="160" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Obligate Aerobe</text>
    <text x="35" y="174" fill="#94a3b8" font-size="9" text-anchor="middle">(Top only)</text>
  </g>
  <!-- Tube 2: Obligate Anaerobe (Clostridium) -->
  <g transform="translate(225, 45)">
    <rect x="10" y="10" width="50" height="130" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <!-- Broth fill -->
    <rect x="12" y="30" width="46" height="108" rx="10" fill="#334155"/>
    <!-- Growth at bottom only -->
    <circle cx="25" cy="120" r="3" fill="#f43f5e"/>
    <circle cx="35" cy="128" r="4" fill="#f43f5e"/>
    <circle cx="45" cy="122" r="3" fill="#f43f5e"/>
    <circle cx="35" cy="115" r="3" fill="#f43f5e"/>
    <text x="35" y="160" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">Obligate Anaerobe</text>
    <text x="35" y="174" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Clostridium (Bottom only)</text>
  </g>
  <!-- Tube 3: Facultative Anaerobe -->
  <g transform="translate(385, 45)">
    <rect x="10" y="10" width="50" height="130" rx="12" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <!-- Broth fill -->
    <rect x="12" y="30" width="46" height="108" rx="10" fill="#334155"/>
    <!-- Growth throughout -->
    <circle cx="35" cy="40" r="4" fill="#10b981"/>
    <circle cx="25" cy="70" r="3" fill="#10b981"/>
    <circle cx="42" cy="90" r="3" fill="#10b981"/>
    <circle cx="30" cy="120" r="3" fill="#10b981"/>
    <text x="35" y="160" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Facultative</text>
    <text x="35" y="174" fill="#94a3b8" font-size="9" text-anchor="middle">(Throughout)</text>
  </g>
</svg>''',

    # SVG 8: Botulinum toxin mechanism
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Botulinum Neurotoxin Action at Neuromuscular Junction</text>
  <!-- Presynaptic motor terminal -->
  <path d="M 120 45 C 120 120 180 140 250 140 C 320 140 380 120 380 45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="250" y="70" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Presynaptic Motor Terminal</text>
  <!-- Vesicles blocked -->
  <circle cx="210" cy="100" r="10" fill="#fbbf24"/>
  <circle cx="250" cy="105" r="10" fill="#fbbf24"/>
  <circle cx="290" cy="100" r="10" fill="#fbbf24"/>
  <text x="250" y="104" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">ACh</text>
  <!-- Big Red X: Botulinum blocks SNAP-25 -->
  <path d="M 235 125 L 265 145 M 265 125 L 235 145" stroke="#ef4444" stroke-width="4"/>
  <text x="345" y="145" fill="#ef4444" font-size="11" font-weight="bold">BLOCKED by Botulinum Toxin</text>
  <!-- Muscle fibre below -->
  <rect x="100" y="165" width="300" height="40" rx="6" fill="#475569" stroke="#94a3b8"/>
  <text x="250" y="190" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Muscle Fiber: NO Acetylcholine Release &#8594; Flaccid Paralysis</text>
</svg>''',

    # SVG 9: Tetanus vs Botulism comparison
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Contrast: Tetanospasmin vs Botulinum Toxin</text>
  <!-- Botulism Panel -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="102" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Botulism (C. botulinum)</text>
    <text x="12" y="55" fill="#f8fafc" font-size="11">&#8226; Ingestion in spoiled canned food</text>
    <text x="12" y="78" fill="#f8fafc" font-size="11">&#8226; Blocks ACh release</text>
    <text x="12" y="101" fill="#f8fafc" font-size="11">&#8226; Muscle cannot contract</text>
    <rect x="12" y="120" width="180" height="32" rx="6" fill="#0284c7"/>
    <text x="102" y="141" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">FLACCID PARALYSIS</text>
  </g>
  <!-- Tetanus Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="102" y="25" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="middle">Tetanus (C. tetani)</text>
    <text x="12" y="55" fill="#f8fafc" font-size="11">&#8226; Enters deep puncture wounds</text>
    <text x="12" y="78" fill="#f8fafc" font-size="11">&#8226; Blocks GABA/glycine inhibitors</text>
    <text x="12" y="101" fill="#f8fafc" font-size="11">&#8226; Muscle cannot relax</text>
    <rect x="12" y="120" width="180" height="32" rx="6" fill="#be123c"/>
    <text x="102" y="141" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">SPASTIC PARALYSIS</text>
  </g>
</svg>''',

    # SVG 10: Hepatitis virus table
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Classification of Hepatitis Viruses</text>
  <!-- Table Header -->
  <rect x="25" y="45" width="450" height="30" fill="#334155" rx="4"/>
  <text x="65" y="65" fill="#38bdf8" font-size="11" font-weight="bold">Type</text>
  <text x="170" y="65" fill="#38bdf8" font-size="11" font-weight="bold">Transmission Route</text>
  <text x="330" y="65" fill="#38bdf8" font-size="11" font-weight="bold">Genome &amp; Vaccine</text>
  <!-- Row 1: Hep A -->
  <rect x="25" y="80" width="450" height="35" fill="#1e293b"/>
  <text x="65" y="102" fill="#f8fafc" font-size="11" font-weight="bold">HAV</text>
  <text x="170" y="102" fill="#94a3b8" font-size="11">Fecal-oral (Water / Food)</text>
  <text x="330" y="102" fill="#10b981" font-size="11">RNA / Vaccine Available</text>
  <!-- Row 2: Hep B -->
  <rect x="25" y="120" width="450" height="35" fill="#1e293b"/>
  <text x="65" y="142" fill="#f8fafc" font-size="11" font-weight="bold">HBV</text>
  <text x="170" y="142" fill="#94a3b8" font-size="11">Blood, Needles, Body Fluids</text>
  <text x="330" y="142" fill="#10b981" font-size="11">DNA / Routine Vaccine</text>
  <!-- Row 3: Hep C -->
  <rect x="25" y="160" width="450" height="35" fill="#1e293b"/>
  <text x="65" y="182" fill="#f8fafc" font-size="11" font-weight="bold">HCV</text>
  <text x="170" y="182" fill="#94a3b8" font-size="11">Blood transfusion / Transmissible</text>
  <text x="330" y="182" fill="#f43f5e" font-size="11">RNA / No vaccine yet</text>
</svg>''',

    # SVG 11: Food temperature danger zone
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Food Safety: Temperature Danger Zone for Bacteria</text>
  <!-- Thermometer bar -->
  <g transform="translate(60, 45)">
    <!-- High temp safe zone -->
    <rect x="0" y="0" width="80" height="40" fill="#dc2626"/>
    <text x="95" y="25" fill="#fca5a5" font-size="11" font-weight="bold">&gt; 60 &#176;C: Cooking / Holding Hot (Bacteria Killed)</text>
    <!-- Danger zone -->
    <rect x="0" y="42" width="80" height="80" fill="#f59e0b"/>
    <text x="95" y="75" fill="#fde68a" font-size="12" font-weight="bold">5 &#176;C to 60 &#176;C: DANGER ZONE</text>
    <text x="95" y="95" fill="#fef08a" font-size="10">Rapid bacterial multiplication &amp; toxin secretion</text>
    <!-- Refrigeration safe zone -->
    <rect x="0" y="124" width="80" height="45" fill="#0284c7"/>
    <text x="95" y="145" fill="#7dd3fc" font-size="11" font-weight="bold">&lt; 5 &#176;C: Refrigeration / Chilling</text>
    <text x="95" y="162" fill="#94a3b8" font-size="10">Bacterial growth severely inhibited</text>
  </g>
</svg>''',

    # SVG 12: Antibiotic zone of inhibition / resistance
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Kirby-Bauer Disk Diffusion: Susceptibility vs Resistance</text>
  <!-- Agar plate 1: Susceptible -->
  <g transform="translate(60, 45)">
    <circle cx="80" cy="80" r="70" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <circle cx="80" cy="80" r="50" fill="#0f172a" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
    <circle cx="80" cy="80" r="10" fill="#f8fafc"/>
    <text x="80" y="83" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">AB 1</text>
    <text x="80" y="168" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Susceptible (Clear Zone)</text>
  </g>
  <!-- Agar plate 2: Resistant -->
  <g transform="translate(280, 45)">
    <circle cx="80" cy="80" r="70" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <circle cx="80" cy="80" r="10" fill="#f8fafc"/>
    <text x="80" y="83" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">AB 2</text>
    <text x="80" y="168" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Resistant (No Zone / Growth)</text>
  </g>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the provided anatomical diagram of Clostridium, what is the survival function of the swollen endospore located at the terminal end?",
        "options": [
            "It facilitates rapid binary fission during abundant nutrient periods",
            "It protects the bacterial genetic material against lethal heat, desiccation, and chemical disinfectants",
            "It conducts oxygenic photosynthesis in direct sunlight",
            "It absorbs atmospheric nitrogen gas to fertilize legumes"
        ],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram highlights the dehydrated, thick-coated terminal endospore of Clostridium, which enables dormant survival under extreme environmental stressors including high heat and dry conditions."
    },
    {
        "q": "Referring to the structural comparison diagram between a bacterium and a virus, which fundamental component is present in bacteria but completely absent in viruses?",
        "options": [
            "Genetic material (DNA or RNA)",
            "Cellular organelles, ribosomes, and a peptidoglycan cell wall",
            "Outer surface antigens",
            "Proteinaceous macromolecular structures"
        ],
        "ans": 1,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "As illustrated, bacteria are cellular organisms containing cytoplasm, ribosomes, and cell walls, whereas viruses are acellular packages consisting solely of nucleic acid enclosed within a protein capsid."
    },
    {
        "q": "Based on the vector comparison diagram, which identifying diagnostic feature distinguishes Aedes aegypti from the malaria vector Anopheles?",
        "options": [
            "Distinct white stripes/bands on thorax and legs, and daytime biting habits",
            "Resting posture tilted at a steep 45-degree angle to the surface",
            "Exclusive preference for deep, highly polluted sewage drains",
            "Inability to transmit any human viral pathogens"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram details Aedes aegypti with conspicuous white lyre patterns and banded legs, daytime biting habits, and preference for clean domestic water containers."
    },
    {
        "q": "According to the Plasmodium lifecycle flowchart, what immediate clinical event is triggered in the human host when red blood cells burst during Stage 4?",
        "options": [
            "Release of hemozoin toxin producing periodic chills and spike in body temperature",
            "Instant suppression of all immune memory cells",
            "Transformation into bacterial vegetative bacilli",
            "Immediate drop in systemic blood pressure to zero"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram traces stage 4 (erythrocyte rupture) where merozoites and the metabolic byproduct hemozoin are released simultaneously, inducing recurring rigor, chills, and high fever."
    },
    {
        "q": "Examining the clinical course curve for Dengue fever, during which timeframe does the critical phase occur where blood platelet count drops to its most dangerous nadir?",
        "options": [
            "Days 4 to 6 from onset of illness",
            "Day 1 immediately upon mosquito bite",
            "Day 14 during full convalescence",
            "Day 30 following complete recovery"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The graph depicts the critical phase between Days 4 and 6, when defervescence is accompanied by marked thrombocytopenia (platelets dropping below 50,000 / uL) and potential plasma leakage."
    },
    {
        "q": "Based on the infectious transmission routes chart, which pair of pathogens is correctly matched to transmission via contaminated food and water?",
        "options": [
            "Salmonella typhi and Vibrio cholerae",
            "Mycobacterium tuberculosis and Influenza A",
            "Plasmodium vivax and Dengue virus",
            "Clostridium tetani and rabies virus"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The quadrant chart groups Salmonella typhi (typhoid) and Vibrio cholerae (cholera) under enteric transmission through contaminated drinking water and unhygienic food."
    },
    {
        "q": "In the thioglycolate broth test tube diagram, why do obligate anaerobes like Clostridium grow exclusively at the very bottom of the tube?",
        "options": [
            "Oxygen diffuses from the top, creating an oxygen-free reducing zone only at the bottom",
            "Gravity pulls all bacterial cells downward regardless of oxygen",
            "The top of the tube contains lethal antibiotic discs",
            "Nutrients are entirely absent from the top layer of broth"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Thioglycolate broth creates an oxygen gradient: atmospheric oxygen diffuses into the top layer, leaving the bottom completely anaerobic where oxygen-intolerant Clostridium proliferates."
    },
    {
        "q": "Referring to the neuromuscular junction diagram, what is the precise molecular action of Botulinum neurotoxin?",
        "options": [
            "It cleaves SNARE docking proteins, blocking acetylcholine vesicle exocytosis and preventing muscle contraction",
            "It permanently opens muscle sodium channels, causing continuous spasms",
            "It destroys myelin sheaths surrounding motor axons",
            "It mimics acetylcholine and causes continuous depolarization"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "The diagram illustrates Botulinum toxin blocking the release of acetylcholine (ACh) vesicles at the motor end plate, resulting in flaccid paralysis."
    },
    {
        "q": "Based on the comparison panel between botulism and tetanus, what fundamental difference exists in their physiological presentations?",
        "options": [
            "Botulism causes flaccid paralysis (failure to contract), whereas tetanus causes spastic paralysis (failure to relax)",
            "Botulism causes violent bone fractures while tetanus causes complete loss of muscle mass",
            "Tetanus is transmitted via canned food while botulism enters rusty puncture wounds",
            "Tetanus is a viral infection while botulism is a fungal infection"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The comparative panel outlines botulism causing flaccid paralysis through blocked acetylcholine release, whereas tetanus causes spastic paralysis (lockjaw) through blocked inhibitory neurotransmitters."
    },
    {
        "q": "According to the Hepatitis classification chart, which type is transmitted primarily via blood and bodily fluids and has a widely administered routine vaccine?",
        "options": [
            "Hepatitis B (HBV)",
            "Hepatitis A (HAV)",
            "Hepatitis C (HCV)",
            "Hepatitis E (HEV)"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "As cataloged in the table, Hepatitis B is a parenterally transmitted DNA virus with an effective recombinant vaccine that prevents chronic hepatitis and hepatocellular carcinoma."
    },
    {
        "q": "Based on the temperature danger zone diagram, what is the hazardous temperature range where foodborne bacteria multiply most vigorously?",
        "options": [
            "5 deg C to 60 deg C",
            "Below 0 deg C",
            "Above 100 deg C",
            "Exactly 0 deg C to 4 deg C"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The food safety chart identifies the 'Danger Zone' between 5 deg C and 60 deg C, where mesophilic pathogenic bacteria divide rapidly and elaborate enterotoxins."
    },
    {
        "q": "Observing the Kirby-Bauer disk diffusion diagram, what does a large, clear halo (zone of inhibition) surrounding antibiotic disk AB 1 demonstrate?",
        "options": [
            "The bacterial strain is susceptible (sensitive) to antibiotic AB 1",
            "The bacteria have developed total resistance against antibiotic AB 1",
            "The antibiotic stimulated rapid bacterial colony growth",
            "The agar medium was improperly prepared and defective"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A clear zone around the disk indicates that the diffused antibiotic inhibited bacterial growth, demonstrating that the organism is susceptible (sensitive) to that antimicrobial agent."
    }
]

def make_doc(item, idx, vault, category, svg=None):
    code = f"{TOPIC_CODE}-{item['type']}-{idx:03d}"
    doc = {
        "questionCode": code,
        "topicCode": TOPIC_CODE,
        "chapterNumber": 8,
        "subjectCode": "SCIT",
        "class": 9,
        "board": "MH",
        "text": item["q"],
        "options": item["options"],
        "correctAnswer": item["ans"],
        "type": item["type"],
        "difficulty": item["difficulty"],
        "marks": 4,
        "negativeMarks": 0,
        "status": "published",
        "usageCount": 0,
        "examCategory": category,
        "vault": vault,
        "explanation": item["exp"]
    }
    if svg:
        doc["figureSvg"] = svg
        doc["requiresFigure"] = True
    return doc

def generate_all():
    docs = []
    idx = 1
    # 40 Exam
    for item in exam_data:
        docs.append(make_doc(item, idx, "exam", "standard"))
        idx += 1
    # 30 Practice
    for item in practice_data:
        docs.append(make_doc(item, idx, "practice", "standard"))
        idx += 1
    # 12 Mock
    for i, item in enumerate(mock_questions):
        svg = svg_diagrams[i]
        docs.append(make_doc(item, idx, "mock", "foundation", svg))
        idx += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(docs)} questions for {TOPIC_CODE} -> {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_all()
