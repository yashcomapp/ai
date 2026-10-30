# scripts/generate_ch7_topic3.py
# Topic: MH-9-SCIT-7-7.3 (Biogeochemical Cycles: Carbon, Oxygen, and Nitrogen Cycles)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-7-7.3"
CHAPTER_NUM = 7

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Biogeochemical Cycle Fundamentals & Carbon Cycle
    ("What is a 'biogeochemical cycle' in ecosystem ecology?",
     ["The rotation of tectonic plates", "The cyclic circulation of chemical nutrient elements between living biotic organisms and non-living abiotic reservoirs (atmosphere, lithosphere, hydrosphere)", "The cycle of ocean tides", "The life cycle of an insect"],
     "B", "OSC", "easy",
     "- Biogeochemical cycles circulate essential life elements (C, H, O, N, P, S) between biotic and abiotic components continuously.\nCorrect Choice is (B)."),

    ("Biogeochemical cycles are broadly categorized into two major classes:",
     ["Hot and cold cycles", "Gaseous cycles and Sedimentary cycles", "Solar and lunar cycles", "Fast and dead cycles"],
     "B", "OSC", "easy",
     "- Gaseous cycles have their primary reservoir in the atmosphere/hydrosphere (C, N, O); sedimentary cycles in the Earth's crust (P, S).\nCorrect Choice is (B)."),

    ("Which of the following elements undergoes a 'gaseous' biogeochemical cycle?",
     ["Phosphorus", "Carbon (as Carbon Dioxide)", "Calcium", "Silicon"],
     "B", "OSC", "easy",
     "- Carbon cycles primarily through the gaseous atmosphere and hydrosphere as carbon dioxide (\\(\\text{CO}_2\\)).\nCorrect Choice is (B)."),

    ("Which primary biological process removes massive amounts of carbon dioxide (\\(\\text{CO}_2\\)) from the Earth's atmosphere?",
     ["Volcanic eruption", "Photosynthesis by green plants, algae, and cyanobacteria", "Animal respiration", "Forest fires"],
     "B", "OSC", "easy",
     "- Photosynthesis fixes atmospheric \\(\\text{CO}_2\\) into organic carbohydrates: \\(6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\to \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2\\).\nCorrect Choice is (B)."),

    ("Which biological process continuously releases carbon dioxide back into the atmosphere and aquatic environments?",
     ["Cellular respiration of plants, animals, and decomposers", "Photosynthesis", "Formation of fossil coal", "Nitrogen fixation"],
     "A", "OSC", "easy",
     "- Aerobic respiration oxidizes organic glucose, releasing \\(\\text{CO}_2\\) and water as metabolic byproducts.\nCorrect Choice is (A)."),

    ("How do massive quantities of carbon get locked into the Earth's crust for millions of years?",
     ["By floating into the sky", "By accumulation and compression of dead plant/animal remains under high temperature and pressure, forming fossil fuels (coal, petroleum, natural gas) and limestone", "By dissolving in air", "By magnets"],
     "B", "OSC", "easy",
     "- Geological sequestration traps carbon as sedimentary carbonate rocks (limestone) and fossil hydrocarbons over millions of years.\nCorrect Choice is (B)."),

    ("What rapid anthropogenic (human) activity is causing an abrupt surge in atmospheric \\(\\text{CO}_2\\) levels, upsetting the carbon cycle balance?",
     ["Growing more gardens", "Excessive combustion of fossil fuels (coal, oil, gas) combined with large-scale deforestation", "Drinking mineral water", "Flying hot air balloons"],
     "B", "OSC", "easy",
     "- Burning fossil fuels releases geological carbon sequestered over 300 million years in just two centuries, accelerating the greenhouse effect.\nCorrect Choice is (B)."),

    ("What is the primary role of the Earth's oceans in the global carbon cycle?",
     ["Oceans produce zero carbon", "Oceans act as a colossal carbon sink, dissolving atmospheric \\(\\text{CO}_2\\) as carbonic acid/bicarbonate and incorporating it into marine shell carbonates", "Oceans turn carbon into gold", "Oceans destroy carbon atoms"],
     "B", "OSC", "medium",
     "- Oceans absorb roughly 25-30% of anthropogenic \\(\\text{CO}_2\\), storing it as bicarbonate ions and marine mollusk calcium carbonate shells.\nCorrect Choice is (B)."),

    ("State whether True or False: Decomposers play zero role in the carbon cycle.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Microbial decomposition of dead organic matter returns vast amounts of \\(\\text{CO}_2\\) to the atmosphere via respiration.\nCorrect Choice is (B)."),

    ("What environmental phenomenon is driven by rising atmospheric concentrations of \\(\\text{CO}_2\\) trapping infrared radiation emitted by the Earth?",
     ["Acid rain", "The Enhanced Greenhouse Effect and Global Warming", "Ozone hole depletion", "Earthquakes"],
     "B", "OSC", "easy",
     "- Carbon dioxide is a greenhouse gas that absorbs outgoing terrestrial infrared radiation, warming the troposphere.\nCorrect Choice is (B)."),

    # 11-20: Oxygen Cycle & Atmospheric Interactions
    ("What percentage of Earth's modern dry atmosphere is composed of diatomic molecular oxygen (\\(\\text{O}_2\\))?",
     ["Approximately 78%", "Approximately 21%", "About 0.04%", "About 50%"],
     "B", "OSC", "easy",
     "- Molecular oxygen constitutes roughly 20.95% (~21%) of Earth's atmosphere by volume.\nCorrect Choice is (B)."),

    ("What is the primary source of free atmospheric oxygen on Earth?",
     ["Volcanoes", "Photolysis of water molecules during the light reactions of oxygenic photosynthesis by plants, algae, and cyanobacteria", "Rusting of iron", "Evaporation of seawater"],
     "B", "OSC", "easy",
     "- Oxygen is produced when water molecules are split (photolysis) during photosynthesis: \\(2\\text{H}_2\\text{O} \\to 4\\text{H}^+ + 4e^- + \\text{O}_2\\).\nCorrect Choice is (B)."),

    ("Which major processes continuously consume oxygen from the atmosphere?",
     ["Photosynthesis and transpiration", "Respiration, combustion of fuels, and chemical oxidation (such as rusting and corrosion of metals)", "Rainfall and condensation", "Nitrogen fixation"],
     "B", "OSC", "easy",
     "- Aerobic respiration, combustion of organic fuels, and chemical oxidation of minerals consume atmospheric oxygen.\nCorrect Choice is (B)."),

    ("What triatomic molecule is formed high in the stratosphere when ultraviolet solar radiation dissociates molecular oxygen (\\(\\text{O}_2\\))?",
     ["Carbon monoxide (CO)", "Ozone (\\(\\text{O}_3\\))", "Water vapour (\\(\\text{H}_2\\text{O}\\))", "Nitrous oxide (\\(\\text{N}_2\\text{O}\\))"],
     "B", "OSC", "easy",
     "- In the stratosphere, UV rays split \\(\\text{O}_2\\) into atomic oxygen (O), which combines with another \\(\\text{O}_2\\) to form ozone (\\(\\text{O}_3\\)).\nCorrect Choice is (B)."),

    ("What vital life-protecting function does the stratospheric ozone layer (\\(\\text{O}_3\\)) perform for the biosphere?",
     ["It produces clouds", "It absorbs lethal ultraviolet-B and ultraviolet-C (UV) radiation from sunlight, preventing skin cancers and cellular DNA mutations", "It cools down the moon", "It prevents meteorite impacts"],
     "B", "OSC", "easy",
     "- The ozone layer acts as an umbrella shielding terrestrial life from harmful solar ultraviolet radiation.\nCorrect Choice is (B)."),

    ("What harmful synthetic chemicals, formerly used in refrigerants and aerosol spray cans, caused severe degradation and thinning of the Antarctic ozone layer?",
     ["Carbon dioxide (\\(\\text{CO}_2\\))", "Chlorofluorocarbons (CFCs)", "Methane (\\(\\text{CH}_4\\))", "Water vapor"],
     "B", "OSC", "easy",
     "- CFCs release chlorine radicals in the stratosphere, each of which catalytically destroys over 100,000 ozone molecules.\nCorrect Choice is (B)."),

    ("State whether True or False: Oxygen is a highly reactive element that readily forms oxides with almost all metals and non-metals.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Oxygen is electronegative and chemically reactive, forming oxides (e.g. \\(\\text{Fe}_2\\text{O}_3\\), \\(\\text{SiO}_2\\), \\(\\text{CO}_2\\)).\nCorrect Choice is (A)."),

    ("The burning of wood or fossil fuels consumes oxygen and produces carbon dioxide. This process is called:",
     ["Respiration", "Combustion", "Fermentation", "Calcification"],
     "B", "OSC", "easy",
     "- Combustion is a rapid exothermic oxidation reaction consuming oxygen and releasing heat, light, and \\(\\text{CO}_2\\).\nCorrect Choice is (B)."),

    ("Which organelle in eukaryotic cells consumes molecular oxygen to generate adenosine triphosphate (ATP) via oxidative phosphorylation?",
     ["Chloroplast", "Mitochondria", "Ribosome", "Golgi apparatus"],
     "B", "OSC", "medium",
     "- Mitochondria consume \\(\\text{O}_2\\) as the terminal electron acceptor in the electron transport chain, generating cellular ATP.\nCorrect Choice is (B)."),

    ("What is 'anaerobic respiration'?",
     ["Respiration using pure liquid oxygen", "Cellular respiration occurring in the complete absence of oxygen, utilized by yeast and certain anaerobic bacteria", "Breathing in clean mountain air", "Photosynthesis in the dark"],
     "B", "OSC", "easy",
     "- Anaerobic respiration (or fermentation) breaks down carbohydrates to release energy without requiring molecular oxygen.\nCorrect Choice is (B)."),

    # 21-30: Nitrogen Cycle & Microbial Transformations
    ("What percentage of Earth's atmosphere consists of gaseous elemental nitrogen (\\(\\text{N}_2\\))?",
     ["Approximately 21%", "Approximately 78%", "About 0.04%", "About 10%"],
     "B", "OSC", "easy",
     "- Gaseous diatomic nitrogen (\\(\\text{N}_2\\)) makes up approximately 78% of the atmosphere.\nCorrect Choice is (B)."),

    ("Even though nitrogen constitutes 78% of the air, why can green plants NOT absorb it directly through their leaves like carbon dioxide?",
     ["Because nitrogen is toxic to leaves", "Because two nitrogen atoms are held together by an extremely strong chemical triple covalent bond (\\(\\text{N}\\equiv\\text{N}\\)) which plants lack the biochemical enzymes to break", "Because nitrogen gas is too heavy", "Because plants have no stomata"],
     "B", "OSC", "hard",
     "- The immense bond dissociation energy of the \\(\\text{N}\\equiv\\text{N}\\) triple bond (\\(945\\text{ kJ/mol}\\)) makes atmospheric \\(\\text{N}_2\\) chemically inert to plants.\nCorrect Choice is (B)."),

    ("The biological conversion of inert atmospheric nitrogen gas (\\(\\text{N}_2\\)) into plant-usable nitrogenous compounds (like ammonia) is called:",
     ["Denitrification", "Nitrogen Fixation", "Ammonification", "Transpiration"],
     "B", "OSC", "easy",
     "- Nitrogen fixation is the reduction of atmospheric \\(\\text{N}_2\\) to reactive nitrogen compounds (ammonia/nitrates).\nCorrect Choice is (B)."),

    ("Which symbiotic bacterium lives inside the root nodules of leguminous plants (like pea, gram, bean) and fixes atmospheric nitrogen?",
     ["Escherichia coli", "Rhizobium", "Lactobacillus", "Streptococcus"],
     "B", "OSC", "easy",
     "- Rhizobium bacteria reside symbiotically in root nodules of legumes, synthesizing nitrogenase to fix atmospheric nitrogen.\nCorrect Choice is (B)."),

    ("Which free-living bacterium in the soil fixes atmospheric nitrogen independently without forming nodules?",
     ["Azotobacter (or Clostridium)", "Yeast", "Penicillium", "Salmonella"],
     "A", "OSC", "medium",
     "- Azotobacter is a non-symbiotic, free-living aerobic bacterium in soil capable of fixing atmospheric nitrogen.\nCorrect Choice is (A)."),

    ("Which enzyme, containing molybdenum and iron, catalyzes the biological fixation of nitrogen gas to ammonia?",
     ["Amylase", "Nitrogenase", "Pepsin", "DNA polymerase"],
     "B", "OSC", "hard",
     "- Nitrogenase is the specialized molybdenum-iron complex enzyme that breaks the \\(\\text{N}\\equiv\\text{N}\\) triple bond.\nCorrect Choice is (B)."),

    ("Why is the enzyme nitrogenase in Rhizobium root nodules extremely sensitive to molecular oxygen, and what pink oxygen-scavenging pigment protects it?",
     ["Protected by Chlorophyll", "Inactivated by oxygen; protected by Leghemoglobin", "Protected by Hemoglobin", "Protected by Melanin"],
     "B", "OSC", "hard",
     "- Nitrogenase is irreversibly poisoned by \\(\\text{O}_2\\); leghemoglobin acts as an oxygen buffer, keeping free \\(\\text{O}_2\\) low.\nCorrect Choice is (B)."),

    ("How does physical atmospheric nitrogen fixation occur during thunderstorms?",
     ["Raindrops freeze nitrogen", "High-voltage lightning discharges supply energy for atmospheric \\(\\text{N}_2\\) and \\(\\text{O}_2\\) to combine into nitric oxide (NO) and nitrogen dioxide, which dissolve in rain as nitric acid", "Thunder shakes nitrogen into soil", "Wind blows nitrogen into roots"],
     "B", "OSC", "medium",
     "- Lightning provides thousands of degrees of localized thermal energy to bond \\(\\text{N}_2\\) and \\(\\text{O}_2\\) into nitrates carried by rain.\nCorrect Choice is (B)."),

    ("The process by which decomposers break down nitrogenous organic wastes (urea, uric acid) and dead protein carcasses into ammonia is called:",
     ["Nitrification", "Ammonification", "Denitrification", "Photosynthesis"],
     "B", "OSC", "easy",
     "- Ammonification is the mineralization of organic nitrogen (amino acids, urea) into ammonia (\\(\\text{NH}_3\\)) by ammonifying microbes.\nCorrect Choice is (B)."),

    ("The biological oxidation of toxic ammonia (\\(\\text{NH}_3\\)) first into nitrite (\\(\\text{NO}_2^-\\)) and then into nitrate (\\(\\text{NO}_3^-\\)) is called:",
     ["Ammonification", "Nitrification", "Denitrification", "Assimilation"],
     "B", "OSC", "easy",
     "- Nitrification is the two-step chemoautotrophic oxidation of ammonia to nitrites and nitrates.\nCorrect Choice is (B)."),

    # 31-40: Nitrification, Denitrification & Synthesis
    ("Which soil bacterium oxidizes ammonia (\\(\\text{NH}_3\\)) into nitrite (\\(\\text{NO}_2^-\\)) in the first step of nitrification?",
     ["Nitrobacter", "Nitrosomonas (or Nitrosococcus)", "Pseudomonas", "Rhizobium"],
     "B", "OSC", "medium",
     "- Nitrosomonas bacteria oxidize ammonia to nitrite: \\(2\\text{NH}_3 + 3\\text{O}_2 \\to 2\\text{NO}_2^- + 2\\text{H}^+ + 2\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("Which bacterium oxidizes nitrite (\\(\\text{NO}_2^-\\)) into plant-absorbable nitrate (\\(\\text{NO}_3^-\\)) in the second step of nitrification?",
     ["Nitrosomonas", "Nitrobacter", "Azotobacter", "Lactobacillus"],
     "B", "OSC", "medium",
     "- Nitrobacter converts nitrite to nitrate: \\(2\\text{NO}_2^- + \\text{O}_2 \\to 2\\text{NO}_3^-\\).\nCorrect Choice is (B)."),

    ("The conversion of soil nitrates (\\(\\text{NO}_3^-\\)) back into gaseous nitrogen (\\(\\text{N}_2\\)) that escapes into the atmosphere is called:",
     ["Nitrogen fixation", "Ammonification", "Denitrification", "Eutrophication"],
     "C", "OSC", "easy",
     "- Denitrification completes the nitrogen cycle by returning elemental \\(\\text{N}_2\\) gas back to the atmospheric reservoir.\nCorrect Choice is (C)."),

    ("Which anaerobic soil bacterium is responsible for biological denitrification?",
     ["Rhizobium", "Nitrosomonas", "Pseudomonas denitrificans (or Thiobacillus)", "Nitrobacter"],
     "C", "OSC", "medium",
     "- Pseudomonas and Thiobacillus denitrify nitrates under waterlogged, anaerobic soil conditions.\nCorrect Choice is (C)."),

    ("Why do farmers often rotate leguminous crops (like chickpeas or lentils) between cereal crop plantings?",
     ["To make the field look colorful", "Because Rhizobium in legume nodules naturally enriches the soil with fixed nitrogen nitrates, reducing the need for artificial chemical fertilizers", "Because legumes kill all earthworms", "Because cereals don't grow in soil"],
     "B", "OSC", "easy",
     "- Crop rotation with legumes replenishes soil fertility naturally through symbiotic nitrogen fixation.\nCorrect Choice is (B)."),

    ("Assertion (A): The nitrogen cycle would grind to an abrupt halt without bacteria.\nReason (R): Bacteria are solely responsible for biological nitrogen fixation, ammonification, nitrification, and denitrification.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Every critical enzymatic transformation in the nitrogen cycle is mediated by specialized bacteria.\nCorrect Choice is (A)."),

    ("Assertion (A): Burning coal and petrol contributes significantly to the atmospheric carbon pool.\nReason (R): Fossil fuels represent organic carbon deposits buried and stored millions of years ago during the Carboniferous period.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Combustion of ancient geologically sequestered biomass injects long-stored carbon back into active atmospheric circulation.\nCorrect Choice is (A)."),

    ("Identify the odd one out with respect to biogeochemical cycles: Carbon cycle, Nitrogen cycle, Oxygen cycle, Phosphorus cycle.",
     ["Carbon cycle", "Nitrogen cycle", "Oxygen cycle", "Phosphorus cycle"],
     "D", "OSC", "medium",
     "- Phosphorus cycle is a sedimentary cycle (rocks/soil reservoir); Carbon, Nitrogen, and Oxygen cycles are gaseous cycles.\nCorrect Choice is (D)."),

    ("Excessive runoff of nitrogen and phosphorus fertilizers into ponds causes massive algal blooms and subsequent oxygen depletion, a process known as:",
     ["Biomagnification", "Eutrophication", "Denitrification", "Stratification"],
     "B", "OSC", "medium",
     "- Eutrophication is the nutrient enrichment of water bodies causing rampant algal growth and suffocation of aquatic fauna.\nCorrect Choice is (B)."),

    ("What gas is formed as a major byproduct of the industrial Haber-Bosch process used to manufacture synthetic chemical fertilizers?",
     ["Oxygen (\\(\\text{O}_2\\))", "Ammonia (\\(\\text{NH}_3\\))", "Ozone (\\(\\text{O}_3\\))", "Carbon monoxide (CO)"],
     "B", "OSC", "easy",
     "- The Haber process synthesizes ammonia by reacting \\(\\text{N}_2\\) and \\(\\text{H}_2\\) under high pressure and temperature over an iron catalyst.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Carbon & Oxygen Cycles in Practice
    ("During daylight, a green leaf absorbs carbon dioxide and releases oxygen. What happens inside that same leaf during the dark night?",
     ["It releases nitrogen gas", "Photosynthesis halts without light, but cellular respiration continues, consuming oxygen and releasing carbon dioxide", "It stops all chemical reactions", "It absorbs water through the air"],
     "B", "OSC", "easy",
     "- In the dark, respiration continues uninterrupted, consuming \\(\\text{O}_2\\) and releasing \\(\\text{CO}_2\\).\nCorrect Choice is (B)."),

    ("Which biological pigment gives the root nodules of healthy leguminous plants their characteristic pink or reddish internal color?",
     ["Chlorophyll-a", "Leghemoglobin", "Anthocyanin", "Carotene"],
     "B", "OSC", "easy",
     "- Leghemoglobin is a pink heme-protein that scavenges oxygen to safeguard the oxygen-labile nitrogenase enzyme.\nCorrect Choice is (B)."),

    ("In aquatic ecosystems, how do submerged fish obtain the oxygen required for their cellular respiration?",
     ["They swim to the surface every 5 seconds to gulp atmospheric air", "They extract dissolved oxygen gas (\\(\\text{O}_2\\)) directly from the water using their filamentous gills", "They break water molecules into hydrogen and oxygen inside their stomachs", "They do not require oxygen"],
     "B", "OSC", "easy",
     "- Water flows over vascularized gill filaments where dissolved molecular oxygen diffuses into the bloodstream.\nCorrect Choice is (B)."),

    ("State whether True or False: The carbon cycle and the oxygen cycle are intimately interconnected through the opposing chemical reactions of photosynthesis and respiration.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Photosynthesis consumes \\(\\text{CO}_2\\) and produces \\(\\text{O}_2\\); aerobic respiration consumes \\(\\text{O}_2\\) and produces \\(\\text{CO}_2\\).\nCorrect Choice is (A)."),

    ("Which greenhouse gas, produced by anaerobic decomposition of organic matter in flooded paddy fields and cattle enteric fermentation, has a global warming potential 25 times greater than \\(\\text{CO}_2\\)?",
     ["Argon", "Methane (\\(\\text{CH}_4\\))", "Ozone", "Neon"],
     "B", "OSC", "medium",
     "- Methane is a potent short-lived greenhouse gas produced by methanogenic archaea under anaerobic conditions.\nCorrect Choice is (B)."),

    ("What happens to the pH of ocean water when massive excess amounts of atmospheric carbon dioxide dissolve into it?",
     ["The pH rises to 14", "Ocean acidification occurs as dissolved \\(\\text{CO}_2\\) forms carbonic acid (\\(\\text{H}_2\\text{CO}_3\\)), lowering ocean pH and corroding coral reefs", "The ocean solidifies into ice", "Nothing happens"],
     "B", "OSC", "medium",
     "- Ocean acidification diminishes carbonate ion availability, inhibiting shell building in corals and shellfish.\nCorrect Choice is (B)."),

    ("Which aquatic organism performs more than 50% of the entire planet's total oxygenic photosynthesis?",
     ["Giant redwood trees", "Marine phytoplankton and micro-algae floating in the world's oceans", "Grassland prairies", "Mangrove swamps"],
     "B", "OSC", "medium",
     "- Marine phytoplankton generate over half of the biosphere's oxygen budget.\nCorrect Choice is (B)."),

    ("State whether True or False: Nitrogen gas is an inert filler gas that plays no biological role in proteins or DNA.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Nitrogen is an indispensable constituent of all amino acids, proteins, nucleotides, nucleic acids (DNA/RNA), and vitamins.\nCorrect Choice is (B)."),

    ("Which of the following plants does NOT possess root nodules housing Rhizobium?",
     ["Pea plant", "Gram / Chickpea", "Wheat (Triticum aestivum)", "Soybean"],
     "C", "OSC", "easy",
     "- Wheat is a monocot grass and does not form symbiotic root nodules with Rhizobium; only legumes do.\nCorrect Choice is (C)."),

    ("What type of bacterium is Nitrobacter with respect to its nutritional mode?",
     ["Heterotrophic saprophyte", "Chemoautotroph (obtains energy by oxidizing inorganic nitrite to nitrate)", "Photosynthetic plant", "Parasite"],
     "B", "OSC", "hard",
     "- Nitrobacter is a nitrifying chemoautotroph that synthesizes organic nutrients from \\(\\text{CO}_2\\) using chemical oxidation energy.\nCorrect Choice is (B)."),

    # 51-60: Transformations & Biological Cycles
    ("If an agricultural field is heavily waterlogged for months with stagnant water and deprived of oxygen, which microbial process accelerates rapidly?",
     ["Photosynthesis", "Denitrification (Pseudomonas reduces soil nitrates into nitrogen gas, causing soil nitrogen loss)", "Nitrogen fixation", "Combustion"],
     "B", "OSC", "medium",
     "- Waterlogged, oxygen-depleted soils create ideal anaerobic environments for denitrifying bacteria, stripping soil of nitrate fertilizer.\nCorrect Choice is (B)."),

    ("Which of the following is a non-symbiotic blue-green alga (cyanobacterium) that fixes atmospheric nitrogen in flooded paddy fields?",
     ["Anabaena (or Nostoc)", "Spirogyra", "Yeast", "Ulva"],
     "A", "OSC", "medium",
     "- Anabaena and Nostoc are nitrogen-fixing cyanobacteria with specialized thick-walled cells called heterocysts.\nCorrect Choice is (A)."),

    ("The specialized thick-walled cells in cyanobacteria (like Nostoc) that exclude oxygen to allow nitrogenase to fix nitrogen are termed:",
     ["Akinetes", "Heterocysts", "Chloroplasts", "Pyrenoids"],
     "B", "OSC", "hard",
     "- Heterocysts create micro-anaerobic internal environments where oxygen-sensitive nitrogenase functions effectively.\nCorrect Choice is (B)."),

    ("What happens during 'ammonification' in the nitrogen cycle?",
     ["Nitrates are converted to nitrogen gas", "Decomposers break down nitrogen-rich organic proteins from dead organisms into ammonia", "Plants absorb nitrogen gas directly", "Nitrogen reacts with oxygen in lightning"],
     "B", "OSC", "easy",
     "- Ammonification converts complex nitrogenous organic debris into inorganic ammonia/ammonium ions.\nCorrect Choice is (B)."),

    ("What form of nitrogen is primarily absorbed by the root systems of higher flowering plants?",
     ["Gaseous nitrogen (\\(\\text{N}_2\\))", "Nitrate ions (\\(\\text{NO}_3^-\\)) and Ammonium ions (\\(\\text{NH}_4^+\\))", "Solid protein powder", "Nitrogen dioxide gas"],
     "B", "OSC", "easy",
     "- Plant root transporter proteins primarily absorb soluble nitrate (\\(\\text{NO}_3^-\\)) and ammonium (\\(\\text{NH}_4^+\\)) ions from soil water.\nCorrect Choice is (B)."),

    ("Fill in the blank: The atmospheric layer that contains the high-concentration protective ozone layer is the _______.",
     ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
     "B", "OFB", "easy",
     "- The ozone layer is situated in the lower stratosphere, between approximately 15 and 35 km altitude.\nCorrect Choice is (B)."),

    ("What is the chemical formula of an Ozone molecule?",
     ["\\(\\text{O}\\)", "\\(\\text{O}_2\\)", "\\(\\text{O}_3\\)", "\\(\\text{O}_4\\)"],
     "C", "OSC", "easy",
     "- Ozone is an allotrope of oxygen consisting of three oxygen atoms: \\(\\text{O}_3\\).\nCorrect Choice is (C)."),

    ("Which international treaty, signed in 1987, successfully phased out the production of ozone-depleting chlorofluorocarbons (CFCs)?",
     ["The Kyoto Protocol", "The Montreal Protocol", "The Paris Agreement", "The Geneva Convention"],
     "B", "OSC", "medium",
     "- The Montreal Protocol is recognized as the most successful global environmental agreement, healing the stratospheric ozone layer.\nCorrect Choice is (B)."),

    ("Why is ground-level (tropospheric) ozone considered a dangerous pollutant, while stratospheric ozone is life-saving?",
     ["Tropospheric ozone cools the air", "Ground-level ozone is a powerful toxic oxidant that causes respiratory distress in humans and damages plant tissues; stratospheric ozone shields UV radiation", "Both are harmless", "Stratospheric ozone causes asthma"],
     "B", "OSC", "medium",
     "- 'Good up high, bad nearby': Stratospheric ozone blocks solar UV; tropospheric ozone is a caustic secondary pollutant in photochemical smog.\nCorrect Choice is (B)."),

    ("State whether True or False: Forest trees act as major 'carbon sinks' by sequestering atmospheric carbon into stable cellulose and lignin wood biomass for centuries.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Forest biomass locks up gigatons of carbon, mitigating greenhouse gas concentrations.\nCorrect Choice is (A)."),

    # 61-70: Ten Additional Practice Questions
    ("What percentage of total global carbon is stored in the oceans as dissolved carbonate and bicarbonate ions?",
     ["Less than 1%", "More than 70% of total active carbon pool", "Exactly 5%", "0%"],
     "B", "OSC", "medium",
     "- Oceans represent the largest active carbon pool, storing over 70% of circulating carbon.\nCorrect Choice is (B)."),

    ("Which form of oxygen is essential for aerobic respiration in animals and humans?",
     ["Ozone (\\(\\text{O}_3\\))", "Molecular oxygen (\\(\\text{O}_2\\))", "Monatomic oxygen (O)", "Hydrogen peroxide"],
     "B", "OSC", "easy",
     "- Diatomic molecular oxygen (\\(\\text{O}_2\\)) is inhaled and utilized as the terminal electron acceptor in cellular respiration.\nCorrect Choice is (B)."),

    ("How do volcanic eruptions contribute to the global carbon cycle?",
     ["They consume CO₂", "They vent carbon dioxide stored deep within molten mantle rocks into the atmosphere", "They turn CO₂ into ice", "They produce oxygen"],
     "B", "OSC", "easy",
     "- Volcanic degassing releases geological carbon from the Earth's interior into atmospheric circulation.\nCorrect Choice is (B)."),

    ("In the nitrogen cycle, which process transforms animal excreta like urea into ammonia?",
     ["Denitrification", "Ammonification", "Nitrification", "Assimilation"],
     "B", "OSC", "easy",
     "- Urease-producing bacteria hydrolyze urea from animal urine into ammonia and \\(\\text{CO}_2\\).\nCorrect Choice is (B)."),

    ("State whether True or False: Leguminous plants enrich the soil with nitrogen, while cereal crops tend to deplete soil nitrogen.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Symbiotic Rhizobium in legumes fixes atmospheric nitrogen, whereas non-legume cereals extract available soil nitrates.\nCorrect Choice is (A)."),

    ("What is 'carbon footprint'?",
     ["The size of a shoe made of coal", "The total amount of greenhouse gases (mainly \\(\\text{CO}_2\\)) emitted directly or indirectly by an individual, organization, or activity", "A fossilized dinosaur footprint", "The depth of a coal mine"],
     "B", "OSC", "easy",
     "- A carbon footprint measures cumulative greenhouse gas emissions expressed in equivalent metric tons of \\(\\text{CO}_2\\).\nCorrect Choice is (B)."),

    ("Which microbial genus contains free-living anaerobic nitrogen-fixing bacteria in waterlogged soil?",
     ["Clostridium", "Nitrosomonas", "Nitrobacter", "Yeast"],
     "A", "OSC", "hard",
     "- Clostridium pasteurianum is a classic obligate anaerobic free-living nitrogen-fixing soil bacterium.\nCorrect Choice is (A)."),

    ("What is the primary product absorbed by plants when ammonium fertilizers are applied to agricultural soil?",
     ["Nitrogen gas", "Ammonium ions and nitrates formed after bacterial nitrification", "Ozone", "Methane"],
     "B", "OSC", "easy",
     "- Soil nitrifiers convert applied ammonium into soluble nitrate ions which are readily absorbed by plant roots.\nCorrect Choice is (B)."),

    ("Why is burning plastic waste hazardous to the atmospheric oxygen and carbon balance?",
     ["It produces pure oxygen", "It consumes atmospheric oxygen, emits toxic chlorinated dioxins, furans, and excess \\(\\text{CO}_2\\), and pollutes the air", "It absorbs solar light completely", "It freezes the soil"],
     "B", "OSC", "easy",
     "- Plastic incineration consumes \\(\\text{O}_2\\), emits copious \\(\\text{CO}_2\\), and releases persistent carcinogenic toxic compounds.\nCorrect Choice is (B)."),

    ("Which natural phenomenon acts as a primary terrestrial carbon sink on a global scale?",
     ["Paved highway networks", "Dense tropical rainforests (such as the Amazon basin) and boreal forests", "Open coal mines", "Concrete buildings"],
     "B", "OSC", "easy",
     "- Vast forest ecosystems sequester millions of tons of atmospheric carbon in wood trunks, foliage, and root humus.\nCorrect Choice is (B).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Complete Global Carbon Cycle
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="95" y="22" fill="#38bdf8" font-size="13" font-weight="bold">The Global Carbon Cycle</text>
  <!-- Atmospheric Pool -->
  <rect x="110" y="42" width="150" height="32" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="120" y="62" fill="#38bdf8" font-size="10" font-weight="bold">Atmospheric CO₂ Pool</text>
  <!-- Photosynthesis (Downward arrow) -->
  <line x1="130" y1="74" x2="80" y2="120" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="35" y="95" fill="#34d399" font-size="8.5">Photosynthesis (Plants)</text>
  <!-- Respiration (Upward arrow) -->
  <line x1="95" y1="120" x2="145" y2="74" stroke="#f43f5e" stroke-width="2.5"/>
  <text x="115" y="105" fill="#f87171" font-size="8.5">Respiration</text>
  <!-- Plant & Animal Biomass -->
  <rect x="25" y="120" width="110" height="40" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="136" fill="#34d399" font-size="9" font-weight="bold">Living Biomass</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8">Plants & Animals</text>
  <!-- Combustion (Upward arrow) -->
  <line x1="280" y1="120" x2="230" y2="74" stroke="#f97316" stroke-width="2.5"/>
  <text x="260" y="95" fill="#fb923c" font-size="8.5">Combustion</text>
  <!-- Fossil Fuels Box -->
  <rect x="235" y="120" width="110" height="40" fill="#1e293b" stroke="#f97316" rx="4"/>
  <text x="245" y="136" fill="#fb923c" font-size="9" font-weight="bold">Fossil Fuels ⛽</text>
  <text x="245" y="150" fill="#cbd5e1" font-size="8">Coal, Oil, Natural Gas</text>
  <!-- Burial / Sequestration arrow -->
  <path d="M 80,160 Q 180,200 280,160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2" fill="none"/>
  <text x="110" y="185" fill="#cbd5e1" font-size="8">Geological burial over millions of yrs</text>
  <text x="45" y="210" fill="#fde047" font-size="9.5">Dynamic balance between photosynthetic uptake and respiration/combustion</text>
</svg>
</div>
In the global carbon cycle shown above, which single process is responsible for removing carbon dioxide from the atmospheric pool and fixing it into organic molecules?""",
     ["Volcanic eruption", "Photosynthesis by green plants and phytoplankton", "Combustion of fossil fuels", "Animal cellular respiration"],
     "B", "OSC", "easy",
     "- Photosynthesis is the sole biological mechanism capable of fixing inorganic atmospheric \\(\\text{CO}_2\\) into organic biomass.\nCorrect Choice is (B)."),

    # 72: Complete Nitrogen Cycle Sequence
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="90" y="22" fill="#38bdf8" font-size="13" font-weight="bold">The Global Nitrogen Cycle</text>
  <!-- Atmospheric Pool (N2) -->
  <rect x="110" y="38" width="150" height="26" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="120" y="55" fill="#38bdf8" font-size="9.5" font-weight="bold">Atmospheric N₂ (78%)</text>
  <!-- Nitrogen Fixation Arrow Down -->
  <line x1="120" y1="64" x2="60" y2="95" stroke="#10b981" stroke-width="2"/>
  <text x="20" y="80" fill="#34d399" font-size="8">N₂ Fixation (Rhizobium)</text>
  <!-- Ammonia / Ammonium -->
  <rect x="15" y="95" width="100" height="30" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="25" y="114" fill="#34d399" font-size="9" font-weight="bold">Ammonia (NH₃ / NH₄⁺)</text>
  <!-- Nitrification Step 1 -->
  <line x1="115" y1="110" x2="160" y2="110" stroke="#facc15" stroke-width="2"/>
  <text x="120" y="104" fill="#fde047" font-size="7">Nitrosomonas</text>
  <!-- Nitrites -->
  <rect x="160" y="95" width="85" height="30" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="175" y="114" fill="#facc15" font-size="9" font-weight="bold">Nitrite (NO₂⁻)</text>
  <!-- Nitrification Step 2 -->
  <line x1="245" y1="110" x2="280" y2="110" stroke="#38bdf8" stroke-width="2"/>
  <text x="248" y="104" fill="#38bdf8" font-size="7">Nitrobacter</text>
  <!-- Nitrates -->
  <rect x="280" y="95" width="80" height="30" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="290" y="114" fill="#38bdf8" font-size="9" font-weight="bold">Nitrate (NO₃⁻)</text>
  <!-- Denitrification Arrow Back Up -->
  <path d="M 320,95 Q 320,60 260,50" stroke="#f43f5e" stroke-width="2" fill="none"/>
  <text x="285" y="70" fill="#f87171" font-size="8">Denitrification</text>
  <!-- Plant Assimilation -->
  <text x="260" y="150" fill="#34d399" font-size="8">➔ Absorbed by Plant Roots</text>
  <text x="45" y="185" fill="#cbd5e1" font-size="8.5">- Ammonification: Decomposers turn dead proteins back to NH₃</text>
  <text x="45" y="205" fill="#fde047" font-size="9.5">Bacterial transformations drive every essential step of the cycle</text>
</svg>
</div>
In the nitrogen cycle diagram, which bacterium catalyzes the conversion of Nitrite (\\(\\text{NO}_2^-\\)) into Nitrate (\\(\\text{NO}_3^-\\)) so that plant roots can assimilate it?""",
     ["Rhizobium", "Nitrosomonas", "Nitrobacter", "Pseudomonas"],
     "C", "OSC", "medium",
     "- Nitrobacter performs the second stage of nitrification, oxidizing nitrite into plant-absorbable nitrate (\\(\\text{NO}_3^-\\)).\nCorrect Choice is (C)."),

    # 73: Legume Root Nodules & Rhizobium
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Symbiotic Root Nodule (Rhizobium)</text>
  <!-- Main Root -->
  <line x1="80" y1="50" x2="80" y2="180" stroke="#ca8a04" stroke-width="4"/>
  <!-- Lateral Rootlets -->
  <line x1="80" y1="90" x2="150" y2="110" stroke="#ca8a04" stroke-width="2"/>
  <line x1="80" y1="130" x2="160" y2="145" stroke="#ca8a04" stroke-width="2"/>
  <!-- Pink Nodules -->
  <ellipse cx="140" cy="108" rx="14" ry="10" fill="#fb7185" stroke="#e11d48" stroke-width="1.5"/>
  <ellipse cx="155" cy="143" rx="14" ry="10" fill="#fb7185" stroke="#e11d48" stroke-width="1.5"/>
  <ellipse cx="80" cy="115" rx="12" ry="9" fill="#fb7185" stroke="#e11d48" stroke-width="1.5"/>
  <!-- Zoom In Annotation Box -->
  <rect x="180" y="55" width="145" height="110" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="190" y="75" fill="#fb7185" font-size="9.5" font-weight="bold">Inside the Pink Nodule:</text>
  <text x="190" y="92" fill="#cbd5e1" font-size="8.5">- Rhizobium bacteroids</text>
  <text x="190" y="105" fill="#fde047" font-size="8.5">- Nitrogenase enzyme</text>
  <text x="190" y="120" fill="#fb7185" font-size="8.5">- Leghemoglobin (Pink)</text>
  <text x="190" y="135" fill="#cbd5e1" font-size="7.5">  scavenges O₂ to protect</text>
  <text x="190" y="146" fill="#cbd5e1" font-size="7.5">  nitrogenase from oxygen</text>
  <text x="45" y="195" fill="#34d399" font-size="9.5">Symbiosis: Plant gives carbs; Bacterium gives fixed nitrates</text>
</svg>
</div>
Why are healthy, actively nitrogen-fixing root nodules of pea and bean plants distinctly pink or red on the inside when sliced open?""",
     ["Because they are filled with blood",
      "Because they contain leghemoglobin, an oxygen-binding pigment that protects the nitrogenase enzyme from oxygen poisoning",
      "Because the plant absorbs red dye from soil",
      "Because bacteria have red eyes"],
     "B", "OSC", "medium",
     "- Leghemoglobin is a pink heme-protein that scavenges free oxygen, creating an anaerobic niche for nitrogenase activity.\nCorrect Choice is (B)."),

    # 74: Nitrification Two-step Pathway
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">The Two-Step Nitrification Mechanism</text>
  <!-- Step 1 Box -->
  <rect x="25" y="45" width="290" height="52" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="35" y="65" fill="#facc15" font-size="9.5" font-weight="bold">STEP 1: Ammonia ➔ Nitrite</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8.5">2NH₃ + 3O₂ ➔ 2NO₂⁻ + 2H⁺ + 2H₂O</text>
  <text x="35" y="92" fill="#fde047" font-size="8.5" font-weight="bold">Bacterium: Nitrosomonas / Nitrosococcus</text>
  <!-- Step 2 Box -->
  <rect x="25" y="110" width="290" height="52" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="130" fill="#38bdf8" font-size="9.5" font-weight="bold">STEP 2: Nitrite ➔ Nitrate</text>
  <text x="35" y="145" fill="#cbd5e1" font-size="8.5">2NO₂⁻ + O₂ ➔ 2NO₃⁻</text>
  <text x="35" y="157" fill="#38bdf8" font-size="8.5" font-weight="bold">Bacterium: Nitrobacter</text>
  <text x="45" y="185" fill="#34d399" font-size="9.5">NO₃⁻ (Nitrate) is the primary form absorbed by root hair transporters</text>
</svg>
</div>
Which bacterium is responsible for carrying out Step 1 (oxidizing toxic ammonia into nitrite) in soil nitrification?""",
     ["Nitrobacter", "Nitrosomonas", "Rhizobium", "Pseudomonas"],
     "B", "OSC", "easy",
     "- Nitrosomonas catalyzes the first step of nitrification, oxidizing ammonia to nitrite.\nCorrect Choice is (B)."),

    # 75: Atmospheric Nitrogen Fixation via Lightning
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Atmospheric Fixation via Lightning</text>
  <!-- Thundercloud -->
  <ellipse cx="90" cy="65" rx="50" ry="22" fill="#475569"/>
  <!-- Lightning Bolt -->
  <path d="M 90,85 L 75,115 L 95,115 L 80,155" stroke="#fde047" stroke-width="3" fill="none"/>
  <text x="15" y="125" fill="#fde047" font-size="9" font-weight="bold">⚡ High Temp</text>
  <!-- Reaction Box -->
  <rect x="150" y="45" width="175" height="115" fill="#1e293b" stroke="#fde047" rx="4"/>
  <text x="160" y="65" fill="#fde047" font-size="9" font-weight="bold">1. N₂ + O₂ ➔ 2NO</text>
  <text x="160" y="80" fill="#cbd5e1" font-size="8">Nitric oxide formed in spark</text>
  <text x="160" y="98" fill="#fde047" font-size="9" font-weight="bold">2. 2NO + O₂ ➔ 2NO₂</text>
  <text x="160" y="112" fill="#cbd5e1" font-size="8">Nitrogen dioxide gas</text>
  <text x="160" y="130" fill="#38bdf8" font-size="9" font-weight="bold">3. 4NO₂ + 2H₂O + O₂</text>
  <text x="175" y="145" fill="#38bdf8" font-size="8">➔ 4HNO₃ (Dissolves in rain)</text>
  <text x="45" y="185" fill="#34d399" font-size="9.5">Rain carries natural nitrates to enrich soil fertility</text>
