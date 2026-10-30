# scripts/generate_ch7_topic2.py
# Topic: MH-9-SCIT-7-7.2 (The Energy Pyramid & Lindeman 10% Energy Rule)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-7-7.2"
CHAPTER_NUM = 7

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Ecological Pyramids & Lindeman 10% Rule
    ("Who introduced the graphical concept of ecological pyramids (of numbers, biomass, and energy) in 1927?",
     ["Charles Elton", "Raymond Lindeman", "Arthur Tansley", "Eugene Odum"],
     "A", "OSC", "easy",
     "- British ecologist Charles Elton first introduced the concept of ecological pyramids in 1927.\nCorrect Choice is (A)."),

    ("In 1942, which American ecologist formulated the famous 'Ten Percent Law' (10% Rule) of trophic energy transfer efficiency?",
     ["Raymond Lindeman", "Charles Darwin", "Gregor Mendel", "Robert Brown"],
     "A", "OSC", "easy",
     "- Raymond Lindeman formulated the 10% Law governing energy transfer efficiency between trophic levels in ecosystems.\nCorrect Choice is (A)."),

    ("According to Lindeman's 10% Law, approximately what fraction of the energy available at one trophic level is transferred and stored as biomass in the next higher trophic level?",
     ["Approximately 50%", "Approximately 10%", "Roughly 90%", "Nearly 100%"],
     "B", "OSC", "easy",
     "- Only about 10% of energy entering a trophic level is converted into new biomass available to the next consumer level.\nCorrect Choice is (B)."),

    ("What happens to the remaining ~90% of the energy consumed by an organism at a trophic level?",
     ["It is stored forever in bones", "It is dissipated into the environment as metabolic heat during cellular respiration, locomotion, excretion, and bodily maintenance", "It turns into nuclear energy", "It returns to the sun"],
     "B", "OSC", "easy",
     "- Around 90% of ingested energy is utilized for cellular respiration, work, and lost as non-recoverable low-grade heat.\nCorrect Choice is (B)."),

    ("If green plants (producers) in a forest capture 10,000 Joules of energy from sunlight, how much energy will be transferred to primary consumers (deer)?",
     ["10,000 J", "1,000 J", "100 J", "10 J"],
     "B", "OSC", "easy",
     "- Applying the 10% rule: \\(10,000\\text{ J} \\times 0.10 = 1,000\\text{ J}\\).\nCorrect Choice is (B)."),

    ("Continuing from the previous question, how much energy will reach the secondary consumers (wolves) that prey upon those deer?",
     ["1,000 J", "100 J", "10 J", "1 J"],
     "B", "OSC", "easy",
     "- Applying the 10% rule from deer (1,000 J): \\(1,000\\text{ J} \\times 0.10 = 100\\text{ J}\\).\nCorrect Choice is (B)."),

    ("How much energy will be available to an apex carnivore (tiger) that kills and eats the wolf?",
     ["100 J", "10 J", "1 J", "0.1 J"],
     "B", "OSC", "easy",
     "- Applying the 10% rule from wolf (100 J): \\(100\\text{ J} \\times 0.10 = 10\\text{ J}\\).\nCorrect Choice is (B)."),

    ("Can an ecological 'Pyramid of Energy' EVER be inverted (narrow at the bottom and broad at the top) in any natural ecosystem?",
     ["Yes, in marine ocean ecosystems", "Yes, in desert ecosystems", "No, a pyramid of energy is strictly and ALWAYS upright in all ecosystems", "Yes, during night time"],
     "C", "OSC", "medium",
     "- A pyramid of energy is ALWAYS upright because energy is unavoidably lost as heat at each successive trophic transition.\nCorrect Choice is (C)."),

    ("Why can food chains rarely support more than 4 or 5 trophic levels in nature?",
     ["Because animals run out of space", "Because so much energy is dissipated at each successive link that by the 5th level, residual energy is insufficient to sustain another predator population", "Because gravity increases at higher levels", "Because sunlight only reaches 4 animals"],
     "B", "OSC", "easy",
     "- Starting from 10,000 J, only 1 J remains at the 5th level, rendering a 6th level biologically unsustainable.\nCorrect Choice is (B)."),

    ("Which physical law of nature dictates that energy transfer between trophic levels is inherently inefficient and accompanied by heat dissipation?",
     ["Newton's Law of Universal Gravitation", "The Second Law of Thermodynamics (Law of Entropy)", "Coulomb's Law", "Hooke's Law"],
     "B", "OSC", "medium",
     "- The Second Law of Thermodynamics states that spontaneous energy transformations increase entropy, dissipating useful energy as heat.\nCorrect Choice is (B)."),

    # 11-20: Pyramid Types & Inversions
    ("What does a 'Pyramid of Numbers' represent?",
     ["The number of rainy days per year", "The total number of individual organisms present at each successive trophic level in an ecosystem", "The speed of animals", "The body mass of trees"],
     "B", "OSC", "easy",
     "- A pyramid of numbers shows the total population count of individuals at each trophic level.\nCorrect Choice is (B)."),

    ("In a grassland ecosystem, the Pyramid of Numbers is typically:",
     ["Inverted", "Upright (broad base of countless grass blades tapering to few hawks)", "Spindle-shaped", "Horizontal"],
     "B", "OSC", "easy",
     "- In grasslands, millions of grass plants support thousands of herbivores, hundreds of frogs, and few apex hawks (upright).\nCorrect Choice is (B)."),

    ("In a single large oak tree ecosystem, where one giant producer tree supports hundreds of herbivorous birds and thousands of insect parasites, the Pyramid of Numbers is:",
     ["Upright", "Inverted (narrow single base expanding to thousands at top)", "Spherical", "Completely flat"],
     "B", "OSC", "medium",
     "- A single giant tree (T1 = 1) supports numerous herbivores and parasites, producing an inverted pyramid of numbers.\nCorrect Choice is (B)."),

    ("What does a 'Pyramid of Biomass' represent?",
     ["The volume of water drunk", "The total dry weight of living organic matter (standing crop) present per unit area at each trophic level", "The temperature of animals", "The total area of leaves"],
     "B", "OSC", "easy",
     "- A pyramid of biomass graphically depicts the dry weight of organic matter at each trophic level.\nCorrect Choice is (B)."),

    ("In an open ocean aquatic ecosystem, the Pyramid of Biomass of the standing crop is often:",
     ["Always strictly upright", "Inverted (the biomass of microscopic phytoplankton at any moment is smaller than the biomass of long-lived zooplankton and fish)", "Square-shaped", "Zero"],
     "B", "OSC", "hard",
     "- Rapid reproduction and turnover of microscopic phytoplankton sustains a larger standing biomass of long-lived fish (inverted biomass pyramid).\nCorrect Choice is (B)."),

    ("Even though the open ocean biomass pyramid can be inverted, why is its ocean ENERGY pyramid still strictly upright?",
     ["Because fish produce energy", "Because the rate of energy production by fast-multiplying phytoplankton over time is enormously greater than the energy accumulated in fish", "Because ocean water has high voltage", "Because sunlight penetrates the seabed"],
     "B", "OSC", "hard",
     "- Phytoplankton have an extremely high turnover rate; cumulative energy produced over time always exceeds higher trophic tiers.\nCorrect Choice is (B)."),

    ("What is 'Gross Primary Productivity' (GPP)?",
     ["The total rate of solar energy converted into chemical biomass by producers through photosynthesis per unit area and time", "The energy lost in human factories", "The total oxygen inhaled by fish", "The rate of rock erosion"],
     "A", "OSC", "medium",
     "- GPP is the total rate at which photosynthetic autotrophs fix solar radiant energy into chemical bonds.\nCorrect Choice is (A)."),

    ("What is 'Net Primary Productivity' (NPP)?",
     ["GPP multiplied by 10", "The remaining biomass energy stored in producer tissues after deducting the energy consumed by the plant's own cellular respiration (NPP = GPP - R)", "Total water absorbed by soil", "The energy in moonlight"],
     "B", "OSC", "medium",
     "- Net Primary Productivity represents the actual biomass available for consumption by herbivores: \\(\\text{NPP} = \\text{GPP} - \\text{R}\\).\nCorrect Choice is (B)."),

    ("If an ecosystem has \\(\\text{GPP} = 20,000\\text{ kcal/m}^2/\\text{yr}\\) and plant respiration consumes \\(\\text{R} = 8,000\\text{ kcal/m}^2/\\text{yr}\\), what is the Net Primary Productivity (NPP)?",
     ["28,000 kcal/m²/yr", "12,000 kcal/m²/yr", "160,000 kcal/m²/yr", "2.5 kcal/m²/yr"],
     "B", "OSC", "medium",
     "- \\(\\text{NPP} = \\text{GPP} - \\text{R} = 20,000 - 8,000 = 12,000\\text{ kcal/m}^2/\\text{yr}\\).\nCorrect Choice is (B)."),

    ("Why is eating a predominantly vegetarian diet (consuming primary producers directly) far more energy-efficient and capable of feeding a much larger human population than an animal-based diet?",
     ["Because plants are cheaper to buy", "Because humans bypass the 90% energy loss of the animal intermediary tier, capturing 10 times more of the original solar energy", "Because plants don't have cells", "Because animals require no food"],
     "B", "OSC", "medium",
     "- Eating at T2 directly from grain captures 10x more calories per acre than feeding grain to livestock and eating livestock at T3.\nCorrect Choice is (B)."),

    # 21-30: Numerical Problems & Trophic Calculations
    ("In a pond food chain: Phytoplankton → Zooplankton → Fish → Kingfisher. If 40,000 Joules of energy is available at the phytoplankton tier, how much energy reaches the Kingfisher?",
     ["4,000 J", "400 J", "40 J", "4 J"],
     "C", "OSC", "medium",
     "- T1 = 40,000 J; T2 (Zooplankton) = 4,000 J; T3 (Fish) = 400 J; T4 (Kingfisher) = 40 J.\nCorrect Choice is (C)."),

    ("If a hawk at the 4th trophic level (T₄) possesses 25 Joules of energy, how much energy was originally present in the grass (T₁) that supported this chain?",
     ["250 J", "2,500 J", "25,000 J", "250,000 J"],
     "C", "OSC", "medium",
     "- T4 = 25 J; T3 = 250 J; T2 = 2,500 J; T1 = 25,000 J.\nCorrect Choice is (C)."),

    ("If an agricultural crop receives 1,000,000 Joules of total incident sunlight, approximately how much energy is fixed into plant biomass (assuming 1% capture efficiency)?",
     ["1,000,000 J", "10,000 J", "100,000 J", "1,000 J"],
     "B", "OSC", "medium",
     "- 1% of 1,000,000 J is \\(1,000,000 \\times 0.01 = 10,000\\text{ J}\\).\nCorrect Choice is (B)."),

    ("Continuing from the previous question, if cows eat this crop, how much energy is transferred into cow biomass?",
     ["10,000 J", "1,000 J", "100 J", "10 J"],
     "B", "OSC", "easy",
     "- Applying the 10% rule to 10,000 J yields \\(10,000 \\times 0.10 = 1,000\\text{ J}\\).\nCorrect Choice is (B)."),

    ("State whether True or False: Lindeman's 10% law means that exactly 10.00% is transferred in every single species on Earth without any variation.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. 10% is an empirical ecological average; actual trophic efficiency varies between 5% and 20% depending on organism physiology.\nCorrect Choice is (B)."),

    ("Why do warm-blooded homeothermic animals (like birds and mammals) have lower ecological production efficiencies than cold-blooded poikilotherms (like insects and fish)?",
     ["Because mammals have fur", "Because birds and mammals expend enormous amounts of metabolic energy maintaining a constant internal body temperature via shivering and cellular thermogenesis", "Because insects eat sunlight", "Because fish do not breathe"],
     "B", "OSC", "hard",
     "- Endotherms burn up to 90-95% of consumed energy solely to generate internal body heat, leaving less energy for net tissue growth.\nCorrect Choice is (B)."),

    ("Assertion (A): Energy flow through an ecosystem is unidirectional and cannot be recycled.\nReason (R): Energy entering an ecosystem as light is progressively converted into heat during respiration, and low-grade heat cannot be re-utilized by plants to synthesize sugars.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Solar radiation flows unidirectionally through trophic tiers and exits as dispersed infrared heat into space, obeying thermodynamics.\nCorrect Choice is (A)."),

    ("Assertion (A): A pyramid of energy can have an inverted shape in a deep lake ecosystem.\nReason (R): Microscopic algae multiply so fast that their energy production rate is zero.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "medium",
     "- Both statements are false. A pyramid of energy is universally and strictly UPRIGHT in all ecosystems without exception.\nCorrect Choice is (D)."),

    ("Which trophic level in any upright pyramid of biomass or numbers represents the broadest baseline?",
     ["Decomposers", "Producers (T₁)", "Primary consumers (T₂)", "Apex predators (T₄)"],
     "B", "OSC", "easy",
     "- In standard upright ecological pyramids, the primary producer tier forms the widest basal bar.\nCorrect Choice is (B)."),

    ("In an ecological pyramid, what units are used on the horizontal bars to represent the 'Pyramid of Energy'?",
     ["Number of individuals per square meter", "Kilocalories per square meter per year (\\(\\text{kcal/m}^2/\\text{yr}\\)) or \\(\\text{J/m}^2/\\text{yr}\\)", "Grams per cubic centimeter", "Meters per second"],
     "B", "OSC", "medium",
     "- Energy pyramids quantify the rate of energy flow per unit area per unit time (e.g. \\(\\text{J/m}^2/\\text{yr}\\)).\nCorrect Choice is (B)."),

    # 31-40: Ecological Principles & Systems
    ("What shape does a Pyramid of Numbers take in a parasitic food chain where a single tree supports hundreds of birds, and each bird hosts thousands of ticks and lice?",
     ["Strictly upright", "Inverted pyramid", "Circle", "Wave"],
     "B", "OSC", "easy",
     "- 1 tree → 100 birds → 10,000 lice creates an inverted pyramid of numbers.\nCorrect Choice is (B)."),

    ("If 500 Joules of energy is trapped at the producer level in a chain of 3 trophic levels (Plant → Goat → Human), how much energy reaches the human?",
     ["500 J", "50 J", "5 J", "0.5 J"],
     "C", "OSC", "easy",
     "- T1 = 500 J; T2 (Goat) = 50 J; T3 (Human) = 5 J.\nCorrect Choice is (C)."),

    ("Why are top predators like tigers and snow leopards naturally rare in population density across wilderness landscapes?",
     ["Because they don't like company", "Because the low thermodynamic efficiency of energy transfer leaves only a tiny fraction of total primary productivity available to sustain top carnivores over vast territories", "Because trees poison them", "Because they sleep 23 hours a day"],
     "B", "OSC", "medium",
     "- Sustaining a single top predator requires hundreds of square kilometers of productive herbivore and plant biomass.\nCorrect Choice is (B)."),

    ("What happens to an energy pyramid if an invasive weed outcompetes all native trees and doubles primary productivity?",
     ["The pyramid inverts", "The baseline width (T₁) expands, which can potentially support larger herbivore and consumer biomass throughout the upper tiers", "The pyramid vanishes", "All animals become herbivores"],
     "B", "OSC", "medium",
     "- Expanding the basal energy budget allows more energy to cascade through subsequent trophic tiers.\nCorrect Choice is (B)."),

    ("State whether True or False: Lindeman's energy efficiency accounts for why cattle ranches require vastly more land area than grain farms producing the same caloric yield.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. 90% of grain energy is lost in feeding cattle; farming grain directly for humans is ~10 times more calorie-efficient.\nCorrect Choice is (A)."),

    ("The transfer of energy from herbivore to carnivore is termed:",
     ["Primary production", "Secondary production / Trophic transfer", "Photolysis", "Transpiration"],
     "B", "OSC", "medium",
     "- Secondary production refers to the generation of consumer biomass from ingested food.\nCorrect Choice is (B)."),

    ("Identify the odd one out with respect to pyramid shape: Pyramid of energy in forest, Pyramid of energy in lake, Pyramid of energy in desert, Pyramid of biomass in ocean.",
     ["Pyramid of energy in forest", "Pyramid of energy in lake", "Pyramid of energy in desert", "Pyramid of biomass in ocean"],
     "D", "OSC", "medium",
     "- Pyramids of energy are ALWAYS upright; the pyramid of biomass in an open ocean is inverted.\nCorrect Choice is (D)."),

    ("Which parameter is plotted on the vertical axis of an ecological pyramid?",
     ["Time in days", "Successive Trophic Levels (Producers at bottom, Apex at top)", "Atmospheric pressure", "Wind velocity"],
     "B", "OSC", "easy",
     "- The vertical tiers represent progressive trophic levels from T1 at the base to Tn at the apex.\nCorrect Choice is (B)."),

    ("What percentage of total absorbed food energy is generally consumed by an animal's basic basal metabolic maintenance (respiration)?",
     ["Less than 1%", "Roughly 80% to 90%", "Exactly 10%", "0%"],
     "B", "OSC", "easy",
     "- Basal respiration, organ function, and thermoregulation account for the vast majority (80-90%) of ingested energy.\nCorrect Choice is (B)."),

    ("Who is often referred to as the 'Father of Modern Ecosystem Ecology' for his quantitative work on energy flows at Silver Springs?",
     ["Eugene Odum and Howard T. Odum", "Robert Hooke", "Isaac Newton", "Alexander Fleming"],
     "A", "OSC", "hard",
     "- H.T. Odum and Eugene Odum pioneered comprehensive quantitative measurements of energy flows and trophic dynamics in ecosystems.\nCorrect Choice is (A).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Quantitative Calculations & Ecological Rules
    ("If a field of grass absorbs 50,000 J of light and produces 5,000 J of net plant biomass, what is the net production efficiency of the primary consumers eating this grass?",
     ["They will create 500 J of herbivore biomass", "They will create 5,000 J of biomass", "They will create 50,000 J of biomass", "Zero"],
     "A", "OSC", "easy",
     "- By the 10% rule: \\(5,000\\text{ J} \\times 0.10 = 500\\text{ J}\\).\nCorrect Choice is (A)."),

    ("In an Arctic tundra food chain: Lichen → Caribou → Wolf. If the lichen tier contains 80,000 kcal, how many kcal are stored in the wolves?",
     ["8,000 kcal", "800 kcal", "80 kcal", "8 kcal"],
     "B", "OSC", "easy",
     "- T1 = 80,000 kcal; T2 (Caribou) = 8,000 kcal; T3 (Wolf) = 800 kcal.\nCorrect Choice is (B)."),

    ("Why can a farmer feed ten times more people on a 1-acre plot of sweet potatoes than on beef cattle raised on that same 1-acre plot?",
     ["Beef cattle sleep too much", "Eating crops directly captures 100% of T₂ energy, whereas eating beef loses 90% of that energy during cow metabolism", "Sweet potatoes have more fat than beef", "Cows eat rocks"],
     "B", "OSC", "easy",
     "- Bypassing the intermediate trophic level saves ~90% of available caloric energy.\nCorrect Choice is (B)."),

    ("State whether True or False: Inverted pyramids of biomass occur when the producers have a very short lifespan and high turnover rate compared to consumers.",
     ["True", "False"],
     "A", "OTF", "medium",
     "- True. Phytoplankton reproduce rapidly and are consumed immediately, keeping standing biomass low while producing enormous energy over time.\nCorrect Choice is (A)."),

    ("What happens to an inverted pyramid of numbers when an insect infestation attacks a single tree?",
     ["The base remains 1 tree while thousands of aphids and beetles multiply at the second trophic level, forming an inverted pyramid", "The tree multiplies into 100 trees", "All insects starve", "The pyramid flattens into a line"],
     "A", "OSC", "easy",
     "- A single large producer supports thousands of individual herbivores, giving an inverted shape.\nCorrect Choice is (A)."),

    ("Which form of energy is universally released as an unrecoverable byproduct during every trophic energy transfer?",
     ["Nuclear energy", "Thermal energy (low-grade heat)", "Electromagnetic gamma rays", "Gravitational waves"],
     "B", "OSC", "easy",
     "- Friction and biochemical inefficiencies inevitably convert free energy into dispersed ambient heat.\nCorrect Choice is (B)."),

    ("Why is energy flow in an ecosystem described as 'one-way' or 'non-cyclic'?",
     ["Because plants refuse to reuse heat", "Because heat radiated into outer space can never be re-absorbed by chlorophyll to regenerate chemical bonds", "Because animals travel south", "Because water flows downhill"],
     "B", "OSC", "medium",
     "- Dissipated low-grade heat cannot drive endergonic chemical reactions like photosynthesis; only incoming solar radiation can.\nCorrect Choice is (B)."),

    ("In a food chain consisting of: Grass → Deer → Leopard. If 60,000 J of energy is fixed by grass, calculate the energy dissipated as heat by the deer.",
     ["54,000 J", "6,000 J", "600 J", "60 J"],
     "A", "OSC", "hard",
     "- Deer ingest 60,000 J * 0.10 = 6,000 J. Of this 6,000 J, approximately 90% (\\(6,000 \\times 0.90 = 5,400\\text{ J}\\)) is dissipated as heat/waste.\nCorrect Choice is (A)."),

    ("Which ecological pyramid is considered the most comprehensive and accurate representation of true community functional energetics?",
     ["Pyramid of Numbers", "Pyramid of Energy", "Pyramid of Fresh Weight", "Pyramid of Height"],
     "B", "OSC", "medium",
     "- The pyramid of energy reflects the rate of energy passage over time, avoiding distortions caused by organism size or turnover rates.\nCorrect Choice is (B)."),

    ("What causes the 'standing crop' of an ecosystem to vary between summer and winter seasons?",
     ["Changes in daylight hours, temperature, and seasonal dormancy altering photosynthetic rates and plant biomass production", "Gravity variations", "Tectonic plate shifts", "Changes in the Earth's radius"],
     "A", "OSC", "easy",
     "- Solar insolation and temperature fluctuations directly regulate the standing crop biomass across seasons.\nCorrect Choice is (A)."),

    # 51-60: Trophic Efficiency & Energetics
    ("If an apex eagle requires 500 kcal per day to survive, approximately how many kcal of grass must grow daily to support that eagle in a 4-tier chain (Grass → Grasshopper → Frog → Eagle)?",
     ["500 kcal", "5,000 kcal", "50,000 kcal", "500,000 kcal"],
     "D", "OSC", "medium",
     "- T4 = 500 kcal; T3 = 5,000 kcal; T2 = 50,000 kcal; T1 = 500,000 kcal.\nCorrect Choice is (D)."),

    ("Fill in the blank: The scientific study of energy transformations and flows in living ecological communities is called _______.",
     ["Ecological Energetics (Bioenergetics)", "Paleontology", "Cytology", "Embryology"],
     "A", "OFB", "easy",
     "- Ecological bioenergetics investigates the quantitative acquisition and dissipation of energy in ecosystems.\nCorrect Choice is (A)."),

    ("Why does cold polar sea water support enormous populations of giant baleen whales?",
     ["Because whales eat ice", "Because polar waters have intense phytoplankton blooms fueling dense krill swarms, and whales feed directly on krill at T₃, minimizing intermediate trophic energy losses", "Because polar bears feed whales", "Because salt produces energy"],
     "B", "OSC", "hard",
     "- Short food chains (Algae → Krill → Whale) bypass multiple intermediate energy losses, delivering massive caloric volume to giant mammals.\nCorrect Choice is (B)."),

    ("What is 'assimilation efficiency' in animal nutrition?",
     ["The percentage of ingested food energy that is absorbed across the gut wall into the bloodstream rather than excreted as feces", "The speed at which an animal runs", "The amount of water in an apple", "The temperature of saliva"],
     "A", "OSC", "medium",
     "- Assimilation efficiency measures the proportion of consumed food absorbed into the body versus voided as indigestible waste.\nCorrect Choice is (A)."),

    ("Carnivores typically have a much HIGHER assimilation efficiency (60-80%) than herbivores (20-40%) because:",
     ["Meat is rich in digestible proteins and fats and lacks tough indigestible cellulose walls", "Carnivores drink more milk", "Meat contains chlorophyll", "Carnivores have smaller mouths"],
     "A", "OSC", "medium",
     "- Animal tissue is biochemically similar to the predator's own body and contains no refractory plant cell wall polysaccharides.\nCorrect Choice is (A)."),

    ("State whether True or False: Solar energy that drives photosynthesis was generated millions of miles away by thermonuclear fusion in the core of the Sun.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Hydrogen fusion in the Sun releases radiant photons that traverse 150 million kilometers to illuminate Earth.\nCorrect Choice is (A)."),

    ("If an animal consumes 1,000 J of food, excretes 400 J as feces, and uses 500 J for cellular respiration heat, how much energy is available as new tissue growth (production)?",
     ["1,900 J", "100 J", "900 J", "0 J"],
     "B", "OSC", "medium",
     "- \\(\\text{Production} = \\text{Ingested} - (\\text{Excreted} + \\text{Respiration}) = 1,000 - (400 + 500) = 100\\text{ J}\\).\nCorrect Choice is (B)."),

    ("In an ecosystem, what is the term for organisms that obtain energy by feeding at all trophic levels on dead and decomposing materials?",
     ["Decomposers / Saprotrophs", "Apex predators", "Producers", "Herbivores"],
     "A", "OSC", "easy",
     "- Decomposers operate outside the strict linear sequence, feeding on dead biomass from every trophic tier.\nCorrect Choice is (A)."),

    ("Which ecological pyramid can show a spindle shape (narrow base, broad middle, narrow top)?",
     ["Pyramid of Energy", "Pyramid of Numbers in a forest with few large trees supporting many insects, which are eaten by few birds", "Pyramid of Sunlight", "Pyramid of Gravity"],
     "B", "OSC", "medium",
     "- Few large trees (T1) → numerous herbivorous insects (T2) → few insectivorous birds (T3) creates a spindle-shaped pyramid of numbers.\nCorrect Choice is (B)."),

    ("Why can decomposers not be neatly placed into a single horizontal bar in standard upright ecological pyramids?",
     ["Because they are too small to see", "Because they receive organic matter from every trophic level simultaneously (T₁, T₂, T₃, T₄)", "Because they have no mass", "Because they don't produce heat"],
     "B", "OSC", "medium",
     "- Decomposers draw inputs from all trophic levels upon death, so they are typically placed alongside pyramids rather than in a single tier.\nCorrect Choice is (B)."),

    # 61-70: Ten Additional Practice Questions to reach exactly 30
    ("What is 'ecological efficiency' (trophic level transfer efficiency)?",
     ["The ratio of energy incorporated into new biomass at one trophic level to the energy consumed from the lower trophic level",
      "The speed of an animal's sprint",
      "The percentage of water in an organism",
      "The number of hours animals sleep"],
     "A", "OSC", "easy",
     "- Ecological efficiency is the efficiency with which energy is transferred from one trophic level to the next (typically ~10%).\nCorrect Choice is (A)."),

    ("If an herbivore ingests 5,000 J of plant energy, how much of that energy is estimated to be passed on to the carnivore that eats it?",
     ["5,000 J", "500 J", "50 J", "5 J"],
     "B", "OSC", "easy",
     "- According to the 10% rule: \\(5,000\\text{ J} \\times 0.10 = 500\\text{ J}\\).\nCorrect Choice is (B)."),

    ("In a desert ecosystem, why are large apex predators like mountain lions extremely sparse in density?",
     ["Because they dislike heat", "Because desert primary productivity (NPP) is very low, providing very little total base energy to support top predators", "Because sand blunts their claws", "Because there are no rocks"],
     "B", "OSC", "medium",
     "- Low net primary production sets a tight constraint on the total biomass and carrying capacity of higher trophic tiers.\nCorrect Choice is (B)."),

    ("State whether True or False: In any ecological pyramid, the width of each horizontal bar represents the magnitude of the measured parameter at that trophic level.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. The horizontal length or width of each rectangular block is proportional to the count, biomass, or energy at that level.\nCorrect Choice is (A)."),

    ("Why does the harvesting of marine fish at the 5th trophic level (e.g. Tuna, Swordfish) represent an ecologically expensive food choice for humans?",
     ["Because boats are expensive", "Because tuna are at T₄/T₅, meaning enormous amounts of ocean primary production were dissipated through multiple intermediate tiers to produce 1 kg of tuna", "Because tuna do not contain protein", "Because ocean water is salty"],
     "B", "OSC", "medium",
     "- Producing 1 kg of top predatory fish requires thousands of kilograms of primary phytoplankton production across multiple dissipative steps.\nCorrect Choice is (B)."),

    ("If a grassland contains 2,000,000 kcal of energy fixed in vegetation, how many kcal are stored in the bodies of primary consumers (rodents and insects)?",
     ["2,000,000 kcal", "200,000 kcal", "20,000 kcal", "2,000 kcal"],
     "B", "OSC", "easy",
     "- Applying the 10% rule: \\(2,000,000 \\times 0.10 = 200,000\\text{ kcal}\\).\nCorrect Choice is (B)."),

    ("What happens to the energy lost as metabolic respiration heat from an animal's body?",
     ["It enters the soil to become coal", "It radiates into the atmosphere and space as low-grade infrared thermal energy", "It returns to the sun", "It turns into rain"],
     "B", "OSC", "easy",
     "- Respiratory heat escapes as infrared radiation and is lost permanently from the biological cycle.\nCorrect Choice is (B)."),

    ("Which parameter is plotted on the horizontal bar of a Pyramid of Biomass?",
     ["Number of leaves", "Total dry organic mass per unit area (e.g. g/m² or kg/ha)", "Wind speed", "Volume of blood"],
     "B", "OSC", "easy",
     "- Biomass pyramids measure dry organic mass of living organisms per unit area.\nCorrect Choice is (B)."),

    ("Can a pyramid of numbers ever be inverted in a grassland ecosystem?",
     ["Yes, always", "No, in a typical grassland millions of grass plants support fewer herbivores, keeping it upright", "Only when it rains", "During winter only"],
     "B", "OSC", "easy",
     "- Grassland pyramids of numbers are typically upright due to vast numbers of individual grass plants at the base.\nCorrect Choice is (B)."),

    ("What does Charles Elton's original concept of ecological pyramids illustrate most clearly?",
     ["The architectural shape of Egyptian tombs", "The quantitative step-by-step reduction in numbers, biomass, or energy from the base to the apex of natural communities", "The speed of ocean currents", "The chemical formula of ozone"],
     "B", "OSC", "easy",
     "- Ecological pyramids visually summarize the structural and functional tapering of communities at successive trophic tiers.\nCorrect Choice is (B).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Lindeman 10% Energy Pyramid
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="230" viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Lindeman 10% Energy Pyramid</text>
  <!-- Apex Tier (T4) -->
  <rect x="150" y="45" width="60" height="26" fill="#ef4444" rx="3"/>
  <text x="160" y="62" fill="#ffffff" font-size="10" font-weight="bold">10 J (T₄)</text>
  <text x="215" y="62" fill="#f87171" font-size="9">Apex (Tiger)</text>
  <!-- 3rd Tier (T3) -->
  <rect x="120" y="75" width="120" height="26" fill="#f59e0b" rx="3"/>
  <text x="155" y="92" fill="#ffffff" font-size="10" font-weight="bold">100 J (T₃)</text>
  <text x="245" y="92" fill="#fbbf24" font-size="9">Carnivore (Wolf)</text>
  <!-- 2nd Tier (T2) -->
  <rect x="80" y="105" width="200" height="26" fill="#38bdf8" rx="3"/>
  <text x="150" y="122" fill="#ffffff" font-size="10" font-weight="bold">1,000 J (T₂)</text>
  <text x="285" y="122" fill="#38bdf8" font-size="9">Herbivore (Deer)</text>
  <!-- Producer Base (T1) -->
  <rect x="40" y="135" width="280" height="26" fill="#10b981" rx="3"/>
  <text x="145" y="152" fill="#ffffff" font-size="10" font-weight="bold">10,000 J (T₁)</text>
  <text x="325" y="152" fill="#34d399" font-size="8.5">Producers</text>
  <!-- 90% Heat loss arrow -->
  <path d="M 330,140 Q 350,110 330,80" stroke="#f43f5e" stroke-width="2" fill="none"/>
  <text x="270" y="180" fill="#f87171" font-size="8.5">~90% lost as respiration heat</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Energy decreases exponentially by a factor of 10 at each step</text>
  <text x="45" y="210" fill="#cbd5e1" font-size="8.5">Formulated by Raymond Lindeman (1942)</text>
</svg>
</div>
In the Lindeman Energy Pyramid above, if the producer vegetation synthesizes 10,000 Joules of energy, how much energy is transferred to the apex carnivore at T₄?""",
     ["1,000 J", "100 J", "10 J", "1 J"],
     "C", "OSC", "easy",
     "- Following successive 10% transfers: 10,000 J → 1,000 J (T2) → 100 J (T3) → 10 J (T4).\nCorrect Choice is (C)."),

    # 72: Pyramid of Numbers: Upright vs Inverted
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Pyramid of Numbers: Upright vs Inverted</text>
  <!-- Upright (Grassland) -->
  <rect x="25" y="45" width="145" height="135" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="65" fill="#34d399" font-size="10" font-weight="bold">GRASSLAND (Upright)</text>
  <rect x="75" y="75" width="45" height="15" fill="#ef4444"/>
  <text x="85" y="86" fill="#fff" font-size="8">3 Hawks</text>
  <rect x="60" y="93" width="75" height="15" fill="#38bdf8"/>
  <text x="70" y="104" fill="#fff" font-size="8">300 Frogs</text>
  <rect x="45" y="111" width="105" height="15" fill="#facc15"/>
  <text x="50" y="122" fill="#0f172a" font-size="8">50,000 Insects</text>
  <rect x="35" y="129" width="125" height="18" fill="#10b981"/>
  <text x="40" y="142" fill="#fff" font-size="8">1,500,000 Grass Plants</text>
  <text x="35" y="168" fill="#34d399" font-size="8.5">Normal upright shape</text>
  <!-- Inverted (Tree with Parasites) -->
  <rect x="190" y="45" width="145" height="135" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="200" y="65" fill="#fbbf24" font-size="10" font-weight="bold">TREE PARASITE (Inverted)</text>
  <rect x="200" y="75" width="125" height="18" fill="#ef4444"/>
  <text x="210" y="88" fill="#fff" font-size="8">100,000 Lice/Parasites</text>
  <rect x="225" y="96" width="75" height="15" fill="#38bdf8"/>
  <text x="235" y="107" fill="#fff" font-size="8">50 Birds</text>
  <rect x="250" y="114" width="25" height="18" fill="#10b981"/>
  <text x="255" y="127" fill="#fff" font-size="8">1 Tree</text>
  <text x="200" y="168" fill="#fde047" font-size="8.5">Inverted: 1 tree feeds thousands</text>
  <text x="50" y="202" fill="#38bdf8" font-size="9.5">Organism size influences pyramid of numbers shape</text>
</svg>
</div>
Why does a single oak tree ecosystem exhibit an INVERTED pyramid of numbers?""",
     ["Because the tree dies",
      "Because one giant single producer organism supports hundreds of birds and thousands of small insect parasites",
      "Because trees grow downwards",
      "Because birds have no mass"],
     "B", "OSC", "easy",
     "- The extreme physical size disparity allows a single primary producer (T1 = 1) to support thousands of consumer individuals.\nCorrect Choice is (B)."),

    # 73: Pyramid of Biomass: Upright vs Marine Inverted
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Pyramid of Biomass: Terrestrial vs Marine</text>
  <!-- Terrestrial Forest -->
  <rect x="25" y="45" width="145" height="135" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="65" fill="#34d399" font-size="10" font-weight="bold">TERRESTRIAL (Upright)</text>
  <rect x="75" y="80" width="45" height="15" fill="#ef4444"/>
  <text x="80" y="91" fill="#fff" font-size="8">Tigers (1 kg)</text>
  <rect x="60" y="98" width="75" height="15" fill="#38bdf8"/>
  <text x="65" y="109" fill="#fff" font-size="8">Deer (50 kg)</text>
  <rect x="35" y="116" width="125" height="22" fill="#10b981"/>
  <text x="40" y="131" fill="#fff" font-size="8.5">Forest Trees (1000 kg)</text>
  <text x="35" y="165" fill="#34d399" font-size="8.5">Massive plant standing crop</text>
  <!-- Marine Aquatic -->
  <rect x="190" y="45" width="145" height="135" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="200" y="65" fill="#38bdf8" font-size="10" font-weight="bold">OPEN OCEAN (Inverted)</text>
  <rect x="200" y="80" width="125" height="22" fill="#ef4444"/>
  <text x="210" y="95" fill="#fff" font-size="8.5">Large Fishes / Whales (12 g/m²)</text>
  <rect x="225" y="105" width="75" height="15" fill="#38bdf8"/>
  <text x="230" y="116" fill="#fff" font-size="8">Zooplankton (8 g/m²)</text>
  <rect x="245" y="123" width="35" height="15" fill="#10b981"/>
  <text x="248" y="134" fill="#fff" font-size="8">Phytoplankton (4 g/m²)</text>
  <text x="195" y="165" fill="#fde047" font-size="8">Inverted: High turnover of algae</text>
  <text x="50" y="202" fill="#38bdf8" font-size="9.5">Phytoplankton reproduce and are eaten rapidly</text>
</svg>
</div>
Why can the standing biomass of phytoplankton in an open ocean be smaller than the biomass of the fish feeding on them (inverted biomass pyramid)?""",
     ["Because fish produce their own food",
      "Because phytoplankton have a minuscule individual mass but reproduce at an astonishingly fast turnover rate, sustaining larger standing fish biomass",
      "Because ocean fish eat sea sand",
      "Because phytoplankton are made of metal"],
     "B", "OSC", "hard",
     "- High turnover rate (rapid generational cycles) allows a modest standing crop of micro-algae to fuel a large biomass of long-lived fish.\nCorrect Choice is (B)."),

    # 74: Thermodynamic Irreversibility: Entropy & Heat Loss
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Thermodynamics: Heat Dissipation to Space</text>
  <!-- Solar Input -->
  <circle cx="50" cy="80" r="18" fill="#fde047" stroke="#ca8a04"/>
  <text x="35" y="84" fill="#0f172a" font-size="8" font-weight="bold">SUN ☀️</text>
  <!-- Light Ray -->
  <line x1="70" y1="80" x2="110" y2="80" stroke="#fde047" stroke-width="3" marker-end="url(#arrow)"/>
  <!-- Ecosystem Box -->
  <rect x="110" y="45" width="130" height="115" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="125" y="65" fill="#34d399" font-size="9.5" font-weight="bold">LIVING ECOSYSTEM</text>
  <text x="120" y="85" fill="#cbd5e1" font-size="8.5">- Plant Photosynthesis</text>
  <text x="120" y="100" fill="#cbd5e1" font-size="8.5">- Animal Metabolism</text>
  <text x="120" y="115" fill="#cbd5e1" font-size="8.5">- Cellular Respiration</text>
  <text x="120" y="145" fill="#34d399" font-size="8.5">Biological Work Done</text>
  <!-- Dissipated Heat Arrows -->
  <line x1="240" y1="70" x2="295" y2="50" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="240" y1="100" x2="300" y2="100" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="240" y1="130" x2="295" y2="150" stroke="#ef4444" stroke-width="2.5"/>
  <text x="250" y="40" fill="#f87171" font-size="9" font-weight="bold">Infrared Heat ♨</text>
  <text x="245" y="175" fill="#f87171" font-size="8">Lost to Outer Space</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Second Law: Entropy increases; Heat CANNOT be recycled</text>
</svg>
</div>
According to the Second Law of Thermodynamics illustrated above, what happens to energy once it is converted into low-grade metabolic heat during animal respiration?""",
     ["It is gathered by roots to make wood",
      "It dissipates into the surrounding environment and space and can NEVER be recaptured by plants for photosynthesis",
      "It turns into pure coal",
      "It becomes oxygen gas"],
     "B", "OSC", "easy",
     "- Degraded metabolic heat increases entropy and radiates away; it cannot drive endergonic chemical synthesis.\nCorrect Choice is (B)."),

    # 75: Energy Losses at Each Trophic Step
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Fate of Consumed Energy (100% Ingested)</text>
  <!-- Ingested Box -->
  <rect x="25" y="55" width="90" height="40" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="32" y="75" fill="#38bdf8" font-size="9" font-weight="bold">Ingested Food</text>
  <text x="45" y="90" fill="#ffffff" font-size="9">100%</text>
  <!-- Split into 3 components -->
  <line x1="115" y1="75" x2="160" y2="50" stroke="#94a3b8" stroke-width="2"/>
  <line x1="115" y1="75" x2="160" y2="85" stroke="#94a3b8" stroke-width="2"/>
  <line x1="115" y1="75" x2="160" y2="120" stroke="#94a3b8" stroke-width="2"/>
  <!-- Component 1: Respiration -->
  <rect x="160" y="40" width="150" height="25" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="165" y="57" fill="#f87171" font-size="8.5">Respiration Heat: ~60-70% (Lost)</text>
  <!-- Component 2: Egestion -->
  <rect x="160" y="73" width="150" height="25" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="165" y="90" fill="#fbbf24" font-size="8.5">Feces & Excretion: ~20% (To decomposers)</text>
  <!-- Component 3: New Biomass -->
  <rect x="160" y="108" width="150" height="28" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="165" y="126" fill="#34d399" font-size="9" font-weight="bold">New Biomass (Growth): ~10%</text>
  <text x="45" y="175" fill="#34d399" font-size="10" font-weight="bold">Only ~10% is available for the NEXT predator tier!</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="8.5">Explains why the food chain length is severely constrained</text>
