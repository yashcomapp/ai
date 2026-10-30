# scripts/generate_ch13_topic5.py
# MH-9-SCIT-13-13.5: Carbon Dioxide (CO2) & Methane (CH4) Properties & Fire Extinguishers
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-13-13.5"

# 40 Exam Questions
exam_data = [
    # 1-10: Laboratory Preparation & Physical Properties of CO2
    ("Which chemical reactants are standardly used in the laboratory to prepare carbon dioxide (CO2) gas?""",
     ["Calcium carbonate (marble chips, CaCO3) and dilute hydrochloric acid (HCl)",
      "Sodium metal and cold water",
      "Copper turnings and concentrated nitric acid",
      "Zinc granules and dilute sulfuric acid"],
     "A", "OSC", "easy",
     "In the laboratory, marble chips react with dilute hydrochloric acid: CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (gas), releasing effervescence of carbon dioxide."),

    ("Why is dilute sulfuric acid NOT used in place of dilute hydrochloric acid to prepare CO2 from marble chips?""",
     ["It forms an insoluble coating of calcium sulfate (CaSO4) on the marble chips that stops the reaction prematurely",
      "Sulfuric acid does not react with carbonates",
      "It produces poisonous chlorine gas",
      "It causes the glass apparatus to explode"],
     "A", "OSC", "medium",
     "CaSO4 is sparingly soluble; it precipitates as an impervious crust over the marble chips, halting contact with acid and ending gas generation."),

    ("By which physical method is carbon dioxide gas collected in the laboratory?""",
     ["By the upward displacement of air, because CO2 is approximately 1.5 times denser than air",
      "By the downward displacement of air",
      "Over cold water",
      "Over liquid mercury only"],
     "A", "OSC", "easy",
     "Having a molecular mass of 44 g/mol (compared to air's average ~29 g/mol), dense CO2 sinks to the bottom of the gas jar, displacing lighter air upwards. It is not collected over water because it is moderately water-soluble."),

    ("What is the chemical reaction when carbon dioxide dissolves in water under pressure?""",
     ["It forms weak carbonic acid: CO2 (g) + H2O (l) <=> H2CO3 (aq)",
      "It forms strong sulfuric acid",
      "It forms solid calcium hydroxide",
      "It forms hydrogen gas and ozone"],
     "A", "OSC", "easy",
     "Dissolving CO2 in water establishes an equilibrium with carbonic acid (H2CO3), giving aerated soft drinks their characteristic tangy acidic bite."),

    ("Why does clear lime water turn milky when carbon dioxide gas is passed through it?""",
     ["Insoluble white calcium carbonate (CaCO3) precipitate forms as a suspension: Ca(OH)2 + CO2 -> CaCO3 (s) + H2O",
      "Calcium hydroxide freezes into ice crystals",
      "Carbon dioxide bleaches the solution white",
      "Lime water reacts to produce milk proteins"],
     "A", "OSC", "easy",
     "The reaction precipitates insoluble CaCO3, creating a white suspension that turns the clear lime water visibly milky."),

    ("What happens when carbon dioxide is bubbled through milky lime water in excess for a prolonged period?""",
     ["The solution turns clear and colorless again because insoluble CaCO3 converts into soluble calcium hydrogen carbonate: CaCO3 + H2O + CO2 -> Ca(HCO3)2",
      "The milkiness turns bright red",
      "The test tube shatters from boiling",
      "The liquid solidifies into stone"],
     "A", "OSC", "medium",
     "Excess CO2 converts insoluble CaCO3 into water-soluble calcium bicarbonate, causing the milky suspension to dissolve and clear up completely."),

    ("What is 'dry ice' in chemistry and industry?""",
     ["Solid carbon dioxide (CO2) at or below -78.5 deg C",
      "Frozen water without any salt",
      "Solid nitrogen cubes",
      "Ice coated with paraffin wax"],
     "A", "OSC", "easy",
     "Dry ice is carbon dioxide compressed and chilled into a solid at -78.5 deg C; it sublimates directly into gas without leaving liquid moisture, hence named 'dry' ice."),

    ("Why does dry ice 'sublime' directly into gas at room temperature and standard atmospheric pressure?""",
     ["Carbon dioxide's triple point pressure is 5.1 atmospheres, well above normal atmospheric pressure (1 atm), so it transitions directly from solid to vapor without melting",
      "Dry ice has zero mass",
      "Dry ice contains boiling water",
      "Carbon dioxide cannot exist as a gas"],
     "A", "OSC", "hard",
     "At 1 atm, liquid CO2 cannot exist thermodynamically because 1 atm is below the triple point (5.11 atm). Heating solid CO2 at 1 atm causes sublimation directly to gas at -78.5 deg C."),

    ("What are the major industrial uses of solid dry ice?""",
     ["Refrigerating perishable foods and vaccines during transport, creating theatrical fog effects, and freeze-branding cattle",
      "Fuel for gasoline motorcars",
      "Drinking water in desert areas",
      "Fertilizer for agricultural soil"],
     "A", "OSC", "easy",
     "Dry ice maintains -78.5 deg C without leaving wet melted puddles, making it the premier cryogenic refrigerant for biologicals and stage fog machines."),

    ("State whether the following statement is True or False: Carbon dioxide is a supporter of ordinary candle combustion.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Carbon dioxide is non-combustible and extinguishes ordinary flames by suffocating the supply of oxygen."),

    # 11-20: Fire Extinguishers Working Mechanisms
    ("Why is carbon dioxide widely utilized as an effective fire extinguishing agent?""",
     ["It is non-flammable, does not support combustion, and being denser than air, it blankets the burning material to displace oxygen and cools the fuel",
      "It absorbs fire like a sponge",
      "It turns flames into solid ice",
      "It generates liquid water instantly"],
     "A", "OSC", "easy",
     "CO2 smothers fires by cutting off the oxygen supply (breaking the fire triangle) and cooling burning surfaces through Joule-Thomson expansion chilling."),

    ("Which class of fires is a CO2 fire extinguisher specifically suited for?""",
     ["Electrical fires (Class C/E) and flammable liquid fires (Class B)",
      "Deep forest fires only",
      "Combustible metal fires (sodium/magnesium)",
      "Coal mine underground fires"],
     "A", "OSC", "easy",
     "CO2 is an electrical non-conductor and leaves zero corrosive residue, making it ideal for electrical switchboards, computers, and liquid petrol/solvent fires."),

    ("Why should a CO2 or water fire extinguisher NEVER be used on burning reactive metals like magnesium or sodium?""",
     ["Burning magnesium continues to burn vigorously in CO2 by stripping oxygen from it: 2Mg + CO2 -> 2MgO + C, releasing intense heat and sparks",
      "Metals absorb CO2 to become radioactive",
      "CO2 turns magnesium into poisonous gas",
      "CO2 causes sodium to freeze"],
     "A", "OSC", "medium",
     "Extremely electropositive burning metals reduce CO2 into carbon and metal oxides, fueling the fire rather than extinguishing it."),

    ("What two chemicals are housed in separate compartments inside a traditional soda-acid fire extinguisher?""",
     ["Sodium bicarbonate (baking soda, NaHCO3) solution and concentrated sulfuric acid (H2SO4)",
      "Sodium hydroxide and hydrochloric acid",
      "Calcium carbonate and nitric acid",
      "Ammonium nitrate and water"],
     "A", "OSC", "easy",
     "A soda-acid extinguisher contains aqueous sodium bicarbonate with a glass ampoule of concentrated sulfuric acid."),

    ("What chemical reaction occurs inside a soda-acid extinguisher when struck or inverted?""",
     ["2 NaHCO3 + H2SO4 -> Na2SO4 + 2 H2O + 2 CO2 (gas)",
      "NaCl + H2O -> NaOH + HCl",
      "CaCO3 + H2SO4 -> CaSO4 + CO2",
      "2 H2O -> 2 H2 + O2"],
     "A", "OSC", "easy",
     "Acid mixes with bicarbonate to generate rapid CO2 gas pressure, ejecting a foaming jet of water and CO2 onto the base of the fire."),

    ("What active dry chemical powder is filled inside modern multipurpose ABC dry powder fire extinguishers?""",
     ["Monoammonium phosphate (NH4H2PO4) or sodium bicarbonate",
      "Powdered sulfur",
      "Powdered charcoal",
      "Powdered sugar"],
     "A", "OSC", "medium",
     "Monoammonium phosphate melts at fire temperatures to coat burning embers with a glass-like barrier, while decomposing to release flame-retarding gases."),

    ("Why does the discharge horn of a CO2 fire extinguisher become extremely cold and frosted with white dry-ice snow during operation?""",
     ["Liquid CO2 expands suddenly from high cylinder pressure (~55 bar) to atmospheric pressure (1 bar), absorbing intense heat via Joule-Thomson cooling",
      "The horn is packed with real snow",
      "Liquid nitrogen is mixed into the tank",
      "Electricity is drained from the fire"],
     "A", "OSC", "medium",
     "Rapid adiabatic expansion of compressed liquid CO2 absorbs latent heat from the surroundings (Joule-Thomson effect), cooling the discharge to -78.5 deg C."),

    ("State whether the following statement is True or False: Using water on an energized electrical fire carries a high risk of fatal electrocution.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Tap water contains dissolved mineral electrolytes that conduct electricity readily, conducting high voltages directly to the firefighter."),

    ("State whether the following statement is True or False: Modern liquid CO2 fire extinguishers leave zero powdery or liquid residue after extinguishing a fire.",
     ["True", "False"],
     "A", "OTF", "easy",
     "CO2 dissipates completely into the surrounding atmosphere as a harmless gas, leaving electrical circuits, server rooms, and motors clean and undamaged."),

    ("State whether the following statement is True or False: Carbon dioxide is lighter than air.",
     ["False", "True"],
     "A", "OTF", "easy",
     "CO2 has a molecular weight of 44 g/mol compared to ~29 g/mol for air; it is approximately 1.5 times denser than air."),

    # 21-30: Methane Properties, Biogas & Environmental Impact
    ("What is the common name and chemical formula of the simplest saturated alkane hydrocarbon?""",
     ["Methane (CH4), commonly known as marsh gas",
      "Ethane (C2H6)",
      "Propane (C3H8)",
      "Acetylene (C2H2)"],
     "A", "OSC", "easy",
     "Methane (CH4) is the simplest alkane, colloquially called marsh gas because anaerobic decomposition releases it from swamp mud."),

    ("Why is methane gas colloquially called 'marsh gas'?""",
     ["It is produced naturally in muddy marshes, bogs, and paddy fields by the anaerobic microbial decomposition of plant vegetation",
      "It smells like river mud",
      "It only burns inside water",
      "It was discovered by a chemist named Marsh"],
     "A", "OSC", "easy",
     "Methanogenic archaebacteria ferment submerged cellulose under oxygen-free swamp sediments, releasing bubbles of gaseous methane."),

    ("What are the major constituent gases present in raw 'biogas' (gobar gas) produced in rural biodigesters?""",
     ["Methane (55% to 65%) and carbon dioxide (30% to 40%) with traces of hydrogen, nitrogen, and hydrogen sulfide",
      "100% pure oxygen gas",
      "Carbon monoxide (80%) and chlorine (20%)",
      "Nitrogen dioxide and sulfur dioxide"],
     "A", "OSC", "medium",
     "Biogas generated from cattle dung (gobar) and agricultural biomass contains 55-65% combustible methane and 30-40% incombustible carbon dioxide."),

    ("What are the two valuable products obtained from an agricultural biogas (gobar gas) plant?""",
     ["Clean combustible methane fuel gas for cooking/lighting and nutrient-rich organic manure (spent slurry) for crops",
      "Liquid petrol and plastic beads",
      "Pure gold and drinking water",
      "Solid coal and sulfuric acid"],
     "A", "OSC", "easy",
     "Biogas plants provide clean, smokeless domestic cooking gas while yielding pathogen-free digested slurry rich in nitrogen and phosphorus fertilizer."),

    ("What type of microorganisms are responsible for producing methane inside an anaerobic biogas digester?""",
     ["Anaerobic methanogenic bacteria (methanogens)",
      "Aerobic yeast molds",
      "Photosynthetic green algae",
      "Nitrogen-fixing Rhizobium bacteria"],
     "A", "OSC", "medium",
     "Obligate anaerobic methanogens (such as Methanobacterium) thrive in oxygen-free digester tanks, converting organic acids into methane and CO2."),

    ("What is the density of methane gas compared to atmospheric air?""",
     ["Methane is significantly lighter than air (molecular mass 16 g/mol vs air ~29 g/mol)",
      "Methane is twice as heavy as air",
      "Methane has the exact same density as air",
      "Methane is heavier than carbon dioxide"],
     "A", "OSC", "easy",
     "With a molar mass of only 16 g/mol, methane is much lighter than air and rises rapidly towards the ceiling in enclosed spaces."),

    ("What chemical reaction occurs during the complete combustion of methane in excess oxygen?""",
     ["CH4 (g) + 2 O2 (g) -> CO2 (g) + 2 H2O (g) + 890 kJ/mol of heat",
      "CH4 + O2 -> C + 2 H2O",
      "2 CH4 + O2 -> 2 CH3OH",
      "CH4 -> C + 2 H2"],
     "A", "OSC", "easy",
     "Complete oxidation yields carbon dioxide and water vapor, releasing 890 kJ of clean thermal energy per mole without smoke."),

    ("Why is methane classified as a potent 'greenhouse gas' in atmospheric environmental science?""",
     ["It traps infrared thermal radiation in Earth's atmosphere with over 25 times greater warming potency per molecule than CO2 over a 100-year timescale",
      "It destroys the ozone layer directly with chlorine",
      "It prevents sunlight from reaching Earth",
      "It turns rain into sulfuric acid"],
     "A", "OSC", "medium",
     "Methane molecules absorb infrared radiation very effectively, possessing a Global Warming Potential (GWP) roughly 28 times higher than CO2 over a century."),

    ("State whether the following statement is True or False: Methane gas is highly soluble in liquid water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Methane is a non-polar covalent molecule and is practically insoluble in polar water (only ~22 mg/L at 20 deg C)."),

    ("State whether the following statement is True or False: Pure methane gas is colorless and completely odorless.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Pure methane is colorless, tasteless, and odorless; the pungent smell of commercial natural gas is due to added thiol odorants."),

    # 31-40: Synthesis, Quantitative Calculations & Safety
    ("What mass of carbon dioxide is produced by the complete combustion of 16 grams (one mole) of pure methane? (C = 12, H = 1, O = 16)",
     ["44 grams", "16 grams", "32 grams", "88 grams"],
     "A", "OSC", "easy",
     "CH4 + 2O2 -> CO2 + 2H2O. One mole of methane (16 g) reacts to yield exactly one mole of CO2 (12 + 32 = 44 g)."),

    ("What mass of water vapor is formed when 16 grams of methane are completely burned in oxygen?""",
     ["36 grams (two moles of H2O)", "18 grams", "72 grams", "9 grams"],
     "A", "OSC", "medium",
     "The balanced equation CH4 + 2O2 -> CO2 + 2H2O shows 1 mole of methane produces 2 moles of H2O: 2 * 18 g = 36 g of water vapor."),

    ("Why does a carbon dioxide fire extinguisher have a large, wide bell-shaped discharge horn made of plastic or rubber?""",
     ["To prevent frostbite injury to the operator's hands from extreme Joule-Thomson cooling and to disperse CO2 into a gentle, broad smothering blanket",
      "To amplify the sound of the gas",
      "To collect oxygen from the room",
      "To heat the gas before it reaches the fire"],
     "A", "OSC", "medium",
     "Expanding CO2 cools the horn down to -78.5 deg C; the insulated non-conductive horn protects against severe cryogenic skin burns and diffuses the gas velocity."),

    ("What hazardous physiological condition occurs if a person remains inside an unventilated room with elevated CO2 concentrations exceeding 5%?""",
     ["Hypercapnia (carbon dioxide toxicity), causing shortness of breath, dizziness, confusion, unconsciousness, and respiratory failure",
      "Severe frostbite",
      "Instantaneous internal combustion",
      "Excessive oxygen euphoria"],
     "A", "OSC", "medium",
     "High CO2 displaces oxygen and acidifies blood pH (respiratory acidosis), impairing cerebral oxygenation and inducing loss of consciousness."),

    ("What gas is formed at the anode during the electrolysis of aqueous sodium acetate (Kolbe's electrolysis)?""",
     ["Ethane (C2H6) and carbon dioxide (CO2)",
      "Methane and oxygen",
      "Pure chlorine gas only",
      "Hydrogen gas only"],
     "A", "OSC", "hard",
     "2 CH3COO- -> C2H6 + 2 CO2 + 2e-. Decarboxylation at the anode couples methyl radicals into ethane while releasing carbon dioxide."),

    ("Why are coal miners equipped with methane detectors (formerly safety Davy lamps) in underground coal mines?""",
     ["Methane mixtures with air between 5% and 15% (firedamp) are violently explosive and can be ignited by any small electrical or friction spark",
      "Methane makes coal mines too cold to work in",
      "Methane dissolves coal into water",
      "Methane makes miner uniforms radioactive"],
     "A", "OSC", "easy",
     "Methane trapped in coal seams forms 'firedamp'; between its explosive limits (5-15% in air), any open flame or spark causes catastrophic subterranean explosions."),

    ("Which property of carbon dioxide allows it to be used in supercritical fluid extraction to decaffeinate green coffee beans?""",
     ["Supercritical CO2 (above 31.1 deg C and 73 atm) behaves like a dense gas with liquid-like dissolving power, extracting caffeine without leaving toxic solvent residues",
      "CO2 burns the caffeine away",
      "CO2 turns caffeine into sugar",
      "CO2 freezes the coffee beans solid"],
     "A", "OSC", "hard",
     "Supercritical CO2 acts as an eco-friendly green solvent, dissolving non-polar caffeine selectively and leaving pure coffee when depressurized back to gas."),

    ("State whether the following statement is True or False: Solid dry ice should never be stored in a tightly sealed glass or metallic container.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Dry ice continually sublimates into gas, expanding roughly 800-fold in volume; sealing it creates immense hydrostatic pressure that will violently shatter the container."),

    ("State whether the following statement is True or False: The combustion of methane produces more soot and smoke than the combustion of wood or coal.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Methane is the cleanest burning fossil hydrocarbon, producing purely CO2 and H2O without soot or ash particles."),

    ("Which of the following compounds is the principal organic acid found in effervescent soda water containing dissolved CO2?""",
     ["Carbonic acid (H2CO3)", "Acetic acid", "Formic acid", "Hydrochloric acid"],
     "A", "OSC", "easy",
     "Carbon dioxide dissolved in water forms weak, effervescent carbonic acid: CO2 + H2O <=> H2CO3.")
]