</svg>
</div>
How does an intense lightning thunderstorm physically fix inert atmospheric nitrogen into soil fertilizer?""",
     ["Lightning freezes water into ice",
      "The massive electric spark provides extreme thermal energy to force inert N₂ and O₂ to bond, forming nitrogen oxides that dissolve in rain as nitric acid",
      "Lightning kills all bacteria",
      "Thunder pushes nitrogen into earthworm holes"],
     "B", "OSC", "easy",
     "- Lightning provides the high activation energy required to break the \\(\\text{N}\\equiv\\text{N}\\) triple bond, forming nitrogen oxides that fall as nitrates in rain.\nCorrect Choice is (B)."),

    # 76: Stratospheric Ozone Formation & Shield
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Stratospheric Ozone Umbrella (O₃)</text>
  <!-- Solar UV -->
  <line x1="45" y1="50" x2="110" y2="85" stroke="#f43f5e" stroke-width="3"/>
  <text x="35" y="45" fill="#f87171" font-size="9" font-weight="bold">Lethal UV-B / UV-C</text>
  <!-- Ozone Layer -->
  <rect x="25" y="90" width="290" height="35" fill="#0284c7" opacity="0.7" rx="4"/>
  <text x="100" y="112" fill="#ffffff" font-size="11" font-weight="bold">OZONE LAYER (O₃)</text>
  <!-- Blocked UV rays -->
  <path d="M 170,90 Q 185,70 200,90" stroke="#f43f5e" stroke-width="2" fill="none"/>
  <!-- Biosphere below -->
  <rect x="25" y="150" width="290" height="30" fill="#15803d" opacity="0.6" rx="4"/>
  <text x="115" y="170" fill="#f0fdf4" font-size="10" font-weight="bold">TERRESTRIAL BIOSPHERE</text>
  <text x="35" y="140" fill="#34d399" font-size="8.5">Harmless visible sunlight passes through safely</text>
  <text x="45" y="198" fill="#fde047" font-size="9">Ozone protects against cellular DNA mutations and skin cancer</text>
</svg>
</div>
What harmful radiation from the Sun is selectively absorbed and filtered out by the stratospheric ozone layer?""",
     ["Visible green light", "Harmful Ultraviolet (UV) radiation", "Radio waves", "Infrared heat waves"],
     "B", "OSC", "easy",
     "- Stratospheric ozone absorbs short-wavelength, high-energy UV radiation (UV-B and UV-C) that causes DNA mutations.\nCorrect Choice is (B)."),

    # 77: Greenhouse Effect & Carbon Imbalance
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Enhanced Greenhouse Effect Mechanism</text>
  <!-- Solar Input -->
  <line x1="45" y1="45" x2="85" y2="135" stroke="#fde047" stroke-width="2.5"/>
  <text x="30" y="40" fill="#fde047" font-size="8">Solar visible light</text>
  <!-- Earth Surface -->
  <rect x="25" y="135" width="290" height="25" fill="#334155" rx="3"/>
  <text x="135" y="152" fill="#cbd5e1" font-size="9" font-weight="bold">Earth's Surface</text>
  <!-- Terrestrial IR Re-radiation -->
  <line x1="120" y1="135" x2="160" y2="85" stroke="#ef4444" stroke-width="2.5"/>
  <text x="125" y="75" fill="#f87171" font-size="8">Infrared Heat (IR)</text>
  <!-- Greenhouse Blanket -->
  <rect x="150" y="70" width="160" height="30" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="160" y="88" fill="#fbbf24" font-size="9" font-weight="bold">CO₂ & CH₄ Blanket</text>
  <!-- Trapped IR Reflected Back -->
  <line x1="230" y1="100" x2="250" y2="135" stroke="#ef4444" stroke-width="2.5"/>
  <text x="210" y="125" fill="#ef4444" font-size="7.5">Heat reflected back</text>
  <text x="45" y="185" fill="#fde047" font-size="9.5">Anthropogenic CO₂ release traps excess heat, raising global temperatures</text>
