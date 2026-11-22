# scripts/build_clean_scit_ch19_part3a.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.3 (Subtopics 19.3.1 and 19.3.2)
# 2 subtopics x 80 = 160 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_3_1():
    tc = "MH-9-SCIT-19-19.3.1"
    tname = "Physical vs chemical changes and indicators of chemical reactions"
    archs = [
        # Arch 0: Physical Changes & Characteristics
        {
            'data': [
                ("a change in which a substance undergoes a change in its physical properties (shape, size, state) without forming any new chemical substance", "Physical change (typically reversible)", "Chemical change", "Nuclear transmutation", "Biological degradation"),
                ("the melting of solid ice into liquid water and the subsequent boiling of water into water vapor", "Reversible physical changes of state", "Irreversible chemical transformations", "Electrolytic decomposition reactions", "Endothermic synthesis reactions"),
                ("the physical purification process of obtaining pure solid crystals with well-defined geometric faces from a hot saturated solution", "Crystallization", "Distillation", "Neutralization", "Sedimentation"),
                ("tearing a sheet of paper into multiple small pieces is classified as a physical change because", "No new chemical substance is formed; each shredded piece is still composed of cellulose molecules", "The paper changes its chemical composition", "The paper emits carbon dioxide", "The reaction is reversible by heating"),
                ("the dissolution of solid sugar or common salt (\\(NaCl\\)) into liquid water", "A physical change (solute can be recovered completely by evaporation of the solvent)", "A chemical reaction producing hydrochloric acid", "An irreversible chemical transformation", "A neutralization reaction"),
                ("the glowing of the metallic tungsten filament inside an incandescent electric light bulb when current passes", "A physical change (filament glows due to high temperature and returns to original state when turned off)", "A chemical combination reaction", "An irreversible oxidation of tungsten", "A displacement reaction"),
                ("the conversion of solid iodine or camphor directly into gaseous vapor upon gentle heating without passing through the liquid phase", "Sublimation (a physical change)", "Evaporation", "Condensation", "Combustion"),
                ("the stretching of a coiled steel spring or rubber band within its elastic limit", "A reversible physical change", "An irreversible chemical reaction", "A decomposition process", "A redox reaction"),
                ("the breaking of a glass tumbler into sharp glass shards upon falling to the floor", "An irreversible physical change (no new substance is formed, but broken shape cannot easily be restored)", "A chemical synthesis reaction", "A neutralization reaction", "An exothermic combustion"),
                ("the condensation of steam droplets onto the cold underside of a stainless steel cooking lid", "A physical change of state (gas to liquid)", "A chemical oxidation reaction", "A displacement reaction", "An endothermic decomposition")
            ],
            'tmpls': [
                "Which category of matter transformation is defined as: {0}?",
                "Identify the physical transformation type: {0}.",
                "Which physical separation and purification technique corresponds to: {0}?",
                "What fundamental molecular reason explains why: {0}?",
                "Why is the following aqueous process classified as: {0}?",
                "What thermodynamic physical explanation accounts for: {0}?",
                "Which phase transition phenomenon represents: {0}?",
                "Which mechanical deformation is classified as: {0}?",
                "What structural distinction defines: {0}?",
                "Which phase change is exemplified by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Transformation Classification**\\nThe prompt describes {item[0]}.\\n**Step 2: Physical vs Chemical Criteria**\\nPhysical changes alter physical states, dimensions, or appearances without breaking or forming covalent bonds; no new chemical substance is created.\\n**Step 3: Verification**\\nThe correct answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Chemical Changes & Key Examples
        {
            'data': [
                ("a process in which one or more substances react to produce one or more entirely new substances possessing completely different chemical properties", "Chemical change (Chemical reaction)", "Physical change", "Mechanical mixture", "Allotropic transition"),
                ("the burning of a magnesium ribbon in air producing a dazzling white light and a white powdery ash of magnesium oxide", "A chemical combination reaction (\\(2Mg + O_2 \\rightarrow 2MgO\\))", "A reversible physical change", "A sublimation process", "An endothermic dissociation"),
                ("the reddish-brown flaky coating formed on iron articles exposed to moist air over extended time", "Rust (hydrated ferric oxide, \\(Fe_2O_3\\cdot xH_2O\\))", "Magnetite (\\(Fe_3O_4\\))", "Ferrous carbonate (\\(FeCO_3\\))", "Iron sulphide (\\(FeS\\))"),
                ("the chemical change where fresh milk turns sour and solidifies into curd due to lactic acid bacteria (Lactobacillus)", "Curdling of milk (lactic acid fermentation)", "Evaporative crystallization", "Physical emulsification", "Protein sublimation"),
                ("the biochemical process where green plants synthesize glucose and oxygen from carbon dioxide and water using sunlight and chlorophyll", "Photosynthesis (a complex chemical change)", "Transpiration", "Respiration", "Photolysis of air"),
                ("the digestion of complex dietary carbohydrates, proteins, and lipids by hydrolytic enzymes in the human alimentary canal", "A sequence of irreversible chemical changes", "Purely mechanical grinding", "A reversible physical change", "Thermal dissolution"),
                ("the burning of a candle involves which simultaneous combination of changes?", "Both physical change (melting of wax) and chemical change (combustion of wax vapor to \\(CO_2\\) and \\(H_2O\\))", "Only a physical change", "Only a chemical change", "Neither physical nor chemical"),
                ("the cooking and baking of raw dough into bread inside a high-temperature oven", "An irreversible chemical change (protein denaturation, Maillard reaction, starch gelatinization)", "A reversible physical change", "Purely physical drying", "A sublimation process"),
                ("the violent bursting and luminous sparkling of festival firecrackers and fireworks", "An exothermic chemical explosion releasing light, heat, gas, and acoustic shock", "A reversible physical change", "A nuclear fusion reaction", "A crystallization process"),
                ("the blackening of freshly sliced apples, brinjals, or potatoes when left exposed to atmospheric air", "Enzymatic browning (chemical oxidation of polyphenol compounds catalyzed by polyphenol oxidase)", "Surface crystallization of sugars", "Dehydration of plant cell walls", "Bacterial fermentation")
            ],
            'tmpls': [
                "Which chemical transformation is defined as: {0}?",
                "Identify the chemical synthesis reaction: {0}.",
                "Which chemical compound coating represents: {0}?",
                "Which microbiological chemical change corresponds to: {0}?",
                "Which fundamental autotrophic biochemical process represents: {0}?",
                "Why is digestive metabolism classified as: {0}?",
                "What composite transformation occurs when: {0}?",
                "Why is culinary baking classified as: {0}?",
                "Which energetic chemical event is characterized by: {0}?",
                "Which biochemical oxidative reaction explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Identify Chemical Transformation**\\nThe statement details {item[0]}.\\n**Step 2: Chemical Bond Rearrangement**\\nChemical changes involve bond cleavage and formation, producing novel chemical compounds with distinct chemical identities and energy changes.\\n**Step 3: Verification**\\nThe correct chemical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Indicators of Chemical Reactions (Gas, Color, Precipitate, Heat)
        {
            'data': [
                ("the observation when an iron nail is immersed in a blue copper sulphate (\\(CuSO_4\\)) solution for 30 minutes", "The blue solution turns light pale green (formation of \\(FeSO_4\\)) and reddish-brown copper deposits on the iron nail", "The solution turns bright yellow", "The iron nail dissolves completely without color change", "The solution becomes boiling hot with zero color shift"),
                ("the chemical displacement reaction between iron and aqueous copper sulphate is represented by the balanced equation", "\\(Fe + CuSO_4 \\rightarrow FeSO_4 + Cu\\)", "\\(Fe + 2CuSO_4 \\rightarrow Fe(SO_4)_2 + Cu_2\\)", "\\(2Fe + 3CuSO_4 \\rightarrow Fe_2(SO_4)_3 + 3Cu\\)", "\\(Fe + Cu_2SO_4 \\rightarrow FeSO_4 + 2Cu\\)"),
                ("the observation when baking soda (sodium hydrogen carbonate, \\(NaHCO_3\\)) reacts with dilute acetic acid (vinegar)", "Brisk effervescence with evolution of colorless, odorless carbon dioxide gas (\\(CO_2\\))", "Evolution of pungent chlorine gas", "Formation of a bright yellow precipitate", "Immediate freezing of the mixture"),
                ("the chemical test used to confirm the evolution of carbon dioxide gas (\\(CO_2\\)) in a chemical reaction", "Passing the gas through freshly prepared clear limewater (\\(Ca(OH)_2\\)), which turns milky due to insoluble \\(CaCO_3\\) formation", "Bringing a burning splint which burns brighter", "Smelling a rotten egg odor", "Observing a blue flame"),
                ("the chemical equation representing the turning of limewater milky by carbon dioxide gas", "\\(Ca(OH)_2 + CO_2 \\rightarrow CaCO_3\\downarrow \\text{ (white ppt)} + H_2O\\)", "\\(CaO + CO_2 \\rightarrow CaCO_3\\)", "\\(Ca(HCO_3)_2 \\rightarrow CaCO_3 + H_2O\\)", "\\(CaCl_2 + CO_2 \\rightarrow CaCO_3 + Cl_2\\)"),
                ("a chemical reaction that releases thermal energy to its surroundings, causing the temperature of the reaction mixture to rise", "Exothermic reaction (e.g., reaction of quicklime \\(CaO\\) with water)", "Endothermic reaction", "Photochemical reaction", "Electrolytic reaction"),
                ("a chemical reaction that absorbs thermal energy from its surroundings, causing the temperature of the reaction vessel to drop", "Endothermic reaction (e.g., dissolution of ammonium chloride in water)", "Exothermic reaction", "Combustion reaction", "Neutralization reaction"),
                ("the insoluble solid substance that separates out from a liquid solution during a double displacement chemical reaction", "Precipitate (indicated by \\(\\downarrow\\))", "Filtrate", "Solute", "Supernatant"),
                ("the observation when aqueous silver nitrate (\\(AgNO_3\\)) is mixed with aqueous sodium chloride (\\(NaCl\\))", "A curd-like white precipitate of silver chloride (\\(AgCl\\downarrow\\)) forms immediately", "A brown gas is evolved", "The beaker becomes freezing cold", "A bright pink solution forms"),
                ("the brisk effervescence and popping sound observed when zinc granules react with dilute sulphuric acid", "Evolution of hydrogen gas (\\(H_2\\)), which burns with a characteristic pop sound when a burning splinter is brought near", "Evolution of oxygen gas", "Evolution of sulphur dioxide gas", "Evolution of nitrogen gas")
            ],
            'tmpls': [
                "What diagnostic chemical observation occurs when: {0}?",
                "Which balanced single displacement chemical equation represents: {0}?",
                "What visual and effervescent indicator appears when: {0}?",
                "Which analytical laboratory confirmation test is defined as: {0}?",
                "Which chemical precipitation equation represents: {0}?",
                "Which thermodynamic chemical category is defined by: {0}?",
                "Which heat-absorbing reaction classification corresponds to: {0}?",
                "What insoluble reaction product is defined as: {0}?",
                "What chemical precipitation observation occurs when: {0}?",
                "What characteristic gas evolution test confirms: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Reaction Phenomenon Context**\\nThe statement details {item[0]}.\\n**Step 2: Indicators of Chemical Change**\\nChemical changes manifest via gas evolution, color transitions, precipitate formation, or enthalpy changes (\\(\\Delta H\\)).\\n**Step 3: Verification**\\nThe matching chemical response is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Rusting of Iron, Conditions & Corrosion Prevention
        {
            'data': [
                ("the two indispensable environmental factors both strictly required for the rusting of iron to take place", "Both molecular oxygen (air) and liquid water (or moisture)", "Oxygen alone in bone-dry air", "Pure boiled water completely free of dissolved air", "Carbon dioxide gas alone"),
                ("why iron structures, ships, and vehicles rust significantly faster in coastal cities (e.g., Mumbai, Chennai) than in desert cities (e.g., Jaisalmer)", "Coastal air contains both high humidity and airborne saline salts (\\(NaCl\\)) which act as an electrolyte accelerating electrochemical corrosion", "Desert air contains higher oxygen concentrations", "Coastal temperatures are below 0°C", "Desert sand chemically protects iron"),
                ("the industrial process of coating iron or steel articles with a protective thin layer of molten zinc metal to prevent rusting", "Galvanization", "Electroplating with copper", "Anodizing", "Vulcanization"),
                ("why galvanized iron sheets do not rust even when the protective zinc coating is scratched or chipped", "Zinc is more electrochemically reactive than iron and undergoes sacrificial corrosion, protecting the underlying iron cathodically", "Zinc turns into stainless steel", "Zinc releases poisonous gas that stops oxygen", "Scratches heal by melting"),
                ("the homogeneous metallic mixture of iron with carbon, chromium, and nickel that is highly resistant to rusting", "Stainless steel (contains ~18% Cr and 8% Ni)", "Brass (copper + zinc)", "Bronze (copper + tin)", "Duralumin (aluminum alloy)"),
                ("the ancient archaeological iron structure in New Delhi that has stood exposed to weather for over 1600 years without rusting", "Iron Pillar of Delhi at Mehrauli (Chandragupta II era)", "Qutub Minar", "Ashoka Pillar at Sarnath", "Red Fort gate"),
                ("the scientific reason why the ancient Iron Pillar of Delhi exhibits such exceptional resistance to atmospheric corrosion", "High phosphorus content in wrought iron formed a protective passive amorphous layer of \\(\\text{FePO}_4\\cdot H_2O\\) (misawite)", "It was coated with modern synthetic paint", "It was kept indoors until recently", "It is made of pure silver inside"),
                ("the method of corrosion prevention that involves applying a barrier layer of grease, oil, or enamel paint on exposed metal surfaces", "Barrier protection (prevents direct physical contact of iron with moisture and atmospheric oxygen)", "Sacrificial protection", "Cathodic protection", "Alloying"),
                ("the chemical formula representing hydrated ferric oxide, the principal constituent of rust", "\\(Fe_2O_3\\cdot xH_2O\\)", "\\(FeO\\cdot xH_2O\\)", "\\(Fe_3O_4\\)", "\\(Fe(OH)_2\\)"),
                ("the technique of preventing underground iron pipelines and ship hulls from corroding by connecting them to more reactive magnesium or zinc blocks", "Cathodic (sacrificial anode) protection", "Galvanic electroplating", "Enamelling", "Tin plating")
            ],
            'tmpls': [
                "Which two essential environmental reactants are defined by: {0}?",
                "What geochemical and atmospheric reason explains why: {0}?",
                "Which metallurgical zinc-coating protection method is defined as: {0}?",
                "What electrochemical sacrificial mechanism explains why: {0}?",
                "Which corrosion-resistant alloy is described by: {0}?",
                "Which historical metallurgy monument corresponds to: {0}?",
                "What metallurgical chemical discovery explains why: {0}?",
                "Which surface barrier protection method corresponds to: {0}?",
                "Which stoichiometric chemical formula represents: {0}?",
                "Which electrochemical pipeline engineering technique represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Corrosion Chemistry Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Electrochemical Mechanism of Rusting**\\nRusting requires \\(O_2\\) and \\(H_2O\\) to form \\(Fe_2O_3\\cdot xH_2O\\); prevention relies on barrier coatings, galvanization, sacrificial anodes, or alloying with Cr/Ni.\\n**Step 3: Verification**\\nThe correct physical-chemical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Crystallization Procedure & Separation Techniques
        {
            'data': [
                ("the physical purification technique used to obtain pure solid crystals from an impure commercial sample of a soluble salt", "Crystallization", "Simple distillation", "Fractional sublimation", "Chromatography"),
                ("to prepare large, pure blue crystals of copper sulphate (\\(CuSO_4\\cdot 5H_2O\\)), one must", "Dissolve copper sulphate powder in hot boiling water containing a few drops of dilute \\(H_2SO_4\\) until no more dissolves, filter, and cool slowly undisturbed", "Boil the solution until completely dry and charred", "Add sodium hydroxide until blue precipitate settles", "Freeze the solution at -20°C instantly"),
                ("why a few drops of dilute sulphuric acid (\\(H_2SO_4\\)) are added during the preparation of copper sulphate crystals", "To prevent the hydrolysis of copper sulphate in water and obtain clear, well-formed crystals", "To accelerate evaporation of water", "To change the color of crystals to green", "To neutralize basic impurities"),
                ("why rapid cooling or vigorous stirring during crystallization is undesirable if large, well-defined crystals are desired", "Rapid cooling produces numerous microscopic imperfect crystals, whereas slow undisturbed cooling allows atoms to organize into large, pure geometric lattices", "Rapid cooling decomposes the salt chemically", "Stirring dissolves the crystals permanently", "Rapid cooling causes violent boiling"),
                ("the liquid remaining after filtering out the crystallized solid from a crystallization process", "Mother liquor", "Filtrate slurry", "Aqueous solvent", "Precipitate"),
                ("the geometric blue vitriol crystals of copper sulphate possess which chemical formula containing five molecules of water of crystallization", "\\(CuSO_4\\cdot 5H_2O\\)", "\\(CuSO_4\\cdot 2H_2O\\)", "\\(CuSO_4\\cdot 7H_2O\\)", "\\(CuSO_4\\cdot 10H_2O\\)"),
                ("the white anhydrous powder formed when blue copper sulphate crystals are strongly heated in a dry test tube", "Anhydrous copper sulphate (\\(CuSO_4\\), loses its water of crystallization)", "Copper oxide (\\(CuO\\))", "Copper metal (\\(Cu\\))", "Sulphur dioxide gas"),
                ("the physical change that occurs when a few drops of liquid water are added back onto white anhydrous copper sulphate powder", "The powder immediately turns back into its characteristic sky-blue hydrated form, releasing heat (exothermic hydration)", "The powder dissolves into a colorless gas", "The powder burns with a green flame", "The powder permanently turns black"),
                ("the fixed number of water molecules chemically bound in the crystalline structure of a hydrated salt is termed", "Water of crystallization", "Hygroscopic moisture", "Deliquescent water", "Zeolite water"),
                ("the common crystalline double salt of potassium and aluminum used in water purification and as an aftershave styptic", "Potash alum (Fitkari, \\(K_2SO_4\\cdot Al_2(SO_4)_3\\cdot 24H_2O\\))", "Epsom salt (\\(MgSO_4\\cdot 7H_2O\\))", "Washing soda (\\(Na_2CO_3\\cdot 10H_2O\\))", "Gypsum (\\(CaSO_4\\cdot 2H_2O\\))")
            ],
            'tmpls': [
                "Which physical purification technique is defined as: {0}?",
                "What experimental protocol is used to: {0}?",
                "What chemical hydrolytic rationale explains why: {0}?",
                "What thermodynamic crystal growth kinetic principle explains why: {0}?",
                "Which post-crystallization supernatant solution is termed: {0}?",
                "Which stoichiometric hydrated salt formula represents: {0}?",
                "Which dehydrated chemical compound is produced when: {0}?",
                "What reversible hydration change occurs when: {0}?",
                "Which structural crystalline chemical term is defined as: {0}?",
                "Which traditional astringent double sulphate corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Crystallization Context**\\nThe statement details {item[0]}.\\n**Step 2: Hydration and Lattice Formation**\\nCrystallization purifies salts by thermal saturation and slow cooling; hydrated salts incorporate specific stoichiometric water of crystallization.\\n**Step 3: Verification**\\nThe matching chemical entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Chemical Equations, Balancing & Stoichiometry Basics
        {
            'data': [
                ("the law formulated by Antoine Lavoisier stating that mass can neither be created nor destroyed in a chemical reaction", "Law of Conservation of Mass", "Law of Definite Proportions", "Law of Multiple Proportions", "Avogadro's Law"),
                ("why any valid chemical equation must be strictly balanced with equal numbers of each kind of atom on both reactant and product sides", "To satisfy the Law of Conservation of Mass (total mass of reactants must equal total mass of products)", "To ensure pressure remains constant", "To balance electrical resistance", "To make the reaction proceed faster"),
                ("the balanced chemical equation for the combustion of methane gas in excess oxygen", "\\(CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O\\)", "\\(CH_4 + O_2 \\rightarrow CO_2 + H_2O\\)", "\\(2CH_4 + 3O_2 \\rightarrow 2CO_2 + 2H_2O\\)", "\\(CH_4 + 4O_2 \\rightarrow CO_2 + 4H_2O\\)"),
                ("the balanced chemical equation for the formation of water from hydrogen and oxygen gases", "\\(2H_2 + O_2 \\rightarrow 2H_2O\\)", "\\(H_2 + O_2 \\rightarrow H_2O_2\\)", "\\(H_2 + O_2 \\rightarrow H_2O\\)", "\\(4H + O_2 \\rightarrow 2H_2O\\)"),
                ("the coefficients \\(x\\) and \\(y\\) that correctly balance the equation \\(x Al + y O_2 \\rightarrow 2 Al_2O_3\\)", "\\(x = 4\\) and \\(y = 3\\)", "\\(x = 2\\) and \\(y = 3\\)", "\\(x = 4\\) and \\(y = 2\\)", "\\(x = 2\\) and \\(y = 2\\)"),
                ("the reaction where a single compound breaks down into two or more simpler substances upon heating (e.g., \\(2KClO_3 \\xrightarrow{\\Delta} 2KCl + 3O_2\\))", "Thermal decomposition reaction", "Combination reaction", "Displacement reaction", "Neutralization reaction"),
                ("the reaction where two compounds exchange their ions in aqueous solution to form two new compounds (e.g., \\(BaCl_2 + Na_2SO_4 \\rightarrow BaSO_4\\downarrow + 2NaCl\\))", "Double displacement (precipitation) reaction", "Combination reaction", "Decomposition reaction", "Electrolytic reduction"),
                ("the reaction where two or more reactants combine to form a single product (e.g., \\(CaO + H_2O \\rightarrow Ca(OH)_2\\))", "Combination (synthesis) reaction", "Decomposition reaction", "Single displacement reaction", "Double displacement reaction"),
                ("the chemical reaction where oxygen is added to a substance or electrons/hydrogen are lost", "Oxidation reaction", "Reduction reaction", "Precipitation reaction", "Hydrolysis"),
                ("the chemical reaction where hydrogen or electrons are gained or oxygen is removed from a substance", "Reduction reaction", "Oxidation reaction", "Neutralization reaction", "Combustion")
            ],
            'tmpls': [
                "Which foundational chemical law is defined by: {0}?",
                "What fundamental mass stoichiometry rationale explains why: {0}?",
                "Which balanced hydrocarbon combustion equation represents: {0}?",
                "Which balanced synthesis reaction represents: {0}?",
                "What stoichiometric balancing coefficients resolve: {0}?",
                "Which chemical reaction class is defined as: {0}?",
                "Which ion-exchange reaction classification corresponds to: {0}?",
                "Which combination synthesis reaction type matches: {0}?",
                "Which redox electron/oxygen transfer definition describes: {0}?",
                "Which complementary redox definition corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chemical Reaction Context**\\nThe statement details {item[0]}.\\n**Step 2: Stoichiometric Balancing Analysis**\\nMass conservation mandates atom counts remain invariant: Reactants = Products. Balancing determines integer molar ratios.\\n**Step 3: Verification**\\nThe correct chemical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Everyday Physical vs Chemical Scenarios & Critical Comparisons
        {
            'data': [
                ("making of butter by churning milk or curd in a traditional butter churn", "Physical change (separation of fat globules by centrifugal force without altering fat molecules)", "Chemical fermentation", "Oxidation of lactose", "Thermal decomposition"),
                ("burning of Liquefied Petroleum Gas (LPG) in a domestic kitchen gas stove burner", "Chemical change (combustion of propane/butane releasing carbon dioxide, water vapor, and heat)", "Physical change of state only", "Sublimation of fuel", "Reversible vaporization"),
                ("ripening of a green mango on a tree turning yellow, sweet, and soft", "Chemical change (breakdown of starches into sugars, degradation of chlorophyll, and synthesis of carotenoids/esters)", "Physical change of shape only", "Reversible drying", "Mechanical ripening"),
                ("formation of clouds, rainfall, and snow in the global water cycle", "Physical changes of state (evaporation, condensation, freezing)", "Chemical combination of hydrogen and oxygen", "Photosynthetic reactions", "Acid-base neutralizations"),
                ("electrolysis of water using electric current breaking water molecules into hydrogen and oxygen gases (\\(2H_2O \\rightarrow 2H_2 + O_2\\))", "Chemical change (electrolytic decomposition breaking covalent chemical bonds)", "Physical boiling of water", "Dissolution of water", "Physical phase transition"),
                ("dissolution of quicklime (calcium oxide, \\(CaO\\)) in water with hissing sound releasing tremendous heat and boiling water", "Chemical change (exothermic combination forming calcium hydroxide, \\(Ca(OH)_2\\))", "Physical dissolution", "Endothermic sublimation", "Mechanical suspension"),
                ("drying of wet laundry clothes hanging on a clothesline on a sunny day", "Physical change (evaporation of water into ambient air)", "Chemical oxidation of fabric", "Photochemical decomposition of dye", "Enzymatic hydrolysis"),
                ("fermentation of grape juice into wine by yeast producing ethanol and carbon dioxide", "Chemical change (enzymatic anaerobic fermentation by zymase)", "Physical settling of sediment", "Fractional distillation", "Reversible cooling"),
                ("magnetization of an iron needle by stroking it repeatedly with a permanent bar magnet in one direction", "Physical change (alignment of microscopic magnetic domains without forming any new chemical substance)", "Chemical oxidation of iron", "Nuclear fusion of iron", "Thermal ionization"),
                ("cooking an egg in boiling water causing the liquid egg white (albumin) to turn into an opaque firm white solid", "Chemical change (heat denatures and irreversibly coagulates globular protein chains)", "Physical freezing of albumin", "Sublimation of yolk", "Evaporation of egg proteins")
            ],
            'tmpls': [
                "Classify the culinary mechanical operation: {0}",
                "Classify the household gas combustion event: {0}",
                "Identify the botanical fruit development change: {0}",
                "Classify the atmospheric hydrological phenomenon: {0}",
                "Classify the electrochemical water decomposition: {0}",
                "Classify the hydration reaction of quicklime: {0}",
                "Classify the laundry moisture loss process: {0}",
                "Classify the biochemical winemaking process: {0}",
                "Classify the electromagnetic domain alignment: {0}",
                "Classify the culinary thermal protein coagulation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Scenario Analysis**\\nThe prompt describes {item[0]}.\\n**Step 2: Bonding and Reversibility Analysis**\\nIf chemical composition and bonds change irreversibly, it is a chemical change; if molecular identity is preserved, it is a physical change.\\n**Step 3: Verification**\\nThe matching classification is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Quantitative Problems in Mass Conservation & Chemical Proportions
        {
            'data': [
                ("In a chemical reaction, \\(10.0\\text{ g}\\) of calcium carbonate (\\(CaCO_3\\)) is heated completely, producing \\(5.6\\text{ g}\\) of solid calcium oxide (\\(CaO\\)). According to the Law of Conservation of Mass, what mass of carbon dioxide (\\(CO_2\\)) gas was evolved?", "\\(4.4\\text{ g } (10.0\\text{ g} - 5.6\\text{ g} = 4.4\\text{ g})\\)", "\\(5.6\\text{ g}\\)", "\\(15.6\\text{ g}\\)", "\\(2.2\\text{ g}\\)"),
                ("When \\(12.0\\text{ g}\\) of carbon burns completely in \\(32.0\\text{ g}\\) of oxygen, calculate the total mass of carbon dioxide (\\(CO_2\\)) produced.", "\\(44.0\\text{ g } (12.0\\text{ g} + 32.0\\text{ g} = 44.0\\text{ g})\\)", "\\(20.0\\text{ g}\\)", "\\(48.0\\text{ g}\\)", "\\(36.0\\text{ g}\\)"),
                ("In water (\\(H_2O\\)), hydrogen and oxygen combine in a fixed mass ratio of \\(1 : 8\\). What mass of oxygen gas is required to react completely with \\(3.0\\text{ g}\\) of hydrogen gas?", "\\(24.0\\text{ g of } O_2\\)", "\\(16.0\\text{ g of } O_2\\)", "\\(8.0\\text{ g of } O_2\\)", "\\(32.0\\text{ g of } O_2\\)"),
                ("When \\(4.0\\text{ g}\\) of hydrogen gas reacts completely with \\(32.0\\text{ g}\\) of oxygen gas, calculate the total mass of water (\\(H_2O\\)) formed.", "\\(36.0\\text{ g of water}\\)", "\\(28.0\\text{ g}\\)", "\\(18.0\\text{ g}\\)", "\\(64.0\\text{ g}\\)"),
                ("An iron nail weighing \\(10.0\\text{ g}\\) undergoes complete rusting by absorbing \\(4.3\\text{ g}\\) of oxygen and water from moist air. What is the final mass of the rusted nail?", "\\(14.3\\text{ g } (10.0\\text{ g} + 4.3\\text{ g})\\)", "\\(5.7\\text{ g}\\)", "\\(10.0\\text{ g}\\)", "\\(20.0\\text{ g}\\)"),
                ("Calculate the molecular mass of water (\\(H_2O\\)) taking atomic mass of \\(H = 1\\text{ u}\\) and \\(O = 16\\text{ u}\\).", "\\(18\\text{ u } (2 \\times 1 + 16 = 18\\text{ u})\\)", "\\(17\\text{ u}\\)", "\\(34\\text{ u}\\)", "\\(16\\text{ u}\\)"),
                ("Calculate the molecular mass of carbon dioxide (\\(CO_2\\)) taking atomic mass of \\(C = 12\\text{ u}\\) and \\(O = 16\\text{ u}\\).", "\\(44\\text{ u } (12 + 2 \\times 16 = 44\\text{ u})\\)", "\\(28\\text{ u}\\)", "\\(32\\text{ u}\\)", "\\(40\\text{ u}\\)"),
                ("Calculate the percentage by mass of oxygen in carbon dioxide (\\(CO_2\\), molecular mass \\(44\\text{ u}\\)).", "\\(72.73\\% \\text{ (approx } 73\\%\\))", "\\(50.0\\%\\)", "\\(27.27\\%\\)", "\\(36.36\\%\\)"),
                ("Calculate the formula unit mass of calcium oxide (\\(CaO\\)) taking \\(Ca = 40\\text{ u}\\) and \\(O = 16\\text{ u}\\).", "\\(56\\text{ u } (40 + 16 = 56\\text{ u})\\)", "\\(40\\text{ u}\\)", "\\(48\\text{ u}\\)", "\\(72\\text{ u}\\)"),
                ("In a double displacement reaction, \\(5.85\\text{ g}\\) of \\(NaCl\\) reacts with \\(17.0\\text{ g}\\) of \\(AgNO_3\\) to produce \\(14.35\\text{ g}\\) of \\(AgCl\\downarrow\\) precipitate. Calculate the mass of sodium nitrate (\\(NaNO_3\\)) formed in the solution.", "\\(8.5\\text{ g } (5.85 + 17.0 - 14.35 = 8.50\\text{ g})\\)", "\\(11.15\\text{ g}\\)", "\\(14.35\\text{ g}\\)", "\\(6.25\\text{ g}\\)")
            ],
            'tmpls': [
                "Calculate gas mass released using mass conservation: {0}",
                "Evaluate total product mass formed: {0}",
                "Determine stoichiometric oxygen mass needed: {0}",
                "Calculate total mass of synthesized water: {0}",
                "Compute final mass of corroded iron article: {0}",
                "Calculate molecular mass of water: {0}",
                "Calculate molecular mass of carbon dioxide: {0}",
                "Determine mass percentage composition: {0}",
                "Compute formula unit mass of calcium oxide: {0}",
                "Calculate residual salt mass from double displacement: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract reactant and product masses or atomic masses from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply Law of Conservation of Mass (\\(\\Sigma m_{{\\text{{reactants}}}} = \\Sigma m_{{\\text{{products}}}}\\)) or molecular mass summation \\(\\Sigma A_r\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_19_3_2():
    tc = "MH-9-SCIT-19-19.3.2"
    tname = "Elements, compounds & molecular formulae basics"
    archs = [
        # Arch 0: Definition of Elements, Metals, Non-metals & Metalloids
        {
            'data': [
                ("a pure chemical substance composed of only one type of atom that cannot be broken down into simpler substances by ordinary chemical means", "Element", "Compound", "Mixture", "Solution"),
                ("elements that are generally malleable, ductile, lustrous, sonorous, and excellent conductors of heat and electricity", "Metals (e.g., iron, copper, aluminum, gold)", "Non-metals", "Metalloids", "Noble gases"),
                ("elements that are brittle, non-ductile, non-lustrous, and poor conductors of heat and electricity (with a few exceptions)", "Non-metals (e.g., sulphur, carbon, oxygen, nitrogen)", "Metals", "Alloys", "Superconductors"),
                ("elements whose physical and chemical properties are intermediate between those of typical metals and non-metals", "Metalloids (Semi-metals: silicon, germanium, arsenic, antimony, tellurium)", "Noble gases", "Transition metals", "Alkali metals"),
                ("the only metal that exists as a liquid at standard room temperature (\\(25^\\circ\\text{C}\\))", "Mercury (\\(Hg\\))", "Bromine (\\(Br\\))", "Gallium (\\(Ga\\))", "Sodium (\\(Na\\))"),
                ("the only non-metal that exists as a liquid at standard room temperature", "Bromine (\\(Br_2\\))", "Mercury (\\(Hg\\))", "Chlorine (\\(Cl_2\\))", "Iodine (\\(I_2\\))"),
                ("the non-metal allotrope of carbon that is an exceptional conductor of electricity due to free delocalized electrons in hexagonal layers", "Graphite", "Diamond", "Fullerene (C-60)", "Charcoal"),
                ("the hardest naturally occurring substance known, which is a crystalline allotrope of non-metallic carbon", "Diamond", "Quartz", "Topaz", "Corundum"),
                ("the lustrous, purple-black non-metallic halogen element that sublimes into dense violet vapors", "Iodine (\\(I_2\\))", "Sulphur", "Phosphorus", "Carbon"),
                ("the soft alkali metals that can be sliced easily with a kitchen knife and must be stored submerged under kerosene oil due to extreme reactivity", "Sodium (\\(Na\\)) and Potassium (\\(K\\))", "Iron and Copper", "Gold and Platinum", "Magnesium and Aluminum")
            ],
            'tmpls': [
                "Which fundamental chemical classification is defined as: {0}?",
                "Which elemental material class represents: {0}?",
                "Which chemical elemental category corresponds to: {0}?",
                "Which intermediate elemental class is defined by: {0}?",
                "Identify the unique liquid metallic element: {0}.",
                "Identify the unique liquid non-metallic element: {0}.",
                "Which conductive carbon allotrope represents: {0}?",
                "Which supreme natural abrasive allotrope corresponds to: {0}?",
                "Which lustrous sublimating non-metal represents: {0}?",
                "Which pyrophoric soft alkali metals are described by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Elemental Classification Context**\\nThe statement details {item[0]}.\\n**Step 2: Periodic Properties and Allotropy**\\nElements are divided into metals, non-metals, and metalloids based on luster, conductivity, state, and bonding characteristics.\\n**Step 3: Verification**\\nThe matching chemical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Chemical Symbols (Berzelius System & Latin Origins)
        {
            'data': [
                ("the Swedish chemist who introduced the modern system of using chemical letter symbols based on the first one or two letters of element names", "Jöns Jacob Berzelius (in 1814)", "Antoine Lavoisier", "John Dalton", "Dmitri Mendeleev"),
                ("the chemical symbol 'Fe' for iron is derived from its classical Latin name", "Ferrum", "Ferricus", "Fluor", "Francium"),
                ("the chemical symbol 'Na' for sodium is derived from its classical Latin name", "Natrium", "Niter", "Nitrogenium", "Neptunium"),
                ("the chemical symbol 'K' for potassium is derived from its classical Neo-Latin/Germanic name", "Kalium", "Krypton", "Kali", "Kelvinium"),
                ("the chemical symbol 'Cu' for copper is derived from its Latin name", "Cuprum (from the island of Cyprus)", "Cuprous", "Cobaltum", "Curium"),
                ("the chemical symbol 'Ag' for silver is derived from its classical Latin name", "Argentum", "Aurum", "Astatine", "Antimonium"),
                ("the chemical symbol 'Au' for gold is derived from its classical Latin name", "Aurum (meaning 'shining dawn')", "Argentum", "Aluminium", "Arsenicum"),
                ("the chemical symbol 'Pb' for lead is derived from its Latin name", "Plumbum", "Palladium", "Platinum", "Phosphorus"),
                ("the chemical symbol 'Hg' for mercury is derived from its classical Greek/Latin name meaning 'liquid silver' (water-silver)", "Hydrargyrum", "Helium", "Hydrogenium", "Holmium"),
                ("the chemical symbol 'W' for tungsten is derived from its German mineral name", "Wolfram (from wolframite mineral)", "Wernerite", "Willemite", "Wurtzite")
            ],
            'tmpls': [
                "Name the pioneering Swedish chemist who established: {0}.",
                "Which classical Latin root gives the symbol for: {0}?",
                "Which historical etymological name gives the symbol for: {0}?",
                "Which historical Latin root provides the symbol for: {0}?",
                "Identify the Latin mineral root corresponding to: {0}.",
                "Which classical Latin name gives the symbol for: {0}?",
                "Which ancient Latin name defines the symbol for: {0}?",
                "Which classical Latin word provides the symbol for: {0}?",
                "Which classical Greek/Latin root gives the symbol for: {0}?",
                "Which German mineralogical name provides the symbol for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chemical Nomenclature Context**\\nThe question targets {item[0]}.\\n**Step 2: Etymological and Berzelius Standards**\\nSymbols use one capital letter or one capital and one lowercase letter derived from English or classical Latin/German names.\\n**Step 3: Verification**\\nThe correct scientific symbol origin is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Molecules, Atomicity & Noble Gases
        {
            'data': [
                ("the number of atoms present in a single molecule of an element or compound is defined as its", "Atomicity", "Valency", "Atomic mass", "Isotope number"),
                ("elements that exist as independent single individual atoms with an atomicity of 1, such as helium, neon, argon, and krypton", "Monoatomic elements (Noble gases)", "Diatomic molecules", "Polyatomic networks", "Triatomic elements"),
                ("molecules composed of exactly two atoms chemically bonded together, such as \\(H_2, O_2, N_2, Cl_2, HCl\\)", "Diatomic molecules (atomicity = 2)", "Monoatomic molecules", "Triatomic molecules", "Tetraatomic molecules"),
                ("the triatomic allotrope of oxygen whose molecule contains three chemically bonded oxygen atoms (\\(O_3\\))", "Ozone (atomicity = 3)", "Diatomic dioxygen", "Nascent oxygen", "Hydrogen peroxide"),
                ("the solid non-metal element whose molecule exists as a tetrahedral cluster of four atoms (\\(P_4\\))", "Phosphorus (white phosphorus, atomicity = 4)", "Sulphur", "Carbon", "Silicon"),
                ("the solid non-metal element whose common yellow crystalline crown-shaped molecules contain eight atoms (\\(S_8\\))", "Sulphur (octa-atomic, atomicity = 8)", "Phosphorus", "Selenium", "Boron"),
                ("the group of chemically unreactive elements in Group 18 of the periodic table having completely filled valence electron shells", "Noble gases (Inert gases)", "Halogens", "Alkali metals", "Alkaline earth metals"),
                ("the smallest particle of a substance (element or compound) that has the capability of an independent existence while preserving all chemical properties", "Molecule", "Atom", "Ion", "Proton"),
                ("the smallest indivisible unit of an element that takes part in a chemical reaction", "Atom (John Dalton's atomic concept)", "Molecule", "Crystal", "Compound"),
                ("a molecule composed of atoms of two or more different chemical elements combined in a fixed ratio, such as \\(CO_2\\) or \\(H_2O\\)", "Molecule of a compound (Heteroatomic molecule)", "Molecule of an element (Homoatomic)", "Monoatomic ion", "Polyatomic radical")
            ],
            'tmpls': [
                "Which fundamental structural chemical parameter is defined as: {0}?",
                "Which category of inert gases is characterized by: {0}?",
                "Which molecular category represents: {0}?",
                "Identify the protective triatomic allotrope: {0}.",
                "Which tetra-atomic non-metallic element corresponds to: {0}?",
                "Which octa-atomic molecular crystal represents: {0}?",
                "Which noble periodic chemical group matches: {0}?",
                "Which chemical particle entity is defined as: {0}?",
                "Which foundational atomic entity represents: {0}?",
                "Which molecular chemical class is defined by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Molecular Architecture Context**\\nThe statement details {item[0]}.\\n**Step 2: Atomicity Analysis**\\nAtomicity is the number of atoms in a molecule: monoatomic (\\(He\\)), diatomic (\\(O_2\\)), triatomic (\\(O_3\\)), tetra-atomic (\\(P_4\\)), polyatomic (\\(S_8\\)).\\n**Step 3: Verification**\\nThe matching chemical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Compounds vs Mixtures & Law of Constant Proportions
        {
            'data': [
                ("a substance formed when two or more chemical elements combine chemically in a fixed, definite proportion by mass", "Compound", "Mixture", "Solution", "Colloid"),
                ("the fundamental law of chemical combination formulated by Joseph Proust in 1799 stating that in a chemical substance, elements are always present in definite proportions by mass", "Law of Constant (Definite) Proportions", "Law of Conservation of Mass", "Law of Multiple Proportions", "Gay-Lussac's Law"),
                ("why water (\\(H_2O\\)) is classified as a chemical compound rather than a physical mixture of hydrogen and oxygen gases", "Its constituent elements are chemically bonded in a fixed 1:8 mass ratio, and water exhibits properties totally unlike explosive hydrogen and oxidizing oxygen", "Water is a liquid", "Water can be separated by a simple paper filter", "Water contains air"),
                ("a combination of two or more substances in any arbitrary proportion where the constituent substances retain their individual chemical properties", "Mixture", "Compound", "Pure element", "Molecule"),
                ("when iron filings and sulphur powder are merely ground together at room temperature without heating, the resulting substance is", "A heterogeneous mixture (iron can be separated using a magnet and sulphur by dissolving in \\(CS_2\\))", "A chemical compound (ferrous sulphide)", "An alloy", "A homogeneous solution"),
                ("when the mixture of iron filings and sulphur powder is heated strongly in a test tube to red heat, a vigorous exothermic reaction produces", "A black chemical compound: Ferrous sulphide (\\(FeS\\)), from which iron cannot be extracted with a magnet", "A physical solution", "Pure molten iron", "A mixture of \\(Fe\\) and \\(S\\)"),
                ("a mixture whose components are completely blended with uniform composition and properties throughout (e.g., sugar syrup, air, brass)", "Homogeneous mixture (Solution)", "Heterogeneous mixture", "Suspension", "Colloid"),
                ("a mixture whose components remain physically separated with non-uniform composition and visible boundaries (e.g., oil and water, chalk in water, muddy water)", "Heterogeneous mixture", "Homogeneous mixture", "Pure compound", "True solution"),
                ("the property of constituent elements in a chemical compound compared to their original elemental states", "Properties of a compound are entirely new and completely different from those of its constituent elements", "Properties are the simple mathematical average of its elements", "Elements retain their original properties identically", "Compounds are always gases"),
                ("the mass ratio of carbon to oxygen in pure carbon dioxide (\\(CO_2\\)) irrespective of the method of preparation", "\\(3 : 8\\) by mass (\\(12\\text{ g } C : 32\\text{ g } O\\))", "\\(1 : 2\\) by mass", "\\(3 : 4\\) by mass", "\\(1 : 1\\) by mass")
            ],
            'tmpls': [
                "Which chemical substance category is defined as: {0}?",
                "Which foundational law of chemical stoichiometry represents: {0}?",
                "What chemical bonding and property rationale explains why: {0}?",
                "Which arbitrary composition category corresponds to: {0}?",
                "What physical separation behavior characterizes: {0}?",
                "What chemical compound synthesis occurs when: {0}?",
                "Which uniform composition category is defined as: {0}?",
                "Which non-uniform phase mixture is defined by: {0}?",
                "What fundamental property rule distinguishes: {0}?",
                "What fixed stoichiometric mass ratio defines: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chemical Substance Context**\\nThe query highlights {item[0]}.\\n**Step 2: Compounds vs Mixtures**\\nCompounds form via chemical reactions with fixed mass ratios (Proust's Law) and novel properties; mixtures have variable composition and retain constituent properties.\\n**Step 3: Verification**\\nThe correct chemical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Valency & Radicals (Cations, Anions, Polyatomic Ions)
        {
            'data': [
                ("the combining capacity of an element or atom, measured by the number of hydrogen or chlorine atoms with which one atom of the element combines", "Valency", "Atomic number", "Mass number", "Atomic radius"),
                ("a positively charged ion formed when a neutral atom loses one or more valence electrons, such as \\(Na^+, Ca^{2+}, Al^{3+}\\)", "Cation", "Anion", "Polyatomic radical", "Neutron"),
                ("a negatively charged ion formed when a neutral atom gains one or more electrons, such as \\(Cl^-, O^{2-}, N^{3-}\\)", "Anion", "Cation", "Positron", "Proton"),
                ("a group of tightly bonded atoms carrying a net positive or negative electric charge that behaves as a single unit in chemical reactions", "Polyatomic ion (Radical)", "Molecule of an element", "Noble gas cluster", "Neutral atom"),
                ("the valency and chemical formula of the ammonium polyatomic cation", "\\(+1\\) and formula \\(NH_4^+\\)", "\\(+2\\) and formula \\(NH_3^{2+}\\)", "\\(-1\\) and formula \\(NH_2^-\\)", "\\(+3\\) and formula \\(NH_4^{3+}\\)"),
                ("the valency and chemical formula of the sulphate polyatomic anion", "\\(-2\\) (divalent) and formula \\(SO_4^{2-}\\)", "\\(-1\\) and formula \\(SO_3^-\\)", "\\(-3\\) and formula \\(SO_4^{3-}\\)", "\\(+2\\) and formula \\(SO_4^{2+}\\)"),
                ("the valency and chemical formula of the nitrate polyatomic anion", "\\(-1\\) (monovalent) and formula \\(NO_3^-\\)", "\\(-2\\) and formula \\(NO_2^{2-}\\)", "\\(-3\\) and formula \\(NO_3^{3-}\\)", "\\(+1\\) and formula \\(NO_3^+\\)"),
                ("the valency and chemical formula of the carbonate polyatomic anion", "\\(-2\\) (divalent) and formula \\(CO_3^{2-}\\)", "\\(-1\\) and formula \\(HCO_3^-\\)", "\\(-3\\) and formula \\(CO_3^{3-}\\)", "\\(-4\\) and formula \\(CO_4^{4-}\\)"),
                ("the valency and chemical formula of the hydroxide polyatomic anion", "\\(-1\\) (monovalent) and formula \\(OH^-\\)", "\\(-2\\) and formula \\(OH^{2-}\\)", "\\(+1\\) and formula \\(OH^+\\)", "\\(-3\\) and formula \\(O_2H^{3-}\\)"),
                ("the valency and chemical formula of the phosphate polyatomic anion", "\\(-3\\) (trivalent) and formula \\(PO_4^{3-}\\)", "\\(-2\\) and formula \\(PO_4^{2-}\\)", "\\(-1\\) and formula \\(PO_3^-\\)", "\\(-4\\) and formula \\(PO_4^{4-}\\)")
            ],
            'tmpls': [
                "Which combining capacity metric is defined as: {0}?",
                "Which positive ionic species represents: {0}?",
                "Which negative ionic species corresponds to: {0}?",
                "Which charged atomic group is defined as: {0}?",
                "What is the valency and formula for: {0}?",
                "What is the charge and formula for: {0}?",
                "Identify the ionic charge and formula for: {0}?",
                "What is the chemical charge and formula for: {0}?",
                "Identify the chemical notation for: {0}?",
                "What are the ionic parameters for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Ionic and Valency Identification**\\nThe question targets {item[0]}.\\n**Step 2: Electron Configuration and Charge**\\nCations lose electrons (positive charge); anions gain electrons (negative charge); polyatomic ions carry net charge across bonded groups.\\n**Step 3: Verification**\\nThe matching chemical notation is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Chemical Formula Writing via Criss-Cross Method
        {
            'data': [
                ("Write the chemical formula for aluminium oxide formed by combining aluminium cations (\\(Al^{3+}\\)) and oxide anions (\\(O^{2-}\\)) using the criss-cross valency method.", "\\(Al_2O_3\\)", "\\(AlO\\)", "\\(Al_3O_2\\)", "\\(AlO_3\\)"),
                ("Write the chemical formula for calcium carbonate formed by combining calcium cations (\\(Ca^{2+}\\)) and carbonate anions (\\(CO_3^{2-}\\)).", "\\(CaCO_3\\)", "\\(Ca_2(CO_3)_2\\)", "\\(Ca(CO_3)_2\\)", "\\(Ca_2CO_3\\)"),
                ("Write the chemical formula for magnesium chloride formed by combining magnesium cations (\\(Mg^{2+}\\)) and chloride anions (\\(Cl^-\\)).", "\\(MgCl_2\\)", "\\(Mg_2Cl\\)", "\\(MgCl\\)", "\\(Mg_2Cl_3\\)"),
                ("Write the chemical formula for sodium sulphate formed by combining sodium cations (\\(Na^+\\)) and sulphate anions (\\(SO_4^{2-}\\)).", "\\(Na_2SO_4\\)", "\\(NaSO_4\\)", "\\(Na(SO_4)_2\\)", "\\(Na_2(SO_4)_3\\)"),
                ("Write the chemical formula for ammonium sulphate formed by combining ammonium cations (\\(NH_4^+\\)) and sulphate anions (\\(SO_4^{2-}\\)).", "\\((NH_4)_2SO_4\\)", "\\(NH_4SO_4\\)", "\\(NH_4(SO_4)_2\\)", "\\((NH_4)_3SO_4\\)"),
                ("Write the chemical formula for calcium hydroxide (slaked lime) formed from calcium (\\(Ca^{2+}\\)) and hydroxide (\\(OH^-\\)).", "\\(Ca(OH)_2\\)", "\\(CaOH\\)", "\\(Ca_2OH\\)", "\\(Ca(OH)_3\\)"),
                ("Write the chemical formula for iron(III) chloride (ferric chloride) formed from \\(Fe^{3+}\\) and \\(Cl^-\\).", "\\(FeCl_3\\)", "\\(FeCl_2\\)", "\\(Fe_3Cl\\)", "\\(FeCl\\)"),
                ("Write the chemical formula for copper(II) nitrate formed from cupric cations (\\(Cu^{2+}\\)) and nitrate anions (\\(NO_3^-\\)).", "\\(Cu(NO_3)_2\\)", "\\(CuNO_3\\)", "\\(Cu_2NO_3\\)", "\\(Cu(NO_2)_2\\)"),
                ("Write the chemical formula for zinc phosphate formed from zinc cations (\\(Zn^{2+}\\)) and phosphate anions (\\(PO_4^{3-}\\)).", "\\(Zn_3(PO_4)_2\\)", "\\(ZnPO_4\\)", "\\(Zn_2(PO_4)_3\\)", "\\(Zn(PO_4)_2\\)"),
                ("Write the chemical formula for aluminium sulphate formed from aluminium cations (\\(Al^{3+}\\)) and sulphate anions (\\(SO_4^{2-}\\)).", "\\(Al_2(SO_4)_3\\)", "\\(AlSO_4\\)", "\\(Al_3(SO_4)_2\\)", "\\(Al_2SO_4\\)")
            ],
            'tmpls': [
                "Formulate the stoichiometric compound notation for: {0}",
                "Determine the balanced empirical formula for: {0}",
                "Apply criss-cross valency rules to write: {0}",
                "Write the correct chemical formula for: {0}",
                "Determine the ionic salt formula for: {0}",
                "Formulate the hydroxide compound notation for: {0}",
                "Write the correct ferric halide formula for: {0}",
                "Determine the nitrate compound formula for: {0}",
                "Formulate the phosphate salt formula for: {0}",
                "Apply criss-cross valencies to determine: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula Formulation Rules**\\nIdentify constituent ions and charges from the problem: {item[0]}.\\n**Step 2: Criss-Cross Method**\\nTranspose numerical valencies to subscripts and simplify to lowest whole-number ratios.\\n**Step 3: Verification**\\nThe resulting chemical formula is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Variable Valency & Transition Elements
        {
            'data': [
                ("the phenomenon where a single chemical element exhibits more than one valency in different chemical compounds", "Variable valency", "Allotropy", "Isomerism", "Isotopy"),
                ("iron exhibits variable valency of +2 and +3; the lower valency (+2) in \\(FeCl_2\\) and higher valency (+3) in \\(FeCl_3\\) are traditionally designated by which suffix endings?", "'-ous' for lower valency (Ferrous, \\(Fe^{2+}\\)) and '-ic' for higher valency (Ferric, \\(Fe^{3+}\\))", "'-ic' for lower and '-ous' for higher", "'-ide' and '-ate'", "'-ite' and '-ate'"),
                ("copper exhibits variable valency of +1 and +2; the compound \\(Cu_2O\\) is named", "Cuprous oxide (Copper(I) oxide)", "Cupric oxide (Copper(II) oxide)", "Copper dioxide", "Copper trioxide"),
                ("copper compound \\(CuO\\) where copper exhibits a valency of +2 is systematically named", "Cupric oxide (Copper(II) oxide)", "Cuprous oxide (Copper(I) oxide)", "Copper monate", "Copper peroxide"),
                ("mercury exhibits variable valency of +1 and +2; \\(Hg_2Cl_2\\) (calomel) and \\(HgCl_2\\) (corrosive sublimate) are respectively named", "Mercurous chloride (Mercury(I)) and Mercuric chloride (Mercury(II))", "Mercuric and Mercurous chloride", "Mercury chloride and Mercury dichloride", "Mercury chlorate"),
                ("tin (\\(Sn\\)) exhibits variable valency of +2 and +4; the chemical formula for stannic chloride is", "\\(SnCl_4\\) (Tin(IV) chloride)", "\\(SnCl_2\\)", "\\(Sn_2Cl\\)", "\\(SnCl_3\\)"),
                ("lead (\\(Pb\\)) exhibits variable valency of +2 and +4; the chemical formula for plumbous chloride is", "\\(PbCl_2\\) (Lead(II) chloride)", "\\(PbCl_4\\)", "\\(Pb_2Cl\\)", "\\(PbCl_3\\)"),
                ("phosphorus exhibits variable valencies of 3 and 5; the two binary chlorides formed by phosphorus are", "Phosphorus trichloride (\\(PCl_3\\)) and Phosphorus pentachloride (\\(PCl_5\\))", "\\(PCl\\) and \\(PCl_2\\)", "\\(PCl_4\\) and \\(PCl_6\\)", "\\(P_2Cl_3\\) and \\(P_3Cl_5\\)"),
                ("sulphur exhibits variable valencies of 2, 4, and 6; in hydrogen sulphide (\\(H_2S\\)) and sulphur trioxide (\\(SO_3\\)), sulphur displays valencies of", "2 in \\(H_2S\\) and 6 in \\(SO_3\\)", "4 in \\(H_2S\\) and 2 in \\(SO_3\\)", "1 in \\(H_2S\\) and 3 in \\(SO_3\\)", "6 in both compounds"),
                ("why transition metals exhibit variable valency in chemical bonding", "Electrons from both outermost valence shell and penultimate inner \\(d\\)-subshell can participate in bond formation", "They have variable numbers of protons", "Their atomic nuclei split easily", "They absorb radioactive neutrons")
            ],
            'tmpls': [
                "Which chemical valency property is defined as: {0}?",
                "Which classical nomenclature suffix convention applies to: {0}?",
                "Determine the systematic chemical naming for: {0}?",
                "Identify the oxidation state nomenclature for: {0}?",
                "Which mercury halide naming convention matches: {0}?",
                "Formulate the tetravalent halide notation for: {0}?",
                "Formulate the divalent lead compound formula for: {0}?",
                "Which dual phosphorus chlorides correspond to: {0}?",
                "What specific numerical valencies apply to: {0}?",
                "What subshell electronic configuration rationale explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Variable Valency Context**\\nThe statement details {item[0]}.\\n**Step 2: Oxidation States and Subshell Participation**\\nTransition elements can lose outer \\(s\\)-electrons and variable inner \\(d\\)-electrons, leading to multiple stable valencies ('-ous' and '-ic').\\n**Step 3: Verification**\\nThe matching chemical concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Molecular Mass & Mass Percentage
        {
            'data': [
                ("Calculate the molecular mass of glucose (\\(C_6H_{12}O_6\\)) taking atomic masses: \\(C = 12\\text{ u}\\), \\(H = 1\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(180\\text{ u } (6 \\times 12 + 12 \\times 1 + 6 \\times 16 = 180\\text{ u})\\)", "\\(172\\text{ u}\\)", "\\(196\\text{ u}\\)", "\\(160\\text{ u}\\)"),
                ("Calculate the molecular mass of cane sugar (sucrose, \\(C_{12}H_{22}O_{11}\\)) taking \\(C = 12\\text{ u}\\), \\(H = 1\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(342\\text{ u } (12 \\times 12 + 22 \\times 1 + 11 \\times 16 = 342\\text{ u})\\)", "\\(360\\text{ u}\\)", "\\(310\\text{ u}\\)", "\\(324\\text{ u}\\)"),
                ("Calculate the formula unit mass of sodium chloride (\\(NaCl\\)) taking \\(Na = 23\\text{ u}\\) and \\(Cl = 35.5\\text{ u}\\).", "\\(58.5\\text{ u}\\)", "\\(50.0\\text{ u}\\)", "\\(65.5\\text{ u}\\)", "\\(46.0\\text{ u}\\)"),
                ("Calculate the formula unit mass of calcium carbonate (\\(CaCO_3\\)) taking \\(Ca = 40\\text{ u}\\), \\(C = 12\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(100\\text{ u } (40 + 12 + 3 \\times 16 = 100\\text{ u})\\)", "\\(90\\text{ u}\\)", "\\(112\\text{ u}\\)", "\\(84\\text{ u}\\)"),
                ("Calculate the formula unit mass of sulphuric acid (\\(H_2SO_4\\)) taking \\(H = 1\\text{ u}\\), \\(S = 32\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(98\\text{ u } (2 \\times 1 + 32 + 4 \\times 16 = 98\\text{ u})\\)", "\\(96\\text{ u}\\)", "\\(100\\text{ u}\\)", "\\(82\\text{ u}\\)"),
                ("Calculate the percentage by mass of nitrogen in urea (\\(NH_2CONH_2\\), molecular mass \\(60\\text{ u}\\)) taking \\(N = 14\\text{ u}\\).", "\\(46.67\\% \\text{ (approx } 46.7\\%\\))", "\\(28.0\\%\\)", "\\(35.0\\%\\)", "\\(52.5\\%\\)"),
                ("Calculate the percentage by mass of calcium in calcium carbonate (\\(CaCO_3\\), formula mass \\(100\\text{ u}\\)).", "\\(40.0\\%\\)", "\\(20.0\\%\\)", "\\(48.0\\%\\)", "\\(12.0\\%\\)"),
                ("Calculate the molecular mass of nitric acid (\\(HNO_3\\)) taking \\(H = 1\\text{ u}\\), \\(N = 14\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(63\\text{ u } (1 + 14 + 3 \\times 16 = 63\\text{ u})\\)", "\\(65\\text{ u}\\)", "\\(58\\text{ u}\\)", "\\(72\\text{ u}\\)"),
                ("Calculate the formula unit mass of hydrated copper sulphate (\\(CuSO_4\\cdot 5H_2O\\)) taking \\(Cu = 63.5\\text{ u}\\), \\(S = 32\\text{ u}\\), \\(O = 16\\text{ u}\\), \\(H = 1\\text{ u}\\).", "\\(249.5\\text{ u } (159.5 + 5 \\times 18 = 249.5\\text{ u})\\)", "\\(159.5\\text{ u}\\)", "\\(231.5\\text{ u}\\)", "\\(280.0\\text{ u}\\)"),
                ("Calculate the percentage by mass of water of crystallization in hydrated copper sulphate (\\(CuSO_4\\cdot 5H_2O\\), formula mass \\(249.5\\text{ u}\\)).", "\\(36.07\\% \\text{ (approx } 36.1\\%\\))", "\\(25.0\\%\\)", "\\(45.5\\%\\)", "\\(18.0\\%\\)")
            ],
            'tmpls': [
                "Compute the molecular mass of hexose sugar: {0}",
                "Calculate the disaccharide molecular mass: {0}",
                "Determine sodium chloride formula mass: {0}",
                "Compute calcium carbonate formula mass: {0}",
                "Calculate sulphuric acid molecular mass: {0}",
                "Determine nitrogen mass fraction in fertilizer: {0}",
                "Calculate elemental mass percentage: {0}",
                "Compute nitric acid molecular mass: {0}",
                "Determine hydrated copper sulphate formula mass: {0}",
                "Calculate water of crystallization percentage: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract atomic masses and stoichiometric counts from chemical formula.\\n**Step 2: Arithmetic Evaluation**\\nCompute molecular mass \\(M_r = \\sum n_i A_i\\), and mass percentage \\(\\% = \\frac{{m_{{\\text{{element}}}}}}{{M_r}} \\times 100\\%\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