</svg>
</div>
In the energy partitioning diagram, which physiological pathway accounts for the largest fraction of energy lost by an active animal?""",
     ["New bone growth", "Cellular respiration and metabolic heat generation", "Shedding of hair", "Laying eggs"],
     "B", "OSC", "easy",
     "- Cellular respiration to drive metabolic functions and bodily activity dissipates 60-70% or more of consumed energy as heat.\nCorrect Choice is (B)."),

    # 76: Comparison: Energy vs Biomass vs Numbers
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Comparison: The Three Ecological Pyramids</text>
  <!-- Header Row -->
  <text x="25" y="45" fill="#94a3b8" font-size="9" font-weight="bold">PYRAMID</text>
  <text x="120" y="45" fill="#34d399" font-size="9" font-weight="bold">UNITS</text>
  <text x="230" y="45" fill="#60a5fa" font-size="9" font-weight="bold">CAN IT BE INVERTED?</text>
  <line x1="20" y1="52" x2="350" y2="52" stroke="#475569" stroke-width="1.5"/>
  <!-- Row 1: Numbers -->
  <text x="25" y="75" fill="#cbd5e1" font-size="9" font-weight="bold">1. Numbers</text>
  <text x="120" y="75" fill="#fde047" font-size="8.5">Individuals / area</text>
  <text x="230" y="75" fill="#f87171" font-size="8.5">YES (Tree ecosystem)</text>
  <!-- Row 2: Biomass -->
  <text x="25" y="110" fill="#cbd5e1" font-size="9" font-weight="bold">2. Biomass</text>
  <text x="120" y="110" fill="#fde047" font-size="8.5">g dry wt / m²</text>
  <text x="230" y="110" fill="#f87171" font-size="8.5">YES (Open sea/ocean)</text>
  <!-- Row 3: Energy -->
  <text x="25" y="145" fill="#cbd5e1" font-size="9" font-weight="bold">3. Energy</text>
  <text x="120" y="145" fill="#fde047" font-size="8.5">J / m² / yr (or kcal)</text>
  <text x="230" y="145" fill="#34d399" font-size="9" font-weight="bold">NEVER! (Strictly Upright)</text>
  <line x1="20" y1="165" x2="350" y2="165" stroke="#475569" stroke-width="1.5"/>
  <text x="45" y="190" fill="#38bdf8" font-size="9.5">Energy pyramid is the ONLY one that is UNIVERSALLY UPRIGHT</text>
  <text x="45" y="205" fill="#cbd5e1" font-size="8.5">Because energy dissipation is an immutable thermodynamic law</text>
</svg>
</div>
Which of the three types of ecological pyramids can NEVER be inverted under any circumstances in any ecosystem on Earth?""",
     ["Pyramid of Numbers", "Pyramid of Biomass", "Pyramid of Energy", "All three can be inverted"],
     "C", "OSC", "easy",
     "- The Pyramid of Energy is universally and strictly UPRIGHT because energy is irreversibly lost at every trophic step.\nCorrect Choice is (C)."),

    # 77: Net Primary Production Equation (NPP = GPP - R)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Primary Productivity Energetics</text>
  <!-- GPP Box -->
  <rect x="25" y="50" width="135" height="55" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="10" font-weight="bold">GPP (Gross Primary)</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">Total solar energy fixed</text>
  <text x="35" y="98" fill="#fde047" font-size="8">by photosynthesis</text>
  <!-- Minus Sign -->
  <text x="168" y="82" fill="#f87171" font-size="18" font-weight="bold">−</text>
  <!-- Respiration Box -->
  <rect x="185" y="50" width="130" height="55" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="195" y="70" fill="#f87171" font-size="10" font-weight="bold">R (Respiration)</text>
  <text x="195" y="85" fill="#cbd5e1" font-size="8">Energy plant burns for</text>
  <text x="195" y="98" fill="#cbd5e1" font-size="8">its own cellular life</text>
  <!-- Equals Sign -->
  <text x="168" y="130" fill="#38bdf8" font-size="18" font-weight="bold">▼</text>
  <!-- NPP Box -->
  <rect x="50" y="135" width="240" height="42" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="60" y="153" fill="#38bdf8" font-size="10.5" font-weight="bold">NPP = GPP − R (Net Primary Production)</text>
  <text x="60" y="168" fill="#cbd5e1" font-size="8.5">Actual plant biomass accumulated & available to herbivores</text>
  <text x="50" y="198" fill="#fde047" font-size="9.5">Fundamental equation of planetary ecosystem metabolism</text>
