# scripts/generate_ch8_topic1.py
# Topic: MH-9-SCIT-8-8.1 (Useful Microbes: Lactobacilli, Rhizobium & Yeast)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-8-8.1"
CHAPTER_NUM = 8

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Lactobacilli & Dairy Fermentation
    ("What microscopic morphological shape characterizes the beneficial bacterium Lactobacilli?",
     ["Spherical cocci", "Rod-shaped (bacilli) with blunt or rounded ends", "Spiral spirilla", "Comma-shaped vibrio"],
     "B", "OSC", "easy",
     "- Lactobacilli are non-motile, rod-shaped (bacillus) bacteria.\nCorrect Choice is (B)."),

    ("What sugar naturally present in milk is fermented by Lactobacilli into lactic acid?",
     ["Sucrose", "Lactose (milk sugar)", "Maltose", "Fructose"],
     "B", "OSC", "easy",
     "- Lactobacilli ferment lactose sugar present in milk into lactic acid: \\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11} + \\text{H}_2\\text{O} \\to 4\\text{CH}_3\\text{CH(OH)COOH}\\).\nCorrect Choice is (B)."),

    ("How does the formation of lactic acid turn liquid milk into semi-solid curd (yogurt)?",
     ["By boiling the milk", "Lactic acid lowers the milk pH, causing the primary milk protein (casein) to denature and coagulate into a firm gel", "By adding starch powder", "By evaporating all water"],
     "B", "OSC", "easy",
     "- As lactic acid accumulates, milk pH drops below 4.6 (casein isoelectric point), coagulating casein protein into curd.\nCorrect Choice is (B)."),

    ("Are Lactobacilli aerobic or anaerobic bacteria in their primary metabolic mode of energy generation?",
     ["Strictly obligate aerobes requiring high oxygen", "Anaerobic (or facultative/aerotolerant anaerobes) that can produce energy without using oxygen", "Chemolithotrophic sulfur eaters", "Photosynthetic"],
     "B", "OSC", "medium",
     "- Lactobacilli generate energy via lactic acid fermentation without requiring molecular oxygen.\nCorrect Choice is (B)."),

    ("Why are certain Lactobacilli termed 'probiotics' when consumed in yogurt or kefir?",
     ["They cause severe stomach aches", "They survive gastric acid, colonize the intestines, suppress harmful putrefactive pathogens like Clostridium, and boost digestive immunity", "They destroy all intestinal cells", "They produce plastic fibers"],
     "B", "OSC", "easy",
     "- Probiotics are live beneficial microorganisms that confer health benefits by improving the balance of intestinal microflora.\nCorrect Choice is (B)."),

    ("Which of the following dairy products is manufactured through the commercial activity of Lactobacilli?",
     ["Bread", "Curd, yogurt, buttermilk, and fermented cheeses", "Cane sugar", "Mustard oil"],
     "B", "OSC", "easy",
     "- Lactobacilli are the industrial workhorses producing curd, yogurt, buttermilk, and sour cheeses.\nCorrect Choice is (B)."),

    ("Under the Gram staining method, how do Lactobacilli classify?",
     ["Gram-negative", "Gram-positive (retaining crystal violet dye)", "Acid-fast fungi", "Acellular viruses"],
     "B", "OSC", "medium",
     "- Lactobacilli possess a thick peptidoglycan cell wall and stain Gram-positive (violet/purple).\nCorrect Choice is (B)."),

    ("What gives buttermilk and fresh curd their distinctive pleasant tangy taste?",
     ["Acetic acid (vinegar)", "Lactic acid produced by bacterial fermentation", "Hydrochloric acid", "Citric acid"],
     "B", "OSC", "easy",
     "- Lactic acid imparts the characteristic tangy, sour flavor to curd and buttermilk.\nCorrect Choice is (B)."),

    ("Why does sour buttermilk or curd clean tarnished copper and brass vessels so effectively?",
     ["Because it contains soap", "The mild lactic acid reacts with and dissolves the basic green copper carbonate tarnishing layer, revealing shiny metal", "Because of bacteria eating the metal", "Because of milk fat"],
     "B", "OSC", "medium",
     "- Lactic acid in sour buttermilk neutralizes and dissolves the basic copper carbonate patina (\\(\\text{CuCO}_3\\cdot\\text{Cu(OH)}_2\\)).\nCorrect Choice is (B)."),

    ("In livestock agriculture, what fermented cattle fodder with high nutritional value and long shelf-life is prepared using lactic acid bacteria?",
     ["Dry hay", "Silage (fermented green forage)", "Raw sand", "Wood chips"],
     "B", "OSC", "medium",
     "- Silage is preserved fermented green forage produced by anaerobic lactic fermentation of corn or grasses.\nCorrect Choice is (B)."),

    # 11-20: Rhizobium & Nitrogen Fixation Symbiosis
    ("What symbiotic relationship exists between Rhizobium bacteria and leguminous plants (such as gram, peas, and groundnut)?",
     ["Parasitism where the bacterium kills the plant", "Mutualism where the bacterium supplies fixed nitrates and the plant supplies carbohydrates and shelter", "Commensalism with zero interaction", "Predation"],
     "B", "OSC", "easy",
     "- Mutualism: Rhizobium supplies assimilable nitrates while the legume plant provides photosynthesized carbohydrates and protective nodules.\nCorrect Choice is (B)."),

    ("Where specifically are Rhizobium bacteria housed on the host leguminous plant?",
     ["Inside flower petals", "Inside specialized swollen root nodules along the lateral root system", "Inside leaf stomata", "Inside tree bark"],
     "B", "OSC", "easy",
     "- Rhizobium colonizes the root hairs, triggering root cortical cell proliferation into root nodules.\nCorrect Choice is (B)."),

    ("What biochemical process does Rhizobium perform that is vital for agriculture?",
     ["Alcohol fermentation", "Biological Nitrogen Fixation (converting inert atmospheric \\(\\text{N}_2\\) into nitrates and amino compounds)", "Photosynthesis", "Lactic acid generation"],
     "B", "OSC", "easy",
     "- Rhizobium converts atmospheric \\(\\text{N}_2\\) into ammonia and nitrates using the nitrogenase enzyme system.\nCorrect Choice is (B)."),

    ("Why does cultivating leguminous crops help reduce farmers' dependency on costly chemical nitrogen fertilizers (like urea)?",
     ["Legumes eat weeds", "Rhizobium symbiosis naturally fixes up to 200-300 kg of pure nitrogen per hectare into the soil", "Legumes produce synthetic ammonia gas", "Legumes spray chemicals"],
     "B", "OSC", "easy",
     "- Symbiotic nitrogen fixation replenishes soil nitrates naturally, leaving residual nitrogen for subsequent non-legume crops.\nCorrect Choice is (B)."),

    ("The agricultural practice of coating crop seeds with bacterial cultures before sowing is termed:",
     ["Rhizobial inoculation (seed bacterization)", "Fumigation", "Pasteurization", "Cryopreservation"],
     "A", "OSC", "medium",
     "- Rhizobial seed inoculation ensures dense colonization of emerging seedlings by effective nitrogen-fixing bacterial strains.\nCorrect Choice is (A)."),

    ("Why can Rhizobium NOT fix nitrogen when living freely as independent cells in aerated soil before entering root nodules?",
     ["Because free bacteria are asleep", "Because the nitrogenase enzyme is rapidly inactivated by free oxygen in aerobic soil; the micro-anaerobic nodule with leghemoglobin is strictly required", "Because nitrogen gas is absent in soil air", "Because bacteria need fertilizer"],
     "B", "OSC", "hard",
     "- Nitrogenase is irreversibly denatured by oxygen; only the specialized hypoxic microenvironment inside root nodules permits fixation.\nCorrect Choice is (B)."),

    ("What pinkish protein in root nodules functions as an 'oxygen scavenger' to maintain safe low free \\(\\text{O}_2\\) levels around nitrogenase?",
     ["Hemoglobin", "Leghemoglobin", "Myoglobin", "Bilirubin"],
     "B", "OSC", "medium",
     "- Leghemoglobin binds free oxygen with high affinity, delivering oxygen to bacterial respiration without poisoning nitrogenase.\nCorrect Choice is (B)."),

    ("Which family of flowering plants is famous for its universal association with Rhizobium?",
     ["Poaceae (Grasses)", "Fabaceae / Leguminosae (Pulses and Legumes)", "Solanaceae (Potatoes)", "Brassicaceae (Mustard)"],
     "B", "OSC", "easy",
     "- Family Fabaceae (pulses, beans, clover, alfalfa) hosts symbiotic Rhizobium nodules.\nCorrect Choice is (B)."),

    ("After harvesting leguminous crops, why do farmers frequently plough the remaining root systems back into the soil?",
     ["To attract rodents", "To incorporate the nitrogen-rich root nodule residues as organic green manure that enriches the soil", "To dry the field", "To stop water flow"],
     "B", "OSC", "easy",
     "- Decomposing nodulated legume roots release accumulated organic nitrogen into the soil mineral pool.\nCorrect Choice is (B)."),

    ("State whether True or False: Rhizobium can form nodules and fix nitrogen on wheat, rice, and sugarcane roots.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Rhizobium nodulation is specific to leguminous dicots; it does not naturally form nodules on cereal grasses.\nCorrect Choice is (B)."),

    # 21-30: Yeast & Alcohol Fermentation
    ("What type of organism is Yeast (Saccharomyces cerevisiae)?",
     ["A photosynthetic alga", "A unicellular, eukaryotic heterotrophic fungus", "A prokaryotic bacterium", "A protozoan"],
     "B", "OSC", "easy",
     "- Yeast is a unicellular eukaryotic fungus belonging to Ascomycota.\nCorrect Choice is (B)."),

    ("How does Yeast typically reproduce under favorable, nutrient-rich environmental conditions?",
     ["By seed formation", "Asexually by 'Budding' (forming small daughter outgrowth buds from parent cells)", "By binary fission like bacteria", "By producing pollen"],
     "B", "OSC", "easy",
     "- Yeast reproduces asexually by budding, where a daughter protoplasmic bud emerges, receives a replicated nucleus, and pinches off.\nCorrect Choice is (B)."),

    ("What chemical reaction is catalyzed by Yeast during anaerobic fermentation of sugar solutions?",
     ["\\(\\text{Glucose} \\to \\text{Water} + \\text{Oxygen}\\)",
      "\\(\\text{C}_6\\text{H}_{12}\\text{O}_6 \\to 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 + \\text{Energy}\\) (Ethanol + Carbon Dioxide)",
      "\\(\\text{Glucose} \\to \\text{Lactic acid}\\)",
      "\\(\\text{Glucose} \\to \\text{Methane gas}\\)"],
     "B", "OSC", "easy",
     "- Yeast fermentation breaks 1 molecule of glucose into 2 molecules of ethanol and 2 molecules of carbon dioxide gas.\nCorrect Choice is (B)."),

    ("In bread making, what causes the kneaded dough to rise, swell, and become spongy with soft porous cavities?",
     ["Steam evaporating", "Carbon dioxide (\\(\\text{CO}_2\\)) gas bubbles produced by yeast fermentation get trapped inside the elastic gluten protein matrix, expanding the dough", "Bacteria chewing holes in the dough", "Chemical baking powder only"],
     "B", "OSC", "easy",
     "- \\(\\text{CO}_2\\) gas bubbles released by yeast are trapped within elastic wheat gluten, causing the dough to double in volume.\nCorrect Choice is (B)."),

    ("What happens to the ethanol produced by yeast inside bread dough during the baking process in the oven?",
     ["It poisons the bread", "The ethanol completely evaporates due to the high oven baking temperature (around 200°C), leaving behind porous alcohol-free bread", "It turns into sugar", "It solidifies into salt"],
     "B", "OSC", "easy",
     "- Ethanol has a boiling point of 78.4°C and vaporizes completely during commercial baking.\nCorrect Choice is (B)."),

    ("Which complex carbohydrate in barley or wheat must be broken down into maltose and glucose before yeast can ferment it?",
     ["Cellulose", "Starch", "Keratin", "Lignin"],
     "B", "OSC", "medium",
     "- Diastase/amylase enzymes in germinating barley malt hydrolyze insoluble starch into fermentable maltose sugars for yeast.\nCorrect Choice is (B)."),

    ("What clean liquid biofuel is produced on a huge scale in India by fermenting sugarcane molasses with Saccharomyces cerevisiae?",
     ["Diesel", "Bio-ethanol (Ethyl alcohol)", "Kerosene", "Coal tar"],
     "B", "OSC", "easy",
     "- Fermentation of molasses yields bio-ethanol, which is blended with petrol (E20) as a cleaner automotive fuel.\nCorrect Choice is (B)."),

    ("Which enzyme complex present inside yeast cells is primarily responsible for converting glucose and fructose into ethanol and carbon dioxide?",
     ["Pepsin", "Zymase", "Lipase", "Trypsin"],
     "B", "OSC", "hard",
     "- Eduard Buchner discovered that a cell-free yeast extract called 'zymase' contains the glycolytic enzymes catalyzing alcohol fermentation.\nCorrect Choice is (B)."),

    ("The traditional Indian fermented foods 'Idli' and 'Dosa' become spongy and slightly sour through the combined action of:",
     ["Viruses only", "Lactobacilli and wild Yeasts fermenting the soaked rice and black gram batter", "Synthetic chemical acids", "Freezing in refrigerators"],
     "B", "OSC", "easy",
     "- Natural fermentation of idli/dosa batter by Leuconostoc/Lactobacillus and yeasts produces lactic acid and \\(\\text{CO}_2\\) bubbles.\nCorrect Choice is (B)."),

    ("Which yeast species (such as Yarrowia lipolytica) is utilized in bioremediation to clean up marine oil spills?",
     ["Saccharomyces cerevisiae", "Lipolytic yeast capable of breaking down and metabolizing crude petroleum hydrocarbons", "Mushroom", "Lactobacillus"],
     "B", "OSC", "hard",
     "- Certain yeasts and bacteria produce lipases and biosurfactants that degrade hydrocarbon pollutants into harmless water and \\(\\text{CO}_2\\).\nCorrect Choice is (B)."),

    # 31-40: Synthesis & Comparative Biology
    ("Which of the following useful microbes is a fungus, while the other two are bacteria?",
     ["Lactobacillus", "Rhizobium", "Yeast", "Azotobacter"],
     "C", "OSC", "easy",
     "- Yeast is a eukaryotic unicellular fungus; Lactobacillus and Rhizobium are prokaryotic bacteria.\nCorrect Choice is (C)."),

    ("Assertion (A): Yeast is an essential ingredient in the commercial bakery and brewing industries.\nReason (R): Yeast carries out anaerobic respiration yielding carbon dioxide for bread leavening and ethanol for alcoholic beverages.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Both commercial applications exploit the dual products of yeast fermentation: \\(\\text{CO}_2\\) (leavening) and ethanol (brewing).\nCorrect Choice is (A)."),

    ("Assertion (A): Adding a small teaspoon of fresh curd (starter/inoculum) to lukewarm milk accelerates curd formation.\nReason (R): The starter culture inoculates millions of live, active Lactobacilli cells that rapidly multiply and ferment milk lactose.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- The starter inoculum provides active Lactobacilli cells that thrive in lukewarm temperatures (35-40°C), converting lactose to lactic acid.\nCorrect Choice is (A)."),

    ("Why does milk NOT turn into curd if the starter is added to boiling hot milk (above 80°C)?",
     ["Because hot milk is too sweet", "Because extreme heat denatures proteins and kills the live Lactobacilli bacteria immediately", "Because hot milk repels bacteria", "Because lactic acid boils away"],
     "B", "OSC", "easy",
     "- Temperatures above 60-70°C pasteurize and kill vegetative Lactobacilli, halting biological fermentation.\nCorrect Choice is (B)."),

    ("Identify the odd one out with respect to cellular architecture: Lactobacillus, Rhizobium, Azotobacter, Saccharomyces.",
     ["Lactobacillus", "Rhizobium", "Azotobacter", "Saccharomyces (Yeast)"],
     "D", "OSC", "medium",
     "- Saccharomyces is a eukaryotic organism with a true nucleus and membrane-bound organelles; the other three are prokaryotic bacteria.\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to primary economic product: Curd, Yogurt, Buttermilk, Bread.",
     ["Curd", "Yogurt", "Buttermilk", "Bread"],
     "D", "OSC", "easy",
     "- Bread is a baked grain product made using Yeast; Curd, Yogurt, and Buttermilk are dairy products fermented by Lactobacilli.\nCorrect Choice is (D)."),

    ("What industrial waste byproduct from sugarcane refining serves as the primary sugary raw material for commercial bio-ethanol fermentation?",
     ["Bagasse ash", "Molasses", "Filter cake", "Dry husks"],
     "B", "OSC", "easy",
     "- Molasses is the dense, sugar-rich dark syrup remaining after commercial sucrose crystallization, ideal for yeast fermentation.\nCorrect Choice is (B)."),

    ("State whether True or False: Probiotic bacteria in yogurt destroy the normal healthy bacterial flora of the human intestines.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Probiotics reinforce and restore healthy gut flora, suppressing pathogenic putrefactive bacteria.\nCorrect Choice is (B)."),

    ("Which gas is collected and measured as an indicator of active fermentation rate in a laboratory yeast-glucose fermentation apparatus?",
     ["Oxygen (\\(\\text{O}_2\\))", "Carbon dioxide (\\(\\text{CO}_2\\))", "Nitrogen (\\(\\text{N}_2\\))", "Hydrogen (\\(\\text{H}_2\\))"],
     "B", "OSC", "easy",
     "- The volume of \\(\\text{CO}_2\\) gas bubbles evolved reflects the rate of glycolytic fermentation by yeast.\nCorrect Choice is (B)."),

    ("Which vitamin is synthesized in significant quantities by beneficial probiotic Lactobacilli residing in the human digestive tract?",
     ["Vitamin C", "B-complex vitamins (such as Vitamin B₁₂) and Vitamin K", "Vitamin D only", "Vitamin A only"],
     "B", "OSC", "medium",
     "- Symbiotic intestinal bacteria synthesize essential B-group vitamins and vitamin K, contributing to host nutrition.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Dairy & Microbial Applications
    ("If you examine a drop of diluted fresh buttermilk under a compound microscope at 400x magnification, what will you observe?",
     ["Large swimming amoebae", "Numerous tiny, non-motile rod-shaped microorganisms (Lactobacilli)", "Green spiral chloroplast ribbons", "Branching fungal mycelium with black spores"],
     "B", "OSC", "easy",
     "- A buttermilk smear reveals abundant microscopic, rod-shaped Lactobacilli bacteria.\nCorrect Choice is (B)."),

    ("Why is yogurt considered easier to digest than raw milk for many adults with mild lactose intolerance?",
     ["Yogurt has zero water", "Lactobacilli have already broken down and fermented a substantial fraction of the milk lactose into lactic acid", "Yogurt has no proteins", "Yogurt turns into bread"],
     "B", "OSC", "easy",
     "- Bacterial lactase in yogurt hydrolyzes milk lactose, relieving symptoms of lactose malabsorption.\nCorrect Choice is (B)."),

    ("What is the optimal incubation temperature range for cultivating Lactobacilli to make good curd overnight?",
     ["0°C to 5°C (freezing refrigerator)", "35°C to 40°C (lukewarm ambient warmth)", "70°C to 100°C (boiling point)", "Sub-zero temperatures"],
     "B", "OSC", "easy",
     "- The enzymatic machinery of mesophilic Lactobacilli exhibits maximal growth between 35°C and 40°C.\nCorrect Choice is (B)."),

    ("Which of the following organic acids is produced commercially on a large scale by microbial fermentation for use in food preservatives and pharmaceuticals?",
     ["Sulfuric acid", "Lactic acid", "Nitric acid", "Hydrochloric acid"],
     "B", "OSC", "easy",
     "- Industrial fermentation of corn starch or whey by Lactobacilli yields high-purity lactic acid.\nCorrect Choice is (B)."),

    ("In cheese manufacturing, why are specific microbial cultures added to coagulated milk curds?",
     ["To make the cheese sweet", "To ripen the curd, developing distinct texture, holes (propionic acid \\(\\text{CO}_2\\)), and characteristic gourmet aromas", "To turn cheese green", "To remove all proteins"],
     "B", "OSC", "medium",
     "- Ripening bacteria and molds break down fats and proteins into flavorful esters, peptides, and fatty acids.\nCorrect Choice is (B)."),

    ("State whether True or False: Lactobacilli require sterile oxygen tanks to survive and multiply.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Lactobacilli are aerotolerant anaerobes that thrive in oxygen-poor or anaerobic environments without aeration.\nCorrect Choice is (B)."),

    ("What type of organism is Rhizobium based on its nutritional and cellular classification?",
     ["Prokaryotic Gram-negative nitrogen-fixing bacterium", "Eukaryotic green alga", "Parasitic worm", "Spore-producing moss"],
     "A", "OSC", "medium",
     "- Rhizobium is a Gram-negative, rod-shaped diazotrophic prokaryote.\nCorrect Choice is (A)."),

    ("What is the primary role of the nodule cortex and endodermis in legume root nodules?",
     ["To attract ants", "To provide structural containment, vascular connection to the host plant, and maintain a low oxygen diffusion barrier", "To store sunlight", "To freeze water"],
     "B", "OSC", "hard",
     "- The nodule cortex regulates oxygen diffusion, maintaining the internal hypoxia required by nitrogenase.\nCorrect Choice is (B)."),

    ("Why do plants grown in nitrogen-deficient soil show yellowing of leaves (chlorosis)?",
     ["Because nitrogen is yellow", "Because nitrogen is a fundamental structural component of chlorophyll and proteins; nitrogen deficiency impairs chlorophyll synthesis", "Because nitrogen kills roots", "Because sun turns them yellow"],
     "B", "OSC", "easy",
     "- Nitrogen is an integral element of the porphyrin ring of chlorophyll; deficiency stalls pigment synthesis, causing chlorosis.\nCorrect Choice is (B)."),

    ("What mutual benefit does a chickpea plant provide to its resident Rhizobium bacteria?",
     ["Toxic chemicals", "Sucrose and organic malate synthesized in leaves via photosynthesis, along with a secure ecological niche", "Sunlight inside roots", "Cold water"],
     "B", "OSC", "easy",
     "- The legume plant supplies photosynthetic carbon (dicarboxylic acids and sugars) to fuel bacteroid metabolism.\nCorrect Choice is (B)."),

    # 51-60: Yeast Biochemistry & Fermentation
    ("When dried baker's yeast powder is stored on a dry supermarket shelf for months, the yeast cells remain:",
     ["Completely dead", "Dormant (in a state of suspended animation) until rehydrated with warm water and sugar", "Turned into stones", "Multiplying actively without food"],
     "B", "OSC", "easy",
     "- Anhydrobiotic dried yeast cells are viable but metabolically dormant until rehydrated in warm aqueous sugar solution.\nCorrect Choice is (B)."),

    ("What is the primary function of adding sugar to warm water when preparing yeast for bread making?",
     ["To make the water sticky", "To provide an immediate fermentable carbohydrate substrate that yeast can metabolize to generate energy and \\(\\text{CO}_2\\)", "To change the yeast color", "To kill bacteria"],
     "B", "OSC", "easy",
     "- Glucose and sucrose act as immediate fuel for glycolysis, rapidly kicking off fermentation and gas evolution.\nCorrect Choice is (B)."),

    ("Which carbohydrate polymer in wheat flour provides the elasticity and tensile strength that traps \\(\\text{CO}_2\\) bubbles in bread dough?",
     ["Cellulose", "Gluten (protein complex of gliadin and glutenin)", "Pectin", "Chitin"],
     "B", "OSC", "medium",
     "- Gluten forms an elastic proteinaceous network that stretches and traps expanding \\(\\text{CO}_2\\) gas bubbles.\nCorrect Choice is (B)."),

    ("Why does bread collapse into a flat, dense, rubbery slab if baked with inactive or dead yeast?",
     ["Because flour shrinks", "Because zero \\(\\text{CO}_2\\) gas is produced to aerate and leaven the dough, leaving no soft porous air pockets", "Because salt absorbs water", "Because gluten melts"],
     "B", "OSC", "easy",
     "- Without active microbial \\(\\text{CO}_2\\) generation, the dough remains dense, flat, and unleavened.\nCorrect Choice is (B)."),

    ("How does blending bio-ethanol with commercial petrol benefit the environment?",
     ["It makes cars completely silent", "Bio-ethanol is renewable and oxygenated, resulting in more complete fuel combustion and substantially lower carbon monoxide emissions", "It eliminates road traffic", "It cools engine oil"],
     "B", "OSC", "medium",
     "- Bio-ethanol is a renewable oxygenate that reduces fossil carbon emissions and urban particulate smog.\nCorrect Choice is (B)."),

    ("What type of respiration occurs inside an airtight industrial fermentation vat filled with molasses and yeast?",
     ["Aerobic respiration", "Anaerobic alcoholic fermentation", "Combustion", "Photophosphorylation"],
     "B", "OSC", "easy",
     "- Sealed vats exclude atmospheric oxygen, directing yeast metabolism strictly into anaerobic alcohol fermentation.\nCorrect Choice is (B)."),

    ("Why can yeast NOT continue alcohol fermentation indefinitely in a sugary vat until 100% pure alcohol is formed?",
     ["Because yeast runs out of cells", "Because high ethanol concentrations (above 12-15%) are toxic and kill the yeast cells themselves", "Because alcohol evaporates into rock", "Because water runs out"],
     "B", "OSC", "hard",
     "- Ethanol disrupts cell membrane integrity; concentrations exceeding ~14% become lethal to yeast, halting fermentation naturally.\nCorrect Choice is (B)."),

    ("How is high-concentration fuel-grade ethanol (99.5% anhydrous bio-ethanol) obtained from the fermented wash (which contains only 8-10% alcohol)?",
     ["By freezing it", "By fractional distillation followed by molecular sieve dehydration to remove water", "By passing through paper filters", "By adding salt"],
     "B", "OSC", "medium",
     "- Fractional distillation exploits the boiling point disparity (78.4°C vs 100°C), concentrating ethanol for fuel blending.\nCorrect Choice is (B)."),

    ("State whether True or False: Brewer's yeast and Baker's yeast are different strains of the exact same biological species, Saccharomyces cerevisiae.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Both belong to Saccharomyces cerevisiae, selected for different phenotypic fermentation traits (high gas vs high alcohol tolerance).\nCorrect Choice is (A)."),

    ("Which microbial product is responsible for the refreshing fizz and effervescence in naturally fermented sparkling beverages?",
     ["Methane gas", "Dissolved carbon dioxide (\\(\\text{CO}_2\\)) gas produced by yeast fermentation under pressure", "Oxygen gas", "Hydrogen sulfide"],
     "B", "OSC", "easy",
     "- Trapped \\(\\text{CO}_2\\) dissolves under bottle pressure, forming carbonic acid that effervesces when uncorked.\nCorrect Choice is (B)."),

    # 61-70: Practical Diagnostic Scenarios
    ("A student observes a mother making curd at home. She warms milk until it is comfortably lukewarm, adds a spoonful of buttermilk, covers the bowl, and leaves it in a warm corner for 8 hours. What biological process has occurred?",
     ["Evaporation of milk", "Lactic acid fermentation by Lactobacilli transforming liquid milk into set curd", "Rusting of milk", "Freezing of proteins"],
     "B", "OSC", "easy",
     "- Lukewarm incubation enables inoculated Lactobacilli to ferment lactose into lactic acid, setting the milk casein into curd.\nCorrect Choice is (B)."),

    ("If curd is left outside on a hot summer afternoon for 24 hours, it tastes extremely sour and sharp. Why?",
     ["Because flies touch it", "Because warm temperatures accelerate bacterial fermentation, causing Lactobacilli to produce excess lactic acid that sharply lowers pH", "Because water turns into lemon juice", "Because milk fat turns into vinegar"],
     "B", "OSC", "easy",
     "- Continuous microbial fermentation in high ambient heat over-produces lactic acid, driving pH down to ~3.8.\nCorrect Choice is (B)."),

    ("Why are pulses (dal) such an indispensable staple in vegetarian diets for protein nutrition?",
     ["Pulses contain zero calories", "Thanks to symbiotic Rhizobium nitrogen fixation, legumes synthesize and store abundant protein in their seeds (20-25% protein content)", "Pulses are made of meat", "Pulses absorb protein from rain"],
     "B", "OSC", "easy",
     "- High nitrogen availability from Rhizobium enables legumes to synthesize dense amino acid and protein reserves in seeds.\nCorrect Choice is (B)."),

    ("What is the primary visual difference between a healthy nitrogen-fixing root nodule and an ineffective/dead nodule?",
     ["Healthy nodules are pink/red inside due to leghemoglobin; dead or ineffective nodules are pale white, green, or brown", "Healthy nodules are black; dead ones are yellow", "Healthy nodules have leaves", "Dead nodules turn into stones"],
     "A", "OSC", "medium",
     "- Active nitrogen fixation correlates with the presence of functional pink leghemoglobin; senescent nodules lose pigment.\nCorrect Choice is (A)."),

    ("In an experiment, yeast is mixed with lukewarm sugar water in a conical flask, and an uninflated balloon is stretched over the flask mouth. After 30 minutes, what happens to the balloon?",
     ["It shrinks into the flask", "The balloon inflates with carbon dioxide (\\(\\text{CO}_2\\)) gas evolved during yeast fermentation", "The balloon catches fire", "Nothing happens"],
     "B", "OSC", "easy",
     "- Active fermentation generates gaseous \\(\\text{CO}_2\\) which rises and inflates the sealed balloon.\nCorrect Choice is (B)."),

    ("If the sugar in the previous experiment is replaced with pure table salt (sodium chloride), will the balloon inflate?",
     ["Yes, faster", "No, because yeast cells cannot ferment salt, and high salinity dehydrates and inhibits yeast metabolism", "Yes, with chlorine gas", "Yes, with oxygen"],
     "B", "OSC", "easy",
     "- Salt is not a fermentable carbohydrate and high osmolarity induces plasmolysis in yeast cells.\nCorrect Choice is (B)."),

    ("Fill in the blank: The scientific study of microscopic fungi like yeasts and molds is called _______.",
     ["Mycology", "Bacteriology", "Virology", "Entomology"],
     "A", "OFB", "easy",
     "- Mycology is the specialized branch of biological science dealing with fungi.\nCorrect Choice is (A)."),

    ("Which property of Lactobacilli makes them essential for preserving fermented pickles and sauerkraut without artificial chemical additives?",
     ["They make pickles sweet", "The lactic acid they produce lowers pH below 4.0, an acidic environment where food spoilage bacteria cannot survive", "They absorb all salt", "They produce thick ice"],
     "B", "OSC", "medium",
     "- Natural lactic acidification inhibits pathogenic and putrefactive food spoilage microorganisms.\nCorrect Choice is (B)."),

    ("Which organelle is present in Yeast cells but completely absent in Lactobacillus cells?",
     ["Cell membrane", "Membrane-bound Nucleus and Mitochondria", "Ribosomes", "Cell wall"],
     "B", "OSC", "hard",
     "- Yeast is a eukaryote with a membrane-bound nucleus and mitochondria; Lactobacillus is an anucleate prokaryote.\nCorrect Choice is (B)."),

    ("What is 'Single Cell Protein' (SCP)?",
     ["A protein made of only one atom", "Dried microbial cell biomass (such as yeast, spirulina, or fungi) cultivated as a protein-rich food supplement for humans or animals", "A single egg", "A synthetic pill made of stone"],
     "B", "OSC", "medium",
     "- SCP refers to refined protein biomass harvested from micro-organisms cultured on agro-industrial wastes.\nCorrect Choice is (B).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Lactobacilli under Microscope & Casein Curdling
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Lactobacilli: Milk to Curd Transition</text>
  <!-- Microscopic View Circle -->
  <circle cx="85" cy="110" r="45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Rod-shaped bacteria -->
  <rect x="65" y="90" width="18" height="6" rx="3" fill="#c084fc"/>
  <rect x="75" y="110" width="16" height="6" rx="3" fill="#c084fc"/>
  <rect x="95" y="100" width="20" height="6" rx="3" fill="#c084fc"/>
  <rect x="60" y="125" width="16" height="6" rx="3" fill="#c084fc"/>
  <rect x="85" y="125" width="18" height="6" rx="3" fill="#c084fc"/>
  <text x="50" y="170" fill="#c084fc" font-size="8.5" font-weight="bold">Rod-shaped Bacilli</text>
  <!-- Arrow -->
  <line x1="140" y1="110" x2="180" y2="110" stroke="#fde047" stroke-width="3" marker-end="url(#arrow)"/>
  <!-- Chemical Reaction Box -->
  <rect x="185" y="45" width="160" height="135" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="195" y="65" fill="#34d399" font-size="10" font-weight="bold">Biochemical Mechanism:</text>
  <text x="195" y="85" fill="#cbd5e1" font-size="8.5">- Milk Sugar: Lactose</text>
  <text x="195" y="100" fill="#fde047" font-size="8.5">➔ Fermented to LACTIC ACID</text>
  <text x="195" y="118" fill="#f87171" font-size="8.5">- pH drops below 4.6</text>
  <text x="195" y="135" fill="#34d399" font-size="8.5">- Casein protein coagulates</text>
  <text x="195" y="152" fill="#38bdf8" font-size="8.5">Liquid milk ➔ Firm Curd</text>
  <text x="45" y="200" fill="#fde047" font-size="9.5">Coagulation of casein at acidic pH solidifies the dairy matrix</text>
</svg>
</div>
In the diagram above illustrating milk curdling, what specific milk protein denatures and coagulates when Lactobacilli lower the pH?""",
     ["Keratin", "Casein", "Gluten", "Hemoglobin"],
     "B", "OSC", "easy",
     "- Casein is the predominant milk protein that precipitates and forms curd when lactic acid reduces pH to its isoelectric point (~4.6).\nCorrect Choice is (B)."),

    # 72: Rhizobium Nodule Zone & Nitrogen Fixation
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Root Nodule Symbiosis: Legume & Rhizobium</text>
  <!-- Legume Root -->
  <line x1="80" y1="45" x2="80" y2="180" stroke="#ca8a04" stroke-width="4"/>
  <line x1="80" y1="80" x2="135" y2="100" stroke="#ca8a04" stroke-width="2"/>
  <line x1="80" y1="125" x2="145" y2="140" stroke="#ca8a04" stroke-width="2"/>
  <!-- Pink Nodules -->
  <ellipse cx="125" cy="98" rx="14" ry="10" fill="#fb7185" stroke="#e11d48" stroke-width="2"/>
  <ellipse cx="140" cy="138" rx="14" ry="10" fill="#fb7185" stroke="#e11d48" stroke-width="2"/>
  <text x="40" y="115" fill="#fb7185" font-size="9" font-weight="bold">Root Nodule</text>
  <!-- Exchange Box -->
  <rect x="175" y="45" width="170" height="135" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="185" y="65" fill="#38bdf8" font-size="10" font-weight="bold">Mutualistic Exchange:</text>
  <text x="185" y="85" fill="#34d399" font-size="8.5">Plant gives Rhizobium:</text>
  <text x="185" y="98" fill="#cbd5e1" font-size="8">- Carbohydrates (food)</text>
  <text x="185" y="110" fill="#cbd5e1" font-size="8">- Protected nodule home</text>
  <text x="185" y="128" fill="#fde047" font-size="8.5">Rhizobium gives Plant:</text>
  <text x="185" y="142" fill="#fde047" font-size="8.5">- Fixed nitrates (NH₃/NO₃⁻)</text>
  <text x="185" y="156" fill="#cbd5e1" font-size="8">- Enriched soil fertility</text>
  <text x="45" y="202" fill="#fde047" font-size="9.5">Natural biological nitrogen factory replacing synthetic fertilizers</text>
</svg>
</div>
What mutual biological exchange occurs inside the pink root nodule illustrated in the diagram?""",
     ["Plant provides nitrogen gas; bacterium provides water",
      "Plant provides photosynthetic sugars and shelter; Rhizobium converts atmospheric N₂ into assimilable nitrates for the plant",
      "Plant kills the bacterium for vitamins",
      "Bacterium consumes all root tissues, killing the plant"],
     "B", "OSC", "easy",
     "- In mutualism, the legume supplies carbon nutrients and an anaerobic niche, while Rhizobium provides fixed nitrogen compounds.\nCorrect Choice is (B)."),

    # 73: Yeast Budding Reproduction Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Yeast Asexual Reproduction: Budding</text>
  <!-- Parent Cell -->
  <ellipse cx="110" cy="110" rx="36" ry="42" fill="#1e293b" stroke="#facc15" stroke-width="2.5"/>
  <circle cx="110" cy="110" r="10" fill="#f87171"/>
  <text x="105" y="114" fill="#ffffff" font-size="8" font-weight="bold">N</text>
  <text x="80" y="165" fill="#facc15" font-size="9" font-weight="bold">Parent Yeast</text>
  <!-- Emerging Daughter Bud -->
  <ellipse cx="160" cy="80" rx="18" ry="22" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <circle cx="160" cy="80" r="6" fill="#f87171"/>
  <text x="156" y="83" fill="#ffffff" font-size="7" font-weight="bold">n</text>
  <text x="155" y="55" fill="#fde047" font-size="9" font-weight="bold">Daughter Bud</text>
  <!-- Constriction Line -->
  <path d="M 135,90 Q 140,95 142,88" stroke="#fde047" stroke-width="2" fill="none"/>
  <!-- Chain of Buds -->
  <ellipse cx="195" cy="65" rx="12" ry="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="215" y="70" fill="#38bdf8" font-size="8">Chain formation</text>
  <text x="45" y="195" fill="#34d399" font-size="9.5">Unicellular eukaryotic fungus multiplying via mitotic budding</text>
</svg>
</div>
What type of asexual reproduction is depicted above in the yeast cell (Saccharomyces cerevisiae)?""",
     ["Binary fission", "Budding (formation of daughter buds)", "Spore formation in ferns", "Regeneration"],
     "B", "OSC", "easy",
     "- Yeast reproduces asexually by budding, producing daughter protrusions that detach or form short pseudohyphal chains.\nCorrect Choice is (B)."),

    # 74: Bread Dough Leavening Mechanism
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">How Yeast Leavens Bread Dough</text>
  <!-- Raw Dough -->
  <path d="M 40,140 Q 80,105 120,140 Z" fill="#d97706" stroke="#b45309" stroke-width="2"/>
  <text x="50" y="160" fill="#cbd5e1" font-size="8.5">Kneaded Dough</text>
  <text x="135" y="125" fill="#fde047" font-size="16">➔</text>
  <!-- Risen Spongy Dough -->
  <path d="M 160,140 Q 220,60 280,140 Z" fill="#d97706" stroke="#b45309" stroke-width="2"/>
  <!-- Trapped CO2 bubbles inside -->
  <circle cx="190" cy="115" r="7" fill="#ffffff" opacity="0.8"/>
  <circle cx="220" cy="95" r="9" fill="#ffffff" opacity="0.8"/>
  <circle cx="250" cy="115" r="8" fill="#ffffff" opacity="0.8"/>
  <circle cx="225" cy="125" r="6" fill="#ffffff" opacity="0.8"/>
  <text x="210" y="100" fill="#0f172a" font-size="8" font-weight="bold">CO₂</text>
  <text x="180" y="160" fill="#fde047" font-size="8.5" font-weight="bold">Risen Spongy Dough (Doubled)</text>
  <text x="45" y="185" fill="#38bdf8" font-size="9">C₆H₁₂O₆ ➔ 2C₂H₅OH + 2CO₂↑ (Zymase fermentation)</text>
  <text x="45" y="198" fill="#cbd5e1" font-size="8">Ethanol evaporates during baking; trapped CO₂ leaves soft cavities</text>
</svg>
</div>
What causes the dough to swell and develop soft, spongy porous pockets as shown in the diagram?""",
     ["Oxygen gas produced by plant roots",
      "Carbon dioxide (\\(\\text{CO}_2\\)) gas bubbles produced during yeast fermentation trapped in elastic wheat gluten",
      "Nitrogen gas from lightning",
      "Water turning into steam at room temperature"],
     "B", "OSC", "easy",
     "- \\(\\text{CO}_2\\) gas bubbles generated by anaerobic yeast fermentation become trapped inside gluten, creating a soft porous crumb.\nCorrect Choice is (B)."),

    # 75: Bio-ethanol Fuel Production Flowsheet
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Industrial Bio-Ethanol Flowsheet</text>
  <!-- Step 1: Molasses -->
  <rect x="25" y="50" width="75" height="40" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="32" y="68" fill="#fbbf24" font-size="8.5" font-weight="bold">Sugarcane</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="7.5">Molasses</text>
  <text x="105" y="75" fill="#fde047" font-size="12">➔</text>
  <!-- Step 2: Fermenter Vat -->
  <rect x="120" y="50" width="85" height="40" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="128" y="68" fill="#34d399" font-size="8.5" font-weight="bold">Yeast Vat</text>
  <text x="128" y="80" fill="#cbd5e1" font-size="7.5">Fermentation</text>
  <text x="210" y="75" fill="#fde047" font-size="12">➔</text>
  <!-- Step 3: Distillation Tower -->
  <rect x="225" y="50" width="85" height="40" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="235" y="68" fill="#38bdf8" font-size="8.5" font-weight="bold">Distillation</text>
  <text x="235" y="80" fill="#cbd5e1" font-size="7.5">Concentration</text>
  <!-- Final Fuel Output -->
  <rect x="55" y="115" width="230" height="45" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="65" y="135" fill="#fb7185" font-size="9.5" font-weight="bold">99.5% Anhydrous Bio-Ethanol (C₂H₅OH)</text>
  <text x="65" y="150" fill="#cbd5e1" font-size="8.5">- Blended with Petrol (E20) for green transport</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Renewable energy source reducing fossil carbon footprint</text>