</svg>
</div>
How does an increasing concentration of carbon dioxide in the atmosphere cause global planetary warming?""",
     ["By blocking cold winds from space",
      "By absorbing outgoing terrestrial infrared heat and radiating it back toward Earth rather than letting it escape to space",
      "By producing fire inside clouds",
      "By reflecting visible sunlight away from Earth"],
     "B", "OSC", "easy",
     "- Greenhouse gases are transparent to incoming shortwave solar light but absorb outgoing longwave infrared radiation, trapping heat.\nCorrect Choice is (B)."),

    # 78: Denitrification: Closing the Nitrogen Loop
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Denitrification: Soil to Atmosphere</text>
  <!-- Soil Nitrate Pool -->
  <rect x="25" y="60" width="110" height="40" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="80" fill="#38bdf8" font-size="9" font-weight="bold">Soil Nitrates</text>
  <text x="35" y="94" fill="#cbd5e1" font-size="8">(NO₃⁻ & NO₂⁻)</text>
  <!-- Denitrifying Bacteria Arrow -->
  <line x1="135" y1="80" x2="200" y2="80" stroke="#f43f5e" stroke-width="2.5"/>
  <text x="140" y="72" fill="#f87171" font-size="8">Pseudomonas</text>
  <!-- Atmosphere Box -->
  <rect x="200" y="60" width="115" height="40" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="210" y="80" fill="#34d399" font-size="9" font-weight="bold">Atmosphere</text>
  <text x="210" y="94" fill="#cbd5e1" font-size="8">Elemental N₂ gas</text>
  <!-- Waterlogged condition -->
  <rect x="35" y="125" width="270" height="50" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="45" y="145" fill="#fbbf24" font-size="9" font-weight="bold">Triggered by Anaerobic / Waterlogged Soil:</text>
  <text x="45" y="160" fill="#cbd5e1" font-size="8">Bacteria use nitrate as oxygen substitutes, releasing N₂ back into air</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Prevents all nitrogen on Earth from becoming permanently locked in soil</text>
</svg>
</div>
What vital ecological balance is maintained by denitrifying bacteria in the nitrogen cycle?""",
     ["They make water salty",
      "They return elemental nitrogen gas back to the atmospheric reservoir, preventing all global nitrogen from remaining trapped in soil minerals",
      "They turn soil into gold",
      "They absorb carbon dioxide"],
     "B", "OSC", "easy",
     "- Denitrification maintains equilibrium by recycling fixed nitrates back to gaseous \\(\\text{N}_2\\) in the atmosphere.\nCorrect Choice is (B)."),

    # 79: Gaseous vs Sedimentary Cycle Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Gaseous vs Sedimentary Cycles</text>
  <!-- Gaseous Cycles -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="70" fill="#38bdf8" font-size="10" font-weight="bold">GASEOUS CYCLES</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8.5">- Reservoir: Atmosphere</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8.5">- Highly rapid & dynamic</text>
  <text x="35" y="120" fill="#cbd5e1" font-size="8.5">- Global circulation</text>
  <text x="35" y="145" fill="#fde047" font-size="9" font-weight="bold">e.g. C, N, O cycles</text>
  <!-- Sedimentary Cycles -->
  <rect x="180" y="50" width="135" height="120" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="70" fill="#fbbf24" font-size="10" font-weight="bold">SEDIMENTARY</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8.5">- Reservoir: Lithosphere</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="8.5">- Sluggish, slow cycling</text>
  <text x="190" y="120" fill="#cbd5e1" font-size="8.5">- Involves rock weathering</text>
  <text x="190" y="145" fill="#fde047" font-size="9" font-weight="bold">e.g. Phosphorus, Sulfur</text>
  <text x="45" y="195" fill="#34d399" font-size="9.5">Reservoir location distinguishes the two fundamental types</text>
