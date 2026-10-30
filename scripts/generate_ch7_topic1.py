# scripts/generate_ch7_topic1.py
# Topic: MH-9-SCIT-7-7.1 (Food Chain, Food Web & Trophic Levels)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-7-7.1"
CHAPTER_NUM = 7

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Ecosystem Components & Producers/Consumers
    ("What is an 'ecosystem' in ecological science?",
     ["Only the plants living in a greenhouse", "A dynamic structural and functional unit consisting of a community of living organisms interacting with their physical non-living environment", "Only the wild animals in a zoo", "A laboratory test-tube of bacteria"],
     "B", "OSC", "easy",
     "- An ecosystem consists of biotic (living) and abiotic (physical) components continually interacting through nutrient cycles and energy flows.\nCorrect Choice is (B)."),

    ("Which organisms in an ecosystem are termed 'Producers' (Autotrophs)?",
     ["Fungi and bacteria that rot wood", "Green plants, algae, and photosynthetic bacteria that convert solar radiant energy into chemical energy", "Herbivorous cattle", "Carnivorous lions"],
     "B", "OSC", "easy",
     "- Producers are photosynthetic organisms that synthesize glucose and organic nutrients from carbon dioxide and water using sunlight.\nCorrect Choice is (B)."),

    ("What percentage of total incident solar radiant energy reaching the Earth is captured by green plants via photosynthesis?",
     ["About 50% to 75%", "Roughly 1% to 2%", "Exactly 100%", "Around 25%"],
     "B", "OSC", "medium",
     "- Green plants capture only about 1-2% of incident solar energy, converting it into chemical food energy.\nCorrect Choice is (B)."),

    ("Organisms that directly consume green plants for sustenance are classified as:",
     ["Tertiary consumers", "Primary consumers (Herbivores)", "Apex predators", "Decomposers"],
     "B", "OSC", "easy",
     "- Primary consumers (herbivores like deer, grasshoppers, cows) feed directly on producers.\nCorrect Choice is (B)."),

    ("Which of the following animals is a quintessential Primary Consumer (Herbivore)?",
     ["Frog", "Grasshopper", "Hawk", "Snake"],
     "B", "OSC", "easy",
     "- Grasshoppers feed directly on grasses and green foliage, making them primary consumers.\nCorrect Choice is (B)."),

    ("Animals that prey upon and eat primary consumers (herbivores) are called:",
     ["Autotrophs", "Secondary consumers (Carnivores)", "Decomposers", "Producers"],
     "B", "OSC", "easy",
     "- Secondary consumers (such as frogs, wolves, and insectivorous birds) feed upon herbivores.\nCorrect Choice is (B)."),

    ("A top carnivore that preys upon secondary consumers and is not hunted by any other predator in its habitat is called an:",
     ["Omnivore", "Apex / Tertiary consumer", "Herbivore", "Autotroph"],
     "B", "OSC", "easy",
     "- Apex consumers (such as tigers, lions, and eagles) occupy the top tier of food chains and have no natural predators.\nCorrect Choice is (B)."),

    ("Organisms like humans, crows, and bears that eat both plant products and animal flesh are termed:",
     ["Herbivores", "Omnivores", "Carnivores", "Detritivores only"],
     "B", "OSC", "easy",
     "- Omnivores consume both plant and animal matter across multiple trophic tiers.\nCorrect Choice is (B)."),

    ("What crucial role do 'Decomposers' (microbes like bacteria and saprophytic fungi) perform in an ecosystem?",
     ["They hunt apex predators", "They break down complex organic remains of dead plants and animals into simple inorganic minerals, returning them to soil and air", "They block solar light", "They turn water into rock"],
     "B", "OSC", "easy",
     "- Decomposers perform mineral recycling, returning essential elements (C, N, P) to abiotic reservoirs for re-absorption by plant roots.\nCorrect Choice is (B)."),

    ("What is a 'Food Chain'?",
     ["A metal chain used to tie cattle", "A linear sequence of organisms in an ecosystem through which food energy is transferred as one organism eats another", "A recipe book in a kitchen", "A list of endangered animals"],
     "B", "OSC", "easy",
     "- A food chain represents the straight feeding pathway of energy transfer from producers to successive consumers.\nCorrect Choice is (B)."),

    # 11-20: Trophic Levels & Feeding Networks
    ("Each feeding step or nutritive stage in a food chain is designated as a:",
     ["Taxon", "Trophic level", "Clade", "Niche only"],
     "B", "OSC", "easy",
     "- Each step in a food chain where transfer of food and energy occurs is called a trophic level (T1, T2, T3, etc.).\nCorrect Choice is (B)."),

    ("Which trophic level is always occupied exclusively by autotrophic green plants and algae?",
     ["Second trophic level (T₂)", "First trophic level (T₁)", "Third trophic level (T₃)", "Fourth trophic level (T₄)"],
     "B", "OSC", "easy",
     "- Producers form the foundational base of every ecosystem at the first trophic level (T1).\nCorrect Choice is (B)."),

    ("Primary consumers (herbivores) occupy which trophic level?",
     ["First trophic level (T₁)", "Second trophic level (T₂)", "Third trophic level (T₃)", "Fourth trophic level (T₄)"],
     "B", "OSC", "easy",
     "- Herbivores feeding directly on producers constitute the second trophic level (T2).\nCorrect Choice is (B)."),

    ("Secondary consumers (carnivores like a frog that eats grasshoppers) occupy which trophic level?",
     ["First trophic level (T₁)", "Second trophic level (T₂)", "Third trophic level (T₃)", "Fourth trophic level (T₄)"],
     "C", "OSC", "easy",
     "- Carnivores preying on herbivores occupy the third trophic level (T3).\nCorrect Choice is (C)."),

    ("Consider the food chain: Grass → Grasshopper → Frog → Snake → Hawk. Which organism occupies the fourth trophic level (T₄)?",
     ["Grasshopper", "Frog", "Snake", "Hawk"],
     "C", "OSC", "medium",
     "- T1 = Grass, T2 = Grasshopper, T3 = Frog, T4 = Snake, T5 = Hawk. The fourth trophic level is Snake.\nCorrect Choice is (C)."),

    ("What is an interconnected network of multiple overlapping food chains within an ecological community called?",
     ["Food circle", "Food web", "Linear chain", "Biomass loop"],
     "B", "OSC", "easy",
     "- A complex, interconnected network of food chains is called a food web.\nCorrect Choice is (B)."),

    ("Why is a complex 'Food Web' ecologically more resilient and stable than a single, isolated linear 'Food Chain'?",
     ["Because animals sleep more in a web", "Because organisms have multiple alternate food sources; if one prey species declines, predators can switch to alternatives without collapsing the system", "Because food webs produce more rain", "Because all predators become herbivores"],
     "B", "OSC", "medium",
     "- A food web provides dietary flexibility and alternative pathways, buffering the ecosystem against local extinctions.\nCorrect Choice is (B)."),

    ("In an aquatic pond ecosystem, the microscopic floating photosynthetic algae that act as primary producers are termed:",
     ["Zooplankton", "Phytoplankton", "Nekton", "Benthos"],
     "B", "OSC", "easy",
     "- Phytoplankton (diatoms, micro-algae) are the microscopic photosynthetic autotrophs powering aquatic food chains.\nCorrect Choice is (B)."),

    ("In an aquatic pond food chain, microscopic protozoans and tiny crustaceans that feed on phytoplankton are classified as:",
     ["Producers", "Primary consumers (Zooplankton)", "Top carnivores", "Decomposers"],
     "B", "OSC", "easy",
     "- Zooplankton are tiny floating animals that graze on phytoplankton, functioning as primary consumers.\nCorrect Choice is (B)."),

    ("Consider the pond food chain: Phytoplankton → Zooplankton → Small fish → Large fish → Fish eagle. Which organism occupies the third trophic level (T₃)?",
     ["Phytoplankton", "Zooplankton", "Small fish", "Large fish"],
     "C", "OSC", "medium",
     "- T1 = Phytoplankton, T2 = Zooplankton, T3 = Small fish, T4 = Large fish, T5 = Fish eagle.\nCorrect Choice is (C)."),

    # 21-30: Functional Interactions & Dynamics
    ("What happens to an ecosystem if all decomposers (bacteria and fungi) are completely eliminated?",
     ["Plants grow ten times larger", "Dead plant matter and animal corpses accumulate indefinitely, soil mineral reserves are exhausted, and nutrient cycling halts, leading to ecosystem collapse", "Herbivores turn into carnivores", "Solar energy stops reaching the Earth"],
     "B", "OSC", "medium",
     "- Without decomposers, bio-elements remain locked inside organic carcasses, starving primary producers of soil minerals.\nCorrect Choice is (B)."),

    ("State whether True or False: In a natural ecosystem, a single animal species can occupy more than one trophic level simultaneously in different food chains.",
     ["True", "False"],
     "A", "OTF", "medium",
     "- True. An omnivore like a human is a primary consumer (T2) when eating rice/fruits, and a secondary consumer (T3) when eating fish.\nCorrect Choice is (A)."),

    ("What type of food chain begins with dead organic decaying matter and passes energy to detritivore microbes and worms?",
     ["Grazing food chain", "Detritus food chain", "Parasitic food chain", "Solar food chain"],
     "B", "OSC", "medium",
     "- The detritus food chain starts from dead organic matter (detritus) utilized by detritivores and saprophytes.\nCorrect Choice is (B)."),

    ("A grazing food chain always directly derives its initial energy source from:",
     ["Dead carcasses", "Living green plants utilizing sunlight", "Geothermal vents", "Wind energy"],
     "B", "OSC", "easy",
     "- A grazing food chain starts with living autotrophic plants feeding herbivores.\nCorrect Choice is (B)."),

    ("Which of the following animals acts as a 'scavenger', consuming animals that are already dead rather than hunting live prey?",
     ["Tiger", "Vulture", "Cheetah", "Deer"],
     "B", "OSC", "easy",
     "- Vultures, hyenas, and crows consume dead carrion, serving as important ecological cleaners.\nCorrect Choice is (B)."),

    ("Assertion (A): In any stable ecosystem, the population of producers (plants) is far larger than the population of apex carnivores (tigers).\nReason (R): Energy is progressively lost as metabolic heat at each successive trophic transfer, supporting a progressively smaller biomass of top carnivores.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "- Massive energy dissipation at each trophic tier restricts the number of viable top carnivores an ecosystem can sustain.\nCorrect Choice is (A)."),

    ("Assertion (A): A food web is composed of multiple linear food chains linked together.\nReason (R): Most animals in nature feed on a single exclusive prey species and starve if it disappears.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "C", "OAR", "medium",
     "- (A) is true, but (R) is false; most consumers are polyphagous and feed on several alternate prey species.\nCorrect Choice is (C)."),

    ("Which of the following represents an abiotic component of a forest ecosystem?",
     ["Oak trees", "Earthworms", "Soil pH, minerals, sunlight, and rainfall", "Rabbits"],
     "C", "OSC", "easy",
     "- Soil chemistry, sunlight, temperature, and moisture are abiotic (non-living physical/chemical) factors.\nCorrect Choice is (C)."),

    ("What ecological term describes the functional role and physical position that a particular species occupies in its ecosystem community?",
     ["Habitat", "Ecological niche", "Biome", "Biosphere"],
     "B", "OSC", "medium",
     "- An ecological niche encompasses an organism's functional role, diet, activities, and interactions in its community.\nCorrect Choice is (B)."),

    ("In an agricultural field ecosystem, grasshoppers eat maize plants, and sparrows eat the grasshoppers. If farmers spray chemical pesticide that kills all grasshoppers, what immediate effect occurs?",
     ["Maize plants die immediately", "Sparrows lose their direct food source, while the maize crop is spared from insect grazing", "Frogs become producers", "Rainfall stops"],
     "B", "OSC", "medium",
     "- Removing the herbivore spares the plant host initially but starves secondary insectivorous consumers.\nCorrect Choice is (B)."),

    # 31-40: Special Concepts & Classification
    ("Why are food chains in nature typically limited to only 4 or 5 trophic levels?",
     ["Because larger animals become bored", "Because so much energy is dissipated as metabolic respiration heat at each link that insufficient energy remains to support a viable sixth level", "Because the Earth's gravity stops them", "Because predators refuse to eat after 5 PM"],
     "B", "OSC", "medium",
     "- By the 4th or 5th level, remaining available energy is too minuscule to support the reproductive biomass of another predator tier.\nCorrect Choice is (B)."),

    ("Which organism in the following list represents an Apex Consumer that cannot be preyed upon by any other wild animal in India?",
     ["Spotted deer", "Bengal Tiger", "Peacock", "Hare"],
     "B", "OSC", "easy",
     "- The Bengal Tiger sits at the apex of Indian terrestrial food webs with no natural predators.\nCorrect Choice is (B)."),

    ("Earthworms are classified ecologically as:",
     ["Producers", "Detritivores (consumers of decaying organic matter and humus)", "Apex carnivores", "Parasites of trees"],
     "B", "OSC", "easy",
     "- Earthworms ingest soil organic matter and rotting leaves, acting as essential detritivores.\nCorrect Choice is (B)."),

    ("In an ocean food chain: Micro-algae → Krill → Baleen Whale. What trophic level does the giant Baleen Whale occupy?",
     ["First trophic level (T₁)", "Second trophic level (T₂)", "Third trophic level (T₃)", "Fifth trophic level (T₅)"],
     "C", "OSC", "medium",
     "- T1 = Micro-algae, T2 = Krill (herbivore), T3 = Baleen Whale (carnivore feeding on zooplankton krill).\nCorrect Choice is (C)."),

    ("Which of the following represents a correct sequential food chain?",
     ["Frog → Snake → Grass → Grasshopper",
      "Grass → Grasshopper → Frog → Snake → Eagle",
      "Eagle → Snake → Frog → Grasshopper → Grass",
      "Grasshopper → Grass → Frog → Eagle"],
     "B", "OSC", "easy",
     "- Energy flows linearly from Producer (Grass) → Herbivore (Grasshopper) → Primary Carnivore (Frog) → Secondary Carnivore (Snake) → Apex (Eagle).\nCorrect Choice is (B)."),

    ("Identify the odd one out with respect to trophic position: Cow, Deer, Rabbit, Wolf.",
     ["Cow", "Deer", "Rabbit", "Wolf"],
     "D", "OSC", "easy",
     "- Wolf is a carnivore (secondary consumer); Cow, Deer, and Rabbit are herbivores (primary consumers).\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to ecosystem roles: Mushroom, Bread mould, Nitrogen-fixing bacteria, Green fern.",
     ["Mushroom", "Bread mould", "Nitrogen-fixing bacteria", "Green fern"],
     "D", "OSC", "easy",
     "- Green fern is a photosynthetic autotrophic producer; fungi and bacteria function as decomposers/saprophytes.\nCorrect Choice is (D)."),

    ("State whether True or False: Energy flows in a cyclic, recirculating manner in an ecosystem just like water and carbon.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Energy flow is strictly UNIDIRECTIONAL and non-cyclic; once dissipated as heat, it can never be reused by plants.\nCorrect Choice is (B)."),

    ("What type of organism forms the vital link connecting the biotic living world back to the abiotic chemical world?",
     ["Herbivores", "Decomposers", "Carnivores", "Parasites"],
     "B", "OSC", "easy",
     "- Decomposers mineralize organic matter into inorganic nitrates, phosphates, and CO2, bridging living and non-living realms.\nCorrect Choice is (B)."),

    ("In an ecosystem, what term denotes the total dry organic mass of living organisms present per unit area at a given trophic level at any particular time?",
     ["Gross primary productivity", "Standing crop (Biomass)", "Net trophic yield", "Ecological footprint"],
     "B", "OSC", "hard",
     "- The standing crop represents the total dry mass of living organisms (biomass) present at a specific trophic level at a given time.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Trophic Connections & Classifications
    ("What is the primary ultimate source of energy for virtually all terrestrial and aquatic ecosystems on Earth?",
     ["Nuclear energy inside rocks", "Solar radiant energy from the Sun", "Fossil fuels", "Tidal currents"],
     "B", "OSC", "easy",
     "- Sunlight drives photosynthesis in autotrophic producers, fueling almost all ecosystems.\nCorrect Choice is (B)."),

    ("A caterpillar feeds on the green leaf of a cabbage plant. In this relationship, the caterpillar is functioning as a:",
     ["Producer", "Primary consumer (Herbivore)", "Secondary consumer", "Tertiary consumer"],
     "B", "OSC", "easy",
     "- The caterpillar directly ingests plant tissues, acting as a primary consumer.\nCorrect Choice is (B)."),

    ("A garden lizard spots the caterpillar and eats it. In this food chain, the lizard is acting as a:",
     ["Primary consumer", "Secondary consumer (Carnivore)", "Producer", "Decomposer"],
     "B", "OSC", "easy",
     "- Feeding on an insect herbivore places the lizard at the secondary consumer level.\nCorrect Choice is (B)."),

    ("A domestic cat catches and eats the lizard. What trophic level does the cat represent in this specific food chain?",
     ["First trophic level (T₁)", "Second trophic level (T₂)", "Third trophic level (T₃)", "Fourth trophic level (T₄)"],
     "D", "OSC", "medium",
     "- T1 = Cabbage, T2 = Caterpillar, T3 = Lizard, T4 = Cat.\nCorrect Choice is (D)."),

    ("State whether True or False: Fungi possess chlorophyll and can manufacture their own glucose through photosynthesis.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Fungi completely lack chlorophyll; they are heterotrophic saprophytes or parasites.\nCorrect Choice is (B)."),

    ("Which ecological term refers to organisms that feed on the freshly dead remains, garbage, and fallen leaf litter in forests?",
     ["Herbivores", "Detritivores", "Apex carnivores", "Autotrophs"],
     "B", "OSC", "easy",
     "- Detritivores (like woodlice, millipedes, and dung beetles) consume decaying detritus.\nCorrect Choice is (B)."),

    ("In a mangrove ecosystem, fallen mangrove leaves decaying in brackish water support crabs and shrimp, which are eaten by herons. This sequence represents a:",
     ["Grazing food chain", "Detritus food chain", "Parasitic food chain", "Solar food chain"],
     "B", "OSC", "medium",
     "- Chains beginning with dead organic debris (leaf litter) are detritus food chains.\nCorrect Choice is (B)."),

    ("Why does the removal of a top predator (like a wolf or tiger) frequently trigger catastrophic degradation of the local forest habitat?",
     ["Because trees become lonely", "Because herbivore populations (like deer) explode uncontrollably, leading to severe overgrazing, loss of saplings, soil erosion, and ecosystem breakdown", "Because wolves plant new trees", "Because tigers stop forest fires"],
     "B", "OSC", "medium",
     "- Top predators exert top-down population control on herbivores, maintaining plant biodiversity and soil stability.\nCorrect Choice is (B)."),

    ("An organism that consumes only insects is specifically known as an:",
     ["Herbivore", "Insectivore", "Frugivore", "Sanguinivore"],
     "B", "OSC", "easy",
     "- An insectivore feeds specifically on insects.\nCorrect Choice is (B)."),

    ("Which of the following birds is a dedicated scavenger that feeds on animal carcasses without hunting?",
     ["Sparrow", "Vulture", "Hummingbird", "Parrot"],
     "B", "OSC", "easy",
     "- Vultures have specialized digestive systems capable of breaking down decomposing carrion.\nCorrect Choice is (B)."),

    # 51-60: Ecosystem Stability & Trophic Dynamics
    ("In a grassland food web, if a fungal blight destroys 80% of the grasshoppers, why do the insect-eating birds not immediately die out?",
     ["They hibernate for 10 years", "Because in a complex food web, birds can switch to eating beetles, caterpillars, and seeds", "Because birds can make food from air", "Because grasshoppers regrow within 1 hour"],
     "B", "OSC", "medium",
     "- Web interconnectedness offers dietary alternatives that prevent catastrophic starvation.\nCorrect Choice is (B)."),

    ("What happens to the chemical energy stored in plant biomass when a cow digests grass?",
     ["100% of it becomes cow muscle", "Most of the energy is lost as metabolic heat, respiration, and undigested dung, with only ~10% converted into new cow biomass", "Energy multiplies by 10", "All energy turns into light"],
     "B", "OSC", "medium",
     "- According to the second law of thermodynamics, energy conversion is inefficient; ~90% is dissipated as heat and bodily maintenance.\nCorrect Choice is (B)."),

    ("Which of the following is an example of an artificial, man-made ecosystem?",
     ["Pond", "Crop field / Aquarium", "Forest", "Desert"],
     "B", "OSC", "easy",
     "- Agricultural crop fields and aquaria are artificial ecosystems maintained by human interventions.\nCorrect Choice is (B)."),

    ("In an ecosystem, the non-living chemical and physical factors such as temperature, light, water, and soil minerals are collectively called:",
     ["Biotic components", "Abiotic components", "Trophic components", "Detrital components"],
     "B", "OSC", "easy",
     "- Abiotic components encompass the physical and chemical environment.\nCorrect Choice is (B)."),

    ("What type of organism consumes decaying leaf litter and excretes rich mineral humus, often dubbed 'the farmer's best friend'?",
     ["Tapeworm", "Earthworm", "Mosquito", "Termite"],
     "B", "OSC", "easy",
     "- Earthworms aerate the soil and convert decaying matter into nutrient-rich vermicompost.\nCorrect Choice is (B)."),

    ("Fill in the blank: In an ecological food chain, the arrow pointing from Grass to Zebra (Grass ➔ Zebra) signifies the direction of _______ transfer.",
     ["Water", "Energy and biomass", "Soil", "Oxygen"],
     "B", "OFB", "easy",
     "- Arrows in food chains depict the directional flow of food energy from organism consumed to consumer.\nCorrect Choice is (B)."),

    ("Which of the following is a tertiary consumer in an ocean ecosystem?",
     ["Diatom algae", "Copepod", "Sardine", "Killer whale (Orca) / Shark"],
     "D", "OSC", "easy",
     "- Sharks and killer whales occupy the highest consumer tiers in oceanic food webs.\nCorrect Choice is (D)."),

    ("State whether True or False: Decomposers operate at every single trophic level because all organisms eventually die.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Decomposers process carcasses and wastes originating from producers, primary consumers, secondary consumers, and apex predators alike.\nCorrect Choice is (A)."),

    ("What term describes a food web where every organism depends on a single narrow line of interaction?",
     ["A resilient web", "A fragile, low-diversity chain", "An evergreen forest", "A climax biome"],
     "B", "OSC", "medium",
     "- Low species diversity creates fragile dependency loops vulnerable to environmental shocks.\nCorrect Choice is (B)."),

    ("Which of the following organisms can occupy both the primary consumer level AND the secondary consumer level in human society?",
     ["A cow eating grass", "A human eating a salad (T₂) vs eating roast chicken (T₃)", "A tiger eating deer", "A cactus growing in desert"],
     "B", "OSC", "easy",
     "- Humans are omnivores whose trophic position shifts according to their meal composition.\nCorrect Choice is (B)."),

    # 61-70: Advanced Ecological Scenarios
    ("If an insecticide (like DDT) that cannot be metabolized is sprayed on a crop field, it concentrates progressively at higher trophic levels. This phenomenon is termed:",
     ["Eutrophication", "Biological magnification (Biomagnification)", "Photosynthesis", "Nitrogen fixation"],
     "B", "OSC", "hard",
     "- Biomagnification refers to the increasing concentration of persistent toxins in tissues at each successive trophic tier.\nCorrect Choice is (B)."),

    ("Assertion (A): In a food chain, apex carnivores are the most severely impacted by non-biodegradable pesticides like DDT.\nReason (R): Because of biomagnification, the pesticide concentration multiplies by thousands of times as it moves up successive trophic levels.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "- Non-biodegradable lipophilic toxins accumulate in fatty tissues, reaching peak lethal concentrations in top predators.\nCorrect Choice is (A)."),

    ("Assertion (A): Phytoplankton in a pond can be replaced by plastic balls without affecting fish.\nReason (R): Fish do not require organic calories from food.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "easy",
     "- Both statements are false. Phytoplankton synthesize essential chemical energy for the entire pond food web.\nCorrect Choice is (D)."),

    ("Identify the correct sequence representing a forest food chain:",
     ["Deer → Leaves → Tiger", "Trees (leaves) → Deer → Tiger", "Tiger → Deer → Trees", "Trees → Tiger → Deer"],
     "B", "OSC", "easy",
     "- Producer (Tree leaves) → Primary Consumer (Deer) → Secondary/Apex Consumer (Tiger).\nCorrect Choice is (B)."),

    ("Identify the odd one out with respect to feeding niche: Grasshopper, Deer, Elephant, Leopard.",
     ["Grasshopper", "Deer", "Elephant", "Leopard"],
     "D", "OSC", "easy",
     "- Leopard is a carnivore; Grasshopper, Deer, and Elephant are strict herbivores.\nCorrect Choice is (D)."),

    ("Which of the following organisms in an ecosystem has NO natural predators when fully grown?",
     ["Rabbit", "Frog", "Adult Lion / Tiger", "Sparrow"],
     "C", "OSC", "easy",
     "- Adult lions and tigers are apex predators with zero natural predators in their biomes.\nCorrect Choice is (C)."),

    ("What provides the continuous input of free energy that prevents an ecosystem from decaying into thermal equilibrium (maximum entropy)?",
     ["Rainwater", "Sunlight", "Wind", "Soil minerals"],
     "B", "OSC", "medium",
     "- Constant influx of solar energy counters entropic dissipation, driving biological order and life processes.\nCorrect Choice is (B)."),

    ("State whether True or False: Decomposers require sunlight to perform decomposition of dead leaves.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Decomposers are heterotrophs (fungi and bacteria); they operate efficiently in darkness inside soil and leaf litter.\nCorrect Choice is (B)."),

    ("Which trophic level contains the MAXIMUM total stored energy in any healthy natural ecosystem?",
     ["Producers (T₁)", "Primary consumers (T₂)", "Secondary consumers (T₃)", "Apex predators (T₄)"],
     "A", "OSC", "easy",
     "- Producers capture and contain the largest reservoir of energy; energy diminishes at every subsequent tier.\nCorrect Choice is (A)."),

    ("Which organism functions as an omnivorous scavenger in urban ecosystems, eating grain scraps as well as dead rodents?",
     ["Crow", "Koala", "Cow", "Deer"],
     "A", "OSC", "easy",
     "- Crows are adaptable omnivorous scavengers capable of feeding on plant refuse, insects, and carrion.\nCorrect Choice is (A).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Linear Food Chain with Trophic Levels
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="220" viewBox="0 0 370 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Grassland Food Chain & Trophic Levels</text>
  <!-- Step 1: Grass -->
  <rect x="15" y="55" width="70" height="95" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="32" y="75" fill="#34d399" font-size="11" font-weight="bold">T₁</text>
  <text x="28" y="95" fill="#ffffff" font-size="18">🌿</text>
  <text x="28" y="115" fill="#cbd5e1" font-size="9">Grass</text>
  <text x="20" y="135" fill="#34d399" font-size="8">Producer</text>
  <!-- Arrow 1 -->
  <text x="90" y="105" fill="#fde047" font-size="16">➔</text>
  <!-- Step 2: Grasshopper -->
  <rect x="105" y="55" width="70" height="95" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="122" y="75" fill="#facc15" font-size="11" font-weight="bold">T₂</text>
  <text x="120" y="95" fill="#ffffff" font-size="18">🦗</text>
  <text x="110" y="115" fill="#cbd5e1" font-size="8">Grasshopper</text>
  <text x="110" y="135" fill="#facc15" font-size="8">Herbivore</text>
  <!-- Arrow 2 -->
  <text x="180" y="105" fill="#fde047" font-size="16">➔</text>
  <!-- Step 3: Frog -->
  <rect x="195" y="55" width="70" height="95" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="212" y="75" fill="#38bdf8" font-size="11" font-weight="bold">T₃</text>
  <text x="212" y="95" fill="#ffffff" font-size="18">🐸</text>
  <text x="212" y="115" fill="#cbd5e1" font-size="9">Frog</text>
  <text x="202" y="135" fill="#38bdf8" font-size="8">Carnivore</text>
  <!-- Arrow 3 -->
  <text x="270" y="105" fill="#fde047" font-size="16">➔</text>
  <!-- Step 4: Snake / Hawk -->
  <rect x="285" y="55" width="70" height="95" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="302" y="75" fill="#f43f5e" font-size="11" font-weight="bold">T₄</text>
  <text x="302" y="95" fill="#ffffff" font-size="18">🦅</text>
  <text x="302" y="115" fill="#cbd5e1" font-size="9">Hawk</text>
  <text x="292" y="135" fill="#f43f5e" font-size="8">Apex</text>
  <!-- Sun -->
  <text x="15" y="185" fill="#fde047" font-size="10" font-weight="bold">☀️ Sun's Solar Energy</text>
  <text x="15" y="200" fill="#cbd5e1" font-size="9">Captured by T₁ and passed unidirectionally toward T₄</text>
</svg>
</div>
In the grassland food chain diagram above, what specific trophic category does the frog (T₃) represent?""",
     ["Primary Producer", "Primary Consumer (Herbivore)", "Secondary Consumer (Carnivore)", "Decomposer"],
     "C", "OSC", "easy",
     "- The frog feeds on the herbivorous grasshopper, placing it at the 3rd trophic level (T3) as a secondary consumer.\nCorrect Choice is (C)."),

    # 72: Complex Interconnected Food Web
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="90" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Forest Ecological Food Web</text>
  <!-- Producers at Bottom -->
  <rect x="40" y="170" width="110" height="30" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="50" y="190" fill="#34d399" font-size="10" font-weight="bold">🌿 Green Plants / Trees</text>
  <!-- Herbivores in Middle -->
  <rect x="20" y="105" width="85" height="30" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="32" y="125" fill="#facc15" font-size="9" font-weight="bold">🐇 Rabbit</text>
  <rect x="120" y="105" width="85" height="30" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="130" y="125" fill="#facc15" font-size="9" font-weight="bold">🦗 Insects</text>
  <rect x="220" y="105" width="85" height="30" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="235" y="125" fill="#facc15" font-size="9" font-weight="bold">🐁 Mice</text>
  <!-- Carnivores at Top -->
  <rect x="60" y="45" width="85" height="30" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="75" y="65" fill="#f87171" font-size="9" font-weight="bold">🦊 Fox</text>
  <rect x="200" y="45" width="85" height="30" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="215" y="65" fill="#f87171" font-size="9" font-weight="bold">🦉 Owl</text>
  <!-- Interconnected Lines -->
  <line x1="95" y1="170" x2="60" y2="135" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="95" y1="170" x2="160" y2="135" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="95" y1="170" x2="260" y2="135" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="60" y1="105" x2="100" y2="75" stroke="#facc15" stroke-width="1.5"/>
  <line x1="260" y1="105" x2="100" y2="75" stroke="#facc15" stroke-width="1.5"/>
  <line x1="260" y1="105" x2="240" y2="75" stroke="#facc15" stroke-width="1.5"/>
  <line x1="160" y1="105" x2="240" y2="75" stroke="#facc15" stroke-width="1.5"/>
  <text x="35" y="218" fill="#38bdf8" font-size="9.5">Multiple interlocking feeding paths confer high ecological stability</text>
</svg>
</div>
In the food web shown above, if a disease wipes out the mouse population, why can the owl survive without starving?""",
     ["Because owls can eat dirt",
      "Because the owl has alternative food sources, such as insects and small birds in the web",
      "Because owls can photosynthesize",
      "Because mice turn into rabbits"],
     "B", "OSC", "easy",
     "- Food web complexity provides alternative energy channels; predators shift to other prey when one prey species declines.\nCorrect Choice is (B)."),

    # 73: Decomposers & Mineral Recycling Loop
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Decomposers: The Ecological Recyclers</text>
  <!-- Living World Circle -->
  <rect x="25" y="50" width="135" height="70" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="10" font-weight="bold">BIOTIC COMMUNITY</text>
  <text x="35" y="88" fill="#cbd5e1" font-size="8.5">- Plants (Producers)</text>
  <text x="35" y="102" fill="#cbd5e1" font-size="8.5">- Animals (Consumers)</text>
  <!-- Death Arrow -->
  <path d="M 160,85 Q 230,85 230,120" stroke="#f87171" stroke-width="2" fill="none"/>
  <text x="175" y="80" fill="#fca5a5" font-size="8">Death & Waste</text>
  <!-- Decomposer Box -->
  <rect x="180" y="120" width="135" height="55" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="138" fill="#fbbf24" font-size="9.5" font-weight="bold">DECOMPOSERS 🍄</text>
  <text x="190" y="152" fill="#cbd5e1" font-size="8">Bacteria & Fungi</text>
  <text x="190" y="165" fill="#fde047" font-size="8">Mineralize organic matter</text>
  <!-- Recycled Arrow -->
  <path d="M 180,150 Q 80,180 80,120" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <text x="35" y="165" fill="#38bdf8" font-size="8">Inorganic nutrients (N, P, K)</text>
  <text x="35" y="178" fill="#38bdf8" font-size="8">returned to soil for roots</text>
  <text x="45" y="205" fill="#fde047" font-size="9.5">Nutrients cycle continuously, while energy flows unidirectionally</text>
</svg>
</div>
What would be the ultimate catastrophic consequence on Earth if all decomposers (bacteria and saprophytic fungi) suddenly vanished?""",
     ["Trees would grow taller",
      "Dead organic bodies and wastes would pile up indefinitely without decomposing, and plants would starve as soil minerals were exhausted",
      "Carnivores would become herbivores",
      "The sun would cool down"],
     "B", "OSC", "easy",
     "- Decomposers prevent biological gridlock by mineralizing dead matter and replenishing soil nutrient pools.\nCorrect Choice is (B)."),

    # 74: Aquatic Pond Food Chain
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Aquatic Pond Ecosystem Food Chain</text>
  <!-- Water Background -->
  <rect x="25" y="45" width="290" height="120" fill="#0c4a6e" opacity="0.6" rx="4"/>
  <!-- Phytoplankton -->
  <circle cx="65" cy="100" r="16" fill="#15803d" stroke="#22c55e"/>
  <text x="40" y="130" fill="#4ade80" font-size="8" font-weight="bold">Phytoplankton</text>
  <text x="50" y="142" fill="#cbd5e1" font-size="7">(Algae, T₁)</text>
  <text x="90" y="105" fill="#fde047" font-size="12">➔</text>
  <!-- Zooplankton -->
  <ellipse cx="125" cy="100" rx="14" ry="10" fill="#f59e0b"/>
  <text x="105" y="130" fill="#fbbf24" font-size="8" font-weight="bold">Zooplankton</text>
  <text x="110" y="142" fill="#cbd5e1" font-size="7">(Protozoa, T₂)</text>
  <text x="150" y="105" fill="#fde047" font-size="12">➔</text>
  <!-- Small Fish -->
  <path d="M 175,100 Q 190,90 205,100 L 215,90 L 215,110 Z" fill="#38bdf8"/>
  <text x="175" y="130" fill="#38bdf8" font-size="8" font-weight="bold">Small Fish</text>
  <text x="180" y="142" fill="#cbd5e1" font-size="7">(T₃)</text>
  <text x="225" y="105" fill="#fde047" font-size="12">➔</text>
  <!-- Large Fish / Heron -->
  <path d="M 255,100 Q 275,85 295,100 L 305,90 L 305,110 Z" fill="#f43f5e"/>
  <text x="255" y="130" fill="#f87171" font-size="8" font-weight="bold">Large Fish</text>
  <text x="265" y="142" fill="#cbd5e1" font-size="7">(T₄)</text>
  <text x="45" y="185" fill="#fde047" font-size="9.5">Phytoplankton synthesize 100% of organic food in open water</text>
</svg>
</div>
In an aquatic pond food chain, what role do microscopic floating organisms like Daphnia and Cyclops (Zooplankton) play?""",
     ["Autotrophic producers", "Primary consumers grazing on microscopic algae (phytoplankton)", "Apex predators", "Decomposers"],
     "B", "OSC", "easy",
     "- Zooplankton feed on microscopic phytoplankton, serving as the essential primary consumers of aquatic food webs.\nCorrect Choice is (B)."),

    # 75: Trophic Step Pyramid of Energy Loss
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Trophic Tier Energy Dissipation</text>
  <!-- Apex Tier (Top) -->
  <rect x="135" y="50" width="70" height="25" fill="#ef4444" rx="2"/>
  <text x="145" y="66" fill="#ffffff" font-size="9" font-weight="bold">Apex (T₄)</text>
  <!-- Secondary Tier -->
  <rect x="105" y="77" width="130" height="25" fill="#f59e0b" rx="2"/>
  <text x="125" y="93" fill="#ffffff" font-size="9" font-weight="bold">Carnivores (T₃)</text>
  <!-- Primary Tier -->
  <rect x="75" y="104" width="190" height="25" fill="#38bdf8" rx="2"/>
  <text x="120" y="120" fill="#ffffff" font-size="9" font-weight="bold">Herbivores (T₂)</text>
  <!-- Producers Base -->
  <rect x="45" y="131" width="250" height="25" fill="#10b981" rx="2"/>
  <text x="120" y="147" fill="#ffffff" font-size="9" font-weight="bold">Producers (T₁)</text>
  <!-- Dissipation annotation -->
  <text x="45" y="180" fill="#fde047" font-size="9.5">~90% of energy is lost as metabolic heat at every step</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="8.5">Only ~10% is incorporated into new biomass for the next tier</text>
</svg>
</div>
Why does the width of the trophic pyramid narrow dramatically from the broad producer base (T₁) to the narrow apex predator peak (T₄)?""",
     ["Because animals at higher levels are physically smaller",
      "Because ~90% of energy is lost as metabolic respiration heat at each transfer, leaving very little energy to sustain top tiers",
      "Because sunlight does not reach high levels",
      "Because top predators eat grass"],
     "B", "OSC", "easy",
     "- Progressive 90% energy loss at each step strictly limits the biomass and population size supported at higher trophic tiers.\nCorrect Choice is (B)."),

    # 76: Herbivore vs Carnivore Intestine Adaptations
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Digestive Adaptation to Trophic Diet</text>
  <!-- Herbivore (Long gut) -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="10" font-weight="bold">HERBIVORE (e.g. Cow)</text>
  <path d="M 45,95 Q 60,80 75,95 T 105,95 T 135,95 Q 120,115 105,115 T 75,115 T 45,115" stroke="#22c55e" stroke-width="3" fill="none"/>
  <text x="35" y="135" fill="#fde047" font-size="8.5">- Very LONG small intestine</text>
  <text x="35" y="148" fill="#cbd5e1" font-size="8">Allows time for bacteria to</text>
  <text x="35" y="160" fill="#cbd5e1" font-size="8">digest tough CELLULOSE</text>
  <!-- Carnivore (Short gut) -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="70" fill="#f87171" font-size="10" font-weight="bold">CARNIVORE (e.g. Tiger)</text>
  <line x1="200" y1="105" x2="295" y2="105" stroke="#f87171" stroke-width="4"/>
  <text x="190" y="135" fill="#fde047" font-size="8.5">- Much SHORTER intestine</text>
  <text x="190" y="148" fill="#cbd5e1" font-size="8">Meat is protein-rich and</text>
  <text x="190" y="160" fill="#cbd5e1" font-size="8">digests rapidly without fiber</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Anatomical evolution directly mirrors trophic food level</text>
</svg>
</div>
Why do herbivorous primary consumers (like cows and deer) possess a significantly longer small intestine than carnivores (like tigers and lions)?""",
     ["Because cows eat more salt",
      "Because plant cell walls contain tough cellulose fibers requiring extended transit time and symbiotic microbial fermentation to digest",
      "Because tigers drink no water",
      "Because meat turns into wood"],
     "B", "OSC", "medium",
     "- Cellulose digestion is slow and biochemically difficult, requiring an extended digestive tract housing symbiotic cellulose-fermenting microbes.\nCorrect Choice is (B)."),

    # 77: Detritus Food Chain (Fallen Litter to Soil)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">The Detritus Food Chain Sequence</text>
  <!-- Dead Leaves (Detritus) -->
  <rect x="25" y="55" width="85" height="45" fill="#1e293b" stroke="#ca8a04" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="9" font-weight="bold">Dead Litter</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8">(Fallen leaves)</text>
  <text x="115" y="80" fill="#38bdf8" font-size="14">➔</text>
  <!-- Earthworm (Detritivore) -->
  <rect x="135" y="55" width="85" height="45" fill="#1e293b" stroke="#f472b6" rx="4"/>
  <text x="142" y="75" fill="#f472b6" font-size="9" font-weight="bold">Earthworm 🪱</text>
  <text x="142" y="90" fill="#cbd5e1" font-size="8">(Detritivore)</text>
  <text x="225" y="80" fill="#38bdf8" font-size="14">➔</text>
  <!-- Robin / Bird (Carnivore) -->
  <rect x="245" y="55" width="70" height="45" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="255" y="75" fill="#38bdf8" font-size="9" font-weight="bold">Bird 🐦</text>
  <text x="252" y="90" fill="#cbd5e1" font-size="8">(Carnivore)</text>
  <!-- Annotation -->
  <rect x="35" y="125" width="270" height="60" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="45" y="145" fill="#34d399" font-size="9.5" font-weight="bold">Key Difference from Grazing Chain:</text>
  <text x="45" y="160" fill="#cbd5e1" font-size="8.5">- Grazing chain begins with LIVING plants</text>
  <text x="45" y="174" fill="#cbd5e1" font-size="8.5">- Detritus chain begins with DEAD organic matter</text>
</svg>
</div>
What is the primary starting energy substrate of a Detritus Food Chain compared to a standard Grazing Food Chain?""",
     ["Living green leaves (Grazing) vs Dead decaying organic matter (Detritus)",
      "Solar light (Detritus) vs Geothermal heat (Grazing)",
      "Fresh meat (Grazing) vs Plastic (Detritus)",
      "Pure rain (Detritus) vs River sand (Grazing)"],
     "A", "OSC", "easy",
     "- Grazing food chains initiate with living photosynthetic biomass; detritus food chains initiate with dead organic matter.\nCorrect Choice is (A)."),

    # 78: Keystone Predator Effect (Trophic Cascade)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Trophic Cascade (Keystone Apex Role)</text>
  <!-- Top Predator Present -->
  <rect x="25" y="50" width="135" height="125" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="68" fill="#34d399" font-size="9.5" font-weight="bold">TIGER PRESENT (Healthy)</text>
  <text x="35" y="88" fill="#cbd5e1" font-size="8.5">- Deer population controlled</text>
  <text x="35" y="102" fill="#cbd5e1" font-size="8.5">- Forest saplings survive</text>
  <text x="35" y="116" fill="#cbd5e1" font-size="8.5">- Rich soil, clean rivers</text>
  <text x="35" y="135" fill="#34d399" font-size="10" font-weight="bold">✓ High Biodiversity</text>
  <!-- Top Predator Extirpated -->
  <rect x="180" y="50" width="135" height="125" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="68" fill="#f87171" font-size="9.5" font-weight="bold">TIGER ABSENT (Disaster)</text>
  <text x="190" y="88" fill="#cbd5e1" font-size="8.5">- Deer population explodes</text>
  <text x="190" y="102" fill="#cbd5e1" font-size="8.5">- Severe overgrazing</text>
  <text x="190" y="116" fill="#cbd5e1" font-size="8.5">- Saplings eaten, erosion</text>
  <text x="190" y="135" fill="#f87171" font-size="10" font-weight="bold">✗ Forest Collapse</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Top predators regulate the entire structural architecture of habitats</text>
</svg>
</div>
In ecological science, an apex predator whose presence exerts top-down control over the entire ecosystem diversity (preventing collapse) is called a:""",
     ["Parasite", "Keystone species", "Secondary producer", "Invasive weed"],
     "B", "OSC", "medium",
     "- A keystone species (like the tiger or sea otter) plays an outsized role in structuring the entire community.\nCorrect Choice is (B)."),

    # 79: Biological Magnification (Biomagnification of Toxins)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Biomagnification of Toxic DDT</text>
  <!-- Level 1: Water -->
  <text x="35" y="55" fill="#38bdf8" font-size="8.5">Water: 0.000003 ppm DDT</text>
  <!-- Level 2: Zooplankton -->
  <text x="35" y="85" fill="#4ade80" font-size="8.5">Zooplankton: 0.04 ppm (13,000×)</text>
  <!-- Level 3: Small Fish -->
  <text x="35" y="115" fill="#facc15" font-size="8.5">Small Fish: 0.5 ppm (160,000×)</text>
  <!-- Level 4: Large Fish -->
  <text x="35" y="145" fill="#f97316" font-size="8.5">Large Fish: 2.0 ppm (660,000×)</text>
  <!-- Level 5: Fish-eating Bird -->
  <text x="35" y="175" fill="#ef4444" font-size="9" font-weight="bold">Fish-eating Eagle: 25.0 ppm (8,000,000×)</text>
  <!-- Side Red Bar -->
  <rect x="295" y="45" width="16" height="140" fill="#ef4444" rx="3"/>
  <text x="270" y="120" fill="#f87171" font-size="12">▲</text>
  <text x="45" y="200" fill="#fde047" font-size="9">Non-biodegradable chemicals concentrate at the highest trophic level</text>