</svg>
</div>
What agricultural byproduct from sugar mills is fermented by yeast to manufacture commercial bio-ethanol in India?""",
     ["Sugarcane Molasses", "Paddy straw", "Cotton lint", "Mustard seeds"],
     "A", "OSC", "easy",
     "- Sugarcane molasses is rich in fermentable sucrose and invert sugars, providing the primary feedstock for ethanol distilleries.\nCorrect Choice is (A)."),

    # 76: Probiotic Gut Action in Intestines
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Probiotic Defense in Human Gut</text>
  <!-- Intestinal Epithelial Wall -->
  <rect x="25" y="130" width="290" height="25" fill="#475569" rx="3"/>
  <text x="110" y="147" fill="#cbd5e1" font-size="9" font-weight="bold">Intestinal Epithelial Lining</text>
  <!-- Beneficial Probiotics (Lactobacilli) in Green -->
  <rect x="45" y="105" width="22" height="7" rx="3" fill="#22c55e"/>
  <rect x="85" y="100" width="22" height="7" rx="3" fill="#22c55e"/>
  <rect x="135" y="105" width="22" height="7" rx="3" fill="#22c55e"/>
  <rect x="185" y="100" width="22" height="7" rx="3" fill="#22c55e"/>
  <rect x="245" y="105" width="22" height="7" rx="3" fill="#22c55e"/>
  <text x="35" y="80" fill="#4ade80" font-size="8.5" font-weight="bold">✓ Probiotics (Lactobacilli)</text>
  <text x="35" y="92" fill="#cbd5e1" font-size="7.5">Forms protective protective biofilm</text>
  <!-- Harmful Pathogen Blocked -->
  <circle cx="270" cy="75" r="9" fill="#ef4444"/>
  <text x="210" y="60" fill="#f87171" font-size="8.5" font-weight="bold">✗ Pathogens (Clostridium)</text>
  <text x="210" y="72" fill="#fca5a5" font-size="7.5">Blocked from colonizing</text>
  <text x="45" y="185" fill="#fde047" font-size="9.5">Probiotics competitive exclusion maintains gut immunity and digestion</text>
</svg>
</div>
How do probiotic Lactobacilli protect the human digestive tract from intestinal infections?""",
     ["By digesting intestinal bones",
      "By forming a protective bacterial barrier on gut walls and outcompeting putrefactive pathogens like Clostridium",
      "By cooling body temperature to 0°C",
      "By neutralizing stomach acid completely"],
     "B", "OSC", "easy",
     "- Probiotics practice competitive exclusion, acidifying the lumen and preventing pathogenic microbes from adhering to intestinal villi.\nCorrect Choice is (B)."),

    # 77: Summary Comparison: Lactobacilli vs Rhizobium vs Yeast
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Comparison: The Three Beneficial Microbes</text>
  <!-- Headers -->
  <text x="25" y="45" fill="#94a3b8" font-size="9" font-weight="bold">MICROBE</text>
  <text x="120" y="45" fill="#34d399" font-size="9" font-weight="bold">TYPE</text>
  <text x="200" y="45" fill="#facc15" font-size="9" font-weight="bold">KEY FUNCTION</text>
  <line x1="20" y1="52" x2="350" y2="52" stroke="#475569" stroke-width="1.5"/>
  <!-- Row 1: Lactobacillus -->
  <text x="25" y="75" fill="#cbd5e1" font-size="9" font-weight="bold">Lactobacillus</text>
  <text x="120" y="75" fill="#fde047" font-size="8.5">Bacterium (G+)</text>
  <text x="200" y="75" fill="#cbd5e1" font-size="8.5">Milk ➔ Curd, Probiotics</text>
  <!-- Row 2: Rhizobium -->
  <text x="25" y="110" fill="#cbd5e1" font-size="9" font-weight="bold">Rhizobium</text>
  <text x="120" y="110" fill="#fde047" font-size="8.5">Bacterium (G-)</text>
  <text x="200" y="110" fill="#cbd5e1" font-size="8.5">Root Nodule N₂ Fixation</text>
  <!-- Row 3: Yeast -->
  <text x="25" y="145" fill="#cbd5e1" font-size="9" font-weight="bold">Yeast</text>
  <text x="120" y="145" fill="#38bdf8" font-size="8.5">Fungus (Eukaryote)</text>
  <text x="200" y="145" fill="#cbd5e1" font-size="8.5">Bread leavening & Bio-ethanol</text>
  <line x1="20" y1="165" x2="350" y2="165" stroke="#475569" stroke-width="1.5"/>
  <text x="45" y="190" fill="#fde047" font-size="9.5">Biological pillars of dairy, agricultural, and industrial biotechnology</text>
