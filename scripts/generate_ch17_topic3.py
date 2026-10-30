# -*- coding: utf-8 -*-
"""
Generate 82 canonical questions for MH-9-SCIT-17-17.3
Topic: Agri-tourism, Animal Husbandry & Sericulture
Vault: 40 Exam, 30 Practice, 12 Mock (with dark-theme SVGs)
"""

import json
import os

TOPIC_CODE = "MH-9-SCIT-17-17.3"

def make_q(qcode, topic_code, text, options, correct_key, qtype, difficulty, vault, exam_cat, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic_code,
        "text": text,
        "options": options,
        "correctAnswer": correct_key,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": exam_cat,
        "explanation": explanation,
        "requiresFigure": bool(vault == "mock" and "<svg" in text),
        "chapterNumber": 17,
        "class": "Class 9",
        "board": "MH",
        "subject": "Science and Technology",
        "bloomsTaxonomy": "Application" if difficulty == "hard" else ("Comprehension" if difficulty == "medium" else "Knowledge"),
        "usageCount": 0,
        "used": False
    }

exam_data = [
    # 1: Animal Husbandry definition
    ("What does the agricultural practice of animal husbandry encompass?",
     ["Scientific management, breeding, feeding, disease control, and rearing of livestock animals",
      "Only the hunting of wild animals in forests",
      "The slaughter of all farm animals",
      "Preserving wild animals in zoological parks"],
     "A", "OSC", "easy",
     "Animal husbandry is the agricultural branch concerned with the scientific care, breeding, nutrition, shelter, and health maintenance of domesticated animals such as cattle, sheep, and poultry to obtain economic products efficiently."),

    # 2: Cattle dual purposes
    ("Domesticated cattle in India are broadly classified into which two functional categories based on their agricultural utility?",
     ["Milch animals (dairy) and Draught animals (working/draft)",
      "Carnivorous breeds and Herbivorous breeds",
      "Aquatic breeds and Terrestrial breeds",
      "Flying breeds and Burrowing breeds"],
     "A", "OSC", "easy",
     "Farm cattle are classified into dairy or milch breeds (reared predominantly for milk yield) and draught animals (oxen and bullocks employed for tilling, ploughing, and cart transport)."),

    # 3: Indigenous Indian cow breeds
    ("Which of the following is a high-yielding indigenous (Desi) Indian dairy cattle breed?",
     ["Gir and Sahiwal", "Holstein-Friesian", "Jersey", "Brown Swiss"],
     "A", "OSC", "easy",
     "Gir (native to Gujarat) and Sahiwal (native to Punjab/Haryana) are celebrated indigenous Bos indicus breeds renowned for heat tolerance, disease resistance, and generous milk yield."),

    # 4: Exotic cattle breeds
    ("Which of the following cattle breeds is an exotic (foreign) breed known for producing exceptionally large daily milk volumes over long lactation periods?",
     ["Holstein-Friesian", "Deoni", "Khillari", "Dangi"],
     "A", "OSC", "easy",
     "Holstein-Friesian (originating in the Netherlands/Germany) is an exotic dairy breed characterized by black-and-white patches and an extraordinarily high lactation volume."),

    # 5: Draught cattle breeds of Maharashtra
    ("Which indigenous draught cattle breed from Maharashtra and Karnataka is famous for its tremendous endurance, agility, and speed in agricultural field ploughing?",
     ["Khillari", "Jersey", "Murrah", "White Leghorn"],
     "A", "OSC", "medium",
     "Khillari is a prized draught cattle breed indigenous to southern Maharashtra (Satara, Sangli, Solapur), known for its compact muscular frame, grey coat, backward-sweeping horns, and rapid draught performance."),

    # 6: Cross-breeding cattle objective
    ("Why are exotic cattle breeds (like Jersey or Brown Swiss) cross-bred with indigenous Indian breeds (like Gir or Sindhi)?",
     ["To combine the long lactation and high milk production of exotic breeds with the heat tolerance and disease resistance of Indian breeds",
      "To produce cows with colorful fur patterns for shows",
      "To eliminate the need for drinking water in farm sheds",
      "To produce hornless cattle that can fly"],
     "A", "OSC", "medium",
     "Cross-breeding leverages hybrid vigor (heterosis) by uniting the superior milk volume and extended lactation cycle of exotic cattle with the rugged tropical disease immunity and heat resilience of native Indian cattle."),

    # 7: Cattle feed components
    ("What are the two essential components of a balanced cattle diet?",
     ["Roughage (high fiber like green fodder, hay, silage) and Concentrates (high protein and energy like oil cakes, bran, and cereals)",
      "Pure sugar and cooking oil",
      "Wood chips and chemical fertilizers",
      "Fish flesh and poultry bones"],
     "A", "OSC", "easy",
     "Ruminant nutrition demands roughage (fibrous hay, grass, and silage to sustain rumen digestion and cud-chewing) paired with nutrient-dense concentrates (oilseed cakes, crushed pulses, and cereal bran to supply protein, energy, and minerals)."),

    # 8: Cattle shelter hygiene
    ("Which structural design feature is essential in a scientific cattle shed to maintain animal hygiene and prevent hoof infections?",
     ["A sloping concrete floor with drainage gutters and adequate cross-ventilation",
      "A completely sealed airtight room with no windows",
      "A deep mud pit filled with stagnant rainwater",
      "A carpeted wooden floor with central heating"],
     "A", "OSC", "easy",
     "A sloping floor allows urine and wash water to drain rapidly into external gutters, keeping the bedding dry and clean, which drastically reduces mastitis and hoof rot infections."),

    # 9: Cattle viral disease
    ("Which contagious viral disease causing fever and painful blisters on the tongue, mouth, and hooves affects cloven-hoofed farm livestock?",
     ["Foot and Mouth Disease (FMD)", "Ranikhet disease", "Anthrax", "Ascariasis"],
     "A", "OSC", "medium",
     "Foot and Mouth Disease (FMD) is a highly infectious viral pathogen affecting cows, buffaloes, and goats, causing ulcerated blisters on feet and lips that cripple lactation and draught capability."),

    # 10: Cattle vaccination importance
    ("Why is periodic prophylactic vaccination mandatory in commercial dairy herds?",
     ["To generate active immunological memory against fatal epizootic infections like Anthrax, Black Quarter, and FMD",
      "To double the size of the animal's horns",
      "To change the color of the cow's milk from white to yellow",
      "To make the cattle fall asleep during the day"],
     "A", "OSC", "easy",
     "Scheduled vaccines provoke active protective antibody titers in livestock, shielding entire herds from devastating bacterial and viral epidemics like Black Quarter, Anthrax, Brucellosis, and FMD."),

    # 11: Poultry farming definition
    ("What is the primary commercial purpose of poultry farming?",
     ["Rearing domesticated avian fowl for egg production and table meat",
      "Breeding songbirds for keeping in cages",
      "Catching migratory birds at sea",
      "Training birds to deliver postal mail"],
     "A", "OSC", "easy",
     "Poultry farming is the husbandry of domesticated gallinaceous fowl (chickens, ducks, turkeys) managed scientifically to harvest protein-rich table eggs and tender meat."),

    # 12: Layers vs Broilers distinction
    ("In poultry terminology, how do 'Layers' fundamentally differ from 'Broilers'?",
     ["Layers are specialized egg-laying hens reared up to 72 weeks, whereas Broilers are meat birds reared rapidly for 6 to 8 weeks",
      "Layers are reared for feathers while Broilers are kept as pets",
      "Layers eat only grains while Broilers eat only grass",
      "Layers are male birds while Broilers are exclusively wild ducks"],
     "A", "OSC", "easy",
     "Layers are selected and fed for high ovulatory frequency (yielding 250-300 eggs per laying cycle), whereas Broilers are fast-growing meat birds fed energy- and protein-rich rations to reach marketable body weight in 6 to 8 weeks."),

    # 13: Best layer breed
    ("Which world-famous exotic poultry breed is universally celebrated for maximum white egg production with low maintenance feed requirements?",
     ["White Leghorn", "Aseel", "Brahma", "Plymouth Rock"],
     "A", "OSC", "easy",
     "White Leghorn (originating in Italy) is the preeminent commercial egg layer breed due to its small body size (low maintenance ration), exceptional feed-to-egg conversion ratio, and prolific white egg output."),

    # 14: Broiler nutrition requirements
    ("Which nutritional elements must be provided in elevated amounts in the commercial feed of fast-growing broiler chickens?",
     ["Proteins and fats with adequate vitamin A and K",
      "High dietary fiber and low carbohydrates",
      "Salt crystals and vinegar",
      "Sand, sawdust, and table sugar"],
     "A", "OSC", "medium",
     "Broiler chicks undergo rapid muscle accretion and skeletal elongation over 40-50 days, demanding high levels of crude protein (20-22%), metabolic energy from fats, and vital vitamins (A, K) to prevent hemorrhages and optimize weight gain."),

    # 15: Indigenous game fowl breed
    ("Which indigenous Indian poultry breed from Andhra Pradesh and Uttar Pradesh is renowned for its aggressive fighting temperament, high stamina, and delicious meat quality?",
     ["Aseel", "Rhode Island Red", "White Leghorn", "Minorca"],
     "A", "OSC", "easy",
     "Aseel is a traditional Indian game fowl renowned for its majestic upright carriage, strong bone structure, pugnacity, and lean meat, though it lays relatively few eggs per year."),

    # 16: Poultry viral epidemic
    ("Which lethal viral disease, also known as Newcastle disease, causes respiratory distress, paralysis, greenish diarrhea, and high mortality in poultry flocks?",
     ["Ranikhet disease", "Foot and mouth disease", "Mastitis", "Rinderpest"],
     "A", "OSC", "medium",
     "Ranikhet disease (caused by Newcastle disease paramyxovirus) attacks the respiratory and nervous systems of domestic fowl, causing gasping, twisted necks, and fatal flock-wide mortality unless prevented by ocular/drinking-water vaccines."),

    # 17: Sericulture definition
    ("What does the commercial enterprise of Sericulture involve?",
     ["The scientific rearing of silkworms to produce natural silk fiber",
      "The rearing of honeybees for beeswax",
      "The cultivation of marine pearl oysters",
      "The breeding of earthworms for vermicompost"],
     "A", "OSC", "easy",
     "Sericulture encompasses the cultivation of host food plants (primarily mulberry trees) and the careful rearing of silkworm caterpillars (*Bombyx mori*) to harvest their silk cocoons."),

    # 18: Silkworm scientific species
    ("Which silkworm species is the most widely cultivated commercial producer of fine, lustrous mulberry silk worldwide?",
     ["Bombyx mori", "Apis dorsata", "Laccifer lacca", "Anopheles stephensi"],
     "A", "OSC", "easy",
     "Bombyx mori (the domesticated mulberry silkworm, an insect of order Lepidoptera) feeds exclusively on mulberry leaves and produces the finest, most uniform commercial silk fibers."),

    # 19: Host plant for Bombyx mori
    ("The caterpillars of the domestic silkworm Bombyx mori feed exclusively on the fresh leaves of which botanical plant?",
     ["Mulberry (Morus alba)", "Castor (Ricinus communis)", "Neem (Azadirachta indica)", "Oak (Quercus)"],
     "A", "OSC", "easy",
     "Bombyx mori is a monophagous caterpillar that requires fresh, tender leaves of the mulberry tree (*Morus alba*) containing specific attractant glucosides and nutrients to support rapid larval growth."),

    # 20: Silkworm lifecycle sequence
    ("What is the correct sequential order of developmental stages in the complete metamorphosis of the silkworm moth?",
     ["Egg -> Larva (Caterpillar) -> Pupa (inside Cocoon) -> Adult Moth",
      "Larva -> Egg -> Adult Moth -> Pupa",
      "Egg -> Pupa -> Larva -> Adult Moth",
      "Adult Moth -> Pupa -> Egg -> Larva"],
     "A", "OSC", "easy",
     "The silkworm exhibits holometabolous development: adult females lay microscopic eggs; ravenous larvae hatch and molt through 5 instars; the mature caterpillar spins a protective protective cocoon to transform into a pupa; the adult winged moth emerges to complete the cycle."),

    # 21: Silk filament chemical composition
    ("Chemically, what is the natural silk fiber spun by silkworm caterpillars composed of?",
     ["Two structural proteins: inner Fibroin filaments coated by outer adhesive Sericin gum",
      "Cellulose and plant starch",
      "Lipids, cholesterol, and fatty acids",
      "Calcium carbonate and silica crystals"],
     "A", "OSC", "medium",
     "Silkworm silk is a 100% natural animal protein fiber consisting of a tough crystalline core of fibroin filaments cemented together by an outer gummy glycoprotein coating called sericin secreted by paired labial silk glands."),

    # 22: Stifling process in sericulture
    ("Why are harvested silkworm cocoons subjected to 'stifling' (exposure to boiling water or hot air steam) before silk extraction?",
     ["To kill the developing pupa inside before it cuts through the continuous silk filaments, and to soften the sticky sericin gum for reeling",
      "To hatch thousands of baby silkworms at once",
      "To bleach the silk into red paint",
      "To preserve the pupa as food for aquarium fish"],
     "A", "OSC", "medium",
     "If the pupa metamorphoses into a moth, it secretes an alkaline enzyme (cocoonase) and cuts an exit hole through the cocoon, destroying continuous silk threads into fragmented waste; stifling humanely terminates the pupa and dissolves sericin to allow continuous unwinding."),

    # 23: Silk reeling process
    ("What is the technical term for the unwinding of long, continuous silk filaments from softened cocoons onto spinning reels?",
     ["Reeling", "Spawning", "Milking", "Carding"],
     "A", "OSC", "easy",
     "Reeling is the delicate industrial process wherein ends of single silk baves from 6 to 10 softened cocoons are located, gathered together, twisted into a single composite thread, and wound onto revolving reels."),

    # 24: Pisciculture definition
    ("What is the scientific term for the breeding, rearing, and commercial harvesting of edible fish in controlled freshwater bodies?",
     ["Pisciculture (Fish farming)", "Apiculture", "Sericulture", "Silviculture"],
     "A", "OSC", "easy",
     "Pisciculture (a major branch of aquaculture) is the controlled cultivation and harvesting of finfish in ponds, tanks, or reservoirs under scientifically managed environmental conditions."),

    # 25: Composite fish culture concept
    ("What is the primary ecological advantage of practising 'Composite Fish Culture' in a single freshwater pond?",
     ["Culturing 5 to 6 compatible fish species with distinct feeding zones maximizes total pond food utilization without interspecific food competition",
      "Fish eat each other so the farmer does not need to buy any fish food",
      "It prevents fish from swimming to the pond surface",
      "It turns freshwater into seawater automatically"],
     "A", "OSC", "medium",
     "Composite fish farming leverages ecological niche differentiation: different fish species feed at the surface, middle column, bottom mud, and on aquatic weeds simultaneously, multiplying pond yield without competing for the same food."),

    # 26: Ecological feeding zones of composite carps
    ("In a classic composite fish culture pond, match the Indian major carps to their natural water-column feeding zones:",
     ["Catla = Surface feeder; Rohu = Column/Middle zone feeder; Mrigal = Bottom feeder",
      "Catla = Bottom feeder; Rohu = Surface feeder; Mrigal = Submerged weed feeder",
      "Catla = Submerged plant feeder; Rohu = Bottom feeder; Mrigal = Air breather",
      "All three species feed strictly at the water surface"],
     "A", "OSC", "medium",
     "Catla possesses an upturned mouth adapted to catch zooplankton at the surface; Rohu has a terminal mouth for eating phytoplankton and detritus in the mid-water column; Mrigal possesses a ventral mouth to forage detritus and benthic worms on the pond bottom."),

    # 27: Grass carp weed feeding
    ("Which exotic carp species is introduced into composite fish ponds specifically to control unwanted submerged aquatic macrophytes and weeds?",
     ["Grass Carp (Ctenopharyngodon idella)", "Silver Carp", "Common Carp", "Clarias batrachus"],
     "A", "OSC", "easy",
     "Grass Carp (*Ctenopharyngodon idella*) is an herbivorous fish that voraciously grazes on underwater aquatic vegetation and pond weeds, converting nuisance biomass into valuable fish protein while keeping water clear."),

    # 28: Induced breeding in fish farming
    ("How do fish hatcheries obtain abundant pure, unadulterated fish seed (eggs and milt) during monsoon breeding seasons?",
     ["By induced breeding through pituitary gland extract or synthetic gonadotropin hormone injections (like Ovaprim)",
      "By collecting wild fish eggs from muddy polluted rivers",
      "By keeping fish under bright lights without water",
      "By feeding fish synthetic sugar crystals"],
     "A", "OSC", "medium",
     "Induced breeding injects carps with pituitary extract or synthetic gonadotropins (Ovaprim), triggering coordinated ovulation and sperm release in circular spawning tanks, guaranteeing pure, high-viability fry free from predatory wild species."),

    # 29: Apiculture definition
    ("What is Apiculture?",
     ["The scientific rearing and maintenance of honeybees in modern artificial hives to harvest honey and beeswax",
      "The rearing of earthworms for soil aeration",
      "The commercial cultivation of marine algae",
      "The farming of freshwater crabs"],
     "A", "OSC", "easy",
     "Apiculture is the art and agricultural science of managing honeybee colonies in domestic multi-frame bee boxes (Langstroth hives) to harvest pure natural honey, beeswax, propolis, and enhance crop pollination."),

    # 30: Indigenous honeybee species
    ("Which of the following is the common, docile Indian honeybee species adapted to domestic apiary boxes?",
     ["Apis cerana indica", "Apis dorsata", "Apis florea", "Bombus terrestris"],
     "A", "OSC", "easy",
     "Apis cerana indica (the Indian hive bee) is an indigenous, gentle honeybee species capable of being hived in wooden apiary boxes, yielding 3 to 5 kg of honey per hive annually."),

    # 31: Exotic European bee breed
    ("Why is the exotic European honeybee species Apis mellifera widely adopted across commercial Indian apiaries?",
     ["It produces very high honey yields (25-40 kg/hive/yr), has a mild sting, stays in the hive without absconding, and reproduces prolifically",
      "It is an aggressive bee that stings predatory birds to death",
      "It does not require flowers to make honey",
      "It produces blue-colored honey used in fireworks"],
     "A", "OSC", "easy",
     "Apis mellifera (the Italian/European bee) was successfully acclimatized in India because of its exceptional foraging capacity, high honey surplus yield, docile temperament, and low tendency to swarm or abandon hives."),

    # 32: Honeybee caste division of labor
    ("A well-organized honeybee colony exhibits strict social caste differentiation. What are the three distinct castes present in every hive?",
     ["A single fertile Queen, a few hundred haploid Drones, and thousands of sterile female Workers",
      "All male Worker bees led by a King bee",
      "Only female bees with no males present",
      "Soldier bees, Worker bees, and Farmer bees"],
     "A", "OSC", "easy",
     "A normal colony contains one fertile diploid Queen (the egg layer), several hundred haploid male Drones (whose sole function is mating with virgin queens), and up to 60,000 sterile diploid female Workers performing all hive labor."),

    # 33: Worker bee duties
    ("Which honeybee caste is exclusively responsible for building wax combs, gathering floral nectar and pollen, feeding brood larvae, and defending the hive?",
     ["Worker bees", "Queen bee", "Drone bees", "King bee"],
     "A", "OSC", "easy",
     "Worker bees perform all household and foraging chores: wax gland secretion for honeycomb construction, nursing larvae with royal jelly, guarding the entrance with their sting, and foraging nectar over vast floral landscapes."),

    # 34: Honey nutritional value
    ("What are the predominant biochemical constituents that give natural pure bee honey its sweetness and medicinal antimicrobial properties?",
     ["Fructose and glucose monosaccharides, along with enzymes, minerals, antioxidants, and low moisture content",
      "Synthetic sucrose and food coloring",
      "Pure saturated animal fat and cholesterol",
      "Hydrochloric acid and ethanol"],
     "A", "OSC", "easy",
     "Honey is concentrated floral nectar converted by bee invertase enzymes into simple sugars (approx 38% fructose, 31% glucose) suspended in low water activity (~17%), with hydrogen peroxide generating high antimicrobial and therapeutic properties."),

    # 35: Mushroom cultivation edible species
    ("Which of the following represents the most popular, commercially cultivated edible white button mushroom species worldwide?",
     ["Agaricus bisporus", "Amanita phalloides", "Rhizopus stolonifer", "Puccinia graminis"],
     "A", "OSC", "easy",
     "Agaricus bisporus (the common white button mushroom, a basidiomycete fungus) accounts for over 30% of global edible mushroom production, cherished for its culinary texture and rich nutritional profile."),

    # 36: Mushroom cultivation key stages
    ("What is the correct sequential order of principal steps followed in commercial button mushroom farming?",
     ["Substrate composting -> Spawning (inoculating mycelium) -> Casing (soil cover) -> Pinheading & Cropping",
      "Cropping -> Casing -> Boiling -> Freezing",
      "Spawning -> Substrate composting -> Canning -> Inoculating",
      "Planting seeds in mud -> Watering daily -> Direct sunlight exposure -> Harvesting"],
     "A", "OSC", "medium",
     "Button mushroom farming begins with aerobic/pasteurized composting of wheat or paddy straw; followed by 'spawning' (mixing grain spawn into compost); 'casing' with sterilized alkaline soil to trigger fruiting; and temperature/humidity control to harvest pinheads into mature mushrooms."),

    # 37: Mushroom nutritional profile
    ("Why are cultivated edible mushrooms widely recommended by dietitians and physicians as an exceptional functional food?",
     ["They are rich in digestible proteins, dietary fiber, vitamin B complex, vitamin D, and minerals, while having virtually zero fat and low carbohydrates",
      "They contain pure sugar that boosts blood glucose instantly",
      "They have the exact same chemical makeup as cow butter",
      "They contain synthetic pharmaceutical antibiotics in bulk"],
     "A", "OSC", "easy",
     "Mushrooms provide complete non-animal protein (20-35% dry weight) with all essential amino acids, high ergosterol (precursor of vitamin D), rich selenium and B-vitamins, making them ideal for diabetics, hypertensive patients, and vegetarians."),

    # 38: Agri-tourism concept
    ("How does 'Agri-tourism' empower rural farming communities and foster sustainable economic growth?",
     ["By integrating active farm tourism (farm stays, fresh harvesting, indigenous food, bullock cart rides) to provide farmers with stable secondary income alongside agricultural crops",
      "By converting all agricultural crop lands into concrete factory industrial zones",
      "By banning tourists from ever visiting village villages",
      "By forcing farmers to sell their cattle to city markets"],
     "A", "OSC", "easy",
     "Agri-tourism is an enterprise that invites urban visitors into rural farm environments to experience farm operations, taste unadulterated farm-fresh produce, and participate in rural cultural traditions, generating dependable non-crop seasonal income for farm families."),

    # 39: Agri-tourism biodiversity conservation
    ("How does agri-tourism contribute directly to the conservation of indigenous plant varieties and livestock breeds?",
     ["Demonstrating native crop landraces and heritage cattle breeds to visitors creates consumer demand and commercial incentive for farmers to preserve them",
      "By replacing all traditional crops with imported plastic flowers",
      "By cutting down ancient agroforestry trees",
      "By locking farm gates and abandoning land management"],
     "A", "OSC", "medium",
     "When urban tourists pay to experience organic heritage fruits, indigenous millets, and native cattle breeds (like Gir or Khillari), farmers gain economic justification to maintain ancestral genetic landraces instead of homogenizing monocultures."),

    # 40: Multi-enterprise integrated farming
    ("Combining animal husbandry, poultry, pisciculture, apiculture, sericulture, and mushroom cultivation into an Integrated Farming System (IFS) achieves which vital ecological benefit?",
     ["Zero-waste circular bio-economy where by-products of one enterprise become valuable nutrient inputs for another enterprise",
      "Increased dependence on expensive synthetic chemical pesticides",
      "Complete exhaustion of groundwater reserves within one season",
      "Excessive accumulation of toxic wastes in village landfills"],
     "A", "OSC", "easy",
     "An Integrated Farming System (IFS) recycles materials: cattle dung feeds biogas digesters and pond carps; spent mushroom compost fertilizes crop fields; crop residues feed cattle and compost; and bees boost cross-pollination across all crops, maximizing farm profit with zero ecological waste.")
]

