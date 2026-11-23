import json
import random
import os
from build_cbse8_curi_batch import make_question, get_vaults_and_diffs

random.seed(8828)

def run():
    with open("scripts/cbse8_curi_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 8 DATA
    # -------------------------------------------------------------------------
    ch8_cases = {
        "CBSE-8-CURI-8-8.1.1": [
            ("A mixture is fundamentally defined in chemistry as:", "A physical combination of two or more substances in any proportion where each retains its individual chemical identity", ["A single pure element", "A chemical combination in fixed mass ratio", "A radioactive compound"]),
            ("Which of the following common substances is a mixture rather than a pure chemical compound?", "Air, seawater, brass, and soil", ["Distilled water", "Pure table sugar (sucrose)", "Sodium chloride salt"]),
            ("Can the components of a physical mixture be separated by simple physical methods?", "Yes, by physical techniques such as filtration, evaporation, magnetic separation, or distillation", ["No, only by nuclear fission", "No, they can never be separated", "Only by chemical burning"]),
            ("Do the constituents of a mixture combine in a fixed, definite ratio by mass?", "No, the components of a mixture can be mixed together in any variable proportion whatsoever", ["Yes, strictly 1:1 by mass", "Yes, strictly 2:1 by volume", "Only at freezing point"])
        ],
        "CBSE-8-CURI-8-8.1.2": [
            ("A homogeneous mixture is defined as a mixture that:", "Possesses a completely uniform composition and identical properties throughout its entire bulk", ["Has visibly separate phases and layers", "Settles into mud when left undisturbed", "Cannot be dissolved in water"]),
            ("Which of the following is an example of a homogeneous mixture?", "A clear sugar solution in water, lemonade, and atmospheric clean air", ["A mixture of sand and iron filings", "Chalk powder in water", "Oil floating on water"]),
            ("Solid homogeneous mixtures of two or more metals (or a metal and non-metal) are called:", "Alloys (such as brass, bronze, and stainless steel)", ["Compounds", "Ores", "Minerals"]),
            ("Why is a sample of clean tap water or salt solution considered homogeneous?", "Salt particles are dispersed uniformly at the molecular level, leaving no visible boundary of separation", ["Salt evaporates completely", "Salt molecules turn into water", "The liquid turns into pure glass"])
        ],
        "CBSE-8-CURI-8-8.1.3": [
            ("A heterogeneous mixture is defined as a mixture that:", "Consists of two or more physically distinct phases with non-uniform composition throughout", ["Has identical composition at every microscopic point", "Is completely transparent like pure water", "Cannot be separated by filtration"]),
            ("Which of the following represents a heterogeneous mixture?", "A mixture of sand and water, muddy pond water, and a salad", ["Salt dissolved completely in warm water", "Clean dry atmospheric air", "A gold-copper alloy ring"]),
            ("Why does a mixture of vegetable oil and water form a heterogeneous mixture?", "Oil and water are immiscible liquids with different polarities, forming two visibly distinct separate layers", ["Oil dissolves instantly in water", "Oil chemically burns water", "Both turn into a single gas"]),
            ("When light is shone through a heterogeneous colloidal mixture (like milk or foggy air), the beam becomes visible due to:", "The Tyndall Effect (scattering of light by suspended particles)", ["Regular mirror reflection", "Refraction through glass prisms", "Total absorption of photons"])
        ],
        "CBSE-8-CURI-8-8.1.4": [
            ("When iron filings and sulfur powder are simply mixed together at room temperature without heating, how do they behave?", "They retain their individual chemical properties; iron remains magnetic and sulfur dissolves in carbon disulfide", ["They form a black non-magnetic compound immediately", "They catch fire spontaneously", "Iron turns into sulfur"]),
            ("How can iron filings be separated cleanly from a dry mixture of iron and sulfur powder?", "By passing a bar magnet over the mixture, which attracts and lifts the magnetic iron filings", ["By boiling in water", "By filtering through paper", "By shining a laser"]),
            ("When you drink lemonade (a mixture of water, lemon juice, sugar, and salt), why can you taste both sweetness and sourness?", "The constituent substances (sugar and citric acid) retain their individual chemical properties in the mixture", ["A new chemical compound with no taste is created", "The lemon juice destroys the sugar", "Salt neutralizes all flavor"]),
            ("What happens if the iron-sulfur mixture is heated strongly in a test tube until it glows red?", "A chemical reaction occurs forming a new compound, iron(II) sulfide (FeS), which is non-magnetic and insoluble in CS2", ["It remains a simple physical mixture", "Iron turns into pure gold", "Sulfur turns into oxygen gas"])
        ],
        "CBSE-8-CURI-8-8.2.1": [
            ("A pure substance is scientifically defined in chemistry as:", "A sample of matter consisting of only one single type of constituent particle (atom or molecule) with fixed composition", ["Any food that is unadulterated and fresh", "Milk purchased directly from a dairy farm", "Honey collected from a beehive"]),
            ("Which of the following is classified scientifically as a pure substance?", "Pure distilled water (\\(\\text{H}_2\\text{O}\\)) and pure copper wire (Cu)", ["Fresh market milk", "Pure fruit juice", "Mineral spring water"]),
            ("Can a pure chemical substance be separated into other kinds of matter by any physical separation process?", "No, pure substances cannot be separated into constituent parts by physical methods alone", ["Yes, by simple handpicking", "Yes, by straining through a sieve", "Yes, by boiling gently"]),
            ("Pure chemical substances are broadly subdivided into which two categories?", "Elements and Compounds", ["Metals and Rocks", "Solids and Liquids only", "Homogeneous and Heterogeneous"])
        ],
        "CBSE-8-CURI-8-8.2.2": [
            ("Why do pure chemical substances exhibit sharp, constant melting and boiling points?", "All particles have identical intermolecular forces, requiring an exact, fixed amount of thermal energy to break the lattice", ["Pure substances contain no heat", "Pure substances melt only at zero degrees", "Pure substances have zero boiling point"]),
            ("Pure distilled water at standard atmospheric pressure boils at exactly \\(100^\\circ\\text{C}\\) and freezes at \\(0^\\circ\\text{C}\\). If common salt is dissolved in it:", "The boiling point ELEVATES above \\(100^\\circ\\text{C}\\) and freezing point DEPRESSES below \\(0^\\circ\\text{C}\\)", ["Boiling point drops to 50 degrees", "Freezing point rises to 10 degrees", "Melting and boiling points remain unchanged"]),
            ("How do forensic and analytical chemists routinely verify the purity of an unknown synthesized drug compound?", "By determining its melting point range using a capillary apparatus; pure compounds melt within a sharp \\(0.5^\\circ\\text{C}\\) window", ["By tasting a small pinch of the powder", "By checking if it smells like flowers", "By weighing it on a bathroom scale"]),
            ("A liquid sample boils steadily between \\(102^\\circ\\text{C}\\) and \\(106^\\circ\\text{C}\\) over a range rather than at a sharp fixed temperature. This indicates that:", "The liquid is an impure mixture rather than a pure chemical substance", ["The liquid is 100% pure distilled water", "The thermometer is broken", "The liquid has no boiling point"])
        ],
        "CBSE-8-CURI-8-8.2.3": [
            ("Which comparison correctly distinguishes a pure substance from a mixture?", "A pure substance has a constant, fixed chemical composition throughout, while a mixture has variable composition", ["A mixture has sharp melting points while pure substances do not", "Pure substances can be separated by filtration", "There is no difference in composition"]),
            ("When a compound like water (\\(\\text{H}_2\\text{O}\\)) is formed from hydrogen and oxygen gases, the properties of water are:", "Completely different from those of its constituent elements (water extinguishes fire, while hydrogen burns and oxygen supports combustion)", ["A simple blend of the properties of hydrogen and oxygen", "Identical to hydrogen gas", "Identical to oxygen gas"]),
            ("In which system (a compound or a mixture) is energy (heat/light) usually absorbed or released during its preparation?", "In the formation of a chemical compound (chemical reaction)", ["In the physical preparation of a simple mixture", "In stirring sand into water", "In both equally"]),
            ("Which statement about physical separation is true?", "Components of a mixture can be separated by physical means, but components of a chemical compound can only be separated by chemical or electrochemical methods", ["Compounds can be separated by a kitchen sieve", "Mixtures require nuclear reactors to separate", "Neither can ever be separated"])
        ],
        "CBSE-8-CURI-8-8.3.1": [
            ("An element is defined in modern chemistry as:", "The simplest form of a pure substance that consists of only one kind of atom and cannot be broken down into simpler substances by ordinary chemical means", ["A mixture of two metals", "A liquid containing dissolved salts", "A compound of carbon and hydrogen"]),
            ("Approximately how many chemical elements are currently known to science, and how many occur naturally on Earth?", "118 known elements (94 occurring naturally, and 24 synthesized artificially in laboratories)", ["Over 10,000 elements", "Only 4 elements (earth, air, fire, water)", "Exactly 50 elements"]),
            ("Who was the first French chemist to establish a scientifically useful definition of an element in 1789?", "Antoine Lavoisier", ["Robert Boyle", "John Dalton", "Dmitri Mendeleev"]),
            ("Which of the following chemical substances is a pure chemical element?", "Gold (Au), Oxygen (\\(\\text{O}_2\\)), Iron (Fe), and Nitrogen (\\(\\text{N}_2\\))", ["Water (\\(\\text{H}_2\\text{O}\\))", "Carbon dioxide (\\(\\text{CO}_2\\))", "Methane (\\(\\text{CH}_4\\))"])
        ],
        "CBSE-8-CURI-8-8.3.2": [
            ("What physical property of metals is defined as the ability to be hammered or rolled into thin sheets without shattering?", "Malleability (e.g., gold and aluminium foil)", ["Ductility", "Sonority", "Lustre"]),
            ("What physical property of metals is defined as the ability to be drawn into long, thin wires?", "Ductility (e.g., copper and platinum wires)", ["Malleability", "Brittleness", "Insulation"]),
            ("Which metal is unique because it exists in the LIQUID state at normal room temperature (\\(25^\\circ\\text{C}\\))?", "Mercury (Hg)", ["Sodium (Na)", "Lead (Pb)", "Aluminium (Al)"]),
            ("Which non-metal is an exceptional electrical conductor due to delocalized electrons in its hexagonal planar layers?", "Graphite (an allotrope of Carbon)", ["Diamond", "Sulfur", "Phosphorus"])
        ],
        "CBSE-8-CURI-8-8.3.3": [
            ("A chemical compound is defined as a pure substance formed when:", "Two or more chemical elements combine chemically in a fixed, definite ratio by mass", ["Elements are mixed physically in any random proportion", "Two liquids are stirred together", "An element melts into liquid"]),
            ("According to the Law of Constant Proportions (Proust's Law), what is the fixed mass ratio of hydrogen to oxygen in pure water (\\(\\text{H}_2\\text{O}\\)) regardless of its source?", "\\(1 : 8\\) by mass (since \\(2\\ \\text{g}\\ \\text{H} : 16\\ \\text{g}\\ \\text{O} = 1:8\\))", ["\\(2 : 1\\) by mass", "\\(1 : 1\\) by mass", "\\(8 : 1\\) by mass"]),
            ("What is the chemical name and fixed constituent elements of ordinary table salt?", "Sodium chloride (\\(\\text{NaCl}\\)), composed of Sodium and Chlorine chemically bonded", ["Potassium iodide", "Calcium carbonate", "Sodium bicarbonate"]),
            ("Can the constituent elements of a chemical compound be separated by simple physical filtering or boiling?", "No, breaking a compound requires chemical reactions or electrochemical decomposition", ["Yes, using filter paper", "Yes, using a bar magnet", "Yes, by straining through cloth"])
        ],
        "CBSE-8-CURI-8-8.3.4": [
            ("Water (\\(\\text{H}_2\\text{O}\\)) can be decomposed into hydrogen and oxygen gases by which electrochemical method?", "Electrolysis of acidified water using an electric current", ["Boiling water to steam", "Freezing water into ice cubes", "Filtering through activated charcoal"]),
            ("During the electrolysis of acidified water in a voltameter, at which electrode is hydrogen gas evolved, and in what volume ratio compared to oxygen?", "Hydrogen gas is evolved at the Cathode (-) in a \\(2:1\\) volume ratio to Oxygen gas evolved at the Anode (+)", ["Hydrogen evolves at the Anode in 1:1 ratio", "Oxygen evolves at the Cathode in 3:1 ratio", "Both gases evolve together at the Cathode"]),
            ("What strong fundamental chemical bonds hold the atoms of sodium and chlorine together in sodium chloride?", "Ionic bonds formed by electrostatic attraction between \\(\\text{Na}^+\\) cations and \\(\\text{Cl}^-\\) anions", ["Weak gravitational bonds", "Magnetic dipole interactions", "Temporary friction"]),
            ("When calcium carbonate (limestone, \\(\\text{CaCO}_3\\)) is heated strongly, what thermal decomposition products are formed?", "Calcium oxide (quicklime, \\(\\text{CaO}\\)) and carbon dioxide gas (\\(\\text{CO}_2\\))", ["Calcium metal and oxygen gas", "Calcium hydroxide and water", "Pure carbon and lime"])
        ],
        "CBSE-8-CURI-8-8.4.1": [
            ("Why is copper metal extensively utilized for manufacturing electrical household wiring and power cables?", "Copper has exceptionally high electrical conductivity, excellent ductility, and is relatively inexpensive and corrosion-resistant", ["Copper is an electrical insulator", "Copper melts at room temperature", "Copper is lighter than air"]),
            ("Why is aluminium metal preferred for manufacturing overhead high-voltage power transmission cables and aircraft bodies?", "Aluminium is lightweight (low density), a very good electrical conductor, and forms a protective corrosion-resistant oxide film", ["Aluminium is heavier than lead", "Aluminium never conducts electricity", "Aluminium is as soft as butter"]),
            ("Gold and silver are extensively used for crafting fine jewelry and commemorative ornaments because of their:", "High metallic lustre, permanent resistance to air and moisture corrosion, and supreme malleability and ductility", ["Low melting points like wax", "High chemical reactivity with water", "Magnetic properties"]),
            ("Why is iron alloyed with chromium and nickel to produce Stainless Steel for surgical instruments and kitchen utensils?", "Stainless steel is hard, strong, and does not rust or corrode when exposed to water and atmospheric oxygen", ["To make iron soluble in water", "To make it flexible like rubber", "To make it conduct sound faster"])
        ],
        "CBSE-8-CURI-8-8.4.2": [
            ("Which gaseous non-metal element is absolutely vital for aerobic cellular respiration in almost all living organisms?", "Oxygen (\\(\\text{O}_2\\))", ["Nitrogen", "Chlorine", "Helium"]),
            ("Which non-metal is applied to municipal drinking water supplies and swimming pools as a powerful disinfectant to kill pathogenic bacteria?", "Chlorine (\\(\\text{Cl}_2\\))", ["Sulfur", "Phosphorus", "Carbon"]),
            ("Tincture of Iodine, widely applied on cuts and wounds as an antiseptic medicine, is prepared by dissolving iodine in:", "A mixture of alcohol and water", ["Pure sulfuric acid", "Liquid cooking oil", "Molten sodium"]),
            ("Which non-metal element is an essential ingredient in vulcanizing natural rubber to impart strength and elasticity to automobile tires?", "Sulfur (S)", ["Carbon", "Nitrogen", "Silicon"])
        ],
        "CBSE-8-CURI-8-8.4.3": [
            ("Which chemical compound is the primary chemical ingredient of baking soda used in baking and antacid medicines?", "Sodium hydrogen carbonate (Sodium bicarbonate, \\(\\text{NaHCO}_3\\))", ["Sodium chloride", "Sodium hydroxide", "Calcium sulfate"]),
            ("What is the chemical name and formula of washing soda used extensively in laundering and softening hard water?", "Sodium carbonate decahydrate (\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\))", ["Sodium bicarbonate", "Calcium carbonate", "Copper sulfate"]),
            ("Brass is an important commercial alloy mixture widely used for musical instruments, plumbing fittings, and decorative items. What are its constituent metals?", "Copper (about 70%) and Zinc (about 30%)", ["Copper and Tin (Bronze)", "Iron and Carbon (Steel)", "Lead and Tin (Solder)"]),
            ("Bronze, celebrated since ancient civilization for statues and medals, is an alloy composed of:", "Copper and Tin", ["Copper and Zinc", "Iron and Nickel", "Aluminium and Magnesium"])
        ],
        "CBSE-8-CURI-8-8.5.1": [
            ("What is a 'mineral' scientifically defined as in geology and earth science?", "A naturally occurring, inorganic solid substance with a definite chemical composition and ordered internal atomic crystal structure", ["Any organic compost in soil", "Crude petroleum oil", "Synthetic plastic manufactured in factories"]),
            ("Are all rocks considered pure minerals?", "No, most rocks are heterogeneous aggregates of two or more different minerals (e.g., granite is an aggregate of quartz, feldspar, and mica)", ["Yes, every rock is a single pure element", "Rocks are liquid mixtures", "Rocks contain no minerals"]),
            ("Which common mineral, chemically composed of silicon dioxide (\\(\\text{SiO}_2\\)), is the principal constituent of quartz and beach sand?", "Quartz (Silica)", ["Calcite", "Hematite", "Bauxite"]),
            ("Minerals found on Earth are non-renewable natural resources because:", "They take millions of years of geological tectonic processes to form and cannot be replenished within human timescales", ["They evaporate into clouds", "They burn up in rain", "They turn into water"])
        ],
        "CBSE-8-CURI-8-8.5.2": [
            ("What is an 'ore' in metallurgical science?", "A naturally occurring mineral deposit from which one or more valuable metals can be extracted profitably and conveniently", ["Any useless rock found in a field", "A synthetic alloy made in a foundry", "A liquid chemical solution"]),
            ("Which mineral is the primary commercial ore mined for the industrial extraction of Aluminium metal?", "Bauxite (hydrated aluminium oxide, \\(\\text{Al}_2\\text{O}_3 \\cdot 2\\text{H}_2\\text{O}\\))", ["Hematite", "Galena", "Cinnabar"]),
            ("Hematite (\\(\\text{Fe}_2\\text{O}_3\\)) and Magnetite (\\(\\text{Fe}_3\\text{O}_4\\)) are the primary commercial ores mined for the extraction of which vital metal?", "Iron (Fe)", ["Copper", "Zinc", "Silver"]),
            ("Are all ores minerals, and are all minerals ores?", "All ores are minerals, but NOT all minerals are ores (only those minerals with high metal concentration extracted economically are ores)", ["All minerals are ores, but not all ores are minerals", "Minerals and ores are completely identical", "Neither has any metal content"])
        ],
        "CBSE-8-CURI-8-8.5.3": [
            ("Why is the conservation of mineral and metal resources urgently required for sustainable development?", "Mineral deposits on Earth are finite, non-renewable, and their extraction causes environmental disruption and ecological degradation", ["Because metals will turn into plastic", "Because minerals destroy sunlight", "Because humans will stop needing metals"]),
            ("Which metallurgical practice conserves vast amounts of electrical energy and mineral reserves compared to mining virgin bauxite ore?", "Recycling aluminium scrap and beverage cans (saving 95% of the electrical energy required for virgin extraction)", ["Dumping aluminium into oceans", "Burning aluminium in incinerators", "Burying aluminium deep underground"]),
            ("Sustainable management of mineral resources emphasizes which key strategies?", "Reduce consumption, Reuse metal products, Recycle scrap metals, and develop eco-friendly substitute materials", ["Mining all reserves as fast as possible", "Banning the use of all metals permanently", "Discharging mineral tailings into rivers"]),
            ("How does open-cast mining for iron and coal ores impact surrounding forest ecosystems and local indigenous communities?", "Causes deforestation, biodiversity loss, air and water pollution, soil erosion, and displacement of communities", ["Creates lush agricultural forests", "Purifies drinking water aquifers", "Increases rainfall"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 9 DATA
    # -------------------------------------------------------------------------
    ch9_cases = {
        "CBSE-8-CURI-9-9.1.1": [
            ("A true solution is defined in physical chemistry as:", "A homogeneous mixture of two or more substances whose constituent solute particles are smaller than 1 nanometer in diameter", ["A heterogeneous suspension that settles on standing", "A chemical compound with covalent bonds", "A solid rock"]),
            ("Which of the following is a characteristic property of a true solution?", "It is clear and transparent, solute particles do not settle upon standing, and it cannot be separated by ordinary filter paper", ["It is opaque and cloudy", "Solute particles settle to the bottom within 5 minutes", "It scatters light strongly (shows Tyndall effect)"]),
            ("Why does a flashlight beam pass invisibly through a true solution of copper sulfate in water?", "Solute ions/molecules are smaller than \\(1\\ \\text{nm}\\) (submicroscopic) and cannot scatter visible light wavelengths", ["Copper sulfate absorbs 100% of photons", "Water reflects all light backward", "The liquid turns into ice"]),
            ("Which of the following represents a true solution?", "Clear sugar syrup, saltwater, and carbonated soda water", ["Chalk powder stirred in water", "Clay mud in river water", "Milk"])
        ],
        "CBSE-8-CURI-9-9.1.2": [
            ("In a binary solution, the component present in a smaller amount that dissolves is called the:", "Solute", ["Solvent", "Suspension", "Emulsion"]),
            ("In a solution, the component present in the largest amount in which the solute dissolves is called the:", "Solvent", ["Solute", "Precipitate", "Residue"]),
            ("In a salt-water solution prepared by dissolving \\(15\\ \\text{g}\\) of common salt in \\(100\\ \\text{g}\\) of pure water:", "Salt is the solute, and water is the solvent", ["Water is the solute, and salt is the solvent", "Both are solutes", "Both are solvents"]),
            ("In a cup of sweet tea, what are the solutes and what is the primary solvent?", "Sugar and tea extract chemicals are the solutes, and hot water is the solvent", ["Sugar is the solvent and water is the solute", "Milk is the only solute", "Tea leaves are the solvent"])
        ],
        "CBSE-8-CURI-9-9.1.3": [
            ("Why is liquid water universally celebrated as the 'Universal Solvent' in chemistry and biology?", "Its high dielectric constant and polar molecular structure enable it to dissolve a wider variety of ionic and polar substances than any other liquid", ["It dissolves all solid metals like iron and gold", "It is the only liquid on Earth", "It has zero boiling point"]),
            ("A solution in which water is the dissolving solvent is termed an:", "Aqueous solution (e.g., aqueous sodium chloride solution)", ["Non-aqueous solution", "Organic solution", "Alcoholic tincture"]),
            ("A solution in which a substance is dissolved in a solvent OTHER than water (like alcohol, benzene, or acetone) is called a:", "Non-aqueous solution", ["Aqueous solution", "Hydrated solution", "Dilute aqueous solution"]),
            ("Tincture of iodine, used as an antiseptic for cleaning minor cuts, is a non-aqueous solution of iodine dissolved in:", "Ethyl alcohol (ethanol)", ["Pure water", "Mineral engine oil", "Liquid mercury"])
        ],
        "CBSE-8-CURI-9-9.1.4": [
            ("Which of the following represents a solid-in-liquid solution?", "Common salt or sugar dissolved in water", ["Alcohol mixed with water", "Carbon dioxide gas dissolved in soda water", "Brass alloy"]),
            ("Which of the following represents a liquid-in-liquid solution?", "Vinegar (acetic acid dissolved in water) and alcoholic beverages (ethanol in water)", ["Salt in water", "Oxygen in water", "Amalgam of mercury in zinc"]),
            ("Carbonated beverages (soda water, soft drinks) are commercial examples of which type of solution?", "Gas-in-liquid solution (carbon dioxide gas dissolved under high pressure in water)", ["Liquid-in-solid solution", "Solid-in-gas solution", "Gas-in-gas solution"]),
            ("Clean atmospheric air is a gaseous solution consisting of:", "A gas-in-gas homogeneous solution of nitrogen solvent (78%), oxygen solute (21%), and trace gases", ["A solid-in-liquid solution", "A liquid-in-gas suspension", "A pure chemical compound"])
        ],
        "CBSE-8-CURI-9-9.2.1": [
            ("An 'unsaturated solution' at a given temperature is defined as a solution in which:", "More solute can be dissolved without raising the temperature", ["No more solute can dissolve at that temperature", "Solute crystals precipitate out rapidly", "Solute and solvent have equal masses"]),
            ("A 'saturated solution' at a specified temperature is defined as a solution in which:", "No more solute can dissolve at that specific temperature; an equilibrium exists between dissolved and undissolved solute", ["Only half the maximum solute is dissolved", "The solvent has completely evaporated", "More solute dissolves effortlessly"]),
            ("If a small crystal of copper sulfate is dropped into an UNSATURATED solution of copper sulfate at room temperature:", "The crystal dissolves slowly into the solution", ["The crystal grows ten times larger instantly", "The entire solution turns into a solid rock", "The crystal explodes"]),
            ("If additional solute is added to an already SATURATED solution at constant temperature and stirred vigorously:", "The excess solute remains undissolved and settles to the bottom of the beaker", ["The excess solute dissolves immediately", "The liquid turns into gas", "The temperature drops to absolute zero"])
        ],
        "CBSE-8-CURI-9-9.2.2": [
            ("Solubility of a solute in a particular solvent at a given temperature is officially defined as:", "The maximum mass in grams of solute that dissolves completely in \\(100\\ \\text{g}\\) of solvent to form a saturated solution at that temperature", ["The total volume of solution produced in litres", "The time in seconds required for sugar to dissolve", "The temperature at which the solvent freezes"]),
            ("If a maximum of \\(36\\ \\text{g}\\) of sodium chloride (\\(\\text{NaCl}\\)) dissolves in \\(100\\ \\text{g}\\) of water at \\(20^\\circ\\text{C}\\) to form a saturated solution, what is its solubility?", "\\(36\\ \\text{g}\\) per \\(100\\ \\text{g}\\) of water at \\(20^\\circ\\text{C}\\)", ["\\(72\\ \\text{g}\\)", "\\(18\\ \\text{g}\\)", "\\(100\\ \\text{g}\\)"]),
            ("How much water is required to dissolve completely \\(18\\ \\text{g}\\) of common salt at \\(20^\\circ\\text{C}\\) (solubility \\(= 36\\ \\text{g} / 100\\ \\text{g}\\))?", "\\(50\\ \\text{g}\\) of water (\\(\\frac{18}{36} \\times 100 = 50\\))", ["\\(200\\ \\text{g}\\)", "\\(100\\ \\text{g}\\)", "\\(25\\ \\text{g}\\)"]),
            ("Does the solubility of different solid chemical salts (e.g., potassium nitrate vs sodium chloride) in water differ at the same temperature?", "Yes, each chemical substance has its own characteristic solubility governed by its chemical nature and lattice energy", ["No, all chemical substances have identical solubility of 50 g", "Solubility is the same for all solids in water", "Solubility never changes"])
        ],
        "CBSE-8-CURI-9-9.2.3": [
            ("For most solid solutes (like sugar, potassium nitrate, copper sulfate), how does solubility in water change when temperature is INCREASED?", "Solubility increases significantly with an increase in temperature (dissolution is typically an endothermic process)", ["Solubility decreases to zero", "Solubility remains strictly constant", "The solute turns into a gas"]),
            ("Why can hot water dissolve substantially more sugar than cold water when preparing sweet dessert syrups (chashni)?", "Higher thermal kinetic energy loosens solvent intermolecular structure and supplies enthalpy to break the solute crystal lattice", ["Hot water evaporates all sugar", "Sugar melts into water molecules", "Cold water destroys sugar crystals"]),
            ("What happens when a clear, hot saturated solution of copper sulfate is allowed to cool slowly to room temperature?", "Excess dissolved solute crystallizes out of the solution as pure, geometric copper sulfate crystals", ["The liquid turns into solid stone", "The solution boils vigorously", "All water evaporates instantly"]),
            ("For a few unusual chemical substances like cerium sulfate and slaked lime (\\(\\text{Ca(OH)}_2\\)), how does solubility in water behave with increasing temperature?", "Solubility decreases as temperature rises (dissolution is exothermic)", ["Solubility increases exponentially", "Solubility remains constant at all temperatures", "They turn into ice"])
        ],
        "CBSE-8-CURI-9-9.2.4": [
            ("A 'supersaturated solution' is defined as a solution that:", "Contains more dissolved solute than a normal saturated solution at that temperature, prepared by cooling a hot saturated solution carefully without disturbance", ["Contains zero dissolved solute", "Is completely frozen solid", "Contains equal parts of sand and water"]),
            ("Supersaturated solutions are metastable and thermodynamically unstable because:", "Dropping a single tiny seed crystal of solute immediately triggers rapid crystallization of all excess dissolved solute", ["They evaporate with an explosive sound", "They cannot be touched by glass", "They catch fire at room temperature"]),
            ("The purification technique of 'crystallization' is preferred over simple evaporation to dryness because:", "Crystallization yields pure, well-formed crystals while leaving soluble impurities behind in the mother liquor, preventing thermal decomposition", ["Crystallization is 10 times faster", "Evaporation creates diamonds", "Crystallization uses no water"]),
            ("How are pure large blue crystals of copper sulfate grown in a school science laboratory?", "By filtering a hot saturated solution of copper sulfate and allowing it to cool undisturbed overnight with a seed crystal suspended on a thread", ["By boiling copper sulfate until it turns to ash", "By shaking the hot beaker vigorously", "By adding cold milk to copper sulfate"])
        ],
        "CBSE-8-CURI-9-9.2.5": [
            ("What is Oral Rehydration Solution (ORS) used to treat in medical health emergencies?", "Severe dehydration and vital electrolyte loss caused by cholera, diarrhea, vomiting, and heat stroke", ["Broken leg bones", "Headache from lack of sleep", "Skin fungal rashes"]),
            ("In an emergency at home when packaged commercial ORS sachets are unavailable, how can standard home-made ORS be prepared safely?", "Dissolve 6 level teaspoons of sugar and 1/2 level teaspoon of common salt in 1 litre of clean boiled and cooled drinking water", ["Mix 10 cups of salt in a glass of water", "Mix sugar with milk and vinegar", "Drink raw sea water"]),
            ("Why does ORS contain both glucose (sugar) and sodium chloride (salt) dissolved together in precise proportions?", "Glucose molecules actively facilitate the physiological co-transport of sodium ions and water across the intestinal epithelial wall into blood", ["Sugar is added only for sweet taste", "Salt keeps the sugar from spoiling", "Sodium destroys the stomach lining"]),
            ("Why must the proportions of salt in home-made ORS never be made excessively high?", "Excessive salt concentration can cause dangerous hypernatremia, drawing more water out of body tissues and worsening dehydration in young children", ["Too much salt makes water freeze", "Salt turns into acid in the mouth", "Sugar will evaporate"])
        ],
        "CBSE-8-CURI-9-9.3.1": [
            ("Do atmospheric gases like oxygen (\\(\\text{O}_2\\)) and carbon dioxide (\\(\\text{CO}_2\\)) dissolve in natural water bodies (rivers, lakes, oceans)?", "Yes, gases dissolve in water in small but biologically vital quantities through dissolution at the air-water interface", ["No, gases can never dissolve in liquids", "Only in deep underground oil wells", "Only when water is boiled to steam"]),
            ("What tiny bubbles are seen forming on the inner bottom and walls of a glass beaker long before water begins to boil upon heating?", "Dissolved atmospheric air (oxygen and nitrogen) coming out of solution because gas solubility decreases with rising temperature", ["Bubbles of boiling water steam", "Hydrogen gas from water splitting", "Carbon monoxide gas"]),
            ("How does carbon dioxide gas dissolve into commercial bottled sparkling sodas and soft drinks?", "Dissolved under very high pressure; when the bottle cap is opened, pressure drops and \\(\\text{CO}_2\\) fizzes out with effervescence", ["By freezing \\(\\text{CO}_2\\) ice in the bottle", "By adding baking soda to vinegar inside", "By blowing with a straw"]),
            ("Which fundamental gas law (Henry's Law) governs the solubility of a gas in a liquid at constant temperature?", "The solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the liquid (\\(S \\propto P\\))", ["Boyle's Law", "Charles's Law", "Archimedes' Principle"])
        ],
        "CBSE-8-CURI-9-9.3.2": [
            ("Why is the presence of Dissolved Oxygen (DO) in natural water bodies indispensable for aquatic life?", "Fish, aquatic amphibians, and aquatic plants utilize dissolved oxygen for respiration through specialized respiratory organs like gills", ["Fish breathe water molecules directly by splitting H2O", "Fish have lungs like humans", "Oxygen makes water transparent"]),
            ("How do fish extract dissolved oxygen from water passing over their respiratory gills?", "Oxygen diffuses across thin, highly vascularized gill filaments into the bloodstream while carbon dioxide diffuses out", ["Fish swallow water into stomach to extract oxygen", "Gills burn oxygen like a stove", "Fish store bubbles in bones"]),
            ("How do submerged aquatic green plants (like Hydrilla and Vallisneria) obtain carbon dioxide for photosynthesis underwater?", "They absorb dissolved carbon dioxide directly from the surrounding water through their thin epidermal surfaces", ["They extend leaves into air every night", "They obtain carbon from sand", "They do not perform photosynthesis"]),
            ("What environmental crisis occurs when domestic sewage or chemical fertilizer runoff causes algal blooms in lakes (Eutrophication)?", "Massive decomposition of dead algae by aerobic bacteria depletes all dissolved oxygen, suffocating fish and aquatic animals (dead zones)", ["Lake water turns into drinking milk", "Oxygen levels increase ten times", "Fish multiply uncontrollably"])
        ],
        "CBSE-8-CURI-9-9.3.3": [
            ("Unlike most solid solutes, how does the solubility of a gas in a liquid change when the liquid's temperature is INCREASED?", "The solubility of gases in liquids DECREASES significantly as temperature rises (gas molecules gain kinetic energy and escape)", ["Gas solubility increases rapidly", "Gas solubility remains unchanged", "Gases turn into solid ice"]),
            ("Why do fish in rivers and lakes suffer from respiratory suffocation and die during severe summer heatwaves or thermal factory discharges?", "Warm water holds substantially less dissolved oxygen than cold water, leading to acute aquatic hypoxia", ["Fish prefer freezing ice only", "Water boils in summer", "Sunlight poisons fish skin"]),
            ("What happens to the solubility of carbon dioxide gas in a liquid when the external pressure is INCREASED?", "Gas solubility INCREASES directly with increased pressure (Henry's Law)", ["Gas solubility decreases to zero", "Pressure has no effect on gas solubility", "The liquid turns into solid salt"]),
            ("Why does a carbonated soda bottle hiss loudly and foam with effervescent bubbles the instant you twist open the cap?", "Opening the cap releases high internal pressure; at lower atmospheric pressure, \\(\\text{CO}_2\\) solubility drops suddenly and gas rushes out", ["Air rushes into the bottle from the room", "The soda boils from room heat", "Chemical combustion ignites the soda"])
        ],
        "CBSE-8-CURI-9-9.4.1": [
            ("Density (\\(\\rho\\)) is a characteristic physical property of a substance defined as:", "The mass per unit volume of the substance (\\(\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}}\\))", ["The total weight of an object", "The volume divided by mass", "The surface area per kilogram"]),
            ("What is the density of pure water at \\(4^\\circ\\text{C}\\) in SI units (\\(\\text{kg/m}^3\\)) and in metric units (\\(\\text{g/cm}^3\\))?", "\\(1000\\ \\text{kg/m}^3\\) and \\(1\\ \\text{g/cm}^3\\)", ["\\(100\\ \\text{kg/m}^3\\) and \\(10\\ \\text{g/cm}^3\\)", "\\(500\\ \\text{kg/m}^3\\) and \\(0.5\\ \\text{g/cm}^3\\)", "\\(10{,}000\\ \\text{kg/m}^3\\) and \\(0.1\\ \\text{g/cm}^3\\)"]),
            ("If a metallic block has a mass of \\(400\\ \\text{g}\\) and occupies a volume of \\(50\\ \\text{cm}^3\\), what is its density?", "\\(8\\ \\text{g/cm}^3\\) (\\(400 / 50 = 8\\))", ["\\(20{,}000\\ \\text{g/cm}^3\\)", "\\(0.125\\ \\text{g/cm}^3\\)", "\\(350\\ \\text{g/cm}^3\\)"]),
            ("Which liquid metal has an extraordinary density of approximately \\(13.6\\ \\text{g/cm}^3\\), making an iron cannonball float on its surface?", "Mercury (Hg)", ["Molten lead", "Bromine", "Liquid gallium"])
        ],
        "CBSE-8-CURI-9-9.4.2": [
            ("When equal volumes (\\(100\\ \\text{mL}\\)) of pure water and mustard cooking oil are placed on a beam balance, what is observed?", "The water is heavier than the oil, because water has a higher density (\\(1.0\\ \\text{g/cm}^3\\)) than vegetable oil (\\(\\sim 0.9\\ \\text{g/cm}^3\\))", ["The oil is twice as heavy as water", "Both weigh exactly the same", "The oil evaporates instantly"]),
            ("Why does cooking oil always float on top of water when poured into the same glass?", "Oil is immiscible with water and has a lower density than water, causing it to float naturally on the water surface", ["Oil is heavier and sinks", "Water pushes oil down", "Oil dissolves in water completely"]),
            ("Which of the following common liquids is LESS dense than pure liquid water?", "Kerosene oil, mustard oil, and pure ethyl alcohol", ["Honey", "Glycerine", "Mercury"]),
            ("Why does a thick layer of dense natural honey settle straight to the bottom when poured into a glass of plain water?", "Honey has a significantly higher density (\\(\\sim 1.4\\ \\text{g/cm}^3\\)) than water, causing it to sink through water", ["Honey repels water with magnetic force", "Honey is a solid rock", "Water absorbs all sugar instantly"])
        ],
        "CBSE-8-CURI-9-9.4.3": [
            ("In a classroom 'Density Column' demonstration, honey, colored water, and vegetable oil are poured carefully into a tall glass cylinder. In what order do they layer from bottom to top?", "Honey at bottom (densest), colored water in middle, and vegetable oil on top (least dense)", ["Oil at bottom, honey in middle, water on top", "Water at bottom, oil in middle, honey on top", "They mix together into a brown liquid"]),
            ("If a small plastic die of density \\(1.1\\ \\text{g/cm}^3\\) is dropped into this density column, where will it come to rest?", "It sinks through the oil (\\(0.9\\ \\text{g/cm}^3\\)) and water (\\(1.0\\ \\text{g/cm}^3\\)), and floats on top of the honey (\\(1.4\\ \\text{g/cm}^3\\))", ["Floats on top of the oil", "Sinks to the very bottom beneath honey", "Dissolves in the water"]),
            ("Why do ice cubes float in a glass of drinking water with roughly \\(90\\%\\) submerged and \\(10\\%\\) above the surface?", "Ice has an anomalous open cage-like crystalline structure with lower density (\\(0.92\\ \\text{g/cm}^3\\)) than liquid water (\\(1.0\\ \\text{g/cm}^3\\))", ["Ice is hot and buoyant", "Ice contains helium gas bubbles", "Gravity does not act on solid ice"]),
            ("What ecological life-saving benefit does the anomalous expansion and floating of ice provide to aquatic life in cold winter climates?", "The floating surface ice acts as an insulating blanket, keeping the deep water beneath at \\(4^\\circ\\text{C}\\) so fish and aquatic plants survive", ["Ice turns pond water into steam", "Fish hibernate inside frozen ice cubes", "Ice feeds aquatic plants with sugar"])
        ],
        "CBSE-8-CURI-9-9.4.4": [
            ("What happens to the density of pure water when large amounts of common table salt (\\(\\text{NaCl}\\)) are dissolved in it?", "The density of the water INCREASES substantially because salt ions pack into intermolecular spaces without adding significant volume", ["The density decreases", "The density remains strictly unchanged", "The water turns into gas"]),
            ("A fresh raw chicken egg sinks in a beaker of pure tap water. What happens when several spoonfuls of salt are stirred into the water?", "The egg rises and floats easily on the surface of the dense saltwater", ["The egg dissolves into the brine", "The egg sinks deeper and cracks", "The egg turns into a chick"]),
            ("Why does the raw egg float in concentrated saltwater but sink in pure freshwater?", "The density of the egg is greater than freshwater (so it sinks), but less than the density of concentrated saltwater (so it floats)", ["Saltwater has zero gravity", "The egg shell absorbs salt and becomes lighter", "Freshwater pushes eggs down"]),
            ("Why can human swimmers float effortlessly on the surface of the Dead Sea without swimming strokes?", "The Dead Sea has an extreme salt concentration (\\(\\sim 34\\%\\)) giving the water a high density (\\(\\sim 1.24\\ \\text{g/cm}^3\\)) exceeding human body density", ["The Dead Sea water is boiling hot", "The Dead Sea has magnetic mud pulling people up", "The water has zero depth"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 10 DATA
    # -------------------------------------------------------------------------
    ch10_cases = {
        "CBSE-8-CURI-10-10.1.1": [
            ("A spherical mirror is defined in geometrical optics as:", "A curved mirror whose reflecting surface forms part of a hollow sphere of glass", ["A flat plane window pane", "A triangular prism of quartz", "A cylindrical lens"]),
            ("What are the two fundamental types into which spherical mirrors are classified based on the curvature of their reflecting surface?", "Concave mirrors and Convex mirrors", ["Plane mirrors and Prisms", "Thick mirrors and Thin mirrors", "Cylindrical and Toric"]),
            ("How is a spherical glass bowl converted into a reflecting spherical mirror during industrial manufacturing?", "By coating one surface with a thin layer of highly reflecting silver or aluminium metal protected by red lead oxide paint", ["By polishing glass with sand", "By heating the glass until it turns opaque", "By magnetizing the glass atoms"]),
            ("If the outer bulging surface of a spherical glass piece is silvered and the inner hollow curved surface reflects light, the mirror is a:", "Concave mirror", ["Convex mirror", "Plane mirror", "Biconvex lens"])
        ],
        "CBSE-8-CURI-10-10.1.2": [
            ("A concave mirror is characterized by a reflecting surface that is:", "Curved inward (receding away from the incident light like the interior of a cave)", ["Bulging outward towards incident light", "Completely flat and planar", "Wavy and irregular"]),
            ("Why is a concave mirror also known as a 'converging mirror'?", "It reflects a parallel beam of incident light rays inward to converge at a single focal point in front of the mirror", ["It scatters parallel rays outward in all directions", "It transmits light straight through like a window", "It splits light into seven colors"]),
            ("What type of image is formed by a concave mirror when an object is placed very close to it (between the Pole and the Focus)?", "A virtual, erect, and greatly magnified (enlarged) image behind the mirror", ["A real, inverted, and diminished image", "No image is formed", "A tiny inverted point"]),
            ("When an object is placed far away at infinity from a concave mirror, where is the image formed?", "At the Principal Focus (\\(F\\)), real, inverted, and highly diminished (point-sized)", ["Behind the mirror at infinity", "At the Centre of Curvature", "At the Pole"])
        ],
        "CBSE-8-CURI-10-10.1.3": [
            ("When you look at your reflection in the inner scooped curved surface of a clean, shiny stainless steel spoon, what do you observe at arm's length?", "An inverted (upside down) and diminished image of your face", ["An erect and magnified image", "No reflection at all", "A flat unmagnified image"]),
            ("As you bring the inner scooped surface of the shiny spoon very close to your eye, what dramatic change occurs in your reflection?", "The image flips to become erect (upright) and noticeably magnified", ["The image disappears completely", "The image turns into seven rainbow colors", "The image remains inverted"]),
            ("When you flip the spoon and look at the outer bulging curved surface at any distance, what type of image do you always see?", "An erect (upright) and diminished (smaller) image, acting as a convex mirror", ["An inverted real image", "A magnified giant face", "A blurry black shadow"]),
            ("This simple kitchen spoon demonstration proves that:", "The inner curved surface acts as a concave mirror, while the outer bulging surface acts as a convex mirror", ["Spoons are optical prisms", "Stainless steel polarizes all light", "Curved surfaces cannot reflect light"])
        ],
        "CBSE-8-CURI-10-10.1.4": [
            ("The geometric center point of the reflecting surface of a spherical mirror is called the:", "Pole (symbol: P)", ["Centre of Curvature (C)", "Principal Focus (F)", "Aperture"]),
            ("The center of the hollow sphere of glass of which the spherical mirror forms a part is termed the:", "Centre of Curvature (symbol: C)", ["Pole (P)", "Principal Focus (F)", "Optical Center"]),
            ("The straight line passing through the Pole (P) and the Centre of Curvature (C) of a spherical mirror is the:", "Principal Axis", ["Focal length", "Aperture diameter", "Normal axis"]),
            ("What is the mathematical relationship between the Radius of Curvature (\\(R\\)) and the Focal Length (\\(f\\)) of a spherical mirror?", "\\(R = 2f\\) (or \\(f = R/2\\))", ["\\(R = f/2\\)", "\\(R = f^2\\)", "\\(R = 4f\\)"])
        ],
        "CBSE-8-CURI-10-10.2.1": [
            ("What is the fundamental optical distinction between a 'Real image' and a 'Virtual image'?", "A real image is formed by actual intersection of light rays and can be captured on a screen; a virtual image cannot be captured on a screen", ["A virtual image is always inverted", "A real image is formed behind the mirror", "There is no difference in physics"]),
            ("Which statement about real images formed by spherical mirrors is universally true?", "Real images are always inverted (upside down) relative to the object", ["Real images are always erect", "Real images can never be magnified", "Real images are formed inside the human eye only"]),
            ("The image of your face seen in an ordinary plane dressing table mirror is:", "A virtual, erect, and laterally inverted image that cannot be formed on a physical screen behind the wall", ["A real image projected on the wall", "An inverted real image", "A magnified chromatic image"]),
            ("Cinema movie projections seen on a theater screen are examples of:", "Real, magnified images projected by optical lenses onto the screen", ["Virtual reflections from mirrors", "Diffuse shadows only", "Optical illusions in the brain"])
        ],
        "CBSE-8-CURI-10-10.2.2": [
            ("When an object is placed at the Centre of Curvature (\\(C\\)) of a concave mirror, what are the exact size and nature of the image formed?", "Real, inverted, and exactly the SAME SIZE as the object, located at \\(C\\)", ["Magnified and virtual", "Diminished and erect", "Point-sized at Focus"]),
            ("When an object is located beyond the Centre of Curvature (\\(C\\)) of a concave mirror, the image formed is:", "Real, inverted, and diminished (smaller than the object), situated between \\(F\\) and \\(C\\)", ["Magnified and behind mirror", "Same size at infinity", "Erect and virtual"]),
            ("When an object is placed between the Focus (\\(F\\)) and the Centre of Curvature (\\(C\\)) of a concave mirror, the image is:", "Real, inverted, and magnified (enlarged), formed beyond \\(C\\)", ["Diminished at Focus", "Virtual behind mirror", "Same size at Pole"]),
            ("Optical linear magnification (\\(m\\)) produced by a spherical mirror is defined as:", "The ratio of the height of the image (\\(h_i\\)) to the height of the object (\\(h_o\\)) (\\(m = \\frac{h_i}{h_o}\\))", ["The distance of the object divided by focal length", "The diameter of the mirror aperture", "The speed of light divided by frequency"])
        ],
        "CBSE-8-CURI-10-10.2.3": [
            ("In ray tracing for spherical mirrors, an incident ray traveling parallel to the principal axis after reflection from a concave mirror:", "Passes through the Principal Focus (\\(F\\))", ["Passes through the Centre of Curvature", "Reflects along its own path", "Bends towards the Pole"]),
            ("An incident ray passing through the Centre of Curvature (\\(C\\)) of a concave mirror reflects back along its own path because:", "It strikes the mirror surface normally (along the radial radius, angle of incidence \\(i = 0^\\circ\\))", ["The mirror absorbs the ray", "The focal length is zero at C", "Light loses speed at C"]),
            ("When an object is placed exactly at the Principal Focus (\\(F\\)) of a concave mirror, the reflected rays emerge parallel, forming an image at:", "Infinity (extremely magnified, real, and inverted)", ["At the Pole", "At the Centre of Curvature", "Inside the mirror glass"]),
            ("How many minimum intersecting reflected rays are required in geometrical optics to determine the precise location of an image point?", "At least two reflected rays", ["Only one ray", "At least ten rays", "Exactly five rays"])
        ],
        "CBSE-8-CURI-10-10.2.4": [
            ("What type of image is ALWAYS formed by a convex mirror regardless of the object's distance in front of it?", "Virtual, erect, and diminished (smaller than the object), formed behind the mirror between \\(P\\) and \\(F\\)", ["Real, inverted, and magnified", "Real, inverted, and diminished", "Virtual, erect, and magnified"]),
            ("Why are convex mirrors universally installed as rear-view side mirrors in automobiles, buses, and motorcycles?", "They always form erect, diminished images and provide a much wider field of view of traffic behind than plane mirrors", ["They magnify distant vehicles", "They make night driving darker", "They are cheaper than flat glass"]),
            ("Large convex mirrors mounted at blind hairpin road corners and supermarket aisle intersections serve to:", "Provide a wide-angle view of approaching oncoming vehicles and pedestrians around hidden blind corners", ["Focus sunlight to illuminate roads", "Record video without cameras", "Slow down speeding cars"]),
            ("Can a convex mirror ever form a real, inverted image on a screen under any ordinary object placement?", "No, reflected rays from a convex mirror always diverge, forming strictly virtual images behind the mirror", ["Yes, when the object is at infinity", "Yes, when submerged in water", "Only in moonlight"])
        ],
        "CBSE-8-CURI-10-10.2.5": [
            ("Why do dentists utilize small handheld concave mirrors when examining patients' teeth?", "When held close to a tooth (within focal length), it produces an erect and highly magnified virtual image of the tooth", ["To reflect bright sunlight onto gums", "To measure body temperature", "To take X-ray photographs"]),
            ("Why is a concave parabolic mirror fitted behind the bulb in vehicle headlights, searchlights, and torches?", "When the bulb filament is placed at the Principal Focus (\\(F\\)), reflected rays emerge as a powerful, parallel beam of light", ["To scatter light in all directions", "To absorb heat from the bulb", "To produce yellow light"]),
            ("Why are giant concave mirrors employed in solar furnaces and solar thermal cookers?", "They concentrate parallel rays of incoming sunlight to a sharp focus at the focal point, generating intense heat exceeding \\(1000^\\circ\\text{C}\\)", ["To reflect solar wind into space", "To produce electricity by friction", "To cool the food in shade"]),
            ("Shaving and makeup mirrors are typically concave mirrors because:", "They produce an enlarged, upright view of facial features when held closer than their focal length", ["They show a wide angle of the entire room", "They invert the face upside down", "They never reflect light"])
        ],
        "CBSE-8-CURI-10-10.3.1": [
            ("In the reflection of light, what is the angle between the incident ray and the normal at the point of incidence called?", "Angle of incidence (\\(\\angle i\\))", ["Angle of reflection", "Angle of deviation", "Glancing angle"]),
            ("What is the angle between the reflected ray and the normal at the point of incidence termed?", "Angle of reflection (\\(\\angle r\\))", ["Angle of incidence", "Angle of refraction", "Critical angle"]),
            ("The normal to a reflecting surface at the point of incidence is defined as:", "The perpendicular line drawn at \\(90^\\circ\\) to the reflecting surface at the exact point where the light ray strikes", ["The parallel line along the mirror face", "The line joining the light source to the eye", "The tangent to the mirror edge"]),
            ("If an incident ray makes an angle of \\(40^\\circ\\) with the normal line, what is the value of the angle of incidence \\(i\\)?", "\\(40^\\circ\\)", ["\\(50^\\circ\\)", "\\(80^\\circ\\)", "\\(90^\\circ\\)"])
        ],
        "CBSE-8-CURI-10-10.3.2": [
            ("The First Law of Reflection states that for any reflecting surface:", "The angle of incidence is always strictly equal to the angle of reflection (\\(\\angle i = \\angle r\\))", ["Angle of incidence is twice angle of reflection", "Angle of incidence + Angle of reflection = 90 degrees", "Angle of incidence is greater than angle of reflection"]),
            ("If a light ray strikes a flat plane mirror with an angle of incidence of \\(45^\\circ\\), what is its angle of reflection?", "\\(45^\\circ\\)", ["\\(90^\\circ\\)", "\\(30^\\circ\\)", "\\(0^\\circ\\)"]),
            ("If a light ray strikes a plane mirror perpendicular to its surface (along the normal, \\(i = 0^\\circ\\)), how does it reflect?", "It reflects straight back along its original path (\\(r = 0^\\circ\\))", ["It reflects at \\(90^\\circ\\) along the mirror surface", "It refracts into the glass at \\(45^\\circ\\)", "It is completely absorbed"]),
            ("If the angle between the incident ray and the reflected ray is measured to be \\(80^\\circ\\), what is the angle of incidence \\(i\\)?", "\\(40^\\circ\\) (since \\(\\angle i + \\angle r = 2i = 80^\\circ \\implies i = 40^\\circ\\))", ["\\(80^\\circ\\)", "\\(20^\\circ\\)", "\\(50^\\circ\\)"])
        ],
        "CBSE-8-CURI-10-10.3.3": [
            ("The Second Law of Reflection states that the incident ray, the reflected ray, and the normal at the point of incidence:", "All lie in the same geometric plane", ["Form a three-dimensional spiral", "Are perpendicular to one another", "Intersect only at infinity"]),
            ("What does the 'coplanar property' of reflection guarantee in physics experiments?", "A ray striking a flat tabletop mirror horizontally remains in that same horizontal plane after reflection without tilting vertically", ["Light bends into a rainbow", "Light speed doubles upon reflection", "Photons vanish into the mirror"]),
            ("If the incident ray and the normal lie in the vertical plane of this page, in which plane must the reflected ray lie?", "In the very same vertical plane of this page", ["In a perpendicular plane jutting out of the page", "In a spherical curved plane", "In no plane at all"]),
            ("Do the laws of reflection (\\(\\angle i = \\angle r\\) and coplanarity) apply to irregular rough surfaces like cardboard, wood, and stone?", "Yes, the laws of reflection hold strictly true at every microscopic point of incidence on all surfaces in nature", ["No, laws of reflection only work on silver mirrors", "Only when illuminated by laser light", "Only in complete darkness"])
        ],
        "CBSE-8-CURI-10-10.3.4": [
            ("Regular (specular) reflection occurs when a parallel beam of incident light reflects off:", "A smooth, highly polished flat surface (such as a plane mirror), maintaining parallel reflected rays", ["A rough, unpolished wooden board", "A wrinkled sheet of aluminium foil", "A page of a printed book"]),
            ("Diffuse (irregular) reflection occurs when a parallel beam of incident light strikes a rough surface, causing reflected rays to:", "Scatter in various random directions because surface normals vary at different microscopic points", ["Remain strictly parallel to each other", "Violate the law \\(\\angle i = \\angle r\\)", "Turn into invisible heat waves"]),
            ("Why can you read the printed text on a paper book from almost any viewing angle in a well-lit room?", "Diffuse reflection from the matte, microscopic roughness of paper scatters light evenly in all directions", ["The paper acts as a regular mirror", "The paper emits its own fluorescent light", "The ink reflects light regularly"]),
            ("Why does a calm, still water lake reflect a clear mirror image of mountain peaks, whereas rippling water blurs the image?", "Still water provides a smooth surface for regular specular reflection, while ripples create microscopic tilted planes causing diffuse scattering", ["Ripples absorb all incident light", "Ripples split light into seven colors", "Water turns into ice"])
        ],
        "CBSE-8-CURI-10-10.3.5": [
            ("What are the characteristic properties of an image formed by a flat Plane Mirror?", "Virtual and erect, same size as the object, located as far behind the mirror as the object is in front, and laterally inverted", ["Real, inverted, and magnified", "Real, inverted, and diminished", "Virtual, inverted, and half-sized"]),
            ("If a student stands \\(2\\ \\text{metres}\\) in front of a flat plane mirror, what is the distance between the student and their image?", "\\(4\\ \\text{metres}\\) (\\(2\\ \\text{m}\\ \\text{in front} + 2\\ \\text{m}\\ \\text{behind} = 4\\ \\text{m}\\))", ["\\(2\\ \\text{metres}\\)", "\\(1\\ \\text{metre}\\)", "\\(8\\ \\text{metres}\\)"]),
            ("What is 'Lateral Inversion' observed in a plane mirror reflection?", "The apparent sideways reversal where the left side of the object appears as the right side of the image, and vice-versa", ["The image appearing upside down", "The image turning black and white", "The image shrinking to a point"]),
            ("Why is the word 'AMBULANCE' written in reverse lettering (lateral inversion) on the front of emergency hospital vehicles?", "Drivers viewing it in their car's rear-view mirror read it laterally inverted as normal, readable 'AMBULANCE' and yield way", ["It is an ancient medical tradition", "It prevents speed camera detection", "To save paint on the vehicle"])
        ],
        "CBSE-8-CURI-10-10.4.1": [
            ("Refraction of light is fundamentally defined in optics as:", "The bending or change in the direction of a light ray when it passes obliquely from one optical medium into another of different optical density", ["The bouncing back of light into the same medium", "The splitting of light into colors", "The total absorption of light"]),
            ("What is the fundamental physical cause of the refraction (bending) of light at the boundary between two media?", "The change in the speed of propagation of light as it travels from one optical medium to another", ["Friction with glass atoms", "Gravitational attraction of glass", "Electrostatic charge of photons"]),
            ("When a light ray travels obliquely from an optically rarer medium (air) into an optically denser medium (glass or water), it bends:", "Towards the normal line (speed of light decreases in denser medium)", ["Away from the normal line", "Straight through without bending", "Back into the air"]),
            ("Why does a straight pencil dipped obliquely into a glass tumbler of water appear distinctly bent or broken at the water-air interface?", "Light rays emerging from the submerged pencil refract away from the normal into air, creating a virtual image shifted upward", ["Water physically bends the wooden pencil", "Water dissolves the pencil wood", "Water reflects all rays"])
        ],
        "CBSE-8-CURI-10-10.4.2": [
            ("A Convex Lens is physically shaped such that it is:", "Thicker at the center and thinner at the circular edges", ["Thinner at the center and thicker at edges", "Uniformly flat throughout", "Curved like a cylinder"]),
            ("Why is a convex lens also termed a 'converging lens'?", "It refracts a parallel beam of incident light rays inward, focusing them to meet at a single real focal point on the other side", ["It diverges parallel rays outward", "It reflects light backwards like a mirror", "It polarizes light"]),
            ("A Concave Lens is physically shaped such that it is:", "Thinner at the middle center and thicker at the outer edges (diverging lens)", ["Thicker in the middle", "Spherical like a ball", "Flat on both sides"]),
            ("Why is a concave lens called a 'diverging lens'?", "It refracts parallel incident light rays outward so they spread apart and appear to diverge from a virtual focus", ["It brings rays together to a sharp point", "It turns light into infrared", "It blocks light completely"])
        ],
        "CBSE-8-CURI-10-10.4.3": [
            ("The geometric central point of an optical lens through which light rays pass without undergoing any net angular deviation is the:", "Optical Centre (symbol: O)", ["Principal Focus", "Centre of Curvature", "Aperture"]),
            ("The straight line passing perpendicularly through the optical center and centers of curvature of both faces of a lens is the:", "Principal Axis", ["Focal line", "Normal axis", "Diameter"]),
            ("The distance between the Optical Centre (O) and the Principal Focus (F) of a lens is termed its:", "Focal Length (\\(f\\))", ["Radius of curvature", "Aperture", "Thickness"]),
            ("How many principal foci (focal points) does a thin spherical glass lens have, and why?", "Two principal foci (\\(F_1\\) and \\(F_2\\)), located symmetrically on either side of the lens because light can enter from either face", ["Only one focal point", "Four focal points", "An infinite number of foci"])
        ],
        "CBSE-8-CURI-10-10.4.4": [
            ("When an object is placed between the Focus (\\(F_1\\)) and the Optical Centre (\\(O\\)) of a convex lens, what type of image is formed?", "Virtual, erect, and magnified on the same side as the object (working as a magnifying reading glass)", ["Real, inverted, and diminished", "No image is formed", "Point-sized on the screen"]),
            ("When an object is placed at \\(2F_1\\) (twice the focal length) in front of a convex lens, where is the image formed and what is its size?", "At \\(2F_2\\) on the other side, real, inverted, and exactly the SAME SIZE as the object", ["At Focus, point-sized", "At infinity, magnified", "Virtual behind lens"]),
            ("When parallel rays of sunlight are focused through a convex magnifying lens onto a piece of dry paper, why does the paper begin to scorch and smoke?", "The convex lens converges all parallel solar radiant heat energy onto a tiny focal spot, raising its temperature past the ignition point", ["The glass lens catches fire", "Sunlight is converted into electricity", "The paper is made of gunpowder"]),
            ("When an object is placed beyond \\(2F_1\\) in front of a convex lens, the image formed on the other side is:", "Real, inverted, and diminished, situated between \\(F_2\\) and \\(2F_2\\)", ["Magnified and virtual", "Same size at \\(2F_2\\)", "At infinity"])
        ],
        "CBSE-8-CURI-10-10.4.5": [
            ("What type of image is ALWAYS produced by a Concave (diverging) Lens for any position of an object in front of it?", "Virtual, erect, and diminished (smaller than the object), situated on the same side as the object", ["Real, inverted, and magnified", "Real, inverted, and diminished", "Virtual, erect, and magnified"]),
            ("Can a concave lens ever project a real image onto a physical white screen under any conditions?", "No, refracted rays diverge outward and can never physically intersect to form a real image", ["Yes, when the object is at infinity", "Yes, when submerged in oil", "Only in red light"]),
            ("When looking through a concave spectacle lens, how do distant trees and buildings appear?", "Erect (upright) but noticeably smaller and closer than they really are", ["Inverted upside down", "Magnified like through a microscope", "Completely dark"]),
            ("A student tries to focus sunlight onto a paper using a concave lens. What happens?", "Sunlight diverges outward over a wider area; the paper never burns and no focal spot is formed", ["The paper burns in 1 second", "A real inverted image forms", "The lens shatters"])
        ],
        "CBSE-8-CURI-10-10.4.6": [
            ("A simple hand magnifying glass used by watchmakers and stamp collectors consists of which type of optical lens?", "A convex lens of short focal length held close to the object", ["A concave lens", "A thick flat glass slab", "A cylindrical mirror"]),
            ("Which vision defect (nearsightedness), where a person can see nearby objects clearly but distant objects appear blurred, is corrected using CONCAVE lenses?", "Myopia (Nearsightedness)", ["Hypermetropia (Farsightedness)", "Presbyopia", "Astigmatism"]),
            ("Which vision defect (farsightedness), where a person can see distant objects clearly but cannot focus on nearby reading text, is corrected using CONVEX lenses?", "Hypermetropia (Farsightedness)", ["Myopia", "Cataract", "Glaucoma"]),
            ("High-power compound research microscopes and astronomical refracting telescopes use combinations of:", "Two or more convex lenses (Objective and Eyepiece) to achieve high optical magnification", ["Concave mirrors only", "Flat glass sheets", "Color filters only"])
        ],
        "CBSE-8-CURI-10-10.5.1": [
            ("The optical phenomenon of splitting composite white sunlight into its constituent spectral colors is called:", "Dispersion of light", ["Refraction of light", "Total internal reflection", "Diffraction of light"]),
            ("What is the acronym used to remember the sequence of seven constituent spectral colors produced by the dispersion of white light?", "VIBGYOR (Violet, Indigo, Blue, Green, Yellow, Orange, Red)", ["ROYGBIV reversed", "CMYK", "RGB", "VIBGYO"]),
            ("Why does white light split into seven distinct colors upon passing obliquely through a triangular glass prism?", "Each color of light has a different wavelength and travels at a different speed in glass, undergoing a different angle of deviation", ["The glass prism contains seven internal colored dyes", "Glass absorbs white photons", "Light reacts chemically with silica"]),
            ("Which color of the visible spectrum undergoes the MAXIMUM angle of deviation upon passing through a glass prism?", "Violet light (shortest wavelength, travels slowest in glass)", ["Red light", "Yellow light", "Green light"])
        ],
        "CBSE-8-CURI-10-10.5.2": [
            ("Which color of the visible spectrum undergoes the LEAST angle of deviation (bends the least) upon passing through a glass prism?", "Red light (longest wavelength, travels fastest in glass)", ["Violet light", "Indigo light", "Blue light"]),
            ("The band of seven colored rays obtained on a screen when white light passes through a dispersing prism is termed a:", "Spectrum (visible spectrum)", ["Shadow band", "Diffraction fringe", "Interference ring"]),
            ("Who was the first scientist to demonstrate in 1665 that sunlight is made up of seven constituent colors using a glass prism?", "Sir Isaac Newton", ["Galileo Galilei", "Christian Huygens", "Johannes Kepler"]),
            ("Can a single monochromatic laser ray (e.g., pure red light) be dispersed into other colors upon passing through a glass prism?", "No, monochromatic light has only one wavelength and refracts without splitting into other colors", ["Yes, it splits into green and blue", "Yes, into seven new colors", "It turns into white light"])
        ],
        "CBSE-8-CURI-10-10.5.3": [
            ("What was Sir Isaac Newton's recombination experiment to prove that colors originate from sunlight and not from the glass prism itself?", "Placing an identical second glass prism in an inverted position behind the first prism recombined the seven colors back into white light", ["Painting the prism black", "Heating the prism in fire", "Shining moonlight through the prism"]),
            ("A circular disc divided into seven sectors painted with the spectral colors VIBGYOR is known as a:", "Newton's Disc", ["Faraday's Wheel", "Galileo's Dial", "Kepler's Ring"]),
            ("When a Newton's Disc is spun rapidly on an axle, why does the disc appear white (or pale greyish-white)?", "Persistence of vision causes the rapid succession of colored retinal stimuli to blend together in the human brain as white light", ["The paint rubs off at high speed", "Air friction bleaches the pigments", "The colors turn into heat"]),
            ("What duration does the human retina retain a visual impression of an image before it fades away (persistence of vision)?", "About \\(1/16^{\\text{th}}\\) of a second", ["About 5 seconds", "About 1 minute", "Instantaneously zero"])
        ],
        "CBSE-8-CURI-10-10.5.4": [
            ("Which spectacular natural meteorological phenomenon is a natural demonstration of the dispersion of sunlight in the sky?", "A Rainbow", ["A Mirage in a hot desert", "An Aurora Borealis", "A Solar Eclipse"]),
            ("In the formation of a natural rainbow, what tiny natural objects act as millions of miniature dispersing prisms in the atmosphere?", "Spherical suspended raindrops in the air after a rainfall shower", ["Floating dust particles", "Ice crystals in clouds only", "Microscopic pollen grains"]),
            ("What three optical phenomena occur inside a raindrop to produce a primary rainbow?", "Refraction and dispersion upon entry, total internal reflection at the back drop surface, and refraction upon exiting the drop", ["Only regular reflection from drop surface", "Only diffraction through air", "Scattering of light only"]),
            ("In what direction must an observer face relative to the Sun to see a rainbow in the sky?", "The observer's back must be towards the Sun, looking towards the rain shower (rainbow appears opposite the Sun)", ["Looking directly at the Sun", "Facing North only", "Facing directly upward into space"])
        ]
    }

    # Generate Chapters 8, 9, 10
    for ch_num, cases_dict in [(8, ch8_cases), (9, ch9_cases), (10, ch10_cases)]:
        item = next(x for x in manifest if str(x["chapterNumber"]) == str(ch_num))
        ch_questions = []
        start_seq = 300
        for lf in item["leafs"]:
            tc = lf["topicCode"]
            needed = lf["needed"]
            sub_name = lf["name"]
            cases = cases_dict[tc]
            vaults, diffs = get_vaults_and_diffs(needed)

            for i in range(needed):
                ctx, ans, wrongs = cases[i % len(cases)]
                step1 = f"Identify the scientific concept relating to {sub_name}."
                step2 = f"Evaluate key principles: {ctx}"
                step3 = f"Therefore, the correct answer is {ans}."
                q = make_question(tc, sub_name, ctx, ans, wrongs, step1, step2, step3, diffs[i], vaults[i], start_seq)
                start_seq += 1
                ch_questions.append(q)

        out_path = f"scripts/cbse8_curi_ch{ch_num}_topup.json"
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(ch_questions, out_f, indent=2)
        print(f"Generated {len(ch_questions)} questions for Chapter {ch_num} -> {out_path}")

if __name__ == "__main__":
    run()