# 30 Practice Questions
practice_data = [
    ("What gas is collected in the gas jar when marble chips react with dilute hydrochloric acid?""",
     ["Carbon dioxide (CO2)", "Hydrogen (H2)", "Oxygen (O2)", "Chlorine (Cl2)"],
     "A", "OSC", "easy",
     "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (gas)."),

    ("What is the molecular mass of a carbon dioxide (CO2) molecule? (C = 12, O = 16)",
     ["44 atomic mass units (u)", "28 u", "32 u", "16 u"],
     "A", "OSC", "easy",
     "Molecular mass = 12 + 2(16) = 12 + 32 = 44 u."),

    ("What is the molecular mass of a methane (CH4) molecule? (C = 12, H = 1)",
     ["16 atomic mass units (u)", "12 u", "20 u", "28 u"],
     "A", "OSC", "easy",
     "Molecular mass = 12 + 4(1) = 16 u."),

    ("What is the temperature of solid dry ice at standard atmospheric pressure?""",
     ["-78.5 deg C", "0 deg C", "-100 deg C", "-273 deg C"],
     "A", "OSC", "easy",
     "Dry ice sublimates at -78.5 deg C under 1 atmosphere pressure."),

    ("State whether the following statement is True or False: Carbon dioxide turns moist blue litmus paper red.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Dissolving in moisture, CO2 forms acidic carbonic acid (H2CO3), turning blue litmus red."),

    ("State whether the following statement is True or False: Methane is denser than air.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Methane has a molar mass of 16 g/mol, which is much lighter than air (~29 g/mol)."),

    ("State whether the following statement is True or False: Biogas burns with a smoky yellow flame like kerosene.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Biogas contains clean-burning methane that burns with a clean, smokeless blue flame."),

    ("What chemical formula represents the white precipitate formed when CO2 bubbles through lime water?""",
     ["CaCO3 (calcium carbonate)", "Ca(HCO3)2", "CaO", "CaCl2"],
     "A", "OSC", "easy",
     "Insoluble calcium carbonate (CaCO3) forms the milky precipitate."),

    ("What chemical formula represents the soluble compound formed when excess CO2 dissolves the milky precipitate?""",
     ["Ca(HCO3)2 (calcium hydrogen carbonate)", "CaCO3", "CaO", "Ca(OH)2"],
     "A", "OSC", "easy",
     "Excess CO2 converts CaCO3 into soluble calcium hydrogen carbonate [Ca(HCO3)2]."),

    ("Why does blowing through a straw into a beaker of clear lime water turn it milky after a few seconds?""",
     ["Human exhaled breath contains approximately 4% to 5% carbon dioxide from cellular respiration",
      "Saliva turns lime water white",
      "Air from the room enters the straw",
      "Lime water reacts with human body heat"],
     "A", "OSC", "easy",
     "Exhaled air carries respiratory CO2 waste (~4%), which precipitates CaCO3 in the lime water."),

    # 11-20
    ("What component in a fire extinguisher displaces oxygen from the surface of burning materials?""",
     ["Carbon dioxide gas", "Nitrogen dioxide", "Sulfur dioxide", "Carbon monoxide"],
     "A", "OSC", "easy",
     "Dense CO2 blankets the burning surface, isolating fuel from atmospheric oxygen."),

    ("What type of gas pressure propels the water spray out of a soda-acid fire extinguisher?""",
     ["High pressure of carbon dioxide gas generated rapidly inside the sealed cylinder",
      "An electric water pump",
      "Compressed helium",
      "A hand lever spring"],
     "A", "OSC", "easy",
     "The rapid acid-carbonate reaction produces CO2 gas, building internal pressure that propels the liquid stream."),

    ("Why can carbon dioxide be liquefied easily at room temperature under pressure (~55-60 atmospheres)?""",
     ["Its critical temperature is 31.1 deg C, which is above normal room temperature (20-25 deg C)",
      "It has zero molecular mass",
      "It reacts with steel tanks",
      "It dissolves into liquid metal"],
     "A", "OSC", "medium",
     "Because its critical temperature is 31.1 deg C, compressing CO2 at ordinary ambient temperatures condenses it into liquid."),

    ("What is the major source of atmospheric methane emissions from agriculture?""",
     ["Enteric fermentation in ruminant livestock (cows/sheep) and submerged anaerobic flooded rice paddy fields",
      "Tractor exhaust fumes",
      "Spraying chemical fertilizers",
      "Plowing dry wheat fields"],
     "A", "OSC", "easy",
     "Ruminant enteric digestion and microbial fermentation in waterlogged rice soils release millions of tons of biogenic methane annually."),

    ("What percentage of carbon dioxide is present in the bubbles that give effervescence to champagne and carbonated sodas?""",
     ["100% carbon dioxide gas", "50% oxygen and 50% nitrogen", "Pure hydrogen", "Pure helium"],
     "A", "OSC", "easy",
     "The fizzy bubbles in soft drinks, beer, and sparkling wines consist of dissolved CO2 escaping as pressure drops."),

    ("State whether the following statement is True or False: Dry ice can be handled safely with bare hands for long periods.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Dry ice is at -78.5 deg C; direct prolonged bare skin contact causes severe cryogenic frostbite and tissue destruction."),

    ("State whether the following statement is True or False: Methane is the second most important greenhouse gas contributing to human-induced climate change after carbon dioxide.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Methane ranks second only to CO2 in overall historical radiative forcing, accounting for ~20-30% of modern global warming."),

    ("State whether the following statement is True or False: A soda-acid fire extinguisher can be safely used on high-voltage electrical equipment.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Soda-acid extinguishers spray water containing dissolved conductive sodium sulfate salt, posing severe electrocution risk."),

    ("What is the volume of CO2 gas released at room temperature when 1 kg of solid dry ice sublimates completely?""",
     ["Approximately 550 to 800 litres of gas",
      "Approximately 1 litre",
      "Approximately 10 litres",
      "Zero litres"],
     "A", "OSC", "medium",
     "One kilogram of solid CO2 expands roughly 800-fold upon sublimating into atmospheric gas at room temperature."),

    ("Which compound is formed when methane reacts with oxygen in a limited or deficient air supply?""",
     ["Toxic carbon monoxide (CO) gas and black soot (carbon black)",
      "Pure carbon dioxide only",
      "Methanol only",
      "Hydrogen peroxide"],
     "A", "OSC", "easy",
     "Restricted oxygen causes incomplete combustion: 2CH4 + 3O2 -> 2CO + 4H2O, generating hazardous carbon monoxide."),

    # 21-30
    ("What is the chemical name and formula of 'slaked lime' used to prepare lime water?""",
     ["Calcium hydroxide, Ca(OH)2", "Calcium carbonate, CaCO3", "Calcium oxide, CaO", "Calcium sulfate, CaSO4"],
     "A", "OSC", "easy",
     "Slaked lime is calcium hydroxide [Ca(OH)2], formed by hydrating quicklime (CaO) with water."),

    ("What is the chemical name of 'quicklime'?""",
     ["Calcium oxide (CaO)", "Calcium hydroxide", "Calcium carbonate", "Calcium carbide"],
     "A", "OSC", "easy",
     "Quicklime is anhydrous calcium oxide (CaO)."),

    ("What is the chemical name of 'limestone'?""",
     ["Calcium carbonate (CaCO3)", "Calcium hydroxide", "Calcium oxide", "Calcium sulfate"],
     "A", "OSC", "easy",
     "Limestone is sedimentary rock composed primarily of mineral calcite (calcium carbonate, CaCO3)."),

    ("State whether the following statement is True or False: Burning methane produces toxic sulfur dioxide gas.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Pure methane contains only carbon and hydrogen, producing purely CO2 and H2O with zero sulfur dioxide emissions."),

    ("State whether the following statement is True or False: The gas produced inside a gobar gas plant can be used directly for cooking in domestic kitchen stoves.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Biogas has an adequate calorific value (~20-25 MJ/m^3) to burn cleanly in household burner nozzles."),

    ("Why is an underground digester pit ideal for a rural biogas plant?""",
     ["It maintains a warm, steady anaerobic temperature insulated from winter atmospheric cold, optimizing bacterial methanogenesis",
      "It prevents biogas from exploding into space",
      "It keeps the dung from touching air",
      "It allows earthworms to eat the gas"],
     "A", "OSC", "medium",
     "Underground subterranean tanks buffer temperature fluctuations, preserving the 30-38 deg C mesophilic range required by methanogens."),

    ("How is carbon dioxide removed from submarine and spacecraft atmospheres where crew members continuously exhale it?""",
     ["By passing exhaled cabin air through chemical scrubbers containing lithium hydroxide (LiOH) or soda lime",
      "By freezing all the air into liquid",
      "By releasing all the air into outer space",
      "By burning the air with torches"],
     "A", "OSC", "medium",
     "LiOH granules absorb metabolic CO2: 2LiOH + CO2 -> Li2CO3 + H2O, preventing toxic hypercapnia in enclosed life-support systems."),

    ("What gas is released during the fermentation of glucose sugar by brewer's yeast in bread-making and brewing?""",
     ["Carbon dioxide (CO2) and ethanol (ethyl alcohol)",
      "Methane gas only",
      "Oxygen gas only",
      "Sulfur dioxide gas"],
     "A", "OSC", "easy",
     "Yeast enzymatically converts glucose into ethanol and carbon dioxide: C6H12O6 -> 2 C2H5OH + 2 CO2 (gas)."),

    ("Why does bread dough rise and double in volume during proofing before baking?""",
     ["Fermenting yeast produces carbon dioxide gas bubbles trapped in the elastic gluten matrix of the wheat dough",
      "The flour turns into boiling water",
      "Air is sucked from the room into the dough",
      "Sugar crystals expand by 100 times"],
     "A", "OSC", "easy",
     "Bubbles of expanding CO2 gas inflate microscopic cavities within the kneaded gluten network, causing the dough to rise."),

    ("What property of carbon dioxide explains why it accumulates in deep unused wells, caves, and wine fermentation cellars?""",
     ["It is denser than atmospheric air and pools in low-lying depressions without naturally dispersing unless ventilated",
      "It is attracted to underground rocks magnetically",
      "It turns into liquid water in wells",
      "It cannot pass through doorway openings"],
     "A", "OSC", "easy",
     "Because CO2 is ~1.5 times heavier than air, it settles into subterranean pits and unventilated silos, posing invisible asphyxiation hazards.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Laboratory Preparation of CO2 Apparatus
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <rect x="50" y="70" width="80" height="80" fill="#334155" stroke="#94a3b8" stroke-width="1.5" rx="4"/>
  <line x1="70" y1="20" x2="70" y2="135" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="60,20 80,20 70,35" fill="#38bdf8"/>
  <text x="35" y="15" fill="#38bdf8" font-size="8">Thistle Funnel (Dil. HCl)</text>
  <circle cx="80" cy="138" r="5" fill="#f8fafc"/>
  <circle cx="95" cy="140" r="6" fill="#f8fafc"/>
  <circle cx="110" cy="138" r="5" fill="#f8fafc"/>
  <text x="75" y="125" fill="#fde68a" font-size="8">Marble Chips (CaCO3)</text>
  <path d="M 105 70 L 105 45 L 230 45 L 230 140" stroke="#facc15" stroke-width="2" fill="none"/>
  <rect x="210" y="60" width="40" height="95" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <text x="200" y="170" fill="#38bdf8" font-size="8" font-weight="bold">Gas Jar (Dense CO2)</text>
  <text x="35" y="185" fill="#4ade80" font-size="9">CaCO3 (s) + 2 HCl (aq) -> CaCl2 + H2O + CO2 (gas)</text>
  <text x="50" y="165" fill="#facc15" font-size="8">Collected by upward displacement of air (CO2 denser than air)</text>
</svg>
</div>
The laboratory apparatus shows the standard preparation and collection of carbon dioxide gas. Why is CO2 gas collected by the upward displacement of air rather than over water?""",
     ["Carbon dioxide is roughly 1.5 times denser than air and is moderately soluble in water, so it sinks in the gas jar displacing air upwards",
      "Carbon dioxide explodes on contact with water",
      "Carbon dioxide is lighter than air and escapes downwards",
      "Water dissolves the glass jar completely"],
     "A", "medium",
     "With a molar mass of 44 g/mol (vs ~29 g/mol for air), dense CO2 settles into the upright gas jar and displaces lighter air out of the mouth; it is not collected over water due to its moderate solubility."),

    # 72: Soda-Acid Fire Extinguisher Internal Schematic
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <rect x="90" y="30" width="100" height="135" fill="#dc2626" stroke="#f87171" stroke-width="2" rx="10"/>
  <rect x="95" y="85" width="90" height="75" fill="#38bdf8" opacity="0.4" rx="4"/>
  <text x="100" y="125" fill="#ffffff" font-size="8" font-weight="bold">Aqueous NaHCO3</text>
  <rect x="125" y="45" width="30" height="35" fill="#facc15" stroke="#ca8a04" stroke-width="1.5" rx="3"/>
  <text x="130" y="65" fill="#0f172a" font-size="7" font-weight="bold">Conc.</text>
  <text x="128" y="74" fill="#0f172a" font-size="7" font-weight="bold">H2SO4</text>
  <rect x="135" y="18" width="10" height="12" fill="#94a3b8"/>
  <circle cx="140" cy="14" r="5" fill="#ef4444"/>
  <path d="M 175 40 Q 210 40 240 60" stroke="#facc15" stroke-width="3" fill="none"/>
  <polygon points="240,56 250,60 242,65" fill="#facc15"/>
  <text x="210" y="80" fill="#fde68a" font-size="8" font-weight="bold">Foaming Jet</text>
  <text x="210" y="92" fill="#4ade80" font-size="8">(CO2 + Na2SO4 + H2O)</text>
  <text x="35" y="185" fill="#fde68a" font-size="9">2 NaHCO3 + H2SO4 -> Na2SO4 + 2 H2O + 2 CO2</text>
</svg>
</div>
The cutaway schematic illustrates a classic soda-acid fire extinguisher. What chemical reaction generates the pressurized discharge when the striker knob breaks the internal acid bottle?""",
     ["Concentrated sulfuric acid reacts with sodium bicarbonate solution to produce carbon dioxide gas: 2 NaHCO3 + H2SO4 -> Na2SO4 + 2 H2O + 2 CO2",
      "Hydrochloric acid reacts with sodium hydroxide to produce salt",
      "Water boils instantly into steam pressure",
      "Oxygen gas is released by electrical discharge"],
     "A", "easy",
     "Striking the plunger shatters the internal glass vial, allowing concentrated H2SO4 to mix with aqueous NaHCO3, generating high CO2 gas pressure that expels a foaming smothering stream."),

    # 73: Dry Ice Sublimation Phase Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="50" y1="150" x2="290" y2="150" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="50" y1="150" x2="50" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="250" y="165" fill="#94a3b8" font-size="8">Temperature</text>
  <text x="25" y="40" fill="#94a3b8" font-size="8">Pressure</text>
  <circle cx="130" cy="80" r="4" fill="#ef4444"/>
  <text x="135" y="78" fill="#fca5a5" font-size="8" font-weight="bold">Triple Point (5.11 atm)</text>
  <line x1="50" y1="120" x2="290" y2="120" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="55" y="115" fill="#facc15" font-size="8">1 atm (Normal Pressure)</text>
  <circle cx="95" cy="120" r="4" fill="#38bdf8"/>
  <text x="65" y="135" fill="#38bdf8" font-size="8" font-weight="bold">-78.5 deg C</text>
  <text x="70" y="60" fill="#cbd5e1" font-size="9">SOLID</text>
  <text x="180" y="60" fill="#cbd5e1" font-size="9">LIQUID</text>
  <text x="180" y="135" fill="#cbd5e1" font-size="9">GAS</text>
  <text x="45" y="180" fill="#4ade80" font-size="9">At 1 atm, CO2 transitions directly from SOLID to GAS (Sublimation)</text>
</svg>
</div>
The phase diagram of carbon dioxide (shown above) illustrates why solid CO2 is called 'dry ice'. Why can liquid carbon dioxide NOT exist at normal atmospheric pressure (1 atm)?""",
     ["The triple point of CO2 occurs at 5.11 atmospheres, so at 1 atmosphere heating solid CO2 bypasses the liquid state entirely, subliming directly to gas at -78.5 deg C",
      "Liquid CO2 is prohibited by gravitational laws",
      "Carbon dioxide atoms can only form solids or gases",
      "Atmospheric oxygen reacts with liquid CO2 to destroy it"],
     "A", "hard",
     "Liquid CO2 only exists at pressures greater than its triple point (5.11 atm). Below 5.11 atm (such as ambient 1 atm), solid CO2 sublimes directly into gas at -78.5 deg C without forming liquid."),

    # 74: Biogas (Gobar Gas) Underground Plant Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <line x1="20" y1="70" x2="320" y2="70" stroke="#78350f" stroke-width="3"/>
  <text x="25" y="65" fill="#d97706" font-size="8">Ground Level</text>
  <rect x="90" y="70" width="160" height="100" fill="#334155" stroke="#64748b" stroke-width="2" rx="4"/>
  <rect x="95" y="110" width="150" height="55" fill="#78350f" opacity="0.6"/>
  <text x="105" y="140" fill="#fde68a" font-size="8">Fermenting Cattle Dung Slurry</text>
  <path d="M 115 110 Q 170 60 225 110 Z" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="135" y="95" fill="#38bdf8" font-size="9" font-weight="bold">Biogas Dome</text>
  <line x1="170" y1="65" x2="170" y2="25" stroke="#facc15" stroke-width="3"/>
  <polygon points="167,25 173,25 170,18" fill="#facc15"/>
  <text x="180" y="30" fill="#facc15" font-size="8" font-weight="bold">Gas Valve -> Kitchen</text>
  <polygon points="40,50 85,75 85,130 50,110" fill="#475569"/>
  <text x="35" y="45" fill="#cbd5e1" font-size="8">Inlet (Dung+H2O)</text>
  <polygon points="295,50 255,75 255,130 285,110" fill="#475569"/>
  <text x="260" y="45" fill="#cbd5e1" font-size="8">Spent Slurry Manure</text>
  <text x="45" y="185" fill="#4ade80" font-size="9">Anaerobic methanogenesis produces ~60% CH4 fuel + organic fertilizer</text>
</svg>
</div>
The diagram shows a fixed-dome underground biogas (gobar gas) plant. Which biological conditions inside the subterranean digester allow methanogenic bacteria to produce methane fuel gas?""",
     ["Complete absence of oxygen (anaerobic environment), steady underground temperature, and neutral-to-mildly alkaline organic slurry",
      "Continuous exposure to direct sunlight and wind",
      "High concentrations of chlorine gas",
      "Freezing temperatures below 0 deg C"],
     "A", "medium",
     "Methanogens are obligate anaerobes that perish in oxygen; an airtight, temperature-buffered subterranean chamber allows them to ferment dung into methane and CO2."),

    # 75: Smothering the Fire Triangle with CO2
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="70" y1="140" x2="230" y2="140" stroke="#f59e0b" stroke-width="4"/>
  <text x="130" y="158" fill="#fde68a" font-size="10" font-weight="bold">FUEL</text>
  <line x1="70" y1="140" x2="150" y2="40" stroke="#ef4444" stroke-width="4"/>
  <text x="85" y="80" fill="#fca5a5" font-size="10" font-weight="bold">HEAT</text>
  <line x1="230" y1="140" x2="150" y2="40" stroke="#64748b" stroke-width="3" stroke-dasharray="4,4"/>
  <text x="180" y="80" fill="#94a3b8" font-size="10" font-weight="bold">OXYGEN (O2)</text>
  <polygon points="180,60 250,90 220,120 170,80" fill="#38bdf8" opacity="0.4"/>
  <text x="195" y="105" fill="#38bdf8" font-size="9" font-weight="bold">CO2 Blanket</text>
  <text x="45" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Displacing Oxygen Cuts the Fire Triangle</text>
  <text x="40" y="180" fill="#a7f3d0" font-size="8">Dense CO2 isolates fuel from atmospheric oxygen, extinguishing the flame</text>