practice_data = [
    # 41: Foot and mouth disease symptoms
    ("A dairy farmer notices that several cows have high fever, profuse frothy salivation, and painful blister-like vesicles between their hooves, causing severe lameness. What disease should the veterinary doctor immediately suspect?",
     ["Foot and Mouth Disease (FMD)", "Ascariasis", "Avian Influenza", "Down syndrome"],
     "A", "OSC", "medium",
     "Foot and Mouth Disease (FMD) is a contagious aphtovirus infection causing characteristic blister eruptions (aphthae) inside the oral cavity and interdigital clefts of hooves, resulting in painful drooling and severe lameness."),

    # 42: Concentrates in cattle nutrition
    ("Which of the following feed items belongs to the 'Concentrate' category in dairy cattle management?",
     ["Cottonseed cake and groundnut meal", "Green Napier grass", "Dry sorghum straw (kadbi)", "Paddy straw"],
     "A", "OSC", "easy",
     "Concentrates are nutrient-dense feedstuffs low in crude fiber (<18%) but rich in digestible protein and carbohydrates, exemplified by oilseed cakes (cottonseed, mustard, groundnut) and cereal grains, unlike fibrous roughage."),

    # 43: Artificial insemination in cattle
    ("What is the primary technological benefit of utilizing Artificial Insemination (AI) with cryopreserved bull semen in dairy cattle breeding?",
     ["Superior genetic traits of elite pedigree bulls can be disseminated to thousands of native cows across distant geographical regions while preventing venereal disease transmission",
      "It guarantees that cows give birth to twins every single month",
      "It eliminates the need to provide cows with drinking water",
      "It allows bulls to produce milk instead of cows"],
     "A", "OSC", "medium",
     "Artificial insemination uses frozen semen from proven high-merit sires to fertilize thousands of cows safely, drastically upgrading the genetic potential for milk production across an entire district while avoiding transport risks and venereal pathogens."),

    # 44: White Leghorn egg efficiency
    ("Why is White Leghorn preferred in commercial poultry egg units over heavier breeds like Rhode Island Red or Australorp?",
     ["It consumes less feed due to light body weight while converting feed into eggs with maximum metabolic efficiency",
      "It lays four eggs every single day",
      "It lays eggs with pre-cooked hard shells",
      "It acts as a guard dog to protect the farm from foxes"],
     "A", "OSC", "medium",
     "Because White Leghorns have a compact body weight (~1.8-2.0 kg), their basal metabolic maintenance energy requirement is low; almost all nutrients in their feed ration are diverted directly into ovulating eggs, yielding high profits per kilogram of feed."),

    # 45: Broiler floor management (Deep Litter System)
    ("In commercial broiler poultry rearing, what is the purpose of spreading a 5 cm thick layer of dry saw dust or rice husk as 'deep litter' on the shed floor?",
     ["To absorb avian moisture and excreta, insulate birds against cold ground, and maintain a dry hygienic floor that inhibits coccidiosis parasites",
      "To provide seeds for the chickens to plant in the ground",
      "To prevent chickens from flying out of the roof",
      "To color chicken feathers green for market sale"],
     "A", "OSC", "medium",
     "Deep litter using absorbent organic materials (rice husk, wood shavings) absorbs wet feces, promotes beneficial bacterial breakdown of droppings, provides thermal insulation, and keeps feet clean and dry, minimizing pathogenic bacterial and coccidial outbreaks."),

    # 46: Ranikhet vaccine administration
    ("Poultry chicks are vaccinated against Ranikhet disease (F1/Lasota strain) at a very young age (5-7 days old) typically through which administrative route?",
     ["Ocular (eye drop) or nasal droplet", "Intravenous blood injection", "Subcutaneous tail incision", "Surgical bone implant"],
     "A", "OSC", "easy",
     "The primary Newcastle disease (Ranikhet) vaccine (F1 / Lasota strain) is administered as an eye drop or nostril droplet, rapidly colonizing respiratory and conjunctival mucous membranes to establish local mucosal IgA immunity."),

    # 47: Silkworm salivary glands modification
    ("From which anatomical structure of the silkworm caterpillar are the silk-producing fibroin and sericin proteins secreted?",
     ["Modified labial salivary glands located in the caterpillar's head",
      "The midgut digestive stomach",
      "The antennae and sensory palps",
      "The claws on abdominal pseudolegs"],
     "A", "OSC", "medium",
     "Silk glands are enormous, modified labial salivary glands running along both sides of the caterpillar's body; they produce viscous structural proteins that exit via a microscopic median spinning tube called the spinneret located on the lower lip."),

    # 48: Silkworm cocoon spinning duration
    ("How long does a fully grown fifth-instar silkworm caterpillar take to completely spin its silk cocoon around itself?",
     ["Approximately 3 to 4 days, executing continuous figure-eight head movements",
      "Exactly 5 minutes",
      "Over 6 months",
      "One full year"],
     "A", "OSC", "easy",
     "A mature 5th-instar silkworm ceases feeding, finds a dry branch or plastic spinning frame (chandrika), and oscillates its head in figure-8 motions uninterruptedly for 72 to 96 hours, spinning an unbroken filament 800 to 1,200 meters long into a cocoon."),

    # 49: Length of single cocoon silk thread
    ("What is the typical approximate length of a single continuous silk filament obtained from one unbroken commercial Bombyx mori cocoon?",
     ["800 to 1,200 meters", "2 to 3 centimeters", "50 to 60 kilometers", "10 to 12 millimeters"],
     "A", "OSC", "medium",
     "A single intact mulberry cocoon yields an extraordinarily long, unbroken double-filament of silk (called a bave) measuring between 800 and 1,200 meters in length, prized for luxurious textiles."),

    # 50: Catla surface feeding anatomical adaptation
    ("Which morphological feature of the Indian major carp Catla catla allows it to efficiently harvest plankton floating at the water surface?",
     ["A prominent upturned mouth with a protruding lower jaw and absence of barbels",
      "A downward-facing ventral mouth designed to scrape mud",
      "Large sharp teeth designed to crush snail shells",
      "A long probe-like beak like a pelican"],
     "A", "OSC", "medium",
     "Catla possesses a wide, oblique upturned superior mouth with a prominent lower jaw, perfectly oriented to scoop up microscopic zooplankton drifting on the surface layer of the pond."),

    # 51: Rohu middle-layer feeding niche
    ("What is the primary natural food item consumed by Rohu (Labeo rohita) swimming in the column zone of a composite fish pond?",
     ["Phytoplankton, microscopic algae, and decaying submerged vegetation",
      "Large frogs, snakes, and water birds",
      "Mud particles and sand pebbles exclusively",
      "Grass floating on dry land outside the pond"],
     "A", "OSC", "easy",
     "Rohu is a column feeder whose fringed lips and gill-rakers strain microscopic unicellular and filamentous algae (phytoplankton) as well as soft detritus suspended in the middle depths of the water."),

    # 52: Mrigal bottom feeding habits
    ("Why is Mrigal (Cirrhinus mrigala) classified as a benthic bottom feeder in composite fish aquaculture?",
     ["It possesses a ventral, downward-directed mouth adapted to forage on bottom detritus, decomposing organic matter, and benthic invertebrates",
      "It catches flying insects jumping above the water surface",
      "It only eats green tree leaves floating on the surface",
      "It crawls onto the dry shore to graze on lawn grass"],
     "A", "OSC", "easy",
     "Mrigal has a ventral mouth positioned underneath its snout, enabling it to scour the pond floor, consuming decaying organic mud, microscopic benthic algae, and aquatic worms, effectively cleaning the pond bed."),

    # 53: Queen bee royal jelly nutrition
    ("What exclusive diet triggers a normal female honeybee larva to develop into a fully fertile, long-lived Queen bee instead of a sterile worker?",
     ["Royal jelly secreted continuously by nurse worker hypopharyngeal glands throughout its entire larval development",
      "Pure honey mixed with dry sand",
      "Undigested pollen grains alone",
      "Ordinary water with table salt"],
     "A", "OSC", "medium",
     "All bee larvae receive royal jelly for the first 3 days, but queen larvae are placed in specialized vertical queen cups and fed copious quantities of nutrient-rich royal jelly exclusively throughout their entire larval period, activating fertility hormones."),

    # 54: Drone bee haploid origin
    ("In honeybee biology, how are male Drones produced inside the colony?",
     ["By parthenogenesis: from unfertilized haploid eggs laid by the queen",
      "From fertilized diploid eggs fed with high-protein pollen",
      "By metamorphosis of elderly worker bees",
      "By catching wild flies and bringing them into the hive"],
     "A", "OSC", "medium",
     "Honeybees display haplodiploid sex determination: fertilized diploid eggs (having 32 chromosomes) develop into females (workers or queens), while unfertilized eggs laid by the queen develop via arrhenotokous parthenogenesis into haploid males (drones, with 16 chromosomes)."),

    # 55: Bee waggle dance function
    ("Why do foraging worker honeybees perform the famous 'waggle dance' on the vertical comb inside the hive?",
     ["To communicate the exact distance and directional angle of a rich nectar source relative to the position of the sun",
      "To scare away predator hornets from the hive",
      "To cool the hive down during hot summer afternoons",
      "To entertain the queen bee while she lays eggs"],
     "A", "OSC", "hard",
     "Deciphered by Karl von Frisch, the waggle dance encodes polar vector coordinates: the angle of the waggle run relative to gravity communicates the direction of flowers relative to the sun, while the tempo indicates flight distance."),

    # 56: Honeybee pollination service
    ("Economically, why is the pollination service rendered by honeybees considered far more valuable than the actual honey produced by apiaries?",
     ["Cross-pollination by foraging bees dramatically boosts fruit set, seed yield, and crop quality in oilseeds, pulses, fruits, and vegetables",
      "Bees inject honey directly into plant roots to make plants grow",
      "Bees trim dead leaves from trees like garden shears",
      "Bees warm up the soil so seeds germinate faster"],
     "A", "OSC", "easy",
     "While honey provides sweet food, the ecological pollination service of honeybees increases agricultural crop yields by 20 to 100% in crops like sunflower, mustard, apple, and cucurbits, valued at billions of dollars annually."),

    # 57: Mushroom spawn definition
    ("In commercial mushroom cultivation, what does the term 'Spawn' refer to?",
     ["Pure fungal mycelium grown and multiplied on sterilized cereal grains (like wheat or rye) used as planting seed",
      "The poisonous spores collected from wild forests",
      "Chemical pesticide powder dusted over compost",
      "A liquid fertilizer made from animal blood"],
     "A", "OSC", "easy",
     "Mushroom 'spawn' is the fungal equivalent of crop seed: it consists of sterilized cereal grains (wheat, sorghum, rye) permeated with vigorous, pure vegetative mycelium of the selected edible mushroom species."),

    # 58: Casing soil in mushroom beds
    ("Why is a 3 to 4 cm layer of sterilized 'casing soil' (chalk and peat or decomposed farmyard manure) spread over colonized mushroom compost?",
     ["It retains moisture, provides structural support, and stimulates vegetative mycelium to transition into reproductive fruiting bodies (pinheads)",
      "It poisons all competitor fungi instantly",
      "It blocks all oxygen from reaching the compost",
      "It acts as a permanent roof so mushrooms can grow in complete darkness forever"],
     "A", "OSC", "medium",
     "Casing soil provides high water-holding capacity, neutral to slightly alkaline pH (~7.5), and low nutrient density, signaling the vegetative mycelium that nutrient exhaustion has occurred, which induces pinhead formation and fruiting body emergence."),

    # 59: Oyster mushroom cultivation advantages
    ("Why is the Oyster mushroom (Pleurotus species / Dhingri) exceptionally popular among small-scale rural farmers in India?",
     ["It can be cultivated easily on unfermented chopped paddy straw bags at ambient room temperatures (20-30°C) with low initial capital investment",
      "It grows inside refrigerators at freezing temperatures",
      "It requires expensive imported air-conditioned chambers",
      "It produces edible gold flakes along with mushroom caps"],
     "A", "OSC", "easy",
     "Unlike button mushrooms requiring pasteurized compost and chilled casing rooms, Oyster mushrooms (*Pleurotus sajor-caju*) thrive on simple boiled agricultural straw at room temperatures, making them ideal for low-cost cottage industries."),

    # 60: Agri-tourism educational impact
    ("How does agri-tourism serve as an educational platform for urban school children and families?",
     ["It reconnects urban citizens with the origins of their food, demonstrating soil conservation, milk production, organic pest management, and biodiversity firsthand",
      "It teaches children how to operate video games on the farm",
      "It trains children to replace all nature with concrete structures",
      "It promotes eating processed chemical junk foods"],
     "A", "OSC", "easy",
     "Agri-tourism bridges the urban-rural divide by allowing city residents to touch living farm animals, understand crop sowing and harvesting, taste raw honey from bee boxes, and appreciate ecological stewardship."),

    # 61: Multiple choice OMC on cattle breeds
    ("Which of the following are recognized INDIGENOUS (Desi) Indian breeds of cattle? (Select all that apply)",
     ["Gir (Gujarat)", "Sahiwal (Punjab/Haryana)", "Khillari (Maharashtra)", "Holstein-Friesian (Netherlands)"],
     "A,B,C", "OMC", "medium",
     "Gir, Sahiwal, and Khillari are indigenous *Bos indicus* breeds with characteristic humps and dewlaps, whereas Holstein-Friesian is a temperate exotic *Bos taurus* breed originating in Europe."),

    # 62: Multiple choice OMC on honeybee products
    ("Which commercial products are harvested from scientific apiculture? (Select all that apply)",
     ["Natural honey", "Beeswax used in cosmetics and pharmaceuticals", "Royal jelly and Bee venom", "Synthetic nylon thread"],
     "A,B,C", "OMC", "easy",
     "Bees yield honey, beeswax (from abdominal wax glands), royal jelly (superfood), propolis (plant resin sealant with antibiotic properties), and purified bee venom (used in apitherapy for arthritis). Nylon is a synthetic petroleum polymer."),

    # 63: Multiple choice OMC on composite fish carps
    ("Which of the following fish species are compatible members of a six-species composite fish culture system? (Select all that apply)",
     ["Catla (surface feeder)", "Rohu (column feeder)", "Mrigal (bottom feeder)", "Grass Carp (weed feeder)"],
     "A,B,C,D", "OMC", "medium",
     "All four carps occupy non-overlapping trophic niches: Catla at the surface, Rohu in the mid-column, Mrigal on the bottom mud, and Grass Carp consuming nuisance weeds, enabling complete resource exploitation."),

    # 64: True or False on silkworm stifling
    ("State whether True or False: If silkworm cocoons are allowed to hatch naturally, the emerging adult moth cuts through the continuous silk filaments, making the silk unsuitable for industrial high-grade reeling.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The emerging adult moth dissolves an opening in the cocoon shell with alkaline salivary enzymes, severing continuous kilometer-long silk filaments into fragmented pieces usable only as inferior spun silk yarn."),

    # 65: True or False on Broiler vs Layer diet
    ("State whether True or False: Broiler chickens reared for table meat require higher protein and fat content in their feed compared to egg-laying hens.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Broiler chicks require high-protein rations (20-22%) and energy-dense fats to rapidly gain body weight in 6-8 weeks, whereas adult layers require moderate protein (16-18%) supplemented with high calcium (3.5-4%) for eggshell calcification."),

    # 66: True or False on Drone bees
    ("State whether True or False: Male Drone honeybees possess powerful venomous stings and actively forage outside the hive to gather nectar and pollen.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Drones are stingless (the sting is a modified ovipositor present only in females: workers and queen) and do not forage; their sole role is mating with a young virgin queen during the nuptial flight."),

    # 67: Assertion and Reason on Cattle cross-breeding
    ("Assertion (A): Exotic cattle breeds like Jersey are cross-bred with indigenous Indian breeds like Gir or Sahiwal.\nReason (R): The resulting cross-bred progeny combine high milk yields and prolonged lactation with excellent heat tolerance and disease resistance.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "Cross-breeding unites the commercial milk abundance and extended lactation of exotic temperate stock with the rugged tick-resistance, tropical heat tolerance, and hardiness of native humped cattle."),

    # 68: Assertion and Reason on Composite fish culture
    ("Assertion (A): Culturing Catla, Rohu, and Mrigal together in one pond produces drastically higher fish yield per hectare than rearing a single species alone.\nReason (R): These three fish species consume food from the surface, column, and bottom layers respectively, eliminating competition for food resources.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "Stratified vertical feeding habits prevent interspecific competition: each species exploits its specific micro-habitat (surface, water column, bottom sediment), maximizing total biomass yield per unit pond volume."),

    # 69: Fill in the blank on Sericulture
    ("Fill in the blank: The natural protein core of silk fiber is known as ________, which is surrounded by an adhesive gum called sericin.",
     ["fibroin", "keratin", "collagen", "hemoglobin"],
     "A", "OFB", "medium",
     "Silk fiber contains 70-80% fibroin (an insoluble structural protein composed of glycine, alanine, and serine beta-sheets) enveloped by 20-30% sericin (a gummy hydrophilic glue)."),

    # 70: Numerical objective on Apis mellifera yield
    ("An apiary maintains 50 modern Langstroth bee boxes with Italian honeybees (Apis mellifera). If each colony produces an average annual surplus of 30 kg of pure honey, calculate the total annual honey harvest from the apiary in kilograms.",
     ["1500", "500", "3000", "150"],
     "A", "ONE", "easy",
     "Total annual honey harvest = Number of bee hives * Average yield per hive = 50 hives * 30 kg/hive = 1500 kg.")
]

mock_data = [
    # 71: Silkworm Complete Metamorphosis Lifecycle
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Circular Stages -->
  <!-- 1. Eggs on Mulberry leaf -->
  <rect x="25" y="25" width="80" height="65" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
  <circle cx="55" cy="50" r="3" fill="#facc15"/>
  <circle cx="65" cy="52" r="3" fill="#facc15"/>
  <circle cx="60" cy="62" r="3" fill="#facc15"/>
  <text x="65" y="78" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">1. Eggs (300-500)</text>
  <!-- Arrow 1 to 2 -->
  <line x1="110" y1="55" x2="145" y2="55" stroke="#facc15" stroke-width="2"/>
  <!-- 2. Caterpillar -->
  <rect x="150" y="25" width="95" height="65" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 165 55 Q 180 45 195 55 T 225 55" stroke="#4ade80" stroke-width="4" fill="none"/>
  <text x="197" y="78" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">2. Larva / Caterpillar</text>
  <text x="197" y="86" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">Feeds on Mulberry</text>
  <!-- Arrow 2 to 3 -->
  <line x1="250" y1="55" x2="285" y2="55" stroke="#facc15" stroke-width="2"/>
  <!-- 3. Cocoon & Pupa -->
  <rect x="290" y="25" width="85" height="65" rx="6" fill="#854d0e" stroke="#eab308" stroke-width="1.5"/>
  <ellipse cx="332" cy="50" rx="16" ry="12" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
  <text x="332" y="78" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">3. Cocoon (Silk)</text>
  <text x="332" y="86" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">Spins 1000m thread!</text>
  <!-- Arrow down to Adult -->
  <path d="M 332 95 L 332 120" stroke="#facc15" stroke-width="2"/>
  <!-- 4. Adult Moth -->
  <rect x="150" y="115" width="105" height="80" rx="6" fill="#18181b" stroke="#f43f5e" stroke-width="1.5"/>
  <ellipse cx="202" cy="150" rx="12" ry="16" fill="#cbd5e1"/>
  <path d="M 190 145 Q 170 135 175 160 Z" fill="#94a3b8"/>
  <path d="M 214 145 Q 234 135 229 160 Z" fill="#94a3b8"/>
  <text x="202" y="180" fill="#f43f5e" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">4. Adult Silkmoth</text>
  <text x="202" y="190" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Flies, mates & dies</text>
  <!-- Arrow back -->
  <path d="M 145 155 Q 65 155 65 95" stroke="#facc15" stroke-width="2" fill="none"/>
  <!-- Critical Stifling Callout -->
  <rect x="265" y="125" width="125" height="65" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="327" y="145" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">STIFLING INTERVENTION:</text>
  <text x="327" y="160" fill="#fecaca" font-size="7" font-family="sans-serif" text-anchor="middle">Steam kill pupa at Stage 3</text>
  <text x="327" y="175" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Prevents moth cutting silk!</text>
</svg>
</div>
At which precise developmental stage shown above must sericulture farmers intervene with heat stifling to harvest continuous, unbroken silk filaments?""",
     ["Stage 3: The cocoon containing the living pupa before it metamorphoses into an adult moth",
      "Stage 1: As soon as the eggs are laid on mulberry leaves",
      "Stage 2: When the caterpillar reaches its first instar stage",
      "Stage 4: After the winged adult moth flies away into the forest"],
     "A", "OSC", "easy",
     "Sericulture relies on boiling or steaming cocoons at Stage 3 while the pupa is intact inside; allowing metamorphosis to proceed to Stage 4 results in the adult moth secreting alkaline cocoonase and biting through the continuous silk bave, reducing it to fragmented waste."),

    # 72: Honeybee Colony Caste Hierarchy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Caste 1: Queen -->
  <rect x="20" y="25" width="110" height="155" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <ellipse cx="75" cy="65" rx="14" ry="26" fill="#eab308"/>
  <text x="75" y="110" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">QUEEN (1 per hive)</text>
  <text x="75" y="128" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Diploid Female (2n=32)</text>
  <text x="75" y="143" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Fed on Royal Jelly</text>
  <text x="75" y="160" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Lays 1500-2000 eggs/day</text>
  <!-- Caste 2: Drone -->
  <rect x="145" y="25" width="110" height="155" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="200" cy="65" rx="16" ry="20" fill="#0284c7"/>
  <text x="200" y="110" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">DRONES (Hundreds)</text>
  <text x="200" y="128" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Haploid Male (n=16)</text>
  <text x="200" y="143" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">From unfertilized eggs</text>
  <text x="200" y="160" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">Sole duty: Mate with Queen</text>
  <!-- Caste 3: Worker -->
  <rect x="270" y="25" width="110" height="155" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <ellipse cx="325" cy="65" rx="11" ry="16" fill="#16a34a"/>
  <text x="325" y="110" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">WORKERS (Thousands)</text>
  <text x="325" y="128" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Sterile Female (2n=32)</text>
  <text x="325" y="143" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Wax secretion & nursing</text>
  <text x="325" y="160" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Nectar/pollen collection</text>
</svg>
</div>
Based on the biological caste hierarchy depicted above, how is sex and social role determined in honeybees?""",
     ["Females (Queen and Workers) are diploid (2n=32) developing from fertilized eggs, while males (Drones) are haploid (n=16) developing parthenogenetically from unfertilized eggs",
      "All bees in the hive are males with different fur patterns",
      "Queen bees are born from stones while workers are born from trees",
      "Drones lay eggs while the Queen gathers floral nectar"],
     "A", "OSC", "medium",
     "Honeybees display haplodiploidy: unfertilized eggs hatch into haploid males (drones, n=16), while fertilized eggs develop into diploid females (2n=32), which differentiate into a fertile queen (via continuous royal jelly feeding) or sterile worker bees (via worker jelly and bee bread)."),

    # 73: Composite Fish Culture Depth Zones
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Zone 1: Surface Layer -->
  <rect x="30" y="20" width="340" height="45" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="1"/>
  <ellipse cx="70" cy="42" rx="20" ry="8" fill="#38bdf8"/>
  <text x="110" y="38" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">SURFACE FEEDERS: Catla & Silver Carp</text>
  <text x="110" y="52" fill="#cbd5e1" font-size="8" font-family="sans-serif">Upturned mouth -> Consume floating zooplankton & phytoplankton</text>
  <!-- Zone 2: Column / Middle Layer -->
  <rect x="30" y="75" width="340" height="45" rx="4" fill="#1e3a8a" stroke="#2563eb" stroke-width="1"/>
  <ellipse cx="70" cy="97" rx="22" ry="7" fill="#60a5fa"/>
  <text x="110" y="93" fill="#93c5fd" font-size="10" font-family="sans-serif" font-weight="bold">COLUMN FEEDERS: Rohu (Labeo rohita)</text>
  <text x="110" y="107" fill="#cbd5e1" font-size="8" font-family="sans-serif">Terminal mouth -> Grazes suspended microalgae & mid-depth plankton</text>
  <!-- Zone 3: Bottom Layer -->
  <rect x="30" y="130" width="340" height="45" rx="4" fill="#78350f" stroke="#d97706" stroke-width="1"/>
  <ellipse cx="70" cy="152" rx="20" ry="7" fill="#f59e0b"/>
  <text x="110" y="148" fill="#fcd34d" font-size="10" font-family="sans-serif" font-weight="bold">BOTTOM FEEDERS: Mrigal & Common Carp</text>
  <text x="110" y="162" fill="#fde68a" font-size="8" font-family="sans-serif">Ventral mouth -> Scavenges benthic worms, detritus & pond floor mud</text>
  <!-- Bottom summary -->
  <text x="200" y="195" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ecological Result: 100% Pond Volume Utilized with Zero Interspecific Food Competition!</text>
</svg>
</div>
How does the spatial depth stratification shown in composite fish culture prevent different carp species from competing for sustenance in the same pond?""",
     ["Each fish species possesses mouth adaptations suited to forage strictly within its designated vertical zone (surface, middle column, or bottom sediment)",
      "The farmer builds concrete underwater fences between different fish",
      "Fish are tied to ropes so they cannot swim to other depths",
      "Fish only eat during different months of the year"],
     "A", "OSC", "easy",
     "Composite fish farming exploits morphological niche partitioning: Catla feeds exclusively at the surface with an upturned mouth, Rohu grazes in the middle water column, and Mrigal scavenges the pond bottom floor with a ventral mouth, eliminating competition."),

    # 74: Button Mushroom Fruiting Body Anatomy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Mushroom Drawing -->
  <!-- Pileus (Cap) -->
  <path d="M 80 80 Q 140 15 200 80 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Gills under cap -->
  <line x1="90" y1="80" x2="135" y2="80" stroke="#f43f5e" stroke-width="3"/>
  <line x1="145" y1="80" x2="190" y2="80" stroke="#f43f5e" stroke-width="3"/>
  <!-- Stipe (Stem) -->
  <rect x="125" y="80" width="30" height="80" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Annulus (Ring) -->
  <path d="M 120 110 Q 140 120 160 110" stroke="#facc15" stroke-width="3" fill="none"/>
  <!-- Underground Mycelium -->
  <path d="M 140 160 Q 110 180 90 190" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
  <path d="M 140 160 Q 150 185 170 190" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
  <!-- Labels -->
  <line x1="140" y1="45" x2="240" y2="45" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="245" y="48" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold">Pileus (Fleshy Cap)</text>
  <line x1="170" y1="80" x2="240" y2="80" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="245" y="83" fill="#f87171" font-size="10" font-family="sans-serif" font-weight="bold">Gills (Lamellae with Basidia)</text>
  <text x="245" y="96" fill="#cbd5e1" font-size="8" font-family="sans-serif">Produces billions of microscopic spores</text>
  <line x1="150" y1="110" x2="240" y2="110" stroke="#facc15" stroke-width="1.5"/>
  <text x="245" y="113" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Annulus (Veil Remnant Ring)</text>
  <line x1="155" y1="135" x2="240" y2="135" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="245" y="138" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold">Stipe (Central Stalk / Stem)</text>
  <line x1="140" y1="175" x2="240" y2="175" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="245" y="178" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Vegetative Mycelium in Compost</text>
</svg>
</div>
In the anatomical structure of the edible mushroom fruiting body shown above, where are the reproductive microscopic basidiospores produced?""",
     ["On the microscopic basidia lining the fleshy pink/brown gills (lamellae) situated underneath the pileus cap",
      "Inside the central solid stipe stalk",
      "On top of the smooth umbrella skin",
      "Inside the annulus ring exclusively"],
     "A", "OSC", "medium",
     "The under-surface of the mushroom cap (pileus) bears radiating vertical plates called gills (lamellae), lined with club-shaped basidia that discharge millions of haploid basidiospores into passing air currents."),

    # 75: Cattle Breeds Classification Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Indigenous Box -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">INDIGENOUS (Bos indicus)</text>
  <text x="107" y="65" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Prominent hump & dewlap</text>
  <text x="107" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- High tropical heat resistance</text>
  <text x="107" y="95" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Tick & parasite resistance</text>
  <text x="107" y="118" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Milch: Gir, Sahiwal, Red Sindhi</text>
  <text x="107" y="135" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Draught: Khillari, Dangi, Hallikar</text>
  <text x="107" y="152" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">A2 beta-casein rich milk</text>
  <!-- Exotic Box -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="48" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">EXOTIC (Bos taurus)</text>
  <text x="292" y="65" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- No hump; temperate origin</text>
  <text x="292" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Very high milk yield / day</text>
  <text x="292" y="95" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Extended lactation period</text>
  <text x="292" y="118" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Jersey (Island of Jersey, UK)</text>
  <text x="292" y="135" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Holstein-Friesian (Netherlands)</text>
  <text x="292" y="152" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">Susceptible to tropical heat stress</text>
</svg>
</div>
What anatomical and environmental adaptation distinguishes indigenous Indian cattle (Bos indicus) from exotic temperate dairy cattle (Bos taurus)?""",
     ["Indigenous cattle possess a prominent dorsal hump, large folded dewlap, and sweat glands conferring outstanding tropical heat and tick resistance",
      "Indigenous cattle have wings while exotic cattle do not",
      "Indigenous cattle can survive without oxygen",
      "Exotic cattle drink sea water while indigenous cattle drink oil"],
     "A", "OSC", "easy",
     "Bos indicus evolved large vascular dewlaps, dorsal muscular humps, and abundant sweat glands that dissipate heat under blazing tropical conditions while conferring innate resistance against tick-borne hemoparasites."),

    # 76: Integrated Farming System (IFS) Circular Economy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Central Hub: Zero Waste Farm -->
  <circle cx="200" cy="100" r="32" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="98" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">INTEGRATED</text>
  <text x="200" y="108" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">FARMING</text>
  <!-- Node 1: Dairy Cattle (Top Left) -->
  <rect x="30" y="25" width="100" height="40" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="80" y="48" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">1. Cattle / Dairy</text>
  <!-- Node 2: Biogas & Vermicompost (Top Right) -->
  <rect x="270" y="25" width="100" height="40" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="320" y="48" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">2. Biogas / Slurry</text>
  <!-- Node 3: Fish Pond (Bottom Right) -->
  <rect x="270" y="135" width="100" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="320" y="158" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">3. Fish Pond</text>
  <!-- Node 4: Crops & Apiculture (Bottom Left) -->
  <rect x="30" y="135" width="100" height="40" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="80" y="158" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">4. Crops & Bees</text>
  <!-- Flow Lines -->
  <line x1="130" y1="45" x2="270" y2="45" stroke="#facc15" stroke-width="2"/>
  <text x="200" y="38" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Cow Dung & Urine</text>
  <line x1="320" y1="65" x2="320" y2="135" stroke="#38bdf8" stroke-width="2"/>
  <text x="345" y="105" fill="#38bdf8" font-size="7" font-family="sans-serif">Digested Slurry</text>
  <line x1="270" y1="155" x2="130" y2="155" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="170" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">Pond Silt -> Rich Manure</text>
  <line x1="80" y1="135" x2="80" y2="65" stroke="#22c55e" stroke-width="2"/>
  <text x="50" y="105" fill="#22c55e" font-size="7" font-family="sans-serif">Green Fodder</text>
</svg>
</div>
How does the Integrated Farming System (IFS) model shown above achieve zero-waste sustainable agriculture?""",
     ["By-products and waste streams from one enterprise (like cattle dung) serve directly as energy or nutrient inputs for other components (biogas, fish ponds, and crop fertilizers)",
      "By purchasing synthetic chemical fertilizers in bulk from overseas factories",
      "By throwing all agricultural wastes into nearby rivers",
      "By running tractor engines on pure cooking oil 24 hours a day"],
     "A", "OSC", "easy",
     "IFS operates as a closed circular bio-loop: cattle dung feeds biogas digesters; nutrient-rich effluent fertilizes fish ponds and organic crop plots; crop residues return as livestock fodder; and apiary bees multiply crop fruit set."),

    # 77: Honeybee Waggle Dance Directional Encoding
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Vertical Sun Gravity Reference -->
  <line x1="120" y1="170" x2="120" y2="30" stroke="#facc15" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="120" cy="25" r="12" fill="#eab308"/>
  <text x="120" y="28" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SUN</text>
  <text x="90" y="100" fill="#facc15" font-size="8" font-family="sans-serif">Gravity (Up = Sun)</text>
  <!-- Waggle Run Line at Angle Theta -->
  <line x1="120" y1="140" x2="175" y2="70" stroke="#f43f5e" stroke-width="4"/>
  <path d="M 120 100 A 40 40 0 0 1 150 80" stroke="#f43f5e" stroke-width="1.5" fill="none"/>
  <text x="145" y="105" fill="#f43f5e" font-size="11" font-family="sans-serif" font-weight="bold">theta</text>
  <!-- Return loops (Figure-8) -->
  <path d="M 175 70 C 210 90 200 130 120 140" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2" fill="none"/>
  <path d="M 175 70 C 130 50 80 80 120 140" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2" fill="none"/>
  <!-- Info Box -->
  <rect x="220" y="35" width="160" height="130" rx="6" fill="#090d16" stroke="#facc15" stroke-width="1"/>
  <text x="300" y="55" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Karl von Frisch Discovery:</text>
  <text x="230" y="75" fill="#cbd5e1" font-size="8" font-family="sans-serif">1. Angle (theta) relative to vertical</text>
  <text x="230" y="90" fill="#cbd5e1" font-size="8" font-family="sans-serif">   = Angle to flowers relative to Sun</text>
  <text x="230" y="110" fill="#cbd5e1" font-size="8" font-family="sans-serif">2. Duration of waggle run</text>
  <text x="230" y="125" fill="#cbd5e1" font-size="8" font-family="sans-serif">   = Distance to nectar source</text>
  <text x="230" y="145" fill="#4ade80" font-size="8" font-family="sans-serif">3. Abdomen shaking = Richness!</text>
