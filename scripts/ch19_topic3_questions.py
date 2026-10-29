# -*- coding: utf-8 -*-
"""
Chapter 19 Topic 19.3 Gold-Standard Question Authoring Engine
Class 9 Science & Technology: Class 7 Science Foundation Core
Topic 19.3: Properties of Matter, Chemical Changes & Natural Resources (7th Review)
Total: 40 brand-new gold-standard questions (20 OSC, 8 OTF, 6 OAR, 6 OMC)
"""

import json

qs_t3 = []

# --- 20 OSC QUESTIONS ---
osc_t3 = [
    {
        "code": "MH-9-SCIT-19-19.3-OSC-001",
        "text": "Which of the following processes is a chemical change?",
        "options": ["Melting of ice into water", "Dissolving sugar in water", "Rusting of an iron nail", "Tearing a sheet of paper into small pieces"],
        "ca": "C",
        "concept": "A chemical change involves a chemical reaction where new substances with entirely different chemical properties are formed through molecular rearrangement (e.g., formation of hydrated iron(III) oxide during rusting).",
        "analysis": [
            "Incorrect; melting of ice is a reversible physical change of state without altering molecular \\(\\ce{H2O}\\).",
            "Incorrect; dissolving sugar is a reversible physical dissolution process.",
            "Rusting is an irreversible chemical oxidation forming a brand-new chemical compound (hydrated iron(III) oxide, \\(\\ce{Fe2O3.xH2O}\\)).",
            "Incorrect; tearing paper changes only size and shape (physical change)."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-002",
        "text": "What color change is observed when blue litmus paper is dipped into an acidic solution (such as dilute hydrochloric acid)?",
        "options": ["Turns bright red", "Turns dark green", "Turns yellow", "Remains blue"],
        "ca": "A",
        "concept": "Litmus is a natural acid-base indicator extracted from lichens. Under acidic conditions (pH < 7), blue litmus paper turns red.",
        "analysis": [
            "Blue litmus turns red in the presence of acidic hydrogen ions (\\(\\ce{H+}\\)).",
            "Incorrect; green is characteristic of neutral universal indicator, not litmus paper.",
            "Incorrect; yellow is observed with methyl orange in neutral/basic solutions.",
            "Incorrect; remaining blue indicates a neutral or alkaline solution."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-003",
        "text": "Which acid is naturally present in curd (yogurt) and sour milk?",
        "options": ["Acetic acid", "Lactic acid", "Citric acid", "Oxalic acid"],
        "ca": "B",
        "concept": "Lactic acid bacteria (such as \\(\\textit{Lactobacillus}\\)) ferment lactose sugar in milk into lactic acid, imparting curd its characteristic sour taste.",
        "analysis": [
            "Incorrect; acetic acid is the primary component of vinegar.",
            "Lactic acid is produced by bacterial fermentation of milk lactose into curd.",
            "Incorrect; citric acid is abundant in citrus fruits like lemons and oranges.",
            "Incorrect; oxalic acid is found in tomatoes and spinach."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-004",
        "text": "What are the products formed in a standard chemical neutralisation reaction between an acid and a base?",
        "options": ["Salt and water only", "Hydrogen gas and oxygen only", "Acid and carbon dioxide", "Precipitate and ozone"],
        "ca": "A",
        "concept": "A neutralisation reaction occurs when hydrogen ions (\\(\\ce{H+}\\)) from an acid react with hydroxide ions (\\(\\ce{OH-}\\)) from a base to produce a salt and water: \\(\\text{Acid} + \\text{Base} \\to \\text{Salt} + \\ce{H2O}\\).",
        "analysis": [
            "A neutralisation reaction between an acid and a base universally yields a salt and water (\\(\\ce{HCl + NaOH -> NaCl + H2O}\\)).",
            "Incorrect; hydrogen gas is evolved when acids react with reactive metals.",
            "Incorrect; carbon dioxide is evolved when acids react with carbonates.",
            "Incorrect; ozone is an atmospheric gas, not a neutralisation product."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-005",
        "text": "Which gas is evolved with brisk effervescence when dilute hydrochloric acid is added to baking soda (sodium hydrogen carbonate)?",
        "options": ["Oxygen (\\(\\ce{O2}\\))", "Carbon dioxide (\\(\\ce{CO2}\\))", "Hydrogen (\\(\\ce{H2}\\))", "Nitrogen (\\(\\ce{N2}\\))"],
        "ca": "B",
        "concept": "Acids react with metal carbonates and hydrogen carbonates to release carbon dioxide gas with brisk effervescence: \\(\\ce{NaHCO3 + HCl -> NaCl + H2O + CO2 ^}\\).",
        "analysis": [
            "Incorrect; oxygen does not cause acidic effervescence.",
            "Carbon dioxide gas is rapidly released, turning lime water milky due to calcium carbonate precipitation.",
            "Incorrect; hydrogen gas is produced with reactive metals, not carbonates.",
            "Incorrect; nitrogen is an unreactive atmospheric gas."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-006",
        "text": "What chemical substance is commonly taken as an antacid to relieve hyperacidity and stomach burn?",
        "options": ["Dilute sulfuric acid", "Milk of magnesia (magnesium hydroxide)", "Sodium chloride", "Concentrated nitric acid"],
        "ca": "B",
        "concept": "Milk of magnesia (\\(\\ce{Mg(OH)2}\\)) is a mild, non-toxic basic suspension that neutralizes excess hydrochloric acid in gastric juice.",
        "analysis": [
            "Incorrect; sulfuric acid is a strong, highly corrosive mineral acid.",
            "Milk of magnesia (\\(\\ce{Mg(OH)2}\\)) safely neutralizes excess stomach acid, forming magnesium chloride and water.",
            "Incorrect; sodium chloride is a neutral table salt and does not neutralize acid.",
            "Incorrect; nitric acid is a powerful, dangerous oxidizing acid."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-007",
        "text": "What is the correct chemical formula of common table salt?",
        "options": ["\\(\\ce{NaCl}\\)", "\\(\\ce{KCl}\\)", "\\(\\ce{NaOH}\\)", "\\(\\ce{CaCl2}\\)"],
        "ca": "A",
        "concept": "Common table salt is chemically known as sodium chloride, composed of sodium and chlorine ions in a 1:1 ionic ratio, giving the empirical formula \\(\\ce{NaCl}\\).",
        "analysis": [
            "Sodium chloride has the chemical formula \\(\\ce{NaCl}\\).",
            "Incorrect; \\(\\ce{KCl}\\) is potassium chloride.",
            "Incorrect; \\(\\ce{NaOH}\\) is sodium hydroxide (caustic soda), a strong base.",
            "Incorrect; \\(\\ce{CaCl2}\\) is calcium chloride."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-008",
        "text": "Which gas constitutes the largest percentage of dry atmospheric air by volume (approximately 78%)?",
        "options": ["Oxygen (\\(\\ce{O2}\\))", "Nitrogen (\\(\\ce{N2}\\))", "Carbon dioxide (\\(\\ce{CO2}\\))", "Argon (\\(\\ce{Ar}\\))"],
        "ca": "B",
        "concept": "Clean dry air consists of approximately 78% diatomic nitrogen (\\(\\ce{N2}\\)), 21% oxygen (\\(\\ce{O2}\\)), 0.93% argon (\\(\\ce{Ar}\\)), and 0.04% carbon dioxide (\\(\\ce{CO2}\\)).",
        "analysis": [
            "Incorrect; oxygen makes up approximately 21% of the atmosphere.",
            "Diatomic nitrogen (\\(\\ce{N2}\\)) makes up approximately 78.08% of atmospheric air.",
            "Incorrect; carbon dioxide constitutes approximately 0.04%.",
            "Incorrect; argon constitutes approximately 0.93%."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-009",
        "text": "The dark, organic component of fertile topsoil formed by the microbial decomposition of dead plant and animal remains is called:",
        "options": ["Gravel", "Humus", "Subsoil bedrock", "Clay mineral"],
        "ca": "B",
        "concept": "Humus is rich, dark, amorphous organic matter produced by decomposer microorganisms in soil, providing essential plant nutrients and improving soil water retention.",
        "analysis": [
            "Incorrect; gravel consists of coarse rock pebbles.",
            "Humus is the dark, nutrient-rich decomposed organic fraction that gives fertile topsoil its structure.",
            "Incorrect; bedrock is the solid parent rock underlying all soil layers.",
            "Incorrect; clay consists of fine inorganic silicate minerals."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-010",
        "text": "A yellow turmeric stain on a white shirt turns reddish-brown when washed with laundry soap because:",
        "options": ["Soap solution is acidic", "Soap solution is basic (alkaline)", "Turmeric reacts with tap water only", "Soap bleaches all natural colors"],
        "ca": "B",
        "concept": "Turmeric contains the natural curcumin pigment, which acts as an acid-base indicator. Curcumin remains yellow in acidic and neutral media, but turns reddish-brown in basic solutions (like soap).",
        "analysis": [
            "Incorrect; soap is alkaline, not acidic.",
            "Soap solutions contain basic salts of fatty acids, turning the yellow curcumin in turmeric reddish-brown.",
            "Incorrect; pure tap water does not turn turmeric reddish-brown.",
            "Incorrect; soap acts as an alkaline indicator with turmeric, not a universal bleach."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-011",
        "text": "The sting of a honeybee or ant causes burning pain due to the injection of:",
        "options": ["Methanoic acid (formic acid)", "Citric acid", "Hydrochloric acid", "Sodium hydroxide"],
        "ca": "A",
        "concept": "Ants and bee stings inject formic acid (methanoic acid, \\(\\ce{HCOOH}\\)), which irritates nerves and causes local inflammation; applying mild bases like baking soda neutralizes the acid.",
        "analysis": [
            "Bee and ant venom contains formic acid (methanoic acid, \\(\\ce{HCOOH}\\)), causing painful burning sensations.",
            "Incorrect; citric acid is found in citrus fruits.",
            "Incorrect; hydrochloric acid is stomach acid.",
            "Incorrect; sodium hydroxide is a caustic base."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-012",
        "text": "Which chemical element is represented by the chemical symbol 'Fe'?",
        "options": ["Fluorine", "Iron", "Lead", "Phosphorus"],
        "ca": "B",
        "concept": "Chemical symbols of elements often derive from Latin names; 'Fe' is derived from \\(\\textit{Ferrum}\\), the Latin name for iron.",
        "analysis": [
            "Incorrect; fluorine is represented by \\(\\ce{F}\\).",
            "'Fe' represents iron, derived from its Latin root \\(\\textit{Ferrum}\\).",
            "Incorrect; lead is represented by \\(\\ce{Pb}\\) (from \\(\\textit{Plumbum}\\)).",
            "Incorrect; phosphorus is represented by \\(\\ce{P}\\)."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-013",
        "text": "What type of mixture is air classified as?",
        "options": ["Homogeneous mixture of gases", "Pure chemical compound", "Single elemental substance", "Heterogeneous colloid"],
        "ca": "A",
        "concept": "Air is a homogeneous gaseous mixture whose constituent gases (nitrogen, oxygen, argon, carbon dioxide) are uniformly distributed without chemical bonding.",
        "analysis": [
            "Air is a homogeneous solution (mixture) of multiple gases uniformly intermingled.",
            "Incorrect; air is not a compound because its gases are not chemically bonded in a fixed ratio.",
            "Incorrect; air contains multiple different chemical elements and compounds.",
            "Incorrect; clean gaseous air is a true solution, not a colloid."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-014",
        "text": "Which of the following conditions are necessary for the rusting of iron?",
        "options": ["Only oxygen", "Only dry moisture-free air", "Both oxygen and moisture (water vapor)", "Only nitrogen gas"],
        "ca": "C",
        "concept": "Rusting of iron is an electrochemical corrosion process requiring both oxygen (\\(\\ce{O2}\\)) and moisture (\\(\\ce{H2O}\\)) to form hydrated iron(III) oxide: \\(\\ce{4Fe + 3O2 + 2x H2O -> 2Fe2O3.xH2O}\\).",
        "analysis": [
            "Incorrect; iron does not rust in dry oxygen without moisture.",
            "Incorrect; iron does not rust in boiled deoxygenated water.",
            "Both oxygen and water vapor (moisture) are chemically indispensable for iron corrosion.",
            "Incorrect; nitrogen is an inert blanket that prevents rusting."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-015",
        "text": "Galvanization protects iron articles from rusting by coating them with a thin layer of:",
        "options": ["Copper", "Zinc", "Silver", "Lead"],
        "ca": "B",
        "concept": "Galvanization deposits a thin protective layer of zinc (\\(\\ce{Zn}\\)) over iron. Zinc forms an impermeable oxide barrier and acts as a sacrificial anode because it oxidizes more readily than iron.",
        "analysis": [
            "Incorrect; copper coating accelerates iron rusting if scratched.",
            "Zinc provides sacrificial cathodic protection and a physical barrier, preventing iron corrosion.",
            "Incorrect; silver is prohibitively expensive for industrial coating.",
            "Incorrect; lead is toxic and not used for galvanizing."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-016",
        "text": "What is the chemical formula of quicklime (calcium oxide)?",
        "options": ["\\(\\ce{CaO}\\)", "\\(\\ce{CaCO3}\\)", "\\(\\ce{Ca(OH)2}\\)", "\\(\\ce{CaCl2}\\)"],
        "ca": "A",
        "concept": "Quicklime is pure calcium oxide (\\(\\ce{CaO}\\)), produced by the thermal decomposition of limestone (calcium carbonate, \\(\\ce{CaCO3}\\)).",
        "analysis": [
            "Quicklime is calcium oxide with the chemical formula \\(\\ce{CaO}\\).",
            "Incorrect; \\(\\ce{CaCO3}\\) is limestone or marble.",
            "Incorrect; \\(\\ce{Ca(OH)2}\\) is slaked lime (calcium hydroxide).",
            "Incorrect; \\(\\ce{CaCl2}\\) is calcium chloride."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-017",
        "text": "When quicklime (\\(\\ce{CaO}\\)) is added to water, vigorous heat is produced along with a hissing sound, forming slaked lime. This is an example of an:",
        "options": ["Endothermic reaction", "Exothermic reaction", "Electrolytic decomposition", "Physical dissolution"],
        "ca": "B",
        "concept": "The slaking of lime (\\(\\ce{CaO + H2O -> Ca(OH)2 + Heat}\\)) releases a substantial amount of heat energy, making it a classic exothermic combination reaction.",
        "analysis": [
            "Incorrect; endothermic reactions absorb heat from the surroundings.",
            "The reaction liberates large amounts of thermal energy, boiling the water in an exothermic process.",
            "Incorrect; no electrical current is involved.",
            "Incorrect; a brand-new chemical compound (\\(\\ce{Ca(OH)2}\\)) is formed, making it a chemical change."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-018",
        "text": "Which method is commonly employed in arid and drought-prone regions to collect and store roof runoff rainwater for recharging groundwater?",
        "options": ["Open channel canal evaporation", "Rainwater harvesting", "Deforestation", "Surface strip mining"],
        "ca": "B",
        "concept": "Rainwater harvesting channels rooftop and surface precipitation through filtration beds into underground storage tanks or recharge borewells, replenishing water tables.",
        "analysis": [
            "Incorrect; open canals promote severe evaporation losses.",
            "Rainwater harvesting captures and filters rainwater to conserve fresh water and recharge aquifers.",
            "Incorrect; deforestation accelerates runoff and topsoil erosion.",
            "Incorrect; strip mining causes severe land degradation."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-019",
        "text": "Which of the following natural resources is an inexhaustible, renewable resource?",
        "options": ["Coal", "Petroleum", "Solar energy", "Natural gas"],
        "ca": "C",
        "concept": "Solar energy is an inexhaustible renewable resource powered by nuclear fusion in the Sun's core, replenishable continuously on a human timescale.",
        "analysis": [
            "Incorrect; coal is a finite fossil fuel formed over millions of years.",
            "Incorrect; petroleum is a non-renewable fossil fuel subject to depletion.",
            "Solar radiation is clean, inexhaustible, and naturally replenished every day.",
            "Incorrect; natural gas is a finite, depletable hydrocarbon resource."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.3-OSC-020",
        "text": "What type of soil has the largest particle size and highest drainage rate, but the poorest water-holding capacity?",
        "options": ["Clayey soil", "Sandy soil", "Loamy soil", "Humus-rich silt"],
        "ca": "B",
        "concept": "Sandy soil consists of large mineral particles (> 0.05 mm) with large pore spaces, allowing water to drain rapidly while retaining minimal moisture.",
        "analysis": [
            "Incorrect; clayey soil has the smallest particle size and highest water retention.",
            "Sandy soil has large particles and large aeration spaces, resulting in rapid drainage and poor water retention.",
            "Incorrect; loamy soil has a balanced blend of sand, silt, and clay.",
            "Incorrect; humus enhances soil water-holding capacity."
        ]
    }
]

# --- 8 OTF QUESTIONS ---
otf_t3 = [
    {
        "code": "MH-9-SCIT-19-19.3-OTF-001",
        "text": "The curdling of milk to form curd is an irreversible chemical change brought about by lactic acid bacteria.",
        "truth": True,
        "concept": "Bacterial fermentation permanently changes milk proteins (casein coagulation) into curd, a reaction that cannot be reversed by physical means.",
        "analysis": "This statement is **True**. The formation of curd alters chemical composition irreversibly via biochemical reactions."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-002",
        "text": "A neutralisation reaction between an acid and a base is always an endothermic reaction that absorbs heat.",
        "truth": False,
        "concept": "Neutralisation of hydrogen and hydroxide ions (\\(\\ce{H+ + OH- -> H2O}\\)) is universally an exothermic process that releases heat.",
        "analysis": "This statement is **False**. Neutralisation reactions release thermal energy and are strictly exothermic."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-003",
        "text": "Carbon dioxide gas turns clear lime water milky due to the precipitation of insoluble calcium carbonate.",
        "truth": True,
        "concept": "\\(\\ce{Ca(OH)2 + CO2 -> CaCO3 v + H2O}\\); white calcium carbonate precipitate gives lime water its milky appearance.",
        "analysis": "This statement is **True**. Formation of insoluble white \\(\\ce{CaCO3}\\) is the standard diagnostic test for carbon dioxide."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-004",
        "text": "Both oxygen and moisture are strictly required for the rusting of iron.",
        "truth": True,
        "concept": "Iron corrosion requires both dissolved atmospheric oxygen and water to carry out the electrochemical oxidation of iron to hydrated ferric oxide.",
        "analysis": "This statement is **True**. Without either oxygen or moisture, iron will not rust."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-005",
        "text": "Acids turn red litmus paper blue, while bases turn blue litmus paper red.",
        "truth": False,
        "concept": "Acids turn blue litmus red, whereas bases turn red litmus blue.",
        "analysis": "This statement is **False**. The colors are reversed: acids turn blue litmus red, and bases turn red litmus blue."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-006",
        "text": "Humus is the dark, decomposed organic matter in topsoil that provides essential nutrients to crops.",
        "truth": True,
        "concept": "Humus improves soil aeration, water retention, and microbial ecology while slowly releasing nitrogen, phosphorus, and potassium.",
        "analysis": "This statement is **True**. Humus is critical for soil fertility and healthy plant development."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-007",
        "text": "Fossil fuels such as petroleum and coal are renewable natural resources that replenish within a few days.",
        "truth": False,
        "concept": "Fossil fuels take millions of years of geological heat and pressure to form, classifying them as exhaustible, non-renewable resources.",
        "analysis": "This statement is **False**. Fossil fuels are finite, non-renewable energy resources that deplete with extraction."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OTF-008",
        "text": "Galvanizing iron with a protective coating of zinc prevents it from rusting.",
        "truth": True,
        "concept": "Zinc serves as both a barrier layer and a sacrificial anode, shielding underlying iron from atmospheric oxygen and moisture.",
        "analysis": "This statement is **True**. Galvanization is a premier industrial method for rust prevention."
    }
]

# --- 6 OAR QUESTIONS ---
oar_t3 = [
    {
        "code": "MH-9-SCIT-19-19.3-OAR-001",
        "text": "Assertion (A): Iron gates and railings in coastal areas rust much faster than in inland desert regions.\nReason (R): Coastal air contains higher atmospheric humidity and saline moisture, which accelerates electrochemical oxidation.",
        "ca": "A",
        "concept": "Electrochemical rusting requires electrolytes; maritime air carrying water vapor and sodium chloride accelerates ionic conduction and corrosion.",
        "a_exp": "True — Coastal structures experience aggressive, accelerated rusting compared to dry inland areas.",
        "r_exp": "True — High humidity and airborne sea salt act as strong electrolytic accelerators for iron oxidation."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OAR-002",
        "text": "Assertion (A): An ant bite can be treated by gently rubbing moist baking soda or calamine lotion on the affected skin.\nReason (R): Baking soda (sodium hydrogen carbonate) and calamine (zinc carbonate) are basic compounds that neutralize the acidic formic acid injected by the ant.",
        "ca": "A",
        "concept": "Formic acid is neutralized by mild alkaline compounds, converting it into harmless salt and water, providing rapid pain relief.",
        "a_exp": "True — Applying mild bases provides immediate therapeutic relief from insect stings.",
        "r_exp": "True — The alkaline agents chemically neutralize the injected formic acid."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OAR-003",
        "text": "Assertion (A): Burning a candle involves both a physical change and a chemical change simultaneously.\nReason (R): The melting and vaporisation of candle wax is a physical change, while the combustion of wax vapor into carbon dioxide and water is a chemical change.",
        "ca": "A",
        "concept": "Phase changes of wax (solid -> liquid -> gas) are physical, while the exothermic combustion reaction \\(\\ce{C_nH_{2n+2} + O2 -> CO2 + H2O}\\) is chemical.",
        "a_exp": "True — Candle burning represents a simultaneous co-occurrence of physical and chemical transformations.",
        "r_exp": "True — Phase transitions are physical changes, while oxidation of hydrocarbons is a chemical reaction."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OAR-004",
        "text": "Assertion (A): Soil erosion is significantly more severe on barren hill slopes than on forest-covered slopes.\nReason (R): Dense tree roots bind soil particles firmly together and foliage shields topsoil from the direct impact of torrential rainfall.",
        "ca": "A",
        "concept": "Vegetation acts as a natural mechanical barrier against soil erosion through root anchorage and leaf canopy interception.",
        "a_exp": "True — Barren, deforested terrains suffer catastrophic loss of fertile topsoil during rains.",
        "r_exp": "True — Plant roots anchor soil particles and reduce the velocity of water runoff."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OAR-005",
        "text": "Assertion (A): When vinegar is mixed with baking soda, bubbling gas is produced that turns lime water milky.\nReason (R): Acetic acid in vinegar reacts with sodium hydrogen carbonate to release carbon dioxide gas.",
        "ca": "A",
        "concept": "\\(\\ce{CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2 ^}\\); evolved \\(\\ce{CO2}\\) precipitates \\(\\ce{CaCO3}\\) in lime water.",
        "a_exp": "True — The reaction produces vigorous effervescence of \\(\\ce{CO2}\\), turning lime water milky.",
        "r_exp": "True — Carbon dioxide is chemically generated by the reaction between acetic acid and bicarbonate."
    },
    {
        "code": "MH-9-SCIT-19-19.3-OAR-006",
        "text": "Assertion (A): Rainwater harvesting is an essential conservation strategy for maintaining water security in drought-prone areas.\nReason (R): Rainwater is inherently non-renewable and cannot be replenished through the natural water cycle.",
        "ca": "C",
        "concept": "Rainwater is renewable through the global hydrologic cycle, but harvesting is critical because precipitation is temporally seasonal and localized.",
        "a_exp": "True — Rainwater harvesting buffers communities against seasonal water scarcity and recharges aquifers.",
        "r_exp": "False — Water is a renewable natural resource continually recycled through global evaporation and precipitation."
    }
]

# --- 6 OMC QUESTIONS ---
omc_t3 = [
    {
        "code": "MH-9-SCIT-19-19.3-OMC-001",
        "text": "Which of the following phenomena represent irreversible chemical changes? (Select all that apply)",
        "options": [
            "Rusting of an iron bicycle frame",
            "Cooking of raw vegetables and rice",
            "Dissolving common salt in water",
            "Burning of dry wood into ash and smoke"
        ],
        "cas": [
            "Rusting of an iron bicycle frame",
            "Cooking of raw vegetables and rice",
            "Burning of dry wood into ash and smoke"
        ],
        "concept": "Chemical changes alter molecular composition, creating new chemical species that cannot be reversed by simple physical methods.",
        "analysis": {
            "Rusting of an iron bicycle frame": "Correct; oxidation forms hydrated iron oxide irreversibly.",
            "Cooking of raw vegetables and rice": "Correct; thermal denaturation of proteins and starch gelatinization are irreversible.",
            "Dissolving common salt in water": "Incorrect; physical dissolution; evaporating water completely recovers the solid salt.",
            "Burning of dry wood into ash and smoke": "Correct; combustion chemically converts cellulose into carbon dioxide, water, and ash."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.3-OMC-002",
        "text": "Which of the following substances are naturally occurring acids found in everyday foods? (Select all that apply)",
        "options": [
            "Citric acid in lemons and oranges",
            "Lactic acid in sour milk and curd",
            "Tartaric acid in tamarind and unripened grapes",
            "Sodium hydroxide in laundry detergent"
        ],
        "cas": [
            "Citric acid in lemons and oranges",
            "Lactic acid in sour milk and curd",
            "Tartaric acid in tamarind and unripened grapes"
        ],
        "concept": "Organic acids occur naturally in fruits and fermented dairy products, giving them characteristic sour tastes.",
        "analysis": {
            "Citric acid in lemons and oranges": "Correct; abundant in all citrus fruits.",
            "Lactic acid in sour milk and curd": "Correct; produced by lactic bacterial fermentation.",
            "Tartaric acid in tamarind and unripened grapes": "Correct; imparts tartness to tamarind and grapes.",
            "Sodium hydroxide in laundry detergent": "Incorrect; sodium hydroxide is a synthetic strong base, not an edible natural acid."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.3-OMC-003",
        "text": "Which of the following are effective methods for preventing the rusting of iron structures? (Select all that apply)",
        "options": [
            "Applying a coat of oil-based paint or grease",
            "Galvanizing iron with a thin surface coating of zinc",
            "Allowing iron articles to remain continuously submerged in salty water",
            "Electroplating iron with corrosion-resistant chromium or nickel"
        ],
        "cas": [
            "Applying a coat of oil-based paint or grease",
            "Galvanizing iron with a thin surface coating of zinc",
            "Electroplating iron with corrosion-resistant chromium or nickel"
        ],
        "concept": "Rust prevention relies on isolating iron from atmospheric moisture and oxygen or providing sacrificial cathodic protection.",
        "analysis": {
            "Applying a coat of oil-based paint or grease": "Correct; creates an impermeable physical barrier against air and moisture.",
            "Galvanizing iron with a thin surface coating of zinc": "Correct; provides durable barrier and sacrificial protection.",
            "Allowing iron articles to remain continuously submerged in salty water": "Incorrect; saltwater strongly accelerates electrochemical corrosion.",
            "Electroplating iron with corrosion-resistant chromium or nickel": "Correct; chromium electroplating forms a shining, corrosion-proof layer."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.3-OMC-004",
        "text": "Which of the following statements correctly describe natural soil layers and soil conservation? (Select all that apply)",
        "options": [
            "Topsoil is the uppermost fertile layer containing abundant humus and micro-organisms.",
            "Plant roots bind soil particles, significantly reducing erosion caused by wind and running water.",
            "Soil formation occurs within a few minutes during a heavy rainstorm.",
            "Overgrazing and indiscriminate deforestation accelerate severe topsoil erosion."
        ],
        "cas": [
            "Topsoil is the uppermost fertile layer containing abundant humus and micro-organisms.",
            "Plant roots bind soil particles, significantly reducing erosion caused by wind and running water.",
            "Overgrazing and indiscriminate deforestation accelerate severe topsoil erosion."
        ],
        "concept": "Soil is a precious natural resource formed over centuries through rock weathering and organic enrichment.",
        "analysis": {
            "Topsoil is the uppermost fertile layer containing abundant humus and micro-organisms.": "Correct; vital for agriculture and nutrient cycling.",
            "Plant roots bind soil particles, significantly reducing erosion caused by wind and running water.": "Correct; vegetation is nature's primary defense against erosion.",
            "Soil formation occurs within a few minutes during a heavy rainstorm.": "Incorrect; forming a centimeter of fertile soil takes hundreds of years of weathering.",
            "Overgrazing and indiscriminate deforestation accelerate severe topsoil erosion.": "Correct; removing vegetative cover exposes topsoil to erosive forces."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.3-OMC-005",
        "text": "Which of the following are examples of renewable, inexhaustible natural energy resources? (Select all that apply)",
        "options": [
            "Solar radiation from the Sun",
            "Wind energy driving wind turbines",
            "Fossil coal extracted from underground mines",
            "Biomass and flowing hydroelectric energy"
        ],
        "cas": [
            "Solar radiation from the Sun",
            "Wind energy driving wind turbines",
            "Biomass and flowing hydroelectric energy"
        ],
        "concept": "Renewable energy resources replenish naturally on human timescales without depleting planetary reserves.",
        "analysis": {
            "Solar radiation from the Sun": "Correct; inexhaustible clean solar flux.",
            "Wind energy driving wind turbines": "Correct; continuously replenished by atmospheric thermal circulation.",
            "Fossil coal extracted from underground mines": "Incorrect; coal is a finite, exhaustible fossil fuel.",
            "Biomass and flowing hydroelectric energy": "Correct; sustained by the hydrological and biological carbon cycles."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.3-OMC-006",
        "text": "Which of the following are characteristic properties of acidic solutions in chemistry? (Select all that apply)",
        "options": [
            "They turn blue litmus paper red.",
            "They taste sour to human taste receptors.",
            "They react with metal carbonates to release carbon dioxide gas with effervescence.",
            "They feel slippery and soapy to the touch."
        ],
        "cas": [
            "They turn blue litmus paper red.",
            "They taste sour to human taste receptors.",
            "They react with metal carbonates to release carbon dioxide gas with effervescence."
        ],
        "concept": "Acids are chemical substances containing ionizable hydrogen that turn blue litmus red, taste sour, and react with carbonates to yield \\(\\ce{CO2}\\).",
        "analysis": {
            "They turn blue litmus paper red.": "Correct; standard indicator response for acids.",
            "They taste sour to human taste receptors.": "Correct; acid taste (e.g. vinegar, lemon juice) is characteristically sour.",
            "They react with metal carbonates to release carbon dioxide gas with effervescence.": "Correct; yields salt, water, and effervescent \\(\\ce{CO2}\\).",
            "They feel slippery and soapy to the touch.": "Incorrect; feeling soapy or slippery is a defining characteristic of bases, not acids."
        }
    }
]

# Assemble all 40 questions
# OSC
for item in osc_t3:
    lines = []
    corr_idx = ord(item['ca']) - 65
    for i, opt in enumerate(item['options']):
        let = chr(65 + i)
        is_c = (i == corr_idx)
        c_tag = " (Correct)" if is_c else ""
        lines.append(f"- **({let}) {opt}{c_tag}** — {item['analysis'][i]}")
    
    sol = f"""**Key Concept:**
{item['concept']}

**Option Analysis:**
{chr(10).join(lines)}"""
    
    qs_t3.append({
        "questionCode": item['code'],
        "type": "OSC",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.3",
        "text": item['text'],
        "options": item['options'],
        "correctAnswer": item['ca'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OTF
for item in otf_t3:
    truth_str = "True" if item['truth'] else "False"
    c_let = "A" if item['truth'] else "B"
    sol = f"""**Key Concept:**
{item['concept']}

**Statement Evaluation:**
- **Statement:** "{item['text']}"
- **Analysis:** {item['analysis']}
- **Conclusion ({c_let}) (Correct)** — The statement is verified as **{truth_str}**."""
    
    qs_t3.append({
        "questionCode": item['code'],
        "type": "OTF",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.3",
        "text": item['text'],
        "options": ["True", "False"],
        "correctAnswer": truth_str,
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OAR
for item in oar_t3:
    sol = f"""**Key Concept:**
{item['concept']}

**Assertion & Reason Analysis:**
- **Assertion (A):** {item['a_exp']}
- **Reason (R):** {item['r_exp']}
- **Conclusion ({item['ca']}) (Correct)** — Evaluated according to chemical and natural resource principles."""
    
    qs_t3.append({
        "questionCode": item['code'],
        "type": "OAR",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.3",
        "text": item['text'],
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": item['ca'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OMC
for item in omc_t3:
    lines = []
    for i, opt in enumerate(item['options']):
        let = chr(65 + i)
        is_c = (opt in item['cas'])
        c_tag = " (Correct)" if is_c else ""
        lines.append(f"- **({let}) {opt}{c_tag}** — {item['analysis'][opt]}")
        
    sol = f"""**Key Concept:**
{item['concept']}

**Option Analysis:**
{chr(10).join(lines)}"""
    
    qs_t3.append({
        "questionCode": item['code'],
        "type": "OMC",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.3",
        "text": item['text'],
        "options": item['options'],
        "correctAnswers": item['cas'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

print(f"Generated {len(qs_t3)} brand-new gold-standard questions for Topic 19.3.")

with open('backups/staging/mh9_scit_19_topic3_new.json', 'w', encoding='utf-8') as f:
    json.dump(qs_t3, f, indent=2, ensure_ascii=False)

print("Saved backups/staging/mh9_scit_19_topic3_new.json")