</svg>
</div>
How does discharging carbon dioxide gas extinguish a blazing petrol fire, according to the 'fire triangle' concept?""",
     ["Dense CO2 gas displaces atmospheric oxygen, severing the oxidizer leg of the fire triangle and suffocating the combustion reaction",
      "CO2 chemically feeds the fire until it gets exhausted",
      "CO2 destroys the fuel completely",
      "CO2 increases the room's atmospheric pressure to 100 atmospheres"],
     "A", "easy",
     "Fire requires Fuel, Heat, and Oxygen (the fire triangle). Heavy CO2 blankets the liquid fuel surface, cutting off oxygen access and extinguishing the fire."),

    # 76: Methane Combustion Energy Balance
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="45" width="105" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="65" fill="#38bdf8" font-size="9" font-weight="bold">Reactants:</text>
  <text x="35" y="85" fill="#fde68a" font-size="9">CH4 (16 g)</text>
  <text x="35" y="102" fill="#cbd5e1" font-size="8">+ 2 O2 (64 g)</text>
  <line x1="135" y1="80" x2="195" y2="80" stroke="#ef4444" stroke-width="3"/>
  <polygon points="195,76 205,80 195,84" fill="#ef4444"/>
  <text x="145" y="70" fill="#f87171" font-size="8" font-weight="bold">Exothermic</text>
  <rect x="210" y="45" width="105" height="70" fill="#1e293b" stroke="#4ade80" stroke-width="1.5" rx="4"/>
  <text x="220" y="65" fill="#4ade80" font-size="9" font-weight="bold">Products:</text>
  <text x="220" y="85" fill="#fde68a" font-size="9">CO2 (44 g)</text>
  <text x="220" y="102" fill="#cbd5e1" font-size="8">+ 2 H2O (36 g)</text>
  <rect x="25" y="125" width="290" height="30" fill="#7f1d1d" rx="3"/>
  <text x="45" y="145" fill="#fef08a" font-size="9" font-weight="bold">Heat = -890 kJ/mol (Clean thermal combustion without soot or ash)</text>
  <text x="45" y="175" fill="#cbd5e1" font-size="8">High calorific value makes natural gas the premier transition fuel</text>
</svg>
</div>
The stoichiometry chart illustrates the combustion of methane. How much thermal energy is released per mole (16 grams) of methane burned completely in oxygen?""",
     ["Approximately 890 kJ of heat energy",
      "Approximately 10 kJ of heat energy",
      "Zero heat (it absorbs heat)",
      "Approximately 5,000,000 kJ of heat energy"],
     "A", "medium",
     "Complete combustion of one mole (16 g) of methane releases 890 kJ of thermal energy: CH4 + 2O2 -> CO2 + 2H2O + 890 kJ."),

    # 77: Modern CO2 Cylinder Fire Extinguisher
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="60" y="40" width="70" height="120" fill="#dc2626" stroke="#991b1b" stroke-width="2" rx="10"/>
  <rect x="70" y="70" width="50" height="70" fill="#0284c7" opacity="0.4" rx="3"/>
  <text x="73" y="105" fill="#ffffff" font-size="7" font-weight="bold">Liquid CO2</text>
  <text x="75" y="115" fill="#fde68a" font-size="7">(55 bar)</text>
  <rect x="85" y="25" width="20" height="15" fill="#1e293b"/>
  <polygon points="140,55 190,40 190,80" fill="#1e293b" stroke="#64748b"/>
  <text x="145" y="95" fill="#94a3b8" font-size="8">Discharge Horn</text>
  <path d="M 190 40 Q 240 25 280 40 Q 290 60 270 75 Q 230 85 190 80 Z" fill="#38bdf8" opacity="0.3"/>
  <text x="210" y="60" fill="#67e8f9" font-size="9" font-weight="bold">Cold CO2 Cloud</text>
  <text x="210" y="72" fill="#67e8f9" font-size="8">(-78.5 deg C)</text>
  <text x="45" y="175" fill="#facc15" font-size="9">Class B (Liquids) & Class C/E (Electrical): Leaves ZERO residue</text>