</svg>
</div>
In the honeybee communication mechanism illustrated above, what specific information is conveyed by the angle (theta) of the straight waggle run relative to vertical gravity?""",
     ["The flight direction of the floral nectar source relative to the current azimuth position of the sun",
      "The exact temperature of the honeycomb wax",
      "The number of hornets attacking the hive",
      "The time remaining until sunset"],
     "A", "OSC", "hard",
     "Worker bees translate celestial vectors onto the vertical dark comb: the deviation angle (theta) between the waggle run and vertical gravity represents the precise flight bearing toward rich floral patches relative to the sun."),

    # 78: Deep Litter System in Poultry Housing
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Shed Roof & Wire Mesh Ventilation -->
  <polygon points="40,40 200,15 360,40" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <rect x="50" y="40" width="300" height="60" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <text x="200" y="65" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Wire Mesh Walls -> Ample Cross-Ventilation</text>
  <!-- Feeders & Drinkers Suspended -->
  <rect x="90" y="70" width="25" height="20" fill="#facc15"/>
  <text x="102" y="83" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle">Feed</text>
  <circle cx="280" cy="80" r="10" fill="#0284c7"/>
  <text x="280" y="83" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">H2O</text>
  <!-- Deep Litter Layer on Floor -->
  <rect x="50" y="100" width="300" height="40" fill="#78350f" stroke="#d97706" stroke-width="2"/>
  <text x="200" y="122" fill="#fef08a" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">DEEP LITTER LAYER (5-10 cm dry sawdust / rice husk)</text>
  <!-- Floor base -->
  <rect x="50" y="140" width="300" height="20" fill="#334155"/>
  <text x="200" y="153" fill="#94a3b8" font-size="8" font-family="sans-serif" text-anchor="middle">Dry Concrete Floor Base</text>
  <!-- Sanitation benefits -->
  <text x="200" y="178" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Absorbs manure moisture -> Microbes ferment droppings -> Hygienic, warm & odor-free!</text>
</svg>
</div>
Why is maintaining a dry, well-stirred deep litter layer (such as rice husk or sawdust) critical in commercial broiler management?""",
     ["It absorbs moisture from poultry droppings, insulates birds from the cold floor, and prevents dampness that fosters coccidiosis and foot-pad dermatitis",
      "It serves as the sole food source for broiler chickens",
      "It prevents broiler chickens from gaining body weight",
      "It turns chicken feathers into raw silk thread"],
     "A", "OSC", "easy",
     "Wet manure generates toxic ammonia gas and fosters parasitic coccidia and bacterial foot lesions; a dry organic deep litter layer aerates the floor, absorbs excreta, and maintains sanitary conditions."),

    # 79: Induced Breeding Spawning Pool in Fish Hatcheries
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Circular Spawning Tank -->
  <ellipse cx="140" cy="100" rx="100" ry="60" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
  <ellipse cx="140" cy="100" rx="70" ry="40" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Water inlet creating circular flow -->
  <path d="M 60 70 A 90 50 0 0 1 220 70" stroke="#facc15" stroke-width="3" fill="none" stroke-dasharray="6"/>
  <text x="140" y="95" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Simulated River Current</text>
  <text x="140" y="110" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">(Continuous Water Shower)</text>
  <!-- Fish swimming in current -->
  <ellipse cx="100" cy="115" rx="16" ry="6" fill="#f8fafc"/>
  <ellipse cx="180" cy="85" rx="16" ry="6" fill="#f8fafc"/>
  <!-- Side Protocol Box -->
  <rect x="255" y="25" width="130" height="145" rx="5" fill="#18181b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="320" y="45" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">INDUCED BREEDING STEPS:</text>
  <text x="265" y="65" fill="#cbd5e1" font-size="8" font-family="sans-serif">1. Select mature brooders</text>
  <text x="265" y="80" fill="#cbd5e1" font-size="8" font-family="sans-serif">   (Male:Female = 2:1)</text>
  <text x="265" y="98" fill="#facc15" font-size="8" font-family="sans-serif">2. Inject Pituitary Extract</text>
  <text x="265" y="112" fill="#facc15" font-size="8" font-family="sans-serif">   or synthetic Ovaprim</text>
  <text x="265" y="130" fill="#38bdf8" font-size="8" font-family="sans-serif">3. Shower simulates monsoon</text>
  <text x="265" y="148" fill="#86efac" font-size="8" font-family="sans-serif">4. Synchronized spawning!</text>
