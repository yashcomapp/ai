# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-9-9.2: Solid Waste Management: Biodegradable vs Non-biodegradable
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-9-9.2"
OUTPUT_FILE = "scripts/ch9_topic2.json"

exam_data = [
    {
        "q": "Which of the following belongs to the category of biodegradable (wet) solid waste?",
        "options": ["Plastic carry bags", "Fruit peels and vegetable scraps", "Thermocol (expanded polystyrene)", "Glass bottles"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Fruit and vegetable scraps are organic matter that can be broken down naturally by bacteria and fungi, making them biodegradable wet waste."
    },
    {
        "q": "What is the primary danger associated with electronic waste (e-waste) disposed of in open dumps?",
        "options": [
            "Leaching of heavy metals like lead, mercury, and cadmium into soil and groundwater",
            "Rapid overgrowth of algal blooms",
            "Excessive production of ozone at ground level",
            "Immediate spontaneous nuclear fission"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "E-waste contains hazardous heavy metals such as lead, mercury, cadmium, and brominated flame retardants that leach into groundwater aquifers from unlined dumps."
    },
    {
        "q": "Under standard municipal waste segregation guidelines in India, which color bin is officially designated for wet biodegradable waste?",
        "options": ["Blue", "Green", "Red", "Black"],
        "ans": 1,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Green bins are designated for biodegradable wet waste (kitchen scraps, food waste), while blue bins are designated for dry recyclable waste."
    },
    {
        "q": "Which international symbol must be displayed prominently on containers holding hazardous hospital and clinic waste?",
        "options": ["Biohazard symbol", "Radioactive trefoil", "Recycle Mobius loop", "Green dot eco-mark"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Biomedical waste containers and bags must carry the universal biohazard symbol to indicate infectious, pathological, or pathogenic materials."
    },
    {
        "q": "Which of the following items requires the longest time for complete natural degradation in the environment?",
        "options": ["Cotton cloth (2-5 months)", "Banana peel (3-4 weeks)", "Plastic PET bottle (450+ years)", "Woolen sock (1 year)"],
        "ans": 2,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "PET plastic bottles resist microbial degradation and persist in the natural environment for an estimated 450 to 1,000 years."
    },
    {
        "q": "What does the 'R' standing for 'Refuse' signify in the modern 7 R's hierarchy of solid waste management?",
        "options": [
            "Refusing to buy or accept non-recyclable single-use plastic items",
            "Throwing waste into public streets",
            "Refusing to segregate waste at home",
            "Refusing to pay municipal waste collection fees"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "'Refuse' means proactively saying no to unnecessary, unsustainable single-use items (like plastic straws or disposable bags) before they enter the waste stream."
    },
    {
        "q": "Which toxic metal present in older computer monitors (Cathode Ray Tubes) poses severe neurological and renal risks if dumped unsafely?",
        "options": ["Lead (Pb)", "Sodium (Na)", "Calcium (Ca)", "Magnesium (Mg)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "CRTs and circuit board solder contain substantial quantities of lead, a potent neurotoxin that causes renal and central nervous system damage."
    },
    {
        "q": "Why is thermocol (expanded polystyrene) considered environmentally hazardous?",
        "options": [
            "It is completely non-biodegradable and releases carcinogenic styrene vapors when burned",
            "It decomposes in less than 24 hours into toxic acid",
            "It absorbs atmospheric oxygen and depletes breathing air",
            "It attracts pathogenic mosquitoes exclusively"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Thermocol takes centuries to decompose, clogs waterways, and emits hazardous carcinogenic pollutants like styrene and dioxins when incinerated."
    },
    {
        "q": "In biomedical waste segregation, which color-coded container is specifically reserved for human anatomical waste and soiled dressings?",
        "options": ["Yellow bag", "Blue bin", "Black container", "Green bin"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Under Bio-Medical Waste Management Rules, Yellow bags are designated for infectious human anatomical waste, soiled cotton, plaster casts, and body tissue."
    },
    {
        "q": "What is the toxic liquid that percolates through unscientific open garbage dumps and contaminates groundwater called?",
        "options": ["Leachate", "Distillate", "Condensate", "Permeate"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Leachate is the heavily contaminated foul liquid that leaches through decomposing solid waste, dissolving heavy metals, organic pollutants, and pathogens."
    },
    {
        "q": "Which resin identification code number represents Polyethylene Terephthalate (PET or PETE), widely used for mineral water and soda bottles?",
        "options": ["1", "2", "5", "6"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Resin identification code 1 is assigned to Polyethylene Terephthalate (PET), the most commonly recycled plastic polymer."
    },
    {
        "q": "What is microplastic, which has become a severe environmental and marine pollutant?",
        "options": [
            "Plastic particles smaller than 5 mm in diameter resulting from the fragmentation of plastic debris",
            "A newly discovered species of photosynthetic algae",
            "A microscopic bacteria that eats metal wires",
            "Pure elemental carbon synthesized in laboratories"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Microplastics are tiny plastic pieces less than 5 mm long that result from the physical and photochemical breakdown of commercial consumer plastics."
    },
    {
        "q": "Which principle in the 7 R's focuses on processing discarded scrap metal, paper, or glass into raw materials to manufacture brand-new products?",
        "options": ["Recycle", "Refuse", "Rethink", "Regulate"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Recycling involves collecting waste materials, processing them into secondary raw materials, and remanufacturing them into new goods."
    },
    {
        "q": "Which toxic compound is released into the atmosphere when chlorinated plastics like Polyvinyl Chloride (PVC) are burned at low temperatures?",
        "options": ["Dioxins and furans", "Pure oxygen", "Liquid helium", "Argon gas"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Incomplete, low-temperature combustion of PVC releases chlorinated dioxins and furans, which are persistent organic pollutants and potent carcinogens."
    },
    {
        "q": "What is the primary objective of Extended Producer Responsibility (EPR) in solid waste policy?",
        "options": [
            "Making manufacturers financially and operationally responsible for the end-of-life collection and recycling of their products",
            "Prohibiting consumers from ever buying packaged goods",
            "Exempting multinational corporations from municipal environmental laws",
            "Shifting 100% of recycling costs to public taxpayers"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "EPR mandates that producers, importers, and brand owners establish take-back mechanisms and finance the environmentally sound recycling of their post-consumer packaging."
    },
    {
        "q": "Which of the following wastes is classified under 'Hazardous Domestic Waste'?",
        "options": ["Old pesticide bottles, expired medicines, and lead-acid batteries", "Dry fallen tree leaves", "Potato peels", "Cardboard delivery boxes"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Expired pharmaceuticals, insecticides, car batteries, and paint cans contain toxic chemicals and require segregated hazardous disposal."
    },
    {
        "q": "Why should discarded glass bottles be segregated from general municipal trash before compaction?",
        "options": [
            "Broken glass shards injure sanitation workers and contaminate compost batches",
            "Glass melts at normal room temperature and poisons air",
            "Glass evaporates into hazardous radioactive steam",
            "Glass is rapidly digested by anaerobic composting bacteria"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Broken glass presents serious occupational puncture hazards to waste handlers and renders organic compost unusable if fragmented into soil."
    },
    {
        "q": "Which metal commonly extracted from disposed mobile phone circuit boards and contact pins has the highest electrical conductivity and corrosion resistance?",
        "options": ["Gold (Au)", "Iron (Fe)", "Lead (Pb)", "Zinc (Zn)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Gold is utilized on microelectronic contacts and connector pins for its superior electrical conductivity and exceptional tarnish resistance."
    },
    {
        "q": "What happens when non-biodegradable plastics are dumped in agricultural fields?",
        "options": [
            "They impede rainwater percolation into deep soil layers and obstruct plant root respiration",
            "They accelerate nitrogen fixation by leguminous crops",
            "They transform into natural organic humus within hours",
            "They increase earthworm populations tenfold"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Plastic films in soil form impermeable physical barriers that hinder water infiltration, cause soil compaction, and suffocate plant root networks."
    },
    {
        "q": "Which of the following represents an example of 'Upcycling' in solid waste management?",
        "options": [
            "Converting discarded glass bottles into decorative artistic hanging lamps",
            "Burning paper in an open backyard fire",
            "Dumping discarded refrigerators in a riverbed",
            "Burying plastic bags under fresh soil"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Upcycling creatively transforms waste materials or unwanted products into new items of superior environmental, aesthetic, or monetary value."
    },
    {
        "q": "Select ALL items that are biodegradable:",
        "options": [
            "Egg shells and banana peels",
            "Cotton waste rags and wood shavings",
            "Aluminum soft drink cans",
            "Fallen autumn leaves"
        ],
        "ans": [0, 1, 3],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Eggshells, cotton, wood, and dry leaves are organic biodegradable materials. Aluminum cans are non-biodegradable metals."
    },
    {
        "q": "Select ALL principles included in the 7 R's of waste management:",
        "options": [
            "Rethink",
            "Reduce",
            "Recycle",
            "Release into ocean"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "The 7 R's include Rethink, Refuse, Reduce, Reuse, Recycle, Regulate, and Recover. Dumping into oceans is an illegal pollutant practice."
    },
    {
        "q": "Select ALL heavy metals typically found in unprocessed electronic waste (e-waste):",
        "options": [
            "Cadmium (in rechargeable batteries and chip resistors)",
            "Lead (in CRT glass and solder joints)",
            "Mercury (in tilt switches and fluorescent backlights)",
            "Chlorophyll"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Cadmium, lead, and mercury are major hazardous heavy metals in electronics. Chlorophyll is a botanical pigment found in plants."
    },
    {
        "q": "True or False: Biodegradable waste can be converted into nutrient-rich organic compost by microorganisms.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Aerobic and anaerobic microbial composting converts organic biodegradable waste into dark, nutrient-rich soil humus."
    },
    {
        "q": "True or False: Incinerating biomedical plastic waste without proper high-temperature flue-gas scrubbers can release dangerous cancer-causing dioxins.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Medical waste incinerators must operate above 1050 deg C with alkaline scrubbers to destroy chlorinated dioxins and furans."
    },
    {
        "q": "True or False: Glass is a biodegradable material that decomposes within 3 months when buried in moist garden soil.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Glass is an inorganic amorphous silicate that does not decompose biologically; it lasts for an estimated one million years."
    },
    {
        "q": "True or False: Carrying a reusable cloth bag when shopping at the grocery store is a practical implementation of the 'Reduce' and 'Reuse' principles.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Reusing a sturdy cloth bag prevents dozens of disposable single-use plastic bags from entering the municipal waste stream."
    },
    {
        "q": "Assertion (A): Source segregation of domestic solid waste into dry and wet categories is critical for successful waste management.\\nReason (R): Mixing wet kitchen waste with dry recyclable plastics and paper makes sorting nearly impossible and ruins the recycling quality of paper.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Segregating at the point of origin keeps recyclables clean and enables wet waste to be composted without toxic chemical or glass contamination."
    },
    {
        "q": "Assertion (A): Open burning of roadside municipal garbage heaps is strictly banned under Indian environmental legislation.\\nReason (R): Uncontrolled burning of mixed garbage generates dense smoke rich in carbon monoxide, particulate matter (PM2.5), and carcinogenic polycyclic aromatic hydrocarbons.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Open burning generates severe air pollution and toxic smoke without flue filtration, aggravating asthma and chronic pulmonary conditions."
    },
    {
        "q": "Assertion (A): Thermocol is an excellent material for environmentally friendly single-use dining plates.\\nReason (R): Thermocol rapidly digests in municipal sewage pipes and releases beneficial nutrients for aquatic fish.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "Both A and R are false"
        ],
        "ans": 3,
        "type": "OAR",
        "difficulty": "easy",
        "exp": "Both statements are completely false. Thermocol is non-biodegradable polystyrene that chokes drains and harms aquatic fauna when mistaken for food."
    },
    {
        "q": "Fill in the blank: The municipal bin designated for collecting recyclable dry waste such as clean paper, metal tins, and plastics is the ________ bin.",
        "options": ["blue", "green", "black", "yellow"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Blue bins are standard for non-biodegradable, clean recyclable dry waste."
    },
    {
        "q": "Fill in the blank: Waste generated from healthcare facilities, laboratories, and diagnostic clinics is officially classified as ________ waste.",
        "options": ["biomedical", "agricultural", "inert", "mining"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Biomedical waste encompasses all waste generated during medical diagnosis, treatment, research, or immunization of human beings or animals."
    },
    {
        "q": "Fill in the blank: The process of breaking down discarded plastic polymers into smaller synthetic monomers or fuel oils via thermal heating in the absence of oxygen is called ________.",
        "options": ["pyrolysis", "aerobic composting", "precipitation", "hydrolysis"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "Pyrolysis is the thermochemical decomposition of organic polymers and plastics at elevated temperatures in an oxygen-free atmosphere."
    },
    {
        "q": "Fill in the blank: In the 7 R's framework, re-evaluating our consumption habits to eliminate unnecessary purchases before generating waste is termed ________.",
        "options": ["Rethink", "Recycle", "Recharge", "Recover"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Rethink invites consumers to analyze their true needs and choose environmentally sustainable lifestyles before purchasing."
    },
    {
        "q": "Fill in the blank: The accumulation of non-biodegradable synthetic chemical pollutants in increasing concentrations across successive trophic levels of a food chain is called ________.",
        "options": ["biomagnification", "biofertilization", "bioremediation", "biomimicry"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "Biomagnification is the progressive increase in the concentration of toxic non-biodegradable substances (e.g. microplastics, heavy metals) as they pass up the food web."
    },
    {
        "q": "If a family of 4 generates 2.5 kg of total municipal solid waste per day, how many kilograms of waste do they produce over a 30-day month?",
        "options": ["75", "60", "90", "100"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total waste generated = 2.5 kg/day * 30 days = 75 kg."
    },
    {
        "q": "If 60% of a city's 500 tonnes of daily garbage is biodegradable wet waste and the remaining 40% is dry waste, how many tonnes of wet waste can be diverted to composting plants each day?",
        "options": ["300", "200", "250", "350"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Wet waste tonnes = 500 * 0.60 = 300 tonnes per day."
    },
    {
        "q": "Plastic micro-particles are formally defined by marine ecologists as synthetic polymer particles having a maximum diameter less than how many millimeters?",
        "options": ["5", "10", "1", "15"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Under international scientific consensus, microplastics are defined as synthetic solid plastic particles ranging from 1 micrometer to 5 millimeters in size."
    },
    {
        "q": "If a municipal recycling facility processes 80 tonnes of discarded PET plastic bottles into 64 tonnes of clean recycled polyester fiber pellets, what is the process recovery efficiency percentage?",
        "options": ["80", "75", "85", "90"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Recovery Efficiency = (64 tonnes / 80 tonnes) * 100 = 80%."
    },
    {
        "q": "How many core principles comprise the modern environmental 'R' framework recognized for sustainable solid waste management?",
        "options": ["7", "3", "5", "10"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The expanded sustainable framework comprises the 7 R's: Rethink, Refuse, Reduce, Reuse, Recycle, Regulate, and Recover."
    }
]

practice_data = [
    {
        "q": "Which of the following materials is completely non-biodegradable under natural atmospheric conditions?",
        "options": ["Aluminum beverage foil", "Woolen pullover", "Leather shoe", "Mango seed"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Aluminum foil is an inorganic elemental metal that does not undergo microbial enzymatic decomposition; organic materials like wool, leather, and seeds decay biologically."
    },
    {
        "q": "What is the primary objective of sanitary landfilling compared to traditional open dumping?",
        "options": [
            "Lining the landfill base with impermeable clay and geomembranes to prevent leachate from polluting groundwater",
            "Allowing garbage to wash freely into adjacent rivers",
            "Burning waste continuously day and night",
            "Mixing hazardous hospital waste into residential garden soil"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Sanitary landfills are engineered with protective composite liners, leachate drainage systems, and soil daily covers to prevent soil and groundwater contamination."
    },
    {
        "q": "Which common household item contains toxic mercury and must never be broken or disposed of in general domestic garbage?",
        "options": ["Compact Fluorescent Lamps (CFLs) and old mercury thermometers", "Ordinary ceramic dinner plates", "Stainless steel spoons", "Cotton bedsheets"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "CFL bulbs and glass mercury thermometers contain elemental mercury vapor, which is neurotoxic upon inhalation and bioaccumulative in waterways."
    },
    {
        "q": "What term describes the extraction of useful energy, electricity, or heat from non-recyclable solid waste through incineration or gasification?",
        "options": ["Waste-to-Energy (WtE) recovery", "Deep ocean trench disposal", "Atmospheric dusting", "Subterranean leaching"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Waste-to-Energy (WtE) technologies recover thermal and electrical energy from municipal combustible residues, fulfilling the 'Recover' principle."
    },
    {
        "q": "Why is the use of thin plastic carry bags (less than 120 microns) banned under India's Plastic Waste Management Rules?",
        "options": [
            "Thin plastic bags have minimal scrap value, get littered everywhere, choke city storm-drains, and are eaten by grazing cows",
            "They are too expensive for ordinary citizens to purchase",
            "They block satellite radio communications",
            "They conduct high-voltage electric currents spontaneously"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Thin bags cannot be collected or recycled economically by ragpickers, causing massive drain blockages, urban flooding, and intestinal obstruction in stray livestock."
    },
    {
        "q": "Which organism is commonly used in vermicomposting to convert wet organic kitchen scraps into high-quality organic vermicompost?",
        "options": ["Red earthworms (Eisenia fetida)", "Honeybees", "Ladybird beetles", "Mosquito larvae"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Eisenia fetida (red wigglers) are voracious epigeic earthworms that feed on decaying organic matter, excreting rich worm castings (vermicompost)."
    },
    {
        "q": "Which component of an automobile is the largest source of recyclable secondary lead metal?",
        "options": ["Lead-acid starter battery", "Rubber radial tires", "Tempered glass windshield", "Cast-iron engine block"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Lead-acid car batteries have a high recycling rate (>95%), allowing the lead electrodes and sulfuric acid to be recovered and remanufactured."
    },
    {
        "q": "What is the primary gas generated by the anaerobic decomposition of wet organic waste in deep landfill layers?",
        "options": ["Methane (CH4)", "Pure helium (He)", "Sulfur hexafluoride (SF6)", "Nitrous oxide (N2O)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Anaerobic methanogenic bacteria digest organic waste in deep landfill strata, producing landfill gas consisting of approximately 50-55% methane and 45% carbon dioxide."
    },
    {
        "q": "Why is landfill gas (methane) collected using vertical extraction wells in modern sanitary landfills?",
        "options": [
            "To prevent underground fires/explosions and harness the methane for green electricity generation",
            "To pump the methane into municipal drinking water pipes",
            "To create thick clouds of fog over the city",
            "To cool down the global stratosphere"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Methane is flammable and a potent greenhouse gas (28x more potent than CO2). Capturing it eliminates explosion hazards and provides clean electrical power."
    },
    {
        "q": "Which type of waste constitutes the largest percentage by weight in typical Indian municipal solid waste (MSW)?",
        "options": ["Biodegradable organic / wet kitchen waste (50-60%)", "Electronic computer chips (<2%)", "Automobile tires (<3%)", "Dry glass bottles (<5%)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "In developing countries like India, wet compostable kitchen food waste makes up more than 50% of the daily municipal waste stream."
    },
    {
        "q": "What is 'E-waste mining' (urban mining)?",
        "options": [
            "Recovering valuable precious metals (gold, silver, copper, palladium) from discarded electronics rather than extracting virgin ores from mines",
            "Digging deep coal mines in urban city centers",
            "Installing computer servers in agricultural fields",
            "Burying computers under concrete highways"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Urban mining recovers precious and rare-earth metals from electronic scrap, consuming up to 80% less energy than virgin subterranean mineral extraction."
    },
    {
        "q": "Which plastic polymer, represented by resin identification code 5, is widely used for reusable microwave food containers and medicine bottles due to its high heat resistance?",
        "options": ["Polypropylene (PP)", "Polystyrene (PS)", "Polyvinyl chloride (PVC)", "Low-Density Polyethylene (LDPE)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Polypropylene (PP, code 5) has a high melting point (~160 deg C), excellent chemical resistance, and is safe for microwave-safe foodware."
    },
    {
        "q": "Which color bag is designated for discarded glass bottles and medicine vials in hospital biomedical waste disposal?",
        "options": ["Blue bag / cardboard box", "Yellow bag", "Red bag", "Black container"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Blue-coded puncture-proof boxes or bags are designated for glassware (ampoules, vials, microscope slides) in biomedical facilities."
    },
    {
        "q": "What is the consequence of marine animals (such as sea turtles) mistaking floating translucent plastic bags for jellyfish?",
        "options": [
            "Severe intestinal blockage leading to starvation and death",
            "Immediate evolution into terrestrial reptiles",
            "Enhanced swimming speed and reproductive rates",
            "Increased ability to digest marine coral reefs"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Sea turtles ingest floating plastic bags mistaking them for jellyfish; the non-digestible plastic impacts their gastrointestinal tract, causing fatal blockage."
    },
    {
        "q": "Which solid waste management principle is exemplified when an individual refills an ink cartridge or reuses glass jam jars to store kitchen spices?",
        "options": ["Reuse", "Incinerate", "Recover", "Discard"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Reusing items in their existing form extends product lifespan and delays disposal into landfills."
    },
    {
        "q": "Select ALL items classified as Dry (Non-biodegradable) Waste suitable for blue municipal bins:",
        "options": [
            "Clean cardboard shipping cartons",
            "Empty tin cans and soda cans",
            "Discarded plastic bottles",
            "Rotten tomatoes and watermelon rinds"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Cardboard, tin cans, and plastic bottles are recyclable dry waste. Rotten tomatoes and melon rinds are wet biodegradable kitchen waste."
    },
    {
        "q": "Select ALL environmental benefits of practicing vermicomposting at home:",
        "options": [
            "Reduces garbage volume sent to municipal landfills",
            "Produces chemical-free, nutrient-rich organic bio-fertilizer for plants",
            "Eliminates greenhouse gas emissions associated with garbage transport",
            "Increases the amount of toxic plastic in the soil"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Home vermicomposting minimizes municipal transport burdens, enriches garden soil, and lowers landfill methane emissions."
    },
    {
        "q": "Select ALL hazardous domestic waste items that must NOT be thrown into general garbage bins:",
        "options": [
            "Discarded chemical paint cans and thinner bottles",
            "Used automotive motor oil",
            "Rechargeable lithium-ion phone batteries",
            "Dry vegetable peelings"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Paints, motor oil, and lithium batteries contain toxic, flammable, and corrosive chemicals and require dedicated hazardous disposal."
    },
    {
        "q": "True or False: Burning dry autumn leaves in open residential gardens is an eco-friendly waste disposal practice.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Burning leaf piles releases thick toxic smoke and carbon monoxide; leaves should instead be composted to nourish soil."
    },
    {
        "q": "True or False: Aluminum and steel cans can be recycled indefinitely without losing their inherent structural metal properties.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Metals are infinitely recyclable elements; remelting aluminum saves 95% of the energy required to extract primary aluminum from bauxite ore."
    },
    {
        "q": "True or False: Biomedical sharps (needles and surgical scalpels) can be safely discarded directly in ordinary blue plastic bags alongside dry paper.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Sharps puncture bags and transmit dangerous bloodborne pathogens (HIV, Hepatitis B/C) to waste workers; they must be put into puncture-proof white containers."
    },
    {
        "q": "True or False: Leachate from open dumps can infiltrate permeable soil layers and contaminate deep underground drinking water wells.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. In unlined dumps, rainwater dissolves toxic metals and organic toxins, creating toxic leachate that percolates into the underlying water table."
    },
    {
        "q": "Assertion (A): Microplastics pose a severe threat to marine ecosystems.\\nReason (R): Microplastics absorb persistent organic pollutants from seawater and are ingested by zooplankton and small fish, entering the human marine food chain.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Microplastics act as hydrophobic sponges for environmental toxins like PCBs and DDT, bioaccumulating across marine trophic levels."
    },
    {
        "q": "Assertion (A): Recycling aluminum cans saves substantial electrical energy compared to producing new aluminum from bauxite ore.\\nReason (R): Bauxite refining via the Hall-Héroult electrolytic smelting process requires massive continuous electrical current at extreme temperatures.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Primary aluminum extraction requires about 14-15 kWh of electricity per kg, whereas remelting clean scrap aluminum requires only 5% of that energy."
    },
    {
        "q": "Fill in the blank: The engineered waste disposal site that prevents contamination through impermeable bottom liners and daily soil compaction is a ________ landfill.",
        "options": ["sanitary", "open", "subterranean", "marine"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "A sanitary landfill is an engineered facility designed to isolate waste from the surrounding environment."
    },
    {
        "q": "Fill in the blank: The dark, crumbly organic residue formed after the complete microbial decomposition of wet agricultural and kitchen waste is called ________.",
        "options": ["compost", "slag", "leachate", "ash"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Compost is biologically stabilized humus that enriches soil structure and replenishes macronutrients (NPK)."
    },
    {
        "q": "Fill in the blank: Puncture-proof containers designated for collecting used medical syringes and needles are colored ________ under BMW rules.",
        "options": ["white (translucent)", "yellow", "green", "black"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Under Indian Biomedical Waste Management rules, White puncture-proof, tamper-proof containers are strictly reserved for sharps."
    },
    {
        "q": "Fill in the blank: The economic model that aims to eliminate waste by continually keeping resources in productive use through repair, reuse, and recycling is called the ________ economy.",
        "options": ["circular", "linear", "disposable", "extractive"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "A circular economy replaces the traditional 'take-make-dispose' linear economy with closed-loop recycling and reuse."
    },
    {
        "q": "If an average citizen consumes and discards 150 single-use plastic water bottles in a year, how many bottles does a housing society with 200 residents discard annually?",
        "options": ["30000", "15000", "20000", "50000"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total bottles = 150 * 200 = 30,000 plastic bottles per year."
    },
    {
        "q": "If recycling 1 tonne of paper saves approximately 17 mature trees from being felled, how many mature trees are conserved by a school district that collects and recycles 10 tonnes of waste exam paper?",
        "options": ["170", "100", "250", "340"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Trees saved = 10 tonnes * 17 trees/tonne = 170 mature trees."
    }
]

svg_diagrams = [
    # SVG 1: Wet vs Dry Bin Segregation
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Source Segregation: Green Bin (Wet) vs Blue Bin (Dry)</text>
  <!-- Green Bin -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="170" height="165" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
    <text x="85" y="28" fill="#86efac" font-size="13" font-weight="bold" text-anchor="middle">GREEN BIN (Wet Waste)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Vegetable &amp; fruit peels</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Leftover cooked food</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Tea leaves, egg shells</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Garden leaves &amp; flowers</text>
    <rect x="15" y="136" width="140" height="20" rx="4" fill="#15803d"/>
    <text x="85" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Compost / Biogas</text>
  </g>
  <!-- Blue Bin -->
  <g transform="translate(270, 45)">
    <rect x="0" y="0" width="170" height="165" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
    <text x="85" y="28" fill="#7dd3fc" font-size="13" font-weight="bold" text-anchor="middle">BLUE BIN (Dry Waste)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Plastic bottles &amp; cups</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Paper, cardboard, newsprint</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Metal tins &amp; foil</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Clean glass jars</text>
    <rect x="15" y="136" width="140" height="20" rx="4" fill="#0284c7"/>
    <text x="85" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Recycle / Material Recovery</text>
  </g>
</svg>''',

    # SVG 2: Decomposition Timeline
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Environmental Degradation Timeline of Common Waste</text>
  <!-- Timeline bars -->
  <g transform="translate(30, 45)">
    <!-- Banana Peel -->
    <rect x="0" y="0" width="440" height="28" rx="4" fill="#1e293b"/>
    <rect x="0" y="0" width="40" height="28" rx="4" fill="#22c55e"/>
    <text x="50" y="18" fill="#f8fafc" font-size="11">Banana Peel / Food Scraps: 3 to 4 Weeks</text>
    <!-- Paper -->
    <rect x="0" y="36" width="440" height="28" rx="4" fill="#1e293b"/>
    <rect x="0" y="36" width="85" height="28" rx="4" fill="#10b981"/>
    <text x="95" y="54" fill="#f8fafc" font-size="11">Paper &amp; Cardboard: 2 to 5 Months</text>
    <!-- Aluminum Can -->
    <rect x="0" y="72" width="440" height="28" rx="4" fill="#1e293b"/>
    <rect x="0" y="72" width="200" height="28" rx="4" fill="#f59e0b"/>
    <text x="210" y="90" fill="#f8fafc" font-size="11">Aluminum Beverage Can: 80 to 200 Years</text>
    <!-- Plastic Bottle -->
    <rect x="0" y="108" width="440" height="28" rx="4" fill="#1e293b"/>
    <rect x="0" y="108" width="340" height="28" rx="4" fill="#ef4444"/>
    <text x="350" y="126" fill="#fca5a5" font-size="11">Plastic PET Bottle: 450+ Years</text>
    <!-- Glass Bottle -->
    <rect x="0" y="144" width="440" height="28" rx="4" fill="#1e293b"/>
    <rect x="0" y="144" width="440" height="28" rx="4" fill="#be123c"/>
    <text x="220" y="162" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Glass Bottle: 1 Million+ Years (Non-biodegradable)</text>
  </g>
</svg>''',

    # SVG 3: The 7 R's Pyramid
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hierarchy of Waste Management: The 7 R&#39;s</text>
  <!-- Pyramid Tiers -->
  <g transform="translate(100, 45)">
    <!-- Top tier: Refuse / Rethink -->
    <polygon points="150,0 80,35 220,35" fill="#15803d"/>
    <text x="150" y="25" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. RETHINK &amp; REFUSE</text>
    <!-- Tier 2: Reduce -->
    <polygon points="80,38 220,38 250,75 50,75" fill="#16a34a"/>
    <text x="150" y="60" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2. REDUCE at Source</text>
    <!-- Tier 3: Reuse -->
    <polygon points="50,78 250,78 280,115 20,115" fill="#0284c7"/>
    <text x="150" y="100" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. REUSE &amp; REPAIR</text>
    <!-- Tier 4: Recycle -->
    <polygon points="20,118 280,118 300,150 0,150" fill="#eab308"/>
    <text x="150" y="137" fill="#0f172a" font-size="11" font-weight="bold" text-anchor="middle">4. RECYCLE Materials</text>
    <!-- Base: Recover & Disposal -->
    <polygon points="0,153 300,153 310,180 -10,180" fill="#dc2626"/>
    <text x="150" y="170" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">5. RECOVER Energy / Landfill (Least Favored)</text>
  </g>
</svg>''',

    # SVG 4: Biomedical Waste Color Coding
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Bio-Medical Waste Management Rules: Color Coding</text>
  <!-- Yellow -->
  <g transform="translate(25, 45)">
    <rect x="0" y="0" width="105" height="155" rx="6" fill="#854d0e" stroke="#eab308"/>
    <text x="52" y="25" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">YELLOW</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Anatomical tissue</text>
    <text x="10" y="75" fill="#f8fafc" font-size="9">&#8226; Soiled cotton/gauze</text>
    <text x="10" y="95" fill="#f8fafc" font-size="9">&#8226; Expired drugs</text>
    <text x="52" y="140" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Incineration</text>
  </g>
  <!-- Red -->
  <g transform="translate(140, 45)">
    <rect x="0" y="0" width="105" height="155" rx="6" fill="#991b1b" stroke="#ef4444"/>
    <text x="52" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">RED</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Contaminated plastics</text>
    <text x="10" y="75" fill="#f8fafc" font-size="9">&#8226; IV tubing &amp; bottles</text>
    <text x="10" y="95" fill="#f8fafc" font-size="9">&#8226; Catheters, syringes</text>
    <text x="52" y="140" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Autoclave/Recycle</text>
  </g>
  <!-- White -->
  <g transform="translate(255, 45)">
    <rect x="0" y="0" width="105" height="155" rx="6" fill="#334155" stroke="#f8fafc"/>
    <text x="52" y="25" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">WHITE</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Needles &amp; scalpels</text>
    <text x="10" y="75" fill="#f8fafc" font-size="9">&#8226; Surgical blades</text>
    <text x="10" y="95" fill="#f8fafc" font-size="9">&#8226; Puncture proof box</text>
    <text x="52" y="140" fill="#f8fafc" font-size="9" font-weight="bold" text-anchor="middle">Shred / Encapsulate</text>
  </g>
  <!-- Blue -->
  <g transform="translate(370, 45)">
    <rect x="0" y="0" width="105" height="155" rx="6" fill="#075985" stroke="#38bdf8"/>
    <text x="52" y="25" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">BLUE</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Broken glassware</text>
    <text x="10" y="75" fill="#f8fafc" font-size="9">&#8226; Medicine vials</text>
    <text x="10" y="95" fill="#f8fafc" font-size="9">&#8226; Metallic implants</text>
    <text x="52" y="140" fill="#7dd3fc" font-size="9" font-weight="bold" text-anchor="middle">Disinfect / Recycle</text>
  </g>
</svg>''',

    # SVG 5: E-waste Hazardous Heavy Metals
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Toxic Contaminants in Electronic Waste (E-Waste)</text>
  <!-- Stylized circuit board -->
  <rect x="30" y="50" width="160" height="150" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
  <text x="110" y="80" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Circuit Board &amp;</text>
  <text x="110" y="96" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Electronics</text>
  <!-- Traces -->
  <path d="M 50 120 L 80 120 L 100 145 L 140 145" fill="none" stroke="#fbbf24" stroke-width="2"/>
  <circle cx="140" cy="145" r="4" fill="#fbbf24"/>
  <rect x="60" y="145" width="25" height="25" fill="#0f172a" stroke="#94a3b8"/>
  <!-- Toxic elements list -->
  <g transform="translate(215, 50)">
    <rect x="0" y="0" width="255" height="42" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="12" y="18" fill="#ef4444" font-size="11" font-weight="bold">Lead (Pb) - Solder &amp; CRT Glass</text>
    <text x="12" y="34" fill="#94a3b8" font-size="9">Damages central nervous system and kidneys</text>
    <rect x="0" y="52" width="255" height="42" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="12" y="70" fill="#f59e0b" font-size="11" font-weight="bold">Mercury (Hg) - Switches &amp; Monitors</text>
    <text x="12" y="86" fill="#94a3b8" font-size="9">Bioaccumulates in aquatic food chains</text>
    <rect x="0" y="104" width="255" height="42" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="12" y="122" fill="#38bdf8" font-size="11" font-weight="bold">Cadmium (Cd) - Chip Resistors</text>
    <text x="12" y="138" fill="#94a3b8" font-size="9">Carcinogenic and causes severe bone mineral loss</text>
  </g>
</svg>''',

    # SVG 6: Plastic Resin Codes
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Plastics Resin Identification Codes (RIC)</text>
  <!-- 6 Code badges -->
  <g transform="translate(30, 45)">
    <!-- Code 1 PET -->
    <rect x="0" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="32" y="30" fill="#38bdf8" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 1</text>
    <text x="32" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">PETE</text>
    <text x="32" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Water bottles</text>
    <!-- Code 2 HDPE -->
    <rect x="75" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="107" y="30" fill="#10b981" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 2</text>
    <text x="107" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">HDPE</text>
    <text x="107" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Milk jugs</text>
    <!-- Code 3 PVC -->
    <rect x="150" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="182" y="30" fill="#ef4444" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 3</text>
    <text x="182" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">PVC</text>
    <text x="182" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Pipes</text>
    <!-- Code 4 LDPE -->
    <rect x="225" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="257" y="30" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 4</text>
    <text x="257" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">LDPE</text>
    <text x="257" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Grocery bags</text>
    <!-- Code 5 PP -->
    <rect x="300" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#8b5cf6"/>
    <text x="332" y="30" fill="#a78bfa" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 5</text>
    <text x="332" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">PP</text>
    <text x="332" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Food boxes</text>
    <!-- Code 6 PS -->
    <rect x="375" y="0" width="65" height="70" rx="6" fill="#1e293b" stroke="#be123c"/>
    <text x="407" y="30" fill="#fb7185" font-size="18" font-weight="bold" text-anchor="middle">&#9851; 6</text>
    <text x="407" y="50" fill="#f8fafc" font-size="10" text-anchor="middle">PS</text>
    <text x="407" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Thermocol</text>
  </g>
  <!-- Summary text -->
  <rect x="30" y="135" width="440" height="75" rx="6" fill="#334155"/>
  <text x="250" y="160" fill="#fef08a" font-size="12" font-weight="bold" text-anchor="middle">Recyclability Hierarchy</text>
  <text x="250" y="180" fill="#f8fafc" font-size="11" text-anchor="middle">Codes 1 (PET) and 2 (HDPE) are most easily and widely recycled.</text>
  <text x="250" y="196" fill="#fca5a5" font-size="11" text-anchor="middle">Codes 3 (PVC) and 6 (PS / Thermocol) are hazardous and rarely recycled.</text>
</svg>''',

    # SVG 7: Solid Waste Composition Pie Chart
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Typical Municipal Solid Waste (MSW) Composition in India</text>
  <!-- Visual breakdown bars -->
  <g transform="translate(40, 50)">
    <!-- Wet Waste 55% -->
    <rect x="0" y="0" width="230" height="35" rx="4" fill="#16a34a"/>
    <text x="115" y="22" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Biodegradable / Wet Waste (55%)</text>
    <!-- Paper 15% -->
    <rect x="0" y="42" width="63" height="30" rx="4" fill="#0284c7"/>
    <text x="75" y="62" fill="#7dd3fc" font-size="11">Paper &amp; Cardboard (15%)</text>
    <!-- Plastic 12% -->
    <rect x="0" y="78" width="50" height="30" rx="4" fill="#eab308"/>
    <text x="65" y="98" fill="#fef08a" font-size="11">Plastics (12%)</text>
    <!-- Glass & Metal 8% -->
    <rect x="0" y="114" width="34" height="30" rx="4" fill="#8b5cf6"/>
    <text x="45" y="134" fill="#ddd6fe" font-size="11">Glass &amp; Metal (8%)</text>
    <!-- Inerts & Others 10% -->
    <rect x="0" y="150" width="42" height="25" rx="4" fill="#64748b"/>
    <text x="55" y="167" fill="#cbd5e1" font-size="11">Inerts, Dirt &amp; Street Sweepings (10%)</text>
  </g>
</svg>''',

    # SVG 8: Marine Plastic Biomagnification
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Microplastic Biomagnification in Aquatic Food Webs</text>
  <!-- Step 1: Plastic litter -->
  <g transform="translate(15, 60)">
    <rect x="0" y="0" width="95" height="90" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="47" y="25" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Plastic Litter</text>
    <text x="47" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Bottles, bags</text>
    <text x="47" y="60" fill="#94a3b8" font-size="8" text-anchor="middle">Solar UV &amp; Waves</text>
    <text x="47" y="75" fill="#fca5a5" font-size="8" text-anchor="middle">&#8594; Microplastics</text>
  </g>
  <!-- Arrow -->
  <path d="M 115 105 L 135 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 2: Zooplankton -->
  <g transform="translate(140, 60)">
    <rect x="0" y="0" width="95" height="90" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="47" y="25" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Zooplankton</text>
    <text x="47" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Ingest microplastic</text>
    <text x="47" y="60" fill="#94a3b8" font-size="8" text-anchor="middle">particles mistaken</text>
    <text x="47" y="75" fill="#94a3b8" font-size="8" text-anchor="middle">for phytoplankton</text>
  </g>
  <!-- Arrow -->
  <path d="M 240 105 L 260 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 3: Small Fish -->
  <g transform="translate(265, 60)">
    <rect x="0" y="0" width="95" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="47" y="25" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">Small Fish</text>
    <text x="47" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Feed on plankton</text>
    <text x="47" y="60" fill="#94a3b8" font-size="8" text-anchor="middle">Toxins accumulate</text>
    <text x="47" y="75" fill="#94a3b8" font-size="8" text-anchor="middle">in fatty tissue</text>
  </g>
  <!-- Arrow -->
  <path d="M 365 105 L 385 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 4: Apex Consumer / Humans -->
  <g transform="translate(390, 60)">
    <rect x="0" y="0" width="95" height="90" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="47" y="25" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Humans / Birds</text>
    <text x="47" y="45" fill="#f8fafc" font-size="8" text-anchor="middle">Apex Predators</text>
    <text x="47" y="60" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Highest Toxic</text>
    <text x="47" y="75" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Concentration</text>
  </g>
  <!-- Bottom note -->
  <text x="250" y="195" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">BIOMAGNIFICATION: Concentration increases up the food chain</text>
</svg>''',

    # SVG 9: Leachate Contamination of Groundwater
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Leachate Percolation from Open Dumps into Groundwater</text>
  <!-- Garbage Mound -->
  <path d="M 80 85 L 200 45 L 320 85 Z" fill="#78350f" stroke="#b45309" stroke-width="2"/>
  <text x="200" y="70" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Unlined Garbage Dump</text>
  <!-- Ground level line -->
  <line x1="40" y1="85" x2="460" y2="85" stroke="#64748b" stroke-width="2"/>
  <!-- Rain falling -->
  <line x1="160" y1="30" x2="160" y2="40" stroke="#38bdf8" stroke-dasharray="2"/>
  <line x1="200" y1="28" x2="200" y2="38" stroke="#38bdf8" stroke-dasharray="2"/>
  <line x1="240" y1="30" x2="240" y2="40" stroke="#38bdf8" stroke-dasharray="2"/>
  <text x="320" y="38" fill="#38bdf8" font-size="10">Rainfall Infiltration</text>
  <!-- Leachate seepage arrows -->
  <path d="M 200 85 L 200 135" stroke="#ef4444" stroke-width="3" stroke-dasharray="3"/>
  <text x="205" y="115" fill="#fca5a5" font-size="10" font-weight="bold">Toxic Leachate</text>
  <!-- Groundwater aquifer layer -->
  <rect x="40" y="140" width="420" height="55" rx="6" fill="#0369a1" fill-opacity="0.3" stroke="#0284c7"/>
  <text x="250" y="165" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Groundwater Aquifer / Drinking Water Table</text>
  <!-- Contamination plume -->
  <ellipse cx="200" cy="165" rx="80" ry="20" fill="#7f1d1d" fill-opacity="0.6"/>
  <text x="200" y="170" fill="#fecaca" font-size="9" text-anchor="middle">Heavy metals &amp; organic poisons</text>
</svg>''',

    # SVG 10: Packaging Environmental Footprint
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Shopping Bags: Single-Use Plastic vs Reusable Cotton Bag</text>
  <!-- Plastic Bag -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="180" height="150" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="90" y="25" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Single-Use Plastic Bag</text>
    <text x="15" y="55" fill="#f8fafc" font-size="10">&#8226; Average use: 12 minutes</text>
    <text x="15" y="75" fill="#f8fafc" font-size="10">&#8226; Degrades in 400+ years</text>
    <text x="15" y="95" fill="#f8fafc" font-size="10">&#8226; Chokes storm-water drains</text>
    <text x="15" y="115" fill="#f8fafc" font-size="10">&#8226; Ingested by cattle and marine life</text>
    <rect x="15" y="125" width="150" height="18" rx="4" fill="#7f1d1d"/>
    <text x="90" y="138" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">High Environmental Hazard</text>
  </g>
  <!-- Reusable Bag -->
  <g transform="translate(280, 50)">
    <rect x="0" y="0" width="180" height="150" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="90" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Reusable Cotton / Jute Bag</text>
    <text x="15" y="55" fill="#f8fafc" font-size="10">&#8226; Reused hundreds of times</text>
    <text x="15" y="75" fill="#f8fafc" font-size="10">&#8226; Natural plant fiber (cellulose)</text>
    <text x="15" y="95" fill="#f8fafc" font-size="10">&#8226; 100% Biodegradable</text>
    <text x="15" y="115" fill="#f8fafc" font-size="10">&#8226; Easily washable and durable</text>
    <rect x="15" y="125" width="150" height="18" rx="4" fill="#14532d"/>
    <text x="90" y="138" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Sustainable Choice</text>
  </g>
</svg>''',

    # SVG 11: Hazardous Symbols Triad
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hazardous Chemical Waste Identification Symbols</text>
  <!-- Corrosive -->
  <g transform="translate(40, 55)">
    <polygon points="55,5 105,95 5,95" fill="#1e293b" stroke="#eab308" stroke-width="3"/>
    <text x="55" y="120" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Corrosive</text>
    <text x="55" y="138" fill="#94a3b8" font-size="9" text-anchor="middle">Acids &amp; Strong Alkalis</text>
    <text x="55" y="150" fill="#94a3b8" font-size="9" text-anchor="middle">Destroys skin / metal</text>
  </g>
  <!-- Flammable -->
  <g transform="translate(195, 55)">
    <polygon points="55,5 105,95 5,95" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
    <text x="55" y="120" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">Flammable</text>
    <text x="55" y="138" fill="#94a3b8" font-size="9" text-anchor="middle">Solvents, paints &amp; oils</text>
    <text x="55" y="150" fill="#94a3b8" font-size="9" text-anchor="middle">Catches fire easily</text>
  </g>
  <!-- Toxic / Poison -->
  <g transform="translate(350, 55)">
    <polygon points="55,5 105,95 5,95" fill="#1e293b" stroke="#a855f7" stroke-width="3"/>
    <text x="55" y="120" fill="#d8b4fe" font-size="12" font-weight="bold" text-anchor="middle">Toxic / Poison</text>
    <text x="55" y="138" fill="#94a3b8" font-size="9" text-anchor="middle">Pesticides &amp; Mercury</text>
    <text x="55" y="150" fill="#94a3b8" font-size="9" text-anchor="middle">Fatal if ingested</text>
  </g>
</svg>''',

    # SVG 12: Circular vs Linear Economy
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Resource Models: Linear Economy vs Circular Economy</text>
  <!-- Linear Economy -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="205" height="150" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="102" y="25" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Linear Economy (Take-Make-Waste)</text>
    <text x="20" y="60" fill="#f8fafc" font-size="11">Raw Materials &#8594; Extraction</text>
    <text x="20" y="85" fill="#f8fafc" font-size="11">Manufacturing &#8594; Product</text>
    <text x="20" y="110" fill="#f8fafc" font-size="11">One-time Use &#8594; Landfill Dump</text>
    <text x="102" y="138" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Resource Depletion &amp; High Waste</text>
  </g>
  <!-- Circular Economy -->
  <g transform="translate(265, 50)">
    <rect x="0" y="0" width="205" height="150" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="102" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Circular Economy (Closed Loop)</text>
    <text x="20" y="60" fill="#34d399" font-size="11">Design for Longevity</text>
    <text x="20" y="85" fill="#34d399" font-size="11">Reuse, Repair, Remanufacture</text>
    <text x="20" y="110" fill="#34d399" font-size="11">Recycle &amp; Biological Composting</text>
    <text x="102" y="138" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Zero Waste &amp; Sustainable Growth</text>
  </g>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the municipal waste segregation guide, which category of waste is correctly assigned to the Green Bin?",
        "options": [
            "Vegetable scraps, fruit peels, and leftover food suitable for composting",
            "Crushed aluminum beverage cans and steel cutlery",
            "Intact glass bottles and laboratory test tubes",
            "Electronic computer motherboards and mobile batteries"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The green bin is strictly reserved for biodegradable wet waste like vegetable peels and kitchen food scraps that can be converted into organic compost or biogas."
    },
    {
        "q": "Referring to the environmental degradation timeline, why are plastic bottles and glass containers considered far more hazardous to landfills than banana peels?",
        "options": [
            "Banana peels decompose in a few weeks, whereas plastics persist for over 450 years and glass for over a million years",
            "Plastics dissolve instantly in air and create vacuum pockets",
            "Banana peels emit radioactive alpha particles",
            "Glass containers spontaneously explode when touched by rainwater"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The timeline contrasts organic items (which biodegrade within weeks) with synthetic polymers and silicates (which resist microbial enzymes for centuries or millennia)."
    },
    {
        "q": "According to the 7 R's waste management hierarchy pyramid, which level represents the most preferred action at the very top of the pyramid?",
        "options": [
            "Rethink and Refuse unnecessary single-use items",
            "Open dumping on public roads",
            "Landfilling in rural wetlands",
            "Incinerating waste without energy recovery"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The pinnacle of the hierarchy is 'Rethink & Refuse', preventing waste from being generated in the first place, whereas disposal in landfills is the least favored option at the base."
    },
    {
        "q": "In the Bio-Medical Waste color-coding diagram, what treatment method is mandated for human anatomical waste and infected gauze disposed in YELLOW containers?",
        "options": [
            "High-temperature incineration",
            "Dumping in municipal open drainage",
            "Composting in residential vegetable patches",
            "Feeding directly to stray animals"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Yellow-bagged pathological and anatomical waste must be destroyed via controlled high-temperature medical incineration to eliminate pathogens and disease transmission."
    },
    {
        "q": "Based on the toxic contaminants diagram of e-waste, which heavy metal present in solder and cathode ray tubes attacks the human central nervous system?",
        "options": ["Lead (Pb)", "Calcium (Ca)", "Iron (Fe)", "Magnesium (Mg)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Lead (Pb) in solders and CRT glass is a potent neurotoxicant that causes severe irreversible damage to the brain, kidneys, and peripheral nervous system."
    },
    {
        "q": "Observing the Resin Identification Code (RIC) chart, which plastic resin code corresponds to High-Density Polyethylene (HDPE) commonly used for sturdy milk bottles and shampoo containers?",
        "options": ["2", "1", "3", "6"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Resin code 2 identifies HDPE (High-Density Polyethylene), a strong, rigid, easily recycled thermoplastic."
    },
    {
        "q": "According to the municipal solid waste composition chart, what fraction of Indian urban garbage consists of compostable, biodegradable organic matter?",
        "options": [
            "More than 50% (approximately 55%)",
            "Less than 5%",
            "Exactly 100%",
            "Zero percent"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The chart illustrates that wet organic waste constitutes the majority (approximately 55%) of Indian municipal solid waste."
    },
    {
        "q": "In the marine food chain biomagnification diagram, why do apex predators and humans end up with the highest concentration of microplastic-associated toxins?",
        "options": [
            "Toxins bioaccumulate in fatty tissues and multiply at each successive trophic feeding level",
            "Apex predators only eat pure sand from the sea floor",
            "Microplastics multiply biologically inside fish like bacteria",
            "Sunlight generates microplastics directly inside animal blood"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Non-biodegradable persistent contaminants are not excreted; as each predator consumes numerous prey, the concentration of toxins magnifies at higher trophic tiers."
    },
    {
        "q": "Examining the leachate percolation diagram, what natural resource is directly contaminated when rainwater seeps through an unlined garbage dump?",
        "options": [
            "Underground aquifer / drinking water table",
            "The upper stratospheric ozone layer",
            "Solar ultraviolet rays",
            "Lunar gravitational tides"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Rainwater dissolving soluble pollutants forms toxic leachate that filters downward through porous soil strata, poisoning groundwater aquifers and nearby wells."
    },
    {
        "q": "Based on the shopping bag footprint comparison, what is the primary ecological advantage of using a cotton or jute tote bag?",
        "options": [
            "It can be reused hundreds of times and is completely biodegradable upon eventual disposal",
            "It never gets dirty and cannot be washed",
            "It is made of synthetic petroleum polymers",
            "It repels all forms of sunlight"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Cotton and jute bags are made of durable, renewable plant fibers that can be reused for years, eliminating hundreds of disposable plastic bags."
    },
    {
        "q": "Referring to the hazardous symbols panel, which symbol warns that a chemical can cause severe burns to human skin and corrode metal containers?",
        "options": ["Corrosive symbol (acid pouring on surface and hand)", "Flammable flame symbol", "Toxic skull and crossbones", "Biohazard symbol"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The corrosive symbol denotes strong acids or alkalis that chemically attack and destroy living tissue and structural metals."
    },
    {
        "q": "Based on the economic resource models diagram, how does a Circular Economy differ fundamentally from a traditional Linear Economy?",
        "options": [
            "A circular economy loops resources through reuse, repair, and recycling to eliminate waste, whereas a linear economy discards products after one use",
            "A circular economy relies entirely on single-use plastics",
            "A linear economy has zero waste and protects all natural minerals",
            "Both models dump all manufactured products into the ocean"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A circular economy decouples economic activity from finite resource consumption by designing closed-loop systems that prioritize maintenance, reuse, and recycling."
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