</svg>
</div>
In the fundamental ecosystem productivity equation shown above, what does Net Primary Productivity (NPP) represent?""",
     ["Total solar light reflecting off clouds",
      "The actual biomass accumulated in plant tissues that remains available for consumption by herbivores after subtracting plant respiration",
      "Total water evaporated by lakes",
      "The mass of soil rock"],
     "B", "OSC", "easy",
     "- \\(\\text{NPP} = \\text{GPP} - \\text{R}\\) represents the net organic matter stored by plants available to heterotrophic consumers.\nCorrect Choice is (B)."),

    # 78: Agricultural Energetics: Vegetarian vs Carnivorous Diet
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Dietary Energetics: Plant vs Meat</text>
  <!-- Path A: Direct Plant Eating -->
  <rect x="25" y="48" width="290" height="48" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="66" fill="#34d399" font-size="9" font-weight="bold">PATH A: Grain / Vegetables ➔ Human (T₂)</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8">- 10,000 J grain ➔ 1,000 J absorbed by humans</text>
  <text x="35" y="92" fill="#fde047" font-size="8 font-weight=bold">High Efficiency: Feeds 10× more humans per hectare</text>
  <!-- Path B: Grain Fed to Cattle -->
  <rect x="25" y="105" width="290" height="52" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="122" fill="#f87171" font-size="9" font-weight="bold">PATH B: Grain ➔ Cattle (T₂) ➔ Human (T₃)</text>
  <text x="35" y="136" fill="#cbd5e1" font-size="8">- 10,000 J grain ➔ 1,000 J cow ➔ ONLY 100 J to humans</text>
  <text x="35" y="148" fill="#ef4444" font-size="8 font-weight=bold">90% of grain energy is lost as cow respiration heat</text>
  <text x="45" y="185" fill="#38bdf8" font-size="9.5">Eating at lower trophic levels dramatically reduces land footprint</text>
</svg>
</div>
Based on trophic energetics shown in the comparison, why can a given agricultural acreage sustain roughly ten times more humans on a plant-based diet than on a livestock meat diet?""",
     ["Because plants grow faster than cattle walk",
      "Because eating plants directly avoids the ~90% trophic energy loss incurred during livestock metabolism",
      "Because cows eat no grain",
      "Because vegetables have more bones"],
     "B", "OSC", "easy",
     "- Inserting an intermediate livestock tier dissipates 90% of the crop's caloric energy, requiring ~10x more land area per human calorie.\nCorrect Choice is (B)."),

    # 79: Endotherm vs Ectotherm Energy Efficiency
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Production Efficiency: Mammals vs Insects</text>
  <!-- Endotherm (Mammal) -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="70" fill="#f87171" font-size="10" font-weight="bold">ENDOTHERM (e.g. Mouse)</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- High metabolic rate</text>
  <text x="35" y="105" fill="#f87171" font-size="8.5">- 95-98% energy burned</text>
  <text x="35" y="118" fill="#f87171" font-size="8.5">  to stay warm at 37°C</text>
  <text x="35" y="140" fill="#fde047" font-size="9" font-weight="bold">Production: ~1-3% only</text>
  <!-- Ectotherm (Insect) -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="70" fill="#34d399" font-size="10" font-weight="bold">ECTOTHERM (e.g. Beetle)</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8.5">- Cold-blooded body</text>
  <text x="190" y="105" fill="#34d399" font-size="8.5">- Zero energy spent on</text>
  <text x="190" y="118" fill="#34d399" font-size="8.5">  internal heaters</text>
  <text x="190" y="140" fill="#fde047" font-size="9" font-weight="bold">Production: ~20-40%!</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Ectotherms convert far more consumed food into new body biomass</text>