</svg>
</div>
How does induced breeding technology overcome the major bottleneck of Indian major carps failing to spawn in stagnant pond waters?""",
     ["Hormonal injections (pituitary extract or Ovaprim) coupled with flowing water currents simulate natural monsoon river environments, triggering synchronized ovulation and fertilization",
      "It freezes the fish eggs so they do not drown in water",
      "It genetically modifies fish to lay eggs on dry grass",
      "It uses electric shocks to force fish to reproduce"],
     "A", "OSC", "medium",
     "Indian carps naturally breed only in turbulent monsoon-flooded rivers; injecting gonadotropic hormones (pituitary extract or Ovaprim) in circular eco-hatcheries with running water mimics river currents, inducing complete, synchronized egg release."),

    # 80: Silk Reeling from Softened Cocoons
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Hot Water Basin -->
  <rect x="40" y="80" width="120" height="70" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="105" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hot Water Basin (90-95°C)</text>
  <text x="100" y="120" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Softens Sericin Gum</text>
  <!-- Cocoons floating in basin -->
  <ellipse cx="65" cy="135" rx="10" ry="7" fill="#fef08a"/>
  <ellipse cx="90" cy="140" rx="10" ry="7" fill="#fef08a"/>
  <ellipse cx="115" cy="135" rx="10" ry="7" fill="#fef08a"/>
  <ellipse cx="135" cy="140" rx="10" ry="7" fill="#fef08a"/>
  <!-- Silk Filaments rising -->
  <line x1="65" y1="128" x2="190" y2="60" stroke="#fef08a" stroke-width="1"/>
  <line x1="90" y1="133" x2="190" y2="60" stroke="#fef08a" stroke-width="1"/>
  <line x1="115" y1="128" x2="190" y2="60" stroke="#fef08a" stroke-width="1"/>
  <line x1="135" y1="133" x2="190" y2="60" stroke="#fef08a" stroke-width="1"/>
  <!-- Gathering Eyelet Guide -->
  <circle cx="190" cy="60" r="6" fill="#f43f5e"/>
  <text x="190" y="48" fill="#f43f5e" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Twisting Eyelet</text>
  <!-- Composite Silk Thread to Reel -->
  <line x1="196" y1="60" x2="290" y2="85" stroke="#facc15" stroke-width="3"/>
  <!-- Rotating Reel -->
  <circle cx="310" cy="95" r="30" fill="none" stroke="#eab308" stroke-width="4"/>
  <line x1="280" y1="95" x2="340" y2="95" stroke="#eab308" stroke-width="2"/>
  <line x1="310" y1="65" x2="310" y2="125" stroke="#eab308" stroke-width="2"/>
  <text x="310" y="145" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Reeling Wheel</text>
  <text x="310" y="160" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Single Raw Silk Thread</text>
  <!-- Bottom info -->
  <text x="200" y="180" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">8-10 cocoon baves twisted together = Uniform commercial raw silk yarn</text>
</svg>
</div>
Why must individual filaments from 6 to 10 softened cocoons be gathered and reeled together into a single composite thread?""",
     ["A single cocoon silk filament (bave) is too delicate and microscopic to be woven directly; combining multiple strands creates a strong, uniform commercial yarn",
      "To change the color of the silk thread from white to blue",
      "Because cocoons cannot be opened one by one",
      "To prevent the silk thread from melting at room temperature"],
     "A", "OSC", "easy",
     "A single silkworm bave has a diameter of only ~10-15 microns and breaks easily under mechanical loom tension; uniting 6 to 10 filaments through an eyelet fuses their softening sericin coats into one strong commercial thread."),

    # 81: Agri-tourism Farm Value Chain
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Traditional Agriculture (Left) -->
  <rect x="20" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="102" y="48" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">TRADITIONAL MONOCULTURE</text>
  <text x="102" y="70" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Vulnerable to market price crashes</text>
  <text x="102" y="90" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Vulnerable to drought / unseasonal rain</text>
  <text x="102" y="110" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- High middleman profit deduction</text>
  <text x="102" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Single annual seasonal income</text>
  <text x="102" y="150" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">High Financial Risk</text>
  <!-- Agri-Tourism Diversification (Right) -->
  <rect x="215" y="25" width="165" height="140" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="297" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">AGRI-TOURISM MODEL</text>
  <text x="297" y="70" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Direct farm-gate produce sales</text>
  <text x="297" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Year-round hospitality & tour income</text>
  <text x="297" y="110" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Zero middleman commission loss</text>
  <text x="297" y="130" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">- Employment for village youth</text>
  <text x="297" y="150" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Resilient Rural Enterprise!</text>