</svg>
</div>
Why are high-pressure liquid CO2 extinguishers the mandatory standard for protecting server computer rooms and electrical power substations?""",
     ["CO2 is an electrical insulator and completely sublimates away as gas, leaving zero liquid moisture or chemical powder residue to short-circuit sensitive electronics",
      "CO2 is cheaper than air",
      "CO2 cleans computer monitors with blue light",
      "CO2 increases processor clock speeds"],
     "A", "easy",
     "Unlike water (conductive) or dry powder (corrosive residue), CO2 is completely dielectric and vaporizes cleanly into the air without damaging microprocessors or circuitry."),

    # 78: Greenhouse Effect Mechanism of Methane vs CO2
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="30" y="30" width="280" height="50" fill="#0369a1" opacity="0.3" stroke="#38bdf8" rx="4"/>
  <text x="40" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Atmosphere: Greenhouse Gases (CO2, CH4, H2O)</text>
  <text x="40" y="68" fill="#facc15" font-size="8">CH4 has 28x higher Global Warming Potential (GWP) than CO2</text>
  <rect x="30" y="140" width="280" height="25" fill="#15803d" rx="3"/>
  <text x="130" y="157" fill="#ffffff" font-size="9" font-weight="bold">Earth Surface</text>
  <line x1="80" y1="10" x2="100" y2="140" stroke="#facc15" stroke-width="2"/>
  <text x="60" y="105" fill="#facc15" font-size="8">Solar UV/Visible</text>
  <line x1="180" y1="140" x2="200" y2="80" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="200" y1="80" x2="220" y2="140" stroke="#ef4444" stroke-width="2.5"/>
  <text x="210" y="110" fill="#f87171" font-size="8">Infrared Trapped</text>
  <text x="45" y="180" fill="#a7f3d0" font-size="9">Methane absorbs terrestrial infrared radiation strongly at 7.7 micrometres</text>
</svg>
</div>
Why is curbing atmospheric methane emissions considered an urgent climate change priority despite methane being less abundant than carbon dioxide?""",
     ["Methane absorbs infrared radiation intensely, possessing a Global Warming Potential roughly 28 times greater than CO2 per molecule over a 100-year timescale",
      "Methane creates holes in the Earth's crust",
      "Methane freezes the atmosphere into ice",
      "Methane turns clouds into iron"],
     "A", "medium",
     "Although atmospheric concentrations of CH4 (~1.9 ppm) are lower than CO2 (~420 ppm), methane's molecular absorption bands trap heat ~28 times more efficiently over a 100-year horizon."),

    # 79: Comparison of Complete vs Incomplete Methane Combustion
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="30" width="135" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Complete Combustion</text>
  <text x="35" y="70" fill="#cbd5e1" font-size="8">- Excess air supply</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">- CH4 + 2O2 -> CO2 + 2H2O</text>
  <text x="35" y="105" fill="#4ade80" font-size="9" font-weight="bold">Clean Blue Flame</text>
  <text x="35" y="125" fill="#cbd5e1" font-size="8">High heat, no smoke</text>
  <rect x="180" y="30" width="135" height="120" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fbbf24" font-size="9" font-weight="bold">Incomplete Combustion</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">- Deficient air supply</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="8">- 2CH4 + 3O2 -> 2CO + 4H2O</text>
  <text x="190" y="105" fill="#facc15" font-size="9" font-weight="bold">Yellow Sooty Flame</text>
  <text x="190" y="125" fill="#ef4444" font-size="8">Toxic CO + Black soot</text>
  <text x="45" y="170" fill="#fde68a" font-size="9">Air supply ratio governs burner flame efficiency and safety</text>
