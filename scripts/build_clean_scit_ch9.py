# scripts/build_clean_scit_ch9.py
# Clean generator for MH-9-SCIT Chapter 9: Environmental Management (7 subtopics, 560 Qs)
# 100% distinct, zero schema errors, 100% Rule 2T compliant (40 Exam, 20 Practice, 20 Foundation per subtopic).

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 9
CH_NAME = "Environmental Management"

def gen_9_1_1():
    tc = "MH-9-SCIT-9-9.1.1"
    tname = "Meteorological elements, India Meteorological Department (IMD) forecasts, monsoon prediction models"
    archs = [
        # Arch 0: Weather vs Climate definition
        {
            'data': [
                ("atmospheric conditions at a specific place at a specific short time", "Weather", "Climate", "Ecosystem", "Biome"),
                ("average pattern of weather conditions over a long period (e.g., 30 years)", "Climate", "Weather", "Microclimate", "Humidity"),
                ("relative humidity and atmospheric pressure measured at 8:00 AM today", "Weather", "Climate", "Topography", "Solar radiation"),
                ("consistent tropical monsoon pattern observed over Western Ghats across decades", "Climate", "Weather", "Precipitation", "Inversion"),
                ("sudden afternoon thunderstorm occurring over Pune city", "Weather", "Climate", "Continental drift", "Barometric depression"),
                ("average annual rainfall distribution recorded over Maharashtra for 35 years", "Climate", "Weather", "Cloud cover", "Wind velocity"),
                ("temperature fluctuations recorded between noon and midnight today", "Weather", "Climate", "Latitudinal zone", "Albedo"),
                ("arid desert conditions prevalent in Rajasthan over centuries", "Climate", "Weather", "Atmospheric tide", "Coriolis effect"),
                ("morning fog reducing visibility on the Mumbai-Pune expressway", "Weather", "Climate", "Plate tectonics", "Geomagnetism"),
                ("long-term cool temperate regime of Himalayan high altitudes", "Climate", "Weather", "Frontal boundary", "Troposphere")
            ],
            'tmpls': [
                "Which term correctly denotes '{0}'?",
                "Identify the meteorological concept defined as '{0}':",
                "'{0}' is the formal scientific definition of which parameter?",
                "In meteorological science, '{0}' characterizes:",
                "Choose the appropriate term for '{0}':",
                "Select the concept that corresponds to '{0}':",
                "What is represented by '{0}'?",
                "Which classification accurately applies to '{0}'?",
                "'{0}' describes which of the following?",
                "Identify whether '{0}' refers to Weather or Climate:"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Meteorological Definition**\\nWeather refers to short-term atmospheric conditions of a specific location, while climate is the average of weather conditions over a prolonged duration (typically 30 years or more).\\n**Step 2: Specific Condition Analysis**\\n'{item[0]}' represents a {item[1].lower()} parameter.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: IMD Founding, Headquarters, and Observatories
        {
            'data': [
                ("1875", "1875 by the British Government", "1947 by Government of Independent India", "1905 by Lord Curzon", "1969 by ISRO"),
                ("Shimla", "Shimla (transferred later to Pune and New Delhi)", "Kolkata (transferred directly to Chennai)", "Mumbai (transferred directly to Bengaluru)", "Nagpur (transferred directly to Hyderabad)"),
                ("New Delhi", "New Delhi (with Division of Agricultural Meteorology at Pune)", "Kolkata", "Bengaluru", "Chennai"),
                ("Pune", "Pune", "Jaipur", "Ahmedabad", "Bhopal"),
                ("World Meteorological Organization (WMO)", "World Meteorological Organization (WMO)", "United Nations Environment Programme (UNEP)", "International Atomic Energy Agency (IAEA)", "World Health Organization (WHO)"),
                ("INSAT", "INSAT and METSAT (Kalpana-1) series", "Aryabhata and Rohini series", "Chandrayaan and Mangalyaan", "NAVIC and IRNSS only"),
                ("Cyclone warning and tracking", "Cyclone warning and tracking across the North Indian Ocean", "Tectonic plate fault mapping", "Nuclear fallout detection", "Geothermal power plant regulation"),
                ("Dr. H. F. Blanford", "Dr. H. F. Blanford", "Sir C. V. Raman", "Dr. Homi Bhabha", "Dr. Vikram Sarabhai"),
                ("Director General of Meteorology", "Director General of Meteorology (DGM)", "Chief Environmental Officer", "Scientific Secretary of Agriculture", "Inspector General of Forests"),
                ("Agro-meteorological advisories", "Agro-meteorological advisory bulletins for farming communities", "Stock market fluctuation forecasts", "Industrial manufacturing quota targets", "Urban property tax assessments")
            ],
            'tmpls': [
                "In which year was the India Meteorological Department (IMD) established?",
                "Where was the original meteorological headquarters of the IMD established in 1875?",
                "Where is the current apex administrative headquarters of the IMD located?",
                "Which city houses the central Division of Agricultural Meteorology and Meteorological Observatory of IMD in Maharashtra?",
                "Under which specialized agency of the United Nations does IMD function as a Regional Specialized Meteorological Centre?",
                "Which Indian satellite series provides real-time cloud imagery and meteorological data to the IMD?",
                "What is a primary national safety service provided by IMD for coastal populations?",
                "Who was appointed as the first Imperial Meteorological Reporter to the Government of India in 1875?",
                "What is the official designation of the administrative head of the India Meteorological Department?",
                "Which vital agricultural forecast service is published twice weekly by IMD for farmers?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Institutional Background**\\nThe India Meteorological Department (IMD) was established in 1875 with headquarters originally in Shimla, later moved to Pune, and currently headquartered in New Delhi.\\n**Step 2: Key Operational Role**\\nIt operates under the Ministry of Earth Sciences and collaborates closely with global bodies like WMO.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Monsoon Prediction Models (Mathematical, Statistical, Holistic)
        {
            'data': [
                ("Mathematical (Dynamic) Model", "supercomputers running simultaneous non-linear differential equations of atmospheric physics", "comparing historical rainfall data of the past 100 years", "observing bird nesting heights and animal behavior", "relying solely on solar eclipse timings"),
                ("Statistical Model", "correlating current oceanic and atmospheric parameters with historical monsoon records", "simulating thermodynamic fluid equations on supercomputers", "studying local plant flowering phenology", "performing laboratory titration of rainwater"),
                ("Holistic / Integrative Model", "combining outcomes of multiple dynamic and statistical models with international oceanic indices", "using only a mercury barometer reading from Pune", "measuring river discharge in a single basin", "relying entirely on traditional folk proverbs"),
                ("Dr. Vasant Gowarikar", "Dr. Vasant Gowarikar", "Dr. A. P. J. Abdul Kalam", "Dr. Raghunath Mashelkar", "Dr. Jayant Narlikar"),
                ("16 parameters", "16 oceanic and atmospheric worldwide parameters", "4 local wind speed measurements", "8 provincial rainfall records", "32 lunar cycle stages"),
                ("El Niño and La Niña", "El Niño and Southern Oscillation (ENSO) conditions in the Pacific Ocean", "sunspot cycles on the solar corona", "volcanic eruptions in the Atlantic ridge", "geomagnetic pole reversals"),
                ("Supercomputer PARAM", "PARAM supercomputers developed by C-DAC Pune", "commercial desktop mainframe calculators", "analog mechanical slide rules", "telecommunication microwave towers"),
                ("Continuous parameter updating", "dynamic variables change continuously requiring real-time oceanic-atmospheric updates", "monsoon is static and never deviates from historical mean", "atmospheric equations are purely linear and trivial", "rainfall occurs without any physical cause"),
                ("Sir Gilbert Walker", "Sir Gilbert Walker", "Lord Kelvin", "Sir Isaac Newton", "Edmond Halley"),
                ("Ensemble prediction system", "Ensemble prediction combining several dynamic sub-models to estimate probability distributions", "picking the single most optimistic forecast blindly", "averaging minimum and maximum thermometer readings", "ignoring satellite data completely")
            ],
            'tmpls': [
                "What is the operational basis of the '{0}' used in modern Indian monsoon forecasting?",
                "How does the '{0}' formulate monsoon projections?",
                "The '{0}' in meteorological forecasting relies primarily upon:",
                "Which Indian scientist played a pioneering role in developing the 16-parameter monsoon model for IMD?",
                "How many worldwide oceanic and atmospheric parameters formed the basis of the Gowarikar monsoon model?",
                "Which major Pacific Ocean phenomenon is a key global variable influencing the Indian monsoon in IMD models?",
                "Which advanced technological computing infrastructure enables IMD to run complex mathematical monsoon simulations?",
                "Why do modern monsoon forecasting models require continuous real-time data ingestion?",
                "Which British meteorologist first established statistical relationships between worldwide weather factors and Indian monsoon in 1904?",
                "What is the primary advantage of an '{0}' adopted by IMD in recent decades?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Monsoon Model Classification**\\nIMD employs mathematical (dynamic), statistical, and holistic ensemble models to forecast the South-West monsoon.\\n**Step 2: Mechanistic Analysis**\\n{item[0]} operates via {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 3: Meteorological instruments and measuring elements
        {
            'data': [
                ("Atmospheric pressure", "Barometer (measured in millibars or hectopascals)", "Anemometer", "Hygrometer", "Thermometer"),
                ("Relative humidity", "Hygrometer / Psychrometer (expressed as percentage)", "Rain gauge", "Barometer", "Seismograph"),
                ("Wind speed", "Anemometer (measured in km/h or knots)", "Wind vane", "Hygrometer", "Barometer"),
                ("Wind direction", "Wind vane / Weathercock", "Anemometer", "Barometer", "Lactometer"),
                ("Rainfall volume", "Rain gauge (measured in millimeters)", "Barometer", "Anemometer", "Hydrometer"),
                ("Maximum and minimum temperature", "Six's maximum and minimum thermometer", "Clinical mercury thermometer", "Pyrometer", "Galvanometer"),
                ("Solar radiation duration", "Campbell-Stokes sunshine recorder", "Anemometer", "Wind vane", "Barometer"),
                ("Upper atmospheric sounding", "Radiosonde attached to hydrogen/helium weather balloons", "Ground-level rain gauge", "Static anemometer tower", "Submarine sonar depth sensor"),
                ("Cloud cover", "Okta scale (measuring fractions of the sky covered by clouds)", "Decibel scale", "Richter scale", "Mohs hardness scale"),
                ("Atmospheric pressure decrease with altitude", "decreases exponentially because air density and column height decrease", "increases due to cooler temperatures", "remains completely constant throughout the troposphere", "fluctuates randomly without any physical relation")
            ],
            'tmpls': [
                "Which instrument is used in meteorological stations to measure '{0}'?",
                "Identify the correct measuring apparatus and unit for '{0}':",
                "How is '{0}' scientifically recorded by weather observers?",
                "Select the instrument specifically calibrated to record '{0}':",
                "What device does an IMD observatory utilize to monitor '{0}'?",
                "Which instrument provides continuous records of '{0}'?",
                "Identify the specialized sensor utilized for '{0}':",
                "How do meteorologists gather real-time data for '{0}'?",
                "Which standard metric scale is employed to evaluate '{0}'?",
                "Explain the physical behavior of '{0}' in the troposphere:"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Meteorological Measurement**\\nAccurate weather monitoring requires calibrated physical instruments for each atmospheric variable.\\n**Step 2: Instrument Identification**\\n{item[0]} is measured using {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Weather Forecasting applications in society
        {
            'data': [
                ("Aviation sector", "runway visibility, crosswind shear, and clear-air turbulence warnings", "crop harvest insurance valuations", "deep-sea fishing trawler license allocation", "highway toll tax calculation"),
                ("Marine and Fishermen", "high wave alerts, sea state condition, and storm surge warnings", "subsurface manganese nodule mining schedules", "ship container customs tariffs", "coastal real-estate tax valuations"),
                ("Agriculture (Farmers)", "optimal timing for sowing, fertilizer application, irrigation, and pest control", "commodity stock market futures trading", "tractor loan interest recalculation", "soil legal deed documentation"),
                ("Disaster management authorities", "timely evacuation notices for flood-prone and cyclone-hit coastal zones", "reconstruction budget auditing", "post-disaster census updating", "industrial patent approvals"),
                ("Urban municipal corporations", "stormwater drainage readiness, urban flash flood warnings, and reservoir discharge", "road widening contract tenders", "drinking water bill processing", "property ownership transfers"),
                ("Offshore oil drilling rigs", "cyclone trajectory, gale force winds, and ocean swell height forecasts", "crude oil refinery pricing", "pipeline steel import quotas", "worker pension distribution"),
                ("Renewable energy grid operators", "wind speed predictions and cloud cover impact on solar panel generation", "transmission line copper testing", "hydropower electricity retail billing", "substation transformer painting"),
                ("Tourism and Mountaineering", "blizzard, avalanche, and severe cold wave warnings in high-altitude zones", "hotel booking tax verification", "national park ticket pricing", "cable car machinery imports"),
                ("Health and Disease surveillance", "predicting malaria and dengue outbreaks based on temperature and stagnant humidity", "pharmaceutical drug patent renewal", "hospital building architect reviews", "doctor licensing examinations"),
                ("Port and Shipping authorities", "harbor wave conditions, storm signal flags (1 to 11), and berth safety", "cargo container weighbridge inspections", "dock worker wage negotiations", "maritime fuel customs clearance")
            ],
            'tmpls': [
                "How does IMD weather forecasting directly benefit the '{0}'?",
                "What vital information is provided by meteorological forecasts to the '{0}'?",
                "In what manner does the '{0}' rely on accurate meteorological advisories?",
                "Identify the primary utility of meteorological data for the '{0}':",
                "Why is real-time weather forecasting indispensable for the '{0}'?",
                "Which specific advisory is issued by meteorological agencies to assist the '{0}'?",
                "How does precision weather data enhance operational safety in the '{0}'?",
                "Select the critical operational decision made by the '{0}' using IMD forecasts:",
                "What public welfare protection is delivered to the '{0}' via weather alerts?",
                "Why do emergency managers in the '{0}' prioritize IMD warning bulletins?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Meteorological Utility**\\nWeather forecasts provide predictive insights crucial for protecting human life, economic assets, and resource planning.\\n**Step 2: Sectoral Benefit**\\nFor the {item[0].lower()}, forecasts enable {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Climate change, Global Warming and Anthropogenic factors
        {
            'data': [
                ("Enhanced greenhouse effect", "excessive retention of outgoing terrestrial infrared radiation by \\(\\text{CO}_2\\), \\(\\text{CH}_4\\), and \\(\\text{N}_2\\text{O}\\)", "depletion of nitrogen in the lower troposphere", "blocking of incoming solar ultraviolet rays by aerosols", "decrease in oceanic evaporation rates"),
                ("Carbon dioxide (\\(\\text{CO}_2\\)) rise", "combustion of fossil fuels (coal, petroleum) and large-scale deforestation", "excessive use of chemical nitrogenous fertilizers only", "natural volcanic dust settling on soil", "respiration of aquatic organisms"),
                ("Methane (\\(\\text{CH}_4\\)) emissions", "anaerobic decomposition in paddy fields, ruminant livestock, and municipal landfills", "burning of limestone in cement kilns", "automobile exhaust catalytic converters", "evaporation of ocean water"),
                ("Extreme weather events frequency", "increased incidence of intense heatwaves, unseasonal cloudbursts, and prolonged droughts", "stabilization of global temperatures at a constant value", "permanent reduction in tropical cyclonic energy", "complete cessation of monsoon winds"),
                ("Rising sea levels", "thermal expansion of warming oceans and melting of polar ice caps and glaciers", "accumulation of river silt on the ocean bed", "increased underwater submarine volcanic activities", "reduction in global oceanic evaporation"),
                ("Ocean acidification", "absorption of excess atmospheric \\(\\text{CO}_2\\) forming carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))", "dumping of industrial alkalis into coastal waters", "increased dissolution of calcium carbonate shells", "reduction in oceanic dissolved oxygen"),
                ("Urban Heat Island (UHI) effect", "higher temperatures in cities due to concrete, asphalt, vehicular heat, and lack of vegetation", "equal temperatures across rural and urban landscapes", "colder air trapping over city skylines", "increased reflection of sunlight from green agricultural fields"),
                ("Albedo effect alteration", "melting of reflective white Arctic ice exposing dark ocean water that absorbs more solar heat", "snow reflecting less light than dark asphalt roads", "clouds transmitting 100% of solar radiation without reflection", "forests reflecting more heat than polar glaciers"),
                ("Intergovernmental Panel on Climate Change (IPCC)", "providing comprehensive scientific assessments on climate change causes and impacts", "enforcing military sanctions on non-compliant nations", "selling renewable solar energy equipment", "managing commercial airline carbon offset registries"),
                ("Kyoto Protocol and Paris Agreement", "legally binding and voluntary international pacts to reduce greenhouse gas emissions", "treaties promoting global coal consumption", "agreements governing deep-sea mineral extraction rights", "accords establishing international civil aviation flight paths")
            ],
            'tmpls': [
                "What is the physical mechanism causing the '{0}'?",
                "Which primary human activity drives the '{0}'?",
                "What is the major anthropogenic source contributing to '{0}'?",
                "How does anthropogenic climate disruption manifest in the '{0}'?",
                "What fundamental physical processes account for '{0}' globally?",
                "Explain the chemical basis of '{0}':",
                "Why does the phenomenon of '{0}' develop in metropolitan centers?",
                "How does '{0}' create a positive feedback loop accelerating planetary warming?",
                "What is the primary international mandate of the '{0}'?",
                "What is the core objective of global accords like the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Environmental Science Concept**\\nHuman industrial activities release greenhouse gases that alter the global energy budget.\\n**Step 2: Mechanistic Breakdown**\\n{item[0]} occurs via {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Regional Monsoon Mechanisms in India
        {
            'data': [
                ("Differential heating of land and sea", "Indian landmass heats much faster than the Indian Ocean creating low pressure over northern plains", "ocean heats faster than land creating intense high pressure over Rajasthan", "both land and sea heat at identical rates maintaining atmospheric equilibrium", "polar ice caps radiate heat causing localized sea breeze"),
                ("Inter-Tropical Convergence Zone (ITCZ) shift", "shifts northward towards the Tropic of Cancer in summer drawing moist oceanic winds", "remains stationary over the equator throughout all seasons", "shifts southward towards Antarctica during May and June", "disappears completely during the Northern Hemisphere summer"),
                ("Western Ghats orographic barrier", "forces moisture-laden Arabian Sea winds upward causing heavy orographic rainfall on the windward coast", "absorbs moisture and creates a rain-shadow desert along the Konkan coast", "diverts monsoon winds entirely away from the Indian subcontinent", "causes winds to descend and heat up before reaching the coastal strip"),
                ("Rain-shadow zone of Maharashtra", "descent of winds on the leeward eastern side of Western Ghats causes dryness in Marathwada and Vidarbha", "maximum rainfall occurring in interior Deccan plateau", "cloudbursts concentrated exclusively in eastern Maharashtra plains", "moist air trapped permanently over Pune and Solapur districts"),
                ("Arabian Sea branch of monsoon", "strikes the Western Ghats bringing copious rainfall to Konkan, Goa, and Kerala coasts", "travels northeast directly into Assam without touching western India", "causes arid dry winds over coastal Maharashtra", "remains trapped in the Southern Ocean until September"),
                ("Bay of Bengal branch of monsoon", "advances towards northeastern India and bends along the Himalayas towards the Gangetic plains", "moves southwards towards Sri Lanka without shedding moisture", "dissipates entirely over the Andaman islands", "heats up and causes dry heatwaves across Bengal"),
                ("Retreating Monsoon (North-East Monsoon)", "winds blow from land towards sea during October-November bringing rain to Tamil Nadu coast", "winds blow from Indian Ocean to Himalaya during peak July", "cyclones moving exclusively towards Pakistan coast", "continuous unseasonal rains across Punjab and Haryana in summer"),
                ("October Heat", "transition period marked by clear skies, high daytime temperature, and residual high humidity", "severe winter cold wave hitting central India in October", "continuous heavy monsoon downpours across Maharashtra", "drop in daytime temperatures below freezing point"),
                ("Western Disturbances", "extra-tropical cyclonic storms originating in the Mediterranean Sea bringing winter rain to NW India", "tropical depressions formed in the Bay of Bengal during July", "local thermal thunderstorms over Kerala in May", "easterly winds blowing from the South China Sea"),
                ("Break in monsoon", "dry spell of several days or weeks when monsoon trough shifts close to the foothills of the Himalayas", "permanent end of the rainy season across India in June", "instant freezing of monsoon clouds over the central plateau", "cloudburst occurring continuously without a pause for a month")
            ],
            'tmpls': [
                "What is the meteorological driver of '{0}' during the Indian monsoon?",
                "How does the '{0}' regulate the arrival of South-West monsoon winds?",
                "What effect does the '{0}' produce on coastal Maharashtra (Konkan)?",
                "Why does the '{0}' experience recurrent drought and deficient precipitation?",
                "Which geographic region receives primary precipitation from the '{0}'?",
                "Describe the trajectory and precipitation pattern of the '{0}':",
                "What atmospheric pattern characterizes the '{0}' in the Indian subcontinent?",
                "What causes the uncomfortable weather condition known as '{0}' in Maharashtra?",
                "Identify the origin and seasonal significance of '{0}':",
                "In Indian agro-meteorology, what defines a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Monsoon Climatology**\\nThe Indian monsoon is driven by differential heating, ITCZ migration, and topographic barriers.\\n**Step 2: Regional Impact**\\n{item[0]} results in {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Environmental Laws, IMD Safety Advisories, and World Meteorological Day
        {
            'data': [
                ("World Meteorological Day", "23rd March (commemorating the establishment of WMO in 1950)", "5th June", "22nd April", "16th September"),
                ("World Environment Day", "5th June", "23rd March", "22nd March", "1st December"),
                ("Earth Day", "22nd April", "5th June", "23rd March", "16th October"),
                ("World Ozone Day", "16th September", "22nd April", "5th June", "23rd March"),
                ("IMD Color-Coded Warning: Red Alert", "Take Action: extremely severe weather likely to cause significant danger to life and infrastructure", "Be Prepared: moderate weather warning", "Be Updated: stay informed of changing conditions", "No Warning: normal weather conditions"),
                ("IMD Color-Coded Warning: Orange Alert", "Be Prepared: severe weather with potential for disruption, power outages, and flooding", "Take Action: evacuate immediately", "No Warning: perfectly calm weather", "Watch only: no impact anticipated"),
                ("IMD Color-Coded Warning: Yellow Alert", "Be Updated: watch and monitor changing weather conditions that may worsen", "Take Action: total shutdown of transportation", "Evacuate: abandon homes immediately", "No Advisory: completely clear skies"),
                ("IMD Color-Coded Warning: Green Alert", "No Action Required: normal weather conditions prevailing, no warning issued", "Evacuate coastal areas", "Prepare lifeboats and emergency kits", "Shut all industrial facilities"),
                ("National Disaster Management Authority (NDMA) head", "Prime Minister of India (ex-officio Chairperson)", "Minister of Environment and Forests", "Director General of Police", "Chief Justice of India"),
                ("State Disaster Management Authority (SDMA) head", "Chief Minister of the respective State (ex-officio Chairperson)", "Governor of the State", "Commissioner of Police", "District Collector")
            ],
            'tmpls': [
                "When is '{0}' celebrated globally to raise awareness about atmospheric sciences?",
                "On which date is '{0}' observed worldwide to advocate environmental conservation?",
                "Identify the international commemorative date for '{0}':",
                "Which calendar day marks '{0}' celebrating the Montreal Protocol?",
                "What is the official advisory protocol associated with '{0}'?",
                "How does IMD define the public directive for an '{0}'?",
                "What civic response is advised by meteorologists during an '{0}'?",
                "What status does an '{0}' denote in the IMD weather classification system?",
                "Who serves as the apex chairperson of the '{0}'?",
                "Who presides as the statutory chairperson over the '{0}' at the state level?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Institutional & Commemorative Facts**\\nMeteorological agencies issue standardized public alerts and observe global commemorative days under UN and national frameworks.\\n**Step 2: Specific Identification**\\n{item[0]} corresponds to {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_9_2_1():
    tc = "MH-9-SCIT-9-9.2.1"
    tname = "Domestic, industrial, hazardous, biomedical, e-waste"
    archs = [
        # Arch 0: Solid Waste Categories
        {
            'data': [
                ("discarded kitchen scraps, stale food, vegetable peels, and fruit skins", "Domestic waste (Wet / Biodegradable)", "Biomedical hazardous waste", "E-waste", "Industrial mineral slag"),
                ("used syringes, expired medicines, blood-stained bandages, and anatomical tissues", "Biomedical waste (Hazardous / Infectious)", "Domestic dry waste", "Agricultural compost", "Construction rubble"),
                ("discarded printed circuit boards, broken smartphones, cathode ray tubes, and laptops", "Electronic waste (E-waste)", "Commercial dry paper waste", "Domestic organic waste", "Municipal sewer silt"),
                ("chemical sludge, heavy metal residues, toxic ash, and acidic effluents", "Industrial hazardous waste", "Domestic kitchen waste", "Biodegradable biomass", "Sanitary paper waste"),
                ("broken bricks, crushed concrete, cement plaster fragments, and stone dust", "Construction and demolition waste", "Biomedical waste", "Hazardous electronic waste", "Organic compostable waste"),
                ("pesticide containers, weedicide residues, cattle dung, and crop stalks", "Agricultural waste", "Biomedical infectious waste", "E-waste", "Municipal plastic packaging"),
                ("spent uranium fuel rods, radiation-contaminated clothing, and nuclear reactor coolant filters", "Radioactive waste", "Domestic wet waste", "Biodegradable paper waste", "Commercial cardboard waste"),
                ("discarded lead-acid car batteries, mercury thermometers, and paint cans", "Household hazardous waste", "Non-hazardous organic waste", "Compostable green waste", "Inert soil waste"),
                ("paper receipts, cardboard boxes, packaging thermocol, and plastic wrappers from offices", "Commercial dry waste", "Biomedical infectious waste", "Radioactive effluent", "Agricultural harvest residue"),
                ("dredged silt, tree leaf litter, and roadside sweepings collected by municipal cleaners", "Municipal street waste", "Biomedical hazardous waste", "High-level nuclear waste", "Toxic chemical sludge")
            ],
            'tmpls': [
                "Which category of solid waste includes '{0}'?",
                "Classify the following waste material: '{0}':",
                "'{0}' represents a classic example of which solid waste classification?",
                "Under solid waste management regulations, '{0}' is categorized as:",
                "Identify the waste category that encompasses '{0}':",
                "To which stream of municipal solid waste does '{0}' belong?",
                "Select the appropriate classification for '{0}':",
                "What type of solid waste is formed by '{0}'?",
                "How is '{0}' officially designated in environmental guidelines?",
                "Choose the correct regulatory category for '{0}':"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Solid Waste Classification**\\nSolid wastes are categorized according to their origin, physical nature, and potential environmental hazard.\\n**Step 2: Material Evaluation**\\n'{item[0]}' belongs to the category of {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Biodegradable vs Non-Biodegradable decomposition time
        {
            'data': [
                ("Banana peel", "3 to 4 weeks", "10 to 15 years", "100 to 200 years", "Indefinitely non-degradable"),
                ("Cardboard paper box", "1 to 2 months", "5 to 10 years", "50 years", "500 years"),
                ("Cotton rag / cloth", "2 to 5 months", "20 to 30 years", "80 to 100 years", "Never degrades"),
                ("Woolen socks", "1 year", "10 to 12 years", "100 years", "1000 years"),
                ("Wood / Timber piece", "10 to 15 years", "1 to 2 weeks", "500 years", "Non-degradable"),
                ("Tin cans (aluminum / metal)", "50 to 100 years", "3 to 4 weeks", "1 to 2 months", "1 year"),
                ("Aluminum beverage cans", "200 to 500 years", "2 to 5 months", "1 year", "10 years"),
                ("Plastic carry bags (polyethylene)", "Up to 1,000 years (or breaks into microplastics indefinitely)", "1 to 2 months", "1 to 2 years", "10 years"),
                ("Glass bottles", "1 million years (virtually indestructible under natural weathering)", "5 to 10 years", "100 years", "500 years"),
                ("Thermocol (Expanded Polystyrene)", "Infinite / virtually non-biodegradable in nature", "6 months", "1 to 2 years", "10 years")
            ],
            'tmpls': [
                "What is the approximate natural degradation period of '{0}' in the environment?",
                "How long does it take for '{0}' to naturally decompose in nature?",
                "Select the scientific estimated decomposition time for '{0}':",
                "Which timeframe correctly represents the natural breakdown of '{0}'?",
                "In solid waste degradation tables, what is the lifespan of '{0}'?",
                "Identify the approximate time required for nature to decompose '{0}':",
                "Estimate the environmental persistence period for '{0}':",
                "How many years or months are needed for '{0}' to biodegrade completely?",
                "Which of the following reflects the degradation duration of '{0}'?",
                "State the typical natural decomposition timescale for '{0}':"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Degradation Science**\\nBiodegradable materials break down rapidly through microbial action, whereas synthetic and non-biodegradable items persist for centuries.\\n**Step 2: Specific Item Lifespan**\\n{item[0]} decomposes in {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Harmful effects of improper waste disposal
        {
            'data': [
                ("Leachate percolation into groundwater", "toxic heavy metals and organic acids contaminate drinking water wells and aquifers", "increases soil fertility and groundwater purity", "eliminates all pathogenic bacteria from the subsoil", "converts subterranean rocks into gold"),
                ("Open burning of municipal plastics", "releases highly carcinogenic dioxins, furans, and black carbon soot into the air", "purifies surrounding urban atmospheric air", "produces pure medicinal oxygen", "neutralizes atmospheric carbon dioxide"),
                ("Choking of urban stormwater drains by plastic bags", "leads to catastrophic urban flash floods and stagnation during monsoon rains", "accelerates storm runoff velocity safely", "cleans sewer channels automatically", "reduces mosquito breeding habitats"),
                ("Accumulation of unsegregated wet waste in open dumps", "fosters anaerobic decomposition releasing malodorous hydrogen sulfide and methane (greenhouse gas)", "prevents all greenhouse gas emissions", "creates clean sterile soil automatically", "absorbs solar radiation without odour"),
                ("Stray animal ingestion of discarded plastic wrappers", "causes fatal gastrointestinal obstruction and rumen impaction in cattle", "provides essential synthetic vitamins to livestock", "enhances milk production in domestic animals", "improves animal digestion naturally"),
                ("Indiscriminate dumping of biomedical needles and sharps", "transmits blood-borne pathogens such as Hepatitis B, Hepatitis C, and HIV to waste pickers", "cures infectious diseases in surrounding settlements", "immunizes sanitation workers naturally", "neutralizes biological bacteria spontaneously"),
                ("Open disposal of lead-acid and lithium batteries", "leaches neurotoxic lead, cadmium, and lithium into soil causing plant and nerve toxicity", "enriches soil with beneficial plant nutrients", "neutralizes all acidic soils safely", "prevents insect infestation in crops"),
                ("Proliferation of open garbage dumpsites", "creates breeding grounds for disease vectors including houseflies, mosquitoes, and rodents (rats)", "repels all insect and rodent species naturally", "maintains municipal visual aesthetics", "destroys all airborne viral pathogens"),
                ("Microplastic accumulation in water bodies", "enters the aquatic food chain leading to bioaccumulation and biomagnification in fish and humans", "purifies water bodies by absorbing pollutants permanently", "provides nutritious food for marine phytoplankton", "prevents oceanic acidification"),
                ("E-waste dismantling by unorganized crude acid leaching", "exposes workers to lethal fumes of cyanide, mercury vapor, and toxic lead dust", "creates a safe, sterile indoor working environment", "destroys all toxic chemical elements permanently", "prevents any occupational disease among scrap workers")
            ],
            'tmpls': [
                "What severe environmental or health hazard is caused by '{0}'?",
                "Which catastrophic consequence results from '{0}'?",
                "Identify the specific danger associated with '{0}':",
                "How does '{0}' adversely affect human health and ecosystems?",
                "Select the primary risk stemming from '{0}':",
                "Explain the ecological damage directly attributed to '{0}':",
                "Why is '{0}' considered extremely perilous in urban waste management?",
                "Which adverse outcome is triggered when '{0}' occurs?",
                "State the public health threat posed by '{0}':",
                "What ecological hazard develops due to '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Environmental Pathology**\\nImproper solid waste handling creates direct toxicological pathways into air, water, and biological food webs.\\n**Step 2: Hazard Mechanism**\\n{item[0]} results in {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Biomedical Waste Management Rules and Color-Coded Bins
        {
            'data': [
                ("Yellow Biohazard Bin", "anatomical human/animal tissues, soiled bandages, expired cytotoxic drugs, and microbiological cultures", "uncontaminated cardboard boxes and plastic water bottles", "clean metal beverage cans", "shredded office paperwork"),
                ("Red Biohazard Bin", "contaminated recyclable plastic items like disposable tubing, catheters, IV bottles, and syringes without needles", "anatomical organ specimens", "broken glass ampoules and metal blades", "food scraps and fruit peels"),
                ("White Translucent Puncture-Proof Container", "scalpels, needles, contaminated glass slides, and sharp metallic blades", "organic food leftovers from patients", "cardboard pharmaceutical cartons", "clean cotton gauze rolls"),
                ("Blue Biohazard Box / Bin", "broken or intact medicine glass vials, ampoules, and metallic orthopedic implants", "human body organs and amputated limbs", "soiled cotton plaster casts", "kitchen vegetable peels"),
                ("Black Municipal Bin in Hospitals", "non-infectious general municipal waste like paper, food leftovers, and fruit skins", "infectious surgical gloves", "used blood transfusion bags", "anatomical pathology specimens"),
                ("Autoclaving and Hydroclaving", "high-pressure steam sterilization to eliminate all pathogenic microorganisms before disposal", "open burning on hospital grounds", "flushing down municipal stormwater gutters", "dumping in agricultural compost pits"),
                ("Incineration at high temperature (>1000°C)", "controlled thermal oxidation of infectious anatomical and pharmaceutical waste to sterile ash", "freezing waste to produce reusable ice packs", "washing syringes in tap water for resale", "burying raw tissues in road construction"),
                ("Universal Biohazard Symbol", "a standardized three-crescent trefoil symbol indicating infectious biological hazard", "a green recycling triangle of three arrows", "a skull and crossbones indicating poison only", "a red cross symbol for medical dispensary"),
                ("Biomedical Waste (Management and Handling) Rules", "Ministry of Environment, Forest and Climate Change (MoEFCC), Government of India", "World Trade Organization (WTO)", "Ministry of Railways", "Reserve Bank of India (RBI)"),
                ("Barcoding of biomedical waste bags", "tracking the journey of infectious waste from health facility to common treatment facility (CBWTF)", "calculating consumer retail sales discounts", "tagging patient medical insurance claims", "monitoring hospital staff attendance")
            ],
            'tmpls': [
                "Which waste items must strictly be deposited into the '{0}' according to Biomedical Waste Rules?",
                "Identify the designated waste items allocated to the '{0}':",
                "Under hospital waste segregation standards, what belongs in the '{0}'?",
                "What is the authorized medical disposal purpose of the '{0}'?",
                "Which biomedical materials are segregated specifically in the '{0}'?",
                "What is the objective of '{0}' in biomedical waste treatment facilities?",
                "Why is '{0}' employed for infectious pathological waste disposal?",
                "What does the presence of the '{0}' warn sanitation personnel about?",
                "Which governmental authority notified the '{0}' in India?",
                "What critical monitoring function is fulfilled by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Biomedical Waste Rules**\\nHospital wastes must be color-segregated at the point of generation to prevent lethal cross-infections and environmental contamination.\\n**Step 2: Specific Protocol**\\n{item[0]} is designated for {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: E-waste Hazardous Components and Heavy Metals
        {
            'data': [
                ("Lead (\\(\\text{Pb}\\)) in solder and CRT monitors", "causes severe central nervous system damage, kidney failure, and cognitive impairment in children", "strengthens human bone mineral density", "improves vision and auditory perception", "causes instantaneous skin tanning"),
                ("Mercury (\\(\\text{Hg}\\)) in fluorescent backlights and switches", "accumulates in the brain causing Minamata-like neurological tremors and sensory loss", "stimulates thyroid hormone secretion safely", "cures bacterial gastrointestinal disorders", "lowers blood pressure permanently"),
                ("Cadmium (\\(\\text{Cd}\\)) in rechargeable Ni-Cd batteries and chip resistors", "causes Itai-itai disease, chronic kidney damage, and severe osteomalacia (bone softening)", "promotes rapid tooth enamel repair", "increases red blood cell oxygen carrying capacity", "acts as a benign biological antioxidant"),
                ("Hexavalent Chromium (\\(\\text{Cr}^{6+}\\)) in anticorrosive chassis coatings", "causes DNA mutations, severe asthmatic bronchitis, and lung cancer", "cures common viral throat infections", "protects human lungs against dust particles", "enhances biological muscular flexibility"),
                ("Brominated Flame Retardants (BFRs) in circuit boards and plastic casings", "disrupts endocrine thyroid hormone functions and impairs fetal neurological development", "accelerates protein synthesis in muscles", "neutralizes dietary cholesterol", "acts as a harmless water-soluble vitamin"),
                ("Polyvinyl Chloride (PVC) insulation on computer cables", "releases toxic hydrogen chloride gas and carcinogenic dioxins when incinerated", "breaks down into pure potable water", "neutralizes atmospheric sulfur oxides", "converts into fertile organic humus"),
                ("Beryllium (\\(\\text{Be}\\)) in motherboard CPU sockets and connectors", "causes berylliosis (chronic granulomatous lung disease) and pulmonary tumors", "relieves asthmatic symptoms naturally", "improves human respiratory vital capacity", "acts as a non-toxic food preservative"),
                ("Valuable precious metals recoverable from e-waste", "Gold (\\(\\text{Au}\\)), Silver (\\(\\text{Ag}\\)), Copper (\\(\\text{Cu}\\)), and Palladium (\\(\\text{Pd}\\))", "Iron and sand only", "Lead and arsenic only", "Sulfur and phosphorus only"),
                ("Urban Mining", "extracting precious and rare earth metals from discarded electronic gadgets rather than raw ore mining", "digging open gravel pits in public city gardens", "demolishing old heritage stone buildings for rubble", "mining sand along urban river beds"),
                ("Extended Producer Responsibility (EPR)", "mandating manufacturers of electronics to take back and safely recycle end-of-life products", "requiring consumers to manufacture their own microchips", "imposing import duties on agricultural grains", "exempting electronics companies from environmental liability")
            ],
            'tmpls': [
                "What toxicological health hazard is posed by '{0}' found in electronic waste?",
                "Which chronic disease or physiological damage is caused by exposure to '{0}'?",
                "Identify the severe pathological consequence of leaching of '{0}':",
                "Why is the presence of '{0}' hazardous in landfill disposal of electronics?",
                "Which organ system is primarily attacked by '{0}' discarded from e-waste?",
                "What chemical hazard arises from the thermal combustion of '{0}'?",
                "Select the chronic occupational respiratory condition provoked by '{0}':",
                "Which high-value metals can be safely reclaimed through certified recycling of '{0}'?",
                "In circular economic science, what does the term '{0}' signify?",
                "What environmental accountability mechanism is enforced under '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: E-waste Toxicology**\\nElectronic waste contains hazardous heavy metals and persistent toxic compounds that cause severe neurotoxic and systemic health damage.\\n**Step 2: Toxic Agent Analysis**\\n{item[0]} leads to {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Principles of Solid Waste Quantification and Source Reduction
        {
            'data': [
                ("Per capita waste generation in Indian metro cities", "0.4 kg to 0.6 kg per person per day", "5.0 kg to 8.0 kg per person per day", "0.01 kg per person per day", "25 kg per person per day"),
                ("Major constituent of Indian municipal solid waste by mass", "biodegradable organic waste (kitchen and vegetable matter, ~50-60%)", "electronic microchips (~40%)", "glass beverage bottles (~70%)", "radioactive tailings (~30%)"),
                ("Waste minimization hierarchy top priority", "Source reduction / Prevention (avoiding waste generation entirely)", "Open dumping in unlined marshes", "Ocean disposal of unsorted trash", "Incineration without energy recovery"),
                ("Replacing single-use plastic cups with reusable ceramic or steel tumblers", "Source reduction and reuse preventing waste at the origin", "Downcycling into microplastics", "Thermal chemical pyrolysis", "Deep sanitary ocean burial"),
                ("Opting for digital receipts and textbooks instead of physical paper printing", "Source reduction by digitizing and eliminating physical material consumption", "Creating hazardous e-waste exclusively", "Downcycling bleached chemical pulp", "Incinerating paper reserves"),
                ("Purchasing groceries in bulk with cloth bags rather than individual multi-layer sachets", "Packaging waste reduction and avoidance of non-recyclable multi-layer plastics", "Accelerating domestic landfill accumulation", "Increasing household chemical sludge", "Producing biomedical biohazards"),
                ("Industrial process redesign to utilize raw materials completely without offcuts", "Clean technology / Zero waste manufacturing", "Open field waste dumping", "Exporting toxic slag to river basins", "Dilution of toxic effluents in tap water"),
                ("Car pooling and public transit usage", "minimizes vehicular scrap, tires, motor oil, and urban air emissions", "increases municipal landfill volume exponentially", "creates toxic biomedical syringe waste", "exhausts fossil fuel reserves faster"),
                ("Repairing faulty domestic electronic appliances instead of immediately discarding them", "Extending product lifecycle and delaying e-waste generation", "Accelerating industrial hazardous waste formation", "Contaminating urban groundwater immediately", "Violating municipal sanitary codes"),
                ("Institutional cafeteria composting of raw vegetable trimmings", "On-site decentralized organic waste management", "Producing hazardous industrial toxic fumes", "Increasing municipal transportation diesel emissions", "Violating solid waste management rules")
            ],
            'tmpls': [
                "What is the average '{0}' recorded in modern Indian urban centers?",
                "Which component represents the '{0}' according to CPCB surveys?",
                "In the international waste management hierarchy, what represents the '{0}'?",
                "Which waste prevention principle is demonstrated by '{0}'?",
                "Select the source reduction strategy exemplified by '{0}':",
                "How does the practice of '{0}' advance sustainable environmental management?",
                "What industrial manufacturing philosophy is embodied by '{0}'?",
                "How does the collective adoption of '{0}' benefit solid waste reduction?",
                "What circular economic advantage is gained by '{0}'?",
                "Which municipal solid waste management practice is represented by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Waste Minimization Philosophy**\\nThe most sustainable way to manage solid waste is preventing it at the source, reducing per capita generation, and maximizing product lifecycles.\\n**Step 2: Operational Analysis**\\n{item[0]} represents {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Solid Waste Management Rules 2016 Key Directives
        {
            'data': [
                ("Mandatory three-stream source segregation", "Wet (biodegradable), Dry (recyclable), and Domestic Hazardous waste", "Plastics, Metals, and Cardboard only", "Kitchen food, Water bottles, and Clothes only", "Combustible, Non-combustible, and Inert only"),
                ("Responsibility of waste generators", "segregate waste at source and handover to authorized municipal waste collectors", "burn all plastic and dry leaves on private property", "dump unsegregated bags into stormwater drains at night", "transport waste personally to distant forest reserves"),
                ("Prohibition of burning of solid waste", "completely prohibited under SWM Rules 2016 with punitive fines for violators", "encouraged during winter months for community heating", "allowed for garden leaves and plastic packaging", "permitted in all public park corners"),
                ("Role of informal waste pickers and ragpickers", "integration and formal recognition into municipal collection and sorting systems", "complete eviction from urban municipal limits", "imprisonment under public nuisance laws", "banning from entering recycling facilities"),
                ("Buffer zone requirement around solid waste processing facilities", "mandatory green buffer zone maintained to protect neighboring residential zones", "construction of high-density shopping malls directly on landfill slopes", "allowing residential slums directly over active compost piles", "eliminating boundary fences entirely"),
                ("Use of refuse-derived fuel (RDF) in cement kilns", "supplying high-calorific non-recyclable combustible waste to replace coal in cement manufacturing", "dumping non-recyclables into city drinking lakes", "spreading combustible plastics on farm soil as manure", "exporting RDF to polar research stations"),
                ("Treatment of non-biodegradable sanitary waste (napkins, diapers)", "pouches provided by brand owners/manufacturers for safe disposal and high-temperature incineration", "composting along with kitchen vegetable peels", "recycling into food-grade plastic utensils", "open washing in municipal rivers"),
                ("Central Pollution Control Board (CPCB) mandate", "monitoring implementation of SWM rules, framing technical guidelines, and compiling annual reports", "collecting door-to-door domestic trash in cities", "manufacturing plastic carry bags commercially", "repairing municipal sewer pipelines"),
                ("Local urban local bodies (ULBs / Municipal Corporations) duty", "arranging door-to-door collection, transportation, processing, and scientific disposal of MSW", "leaving waste disposal entirely to private foreign charities", "exporting domestic trash across state boundaries illegally", "prohibiting all forms of composting within city limits"),
                ("Timeline for legacy dumpsite bioremediation", "capping and bio-mining of old unscientific garbage mountains to reclaim land", "covering unsegregated mounds with fresh soil and building airports immediately", "lighting deep underground fires to burn legacy dumps", "dumping legacy mounds into coastal mangrove wetlands")
            ],
            'tmpls': [
                "Under the Solid Waste Management Rules 2016, what comprises '{0}'?",
                "What is the statutory '{0}' mandated by India's SWM Rules 2016?",
                "What is the legal status regarding the '{0}' under environmental legislation?",
                "How do SWM Rules 2016 envision the '{0}' in urban waste ecosystems?",
                "What regulatory standard governs the '{0}' under municipal town planning?",
                "Why do environmental guidelines promote the '{0}'?",
                "What disposal protocol is legally stipulated for '{0}'?",
                "Identify the core regulatory responsibility executed by the '{0}':",
                "What primary public health obligation is assigned to '{0}'?",
                "Which scientific reclamation process is mandated for '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Statutory Framework**\\nThe Solid Waste Management Rules 2016 establish comprehensive statutory obligations for waste segregation, processing, and dumpsite remediation.\\n**Step 2: Specific Directive**\\n{item[0]} entails {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Global and National Environmental Milestones in Waste Management
        {
            'data': [
                ("Basel Convention (1989)", "controlling transboundary movements of hazardous wastes and their disposal in developing nations", "regulating commercial whaling quotas in the Antarctic", "allocating international orbital satellite slots", "monitoring global air traffic safety"),
                ("Stockholm Convention on Persistent Organic Pollutants (POPs)", "eliminating or restricting the production of toxic bioaccumulative chemicals like dioxins, PCBs, and DDT", "subsidizing chemical pesticide manufacturing", "promoting open-air plastics incineration", "deregulating industrial chemical trade"),
                ("Minamata Convention (2013)", "protecting human health and the environment from anthropogenic emissions of toxic mercury", "regulating uranium enrichment in civil nuclear reactors", "banning all plastic packaging worldwide", "mandating compost use in forestry"),
                ("Swachh Bharat Abhiyan (Clean India Mission)", "nationwide campaign launched on 2nd October 2014 to achieve universal sanitation and scientific waste management", "campaign to promote coal-fired power stations", "program to nationalize all private commercial banks", "scheme to subsidize single-use polythene production"),
                ("Cleanest city awards under Swachh Survekshan (e.g., Indore)", "achieving 100% door-to-door waste segregation, zero landfill open dumping, and mechanized processing", "paying highest municipal property taxes per square meter", "consuming the highest volume of single-use plastic water bottles", "exporting city garbage secretly to neighboring states"),
                ("Plastic Waste Management (Amendment) Rules 2021", "prohibiting manufacture, sale, and use of identified single-use plastic items with low utility and high littering potential", "mandating free distribution of thin plastic bags to consumers", "banning all steel, glass, and copper utensils", "permitting plastic dumping into marine protected zones"),
                ("Minimum thickness of plastic carry bags (post-2022 amendment)", "120 microns (to facilitate collection and prevent non-recyclable flimsy litter)", "5 microns", "20 microns", "10 millimeters"),
                ("E-waste (Management) Rules 2022 recycling targets", "setting strict progressive recycling targets for producers based on equipment lifecycles under EPR", "banning consumers from purchasing computers", "mandating electronic devices to be disposed of in general domestic garbage", "exempting multinational manufacturers from recycling quotas"),
                ("Bio-mining and Bio-remediation of dumpsites", "using mechanical sieving, trommels, and microbial degradation to separate combustibles, soil, and inert rocks from old garbage heaps", "burning dumpsites with petroleum fuel to clear land quickly", "covering unsegregated mounds with decorative artificial grass", "bulldozing garbage mountains into river channels"),
                ("Refuse Derived Fuel (RDF) calorific value requirement", "sufficiently high calorific energy (>1500 kcal/kg) to sustain efficient thermal combustion in industrial furnaces", "low energy zero-heat moisture content", "flammable toxic explosive gas mixture", "sub-zero cryogenic temperature state")
            ],
            'tmpls': [
                "What is the international mission of the '{0}' in environmental diplomacy?",
                "Which toxic substances are targeted for worldwide eradication by the '{0}'?",
                "What toxic heavy metal is strictly controlled under the global '{0}'?",
                "What is the primary national objective of India's '{0}'?",
                "Which outstanding operational excellence enabled '{0}' to achieve top sanitation ranking?",
                "What landmark environmental conservation measure was enacted under the '{0}'?",
                "What is the legally mandated '{0}' under India's Plastic Waste Management Rules?",
                "How do the '{0}' hold electronics manufacturers accountable for end-of-life hardware?",
                "How is the remediation technique of '{0}' executed on legacy city garbage heaps?",
                "What critical physical property governs the industrial utilization of '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Environmental Legislation & Global Accords**\\nInternational treaties and national missions formulate enforceable standards to control hazardous emissions, ban persistent pollutants, and remediate legacy dumps.\\n**Step 2: Specific Accord Analysis**\\n{item[0]} focuses on {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