</svg>
</div>
Which biogeochemical cycle is categorized as a Sedimentary Cycle because its main natural reservoir lies in rock formations of the Earth's crust rather than the atmosphere?""",
     ["Carbon cycle", "Nitrogen cycle", "Phosphorus cycle", "Oxygen cycle"],
     "C", "OSC", "easy",
     "- Phosphorus does not form a stable atmospheric gas; its reservoir resides in rock mineral phosphate deposits (sedimentary cycle).\nCorrect Choice is (C)."),

    # 80: Interlocking of Carbon, Oxygen and Nitrogen Cycles
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Interlocking of Biogeochemical Cycles</text>
  <!-- Carbon Circle -->
  <circle cx="110" cy="90" r="38" fill="#15803d" opacity="0.5" stroke="#22c55e" stroke-width="2"/>
  <text x="95" y="75" fill="#4ade80" font-size="9" font-weight="bold">Carbon</text>
  <!-- Oxygen Circle -->
  <circle cx="230" cy="90" r="38" fill="#0369a1" opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
  <text x="215" y="75" fill="#38bdf8" font-size="9" font-weight="bold">Oxygen</text>
  <!-- Nitrogen Circle -->
  <circle cx="170" cy="140" r="38" fill="#a16207" opacity="0.5" stroke="#facc15" stroke-width="2"/>
  <text x="155" y="155" fill="#fde047" font-size="9" font-weight="bold">Nitrogen</text>
  <!-- Central Intersection -->
  <text x="150" y="105" fill="#ffffff" font-size="9" font-weight="bold">DNA &</text>
  <text x="145" y="117" fill="#ffffff" font-size="9" font-weight="bold">Proteins</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="9">All major life cycles merge to synthesize living protoplasm</text>