</svg>
</div>
Why do cold-blooded insects have a vastly higher biomass production efficiency (~20-40%) than warm-blooded mammals (~1-3%)?""",
     ["Because insects drink oil",
      "Because insects do not burn large quantities of food energy maintaining a high, constant internal body temperature",
      "Because mammals have no hearts",
      "Because insects have no cells"],
     "B", "OSC", "medium",
     "- Maintaining endothermic homeothermy is energetically expensive, leaving very little energy for new tissue production in mammals.\nCorrect Choice is (B)."),

    # 80: Multi-tier Trophic Calculation Visualizer
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Step-by-Step 10% Math Problem</text>
  <!-- Problem statement -->
  <rect x="25" y="45" width="290" height="135" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="65" fill="#fde047" font-size="9" font-weight="bold">GIVEN: Sunlight captured = 200,000 J</text>
  <text x="35" y="85" fill="#34d399" font-size="8.5">- Plant Producer (T₁) = 200,000 J</text>
  <text x="35" y="105" fill="#facc15" font-size="8.5">- Herbivorous Deer (T₂) = 200,000 × 0.10 = 20,000 J</text>
  <text x="35" y="125" fill="#38bdf8" font-size="8.5">- Carnivorous Wolf (T₃) = 20,000 × 0.10 = 2,000 J</text>
  <text x="35" y="145" fill="#f87171" font-size="9" font-weight="bold">- Apex Tiger (T₄) = 2,000 × 0.10 = 200 J</text>
  <text x="35" y="165" fill="#cbd5e1" font-size="8">Energy reaching Tiger: exactly 0.1% of original plant energy</text>
  <text x="45" y="200" fill="#fde047" font-size="9.5">Each step retains 1/10th and loses 9/10ths to the environment</text>
</svg>
</div>
In the step-by-step mathematical example above, what percentage of the original plant energy (T₁) ultimately reaches the apex tiger at T₄?""",
     ["10%", "1%", "0.1% (one-thousandth)", "50%"],
     "C", "OSC", "medium",
     "- Across 3 trophic transfers: \\(0.10 \\times 0.10 \\times 0.10 = 0.001\\) or 0.1% of the original plant energy.\nCorrect Choice is (C)."),

    # 81: Ocean Food Chain Energy Efficiency
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Ocean Food Chain: Whale vs Shark</text>
  <!-- Short Whale Chain -->
  <rect x="25" y="45" width="290" height="60" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="65" fill="#34d399" font-size="9.5" font-weight="bold">SHORT CHAIN: Phytopl. ➔ Krill ➔ Blue Whale (T₃)</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8.5">- Only 2 transfers! Massive energy reaches Whale</text>
  <text x="35" y="95" fill="#fde047" font-size="8.5">Enables gigantic 100-ton body mass to thrive</text>
  <!-- Long Shark Chain -->
  <rect x="25" y="115" width="290" height="60" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="135" fill="#f87171" font-size="9.5" font-weight="bold">LONG CHAIN: Phytopl. ➔ Zoopl. ➔ Small Fish ➔ Tuna ➔ Shark (T₅)</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8.5">- 4 transfers! Energy diluted 10,000-fold</text>
  <text x="35" y="165" fill="#f87171" font-size="8.5">Great White Sharks remain rare apex hunters</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Shorter chains deliver exponentially higher energy yields to giants</text>