</svg>
</div>
What dangerous toxic byproduct is generated when gas heaters burn methane with insufficient ventilation or a blocked air shutter?""",
     ["Poisonous carbon monoxide (CO) gas",
      "Pure oxygen gas",
      "Liquid petroleum",
      "Nitrogen gas"],
     "A", "easy",
     "Oxygen starvation causes incomplete combustion: 2CH4 + 3O2 -> 2CO + 4H2O, releasing silent, lethal carbon monoxide gas."),

    # 80: Aerated Soft Drink Effervescence
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <rect x="50" y="45" width="45" height="90" fill="#334155" stroke="#94a3b8" rx="4"/>
  <rect x="62" y="30" width="20" height="15" fill="#ef4444"/>
  <text x="40" y="25" fill="#ef4444" font-size="8">Sealed (P ~ 3-4 atm)</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8">CO2 dissolved as H2CO3</text>
  <line x1="110" y1="85" x2="190" y2="85" stroke="#facc15" stroke-width="2"/>
  <polygon points="190,81 200,85 190,89" fill="#facc15"/>
  <text x="120" y="75" fill="#facc15" font-size="8" font-weight="bold">Open Cap (P -> 1 atm)</text>
  <rect x="220" y="45" width="45" height="90" fill="#0284c7" opacity="0.3" stroke="#38bdf8" rx="4"/>
  <circle cx="235" cy="110" r="3" fill="#f8fafc"/>
  <circle cx="245" cy="95" r="4" fill="#f8fafc"/>
  <circle cx="238" cy="70" r="3" fill="#f8fafc"/>
  <text x="210" y="25" fill="#38bdf8" font-size="8" font-weight="bold">Effervescence!</text>
  <text x="205" y="150" fill="#cbd5e1" font-size="8">Henry's Law: Gas escapes</text>
  <text x="35" y="170" fill="#4ade80" font-size="9">Henry's Law: Solubility of gas is directly proportional to applied pressure</text>
</svg>
</div>
Why do fizzy bubbles of carbon dioxide vigorously escape when the cap of an aerated soda bottle is opened?""",
     ["Opening the bottle drops the internal pressure to 1 atm; according to Henry's Law, gas solubility decreases, causing excess dissolved CO2 to bubble out",
      "Opening the cap heats the soda to 100 deg C",
      "Air from the room dissolves into the soda",
      "The soda liquid turns into solid ice"],
     "A", "medium",
     "Soda is bottled under 3-4 atm of CO2. When uncapped, the pressure drops to 1 atm, dramatically decreasing CO2 solubility and releasing gas bubbles (effervescence)."),

    # 81: Calcium Carbonate - Lime - Carbon Dioxide Cycle
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="110" y="15" width="120" height="30" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="125" y="34" fill="#38bdf8" font-size="9" font-weight="bold">Limestone (CaCO3)</text>
  <line x1="120" y1="48" x2="70" y2="90" stroke="#ef4444" stroke-width="2"/>
  <text x="40" y="65" fill="#f87171" font-size="8">Heat (- CO2)</text>
  <rect x="20" y="95" width="110" height="30" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="30" y="114" fill="#fbbf24" font-size="9" font-weight="bold">Quicklime (CaO)</text>
  <line x1="135" y1="110" x2="195" y2="110" stroke="#38bdf8" stroke-width="2"/>
  <text x="145" y="100" fill="#38bdf8" font-size="8">+ H2O</text>
  <rect x="200" y="95" width="125" height="30" fill="#1e293b" stroke="#4ade80" rx="3"/>
  <text x="205" y="114" fill="#4ade80" font-size="9" font-weight="bold">Slaked Lime [Ca(OH)2]</text>
  <line x1="260" y1="92" x2="220" y2="48" stroke="#facc15" stroke-width="2"/>
  <text x="245" y="65" fill="#facc15" font-size="8">+ CO2</text>
  <text x="40" y="165" fill="#fde68a" font-size="9">The Lime-Carbon Dioxide Chemical Cycle in Industry</text>
  <text x="40" y="180" fill="#cbd5e1" font-size="8">Whitewash absorbs atmospheric CO2 to form a hard, shiny CaCO3 surface</text>