</svg>
</div>
Which of the beneficial microbes listed in the master matrix is a single-celled Eukaryote, while the other two are prokaryotes?""",
     ["Lactobacillus", "Rhizobium", "Yeast (Saccharomyces cerevisiae)", "All three are eukaryotes"],
     "C", "OSC", "easy",
     "- Yeast is a eukaryotic fungus with a true membrane-bound nucleus; Lactobacilli and Rhizobia are prokaryotic eubacteria.\nCorrect Choice is (C)."),

    # 78: Inoculation of Seeds with Rhizobium
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Rhizobial Inoculation of Legume Seeds</text>
  <!-- Seed -->
  <ellipse cx="85" cy="100" rx="30" ry="22" fill="#d97706" stroke="#b45309" stroke-width="2"/>
  <text x="70" y="105" fill="#ffffff" font-size="9" font-weight="bold">Seed</text>
  <!-- Bacterial Coating -->
  <path d="M 50,100 C 50,70 120,70 120,100 C 120,130 50,130 50,100 Z" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,2"/>
  <text x="35" y="60" fill="#4ade80" font-size="8.5" font-weight="bold">Rhizobium bacterial coating</text>
  <!-- Benefits Box -->
  <rect x="150" y="50" width="165" height="110" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="160" y="70" fill="#34d399" font-size="9.5" font-weight="bold">Agricultural Benefits:</text>
  <text x="160" y="88" fill="#cbd5e1" font-size="8.5">- Rapid early nodulation</text>
  <text x="160" y="102" fill="#cbd5e1" font-size="8.5">- Robust seedling vigor</text>
  <text x="160" y="118" fill="#fde047" font-size="8.5">- 25-30% higher crop yield</text>
  <text x="160" y="134" fill="#38bdf8" font-size="8.5">- Zero chemical pollution</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Eco-friendly biofertilizer technology sustainable for soil health</text>
</svg>
</div>
Why are legume seeds routinely treated with a slurry of Rhizobium inoculant prior to planting?""",
     ["To color the seeds green",
      "To ensure that emerging seedling roots are immediately colonized by high-efficiency nitrogen-fixing bacteria",
      "To prevent seeds from absorbing water",
      "To turn the plants into wheat"],
     "B", "OSC", "easy",
     "- Seed inoculation guarantees that vigorous nitrogen-fixing bacterial strains colonize the rhizosphere immediately upon germination.\nCorrect Choice is (B)."),

    # 79: Gram Staining of Lactobacilli
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Gram Staining of Lactobacilli</text>
  <!-- Microscope field -->
  <circle cx="85" cy="110" r="45" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
  <!-- Purple Rods -->
  <rect x="60" y="95" width="22" height="6" rx="3" fill="#a855f7"/>
  <rect x="80" y="115" width="20" height="6" rx="3" fill="#a855f7"/>
  <rect x="95" y="90" width="18" height="6" rx="3" fill="#a855f7"/>
  <rect x="65" y="125" width="22" height="6" rx="3" fill="#a855f7"/>
  <text x="45" y="170" fill="#c084fc" font-size="9" font-weight="bold">Deep Violet / Purple Rods</text>
  <!-- Explanation Box -->
  <rect x="155" y="50" width="165" height="110" fill="#1e293b" stroke="#c084fc" rx="4"/>
  <text x="165" y="70" fill="#c084fc" font-size="9.5" font-weight="bold">Gram-Positive Cell Wall:</text>
  <text x="165" y="88" fill="#cbd5e1" font-size="8.5">- Thick Peptidoglycan mesh</text>
  <text x="165" y="104" fill="#cbd5e1" font-size="8.5">- Retains Crystal Violet-Iodine</text>
  <text x="165" y="120" fill="#fde047" font-size="8.5">- Resists alcohol wash</text>
  <text x="165" y="136" fill="#34d399" font-size="8.5">Definitive diagnostic proof</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Gram-positive rod morphology separates Lactobacilli from E. coli</text>