</svg>
</div>
How does establishing an Agri-tourism venture insulate rural farming households against unexpected climate shocks and crop failure?""",
     ["Hospitality revenues, guided tours, and direct-to-consumer farm sales generate continuous non-crop secondary cash flow independent of erratic weather",
      "Agri-tourism stops rain from falling on the farm",
      "It requires farmers to abandon all agricultural fields completely",
      "It replaces farm crops with plastic decorative statues"],
     "A", "OSC", "easy",
     "Monoculture exposes farmers to devastating single-point harvest failures; agri-tourism provides dependable non-farm tertiary income via rustic accommodations, rural culinary experiences, and on-farm produce sales that cushion climate hazards."),

    # 82: Edible vs Poisonous Mushroom Recognition
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Safe Edible Mushroom -->
  <rect x="25" y="20" width="165" height="150" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="42" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">SAFE EDIBLE MUSHROOMS</text>
  <text x="107" y="60" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Cultivated in hygienic compost</text>
  <text x="107" y="80" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Agaricus bisporus (Button)</text>
  <text x="107" y="98" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pleurotus (Oyster / Dhingri)</text>
  <text x="107" y="116" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Volvariella (Paddy straw)</text>
  <text x="107" y="140" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">High protein, zero toxins</text>
  <text x="107" y="155" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Safe for human consumption!</text>
  <!-- Poisonous Toadstool -->
  <rect x="210" y="20" width="165" height="150" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  <text x="292" y="42" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">DEADLY POISONOUS TOADSTOOLS</text>
  <text x="292" y="60" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Wild unverified forest mushrooms</text>
  <text x="292" y="80" fill="#fecaca" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Amanita phalloides (Death Cap)</text>
  <text x="292" y="98" fill="#fecaca" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Amanita muscaria (Fly Agaric)</text>
  <text x="292" y="120" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Contain amatoxins & phallotoxins</text>
  <text x="292" y="140" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle">Causes fatal liver/kidney failure!</text>
  <text x="292" y="155" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">NEVER collect wild mushrooms!</text>
</svg>
</div>
Why is it strictly warned that amateur individuals should NEVER collect and consume wild mushrooms gathered from forest floors?""",
     ["Many wild toadstools (like Amanita phalloides) closely resemble edible mushrooms but contain deadly heat-stable amatoxins that cause fatal hepatic and renal failure",
      "Wild mushrooms taste like salty rocks",
      "Wild mushrooms will turn into snakes when boiled",
      "Forest mushrooms are made of solid wood"],
     "A", "OSC", "easy",
     "Species of genus Amanita synthesize bicyclic octapeptide amatoxins that inhibit RNA polymerase II, leading to irreversible liver and kidney necrosis with high fatality rates; only certified cultivated mushrooms should be eaten.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch17_topic3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