</svg>
</div>
Why did top predatory raptor birds (like eagles and pelicans) lay fragile, thin-shelled eggs that broke before hatching during the heavy use of agricultural DDT?""",
     ["Because eagles ate less calcium",
      "Because DDT biomagnified to toxic levels at the apex trophic tier, interfering with calcium deposition in eggshells",
      "Because water became too cold",
      "Because birds stopped building nests"],
     "B", "OSC", "medium",
     "- Biomagnification results in apex predators carrying millions of times higher pesticide concentrations, disrupting eggshell calcification.\nCorrect Choice is (B)."),

    # 80: Omnivore Multiple Trophic Position
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Omnivore: Shifting Trophic Position</text>
  <!-- Scenario A: Human eating Rice -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="9.5" font-weight="bold">MEAL 1: Rice / Wheat 🌾</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- Plant (T₁)</text>
  <text x="35" y="105" fill="#fde047" font-size="8.5">➔ Human consumes directly</text>
  <text x="35" y="125" fill="#34d399" font-size="10" font-weight="bold">Human = T₂ Consumer</text>
  <text x="35" y="140" fill="#cbd5e1" font-size="8">(Primary Consumer / Herbivore)</text>
  <!-- Scenario B: Human eating Fish -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#60a5fa" rx="4"/>
  <text x="190" y="70" fill="#60a5fa" font-size="9.5" font-weight="bold">MEAL 2: Fish 🐟</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8.5">- Algae (T₁) ➔ Zoopl. (T₂)</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="8.5">➔ Fish (T₃) ➔ Human</text>
  <text x="190" y="125" fill="#60a5fa" font-size="10" font-weight="bold">Human = T₄ Consumer</text>
  <text x="190" y="140" fill="#cbd5e1" font-size="8">(Tertiary Consumer)</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Trophic level is a functional state, NOT a fixed taxonomic species tag</text>
</svg>
</div>
Based on the diagram, why can an omnivorous animal like a human or a bear occupy different trophic levels at different times?""",
     ["Because animals change their species",
      "Because trophic level is determined strictly by what the organism is actively eating in that specific food chain",
      "Because animals sleep at different heights",
      "Because humans can photosynthesize"],
     "B", "OSC", "easy",
     "- Trophic level reflects an organism's specific feeding position in a particular energy path, not an immutable taxonomic label.\nCorrect Choice is (B)."),

    # 81: Unidirectional Energy Flow vs Cyclic Nutrient Flow
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Energy Flow vs Nutrient Recycling</text>
  <!-- Energy: Linear & One-way -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="70" fill="#fbbf24" font-size="10" font-weight="bold">ENERGY FLOW</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- Sun ➔ Plant ➔ Animal</text>
  <text x="35" y="105" fill="#ef4444" font-size="8.5">- Lost as heat to space</text>
  <text x="35" y="125" fill="#fde047" font-size="9.5" font-weight="bold">STRICTLY ONE-WAY</text>
  <text x="35" y="140" fill="#cbd5e1" font-size="8">Never cycles back to Sun</text>
  <!-- Nutrients: Cyclic -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="70" fill="#34d399" font-size="10" font-weight="bold">NUTRIENT FLOW</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8.5">- Soil ➔ Plant ➔ Animal</text>
  <text x="190" y="105" fill="#34d399" font-size="8.5">- Decomposers ➔ Soil</text>
  <text x="190" y="125" fill="#34d399" font-size="9.5" font-weight="bold">CYCLIC & REUSED</text>
  <text x="190" y="140" fill="#cbd5e1" font-size="8">Reused for millions of yrs</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Thermodynamic rule: Energy dissipates; Matter is conserved</text>