</svg>
</div>
Why does freshly applied slaked lime whitewash on household walls develop a hard, shiny white surface after 2 to 3 days?""",
     ["Aqueous calcium hydroxide [Ca(OH)2] slowly absorbs carbon dioxide from air to form a hard layer of calcium carbonate (CaCO3)",
      "The paint absorbs light from electric bulbs",
      "The water evaporates and leaves white plaster",
      "Calcium hydroxide turns into metallic calcium"],
     "A", "medium",
     "Slaked lime reacts with ambient atmospheric CO2 over several days: Ca(OH)2 + CO2 -> CaCO3 (hard crystalline limestone layer) + H2O, producing a durable gleaming white finish."),

    # 82: Firedamp Explosion Risk in Coal Mines
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="40" y="55" width="260" height="25" fill="#334155" rx="3"/>
  <rect x="40" y="55" width="50" height="25" fill="#22c55e" rx="3"/>
  <text x="45" y="45" fill="#4ade80" font-size="8">Too Lean (<5%)</text>
  <rect x="90" y="55" width="80" height="25" fill="#dc2626"/>
  <text x="95" y="45" fill="#f87171" font-size="8" font-weight="bold">EXPLOSIVE (5-15%)</text>
  <rect x="170" y="55" width="130" height="25" fill="#f59e0b" rx="3"/>
  <text x="180" y="45" fill="#fbbf24" font-size="8">Too Rich (>15%)</text>
  <rect x="140" y="100" width="30" height="40" fill="#1e293b" stroke="#facc15" stroke-width="1.5" rx="3"/>
  <circle cx="155" cy="120" r="4" fill="#f59e0b"/>
  <text x="100" y="160" fill="#facc15" font-size="8" font-weight="bold">Davy Flame Safety Lamp</text>
  <text x="45" y="180" fill="#fde68a" font-size="9">Wire gauze conducts heat away to prevent ignited gas from igniting the mine</text>
</svg>
</div>
What is the flammable and explosive concentration range (firedamp) of methane in air that poses a critical explosion danger in coal mines?""",
     ["Between 5% and 15% methane by volume in air",
      "Between 50% and 90%",
      "Above 99% only",
      "Less than 0.1% only"],
     "A", "medium",
     "Methane has a lower explosive limit (LEL) of 5% and upper explosive limit (UEL) of 15% in air. Within this firedamp window, any ignition spark triggers violent coal mine explosions.")
]

def generate():
    all_qs = []
    
    # 40 Exam
    for i, item in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice
    for i, item in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], "OSC", item[3], "mock", "foundation", item[4]))

    out_file = "scripts/ch13_topic5.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
