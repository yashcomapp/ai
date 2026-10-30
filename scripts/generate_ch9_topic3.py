# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-9-9.3: Scientific Waste Disposal: Composting, Vermicomposting, Incineration, Landfills
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-9-9.3"
OUTPUT_FILE = "scripts/ch9_topic3.json"

exam_data = [
    {
        "q": "What is the biological process of decomposing organic wet waste into dark, nutrient-rich soil conditioner using aerobic microorganisms called?",
        "options": ["Composting", "Pyrolysis", "Incineration", "Landfilling"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Composting is the aerobic microbial decomposition of organic biodegradable waste into nutrient-rich humus (compost) that enriches soil structure."
    },
    {
        "q": "Which earthworm species is most commonly and effectively utilized in vermicomposting systems?",
        "options": ["Eisenia fetida (red wiggler)", "Pheretima posthuma", "Lumbricus terrestris", "Hirudinaria granulosa"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Eisenia fetida (red wiggler) is the premier epigeic earthworm used in vermicomposting due to its rapid reproduction and high consumption rate of organic waste."
    },
    {
        "q": "What is the primary function of the high-density polyethylene (HDPE) geomembrane liner installed at the bottom of a sanitary landfill?",
        "options": [
            "To form an impermeable barrier preventing toxic leachate from contaminating underlying groundwater",
            "To keep the landfill warm during winter",
            "To conduct electricity across the landfill",
            "To attract burrowing rodents to decompose plastic"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The HDPE geomembrane combined with a compacted clay liner forms an impermeable barrier that catches leachate and stops it from percolating into aquifers."
    },
    {
        "q": "At what typical temperature does the secondary combustion chamber of a modern biomedical waste incinerator operate to ensure complete destruction of hazardous toxins and pathogens?",
        "options": ["1050 deg C to 1100 deg C", "100 deg C to 150 deg C", "300 deg C to 400 deg C", "2500 deg C to 3000 deg C"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Secondary chambers in medical waste incinerators must maintain temperatures between 1050 deg C and 1100 deg C with a minimum 2-second gas residence time to destroy dioxins and furans."
    },
    {
        "q": "What is the thermal degradation of organic matter and plastic waste at high temperatures in the strict absence of oxygen called?",
        "options": ["Pyrolysis", "Aerobic composting", "Sanitary landfilling", "Bioremediation"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Pyrolysis is the thermal cracking of organic polymers at high temperatures (400-800 deg C) in an oxygen-free environment, generating bio-oil, syngas, and biochar."
    },
    {
        "q": "What is the primary combustible gas generated in a biogas plant during the anaerobic digestion of wet organic waste and animal dung?",
        "options": ["Methane (CH4)", "Carbon monoxide (CO)", "Sulfur dioxide (SO2)", "Chlorine (Cl2)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Biogas typically contains 55% to 65% methane (CH4) alongside carbon dioxide, making it a clean, renewable gaseous fuel for cooking and power generation."
    },
    {
        "q": "During aerobic composting of municipal solid waste, the temperature inside the compost pile rises to 55 deg C - 65 deg C during the thermophilic phase. Why is this high temperature beneficial?",
        "options": [
            "It pasteurizes the compost by killing human pathogens and destroying weed seeds",
            "It turns the compost pile into pure metallic ash",
            "It permanently freezes all microbial activity",
            "It evaporates all carbon atoms into outer space"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Thermophilic composting temperatures (55-65 deg C) kill pathogenic bacteria, parasite eggs, and weed seeds, ensuring the resulting organic compost is biologically safe."
    },
    {
        "q": "Why are vertical gas extraction wells drilled into capped sanitary landfills?",
        "options": [
            "To extract and capture methane gas to prevent underground explosions and generate green electricity",
            "To pump municipal drinking water into the landfill",
            "To inject fresh air into deep landfill layers to support birds",
            "To allow rain to enter and dissolve the waste faster"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Landfill gas wells extract methane from anaerobic decomposition, mitigating fire/explosion hazards and greenhouse emissions while harnessing the gas as fuel."
    },
    {
        "q": "Which valuable by-product produced by earthworms during vermicomposting is rich in nitrogen, phosphorus, potassium, and plant growth hormones?",
        "options": ["Worm castings (vermicompost)", "Fly ash", "Slag", "Leachate"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Worm castings (excreta of earthworms) form rich vermicompost, possessing balanced N-P-K ratios, micronutrients, and beneficial soil microbes."
    },
    {
        "q": "What is the liquid bio-fertilizer that drains from vermicomposting beds and is collected to spray on crops as a foliar nutrient spray called?",
        "options": ["Vermiwash", "Leachate", "Black liquor", "Effluent slurry"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Vermiwash is a nutrient- and enzyme-rich liquid extract collected by passing water through active vermicomposting beds, widely used as an organic foliar spray."
    },
    {
        "q": "In an engineered sanitary landfill, why is a daily cover of compacted soil (approx. 15 cm) applied over freshly dumped garbage every evening?",
        "options": [
            "To prevent foul odors, eliminate windblown litter, and deny food access to flies, birds, and rodents",
            "To permanently stop the waste from ever decomposing",
            "To convert the garbage directly into diamond crystals",
            "To prevent trucks from driving across the site"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Daily soil covers seal off odor, control vector infestation (flies, rats, crows), prevent litter dispersion by wind, and minimize rainwater infiltration."
    },
    {
        "q": "What air pollution control device is installed in modern waste incineration plants to capture fine particulate matter and fly ash from flue gases using electrostatic charges?",
        "options": ["Electrostatic Precipitator (ESP)", "Barometer", "Centrifugal water pump", "Mercury thermometer"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Electrostatic Precipitators (ESPs) charge airborne particulate matter electrically and collect the dust on oppositely charged plates, removing over 99% of fly ash."
    },
    {
        "q": "What solid byproduct remaining after pyrolysis of organic biomass acts as a permanent soil amendment that enhances water retention and carbon sequestration?",
        "options": ["Biochar", "Thermocol", "Slag", "Fly ash"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Biochar is a highly porous, stable carbon-rich material produced via pyrolysis that improves soil moisture retention and sequesters carbon for centuries."
    },
    {
        "q": "Why is open dumping of mixed waste on unlined riverbeds strictly prohibited by environmental laws?",
        "options": [
            "It causes severe water pollution, groundwater poisoning through leachate, and epidemics of vector-borne diseases",
            "It accelerates the speed of river navigation boats",
            "It cools down regional river water temperatures too quickly",
            "It turns river water into solid concrete"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Open dumping contaminates surface and subsurface water supplies with hazardous chemicals and pathogens, triggering waterborne and vector-borne epidemics."
    },
    {
        "q": "Which parameter must be carefully controlled in an aerobic compost pile to prevent it from turning foul-smelling and anaerobic?",
        "options": [
            "Adequate aeration (turning the pile regularly) and proper moisture content (40-60%)",
            "Total exclusion of all atmospheric air and oxygen",
            "Adding heavy doses of synthetic chemical pesticides",
            "Keeping the pile submerged permanently under 5 meters of standing water"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Aerobic composting requires oxygen; turning the pile regularly introduces air, preventing anaerobic decay that generates foul hydrogen sulfide and methane."
    },
    {
        "q": "What is the optimal Carbon-to-Nitrogen (C:N) ratio recommended for rapid and odor-free aerobic composting?",
        "options": ["Approximately 25:1 to 30:1", "1:100", "500:1", "1:1"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Microorganisms require about 30 parts of carbon for energy to 1 part of nitrogen for protein synthesis; a C:N ratio of 25:1 to 30:1 ensures rapid decomposition without nitrogen loss."
    },
    {
        "q": "What is the main advantage of Waste-to-Energy (WtE) mass-burn incineration over landfills for dense urban metropolises with scarce vacant land?",
        "options": [
            "It reduces waste volume by up to 90% while recovering thermal and electrical energy",
            "It generates zero carbon dioxide under all conditions",
            "It requires zero capital cost and zero skilled labor",
            "It transforms plastic directly into edible food grain"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Incineration reduces the volume of solid waste by 85-90% and mass by 70%, which is critical in space-constrained megacities, while generating electricity."
    },
    {
        "q": "Which material is used in wet flue-gas scrubbers in waste incinerators to neutralize acidic gases like sulfur dioxide (SO2) and hydrogen chloride (HCl)?",
        "options": ["Lime (calcium hydroxide / calcium carbonate slurry)", "Concentrated hydrochloric acid", "Liquid petroleum gas", "Pure mercury solution"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Alkaline reagents like lime slurry react with acidic acid-gas pollutants (SO2, HCl, HF) in flue gases, neutralizing them into harmless calcium salts."
    },
    {
        "q": "What happens to the nutrient-rich digested slurry discharged from an agricultural biogas plant?",
        "options": [
            "It is dried and applied to agricultural fields as superior organic bio-fertilizer",
            "It is incinerated as toxic medical waste",
            "It is disposed of in deep sea ocean trenches",
            "It is converted into lead-acid batteries"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Digested biogas slurry contains mineralized nitrogen, phosphorus, and organic matter and serves as excellent organic manure for crops."
    },
    {
        "q": "Which of the following organic wastes should generally be avoided in a backyard vermicomposting bin to prevent odor and pest infestation?",
        "options": ["Excessive dairy, meat scraps, oily curries, and pet feces", "Dry banana peels and fruit scraps", "Crushed eggshells", "Shredded unprinted cardboard"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Meat, dairy, and oils putrefy anaerobically, attract rodents and maggots, and create foul odors that can harm earthworms in vermiculture systems."
    },
    {
        "q": "Select ALL major scientific components of a modern sanitary landfill:",
        "options": [
            "Impermeable bottom clay and geomembrane liner",
            "Perforated leachate collection pipes and treatment sump",
            "Vertical methane gas extraction wells",
            "Open bonfire pits for burning garbage"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Sanitary landfills incorporate impermeable composite liners, leachate drainage systems, and methane recovery wells. Open burning is strictly forbidden."
    },
    {
        "q": "Select ALL key advantages of vermicomposting over chemical chemical fertilizers:",
        "options": [
            "Improves soil water retention and porosity naturally",
            "Supplies micronutrients and beneficial soil microorganisms",
            "Leaves zero toxic chemical residues in groundwater",
            "Contains high concentrations of radioactive uranium"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Vermicompost improves soil physical structure, enhances microbial diversity, and prevents chemical runoff pollution."
    },
    {
        "q": "Select ALL products obtained from the pyrolysis of municipal plastic and biomass waste:",
        "options": [
            "Bio-oil (liquid hydrocarbon fuel)",
            "Syngas (combustible synthetic gas containing H2 and CO)",
            "Biochar (solid carbon residue)",
            "Pure liquid gold"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Pyrolysis yields three fractions: liquid bio-oil, combustible gaseous syngas, and solid carbonaceous biochar."
    },
    {
        "q": "True or False: Vermicomposting requires high temperatures of 80 deg C inside the bed for earthworms to thrive.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Earthworms are sensitive living invertebrates; temperatures above 35 deg C can be fatal to them. Vermicomposting operates at ambient temperatures (20-30 deg C)."
    },
    {
        "q": "True or False: Sanitary landfills are engineered with daily soil covers to control odors and prevent disease-carrying flies from breeding.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Daily soil covering of compacted refuse isolates waste, mitigating odors, vector attraction, and fire risks."
    },
    {
        "q": "True or False: Flue gas scrubbers in modern incinerators use activated carbon injection to capture and remove mercury and dioxins from emissions.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Activated carbon has an immense specific surface area that adsorbs volatile heavy metals like mercury and toxic dioxins from the flue stream."
    },
    {
        "q": "True or False: Leachate collected from landfills can be discharged directly into public rivers without any treatment.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Leachate is heavily laden with toxic organic compounds, heavy metals, and ammonia; it must undergo biological and reverse-osmosis treatment before discharge."
    },
    {
        "q": "Assertion (A): Incineration is the legally mandated treatment method for infectious human anatomical waste.\\nReason (R): High-temperature thermal destruction completely sterilizes pathogens, destroys anatomical tissue, and reduces waste to inert mineral ash.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Medical incineration above 1050 deg C guarantees complete destruction of infectious pathogens, viruses, and anatomical tissues."
    },
    {
        "q": "Assertion (A): Earthworms accelerate the composting rate of organic waste significantly compared to ordinary microbial composting alone.\\nReason (R): Earthworms physically grind organic material in their muscular gizzards and coat it with enzymatic digestive fluids, increasing surface area for bacterial colonization.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Earthworms act as mechanical shredders and biological aerators, processing organic matter into fine, enzyme-coated particles that microbes decompose rapidly."
    },
    {
        "q": "Assertion (A): Biogas plants contribute toward mitigating global climate change.\\nReason (R): Capturing methane from decomposing animal waste prevents potent methane emissions into the atmosphere and displaces fossil fuel usage.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Methane is 28 times more potent as a greenhouse gas than CO2 over 100 years. Harnessing it in biogas plants avoids direct atmospheric release and replaces fossil fuels."
    },
    {
        "q": "Fill in the blank: The specialized earthworm species widely renowned as the 'Red Wiggler' used in vermicomposting is Eisenia ________.",
        "options": ["fetida", "maxima", "indica", "vulgaris"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Eisenia fetida is the scientific binomial name of the red wiggler earthworm."
    },
    {
        "q": "Fill in the blank: The thermal treatment process that combusts waste in excess oxygen at high temperatures is called ________.",
        "options": ["incineration", "pyrolysis", "composting", "fermentation"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Incineration is the controlled combustion of waste in the presence of oxygen."
    },
    {
        "q": "Fill in the blank: In a biogas digester, organic matter is converted into methane and carbon dioxide by anaerobic bacteria known as ________.",
        "options": ["methanogens", "lactobacilli", "rhizobia", "cyanobacteria"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Methanogenic archaea (methanogens) execute the final step of anaerobic digestion, converting acetate, hydrogen, and CO2 into methane gas."
    },
    {
        "q": "Fill in the blank: The liquid collected from vermiculture beds that contains beneficial microbes and water-soluble plant nutrients is called ________.",
        "options": ["vermiwash", "leachate", "slurry", "compost tea"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Vermiwash is the nutrient-laden co-product collected from vermicomposting units."
    },
    {
        "q": "Fill in the blank: The impermeable synthetic plastic membrane sheet laid beneath a sanitary landfill is called a ________.",
        "options": ["geomembrane", "geode", "geotextile", "cellulose sheet"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "An HDPE geomembrane is the synthetic barrier installed in modern sanitary landfills to contain leachate."
    },
    {
        "q": "If 1,000 kg of fresh wet kitchen waste is composted aerobically and yields 250 kg of mature finished compost, what is the finished compost yield percentage?",
        "options": ["25", "10", "50", "75"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Yield % = (250 kg / 1000 kg) * 100 = 25% (the remaining mass is lost as evaporated water and CO2 during decomposition)."
    },
    {
        "q": "If a modern mass-burn incinerator reduces 200 tonnes of municipal combustible waste to 20 tonnes of bottom ash, by what percentage has the mass of the waste been reduced?",
        "options": ["90", "80", "95", "70"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Mass reduction = 200 - 20 = 180 tonnes. Reduction % = (180 / 200) * 100 = 90%."
    },
    {
        "q": "In an agricultural biogas plant producing 100 cubic meters of biogas daily containing 60% methane by volume, what is the volume of pure methane generated per day in cubic meters?",
        "options": ["60", "40", "50", "75"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Methane volume = 100 * 0.60 = 60 cubic meters."
    },
    {
        "q": "Under Indian Central Pollution Control Board (CPCB) standards, what is the minimum thickness in millimeters required for an HDPE geomembrane liner in a sanitary landfill?",
        "options": ["1.5", "0.5", "0.2", "5.0"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "hard",
        "exp": "CPCB regulations mandate a minimum thickness of 1.5 mm for high-density polyethylene (HDPE) geomembrane bottom liners in sanitary landfills."
    },
    {
        "q": "If 1 kg of active red wiggler earthworms consumes approximately 0.5 kg of organic kitchen scraps per day, how many kilograms of earthworms are needed to process 5 kg of scraps daily?",
        "options": ["10", "5", "2", "20"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Earthworms required = 5 kg / 0.5 kg/worm-kg = 10 kg of earthworms."
    }
]

practice_data = [
    {
        "q": "What is the primary role of earthworms in accelerating decomposition during vermicomposting?",
        "options": [
            "Aerating the organic bed by burrowing and excreting microbe-rich castings",
            "Freezing the compost bed to stop bacteria",
            "Absorbing all moisture to keep the bed completely dry",
            "Synthesizing plastic polymers from fruit sugars"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Earthworms aerate the bed through continuous burrowing and break waste into fine particles, inoculating it with beneficial gut microflora."
    },
    {
        "q": "Why is regular turning or forced aeration essential in large-scale windrow composting?",
        "options": [
            "To replenish oxygen and dissipate excessive internal heat and moisture, maintaining aerobic conditions",
            "To ensure the pile stays cold below freezing",
            "To destroy all beneficial aerobic bacteria",
            "To attract stray birds to nest in the compost"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Turning windrows introduces oxygen to maintain aerobic respiration and prevents temperatures from exceeding 65 deg C, which would kill beneficial microbes."
    },
    {
        "q": "What happens to the combustible syngas (mixture of CO and H2) produced during the pyrolysis of plastic waste?",
        "options": [
            "It can be captured and burned as a clean fuel gas to power the pyrolysis heating reactor or generate electricity",
            "It must be pumped into domestic drinking water tanks",
            "It is condensed into solid ice cubes",
            "It is dumped into municipal sewage drains"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Syngas has high calorific value and is recycled to supply process heat for the pyrolysis reactor or utilized in gas engines for power generation."
    },
    {
        "q": "Which of the following is an essential requirement for a well-maintained vermicomposting pit?",
        "options": [
            "Maintaining proper moisture (around 50-60%) and keeping the pit shaded from direct sunlight",
            "Flooding the pit with boiling water daily",
            "Exposing the bed to scorching midday sun",
            "Sprinkling chemical insecticides inside the pit"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Earthworms breathe through their moist skin and are photophobic (averse to light); maintaining 50-60% moisture and shaded conditions is vital."
    },
    {
        "q": "What is the primary disadvantage of disposing of untreated mixed municipal solid waste in unlined open dumps?",
        "options": [
            "Unrestricted generation of toxic leachate, emission of uncontrolled greenhouse gases, and frequent spontaneous dump fires",
            "Excessive production of purified distilled water",
            "Rapid creation of fertile agricultural forests",
            "Complete elimination of all flies and mosquitoes"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Open dumps generate toxic leachate that poisons groundwater, emit methane causing uncontrollable fires, and breed disease vectors."
    },
    {
        "q": "Which type of waste incinerator uses a bed of sand suspended by upward-blowing hot air to burn shredded combustible waste efficiently?",
        "options": ["Fluidized Bed Incinerator", "Rotary Kiln", "Moving Grate", "Single Chamber Pit"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Fluidized bed incinerators suspend hot sand particles in a turbulent air stream, ensuring rapid thermal transfer and uniform combustion at lower NOx emission levels."
    },
    {
        "q": "What is the primary function of a leachate collection system in a modern sanitary landfill?",
        "options": [
            "To channel contaminated percolating liquids through perforated pipes into a dedicated treatment facility",
            "To pump toxic leachate into nearby swimming pools",
            "To spray leachate into municipal drinking fountains",
            "To freeze groundwater aquifers solid"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Leachate pipes collect contaminated liquids above the impermeable liner and pump them to wastewater treatment plants for purification."
    },
    {
        "q": "Which microorganism group performs the first stage of anaerobic digestion in a biogas plant, breaking down complex polymers (proteins, carbohydrates) into simple monomers?",
        "options": ["Hydrolytic bacteria", "Methanogens", "Nitrifying bacteria", "Sulfur-reducing archaebacteria"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Hydrolytic fermentative bacteria secrete extracellular enzymes that break down complex biopolymers into soluble monomers (sugars, amino acids, fatty acids)."
    },
    {
        "q": "What is the primary difference between incineration and pyrolysis?",
        "options": [
            "Incineration is complete combustion in excess oxygen, whereas pyrolysis is thermal degradation in the absence of oxygen",
            "Incineration produces biochar while pyrolysis produces pure ash",
            "Incineration operates at freezing temperatures while pyrolysis operates in direct sunlight",
            "There is no difference; both terms are identical"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Incineration burns waste with oxygen, releasing heat and flue gases; pyrolysis heats waste without oxygen, yielding reusable chemical fuels (bio-oil, syngas, biochar)."
    },
    {
        "q": "What is 'Refuse-Derived Fuel' (RDF) produced from municipal solid waste?",
        "options": [
            "Shredded, dried high-calorific non-recyclable combustible fractions (plastics, paper, textiles) processed into pellets or fluff for industrial boilers/cement kilns",
            "Liquid diesel extracted from sea water",
            "Solid rock extracted from granite quarries",
            "Pure distilled alcohol for pharmaceutical use"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "RDF is produced by segregating, drying, and shredding high-calorific municipal waste fractions for co-processing in cement kilns and power plants."
    },
    {
        "q": "Why is adding lime (CaO or Ca(OH)2) to the flue gas stream of a waste incinerator essential?",
        "options": [
            "To neutralize acidic gases like sulfur dioxide (SO2) and hydrogen chloride (HCl) before release",
            "To ignite the flue gas into a secondary flame",
            "To cool down the stack to room temperature instantly",
            "To turn the exhaust gas completely into liquid water"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Lime reacts chemically with acidic combustion gases (HCl, SO2, HF) to form stable calcium salts that are captured in dust filters."
    },
    {
        "q": "What moisture percentage should be maintained in an active aerobic compost pile?",
        "options": ["40% to 60%", "Less than 5%", "Exactly 100% (flooded)", "0% (completely dry)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Optimal aerobic composting requires 40-60% moisture; below 40% microbial activity slows, while above 60% pores become waterlogged, inducing anaerobiosis."
    },
    {
        "q": "What term describes the biological reclamation of contaminated soil or waste dumps using living plants to absorb heavy metals?",
        "options": ["Phytoremediation", "Pyrolysis", "Incineration", "Sanitary capping"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Phytoremediation uses hyperaccumulating plants (like sunflowers or mustard) to extract, stabilize, or degrade environmental pollutants from soil."
    },
    {
        "q": "What is the purpose of installing a final clay and geomembrane cap over a filled sanitary landfill cell?",
        "options": [
            "To prevent rainwater infiltration that would generate additional leachate, and seal in methane for controlled recovery",
            "To make the landfill surface ready for building high-rise skyscrapers immediately",
            "To allow trees to sink deep taproots into the garbage",
            "To permanently cool the Earth's mantle"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Engineered top capping seals out rainwater, stopping further leachate formation, and traps landfill methane for managed recovery."
    },
    {
        "q": "Which material serves as ideal dry 'brown' carbon-rich bedding in a vermicomposting unit?",
        "options": ["Dry coconut coir, shredded cardboard, and dried leaves", "Fresh meat scraps", "Wet cow dung mixed with toxic pesticides", "Crushed glass bottles"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Coconut coir, dried leaves, and shredded paper provide a carbon-rich, well-aerated, moisture-retentive bedding matrix for earthworms."
    },
    {
        "q": "Select ALL gases commonly found in raw biogas produced from anaerobic waste digesters:",
        "options": [
            "Methane (CH4)",
            "Carbon dioxide (CO2)",
            "Hydrogen sulfide (H2S in trace amounts)",
            "Pure liquid nitrogen"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Raw biogas consists predominantly of methane (55-65%) and CO2 (35-45%), with trace amounts of H2S, moisture, and siloxanes."
    },
    {
        "q": "Select ALL environmental benefits of diverting organic waste from landfills to composting units:",
        "options": [
            "Prevents potent methane greenhouse emissions from anaerobic landfill zones",
            "Prolongs the operational lifespan of municipal landfill capacity",
            "Produces valuable organic fertilizer that restores agricultural soil health",
            "Permanently destroys the Earth's gravity"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Composting diverts massive organic bulk from landfills, curtails fugitive methane emissions, and returns nutrients to topsoil."
    },
    {
        "q": "Select ALL air pollution control systems utilized in modern waste-to-energy incineration facilities:",
        "options": [
            "Electrostatic precipitators (ESPs) or fabric baghouse filters",
            "Dry or wet alkaline lime scrubbers",
            "Activated carbon injection systems for dioxins and mercury",
            "Open atmospheric chimneys without any internal filters"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "State-of-the-art incinerators deploy multi-stage flue treatment: lime scrubbers, activated carbon injection, and fabric baghouse filters."
    },
    {
        "q": "True or False: Biochar produced via pyrolysis has a highly porous microscopic structure that serves as a permanent habitat for beneficial soil microbes.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The high specific surface area and microporosity of biochar provide shelter for soil microorganisms and boost water/nutrient retention."
    },
    {
        "q": "True or False: Feeding non-biodegradable plastics and thermocol to earthworms produces high-grade vermicompost.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Earthworms can only consume biodegradable organic matter. Plastics are indigestible and can choke or poison earthworms."
    },
    {
        "q": "True or False: In a sanitary landfill, leachate collection pipes are laid directly at the bottom above the impermeable liner.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Perforated collection pipes rest in a gravel drainage layer situated directly on top of the geomembrane liner to evacuate leachate."
    },
    {
        "q": "True or False: Wet composting generates temperatures up to 1000 deg C during the thermophilic phase.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Biological composting achieves maximum temperatures between 55 deg C and 65 deg C. Temperatures of 1000 deg C occur only in thermal incinerators."
    },
    {
        "q": "Assertion (A): Capping a decommissioned sanitary landfill with an impermeable multi-layer seal is mandatory.\\nReason (R): The cap prevents rainwater from entering the waste mass, permanently halting fresh leachate production.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Without an impermeable top cap, rainfall continually percolates through buried waste, producing toxic leachate for decades."
    },
    {
        "q": "Assertion (A): Vermicompost contains significantly higher available N, P, and K than ordinary un-composted topsoil.\\nReason (R): Passage of organic waste through the earthworm gut breaks down complex minerals into easily absorbable plant-available ionic forms.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Earthworm intestinal enzymes and microbial mutualists convert bound nitrogen, phosphorus, and potassium into bioavailable nitrates, phosphates, and potash."
    },
    {
        "q": "Fill in the blank: The thermal process that breaks down shredded waste plastics into fuel gases and liquid hydrocarbons in an oxygen-free chamber is ________.",
        "options": ["pyrolysis", "incineration", "calcination", "composting"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Pyrolysis operates strictly in the absence of oxygen to convert waste polymers into fuel fractions."
    },
    {
        "q": "Fill in the blank: The gaseous fuel consisting primarily of methane generated from anaerobic digestion of organic matter in rural villages is known as ________ gas.",
        "options": ["biogas (gobar gas)", "water gas", "coal gas", "producer gas"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Biogas (often termed Gobar gas in rural India when derived from cow dung) provides renewable thermal energy."
    },
    {
        "q": "Fill in the blank: The temperature range of ________ deg C to 65 deg C during the thermophilic stage of aerobic composting is crucial for destroying plant pathogens and weed seeds.",
        "options": ["55", "30", "15", "85"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "The thermophilic stage operates between 55 deg C and 65 deg C, sanitizing the compost pile."
    },
    {
        "q": "Fill in the blank: Fabric filters installed in industrial incinerator baghouses remove microscopic particles of ________ ash from flue gases.",
        "options": ["fly", "bottom", "volcanic", "wood"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Fly ash refers to the fine, light particulate ash entrained in flue gas streams, captured by fabric baghouses."
    },
    {
        "q": "If an earthworm population in a 2-meter vermicomposting pit consumes 4 kg of wet kitchen waste each day, how many kilograms of waste do they convert over a 90-day composting cycle?",
        "options": ["360", "180", "450", "270"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total waste processed = 4 kg/day * 90 days = 360 kg."
    },
    {
        "q": "If an engineered landfill gas collection well extracts 50 cubic meters of methane per hour, how many cubic meters of methane are captured in a full 24-hour day?",
        "options": ["1200", "600", "2400", "1000"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Methane extracted = 50 m^3/hr * 24 hr = 1,200 cubic meters."
    }
]

svg_diagrams = [
    # SVG 1: Sanitary Landfill Cross-Section
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Cross-Section of an Engineered Sanitary Landfill</text>
  <!-- Top Cap -->
  <path d="M 60 80 Q 250 50 440 80 L 440 90 Q 250 60 60 90 Z" fill="#15803d"/>
  <text x="250" y="68" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Vegetation &amp; Top Clay Cap</text>
  <!-- Waste Compaction Layers -->
  <rect x="60" y="90" width="380" height="70" fill="#78350f" stroke="#b45309"/>
  <text x="250" y="115" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Compacted Waste Layers + Daily Soil Cover</text>
  <!-- Vertical Methane Gas Well -->
  <line x1="200" y1="50" x2="200" y2="160" stroke="#f59e0b" stroke-width="4"/>
  <text x="200" y="44" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Methane Extraction Well</text>
  <!-- Leachate Drainage Pipes -->
  <rect x="60" y="160" width="380" height="15" fill="#334155"/>
  <circle cx="120" cy="167" r="5" fill="#38bdf8"/>
  <circle cx="250" cy="167" r="5" fill="#38bdf8"/>
  <circle cx="380" cy="167" r="5" fill="#38bdf8"/>
  <text x="250" y="188" fill="#38bdf8" font-size="9" text-anchor="middle">Perforated Leachate Collection Pipes</text>
  <!-- Impermeable HDPE Geomembrane & Compacted Clay -->
  <line x1="60" y1="175" x2="440" y2="175" stroke="#ef4444" stroke-width="3"/>
  <rect x="60" y="178" width="380" height="20" fill="#92400e"/>
  <text x="250" y="210" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">HDPE Geomembrane (1.5mm) + Compacted Clay Liner</text>
</svg>''',

    # SVG 2: Vermicomposting Pit
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Anatomy of a Vermicomposting Bed (Eisenia fetida)</text>
  <!-- Brick Pit Outline -->
  <rect x="60" y="45" width="380" height="155" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- Top: Moist gunny bag cover -->
  <rect x="70" y="52" width="360" height="12" fill="#713f12" rx="2"/>
  <text x="250" y="62" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Moist Gunny Bag Cover (Maintains Darkness &amp; Humidity)</text>
  <!-- Layer 1: Bio-waste & Earthworms -->
  <rect x="70" y="68" width="360" height="55" fill="#14532d"/>
  <text x="250" y="88" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Organic Kitchen Waste + Earthworms (Eisenia fetida)</text>
  <text x="250" y="105" fill="#dcfce7" font-size="9" text-anchor="middle">Continuous burrowing &amp; casting formation</text>
  <!-- Layer 2: Bedding material (Coconut coir / Straw) -->
  <rect x="70" y="126" width="360" height="35" fill="#78350f"/>
  <text x="250" y="148" fill="#fef08a" font-size="10" text-anchor="middle">Bedding Layer: Coconut Coir &amp; Chopped Dry Leaves</text>
  <!-- Layer 3: Coarse sand & gravel for drainage -->
  <rect x="70" y="163" width="360" height="25" fill="#475569"/>
  <text x="250" y="180" fill="#e2e8f0" font-size="9" text-anchor="middle">Base Drainage Layer: Coarse Sand &amp; Gravel (Vermiwash Outlet)</text>
  <!-- Vermiwash outlet tap -->
  <circle cx="430" cy="175" r="6" fill="#38bdf8"/>
  <text x="445" y="198" fill="#38bdf8" font-size="8">Vermiwash Tap</text>
</svg>''',

    # SVG 3: Modern Incinerator WtE
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Waste-to-Energy (WtE) High-Temperature Incinerator</text>
  <!-- Waste Hopper -->
  <g transform="translate(30, 50)">
    <path d="M 0 0 L 40 0 L 30 60 L 10 60 Z" fill="#475569" stroke="#94a3b8"/>
    <text x="20" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Waste Feed</text>
  </g>
  <!-- Primary Chamber 850 C -->
  <g transform="translate(85, 60)">
    <rect x="0" y="0" width="65" height="90" rx="4" fill="#991b1b" stroke="#ef4444"/>
    <text x="32" y="35" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Primary</text>
    <text x="32" y="50" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Chamber</text>
    <text x="32" y="75" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">850 &#176;C</text>
  </g>
  <!-- Secondary Chamber 1100 C -->
  <g transform="translate(160, 45)">
    <rect x="0" y="0" width="65" height="105" rx="4" fill="#dc2626" stroke="#f87171"/>
    <text x="32" y="35" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Secondary</text>
    <text x="32" y="50" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Chamber</text>
    <text x="32" y="85" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">1100 &#176;C</text>
  </g>
  <!-- Boiler & Steam Turbine -->
  <g transform="translate(235, 55)">
    <rect x="0" y="0" width="65" height="85" rx="4" fill="#0369a1" stroke="#38bdf8"/>
    <text x="32" y="35" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Boiler &amp;</text>
    <text x="32" y="50" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Steam</text>
    <text x="32" y="75" fill="#7dd3fc" font-size="9" text-anchor="middle">Electricity</text>
  </g>
  <!-- Flue gas scrubber -->
  <g transform="translate(310, 50)">
    <rect x="0" y="0" width="65" height="95" rx="4" fill="#15803d" stroke="#22c55e"/>
    <text x="32" y="35" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Lime &amp; Carbon</text>
    <text x="32" y="50" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Scrubber</text>
    <text x="32" y="75" fill="#86efac" font-size="8" text-anchor="middle">Neutralizes Acid</text>
  </g>
  <!-- ESP & Stack -->
  <g transform="translate(385, 40)">
    <rect x="0" y="20" width="35" height="100" rx="3" fill="#334155"/>
    <rect x="45" y="0" width="20" height="135" fill="#64748b"/>
    <text x="55" y="155" fill="#f8fafc" font-size="9" text-anchor="middle">Clean Stack</text>
  </g>
</svg>''',

    # SVG 4: Biogas Digester
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Fixed-Dome Biogas Plant (Anaerobic Digestion)</text>
  <!-- Inlet Tank -->
  <g transform="translate(30, 80)">
    <rect x="0" y="0" width="60" height="60" rx="4" fill="#1e293b" stroke="#94a3b8"/>
    <text x="30" y="25" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">Inlet Tank</text>
    <text x="30" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Slurry In</text>
  </g>
  <!-- Inlet pipe -->
  <line x1="90" y1="120" x2="160" y2="150" stroke="#94a3b8" stroke-width="8"/>
  <!-- Central Digester & Dome -->
  <g transform="translate(160, 50)">
    <!-- Underground digester body -->
    <rect x="0" y="50" width="180" height="110" rx="10" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <text x="90" y="115" fill="#dcfce7" font-size="12" font-weight="bold" text-anchor="middle">Anaerobic Fermentation</text>
    <text x="90" y="132" fill="#86efac" font-size="10" text-anchor="middle">Methanogenic Bacteria</text>
    <!-- Dome cap -->
    <path d="M 10 50 Q 90 0 170 50 Z" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <text x="90" y="35" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Biogas (CH4 + CO2)</text>
    <!-- Gas valve pipe -->
    <line x1="90" y1="12" x2="90" y2="-5" stroke="#fbbf24" stroke-width="4"/>
  </g>
  <!-- Outlet pipe -->
  <line x1="340" y1="150" x2="410" y2="120" stroke="#94a3b8" stroke-width="8"/>
  <!-- Outlet Tank -->
  <g transform="translate(410, 80)">
    <rect x="0" y="0" width="60" height="60" rx="4" fill="#1e293b" stroke="#94a3b8"/>
    <text x="30" y="25" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Outlet Tank</text>
    <text x="30" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Bio-fertilizer</text>
  </g>
</svg>''',

    # SVG 5: Aerobic Composting Thermal Curve
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Temperature Phases of Aerobic Composting</text>
  <!-- Axes -->
  <line x1="60" y1="190" x2="450" y2="190" stroke="#64748b" stroke-width="2"/>
  <line x1="60" y1="40" x2="60" y2="190" stroke="#64748b" stroke-width="2"/>
  <text x="250" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Time Elapsed (Days 1 to 45)</text>
  <text x="25" y="115" fill="#94a3b8" font-size="10" transform="rotate(-90 25,115)" text-anchor="middle">Temperature (&#176;C)</text>
  <!-- Curve -->
  <path d="M 60 170 Q 110 70 170 65 T 260 80 T 360 150 T 440 170" fill="none" stroke="#ef4444" stroke-width="3"/>
  <!-- Phases highlights -->
  <!-- Phase 1: Mesophilic -->
  <text x="90" y="150" fill="#38bdf8" font-size="9">Mesophilic</text>
  <!-- Phase 2: Thermophilic -->
  <rect x="140" y="45" width="120" height="30" rx="4" fill="#7f1d1d" fill-opacity="0.6"/>
  <text x="200" y="65" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Thermophilic (55-65 &#176;C)</text>
  <text x="200" y="90" fill="#fef08a" font-size="8" text-anchor="middle">Pathogens &amp; Weed Seeds Killed</text>
  <!-- Phase 3: Maturation -->
  <text x="380" y="130" fill="#10b981" font-size="9">Maturation &amp; Curing</text>
</svg>''',

    # SVG 6: Pyrolysis Flow Diagram
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Pyrolysis Process: Zero-Oxygen Polymer Conversion</text>
  <!-- Shredder -->
  <rect x="25" y="55" width="85" height="100" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="67" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Shredded</text>
  <text x="67" y="105" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Plastics /</text>
  <text x="67" y="125" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Biomass</text>
  <!-- Arrow -->
  <path d="M 115 105 L 140 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Reactor -->
  <rect x="145" y="45" width="110" height="120" rx="8" fill="#7f1d1d" stroke="#ef4444"/>
  <text x="200" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Pyrolysis</text>
  <text x="200" y="95" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Reactor</text>
  <text x="200" y="120" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">500 &#176;C to 800 &#176;C</text>
  <text x="200" y="145" fill="#fca5a5" font-size="9" text-anchor="middle">NO OXYGEN</text>
  <!-- Solid bottom output: Biochar -->
  <path d="M 200 168 L 200 190" stroke="#f8fafc" stroke-width="2"/>
  <rect x="155" y="190" width="90" height="30" rx="4" fill="#0f172a" stroke="#94a3b8"/>
  <text x="200" y="210" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Solid Biochar</text>
  <!-- Arrow to Condenser -->
  <path d="M 260 105 L 290 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Condenser -->
  <rect x="295" y="55" width="85" height="100" rx="6" fill="#0c4a6e" stroke="#0284c7"/>
  <text x="337" y="95" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Condenser</text>
  <text x="337" y="120" fill="#94a3b8" font-size="9" text-anchor="middle">Cooling</text>
  <!-- Outputs -->
  <!-- Gas output -->
  <path d="M 385 80 L 415 80" stroke="#f59e0b" stroke-width="2"/>
  <rect x="415" y="65" width="70" height="30" rx="4" fill="#78350f"/>
  <text x="450" y="85" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Syngas</text>
  <!-- Liquid output -->
  <path d="M 385 130 L 415 130" stroke="#10b981" stroke-width="2"/>
  <rect x="415" y="115" width="70" height="30" rx="4" fill="#064e3b"/>
  <text x="450" y="135" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Bio-Oil</text>
</svg>''',

    # SVG 7: Waste Treatment Comparison Matrix
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Scientific Waste Disposal Methods Compared</text>
  <!-- Table Header -->
  <rect x="25" y="45" width="450" height="28" fill="#334155" rx="4"/>
  <text x="80" y="63" fill="#38bdf8" font-size="11" font-weight="bold">Method</text>
  <text x="180" y="63" fill="#38bdf8" font-size="11" font-weight="bold">Target Waste</text>
  <text x="310" y="63" fill="#38bdf8" font-size="11" font-weight="bold">End Product</text>
  <text x="420" y="63" fill="#38bdf8" font-size="11" font-weight="bold">Footprint</text>
  <!-- Row 1: Composting -->
  <rect x="25" y="78" width="450" height="32" fill="#1e293b"/>
  <text x="80" y="98" fill="#10b981" font-size="10" font-weight="bold">Composting</text>
  <text x="180" y="98" fill="#f8fafc" font-size="10">Wet organic waste</text>
  <text x="310" y="98" fill="#86efac" font-size="10">Nutrient humus</text>
  <text x="420" y="98" fill="#10b981" font-size="10">Zero waste</text>
  <!-- Row 2: Vermicompost -->
  <rect x="25" y="115" width="450" height="32" fill="#1e293b"/>
  <text x="80" y="135" fill="#38bdf8" font-size="10" font-weight="bold">Vermiculture</text>
  <text x="180" y="135" fill="#f8fafc" font-size="10">Kitchen / Agri waste</text>
  <text x="310" y="135" fill="#7dd3fc" font-size="10">Castings + wash</text>
  <text x="420" y="135" fill="#10b981" font-size="10">Enriches soil</text>
  <!-- Row 3: Incineration -->
  <rect x="25" y="152" width="450" height="32" fill="#1e293b"/>
  <text x="80" y="172" fill="#ef4444" font-size="10" font-weight="bold">Incineration</text>
  <text x="180" y="172" fill="#f8fafc" font-size="10">Biomedical / Toxic</text>
  <text x="310" y="172" fill="#fca5a5" font-size="10">Ash + Electricity</text>
  <text x="420" y="172" fill="#eab308" font-size="10">90% volume cut</text>
  <!-- Row 4: Landfill -->
  <rect x="25" y="189" width="450" height="32" fill="#1e293b"/>
  <text x="80" y="209" fill="#f59e0b" font-size="10" font-weight="bold">Sanitary Landfill</text>
  <text x="180" y="209" fill="#f8fafc" font-size="10">Inert &amp; residual waste</text>
  <text x="310" y="209" fill="#fde68a" font-size="10">Methane fuel</text>
  <text x="420" y="209" fill="#ef4444" font-size="10">Needs liners</text>
</svg>''',

    # SVG 8: Earthworm Castings Nutrients
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Nutrient Superiority: Vermicompost Castings vs Topsoil</text>
  <!-- Nitrogen Bar -->
  <g transform="translate(40, 50)">
    <text x="0" y="18" fill="#38bdf8" font-size="11" font-weight="bold">Nitrogen (N): 5x Higher</text>
    <rect x="180" y="5" width="220" height="18" rx="4" fill="#0284c7"/>
    <rect x="180" y="5" width="44" height="18" rx="4" fill="#64748b"/>
    <text x="410" y="18" fill="#93c5fd" font-size="10">500%</text>
  </g>
  <!-- Phosphorus Bar -->
  <g transform="translate(40, 85)">
    <text x="0" y="18" fill="#10b981" font-size="11" font-weight="bold">Phosphorus (P): 7x Higher</text>
    <rect x="180" y="5" width="240" height="18" rx="4" fill="#15803d"/>
    <rect x="180" y="5" width="34" height="18" rx="4" fill="#64748b"/>
    <text x="430" y="18" fill="#86efac" font-size="10">700%</text>
  </g>
  <!-- Potassium Bar -->
  <g transform="translate(40, 120)">
    <text x="0" y="18" fill="#f59e0b" font-size="11" font-weight="bold">Potassium (K): 11x Higher</text>
    <rect x="180" y="5" width="250" height="18" rx="4" fill="#b45309"/>
    <rect x="180" y="5" width="23" height="18" rx="4" fill="#64748b"/>
    <text x="440" y="18" fill="#fde68a" font-size="10">1100%</text>
  </g>
  <!-- Summary Box -->
  <rect x="40" y="160" width="420" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="250" y="182" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Earthworm digestive tracts solubilize bound soil minerals</text>
  <text x="250" y="200" fill="#f8fafc" font-size="10" text-anchor="middle">Supplies calcium, magnesium, auxin hormones, and beneficial bacteria</text>
</svg>''',

    # SVG 9: Leachate Treatment Plant
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Multi-Stage Landfill Leachate Treatment System</text>
  <!-- Stage 1: Equalization sump -->
  <g transform="translate(25, 55)">
    <rect x="0" y="0" width="95" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="47" y="25" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">1. Equalization</text>
    <text x="47" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Raw Leachate</text>
    <text x="47" y="65" fill="#ef4444" font-size="9" text-anchor="middle">High COD/BOD</text>
    <text x="47" y="85" fill="#ef4444" font-size="9" text-anchor="middle">Heavy Metals</text>
  </g>
  <!-- Arrow -->
  <path d="M 125 110 L 145 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Stage 2: Aerobic Biological Tank -->
  <g transform="translate(150, 55)">
    <rect x="0" y="0" width="95" height="110" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="47" y="25" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">2. Aeration Tank</text>
    <text x="47" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Activated Sludge</text>
    <text x="47" y="65" fill="#fbbf24" font-size="9" text-anchor="middle">Microbes digest</text>
    <text x="47" y="85" fill="#fbbf24" font-size="9" text-anchor="middle">organic toxins</text>
  </g>
  <!-- Arrow -->
  <path d="M 250 110 L 270 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Stage 3: Reverse Osmosis (RO) -->
  <g transform="translate(275, 55)">
    <rect x="0" y="0" width="95" height="110" rx="6" fill="#1e293b" stroke="#0284c7"/>
    <text x="47" y="25" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">3. High-Pressure</text>
    <text x="47" y="40" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">Reverse Osmosis</text>
    <text x="47" y="65" fill="#38bdf8" font-size="9" text-anchor="middle">Membrane</text>
    <text x="47" y="85" fill="#38bdf8" font-size="9" text-anchor="middle">Filtration</text>
  </g>
  <!-- Arrow -->
  <path d="M 375 110 L 395 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Stage 4: Safe Treated Effluent -->
  <g transform="translate(400, 55)">
    <rect x="0" y="0" width="85" height="110" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="42" y="25" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">4. Discharge</text>
    <text x="42" y="45" fill="#34d399" font-size="9" text-anchor="middle">Purified Water</text>
    <text x="42" y="65" fill="#34d399" font-size="9" text-anchor="middle">Safe for</text>
    <text x="42" y="85" fill="#34d399" font-size="9" text-anchor="middle">Irrigation</text>
  </g>
  <text x="250" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">Eliminates 99%+ of organic poisons and heavy metals</text>
</svg>''',

    # SVG 10: Flue Gas Cleaning System
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Incinerator Flue Gas Cleaning: Emissions Scrubbing</text>
  <!-- Gas pipe flow -->
  <line x1="40" y1="120" x2="440" y2="120" stroke="#475569" stroke-width="20"/>
  <!-- Injection 1: Hydrated Lime -->
  <g transform="translate(90, 45)">
    <path d="M 25 0 L 25 55" stroke="#38bdf8" stroke-width="4" marker-end="url(#arr)"/>
    <rect x="0" y="0" width="50" height="25" fill="#0369a1" rx="3"/>
    <text x="25" y="16" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Lime</text>
    <text x="25" y="70" fill="#7dd3fc" font-size="8" text-anchor="middle">Neutralizes SO2/HCl</text>
  </g>
  <!-- Injection 2: Activated Carbon -->
  <g transform="translate(190, 45)">
    <path d="M 25 0 L 25 55" stroke="#f59e0b" stroke-width="4"/>
    <rect x="0" y="0" width="50" height="25" fill="#78350f" rx="3"/>
    <text x="25" y="16" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Carbon</text>
    <text x="25" y="70" fill="#fde68a" font-size="8" text-anchor="middle">Adsorbs Dioxins/Hg</text>
  </g>
  <!-- Filter 3: Fabric Baghouse Filter -->
  <g transform="translate(290, 60)">
    <rect x="0" y="0" width="75" height="110" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="4"/>
    <text x="37" y="30" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Baghouse</text>
    <text x="37" y="48" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Fabric Filter</text>
    <text x="37" y="75" fill="#94a3b8" font-size="8" text-anchor="middle">Captures Fly Ash</text>
    <text x="37" y="90" fill="#94a3b8" font-size="8" text-anchor="middle">PM2.5 / PM10</text>
  </g>
  <!-- Clean Emission to Stack -->
  <g transform="translate(400, 70)">
    <rect x="0" y="0" width="55" height="90" fill="#15803d" rx="4"/>
    <text x="27" y="45" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Clean</text>
    <text x="27" y="60" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Air Stack</text>
  </g>
</svg>''',

    # SVG 11: Home Composting Bin
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Household Aerobic Compost Bin Architecture</text>
  <!-- Bin Body -->
  <g transform="translate(140, 45)">
    <rect x="20" y="0" width="180" height="150" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Ventilation holes -->
    <circle cx="50" cy="40" r="4" fill="#38bdf8"/>
    <circle cx="80" cy="40" r="4" fill="#38bdf8"/>
    <circle cx="110" cy="40" r="4" fill="#38bdf8"/>
    <circle cx="140" cy="40" r="4" fill="#38bdf8"/>
    <circle cx="170" cy="40" r="4" fill="#38bdf8"/>
    <circle cx="50" cy="80" r="4" fill="#38bdf8"/>
    <circle cx="80" cy="80" r="4" fill="#38bdf8"/>
    <circle cx="110" cy="80" r="4" fill="#38bdf8"/>
    <circle cx="140" cy="80" r="4" fill="#38bdf8"/>
    <circle cx="170" cy="80" r="4" fill="#38bdf8"/>
    <text x="110" y="115" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Aerobic Waste Core</text>
    <text x="110" y="132" fill="#86efac" font-size="9" text-anchor="middle">60% Kitchen scraps + 40% Dry leaves</text>
    <!-- Tap at bottom -->
    <rect x="185" y="130" width="25" height="12" fill="#f59e0b"/>
    <circle cx="215" cy="136" r="6" fill="#f59e0b"/>
    <text x="215" y="160" fill="#fbbf24" font-size="9">Compost Tea Tap</text>
  </g>
  <!-- Labels -->
  <text x="60" y="90" fill="#38bdf8" font-size="10">Aeration Holes</text>
  <text x="60" y="105" fill="#94a3b8" font-size="8">(Prevents foul odors)</text>
</svg>''',

    # SVG 12: Integrated Solid Waste Management Flow
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Integrated Solid Waste Management (ISWM) Mass Flow</text>
  <!-- 100 Tonnes Input -->
  <rect x="20" y="80" width="90" height="60" rx="6" fill="#334155" stroke="#94a3b8"/>
  <text x="65" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">100 Tonnes</text>
  <text x="65" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Raw City Waste</text>
  <!-- Diverted Streams -->
  <!-- 55 Tonnes Composting -->
  <g transform="translate(160, 45)">
    <rect x="0" y="0" width="140" height="35" rx="4" fill="#14532d"/>
    <text x="70" y="22" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">55 T &#8594; Composting (Humus)</text>
  </g>
  <!-- 25 Tonnes Recycling -->
  <g transform="translate(160, 90)">
    <rect x="0" y="0" width="140" height="35" rx="4" fill="#0c4a6e"/>
    <text x="70" y="22" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">25 T &#8594; Recycling (Paper/Plastic)</text>
  </g>
  <!-- 15 Tonnes WtE -->
  <g transform="translate(160, 135)">
    <rect x="0" y="0" width="140" height="35" rx="4" fill="#78350f"/>
    <text x="70" y="22" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">15 T &#8594; WtE / RDF Pellets</text>
  </g>
  <!-- 5 Tonnes Landfill -->
  <g transform="translate(160, 180)">
    <rect x="0" y="0" width="140" height="35" rx="4" fill="#7f1d1d"/>
    <text x="70" y="22" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Only 5 T &#8594; Inert Landfill</text>
  </g>
  <!-- Diversion achievement banner -->
  <rect x="330" y="80" width="150" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="405" y="108" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">95% Landfill</text>
  <text x="405" y="128" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Diversion Rate</text>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the cross-section diagram of an engineered sanitary landfill, which component is installed directly above the compacted clay liner to intercept hazardous leachate?",
        "options": [
            "An impermeable high-density polyethylene (HDPE) geomembrane sheet (1.5 mm)",
            "A layer of dry autumn leaves",
            "A network of high-voltage electric wires",
            "A series of water sprinkler fountains"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram details the composite barrier system consisting of an impermeable HDPE geomembrane laid directly over compacted clay to stop toxic leachate from escaping."
    },
    {
        "q": "Referring to the vermicomposting bed schematic, what is the ecological purpose of placing a moist gunny bag cover over the top surface?",
        "options": [
            "To maintain darkness and 50-60% humidity, which are ideal living conditions for light-sensitive earthworms",
            "To cook the organic waste using direct solar heat",
            "To completely block all entry of atmospheric oxygen",
            "To crush the earthworms mechanically"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Earthworms are photophobic and breathe through moist skin; the damp gunny bag preserves humidity, shields against light, and protects them from predators."
    },
    {
        "q": "According to the Waste-to-Energy incinerator flow diagram, why is flue gas passed through a secondary combustion chamber maintained at 1100 deg C?",
        "options": [
            "To ensure complete thermal destruction of hazardous dioxins, furans, and volatile organic pollutants",
            "To freeze the exhaust gases into dry ice",
            "To convert the waste directly into liquid water",
            "To synthesize artificial plastic polymers"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "High temperature (1100 deg C) in the secondary chamber with turbulent airflow destroys persistent organic pollutants like dioxins and furans before emissions enter the stack."
    },
    {
        "q": "Examining the fixed-dome biogas digester diagram, where is the combustible biogas collected before being drawn through the control valve for cooking?",
        "options": [
            "In the sealed masonry dome situated directly above the anaerobic slurry level",
            "Inside the open inlet feed tank",
            "Underneath the coarse gravel base",
            "In the soil surrounding the plant"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Biogas generated by anaerobic methanogens rises buoyantly and accumulates under pressure in the upper gas holder dome above the fermenting slurry."
    },
    {
        "q": "Based on the aerobic composting thermal curve, what critical biological milestone is accomplished when pile temperature reaches the 55 deg C - 65 deg C thermophilic peak?",
        "options": [
            "Pathogenic microorganisms and plant weed seeds are eradicated",
            "All water in the universe evaporates",
            "The compost turns into solid metal",
            "Earthworms multiply by 10,000 times"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The graph notes that sustained heat in the thermophilic phase pasteurizes the pile, destroying weed seeds and harmful human/plant pathogens."
    },
    {
        "q": "In the pyrolysis flow diagram, why must the pyrolysis reactor operate under strictly oxygen-free conditions at 500 deg C - 800 deg C?",
        "options": [
            "To thermally crack polymers into bio-oil, syngas, and biochar instead of allowing ordinary flaming combustion into CO2 and ash",
            "To freeze the plastics into liquid nitrogen",
            "To allow living earthworms to consume the plastic",
            "To eliminate the force of gravity inside the chamber"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Absence of oxygen prevents oxidation/combustion, directing the thermal energy to crack long-chain polymer bonds into useful hydrocarbon fuels."
    },
    {
        "q": "According to the scientific disposal methods comparison matrix, which method is uniquely capable of reducing the physical volume of combustible solid waste by approximately 90%?",
        "options": [
            "Thermal incineration",
            "Aerobic composting",
            "Vermicomposting",
            "Unlined open dumping"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "As indicated in the matrix, incineration achieves an 85-90% volumetric reduction, making it indispensable for space-constrained metropolises."
    },
    {
        "q": "Referring to the nutrient bar chart comparing earthworm castings with surrounding topsoil, by what factor is available Potassium (K) concentrated in vermicompost?",
        "options": [
            "11 times higher (1100%)",
            "2 times lower",
            "Exactly equal to topsoil",
            "Zero percent"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The nutrient chart illustrates that earthworm castings contain 11 times (1100%) more bioavailable Potassium (K) than ordinary garden topsoil."
    },
    {
        "q": "In the multi-stage leachate treatment schematic, what is the role of High-Pressure Reverse Osmosis (RO) in Stage 3?",
        "options": [
            "To filter out dissolved heavy metal ions, refractory organics, and mineral salts using semi-permeable membranes",
            "To add toxic chlorine gas to the water",
            "To boil the leachate into steam",
            "To freeze the water into ice cubes"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Reverse osmosis forces biological effluent across dense membranes under high hydraulic pressure, separating clean water from heavy metals and toxic salts."
    },
    {
        "q": "Based on the flue gas cleaning system diagram, what is injected into the flue gas stream specifically to neutralize acidic sulfur dioxide (SO2) and hydrochloric acid (HCl) vapors?",
        "options": [
            "Hydrated lime (calcium hydroxide slurry)",
            "Concentrated battery acid",
            "Shredded plastic pellets",
            "Pure gasoline"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram highlights alkaline lime injection, which reacts with and neutralizes acid gases to form solid calcium salts collected downstream."
    },
    {
        "q": "Examining the home compost bin diagram, why are numerous small aeration holes drilled across the bin walls?",
        "options": [
            "To supply continuous oxygen to aerobic bacteria, preventing anaerobic putrefaction and foul odor emissions",
            "To let all the food scraps fall out onto the floor",
            "To allow mice and rats to crawl in easily",
            "To let rainwater drown the bacteria"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Ventilation perforations facilitate natural convective airflow, ensuring aerobic bacteria receive sufficient oxygen to decompose waste without producing foul sulfur odors."
    },
    {
        "q": "According to the Integrated Solid Waste Management (ISWM) mass flow diagram, what landfill diversion rate is achieved when wet waste is composted, dry recyclables recovered, and combustibles processed into fuel pellets?",
        "options": [
            "95% diversion (only 5% residual inert waste reaches the landfill)",
            "Zero percent diversion",
            "Exactly 50% diversion",
            "10% diversion"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The flowchart proves that integrated management diverts 95 tonnes of every 100 tonnes of city garbage, sending only 5 tonnes of non-recyclable inerts to the landfill."
    }
]

def make_doc(item, idx, vault, category, svg=None):
    code = f"{TOPIC_CODE}-{item['type']}-{idx:03d}"
    doc = {
        "questionCode": code,
        "topicCode": TOPIC_CODE,
        "chapterNumber": 9,
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