</svg>
</div>
What vital organic macromolecules inside every living cell are synthesized through the simultaneous convergence of the Carbon, Oxygen, and Nitrogen cycles?""",
     ["Pure gold nuggets", "Proteins and Nucleic Acids (DNA & RNA)", "Glass fibers", "Plastic bottles"],
     "B", "OSC", "easy",
     "- Amino acids (proteins) and nucleotides (DNA/RNA) contain carbon, oxygen, hydrogen, and nitrogen atoms working in concert.\nCorrect Choice is (B)."),

    # 81: Ocean as Colossal Carbon Sink
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Oceans: The Planetary Carbon Sink</text>
  <!-- Atmosphere -->
  <rect x="25" y="45" width="290" height="30" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="35" y="64" fill="#38bdf8" font-size="9">Atmosphere: CO₂ Gas</text>
  <!-- Ocean Dissolution Arrow -->
  <line x1="170" y1="75" x2="170" y2="105" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <!-- Ocean Water -->
  <rect x="25" y="105" width="290" height="70" fill="#0c4a6e" rx="3"/>
  <text x="35" y="125" fill="#bae6fd" font-size="9" font-weight="bold">Dissolved Bicarbonate Ions (HCO₃⁻)</text>
  <text x="35" y="142" fill="#cbd5e1" font-size="8">- Marine phytoplankton photosynthesis</text>
  <text x="35" y="156" fill="#fde047" font-size="8">- Shellfish & corals build CaCO₃ skeletons</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Oceans buffer climate by absorbing ~30% of human CO₂ emissions</text>
</svg>
</div>
How do marine organisms like corals and mollusks permanently store dissolved oceanic carbon?""",
     ["By exhaling it into space",
      "By combining bicarbonate with calcium to construct insoluble Calcium Carbonate (\\(\\text{CaCO}_3\\)) shells and reefs",
      "By turning it into salt",
      "By boiling seawater"],
     "B", "OSC", "easy",
     "- Marine calcifiers synthesize insoluble \\(\\text{CaCO}_3\\) shells that accumulate on the ocean floor to form limestone strata.\nCorrect Choice is (B)."),

    # 82: Summary Diagnostic of Biogeochemical Cycles
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Summary: Planetary Biogeochemical Loops</text>
  <!-- Cycle 1 -->
  <rect x="20" y="42" width="320" height="38" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="30" y="58" fill="#34d399" font-size="9.5" font-weight="bold">1. Carbon Cycle:</text>
  <text x="30" y="72" fill="#cbd5e1" font-size="8.5">Photosynthesis fixes CO₂; Respiration & Combustion return it</text>
  <!-- Cycle 2 -->
  <rect x="20" y="85" width="320" height="38" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="101" fill="#38bdf8" font-size="9.5" font-weight="bold">2. Oxygen Cycle:</text>
  <text x="30" y="115" fill="#cbd5e1" font-size="8.5">Photolysis creates O₂; Respiration consumes it; Stratospheric O₃ protects</text>
  <!-- Cycle 3 -->
  <rect x="20" y="128" width="320" height="42" fill="#1e293b" stroke="#facc15" rx="3"/>
  <text x="30" y="144" fill="#fde047" font-size="9.5" font-weight="bold">3. Nitrogen Cycle:</text>
  <text x="30" y="158" fill="#cbd5e1" font-size="8.5">Fixation ➔ Ammonification ➔ Nitrification ➔ Denitrification</text>
  <text x="45" y="195" fill="#38bdf8" font-size="9.5">Preserves biosphere chemical homeostasis across evolutionary millennia</text>
</svg>
</div>
What overarching ecological principle ensures that the Earth does not run out of carbon, oxygen, or nitrogen despite billions of years of biological consumption?""",
     ["Continuous arrival of elements on meteorites",
      "Biogeochemical cycles continuously recycle and recirculate elements between biotic living tissues and abiotic reservoirs",
      "Earth manufactures new elements inside the mantle",
      "Animals can live without chemicals"],
     "B", "OSC", "easy",
     "- Closed-loop biogeochemical cycling guarantees that identical chemical atoms are reused indefinitely across generations.\nCorrect Choice is (B).")
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

out_file = "scripts/ch7_topic3.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
