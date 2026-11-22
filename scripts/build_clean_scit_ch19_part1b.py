# scripts/build_clean_scit_ch19_part1b.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.1 (Subtopics 19.1.3 and 19.1.4)
# 2 subtopics x 80 = 160 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_1_3():
    tc = "MH-9-SCIT-19-19.1.3"
    tname = "Nutrition, digestive process & respiration in living organisms"
    archs = [
        # Arch 0: Plant nutrition & insectivorous/saprophytic modes
        {
            'data': [
                ("plants that trap and digest insects to fulfill their nitrogen requirements in nutrient-deficient bogs", "Insectivorous plants (e.g., Drosera, Nepenthes, Utricularia)", "Parasitic plants (e.g., Cuscuta)", "Symbiotic epiphytes (e.g., Vanda)", "Saprophytic fungi (e.g., Agaricus)"),
                ("the yellow, tubular parasitic plant that lacks chlorophyll and absorbs nutrients via haustorial roots from a host plant", "Cuscuta (Dodder)", "Drosera burmannii", "Pitcher plant (Nepenthes)", "Bladderwort (Utricularia)"),
                ("the symbiotic association between nitrogen-fixing bacteria and leguminous root nodules providing nitrates to the plant", "Rhizobium symbiosis", "Mycorrhizal parasitism", "Saprophytic decomposition", "Lichen epiphyte mutualism"),
                ("the mutualistic association between an alga (phycobiont) providing food and a fungus (mycobiont) providing shelter and water/minerals", "Lichen", "Bacteriophage", "Cuscuta", "Mistletoe"),
                ("organisms that obtain nutrition by secreting digestive enzymes onto dead and decaying organic matter and absorbing soluble products", "Saprotrophs (Saprophytes)", "Autotrophs", "Holozoic consumers", "Obligate parasites"),
                ("the structural adaptation of Nepenthes that traps insects in a fluid-filled cavity with downward-pointing hairs", "Modified leaf lamina forming a pitcher with a lid", "Modified root spines", "Modified stipular thorns", "Modified floral petals"),
                ("the mineral element whose deficiency in marshy soils drives the evolution of insectivorous trapping mechanisms in plants", "Nitrogen (\\(N\\))", "Carbon (\\(C\\))", "Hydrogen (\\(H\\))", "Oxygen (\\(O\\))"),
                ("the Indian naturalist who extensively studied and documented Drosera burmannii in India", "Johannes Burman", "Homi Bhabha", "Jagadish Chandra Bose", "Birbal Sahni"),
                ("the green pigment contained in chloroplasts that absorbs sunlight energy for the chemical reduction of carbon dioxide into glucose", "Chlorophyll", "Anthocyanin", "Carotene", "Xanthophyll"),
                ("the overall chemical equation representing oxygenic photosynthesis in green autotrophic plants", "\\(6CO_2 + 6H_2O \\xrightarrow{\\text{sunlight, chlorophyll}} C_6H_{12}O_6 + 6O_2\\)", "\\(C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O + \\text{ATP}\\)", "\\(2H_2O \\rightarrow 2H_2 + O_2\\)", "\\(6CO_2 + 12H_2S \\rightarrow C_6H_{12}O_6 + 12S + 6H_2O\\)")
            ],
            'tmpls': [
                "Which category of specialized flora is defined as: {0}?",
                "Identify the parasitic plant characterized as: {0}.",
                "In soil microbiology and plant nutrition, name the mechanism: {0}.",
                "Select the dual mutualistic organism described as: {0}.",
                "Which nutritional category comprises: {0}?",
                "What morphological modification represents: {0}?",
                "Which essential nutrient deficiency explains: {0}?",
                "Name the historical botanical researcher associated with: {0}.",
                "Which photosynthetic pigment is identified as: {0}?",
                "Identify the balanced stoichiometric chemical equation for: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Identify Key Concepts**\\nThe query describes {item[0]}.\\n**Step 2: Analysis of Nutritional Adaptations**\\nAutotrophic, heterotrophic, insectivorous, and parasitic adaptations serve distinct ecological niches to secure energy and essential nitrogen.\\n**Step 3: Verification**\\nTherefore, the correct identification is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Human Digestive System: Organs & Enzymes
        {
            'data': [
                ("the enzyme secreted by salivary glands that initiates starch breakdown into maltose in the buccal cavity", "Salivary amylase (Ptyalin)", "Pepsin", "Trypsin", "Pancreatic lipase"),
                ("the muscular, wavelike rhythmic contraction and relaxation of the alimentary canal propelling food bolus downward", "Peristalsis", "Mastication", "Emulsification", "Deglutition"),
                ("the hydrochloric acid and enzyme-secreting organ where acidic gastric digestion of proteins occurs", "Stomach (gastric glands)", "Duodenum", "Caecum", "Oesophagus"),
                ("the protein-digesting enzyme secreted in inactive form by gastric glands and activated by hydrochloric acid (pH 1.5-2.5)", "Pepsin (from pepsinogen)", "Trypsin", "Salivary amylase", "Lactase"),
                ("the substance produced by the liver, stored in the gallbladder, which neutralizes acidic chyme and emulsifies fats", "Bile juice (containing bile salts)", "Pancreatic juice", "Gastric juice", "Saliva"),
                ("the pancreatic enzyme that digests proteins into peptones and peptides in an alkaline intestinal medium", "Trypsin", "Pepsin", "Maltase", "Rennin"),
                ("the pancreatic enzyme that hydrolyzes emulsified lipid droplets into fatty acids and glycerol", "Pancreatic lipase", "Bile salts", "Amylase", "Sucrase"),
                ("the finger-like microscopic projections on the inner mucosal lining of the small intestine that tremendously increase absorption surface area", "Intestinal villi (with microvilli)", "Rugae", "Crypts of Lieberkuhn", "Plicae circulares"),
                ("the primary site where maximum digestion and nutrient absorption takes place in the human alimentary canal", "Small intestine (Ileum & Jejunum)", "Stomach", "Large intestine (Colon)", "Buccal cavity"),
                ("the primary physiological role of the large intestine (colon) in human digestion", "Absorption of excess water and electrolytes and formation of solid feces", "Secretion of digestive lipases", "Digestion of complex starches", "Synthesis of bile pigments")
            ],
            'tmpls': [
                "Name the salivary enzyme described as: {0}.",
                "Which gastrointestinal motility process is defined as: {0}?",
                "Identify the digestive organ functioning as: {0}.",
                "Which gastric enzyme corresponds to: {0}?",
                "Identify the hepatic secretion acting as: {0}.",
                "Which proteolytic pancreatic enzyme is defined by: {0}?",
                "Name the lipid-hydrolyzing pancreatic enzyme described as: {0}.",
                "What microscopic anatomical structures are characterized as: {0}?",
                "Which anatomical region functions as: {0}?",
                "Select the primary physiological function described by: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Understand the Digestive Stage**\\nThe question focuses on {item[0]}.\\n**Step 2: Enzymatic and Functional Specificity**\\nEnzymatic digestion proceeds sequentially through mouth, stomach, duodenum, and ileum, each requiring specific pH and catalytic enzymes.\\n**Step 3: Conclusion**\\nThe correct component is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Steps of Holozoic Nutrition (Ingestion, Digestion, Absorption, Assimilation, Egestion)
        {
            'data': [
                ("the process of taking food into the body through the oral cavity or buccal opening", "Ingestion", "Digestion", "Absorption", "Assimilation"),
                ("the conversion of complex, insoluble food macromolecules into simple, soluble, absorbable molecules by mechanical and chemical action", "Digestion", "Ingestion", "Assimilation", "Egestion"),
                ("the passage of digested soluble nutrients through the intestinal epithelial mucosa into blood capillaries and lymph lacteals", "Absorption", "Assimilation", "Ingestion", "Egestion"),
                ("the uptake, incorporation, and biochemical utilization of absorbed nutrients by body cells for energy production, growth, and tissue repair", "Assimilation", "Absorption", "Digestion", "Egestion"),
                ("the elimination or voiding of undigested, unabsorbed waste matter from the body through the anus", "Egestion (Defecation)", "Excretion of urea", "Absorption", "Assimilation"),
                ("the physiological difference between egestion and excretion in animal metabolism", "Egestion eliminates undigested food residue; excretion eliminates metabolic wastes (urea, uric acid, \\(CO_2\\))", "Egestion produces urine; excretion produces feces", "Egestion occurs via kidneys; excretion occurs via rectum", "Egestion is chemical; excretion is purely mechanical"),
                ("the cellular organelle where absorbed glucose undergoes aerobic breakdown to synthesize high-energy ATP molecules", "Mitochondria", "Ribosome", "Golgi apparatus", "Lysosome"),
                ("the specialized lymphatic vessels located inside each intestinal villus that absorb digested fatty acids and glycerol", "Lacteals (lymphatic capillaries)", "Arterioles", "Venules", "Hepatic portal vein"),
                ("the large vein that directly transports blood rich in absorbed nutrients from the stomach and intestine to the liver for metabolic processing", "Hepatic portal vein", "Hepatic vein", "Inferior vena cava", "Renal vein"),
                ("the physiological condition resulting from inadequate intake of proteins and calories leading to severe muscle wasting in infants", "Protein-energy malnutrition (Marasmus / Kwashiorkor)", "Hyperthyroidism", "Pernicious anemia", "Scurvy")
            ],
            'tmpls': [
                "Which primary step of holozoic nutrition is defined as: {0}?",
                "Identify the physiological step described as: {0}.",
                "Which nutrient transport step corresponds to: {0}?",
                "Name the cellular utilization phase defined by: {0}.",
                "Which terminal elimination process is characterized as: {0}?",
                "What is the key physiological distinction regarding: {0}?",
                "Which metabolic organelle carries out: {0}?",
                "Identify the mucosal lymphatic vessel described as: {0}.",
                "Which major circulatory vessel is defined by: {0}?",
                "Identify the pediatric nutritional syndrome characterized by: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Nutritional Stage Identification**\\nThe question targets {item[0]}.\\n**Step 2: Sequence of Holozoic Nutrition**\\nHolozoic nutrition strictly follows: Ingestion \\(\\rightarrow\\) Digestion \\(\\rightarrow\\) Absorption \\(\\rightarrow\\) Assimilation \\(\\rightarrow\\) Egestion.\\n**Step 3: Verification**\\nThus, the correct terminology is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Cellular Respiration: Aerobic vs Anaerobic & Pathways
        {
            'data': [
                ("respiration that occurs in the presence of molecular oxygen, completely breaking down glucose into carbon dioxide, water, and 38 (or 36-38) ATP", "Aerobic respiration", "Anaerobic fermentation", "Lactic acid fermentation", "Photophosphorylation"),
                ("the initial 10-step metabolic pathway converting one molecule of glucose into two molecules of pyruvic acid in the cytoplasm without oxygen", "Glycolysis (EMP pathway)", "Krebs cycle (TCA cycle)", "Electron transport system", "Calvin cycle"),
                ("the site inside eukaryotic cells where the Krebs cycle and oxidative phosphorylation take place", "Mitochondrial matrix and inner mitochondrial membrane (cristae)", "Cytosol exclusively", "Nuclear nucleoplasm", "Endoplasmic reticulum lumen"),
                ("respiration occurring in yeast cells under anaerobic conditions producing ethanol, carbon dioxide, and 2 ATP", "Alcoholic fermentation", "Lactic acid fermentation", "Aerobic respiration", "Photorespiration"),
                ("the metabolic process occurring in human skeletal muscle cells during vigorous exercise under oxygen debt, producing muscle cramps", "Lactic acid fermentation (accumulation of lactate)", "Alcoholic fermentation producing ethanol", "Aerobic complete oxidation", "Beta-oxidation of fatty acids"),
                ("the universal cellular energy currency that stores chemical energy in high-energy phosphoanhydride bonds", "Adenosine triphosphate (ATP)", "Deoxyribonucleic acid (DNA)", "Nicotinamide adenine dinucleotide (NAD+)", "Flavin adenine dinucleotide (FAD)"),
                ("the net ATP yield produced per glucose molecule through anaerobic fermentation versus complete aerobic respiration", "2 ATP in fermentation vs ~36-38 ATP in aerobic respiration", "38 ATP in fermentation vs 2 ATP in aerobic", "4 ATP in fermentation vs 10 ATP in aerobic", "12 ATP in fermentation vs 24 ATP in aerobic"),
                ("the chemical equation representing anaerobic fermentation in Saccharomyces cerevisiae (yeast)", "\\(C_6H_{12}O_6 \\rightarrow 2C_2H_5OH + 2CO_2 + 2\\text{ ATP}\\)", "\\(C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O + 38\\text{ ATP}\\)", "\\(C_6H_{12}O_6 \\rightarrow 2CH_3CH(OH)COOH + 2\\text{ ATP}\\)", "\\(6CO_2 + 6H_2O \\rightarrow C_6H_{12}O_6 + 6O_2\\)"),
                ("the chemical equation representing lactic acid fermentation in oxygen-depleted muscle cells", "\\(C_6H_{12}O_6 \\rightarrow 2\\text{ Lactic acid } (C_3H_6O_3) + 2\\text{ ATP}\\)", "\\(C_6H_{12}O_6 \\rightarrow 2C_2H_5OH + 2CO_2 + 2\\text{ ATP}\\)", "\\(C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O\\)", "\\(2\\text{ Pyruvate} + 2H_2O \\rightarrow 2\\text{ Acetate} + 2CO_2\\)"),
                ("the gaseous exchange occurring during cellular respiration across respiratory surfaces", "Uptake of oxygen (\\(O_2\\)) and release of carbon dioxide (\\(CO_2\\))", "Uptake of nitrogen and release of oxygen", "Uptake of carbon dioxide and release of oxygen", "Release of both oxygen and carbon monoxide")
            ],
            'tmpls': [
                "Which respiratory bioenergetic pathway is defined as: {0}?",
                "Name the cytosolic metabolic sequence described as: {0}.",
                "Where in eukaryotic cells does the following event occur: {0}?",
                "Which anaerobic fermentation pathway corresponds to: {0}?",
                "Identify the muscle metabolic adaptation defined by: {0}.",
                "Which biochemical molecule represents: {0}?",
                "What is the comparative ATP yield described by: {0}?",
                "Identify the chemical stoichiometric equation for: {0}.",
                "Which chemical reaction equation represents: {0}?",
                "What fundamental gas exchange dynamic is described as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Identify Pathway and Conditions**\\nThe statement details {item[0]}.\\n**Step 2: Biochemical Reaction Analysis**\\nGlycolysis occurs in cytosol; in oxygen presence pyruvate enters mitochondria yielding 36-38 ATP, whereas anaerobic branches yield 2 ATP with ethanol or lactate.\\n**Step 3: Verification**\\nThe correct biological answer is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Respiratory Organs across Animal Groups & Human Breathing
        {
            'data': [
                ("the respiratory mechanism in earthworms where gases diffuse directly across a thin, moist, mucus-covered vascular skin", "Cutaneous respiration", "Pulmonary respiration", "Tracheal respiration", "Branchial respiration"),
                ("the network of air tubes (tracheae) opening via spiracles on the body surface used for respiration in insects (e.g., cockroaches)", "Tracheal system (spiracles and tracheae)", "Book lungs", "Gills (ctenidia)", "Cutaneous vascular network"),
                ("the specialized vascular respiratory organs in aquatic fish that extract dissolved oxygen from water via counter-current flow", "Gills (Branchiae)", "Lungs", "Air sacs", "Skin pores"),
                ("the dome-shaped muscular sheet separating the thoracic and abdominal cavities that contracts and flattens during inhalation", "Diaphragm", "Intercostal fascia", "Peritoneum", "Pericardium"),
                ("the microscopic air sacs surrounded by dense capillary networks in human lungs where gas exchange occurs", "Alveoli (pulmonary alveoli)", "Bronchioles", "Tracheal rings", "Pleural cavities"),
                ("the physiological mechanism causing air to rush into human lungs during inhalation (inspiration)", "Diaphragm contracts and flattens, ribcage moves up and out, thoracic volume increases, intra-alveolar pressure drops below atmospheric pressure", "Diaphragm relaxes and arches up, thoracic volume decreases", "Abdominal muscles compress visceral organs forcing air inward", "Lungs actively contract like muscle pumps"),
                ("the iron-containing respiratory pigment present in red blood cells that reversibly binds oxygen to form oxyhemoglobin", "Hemoglobin", "Hemocyanin", "Myoglobin", "Chlorocruorin"),
                ("the percentage of oxygen (\\(O_2\\)) and carbon dioxide (\\(CO_2\\)) in inhaled atmospheric air versus exhaled alveolar air", "Inhaled: ~21% \\(O_2\\), 0.04% \\(CO_2\\); Exhaled: ~16.4% \\(O_2\\), 4.4% \\(CO_2\\)", "Inhaled: 78% \\(O_2\\), 21% \\(CO_2\\); Exhaled: 21% \\(O_2\\), 78% \\(CO_2\\)", "Inhaled: 16% \\(O_2\\), 4% \\(CO_2\\); Exhaled: 21% \\(O_2\\), 0.04% \\(CO_2\\)", "Inhaled: 50% \\(O_2\\), 50% \\(CO_2\\); Exhaled: 0% \\(O_2\\), 10% \\(CO_2\\)"),
                ("the normal resting breathing rate in healthy adult humans", "12 to 18 breaths per minute", "40 to 60 breaths per minute", "2 to 4 breaths per minute", "72 to 80 breaths per minute"),
                ("the chemical indicator used in school laboratories to prove that exhaled breath contains carbon dioxide by turning from clear to milky", "Limewater (aqueous calcium hydroxide, \\(Ca(OH)_2\\))", "Litmus solution", "Phenolphthalein in acid", "Iodine solution")
            ],
            'tmpls': [
                "Which respiratory adaptation in annelids is defined as: {0}?",
                "Name the arthropod respiratory apparatus characterized by: {0}.",
                "Which aquatic respiratory organ corresponds to: {0}?",
                "Identify the major mammalian breathing muscle: {0}.",
                "What microscopic functional lung structures represent: {0}?",
                "Which physiological thoracic volume mechanism explains: {0}?",
                "Identify the metalloprotein respiratory pigment described as: {0}.",
                "What are the precise gas volume fractions for: {0}?",
                "What is the typical healthy physiological baseline for: {0}?",
                "Which laboratory chemical reagent is used to verify: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Understand Respiratory Structure**\\nThe question describes {item[0]}.\\n**Step 2: Physiological Gas Exchange Mechanism**\\nRespiratory surfaces require thin walls, large surface area, moisture, and rich vascular supply to maximize gas diffusion rate.\\n**Step 3: Verification**\\nThe correct match is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Dental formula, Tooth types, & Digestive disorders
        {
            'data': [
                ("the permanent adult human dental formula representing teeth in one half of upper and lower jaw", "\\(\\frac{2, 1, 2, 3}{2, 1, 2, 3}\\) (2 incisors, 1 canine, 2 premolars, 3 molars)", "\\(\\frac{2, 1, 0, 2}{2, 1, 0, 2}\\)", "\\(\\frac{3, 1, 4, 3}{3, 1, 4, 3}\\)", "\\(\\frac{1, 2, 3, 4}{1, 2, 3, 4}\\)"),
                ("the deciduous (milk) dental formula in human children representing 20 temporary teeth", "\\(\\frac{2, 1, 0, 2}{2, 1, 0, 2}\\) (2 incisors, 1 canine, 0 premolars, 2 molars)", "\\(\\frac{2, 1, 2, 3}{2, 1, 2, 3}\\)", "\\(\\frac{1, 1, 2, 1}{1, 1, 2, 1}\\)", "\\(\\frac{2, 0, 2, 2}{2, 0, 2, 2}\\)"),
                ("the hardest substance in the human body that forms the outer protective coating of the tooth crown", "Tooth enamel (calcium hydroxyapatite)", "Dentine", "Cementum", "Bone matrix"),
                ("the sharp, pointed teeth specialized for piercing and tearing flesh in carnivorous mammals", "Canines", "Incisors", "Premolars", "Wisdom molars"),
                ("the chisel-shaped front teeth specialized for cutting and biting food items", "Incisors", "Canines", "Molars", "Bicuspids"),
                ("the condition caused by acid-producing oral bacteria fermenting trapped dietary sugars on teeth leading to enamel demineralization", "Dental caries (tooth decay)", "Gingivitis", "Pyorrhea", "Fluorosis"),
                ("the yellowish sticky film consisting of saliva, food particles, and bacterial colonies that adheres to tooth surfaces", "Dental plaque", "Tartar (calculus)", "Dentine", "Enamel prism"),
                ("the digestive disorder characterized by burning sensation in the chest (heartburn) due to acid regurgitation through the gastroesophageal sphincter", "Acid reflux / Acidity (GERD)", "Jaundice", "Appendicitis", "Constipation"),
                ("the abnormal accumulation of bilirubin in blood and body tissues turning the skin and sclera of the eyes yellow, caused by liver dysfunction or bile duct blockage", "Jaundice (Hyperbilirubinemia)", "Anemia", "Hepatomegaly", "Cirrhosis"),
                ("the physiological purpose of administering Oral Rehydration Solution (ORS) during severe diarrhea and vomiting", "To restore lost water and essential electrolytes (sodium, potassium, glucose) to prevent fatal dehydration", "To destroy pathogenic bacteria in stomach", "To provide digestive enzymes to intestines", "To reduce gastric hydrochloric acid secretion")
            ],
            'tmpls': [
                "Which anatomical formula represents: {0}?",
                "Identify the pediatric dental formula characterized as: {0}.",
                "Name the highly mineralized anatomical tissue described as: {0}.",
                "Which morphological tooth class corresponds to: {0}?",
                "Which anterior tooth type is specialized for: {0}?",
                "Which oral microbial pathology is described by: {0}?",
                "What clinical biofilm is defined as: {0}?",
                "Identify the gastrointestinal symptom complex defined by: {0}.",
                "Which hepatic/biliary clinical condition matches: {0}?",
                "What is the clinical therapeutic rationale for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Clinical / Anatomical Concept**\\nThe query highlights {item[0]}.\\n**Step 2: Dental and Digestive Pathology**\\nDental health and gastrointestinal balance depend on structural integrity, microbial balance, and proper hydration.\\n**Step 3: Conclusion**\\nThe correct concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Plant respiration, Stomata & Lenticels
        {
            'data': [
                ("the microscopic pores present on the epidermis of plant leaves guarded by kidney-shaped (or dumb-bell) guard cells for gas exchange", "Stomata", "Lenticels", "Hydathodes", "Phelloderm"),
                ("the loose, porous cell openings present on the woody bark of mature tree stems facilitating gas exchange", "Lenticels", "Stomata", "Plasmodesmata", "Trichomes"),
                ("the mechanism regulating stomatal opening in green leaves during daylight", "Accumulation of potassium (\\(K^+\\)) ions in guard cells causes water influx by endosmosis, increasing turgor pressure so guard cells curve outward", "Loss of water causing plasmolysis of guard cells", "Direct closing under intense sunlight", "Deposition of suberin in guard cell walls"),
                ("the key metabolic difference between plant gas exchange during daytime versus nighttime", "Daytime: photosynthesis exceeds respiration, net release of \\(O_2\\); Nighttime: only respiration occurs, net release of \\(CO_2\\)", "Plants only respire during the day and sleep at night", "Daytime plants take in \\(O_2\\) and release nitrogen", "Nighttime plants perform photosynthesis using moonlight"),
                ("the adaptation of mangrove trees growing in waterlogged, saline, oxygen-deficient coastal soils where roots grow vertically upward above water", "Pneumatophores (respiratory roots with pneumathodes)", "Prop roots", "Stilt roots", "Haustorial roots"),
                ("the plant organelle where the biochemical reactions of cellular respiration occur to oxidize glucose produced during photosynthesis", "Mitochondria", "Chloroplast", "Central vacuole", "Peroxisome"),
                ("the water droplets appearing along leaf margins of herbaceous plants in early morning due to root pressure when transpiration is suppressed", "Guttation (via hydathodes)", "Transpiration", "Condensation", "Evaporation"),
                ("the rate of respiration in germinating seeds compared to dormant dry seeds", "Significantly higher in germinating seeds due to intense cellular division and metabolic growth", "Equal in both states", "Lower in germinating seeds", "Completely absent in germinating seeds"),
                ("the biological reason why plants in completely waterlogged soils wilt and die", "Water displaces soil air pockets, suffocating root cells due to lack of oxygen for aerobic root respiration", "Excess water dilutes plant chlorophyll pigments", "Root cells absorb too much oxygen and burst", "Water prevents roots from absorbing sunlight"),
                ("the gas absorbed by plants during respiration versus the gas absorbed during photosynthesis", "Respiration absorbs \\(O_2\\); Photosynthesis absorbs \\(CO_2\\)", "Respiration absorbs \\(CO_2\\); Photosynthesis absorbs \\(O_2\\)", "Both absorb \\(CO_2\\)", "Both absorb \\(N_2\\)")
            ],
            'tmpls': [
                "Which foliar epidermal structure is characterized as: {0}?",
                "Name the woody stem gas exchange opening defined as: {0}.",
                "Which physiological turgor mechanism explains: {0}?",
                "What is the diurnal metabolic gas exchange distinction in: {0}?",
                "Which specialized halophytic root adaptation is described by: {0}?",
                "Which organelle in plant cells carries out: {0}?",
                "Which botanical fluid exudation phenomenon represents: {0}?",
                "How does metabolic activity compare in: {0}?",
                "What physiological failure mechanism explains: {0}?",
                "What is the exact gas intake distinction specified by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Botanical Concept Analysis**\\nThe prompt addresses {item[0]}.\\n**Step 2: Plant Gas Exchange Mechanisms**\\nPlants respire continuously through stomata, lenticels, and root surfaces, while photosynthesis occurs concurrently only in light.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Nutrition, Respiration & Calorimetry
        {
            'data': [
                ("A food sample containing \\(10\\text{ g}\\) of carbohydrates, \\(5\\text{ g}\\) of proteins, and \\(2\\text{ g}\\) of fats is metabolized. Taking physiological fuel values as \\(4\\text{ kcal/g}\\) for carbohydrates, \\(4\\text{ kcal/g}\\) for proteins, and \\(9\\text{ kcal/g}\\) for fats, calculate total energy yield.", "\\(78\\text{ kcal}\\)", "\\(68\\text{ kcal}\\)", "\\(88\\text{ kcal}\\)", "\\(100\\text{ kcal}\\)"),
                ("A yeast culture completely ferments \\(3\\text{ moles}\\) of glucose anaerobically into ethanol. Calculate the total moles of carbon dioxide (\\(CO_2\\)) gas released.", "\\(6\\text{ moles of } CO_2\\)", "\\(3\\text{ moles of } CO_2\\)", "\\(12\\text{ moles of } CO_2\\)", "\\(1.5\\text{ moles of } CO_2\\)"),
                ("Calculate the theoretical net ATP yield produced by the complete aerobic oxidation of \\(5\\text{ molecules}\\) of glucose in a eukaryotic cell (assuming \\(38\\text{ ATP}\\) per glucose).", "\\(190\\text{ ATP}\\)", "\\(150\\text{ ATP}\\)", "\\(100\\text{ ATP}\\)", "\\(76\\text{ ATP}\\)"),
                ("An athlete inhales \\(500\\text{ mL}\\) of tidal air per breath containing \\(21\\%\\) oxygen and exhales air containing \\(16\\%\\) oxygen. Calculate the volume of oxygen absorbed per single breath.", "\\(25\\text{ mL}\\)", "\\(50\\text{ mL}\\)", "\\(15\\text{ mL}\\)", "\\(105\\text{ mL}\\)"),
                ("If a person's resting respiratory rate is \\(16\\text{ breaths per minute}\\) and tidal volume is \\(500\\text{ mL}\\), calculate the total pulmonary ventilation volume per minute.", "\\(8.0\\text{ litres/min } (8000\\text{ mL})\\)", "\\(5.0\\text{ litres/min}\\)", "\\(10.5\\text{ litres/min}\\)", "\\(12.0\\text{ litres/min}\\)"),
                ("In an experiment, \\(2\\text{ moles}\\) of glucose undergo lactic acid fermentation in muscle cells under oxygen deficit. How many moles of lactic acid and net ATP are formed?", "\\(4\\text{ moles of lactic acid and } 4\\text{ moles of ATP}\\)", "\\(2\\text{ moles of lactic acid and } 2\\text{ moles of ATP}\\)", "\\(4\\text{ moles of lactic acid and } 76\\text{ moles of ATP}\\)", "\\(2\\text{ moles of lactic acid and } 38\\text{ moles of ATP}\\)"),
                ("Calculate the total number of permanent teeth in an adult human jaw containing \\(8\\text{ incisors}\\), \\(4\\text{ canines}\\), \\(8\\text{ premolars}\\), and \\(12\\text{ molars}\\).", "\\(32\\text{ teeth}\\)", "\\(28\\text{ teeth}\\)", "\\(30\\text{ teeth}\\)", "\\(24\\text{ teeth}\\)"),
                ("A child has \\(20\\text{ deciduous (milk) teeth}\\). When replaced by the permanent dentition of \\(32\\text{ teeth}\\), how many additional permanent teeth erupt that had no milk predecessors?", "\\(12\\text{ permanent teeth (premolars and 3rd molars)}\\)", "\\(8\\text{ teeth}\\)", "\\(16\\text{ teeth}\\)", "\\(4\\text{ teeth}\\)"),
                ("A person consumes a meal of \\(40\\text{ g}\\) fat. If pancreatic lipase hydrolyzes this completely into fatty acids and glycerol, what is the caloric energy obtained assuming \\(9\\text{ kcal/g}\\)?", "\\(360\\text{ kcal}\\)", "\\(160\\text{ kcal}\\)", "\\(400\\text{ kcal}\\)", "\\(280\\text{ kcal}\\)"),
                ("During respiration, the respiratory quotient \\(\\text{RQ} = \\frac{\\text{Volume of } CO_2 \\text{ evolved}}{\\text{Volume of } O_2 \\text{ consumed}}\\). For complete oxidation of glucose (\\(C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O\\)), calculate the theoretical RQ value.", "\\(1.0\\)", "\\(0.7\\)", "\\(0.85\\)", "\\(1.33\\)")
            ],
            'tmpls': [
                "Solve the following physiological caloric calculation: {0}",
                "Calculate the fermentation stoichiometry result: {0}",
                "Evaluate the net bioenergetic ATP yield: {0}",
                "Determine the pulmonary gas uptake quantity: {0}",
                "Compute the minute ventilation rate: {0}",
                "Solve the anaerobic muscular conversion problem: {0}",
                "Calculate the total anatomical count for: {0}",
                "Determine the permanent dental succession difference: {0}",
                "Evaluate the total lipid caloric energy: {0}",
                "Compute the theoretical respiratory quotient: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the stoichiometric coefficients, caloric multipliers, or physiological formulas from the problem.\\n**Step 2: Arithmetic Evaluation**\\nPerform the stepwise algebraic multiplication or division.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_19_1_4():
    tc = "MH-9-SCIT-19-19.1.4"
    tname = "Circulation and transportation of substances in animals & plants"
    archs = [
        # Arch 0: Plant Transportation: Xylem, Phloem & Mechanisms
        {
            'data': [
                ("the specialized complex permanent vascular tissue responsible for conducting water and dissolved mineral salts unidirectionally from roots to leaves", "Xylem (tracheids, vessels, xylem parenchyma, xylem fibers)", "Phloem", "Collenchyma", "Sclerenchyma"),
                ("the living complex permanent vascular tissue responsible for bidirectional translocation of synthesized sugars (sucrose) and amino acids from source to sink", "Phloem (sieve tubes, companion cells, phloem parenchyma, phloem fibers)", "Xylem", "Cambium", "Cortex"),
                ("the loss of water in the form of water vapor from the aerial surfaces of leaves primarily through stomata", "Transpiration", "Guttation", "Inbibition", "Precipitation"),
                ("the physical mechanism explaining the upward continuous ascent of sap in tall trees driven by cohesion, adhesion, and transpirational suction pull", "Cohesion-Tension / Transpiration Pull Theory (Dixon and Joly)", "Root Pressure Theory exclusively", "Capillary Action alone", "Active mechanical pumping by xylem"),
                ("the hydrostatic pressure developed in root cortical cells due to active absorption of mineral ions that forces water upward in herbaceous stems", "Root pressure", "Transpiration pull", "Turgor pressure", "Osmotic potential"),
                ("the physiological process of transporting photosynthetic food products from leaves to storage organs and growing points", "Translocation (requiring metabolic energy in the form of ATP)", "Transpiration", "Guttation", "Desiccation"),
                ("the living cells in phloem that lack nuclei at maturity and possess perforated end walls forming continuous conduits for sucrose transport", "Sieve tube elements", "Xylem vessels", "Tracheids", "Sclereids"),
                ("the specialized parenchymatous cells intimately associated with sieve tube elements via plasmodesmata that regulate sieve tube transport activities", "Companion cells", "Guard cells", "Subsidiary cells", "Mesophyll cells"),
                ("the physical forces of attraction between water molecules (cohesion) and between water molecules and xylem vessel walls (adhesion)", "Cohesion and Adhesion forces", "Gravitational electrostatic forces", "Ionic bond attractions", "Van der Waals London forces only"),
                ("the classic tree trunk ringing (girdling) experiment removing the bark and phloem layer demonstrates that", "Phloem transports food, leading to swelling above the ring and starvation of roots below", "Xylem transports sugars to leaves", "Roots transport food to leaves", "Leaves cannot absorb carbon dioxide")
            ],
            'tmpls': [
                "Which plant vascular conducting tissue is defined as: {0}?",
                "Name the bidirectional nutrient-transporting phloem complex described as: {0}.",
                "Which evaporative plant water loss process corresponds to: {0}?",
                "Which classical biophysical theory accounts for: {0}?",
                "What positive hydrostatic root mechanism is characterized by: {0}?",
                "Which active botanical transport mechanism is defined as: {0}?",
                "Identify the specialized enucleated vascular conduits: {0}.",
                "Which metabolic regulator cells correspond to: {0}?",
                "Which biophysical intermolecular forces explain: {0}?",
                "What conclusion is experimentally deduced from: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Understand Plant Transport Vascularization**\\nThe statement details {item[0]}.\\n**Step 2: Mechanism Analysis**\\nXylem transports sap unidirectionally via transpiration pull and root pressure; phloem translocates photosynthates bidirectionally via sieve tubes and companion cells.\\n**Step 3: Verification**\\nThe correct component is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Human Heart Structure & Chambers
        {
            'data': [
                ("the tough, double-walled protective sac filled with fluid that encloses the human heart to reduce friction during heartbeats", "Pericardium (with pericardial fluid)", "Pleura", "Peritoneum", "Endocardium"),
                ("the four distinct muscular chambers making up the human heart", "Two thin-walled upper atria (auricles) and two thick-walled lower ventricles", "Two ventricles and two aortas", "Four ventricles", "One atrium and three ventricles"),
                ("the thick muscular chamber of the heart that pumps oxygenated blood with maximum pressure into the systemic aorta to supply the entire body", "Left ventricle (thickest myocardium)", "Right ventricle", "Left atrium", "Right atrium"),
                ("the valve situated between the left atrium and left ventricle preventing backflow of oxygenated blood", "Bicuspid (Mitral) valve", "Tricuspid valve", "Pulmonary semilunar valve", "Aortic semilunar valve"),
                ("the valve situated between the right atrium and right ventricle preventing backflow of deoxygenated blood", "Tricuspid valve", "Bicuspid (Mitral) valve", "Semilunar valve", "Eustachian valve"),
                ("the muscular dividing wall that completely separates the right and left sides of the heart preventing mixing of oxygenated and deoxygenated blood", "Interventricular and interatrial septum", "Pericardium", "Endocardium", "Myocardium"),
                ("the semilunar valves located at the bases of the two major outflow arteries from the ventricles", "Pulmonary semilunar valve and Aortic semilunar valve", "Bicuspid and Tricuspid valves", "Mitral and venous valves", "Pyloric and cardiac valves"),
                ("the specialized neuromuscular tissue located in the right atrium known as the natural cardiac pacemaker generating rhythmic electrical impulses", "Sinoatrial node (SA node)", "Atrioventricular node (AV node)", "Bundle of His", "Purkinje fibers"),
                ("the strong, non-elastic fibrous cords connecting the papillary muscles of ventricular walls to the cusps of atrioventricular valves", "Chordae tendineae", "Ligamentum arteriosum", "Coronary ligaments", "Trabeculae carneae"),
                ("the specific blood vessels that supply oxygenated blood and nutrients directly to the muscular heart myocardium itself", "Coronary arteries", "Carotid arteries", "Pulmonary arteries", "Renal arteries")
            ],
            'tmpls': [
                "Which protective cardiac membrane is characterized as: {0}?",
                "Describe the anatomical arrangement comprising: {0}.",
                "Which high-pressure pumping chamber represents: {0}?",
                "Which left atrioventricular valve corresponds to: {0}?",
                "Which right atrioventricular valve corresponds to: {0}?",
                "Identify the muscular cardiac partition defined by: {0}.",
                "Which arterial outflow gates represent: {0}?",
                "Identify the cardiac pacemaker tissue described as: {0}.",
                "Which fibrous structural cords correspond to: {0}?",
                "Which specialized vascular branches supply: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Anatomical Identification**\\nThe query focuses on {item[0]}.\\n**Step 2: Cardiac Chamber and Valve Dynamics**\\nDeoxygenated blood enters the right side; oxygenated blood enters the left side. Heart valves ensure strictly unidirectional flow.\\n**Step 3: Verification**\\nThe correct structure is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Blood Vessels: Arteries, Veins, & Capillaries
        {
            'data': [
                ("thick-walled, highly elastic muscular blood vessels that carry oxygenated blood under high pressure away from the heart to tissues (except pulmonary artery)", "Arteries", "Veins", "Capillaries", "Lymphatics"),
                ("thin-walled, wide-lumen blood vessels possessing internal valves that carry deoxygenated blood under low pressure back toward the heart (except pulmonary vein)", "Veins", "Arteries", "Arterioles", "Capillaries"),
                ("microscopic, single-endothelial-cell thick blood vessels where actual diffusion of nutrients, gases, and wastes between blood and tissue fluid occurs", "Capillaries", "Arteries", "Veins", "Venules"),
                ("the only artery in the human body that carries deoxygenated blood from the right ventricle to the lungs for oxygenation", "Pulmonary artery", "Aorta", "Renal artery", "Carotid artery"),
                ("the only veins in the human body that carry fully oxygenated blood from the lungs into the left atrium of the heart", "Pulmonary veins (four in number)", "Superior vena cava", "Inferior vena cava", "Jugular veins"),
                ("the largest systemic artery in the human body originating directly from the left ventricle", "Aorta (Systemic aorta)", "Superior vena cava", "Pulmonary trunk", "Subclavian artery"),
                ("the two largest veins that return deoxygenated venous blood from upper and lower body parts into the right atrium", "Superior and Inferior Vena Cava", "Pulmonary veins", "Portal veins", "Carotid sinuses"),
                ("the physiological reason why veins possess internal pocket-like valves while systemic arteries do not", "To prevent backflow of blood under low pressure and against the pull of gravity", "To increase heart pumping speed", "To filter bacteria from blood", "To absorb oxygen directly through vein walls"),
                ("the physiological condition known as arteriosclerosis or atherosclerosis", "Narrowing and hardening of arterial walls due to cholesterol plaque deposition restricting blood flow", "Inflammation of vein valves", "Rupture of capillary beds", "Excessive dilation of lymphatic ducts"),
                ("the pressure exerted by circulating blood against the walls of systemic arteries during ventricular contraction (systole) and ventricular relaxation (diastole)", "Blood pressure (normal resting value: \\(120/80\\text{ mmHg}\\))", "Pulse pressure", "Hydrostatic osmotic pressure", "Central venous pressure")
            ],
            'tmpls': [
                "Which vascular vessel class is defined as: {0}?",
                "Which low-pressure vascular vessels correspond to: {0}?",
                "Which microvascular diffusion networks represent: {0}?",
                "Which exceptional arterial conduit carries: {0}?",
                "Which exceptional venous conduits carry: {0}?",
                "Identify the primary systemic artery described as: {0}.",
                "Which major caval conduits are characterized as: {0}?",
                "What physiological necessity explains: {0}?",
                "Which arterial cardiovascular pathology is defined by: {0}?",
                "Which hemodynamic metric is described as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Vascular Vessel Structure**\\nThe question targets {item[0]}.\\n**Step 2: Comparison of Vessels**\\nArteries have thick elastic walls and no valves; veins have thin walls, wide lumens, and valves; capillaries consist of a single layer of endothelial cells for rapid diffusion.\\n**Step 3: Verification**\\nThe correct vessel entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Blood Composition: Plasma, RBCs, WBCs & Platelets
        {
            'data': [
                ("the straw-colored, slightly alkaline liquid matrix comprising ~55% of total blood volume consisting of water (90-92%), proteins, salts, and nutrients", "Blood plasma", "Formed elements", "Lymph fluid", "Serum alone"),
                ("the non-nucleated biconcave disc-shaped cells packed with hemoglobin specialized for transporting oxygen in blood", "Red blood cells (Erythrocytes / RBCs)", "White blood cells (Leukocytes)", "Platelets (Thrombocytes)", "Macrophages"),
                ("the average lifespan of human red blood cells before being broken down and recycled in the spleen and liver", "Approximately 120 days", "3 to 5 days", "10 to 12 hours", "Over 10 years"),
                ("the nucleated, amoeboid blood cells responsible for immune defense, destroying pathogens, and producing antibodies", "White blood cells (Leukocytes / WBCs)", "Erythrocytes", "Platelets", "Reticulocytes"),
                ("the small, non-nucleated cell fragments derived from megakaryocytes in bone marrow essential for blood clotting and hemostasis", "Platelets (Thrombocytes)", "Erythrocytes", "Neutrophils", "Monocytes"),
                ("the major plasma protein responsible for maintaining blood colloid osmotic (oncotic) pressure preventing fluid leakage into tissues", "Albumin", "Fibrinogen", "Immunoglobulin G", "Prothrombin"),
                ("the soluble plasma protein converted into insoluble fibrin meshwork during blood coagulation to seal wounds", "Fibrinogen", "Albumin", "Globulin", "Heparin"),
                ("the fluid that remains when blood has clotted and the cellular elements and fibrinogen have been removed", "Blood serum", "Plasma", "Lymph", "Synovial fluid"),
                ("the condition characterized by abnormally low red blood cell count or low hemoglobin concentration impairing oxygen delivery", "Anemia", "Polycythemia", "Leukemia", "Thrombocytopenia"),
                ("the natural anticoagulant produced by mast cells and basophils that prevents intravascular blood clotting within intact vessels", "Heparin", "Histamine", "Fibrin", "Thrombin")
            ],
            'tmpls': [
                "Which liquid blood compartment is defined as: {0}?",
                "Which cellular corpuscle class is described as: {0}?",
                "What is the average physiological duration for: {0}?",
                "Which immune blood cells correspond to: {0}?",
                "Which hemostatic cellular fragments represent: {0}?",
                "Which major oncotic plasma protein is identified as: {0}?",
                "Which coagulation precursor protein corresponds to: {0}?",
                "What biological fluid residue is characterized as: {0}?",
                "Which hematological deficiency disorder is defined by: {0}?",
                "Which endogenous anticoagulant is described as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Hematological Component Analysis**\\nThe prompt highlights {item[0]}.\\n**Step 2: Functional Role in Circulation**\\nBlood is composed of fluid plasma (~55%) and formed elements (~45%: RBCs for gas transport, WBCs for immunity, and platelets for clotting).\\n**Step 3: Verification**\\nThe correct match is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Double Circulation, Cardiac Cycle & Blood Pressure
        {
            'data': [
                ("the circulatory pathway where blood travels from the right ventricle through pulmonary arteries to lungs and returns via pulmonary veins to the left atrium", "Pulmonary circulation", "Systemic circulation", "Hepatic portal circulation", "Coronary circulation"),
                ("the circulatory pathway where oxygenated blood is pumped from left ventricle through aorta to systemic tissues and deoxygenated blood returns via vena cava to right atrium", "Systemic circulation", "Pulmonary circulation", "Lymphatic circulation", "Cerebral circulation"),
                ("the phenomenon in humans and birds where blood passes twice through the heart during one complete circuit of the body", "Double circulation (pulmonary and systemic)", "Single circulation (as in fishes)", "Open circulation (as in insects)", "Triple incomplete circulation"),
                ("the phase of the cardiac cycle during which ventricular heart muscle contracts and pumps blood out into arteries", "Ventricular systole", "Ventricular diastole", "Atrial diastole", "Joint diastole"),
                ("the phase of the cardiac cycle during which ventricular heart muscle relaxes and chambers fill with blood", "Ventricular diastole", "Ventricular systole", "Isovolumetric contraction", "Atrial systole"),
                ("the first heart sound ('lubb') heard through a stethoscope during a cardiac examination is produced by", "Simultaneous closure of the atrioventricular (bicuspid and tricuspid) valves at the onset of ventricular systole", "Closure of aortic and pulmonary semilunar valves", "Rapid rush of blood through capillaries", "Contraction of the pericardium"),
                ("the second heart sound ('dubb') heard through a stethoscope is produced by", "Simultaneous closure of the semilunar (aortic and pulmonary) valves at the onset of ventricular diastole", "Closure of atrioventricular valves", "Opening of the mitral valve", "Turbulence in the vena cava"),
                ("the medical instrument used to measure arterial blood pressure non-invasively using an inflatable arm cuff and manometer", "Sphygmomanometer", "Stethoscope", "Electrocardiograph (ECG)", "Spirometer"),
                ("the medical instrument invented by René Laennec used for listening to internal sounds of the heart and lungs", "Stethoscope", "Sphygmomanometer", "Thermometer", "Otoscope"),
                ("the clinical condition characterized by persistently elevated resting arterial blood pressure exceeding \\(140/90\\text{ mmHg}\\)", "Hypertension (high blood pressure)", "Hypotension", "Atherosclerosis", "Bradycardia")
            ],
            'tmpls': [
                "Which specific cardiovascular circuit is defined as: {0}?",
                "Which extensive systemic circuit corresponds to: {0}?",
                "Which mammalian circulatory design represents: {0}?",
                "Which mechanical cardiac cycle phase is defined as: {0}?",
                "Which cardiac ventricular relaxation phase corresponds to: {0}?",
                "What cardiac valve event produces: {0}?",
                "What valve closure event generates: {0}?",
                "Which clinical diagnostic instrument is described as: {0}?",
                "Name the auscultatory medical device invented by René Laennec: {0}.",
                "Which clinical hemodynamic condition is defined by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cardiovascular Dynamics Context**\\nThe description refers to {item[0]}.\\n**Step 2: Functional Hemodynamics**\\nDouble circulation prevents mixing of oxygenated and deoxygenated blood; systole and diastole drive rhythmic heart sounds and blood pressure cycles.\\n**Step 3: Verification**\\nThe correct identification is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Blood Groups, ABO System, Rh Factor & Transfusion Rules
        {
            'data': [
                ("the Austrian biologist and physician who discovered the ABO human blood group system in 1900 and received the Nobel Prize in 1930", "Karl Landsteiner", "William Harvey", "Alexander Fleming", "Robert Koch"),
                ("the blood group whose red blood cells possess both A and B antigens and lacks both anti-A and anti-B antibodies in plasma, known as the universal recipient", "Blood Group AB (specifically AB+)", "Blood Group O (specifically O-)", "Blood Group A", "Blood Group B"),
                ("the blood group whose red blood cells lack both A and B antigens and whose plasma contains both anti-A and anti-B antibodies, known as the universal donor", "Blood Group O (specifically O-)", "Blood Group AB", "Blood Group A+", "Blood Group B+"),
                ("the red blood cell antigen first discovered in Rhesus macaque monkeys present in ~85% of human populations (Rh-positive)", "Rh factor (D-antigen)", "H-antigen", "MHC complex", "HLA-A antigen"),
                ("the severe hemolytic disease of the newborn occurring when an Rh-negative mother carries a second Rh-positive fetus", "Erythroblastosis fetalis (Hemolytic disease of the newborn)", "Sickle cell anemia", "Thalassemia major", "Hemophilia A"),
                ("the physiological reaction of clumping and hemolysis occurring when incompatible blood groups are transfused due to antigen-antibody reaction", "Agglutination", "Coagulation", "Sedimentation", "Hemoconcentration"),
                ("the English physician who first discovered and described the complete systemic circulation of blood pumped by the heart in 1628", "William Harvey", "Andreas Vesalius", "Hippocrates", "Marcello Malpighi"),
                ("a person with blood group A positive can safely donate red blood cells to individuals with which blood groups", "Blood Groups A+ and AB+", "Blood Groups A+ and O+", "Blood Groups B+ and AB+", "Blood Group O- only"),
                ("a person with blood group B negative can safely receive red blood cells from which blood groups", "Blood Groups B- and O-", "Blood Groups B+ and AB+", "Blood Group AB- only", "Blood Groups A- and O-"),
                ("the temperature at which collected donor blood is preserved in blood banks with anticoagulant solutions (e.g., CPD / ACD)", "Between \\(2^\\circ\\text{C}\\) and \\(6^\\circ\\text{C}\\) (typically \\(4^\\circ\\text{C}\\))", "At \\(-20^\\circ\\text{C}\\)", "At room temperature (\\(25^\\circ\\text{C}\\))", "At human body temperature (\\(37^\\circ\\text{C}\\))")
            ],
            'tmpls': [
                "Name the pioneering Nobel laureate associated with: {0}.",
                "Which immunological phenotype is characterized as: {0}?",
                "Which universal donor phenotype matches: {0}?",
                "Which surface erythrocyte antigen is described as: {0}?",
                "Which neonatal isoimmune pathology is defined by: {0}?",
                "Which immunological clumping reaction corresponds to: {0}?",
                "Name the historical English physician who first proved: {0}.",
                "Under transfusion protocol, determine compatibility for: {0}.",
                "In clinical transfusion practice, evaluate recipient rules for: {0}.",
                "What is the standard blood banking storage parameter for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Blood Group and Immunohematology Context**\\nThe statement details {item[0]}.\\n**Step 2: Antigen-Antibody Compatibility**\\nABO compatibility depends on RBC surface antigens and reciprocal plasma antibodies; Rh incompatibility can trigger erythroblastosis fetalis or acute hemolysis.\\n**Step 3: Verification**\\nThe correct concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Lymphatic System & Comparative Circulation
        {
            'data': [
                ("the colorless fluid tissue consisting of blood plasma and lymphocytes that drains from intercellular interstitial spaces back into the venous system", "Lymph (tissue fluid filtrate)", "Bile", "Synovial fluid", "Aqueous humor"),
                ("the specialized primary white blood cells present in lymph nodes responsible for cell-mediated and humoral immune defense", "Lymphocytes (T-cells and B-cells)", "Erythrocytes", "Thrombocytes", "Neutrophils exclusively"),
                ("the circulatory system where blood is pumped into open body cavities (hemocoel) bathing tissues directly, as found in insects and mollusks", "Open circulatory system", "Closed circulatory system", "Double circulatory system", "Lymphatic system"),
                ("the circulatory system where blood remains enclosed inside continuous blood vessels throughout its circulation, as found in earthworms and vertebrates", "Closed circulatory system", "Open circulatory system", "Lacunar circulatory system", "Coelomic vascular system"),
                ("the number of heart chambers and circulatory pattern present in fishes", "Two-chambered heart (one atrium and one ventricle) with single circulation", "Three-chambered heart with incomplete double circulation", "Four-chambered heart with complete double circulation", "One-chambered tubular heart"),
                ("the number of heart chambers present in amphibians and most reptiles", "Three-chambered heart (two atria and one partially divided ventricle)", "Two-chambered heart", "Four-chambered heart with complete separation", "Five-chambered heart"),
                ("the exceptional reptile that possesses a fully four-chambered heart like birds and mammals", "Crocodile", "Lizard (Calotes)", "Snake (Cobra)", "Tortoise"),
                ("the small oval masses of lymphoid tissue located along lymphatic vessels that filter out cellular debris and bacteria from lymph", "Lymph nodes", "Tonsils only", "Peyer's patches only", "Thymus lobes"),
                ("the largest lymphoid organ in the human body located on the left side of the abdomen that filters old RBCs and stores platelets", "Spleen ('graveyard of RBCs')", "Liver", "Pancreas", "Gallbladder"),
                ("the major lymphatic duct that collects lymph from the lower limbs, pelvis, and left upper body and empties into the left subclavian vein", "Thoracic duct (left lymphatic duct)", "Right lymphatic duct", "Cisterna chyli", "Jugular trunk")
            ],
            'tmpls': [
                "Which secondary vascular fluid tissue is characterized as: {0}?",
                "Which immune cells abundantly found in lymphatic tissue match: {0}?",
                "Which invertebrate circulatory architectural design represents: {0}?",
                "Which vertebrate vascular plan is defined as: {0}?",
                "What cardiac anatomy and circulatory dynamic characterizes: {0}?",
                "Which cardiac chamber structure represents: {0}?",
                "Identify the unique reptilian species featuring: {0}.",
                "What encapsulated lymphoid filtration structures represent: {0}?",
                "Which abdominal lymphoid organ corresponds to: {0}?",
                "Name the principal lymphatic drainage conduit defined as: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Identify System and Animal Group**\\nThe question describes {item[0]}.\\n**Step 2: Comparative Circulation Analysis**\\nOpen vs closed circulation, chamber evolution (2 chambers in fish, 3 in amphibians/reptiles, 4 in crocodiles/birds/mammals), and lymphatic filtration ensure fluid homeostasis and immunity.\\n**Step 3: Verification**\\nThe matching biological entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Cardiac Output, Blood Counts & Transpiration
        {
            'data': [
                ("If an adult's resting heart rate is \\(72\\text{ beats per minute}\\) and the stroke volume pumped per ventricular contraction is \\(70\\text{ mL}\\), calculate the total resting cardiac output.", "\\(5.04\\text{ litres per minute } (5040\\text{ mL/min})\\)", "\\(3.50\\text{ litres per minute}\\)", "\\(7.20\\text{ litres per minute}\\)", "\\(1.20\\text{ litres per minute}\\)"),
                ("During strenuous athletic exercise, an athlete's heart rate increases to \\(150\\text{ beats/min}\\) and stroke volume rises to \\(120\\text{ mL}\\). Calculate the exercise cardiac output.", "\\(18.0\\text{ litres per minute } (18000\\text{ mL/min})\\)", "\\(12.0\\text{ litres per minute}\\)", "\\(25.0\\text{ litres per minute}\\)", "\\(9.0\\text{ litres per minute}\\)"),
                ("The duration of a single complete cardiac cycle at a heart rate of \\(75\\text{ beats per minute}\\) is calculated by dividing 60 seconds by 75. What is the precise cardiac cycle duration?", "\\(0.8\\text{ seconds}\\)", "\\(1.0\\text{ second}\\)", "\\(0.5\\text{ seconds}\\)", "\\(0.25\\text{ seconds}\\)"),
                ("Calculate the normal pulse pressure for an individual with an arterial blood pressure of \\(120/80\\text{ mmHg}\\) (Pulse pressure = Systolic pressure - Diastolic pressure).", "\\(40\\text{ mmHg}\\)", "\\(80\\text{ mmHg}\\)", "\\(120\\text{ mmHg}\\)", "\\(200\\text{ mmHg}\\)"),
                ("Calculate the Mean Arterial Pressure (MAP) using the standard clinical formula \\(\\text{MAP} = \\text{Diastolic BP} + \\frac{1}{3}(\\text{Systolic BP} - \\text{Diastolic BP})\\) for \\(120/80\\text{ mmHg}\\).", "\\(93.33\\text{ mmHg}\\)", "\\(100.0\\text{ mmHg}\\)", "\\(80.0\\text{ mmHg}\\)", "\\(110.5\\text{ mmHg}\\)"),
                ("In a laboratory potometer experiment, a leafy shoot absorbs and transpires \\(15\\text{ mL}\\) of water over \\(3\\text{ hours}\\). Calculate the average transpiration rate per hour.", "\\(5.0\\text{ mL per hour}\\)", "\\(15.0\\text{ mL per hour}\\)", "\\(3.0\\text{ mL per hour}\\)", "\\(45.0\\text{ mL per hour}\\)"),
                ("A blood sample of \\(1\\text{ mm}^3\\) (microlitre) from a healthy adult contains \\(5\\text{ million}\\) red blood cells. Calculate the estimated total number of RBCs present in \\(5\\text{ litres}\\) (\\(5 \\times 10^6\\text{ mm}^3\\)) of total circulating blood.", "\\(2.5 \\times 10^{13}\\text{ RBCs } (25\\text{ trillion})\\)", "\\(2.5 \\times 10^{10}\\text{ RBCs}\\)", "\\(1.0 \\times 10^{12}\\text{ RBCs}\\)", "\\(5.0 \\times 10^{14}\\text{ RBCs}\\)"),
                ("If an adult human has \\(5000\\text{ mL}\\) of circulating blood and plasma constitutes \\(55\\%\\) of this volume, calculate the volume of liquid blood plasma.", "\\(2750\\text{ mL}\\)", "\\(2250\\text{ mL}\\)", "\\(3000\\text{ mL}\\)", "\\(1500\\text{ mL}\\)"),
                ("A donor donates \\(350\\text{ mL}\\) of whole blood at a blood donation camp. If the donor's total blood volume is \\(5000\\text{ mL}\\), what percentage of their total blood volume was donated?", "\\(7.0\\%\\)", "\\(12.5\\%\\)", "\\(3.5\\%\\)", "\\(15.0\\%\\)"),
                ("In capillary microcirculation, capillary hydrostatic pressure is \\(32\\text{ mmHg}\\) and plasma colloid oncotic pressure is \\(22\\text{ mmHg}\\). Calculate the net outward filtration pressure at the arteriolar end.", "\\(+10\\text{ mmHg}\\)", "\\(-10\\text{ mmHg}\\)", "\\(+54\\text{ mmHg}\\)", "\\(+22\\text{ mmHg}\\)")
            ],
            'tmpls': [
                "Calculate the resting cardiac output volume: {0}",
                "Evaluate the exercise cardiac output capacity: {0}",
                "Compute the single cardiac cycle duration: {0}",
                "Determine the clinical pulse pressure: {0}",
                "Calculate the mean arterial pressure (MAP): {0}",
                "Compute the potometer transpiration rate: {0}",
                "Evaluate the total erythrocyte circulating count: {0}",
                "Determine the total liquid plasma volume: {0}",
                "Calculate the blood donation fractional percentage: {0}",
                "Compute the capillary net filtration pressure: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the heart rate, stroke volume, pressures, or fluid measurements given in the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply the cardiovascular formula: \\(\\text{{Cardiac Output}} = \\text{{Heart Rate}} \\times \\text{{Stroke Volume}}\\), or corresponding algebraic relation.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