</svg>
</div>
What is the fundamental thermodynamic difference between the flow of Energy and the flow of Minerals (Matter) in an ecosystem?""",
     ["Energy is recycled in cycles; minerals are lost to outer space",
      "Energy flow is strictly unidirectional (never cycles back); mineral matter cycles continuously between living and non-living realms",
      "Both energy and minerals flow in identical cycles",
      "Neither energy nor minerals move"],
     "B", "OSC", "easy",
     "- Energy is dissipated irreversibly as respiratory heat; nutrient elements (C, N, P) cycle indefinitely via biogeochemical loops.\nCorrect Choice is (B)."),

    # 82: Summary Diagnostic of Ecosystem Trophic Organization
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Ecosystem Trophic Architecture Summary</text>
  <!-- Tier 1 -->
  <rect x="25" y="45" width="310" height="30" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="35" y="64" fill="#34d399" font-size="9.5" font-weight="bold">Producers (T₁):</text>
  <text x="125" y="64" fill="#cbd5e1" font-size="9">Sunlight ➔ Photosynthesis (Green Plants / Algae)</text>
  <!-- Tier 2 -->
  <rect x="25" y="80" width="310" height="30" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="35" y="99" fill="#facc15" font-size="9.5" font-weight="bold">Herbivores (T₂):</text>
  <text x="125" y="99" fill="#cbd5e1" font-size="9">Primary Consumers (Cattle, Deer, Grasshoppers)</text>
  <!-- Tier 3 -->
  <rect x="25" y="115" width="310" height="30" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="35" y="134" fill="#38bdf8" font-size="9.5" font-weight="bold">Carnivores (T₃/T₄):</text>
  <text x="145" y="134" fill="#cbd5e1" font-size="9">Secondary & Apex Predators (Frogs, Wolves, Tigers)</text>
  <!-- Tier 4 -->
  <rect x="25" y="150" width="310" height="30" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="35" y="169" fill="#fbbf24" font-size="9.5" font-weight="bold">Decomposers:</text>
  <text x="125" y="169" fill="#cbd5e1" font-size="9">Recycle minerals from all dead tiers back to soil</text>
  <text x="45" y="205" fill="#38bdf8" font-size="9.5">Maintains the living biosphere in dynamic chemical equilibrium</text>
</svg>
</div>
Which group of organisms forms the fundamental biological foundation without which no consumers or predators could exist in any ecosystem?""",
     ["Herbivores", "Autotrophic Producers (Green Plants and Phytoplankton)", "Apex predators", "Scavengers"],
     "B", "OSC", "easy",
     "- Autotrophic producers are the sole organisms capable of harvesting external solar energy and converting it into organic food for all other living tiers.\nCorrect Choice is (B).")
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

out_file = "scripts/ch7_topic1.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