</svg>
</div>
What color do Lactobacilli retain under the standard microbiological Gram stain procedure, and why?""",
     ["Bright pink because they are Gram-negative",
      "Deep violet/purple because they are Gram-positive with a thick peptidoglycan cell wall",
      "Green because they contain chlorophyll",
      "Colorless because they have no wall"],
     "B", "OSC", "medium",
     "- Lactobacilli are Gram-positive bacteria whose thick peptidoglycan envelope traps crystal violet dye, staining dark violet/purple.\nCorrect Choice is (B)."),

    # 80: Laboratory Fermentation Setup (Evolution of CO2)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Laboratory Yeast Fermentation Setup</text>
  <!-- Conical Flask (Yeast + Sugar) -->
  <path d="M 70,80 L 50,150 L 110,150 L 90,80 Z" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="50" y="165" fill="#fde047" font-size="8">Yeast + Sugar</text>
  <!-- Delivery Tube -->
  <path d="M 80,80 L 80,55 L 220,55 L 220,130" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <!-- Test Tube (Lime water) -->
  <rect x="205" y="100" width="30" height="60" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="185" y="175" fill="#38bdf8" font-size="8">Lime Water Turns Milky</text>
  <!-- Reaction annotation -->
  <rect x="45" y="180" width="250" height="25" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="55" y="196" fill="#34d399" font-size="8.5">CO₂ gas bubbles through Ca(OH)₂ forming white CaCO₃</text>
</svg>
</div>
In the experimental setup above, why does the clear lime water (\\(\\text{Ca(OH)}_2\\)) in the test tube turn milky when connected to the active yeast-sugar flask?""",
     ["Because yeast cells fly through the tube",
      "Because carbon dioxide (\\(\\text{CO}_2\\)) gas evolved during fermentation reacts with lime water to precipitate insoluble white calcium carbonate (\\(\\text{CaCO}_3\\))",
      "Because alcohol turns lime water white",
      "Because oxygen bleaches the water"],
     "B", "OSC", "easy",
     "- \\(\\text{CO}_2\\) gas bubbles react with \\(\\text{Ca(OH)}_2\\) to form white precipitate: \\(\\text{Ca(OH)}_2 + \\text{CO}_2 \\to \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    # 81: Diverse Fermented Products Matrix
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Spectrum of Useful Fermented Products</text>
  <!-- Box 1: Dairy -->
  <rect x="25" y="50" width="135" height="55" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="70" fill="#38bdf8" font-size="9.5" font-weight="bold">Dairy Products:</text>
  <text x="35" y="86" fill="#cbd5e1" font-size="8.5">- Curd, Yogurt, Cheese, Kefir</text>
  <text x="35" y="98" fill="#fde047" font-size="7.5">Agent: Lactobacilli</text>
  <!-- Box 2: Bakery & Fuel -->
  <rect x="180" y="50" width="135" height="55" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="70" fill="#fbbf24" font-size="9.5" font-weight="bold">Bakery & Energy:</text>
  <text x="190" y="86" fill="#cbd5e1" font-size="8.5">- Bread, Buns, Bio-ethanol</text>
  <text x="190" y="98" fill="#fde047" font-size="7.5">Agent: Saccharomyces (Yeast)</text>
  <!-- Box 3: Agricultural Soil -->
  <rect x="25" y="115" width="290" height="50" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="135" fill="#34d399" font-size="9.5" font-weight="bold">Biofertilizer & Soil Nitrogen:</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8.5">- Enriches pulse crops; eliminates chemical runoff (Agent: Rhizobium)</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Microbes are indispensable partners of human civilization</text>
