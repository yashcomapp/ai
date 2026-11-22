# scripts/build_clean_scit_ch9_part3.py
# Clean generator for MH-9-SCIT Chapter 9 remaining subtopics:
# 9.3.2, 9.4.1, 9.4.2 (3 subtopics x 80 = 240 Qs)

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 9
CH_NAME = "Environmental Management"

def gen_9_3_2():
    tc = "MH-9-SCIT-9-9.3.2"
    tname = "Pyrolysis and sanitary landfilling"
    archs = [
        # Arch 0: Sanitary Landfill Engineering and Impermeable Liners
        {
            'data': [
                ("Impermeable composite bottom liner (compacted clay + HDPE geomembrane)", "prevents toxic leachate from percolating downward and poisoning subterranean groundwater aquifers", "allows toxic chemical liquid to seep freely into drinking wells", "acts as a heat conductor to ignite underground trash", "serves as a decorative carpet for landfill trucks"),
                ("Leachate collection and removal system (perforated pipes in gravel bed)", "intercepts, collects, and pumps toxic leachate to on-site chemical and biological wastewater treatment plants", "sprays toxic black leachate into residential drinking water pipes", "evaporates leachate into open neighborhood air without treatment", "flushes raw chemical leachate into surrounding farm fields"),
                ("Landfill gas (LFG) extraction wells and flaring/energy recovery", "captures flammable methane (\\(\\text{CH}_4\\)) and \\(\\text{CO}_2\\) to generate electricity and prevent explosive pressure buildup", "pumps methane directly into public residential basements", "releases concentrated methane into the open atmosphere without capture", "ignites uncontrolled spontaneous surface fires on the garbage mounds"),
                ("Daily soil cover (15 cm layer of compacted soil or inert material)", "controls insect vector breeding (flies, mosquitoes), deters scavengers/birds, and minimizes odor dispersion", "encourages millions of rats to breed on the garbage face", "keeps the garbage completely exposed to direct monsoon downpours", "increases the flammable surface area of the landfill"),
                ("Final capping and vegetative cover post-closure", "multi-layered barrier (clay, geomembrane, drainage layer, and topsoil with grass) preventing rainwater ingress and soil erosion", "digging open gravel pits across the closed landfill face", "building heavy concrete skyscrapers directly on uncapped mounds", "flooding the closed landfill with industrial toxic wastewater"),
                ("Groundwater monitoring test wells upstream and downstream of landfill", "periodically samples groundwater to detect any early breakthrough or breach of the bottom containment liner", "injects raw sewage directly into the deep pristine aquifer", "measures the speed of underground tectonic plate movements", "extracts drinking water directly from beneath the garbage mass"),
                ("Difference between open dumping and sanitary landfilling", "sanitary landfills use engineered containment, leachate treatment, and gas recovery, while open dumps lack any environmental protection", "open dumps are scientifically sealed and sanitary landfills are uncontrolled garbage heaps", "both methods dispose of untreated radioactive waste legally", "open dumps prevent all groundwater contamination while sanitary landfills do not"),
                ("Site selection criteria for sanitary landfills", "must be away from floodplains, wetlands, fault lines, airports (bird hazard), and high water tables", "must be situated in the direct center of municipal bird sanctuaries", "must be constructed on active river floodplains for easy washing", "must be built directly above unconfined drinking water aquifers"),
                ("Geotextile cushion layer above the HDPE geomembrane", "protects the 1.5 to 2.0 mm thick geomembrane from puncture by sharp gravel stones and debris during compaction", "conducts electrical lightning strikes deep into the trash", "absorbs all methane gas produced in the landfill", "melts the underlying clay liner into liquid mud"),
                ("Bioreactor landfill concept", "re-circulates collected leachate through the waste mass to accelerate anaerobic biodegradation and stabilize waste within 5 to 10 years", "sterilizes the landfill using chemical chlorine bleach", "freezes the waste mass using liquid nitrogen", "converts the landfill into an open radioactive quarry")
            ],
            'tmpls': [
                "What is the indispensable environmental protection provided by the '{0}' in a sanitary landfill?",
                "How does the '{0}' safeguard public health and subterranean ecosystems?",
                "What critical function is fulfilled by the '{0}' installed throughout the landfill cells?",
                "Why is a '{0}' applied across the active working face at the conclusion of each day?",
                "What engineering purpose is served by the '{0}' applied once a landfill reaches maximum design elevation?",
                "Why are '{0}' strategically drilled around the perimeter of an engineered landfill?",
                "What fundamental scientific distinction separates '{0}'?",
                "Which mandatory environmental regulation governs the '{0}' under statutory municipal rules?",
                "What mechanical protective role is executed by the '{0}' in liner construction?",
                "What biological and kinetic acceleration is achieved in a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Sanitary Landfill Engineering**\\nSanitary landfills are engineered containment facilities designed with composite liners, leachate collection, and gas venting to isolate waste from the environment.\\n**Step 2: Component Role**\\n{item[0]} {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Pyrolysis and Gasification Thermochemical Processes
        {
            'data': [
                ("Pyrolysis", "thermal decomposition of organic and carbonaceous materials at high temperatures (300°C to 900°C) in the complete absence of oxygen", "combustion of waste with abundant excess oxygen in open bonfires", "biological breakdown of organic matter using aerobic earthworms", "dissolving plastic polymers in cold tap water"),
                ("Three primary product fractions of pyrolysis", "Bio-oil (liquid pyrolytic oil), Syngas (combustible gases \\(\\text{CO}, \\text{H}_2, \\text{CH}_4\\)), and Biochar (solid carbonaceous residue)", "pure potable mineral water, oxygen gas, and fertile soil", "radioactive uranium, plutonium, and heavy concrete", "nitrogen gas, argon gas, and liquid helium"),
                ("Gasification", "thermochemical conversion of carbonaceous material into syngas (\\(\\text{CO} + \\text{H}_2\\)) under controlled, sub-stoichiometric oxygen/steam at >800°C", "complete burning of garbage into ash under excess air", "fermentation of sugary fruits by baker's yeast", "mechanical crushing of dry glass bottles"),
                ("Pyrolysis of scrap vehicle tires", "recovers valuable fuel oil (substitute for industrial furnace oil), carbon black, and high-tensile steel wire", "produces pure natural latex rubber juice", "dissolves tire rubber into agricultural cooking vinegar", "converts tires into biodegradable organic vegetable fertilizer"),
                ("Syngas (Synthesis Gas) composition and utility", "mixture of carbon monoxide (\\(\\text{CO}\\)) and hydrogen (\\(\\text{H}_2\\)) used for clean power generation in gas turbines or synthetic fuels", "mixture of oxygen and ozone used in hospitals", "toxic sulfur dioxide used as a household beverage", "pure water vapor without any calorific energy"),
                ("Biochar agricultural application and carbon sequestration", "porous stable carbon that improves soil water retention, cation exchange, and locks carbon in soil for centuries", "toxic radioactive powder that sterilizes agricultural land", "acidic chemical salt that corrodes tractor plows", "volatile explosive gas that detonates in sunlight"),
                ("Differences between Pyrolysis and Incineration", "pyrolysis operates without oxygen producing energetic fuels (oil/gas), while incineration combusts waste with excess oxygen releasing flue gas and ash", "incineration operates in total vacuum while pyrolysis operates in open air", "pyrolysis produces zero products while incineration produces gold", "both processes operate at freezing room temperatures"),
                ("Plasma Arc Gasification", "uses an electrical plasma arc torch (>3000°C to 10,000°C) to disintegrate waste into elemental syngas and inert vitrified glass slag", "burns waste using kerosene wick lamps", "freezes industrial scrap in liquid nitrogen blocks", "soaks hazardous waste in warm salt water"),
                ("Feedstock moisture sensitivity in pyrolysis reactors", "requires dried feedstocks (typically <10-15% moisture) because high water content cools the reactor and reduces oil quality", "requires feedstocks saturated with 90% liquid water", "operates exclusively when submerged under ocean water", "explodes violently if dry feedstock is introduced"),
                ("Dioxin and Furan formation suppression in pyrolysis", "absence of free oxygen and temperatures prevents de-novo synthesis of carcinogenic chlorinated dioxins common in open incinerators", "pyrolysis generates 100 times more dioxins than open burning", "oxygen is deliberately pumped in to maximize dioxin production", "dioxins are harmless aromatic perfume additives")
            ],
            'tmpls': [
                "In chemical and environmental engineering, what is the formal definition of '{0}'?",
                "What are the '{0}' generated from the pyrolytic processing of organic polymers?",
                "How is the thermochemical conversion process of '{0}' executed industrially?",
                "What high-value secondary resources are reclaimed from the '{0}'?",
                "Identify the chemical makeup and industrial utility of '{0}':",
                "Why is the production of '{0}' celebrated as a major climate mitigation breakthrough?",
                "What fundamental thermodynamic distinction separates '{0}'?",
                "What extreme thermochemical condition defines the technology of '{0}'?",
                "Why is '{0}' a critical pre-treatment parameter for efficient pyrolytic conversion?",
                "Why is the operational advantage of '{0}' environmentally superior to conventional mass burning?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Thermochemical Conversion Principles**\\nPyrolysis and gasification convert waste polymers and biomass into high-value energetic syngas, bio-oil, and biochar under oxygen-deficient conditions.\\n**Step 2: Technical Breakdown**\\n{item[0]} entails {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: Environmental Pollution Controls in Waste-to-Energy (WTE)
        {
            'data': [
                ("Electrostatic Precipitator (ESP)", "uses high-voltage electrostatic charges to attract and remove fine fly-ash particulates (>99% efficiency) from flue gas", "neutralizes acidic sulfur gases in drinking water", "chills outgoing furnace steam into liquid ice", "measures the weight of incoming refuse trucks"),
                ("Flue Gas Desulfurization (FGD) scrubbers", "sprays alkaline limestone or lime slurry to neutralize acidic sulfur dioxide (\\(\\text{SO}_2\\)) and hydrogen chloride (\\(\\text{HCl}\\))", "injects sulfuric acid into exhaust stacks to increase smoke acidity", "releases toxic chlorine gas into neighborhood skies", "cools down exhaust gas using liquid ammonia"),
                ("Selective Non-Catalytic Reduction (SNCR) / SCR", "injects ammonia or urea into high-temperature flue gases to reduce toxic nitrogen oxides (\\(\\text{NO}_x\\)) into harmless nitrogen gas and water", "oxidizes nitrogen into concentrated nitric acid rain", "converts oxygen gas into toxic carbon monoxide", "creates high levels of explosive hydrogen gas"),
                ("Activated carbon injection in flue gas ductwork", "adsorbs traces of volatile heavy metals (especially vaporous mercury) and toxic dioxins/furans before baghouse filters", "ignites a secondary explosion in the chimney", "bleaches the dark smoke into a bright white color", "dissolves the steel chimney walls through acid corrosion"),
                ("Fabric Baghouse Filters", "woven fabric filter bags that capture ultra-fine sub-micron toxic particles and spent neutralizing lime reagents", "metal wire screens that allow all dust to escape", "paper sheets that dissolve in moist air", "open chimney vents with no barrier"),
                ("Continuous Emission Monitoring System (CEMS)", "automated real-time sensor array measuring stack gas concentrations of \\(\\text{PM}, \\text{SO}_2, \\text{NO}_x, \\text{CO}, \\text{HCl}\\) transmitted directly to CPCB servers", "a manual thermometer read by security guards once a month", "a visual inspection of smoke color through binoculars", "a periodic handwritten report submitted annually"),
                ("Bottom Ash vs Fly Ash in WTE incinerators", "bottom ash (~85-90%) is non-combustible aggregate/glass reusable in road base; fly ash (~10-15%) contains concentrated toxins and must be stabilized in hazardous landfills", "both ash streams are completely non-toxic and used in baby food", "fly ash is pure gold dust and bottom ash is diamond", "bottom ash floats in air while fly ash sinks in water"),
                ("Refuse Derived Fuel (RDF) preparation line", "shredding, magnetic separation, air-classifying, and drying to concentrate high-calorific plastics, textiles, and paper into dense fuel pellets", "adding liquid sewage to soak dry paper boxes", "mixing broken glass bottles with food scraps", "crushing concrete blocks into fine building sand"),
                ("Minimum furnace temperature requirement in modern mass-burn incinerators", "strictly maintained above 850°C to 1100°C with at least 2 seconds residence time to ensure complete thermal destruction of organic molecules", "maintained at 50°C to save electrical energy", "operated at sub-zero freezing temperatures", "allowed to fluctuate between 100°C and 200°C"),
                ("Energy recovery via steam boilers and turbo-generators", "heat from flue gas generates high-pressure superheated steam that drives steam turbines to produce green electricity", "burning fuel to heat up cold municipal tap water without electricity", "venting all furnace heat directly into the open atmosphere", "using electrical heaters to keep garbage warm")
            ],
            'tmpls': [
                "Which specialized pollution control device functions as an '{0}'?",
                "How do modern industrial thermal plants deploy '{0}' to prevent acid rain?",
                "What chemical de-pollution reaction is executed by '{0}' in combustion stacks?",
                "Why is '{0}' indispensable for capturing volatile mercury and persistent organic pollutants?",
                "What mechanical filtration role is executed by '{0}' in environmental air cleansing?",
                "What statutory regulatory mandate is fulfilled by the deployment of '{0}'?",
                "What critical environmental distinction separates '{0}'?",
                "What engineering sequence constitutes a modern '{0}'?",
                "Why is the '{0}' legally enforced under environmental emissions standards?",
                "How does the mechanism of '{0}' convert thermal energy into municipal power?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Flue Gas Cleaning Engineering**\\nWaste combustion facilities utilize multi-stage air pollution control systems (SNCR, lime scrubbers, activated carbon, ESP/baghouses) to comply with strict emissions norms.\\n**Step 2: Component Function**\\n{item[0]} {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 3: Scientific Landfill Reclamation and Bio-mining
        {
            'data': [
                ("Bio-mining / Landfill mining", "excavating, aerating, screening, and mechanically fractionating legacy dumpsite garbage to reclaim land and extract resources", "pumping groundwater to submerge old garbage mountains", "covering garbage heaps with concrete to build housing colonies", "lighting chemical fires to incinerate garbage mounds underground"),
                ("Trommel screen in bio-mining", "rotating cylindrical perforated mesh drum that separates fine soil/compost (<4mm), inert stones (4-50mm), and oversized combustibles (>50mm)", "a high-powered laser that vaporizes plastic wrappers", "an underground pump that extracts crude oil from trash", "a chemical vat that dissolves metals into acid"),
                ("Bio-stabilization before mechanical sieving", "spraying bio-inoculants and turning legacy waste mounds to digest volatile organics and eliminate foul odor and methane", "flooding the garbage mound with kerosene to prevent flies", "freezing the entire dumpsite using liquid carbon dioxide", "burying the garbage under river silt immediately"),
                ("Refuse Derived Fuel (RDF) fraction extracted from bio-mining", "combustible plastics, textile rags, and footwear segregated and shredded for shipment to cement kilns", "pure organic manure packaged for kitchen gardening", "ferrous steel scrap sold to electric arc furnaces", "inert construction sand used for plastering"),
                ("Good earth / Enriched soil fraction recovered from dumpsites", "stabilized, aged organic-mineral fraction screened (<4mm) utilized for road embankments, greening, and quarry filling", "toxic radioactive slag that must be isolated in steel vaults", "flammable chemical fuel powder used in aircraft engines", "edible food flour distributed to local bakeries"),
                ("Inert stones, concrete, and brick fraction recovered", "diverted to aggregate crushing plants for manufacturing recycled concrete aggregate (RCA) and paving blocks", "dumped back into city drinking water lakes", "burned in power plant furnaces", "mixed with agricultural cow dung fertilizer"),
                ("Environmental hazard of legacy unscientific dumpsites (e.g., Ghazipur, Deonar)", "continuous toxic leachate leakage into ground aquifers and chronic spontaneous methane fires polluting city air", "cooling of city climate below freezing point", "spontaneous generation of pure drinking water springs", "absorption of all regional atmospheric pollution"),
                ("Land reclamation economic dividend of bio-mining", "clearing hundreds of acres of prime urban land worth thousands of crores previously locked under garbage hills", "increasing municipal expenditure without any return", "rendering urban land permanently sterile and radioactive", "depleting municipal tax revenues completely"),
                ("Workers safety gear during bio-mining excavation", "respiratory dust masks, safety goggles, hard hats, chemical-resistant gloves, and puncture-resistant steel-toe boots", "swimming trunks and flip-flops without masks", "woolen blankets wrapped around the body", "bare hands and cloth sandals"),
                ("Drone LiDAR and thermal mapping of legacy dumps", "accurately computes total garbage volume, mound topography, and identifies internal thermal hotspots prone to fire", "sprays drinking water over the garbage mound", "broadcasts municipal announcements to birds", "transports heavy garbage trucks across the site")
            ],
            'tmpls': [
                "What is the formal environmental definition and goal of '{0}'?",
                "How does a '{0}' mechanically sort distinct fractions in dumpsite remediation?",
                "Why is the biological procedure of '{0}' performed prior to mechanical screening?",
                "What sustainable industrial destination is assigned to the '{0}'?",
                "How is the '{0}' safely utilized after certification under CPCB guidelines?",
                "What circular infrastructure application consumes the '{0}'?",
                "What chronic ecological disaster is provoked by the persistence of '{0}'?",
                "What is the massive urban economic dividend unlocked through the successful execution of '{0}'?",
                "What occupational safety standard is strictly mandatory for '{0}'?",
                "How does advanced geospatial technology deploy '{0}' to assist dumpsite remediation?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Legacy Dumpsite Remediation & Bio-mining**\\nBio-mining stabilizes and mechanically separates aged dumpsite waste into RDF (fuel), soil/earth (greening/filling), and inert aggregate, reclaiming valuable urban land.\\n**Step 2: Operational Role**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Hazards of Open Burning vs Incineration
        {
            'data': [
                ("Incomplete low-temperature combustion during open burning (<400°C)", "generates dense black soot, carbon monoxide, unburnt hydrocarbons, and highly carcinogenic dioxins/furans", "converts all plastics into harmless oxygen and nitrogen", "destroys all chemical bonds leaving pure water vapor", "cools the ambient air temperature safely"),
                ("Open burning of PVC wires to extract copper metal", "releases toxic hydrogen chloride gas and deadly polychlorinated dibenzodioxins (PCDDs) poisoning nearby communities", "purifies the copper wire without generating any airborne smoke", "converts toxic chlorine into edible table salt", "replenishes atmospheric stratospheric ozone"),
                ("Controlled high-temperature industrial incineration (>1000°C)", "ensures complete thermal oxidation of volatile organic compounds with computerized air-fuel controls and flue-gas scrubbers", "releases 100 times more black soot than an open bonfire", "operates without any chimney or emission monitoring", "burns waste without producing any thermal energy"),
                ("Health hazard to children living near open garbage burning sites", "acute asthmatic bronchospasm, stunted lung development, and elevated blood lead and carboxyhemoglobin levels", "rapid improvement in respiratory endurance and stamina", "complete immunity against all childhood viral illnesses", "natural enhancement of cognitive intelligence"),
                ("Impact of open burning on urban air quality index (AQI)", "causes severe spikes in PM2.5 and PM10 concentrations plunging air quality into 'Severe' and 'Hazardous' categories", "cleans ambient air and reduces PM2.5 levels to zero", "improves visibility to over 50 kilometers", "neutralizes all vehicular traffic emissions"),
                ("Legal status of burning leaves, agricultural crop residue, and garbage in India", "strictly illegal under National Green Tribunal (NGT) orders and SWM Rules with statutory criminal penalties", "promoted by environmental protection agencies as a best practice", "mandated for all suburban housing colonies in winter", "exempted from all environmental regulations"),
                ("Fine particulate matter (PM2.5) physiological hazard", "particles \\(\\le 2.5\\,\\mu\\text{m}\\) penetrate deep into lung alveoli and enter the bloodstream causing strokes and heart attacks", "particles are trapped completely by nose hairs and never enter the lungs", "particles nourish lung cells with essential dietary minerals", "particles dissolve safely into harmless blood plasma proteins"),
                ("Carbon monoxide (\\(\\text{CO}\\)) toxicity mechanism", "binds irreversibly with hemoglobin to form carboxyhemoglobin (HbCO), preventing oxygen delivery to vital brain tissues", "increases the oxygen carrying capacity of red blood cells by 300%", "stimulates cellular ATP generation in cardiac muscles", "acts as a harmless biological vitamin"),
                ("Polycyclic Aromatic Hydrocarbons (PAHs) in garbage smoke", "potent genotoxic mutagens that intercalate into human DNA strands triggering cellular oncogenesis (cancer)", "beneficial biological proteins that accelerate wound healing", "harmless aromatic hydrocarbon perfumes", "plant nutrients that stimulate crop photosynthesis"),
                ("Economic cost of open garbage burning", "billions of dollars in healthcare expenditure, lost labor productivity, and tourism cancellations due to smog", "massive economic profit for municipal corporations", "dramatic reduction in hospital emergency admissions", "spontaneous generation of municipal tax revenue")
            ],
            'tmpls': [
                "What toxicological consequence is produced by '{0}'?",
                "Which extreme chemical and health hazard is unleashed during '{0}'?",
                "What engineering distinction separates '{0}' from uncontrolled open bonfires?",
                "What clinical pediatric pathology is provoked by '{0}'?",
                "How does the practice of '{0}' directly alter the regional environmental index?",
                "What is the statutory judicial position regarding the '{0}'?",
                "Explain the severe systemic physiological threat posed by inhalation of '{0}':",
                "Describe the biochemical mechanism of cellular asphyxiation caused by '{0}':",
                "What long-term molecular and cellular damage is inflicted by '{0}'?",
                "What massive macroeconomic and civic damage results from the practice of '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Combustion Toxicology & Environmental Law**\\nOpen waste burning produces low-temperature incomplete combustion, emitting deadly persistent toxins (dioxins, PM2.5, CO, PAHs), and is strictly prohibited by law.\\n**Step 2: Pathological Analysis**\\n{item[0]} causes {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Hazardous Waste Treatment, Storage & Disposal Facilities (TSDF)
        {
            'data': [
                ("Treatment, Storage and Disposal Facility (TSDF)", "specialized facility for scientific stabilization, secure chemical landfilling, and incineration of hazardous industrial waste", "an open playground for children", "a municipal facility for sorting domestic vegetable peels", "an underground parking lot for city buses"),
                ("Stabilization and Solidification of toxic heavy metal sludge", "mixing sludge with Portland cement, lime, and fly-ash to bind heavy metals into an insoluble, non-leachable solid matrix", "boiling the sludge in open iron pots to evaporate water", "diluting the sludge with fresh river drinking water", "pouring the liquid sludge into municipal crop irrigation canals"),
                ("Secured Landfill (SLF) for hazardous waste vs MSW landfill", "constructed with double composite liners, double leachate collection systems, and leak-detection layers between liners", "an unlined pit dug into sandy beach soil", "an open quarry exposed to direct wind and rain", "a single plastic tarp laid over loose soil"),
                ("Toxicity Characteristic Leaching Procedure (TCLP) test", "standard analytical laboratory test measuring whether toxic heavy metals leach out of stabilized waste under acidic conditions", "measuring the color and fragrance of flower blossoms", "counting the number of bacteria in river water", "weighing the total volume of construction debris"),
                ("Hazardous Waste Manifest System", "six-copy statutory tracking document accompanying hazardous waste from generator to transporter to authorized TSDF", "a retail shopping receipt given to consumers", "a promotional brochure describing factory machinery", "a municipal building construction permit"),
                ("Incineration of hazardous organic solvents in dedicated rotary kilns", "operating at 1100°C to 1200°C with secondary combustion chambers to achieve >99.99% Destruction and Removal Efficiency (DRE)", "operating at 100°C to boil off water gently", "dumping solvents into open earthen ponds to evaporate", "mixing solvents with household drinking water supplies"),
                ("Disposal of expired pesticide stocks and persistent chemical drums", "high-temperature co-processing in cement kilns (>1400°C) where high temperature and alkaline environment destroys compounds", "dumping drums into agricultural irrigation lakes", "burying chemical drums under school playgrounds", "discharging liquid pesticides into city stormwater drains"),
                ("Containment protocol for radioactive medical and laboratory waste", "shielded lead containers stored in dedicated decay-in-storage vaults until radioactivity drops to background clearance levels", "dumping radioactive syringes into ordinary municipal blue bins", "burning radioactive clothing in open backyard incinerators", "flushing radioactive isotopes down municipal domestic toilets"),
                ("Hazardous Waste (Management and Transboundary Movement) Rules", "framed under the Environment (Protection) Act 1986 to regulate hazardous waste handling and prevent illegal dumping", "regulates international maritime passenger cruises", "governs the sale of domestic agricultural food grains", "allocates commercial spectrum to mobile phone companies"),
                ("Emergency preparedness at TSDF sites (HAZMAT response)", "on-site foam fire tenders, chemical neutralizing agents, emergency eye-wash showers, and dedicated containment dikes", "wooden brooms and domestic plastic buckets", "first aid adhesive bandages only", "leaving emergency response entirely to distant city fire brigades")
            ],
            'tmpls': [
                "What is the statutory role and engineering purpose of a '{0}'?",
                "How does the chemical engineering protocol of '{0}' immobilize industrial toxins?",
                "What structural containment standard distinguishes a '{0}'?",
                "In hazardous waste compliance laboratories, what critical property is evaluated by the '{0}'?",
                "What administrative chain-of-custody tracking is enforced through the '{0}'?",
                "What extreme destruction efficiency standard governs the '{0}'?",
                "What advanced industrial technological route is mandated for the safe '{0}'?",
                "What standardized radiological safety protocol governs the '{0}'?",
                "Which parent statutory environmental act empowers the '{0}' in India?",
                "What specialized chemical safety infrastructure is mandatory for '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Hazardous Waste Engineering & TSDF Standards**\\nHazardous industrial wastes require chemical stabilization, double-composite secure landfills, high-temperature incineration, and rigorous manifest tracking.\\n**Step 2: Technical Function**\\n{item[0]} {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Solid Waste Management in Natural Disasters
        {
            'data': [
                ("Earthquake disaster debris generation", "millions of tonnes of collapsed concrete, masonry rubble, shattered glass, and twisted structural steel reinforcement", "pure organic fruit peels and kitchen vegetables", "radioactive uranium rods only", "toxic chemical pesticides only"),
                ("Cyclone and Hurricane disaster debris generation", "uprooted mature trees, collapsed power lines, destroyed roofing sheets, and waterlogged municipal mud", "dry powdered cement only", "solid crystalline plastic granules only", "sterile laboratory glass vials only"),
                ("Tsunami marine inundation debris", "mixture of ocean sand, salt-waterlogged building debris, sunken boats, and decomposing organic fish/animal matter", "clean white office paper reams", "fresh drinking water bottles", "dry agricultural wheat straw"),
                ("Immediate priority in disaster waste clearance", "clearing main transit corridors, hospital access routes, and power/water infrastructure lifelines", "sorting plastic bottles by resin code 1 to 7", "building commercial shopping malls on debris piles", "conducting annual financial tax audits of ruined buildings"),
                ("Staging areas (temporary debris management sites)", "designated vacant fields where disaster debris is collected, sorted for hazardous materials, and crushed to prevent road blockage", "dumping debris into river channels to block floodwaters", "pushing debris into agricultural irrigation canals", "leaving debris piled in residential streets for decades"),
                ("Separation of disaster debris into salvageable streams", "segregating structural timber for reconstruction, metals for scrap smelting, and concrete rubble for mobile rock crushers", "incinerating structural steel girders in open pits", "dumping copper electrical wires into the ocean", "mixing hazardous chemical drums with crushed concrete"),
                ("Disposal of mass animal carcasses following floods or cyclones", "prompt deep burial in lime-disinfected mass burial pits or high-temperature incineration to avert lethal cholera epidemics", "leaving rotting carcasses in drinking water reservoirs", "dumping carcasses along open public highways", "selling flood-drowned animal meat in public markets"),
                ("Disinfection of waterlogged disaster camps and flood mud", "spraying calcium hypochlorite (bleaching powder) and quicklime to disinfect mud and suppress microbial vector proliferation", "spraying liquid crude petroleum over muddy streets", "pouring concentrated sulfuric acid on tent floors", "spreading dry cardboard packaging across wet marshes"),
                ("Mobile concrete and masonry crushers at disaster sites", "crushes demolished concrete and bricks into granular sub-base aggregate for immediate emergency road repair", "melts concrete into transparent glass sheets", "converts crushed concrete into edible food flour", "incinerates concrete into combustible gas"),
                ("Disaster Waste Management Guidelines by NDMA", "standard operating procedures for debris clearance, hazard containment, community involvement, and environmental protection during catastrophes", "instructions on how to cause building collapses", "rules governing commercial real-estate auctions", "regulations on international tourist visas")
            ],
            'tmpls': [
                "What massive waste stream is generated following an '{0}'?",
                "Which physical debris components characterize a '{0}'?",
                "What complex environmental hazard is presented by '{0}'?",
                "In emergency humanitarian logistics, what is the '{0}'?",
                "What engineering purpose is served by setting up '{0}' in disaster-hit zones?",
                "How do disaster recovery engineers execute the '{0}' to speed up reconstruction?",
                "What critical public health and epidemic prevention protocol governs the '{0}'?",
                "Why is the application of '{0}' non-negotiable in flood-ravaged refugee settlements?",
                "How does the deployment of '{0}' accelerate post-disaster infrastructure recovery?",
                "What statutory framework is provided by the '{0}' in India?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Disaster Waste Logistics & Public Health**\\nCatastrophes generate massive composite debris that must be rapidly cleared from lifeline corridors, sorted for salvage, and disinfected to prevent epidemics.\\n**Step 2: Tactical Action**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Calculations on Landfills and Pyrolysis
        {
            'data': [
                ("A city generates 200 tonnes of MSW daily. If 20% is non-recyclable inert reject requiring landfill disposal, calculate the daily landfill load:", "40 tonnes per day", "10 tonnes per day", "100 tonnes per day", "180 tonnes per day"),
                ("If compacted solid waste in a landfill has an in-situ density of 500 kg per cubic meter, what volume is occupied by 1,000 tonnes of waste?", "2,000 cubic meters", "500 cubic meters", "1,000 cubic meters", "5,000 cubic meters"),
                ("A landfill cell has a total volume capacity of 100,000 cubic meters. If 10,000 cubic meters of compacted waste is added annually, what is its design life?", "10 years", "5 years", "20 years", "50 years"),
                ("A pyrolysis reactor processes 10 tonnes of dry plastic scrap. If the pyrolytic oil yield is 70% by weight, what mass of fuel oil is recovered?", "7 tonnes (7,000 kg)", "3 tonnes (3,000 kg)", "1 tonne (1,000 kg)", "9 tonnes (9,000 kg)"),
                ("If 1 tonne of Municipal Solid Waste generates 150 cubic meters of landfill gas, how much gas is generated from 600 tonnes of waste?", "90,000 cubic meters", "15,000 cubic meters", "4,000 cubic meters", "60,000 cubic meters"),
                ("If landfill gas contains 55% Methane (\\(\\text{CH}_4\\)) and 45% Carbon Dioxide (\\(\\text{CO}_2\\)), what volume of pure Methane is present in 2,000 cubic meters of LFG?", "1,100 cubic meters", "900 cubic meters", "550 cubic meters", "1,500 cubic meters"),
                ("A waste-to-energy boiler burns 50 tonnes of RDF per day. If 10% remains as non-combustible bottom ash, what is the daily bottom ash mass produced?", "5 tonnes", "15 tonnes", "25 tonnes", "1 tonne"),
                ("If bio-mining screens 500 tonnes of legacy waste daily and recovers 30% as Refuse Derived Fuel (RDF), how many tonnes of RDF are extracted daily?", "150 tonnes", "50 tonnes", "250 tonnes", "300 tonnes"),
                ("A municipal composting plant processes 100 tonnes of wet waste daily and achieves a 20% conversion yield to mature compost. What is the daily compost yield?", "20 tonnes", "50 tonnes", "10 tonnes", "80 tonnes"),
                ("If a sanitary landfill daily cell covers an area of 500 square meters with a 0.15 meter (15 cm) thick soil layer, what volume of cover soil is needed daily?", "75 cubic meters", "150 cubic meters", "50 cubic meters", "30 cubic meters")
            ],
            'tmpls': [
                "{0}",
                "Solve the following environmental engineering calculation: {0}",
                "Determine the quantitative design metric: {0}",
                "Compute the landfill engineering value: {0}",
                "Evaluate the numerical result: {0}",
                "Calculate the resource recovery yield: {0}",
                "Perform the stoichiometric waste mass balance: {0}",
                "Solve the practical municipal calculation: {0}",
                "Determine the calculated outcome: {0}",
                "Compute the physical quantity requested: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the mass, volume, density, or percentage values from the problem statement.\\n**Step 2: Arithmetic Computation**\\nApply basic volumetric or proportional multiplication: \\(\\text{{Mass}} = \\text{{Volume}} \\times \\text{{Density}}\\) or percentage fraction.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_9_4_1():
    tc = "MH-9-SCIT-9-9.4.1"
    tname = "ABC of first aid (Airway, Breathing, Circulation)"
    archs = [
        # Arch 0: The Core ABC Protocol of First Aid
        {
            'data': [
                ("A - Airway", "checking and opening the casualty's airway by tilting the head back and lifting the chin (Head-tilt Chin-lift maneuver)", "feeding the unconscious casualty hot drinking water", "checking if the person has a driver's license", "administering oral antibiotics immediately"),
                ("B - Breathing", "looking for chest rise, listening for breath sounds, and feeling for breath on the rescuer's cheek for up to 10 seconds (Look, Listen, Feel)", "performing immediate orthopedic bone fracture surgery", "slapping the casualty's cheeks vigorously", "giving heavy solid food to chew"),
                ("C - Circulation", "checking for a carotid pulse in the neck and administering external chest compressions if heartbeat/pulse is absent", "measuring the victim's height and weight", "splinting a minor finger bruise", "checking blood group in a laboratory"),
                ("Cardiac Arrest vs Respiratory Arrest", "in cardiac arrest the heart stops pumping completely requiring immediate CPR; in respiratory arrest breathing stops while pulse may initially persist", "both terms mean a superficial skin scratch", "neither condition is an emergency", "cardiac arrest occurs only in deep sleep"),
                ("CPR (Cardiopulmonary Resuscitation) compression to ventilation ratio", "30 chest compressions followed by 2 rescue breaths (30:2) for adults", "100 rescue breaths followed by 1 compression", "1 compression to 10 breaths", "50 compressions without any pause indefinitely"),
                ("Chest compression depth for adult CPR", "at least 5 cm to 6 cm (2 to 2.4 inches) into the center of the chest (lower half of sternum)", "1 cm (very light superficial touch)", "15 cm (compressing completely to the spine)", "0.5 cm (touching clothing gently)"),
                ("Chest compression rate for CPR", "100 to 120 compressions per minute to the rhythm of 'Stayin' Alive'", "20 compressions per minute (very slow)", "300 compressions per minute (extremely rapid)", "5 compressions per hour"),
                ("Automated External Defibrillator (AED)", "portable electronic device that analyzes heart rhythm and delivers an electrical shock to treat ventricular fibrillation", "a manual blood pressure cuff", "an infrared skin thermometer", "an oxygen cylinder regulator valve"),
                ("Recovery Position (Lateral Recumbent Position)", "placing an unconscious breathing victim on their side with head tilted back to keep the airway open and prevent choking on vomit", "placing the victim flat on their stomach with face buried in pillows", "hanging the victim upside down by their ankles", "forcing the victim to sit upright on a tall stool"),
                ("Choking emergency protocol (Heimlich Maneuver / Abdominal Thrusts)", "standing behind the choking victim and applying upward abdominal thrusts between the navel and ribcage to dislodge the foreign object", "giving the victim large glasses of cold water to drink", "slapping the victim's throat with a flat palm", "forcing the victim to swallow dry bread chunks")
            ],
            'tmpls': [
                "What is the non-negotiable emergency action for '{0}' in primary first aid assessment?",
                "How does a first responder execute '{0}' to evaluate an unconscious patient?",
                "What clinical diagnostic procedure defines '{0}' during emergency life support?",
                "What fundamental medical distinction separates '{0}'?",
                "According to international resuscitation guidelines, what is the standardized '{0}'?",
                "What is the scientifically prescribed '{0}' to ensure adequate cardiac output during CPR?",
                "At what precise speed should a rescuer maintain the '{0}' during CPR?",
                "What life-saving cardiac function is fulfilled by an '{0}' available in public venues?",
                "Why is placing an unconscious breathing victim in the '{0}' critical for survival?",
                "What emergency life-saving technique is performed during '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: First Aid Emergency Protocols**\\nThe ABC protocol (Airway, Breathing, Circulation) establishes immediate life support priorities to maintain cerebral and myocardial oxygenation.\\n**Step 2: Procedural Standard**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Severe Bleeding (Hemorrhage) and Shock Management
        {
            'data': [
                ("Direct pressure on a bleeding wound", "applying firm continuous pressure directly over the wound with a sterile gauze pad or clean cloth to promote clotting", "pouring cold tap water on the wound from a distance", "wiping the blood away every 2 seconds without pressing", "rubbing coarse sand into the open cut"),
                ("Tourniquet application rules", "applied only for life-threatening arterial limb bleeding 5-7 cm above the wound, never over a joint, noting the exact time applied", "tied loosely around the victim's neck", "applied for minor paper cuts on fingertips", "left in place for 3 days without doctor evaluation"),
                ("Arterial vs Venous bleeding characteristics", "arterial blood is bright red and spurts under pulsatile pressure; venous blood is dark red and flows steadily", "arterial blood is black and venous blood is white", "both bleed at identical zero pressure", "venous blood squirts 2 meters into the air"),
                ("Hypovolemic Shock definition and signs", "circulatory failure due to massive blood/fluid loss, marked by rapid weak pulse, pale clammy skin, confusion, and shallow breathing", "high blood pressure with flushed red face and excessive energy", "normal healthy resting state", "severe toothache without bleeding"),
                ("First aid position for a patient in shock (without spinal injury)", "laying patient flat on back and elevating legs 15-30 cm (Trendelenburg/shock position) to enhance venous return to heart and brain", "forcing the patient to stand and run briskly", "hanging the patient head-down from a tree branch", "bending the patient forward with head between knees while standing"),
                ("Keeping a shock patient warm with a blanket", "prevents hypothermia, which impairs biological blood clotting factors and worsens internal shock", "causes the patient's skin to blister", "increases blood loss from capillaries", "cures bacterial wound infections instantly"),
                ("Managing an impaled or embedded foreign object (e.g. knife, glass shard)", "never remove the object; stabilize it in place with bulky dressings and bandages around it and seek urgent surgery", "pull the knife out immediately with a quick jerk", "push the object deeper to stop bleeding", "twist the object to seal the cut artery"),
                ("Epistaxis (Nosebleed) correct first aid posture", "sitting upright, leaning slightly forward, and pinching the soft fleshy part of the nostrils firmly for 10 minutes", "tilting head far back and swallowing blood into stomach", "lying flat on back and blowing nose forcefully", "inserting sharp wooden sticks into nostrils"),
                ("Internal bleeding warning signs following blunt trauma", "bruising (ecchymosis) over abdomen, rigid board-like belly, vomiting blood (hematemesis), and signs of shock", "complete absence of all symptoms forever", "immediate growth of strong muscle tissue", "sudden drop in body temperature to freezing point"),
                ("Severed amputated digit (finger/toe) preservation protocol", "wrap amputated part in sterile gauze, place in sealed waterproof plastic bag, and put the bag on ice (never directly on ice)", "soak the severed finger in hot boiling water", "throw the finger away into a general waste bin", "rub the severed finger with salt and chili powder")
            ],
            'tmpls': [
                "What is the primary first aid step for controlling external hemorrhage: '{0}'?",
                "Which strict clinical guideline must be followed during '{0}'?",
                "How can a first responder distinguish '{0}' at an accident site?",
                "Identify the physiological syndrome and symptoms associated with '{0}':",
                "What is the recommended posture for '{0}'?",
                "Why is the simple intervention of '{0}' vital for trauma victims?",
                "What is the non-negotiable rule when dealing with '{0}'?",
                "Which physical action represents the correct first aid technique for '{0}'?",
                "What critical diagnostic observations indicate potential '{0}'?",
                "What is the standardized medical preservation protocol for a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Hemorrhage & Trauma Protocols**\\nSevere bleeding requires direct pressure or calibrated tourniquets; shock requires leg elevation and warmth; amputated parts require indirect cold storage.\\n**Step 2: Emergency Response**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Burns and Scalds Management
        {
            'data': [
                ("First aid for thermal burns (fire, boiling water, steam)", "cool the burn immediately under gentle cool running tap water for at least 10 to 20 minutes", "apply cold ice cubes directly on the raw burned flesh", "smear toothpaste, butter, or cooking oil over the burn", "rub turmeric powder and soil into the blisters"),
                ("Why ice MUST NOT be applied directly to burns", "extreme cold causes tissue vasoconstriction and thermal frostbite, worsening tissue necrosis and cell damage", "ice causes burns to heal within 2 seconds", "ice makes the burned skin turn permanently into leather", "ice causes systemic blood poisoning"),
                ("Why butter, grease, or cooking oil MUST NOT be applied to burns", "grease traps heat inside the skin tissues, delays medical cooling, and introduces severe bacterial infections", "cooking oil accelerates skin cooling tenfold", "butter causes instant pain relief and sterilizes wounds", "cooking oil turns the burn into a sterile bandage"),
                ("Handling burn blisters (vesicles)", "never puncture or burst blisters because intact skin serves as a natural sterile barrier against deadly bacterial infections", "burst all blisters with a sewing needle immediately", "peel off all loose blister skin with tweezers", "scrub blisters with a rough pumice stone"),
                ("First-degree burn (Superficial burn)", "affects only epidermis, characterized by redness (erythema), mild swelling, and pain without blisters (e.g. mild sunburn)", "destroys muscle and bone tissues completely", "causes painless charred black leathery skin", "involves loss of entire limb function"),
                ("Second-degree burn (Partial-thickness burn)", "affects epidermis and dermis, causing intense pain, redness, and fluid-filled blisters (bullae)", "painless burn that leaves white charred bone", "superficial dry tan with no redness", "destruction of internal abdominal organs"),
                ("Third-degree burn (Full-thickness burn)", "destroys all skin layers, subcutaneous tissue; nerve endings destroyed making the central area painless, appearing charred/waxy white", "mild red sunburn that disappears in 1 hour", "painless blister that bursts safely", "minor scratch on fingernail"),
                ("Chemical burn emergency first aid (acid or alkali splashes)", "copious continuous flushing with clean running water for at least 20 minutes, removing contaminated clothing carefully", "neutralizing strong acid by pouring strong caustic soda lye on the skin", "covering the acid with dry flour and wrapping in wool", "rubbing the chemical deeper with a dry towel"),
                ("Electrical burn hidden internal injury", "electrical current travels along blood vessels and nerves causing cardiac arrhythmias and severe internal muscle necrosis", "electrical burns only affect hair follicles superficially", "current leaves no internal effect whatsoever", "electricity converts human fat into healthy bone"),
                ("Rule of Nines in burn assessment", "clinical tool dividing adult body surface area into sections of 9% (or multiples) to estimate total burn percentage", "counting the number of blisters on the hands", "measuring the victim's pulse rate every 9 seconds", "giving the victim 9 glasses of hot milk")
            ],
            'tmpls': [
                "What is the immediate, evidence-based first aid protocol for '{0}'?",
                "In medical emergency science, explain '{0}':",
                "What is the pathophysiological reason that explains '{0}'?",
                "What is the strict clinical instruction regarding '{0}'?",
                "Identify the clinical symptoms and skin depth of a '{0}':",
                "What physical indicators characterize a '{0}'?",
                "Describe the clinical appearance and severity of a '{0}':",
                "What is the life-saving decontamination protocol for '{0}'?",
                "What critical physiological danger makes an '{0}' deceptively hazardous?",
                "What is the clinical utility of the '{0}' utilized by emergency physicians?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Burn Pathology & First Aid**\\nBurns must be cooled with running water for 10-20 min; ice, grease, and blister popping are contraindicated; full-thickness burns require urgent hospital shock management.\\n**Step 2: Clinical Evaluation**\\n{item[0]} entails {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Bone Fractures, Sprains, and Dislocations (RICE Principle)
        {
            'data': [
                ("R - Rest", "immobilize the injured limb immediately and prevent the casualty from moving or bearing weight on the injury", "encourage the victim to run or jump to test the joint", "force the joint to rotate in all directions", "massage the fractured bone vigorously"),
                ("I - Ice", "apply cold ice packs wrapped in a towel for 15-20 minutes every 2-3 hours to reduce swelling and numb pain", "apply burning hot water bottles directly to the fresh sprain", "pour boiling oil over the swollen ligament", "pack the open fracture with raw mud"),
                ("C - Compression", "wrap the injured joint with an elastic crepe bandage firmly but not too tightly to limit swelling and provide support", "tie a wire tourniquet until the foot turns black and gangrenous", "plaster the limb with wet clay and dry over fire", "leave the swollen joint completely unsupported"),
                ("E - Elevation", "prop the injured limb on pillows above heart level to assist venous return and reduce gravitational edema/swelling", "hang the injured swollen leg downwards off the bed", "tie heavy weights to the injured ankle", "bury the injured foot in warm sand"),
                ("Open (Compound) Fracture vs Closed (Simple) Fracture", "open fracture involves broken bone piercing through skin creating an open infected wound; closed fracture has intact overlying skin", "open fracture occurs only in skulls; closed fracture in toes", "both fractures heal completely in 2 hours", "closed fracture always requires immediate amputation"),
                ("Splinting a fractured limb", "immobilize the joint above and the joint below the fracture site using rigid padded boards, rolled magazines, or cardboard", "attempting to forcefully pull and snap the crooked bone straight yourself", "bending the broken bone back and forth to align it", "leaving the broken limb loose to swing freely during transit"),
                ("Sprain vs Strain definition", "sprain is an injury/tear to a ligament connecting bone to bone; strain is an injury/tear to a muscle or tendon connecting muscle to bone", "sprain affects only teeth; strain affects hair", "both terms are identical to skin sunburn", "sprain is a bacterial blood infection"),
                ("Dislocation of a joint (e.g. shoulder dislocation)", "never attempt to forcefully pop the bone back into the socket; support the limb in the most comfortable position and go to hospital", "pull the arm with two people until it makes a loud popping crack", "hit the shoulder with a heavy mallet to knock it into place", "force the patient to do 50 pushups immediately"),
                ("Checking distal circulation after bandaging or splinting", "check capillary refill (nail bed pink within 2 seconds), warmth, sensation, and peripheral pulse below the bandage", "check if the patient's hair has grown longer", "measure the patient's body height with a tape", "ignore whether the toes become blue and cold"),
                ("Suspected spinal or neck injury immobilization", "never move the head, neck, or spine; maintain manual in-line stabilization until a rigid cervical collar and spine board arrive", "twist the victim's head rapidly from side to side to check hearing", "force the victim to sit up and drink hot tea", "carry the victim in a curved sitting cradle posture")
            ],
            'tmpls': [
                "What is the first aid directive associated with '{0}' in musculoskeletal trauma?",
                "How is the '{0}' step executed scientifically for an acute ligament sprain?",
                "What is the correct protocol for applying '{0}' to a swollen ankle?",
                "Why is the technique of '{0}' crucial within the first 48 hours of joint injury?",
                "What critical anatomical distinction separates an '{0}'?",
                "What is the cardinal rule of first aid when '{0}'?",
                "What is the precise anatomical difference in '{0}'?",
                "What dangerous action must be avoided when handling a '{0}'?",
                "Why must a first responder perform '{0}'?",
                "What life-saving caution governs the management of a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Musculoskeletal First Aid & RICE**\\nTrauma to bones, joints, and ligaments requires RICE (Rest, Ice, Compression, Elevation), splinting spanning adjacent joints, and zero manual bone manipulation.\\n**Step 2: Procedural Rule**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Heat Emergencies, Dehydration, and Hypothermia
        {
            'data': [
                ("Heat Stroke (Sunstroke) definition and danger", "life-threatening failure of thermoregulation with core body temperature >40°C, hot dry skin (no sweating), and altered consciousness", "minor cold shivering that disappears with a hot jacket", "normal body reaction to eating spicy food", "bacterial infection of the digestive tract"),
                ("Heat Exhaustion vs Heat Stroke distinction", "heat exhaustion features heavy sweating, cool pale clammy skin, and normal mental state; heat stroke features dry skin, delirium/coma, and high temp", "heat exhaustion is fatal in 100% of cases while heat stroke is harmless", "both conditions feature core temperature below 30°C", "heat stroke only occurs in polar regions"),
                ("First aid management for Heat Stroke", "move victim to cool shade, remove outer clothing, apply cold wet sponges/ice packs to neck, armpits, and groin, and call emergency ambulance", "cover the victim with three heavy wool blankets", "force the unconscious victim to swallow boiling coffee", "make the victim perform strenuous aerobic exercises"),
                ("Oral Rehydration Salts (ORS) solution composition", "balanced mixture of sodium chloride, glucose, potassium chloride, and trisodium citrate dissolved in clean drinking water", "pure table sugar mixed with carbonated cola drinks", "concentrated chili paste mixed with mustard oil", "unfiltered muddy ditch water"),
                ("Heat cramps cause and treatment", "painful muscle spasms due to electrolyte (salt) depletion from profuse sweating, relieved by rest and drinking electrolyte fluids/ORS", "permanent paralysis requiring surgical limb amputation", "bacterial tetanus infection of the bones", "fracture of the thigh femur bone"),
                ("Hypothermia definition and symptoms", "core body temperature dropping below 35°C (95°F), characterized by violent shivering, slurred speech, clumsy fingers, and progressive apathy", "body temperature rising to 42°C with red hot skin", "excessive sweating and dehydration during marathon runs", "temporary loss of dental enamel"),
                ("First aid for severe Hypothermia", "move to warm shelter, remove wet clothing, rewarm trunk gradually with warm dry blankets, and provide warm sweet non-alcoholic drinks if conscious", "submerge the freezing casualty directly into boiling water", "give large doses of chilled alcohol or vodka to drink", "rub the frozen skin vigorously with rough snow"),
                ("Frostbite definition and handling", "freezing of skin and underlying tissues (fingers, toes, nose); rewarm gently in lukewarm water (37-40°C), never rub frozen tissue", "rub frozen black fingers with rough sandpaper", "hold frozen fingers directly over an open candle flame", "cut off the frozen toes immediately with scissors"),
                ("Trench Foot (Immersion foot)", "tissue damage caused by prolonged exposure of feet to damp, cold conditions (>0°C); keep feet clean, warm, and thoroughly dry", "fungal infection acquired from swimming in chlorinated pools", "acute fracture of the heel calcaneus bone", "allergic reaction to wearing leather sandals"),
                ("Signs of clinical dehydration in children", "sunken eyes, depressed fontanelle in infants, dry tongue/mouth, absence of tears when crying, and skin tenting (loss of turgor)", "excessive urination every 10 minutes", "bright red flushed cheeks with energetic jumping", "swelling of both ankles with fluid accumulation")
            ],
            'tmpls': [
                "What clinical condition is defined as '{0}'?",
                "What is the critical clinical difference that separates '{0}'?",
                "What immediate emergency intervention is required for '{0}'?",
                "What standard formula comprises '{0}' recommended by WHO?",
                "What physiological mechanism triggers '{0}'?",
                "Identify the physiological threshold and signs characterizing '{0}':",
                "What is the life-saving thermal rewarming protocol for '{0}'?",
                "How should a first responder safely manage '{0}' in high-altitude cold environments?",
                "What environmental pathology defines '{0}'?",
                "What pediatric clinical markers diagnose '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Thermoregulatory Pathology**\\nHeat stroke represents catastrophic failure of sweating mechanisms requiring rapid physical cooling; hypothermia requires gentle trunk rewarming.\\n**Step 2: Emergency Response**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Envenomation, Poisoning, and Animal Bites First Aid
        {
            'data': [
                ("Snakebite first aid golden rule (Do's)", "keep the victim calm and still, immobilize the bitten limb with a splint at heart level, and transport immediately to a hospital for Anti-Snake Venom (ASV)", "cut the bite wound with a razor blade and suck out venom by mouth", "tie a tight tourniquet until the limb loses all arterial pulse", "burn the bite puncture marks with a burning matchstick"),
                ("Dangerous traditional snakebite practices that MUST NEVER be done", "cutting, sucking venom by mouth, applying tight tourniquets, applying cow dung, or relying on faith healers (tantriks)", "resting the patient and reassuring them", "washing the bite gently with clean water", "splinting the limb to prevent muscular movement"),
                ("Neurotoxic vs Hemotoxic snake venom effects", "neurotoxic venom (Krait, Cobra) causes drooping eyelids (ptosis), respiratory paralysis, and asphyxiation; hemotoxic (Viper) causes swelling, tissue bleeding, and necrosis", "both venoms are completely harmless to mammalian blood", "neurotoxic venom causes instant bone fractures", "hemotoxic venom makes the heart pump 5 times faster"),
                ("Rabies transmission and animal bite first aid", "wash the animal bite wound immediately with running tap water and soap for 15 minutes, apply antiseptic, and seek Post-Exposure Prophylaxis (PEP) vaccine", "apply red chili powder and lime to the bite wound", "bandage the wound tightly without washing", "wait 6 months to see if the biting dog develops rabies"),
                ("Scorpion sting first aid", "apply cold compress/ice to reduce pain, reassure patient, immobilize limb, and rush to hospital for medical monitoring and prazosin if prescribed", "cut the sting site and pour battery acid inside", "force the patient to drink gasoline", "burn the scorpion on the patient's skin"),
                ("Ingested household poison first aid (e.g. toilet cleaner, acid, kerosene)", "never induce vomiting if corrosive acid/alkali or petroleum was swallowed; call poison center and rush to hospital with container", "force the patient to vomit by sticking fingers down throat", "force the patient to swallow concentrated raw vinegar", "make the patient drink boiling hot saltwater"),
                ("Inhaled carbon monoxide or gas leak poisoning", "evacuate casualty into fresh outdoor air immediately, turn off gas cylinder valve, ensure airway, and administer 100% oxygen", "strike a matchstick inside the gas-filled room to see clearly", "lock all doors and windows to contain the gas", "make the victim lie down on the kitchen floor"),
                ("Eye chemical splash first aid", "flush the open eye continuously with gentle stream of clean lukewarm water or saline for at least 15 to 20 minutes from inner to outer corner", "rub the eye vigorously with a dirty towel", "put concentrated lemon juice into the eye", "bandage the contaminated eye shut without washing"),
                ("Honeybee and Wasp sting removal", "scrape the stinger off sideways using a flat credit card or fingernail (do not squeeze with tweezers to avoid injecting venom sac)", "squeeze the stinger hard with sharp tweezers to crush it", "dig out the stinger with a rusty safety pin", "burn the stinger off with a cigarette lighter"),
                ("Electrolyte and fluid replacement in food poisoning", "administer Oral Rehydration Solution (ORS), clear soups, and tender coconut water to replenish fluid losses and prevent dehydration", "force the patient to eat heavy greasy mutton curry", "deprive the patient of all water for 3 days", "administer unprescribed adult sleeping pills")
            ],
            'tmpls': [
                "What is the life-saving standard of care in '{0}'?",
                "Identify the '{0}' that drastically increase tissue damage and mortality in snakebite cases:",
                "What clinical distinction differentiates '{0}'?",
                "What immediate first aid decontamination protocol is mandatory for '{0}'?",
                "How should a first responder manage an acute '{0}'?",
                "What critical contraindication must be strictly respected in '{0}'?",
                "What is the immediate priority when responding to '{0}'?",
                "What is the mandatory clinical decontamination procedure for an '{0}'?",
                "What is the correct physical removal technique for '{0}'?",
                "What is the foundational first aid supportive therapy for '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Toxicological & Envenomation Protocols**\\nSnakebites require limb immobilization and immediate anti-venom (cutting/sucking is contraindicated); animal bites require 15-min soapy water irrigation.\\n**Step 2: Emergency Response**\\n{item[0]} dictates {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: First Aid Kit Essentials and Emergency Helplines
        {
            'data': [
                ("National Emergency Helpline Number in India", "112 (Universal Emergency Integrated Helpline)", "100 only", "101 only", "102 only"),
                ("Ambulance Emergency Helpline in India", "108 / 102", "100", "101", "103"),
                ("Fire Service Emergency Helpline in India", "101", "100", "108", "102"),
                ("Police Assistance Helpline in India", "100 (or 112)", "101", "108", "1077"),
                ("National Disaster Response Force (NDRF) / Disaster Helpline", "1078 / 1070", "100", "101", "102"),
                ("Essential items in a standard First Aid Box", "sterile gauze pads, roller bandages, triangular bandage, adhesive tape, antiseptic solution (Betadine/Savlon), scissors, tweezers, ORS", "oral antibiotics, surgical scalpels, and intravenous anesthesia drugs", "commercial fireworks, matchboxes, and kerosene", "heavy steel wrenches and mechanical car jacks"),
                ("Triangular bandage primary uses", "making an arm sling, securing splints, or folding into a broad cravat for pressure dressings", "decorating the emergency vehicle dashboard", "tying garbage bags securely", "covering windows to block sunlight"),
                ("Sterile adhesive dressing (Band-Aid) utility", "protecting minor superficial cuts and abrasions from bacterial contamination and dirt", "splinting a fractured thigh bone", "treating full-thickness third degree burns", "closing arterial hemorrhages on the neck"),
                ("Roller (crepe) bandage utility", "providing compression, supporting sprained joints, and holding sterile dressings firmly in place", "stopping internal stomach bleeding", "tying an unconscious patient to a tree", "wrapping around the mouth of a choking victim"),
                ("Antiseptic solution (e.g. Chlorhexidine / Povidone Iodine) use", "cleaning the unbroken skin around wounds to prevent bacterial invasion (avoid pouring deep into open tissue)", "drinking as a beverage to cure throat infections", "washing eyes after chemical acid splashes", "rubbing into open bone fractures")
            ],
            'tmpls': [
                "Which telecommunication number functions as the '{0}'?",
                "Identify the dedicated emergency contact number for '{0}':",
                "What is the official national helpline code for '{0}'?",
                "Which number connects a citizen directly to '{0}'?",
                "What is the specialized statutory telephone helpline for '{0}'?",
                "Which collection of supplies comprises the '{0}'?",
                "What versatile life-support function is fulfilled by the '{0}'?",
                "What is the appropriate first aid application for a '{0}'?",
                "How is the '{0}' utilized in emergency musculoskeletal care?",
                "What is the proper first aid application of an '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Emergency Infrastructure & Logistics**\\nUniversal emergency numbers (112, 108) enable immediate dispatch, while standardized first aid kits provide essential dressings, antiseptics, and slings.\\n**Step 2: Utility Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Legal Protections (Good Samaritan Law) and Triage
        {
            'data': [
                ("Good Samaritan Law in India (Supreme Court Guidelines / Motor Vehicles Amendment Act 2019)", "protects bystanders who voluntarily assist accident victims from civil and criminal liability, harassment by police, or forced hospital payment", "mandates that bystanders who help must pay the victim's entire hospital bill", "imprisons any person who touches an accident victim", "requires bystanders to undergo police interrogation for 30 days"),
                ("Golden Hour in emergency trauma care", "the critical first 60 minutes post-trauma where prompt resuscitation and surgical intervention drastically prevents death", "the golden color of the sky at sunset", "a 24-hour waiting period before calling an ambulance", "the time taken to fill out police paperwork"),
                ("Triage definition in disaster mass casualty incidents", "sorting and categorizing casualties based on the severity of injury and urgency of medical care to optimize survival", "treating only wealthy individuals first", "treating casualties in alphabetical order of their names", "transporting uninjured bystanders to hospitals first"),
                ("Triage Color Code: Red Tag (Immediate)", "life-threatening injuries requiring immediate intervention to survive (e.g. airway obstruction, severe tension pneumothorax, arterial bleed)", "minor superficial cuts and scrapes", "deceased casualties without pulse or respiration", "delayed non-urgent stable fractures"),
                ("Triage Color Code: Yellow Tag (Delayed / Urgent)", "serious injuries requiring surgical care within 2-4 hours, but not in immediate imminent danger of death (e.g. stable femur fracture)", "walking wounded with small finger bruises", "victims who are already dead", "casualties needing CPR immediately"),
                ("Triage Color Code: Green Tag (Minimal / Walking Wounded)", "minor injuries capable of walking and self-care, who can wait several hours for treatment (e.g. minor abrasions)", "unconscious victims with no carotid pulse", "arterial spurting chest wounds", "casualties with severe brain herniation"),
                ("Triage Color Code: Black Tag (Expectant / Deceased)", "casualties who are deceased or have catastrophic injuries incompatible with life under disaster resource constraints", "minor ankle sprains", "healthy rescuer personnel", "unconscious patients who breathe after airway opening"),
                ("Bystander obligation at hospital under Good Samaritan Law", "the hospital cannot force the Samaritan to reveal their identity, pay admission fees, or wait at the hospital", "the bystander must stay at the hospital for 1 week", "the Samaritan must donate blood immediately", "the hospital must confiscate the Samaritan's car"),
                ("Police questioning of Good Samaritan under Indian Law", "bystanders can only be examined on a voluntary basis, at a time and place of their convenience, and cannot be harassed", "police must arrest the Samaritan as the primary murder suspect", "police must force the Samaritan to attend 100 court hearings", "police can impound the Samaritan's mobile phone permanently"),
                ("Primary goal of Mass Casualty Triage", "doing the greatest good for the greatest number of casualties with available medical resources", "providing exhaustive intensive care to only one hopeless patient while others die", "transporting casualties without any assessment", "abandoning all disaster victims without medical aid")
            ],
            'tmpls': [
                "What historic legal protection is enacted under the '{0}'?",
                "In emergency clinical trauma medicine, what is the definition and significance of the '{0}'?",
                "What operational principle defines '{0}' during catastrophic accidents?",
                "Which medical casualty classification is designated by the '{0}'?",
                "What clinical status is categorized under the '{0}' in disaster management?",
                "Which patient group is identified by the '{0}' during mass casualty triage?",
                "What tragic clinical status is denoted by the '{0}' in emergency sorting?",
                "What legal rights are granted to a helper regarding '{0}'?",
                "What strict statutory guideline governs the '{0}'?",
                "What is the philosophical and utilitarian cornerstone of '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Emergency Law & Disaster Triage**\\nThe Good Samaritan Law protects voluntary helpers from liability; Triage (Red, Yellow, Green, Black) allocates scarce medical resources to maximize lives saved.\\n**Step 2: Rule Analysis**\\n{item[0]} means {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_9_4_2():
    tc = "MH-9-SCIT-9-9.4.2"
    tname = "Transportation methods for injured patients (cradle method, human crutch, stretcher)"
    archs = [
        # Arch 0: One-Rescuer Transportation Methods
        {
            'data': [
                ("Cradle Method (Carrying in arms)", "for lightweight casualties or small children who are conscious and have no bone fractures", "for heavy adult victims with fractured spines", "for conscious victims with fractured pelvis bones", "for victims suffering neck fractures"),
                ("Human Crutch (One-rescuer crutch)", "for a conscious casualty with a single uninjured leg who can walk with support on their injured side", "for completely unconscious casualties in coma", "for patients with both legs fractured and shattered", "for casualties with broken spinal columns"),
                ("Carrying on the Back (Piggyback carry)", "for conscious casualties who can hold on to the rescuer's neck/shoulders with their arms", "for deeply unconscious victims with limp flaccid arms", "for patients with multiple fractured ribs and sternum", "for casualties with severe spinal paralysis"),
                ("Firefighter's Carry (Over-the-shoulder carry)", "for carrying an unconscious or semi-conscious casualty over distance, leaving one of the rescuer's hands free", "for patients with suspected broken neck or vertebral fractures", "for pregnant women in active advanced labor", "for casualties with open abdominal organ evisceration"),
                ("Firefighter's Drag (Blanket or clothing drag)", "for dragging an unconscious casualty through smoke-filled rooms, tunnels, or under low ceilings safely", "for carrying casualties up long spiral stairs", "for swimming with casualties across deep rivers", "for transporting casualties over high barbed-wire fences"),
                ("Blanket Drag method", "placing the casualty on a sturdy blanket and pulling the head end of the blanket keeping the spine aligned along the floor", "pulling the casualty sideways by one arm", "rolling the casualty down a flight of concrete stairs", "dragging the casualty by their feet across rough broken glass"),
                ("Clothing / Shirt Drag", "grasping the casualty's coat or shirt collar behind the shoulders and pulling backward while supporting the head on rescuer's forearms", "dragging the casualty forward by their belt buckle", "pulling the casualty by their hair", "pulling the casualty by their shoelaces"),
                ("Ankle Drag (Foot drag)", "emergency short-distance drag across smooth flat surfaces when the rescuer cannot access the head (caution: no head support)", "dragging a victim with broken spinal vertebrae across rocks", "dragging a victim across high staircases", "dragging a victim through fast-flowing flood currents"),
                ("Pack-strap Carry", "draping the casualty's arms over the rescuer's shoulders and crossing their wrists across the rescuer's chest", "carrying the victim balanced horizontally on the head", "stuffing the victim inside a small traveling suitcase", "rolling the victim along the ground like a log"),
                ("Pick-a-back vs Firefighter's carry comparison", "pick-a-back requires an active conscious casualty who can grip; firefighter's carry can transport an unconscious casualty", "both methods are strictly for broken neck fractures", "neither method requires any physical rescuer strength", "firefighter's carry is used exclusively for newborn infants")
            ],
            'tmpls': [
                "Under which specific clinical scenario is the '{0}' appropriately deployed?",
                "What physical condition of the casualty makes the '{0}' the ideal choice?",
                "What prerequisite casualty capability is mandatory for adopting the '{0}'?",
                "What operational advantage is achieved by adopting the '{0}'?",
                "Why is the technique of '{0}' uniquely effective in burning building evacuations?",
                "How is the '{0}' executed to preserve spinal alignment during emergency extraction?",
                "What is the mechanical technique executed during a '{0}'?",
                "When is the use of the '{0}' acceptable as an extreme emergency extraction?",
                "Describe the anatomical grip utilized in the '{0}':",
                "What fundamental casualty status distinguishes the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: One-Rescuer Patient Evacuation**\\nSingle-rescuer evacuation depends on the casualty's weight, consciousness, ability to grasp, and absence of spinal fractures.\\n**Step 2: Method Criteria**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Two-Rescuer Transportation Methods
        {
            'data': [
                ("Two-Hand Seat (Human chair)", "two rescuers grasp wrists to form a seat for carrying a conscious casualty unable to walk but able to hold rescuers' shoulders", "for an unconscious casualty who cannot hold rescuers", "for transporting a casualty with a shattered spine", "for moving casualties through 20-cm narrow drainage pipes"),
                ("Four-Hand Seat", "two rescuers interlock four hands to form a rigid square seat for a conscious patient capable of sitting upright and holding rescuers", "for an unconscious casualty in deep coma", "for carrying a casualty with two broken arms and dislocated shoulders", "for transporting patients with fractured pelvic girdles"),
                ("Fore-and-Aft Carry (Two-rescuer chair carry)", "one rescuer stands behind casualty holding under arms/wrists, second rescuer holds under casualty's knees", "carrying the victim by holding their head and ankles only", "carrying the victim slung between two broomsticks", "swinging the casualty between rescuers like a hammock"),
                ("Two-Rescuer Human Crutch", "rescuers on either side support casualty's arms over their shoulders and grasp casualty's belt/waist for assisted walking", "carrying a completely paralyzed unconscious victim", "dragging a victim across a barbed-wire field", "transporting a victim with broken spinal column"),
                ("Chair Method for stairs evacuation", "sitting casualty securely in a sturdy household chair, one rescuer carries chair back from top, other carries chair legs from below", "sliding the chair down the stairs like a sledge", "throwing the chair down the stairs ahead of the patient", "carrying the chair sideways so the patient falls out"),
                ("Hammock Carry (Three or more rescuers)", "rescuers interlock hands beneath the casualty's shoulders, hips, and knees keeping the body horizontal and level", "wrapping the patient inside a wet blanket and rolling them", "dragging the patient by their clothes across concrete", "carrying the patient vertically by their feet"),
                ("Two-rescuer drag using a coat or blanket", "rescuers hold corners of the blanket near casualty's head and pull backward simultaneously keeping body aligned", "pulling in opposite directions tearing the blanket", "dragging the casualty over high steps head-first", "rolling the blanket into a tight ball around the head"),
                ("Advantages of two-rescuer transport over single rescuer", "distributes casualty's weight evenly, reduces rescuer fatigue, and allows greater stability and spinal protection", "increases casualty pain and doubles the time taken", "requires zero coordination or communication", "guarantees that the patient will fall"),
                ("Verbal coordination command during two-rescuer lifts", "the rescuer at the casualty's head coordinates and calls out commands ('Ready, Lift!', 'Ready, Step!') to synchronize movement", "both rescuers shouting random commands at the same time", "carrying the patient without speaking any words", "allowing the injured patient to steer the rescuers"),
                ("Limitation of Two-Hand and Four-Hand seat carries", "cannot be used for unconscious casualties or patients with suspected spinal, pelvic, or lower limb fractures", "cannot be used for healthy uninjured people", "can only be used when moving inside swimming pools", "requires specialized hydraulic machinery to operate")
            ],
            'tmpls': [
                "What clinical condition permits the use of the '{0}' by two first aiders?",
                "What is the mechanical hand grip and patient requirement for the '{0}'?",
                "Describe the physical technique executed during a '{0}':",
                "Under what condition is the '{0}' the most appropriate assisted transit?",
                "Why is the '{0}' considered the safest technique for moving casualties down narrow building stairs?",
                "How do rescuers coordinate the '{0}' for horizontal patient transfer?",
                "What is the procedural standard for executing a '{0}'?",
                "What physiological and safety advantage is delivered by '{0}'?",
                "Why is standardized '{0}' mandatory during multi-rescuer patient handling?",
                "What critical clinical contraindication governs the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Two-Rescuer Manual Transit**\\nTwo-rescuer manual carries distribute patient load, require synchronized verbal commands, and are strictly contraindicated for unconscious or spinal injury casualties.\\n**Step 2: Technical Description**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Stretcher Construction, Handling, and Standards
        {
            'data': [
                ("Standard Canvas / Military Stretcher", "collapsible canvas bed mounted on two wooden/aluminum poles with cross-spreaders and carrying handles", "a single wooden plank without handles", "a soft woolen blanket held by two fingers", "a metal shopping trolley without wheels"),
                ("Improvised Stretcher using Blanket and Two Poles", "fold blanket into thirds over two sturdy poles so casualty's body weight locks the blanket frictionally in place", "tie blanket loosely to one pole with sewing thread", "cut the blanket into thin strips and tie around victim", "glue the blanket to poles using paper paste"),
                ("Improvised Stretcher using Two Buttoned Shirts/Jackets", "pass two poles through the reversed sleeves of two buttoned jackets/shirts with buttoned side facing downwards", "tear shirts into ribbons and tie around victim's ankles", "stuff shirts into victim's shoes", "drape shirts loosely over victim's face"),
                ("Scoop Stretcher (Orthopedic Stretcher)", "splits longitudinally into two halves that scoop under the casualty from both sides without moving the spine", "a flexible fabric hammock that bends the spine into a curve", "a circular round basket that rolls along the ground", "a rigid steel cage dropped from a helicopter"),
                ("Spine Board (Long Backboard / LBB)", "rigid, non-flexible wooden or plastic board with handholds and immobilization straps for suspected spinal trauma", "a soft spring mattress that sags in the middle", "an inflatable pool raft that bends with every step", "a rubber tire cut in half"),
                ("Basket Stretcher (Stokes Stretcher)", "heavy-duty wire mesh or plastic basket with raised sides used in wilderness, mountain, or helicopter winching rescues", "a domestic wicker picnic basket", "a cardboard carton box", "a plastic laundry wash tub"),
                ("Flexible Roll-up Stretcher (Sked Stretcher)", "flexible heavy plastic sheet that rolls into a backpack and wraps tightly around the casualty for confined space rescue", "a rigid glass mirror that breaks under load", "a heavy lead shield that weighs 100 kg", "a bedsheet held by sewing pins"),
                ("Stretcher direction of travel: Feet first standard", "casualties should normally be carried feet first (so the rear bearer can observe face), except when moving uphill/upstairs where head goes first", "always carried head first in all situations without exception", "carried upside down with feet pointing towards the sky", "rolled along the floor like a barrel"),
                ("Bearer pace while carrying a stretcher", "bearers should walk with broken step (out of step with each other) to prevent rhythmic swaying and nausea for the casualty", "both bearers jumping in unison with both feet", "running at top sprint speed without looking down", "walking in strict military marching cadence"),
                ("Blanketing a casualty on a stretcher", "placing blankets underneath and over casualty to insulate against ground conduction and ambient wind chill (preventing hypothermia)", "wrapping blankets tightly over casualty's nose and mouth", "leaving casualty unclothed on cold metallic frame", "soaking blankets in cold water before laying casualty")
            ],
            'tmpls': [
                "What structural components comprise a '{0}'?",
                "How is an '{0}' assembled securely using frictional body weight locking?",
                "Describe the engineering assembly of an '{0}' at an accident site:",
                "Why is the specialized design of a '{0}' preferred for suspected pelvic or spinal trauma?",
                "What critical immobilization feature distinguishes a '{0}'?",
                "Under what emergency extraction conditions is a '{0}' deployed?",
                "What operational versatility is offered by a '{0}' in technical rescue?",
                "What is the standardized universal rule regarding the '{0}'?",
                "Why is a non-synchronized '{0}' prescribed for stretcher bearers?",
                "What essential thermal protection is achieved by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Stretcher Transport Science**\\nStretchers (standard, scoop, spine board, basket) isolate the casualty from vibration, keep the spine straight, and require broken-step carrying to prevent rhythm sway.\\n**Step 2: Technical Breakdown**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Log-Roll Technique and Spinal Trauma Immobilization
        {
            'data': [
                ("Log-Roll technique purpose", "turning a suspected spinal trauma patient onto their side as a single rigid unit to inspect the back and insert a spine board", "exercising the patient's spine to increase mobility", "spinning the patient around quickly to test balance", "bending the patient's neck forward to touch their chin to chest"),
                ("Minimum personnel required for a controlled Log-Roll", "at least four rescuers (one at head holding manual cervical stabilization, three along trunk/legs)", "one rescuer acting alone without assistance", "two children without training", "zero personnel (patient turns themselves)"),
                ("Role of the Lead Rescuer at the head during Log-Roll", "maintains continuous manual in-line stabilization of head and neck, coordinates timing, and gives all movement commands", "lifts the patient's feet into the air", "leaves the head loose while checking vital signs", "walks around the patient taking photographs"),
                ("Hand placement of rescuers along the patient's side", "rescuers cross arms over casualty's shoulder, hip, pelvis, and lower legs to create a rigid, interlocking lifting plane", "holding the patient by their clothing buttons", "holding the patient by their hair and fingers", "pushing the patient's knees in opposite directions"),
                ("Cervical Collar (C-Collar) role", "restricts flexion, extension, and rotation of the cervical spine, but must always be supplemented with head blocks and straps", "replaces the need for a spine board completely", "acts as a soft pillow for sleeping", "cures spinal fractures instantly without surgery"),
                ("Head blocks (cervical immobilizers) on a spine board", "firm foam wedges placed on both sides of head and secured with forehead and chin straps to prevent all lateral movement", "soft down pillows that allow head to roll freely", "heavy steel weights that press down on the throat", "inflatable balloons that float in air"),
                ("Log-roll sequence command: 'Roll on three'", "on count of three, all rescuers roll patient smoothly towards themselves maintaining anatomical alignment of head, neck, and torso", "one rescuer rolls the hips while the head remains pinned flat", "each rescuer pulls at different times randomly", "dropping the patient onto the floor"),
                ("Danger of twisting or flexing a fractured spine", "bone fragments can sever or compress the spinal cord, causing permanent irreversible quadriplegia (paralysis) or death", "causes minor cosmetic skin wrinkles", "causes the broken bone to heal twice as fast", "improves nerve conduction along the spinal cord"),
                ("Strapping sequence on a spine board", "secure torso/chest first, then pelvis and thighs, then lower legs, and secure the head LAST (Torso first, Head last)", "strap head first and leave body completely loose", "tie legs first, head second, and ignore torso", "use no straps at all during ambulance transport"),
                ("Spine board removal in hospital emergency departments", "patients should be transferred off rigid backboards as soon as cleared by imaging to prevent debilitating pressure ulcers (bedsores)", "patients should remain strapped to rigid boards for 3 weeks", "backboards should be surgically implanted into the patient's spine", "backboards should be burned while the patient lies on them")
            ],
            'tmpls': [
                "What is the life-critical medical objective of the '{0}'?",
                "What is the '{0}' to execute safe spinal motion restriction?",
                "What non-negotiable responsibility is held by the '{0}'?",
                "What biomechanical grip is utilized for '{0}' during a log-roll?",
                "What clinical function and limitation applies to a '{0}'?",
                "Why are '{0}' anchored to a backboard alongside the cervical collar?",
                "What synchronized movement occurs on the standardized '{0}'?",
                "What catastrophic neurological consequence results from the '{0}'?",
                "According to international trauma protocol, what is the standardized '{0}'?",
                "Why do modern hospital clinical guidelines mandate prompt '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spinal Motion Restriction (SMR)**\\nSuspected spinal fractures mandate manual in-line stabilization, multi-person log-roll as a rigid cylinder, and torso-first/head-last strapping.\\n**Step 2: Operational Standard**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Vehicle Extrication and Confined Space Evacuation
        {
            'data': [
                ("Rapid Extrication vs Controlled Extrication from vehicle", "rapid extrication is performed ONLY when immediate danger to life exists (vehicle fire, sinking, scene hazard, or cardiac arrest)", "rapid extrication is always used for minor scratches to save time", "controlled extrication is performed when the car is exploding", "both methods ignore patient airway completely"),
                ("Kendrick Extrication Device (KED)", "semi-rigid corset-like device that wraps around victim's torso and head, immobilizing spine before removal from car seat", "a parachute used to jump from moving vehicles", "an inflatable tire jack used to lift car chassis", "a mechanical winch wire used to tow cars"),
                ("Airbag safety protocol for rescuers entering crashed vehicles", "disconnect vehicle battery, maintain safe distance (5-10-20 rule from steering/dash airbags), and avoid placing bodies in deployment zones", "puncture intact airbags with knives while leaning over steering wheel", "cut all colored wiring bundles simultaneously with steel shears", "leave vehicle engine running at full throttle"),
                ("Breaking vehicle tempered side glass safely", "use a spring-loaded center punch on the bottom corner of side window away from patient, after covering patient with protective blanket", "smash the windshield with a heavy sledgehammer directly over patient's head", "shoot the glass with a firearm", "kick the front windshield inward with steel boots"),
                ("Laminated glass vs Tempered glass in modern automobiles", "windshields are laminated (shatters but remains bonded to plastic interlayer); side windows are tempered (breaks into harmless small granules)", "windshields shatter into long razor-sharp spears", "side windows never break under any force", "both glasses are made of bulletproof solid titanium"),
                ("Vehicle stabilization before patient extrication", "chock vehicle wheels, place step chocks/cribbing under rocker panels, and deflate tires to prevent vehicle shift during cutting", "leave vehicle rocking freely on soft damaged suspensions", "shake the vehicle vigorously to see if it rolls over", "push the car on its side with a bulldozer"),
                ("Confined space hazard assessment (atmospheric testing)", "test with calibrated multi-gas detector for oxygen deficiency (<19.5%), explosive gases, and toxic \\(\\text{H}_2\\text{S}/\\text{CO}\\) before entry", "light a matchstick inside the manhole to check if air is breathable", "send an unprotected rescuer inside to smell the air", "assume all underground sewer pipes contain fresh mountain air"),
                ("Tripod and winch mechanical retrieval system", "overhead aluminum tripod with mechanical retrieval winch and harness for vertical lifting of casualties from deep manholes/silos", "a single thin cotton rope tied around patient's neck", "throwing a wooden ladder down and waiting for patient to climb", "flooding the confined space with water so patient floats up"),
                ("SCBA (Self-Contained Breathing Apparatus) necessity", "mandatory positive-pressure respiratory protection for rescuers entering toxic atmospheres or oxygen-deficient environments", "wearing a wet cotton handkerchief over mouth and nose", "holding one's breath for 20 minutes while carrying patient", "using a paper surgical mask in dense carbon monoxide"),
                ("Hydraulic rescue spreaders and cutters ('Jaws of Life')", "hydraulic tools developing tons of force to pry open crushed vehicle doors, cut structural roof pillars, and displace dashboards", "manual hand hacksaws and wooden chisels", "blowtorches that set car gasoline tanks on fire", "domestic electric carving knives")
            ],
            'tmpls': [
                "What clinical or environmental condition justifies the decision for '{0}'?",
                "What is the life-saving spinal immobilization function of the '{0}'?",
                "What safety protocol protects emergency rescuers regarding '{0}'?",
                "What is the standardized, controlled technique for '{0}' during vehicle rescue?",
                "What structural difference separates '{0}' in emergency rescue operations?",
                "Why is the tactical step of '{0}' non-negotiable prior to victim extrication?",
                "What atmospheric safety protocol must precede '{0}' into underground chambers?",
                "What engineering mechanism is deployed via a '{0}' for confined space rescues?",
                "Why is the deployment of '{0}' mandatory for toxic atmosphere entries?",
                "How do emergency rescue teams deploy '{0}' to free trapped motorists?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Technical Vehicle & Confined Space Rescue**\\nVehicle rescue requires scene stabilization, electrical/airbag isolation, specialized devices (KED), and gas monitoring prior to confined space entry.\\n**Step 2: Technical Standard**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Aquatic Rescues and Water Transit
        {
            'data': [
                ("Drowning rescue order of priority: 'Reach, Throw, Row, Go'", "Reach with pole/branch \\(\\rightarrow\\) Throw lifebuoy/rope \\(\\rightarrow\\) Row boat \\(\\rightarrow\\) Go (swim) only as last resort with flotation aid", "Go (jump in clothes) \\(\\rightarrow\\) Row \\(\\rightarrow\\) Throw \\(\\rightarrow\\) Reach", "Throw \\(\\rightarrow\\) Go \\(\\rightarrow\\) Row \\(\\rightarrow\\) Reach", "Reach \\(\\rightarrow\\) Go \\(\\rightarrow\\) Row \\(\\rightarrow\\) Throw"),
                ("Why jumping into water to rescue a drowning person is dangerous", "a panicking drowning person will instinctively grab, climb on, and push the rescuer underwater, drowning both", "the water will instantly freeze into solid ice", "the drowning person will swim away rapidly", "rescuers never know how to swim"),
                ("Lifebuoy (Ring buoy) deployment", "throw beyond the victim and pull line gently so buoy comes to victim's hands, keeping holding line anchored to shore", "throw the heavy buoy directly onto the victim's head to stun them", "cut the rope before throwing the buoy into the river", "jump into the water while holding the buoy on one's head"),
                ("Throw-bag (Rescue throw line) technique", "open bag, hold loop at end of rope with non-throwing hand, throw bag underhand towards victim's chest, shouting 'Rope!'", "throw the bag and let go of both ends of the rope", "throw the rope coiled up like a ball", "tie the rope to one's neck before throwing"),
                ("Tow technique for an unconscious casualty in water", "Cross-chest carry or Chin carry keeping casualty's face and nose strictly above water while swimming sidestroke/backstroke", "dragging casualty completely submerged beneath the surface", "pushing casualty's head down while holding ankles", "swimming freestyle with both hands leaving casualty behind"),
                ("Cervical spine injury in shallow water diving accidents", "suspect neck fracture in all shallow water diving; maintain in-line spinal stabilization in water using Head-Splint technique before extrication", "drag the diver out by their ankles immediately", "bend diver's head backward and forward to check neck stiffness", "roll diver down a boat slipway"),
                ("Head-Splint technique in water rescue", "rescuers trap victim's head between victim's own extended upper arms, gently squeezing against ears to stabilize cervical spine", "tie a heavy anchor around victim's neck", "twist victim's head 180 degrees", "pull victim's hair with two hands"),
                ("Initial resuscitation step for drowning casualties on shore", "open airway, check breathing, and immediately give 5 initial rescue breaths followed by 30 compressions and 2 breaths (CPR)", "hold casualty upside down by feet to drain all water from stomach", "press hard on the stomach to force water to vomit out", "wait 2 hours for lungs to dry naturally"),
                ("Why abdominal thrusts or 'draining water from lungs' is contraindicated in drowning", "water in lungs is absorbed rapidly into circulation; forcing vomiting causes gastric content aspiration into lungs, causing fatal chemical pneumonitis", "draining water causes instant drowning on land", "stomachs never contain any fluid during drowning", "water in lungs turns into nutritious blood"),
                ("Secondary drowning (Submersion injury pulmonary edema)", "casualty appears fully recovered after inhaling water, but develops delayed pulmonary edema and respiratory failure hours later", "casualty drowns a second time while walking in the park", "casualty loses all memory of their family", "casualty develops an acute allergy to water")
            ],
            'tmpls': [
                "What is the universally taught lifesaving order of precedence for water rescue: '{0}'?",
                "From a lifeguarding perspective, explain '{0}':",
                "What is the correct nautical and lifesaving technique for '{0}'?",
                "How is an emergency '{0}' deployed from shore or riverbank?",
                "Which swimming tow technique is authorized for moving an '{0}'?",
                "What critical trauma protocol applies to '{0}' in swimming pools or rivers?",
                "Describe the biomechanical execution of the '{0}' for in-water stabilization:",
                "According to international resuscitation guidelines, what is the '{0}'?",
                "What physiological danger explains why '{0}' is strictly dangerous?",
                "In emergency clinical medicine, what is '{0}' and why does it mandate hospital admission?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Aquatic Rescue & Resuscitation**\\nWater rescue prioritizes low-risk methods ('Reach, Throw, Row, Go'); drowning victims require initial rescue breaths (5 breaths before CPR); lung drainage is contraindicated.\\n**Step 2: Technical Standard**\\n{item[0]} entails {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Air Ambulance and Aeromedical Transportation
        {
            'data': [
                ("Helicopter Emergency Medical Services (HEMS / Air Ambulance)", "rapid transport of critical trauma casualties over long distances, rugged terrain, or congested urban areas directly to tertiary trauma centers", "slow transport of non-urgent patients for routine dental checkups", "transporting heavy construction cement blocks", "commercial luxury tourism joyrides"),
                ("Helicopter Landing Zone (LZ) safety dimensions", "minimum 30m x 30m (100ft x 100ft) flat, firm ground, clear of overhead wires, trees, loose debris, and illuminated at corners", "a 2m x 2m narrow muddy ditch", "underneath high-voltage overhead electricity cables", "an active crowded vegetable market street"),
                ("Rotor wash hazard and loose debris control", "downward rotor wind force (>100 km/h) can blow loose sheet metal, gravel, and trash into air; securing all loose gear is vital", "rotor wind creates pure soothing cool breezes with no wind force", "rotors never move any ambient air", "downward air turns all debris into dust-free clouds"),
                ("Helicopter approach and departure safety rules", "always approach/depart from the front or sides within pilot's field of vision (10 o'clock to 2 o'clock), in crouched posture, never near tail rotor", "approach casually from directly behind near the tail rotor", "run upright holding long metal poles above head", "walk beneath the tail boom while engine is running"),
                ("Tail rotor danger in helicopters", "tail rotor spins at high speed and is virtually invisible, causing instantaneous fatal trauma if approached from rear", "tail rotor is made of soft harmless sponge rubber", "tail rotor blows sweet perfume", "tail rotor stops spinning when people walk near it"),
                ("Physiological effects of altitude during aeromedical transport (Boyle's Law)", "gas expands as atmospheric pressure drops with altitude; trapped air in pneumothorax, bowel, or endotracheal cuff expands dangerously", "gases shrink into dense heavy liquids at high altitude", "air pressure remains identical at 10,000 feet to sea level", "altitude eliminates all gas from human bodies"),
                ("Pneumothorax pre-flight intervention before air transport", "a chest tube (intercostal drain) must be inserted before aeromedical flight to prevent fatal tension pneumothorax from trapped expanding air", "sealing the chest wound with duct tape without a drain", "inflating the patient's chest with bicycle pump air", "forcing the patient to hold their breath during flight"),
                ("Endotracheal tube and air splint management at altitude", "fill air cuffs with sterile saline instead of air to prevent pressure changes during ascent and descent", "over-inflate the tube cuff with 100 ml of air", "deflate the cuff completely so patient can cough", "cut the breathing tube in half during flight"),
                ("Night operations landing zone illumination", "mark four corners of LZ with weighted lights, point vehicle headlights across LZ (never directly into pilot's eyes)", "shine laser pointers directly into the helicopter cockpit", "light massive bonfires in the direct center of the touchdown pad", "point high-beam spotlights directly at the pilot's windshield"),
                ("Patient packaging for helicopter winch extraction", "casualty secured inside rigid basket stretcher with multi-point harnesses, tag line attached to prevent spinning during hoist", "casualty dangling freely by a single ankle rope", "holding casualty by their shirt collar with one hand", "casualty sitting loose on top of the winch hook")
            ],
            'tmpls': [
                "What clinical mission defines the operations of '{0}'?",
                "What physical criteria and clearance is mandatory for a '{0}'?",
                "Why is management of '{0}' critical prior to helicopter landing?",
                "What is the non-negotiable personal safety rule regarding '{0}'?",
                "What lethal hazard makes the '{0}' the most hazardous area around a rotary aircraft?",
                "How does the physical principle of '{0}' affect injured patients during flight?",
                "What surgical pre-condition must be secured regarding a '{0}' prior to air transit?",
                "How must flight medical crews manage '{0}' to prevent barotrauma?",
                "What standardized lighting protocol governs '{0}' for night medevac?",
                "What technical stabilization is mandatory during '{0}' from mountainous terrain?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Aeromedical Evacuation Protocols**\\nAir ambulance transport requires strict LZ safety (30x30m, 10-2 approach), debris control, and management of altitude gas expansion (Boyle's Law).\\n**Step 2: Operational Standard**\\n{item[0]} requires {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Calculations and First Aid Metrics
        {
            'data': [
                ("A rescuer performs adult CPR for 2 minutes. Following the 30:2 protocol at 100 compressions/minute, how many total cycles of 30:2 are completed?", "approximately 5 complete cycles", "100 cycles", "1 cycle", "50 cycles"),
                ("According to the Rule of Nines, if an adult casualty suffers burns covering the entire anterior chest, entire anterior abdomen, and entire left arm, calculate total burn percentage:", "27% (Chest 9% + Abdomen 9% + Left Arm 9%)", "9%", "18%", "36%"),
                ("According to the Rule of Nines, calculate burn percentage for a casualty with burns on both entire legs (anterior and posterior):", "36% (18% for each entire lower limb)", "18%", "9%", "54%"),
                ("A casualty weighing 70 kg has lost 20% of their estimated blood volume (assuming 70 ml blood per kg body weight). Calculate blood volume lost:", "980 ml (approximately 1 liter)", "200 ml", "2,500 ml", "5,000 ml"),
                ("A medical team needs to administer IV fluids using the Parkland formula: \\(4\\,\\text{ml} \\times \\text{Weight (kg)} \\times \\%\\text{TBSA}\\). For a 60 kg patient with 30% burns, calculate total 24-hr fluid:", "7,200 ml (7.2 liters)", "3,600 ml", "1,800 ml", "14,400 ml"),
                ("In the Parkland formula, how much of the total calculated 24-hour fluid volume must be infused in the first 8 hours post-burn?", "50% (half of the total volume in first 8 hours)", "10% only", "100% in first 8 hours", "25% only"),
                ("A rescuer checks capillary refill time on a patient's nail bed. Normal perfusion returns color within how many seconds?", "within 2 seconds", "within 10 seconds", "within 30 seconds", "within 1 minute"),
                ("If normal adult resting breathing rate is 12 to 20 breaths per minute, a casualty breathing at 36 breaths per minute is classified as having:", "Tachypnea (abnormally rapid breathing indicating shock/distress)", "Bradypnea (slow breathing)", "Apnea (cessation of breathing)", "Eupnea (normal breathing)"),
                ("If normal adult systolic blood pressure is 100-120 mmHg, a trauma patient with systolic BP of 70 mmHg and heart rate of 130 bpm is in:", "Decompensated Hypovolemic Shock", "Hypertensive crisis", "Normal resting cardiovascular state", "Hyperthermic exhaustion"),
                ("Four stretcher bearers carry a 100 kg casualty plus a 10 kg stretcher evenly. What average load is borne by each bearer?", "27.5 kg per bearer (110 kg / 4)", "55 kg per bearer", "100 kg per bearer", "10 kg per bearer")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative emergency metric: {0}",
                "Solve the clinical first aid numerical: {0}",
                "Evaluate the physiological trauma calculation: {0}",
                "Determine the calculated emergency result: {0}",
                "Compute the medical fluid or percentage quantity: {0}",
                "Solve the standard trauma assessment problem: {0}",
                "Calculate the physical load distribution: {0}",
                "Determine the quantitative clinical value: {0}",
                "Compute the following physiological parameter: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Clinical Formula and Given Values**\\nIdentify the clinical formula (e.g. Rule of Nines: \\(\\text{{Limb}}=9\\%\\text{{ or }}18\\%\\), CPR: \\(30:2\\), or linear arithmetic).\\n**Step 2: Arithmetic Computation**\\nApply direct arithmetic calculation as indicated in the clinical protocol.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