</svg>
</div>
Why can the Blue Whale (the largest animal to ever live on Earth) sustain its enormous 150-ton body, whereas top predatory sharks remain far smaller in total biomass?""",
     ["Because whales sleep in deep water",
      "Because the blue whale feeds directly at T₃ on tiny krill, bypassing 2 intermediate trophic transfers and capturing 100 times more energy",
      "Because whales eat seaweed",
      "Because sharks have no bones"],
     "B", "OSC", "hard",
     "- Feeding close to primary producers (T3) provides abundant calories to support colossal body mass.\nCorrect Choice is (B)."),

    # 82: Summary Diagnostic of Ecological Energetics
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Summary: Ecosystem Energetics Laws</text>
  <!-- Law 1 -->
  <rect x="20" y="42" width="320" height="38" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="30" y="58" fill="#34d399" font-size="9.5" font-weight="bold">1. First Law of Thermodynamics:</text>
  <text x="30" y="72" fill="#cbd5e1" font-size="8.5">Energy cannot be created or destroyed, only transformed (Solar ➔ Chemical)</text>
  <!-- Law 2 -->
  <rect x="20" y="85" width="320" height="38" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="30" y="101" fill="#fbbf24" font-size="9.5" font-weight="bold">2. Second Law of Thermodynamics:</text>
  <text x="30" y="115" fill="#cbd5e1" font-size="8.5">Every transformation increases entropy; ~90% lost as respiration heat</text>
  <!-- Law 3 -->
  <rect x="20" y="128" width="320" height="42" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="144" fill="#38bdf8" font-size="9.5" font-weight="bold">3. Lindeman 10% Energy Rule:</text>
  <text x="30" y="158" fill="#cbd5e1" font-size="8.5">Only ~10% passes to next tier; Limits food chains to 4-5 levels</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Universal thermodynamic guardrails governing all biospheres</text>
</svg>
</div>
According to the universal principles of ecosystem energetics, what happens to the total usable free energy as one ascends the trophic ladder from producers to apex predators?""",
     ["It increases by 10% at each step",
      "It diminishes rapidly and irreversibly by approximately 90% at each step, leaving only ~10% for the next tier",
      "It stays exactly constant",
      "It doubles at every step"],
     "B", "OSC", "easy",
     "- Usable free energy declines exponentially by ~90% at each successive trophic tier, adhering to the laws of thermodynamics.\nCorrect Choice is (B).")
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

out_file = "scripts/ch7_topic2.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