</svg>
</div>
Which microscopic organisms are responsible for the spongy softness of baker's bread and the natural curdling of dairy milk, respectively?""",
     ["Bacteria for bread; fungi for curd",
      "Yeast (a fungus) for bread; Lactobacilli (bacteria) for curd",
      "Viruses for both",
      "Algae for bread; protozoa for curd"],
     "B", "OSC", "easy",
     "- Yeast leavens bread via \\(\\text{CO}_2\\) evolution; Lactobacilli ferment milk lactose into lactic acid to set curd.\nCorrect Choice is (B)."),

    # 82: Summary Diagnostic of Beneficial Microbes
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Summary: Useful Microbes in Science</text>
  <!-- Lactobacilli -->
  <rect x="20" y="42" width="320" height="38" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="58" fill="#38bdf8" font-size="9.5" font-weight="bold">1. Lactobacilli (Bacteria):</text>
  <text x="30" y="72" fill="#cbd5e1" font-size="8.5">Ferments lactose to lactic acid; curdles casein; probiotic intestinal defense</text>
  <!-- Rhizobium -->
  <rect x="20" y="85" width="320" height="38" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="30" y="101" fill="#34d399" font-size="9.5" font-weight="bold">2. Rhizobium (Bacteria):</text>
  <text x="30" y="115" fill="#cbd5e1" font-size="8.5">Nodule symbiosis in legumes; fixes atmospheric N₂; protected by leghemoglobin</text>
  <!-- Yeast -->
  <rect x="20" y="128" width="320" height="42" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="30" y="144" fill="#fde047" font-size="9.5" font-weight="bold">3. Saccharomyces cerevisiae (Yeast, Fungus):</text>
  <text x="30" y="158" fill="#cbd5e1" font-size="8.5">Anaerobic alcoholic fermentation; leavens bread dough; generates bio-ethanol</text>
  <text x="45" y="195" fill="#34d399" font-size="9.5">Applied industrial microbiology driving food security and clean energy</text>
</svg>
</div>
According to the master summary, what overarching role do these three micro-organisms share in common?""",
     ["They are deadly human pathogens",
      "They are highly beneficial microbes applied industrially for food production, agriculture, and renewable bio-energy",
      "They can only live in freezing ice",
      "They destroy all soil fertility"],
     "B", "OSC", "easy",
     "- Lactobacilli, Rhizobia, and Yeasts are foundational industrial and ecological microbes that support agriculture, nutrition, and biotechnology.\nCorrect Choice is (B).")
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

out_file = "scripts/ch8_topic1.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
