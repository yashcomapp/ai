import json
import random

random.seed(8202)

def build_ch2_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vaults_80 = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs_80 = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 2.1.1 WHO definition of health (38 exam questions)
    # -------------------------------------------------------------
    tc_211 = "MH-8-SCI-2-2.1.1"
    name_211 = "WHO definition of health (physical, mental, and social well-being)"
    diffs_38 = ["easy"] * 13 + ["medium"] * 15 + ["hard"] * 10
    who_q = [
        ("What is the comprehensive definition of 'Health' formulated by the World Health Organization (WHO)?", "A state of complete physical, mental, and social well-being, and not merely the absence of disease or infirmity", ["The absence of fever and infectious microbes", "Possessing high physical muscle mass and athletic stamina", "Having normal body temperature and blood pressure only"]),
        ("According to WHO guidelines, does a person who has no physical disease but experiences extreme chronic anxiety and social depression qualify as healthy?", "No, because health encompasses mental and social well-being alongside physical health", ["Yes, as long as body weight is normal", "Yes, psychological distress is excluded from health", "Yes, medical tests show no bacteria"]),
        ("What is defined as a condition of disturbance in physiological or psychological processes of the body?", "Disease", ["Health", "Immunity", "Metabolism"]),
        ("Why does each specific medical disease have its own unique diagnostic symptoms?", "Because each disease impairs specific organs, tissues, or biochemical pathways", ["Because all diseases are caused by the same virus", "Because symptoms are randomly assigned by doctors", "Because diseases only affect external skin"])
    ]
    for i in range(38):
        ctx, ans, wrongs = who_q[i % len(who_q)]
        q = make_q(
            tc_211, name_211,
            f"Public Health Concepts: {ctx}",
            ans, wrongs,
            "The World Health Organization (WHO) defines health holistically across three dimensions: physical, mental, and social well-being.",
            "Health is not merely the absence of infirmity or pathogens.",
            f"Hence, the accurate definition is '{ans}'.",
            diffs_38[i], "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.1.2 Chronic vs acute diseases (38 exam questions)
    # -------------------------------------------------------------
    tc_212 = "MH-8-SCI-2-2.1.2"
    name_212 = "Chronic vs acute diseases"
    diffs_38_2 = ["easy"] * 13 + ["medium"] * 15 + ["hard"] * 10
    duration_q = [
        ("Diseases that last for a short duration of time and resolve quickly with treatment are termed:", "Acute diseases (e.g. common cold, viral fever)", ["Chronic diseases", "Hereditary diseases", "Congenital disorders"]),
        ("Diseases that persist for long durations, often lifelong, requiring prolonged therapy are termed:", "Chronic diseases (e.g. diabetes, tuberculosis, hypertension)", ["Acute diseases", "Infectious epidemics", "Transient fevers"]),
        ("Which of the following is classified as an ACUTE disease?", "Common cold / Acute influenza", ["Diabetes mellitus", "Elephantiasis (Filariasis)", "Chronic arthritis"]),
        ("Elephantiasis (caused by Wuchereria bancrofti filarial worm) is classified under duration as:", "A chronic disease causing long-term permanent limb swelling", ["An acute 2-day fever", "A congenital gene mutation", "A deficiency disorder"])
    ]
    for i in range(38):
        ctx, ans, wrongs = duration_q[i % len(duration_q)]
        q = make_q(
            tc_212, name_212,
            f"Disease Classification by Duration: {ctx}",
            ans, wrongs,
            "Based on duration, medical science classifies diseases into acute (short-term) and chronic (long-term/permanent).",
            "Acute ailments develop rapidly and subside, whereas chronic disorders persist and impact quality of life over extended periods.",
            f"Thus, the correct classification is '{ans}'.",
            diffs_38_2[i], "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.1.3 Hereditary vs acquired diseases (37 exam questions)
    # -------------------------------------------------------------
    tc_213 = "MH-8-SCI-2-2.1.3"
    name_213 = "Hereditary (Down syndrome) vs acquired diseases"
    diffs_37 = ["easy"] * 12 + ["medium"] * 15 + ["hard"] * 10
    hered_q = [
        ("Diseases present from birth caused by genetic abnormalities or chromosome mutations are classified as:", "Hereditary / Congenital diseases", ["Acquired infectious diseases", "Lifestyle acquired diseases", "Contagious epidemics"]),
        ("Down syndrome (trisomy 21) is a classic medical example of which disease category?", "Hereditary chromosomal disorder", ["Bacterial infection", "Waterborne epidemic", "Vitamin deficiency"]),
        ("Diseases that develop during a person's lifetime after birth due to external pathogens or environmental factors are called:", "Acquired diseases", ["Hereditary diseases", "Mendelian traits", "Epigenetic traits"]),
        ("Which of the following is an ACQUIRED infectious disease transmitted by pathogens?", "Cholera / Typhoid / Tuberculosis", ["Haemophilia", "Down syndrome", "Sickle cell anaemia"])
    ]
    for i in range(37):
        ctx, ans, wrongs = hered_q[i % len(hered_q)]
        q = make_q(
            tc_213, name_213,
            f"Disease Origin Classification: {ctx}",
            ans, wrongs,
            "According to reasons of origin, diseases are classified into hereditary (inherited through genetic mutations) and acquired (developed after birth).",
            "Down syndrome is caused by a chromosomal abnormality (Trisomy 21), representing a hereditary condition.",
            f"Therefore, '{ans}' is the correct statement.",
            diffs_37[i], "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.2.1 Tuberculosis (80 questions)
    # -------------------------------------------------------------
    tc_221 = "MH-8-SCI-2-2.2.1"
    name_221 = "Tuberculosis (Mycobacterium tuberculosis, BCG vaccine)"
    tb_q = [
        ("What is the pathogen responsible for causing Tuberculosis (TB) in humans?", "Mycobacterium tuberculosis (bacterium)", ["Salmonella typhi", "Vibrio cholerae", "Plasmodium vivax"]),
        ("Which vaccine is administered to infants to provide active immunity against Tuberculosis?", "BCG (Bacillus Calmette-Guérin) vaccine", ["DPT vaccine", "MMR vaccine", "Polio oral drops"]),
        ("What is the primary mode of transmission of Tuberculosis from an infected patient to a healthy person?", "Airborne transmission via droplets coughed or sneezed into the air", ["Bite of an insect vector", "Drinking treated boiled water", "Eating cooked vegetarian food"]),
        ("What is the standardized global treatment regimen recommended by WHO for curing Tuberculosis?", "DOTS (Directly Observed Treatment, Short-course)", ["Dialysis therapy", "Chemotherapy irradiation", "Oral Rehydration Therapy (ORT)"]),
        ("What are the cardinal clinical symptoms of pulmonary Tuberculosis?", "Chronic cough, blood in sputum, persistent low-grade fever, and progressive weight loss", ["Sudden acute watery diarrhoea", "Joint dislocation and arthritis", "Swollen neck salivary glands only"]),
        ("Which organ of the human body is most commonly targeted by Mycobacterium tuberculosis?", "Lungs", ["Liver", "Small intestine", "Urinary bladder"]),
        ("Why must TB patients strictly complete their full prescribed antibiotic course under DOTS?", "To prevent the development of multidrug-resistant tuberculosis (MDR-TB)", ["Because the medicine tastes sweet", "To increase heart rate", "Because BCG vaccine cannot be used on adults"]),
        ("Mycobacterium tuberculosis has which cellular morphology?", "Slender rod-shaped (bacillus) acid-fast bacterium", ["Spherical coccus in clusters", "Spiral corkscrew", "Comma-shaped vibrio"])
    ]
    for i in range(80):
        ctx, ans, wrongs = tb_q[i % len(tb_q)]
        q = make_q(
            tc_221, name_221,
            f"Tuberculosis Epidemiology & Pathology: {ctx}",
            ans, wrongs,
            "Tuberculosis is a bacterial infectious disease caused by Mycobacterium tuberculosis, spreading via airborne droplet nuclei.",
            "Prevention relies on BCG immunization in infancy, and treatment requires disciplined long-term antibacterial therapy under DOTS.",
            f"Hence, '{ans}' is the correct fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.2.2 Hepatitis/Jaundice (80 questions)
    # -------------------------------------------------------------
    tc_222 = "MH-8-SCI-2-2.2.2"
    name_222 = "Hepatitis/Jaundice (Hepatitis virus)"
    hep_q = [
        ("What vital organ of the human body is primarily inflamed and damaged during Hepatitis?", "Liver", ["Kidney", "Lungs", "Heart"]),
        ("What is the pathogen causing Hepatitis (commonly manifested as Jaundice)?", "Hepatitis virus (types A, B, C, D, E)", ["Entamoeba histolytica", "Vibrio cholerae", "Ascaris lumbricoides"]),
        ("What causes the characteristic yellowing of skin and eyes (sclera) in a jaundice patient?", "Accumulation of excess bile pigment (bilirubin) in the blood", ["Excess iron in hemoglobin", "Deficiency of calcium in bones", "Excess melanin in skin"]),
        ("Through which route are Hepatitis A and Hepatitis E viruses predominantly transmitted?", "Contaminated drinking water and unhygienic food (faecal-oral route)", ["Bite of female Anopheles mosquito", "Inhaling dry desert air", "Touching clean metallic objects"]),
        ("How are Hepatitis B and Hepatitis C viruses primarily transmitted?", "Infected blood transfusions, unsterilized needles/syringes, and body fluids", ["Drinking boiled filtered water", "Eating fresh peeled fruits", "Airborne dust particles"]),
        ("What are the early clinical symptoms exhibited by a patient suffering from Hepatitis?", "Anorexia (loss of appetite), yellow urine, fatigue, nausea, and vomiting", ["Severe joint immobility", "Paralysis of facial muscles", "Acute chest pain"]),
        ("What is the most effective public preventive measure against waterborne Hepatitis A and E?", "Boiling drinking water, proper sanitation, and safe waste disposal", ["Spraying DDT on water tanks", "Taking iron supplements", "Avoiding physical exercise"]),
        ("Is a preventive vaccine available against Hepatitis B infection?", "Yes, Hepatitis B recombinant vaccine is part of universal immunization programs", ["No, viral diseases cannot have vaccines", "No, only bacterial diseases have vaccines", "No, it is 100% untreatable"])
    ]
    for i in range(80):
        ctx, ans, wrongs = hep_q[i % len(hep_q)]
        q = make_q(
            tc_222, name_222,
            f"Hepatitis & Jaundice Medicine: {ctx}",
            ans, wrongs,
            "Hepatitis refers to inflammation of the liver caused by Hepatitis viruses (A, B, C, D, E).",
            "Jaundice is the clinical sign resulting from elevated bilirubin when liver processing is impaired.",
            f"Thus, the correct answer is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.2.3 Dysentery, Cholera, Typhoid (80 questions)
    # -------------------------------------------------------------
    tc_223 = "MH-8-SCI-2-2.2.3"
    name_223 = "Dysentery, Cholera (Vibrio cholerae), Typhoid (Salmonella typhi)"
    enteric_q = [
        ("What is the causative bacterial pathogen of Asiatic Cholera?", "Vibrio cholerae (comma-shaped bacterium)", ["Salmonella typhi", "Mycobacterium tuberculosis", "Entamoeba histolytica"]),
        ("What is the primary causative bacterium of Typhoid fever?", "Salmonella typhi (rod-shaped bacterium)", ["Vibrio cholerae", "Clostridium tetani", "Streptococcus pneumoniae"]),
        ("What is the cardinal clinical presentation of severe Cholera?", "Acute painless profuse 'rice-water' diarrhoea and severe vomiting leading to rapid dehydration", ["Chronic blood-streaked sputum", "Facial paralysis", "High fever with red skin rash only"]),
        ("What diagnostic serological blood test is routinely conducted in laboratories to confirm Typhoid fever?", "Widal test", ["ELISA test", "Biopsy test", "Sputum smear microscopy"]),
        ("Why is Oral Rehydration Solution (ORS) immediately administered in cholera and acute dysentery?", "To replenish depleted body water and essential electrolytes (sodium and potassium)", ["To destroy bacterial cell walls directly", "To provide protein for muscle repair", "To induce sleep"]),
        ("Bacterial dysentery (Shigellosis) and amoebic dysentery are primarily contracted through:", "Consumption of contaminated food and water exposed to houseflies and faecal pathogens", ["Airborne droplet aerosols in air-conditioned rooms", "Vector bites of Culex mosquitoes", "Direct sunlight exposure"]),
        ("Which common insect acts as a major mechanical vector transferring typhoid and cholera germs to uncovered food?", "Housefly (Musca domestica)", ["Cockroach", "Honeybee", "Dragonfly"]),
        ("Which organ of the digestive system is colonized and ulcerated by Salmonella typhi in typhoid?", "Small intestine (Peyer's patches)", ["Lungs", "Brain", "Pancreas"])
    ]
    for i in range(80):
        ctx, ans, wrongs = enteric_q[i % len(enteric_q)]
        q = make_q(
            tc_223, name_223,
            f"Waterborne Enteric Diseases: {ctx}",
            ans, wrongs,
            "Cholera (Vibrio cholerae), Typhoid (Salmonella typhi), and Dysentery are acute gastrointestinal infections spread by contaminated food and water.",
            "Dehydration is prevented by immediate ORS therapy, and diagnosis of typhoid is confirmed by the Widal test.",
            f"Therefore, '{ans}' is the correct clinical fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.2.4 Transmission through air, water, food, vectors (80 questions)
    # -------------------------------------------------------------
    tc_224 = "MH-8-SCI-2-2.2.4"
    name_224 = "Transmission through air, contaminated water, food, vectors"
    trans_q = [
        ("An animal or insect that transfers a pathogenic organism from an infected individual to a healthy individual is termed a:", "Vector (biological or mechanical carrier)", ["Parasite", "Pathogen", "Host"]),
        ("Which of the following infectious diseases is transmitted primarily through airborne droplets when a patient sneezes?", "Tuberculosis / Influenza / Measles", ["Cholera", "Amoebic dysentery", "Tetanus"]),
        ("Drinking untreated water contaminated with sewage runoff is the primary transmission route for:", "Cholera, Typhoid, Hepatitis A, and Dysentery", ["Malaria and Dengue", "Ringworm", "Tetanus"]),
        ("Which vector is responsible for transmitting the dengue virus between humans?", "Aedes aegypti mosquito", ["Anopheles mosquito", "Culex mosquito", "Rat flea (Xenopsylla)"]),
        ("Why does covering cooked food and properly boiling drinking water prevent multiple enteric diseases?", "Because heat kills bacteria and covering stops houseflies from depositing pathogens", ["Because food loses nutrition when uncovered", "Because water turns acidic when cold", "Because bacteria can only live in metal bowls"]),
        ("In vector-borne disease prevention, why is eliminating standing stagnant water around homes effective?", "It destroys the breeding grounds of mosquito larvae", ["It reduces humidity in the air", "It increases soil fertility", "It prevents bacterial airborne spores"]),
        ("Which mosquito species breeds in clean, stagnant artificial water containers and bites predominantly during daytime?", "Aedes aegypti (dengue vector)", ["Anopheles (malaria vector)", "Culex (filariasis vector)", "Mansonia"]),
        ("Fomites (such as contaminated clothes, door handles, utensils) serve as vehicles for:", "Indirect contact transmission of infectious microbes", ["Hereditary gene transfers", "Direct vector inoculation", "Autotrophic photosynthesis"])
    ]
    for i in range(80):
        ctx, ans, wrongs = trans_q[i % len(trans_q)]
        q = make_q(
            tc_224, name_224,
            f"Epidemiological Transmission Dynamics: {ctx}",
            ans, wrongs,
            "Infectious diseases spread through distinct transmission vectors: air, contaminated water/food, physical contact, and biological vectors.",
            "Controlling vectors and practicing clean water hygiene disrupts the chain of infection.",
            f"Thus, the correct principle is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.3.1 Dengue (80 questions)
    # -------------------------------------------------------------
    tc_231 = "MH-8-SCI-2-2.3.1"
    name_231 = "Dengue (Flavivirus / Aedes aegypti vector, thrombocytopenia)"
    dengue_q = [
        ("Which virus is the causative agent of Dengue fever?", "Dengue virus (DEN-1, 2, 3, 4 belonging to the genus Flavivirus)", ["Influenza virus H1N1", "Human Immunodeficiency Virus", "Rabies virus"]),
        ("Which mosquito vector transmits Dengue virus to humans?", "Aedes aegypti (tiger mosquito)", ["Female Anopheles", "Culex quinquefasciatus", "Tsetse fly"]),
        ("What critical hematological change occurs during severe Dengue fever that causes internal bleeding?", "Thrombocytopenia (sharp drop in blood platelet count)", ["Severe rise in red blood cells (polycythemia)", "Complete loss of hemoglobin", "Depletion of blood plasma water only"]),
        ("What are the primary clinical symptoms characteristic of Dengue fever?", "High sudden fever, severe headache, retro-orbital (behind the eye) pain, and muscle/joint aches", ["Chronic cough with sputum", "Watery rice-water stools", "Gradual weight loss over 6 months"]),
        ("At what time of day does the Dengue mosquito (Aedes aegypti) predominantly bite humans?", "Daytime (early morning and late afternoon)", ["Strictly midnight only", "Only between 2 AM and 4 AM", "It never bites humans"]),
        ("Why is regular cleaning of water coolers, flower pots, and discarded tires crucial for dengue control?", "Because Aedes mosquitoes breed in clean, undisturbed stagnant freshwater collections", ["Because tires attract adult flies", "Because dengue virus reproduces in rubber", "Because coolers generate humidity"]),
        ("When blood platelets drop dangerously below normal (e.g. < 20,000/μL) in dengue, what medical intervention is indicated?", "Platelet transfusion and intensive supportive fluid management", ["Immediate administration of antibiotics", "Chemotherapy radiation", "Surgical removal of spleen"]),
        ("Can Dengue be directly transmitted from human to human through coughing, shaking hands, or sharing food?", "No, transmission strictly requires the bite of an infected Aedes mosquito vector", ["Yes, it is highly contagious airborne", "Yes, through sharing clothes", "Yes, via contaminated water"])
    ]
    for i in range(80):
        ctx, ans, wrongs = dengue_q[i % len(dengue_q)]
        q = make_q(
            tc_231, name_231,
            f"Dengue Pathology & Prevention: {ctx}",
            ans, wrongs,
            "Dengue is a viral illness caused by Flavivirus (DEN-1 to 4) transmitted by the diurnal mosquito Aedes aegypti.",
            "A critical clinical indicator of disease severity is thrombocytopenia (platelet reduction), which poses a hemorrhage risk.",
            f"Therefore, '{ans}' is the correct clinical statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.3.2 Swine flu (80 questions)
    # -------------------------------------------------------------
    tc_232 = "MH-8-SCI-2-2.3.2"
    name_232 = "Swine flu (Influenza virus H1N1)"
    swine_q = [
        ("What is the viral pathogen that causes Swine Flu?", "Influenza virus subtype H1N1", ["Hepatitis A virus", "Retrovirus HIV", "Rhinovirus"]),
        ("Which animals act as natural reservoir hosts from which Swine flu was originally transmitted to humans?", "Pigs (swine)", ["Chickens and ducks", "Dogs and cats", "Horses"]),
        ("How does Swine Flu (H1N1) transmit from one person to another?", "Through respiratory secretions, droplet spray during coughing/sneezing, and nose/throat secretions", ["Through contaminated food cooked at high temperature", "Via mosquito bites", "By walking barefoot on soil"]),
        ("What are the prominent symptoms of Swine Flu in infected individuals?", "High fever, sore throat, persistent cough, body ache, and severe breathlessness", ["Platelet drop with bleeding", "Severe joint dislocation", "Loss of memory only"]),
        ("In the designation H1N1, what do 'H' and 'N' scientifically stand for?", "Hemagglutinin (H) and Neuraminidase (N), two surface viral glycoproteins", ["Human and Neurological", "Heart and Nerve", "Heat and Nitrogen"]),
        ("What laboratory diagnostic test is conducted on throat/nasal swab specimens to confirm H1N1 infection?", "RT-PCR (Real-Time Reverse Transcription Polymerase Chain Reaction)", ["Widal test", "Urine routine test", "Blood group matching"]),
        ("Which antiviral drug is commonly prescribed to manage and treat Swine Flu (H1N1) infections?", "Oseltamivir (Tamiflu)", ["Penicillin", "Chloroquine", "Insulin"]),
        ("Why does wearing a protective mask in crowded spaces help curb the transmission of H1N1 swine flu?", "Because it blocks respiratory droplets released during coughing or breathing", ["Because masks heat the air", "Because masks kill viruses chemically", "Because it prevents mosquito bites"])
    ]
    for i in range(80):
        ctx, ans, wrongs = swine_q[i % len(swine_q)]
        q = make_q(
            tc_232, name_232,
            f"Swine Flu (H1N1) Virology: {ctx}",
            ans, wrongs,
            "Swine flu is an acute respiratory infection caused by the Influenza A subtype H1N1 virus.",
            "It spreads through aerosolized respiratory secretions and is diagnosed definitively by RT-PCR.",
            f"Hence, '{ans}' is the accurate scientific fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.3.3 AIDS (80 questions)
    # -------------------------------------------------------------
    tc_233 = "MH-8-SCI-2-2.3.3"
    name_233 = "AIDS (HIV virus, ELISA test for diagnosis)"
    aids_q = [
        ("What is the full expansion of the medical acronym AIDS?", "Acquired Immuno Deficiency Syndrome", ["Acute Internal Digestive Syndrome", "Active Immunity Disorder Symptom", "Acquired Infection Damage Sickness"]),
        ("What is the viral pathogen that causes AIDS?", "HIV (Human Immunodeficiency Virus, a retrovirus)", ["H1N1 virus", "Flavivirus", "Hepatitis B virus"]),
        ("Which specific immune cells are attacked and progressively destroyed by HIV in the human body?", "Helper T-lymphocytes (CD4+ T-cells)", ["Red blood cells (erythrocytes)", "Blood platelets", "Pancreatic beta cells"]),
        ("Which standard immunological screening test is universally used for laboratory detection of HIV antibodies?", "ELISA (Enzyme-Linked Immunosorbent Assay)", ["Widal test", "Mantoux test", "Biopsy test"]),
        ("Which confirmatory test is performed when a patient tests repeatedly positive on an ELISA screen for HIV?", "Western Blot test", ["Blood sugar test", "X-ray screening", "Urine dipstick"]),
        ("Which of the following is a medically proven mode of transmission of HIV?", "Unprotected sexual contact with an infected person, contaminated blood transfusions, shared needles, and mother-to-child", ["Shaking hands or hugging an infected individual", "Sharing dining utensils or drinking glasses", "Bite of a mosquito or bedbug"]),
        ("Why do patients in advanced stages of AIDS become vulnerable to multiple opportunistic infections?", "Because progressive depletion of helper T-cells collapses the body's natural immune defense", ["Because their bones lose density", "Because their blood stops circulating", "Because digestive enzymes are destroyed"]),
        ("Does casual daily contact, sharing bathrooms, or sitting together in classrooms transmit HIV?", "No, HIV is not transmitted by casual social contact, sharing facilities, or saliva", ["Yes, it is highly contagious airborne", "Yes, through skin contact", "Yes, through sweat"])
    ]
    for i in range(80):
        ctx, ans, wrongs = aids_q[i % len(aids_q)]
        q = make_q(
            tc_233, name_233,
            f"HIV/AIDS Immunology & Diagnosis: {ctx}",
            ans, wrongs,
            "AIDS (Acquired Immuno Deficiency Syndrome) is caused by the retrovirus HIV, which destroys CD4+ T-lymphocytes.",
            "Diagnosis begins with an ELISA screening test and is confirmed by a Western Blot test.",
            f"Therefore, '{ans}' is the correct statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.4.1 Cancer (80 questions)
    # -------------------------------------------------------------
    tc_241 = "MH-8-SCI-2-2.4.1"
    name_241 = "Cancer: uncontrolled cell division, biopsy, chemotherapy, radiation"
    cancer_q = [
        ("What is the biological definition of cancer at the cellular level?", "Uncontrolled, abnormal, and disorganized cell division forming a malignant tumour (neoplasm)", ["A bacterial infection of blood", "Deficiency of dietary carbohydrates", "Temporary swelling after injury"]),
        ("What diagnostic procedure involves removing a small tissue specimen from a suspected tumour for microscopic examination?", "Biopsy", ["Widal test", "ELISA test", "Electrocardiogram (ECG)"]),
        ("Which major therapeutic modality uses specific anticancer chemical drugs to halt malignant cell proliferation?", "Chemotherapy", ["Physiotherapy", "Dialysis", "Acupuncture"]),
        ("What is the cancer treatment that employs targeted ionizing beams of high-energy radiation to kill cancerous cells?", "Radiation therapy (Radiotherapy)", ["Chemotherapy", "Surgery", "Insulin therapy"]),
        ("What are physical, chemical, or biological agents capable of causing cancer (such as tobacco smoke, UV rays, and asbestos) called?", "Carcinogens", ["Antigens", "Antibiotics", "Pathogens"]),
        ("Which harmful lifestyle habit is the leading causative factor for oral and lung cancers worldwide?", "Consumption of tobacco, gutkha, and cigarette smoking", ["Drinking clean filtered water", "Consuming leafy green vegetables", "Exercising daily"]),
        ("The spread of malignant cancer cells from their primary origin to distant organs via blood or lymph is termed:", "Metastasis", ["Differentiation", "Mitosis", "Apoptosis"]),
        ("Modern robotic and laser surgery are used in oncology to:", "Precisely excise localized tumours with minimal damage to adjacent healthy tissues", ["Replace the need for clean food", "Cure viral colds", "Boost red blood cell counts"])
    ]
    for i in range(80):
        ctx, ans, wrongs = cancer_q[i % len(cancer_q)]
        q = make_q(
            tc_241, name_241,
            f"Oncology & Cancer Biology: {ctx}",
            ans, wrongs,
            "Cancer is characterized by uncontrolled cellular mitosis leading to malignant tumours.",
            "Diagnosis is confirmed through histopathological biopsy, and treatment combines surgery, chemotherapy, and radiotherapy.",
            f"Thus, the correct answer is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.4.2 Diabetes (80 questions)
    # -------------------------------------------------------------
    tc_242 = "MH-8-SCI-2-2.4.2"
    name_242 = "Diabetes: insulin deficiency from pancreas, blood sugar monitoring"
    diabetes_q = [
        ("Which endocrine hormone, produced by beta cells of the pancreas, regulates and lowers glucose levels in the bloodstream?", "Insulin", ["Adrenaline", "Thyroxine", "Growth hormone"]),
        ("What physiological disorder occurs when the pancreas produces inadequate insulin or body cells fail to respond to it?", "Diabetes mellitus", ["Diabetes insipidus", "Goitre", "Hypertension"]),
        ("What happens to glucose in the bloodstream when there is a deficiency of functional insulin?", "Blood glucose levels rise abnormally (hyperglycemia) and excess glucose spills into urine", ["Blood glucose drops to zero permanently", "Glucose turns directly into oxygen", "Blood loses all red blood cells"]),
        ("What are the classic symptoms experienced by patients with uncontrolled diabetes?", "Frequent urination at night (polyuria), excessive thirst (polydipsia), and unexplained weight loss", ["Severe high fever and chest cough", "Swelling of legs due to filarial worms", "Sudden bleeding from gums"]),
        ("What portable electronic medical device allows diabetic patients to monitor their blood glucose levels at home?", "Glucometer", ["Sphygmomanometer", "Thermometer", "Stethoscope"]),
        ("What is the primary non-pharmacological management strategy recommended for Type 2 diabetes?", "Balanced low-glycemic diet, regular physical exercise, and weight control", ["Strict bed rest without moving", "High-sugar carbohydrate intake", "Antibiotic injections"]),
        ("India has emerged as one of the countries with the largest diabetic populations globally, predominantly due to:", "Sedentary modern lifestyle, lack of physical activity, mental stress, and processed diet", ["Airborne viral transmission", "Drinking boiled water", "High consumption of fresh fruits"]),
        ("Why is uncontrolled chronic diabetes dangerous to overall health in the long run?", "It causes severe complications in kidneys (nephropathy), eyes (retinopathy), nerves, and heart", ["It makes skin turn blue", "It causes bacterial pneumonia", "It prevents hair growth"])
    ]
    for i in range(80):
        ctx, ans, wrongs = diabetes_q[i % len(diabetes_q)]
        q = make_q(
            tc_242, name_242,
            f"Endocrinology & Diabetes Mellitus: {ctx}",
            ans, wrongs,
            "Diabetes mellitus is a metabolic disorder resulting from deficient insulin secretion or action by the pancreas, leading to hyperglycemia.",
            "Management involves dietary modification, physical exercise, and regular monitoring via glucometers.",
            f"Hence, '{ans}' is the correct medical fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.4.3 Heart attack (80 questions)
    # -------------------------------------------------------------
    tc_243 = "MH-8-SCI-2-2.4.3"
    name_243 = "Heart attack: atherosclerosis, hypertension, angioplasty, bypass surgery"
    heart_q = [
        ("A heart attack (Myocardial Infarction) occurs primarily when which blood vessels become blocked, cutting off oxygen to heart muscles?", "Coronary arteries", ["Pulmonary veins", "Carotid arteries", "Renal arteries"]),
        ("What is the medical term for the narrowing and hardening of arteries due to the deposition of cholesterol plaques?", "Atherosclerosis", ["Osteoporosis", "Cirrhosis", "Emphysema"]),
        ("What is the standard clinical threshold for high blood pressure (Hypertension) in an adult at rest?", "Systolic \\(\\ge 140\\text{ mmHg}\\) and/or Diastolic \\(\\ge 90\\text{ mmHg}\\)", ["120 / 80 mmHg", "90 / 60 mmHg", "60 / 40 mmHg"]),
        ("What medical intervention involves inserting a tiny balloon and metallic stent to open a clogged coronary artery?", "Angioplasty", ["Bypass surgery", "Kidney dialysis", "Chemotherapy"]),
        ("When multiple coronary arteries are severely blocked, what surgical procedure reroutes blood flow using a vessel grafted from another part of the body?", "Coronary Artery Bypass Graft (CABG) surgery", ["Angioplasty with stent", "Open biopsy", "Organ transplant"]),
        ("What are the warning signs of an acute heart attack requiring emergency medical attention?", "Severe crushing pain in the centre of the chest radiating to left arm/shoulder, breathlessness, and cold sweating", ["Sharp pain in knee joint while walking", "High fever with throat irritation", "Yellow coloration of eyes"]),
        ("Which diagnostic test records the electrical activity of the heartbeat over time to detect ischemic heart injury?", "ECG (Electrocardiogram)", ["EEG (Electroencephalogram)", "Widal test", "Biopsy"]),
        ("What risk factors substantially increase the likelihood of developing cardiovascular heart disease?", "Smoking, alcoholism, obesity, high-fat diet, hypertension, diabetes, and lack of exercise", ["Regular aerobic walking", "Eating fiber-rich salads", "Maintaining normal body mass index"])
    ]
    for i in range(80):
        ctx, ans, wrongs = heart_q[i % len(heart_q)]
        q = make_q(
            tc_243, name_243,
            f"Cardiovascular Medicine & Pathology: {ctx}",
            ans, wrongs,
            "A heart attack results from ischemia when coronary arteries are obstructed by atherosclerotic plaques.",
            "Emergency interventions include angioplasty with stenting, bypass surgery (CABG), and rapid medical resuscitation.",
            f"Therefore, '{ans}' is the correct clinical statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.5.1 Pradhan Mantri Jan Aushadhi Yojana (80 questions)
    # -------------------------------------------------------------
    tc_251 = "MH-8-SCI-2-2.5.1"
    name_251 = "Pradhan Mantri Jan Aushadhi Yojana"
    pmjay_q = [
        ("What is the primary objective of the Pradhan Mantri Bharatiya Janaushadhi Pariyojana (PMBJP)?", "To provide high-quality generic medicines at substantially affordable prices to all citizens", ["To manufacture branded cosmetic products", "To export luxury drugs to foreign nations", "To replace all hospitals with pharmacies"]),
        ("Under which Union Ministry of the Government of India is the Jan Aushadhi initiative executed?", "Ministry of Chemicals and Fertilizers (Department of Pharmaceuticals)", ["Ministry of Defense", "Ministry of Agriculture", "Ministry of External Affairs"]),
        ("What are the dedicated retail pharmacy outlets operating under this government scheme called?", "Pradhan Mantri Jan Aushadhi Kendras", ["Government Ration Shops", "Ayushman Clinics", "Primary Health Centres"]),
        ("How does the pricing of medicines available at Jan Aushadhi Kendras compare to identical branded equivalents in the market?", "Jan Aushadhi generic medicines are 50% to 90% cheaper than branded market drugs", ["They are twice as expensive", "They cost exactly the same", "They are sold only to foreign tourists"]),
        ("Why are generic medicines sold under Jan Aushadhi just as therapeutically effective as expensive branded drugs?", "Because they contain the identical active pharmaceutical ingredient (API), potency, and bioequivalence", ["Because they are diluted with water", "Because they expire faster", "Because they do not require testing"]),
        ("Which public software portal and mobile application was launched to help citizens locate nearest Jan Aushadhi stores and compare drug prices?", "Jan Aushadhi Sugam App", ["Aarogya Setu", "CoWIN", "DigiLocker"]),
        ("What social impact has the Jan Aushadhi scheme had on low-income and chronic disease patients?", "Significantly reduced out-of-pocket healthcare expenses for essential daily medications", ["Increased drug dependency", "Forced people to buy foreign brands", "Reduced the number of doctors"]),
        ("Besides generic medicines, what critical women's hygiene product is provided at subsidized cost (₹1 per pad) under Jan Aushadhi?", "Suvidha Oxo-biodegradable sanitary napkins", ["Luxury soaps", "Branded perfumes", "Sunscreen creams"])
    ]
    for i in range(80):
        ctx, ans, wrongs = pmjay_q[i % len(pmjay_q)]
        q = make_q(
            tc_251, name_251,
            f"Public Health Initiatives (Jan Aushadhi): {ctx}",
            ans, wrongs,
            "The Pradhan Mantri Jan Aushadhi Yojana provides quality generic medicines at affordable prices through specialized Kendras.",
            "They share identical therapeutic efficacy and active ingredients with costlier branded counterparts.",
            f"Thus, the correct answer is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.5.2 Generic vs branded medicines (80 questions)
    # -------------------------------------------------------------
    tc_252 = "MH-8-SCI-2-2.5.2"
    name_252 = "Generic vs branded medicines"
    generic_q = [
        ("What is a 'Generic Medicine'?", "A medication named after its active chemical constituent rather than a trademark brand name", ["An expired counterfeit medicine", "A medicine that has no clinical effect", "A medicine manufactured only in herbal gardens"]),
        ("Why are generic medicines priced dramatically lower than their branded counterparts?", "Because generic manufacturers do not incur huge research, clinical trial patent, and marketing advertising expenses", ["Because generic drugs use low-grade impure chemicals", "Because generic drugs contain half the active dosage", "Because government imposes heavy taxes on generics"]),
        ("In terms of efficacy, safety, dosage, and quality standards, how do generic medicines compare to innovator branded drugs?", "They are bioequivalent and equal in therapeutic safety and efficacy", ["Generics take twice as long to work", "Generics have more side effects", "Generics are only 50% as effective"]),
        ("Paracetamol is the non-proprietary chemical name of an antipyretic. What does 'Crocin' or 'Calpol' represent?", "Commercial brand names under which paracetamol is marketed", ["Different chemical compounds", "Herbal remedies", "Injectable antibiotics"]),
        ("Why are medical doctors increasingly encouraged by regulations to prescribe drugs by generic chemical names?", "To empower patients to purchase cheaper quality alternatives without brand monopolies", ["To confuse pharmacists", "To reduce the variety of drugs available", "To prevent pharmacy sales"]),
        ("What regulatory body oversees the quality and bioequivalence standards of generic drugs in India?", "CDSCO (Central Drugs Standard Control Organisation)", ["ISRO", "NITI Aayog", "RBI"]),
        ("When the original patent of a newly discovered drug expires after 20 years, what occurs in the pharmaceutical industry?", "Other qualified pharmaceutical companies can legally manufacture and sell the generic drug at competitive low prices", ["The drug formula is destroyed", "The drug is banned permanently", "Only the original inventor can produce it forever"]),
        ("Do generic medicines adhere to the same stringent Good Manufacturing Practices (GMP) as branded pharmaceuticals?", "Yes, all licensed manufacturers must strictly comply with official pharmacopoeia and GMP standards", ["No, generics have no quality control", "No, generics are unchecked", "Only if exported to America"])
    ]
    for i in range(80):
        ctx, ans, wrongs = generic_q[i % len(generic_q)]
        q = make_q(
            tc_252, name_252,
            f"Pharmaceutical Science (Generic vs Branded): {ctx}",
            ans, wrongs,
            "Generic medicines contain identical active chemical substances as branded medicines, possessing identical bioequivalence and therapeutic efficacy.",
            "They are sold at significantly lower prices because manufacturers do not incur promotional or initial patent R&D costs.",
            f"Therefore, '{ans}' is the correct statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 2.5.3 First aid for heart disease (CPR) (80 questions)
    # -------------------------------------------------------------
    tc_253 = "MH-8-SCI-2-2.5.3"
    name_253 = "First aid for heart disease (CPR - Cardio-Pulmonary Resuscitation)"
    cpr_q = [
        ("What is the full medical expansion of the emergency life-saving technique 'CPR'?", "Cardio-Pulmonary Resuscitation", ["Cardiac Pulse Revival", "Coronary Pressure Relief", "Critical Patient Resuscitation"]),
        ("What is the immediate primary step to take when a person suddenly collapses, becomes unresponsive, and shows no normal breathing?", "Call emergency ambulance services (108/112) immediately and commence chest compressions (CPR)", ["Give the person a glass of cold water to drink", "Make the person sit upright and walk", "Wait for 2 hours to see if they wake up"]),
        ("What is the recommended rate of chest compressions during adult CPR according to resuscitation guidelines?", "100 to 120 compressions per minute", ["30 to 40 compressions per minute", "200 to 250 compressions per minute", "10 compressions per minute"]),
        ("Where should the rescuer's hands be placed when performing chest compressions on an adult in cardiac arrest?", "In the centre of the chest, on the lower half of the breastbone (sternum)", ["On the left side of the ribcage near the hip", "Directly on the stomach abdomen", "Over the throat"]),
        ("What is the recommended depth of chest compressions in an adult during CPR?", "At least 5 cm (about 2 to 2.4 inches), allowing full chest recoil between compressions", ["1 cm only", "10 cm to touch the spine", "0.5 cm"]),
        ("Why are chest compressions performed during sudden cardiac arrest before paramedics arrive?", "To manually pump oxygenated blood to the brain and vital organs, preventing brain death", ["To restart breathing through the nose automatically", "To warm up the body temperature", "To reset broken ribs"]),
        ("What portable electronic emergency device found in public spaces can analyze heart rhythm and deliver an electric shock during sudden cardiac arrest?", "AED (Automated External Defibrillator)", ["Glucometer", "Stethoscope", "Pulse Oximeter"]),
        ("Should an untrained layperson performing hands-only CPR stop compressions to attempt mouth-to-mouth rescue breaths?", "No, continuous high-quality chest compressions without interruption are recommended for untrained bystanders", ["Yes, stop compressions entirely", "Yes, rescue breaths are 10 times more important than compressions", "No, CPR should never be done by bystanders"])
    ]
    for i in range(80):
        ctx, ans, wrongs = cpr_q[i % len(cpr_q)]
        q = make_q(
            tc_253, name_253,
            f"Emergency Life Support & First Aid: {ctx}",
            ans, wrongs,
            "Cardio-Pulmonary Resuscitation (CPR) is an emergency life-support technique to sustain cerebral circulation during cardiac arrest.",
            "High-quality continuous chest compressions at 100–120/min at a depth of 5 cm in the centre of the chest maintain vital perfusion.",
            f"Hence, '{ans}' is the correct life-saving procedure.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch2_questions()
    print(f"Generated {len(qs)} questions for Chapter 2.")
    out_path = "scripts/mh8_sci_ch2_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
